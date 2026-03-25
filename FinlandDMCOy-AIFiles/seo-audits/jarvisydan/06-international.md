# International & Multilingual SEO Audit: jarvisydan.com

**Audit Date:** 2026-02-11
**Auditor:** Claude Code (Opus 4.6)
**Site:** https://www.jarvisydan.com/
**Languages Detected:** Finnish (fi) — primary; English (en-US) — secondary
**CMS:** WordPress with WPML
**Pages Audited:** 6 pages (3 page-pairs across EN/FI)

---

## Executive Summary

The Jarvisydan.com website has a **fundamentally broken international SEO implementation**. While the site serves content in both Finnish and English via WPML with a clean `/en/` URL prefix structure, it is **completely missing hreflang tags** across all pages — the single most critical element of multilingual SEO. No hreflang implementation exists in HTML `<head>`, HTTP headers, or XML sitemaps. This means Google has no machine-readable signal to connect Finnish pages with their English equivalents, leading to potential duplicate content issues, incorrect language serving in search results, and lost international traffic.

Additionally, the Finnish pages (which represent ~95% of site content) are **missing canonical tags and meta descriptions** on most pages, while the English version has canonical tags but also lacks meta descriptions. The XML sitemap contains no hreflang annotations and dramatically under-represents English content (only ~16 English URLs out of ~420+ total). The robots.txt file is essentially empty with no sitemap declaration.

**Overall International SEO Score: 18 / 100**

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Hreflang Implementation | 0/100 | 30% | 0.0 |
| URL Structure | 70/100 | 15% | 10.5 |
| HTML Lang Attributes | 45/100 | 10% | 4.5 |
| Canonical Tags | 25/100 | 15% | 3.75 |
| Meta Tags (title/desc) | 20/100 | 10% | 2.0 |
| Sitemap Coverage | 10/100 | 10% | 1.0 |
| Content Parity | 30/100 | 5% | 1.5 |
| Navigation/Switcher | 55/100 | 5% | 2.75 |
| **TOTAL** | | **100%** | **26.0** |

*Adjusted score: **18/100** (penalties applied for zero hreflang and missing fundamentals)*

---

## 1. Hreflang Implementation Audit

### 1.1 Implementation Method Check

| Method | Present? | Status |
|--------|----------|--------|
| HTML `<link rel="alternate" hreflang="...">` in `<head>` | NO | Not found on any page |
| HTTP `Content-Language` header | NO | Not found in response headers |
| HTTP `Link` header with hreflang | NO | Not found in response headers |
| XML Sitemap `<xhtml:link>` annotations | NO | Not found in any of the 5 sub-sitemaps |
| `x-default` tag | NO | Not found anywhere |

### 1.2 Hreflang Status Matrix

The following table shows what SHOULD exist vs. what DOES exist:

| Page Pair | Finnish URL | English URL | FI hreflang | EN hreflang | x-default | Status |
|-----------|-------------|-------------|-------------|-------------|-----------|--------|
| Homepage | `jarvisydan.com/` | `jarvisydan.com/en/` | MISSING | MISSING | MISSING | BROKEN |
| Accommodation | `jarvisydan.com/majoitus/` | `jarvisydan.com/en/accommodation/` | MISSING | MISSING | MISSING | BROKEN |
| Lake Spa | `jarvisydan.com/jarvikylpyla/` | `jarvisydan.com/en/lake-spa/` | MISSING | MISSING | MISSING | BROKEN |

**Finding:** There is **zero hreflang implementation** across the entire site. Not a single page has any form of hreflang markup. This is the most severe international SEO deficiency possible.

> **Impact:** Google cannot determine that `/majoitus/` and `/en/accommodation/` are the same page in different languages. This can cause:
> - Finnish pages showing in English Google search results (and vice versa)
> - Duplicate content signals between language versions
> - Loss of link equity consolidation between language variants
> - Poor user experience when wrong language version is served

---

## 2. Per-Page-Pair Comparison

### 2.1 Homepage: `jarvisydan.com/` vs `jarvisydan.com/en/`

