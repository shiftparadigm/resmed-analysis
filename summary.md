# ResMed Website Portfolio Content Migration Analysis - Executive Summary

**Analysis Date:** 2025-12-09
**Analyst:** Claude (Sonnet 4.5)
**Scope:** Content Migration to New Site with New Content Model
**Migration Type:** Content extraction and mapping (NOT frontend preservation)

---

## Quick Stats

| Metric | Value |
|--------|-------|
| **Total Sites in Catalog** | 113 sites |
| **Sites Analyzed** | 54 brand/marketing sites (96% coverage) |
| **Sites Excluded** | 59 sites (e-commerce, SAAS, apps, etc.) |
| **Average Content Quality Score** | 6.3/10 |
| **Total Content Migration Effort** | 8,900-14,200 hours |
| **Estimated Timeline** | 20-26 months |
| **Estimated Budget** | $4.5-6M |
| **Team Size Required** | 12-16 FTE |

---

## Critical Discovery: Best-in-Class Content Structure 🌟

**me.resmed.com (Middle East)** - Content Quality: 7.5/10
- Only **2-3% inline styling** = cleanest, most structured content (vs 42% avg for HubSpot, 17% avg for WordPress)
- Content properly separated from presentation
- **Recommendation:** Use as reference for content model mapping
- Clean extraction patterns could save 20-30% effort on other sites

---

## Platform Breakdown

### WordPress/Everest Sites (27 sites)
- **AWS Account:** 270184546258 (rmd-app-everest-prd)
- **Content Messiness:** 2-45% inline styling (highly variable)
- **Content Extraction:** WordPress REST API + WP-CLI for bulk export
- **Total Content Cleanup Effort:** ~4,100-6,400 hours
- **Key Sites:** UK, FR, DE, ES, IT, PT, NL, CZ, PL, CH, SE, DK, FI, NO, ME
- **Challenge:** Variable content quality - some sites well-structured, others heavy WYSIWYG abuse

### HubSpot Sites (21 sites)
- **5 Portal Instances:** BR (6550155), ANZ (2163007), JP (43921914), EA (3445757), IN (5935712)
- **Content Messiness:** 15-90% inline styling (indicates heavy WYSIWYG abuse)
- **Content Extraction:** HubSpot Content API for programmatic export
- **Total Content Cleanup Effort:** ~2,800-4,500 hours
- **Challenge:** Extreme inline CSS = content deeply coupled with presentation. 11 countries on EA Instance share content structure

### Other Platforms (6 sites)
- ExpressionEngine, Rails SPA, Custom applications
- **Content Extraction:** Custom scraping or database exports
- **Total Content Cleanup Effort:** ~1,000-1,700 hours

---

## Key Findings

### The Good ✅
1. **ME site proves clean content is possible:** 2-3% inline styling = properly structured content
2. **Some sites already consolidated:** edensleep→resmed.co.nz, cpapaustralia blog→resmed.com.au/blog
3. **Awareness site opportunity:** 6+ similar sites can use single content template (saves 300-600 hrs)
4. **Better than feared:** 8.9-14.2k hours for content migration vs 10.5-16.5k for full frontend preservation

### The Bad ⚠️
1. **HubSpot content much messier than WordPress:** 42% avg inline CSS vs 17% = content/presentation coupling
2. **EA Instance coordination challenge:** 11 countries share one portal (SG, HK, KR, ID, MY, PH, TH, VN, TW, LA, MM, KH, BN) = shared content structures
3. **WordPress content quality varies wildly:** 2-3% (ME) to 35-45% (FI) inline styling
4. **Content deeply coupled with presentation:** Heavy inline styling requires extensive cleanup during extraction

