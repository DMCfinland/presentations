# Full SEO Audit Report: jarvisydan.com

**Audit Date:** 2026-02-11
**Client:** Hotel & Spa Resort Jarvisydan (Jarvisydan Oy)
**Auditor:** Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy
**Domain:** https://www.jarvisydan.com/en/
**CMS:** WordPress with Digitaali custom theme, Yoast SEO, WPML
**Pages Audited:** 5 English pages + 3 Finnish equivalents
**Sub-audits Completed:** 7 (Technical, On-Page, Schema, Images, Content Quality, International, GEO/AI Search)

---

## SEO Health Score: 38 / 100

| Category | Weight | Score | Weighted | Source |
|----------|--------|-------|----------|--------|
| Technical SEO | 25% | 40/100 | 10.0 | 01-technical + 06-international |
| Content Quality | 25% | 52/100 | 13.0 | 05-content |
| On-Page SEO | 20% | 41/100 | 8.2 | 02-on-page |
| Schema Markup | 10% | 18/100 | 1.8 | 03-schema |
| Performance (CWV) | 10% | 25/100 | 2.5 | 01-technical (CWV section) |
| Image SEO | 5% | 18/100 | 0.9 | 04-images |
| AI Search / GEO | 5% | 34/100 | 1.7 | 07-geo-ai-search |
| **TOTAL** | **100%** | | **38.1** | |

**Rating: POOR** -- The site has a solid WordPress foundation, good internal linking, and functional navigation, but suffers from critical gaps in internationalization, schema markup, image optimization, and content depth that severely limit organic search visibility for a tourism business targeting international visitors.

### Score Methodology

- **Technical SEO (40/100):** Blended from the technical audit (48/100) and the comprehensive international audit (18/100), which confirmed zero hreflang implementation site-wide -- catastrophic for a bilingual tourism site.
- **Performance (25/100):** Derived from the Core Web Vitals risk assessment in the technical audit (5/20 scaled to 25/100). No lazy loading, no responsive images, render-blocking scripts, excessive inline CSS.
- **Content Quality (52/100):** Best-performing category. Activities page is strong (2,800 words); homepage adequate. Spa page critically thin due to redirect. Geo-keywords underused.
- **On-Page (41/100):** Meta descriptions missing on 3/5 pages. Homepage title wastes keywords. H1 tags are poetic, not optimized. Open Graph tags absent.
- **Schema (18/100):** Only generic Yoast defaults (WebPage, Organization, BreadcrumbList). Zero business-specific schemas: no Hotel, no Restaurant, no Spa, no TouristAttraction.
- **Images (18/100):** 3 of 5 pages have zero visible content images. No WebP, no srcset, no lazy loading, no alt text on hero images.
- **AI Search (34/100):** No llms.txt, no FAQ schema, no citable passages. Good server-side rendering. Finnish Wikipedia contains negative content; no English Wikipedia article exists.

---

## Executive Summary

