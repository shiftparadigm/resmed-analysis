# ResMed Content Model Recommendations

**Based on Analysis of 54 Brand/Marketing Websites**
**Date:** 2025-12-09

---

## Executive Summary

Analysis of 54 ResMed brand/marketing websites revealed consistent **content patterns and component types** across all sites, despite varying platforms (WordPress, HubSpot) and quality levels.

**Key Finding:** A unified content model with **5 core content types** and **15-20 reusable components** can support all brand/marketing site needs.

---

## Core Content Types

### 1. Page (Flexible Page Builder)

**Purpose:** Standard pages with flexible component composition

**Fields:**
- Title (required)
- Meta Description (SEO)
- Hero Section (optional - component)
- Body (component builder - add/remove/reorder)
- Sidebar (optional - regional navigation, CTAs)

**Examples Found:**
- Homepage (all sites)
- About pages
- Product category pages
- Service pages
- General information pages

**Usage:** ~60-70% of all content

---

### 2. Blog Post / Article

**Purpose:** News, updates, educational content, thought leadership

**Fields:**
- Title (required)
- Author (optional - some sites have, others don't)
- Publication Date (required)
- Categories/Tags (taxonomy)
- Featured Image (required)
- Excerpt/Summary (optional)
- Body (rich text + components)
- Related Articles (automated or manual)

**Examples Found:**
- resmed.com.au/blog
- Most awareness sites (somnapne.se, sovnapno.dk, etc.)
- Some main sites have blog sections

**Usage:** ~15-20% of all content

**Note:** Only about 40% of sites have active blogs. Consider if this is needed globally or per-region.

---

### 3. Landing Page (Conversion-Focused)

**Purpose:** Campaign pages, lead generation, product launches

**Fields:**
- Title (required)
- Meta Description (SEO)
- Hero Section (required - strong CTA)
- Body (component builder - conversion-optimized)
- Form (required - lead capture)
- No header/footer option (for campaigns)
- Tracking codes (campaign-specific)

**Examples Found:**
- hifae-hft.com (trial landing page)
- hilot-hft.com (trial landing page)
- sleepsurvey.resmed.com (survey campaign)
- Various campaign pages across sites

**Usage:** ~10-15% of all content

**Characteristics:**
- High CTA density
- Forms are critical
- Often single-purpose
- Tracking-heavy

---

### 4. Awareness Page (Disease/Condition Education)

**Purpose:** Educational content about sleep apnea, respiratory conditions, health topics

**Fields:**
- Title (required)
- Condition/Topic (taxonomy)
- Meta Description (SEO)
- Hero Section (educational focus)
- Body (rich text + components)
- Related Conditions (links)
- Related Resources (downloads, videos)
- CTA (screening tool, find a provider, etc.)

**Examples Found:**
- syndrome-apnee-sommeil.fr (French sleep apnea awareness)
- deinschlaf-deintag.de (German sleep awareness)
- somnapne.se (Swedish sleep apnea)
- Awareness sections on main sites

**Usage:** ~10-15% of all content

**Characteristics:**
- Educational tone
- Medical/scientific accuracy required
- Compliance/regulatory review needed
- Regional variations (language, medical practices)

---

### 5. Resource / Download

**Purpose:** PDFs, guides, whitepapers, videos, webinar recordings

**Fields:**
- Title (required)
- Type (PDF, Video, Webinar, Guide, etc.)
- Description/Summary
- File Upload OR External URL
- Thumbnail Image
- Categories/Tags (taxonomy)
- Gated (yes/no - requires form fill)
- Target Audience (Patient, Professional, Both)

**Examples Found:**
- webinars.resmed.eu (webinar recordings)
- Various PDF downloads across sites
- Product guides
- Clinical resources

**Usage:** ~5-10% of all content

**Note:** Current architecture has these scattered. Recommend centralizing in DAM (Aprimo) with references in CMS.

---

## Component Library (15-20 Core Components)

Based on `data-component` attributes found across WordPress sites and HubSpot module patterns.

### Navigation Components

#### 1. Hero Banner
**Found on:** 95% of sites
**Variants:**
- Full-width with background image
- Video background
- Split layout (image left/right)
- Minimal (text-only for awareness pages)

**Content Fields:**
- Heading (H1)
- Subheading/description
- Background image/video
- CTA button(s) (1-2 buttons)
- Text alignment (left, center, right)

**Examples:**
- resmed.com/en-us - large hero with video
- me.resmed.com - clean image hero
- deinschlaf-deintag.de - minimal text hero

---

#### 2. Navigation / Mega Menu
**Found on:** All sites
**Patterns:**
- 2-3 level navigation
- Mega-menu (some sites)
- Mobile hamburger menu
- Country/language selector

**Content Fields:**
- Menu items (hierarchical)
- Featured links (in mega-menu)
- Icons (optional)
- Promotional callout (some sites)

**Note:** All sites have complex multi-level navigation. New CMS must support this.

---

#### 3. Breadcrumbs
**Found on:** 80% of sites
**Pattern:** Home > Category > Page

**Note:** Consistently used for SEO and navigation. Auto-generate from page hierarchy.

---

### Content Components

#### 4. Card Grid
**Found on:** 90% of sites
**Most common component type**

**Variants:**
- Product cards
- Blog/article cards
- Service cards
- Team member cards
- Feature/benefit cards

**Content Fields (per card):**
- Image (optional)
- Icon (optional - some sites)
- Heading
- Description
- Link/CTA
- Badge/tag (optional - "New", "Featured", etc.)

**Layout Options:**
- 2, 3, or 4 columns
- With or without images
- Grid or list view

**Examples:**
- resmed.com.au - product cards (3-col)
- resmed.co.uk - service cards (4-col)
- Blog listings across all sites

---

#### 5. Text Block (Rich Text)
**Found on:** 100% of sites
**Purpose:** Main content area with formatting

**Features Needed:**
- Headings (H2-H6)
- Paragraphs
- Bold, italic, underline
- Lists (ordered, unordered)
- Links
- Images (inline)
- Blockquotes
- Tables (rarely used, but some sites have)

**Note:** This is where high inline CSS sites went wrong - WYSIWYG abuse. New CMS should limit styling options.

---

#### 6. Media / Text Split
**Found on:** 70% of sites
**Pattern:** Image on one side, text on other

**Content Fields:**
- Image (left or right)
- Heading
- Body text
- CTA button (optional)
- Background color/style (optional)

**Examples:**
- resmed.com/en-us - product features
- resmed.it - benefit sections
- Most sites use this heavily

---

#### 7. CTA Block (Call to Action)
**Found on:** 95% of sites
**Purpose:** Standalone conversion element

**Variants:**
- Simple button
- Button with text
- Full-width banner with CTA
- Split CTA (2 options)

**Content Fields:**
- Heading (optional)
- Description (optional)
- Button text
- Button link
- Button style (primary, secondary, outline)
- Background color/image

**Examples:**
- "Find a Provider" CTAs
- "Shop Now" CTAs
- "Learn More" buttons throughout

---

#### 8. Accordion / FAQ
**Found on:** 60% of sites
**Purpose:** Q&A, expandable content sections

**Content Fields (per item):**
- Question/heading
- Answer/body (rich text)
- Initially open/closed

**Examples:**
- FAQ sections on most main sites
- Product information expandables
- Awareness site Q&A sections

**Note:** Very common pattern. Must be accessible (ARIA).

---

#### 9. Carousel / Slider
**Found on:** 50% of sites
**Purpose:** Testimonials, product showcases, image galleries

**Common Uses:**
- Customer testimonials (resmed.com.au - Slick carousel)
- Product features
- Image galleries
- Partner logos

**Content Fields (per slide):**
- Image (optional)
- Heading (optional)
- Body text
- CTA (optional)

**Controls:**
- Auto-advance (yes/no)
- Navigation dots/arrows
- Number of slides to show

**Note:** Modern accessibility concerns - consider alternatives. But found on many sites.

---

#### 10. Video Embed
**Found on:** 40% of sites
**Sources:**
- YouTube (most common)
- Brightcove (some sites)
- Vimeo (rare)

**Content Fields:**
- Video URL OR embed code
- Thumbnail image (optional - usually auto from video)
- Caption (optional)
- Autoplay (yes/no)

**Examples:**
- Product demo videos
- Educational content
- Webinar recordings

---

#### 11. Form
**Found on:** 90% of sites
**Types:**
- Contact forms (simple)
- Newsletter signup (simple)
- Lead generation (medium)
- Multi-step forms (complex - some sites)
- Assessment tools (complex - selfiescreener)

**Common Fields:**
- Name (first, last or full)
- Email (required almost always)
- Phone (optional)
- Country/Region
- Message/Comments
- Consent checkboxes (GDPR)

**Integrations Needed:**
- Email service (Mailchimp, HubSpot, etc.)
- CRM (Salesforce - some sites)
- Marketing automation

**Note:** HubSpot sites have complex form logic (lead scoring, routing). Need to decide how to handle this.

---

#### 12. Stats / Metrics Block
**Found on:** 30% of sites
**Purpose:** Highlight key numbers, achievements

**Content Fields (per metric):**
- Number/statistic
- Label/description
- Icon (optional)

**Layout:** 2-4 columns

**Examples:**
- "10M+ patients helped"
- "140+ countries"
- Clinical trial results

---

#### 13. Testimonial / Quote Block
**Found on:** 40% of sites
**Purpose:** Customer quotes, reviews

**Content Fields:**
- Quote text
- Author name
- Author title/location (optional)
- Author photo (optional)
- Rating (optional - stars)

**Examples:**
- Patient testimonials (resmed.com.au)
- Healthcare provider quotes
- Case study quotes

---

#### 14. Tabs
**Found on:** 30% of sites
**Purpose:** Organize content into tabbed sections

**Content Fields (per tab):**
- Tab label
- Tab content (rich text + components)

**Examples:**
- Product specifications (different tabs for features, specs, support)
- Regional content (different tabs per region)

**Note:** Less common, but useful for dense content.

---

#### 15. Image Gallery
**Found on:** 25% of sites
**Purpose:** Multiple images, lightbox viewer

**Content Fields (per image):**
- Image
- Caption (optional)
- Alt text

**Layout:**
- Grid (2x2, 3x3, etc.)
- Masonry (Pinterest-style)

---

### Interactive Components (Specialized)

#### 16. Solution Finder / Quiz
**Found on:** 10% of sites
**Examples:**
- resmed.sg - solution finder quiz
- selfiescreener.resmed.com - OSA screening tool

**Purpose:** Interactive tools to guide users

**Characteristics:**
- Multi-step
- Conditional logic
- Result pages based on answers
- Often leads to form/CRM

**Recommendation:** Build as custom modules OR integrate third-party quiz/assessment tools.

---

#### 17. Product Comparison Table
**Found on:** 15% of sites
**Purpose:** Compare features across products

**Content Fields:**
- Products to compare (select from product content type OR manual)
- Features to compare (rows)
- Values per product (cells)

**Note:** Not heavily used, but valuable for some regions.

---

#### 18. Download List / Resource Library
**Found on:** 20% of sites
**Purpose:** List of PDFs, videos, resources

**Content Fields:**
- Resource items (from Resource content type)
- Filter options (by type, category, audience)
- Search

**Examples:**
- webinars.resmed.eu - webinar library
- Clinical resource sections
- Product documentation

---

### Footer Components

#### 19. Footer Navigation
**Found on:** 100% of sites
**Pattern:** Multi-column link lists

**Common Sections:**
- About Us
- Products/Services
- Support
- Legal (Privacy, Terms)
- Contact
- Social media links
- Country/language selector
- Copyright

**Note:** Very consistent across all sites. Template once, localize per region.

---

#### 20. Newsletter Signup (Footer)
**Found on:** 40% of sites
**Purpose:** Email capture in footer

**Content Fields:**
- Heading
- Description
- Email field
- Submit button
- Privacy/consent text

---

## Content Taxonomies

### Categories / Tags

**Blog Categories** (if blogs are used):
- Sleep Health
- Product News
- Clinical Research
- Patient Stories
- Company News

**Product Categories** (if products in CMS):
- CPAP Devices
- Masks
- Accessories
- Diagnostics
- Respiratory Care

**Audience Tags:**
- Patients
- Healthcare Professionals
- Sleep Specialists
- Respiratory Therapists

**Condition Tags:**
- Sleep Apnea
- COPD
- Asthma
- Snoring
- Insomnia

**Region/Country:**
- Should be at site/instance level, not content level
- Multi-site/multi-language architecture

---

## Regional / Multi-Language Considerations

### Patterns Found:

**WordPress Sites (Everest):**
- Single WordPress multi-site network OR separate installs per country
- Country selector in navigation (40-140+ countries)
- Language variants (DE/FR for Switzerland, etc.)

**HubSpot Sites:**
- Separate portals by region (BR, ANZ, JP, EA, IN)
- Some portals serve multiple countries (EA = 11 countries)
- Language parameter (hsLang=en-us, etc.)

### Recommendations:

**Option 1: Multi-site Architecture**
- One CMS instance per region/language
- Shared component library
- Region-specific content

**Option 2: Single Instance with Localization**
- One CMS, multiple language/region versions
- Content translation workflow
- Region-specific fields/components

**Preferred:** Option 1 (multi-site) - simpler, less coupling, aligns with current architecture

---

## Form Strategy

### Form Types Needed:

1. **Contact Form** (simple)
   - Name, Email, Message
   - Used on: 90% of sites

2. **Newsletter Signup** (simple)
   - Email only
   - Used on: 70% of sites

3. **Lead Generation Form** (medium)
   - Name, Email, Phone, Country, Comments
   - Consent checkboxes (GDPR)
   - Used on: 60% of sites

4. **Sleep Assessment / Screener** (complex)
   - Multi-step
   - Conditional logic
   - Result calculation
   - Used on: 10% of sites

5. **Webinar Registration** (medium)
   - Name, Email, Company, Job Title
   - Used on: webinar sites

### Integration Requirements:

**Must integrate with:**
- Email service (Mailchimp, SendGrid, or HubSpot)
- CRM (Salesforce - for lead routing)
- Marketing automation (for nurture campaigns)

**HubSpot Sites Currently Use:**
- HubSpot Forms API
- Lead scoring and routing
- Salesforce CRM integration (some sites)
- AWS Lambda endpoints (custom processing - some sites)

**Decision Needed:**
- Use new CMS's native forms?
- Use HubSpot forms embedded (keep CRM integration)?
- Use third-party form builder (Typeform, Gravity Forms, etc.)?

---

## Design System Implications

### Spacing/Layout System

**Found patterns:**
- Grid layouts (2, 3, 4 columns)
- Consistent spacing between sections
- Full-width and contained sections
- White backgrounds and colored backgrounds

**Recommendation:** Define spacing scale (8px, 16px, 24px, 32px, 48px, 64px, 96px)

### Typography Hierarchy

**Headings Found:**
- H1: Page title (hero)
- H2: Section headings
- H3: Subsection headings
- H4: Component headings (cards, etc.)
- H5-H6: Rarely used

**Body Text:**
- Paragraph text
- Lists (ordered, unordered)
- Links (inline, standalone)

### Color Usage

**Common Patterns:**
- Primary brand color (CTAs, highlights)
- Secondary color (accents)
- Neutral grays (text, borders, backgrounds)
- Success/error states (forms)
- White and light gray backgrounds (alternating sections)

### Button Styles

**Found:**
- Primary button (solid background, brand color)
- Secondary button (outline or ghost)
- Text link (underlined or plain)
- Icon buttons (arrows, close, etc.)

---

## Component Usage Frequency (Across All Sites)

| Component | Usage % | Priority |
|-----------|---------|----------|
| Hero Banner | 95% | Critical |
| Card Grid | 90% | Critical |
| Text Block | 100% | Critical |
| CTA Block | 95% | Critical |
| Form | 90% | Critical |
| Media/Text Split | 70% | High |
| Accordion/FAQ | 60% | High |
| Navigation/Mega Menu | 100% | Critical |
| Breadcrumbs | 80% | High |
| Footer Navigation | 100% | Critical |
| Carousel/Slider | 50% | Medium |
| Video Embed | 40% | Medium |
| Testimonial | 40% | Medium |
| Stats/Metrics | 30% | Medium |
| Tabs | 30% | Medium |
| Image Gallery | 25% | Low |
| Download List | 20% | Low |
| Product Comparison | 15% | Low |
| Solution Finder/Quiz | 10% | Low (custom) |
| Newsletter Signup | 40% | Medium |

**Build Priority:**
1. **Critical (must-have for MVP):** 8 components
2. **High (needed early):** 3 components
3. **Medium (can come later):** 5 components
4. **Low (as needed):** 4 components

---

## Content Governance Insights

### Sites with Good Content Governance (Low Inline CSS):

**Indicators:**
- Content fits templates
- Consistent component usage
- Authors follow style guide
- Limited WYSIWYG styling

**Examples:**
- me.resmed.com (2-3% inline)
- deinschlaf-deintag.de (5% inline)
- resmed.cz (5-10% inline)

**Lessons:**
- Restrict WYSIWYG styling options
- Provide good component library
- Train content authors
- Enforce templates

### Sites with Poor Content Governance (High Inline CSS):

**Indicators:**
- Every page looks different
- Heavy WYSIWYG use
- Custom styles per page
- Inconsistent branding

**Examples:**
- resmed.co.in (60-70% inline)
- sleepsurvey.resmed.com (85-90% inline)
- resmed.lat (70-75% inline)

**Lessons:**
- Don't give authors too much freedom
- Make templates easy to use
- Provide pre-styled components
- Lock down WYSIWYG editor

---

## Recommendations for New Content Model

### 1. Component-First Approach

**Principle:** Pages are built from components, not WYSIWYG

**Implementation:**
- Page content type has component builder field
- Authors select from component library
- Each component has structured fields
- WYSIWYG is limited to simple rich text (no styling)

**Benefits:**
- Consistent design
- Easier to maintain
- Better governance
- Prevents inline CSS mess

### 2. Structured Content Over Freeform

**Principle:** Use structured fields instead of rich text where possible

**Example:**
- Card component: structured fields (image, heading, description, link)
- NOT: rich text field where authors build cards manually

**Benefits:**
- Forces consistency
- Easier to redesign
- Content is portable
- Better for headless/omnichannel

### 3. Limit WYSIWYG Styling Options

**Allowed:**
- Headings (H2-H6)
- Bold, italic
- Lists
- Links
- Images (with alt text)

**NOT Allowed:**
- Custom colors
- Font sizes
- Margins/padding
- Background colors
- Alignment (use components instead)

**Benefits:**
- Prevents inline CSS
- Forces use of design system
- Consistent branding
- Easier maintenance

### 4. Regional Content Strategy

**Recommendation:** Multi-site with shared component library

**Structure:**
- One CMS instance per major region/language
- Shared component definitions
- Regional content authoring
- Centralized design system

**Regions:**
- US/Americas (English)
- UK/Europe (English)
- France (French)
- Germany (German)
- Spain (Spanish)
- Italy (Italian)
- Nordics (Swedish/Danish/Norwegian/Finnish)
- LATAM (Spanish/Portuguese)
- APAC (English + local languages)
- Japan (Japanese)
- China (Chinese) - if applicable

### 5. Content Workflow

**Recommendation:** Approval workflow for quality control

**Workflow:**
- Draft → Review → Approved → Published
- Role-based permissions (Author, Editor, Admin)
- Version control (content history)

**Benefits:**
- Quality control
- Prevents bad content from going live
- Accountability

---

## Migration Complexity by Content Cleanup Effort

### Tier 1: Minimal Cleanup (Well-Structured Sites)

**Sites:** me.resmed.com, deinschlaf-deintag.de, resmed.cz, resmed.pl, resmed.se

**Characteristics:**
- Content already fits templates
- Low inline CSS (2-10%)
- Component-based structure

**Mapping Effort:** 1x baseline (easy)

**Process:**
1. Extract content
2. Map to new components (1:1 mapping)
3. Light QA
4. Done

---

### Tier 2: Moderate Cleanup (Partially Structured)

**Sites:** resmed.co.uk, resmed.it, resmed.de, resmed.fr, most Everest sites

**Characteristics:**
- Mostly template-based
- Some custom pages
- Medium inline CSS (15-30%)

**Mapping Effort:** 2x baseline (moderate)

**Process:**
1. Extract content
2. Strip some inline styles
3. Map to new components (mostly 1:1, some restructuring)
4. QA and fix outliers
5. Done

---

### Tier 3: Heavy Cleanup (Unstructured Content)

**Sites:** resmed.co.in, resmed.sg, resmed.lat, sleepsurvey.resmed.com

**Characteristics:**
- Every page is unique
- Heavy WYSIWYG abuse
- High inline CSS (40-90%)

**Mapping Effort:** 5-8x baseline (difficult)

**Process:**
1. Extract content
2. **Major cleanup:** Strip all inline styles
3. **Restructure:** Break apart WYSIWYG content into components
4. **Decide per page:** Can it map to standard template or needs custom?
5. Extensive QA
6. May need content rewrite

**Recommendation:** For these sites, consider selective migration (just critical pages) or rebuild.

---

## Next Steps

### 1. Content Model Design

**Action:** Design content model in target CMS based on this analysis

**Deliverables:**
- Content type definitions (5 types)
- Component library design (15-20 components)
- Field schemas
- Taxonomy structure

### 2. Design System Creation

**Action:** Create design system with components

**Deliverables:**
- Component designs (Figma/Sketch)
- Style guide
- Spacing/typography/color scales
- Accessibility standards

### 3. Pilot Migration (ME Site)

**Action:** Test content model with best site (me.resmed.com)

**Process:**
1. Extract ME site content
2. Map to new content model
3. Build templates
4. Test component library
5. Measure effort
6. Refine process

### 4. Develop Migration Toolkit

**Action:** Build tools for content extraction and transformation

**Tools:**
- WordPress content extractor
- HubSpot API client
- Content cleanup scripts (strip inline CSS)
- Content mapper (old structure → new structure)
- Asset migration tool

### 5. Create Content Governance

**Action:** Establish rules for content authoring in new CMS

**Deliverables:**
- Style guide
- Component usage guide
- Training materials
- Author permissions
- Approval workflow

---

## Appendix: Component Examples from Analysis

### Example 1: Card Grid (resmed.com.au)

**Structure:**
```
<div class="card-grid">
  <div class="card">
    <img src="product.jpg">
    <h3>Product Name</h3>
    <p>Description...</p>
    <a href="/product">Learn More</a>
  </div>
  <!-- Repeat 2-4 times -->
</div>
```

**Map to:** Card Grid component with 3 cards

### Example 2: Hero Banner (me.resmed.com)

**Structure:**
```
<section class="hero">
  <h1>Heading</h1>
  <p>Subheading</p>
  <a href="/cta" class="button">Call to Action</a>
  <img src="hero-bg.jpg" class="hero-background">
</section>
```

**Map to:** Hero component with image background

### Example 3: FAQ Accordion (resmed.co.uk)

**Structure:**
```
<div class="component-faq">
  <div class="faq-item">
    <h3>Question?</h3>
    <div class="answer">Answer...</div>
  </div>
  <!-- Repeat 5-10 times -->
</div>
```

**Map to:** Accordion component with FAQ items

---

**End of Content Model Recommendations**