### The Ugly 🚨
1. **India site:** 2,500+ lines inline CSS = content inseparable from styling - **SELECTIVE MIGRATION OR REBUILD**
2. **Singapore site:** 5,600+ lines inline code = extreme content/presentation coupling - **SELECTIVE MIGRATION**
3. **sleepsurvey.resmed.com:** 85-90% inline CSS = nearly impossible to cleanly extract - **DEFER/REBUILD**
4. **"Wild west" content editing confirmed:** Especially HubSpot - WYSIWYG editors used to build bespoke layouts per page

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

## Content Model Approach

This migration will map existing content to a **new unified content model** with modern component-based architecture. See `content-model-recommendations.md` for full specification.

### New Content Architecture
**5 Core Content Types:**
1. Page (flexible page builder)
2. Blog Post / Article
3. Landing Page (conversion-focused)
4. Awareness Page (educational)
5. Resource / Download

**15-20 Reusable Components:**
- Hero Banner, Card Grid, Text Block, CTA Block, Form, Media/Text Split, Accordion/FAQ, etc.
- No WYSIWYG styling allowed (colors, fonts, margins disabled)
- Content separated from presentation

### Content Cleanup Tiers

**Tier 1: Minimal Cleanup (2-10% inline styling)**
- Sites: ME, deinschlaf-deintag, CZ, PL
- **Effort Multiplier:** 1x baseline
- Process: Extract → Map 1:1 → Light QA

**Tier 2: Moderate Cleanup (15-30% inline styling)**
- Sites: UK, IT, DE, FR, most WordPress/Everest
- **Effort Multiplier:** 2x baseline
- Process: Extract → Strip inline styles → Map to components → QA

**Tier 3: Heavy Cleanup (40-90% inline styling)**
- Sites: IN, SG, LATAM, sleepsurvey, some HubSpot
- **Effort Multiplier:** 5-8x baseline
- Process: Extract → Major cleanup → Restructure to components → Extensive QA
- **Recommendation:** Consider selective migration (priority pages only) or rebuild

### Migration Strategy
1. **Extract content** via platform APIs (WordPress REST API, HubSpot Content API)
2. **Clean inline styling** and presentation-coupled markup
3. **Map to new content model** - identify components, restructure to new types
4. **Import to new CMS** using structured data
5. **QA & validation** - content integrity, analytics, SEO

---

## Recommended Phased Approach

### Phase 1: Pattern Establishment (5-8 months, 850-1,500 hrs)
**Start with cleanest content to establish extraction & mapping patterns:**
1. me.resmed.com (Tier 1: reference content model mapping)
2. deinschlaf-deintag.de (Tier 1: awareness template)
3. resmed.cz (Tier 1: clean extraction)
4. resmed.pl (Tier 1: clean extraction)
5. resmed.co.uk (Tier 2: major market, moderate cleanup)
6. resmed.it (Tier 2: major market, moderate cleanup)

**Deliverables:** Extraction scripts, cleanup tooling, component mapping playbook

### Phase 2: Core WordPress Content (8-14 months, 2,500-3,800 hrs)
- Remaining European WordPress sites (mostly Tier 2)
- Apply extraction patterns from Phase 1
- Refine automated cleanup tooling
- Coordinate multi-language content structures

### Phase 3: HubSpot Content Extraction (14-22 months, 2,900-4,600 hrs)
- BR Instance (Brazil, Mexico, LATAM) - Tier 2-3
- ANZ Instance (Australia, New Zealand) - Tier 2
- JP Instance (Japan) - Tier 2
- Awareness site content template rollout
- **Challenge:** Higher cleanup effort due to presentation coupling

### Phase 4: Complex Content / EA Instance (22-26 months, 2,100-3,400 hrs)
- EA Instance (11 countries - shared content structures)
- Complex markets with heavy inline styling
- Remaining specialized sites
- Selective migration for Tier 3 sites

### Selective Migration / Rebuilds (Ongoing, 400-900 hrs)
- India site (migrate priority pages only, rebuild rest)
- Singapore site (migrate priority pages only, rebuild rest)
- airdx.resmed.de (Rails SPA - custom extraction)
- narval-easy.resmed.eu (custom auth - rebuild)

