# Jarvisydan SEO: Page-by-Page TODO List
## 5 Priority Pages — Concrete Action Items

**Generated:** 2026-02-11
**Overall Site Score:** 33/100
**Target Score After Fixes:** 70-80/100

---

## Sitewide TODOs (Apply to ALL 5 Pages)

These fixes are template/theme-level — do once, fix everywhere.

### WordPress / Theme (Digitaali)

- [ ] **Enable hreflang in WPML** — WPML > Languages > SEO Options > Enable "Head langs"
  - Severity: CRITICAL | Effort: 15 min | Impact: +30-50% international traffic
  - Currently: Zero hreflang on entire site. Google can't connect /fi/ and /en/ pages

- [ ] **Fix WordPress lazy loading** — The Digitaali theme suppresses WP's native `loading="lazy"`
  - Check `functions.php` for `wp_lazy_loading_enabled` filter or `wp_img_tag_add_loading_attr` removal
  - Severity: HIGH | Effort: 30 min investigation

- [ ] **Fix WordPress srcset/responsive images** — Theme suppresses WP's native `srcset`
  - Check `functions.php` for `wp_calculate_image_srcset` filter removal
  - Severity: HIGH | Effort: 30 min investigation

- [ ] **Install WebP conversion plugin** — ShortPixel or Imagify
  - Auto-converts all JPG/PNG to WebP with fallback
  - Severity: HIGH | Effort: 15 min

- [ ] **Add Open Graph meta tags** — Enable in Yoast SEO > Social > Facebook/Twitter tabs
  - Missing on ALL pages. Kills social sharing previews
  - Severity: HIGH | Effort: 10 min

- [ ] **Add sitemap reference to robots.txt** — Add `Sitemap: https://www.jarvisydan.com/sitemap.xml`
  - Currently robots.txt is essentially empty
  - Severity: HIGH | Effort: 1 min

- [ ] **Add robots.txt Disallow rules** — Block `/wp-admin/`, `/?s=`, `/?page_id=`, `/?p=`
  - Severity: MEDIUM | Effort: 5 min

- [ ] **Clean duplicate URLs from sitemaps** — Audit Yoast settings
  - Severity: MEDIUM | Effort: 30 min

- [ ] **Add "Rantasalmi" to every page** — Currently appears only 1x total (footer address)
  - Add to first paragraph of each page: "...in Rantasalmi, Finnish Lakeland"
  - Severity: CRITICAL | Effort: 30 min

- [ ] **Add "Finnish Lakeland" to every page** — Currently appears only 1x total
  - Severity: CRITICAL | Effort: 30 min

### Schema (Sitewide)

- [ ] **Fix Organization schema** — Add address, telephone, email, geo, description
  - Ready-to-use JSON-LD in [03-schema.md](03-schema.md)
  - Severity: HIGH | Effort: 15 min

- [ ] **Add WebSite SearchAction schema** — Enable sitelinks search box
  - Ready-to-use JSON-LD in [03-schema.md](03-schema.md)
  - Severity: HIGH | Effort: 10 min

---

## PAGE 1: Homepage `/en/`

**Current Score: 42/100 (On-Page) | 61/100 (Content)**

### CRITICAL

- [ ] **Rewrite title tag**
  - FROM: `Front page - Hotel & Spa Resort Jarvisydan`
  - TO: `Hotel & Spa Resort Jarvisydan | Lake Saimaa, Finland`
  - WHERE: Yoast SEO > Edit Page > SEO Title
  - Effort: 2 min

- [ ] **Write meta description**
  - CURRENTLY: Missing entirely
  - WRITE: `Discover Jarvisydan, a nature hotel & spa resort on Lake Saimaa in Rantasalmi, Finnish Lakeland. Award-winning restaurants, ecological lake spa & year-round activities. Book your escape.`
  - WHERE: Yoast SEO > Edit Page > Meta Description
  - Effort: 5 min

