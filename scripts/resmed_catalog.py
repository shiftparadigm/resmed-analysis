#!/usr/bin/env python3
import asyncio, httpx, re, csv, socket, json
from parsel import Selector
import tldextract
import dns.resolver

SELECTORS = [
    "https://ap.resmed.com/home/country-selector",        # APAC hub
    "https://www.resmed.asia/en-bn/country_selector",     # Asia variant
    "https://www.resmed.tw/zh-tw/consumer/country_selector",
    "https://www.resmed.co.th/en-th/consumer/country_selector",
    "https://www.resmed.lat/healthcare-professional/country_selector",
    "https://www.resmed.la/country-selector",
    "https://me.resmed.com/",                             # Middle East site (links within)
]

# Common subdomains to enumerate
SUBDOMAINS = ["www", "shop", "support", "blog", "portal", "api", "mail", "webmail",
              "admin", "secure", "vpn", "remote", "careers", "investor", "newsroom",
              "dev", "stage", "staging", "test", "prod", "china", "ap", "me", "eu"]

# Common TLDs and multi-part TLDs to test
TLDS = ["com", "org", "net", "co.uk", "com.au", "com.cn", "co.jp", "co.kr",
        "co.th", "co.in", "co.id", "co.nz", "com.br", "com.tw", "com.hk", "com.sg",
        "com.my", "com.ph", "com.vn", "de", "fr", "es", "it", "nl", "be", "ch",
        "at", "dk", "se", "no", "fi", "pl", "cz", "pt", "ie", "gr", "ru", "ua",
        "ca", "mx", "ar", "cl", "pe", "lat", "la", "asia", "ae", "sa", "qa", "eg",
        "za", "jp", "kr", "tw", "hk", "sg", "my", "th", "id", "ph", "vn", "in"]

HEADERS = {"User-Agent":"Mozilla/5.0 (ResMedCatalogBot/1.0; +https://example.com/bot)"}
TIMEOUT = httpx.Timeout(20.0)
SEM = asyncio.Semaphore(20)

def is_resmed_url(u:str)->bool:
    return bool(re.match(r"^https?://[^/]*resmed\.[a-z\.]+(/|$)", u, re.I))

def should_exclude(u:str)->bool:
    """Exclude VPN, mail, admin, dev, stage/staging, API subdomains, and resmed.ca"""
    host = re.sub(r"^https?://", "", u).split("/")[0].lower()

    # Exclude all resmed.ca domains
    if "resmed.ca" in host:
        return True

    # Check for excluded prefixes
    excluded_prefixes = [
        "vpn.", "mail.", "webmail.",
        "admin.", "admin-",
        "api.", "api-", "apim.", "apigateway",
        "dev.", "dev-", "dev2-", "dev3-", "developer.",
        "stage.", "staging.", "staging-",
        "test.", "test-",
        "uat.", "uat-", "uat2-",
        "qa.", "qa-", "qa2-",
        "sbx.", "-sbx.", "sandbox.",
        "sit.", "-sit.",
        "poc.", "-poc.",
        "internal-",
    ]

    for prefix in excluded_prefixes:
        if host.startswith(prefix) or f"-{prefix.rstrip('.-')}" in host:
            return True

    # Check for excluded keywords anywhere in hostname (substring match)
    excluded_keywords = [
        "dev", "uat", "test", "staging", "stage", "admin", "sandbox", "sbx", "sit", "qa", "poc",
        "api", "backend", "analytics", "cognos", "portal"
    ]

    parts = host.split(".")
    for part in parts:
        # Check if any excluded keyword appears anywhere in this part
        for keyword in excluded_keywords:
            if keyword in part:
                return True

    return False

def should_exclude_result(status:int|None, title:str|None, hosting:str|None, ip:str|None)->bool:
    """Exclude based on response characteristics"""
    # Exclude 404s, 503s, 429s, 401s, and 403s
    if status in [404, 503, 429, 401, 403]:
        return True

    # Exclude login/signin pages
    if title:
        title_lower = title.lower()
        if any(word in title_lower for word in ["sign in", "signin", "login", "sign-in"]):
            return True

    # Exclude if we have NO useful data at all (no status, no title, no hosting)
    # Even if we have IP, that's not enough without other context
    if not status and not title and not hosting:
        return True

    return False

def norm_root(u:str)->str:
    m = re.match(r"^(https?://[^/]+)", u)
    return m.group(1).rstrip("/") if m else u

