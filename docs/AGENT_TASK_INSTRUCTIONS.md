# Agent Task: HTML Consistency & Migration Analysis

## Objective
Analyze assigned ResMed websites to assess migration difficulty for consolidation into a centralized CMS. Focus on HTML quality, content patterns, and automation potential.

## Your Assignment
You will be assigned a chunk of ~8-9 websites from the total 33 sites. Analyze each site thoroughly.

## Analysis Tasks

For each website in your assigned chunk, perform the following analysis:

### 1. Platform Identification
- Determine the CMS/platform (WordPress, HubSpot, Shopify, custom)
- Identify platform version if possible
- Note any platform-specific signatures in HTML

### 2. HTML Sampling & Analysis
**Sample Pages to Analyze:**
- Homepage
- 3-5 random interior pages (different page types: product, blog, landing page, etc.)
- Try to get diverse page templates

**For each page, analyze:**

#### 2.1 Inline Styling Analysis
- Estimate % of inline styles vs CSS classes (e.g., `style="..."` attributes)
- Identify common inline style patterns
- Rate inline style usage: Low (<20%), Medium (20-60%), High (>60%)

#### 2.2 HTML Structure & Consistency
- Are page structures similar across pages?
- Do pages use semantic HTML or div soup?
- Rate structure consistency: Low, Medium, High

#### 2.3 Content Patterns & Components
- Identify 5-10 common content patterns (e.g., hero banners, product cards, CTAs)
- Note how they're implemented (proper components vs custom HTML each time)
- Document custom shortcodes or platform-specific markup (WordPress shortcodes, HubSpot HubL)

#### 2.4 Anti-Patterns & Red Flags
Identify problematic patterns that will make migration difficult:
- Heavy inline styling
- Inconsistent page structures
- Custom JavaScript embedded in content
- Non-semantic HTML (excessive div nesting)
- Mixed content formats (Classic editor + Gutenberg blocks)
- Custom fonts/styles per section
- Hard-coded URLs
- Embedded iframes, custom widgets

#### 2.5 Content Complexity
- Estimate page complexity: Simple, Medium, Complex
- Note special features (forms, calculators, interactive elements)
- Identify dynamic content or personalization

### 3. Automation Assessment
Based on your analysis, estimate:
- **Automation Potential**: What % of content migration could be automated? (0-100%)
- **Manual Effort**: What will require human intervention?

### 4. Migration Difficulty Score
Provide a score from 1-10 for each site:
- **10 = Easy**: Clean HTML, consistent structure, high automation potential
- **7-9 = Medium**: Some issues but manageable
- **4-6 = Challenging**: Inconsistent HTML, moderate inline styling
- **1-3 = Very Difficult**: "Wild west" HTML, heavy inline styling, inconsistent structure

**Scoring Rubric:**
- Inline styles (30%): Less = better
- Structure consistency (25%): More = better
- Semantic HTML (20%): Better = higher score
- Custom code/shortcodes (15%): Less = better
- Complexity/nesting (10%): Less = better

### 5. Effort Estimation
For each site, estimate:
- **Total pages**: Approximate page count (crawl sitemap if available)
- **Average effort per page**: Hours (e.g., 0.5h for simple, 2-4h for complex)
- **Total migration hours**: Pages × Hours/page

## Output Format

For each site in your chunk, provide a structured analysis:

```markdown
## Site: [URL]

### Platform
- CMS: [WordPress/HubSpot/Shopify/Custom]
- Version: [if identifiable]
- Hosting: [from catalog data]

### HTML Consistency Score: X/10

### Analysis

#### Inline Styling
- **Usage Level**: [Low/Medium/High] (X%)
- **Patterns**: [describe common inline style patterns]

#### Structure Consistency
- **Rating**: [Low/Medium/High]
- **Notes**: [observations about structure]

#### Content Patterns
**Common patterns identified:**
1. [Pattern name]: [how implemented]
2. [Pattern name]: [how implemented]
3. ...

#### Anti-Patterns & Red Flags
- [Red flag 1]
- [Red flag 2]
- ...

#### Complexity
- **Rating**: [Simple/Medium/Complex]
- **Special Features**: [list any]

### Migration Assessment

#### Automation Potential: X%
**Automatable:**
- [what can be automated]

**Manual Work Required:**
- [what needs human touch]

#### Effort Estimate
- **Est. Total Pages**: ~X pages
- **Effort per Page**: X hours
- **Total Effort**: ~X hours

#### Migration Priority
[High/Medium/Low] - [brief reasoning]

#### Key Recommendations
- [Recommendation 1]
- [Recommendation 2]

---
```

## Summary Report

After analyzing all sites in your chunk, provide a summary:

```markdown
# Chunk [N] Summary

## Sites Analyzed: [count]

## Overall Findings

### Score Distribution
- Easy migrations (7-10): X sites
- Medium migrations (4-6): X sites
- Difficult migrations (1-3): X sites

### Total Effort Estimate
- Total pages (all sites): ~X pages
- Total hours (all sites): ~X hours
- Average hours per site: ~X hours

### Platform Breakdown
- WordPress: X sites
- HubSpot: X sites
- Shopify: X sites
- Custom: X sites

### Key Insights
1. [Major insight across sites in this chunk]
2. [Pattern observed]
3. [Recommendation]

### Highest Priority Sites (Easy Wins)
1. [Site URL] - Score: X/10, ~X hours
2. ...

### Most Challenging Sites
1. [Site URL] - Score: X/10, ~X hours, [why challenging]
2. ...
```

## Tools & Methods

### How to Sample Pages
1. Visit the site homepage
2. Click through to different page types
3. View page source (right-click → View Page Source)
4. Look for patterns in HTML structure
5. Check for `style=` attributes (inline styles)
6. Identify CMS signatures (wp-content, hubspot, etc.)

### Quick Platform Detection
- **WordPress**: Look for `/wp-content/`, `/wp-includes/`, `wp-json` API
- **HubSpot**: Look for `hubspot.com` in scripts, `hscoscdn`, HubL syntax
- **Shopify**: Look for `myshopify.com`, `cdn.shopify.com`

### Estimating Inline Style %
- Sample 5-10 content blocks per page
- Count blocks with `style=` attributes
- Estimate percentage

### Page Count Estimation
- Check `sitemap.xml` (add `/sitemap.xml` to domain)
- Or crawl main navigation and estimate depth × breadth

## Important Notes

- **Be honest**: Don't sugar-coat difficulties. Accurate assessment is critical.
- **Document evidence**: Note specific examples of good/bad HTML
- **Think about Art's warnings**: WordPress + HubSpot = "extremely painful" due to "wild west" HTML
- **Focus on migration impact**: Not just code quality, but how hard it is to migrate
- **Consider content editors**: Are they using WYSIWYG editors with inline styling?

## Deliverable

Submit one markdown file with:
1. Detailed analysis for each site in your chunk
2. Summary report at the end

Save as: `analysis_chunk_[N].md` where N is your chunk number (1-4)
