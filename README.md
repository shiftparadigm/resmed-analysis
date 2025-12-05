# ResMed Multi-Site Discovery Project

Discovery phase for consolidating 117+ ResMed websites into a centralized CMS.

## Project Structure

```
.
├── scripts/          # Site discovery and analysis scripts
│   └── resmed_catalog.py    # Main site enumeration script
├── data/             # Generated data and inventories
│   └── resmed_sites.csv     # Catalog of 33+ discovered sites
├── docs/             # Documentation and planning
│   └── MIGRATION_PLAN.md    # Discovery phase plan (4-6 weeks)
├── venv/             # Python virtual environment
└── README.md         # This file
```

## Quick Start

### Setup
```bash
# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run Site Catalog
```bash
python scripts/resmed_catalog.py
```

This will discover ResMed sites and output to `data/resmed_sites.csv`.

## Current Status

- **Sites Cataloged**: 33+ production sites
- **Primary Platforms**: WordPress (majority), HubSpot (ap.resmed.com)
- **Additional Platforms**: Shopify (e-commerce), Nginx/Apache (custom)
- **Total Target**: 117+ sites across all regions

## Key Documents

- **[MIGRATION_PLAN.md](docs/MIGRATION_PLAN.md)** - Discovery phase plan with tasks, deliverables, and critical insights from industry experience

## Discovery Phase

**Duration**: 4-6 weeks
**Team**: ~1.5 FTE
**Output**: Migration plan, CMS recommendation, effort estimates

### Critical Activities
1. HTML consistency analysis (AI-powered)
2. Platform identification for all 117 sites
3. Content/asset inventory
4. CMS evaluation and recommendation
5. Effort estimation and timeline

See [docs/MIGRATION_PLAN.md](docs/MIGRATION_PLAN.md) for full details.

## Data Files

### `data/resmed_sites.csv`
Columns:
- `host` - Domain name
- `url` - Full URL
- `status` - HTTP status code
- `title` - Page title
- `hosting_provider` - Detected hosting/CDN (Cloudflare, Akamai, HubSpot, etc.)
- `ip` - IP address
- `cname_chain` - DNS CNAME chain

## Scripts

### `scripts/resmed_catalog.py`
Multi-phase site discovery:
1. Scrapes country selector pages
2. Expands via hreflang tags
3. Queries Certificate Transparency logs
4. Enumerates TLD variations
5. Enumerates subdomains
6. Catalogs with platform detection

**Filters**: Excludes dev/staging/admin/test/api domains and login/404 pages.

## Multi-Agent Analysis

This project is configured for parallel analysis using 4 agents.

**Quick Start**:
```bash
# Split sites into chunks (already done)
python scripts/split_sites.py

# Run your multi-agent tool with the chunks
# Each agent analyzes 8 sites in parallel
# See docs/MULTI_AGENT_SETUP.md for details
```

**Documentation**:
- [`docs/MULTI_AGENT_SETUP.md`](docs/MULTI_AGENT_SETUP.md) - Agent configuration and execution
- [`docs/AGENT_TASK_INSTRUCTIONS.md`](docs/AGENT_TASK_INSTRUCTIONS.md) - Detailed analysis instructions

**Input**: `data/chunks/chunk_N_urls.json` (N=1-4)
**Output**: `data/analysis/analysis_chunk_N.md`
**Consolidate**: `python scripts/consolidate_analysis.py`

## Next Steps

1. ✅ Sites cataloged (32 sites discovered)
2. ✅ Chunks created (4 chunks of 8 sites each)
3. **→ Run multi-agent HTML analysis** (THE CRITICAL TASK)
4. Consolidate agent reports
5. Generate final migration plan
6. Secure access to WordPress/HubSpot admin panels (for pilot migration)
7. Schedule stakeholder interviews for CMS requirements

## Notes

Based on industry experience (Art Golk):
- WordPress + HubSpot migrations are "extremely painful"
- HTML consistency analysis is critical first step
- Content cleaning is the "largest tent stake" (60-70% of effort)
- Use AI to analyze HTML consistency at scale