def guess_hosting(headers:dict, cname_chain:list[str], ip:str|None=None)->str|None:
    """Enhanced hosting/CDN provider detection"""
    h = {k.lower():v for k,v in headers.items()}
    server = h.get("server","").lower()
    via = h.get("via","").lower()
    powered_by = h.get("x-powered-by","").lower()
    cname = " ".join(cname_chain).lower()

    # Combine all signals
    hay = f"{server} {via} {cname} {powered_by}".lower()

    # CDNs (check first as they're most common)
    if "cloudflare" in hay or "cf-ray" in h: return "Cloudflare"
    if "akamai" in hay or "edgesuite.net" in hay or "akamaihd.net" in hay or "akamaiedge" in hay: return "Akamai"
    if "fastly" in hay or "fastly.net" in hay: return "Fastly"
    if "cloudfront" in hay or "cloudfront.net" in hay: return "Amazon CloudFront"

    # E-commerce platforms
    if "shopify" in hay or "myshopify.com" in hay: return "Shopify"
    if "bigcommerce" in hay or "mybigcommerce.com" in hay: return "BigCommerce"
    if "woocommerce" in powered_by: return "WooCommerce"

    # CMS/Marketing platforms
    if "hubspot" in hay or "hscoscdn" in hay or "hubspot.net" in hay: return "HubSpot"
    if "wordpress.com" in hay or "wp.com" in hay: return "WordPress.com"
    if "squarespace" in hay: return "Squarespace"
    if "wix" in hay: return "Wix"
    if "webflow" in hay: return "Webflow"
    if "ghost" in hay: return "Ghost"

    # Managed WordPress
    if "wpengine" in hay or "wpenginepowered" in hay: return "WP Engine"
    if "kinsta" in hay: return "Kinsta"
    if "pantheon" in hay or "pantheonsite.io" in hay: return "Pantheon"
    if "flywheel" in hay: return "Flywheel"

    # PaaS/Hosting
    if "vercel" in hay or "vercel-dns" in hay or "vercel.app" in hay: return "Vercel"
    if "netlify" in hay or "netlify.app" in hay or "netlify.com" in hay: return "Netlify"
    if "heroku" in hay or "herokuapp.com" in hay: return "Heroku"
    if "aws" in hay or "amazon" in hay or "elastic" in hay: return "AWS"
    if "azure" in hay or "azurewebsites" in hay or "windows" in hay: return "Microsoft Azure"
    if "google" in hay or "gcp" in hay or "appspot" in hay: return "Google Cloud"
    if "digitalocean" in hay: return "DigitalOcean"
    if "linode" in hay: return "Linode"
    if "vultr" in hay: return "Vultr"

    # Enterprise/Other
    if "equisolve" in hay: return "Q4 (Equisolve)"
    if "q4web" in hay: return "Q4 Web Systems"
    if "adobedc" in hay or "adobedtm" in hay or "omtrdc" in hay: return "Adobe Experience Cloud"
    if "optimizely" in hay or "episerver" in hay: return "Optimizely"
    if "sitecore" in hay: return "Sitecore"
    if "acquia" in hay: return "Acquia"

    # Web servers (only if no hosting platform detected)
    if "nginx" in server: return "Nginx (self-hosted)"
    if "apache" in server: return "Apache (self-hosted)"
    if "iis" in server or "microsoft" in server: return "IIS (self-hosted)"
    if "litespeed" in server: return "LiteSpeed (self-hosted)"

    return None

async def fetch(client:httpx.AsyncClient, url:str)->tuple[httpx.Response|None, str|None]:
    """Fetch URL and return (response, final_url_after_redirects)"""
    try:
        r = await client.get(url, headers=HEADERS, timeout=TIMEOUT, follow_redirects=True)
        final_url = str(r.url) if r else None
        return (r, final_url)
    except Exception:
        return (None, None)

async def resolve_cname_chain(host:str)->list[str]:
    chain=[]
    try:
        # follow up to 5 CNAMEs
        cur=host
        for _ in range(5):
            answers = dns.resolver.resolve(cur, 'CNAME')
            cname=str(answers[0].target).rstrip(".")
            chain.append(cname)
            cur=cname
    except Exception:
        pass
    return chain

async def ip_to_org(host:str)->str|None:
    try:
        ip = socket.gethostbyname(host)
        # quick-and-dirty ASN org hint via reverse name (works sometimes)
        return ip
    except Exception:
        return None