- [ ] **Rewrite H1 with keywords**
  - FROM: `Stories to be saved in hearts Experience the Savonian hospitality.`
  - TO: `Nature Hotel & Spa Resort on Lake Saimaa` (keep old text as subtitle/H2)
  - Effort: 5 min

- [ ] **Add alt text to hero image**
  - IMAGE: `Winter-Activities-2-14.jpg`
  - ALT: `Winter activities at Hotel & Spa Resort Jarvisydan on Lake Saimaa, Finland`
  - WHERE: WordPress Media Library or page editor
  - Effort: 2 min

### HIGH

- [ ] **Add `fetchpriority="high"` to hero image** — LCP optimization
- [ ] **Add width/height attributes to hero image** — CLS prevention
- [ ] **Add Hotel schema to homepage** — Ready-to-use JSON-LD in [03-schema.md](03-schema.md)
  - Includes address, amenities, check-in/out, containsPlace for restaurants/spa
- [ ] **Expand "Our roots date back to 1658" heritage story** — Currently one sentence
  - Add 2-3 sentences about family history, location significance
  - Strong E-E-A-T differentiator

### MEDIUM

- [ ] **Add H3 subheadings** — Currently flat H1>H2 structure, no H3 depth
- [ ] **Add guest testimonial/review section** — Zero reviews on any page
- [ ] **Rename hero image file** — `Winter-Activities-2-14.jpg` → `jarvisydan-winter-activities-lake-saimaa.jpg`

---

## PAGE 2: Accommodation `/en/accommodation/`

**Current Score: 32/100 (On-Page) | 38/100 (Content)**
**Weakest on-page score. Needs most work.**

### CRITICAL

- [ ] **Write meta description**
  - CURRENTLY: Missing entirely
  - WRITE: `Choose from lakeside villas, themed suites, Kuru Resort rooms, caravan area & guest harbour at Jarvisydan on Lake Saimaa, Rantasalmi. Book your Finnish Lakeland stay.`
  - Effort: 5 min

- [ ] **Expand page content from ~150 words to 500+ words**
  - Currently critically thin — mostly just links to subpages
  - ADD for each accommodation type: brief description, capacity, key amenities, view/location
  - ADD: comparison table (type | guests | price from | features)
  - ADD: check-in/out times, pet policy, accessibility info
  - Effort: 1-2 hours

- [ ] **Fix "Hearth" typo in H1**
  - FROM: `Relax in The Hearth of Lake Saimaa`
  - TO: `Accommodation on Lake Saimaa, Finnish Lakeland`
  - Effort: 2 min

- [ ] **Add alt text to hero image**
  - IMAGE: `Image-282.jpg` (generic name!)
  - ALT: `Lakeside accommodation at Jarvisydan resort overlooking Lake Saimaa`
  - Effort: 2 min

- [ ] **Rename generic hero image**
  - FROM: `Image-282.jpg`
  - TO: `jarvisydan-lakeside-accommodation-saimaa.jpg`
  - Re-upload in WordPress Media Library
  - Effort: 10 min

### HIGH

- [ ] **Rewrite title tag with location**
  - FROM: `Accommodation - Hotel & Spa Resort Jarvisydan`
  - TO: `Accommodation on Lake Saimaa | Hotel & Spa Jarvisydan, Finland`
  - Effort: 2 min

- [ ] **Fix URL typo** — Internal link goes to `/en/accommodation/accomodations/` (missing 'm')
  - Set up 301 redirect from misspelled URL to correct one
  - Effort: 10 min

- [ ] **Add accommodation photos** — Currently only 1 image for entire page
  - Need: 1 photo per accommodation type (villas, suites, hotel rooms, Kuru, caravan, harbour)
  - Each with descriptive alt text
  - Effort: 1 hour

- [ ] **Add H2s for each accommodation type** — Currently missing "Hotel Rooms", "Villas", "Kuru Suites" headings
- [ ] **Add Hotel/LodgingBusiness schema with room offers** — JSON-LD in [03-schema.md](03-schema.md)

