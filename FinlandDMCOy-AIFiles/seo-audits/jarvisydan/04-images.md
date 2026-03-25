# Image SEO Audit: jarvisydan.com

**Audit Date:** 2026-02-11
**Auditor:** Claude Opus 4.6 (automated)
**Pages Audited:** 5
**Site Platform:** WordPress (theme: Digitaali)

---

## Executive Summary

The jarvisydan.com website has **severe image SEO deficiencies** across all five audited pages. The site uses an extremely minimal number of content images (only 1-2 unique images per page beyond shared navigation/footer elements), relies heavily on text-only layouts, and the images that do exist lack critical SEO and accessibility attributes.

**Key findings:**
- Zero images have `loading="lazy"` attribute on any page
- Zero images use `srcset` or responsive image techniques
- Zero images use modern formats (WebP/AVIF) -- all are JPG or PNG
- Multiple hero images are missing alt text entirely
- No `<picture>` elements are used anywhere on the site
- Several pages (spa, activities) have hero images only in metadata, not rendered in HTML
- No width/height attributes on most images, creating CLS risk
- File names are a mix of descriptive and generic ("Image-282.jpg")

**Overall Score: 18 / 100**

---

## Scoring Breakdown

| Category | Max Points | Score | Notes |
|----------|-----------|-------|-------|
| Alt text coverage | 20 | 6 | ~40% of images have alt text; hero images missing |
| Modern formats (WebP/AVIF) | 15 | 0 | All images are JPG/PNG/SVG -- zero WebP/AVIF |
| Responsive images (srcset) | 15 | 0 | No srcset or sizes attributes anywhere |
| Lazy loading | 10 | 0 | No loading="lazy" on any image |
| CLS prevention (width/height) | 10 | 2 | Only 2 of ~13 unique images have dimensions |
| File naming | 10 | 4 | Mixed -- some descriptive, some generic |
| File size optimization | 10 | 3 | Hero images at full resolution (1920px+) served without optimization |
| Image quantity/coverage | 10 | 3 | Very few content images; spa and activities pages have zero visible content images |
| **TOTAL** | **100** | **18** | |

---

## Global / Shared Images (appear on all 5 pages)

These images are present in the header and footer of every page:

| # | Image | src | alt | W x H attrs | loading | srcset | Format | Severity |
|---|-------|-----|-----|-------------|---------|--------|--------|----------|
| G1 | Header logo | `.../Digitaali/images/logo.svg` | "Hotel & Spa Resort Jarvisydan" (inconsistent across pages) | Missing | No | No | SVG | 🟡 |
| G2 | Footer logo (negative) | `.../Digitaali/images/logo-nega.png` | "Hotel & Spa Resort Jarvisydan" (inconsistent) | Missing | No | No | PNG | 🟡 |
| G3 | Footer 3D logo | `.../Digitaali/images/jarvisydan_3D_logo_nega.png` | "Hotel & Spa Resort Jarvisydan" (inconsistent) | Missing | No | No | PNG | 🟡 |
| G4 | Green Key badge | `.../uploads/2024/12/greenkey_logo_2012_1-200x252-1.jpg` | "Greenkey" (inconsistent -- missing on some pages) | Missing (some pages) | No | No | JPG | 🟠 |

### Issues with Global Images

- 🔴 **Alt text inconsistency:** Homepage fetch returned MISSING alt for all images; other pages returned "Hotel & Spa Resort Jarvisydan". This suggests alt text may be inconsistently rendered or conditionally set.
- 🟠 **No width/height on logos:** All three logo images lack dimension attributes, risking CLS during page load.
- 🟡 **PNG logos should be SVG or WebP:** `logo-nega.png` and `jarvisydan_3D_logo_nega.png` would be better served as SVG for scalability or WebP for smaller file size.
- 🟡 **Green Key badge is JPG:** A certification logo should be SVG or PNG for crisp rendering; the JPG format introduces compression artifacts. File name includes dimensions in the name (`200x252`) suggesting WordPress thumbnail handling.

---

## Page 1: Homepage (`/en/`)

### Image Inventory