async def scrape_selectors()->set[str]:
    roots=set()
    async with httpx.AsyncClient(http2=True) as client:
        for u in SELECTORS:
            r, _ = await fetch(client,u)
            if not r: continue
            sel = Selector(r.text)
            links = [a.attrib.get("href","") for a in sel.css("a")]
            for L in links:
                if L and is_resmed_url(L):
                    roots.add(norm_root(L))
    return roots

async def expand_hreflang(roots:set[str])->set[tuple[str,str]]:
    out=set()
    async with httpx.AsyncClient(http2=True) as client:
        async def worker(root):
            async with SEM:
                r, _ = await fetch(client, root)
                if not r:
                    out.add((root,"n"))
                    return
                sel = Selector(r.text)
                alts = sel.xpath("//link[translate(@rel,'ABCDEFGHIJKLMNOPQRSTUVWXYZ','abcdefghijklmnopqrstuvwxyz')='alternate' and @hreflang]/@href").getall()
                found=False
                for a in alts:
                    if is_resmed_url(a):
                        out.add((norm_root(a),"y"))
                        found=True
                out.add((root,"n" if not found else "n")) # keep root too
        await asyncio.gather(*(worker(u) for u in roots))
    return out

async def query_crt_sh()->set[str]:
    """Query Certificate Transparency logs via crt.sh for resmed domains"""
    domains = set()
    print("Querying Certificate Transparency logs...")
    async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
        try:
            # Query for %.resmed.com and %.resmed.%
            r = await client.get("https://crt.sh/?q=%.resmed.com&output=json")
            if r.status_code == 200:
                data = r.json()
                for entry in data:
                    name = entry.get("name_value", "")
                    for line in name.split("\n"):
                        line = line.strip().lower()
                        if "resmed." in line and not line.startswith("*"):
                            # Extract domain, handle wildcards
                            domain = line.replace("*.", "")
                            if domain and not domain.startswith("."):
                                domains.add(f"https://{domain}")
            print(f"  Found {len(domains)} domains from crt.sh")
        except Exception as e:
            print(f"  Certificate Transparency query failed: {e}")
    return domains

async def enumerate_tlds()->set[str]:
    """Try common TLD variations of resmed"""
    domains = set()
    print("Enumerating TLD variations...")
    for tld in TLDS:
        domains.add(f"https://resmed.{tld}")
        domains.add(f"https://www.resmed.{tld}")
    print(f"  Generated {len(domains)} TLD variations")
    return domains

async def enumerate_subdomains(base_domains:set[str])->set[str]:
    """Try common subdomains on known domains"""
    domains = set()
    print("Enumerating subdomains...")
    # Extract unique base domains (without subdomain)
    bases = set()
    for url in base_domains:
        host = re.sub(r"^https?://", "", url).split("/")[0]
        extracted = tldextract.extract(host)
        if extracted.domain == "resmed":
            base = f"{extracted.domain}.{extracted.suffix}"
            bases.add(base)

    # Try each subdomain on each base
    for base in bases:
        for sub in SUBDOMAINS:
            domains.add(f"https://{sub}.{base}")

    print(f"  Generated {len(domains)} subdomain combinations")
    return domains

async def check_domain_exists(client:httpx.AsyncClient, url:str)->str|None:
    """Quick check if domain responds (HEAD request)"""
    try:
        host = re.sub(r"^https?://", "", url).split("/")[0]
        # Try DNS lookup first (faster than HTTP)
        socket.gethostbyname(host)
        return url
    except Exception:
        return None

async def filter_live_domains(domains:set[str])->set[str]:
    """Filter to only domains that resolve in DNS"""
    live = set()
    print(f"Checking {len(domains)} domains for DNS resolution...")

    async with httpx.AsyncClient(http2=True) as client:
        async def worker(url):
            async with SEM:
                result = await check_domain_exists(client, url)
                if result:
                    live.add(result)

        await asyncio.gather(*(worker(u) for u in domains))

    print(f"  {len(live)} domains resolve in DNS")
    return live

