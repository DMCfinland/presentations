# SEO Action Plan: jarvisydan.com

**Generated:** 2026-02-11
**Current SEO Health Score:** 38/100
**Domain:** www.jarvisydan.com
**CMS:** WordPress + Digitaali theme + Yoast SEO + WPML
**Source:** 7 specialist audit reports (Technical, On-Page, Schema, Images, Content, International, GEO/AI)

---

## Priority Summary

| Priority | Items | Estimated Effort | Score Impact |
|----------|-------|-----------------|-------------|
| Critical | 8 items | 2-3 hours | 38 → 50 |
| High | 12 items | 1-2 weeks | 50 → 65 |
| Medium | 12 items | 2-4 weeks | 65 → 75 |
| Low | 8 items | Ongoing | 75 → 80+ |

---

## CRITICAL -- Fix Immediately (Blocks Indexing or Causes Active Harm)

### C1. Enable Hreflang Tags via WPML

**Impact:** Very High | **Effort:** 15-30 min | **Owner:** Developer/IT
**Source:** [06-international.md](06-international.md) findings F01-F03

The site has **zero hreflang implementation** across all 420+ pages. This is catastrophic for a bilingual tourism site. Google cannot connect Finnish and English page pairs.

**Actions:**
1. WPML > Languages > SEO Options > Enable "Use head langs"
2. Verify all page pairs are connected in WPML Translation Management
3. Run WPML > Support > Troubleshooting > "Check translation status"
4. Yoast SEO > Verify hreflang output is not disabled
5. Configure x-default to point to Finnish version (primary market)
6. Verify hreflang appears in XML sitemaps after enabling

**Verify:** Check page source for `<link rel="alternate" hreflang="fi" ...>` and `hreflang="en" ...>` tags in `<head>`.

---

### C2. Fix /en/spa/ Canonical Mismatch & Redirect

**Impact:** Very High | **Effort:** 10 min | **Owner:** Developer/IT
**Source:** [01-technical.md](01-technical.md) finding #1

The page at `/en/spa/` declares its canonical as `/en/lomapaketit/spa-holiday/` (a thin 280-word package page). The actual rich spa content (~3,000 words) lives at `/en/lake-spa/`.

**Actions:**
1. 301 redirect `/en/spa/` to `/en/lake-spa/` (the page with actual spa facility content)
2. Verify the canonical on `/en/lake-spa/` is self-referencing
3. Update any internal links pointing to `/en/spa/` to use `/en/lake-spa/`
4. Update navigation if spa link points to wrong URL

---

### C3. Add Sitemap Directive to robots.txt

**Impact:** High | **Effort:** 1 min | **Owner:** Developer/IT
**Source:** [01-technical.md](01-technical.md) finding #3

Current robots.txt is nearly empty. Add one line.

**Action:** Add to robots.txt:
```
Sitemap: https://www.jarvisydan.com/sitemap.xml
```

---

### C4. Fix Homepage Title Tag

**Impact:** High | **Effort:** 2 min | **Owner:** Content/Marketing
**Source:** [02-on-page.md](02-on-page.md) finding C2

**Current:** "Front page - Hotel & Spa Resort Jarvisydan"
**Change to:** "Hotel & Spa Resort Jarvisydan | Lake Saimaa, Finland"

Location: Yoast SEO > Edit Homepage > SEO title

---

### C5. Write Meta Descriptions for 3 Missing Pages

**Impact:** High | **Effort:** 20 min | **Owner:** Content/Marketing
**Source:** [02-on-page.md](02-on-page.md) finding C1

| Page | Suggested Meta Description |
|------|---------------------------|
| Homepage | "Discover Jarvisydan, a nature hotel & spa resort on Lake Saimaa, Finland. Award-winning restaurants, ecological lake spa, activities & accommodation. Book your lakeside escape." |
| Accommodation | "Choose from lakeside villas, themed suites, luxury Kuru Resort, houseboats & hotel rooms at Jarvisydan on Lake Saimaa, Finnish Lakeland. Book now." |
| Restaurants | "Six restaurants at Jarvisydan on Lake Saimaa. Restaurant Solitary (9th best in Finland), Wine Cellar Fire Kitchen, Bistro & more. Reserve your table." |