### MEDIUM

- [ ] **Add distance info** — "330 km from Helsinki (4h drive), 60 km from Savonlinna"
- [ ] **Add "Savonlinna" keyword** — Nearest well-known city, absent from this page
- [ ] **Add comparison table** — Helps users choose and adds structured content

---

## PAGE 3: Spa `/en/spa/` → `/en/lake-spa/`

**Current Score: 52/100 (On-Page, actual spa page) | 29/100 (Content, /spa/ redirect target)**
**Biggest structural problem on the site.**

### CRITICAL

- [ ] **Fix /en/spa/ redirect**
  - PROBLEM: `/en/spa/` redirects to thin holiday package page (280 words)
  - ACTUAL spa content lives at `/en/lake-spa/` with ~3,000 words (pools, saunas, pricing, hours)
  - FIX: 301 redirect `/en/spa/` → `/en/lake-spa/` OR create proper overview at `/en/spa/`
  - ALSO: Fix canonical tag (currently points to `/en/lomapaketit/spa-holiday/`)
  - Effort: 15 min
  - Impact: VERY HIGH — spa keywords are primary search terms

- [ ] **Add visible images to spa page**
  - PROBLEM: Zero content images in HTML body. Hero image exists only in JSON-LD metadata
  - ADD: Pool photos, sauna photos, treatment room, outdoor lake pool
  - The image `Spa-7-scaled.jpg` (2048x2560) exists but isn't rendered — add it and resize
  - Effort: 30 min

### HIGH

- [ ] **Rewrite title tag**
  - FROM: `Lake Spa & Day Spa - Hotel & Spa Resort Jarvisydan`
  - TO: `Lake Spa & Day Spa | Jarvisydan, Lake Saimaa Finland — Finland's Most Ecological Spa`
  - Effort: 2 min

- [ ] **Fix Finnish alt text on English page**
  - Gallery images have Finnish alt text ("Jarvikylpylan paaallas") on the English page
  - Translate all alt text to English
  - Effort: 30 min

- [ ] **Expand meta description with CTA**
  - FROM: `Welcome to Finland's most ecological lake spa!...` (128 chars, no CTA)
  - TO: `Finland's most ecological lake spa on Lake Saimaa. Indoor & outdoor pools, 6 saunas, peat treatments & salt room. Day Spa from €XX. Book your visit.`
  - Effort: 5 min

- [ ] **Add HealthAndBeautyBusiness schema** — Ready-to-use JSON-LD in [03-schema.md](03-schema.md)
  - Includes: opening hours, pricing, services, amenities

- [ ] **Resize oversized metadata image** — `Spa-7-scaled.jpg` at 2048x2560 is excessive
  - Resize to max 1920px wide
  - Effort: 5 min

### MEDIUM

- [ ] **Add staff credentials** — No spa therapist profiles or certifications shown
- [ ] **Surface sustainability story on spa page** — 500-year sinker logs, solar, geothermal is compelling and unique

---

## PAGE 4: Restaurants `/en/restaurants/`

**Current Score: 45/100 (On-Page) | 46/100 (Content)**

### CRITICAL

- [ ] **Write meta description**
  - CURRENTLY: Missing entirely
  - WRITE: `Six restaurants at Jarvisydan resort on Lake Saimaa. From Restaurant Solitary (Finland's 9th best) to Wine Cellar Fire Kitchen & lakeside dining. See menus & book a table.`
  - Effort: 5 min

- [ ] **Add visible images**
  - PROBLEM: Zero content images in HTML body. Hero image exists only in metadata
  - ADD: Photo for each restaurant (Solitary, Fire Kitchen, Piikatytto, Bistro, Lotja, Kota)
  - Each with descriptive English alt text
  - Effort: 1 hour

### HIGH

- [ ] **Rewrite H1 with keywords**
  - FROM: `Restaurants`
  - TO: `Restaurants & Dining at Jarvisydan, Lake Saimaa`
  - Effort: 2 min