Hotel & Spa Resort Jarvisydan operates a visually appealing bilingual WordPress website that fundamentally fails to communicate its offerings to search engines and AI systems. The resort has genuine competitive advantages -- a lakeside spa on Lake Saimaa, a nationally-ranked restaurant (Solitary, #9 in Finland), heritage dating to 1658, and proximity to Linnansaari National Park -- but these assets are invisible to search engines due to missing structured data, absent hreflang tags, thin content on key pages, and marketing-focused prose that AI systems cannot parse or cite.

### The 5 Biggest Problems

1. **Zero hreflang implementation** on a bilingual tourism site. Google cannot connect Finnish and English pages. Wrong language versions may appear in search results. Only 16 of 420+ sitemap URLs are English.

2. **No business-specific schema markup.** Google sees a generic website with an organization name. It cannot identify this as a hotel, surface restaurant information, show spa details, or display activity pricing. Schema score: 18/100.

3. **3 of 5 key pages have zero visible content images.** The spa, restaurants, and activities pages reference images only in metadata -- users see no photos. The accommodation page has only a generic `Image-282.jpg`.

4. **Critical content gaps.** The `/en/spa/` URL redirects to a thin 280-word holiday package page instead of the rich spa content at `/en/lake-spa/`. Meta descriptions missing on 3/5 pages. H1 tags use poetic taglines instead of keywords.

5. **Invisible to AI search engines.** No llms.txt, no FAQ schema, no citable passages, no English Wikipedia article. The Finnish Wikipedia article contains negative content (legionella, labor investigations, corporate restructuring) that AI systems may surface.

### What's Working Well

- Clean URL structure with `/en/` prefix for English
- Server-side rendering (all content in initial HTML -- excellent for AI crawlers)
- Functional language switcher with correct URL mapping
- Strong internal linking with descriptive anchor text
- Comprehensive activities page (2,800 words, 22 activities with pricing)
- Restaurant Solitary's "9th best in Finland" ranking -- powerful E-E-A-T signal
- Green Key certification displayed
- 1658 heritage claim -- unique differentiator
- Yoast SEO + WPML stack supports all needed fixes (no new tools needed)
- HTTPS throughout, consistent www canonicalization
- All AI crawlers allowed (robots.txt has no blocks)
- Wikidata entity exists (Q112112665) with 16 properties

---

## Detailed Findings by Category

### 1. Technical SEO (40/100)

**Full report:** [01-technical.md](01-technical.md) | **International detail:** [06-international.md](06-international.md)

#### Crawlability & Indexation (6/15)

| Issue | Severity | Detail |
|-------|----------|--------|
| robots.txt has no Sitemap directive | High | Nearly empty file: just `User-Agent: *` |
| Query-string URLs in event sitemap | High | `/?post_type=dg_event&p=10858` format -- 20+ events |
| English pages: 16 of 420+ in sitemap (3.8%) | High | English content largely undiscoverable |
| Duplicate URLs in sitemaps | Medium | post-sitemap and event-sitemap contain duplicates |
| `?page_id=` URL in page sitemap | Medium | Non-canonical WordPress URL indexed |
| No Disallow rules | Medium | wp-admin, search, query params all crawled |

#### URL Structure & Canonicalization (7/15)

| Issue | Severity | Detail |
|-------|----------|--------|
| Canonical mismatch on `/en/spa/` | **Critical** | Declares canonical as `/en/lomapaketit/spa-holiday/` -- a different page |
| Finnish pages missing canonical tags | High | Homepage and accommodation pages lack self-referencing canonicals |
| Canonical via JSON-LD only (unverified in head) | Medium | Yoast should output `<link rel="canonical">` -- needs verification |
| URL typo: `/accomodations/` | Medium | Missing 'm' in internal link |

#### Page Speed & Core Web Vitals (5/20 = 25/100)

| Issue | Severity | Detail |
|-------|----------|--------|
| ~2,000+ lines inline CSS in `<head>` | High | Blocks rendering until parsed |
| Multiple synchronous JS (jQuery, Bootstrap, Slick, etc.) | High | No `defer` or `async` attributes |
| No `loading="lazy"` on any image | High | All images load immediately |
| Missing width/height on most images | High | Cumulative Layout Shift (CLS) |
| Oversized hero images (up to 2048x2560) | High | Excessive bandwidth |
| ~12 external scripts per page | High | Heavy JS payload |
| Typekit fonts with 3-second timeout | Medium | Potential invisible text |
| Logo SVG declared as 1x1px | Medium | CLS risk |

#### Mobile & Rendering (10/15)

- Bootstrap 4 responsive framework: Acceptable
- Viewport meta tag: Not verified (needs manual check)
- JavaScript-dependent content: Some content relies on JS execution

#### Internationalization (3/15 -- confirmed 0/100 in detailed audit)

| Issue | Severity | Detail |
|-------|----------|--------|
| **Zero hreflang tags site-wide** | **Critical** | Not in HTML head, HTTP headers, or XML sitemaps |
| No x-default hreflang | **Critical** | No fallback language for unsupported regions |
| No hreflang annotations in sitemaps | **Critical** | Even after HTML fix, sitemap hreflang adds redundancy |
| English sitemap coverage: 3.8% | High | WPML not generating English sitemap entries |
| Finnish canonical tags missing | High | At least homepage and accommodation lack canonicals |
| Meta descriptions missing on English pages | High | All audited English pages lack meta descriptions |
| No og:locale tags | Medium | Social sharing language detection broken |
| Untranslated URL slugs on some EN pages | Medium | e.g., `/en/sijoittajille/` (Finnish slug) |
| ~95% content parity gap | Medium | Blog, events, seasonal content almost entirely Finnish-only |

**Root cause:** WPML is installed but hreflang output is either disabled or broken. WPML + Yoast fully supports automatic hreflang generation -- this is a configuration issue, not a tooling gap.

#### Content Parity (EN vs FI)

| Content Area | Finnish | English | Parity |
|-------------|---------|---------|--------|
| Core service pages | Full | Full | ~70% |
| Blog/News | ~170 posts | ~8 posts | 5% |
| Events | ~48 events | ~3 events | 7% |
| Seasonal content | 6 pages | 0 pages | 0% |
| **Overall URLs** | **~405** | **~16** | **~4%** |

---

### 2. Content Quality (52/100)

**Full report:** [05-content.md](05-content.md)

#### Per-Page Scores

| Page | Score | Word Count (unique) | Key Issue |
|------|-------|---------------------|-----------|
| Homepage | 61/100 | ~1,200 | H1 is poetic tagline, not keyword-optimized |
| Accommodation | 38/100 | ~600 | Critically thin; no room details, no amenities |
| Spa (/spa/ URL) | 29/100 | ~280 | Redirects to thin package page; real content at /lake-spa/ |
| Restaurants | 46/100 | ~850 | ~120 words per restaurant; no chef profiles |
| Activities | 69/100 | ~2,800 | Strongest page; 22 activities with pricing |
| **Average** | **52/100** | | |

#### Geo-Keyword Coverage

| Keyword | Total Mentions (5 pages) | Assessment |
|---------|--------------------------|------------|
| Lake Saimaa / Saimaa | 18 | Good |
| Linnansaari | 6 | Adequate (concentrated on activities) |
| Savonlinna | 5 | Underused |
| Finland | 5 | Underused |
| **Rantasalmi** | **1** (address only) | **CRITICAL GAP** |
| **Finnish Lakeland** | **1** | **CRITICAL GAP** |

#### E-E-A-T Assessment

| Signal | Status | Key Gaps |
|--------|--------|----------|
| **Experience** | Moderate | 1658 heritage mentioned once, never expanded; no guest stories |
| **Expertise** | Weak | Only 1 staff member named across 5 pages; no chef/therapist/guide profiles |
| **Authoritativeness** | Mixed | Green Key + Solitary ranking are strong; no press/tourism board mentions |
| **Trustworthiness** | Mixed | Pricing transparent; premium-rate phone (0600 = EUR 0.65/min) is a trust barrier for international tourists |

#### Critical Content Gaps

| Gap | Impact |
|-----|--------|
| No guest reviews/testimonials on any page | Severely weakens trust signals |
| No "About Us" / heritage story expansion | 1658 heritage = massive underused asset |
| No staff/team profiles | Only 1 staff named; no chef, therapist, or guide visibility |
| Spa facility page not at /spa/ URL | Primary spa queries land on thin content |
| No FAQ content on service pages | Missing FAQ schema and featured snippet opportunities |
| No "How to get here" content | Missing geographic context for international visitors |
| No seasonal content hub | Summer/winter not presented as distinct offerings |

---

### 3. On-Page SEO (41/100)

**Full report:** [02-on-page.md](02-on-page.md)

#### Per-Page Scores

| Page | Score | Critical Issues |
|------|-------|-----------------|
| Homepage | 42/100 | Title starts with "Front page", no meta description, H1 not optimized |
| Accommodation | 32/100 | No meta description, thin content, "Hearth" typo, generic image name |
| Spa (lakespa-dayspa) | 52/100 | /spa/ URL mismatch, Finnish alt text on EN page |
| Restaurants | 45/100 | No meta description, generic H1, no location keywords |
| Activities | 48/100 | Repeated phrase in meta description, generic H1, flat heading structure |

#### Title Tags

| Page | Current Title | Issue |
|------|--------------|-------|
| Homepage | "Front page - Hotel & Spa Resort Jarvisydan" | "Front page" wastes primary keyword position |
| Accommodation | "Accommodation - Hotel & Spa Resort Jarvisydan" | No location qualifier |
| Spa | "Lake Spa & Day Spa - Hotel & Spa Resort Jarvisydan" | Missing "Finland", "Saimaa" |
| Restaurants | "Restaurants - Hotel & Spa Resort Jarvisydan" | No location or differentiator |
| Activities | "Activities - Hotel & Spa Resort Jarvisydan" | No location or activity type |

**Key finding:** "Lake Saimaa" and "Finland" appear in zero title tags.

#### Meta Descriptions

| Page | Status |
|------|--------|
| Homepage | MISSING |
| Accommodation | MISSING |
| Spa (lakespa-dayspa) | Present (128 chars, no CTA) |
| Restaurants | MISSING |
| Activities | Present (147 chars, repeated phrase) |

#### Other Critical On-Page Issues

| Issue | Pages | Impact |
|-------|-------|--------|
| Open Graph tags missing entirely | All 5 | Poor social sharing previews |
| H1 tags lack target keywords | Homepage, Activities, Restaurants | Primary heading doesn't signal topic |
| H1 typo: "Hearth" should be "Heart" | Accommodation | Unprofessional |
| Duplicate H1 tags | Activities | Invalid HTML structure |
| No H3 tags on any page | All 5 | Flat heading hierarchy |
| Finnish alt text on English page | Spa | Confuses language signals |

---

### 4. Schema Markup (18/100)

**Full report:** [03-schema.md](03-schema.md) -- includes 12 ready-to-use JSON-LD code blocks

#### What Google Currently Understands

| Question | Answer |
|----------|--------|
| Is this a website? | Yes |
| Is this a hotel? | **No** |
| Does it have restaurants? | **No** |
| Does it have a spa? | **No** |
| Business address and location? | **No** |
| Business phone number? | **No** |
| Room types and prices? | **No** |
| Restaurant menus and prices? | **No** |
| Activities and experiences? | **No** |
| Breadcrumb navigation? | Yes (partial) |
| Social media profiles? | Yes |
| Site search capability? | **No** |

#### What Exists (Yoast Defaults)

| Schema | Status | Issues |
|--------|--------|--------|
| WebPage | Present on all pages | Missing `description` property on most |
| Organization | Present on all pages | Missing address, phone, geo, description, email |
| BreadcrumbList | Present on all pages | Homepage has only 1 item with no URL |
| WebSite | Present | Missing `potentialAction` (SearchAction) |
| ImageObject | Present on some pages | Basic |

#### What's Completely Missing

| Missing Schema | Business Impact | Priority |
|----------------|-----------------|----------|
| **Hotel / LodgingBusiness** | Cannot appear in hotel rich results or Google Hotels | Critical |
| **Restaurant** (6 venues incl. Solitary #9 in Finland) | Cannot surface dining info in search | Critical |
| **HealthAndBeautyBusiness** (Lake Spa) | Spa invisible to search | High |
| **TouristAttraction / TouristDestination** | Activities not machine-readable | High |
| **FAQ** | Cannot appear in featured snippets | High |
| **SearchAction** | Ineligible for sitelinks search box | High |
| **Offer** (packages with prices) | Price rich results blocked | Medium |
| **Menu** (restaurant menus with items) | Menu search features blocked | Medium |
| **ReserveAction** (table bookings) | Reservation rich results blocked | Medium |

**Implementation:** Ready-to-use JSON-LD for Hotel, Organization (enhanced), WebSite+SearchAction, 4 Restaurants, Bar, Spa, and TouristDestination with 5 TouristAttractions are provided in [03-schema.md](03-schema.md). Can be deployed via Google Tag Manager or WordPress header plugin without developer code changes.

---

### 5. Image SEO (18/100)

**Full report:** [04-images.md](04-images.md)

#### Summary Statistics

| Metric | Value |
|--------|-------|
| Total unique content images (5 pages) | 5 |
| Total unique images including nav/footer | 9 |
| Pages with zero visible content images | **3 of 5 (60%)** |
| Images with alt text | ~44% (inconsistent) |
| Images with width/height attributes | 22% |
| Images with loading="lazy" | **0%** |
| Images with srcset | **0%** |
| Images using WebP/AVIF | **0%** |
| Images using `<picture>` element | **0%** |
| Images with fetchpriority | **0%** |

#### Critical Image Issues

| Issue | Pages | Detail |
|-------|-------|--------|
| Spa, Restaurants, Activities have **zero visible content images** | 3 pages | Images exist in metadata but are not rendered in HTML body |
| Hero images missing alt text | Homepage, Accommodation, Activities | WCAG 2.1 A violation; lost SEO signals |
| No accommodation photos | Accommodation | Page has single generic `Image-282.jpg` |
| No food/dining photos | Restaurants | Restaurant page without food photos |
| No spa facility photos | Spa | Spa page without spa photos |
| Oversized metadata image (2048x2560) | Spa | Unnecessary bandwidth for crawlers |

#### WordPress Theme Issue

The Digitaali theme appears to suppress WordPress's built-in responsive image features:
- Native `loading="lazy"` (available since WP 5.5)
- Automatic `srcset` generation (available since WP 4.4)
- Responsive image handling

Investigation of theme `functions.php` needed.

---

### 6. International SEO (18/100)

**Full report:** [06-international.md](06-international.md)

#### Hreflang Implementation: ZERO

| Method | Status |
|--------|--------|
| HTML `<link rel="alternate" hreflang="...">` in `<head>` | **NOT FOUND on any page** |
| HTTP `Content-Language` header | **NOT FOUND** |
| HTTP `Link` header with hreflang | **NOT FOUND** |
| XML Sitemap `<xhtml:link>` annotations | **NOT FOUND** |
| `x-default` tag | **NOT FOUND** |

This is the most severe international SEO deficiency possible for a bilingual site. Google has no machine-readable signal to connect Finnish pages with their English equivalents.

#### What Works

- Schema `inLanguage` correctly set on all pages (`"fi"` / `"en-US"`)
- Language switcher functional and bidirectional
- Translated URL slugs (e.g., `/majoitus/` vs `/accommodation/`)
- Clean `/en/` prefix structure (Google-approved pattern)

#### WPML Configuration Checklist

Since WPML is installed but hreflang is broken, verify:
- [ ] WPML > Languages > SEO Options > "Use head langs" = enabled
- [ ] WPML > Translation Management > All page pairs properly connected
- [ ] Yoast SEO > Search Appearance > hreflang output = enabled
- [ ] WPML > Troubleshooting > "Check translation status" for disconnected pages

---

### 7. GEO / AI Search Readiness (34/100)

**Full report:** [07-geo-ai-search.md](07-geo-ai-search.md)

#### Scores by Subcategory

| Category | Score | Status |
|----------|-------|--------|
| AI Crawler Access | 5/15 | Accidentally permissive; no Sitemap directive |
| llms.txt & AI Discoverability | 0/10 | 404 Not Found |
| Passage-Level Citability | 8/25 | Marketing prose, no citable passages |
| Brand & Entity Presence | 10/20 | Wikidata exists; no English Wikipedia |
| Server-Side Rendering | 12/15 | Excellent -- all content in initial HTML |
| Platform-Specific Readiness | 7/15 | Poor across all 3 platforms |

#### Platform Readiness

| Platform | Score | Key Gap |
|----------|-------|---------|
| Google AI Overviews | 4/10 | No passage optimization, no FAQ schema, thin schema |
| ChatGPT Web Search | 3/10 | No English Wikipedia, no llms.txt, marketing prose |
| Perplexity | 3/10 | Single-source signal, no citable data tables |

#### Entity Presence

| Platform | Status |
|----------|--------|
| Wikidata | Exists (Q112112665) -- 16 properties, well-populated |
| Finnish Wikipedia | Exists -- contains significant negative content |
| English Wikipedia | **MISSING** -- major gap for English-language AI |
| Google Knowledge Panel | Likely exists (Wikidata + GMB) |
| Social profiles in schema | 4 of 5 (LinkedIn missing) |

#### Wikipedia Risk (HIGH)

The Finnish Wikipedia article contains: legionella bacteria incident (Aug 2025), police investigation into treatment of foreign workers, pattern of delayed invoice payments, EUR 9.8M in public subsidies, Siemens Financial Services restructuring filing (Jan 2026), and bankruptcy petition (Jan 2026). AI systems reading Finnish Wikipedia may surface this information.

**Defensive strategy:** Create strong positive content on own website + llms.txt + third-party coverage. Do not edit Wikipedia (violates policies).

#### Passage Citability Analysis

| Page | Citability Score | Issue |
|------|-----------------|-------|
| Homepage | 3/10 | H1 is poetic ("Stories to be saved in hearts"); first-person voice; no structured data |
| Activities | 3/10 | Descriptions 1-3 sentences each; duplicate H1; no seasonal overview |
| Restaurants | 4/10 | Solitary pricing/ranking are citable; missing attribution for ranking source |

**Key gap:** No question-based headings, no FAQ sections, no comparison tables, no 134-167 word factual passages that AI systems can cite.

---

## Cross-Cutting Themes

### 1. The WPML Configuration Gap
WPML is installed and functional (language switcher works, translated slugs work) but its SEO outputs are broken or disabled. Fixing WPML + Yoast integration would resolve: zero hreflang, missing Finnish canonicals, English sitemap under-representation, and og:locale gaps. This is likely a single settings session (~15 minutes).

### 2. The Digitaali Theme Suppression
The custom Digitaali theme appears to suppress WordPress's built-in responsive image features (srcset/sizes) and native lazy loading. Investigating `functions.php` could unlock significant image performance gains without plugin changes.

### 3. Marketing Voice vs. Search Visibility
The site prioritizes emotional, first-person marketing copy ("Stories to be saved in hearts", "We invite you") over keyword-rich, factual content that search engines and AI systems can parse. This is a fundamental content strategy tension: the emotional copy can remain, but it must be supplemented with factual, keyword-optimized elements (H1 tags, meta descriptions, schema, FAQ sections).

### 4. Content Architecture Mismatch
The site's strongest content (Lake Spa at `/en/lake-spa/`, ~3,000 words) is not at the URL users expect (`/en/spa/`). The accommodation page is thin while detailed room descriptions likely exist elsewhere. Activities is the only page where content depth matches user intent.

### 5. Schema Desert
The site uses only Yoast's auto-generated generic schemas. For a resort with 7+ bookable venue types (hotel rooms, villas, 6 restaurants, spa, 22 activities), the absence of ANY business-specific schema is the single largest missed opportunity. The [03-schema.md](03-schema.md) report provides 12 ready-to-deploy JSON-LD blocks.

---

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Wrong language served in SERPs (no hreflang) | High | High | Fix WPML hreflang immediately |
| Spa page not ranking (canonical mismatch) | High | High | Fix canonical or redirect /spa/ to /lake-spa/ |
| AI systems surfacing Finnish Wikipedia negatives | Medium | High | Deploy llms.txt + strong positive content |
| Thin pages flagged by Google quality update | Medium | Medium | Expand Accommodation to 500+ words |
| Core Web Vitals failing field test | High | Medium | Implement lazy loading, defer JS, add srcset |
| Image accessibility complaints (WCAG) | Low | Medium | Add alt text to all images |
| Social sharing producing blank previews | High | Low | Enable Open Graph tags in Yoast |

---

## Appendix: Sub-Audit Report Index

| Report | File | Score | Key Finding |
|--------|------|-------|-------------|
| Technical SEO | [01-technical.md](01-technical.md) | 48/100 | Canonical mismatch, empty robots.txt, render-blocking resources |
| On-Page SEO | [02-on-page.md](02-on-page.md) | 41/100 | 3/5 pages missing meta descriptions, H1s not optimized |
| Schema Markup | [03-schema.md](03-schema.md) | 18/100 | Zero business-specific schemas; 12 JSON-LD templates provided |
| Image SEO | [04-images.md](04-images.md) | 18/100 | 60% of pages have zero visible images; theme suppresses WP features |
| Content Quality | [05-content.md](05-content.md) | 52/100 | Spa page critically thin; geo-keywords underused; E-E-A-T gaps |
| International SEO | [06-international.md](06-international.md) | 18/100 | Zero hreflang; 96% of sitemap is Finnish-only |
| GEO / AI Search | [07-geo-ai-search.md](07-geo-ai-search.md) | 34/100 | No llms.txt; no English Wikipedia; marketing prose uncitable |

---

*Report compiled 2026-02-11 by Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy.*
*Total findings: 65+ issues across 7 audit dimensions.*
*Next step: Execute Critical items in [ACTION-PLAN.md](ACTION-PLAN.md) (estimated 2-3 hours for quick wins, score improvement to ~50+).*