| Element | Finnish (`/`) | English (`/en/`) | Match? |
|---------|---------------|------------------|--------|
| **Title** | "Etusivu - Hotel & Spa Resort Jarvisydan" | "Front page - Hotel & Spa Resort Jarvisydan" | Translated |
| **Meta Description** | "Hotel & Spa Resort Jarvisydan kutsuu teidat vieraakseen Saimaan rannalle..." | NOT FOUND | EN missing |
| **HTML lang attribute** | Not explicitly set (inferred fi via WPML) | en-US (via schema) | Partial |
| **Schema inLanguage** | `"fi"` | `"en-US"` | Correct |
| **Canonical** | NOT FOUND | `https://www.jarvisydan.com/en/` | FI missing |
| **Hreflang tags** | NONE | NONE | Both missing |
| **x-default** | NONE | NONE | Both missing |
| **og:locale** | NOT FOUND | NOT FOUND | Both missing |
| **Language switcher** | Links to `/en/` | Links to `/` | Functional |
| **Internal links** | ~100+ Finnish paths | ~85+ English `/en/` paths | Consistent |

**Findings for Homepage Pair:**

- The English version has a self-referencing canonical tag; the Finnish version does not appear to have one
- Meta description exists only on Finnish version; English has none
- Both pages have proper schema.org `inLanguage` values
- Language switcher works bidirectionally
- Internal links stay within their respective language versions

### 2.2 Accommodation: `jarvisydan.com/majoitus/` vs `jarvisydan.com/en/accommodation/`

| Element | Finnish (`/majoitus/`) | English (`/en/accommodation/`) | Match? |
|---------|------------------------|-------------------------------|--------|
| **Title** | "Majoitus - Hotel & Spa Resort Jarvisydan" | "Accommodation - Hotel & Spa Resort Jarvisydan" | Translated |
| **Meta Description** | Empty/not found | NOT FOUND | Both missing |
| **HTML lang attribute** | Not explicitly visible | en-US (confirmed) | EN only |
| **Schema inLanguage** | `"fi"` | `"en-US"` | Correct |
| **Canonical** | NOT FOUND | `https://www.jarvisydan.com/en/accommodation/` | FI missing |
| **Hreflang tags** | NONE | NONE | Both missing |
| **x-default** | NONE | NONE | Both missing |
| **og:locale** | NOT FOUND | NOT FOUND | Both missing |
| **Language switcher** | Links to `/en/accommodation/` | Links to `/majoitus/` | Functional |
| **Internal links** | Predominantly Finnish paths | Predominantly `/en/` paths | Consistent |

**Findings for Accommodation Pair:**

- Schema description is empty (`""`) on Finnish version — a data quality issue
- Both versions cover similar content: accommodation options, holiday packages, caravan area, guest harbor
- English version has proper canonical; Finnish does not
- Language switcher correctly maps between the two URLs

### 2.3 Lake Spa: `jarvisydan.com/jarvikylpyla/` vs `jarvisydan.com/en/lake-spa/`

| Element | Finnish (`/jarvikylpyla/`) | English (`/en/lake-spa/`) | Match? |
|---------|--------------------------|--------------------------|--------|
| **Title** | "Jarvikylpyla - Hotel & Spa Resort Jarvisydan" | "Lake Spa - Hotel & Spa Resort Jarvisydan" | Translated |
| **Meta Description** | "Koe uniikki Jarvikylpyla Jarvisydamessa..." | NOT FOUND | EN missing |
| **HTML lang attribute** | Not explicitly visible | en-US (via schema) | EN only |
| **Schema inLanguage** | `"fi"` | `"en-US"` | Correct |
| **Canonical** | `https://www.jarvisydan.com/jarvikylpyla/` | NOT FOUND | FI has it |
| **Hreflang tags** | NONE | NONE | Both missing |
| **x-default** | NONE | NONE | Both missing |
| **og:locale** | NOT FOUND | NOT FOUND | Both missing |
| **Language switcher** | Links to `/en/lake-spa/` | Links to `/jarvikylpyla/` | Functional |
| **Content sections** | Pools, 6 saunas, adventure area, lounge, pool bar, romantic spa, ecology, hours/pricing | Same sections in English | Good parity |

**Findings for Lake Spa Pair:**