Also fix Activities meta description: remove "throughout the year" duplication.

Location: Yoast SEO > Edit each page > Meta description field

---

### C6. Add Missing Geo-Keywords Site-Wide

**Impact:** High | **Effort:** 30 min | **Owner:** Content/Marketing
**Source:** [05-content.md](05-content.md) geo-keyword matrix

"Rantasalmi" appears only 1x (footer address) and "Finnish Lakeland" appears only 1x across ALL 5 audited pages. These are primary search terms for international tourists.

**Actions:**
1. Add "in Rantasalmi, Finnish Lakeland" to the first paragraph of every English service page
2. Add "Finnish Lakeland" to at least one H2 on the homepage
3. Mention "Savonlinna (45 min)" on accommodation and activities pages
4. Add "Finland" to pages where it's currently absent (Accommodation, Spa)

---

### C7. Deploy llms.txt File

**Impact:** High | **Effort:** 30 min | **Owner:** Developer/Content
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md) Section 2

No `/llms.txt` exists (404). A ready-to-use llms.txt with full property information (accommodation types, 7 restaurants with pricing, spa facilities, activities with prices, location details) is provided in [07-geo-ai-search.md](07-geo-ai-search.md) Section 2.

**Action:** Create `/llms.txt` as a static text file at the root domain using the recommended content.

---

### C8. Fix Finnish Canonical Tags

**Impact:** High | **Effort:** 15 min | **Owner:** Developer/IT
**Source:** [06-international.md](06-international.md) finding F05

Finnish homepage (`/`) and accommodation page (`/majoitus/`) are missing self-referencing canonical tags while English equivalents have them. Likely a Yoast/theme conflict.

**Action:** Check Yoast SEO canonical output on Finnish pages. If theme is overriding, fix in `functions.php`.

---

## HIGH -- Fix Within 1-2 Weeks (Significantly Impacts Rankings & Visibility)

### H1. Implement Hotel/LodgingBusiness Schema

**Impact:** Very High | **Effort:** 1-2 hours | **Owner:** Developer
**Source:** [03-schema.md](03-schema.md) -- ready-to-use JSON-LD provided

Google cannot identify this website as representing a hotel. Implementing Hotel schema unlocks hotel rich results, Google Hotels integration, and knowledge panels.

**Action:** Deploy the Hotel JSON-LD from [03-schema.md](03-schema.md) on the homepage and accommodation page. Deploy via Google Tag Manager or WordPress header plugin.

**Note:** Verify geo coordinates (62.0456, 28.3667 are approximate), check-in/check-out times, number of rooms, and star rating before deploying.

---

### H2. Implement Restaurant Schemas (4+ Venues)

**Impact:** Very High | **Effort:** 1-2 hours | **Owner:** Developer
**Source:** [03-schema.md](03-schema.md) -- ready-to-use JSON-LD for Solitary, Fire Kitchen, Piikatytto, Bistro, Lotja

Restaurant Solitary is ranked **9th best restaurant in Finland** but has zero schema markup. Google cannot surface any restaurant information.

**Action:** Deploy Restaurant JSON-LD for all venues from [03-schema.md](03-schema.md). Solitary schema includes Menu with pricing (EUR 64/94) and ReserveAction for online booking.

---

### H3. Implement Spa Schema (HealthAndBeautyBusiness)

**Impact:** High | **Effort:** 30 min | **Owner:** Developer
**Source:** [03-schema.md](03-schema.md)

The Lake Spa is a flagship attraction with zero structured data. Deploy HealthAndBeautyBusiness schema on `/en/lake-spa/`.

---

### H4. Implement TouristDestination/TouristAttraction Schema

