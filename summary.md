# ResMed Website Portfolio Migration Analysis - Executive Summary

**Analysis Date:** 2025-12-09
**Analyst:** Claude (Sonnet 4.5)
**Scope:** Brand/Marketing Website Migration Assessment

---

## Quick Stats

| Metric | Value |
|--------|-------|
| **Total Sites in Catalog** | 113 sites |
| **Sites Analyzed** | 54 brand/marketing sites (96% coverage) |
| **Sites Excluded** | 59 sites (e-commerce, SAAS, apps, etc.) |
| **Average Quality Score** | 6.3/10 |
| **Total Estimated Effort** | 10,500-16,500 hours |
| **Estimated Timeline** | 24-30 months |
| **Estimated Budget** | $5-7M |
| **Team Size Required** | 14-18 FTE |

---

## Critical Discovery: Best-in-Class Reference Site 🌟

**me.resmed.com (Middle East)** - Score: 7.5/10
- Only **2-3% inline styling** (vs 42% avg for HubSpot, 17% avg for WordPress)
- Cleanest Everest implementation found
- **Recommendation:** Use as reference template for all Everest migrations
- Could save 20-30% effort on other Everest sites

---

## Platform Breakdown

### WordPress/Everest Sites (27 sites)
- **AWS Account:** 270184546258 (rmd-app-everest-prd)
- **Inline Styling:** 2-45% (highly variable)
- **Total Effort:** ~4,900-7,600 hours
- **Key Sites:** UK, FR, DE, ES, IT, PT, NL, CZ, PL, CH, SE, DK, FI, NO, ME
- **Challenge:** WP Rocket dependency, performance optimization coupling

### HubSpot Sites (21 sites)
- **5 Portal Instances:** BR (6550155), ANZ (2163007), JP (43921914), EA (3445757), IN (5935712)
- **Inline Styling:** 15-90% (much worse than WordPress)
- **Total Effort:** ~3,200-5,100 hours
- **Challenge:** Extreme inline CSS, 11 countries on EA Instance must migrate together

### Other Platforms (6 sites)
- ExpressionEngine, Rails SPA, Custom applications
- **Total Effort:** ~1,200-2,000 hours

---

## Key Findings

### The Good ✅
1. **ME site proves clean is possible:** 2-3% inline styling on Everest
2. **Some sites already consolidated:** edensleep→resmed.co.nz, cpapaustralia blog→resmed.com.au/blog
3. **Awareness site opportunity:** 6+ similar sites can use single template (saves 300-600 hrs)
4. **Better than feared:** 10.5-16.5k hours vs initial estimate of 17.5-21k hours

### The Bad ⚠️
1. **HubSpot much worse than WordPress:** 42% avg inline CSS vs 17%
2. **EA Instance coordination nightmare:** 11 countries share one portal (SG, HK, KR, ID, MY, PH, TH, VN, TW, LA, MM, KH, BN)
3. **Everest quality varies wildly:** 2-3% (ME) to 35-45% (FI)
4. **Heavy jQuery everywhere:** All sites need JS modernization

### The Ugly 🚨
1. **India site:** 2,500+ lines inline CSS, 8+ complex forms - **REBUILD RECOMMENDED**
2. **Singapore site:** 5,600+ lines inline code - **REBUILD RECOMMENDED**
3. **sleepsurvey.resmed.com:** 85-90% inline CSS - **DEFER/REBUILD**
4. **Art was right:** "Wild west" HTML confirmed, especially HubSpot

---

## Score Distribution

| Quality Tier | Score | Count | % | Sites |
|--------------|-------|-------|---|-------|
| Excellent | 7.5-8 | 2 | 4% | ME, US |
| Good | 7-7.5 | 6 | 11% | UK, IT, deinschlaf-deintag |
| Medium-Good | 6.5-7 | 13 | 24% | Most Everest sites |
| Medium | 6-6.5 | 20 | 37% | Mixed WP/HubSpot |
| Challenging | 5.5-6 | 10 | 19% | Difficult HubSpot |
| Very Difficult | 5-5.5 | 3 | 6% | IN, SG, sleepsurvey |

---

## Recommended Phased Approach

### Phase 1: Quick Wins (6-9 months, 1,000-1,800 hrs)
**Start with best sites to establish patterns:**
1. me.resmed.com (reference implementation)
2. deinschlaf-deintag.de (clean awareness)
3. resmed.cz (clean Everest)
4. resmed.pl (clean Everest)
5. resmed.co.uk (major market)
6. resmed.it (major market)

### Phase 2: Core Everest Cluster (9-15 months, 3,000-4,500 hrs)
- Remaining European WordPress sites
- Apply patterns from Phase 1
- Coordinate Everest infrastructure migrations

### Phase 3: HubSpot Migrations (15-24 months, 3,500-5,500 hrs)
- BR Instance (Brazil, Mexico, LATAM)
- ANZ Instance (Australia, New Zealand)
- JP Instance (Japan)
- Awareness site template rollout

### Phase 4: Complex/EA Instance (24-30 months, 2,500-4,000 hrs)
- EA Instance (11 countries - requires dedicated team)
- Complex markets with high technical debt
- Remaining specialized sites