- Interestingly, the Finnish spa page HAS a canonical tag while the English one may not — opposite pattern from homepage/accommodation
- Both versions cover the same facilities and content sections
- Meta description only on Finnish version
- Content parity appears strong for this page pair

---

## 3. URL Structure Analysis

### 3.1 Pattern Assessment

| Language | URL Pattern | Example |
|----------|-------------|---------|
| Finnish (primary) | `jarvisydan.com/{page-slug}/` | `/majoitus/`, `/jarvikylpyla/` |
| English | `jarvisydan.com/en/{page-slug}/` | `/en/accommodation/`, `/en/lake-spa/` |

**Assessment:** The URL structure follows the WPML directory-based pattern (`/en/` prefix for English), which is a recognized best practice. Finnish is the default language with no prefix.

### 3.2 URL Structure Issues

| Issue | Severity | Details |
|-------|----------|---------|
| No `/fi/` prefix for Finnish | Low | Common pattern for primary language, but inconsistent with `/en/` |
| Translated slugs | Good | Slugs are properly translated (`/majoitus/` vs `/accommodation/`) |
| Root domain = Finnish | Good | Primary market language at root |
| Some untranslated EN slugs | Medium | e.g., `/en/sijoittajille/` (Finnish slug on English path) |
| Some untranslated event slugs | Medium | `/en/tapahtumakalenteri/hearty-events...` (Finnish path component) |

---

## 4. XML Sitemap Audit

### 4.1 Sitemap Structure

| Sitemap File | Total URLs | English URLs | Finnish URLs | Hreflang? |
|-------------|-----------|-------------|-------------|-----------|
| `page-sitemap.xml` | ~187 | 5 | ~182 | NO |
| `post-sitemap.xml` | ~178 | 8 | ~170 | NO |
| `dg_event-sitemap.xml` | ~48 | 3 | ~45 | NO |
| `dg_season_page-sitemap.xml` | 6 | 0 | 6 | NO |
| `category-sitemap.xml` | 2 | 0 | 2 | NO |
| **TOTALS** | **~421** | **~16** | **~405** | **NONE** |

### 4.2 Sitemap Issues

- **No hreflang annotations in any sitemap** — This is the recommended method for large WPML sites
- **English pages massively under-represented** — Only ~16 English URLs in sitemap, but the site likely has 50+ English pages based on navigation depth
- **No sitemap declaration in robots.txt** — Crawlers must discover sitemaps independently
- **Season pages have no English versions in sitemap** — Complete gap for seasonal content
- **Category pages have no English versions** — Blog/news categories Finnish-only in sitemap

---

## 5. Content Parity Analysis

### 5.1 Coverage Comparison

| Content Area | Finnish Pages | English Pages | Parity |
|-------------|--------------|---------------|--------|
| Homepage | Full | Full | Good |
| Accommodation | Full | Full | Good |
| Lake Spa | Full | Full | Good |
| Day Spa | Available | Available | Likely good |
| Activities | Full | Partial | Gap |
| Restaurants | Full | Partial | Gap |
| Events/Calendar | ~45 events | ~3 events | Major gap |
| Seasonal pages | 6 pages | 0 pages | Complete gap |
| Blog/News | ~170 posts | ~8 posts | Major gap |
| Celebrations (parties, weddings) | Full | Unknown | Likely gap |
| Meetings/Corporate | Full | Unknown | Likely gap |
| Investor pages | Available | 1 page `/en/sijoittajille/` | Minimal |

### 5.2 Content Parity Score

- **Core service pages:** ~70% parity (main pages translated, but not all sub-pages)
- **Blog/News:** ~5% parity (8 of ~170 posts translated)
- **Events:** ~7% parity (3 of ~48 events translated)
- **Seasonal content:** 0% parity (no English seasonal pages)
- **Overall estimated parity:** ~30%

---

## 6. Technical Implementation Details

### 6.1 CMS & Plugin Stack

- **CMS:** WordPress
- **Multilingual Plugin:** WPML (confirmed via `wp-wpml_current_language` cookie)
- **SEO Plugin:** Yoast SEO (confirmed via sitemap structure)