- [ ] **Rewrite title tag**
  - FROM: `Restaurants - Hotel & Spa Resort Jarvisydan`
  - TO: `Restaurants & Dining | Jarvisydan, Lake Saimaa — Award-Winning Finnish Cuisine`
  - Effort: 2 min

- [ ] **Add Restaurant schema for each venue** — Ready-to-use JSON-LD in [03-schema.md](03-schema.md)
  - Especially Restaurant Solitary (9th best in Finland = rich result goldmine)
  - Include: cuisine type, price range, opening hours, reservation URL
  - 4 separate Restaurant schemas + 1 BarOrNightClub (Lotja)

- [ ] **Expand restaurant descriptions** — Currently ~120 words per restaurant
  - Add: signature dishes, chef name, local sourcing details, seasonal menu mention
  - Target: 200-300 words per restaurant
  - Effort: 2 hours

- [ ] **Add missing geo-keywords**
  - "Lake Saimaa" appears only 1x (Solitary context)
  - Add "Rantasalmi", "Savonlinna area", "Finnish Lakeland" to intro text
  - Effort: 15 min

### MEDIUM

- [ ] **Add chef profiles** — 7 restaurants, zero chefs named. Huge E-E-A-T gap
- [ ] **Rename hero image** — `Illallinen-tulikeittio.jpg` → `fire-kitchen-dining-jarvisydan.jpg`
- [ ] **Add price range indicators** — Only Solitary shows pricing (64/94 EUR)

---

## PAGE 5: Activities `/en/activities/`

**Current Score: 48/100 (On-Page) | 69/100 (Content)**
**Strongest page overall. Needs polish, not overhaul.**

### CRITICAL

- [ ] **Add visible images**
  - PROBLEM: Zero content images in HTML body despite 22+ activity listings
  - ADD: Photo for each activity card (or at minimum, category headers)
  - Hero image `1920-Tahtitaivaan-rekiretki_16.jpg` exists in metadata but isn't rendered
  - Effort: 1-2 hours

- [ ] **Add alt text to hero image**
  - ALT: `Starry sky sleigh ride at Jarvisydan resort, Finnish Lakeland`
  - Effort: 2 min

### HIGH

- [ ] **Rewrite H1 with keywords**
  - FROM: `Explore Porosalmi trails!` (seasonal promo, "Porosalmi" is not a tourist search term)
  - TO: `Activities & Nature Experiences on Lake Saimaa`
  - Effort: 2 min

- [ ] **Rewrite title tag**
  - FROM: `Activities - Hotel & Spa Resort Jarvisydan`
  - TO: `Activities & Nature Experiences | Jarvisydan, Lake Saimaa Finland`
  - Effort: 2 min

- [ ] **Improve meta description**
  - FROM: `Seasonal activities throughout the year...throughout the year!` (repeated phrase)
  - TO: `Yoga, fishing, national park excursions, seal watching, snowshoeing & more at Jarvisydan on Lake Saimaa. Year-round guided activities in Finnish Lakeland. Book your adventure.`
  - Effort: 5 min

- [ ] **Add TouristDestination/TouristAttraction schema** — JSON-LD in [03-schema.md](03-schema.md)
  - Includes: Linnansaari National Park, Saimaa Ringed Seal, activities with pricing

### MEDIUM

- [ ] **Restructure headings** — Currently 24 H2s (one per activity), very flat
  - Group into category H2s: "Yoga & Wellness", "Nature Tours", "Water Activities", "Winter Activities"
  - Individual activities become H3s under each category
  - Effort: 30 min

- [ ] **Add "Finnish Lakeland" keyword** — Currently missing from this page
- [ ] **Give Linnansaari National Park more prominence** — 4 mentions but deserves a dedicated section
- [ ] **Rename hero image** — Remove resolution prefix and camera number

---

## Implementation Priority Matrix

### This Week (< 4 hours total)