**Impact:** High | **Effort:** 30 min | **Owner:** Developer
**Source:** [03-schema.md](03-schema.md)

Activities page has 22 bookable experiences with pricing but no structured data. Deploy TouristDestination schema with TouristAttraction items.

---

### H5. Enhance Organization + WebSite Schemas

**Impact:** High | **Effort:** 30 min | **Owner:** Developer
**Source:** [03-schema.md](03-schema.md)

Current Organization schema is missing: address, telephone, email, geo coordinates, description, and contactPoint. WebSite schema is missing SearchAction.

**Action:** Replace existing Yoast Organization and WebSite schemas with enhanced versions from [03-schema.md](03-schema.md).

---

### H6. Add Image Alt Text to All Images

**Impact:** High | **Effort:** 1 hour | **Owner:** Content/Marketing
**Source:** [04-images.md](04-images.md) findings C2, [02-on-page.md](02-on-page.md) finding C3

~60% of images lack alt text, including ALL hero images. This is a WCAG 2.1 A accessibility violation.

**Action:** Add descriptive, keyword-rich alt text to every image. Format: "[description] at Jarvisydan, Lake Saimaa". Example: "Winter sleigh ride under starry sky at Jarvisydan resort, Finnish Lakeland".

---

### H7. Add Visible Content Images to 3 Empty Pages

**Impact:** High | **Effort:** 2-3 hours | **Owner:** Content + Developer
**Source:** [04-images.md](04-images.md) findings C1, C3-C6

Spa, Restaurants, and Activities pages have **zero visible content images** in HTML. Images exist in the media library but are only referenced in metadata.

**Actions:**
1. Add hero images to spa, restaurants, and activities pages (images already exist)
2. Add content images throughout: room photos, food photos, spa facility photos, activity photos
3. Add `fetchpriority="high"` to above-fold hero images
4. Add width/height attributes to prevent CLS

---

### H8. Enable Open Graph Tags

**Impact:** Medium-High | **Effort:** 10 min | **Owner:** Content/Developer
**Source:** [02-on-page.md](02-on-page.md) finding H1

Open Graph tags are missing on ALL pages. Social sharing produces blank/poor previews.

**Action:** Yoast SEO > Social > Facebook tab > Enable. Yoast SEO > Social > Twitter tab > Enable.

---

### H9. Rewrite All H1 Tags with Target Keywords

**Impact:** High | **Effort:** 30 min | **Owner:** Content/Marketing
**Source:** [02-on-page.md](02-on-page.md) finding H2, [07-geo-ai-search.md](07-geo-ai-search.md) finding #2

| Page | Current H1 | Recommended H1 |
|------|-----------|----------------|
| Homepage | "Stories to be saved in hearts" | "Nature Hotel & Spa Resort on Lake Saimaa, Finland" |
| Accommodation | "Relax in The Hearth of Lake Saimaa" | "Accommodation on Lake Saimaa, Finnish Lakeland" |
| Restaurants | "Restaurants" | "Restaurants & Dining at Jarvisydan, Lake Saimaa" |
| Activities | "Explore Porosalmi trails!" | "Activities & Nature Experiences on Lake Saimaa" |

**Note:** Also fixes "Hearth" typo on accommodation page. Keep emotional taglines as H2 subtitles.

---

### H10. Fix WordPress Theme Image Features

**Impact:** Medium-High | **Effort:** 1-2 hours | **Owner:** Developer
**Source:** [04-images.md](04-images.md), [01-technical.md](01-technical.md)

The Digitaali theme suppresses WordPress native lazy loading and srcset generation.

**Actions:**
1. Check `functions.php` for `remove_filter('the_content', 'wp_make_content_images_responsive')` or similar
2. Check for `add_filter('wp_lazy_loading_enabled', '__return_false')`
3. Re-enable native WordPress image features
4. Install WebP conversion plugin (ShortPixel or Imagify)

---

### H11. Add Location Keywords to All Title Tags

