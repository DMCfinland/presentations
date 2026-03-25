# Technical SEO Audit: jarvisydan.com

**Audit Date:** 2026-02-11
**Auditor:** Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy
**Site:** https://www.jarvisydan.com/en/
**CMS:** WordPress with Digitaali custom theme
**SEO Plugin:** Yoast SEO
**Pages Analyzed:**
- Homepage: `/en/`
- Accommodation: `/en/accommodation/`
- Spa: `/en/spa/`
- Restaurants: `/en/restaurants/`

---

## Executive Summary

Hotel & Spa Resort Jarvisydan's website runs on WordPress with a custom theme (Digitaali) and Yoast SEO. The site has a solid foundation with good structured data implementation and a functional sitemap setup, but suffers from several significant technical issues that are likely impacting search performance. The most critical problems are: a nearly empty robots.txt with no sitemap reference, missing or unverifiable hreflang implementation on a bilingual site, a canonical URL mismatch on the spa page, excessive render-blocking resources, and missing image optimization attributes. The sitemap contains duplicate URLs, query-string-based URLs, and almost exclusively Finnish-language pages -- the English section of the site is severely underrepresented.

**Overall Technical SEO Score: 48/100**

| Category | Score | Status |
|----------|-------|--------|
| Crawlability & Indexation | 6/15 | Needs Work |
| URL Structure & Canonicalization | 7/15 | Needs Work |
| Page Speed & Core Web Vitals | 5/20 | Poor |
| Mobile & Rendering | 10/15 | Acceptable |
| Internationalization (hreflang) | 3/15 | Poor |
| Structured Data | 12/10 | Excellent |
| Security & Headers | 5/10 | Acceptable |

---

## 1. Crawlability & Indexation

### 1.1 Robots.txt Analysis

**URL:** https://www.jarvisydan.com/robots.txt

**Current content:**
```
# This space intentionally left blank
User-Agent: *
```

#### Findings

- **No Sitemap directive** - The robots.txt does not reference the XML sitemap. Search engines rely on this as a primary discovery mechanism.
  - Severity: **High**
  - Recommendation: Add `Sitemap: https://www.jarvisydan.com/sitemap.xml` to the robots.txt file.

- **No Disallow rules** - While intentionally open crawling is acceptable, the site exposes WordPress admin paths, search result pages, and other low-value URLs to crawlers.
  - Severity: **Medium**
  - Recommendation: Add Disallow rules for `/wp-admin/`, `/wp-includes/`, `/?s=`, `/haku/`, and query-parameter pages like `/?page_id=` and `/?p=`.

- **No crawl-delay** - Not required, but worth noting.
  - Severity: **Low** (informational)

### 1.2 XML Sitemap Analysis

**URL:** https://www.jarvisydan.com/sitemap.xml (Yoast SEO sitemap index)

**Sub-sitemaps discovered:**

| Sub-sitemap | URLs | Last Modified |
|-------------|------|---------------|
| post-sitemap.xml | ~104 unique (126 entries with duplicates) | 2026-01-30 |
| page-sitemap.xml | ~184 | 2026-02-10 |
| dg_event-sitemap.xml | ~39 unique (43 entries with duplicates) | 2026-02-09 |
| dg_season_page-sitemap.xml | 6 | 2026-01-28 |
| category-sitemap.xml | 2 | 2025-05-14 |

**Total estimated URLs: ~335 unique URLs across all sub-sitemaps**

#### Findings

- **Duplicate URLs in sitemaps** - Both the post-sitemap and event-sitemap contain duplicate entries (e.g., `/tapahtumakalenteri/jarvisydamen-bliniviikot/` appears twice).
  - Severity: **Medium**
  - Recommendation: Audit Yoast settings to prevent duplicate entries. This wastes crawl budget and signals quality issues to search engines.

- **Query-string URLs in sitemap** - The event sitemap contains URLs like `/?post_type=dg_event&p=10858` instead of clean, readable URLs. At least 20 events use this ugly format.
  - Severity: **High**
  - Recommendation: Ensure all custom post types (dg_event) have proper permalink structures. These query-string URLs are poor for SEO and user experience.

