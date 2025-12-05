# ResMed Multi-Site CMS Discovery Phase

## Executive Summary
Discovery phase to assess feasibility and scope of consolidating 117+ ResMed websites from disparate platforms (primarily WordPress and HubSpot) into a centralized CMS. This discovery will produce a migration plan, effort estimates, and CMS recommendations.

### Current State
- **Sites Cataloged**: 33+ production sites across multiple platforms
- **Primary Platforms**: WordPress (majority), HubSpot (ap.resmed.com + others)
- **Additional Platforms**: Shopify (e-commerce), Nginx/Apache (custom)
- **Geographic Spread**: Global sites across APAC, EMEA, LATAM, NA

### Discovery Objectives
1. Understand migration difficulty (HTML consistency analysis)
2. Estimate total effort and timeline
3. Recommend target CMS platform
4. Identify risks and mitigation strategies
5. Produce actionable migration plan

---

## Known Migration Challenges (From Industry Experience)

### 1. Content Extraction (HIGH RISK)
**Challenge**: WordPress and HubSpot allow "wild west" HTML practices

#### WordPress-Specific Issues
- **Inconsistent HTML structure** across pages
- **Inline styling** in content (not components)
- **Custom shortcodes** that need translation
- **Plugin-generated content** embedded in posts
- **Multiple theme variations** across sites
- **Mixed editor formats** (Classic, Gutenberg blocks, page builders)

#### HubSpot-Specific Issues
- **CMS modules** with custom HTML
- **HubL templating** mixed with content
- **Marketing automation** markup in content
- **Form embeds** and CTAs as inline code
- **Dynamic content** personalization tokens

**Discovery Questions**:
- How consistent is the HTML across WordPress sites?
- What custom plugins/shortcodes are in use?
- How much inline styling exists?
- What content extraction methods are available?
- What's the effort per page to clean/migrate?

**Discovery Activities** (see detailed tasks below)

---

### 2. Asset Migration (MEDIUM RISK)
**Challenge**: Scattered media across multiple DAMs, CDNs, and local uploads

**Discovery Questions**:
- How many assets per site? (total volume estimate)
- Where are assets stored? (WordPress media library, HubSpot file manager, CDNs)
- What's the total storage requirement? (GB)
- Are there broken asset links currently?
- What asset formats/types are in use?

**Discovery Activities** (see detailed tasks below)

---

### 3. Link Changing (MEDIUM RISK)
**Challenge**: Cross-site navigation, internal links, legacy URL structures

**Discovery Questions**:
- What are the URL patterns for each site?
- How many pages per site?
- How many internal vs cross-domain links?
- Are there dynamic URLs (query params, etc.)?
- What's the link structure complexity?

**Discovery Activities** (see detailed tasks below)

---

### 4. Content Cleaning (HIGHEST RISK - "Largest Tent Stake")
**Challenge**: Converting platform-specific HTML to new CMS components

#### The Core Problem
Art's Warning: "if they are a trad CMS using components and not allowing for inline styling then it will be a lot easier than them allowing the wild west"

**Reality**: WordPress and HubSpot = Wild West

#### Expected Issues
```html
<!-- WordPress Example: Inline Styles -->
<div style="background:#f4f4f4;padding:20px;margin-bottom:30px;">
  <h2 style="color:#003366;font-size:28px;">Product Title</h2>
  <p><span style="font-weight:bold;color:#ff0000;">Special Offer!</span></p>
</div>

<!-- HubSpot Example: Custom Modules -->
<div class="hs-module" data-module-id="12345">
  {% if content.featured %}
    <div class="featured-banner">...</div>
  {% endif %}
</div>

<!-- MUST BECOME -->
<ProductCard featured="true">
  <Title>Product Title</Title>
  <Badge>Special Offer!</Badge>
</ProductCard>
```

**Discovery Questions (CRITICAL)**:
- How consistent is the HTML across each site?
- What's the inline styling percentage?
- How many unique content patterns exist?
- What's the automation potential (% of pages)?
- What's the estimated effort per page?
- How many pages total across all 117 sites?