async def catalog():
    all_domains = set()

    # 1. Original scraping method
    print("\n=== Phase 1: Scraping country selectors ===")
    seed = await scrape_selectors()
    print(f"Found {len(seed)} domains from selectors")
    all_domains.update(seed)

    # 2. Expand via hreflang
    print("\n=== Phase 2: Expanding via hreflang tags ===")
    expanded = await expand_hreflang(seed)
    hreflang_domains = {u for (u,_) in expanded}
    print(f"Found {len(hreflang_domains)} domains via hreflang")
    all_domains.update(hreflang_domains)

    # 3. Certificate Transparency
    print("\n=== Phase 3: Certificate Transparency ===")
    crt_domains = await query_crt_sh()
    all_domains.update(crt_domains)

    # 4. TLD enumeration
    print("\n=== Phase 4: TLD enumeration ===")
    tld_domains = await enumerate_tlds()
    tld_live = await filter_live_domains(tld_domains)
    all_domains.update(tld_live)

    # 5. Subdomain enumeration on discovered domains
    print("\n=== Phase 5: Subdomain enumeration ===")
    subdomain_candidates = await enumerate_subdomains(all_domains)
    subdomain_live = await filter_live_domains(subdomain_candidates)
    all_domains.update(subdomain_live)

    # Deduplicate and filter out excluded domains
    hosts = sorted([d for d in set(all_domains) if not should_exclude(d)])
    print(f"\n=== Total unique domains discovered: {len(hosts)} (after filtering) ===")

    # Catalog all discovered domains
    print("\n=== Phase 6: Cataloging all domains ===")
    all_rows=[]
    async with httpx.AsyncClient(http2=True) as client:
        async def worker(u):
            async with SEM:
                r, final_url = await fetch(client,u)
                status = r.status_code if r else None
                title = None
                headers = {}
                if r:
                    headers = dict(r.headers)
                    content_type = headers.get("content-type", "").lower()
                    # Only try to parse HTML for title
                    if "text/html" in content_type:
                        try:
                            sel = Selector(r.text)
                            t = sel.xpath("//title/text()").get()
                            title = t.strip() if t else None
                        except Exception:
                            pass
                host = re.sub(r"^https?://","",u).split("/")[0]
                cname_chain = await resolve_cname_chain(host)
                ip = await ip_to_org(host)
                hosting = guess_hosting(headers, cname_chain, ip)
                # Include final_url for deduplication
                all_rows.append([host,u,status,title,hosting,ip,";".join(cname_chain),final_url])
        await asyncio.gather(*(worker(u) for u in hosts))

    # Filter results based on response characteristics
    # row format: [host, url, status, title, hosting, ip, cname_chain, final_url]
    rows = [row for row in all_rows if not should_exclude_result(row[2], row[3], row[4], row[5])]
    print(f"Filtered to {len(rows)} production/public sites (removed admin/dev/test/api/login/404/503/empty)")

    # Deduplicate based on final redirect destination
    # If multiple URLs redirect to the same final root domain, keep only the final one
    seen_final_roots = {}
    deduped_rows = []
    for row in rows:
        final_url = row[7]  # final_url column
        if final_url:
            final_root = norm_root(final_url)
            # If this URL is different from its final destination, it's a redirect
            original_root = norm_root(row[1])  # row[1] is the original URL
            if original_root != final_root:
                # This URL redirects elsewhere
                # Check if we've already seen the final destination
                if final_root not in seen_final_roots:
                    # Use the final destination, not the redirect
                    final_host = re.sub(r"^https?://","",final_root).split("/")[0]
                    row[0] = final_host  # Update host
                    row[1] = final_root  # Update URL to final destination
                    seen_final_roots[final_root] = row
                    deduped_rows.append(row)
                # else: skip this redirect since we already have the destination
            else:
                # No redirect, or redirects to itself
                if final_root not in seen_final_roots:
                    seen_final_roots[final_root] = row
                    deduped_rows.append(row)
        else:
            # No final URL tracked, keep it if we haven't seen this root
            original_root = norm_root(row[1])
            if original_root not in seen_final_roots:
                seen_final_roots[original_root] = row
                deduped_rows.append(row)

    print(f"Deduplicated to {len(deduped_rows)} unique sites (removed redirect duplicates)")

    # Remove the final_url column before writing to CSV
    output_rows = [[r[0], r[1], r[2], r[3], r[4], r[5], r[6]] for r in deduped_rows]

    with open("resmed_sites.csv","w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["host","url","status","title","hosting_provider","ip","cname_chain"])
        w.writerows(output_rows)
    print(f"\n✓ Wrote {len(output_rows)} rows to resmed_sites.csv")

if __name__ == "__main__":
    asyncio.run(catalog())
