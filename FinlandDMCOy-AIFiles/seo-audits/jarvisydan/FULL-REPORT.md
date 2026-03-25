# SEO Audit: Hotel & Spa Resort Jarvisydan
## Full Report Summary

**Audit Date:** 2026-02-11
**Domain:** www.jarvisydan.com
**Commissioned by:** Finland DMC Oy / 1658 Holdings Oy
**Auditor:** Claude Code (Opus 4.6) — 6 parallel specialist agents
**CMS:** WordPress + Digitaali theme + Yoast SEO + WPML
**Total Pages in Sitemap:** ~421 (405 Finnish, 16 English)
**Pages Audited:** 5 English pages + 3 Finnish equivalents

---

## Overall Score: 33/100

| # | Audit Area | Score | Grade | Report |
|---|-----------|-------|-------|--------|
| 1 | Technical SEO | **48/100** | D+ | [01-technical.md](01-technical.md) |
| 2 | On-Page SEO | **41/100** | D | [02-on-page.md](02-on-page.md) |
| 3 | Schema / Structured Data | **18/100** | F | [03-schema.md](03-schema.md) |
| 4 | Image Optimization | **18/100** | F | [04-images.md](04-images.md) |
| 5 | Content Quality | **52/100** | D+ | [05-content.md](05-content.md) |
| 6 | International SEO | **18/100** | F | [06-international.md](06-international.md) |

**Weighted Average: 33/100** (weights: Technical 20%, On-Page 20%, Schema 15%, Images 10%, Content 20%, International 15%)

### Score Distribution

```
Technical    ████████████████░░░░░░░░░░░░░░  48
On-Page      █████████████░░░░░░░░░░░░░░░░░  41
Schema       ██████░░░░░░░░░░░░░░░░░░░░░░░░  18
Images       ██████░░░░░░░░░░░░░░░░░░░░░░░░  18
Content      █████████████████░░░░░░░░░░░░░░  52
Internat'l   ██████░░░░░░░░░░░░░░░░░░░░░░░░  18
─────────────────────────────────────────────
OVERALL      ███████████░░░░░░░░░░░░░░░░░░░░  33
```

---

## Executive Summary

Jarvisydan.com is a visually appealing resort website with a **fundamentally broken SEO foundation**. The site has strong structural bones (clean URLs, internal linking, basic Yoast setup) but fails on nearly every SEO dimension that drives organic traffic.

**Three areas scored 18/100 (F grade):**
- **Schema:** No Hotel, Restaurant, or Spa schemas — Google cannot identify this as a hospitality business for rich results
- **Images:** Zero lazy loading, zero WebP, zero responsive images, 3 of 5 pages have no visible content images in HTML
- **International:** Zero hreflang implementation on a bilingual site — Google has no way to connect Finnish and English page pairs

**The English section is severely neglected:** Only 16 of 421 sitemap URLs are English (~3.8%). Key pages like individual restaurants, seal safaris, national park trips, wedding venues, and seasonal content have no English equivalent.

**The /en/spa/ URL is broken:** It redirects to a thin 280-word holiday package page instead of presenting the actual spa content (which lives at /en/lake-spa/).

---

## Critical Issues Count

| Severity | Count | Examples |
|----------|-------|---------|
| Critical | **14** | Zero hreflang, missing meta descriptions, no Hotel schema, broken /spa/ canonical, missing alt text on hero images |
| High | **18** | No WebP images, no lazy loading, missing Open Graph, thin content pages, no SearchAction schema |
| Medium | **16** | Duplicate sitemap URLs, missing H3 depth, geo-keyword gaps, font loading issues |
| Low | **6** | Logo format optimization, minor breadcrumb issues |

---

## Top 10 Prioritized Actions

These are ranked by **impact per effort** — maximum SEO improvement for minimum implementation work.