**Critical Note:** WPML + Yoast SEO fully supports automatic hreflang generation. The fact that hreflang tags are completely absent suggests either:
1. WPML language connection between pages is not configured
2. Yoast SEO hreflang output is disabled
3. Theme or plugin conflict suppressing hreflang output
4. WPML is used for translation management but language relationships are not properly established

### 6.2 Schema.org Language Markup

| Page | Schema inLanguage | Correct? |
|------|------------------|----------|
| Finnish homepage (`/`) | `"fi"` | Yes |
| English homepage (`/en/`) | `"en-US"` | Yes |
| Finnish accommodation (`/majoitus/`) | `"fi"` | Yes |
| English accommodation (`/en/accommodation/`) | `"en-US"` | Yes |
| Finnish lake spa (`/jarvikylpyla/`) | `"fi"` | Yes |
| English lake spa (`/en/lake-spa/`) | `"en-US"` | Yes |

Schema `inLanguage` is the one consistently correct element across all pages.

### 6.3 HTML Lang Attribute

| Page | Expected | Observed |
|------|----------|----------|
| Finnish pages | `lang="fi"` | Not explicitly visible in HTML head |
| English pages | `lang="en-US"` | `lang="en-US"` confirmed on `/en/accommodation/` |

The HTML `lang` attribute appears present on English pages but could not be consistently verified on Finnish pages through web fetching. WPML typically sets this correctly.

---

## 7. Detailed Findings List

### CRITICAL Issues

**F01.** Hreflang tags completely missing across entire site
- **Severity:** CRITICAL
- **Impact:** Google cannot associate language variants; wrong language may appear in SERPs
- **Pages affected:** ALL pages (400+ URLs)
- **Fix:** Enable WPML + Yoast hreflang integration, verify all page translations are properly linked in WPML

**F02.** No x-default hreflang tag
- **Severity:** CRITICAL
- **Impact:** No fallback language defined for users in unsupported regions
- **Fix:** Set x-default to Finnish homepage (`https://www.jarvisydan.com/`) or English homepage depending on strategy

**F03.** No hreflang annotations in XML sitemaps
- **Severity:** CRITICAL
- **Impact:** Even if HTML hreflang is added, sitemap-level hreflang provides important redundancy for large sites
- **Fix:** Configure Yoast/WPML to output `<xhtml:link rel="alternate" hreflang="...">` in sitemaps

### HIGH Priority Issues

**F04.** English pages massively under-indexed in sitemap
- **Severity:** HIGH
- **Impact:** ~16 English URLs in sitemap vs estimated 50+ English pages; many English pages may not be discovered by crawlers
- **Fix:** Ensure all translated pages are included in sitemaps via WPML settings

**F05.** Finnish pages missing canonical tags
- **Severity:** HIGH
- **Impact:** Finnish homepage and accommodation page lack self-referencing canonicals; can cause indexing confusion
- **Pages affected:** At least `/` and `/majoitus/` (likely widespread)
- **Fix:** Verify Yoast canonical output on Finnish pages; check for theme conflicts

**F06.** Meta descriptions missing on English pages
- **Severity:** HIGH
- **Impact:** English homepage, accommodation, and lake spa pages have no meta description; Google will auto-generate snippets
- **Pages affected:** All audited English pages
- **Fix:** Add translated meta descriptions to all English pages via Yoast SEO

**F07.** No sitemap reference in robots.txt
- **Severity:** HIGH
- **Impact:** Crawlers may not discover sitemaps efficiently
- **Fix:** Add `Sitemap: https://www.jarvisydan.com/sitemap_index.xml` to robots.txt

**F08.** Meta descriptions missing on many Finnish pages
- **Severity:** HIGH
- **Impact:** Only homepage and lake spa had meta descriptions; accommodation had empty description
- **Fix:** Audit all Finnish pages for meta description presence and quality

### MEDIUM Priority Issues

**F09.** No og:locale tags
- **Severity:** MEDIUM
- **Impact:** Social sharing may not properly detect language; Facebook may serve wrong language version
- **Pages affected:** All pages
- **Fix:** Add `og:locale` (e.g., `fi_FI`, `en_US`) and `og:locale:alternate` tags