**Discovery Activities** (see detailed tasks below)

**Preliminary Effort Model** (to validate in discovery):
```
Assumptions (to be tested):
- 117 sites × 50 pages avg = 5,850 pages
- 30-50% of pages need manual cleanup
- Complex pages: 2-4 hours each
- Simple pages: 15-30 minutes each

Rough Estimate:
- Best case (clean HTML): 1-2 FTE years
- Worst case (wild west): 8-10 FTE years
- Likely case: 2.5-4 FTE years

DISCOVERY WILL DETERMINE ACTUAL EFFORT
```

---

## Discovery Phase Tasks (4-6 Weeks)

### Week 1-2: Platform & Content Audit

#### Task 1.1: Platform Identification
**Objective**: Determine exact CMS/platform for each of 117 sites

**Activities**:
- Analyze hosting providers from catalog (WordPress signatures)
- Use WhatCMS/BuiltWith on sample sites
- Check for HubSpot domains (hubspot.net CDN)
- Identify custom/proprietary systems
- Document CMS version where possible

**Deliverable**: Platform inventory spreadsheet
```
Site | URL | Platform | Version | Hosting | Notes
-----|-----|----------|---------|---------|------
www.resmed.com.au | https://... | WordPress | 6.x | Cloudflare | Gutenberg editor
ap.resmed.com | https://... | HubSpot | - | HubSpot | Marketing Hub
```

#### Task 1.2: Access & Credentials Audit
**Objective**: Identify what access we have/need

**Activities**:
- Document WordPress admin access
- Document HubSpot portal access
- Identify API keys/credentials needed
- Note any locked-down or unknown access
- List stakeholders per site/region

**Deliverable**: Access matrix + gaps

#### Task 1.3: HTML Consistency Analysis (CRITICAL - Art's Recommendation)
**Objective**: Score HTML quality/consistency per site to estimate migration difficulty

**Activities**:
1. **Automated Sampling**:
   - Scrape 30-50 pages per site (random sample)
   - Extract HTML structure (strip content)
   - Save samples for analysis

2. **AI-Powered Analysis**:
   ```
   For each site, feed samples to AI with prompt:

   "Analyze these HTML samples. Score 1-10 for consistency:
   - Inline styles vs CSS classes (weight: 30%)
   - Component/pattern reuse (weight: 25%)
   - Semantic HTML quality (weight: 20%)
   - Custom shortcodes/embeds (weight: 15%)
   - Complexity/nesting depth (weight: 10%)

   Return: Score, top 5 patterns, top 5 anti-patterns,
   estimated automation potential (%), red flags"
   ```

3. **Manual Validation**:
   - Review AI scoring for 10 sites manually
   - Adjust scoring rubric if needed
   - Validate automation potential estimates

**Deliverable**: HTML Consistency Report
```
Site | Score | Automation % | Effort/Page | Total Pages | Total Hours | Priority
-----|-------|--------------|-------------|-------------|-------------|----------
www.resmed.sg | 8.5 | 85% | 0.5h | 45 | 22h | High (easy win)
ap.resmed.com | 3.2 | 40% | 3h | 120 | 360h | Low (complex)
```

### Week 3: Content & Asset Inventory

#### Task 3.1: Page Count & Content Types
**Objective**: Understand total content volume

**Activities**:
- Crawl each site's sitemap.xml
- Count pages per site
- Categorize content types (product pages, blog posts, landing pages, etc.)
- Identify page templates in use
- Note dynamic vs static content

**Deliverable**: Content inventory
```
Site | Total Pages | Product Pages | Blog Posts | Landing Pages | Other
-----|-------------|---------------|------------|---------------|-------
```

#### Task 3.2: Asset Inventory
**Objective**: Understand asset volume and storage