---

## Critical Risks & Mitigation

### Risk 1: Content/Presentation Coupling (Tier 3 Sites)
- **Impact:** 40-90% inline styling makes content extraction extremely difficult
- **Sites Affected:** IN, SG, LATAM, sleepsurvey, several HubSpot sites
- **Mitigation:** Build automated cleanup toolkit, test with BR site first. Consider selective migration (priority pages only) for worst sites

### Risk 2: EA Instance Content Coordination (11 Countries)
- **Impact:** Shared HubSpot portal = shared content structures across 11 APAC countries
- **Mitigation:** Dedicate separate team, extract and migrate all 11 together to maintain consistency

### Risk 3: Content Model Mapping Complexity
- **Impact:** Diverse content patterns across 54 sites must map to unified model
- **Mitigation:** Start with Tier 1 sites to establish component library and mapping patterns before tackling complex sites

### Risk 4: Analytics & Metadata Loss
- **Impact:** GTM/dataLayer tracking, SEO metadata, URL structures embedded in content
- **Mitigation:** Document all patterns, preserve metadata during extraction, implement redirects, validation testing

### Risk 5: Automated Cleanup Tool Limitations
- **Impact:** Heavily customized pages may not clean up programmatically (Tier 3)
- **Mitigation:** Manual content review and restructuring for complex pages. Budget 5-8x effort for Tier 3 sites

### Risk 6: Effort Underestimation
- **Impact:** Content cleanup could take 2-3x longer than estimated for messy sites
- **Mitigation:** Start with Tier 1 sites to validate estimates, adjust Phase 2+ planning based on actual effort

---

## Files to Read

### Content Model Design
**`content-model-recommendations.md`** - New unified content architecture (READ THIS FIRST)
- 5 core content types with field specifications
- 15-20 reusable component library
- Component usage frequency across all sites
- Content cleanup tier methodology
- Migration strategy and governance recommendations

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

1. **✅ Content model design** - Define unified content types and component library (COMPLETED: see content-model-recommendations.md)
2. **🔨 Target CMS selection** - Choose platform that supports component-based content (headless CMS recommended)
3. **🔨 Content extraction toolkit development** - WordPress REST API + HubSpot Content API extraction scripts
4. **🔨 Automated cleanup toolkit** - Strip inline CSS, restructure to semantic HTML
5. **🔨 Component mapping playbook** - Document how to map old patterns to new components
6. **🔨 ME site pattern analysis** - Deep-dive into cleanest content structure, use as reference
7. **🔨 Analytics & metadata preservation** - Document all GTM patterns, SEO metadata structures
8. **🔨 India/Singapore selective migration plan** - Identify priority pages vs rebuild candidates
9. **⚠️ Investigate webinars.resmed.eu** - Language variants not verified

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

**This is a complex, multi-year content migration** requiring:
- ✅ **26 months** (~2 years)
- ✅ **$4.5-6M budget**
- ✅ **12-16 FTE team**
- ✅ **Executive commitment**
- ✅ **Strong content strategy leadership**

**Success factors:**
- Start with Tier 1 sites (ME, CZ, PL) to establish extraction & mapping patterns
- Build automated cleanup tooling early - critical for scale
- Use ME site as content model reference (could save 20-30% effort)
- Template-based approach for awareness sites (saves 300-600 hours)
- Selective migration for worst sites (IN, SG) - priority pages only, rebuild rest
- Component-first content architecture - prevent future inline CSS mess
- Establish content governance and editorial guidelines early

**This IS "content migration"** - extracting content from 54 sites, cleaning up presentation coupling, and mapping to a new unified content model with component-based architecture. The new site will have a new design system and frontend - we're only bringing the content forward.

---

**For detailed analysis, read:** `website_analysis.md`