| # | Image | src | alt | W x H | loading | srcset | Format | Position |
|---|-------|-----|-----|-------|---------|--------|--------|----------|
| 1 | Hero/poster image | `.../uploads/2024/01/Winter-Activities-2-14.jpg` | MISSING | 1920 x 1282 (in markup but inconsistently) | No | No | JPG | Above fold |
| + | Global images G1-G4 (see above) | | | | | | | |

### Total unique content images: 1

### Findings

| # | Finding | Severity | Details |
|---|---------|----------|---------|
| H1 | 🔴 Hero image missing alt text | Critical | The main hero image `Winter-Activities-2-14.jpg` has no alt attribute. This is the most prominent image on the site. Missed opportunity for "winter activities at Jarvisydan resort" or similar keyword-rich alt text. |
| H2 | 🔴 Hero image not lazy loaded (acceptable) | N/A | Above-fold hero image should NOT be lazy loaded -- this is correct behavior. However, it should have `fetchpriority="high"` for LCP optimization. |
| H3 | 🟠 No srcset for hero image | High | A 1920x1282 image is served at full size to all devices. Should have srcset with 640w, 1024w, 1920w variants. |
| H4 | 🟠 No WebP/AVIF format | High | Hero image is full JPG. Should serve WebP via `<picture>` element with JPG fallback. Estimated savings: 25-35% file size. |
| H5 | 🟡 File name semi-descriptive | Medium | `Winter-Activities-2-14.jpg` -- partially descriptive but the "-2-14" suffix is generic camera numbering. Better: `jarvisydan-winter-activities-snow.jpg` |
| H6 | 🟡 Missing `fetchpriority="high"` | Medium | As the LCP element, this image should have `fetchpriority="high"` and `decoding="async"`. |

---

## Page 2: Accommodation (`/en/accommodation/`)

### Image Inventory

| # | Image | src | alt | W x H | loading | srcset | Format | Position |
|---|-------|-----|-----|-------|---------|--------|--------|----------|
| 1 | Hero/primary image | `.../uploads/2022/08/Image-282.jpg` | MISSING | 1200 x 800 (in schema data) | No | No | JPG | Above fold |
| + | Global images G1-G4 (see above) | | | | | | | |

### Total unique content images: 1

### Findings

| # | Finding | Severity | Details |
|---|---------|----------|---------|
| A1 | 🔴 Hero image missing alt text | Critical | `Image-282.jpg` has no alt text. Should describe the accommodation (e.g., "lakeside hotel rooms at Jarvisydan resort"). |
| A2 | 🔴 Generic file name | Critical | `Image-282.jpg` is a camera-default file name. Provides zero SEO value. Should be renamed to something like `jarvisydan-lakeside-accommodation.jpg`. |
| A3 | 🔴 No accommodation listing images | Critical | An accommodation page with zero property photos in the HTML is a major SEO and UX failure. Each room/cabin type should have optimized images with descriptive alt text. Content appears to rely on external booking widget. |
| A4 | 🟠 No srcset for hero image | High | 1200x800 image served at single size to all devices. |
| A5 | 🟠 No WebP/AVIF format | High | JPG only, no modern format alternatives. |

---

## Page 3: Spa (`/en/spa/`)

### Image Inventory

| # | Image | src | alt | W x H | loading | srcset | Format | Position |
|---|-------|-----|-----|-------|---------|--------|--------|----------|
| 1 | Hero image (metadata only) | `.../uploads/2023/03/Spa-7-scaled.jpg` | N/A (not in HTML) | 2048 x 2560 (schema data) | N/A | N/A | JPG | NOT RENDERED |
| + | Global images G1-G4 (see above) | | | | | | | |

### Total unique content images: 0 (in visible HTML)

### Findings