**Impact:** High | **Effort:** 15 min | **Owner:** Content/Marketing
**Source:** [02-on-page.md](02-on-page.md)

"Lake Saimaa" and "Finland" appear in zero title tags across the entire site.

| Page | Recommended Title |
|------|------------------|
| Homepage | "Hotel & Spa Resort Jarvisydan | Lake Saimaa, Finland" |
| Accommodation | "Accommodation on Lake Saimaa | Hotel & Spa Jarvisydan, Finland" |
| Spa | "Ecological Lake Spa & Day Spa | Jarvisydan, Lake Saimaa Finland" |
| Restaurants | "Restaurants & Dining | Jarvisydan, Lake Saimaa Finland" |
| Activities | "Activities & Nature Experiences | Jarvisydan, Lake Saimaa Finland" |

---

### H12. Ensure English Pages in XML Sitemap

**Impact:** High | **Effort:** 15 min | **Owner:** Developer/IT
**Source:** [06-international.md](06-international.md) finding F04

Only 16 English URLs appear in sitemaps vs estimated 50+ English pages. Many English pages are undiscoverable.

**Action:** Verify WPML settings include translated pages in sitemaps. Enable hreflang annotations in sitemaps.

---

## MEDIUM -- Fix Within 2-4 Weeks (Optimization & Content Depth)

### M1. Expand Accommodation Page Content

**Effort:** 2-3 hours | **Owner:** Content/Marketing
**Source:** [05-content.md](05-content.md)

Currently ~150 words of unique content -- critically thin. Target: 800+ words.

**Add:** Room type descriptions with amenities, guest capacity, comparison table, check-in/check-out times, pet policy, distance from Savonlinna and Helsinki.

---

### M2. Add Guest Testimonials/Reviews

**Effort:** 2 hours | **Owner:** Content/Marketing
**Source:** [05-content.md](05-content.md)

Zero guest reviews on any page. Critical E-E-A-T gap.

**Options:** TripAdvisor widget, Google review embed, or curated guest quotes with names and dates. Add to homepage, accommodation, and restaurants pages.

---

### M3. Add Staff/Team Profiles

**Effort:** 2-3 hours | **Owner:** Content/Marketing
**Source:** [05-content.md](05-content.md)

Only 1 staff member named across 5 pages. For a resort with 6 restaurants and guided activities, this is a critical expertise gap.

**Add:** Chef profiles (especially for Solitary), Activity Manager bio expansion, spa therapist credentials, nature guide certifications. Target: 5-8 named staff members.

---

### M4. Add FAQ Sections with Schema

**Effort:** 3-4 hours | **Owner:** Content + Developer
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md) finding #4

Zero FAQ content on any page. FAQs are one of the most effective ways to get content cited by AI systems and appear in Google featured snippets.

**Add FAQs to:**
- Homepage: "Where is Jarvisydan located?", "What makes Jarvisydan unique?", "How to get to Jarvisydan?"
- Accommodation: "What types of accommodation are available?", "What is check-in/check-out time?"
- Spa: "What facilities does the Lake Spa have?", "How much does the Day Spa cost?"
- Activities: "What activities are available in winter/summer?", "Can I book activities in advance?"

Deploy with FAQ schema markup for each section.

---

### M5. Add Comparison Tables

**Effort:** 2-3 hours | **Owner:** Content/Marketing
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md) finding #5

No comparison tables exist on any page. Tables are highly citable by AI systems and valuable for user decision-making.

**Create:**
- Accommodation: Type, capacity, price from, features, season
- Restaurants: Name, cuisine, price range, hours, reservation required
- Activities: Activity, season, duration, price, booking required
- Spa: Treatment, duration, price, included features

---

### M6. Expand Restaurant Descriptions

**Effort:** 2 hours | **Owner:** Content/Marketing
**Source:** [05-content.md](05-content.md)