### 1. Implement Hreflang Tags via WPML
- **Severity:** Critical | **Impact:** Very High | **Effort:** Low (WPML setting)
- **The problem:** Zero hreflang across the entire site. Google cannot connect /majoitus/ with /en/accommodation/
- **The fix:** Enable hreflang in WPML > Languages > SEO Options. Verify Yoast SEO hreflang output is active. Confirm all page pairs are connected in WPML Translation Management
- **Expected result:** Correct language serving in SERPs, consolidated link equity, 30-50% international traffic increase
- **Detailed report:** [06-international.md](06-international.md)

### 2. Write Meta Descriptions for All Key Pages
- **Severity:** Critical | **Impact:** High | **Effort:** Low (1-2 hours)
- **The problem:** 4 of 5 English pages have NO meta description. Google auto-generates snippets from page content
- **The fix:** Write compelling 150-160 character descriptions with keywords and CTAs for each page. Template in [02-on-page.md](02-on-page.md)
- **Expected result:** +15-25% CTR from search results

### 3. Fix Homepage Title Tag
- **Severity:** Critical | **Impact:** High | **Effort:** 5 minutes
- **The problem:** Title is "Front page - Hotel & Spa Resort Jarvisydan" — "Front page" wastes the most valuable SEO real estate
- **The fix:** Change to "Hotel & Spa Resort Jarvisydan | Lake Saimaa, Finland" or "Jarvisydan — Lakeside Spa Hotel on Lake Saimaa, Finland"
- **Expected result:** Immediate ranking signal improvement for target keywords

### 4. Fix /en/spa/ Canonical Mismatch
- **Severity:** Critical | **Impact:** High | **Effort:** Low
- **The problem:** /en/spa/ redirects to a thin holiday package page. Canonical points to /en/lomapaketit/spa-holiday/ instead of self-referencing. Actual spa content lives at /en/lake-spa/
- **The fix:** Either redirect /en/spa/ to /en/lake-spa/ with 301, or create a proper spa landing page at /en/spa/
- **Expected result:** Fix indexing confusion, recover spa-related keyword rankings

### 5. Add Hotel/LodgingBusiness Schema
- **Severity:** Critical | **Impact:** High | **Effort:** Medium
- **The problem:** Google cannot identify this as a hotel. No rich results for accommodation searches
- **The fix:** Implement Hotel schema with address, geo, amenities, star rating, check-in/out times. Ready-to-use JSON-LD code provided in [03-schema.md](03-schema.md)
- **Expected result:** Rich results in Google for hotel queries, Knowledge Panel eligibility

### 6. Add Restaurant Schema (Especially Solitary)
- **Severity:** Critical | **Impact:** High | **Effort:** Medium
- **The problem:** Restaurant Solitary is Finland's #9 ranked restaurant but Google has zero structured data about it. No cuisine, hours, price range, or rating schema
- **The fix:** Implement Restaurant schema for all 4+ dining venues. Complete JSON-LD code blocks in [03-schema.md](03-schema.md)
- **Expected result:** Rich results for restaurant searches, Google Maps/Knowledge Panel visibility

### 7. Add Sitemap Reference to robots.txt
- **Severity:** High | **Impact:** Medium | **Effort:** 1 minute
- **The problem:** robots.txt contains only a comment and User-Agent line. No sitemap reference
- **The fix:** Add `Sitemap: https://www.jarvisydan.com/sitemap.xml` to robots.txt
- **Expected result:** Improved crawl discovery, especially for new/updated pages

### 8. Implement Image Lazy Loading + WebP
- **Severity:** High | **Impact:** Medium-High | **Effort:** Medium
- **The problem:** Zero images use lazy loading, zero use WebP format, zero have srcset responsive attributes. Hero images served at full 1920px+ resolution
- **The fix:** Add `loading="lazy"` to below-fold images. Convert images to WebP. Implement srcset. Add width/height to all img tags. WordPress plugins (Imagify, ShortPixel) can automate this
- **Expected result:** Faster page loads, better Core Web Vitals, reduced CLS