| # | Finding | Severity | Details |
|---|---------|----------|---------|
| S1 | 🔴 Zero visible content images | Critical | The spa page has NO content images rendered in the HTML body. The hero image (`Spa-7-scaled.jpg`) exists only in JSON-LD structured data and meta tags. Users see no spa photos. |
| S2 | 🔴 Massive image in metadata | Critical | `Spa-7-scaled.jpg` is 2048x2560 pixels (portrait orientation, "scaled" suffix indicates WordPress auto-scaling). At this resolution, estimated file size is 500KB-1.5MB. Even though not rendered in HTML, social sharing / SEO crawlers will reference this oversized image. |
| S3 | 🔴 No spa facility images | Critical | A spa page should showcase pools, saunas, treatment rooms, relaxation areas. Zero visual content severely impacts both SEO (no image search traffic) and conversion (users cannot see what they are booking). |
| S4 | 🟡 File name semi-descriptive | Medium | `Spa-7-scaled.jpg` -- "Spa" is relevant but "-7-scaled" is generic. Better: `jarvisydan-spa-pool-lakeside.jpg` |

---

## Page 4: Restaurants (`/en/restaurants/`)

### Image Inventory

| # | Image | src | alt | W x H | loading | srcset | Format | Position |
|---|-------|-----|-----|-------|---------|--------|--------|----------|
| 1 | Hero image (metadata only) | `.../uploads/2024/03/Illallinen-tulikeittio.jpg` | N/A (not in HTML) | 1412 x 929 (schema data) | N/A | N/A | JPG | NOT RENDERED |
| + | Global images G1-G4 (see above) | | | | | | | |

### Total unique content images: 0 (in visible HTML)

### Findings

| # | Finding | Severity | Details |
|---|---------|----------|---------|
| R1 | 🔴 Zero visible content images | Critical | Same issue as spa page -- the restaurant hero image exists only in metadata, not rendered in HTML. |
| R2 | 🔴 No food/dining images | Critical | A restaurant page with zero visible food or dining images is a major conversion and SEO failure. Should show dishes, dining rooms, fire kitchen experience. |
| R3 | 🟢 File name is descriptive (Finnish) | Low | `Illallinen-tulikeittio.jpg` translates to "dinner fire-kitchen" -- good descriptive naming. However, for English SEO, consider English file names: `fire-kitchen-dinner-jarvisydan.jpg`. |

---

## Page 5: Activities (`/en/activities/`)

### Image Inventory

| # | Image | src | alt | W x H | loading | srcset | Format | Position |
|---|-------|-----|-----|-------|---------|--------|--------|----------|
| 1 | Hero image (metadata only) | `.../uploads/2025/01/1920-Tahtitaivaan-rekiretki_16.jpg` | MISSING | 1920 x 1080 (schema data) | N/A | N/A | JPG | NOT RENDERED |
| + | Global images G1-G4 (see above) | | | | | | | |

### Total unique content images: 0 (in visible HTML)

### Findings

| # | Finding | Severity | Details |
|---|---------|----------|---------|
| AC1 | 🔴 Zero visible content images | Critical | Activities page has no rendered images despite having activity listings. Each activity (starry sky sleigh ride, snowshoeing, etc.) should have an enticing photo. |
| AC2 | 🔴 Hero image missing alt text | Critical | The metadata-referenced image has no alt attribute. Should describe the activity: "starry sky sleigh ride at Jarvisydan resort". |
| AC3 | 🟡 File name has resolution prefix | Medium | `1920-Tahtitaivaan-rekiretki_16.jpg` starts with the resolution "1920" and ends with camera number "_16". "Tahtitaivaan-rekiretki" (starry sky sleigh ride) is descriptive but should be the full filename: `starry-sky-sleigh-ride-jarvisydan.jpg`. |
| AC4 | 🔴 No activity card images | Critical | Activity listing cards are text-only. Each activity card should have a compelling photo to drive bookings. |

---

## CSS Background Images (all pages)

| Image | URL | Purpose | Issue |
|-------|-----|---------|-------|
| bg-1.svg | `.../Digitaali/images/bg-1.svg` | Notification background pattern | 🟢 SVG is correct format for patterns |
| icon-plus.svg | `.../Digitaali/images/icon-plus.svg` | Accordion control | 🟢 SVG is correct for icons |
| icon-minus.svg | `.../Digitaali/images/icon-minus.svg` | Accordion control | 🟢 SVG is correct for icons |
| arrow.svg | `.../Digitaali/images/arrow.svg` | Navigation arrow | 🟢 SVG is correct for icons |