~120 words per restaurant across 7 venues. Add chef names, signature dishes, local ingredient sourcing, seasonal menus. Amplify Solitary's #9 ranking with source attribution.

---

### M7. Leverage 1658 Heritage Story

**Effort:** 1 hour | **Owner:** Content/Marketing
**Source:** [05-content.md](05-content.md)

Mentioned in one sentence on the homepage, never expanded. 360+ years of heritage is a powerful differentiator.

**Action:** Expand to a compelling paragraph on the homepage. Consider a dedicated "Our Story" section visible from main navigation.

---

### M8. Add robots.txt Disallow Rules

**Effort:** 10 min | **Owner:** Developer/IT
**Source:** [01-technical.md](01-technical.md)

Block low-value paths to preserve crawl budget:
```
Disallow: /wp-admin/
Disallow: /wp-includes/
Disallow: /?s=
Disallow: /?page_id=
Disallow: /?p=
```

Also add explicit Allow directives for AI crawlers (recommended in [07-geo-ai-search.md](07-geo-ai-search.md)).

---

### M9. Clean Sitemap Issues

**Effort:** 30 min | **Owner:** Developer/IT
**Source:** [01-technical.md](01-technical.md)

- Remove duplicate URLs from post-sitemap and event-sitemap
- Fix query-string URLs (`/?post_type=dg_event&p=XXXX`) by setting proper permalinks for `dg_event` custom post type
- Remove `?page_id=` URL from page sitemap
- Add English pages to sitemap (see H12)

---

### M10. Add og:locale Tags

**Effort:** 10 min | **Owner:** Developer
**Source:** [06-international.md](06-international.md) finding F09

Add `og:locale` (fi_FI, en_US) and `og:locale:alternate` tags for proper social sharing language detection. Should be handled by Yoast + WPML if properly configured.

---

### M11. Restructure Activities Page Headings

**Effort:** 1 hour | **Owner:** Content/Marketing
**Source:** [02-on-page.md](02-on-page.md), [07-geo-ai-search.md](07-geo-ai-search.md)

24 H2 headings in a flat structure. Also has duplicate H1 tags (invalid HTML).

**Actions:**
1. Fix duplicate H1 -- keep only one
2. Group activities into category H2s: "Yoga & Wellness", "Nature Tours", "Water Activities", "Winter Activities"
3. Individual activities become H3s under their category
4. Add seasonal activity summary table

---

### M12. Write AI-Citable Passages

**Effort:** 2-3 hours | **Owner:** Content/Marketing
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md) finding #6

Add 134-167 word factual overview paragraphs to key pages. Use third-person voice ("Jarvisydan is..." not "We invite you..."). Include specific facts, numbers, and attributable claims.

---

## LOW -- Backlog (Nice to Have / Ongoing)

### L1. Translate Top 20 Finnish Pages to English

**Effort:** High (translation budget) | **Owner:** Content + Translator
**Source:** [06-international.md](06-international.md)

Only 16 of 421 sitemap URLs are English (3.8%). Priority translations:
- Individual restaurant pages (Solitary, Piikatytto, Fire Kitchen)
- Seal safaris, national park trips
- Seasonal landing pages (6 pages, 0% translated)
- Weddings and corporate events

---

### L2. Fix "accomodations" URL Typo

**Effort:** 10 min | **Owner:** Developer
**Source:** [02-on-page.md](02-on-page.md) finding H6

Internal link to `/en/accommodation/accomodations/` missing an 'm'. Set up 301 redirect.

---

### L3. Rename Generic Image Files

**Effort:** 1 hour (requires URL redirects) | **Owner:** Content + Developer
**Source:** [04-images.md](04-images.md)

- `Image-282.jpg` -> `jarvisydan-lakeside-accommodation-saimaa.jpg`
- Remove resolution prefixes and camera numbers from filenames
- Set up 301 redirects from old URLs

---

### L4. Fix YouTube URL Mismatch in Schema

**Effort:** 5 min | **Owner:** Developer
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md)