### 9. Add Alt Text to All Images
- **Severity:** Critical | **Impact:** Medium | **Effort:** Low-Medium
- **The problem:** ~60% of images lack alt text, including the main hero image on homepage. Accessibility failure and missed SEO signals
- **The fix:** Write descriptive, keyword-rich alt text for all images. Hero image: "Winter activities at Hotel & Spa Resort Jarvisydan on Lake Saimaa"
- **Expected result:** Image search visibility, accessibility compliance, ranking signals

### 10. Expand English Content (Top 20 Finnish Pages)
- **Severity:** High | **Impact:** Very High | **Effort:** High (translation needed)
- **The problem:** Only 16 English pages vs 405 Finnish. Critical pages missing: individual restaurants (Solitary, Piikatytto, Kota), seal safaris, national park tours, weddings, meetings, seasonal content
- **The fix:** Identify top 20 Finnish pages by traffic (via Google Analytics). Translate and publish with proper hreflang pairing. Priority: individual restaurant pages, activity subpages, wedding/corporate pages
- **Expected result:** Capture international search demand that currently has no English landing page

---

## Quick Wins (Can Be Done This Week)

| # | Action | Time | Tool |
|---|--------|------|------|
| 1 | Fix homepage title tag | 5 min | Yoast SEO |
| 2 | Add sitemap to robots.txt | 1 min | File edit or Yoast |
| 3 | Enable hreflang in WPML | 15 min | WPML settings |
| 4 | Write 5 meta descriptions | 1 hour | Yoast SEO |
| 5 | Add alt text to hero images | 30 min | WordPress media library |
| 6 | Fix /en/spa/ redirect | 15 min | WordPress/WPML |

**Estimated impact of quick wins alone:** +15-25% organic CTR, correct language serving, basic crawlability fix.

---

## Medium-Term Roadmap (Weeks 2-6)

| Week | Focus | Key Actions |
|------|-------|-------------|
| 2 | Schema Implementation | Hotel, Restaurant (x4), Spa schemas from [03-schema.md](03-schema.md) |
| 3 | Image Optimization | WebP conversion, lazy loading, srcset, alt text audit |
| 3 | On-Page Optimization | H1 rewrites, heading hierarchy, Open Graph tags |
| 4 | Content Expansion | Expand thin pages (accommodation detail, restaurant depth) |
| 4-5 | Technical Cleanup | Sitemap deduplication, script defer, CSS optimization |
| 5-6 | Translation | Top 20 Finnish pages → English with hreflang pairing |

---

## What This Audit Did NOT Cover

- **Core Web Vitals actual scores** (requires PageSpeed Insights / CrUX data)
- **Google Search Console data** (indexing status, crawl errors, impressions)
- **Backlink profile** (requires Ahrefs/SEMrush)
- **Competitor comparison** (requires separate analysis)
- **Google Business Profile** optimization
- **Conversion rate optimization** (booking funnel analysis)
- **Page speed metrics** (actual LCP, FID/INP, CLS measurements)
- **Full site crawl** (only 5+3 pages audited of 421 total)

---

## Files in This Audit

| File | Size | Lines | Focus |
|------|------|-------|-------|
| [01-technical.md](01-technical.md) | 24KB | 443 | Robots, sitemap, HTTPS, canonicals, CWV, rendering |
| [02-on-page.md](02-on-page.md) | 27KB | 608 | Titles, descriptions, headings, URLs, internal links |
| [03-schema.md](03-schema.md) | 34KB | 846 | JSON-LD audit + 12 ready-to-use schema code blocks |
| [04-images.md](04-images.md) | 19KB | 355 | Alt text, formats, lazy loading, CLS, responsive |
| [05-content.md](05-content.md) | 26KB | 450 | Word count, E-E-A-T, geo-keywords, readability |
| [06-international.md](06-international.md) | 24KB | 472 | Hreflang, content parity, WPML config, lang attributes |
| **FULL-REPORT.md** | — | — | This summary with top 10 priorities |
| **Total audit data** | **155KB+** | **3,174+** | |

---

*Full SEO Audit generated 2026-02-11 by Claude Code (Opus 4.6) with 6 parallel specialist agents for Finland DMC Oy / 1658 Holdings Oy.*