CSS background images are appropriately implemented as SVGs. No issues here.

---

## Summary Statistics

| Metric | Value |
|--------|-------|
| **Total unique content images (excl. global)** | 5 (across all 5 pages) |
| **Total unique global images** | 4 (header/footer) |
| **Total unique images site-wide** | 9 |
| **Images actually rendered in HTML body** | 2 of 5 content images (40%) |
| **Images with alt text** | ~4 of 9 (44%) -- inconsistent across pages |
| **Images with width/height attrs** | 2 of 9 (22%) |
| **Images with loading="lazy"** | 0 of 9 (0%) |
| **Images with srcset** | 0 of 9 (0%) |
| **Images using WebP/AVIF** | 0 of 9 (0%) |
| **Images using `<picture>` element** | 0 of 9 (0%) |
| **Images with fetchpriority** | 0 of 9 (0%) |
| **Images with decoding attribute** | 0 of 9 (0%) |
| **Pages with zero visible content images** | 3 of 5 (60%) |
| **Generic/camera-default file names** | 2 of 5 content images (Image-282.jpg, *_16.jpg) |

---

## Consolidated Findings by Severity

### 🔴 Critical (10 findings)

| # | Finding | Pages Affected | Impact |
|---|---------|---------------|--------|
| C1 | 3 pages have zero visible content images (spa, restaurants, activities) | 3 | Users see no photos; zero image search traffic; poor conversion |
| C2 | Hero images missing alt text | Homepage, Accommodation, Activities | Accessibility violation (WCAG 2.1 A); lost SEO keyword signals |
| C3 | No activity card images | Activities | Text-only activity listings hurt conversion |
| C4 | No accommodation listing images | Accommodation | Accommodation page without room photos |
| C5 | No restaurant/food images | Restaurants | Restaurant page without food photos |
| C6 | No spa facility images | Spa | Spa page without spa photos |
| C7 | Generic file name "Image-282.jpg" | Accommodation | Zero SEO value in file name |
| C8 | Oversized metadata image (2048x2560) | Spa | Unnecessary bandwidth for social/SEO crawlers |
| C9 | Hero images exist only in metadata | Spa, Restaurants, Activities | Schema references images not visible to users -- potential schema/content mismatch penalty |
| C10 | No `<picture>` elements anywhere | All 5 | Cannot serve modern formats with fallbacks |

### 🟠 High (4 findings)

| # | Finding | Pages Affected | Impact |
|---|---------|---------------|--------|
| H1 | No srcset/responsive images | All images | All devices download full-size images; wasted bandwidth on mobile |
| H2 | No WebP/AVIF formats used | All images | 25-35% potential file size savings missed |
| H3 | No width/height on most images | All 5 | Cumulative Layout Shift (CLS) during page load |
| H4 | Green Key badge alt text inconsistent | All 5 | Sometimes "Greenkey", sometimes missing |

### 🟡 Medium (4 findings)

| # | Finding | Pages Affected | Impact |
|---|---------|---------------|--------|
| M1 | No `loading="lazy"` on below-fold images | All 5 | Footer images (logos, Green Key badge) load immediately |
| M2 | No `fetchpriority="high"` on hero images | Homepage, Accommodation | LCP optimization missed |
| M3 | PNG logos could be SVG or WebP | All 5 | Slightly larger file sizes than necessary |
| M4 | File names include resolution prefixes/camera numbers | Activities, Homepage | Diluted SEO value |

### 🟢 Low (2 findings)

| # | Finding | Pages Affected | Impact |
|---|---------|---------------|--------|
| L1 | CSS background images correctly use SVG | All 5 | No issue -- good practice |
| L2 | Finnish file names on English pages | Restaurants | Minor SEO impact for English search |

---

## Prioritized Fix List

### Priority 1: Content Crisis (Week 1)

These are not just image optimization issues -- they are fundamental content gaps.

1. **Add visible hero images to spa, restaurants, and activities pages**
   - These pages reference images in metadata but do not render them in HTML
   - Add `<img>` tags with proper alt text, width/height, and fetchpriority
   - Effort: Low (images already exist in media library)