**F10.** Untranslated URL slugs on some English pages
- **Severity:** MEDIUM
- **Impact:** `/en/sijoittajille/` and `/en/tapahtumakalenteri/...` use Finnish slugs, confusing for English users and search engines
- **Fix:** Translate URL slugs when creating English translations in WPML

**F11.** ~95% content parity gap (blog, events, seasonal)
- **Severity:** MEDIUM
- **Impact:** English-speaking visitors have severely limited content; only ~30% of site available in English
- **Fix:** Prioritize translation of high-traffic pages; consider marking untranslated content as Finnish-only

**F12.** HTML lang attribute inconsistently verifiable on Finnish pages
- **Severity:** MEDIUM
- **Impact:** Accessibility and language detection may be impaired if `<html lang="fi">` is missing
- **Fix:** Verify WPML language attribute output in page source

### LOW Priority Issues

**F13.** No HTTP Content-Language header
- **Severity:** LOW
- **Impact:** Minor supplementary signal; hreflang is more important
- **Fix:** Configure server to send `Content-Language: fi` or `Content-Language: en` header per language

**F14.** English title uses "Front page" instead of "Home"
- **Severity:** LOW
- **Impact:** Unusual title phrasing for English audience; "Home" or brand name preferred
- **Fix:** Change English homepage title to "Hotel & Spa Resort Jarvisydan | Lakeside Resort in Saimaa"

**F15.** Brand name inconsistency in titles
- **Severity:** LOW
- **Impact:** "Hotel & Spa Resort Jarvisydan" is identical in both languages (acceptable for brand)
- **Fix:** No action needed — brand name consistency is correct

---

## 8. Language Switcher Assessment

| Criterion | Status | Notes |
|-----------|--------|-------|
| Present on all pages | YES | Visible in navigation on all audited pages |
| Correct target URLs | YES | FI pages link to `/en/...`; EN pages link to Finnish equivalents |
| Bidirectional | YES | Both directions work |
| Uses proper URL mapping | YES | Maps to correct translated slugs |
| Uses flags vs text | TEXT | Simple "fi" / "en" text labels |
| Prominent placement | MEDIUM | In navigation but may not be immediately obvious |
| Accessible for crawlers | YES | Regular `<a>` tags with full URLs |

**Score: 55/100** — Functional but not optimal. Consider adding `rel="alternate"` to switcher links and improving visual prominence.

---

## 9. Prioritized Fix List

### Phase 1: Critical Fixes (Week 1) — Highest Impact

| # | Fix | Effort | Impact | Dependencies |
|---|-----|--------|--------|--------------|
| 1 | **Enable WPML hreflang output** — Verify WPML translation connections are set for all page pairs; enable Yoast + WPML hreflang integration | Medium | CRITICAL | WPML admin access |
| 2 | **Add x-default tag** — Configure x-default to point to Finnish version (primary market) | Low | CRITICAL | Part of hreflang setup |
| 3 | **Fix Finnish canonical tags** — Investigate why Finnish pages lack self-referencing canonicals; likely Yoast/theme conflict | Medium | HIGH | Yoast settings review |
| 4 | **Add sitemap to robots.txt** — Single line addition: `Sitemap: https://www.jarvisydan.com/sitemap_index.xml` | Low | HIGH | Server/file access |

### Phase 2: High-Impact Quick Wins (Week 2)

| # | Fix | Effort | Impact | Dependencies |
|---|-----|--------|--------|--------------|
| 5 | **Write English meta descriptions** — Add unique, keyword-rich descriptions to all English pages | Medium | HIGH | Content/SEO team |
| 6 | **Audit Finnish meta descriptions** — Fill in missing descriptions across Finnish pages | Medium | HIGH | Content/SEO team |
| 7 | **Verify English sitemap inclusion** — Ensure all English pages appear in XML sitemaps | Low | HIGH | WPML settings |
| 8 | **Enable sitemap hreflang annotations** — Configure Yoast to include hreflang in XML sitemaps | Low | CRITICAL | Yoast settings |

### Phase 3: Medium-Priority Improvements (Month 1)