- **English pages severely underrepresented** - Of ~335 URLs in the sitemap, only approximately 10-15 are English (`/en/`) pages. The vast majority are Finnish-only. For a tourism business targeting international visitors, this is a significant gap.
  - Severity: **High**
  - Recommendation: Either create English versions of key pages and include them in the sitemap, or create a separate English sitemap. At minimum, all pages linked from the English navigation should exist in the sitemap.

- **No dedicated English sitemap** - There is no language-specific sitemap (e.g., `en-sitemap.xml`), making it harder for Google to discover and prioritize English content.
  - Severity: **Medium**
  - Recommendation: Consider configuring WPML or Yoast to generate language-specific sitemaps.

- **Page with `?page_id=` parameter in sitemap** - `https://www.jarvisydan.com/?page_id=15003` appears in the page sitemap. This is a non-canonical WordPress URL.
  - Severity: **Medium**
  - Recommendation: Ensure this page has a proper permalink and remove the query-string version from the sitemap.

---

## 2. URL Structure & Canonicalization

### 2.1 HTTPS & WWW Canonicalization

- **HTTPS:** The site serves content over HTTPS. All canonical URLs and sitemap URLs use `https://`. The WebFetch tool automatically upgrades HTTP to HTTPS, confirming HTTPS is the primary protocol.
  - Status: **Likely OK** (full redirect chain verification requires server-side curl testing)
  - Recommendation: Verify via Google Search Console that HTTP-to-HTTPS 301 redirects are in place. Also confirm non-www redirects to www.

- **WWW vs non-www:** All canonical URLs and sitemap references consistently use `www.jarvisydan.com`.
  - Status: **Consistent** in markup
  - Recommendation: Verify `https://jarvisydan.com` 301-redirects to `https://www.jarvisydan.com` at the server level.

### 2.2 Canonical Tags

| Page | Canonical URL | Self-referencing? | Issue? |
|------|---------------|-------------------|--------|
| `/en/` | `https://www.jarvisydan.com/en/` (via JSON-LD @id) | Yes | None detected |
| `/en/accommodation/` | `https://www.jarvisydan.com/en/accommodation/` | Yes | None detected |
| `/en/spa/` | `https://www.jarvisydan.com/en/lomapaketit/spa-holiday/` | **NO - MISMATCH** | **Critical** |
| `/en/restaurants/` | `https://www.jarvisydan.com/en/restaurants/` | Yes | None detected |

#### Findings