| # | Action | Page | Time | Impact |
|---|--------|------|------|--------|
| 1 | Fix homepage title tag | Home | 2 min | HIGH |
| 2 | Write 4 meta descriptions | Home, Accom, Rest, Activities | 20 min | HIGH |
| 3 | Enable hreflang in WPML | All | 15 min | VERY HIGH |
| 4 | Fix /en/spa/ redirect to /en/lake-spa/ | Spa | 15 min | VERY HIGH |
| 5 | Add sitemap to robots.txt | All | 1 min | MEDIUM |
| 6 | Rewrite all 5 H1 tags | All | 15 min | HIGH |
| 7 | Add alt text to all hero images | All | 10 min | HIGH |
| 8 | Add "Rantasalmi" + "Finnish Lakeland" to all pages | All | 30 min | HIGH |
| 9 | Fix "Hearth" typo | Accom | 2 min | LOW |
| 10 | Enable Open Graph in Yoast | All | 10 min | MEDIUM |

**Total: ~2 hours for all quick wins**

### Next 2 Weeks

| # | Action | Time | Impact |
|---|--------|------|--------|
| 11 | Expand accommodation page to 500+ words | 2 hours | HIGH |
| 12 | Add photos to all 5 pages (images exist in media library) | 3 hours | VERY HIGH |
| 13 | Install WebP plugin + fix theme srcset/lazy loading | 1 hour | HIGH |
| 14 | Implement Hotel schema | 30 min | HIGH |
| 15 | Implement Restaurant schemas (x4) | 1 hour | HIGH |
| 16 | Implement Spa schema | 20 min | MEDIUM |
| 17 | Expand restaurant descriptions | 2 hours | MEDIUM |
| 18 | Add guest testimonials section | 1 hour | HIGH |

### Month 2

| # | Action | Time | Impact |
|---|--------|------|--------|
| 19 | Translate top 20 Finnish pages to English | 20+ hours | VERY HIGH |
| 20 | Add chef/staff profiles | 3 hours | MEDIUM |
| 21 | Create seasonal landing pages | 4 hours | MEDIUM |
| 22 | Restructure activities page headings | 30 min | LOW |
| 23 | Create local area guide | 3 hours | MEDIUM |
| 24 | Fix premium phone number issue | 1 hour | MEDIUM |

---

## Score Projection

| Area | Current | After Quick Wins | After 2 Weeks | After 2 Months |
|------|---------|-----------------|---------------|----------------|
| Technical | 48 | 58 | 70 | 78 |
| On-Page | 41 | 62 | 75 | 82 |
| Schema | 18 | 18 | 65 | 75 |
| Images | 18 | 30 | 65 | 80 |
| Content | 52 | 58 | 70 | 82 |
| International | 18 | 45 | 55 | 72 |
| **OVERALL** | **33** | **48** | **67** | **78** |

The quick wins alone should push the site from 33 → 48 (+15 points).
Two weeks of focused work targets 67/100.
Full execution over 2 months targets 78/100.

---

## Files Reference

| File | What It Contains |
|------|-----------------|
| [FULL-REPORT.md](FULL-REPORT.md) | Executive summary, all scores, top 10 priorities |
| [01-technical.md](01-technical.md) | Robots, sitemap, HTTPS, canonicals, Core Web Vitals |
| [02-on-page.md](02-on-page.md) | Title tags, meta descriptions, headings, per-page scorecards |
| [03-schema.md](03-schema.md) | 12 ready-to-use JSON-LD code blocks for all missing schemas |
| [04-images.md](04-images.md) | Per-image inventory, alt text, formats, lazy loading |
| [05-content.md](05-content.md) | Word counts, E-E-A-T analysis, geo-keyword matrix |
| [06-international.md](06-international.md) | Hreflang, content parity, WPML configuration checklist |
| **PAGE-TODOS.md** | This file — concrete per-page checkbox TODOs |

---

*Generated 2026-02-11 by Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy*