**Activities**:
- Count images/videos per site (WordPress media library API)
- Document file sizes and total storage (GB)
- Identify asset types (images, PDFs, videos, downloads)
- Check for broken asset links (404s)
- Note CDN usage patterns

**Deliverable**: Asset report
```
Site | Total Assets | Images | Videos | PDFs | Total GB | Broken Links
-----|--------------|--------|--------|------|----------|-------------
```

#### Task 3.3: Plugin & Custom Code Audit
**Objective**: Identify WordPress plugins and custom functionality

**Activities**:
- List active plugins per WordPress site (via WP-CLI or API)
- Identify critical plugins (forms, e-commerce, SEO, etc.)
- Document custom themes/plugins
- Note HubSpot modules and custom templates
- Identify functionality that must be rebuilt

**Deliverable**: Plugin inventory + rebuild requirements

### Week 4: Link Analysis & SEO Audit

#### Task 4.1: URL Structure Analysis
**Objective**: Map URL patterns for redirect planning

**Activities**:
- Document URL patterns per site
- Identify dynamic URLs (query params, etc.)
- Count internal vs external links per site
- Map cross-domain link patterns (between ResMed sites)
- Note non-standard URLs

**Deliverable**: URL pattern documentation

#### Task 4.2: SEO & Analytics Baseline
**Objective**: Understand current SEO performance (risk of degradation)