2. **Add content images throughout all pages**
   - Accommodation: Add photos for each room/cabin type
   - Spa: Add pool, sauna, treatment room photos
   - Restaurants: Add food, dining room, fire kitchen photos
   - Activities: Add photo to each activity card
   - Effort: Medium (requires photo selection and implementation)

3. **Add alt text to ALL images**
   - Use descriptive, keyword-rich alt text
   - Example: `alt="winter sleigh ride under starry sky at Jarvisydan resort, Finnish Lakeland"`
   - Effort: Low

### Priority 2: Technical Optimization (Week 2)

4. **Add width and height attributes to all `<img>` tags**
   - Prevents CLS; improves Core Web Vitals
   - Effort: Low

5. **Implement `<picture>` elements with WebP**
   - Convert all JPG/PNG content images to WebP
   - Use `<picture>` with `<source type="image/webp">` and JPG fallback
   - WordPress plugins (e.g., ShortPixel, Imagify) can automate this
   - Effort: Low with plugin; Medium if manual

6. **Add srcset and sizes attributes**
   - Generate responsive variants (640w, 1024w, 1920w minimum)
   - Add appropriate `sizes` attribute based on layout
   - Effort: Medium

### Priority 3: Performance Fine-Tuning (Week 3)

7. **Add `loading="lazy"` to below-fold images**
   - Footer logos, Green Key badge, any below-fold content images
   - Do NOT lazy-load above-fold hero images
   - Effort: Low

8. **Add `fetchpriority="high"` to hero/LCP images**
   - Improves Largest Contentful Paint timing
   - Effort: Low

9. **Rename generic file names**
   - `Image-282.jpg` -> `jarvisydan-lakeside-hotel-accommodation.jpg`
   - Remove resolution prefixes and camera numbers from file names
   - Effort: Low (but requires redirect from old URLs)

10. **Resize oversized images**
    - `Spa-7-scaled.jpg` at 2048x2560 is unnecessarily large
    - Cap hero images at 1920px wide max
    - Effort: Low

### Priority 4: Advanced (Week 4+)

11. **Consider AVIF format** for browsers that support it (Chrome, Firefox)
12. **Implement image CDN** (e.g., Cloudflare Polish, imgix) for automatic optimization
13. **Add structured data images** that match visible page content
14. **Create image sitemap** for Google Image Search indexing

---

## WordPress-Specific Recommendations

The site runs on WordPress with a custom "Digitaali" theme. Several quick wins are available:

| Action | Implementation | Effort |
|--------|---------------|--------|
| Auto-WebP conversion | Install ShortPixel or Imagify plugin | 15 min |
| Auto lazy loading | WordPress 5.5+ has native lazy loading -- verify it is not disabled by theme | 5 min |
| Auto srcset | WordPress generates srcset by default since 4.4 -- theme may be overriding this | 30 min investigation |
| Alt text enforcement | Use plugin like "Alt Text Tools" to flag missing alt text | 10 min |
| Image compression | Use Smush or ShortPixel to bulk-compress existing images | 30 min |

**Critical theme issue:** The Digitaali theme appears to suppress WordPress's built-in responsive image features (srcset/sizes) and native lazy loading. This should be investigated in the theme's `functions.php` file.

---

## Estimated Impact of Fixes

| Metric | Current | After Fixes | Improvement |
|--------|---------|-------------|-------------|
| Image SEO Score | 18/100 | 75-85/100 | +57-67 points |
| Google Image Search visibility | Near zero | Moderate | Significant new traffic source |
| Core Web Vitals (CLS) | Poor | Good | Fewer layout shifts |
| Core Web Vitals (LCP) | Suboptimal | Improved | Faster hero image loading |
| Page weight (mobile) | Unoptimized | 30-40% lighter | Faster load times |
| Accessibility compliance | Failing | WCAG 2.1 A compliant | Legal risk reduction |
| Conversion rate | Impacted by missing visuals | Improved | Better visual storytelling |

---

*Report generated 2026-02-11 by automated image SEO audit.*
*Next recommended audit: After implementing Priority 1-2 fixes (target: 2-3 weeks).*