Schema sameAs uses `youtube.com/c/jarvisydan` but footer links `youtube.com/user/LomakylaJarvisydan`. Align to canonical YouTube URL.

---

### L5. Add LinkedIn to Schema sameAs

**Effort:** 5 min | **Owner:** Developer
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md)

LinkedIn URL is in the footer but missing from Organization schema sameAs array.

---

### L6. Build English Wikipedia Article

**Effort:** 10-20 hours | **Owner:** Marketing/PR
**Source:** [07-geo-ai-search.md](07-geo-ai-search.md) finding #4

No English Wikipedia article exists. This is a significant gap for English-language AI systems. Requires verifiable third-party sources (news articles, tourism board references, award announcements).

**Note:** Finnish Wikipedia contains negative content. English article should be factual and balanced per Wikipedia's NPOV policy.

---

### L7. Address Premium Phone Number

**Effort:** Varies | **Owner:** Management
**Source:** [05-content.md](05-content.md)

0600 prefix charges callers EUR 0.65/min -- significant trust barrier for international tourists. Consider adding a standard-rate or free international contact number.

---

### L8. Add Publication/Update Dates to Service Pages

**Effort:** 30 min | **Owner:** Content
**Source:** [05-content.md](05-content.md)

No visible dates on service pages. Reduces freshness signals for Google.

---

## Implementation Timeline

| Week | Focus | Items | Expected Score |
|------|-------|-------|---------------|
| 1 | Critical Quick Wins | C1-C8 | 38 → 50 |
| 2 | Schema Implementation | H1-H5 | 50 → 58 |
| 3 | Images & On-Page | H6-H12 | 58 → 65 |
| 4 | Content Expansion | M1-M3, M6-M7 | 65 → 70 |
| 5-6 | AI Optimization & Structure | M4-M5, M11-M12 | 70 → 75 |
| 7-8 | Technical Cleanup | M8-M10, L2-L5 | 75 → 78 |
| Ongoing | Translation & Entity Building | L1, L6 | 78 → 80+ |

---

## Owner Quick Reference

| Role | Items | Effort |
|------|-------|--------|
| **Developer/IT** | C1, C2, C3, C8, H1-H5, H10, H12, M8-M10 | ~8-12 hours |
| **Content/Marketing** | C4-C6, H6, H7, H8, H9, H11, M1-M7, M11-M12 | ~20-30 hours |
| **Management** | L7 (phone number decision) | Decision only |
| **Translator** | L1 (20 page translations) | Separate budget |
| **Marketing/PR** | L6 (Wikipedia article) | 10-20 hours |

---

## Verification Checklist (After Implementation)

After completing Critical + High items, verify:

- [ ] Hreflang tags visible in page source (`<link rel="alternate" hreflang="fi" ...>`)
- [ ] `/en/spa/` redirects to `/en/lake-spa/` (301)
- [ ] robots.txt contains Sitemap directive
- [ ] Homepage title no longer starts with "Front page"
- [ ] Meta descriptions visible in Yoast for all 5 pages
- [ ] Hotel schema validates at [Google Rich Results Test](https://search.google.com/test/rich-results)
- [ ] Restaurant schema validates
- [ ] All hero images have alt text
- [ ] Open Graph preview works (use [opengraph.xyz](https://opengraph.xyz))
- [ ] llms.txt accessible at `www.jarvisydan.com/llms.txt`
- [ ] Google Search Console resubmit sitemaps
- [ ] PageSpeed Insights score check at [pagespeed.web.dev](https://pagespeed.web.dev)
- [ ] Monitor Google Search Console for hreflang errors (2-4 weeks)

---

*Action Plan compiled 2026-02-11 by Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy.*
*Based on 7 specialist audit reports totaling 65+ findings.*
*All schema JSON-LD templates ready to deploy in [03-schema.md](03-schema.md).*
*Recommended llms.txt content ready in [07-geo-ai-search.md](07-geo-ai-search.md).*