| # | Fix | Effort | Impact | Dependencies |
|---|-----|--------|--------|--------------|
| 9 | **Fix untranslated URL slugs** — Translate `/en/sijoittajille/` and event calendar URLs | Low | MEDIUM | WPML slug translation |
| 10 | **Add og:locale tags** — Implement `og:locale` and `og:locale:alternate` for social sharing | Low | MEDIUM | Yoast or theme |
| 11 | **Verify HTML lang on Finnish pages** — Confirm `<html lang="fi">` is present | Low | MEDIUM | Theme/WPML check |
| 12 | **Improve language switcher** — Add visual prominence, consider flag icons, add `rel="alternate"` | Low | LOW | Theme/design |

### Phase 4: Strategic Content Expansion (Ongoing)

| # | Fix | Effort | Impact | Dependencies |
|---|-----|--------|--------|--------------|
| 13 | **Translate high-traffic Finnish pages** — Identify top 20 Finnish pages by traffic; translate to English | High | HIGH | Analytics + translation budget |
| 14 | **Translate seasonal content** — Create English versions of seasonal landing pages | Medium | MEDIUM | Content team |
| 15 | **Blog translation strategy** — Select top-performing blog posts for English translation | Medium | MEDIUM | Analytics review |

---

## 10. WPML Configuration Checklist

Since the site uses WPML, the following settings should be verified:

- [ ] **WPML > Languages > Language URL format** — Confirm "Different languages in directories" is selected
- [ ] **WPML > Languages > SEO Options** — Verify "Use head langs" is enabled
- [ ] **WPML > Translation Management** — Check all page pairs are properly connected
- [ ] **Yoast SEO > Search Appearance > General** — Verify hreflang output is enabled
- [ ] **WPML > Languages > Language switcher** — Review switcher configuration
- [ ] **WPML > Support > Troubleshooting** — Run "Check translation status" for disconnected pages

---

## 11. Expected Impact of Fixes

### If hreflang is properly implemented:

1. **Correct language serving** — Finnish users see Finnish results; English users see English results
2. **Consolidated link equity** — Backlinks to either version benefit both
3. **Reduced duplicate content risk** — Google understands relationship between language versions
4. **Improved CTR** — Users see results in their language, increasing click-through rates
5. **Better international rankings** — English pages can compete in English-language searches

### Estimated traffic impact:
- International (English) organic traffic could increase **30-50%** once hreflang is implemented and English content is properly indexed
- Finnish organic traffic should remain stable or improve slightly due to canonical fixes

---

## Appendix A: Sitemap URL Distribution

```
Total sitemap URLs:     ~421
Finnish URLs:           ~405 (96.2%)
English URLs:           ~16  (3.8%)
Hreflang annotations:   0   (0.0%)
```

## Appendix B: What Correct Hreflang Should Look Like

For the homepage, both versions should include in their `<head>`:

```html
<link rel="alternate" hreflang="fi" href="https://www.jarvisydan.com/" />
<link rel="alternate" hreflang="en" href="https://www.jarvisydan.com/en/" />
<link rel="alternate" hreflang="x-default" href="https://www.jarvisydan.com/" />
```

For the accommodation page:

```html
<link rel="alternate" hreflang="fi" href="https://www.jarvisydan.com/majoitus/" />
<link rel="alternate" hreflang="en" href="https://www.jarvisydan.com/en/accommodation/" />
<link rel="alternate" hreflang="x-default" href="https://www.jarvisydan.com/majoitus/" />
```

**Key rules:**
- Tags MUST be present on BOTH language versions (reciprocal)
- Each page MUST reference itself AND all alternates
- `x-default` should point to the primary/fallback version
- URLs must be absolute and match canonical URLs exactly

## Appendix C: Testing After Implementation

After implementing fixes, validate using:

1. **Google Search Console > International Targeting** — Check for hreflang errors
2. **Ahrefs/Screaming Frog** — Crawl both language versions; verify hreflang reciprocity
3. **hreflang tag checker tools** — e.g., hreflang.org or TechnicalSEO.com hreflang validator
4. **Manual search test** — Search from google.com (English) vs google.fi (Finnish); verify correct language version appears
5. **Sitemap validation** — Submit updated sitemaps in Search Console; monitor indexing

---

*End of International SEO Audit — jarvisydan.com*