**Activities**:
- Pull Google Analytics data (top pages, traffic)
- Pull Google Search Console data (top keywords, rankings)
- Document current SEO patterns (meta tags, structured data)
- Identify high-value pages (can't afford downtime/ranking loss)
- Note tracking codes (GA, GTM, marketing pixels)

**Deliverable**: SEO baseline report

### Week 5-6: CMS Evaluation & Effort Estimation

#### Task 5.1: CMS Requirements Definition
**Objective**: Define requirements for new centralized CMS

**Activities**:
- Workshop with stakeholders (content teams, marketing, IT)
- Document must-have features
- Document nice-to-have features
- Define content workflows
- Define localization/multi-site requirements
- Define integrations needed (CRM, marketing automation, etc.)

**Deliverable**: CMS Requirements Document

#### Task 5.2: CMS Platform Evaluation
**Objective**: Recommend 2-3 CMS options

**Activities**:
- Evaluate headless CMS options (Contentful, Sanity, Strapi)
- Evaluate traditional CMS (Adobe AEM, Sitecore, Drupal)
- Evaluate modern platforms (Webflow, Builder.io)
- Score against requirements
- Estimate licensing costs
- Assess migration tooling availability

**Deliverable**: CMS Evaluation Matrix + Recommendation

#### Task 5.3: Migration Effort Estimation
**Objective**: Provide realistic timeline and resource estimates

**Activities**:
- Use HTML consistency scores to estimate effort per site
- Calculate total hours (content + assets + links + QA)
- Define team structure (developers, content specialists, QA, PM)
- Propose phased approach (pilots → batches)
- Estimate timeline (optimistic, realistic, pessimistic)
- Calculate total cost (labor + licensing + hosting)

**Deliverable**: Migration Effort Estimate
```
Site Category | # Sites | Avg Hours/Site | Total Hours | Cost
--------------|---------|----------------|-------------|------
Easy (score 7-10) | 30 | 40h | 1,200h | $XX
Medium (score 4-6) | 60 | 120h | 7,200h | $XX
Hard (score 1-3) | 27 | 300h | 8,100h | $XX
TOTAL | 117 | - | 16,500h | $XX
```

#### Task 5.4: Pilot Site Selection
**Objective**: Identify 3-6 sites for pilot migration

**Activities**:
- Select sites across difficulty spectrum (easy, medium, hard)
- Ensure geographic diversity
- Get stakeholder buy-in
- Define pilot success criteria

**Deliverable**: Pilot site list + success criteria

### Week 6: Final Deliverables & Presentation

#### Task 6.1: Migration Plan Document
**Objective**: Comprehensive plan for full migration

**Contents**:
- Executive summary
- HTML consistency findings (the key insight!)
- Effort estimates by phase
- CMS recommendation + rationale
- Risk register
- Phased migration approach
- Resource requirements
- Timeline (Gantt chart)
- Budget
- Success metrics

#### Task 6.2: Stakeholder Presentation
**Objective**: Present findings and get approval to proceed

**Contents**:
- Discovery findings (HTML consistency = critical insight)
- Effort/cost estimates (best/realistic/worst case)
- CMS recommendation
- Migration strategy
- Risks and mitigations
- Decision points (go/no-go, budget approval)

#### Task 6.3: Pilot Migration Proposal
**Objective**: Detailed plan for pilot phase (if approved)

**Contents**:
- Pilot site details
- Pilot timeline (8-12 weeks)
- Pilot team structure
- Pilot deliverables
- Success criteria
- Lessons to validate during pilot

---

## Discovery Phase Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Cannot access WordPress/HubSpot admin for some sites | MEDIUM | HIGH | Identify access gaps early; work with regional teams |
| HTML analysis reveals "wild west" worst case | HIGH | CRITICAL | Be honest in findings; provide best/worst case estimates |
| Stakeholders disagree on CMS requirements | MEDIUM | MEDIUM | Facilitate early workshops; document trade-offs |
| Discovery takes longer than 6 weeks | MEDIUM | LOW | Focus on critical insights (HTML consistency); defer nice-to-haves |
| Cannot get analytics access (SEO baseline) | LOW | MEDIUM | Work with marketing teams early; use alternative data sources |
| 117 sites is undercount (more sites exist) | MEDIUM | MEDIUM | Continue discovery phase site enumeration in parallel |

---

## Discovery Phase Success Criteria

At the end of 4-6 weeks, we should be able to answer:

### Critical Questions
- [ ] How difficult is this migration? (HTML consistency scores per site)
- [ ] How much will it cost? (effort estimate: best/realistic/worst case)
- [ ] How long will it take? (timeline: optimistic/realistic/pessimistic)
- [ ] What CMS should we use? (recommendation with rationale)
- [ ] Should we proceed? (go/no-go recommendation)

### Data Gathered
- [ ] Platform identification for all 117 sites
- [ ] HTML consistency score for all sites
- [ ] Page count and content types per site
- [ ] Asset count and storage requirements
- [ ] Plugin/custom functionality inventory
- [ ] URL structure documentation
- [ ] SEO baseline metrics

### Deliverables
- [ ] Migration Plan Document (comprehensive)
- [ ] CMS Recommendation (2-3 options evaluated)
- [ ] Effort Estimate (hours, cost, timeline)
- [ ] Risk Register (with mitigations)
- [ ] Pilot Proposal (if proceeding)
- [ ] Stakeholder Presentation (exec summary)

---

## Key Insights from Art's Experience

**These inform our discovery approach:**

1. **"Content extraction will eat up hours if not confident"**
   → Discovery must validate extraction methods (WordPress API, HubSpot API)
   → Test on 3-5 sites during discovery

2. **"Cleaner HTML = easier migration"**
   → **HTML consistency analysis is THE critical discovery activity**
   → This determines feasibility and cost more than anything else

3. **"Cleaning content from old components to new = largest tent stake"**
   → Budget 60-70% of effort here in final estimates
   → Discovery must sample enough pages to validate this

4. **"WordPress + HubSpot = extremely painful"**
   → Set realistic expectations in final presentation
   → These platforms allow "wild west" - can't sugar-coat the effort

5. **"Use AI to check HTML consistency"**
   → **This is Art's #1 recommendation - make it central to discovery**
   → AI can analyze 50 pages per site in minutes vs days manually

---

## Discovery Phase Team

### Roles & Responsibilities

**Technical Lead** (0.5 FTE)
- Platform identification
- HTML consistency analysis setup
- Content/asset crawling scripts
- Extraction testing

**CMS Architect** (0.25 FTE)
- CMS requirements workshops
- CMS evaluation
- Technical recommendations

**Content Strategist** (0.25 FTE)
- Content inventory analysis
- Manual HTML validation
- Content pattern documentation

**Project Manager** (0.5 FTE)
- Discovery coordination
- Stakeholder engagement
- Deliverable assembly
- Final presentation

**Total: ~1.5 FTE for 4-6 weeks**

---

## Discovery Phase Outputs

### Output 1: HTML Consistency Report (CRITICAL)
```
Site | Platform | Score | Inline Style % | Automation % | Effort/Page | Total Pages | Total Hours
-----|----------|-------|----------------|--------------|-------------|-------------|-------------
www.resmed.sg | WordPress | 8.5 | 15% | 85% | 0.5h | 45 | 22h
ap.resmed.com | HubSpot | 3.2 | 70% | 40% | 3h | 120 | 360h
[117 rows total]

Summary:
- Easy migrations (score 7-10): 30 sites, 1,200 hours
- Medium migrations (score 4-6): 60 sites, 7,200 hours
- Hard migrations (score 1-3): 27 sites, 8,100 hours
TOTAL: 16,500 hours = $XXX cost
```

### Output 2: Migration Plan Document
**Contents**:
1. Executive Summary (2 pages)
2. Current State Analysis (5 pages)
3. HTML Consistency Findings (10 pages - THE KEY SECTION)
4. CMS Recommendation (5 pages)
5. Migration Approach (10 pages)
6. Effort Estimate & Timeline (5 pages)
7. Risk Register (3 pages)
8. Pilot Proposal (5 pages)
9. Budget & Resources (3 pages)
10. Appendices (platform inventory, access matrix, etc.)

**~50 page document**

### Output 3: Stakeholder Presentation (30 min)
**Slides**:
1. Discovery objectives & approach
2. Current state (117 sites, platforms, geography)
3. **HTML consistency findings** (THE CRITICAL SLIDE)
4. Effort estimate (best/realistic/worst case)
5. CMS recommendation
6. Migration strategy (phased approach)
7. Timeline & milestones
8. Budget
9. Risks & mitigations
10. Pilot proposal
11. Go/no-go decision

**~15-20 slides**

---

## Questions Discovery Phase Will Answer

### Strategic
- [ ] Is this migration feasible? (Or is HTML too inconsistent?)
- [ ] What CMS should we migrate to?
- [ ] Should we migrate all 117 sites or rationalize first?
- [ ] Can we justify the cost/effort? (ROI analysis)

### Tactical
- [ ] How long will it take? (12 months? 24 months?)
- [ ] How many people do we need?
- [ ] What's the critical path? (Content cleaning = bottleneck)
- [ ] Which sites should we migrate first? (Easy wins vs business priority)

### Technical
- [ ] Can we extract content via APIs? (Or need manual export?)
- [ ] How much automation is possible? (50%? 80%?)
- [ ] What custom functionality must be rebuilt?
- [ ] What's the asset migration strategy?

### Organizational
- [ ] Who are the stakeholders? (Regional content teams)
- [ ] What's the governance model? (Centralized vs federated)
- [ ] What's the content workflow? (Approvals, translations)
- [ ] What's the training plan? (New CMS for 100+ content editors)

---

## Next Immediate Steps

1. **Secure discovery phase approval** (4-6 weeks, 1.5 FTE, ~$XX budget)
2. **Assemble discovery team** (Technical Lead, CMS Architect, Content Strategist, PM)
3. **Kick off Week 1 tasks** (Platform identification + access audit)
4. **Start HTML consistency analysis** (THE CRITICAL TASK - don't delay)
5. **Schedule stakeholder interviews** (CMS requirements, content workflows)

---

*Document Version: 2.0 - Discovery Phase Focused*
*Date: 2025-12-05*
*Based on: Art Golk conversation + ResMed site catalog analysis*

**Key Principle**: Discovery phase determines if/how to migrate. Don't commit to migration until HTML consistency analysis is complete.