- **Canonical mismatch on /en/spa/** - The page at `/en/spa/` declares its canonical as `/en/lomapaketit/spa-holiday/`, which is a completely different URL path. This tells Google that `/en/spa/` should not be indexed and that the "real" page is elsewhere. If `/en/spa/` is the intended user-facing page, this is actively harming its rankings.
  - Severity: **Critical**
  - Recommendation: Investigate whether `/en/spa/` and `/en/lomapaketit/spa-holiday/` are meant to be the same page. If `/en/spa/` is the primary page, fix the canonical to be self-referencing. If they are different pages, remove the cross-canonical.

- **Canonical tags delivered via JSON-LD only** - The canonical URL appears to be set primarily through structured data `@id` fields rather than a standard `<link rel="canonical">` tag in the HTML head. While Google can interpret this, the explicit `<link rel="canonical">` tag is the recommended and most reliable method.
  - Severity: **Medium**
  - Recommendation: Verify that Yoast is outputting `<link rel="canonical" href="...">` in the `<head>` of each page. The JSON-LD @id should supplement, not replace, the canonical tag.

### 2.3 Trailing Slashes

- All URLs consistently use trailing slashes (`/en/accommodation/` not `/en/accommodation`).
  - Status: **Consistent and correct.**

---

## 3. Page Speed & Core Web Vitals Risk Factors

### 3.1 Render-Blocking Resources

All four pages analyzed share the same pattern of render-blocking resources:

- **Extensive inline CSS in `<head>`** - Approximately 2,000+ lines of inline CSS including WordPress global styles, theme variables, and component-specific styles are embedded directly in the HTML head. This blocks rendering until the browser parses all of it.
  - Severity: **High**
  - Recommendation: Extract critical CSS (above-the-fold styles only) for inline delivery. Move the rest to external, deferred stylesheets.

- **Multiple synchronous JavaScript files** - Several scripts load without `async` or `defer` attributes:
  - jQuery and jQuery-dependent scripts
  - Bootstrap 4 JavaScript
  - Slick carousel initialization
  - AJAX Search Lite configuration
  - Typekit font loader (has a 3-second timeout)
  - Severity: **High**
  - Recommendation: Add `defer` to all non-critical scripts. Only Google Tag Manager and analytics scripts should use `async`. jQuery can be deferred if DOM-ready handlers are properly used.

- **Google Tag Manager** (`GTM-NTXL4QP`) - Loaded with `async`, which is correct.
  - Status: **OK**

- **Matomo Analytics** - Loaded with `async`, which is correct.
  - Status: **OK**

### 3.2 Image Optimization

- **No `loading="lazy"` attributes detected** - None of the analyzed pages use native lazy loading on images. This means all images (including those below the fold) load immediately, blocking the page.
  - Severity: **High**
  - Recommendation: Add `loading="lazy"` to all images below the fold. Keep hero images as `loading="eager"` (or omit the attribute) for LCP optimization.

- **Missing explicit width/height on images** - Most images rely on CSS for sizing rather than HTML width/height attributes. This causes layout shift (CLS) as images load.
  - Severity: **High**
  - Recommendation: Add explicit `width` and `height` attributes to all `<img>` tags to reserve space and prevent Cumulative Layout Shift.

- **Oversized hero images** - The homepage hero image (`Winter-Activities-2-14.jpg`) is 1920x1282px. The spa page has an image at 2048x2560px (2.6 megapixels). These are likely several hundred KB each without proper compression.
  - Severity: **High**
  - Recommendation: Implement responsive images with `srcset` and `sizes` attributes. Serve WebP format. Target maximum 200KB for hero images. The 2048x2560 spa image should be cropped/resized to appropriate dimensions.

- **Logo SVG with 1x1px dimensions** - The site logo (`logo.svg`) has `width="1"` and `height="1"` specified in the HTML, then is scaled up via CSS. This is a CLS risk.
  - Severity: **Medium**
  - Recommendation: Set the SVG logo's width/height to its actual display dimensions.

### 3.3 JavaScript Payload

- **~12 external scripts** identified on each page, including:
  - Google Tag Manager
  - Matomo Analytics
  - Typekit Font Loading
  - jQuery (core)
  - Slick Carousel
  - Bootstrap 4
  - AJAX Search Lite (multiple instances)
  - BrightView Booking Widget (on some pages)
  - SiteOrigin Panels
  - Severity: **High**
  - Recommendation: Audit which scripts are actually needed on each page. Implement conditional loading (e.g., only load carousel JS on pages with carousels, only load booking widget on booking-relevant pages). Consider replacing jQuery dependency with vanilla JS.

### 3.4 CSS Payload

- **~8+ external/linked stylesheets** plus substantial inline CSS on each page.
  - Severity: **Medium**
  - Recommendation: Combine and minify CSS files. Use WP Rocket or similar to concatenate stylesheets and remove unused CSS. The site appears to reference WP Rocket but optimization may not be fully configured.

### 3.5 Font Loading

- **Typekit fonts loaded synchronously** with a 3-second timeout configuration. If Typekit is slow to respond, this blocks rendering for up to 3 seconds.
  - Severity: **Medium**
  - Recommendation: Consider self-hosting fonts for better performance, or use `font-display: swap` to prevent invisible text during font loading.

---

## 4. Mobile & Rendering

### 4.1 Viewport Meta Tag

- The viewport meta tag was not clearly visible in the fetched content, but the site uses Bootstrap 4 responsive framework and the structured data indicates mobile-responsive design.
  - Severity: **Medium** (needs verification)
  - Recommendation: Verify that `<meta name="viewport" content="width=device-width, initial-scale=1">` is present in the `<head>` of every page. Check Google Search Console's Mobile Usability report.

### 4.2 Responsive Framework

- Bootstrap 4 grid system detected, along with responsive navigation (mobile hamburger menu).
  - Status: **Acceptable**

### 4.3 JavaScript-Dependent Content

- Significant portions of the page appear to load or initialize via JavaScript (carousel sliders, booking widgets, Instagram feed). If search engine crawlers cannot execute JavaScript, this content may not be indexed.
  - Severity: **Medium**
  - Recommendation: Test with Google's Mobile-Friendly Test and URL Inspection tool to verify that Google can render the JavaScript-dependent content. Consider server-side rendering for critical content.

---

## 5. Internationalization (hreflang)

### 5.1 Hreflang Tags

- **No hreflang tags detected** on the homepage (`/en/`), accommodation page, or spa page. The restaurants page showed a Finnish alternative detected (`/ravintolat/`), but this was the only instance found.
  - Severity: **Critical**
  - Recommendation: Implement hreflang tags on EVERY page that has a language equivalent. At minimum:
    ```html
    <link rel="alternate" hreflang="en" href="https://www.jarvisydan.com/en/restaurants/" />
    <link rel="alternate" hreflang="fi" href="https://www.jarvisydan.com/ravintolat/" />
    <link rel="alternate" hreflang="x-default" href="https://www.jarvisydan.com/ravintolat/" />
    ```
  - This should be implemented site-wide for all bilingual pages. WPML should handle this automatically -- check WPML settings.

### 5.2 HTML lang Attribute

- The `lang` attribute on the `<html>` tag was not clearly visible in the fetched content. The structured data references `en-US` for English pages.
  - Severity: **Medium**
  - Recommendation: Verify that English pages use `<html lang="en">` and Finnish pages use `<html lang="fi">`. This is essential for accessibility and search engine language detection.

### 5.3 Language URL Structure

- English pages use `/en/` prefix: `https://www.jarvisydan.com/en/accommodation/`
- Finnish pages use root: `https://www.jarvisydan.com/majoitus/`
- This is a valid subdirectory approach and is well-supported by Google.
  - Status: **Good structure, poor implementation** (due to missing hreflang)

### 5.4 English Content Coverage

- The sitemap reveals that English pages represent only about 3-5% of all indexed URLs. For an international tourism destination, this is a significant missed opportunity.
  - Severity: **High**
  - Recommendation: Prioritize translating high-value pages (activities, booking info, seasonal pages) to English. Each English page needs proper hreflang pairing with its Finnish equivalent.

---

## 6. Structured Data

### 6.1 JSON-LD Implementation

All pages include comprehensive JSON-LD structured data powered by Yoast SEO:

| Schema Type | Present | Quality |
|-------------|---------|---------|
| WebPage | Yes | Good - includes dates, breadcrumbs |
| Organization | Yes | Good - includes social links, contact |
| BreadcrumbList | Yes | Good - proper hierarchy |
| ImageObject | Yes | Good - includes dimensions |
| WebSite | Yes | Good - includes SearchAction |

- **Social profiles linked:** Facebook, X (Twitter), Instagram, YouTube
- **Contact information:** Phone number accessible via schema
- **Search action:** Site search URL template defined
  - Status: **Excellent foundation**

#### Findings

- **Missing Hotel/LodgingBusiness schema** - For a hotel and spa resort, the site should implement `Hotel`, `LodgingBusiness`, or `Resort` schema with properties like `starRating`, `amenityFeature`, `checkinTime`, `checkoutTime`, `priceRange`, etc.
  - Severity: **Medium**
  - Recommendation: Add `Hotel` or `LodgingBusiness` schema to the homepage and accommodation pages. This can enable rich results in Google Search.

- **Missing LocalBusiness schema for restaurants** - The restaurants page should include `Restaurant` schema with menu URLs, cuisine type, opening hours, and price range.
  - Severity: **Medium**
  - Recommendation: Add `Restaurant` schema to `/en/restaurants/` and individual restaurant pages.

- **No Review/AggregateRating schema** - If the hotel has reviews, aggregate rating schema could enable star ratings in search results.
  - Severity: **Low**
  - Recommendation: If guest reviews are collected, implement `AggregateRating` schema.

---

## 7. Security & Headers

### 7.1 HTTPS

- The site serves over HTTPS with all internal references using HTTPS URLs.
  - Status: **Good**

### 7.2 Mixed Content Risk

- Multiple third-party scripts and resources are loaded. Risk of mixed content if any third-party resource serves over HTTP.
  - Severity: **Low** (needs browser DevTools verification)
  - Recommendation: Check browser console for mixed content warnings.

### 7.3 Security Headers

- HTTP security headers (Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, etc.) could not be fully verified via WebFetch.
  - Severity: **Low** (informational)
  - Recommendation: Test with securityheaders.com and implement recommended headers.

---

## 8. Title Tags

| Page | Title | Length | Issues |
|------|-------|--------|--------|
| Homepage | "Front page - Hotel & Spa Resort Jarvisydan" | 46 chars | **"Front page" is wasted keyword space** |
| Accommodation | "Accommodation - Hotel & Spa Resort Jarvisydan" | 49 chars | Acceptable |
| Spa | "NEW! 2-night Spa Holiday - Hotel & Spa Resort Jarvisydan" | 58 chars | **"NEW!" is promotional and will become stale** |
| Restaurants | "Restaurants - Hotel & Spa Resort Jarvisydan" | 46 chars | Acceptable |

#### Findings

- **Homepage title starts with "Front page"** - This is a default WordPress/Yoast title that wastes the most valuable keyword position. The title should lead with primary keywords like "Hotel & Spa Resort" or "Lakeside Resort in Saimaa".
  - Severity: **High**
  - Recommendation: Change to something like "Hotel & Spa Resort Jarvisydan | Lakeside Resort in Rantasalmi, Finland"

- **Spa page title contains "NEW!"** - Time-sensitive promotional text in title tags becomes stale and looks neglected. It also wastes keyword space.
  - Severity: **Medium**
  - Recommendation: Remove "NEW!" from the title. Use "Spa & Wellness | Hotel & Spa Resort Jarvisydan" or similar evergreen title.

---

## 9. Meta Descriptions

- Meta descriptions were not clearly visible in the fetched HTML content for any of the analyzed pages. If Yoast is configured but descriptions are empty, Google will auto-generate snippets from page content.
  - Severity: **High**
  - Recommendation: Verify in Yoast SEO settings that every page has a custom meta description. For a tourism business, compelling meta descriptions directly impact click-through rates from search results.

---

## 10. Meta Robots Tags

- No restrictive meta robots tags (noindex, nofollow) were detected on the analyzed pages.
  - Status: **OK** - pages are indexable.

---

## Summary Table: All Issues

| # | Finding | Severity | Category | Impact |
|---|---------|----------|----------|--------|
| 1 | Canonical URL mismatch on `/en/spa/` | Critical | Canonicalization | Page may not rank; signals sent to wrong URL |
| 2 | Missing hreflang tags site-wide | Critical | Internationalization | Wrong language version shown in search results |
| 3 | No sitemap reference in robots.txt | High | Crawlability | Slower sitemap discovery by search engines |
| 4 | Query-string URLs in event sitemap | High | Crawlability | Poor crawl efficiency; ugly URLs in index |
| 5 | English pages underrepresented in sitemap | High | Crawlability | English content not discoverable |
| 6 | No `loading="lazy"` on images | High | Core Web Vitals | Slow page load; poor LCP scores |
| 7 | Missing image width/height attributes | High | Core Web Vitals | Layout shift (CLS) |
| 8 | Oversized hero images (up to 2048x2560) | High | Core Web Vitals | Slow load; excessive bandwidth |
| 9 | Multiple render-blocking scripts without defer | High | Core Web Vitals | Delayed First Contentful Paint |
| 10 | Extensive inline CSS blocking render | High | Core Web Vitals | Delayed rendering |
| 11 | ~12 external scripts per page | High | Core Web Vitals | Heavy JavaScript payload |
| 12 | Homepage title starts with "Front page" | High | On-Page SEO | Wasted keyword opportunity |
| 13 | Meta descriptions not verified/possibly missing | High | On-Page SEO | Poor click-through rates |
| 14 | Duplicate URLs in sitemaps | Medium | Crawlability | Wasted crawl budget |
| 15 | `?page_id=` URL in page sitemap | Medium | Crawlability | Non-canonical URL in index |
| 16 | No Disallow rules in robots.txt | Medium | Crawlability | Low-value pages crawled |
| 17 | Canonical tags via JSON-LD only (not verified in head) | Medium | Canonicalization | Less reliable signal |
| 18 | Viewport meta tag not verified | Medium | Mobile | Mobile rendering risk |
| 19 | HTML lang attribute not verified | Medium | Internationalization | Language detection risk |
| 20 | No dedicated English sitemap | Medium | Internationalization | Poor English content discovery |
| 21 | Missing Hotel/LodgingBusiness schema | Medium | Structured Data | Missing rich result opportunities |
| 22 | Missing Restaurant schema | Medium | Structured Data | Missing rich result opportunities |
| 23 | Logo SVG with 1x1px dimensions | Medium | Core Web Vitals | Layout shift risk |
| 24 | Typekit font loading with 3s timeout | Medium | Core Web Vitals | Potential render blocking |
| 25 | Spa title contains "NEW!" (stale promotional text) | Medium | On-Page SEO | Looks neglected over time |
| 26 | JavaScript-dependent content rendering | Medium | Crawlability | Content may not be indexed |
| 27 | No Review/AggregateRating schema | Low | Structured Data | Minor missed opportunity |
| 28 | Mixed content risk from third-party scripts | Low | Security | Potential browser warnings |
| 29 | Security headers not verified | Low | Security | Informational |

---

## Priority Action Plan

### Immediate (Week 1) -- Critical & Quick Wins
1. **Fix canonical on `/en/spa/`** -- Change canonical to self-referencing or redirect to the correct URL
2. **Add Sitemap directive to robots.txt** -- One-line addition
3. **Fix homepage title** -- Remove "Front page", add keywords
4. **Verify and fix hreflang implementation** -- Check WPML settings; enable automatic hreflang output

### Short-Term (Weeks 2-3) -- High Impact
5. **Add `loading="lazy"` to all below-fold images**
6. **Add width/height attributes to all images**
7. **Implement responsive images (srcset)** for hero images; convert to WebP
8. **Add `defer` to non-critical scripts** (jQuery, Bootstrap, Slick, etc.)
9. **Fix event URLs** -- Set up proper permalinks for `dg_event` custom post type
10. **Write meta descriptions** for all key English pages
11. **Clean duplicate URLs from sitemaps**

### Medium-Term (Weeks 4-6) -- Optimization
12. **Add Hotel/LodgingBusiness and Restaurant structured data**
13. **Extract critical CSS; defer non-critical CSS**
14. **Reduce JavaScript payload** -- conditional script loading per page
15. **Self-host fonts** or implement font-display: swap
16. **Add Disallow rules to robots.txt** for admin, search, and low-value paths
17. **Expand English content** in sitemap and on-site

### Ongoing
18. **Monitor Core Web Vitals** via Google Search Console
19. **Regular sitemap audits** for duplicates and non-canonical URLs
20. **Test rendered pages** with Google URL Inspection tool

---

## Tools Recommended for Verification

The following checks could not be fully completed via remote fetch and should be verified with browser-based tools:

| Check | Tool |
|-------|------|
| HTTP-to-HTTPS redirect chain | `curl -sIL http://jarvisydan.com/en/` or redirect-checker.org |
| Non-www to www redirect | `curl -sIL https://jarvisydan.com/en/` |
| Core Web Vitals scores | PageSpeed Insights (pagespeed.web.dev) |
| Mobile usability | Google Search Console > Mobile Usability |
| Rendered page content | Google Search Console > URL Inspection > View Rendered Page |
| Security headers | securityheaders.com |
| HTML validation | validator.w3.org |
| Hreflang verification | hreflang.org or Screaming Frog |
| Full crawl analysis | Screaming Frog SEO Spider |

---

*Report generated 2026-02-11 by Claude Code (Opus 4.6) for the Finland DMC / 1658 Holdings SEO audit initiative.*