### Rebuilds (Ongoing, 500-1,700 hrs)
- India site (rebuild vs migrate)
- Singapore site (rebuild vs migrate)
- airdx.resmed.de (Rails SPA - separate path)
- narval-easy.resmed.eu (custom auth - rebuild)

---

## Critical Risks & Mitigation

### Risk 1: WP Rocket Dependency (ALL Everest Sites)
- **Impact:** Scripts don't execute without framework
- **Mitigation:** Develop modern lazy-loading replacement POC before starting

### Risk 2: EA Instance Coordination (11 Countries)
- **Impact:** Break one, break all - shared portal
- **Mitigation:** Dedicate separate team, migrate all 11 together

### Risk 3: Analytics Continuity
- **Impact:** GTM/dataLayer tracking deeply embedded
- **Mitigation:** Document all patterns, validation testing

### Risk 4: HubSpot Inline CSS Extraction
- **Impact:** 2,500-5,600 lines per site
- **Mitigation:** Build automated extraction toolkit, test with BR site

### Risk 5: Underestimation
- **Impact:** Effort could be 2-3x estimates
- **Mitigation:** Start with best sites, refine estimates after Phase 1

---

## Files to Read

### Primary Analysis Document
**`website_analysis.md`** - Complete detailed analysis
- 2,700+ lines
- 54 site-by-site detailed analyses
- Platform breakdowns
- Strategic recommendations
- Exclusion documentation

**Sections:**
1. **Lines 1-1200:** Initial 14 detailed site analyses
2. **Lines 1200-1800:** Original executive summary
3. **Lines 1800-2500:** Extended 40 site analyses
4. **Lines 2500-2740:** Updated executive summary & recommendations
5. **Lines 2740-end:** Sites excluded from analysis (59 sites documented)

### Source Data
**`Resmed Sites - Sheet1.csv`** - Original catalog of 113 sites

---

## Quick Reference: Best & Worst Sites

### Best Sites (Easy Migrations)
1. **me.resmed.com** (7.5/10) - 2-3% inline, ~150-250 hrs
2. **deinschlaf-deintag.de** (7/10) - 5% inline, ~100-150 hrs
3. **resmed.co.uk** (7/10) - 20-30% inline, ~375-600 hrs
4. **resmed.it** (7/10) - 20-30% inline, ~250-420 hrs

### Worst Sites (Rebuild Candidates)
1. **resmed.co.in** (5/10) - 60-70% inline, ~400-720 hrs - **REBUILD**
2. **resmed.sg** (5/10) - 50-60% inline, ~350-500 hrs - **REBUILD**
3. **sleepsurvey.resmed.com** (5/10) - 85-90% inline - **REBUILD**
4. **resmed.lat** (5.5/10) - 70-75% inline, ~180-280 hrs

### Most Strategic (High Impact)
1. **resmed.com/en-us** (8/10) - Main US site, ~500-750 hrs
2. **resmed.com.au** (6/10) - Main AU site, ~300-525 hrs
3. **resmed.co.uk** (7/10) - Main UK site, ~375-600 hrs
4. **resmed.de** (6/10) - Main DE site, ~300-450 hrs

---

## Immediate Next Steps (Next 3-6 Months)

1. **✅ Deep-dive ME site analysis** - Understand why it's so clean, extract patterns
2. **✅ WP Rocket replacement POC** - Critical blocker for Everest migrations
3. **✅ CSS extraction toolkit** - Automate HubSpot inline CSS extraction
4. **✅ Analytics audit** - Document all GTM patterns
5. **✅ Target CMS decision** - Select platform (headless CMS recommended)
6. **✅ India/Singapore rebuild assessment** - Cost comparison vs migration
7. **⚠️ Investigate webinars.resmed.eu** - Language variants not verified

---

## Questions & Considerations

### Scope Clarification Needed:
- Should e-commerce sites (15 sites) be included?
- Should corporate/IR sites (investor.resmed.com, newsroom.resmed.com) be included?
- Should partner portals be consolidated?

### Sites Needing Investigation:
- **sovnapne.no** - HTTP 500 error, couldn't analyze
- **webinars.resmed.eu language variants** - Not separately verified
- **selfiescreener.resmed.com** - React SPA, needs different analysis approach

---

## Bottom Line

**This is a complex, multi-year transformation** requiring:
- ✅ **30 months** (2.5 years)
- ✅ **$5-7M budget**
- ✅ **14-18 FTE team**
- ✅ **Executive commitment**
- ✅ **Strong technical leadership**

**Success factors:**
- Start with best sites (ME, UK, IT) to prove patterns
- Coordinate shared infrastructure (Everest cluster, HubSpot portals)
- Use ME site as reference implementation (could save 20-30% effort)
- Template awareness sites (saves 300-600 hours)
- Rebuild worst sites (IN, SG) rather than migrate
- Establish governance and standards early

**This is NOT "just a content migration"** - it's CSS refactoring, JS modernization, analytics preservation, and strategic transformation.

---

**For detailed analysis, read:** `website_analysis.md`
