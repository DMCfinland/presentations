# Schema / Structured Data Audit: jarvisydan.com

**Audit Date:** 2026-02-11
**Auditor:** Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy
**Site:** https://www.jarvisydan.com/en/
**Business:** Hotel & Spa Resort Jarvisydan, Rantasalmi, Finland

---

## Executive Summary

Jarvisydan.com has **minimal structured data** generated automatically by an SEO plugin (likely Yoast SEO for WordPress). The existing markup covers only basic WebPage, BreadcrumbList, WebSite, Organization, and ImageObject types -- all generic schemas that provide no hotel, restaurant, spa, or tourism-specific information to search engines.

**The site is missing every business-critical schema type** expected for a luxury lakeside resort: Hotel, LodgingBusiness, Restaurant, HealthAndBeautyBusiness (spa), TouristAttraction, and SearchAction. This means Google cannot generate rich results for accommodations, dining, activities, or business information from this site.

The Organization schema is incomplete (missing address, phone, geo coordinates, description). The WebSite schema lacks SearchAction for sitelinks search box eligibility. No page carries any schema with pricing, reviews, amenities, or operational hours.

Implementing the recommended schemas below would unlock rich results in Google Search for hotels, restaurants, local businesses, and tourism -- directly impacting click-through rates and visibility for high-intent travel queries.

---

## Schema Audit Score: 18 / 100

| Category | Max Points | Score | Notes |
|----------|-----------|-------|-------|
| Core Business Schema (Hotel/LodgingBusiness) | 25 | 0 | Completely missing |
| Organization / LocalBusiness | 15 | 4 | Present but severely incomplete |
| Restaurant Schema | 15 | 0 | Completely missing |
| BreadcrumbList | 10 | 8 | Present on most pages, minor issues |
| WebSite + SearchAction | 10 | 3 | WebSite present, SearchAction missing |
| Spa / HealthAndBeautyBusiness | 10 | 0 | Completely missing |
| TouristAttraction / Activities | 10 | 0 | Completely missing |
| WebPage metadata quality | 5 | 3 | Present but basic |

---

## Per-Page Analysis

---

### Page 1: Homepage (`/en/`)

#### Existing Schemas

| Schema Type | Status | Assessment |
|-------------|--------|------------|
| WebPage | Present | Basic -- missing `description` property |
| ImageObject | Present | OK -- has url, width, height |
| BreadcrumbList | Present | Only 1 item (home), no `item` URL -- valid but minimal |
| WebSite | Present | Missing `potentialAction` (SearchAction) |
| Organization | Present | Missing address, phone, geo, description, foundingDate |

#### Findings

- **🔴 Critical -- No Hotel or LodgingBusiness schema.** The homepage represents a hotel and spa resort but carries zero hospitality-specific structured data. Google cannot identify this as a hotel for rich results.

- **🔴 Critical -- Organization schema severely incomplete.** Contains only name, URL, logo, and sameAs. Missing: address, telephone, email, geo coordinates, description, priceRange, openingHours. Logo dimensions are 1x1 pixel (likely SVG rendering issue but still problematic for validators).

- **🟠 High -- WebSite missing SearchAction.** Without `potentialAction` with SearchAction, the site is ineligible for Google's sitelinks search box.

- **🟡 Medium -- WebPage missing description.** The `description` property should mirror or complement the meta description for enhanced crawl understanding.

- **🟡 Medium -- BreadcrumbList has only 1 item with no URL.** Home-only breadcrumb with missing `item` property. While technically valid, it provides minimal value.

#### Missing Schemas for Homepage

**🔴 Hotel Schema (Critical)**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "@id": "https://www.jarvisydan.com/#hotel",
  "name": "Hotel & Spa Resort Jarvisydan",
  "description": "Luxury lakeside hotel and spa resort on the shores of Lake Saimaa in Rantasalmi, Finland. Year-round destination offering themed suites, villa accommodation, Lake Spa, fine dining at Restaurant Solitary, and seasonal nature activities in the Finnish Lakeland.",
  "url": "https://www.jarvisydan.com/en/",
  "telephone": "+358600413160",
  "email": "jarvisydan@jarvisydan.fi",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 62.0456,
    "longitude": 28.3667
  },
  "image": [
    "https://www.jarvisydan.com/wp-content/uploads/2024/01/Winter-Activities-2-14.jpg",
    "https://www.jarvisydan.com/wp-content/uploads/2022/08/Image-282.jpg"
  ],
  "priceRange": "$$$$",
  "starRating": {
    "@type": "Rating",
    "ratingValue": "4"
  },
  "amenityFeature": [
    { "@type": "LocationFeatureSpecification", "name": "Lake Spa", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Indoor Pool", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Outdoor Pool", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Sauna", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Restaurant", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Bar", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Free Parking", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Free WiFi", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Room Service", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Pet Friendly", "value": true }
  ],
  "checkinTime": "15:00",
  "checkoutTime": "11:00",
  "numberOfRooms": 50,
  "petsAllowed": true,
  "containsPlace": [
    { "@type": "Restaurant", "name": "Restaurant Solitary" },
    { "@type": "Restaurant", "name": "Wine Cellar Fire Kitchen" },
    { "@type": "Restaurant", "name": "Restaurant Piikatytto" },
    { "@type": "HealthAndBeautyBusiness", "name": "Lake Spa" }
  ],
  "sameAs": [
    "https://www.facebook.com/Jarvisydan/",
    "https://x.com/jarvisydan",
    "https://www.instagram.com/jarvisydan/",
    "https://www.youtube.com/c/jarvisydan",
    "https://www.linkedin.com/company/holiday-resort-j-rvisyd-n"
  ]
}
</script>
```

> **Note:** Verify and adjust: `latitude`/`longitude` (approximate values used -- confirm from Google Maps), `numberOfRooms` (estimated), `checkinTime`/`checkoutTime` (confirm actual times), `starRating` (confirm official rating), and `petsAllowed` (confirm policy). Remove `amenityFeature` items that do not apply.

**🟠 Enhanced WebSite with SearchAction**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://www.jarvisydan.com/#website",
  "name": "Hotel & Spa Resort Jarvisydan",
  "url": "https://www.jarvisydan.com/",
  "inLanguage": ["en-US", "fi"],
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.jarvisydan.com/?s={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
</script>
```

> **Note:** Verify the search URL pattern. WordPress default is `/?s={query}`. If the site uses a different search URL structure, adjust `urlTemplate` accordingly.

**🟠 Enhanced Organization Schema**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.jarvisydan.com/#organization",
  "name": "Hotel & Spa Resort Jarvisydan",
  "legalName": "Jarvisydan Oy",
  "url": "https://www.jarvisydan.com/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://www.jarvisydan.com/wp-content/uploads/2023/01/logo.svg",
    "width": 250,
    "height": 60
  },
  "image": "https://www.jarvisydan.com/wp-content/uploads/2024/01/Winter-Activities-2-14.jpg",
  "description": "Hotel & Spa Resort Jarvisydan is a luxury lakeside resort on the shores of Lake Saimaa, offering accommodation, fine dining, spa services, and nature activities year-round.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressRegion": "South Savo",
    "addressCountry": "FI"
  },
  "telephone": "+358600413160",
  "email": "jarvisydan@jarvisydan.fi",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 62.0456,
    "longitude": 28.3667
  },
  "sameAs": [
    "https://www.facebook.com/Jarvisydan/",
    "https://x.com/jarvisydan",
    "https://www.instagram.com/jarvisydan/",
    "https://www.youtube.com/c/jarvisydan",
    "https://www.linkedin.com/company/holiday-resort-j-rvisyd-n"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+358600413160",
    "contactType": "reservations",
    "email": "jarvisydan@jarvisydan.fi",
    "availableLanguage": ["Finnish", "English"]
  }
}
</script>
```

> **Note:** Verify `legalName` (company registration name), geo coordinates, and logo pixel dimensions. The SVG logo should still have reasonable declared dimensions.

---

### Page 2: Accommodation (`/en/accommodation/`)

#### Existing Schemas

| Schema Type | Status | Assessment |
|-------------|--------|------------|
| WebPage | Present | Basic -- no description |
| ImageObject | Present | OK |
| BreadcrumbList | Present | 2 items, proper hierarchy |
| Organization | Present | Same incomplete version as homepage |

#### Findings

- **🔴 Critical -- No Hotel or LodgingBusiness schema.** This is the primary accommodation page and should carry the most detailed Hotel schema with room types and offers.

- **🔴 Critical -- No Room/Suite/Offer schemas.** Individual accommodation types (themed suites, hotel rooms, villas) are not marked up. Google Hotel search cannot parse room availability or pricing from this page.

- **🟡 Medium -- No Product or Offer schema for holiday packages.** Packages with pricing are mentioned on the page but not structured for rich results.

#### Missing Schemas for Accommodation Page

**🔴 Hotel with Accommodation Offers**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Hotel",
  "@id": "https://www.jarvisydan.com/#hotel",
  "name": "Hotel & Spa Resort Jarvisydan",
  "description": "Lakeside resort accommodation on Lake Saimaa featuring themed suites, hotel rooms, and private villas surrounded by Finnish nature.",
  "url": "https://www.jarvisydan.com/en/accommodation/",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "telephone": "+358600413160",
  "checkinTime": "15:00",
  "checkoutTime": "11:00",
  "makesOffer": [
    {
      "@type": "Offer",
      "name": "Themed Suite",
      "description": "Individually designed themed suites with unique Finnish lakeland character",
      "url": "https://www.jarvisydan.com/en/accommodation/",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "unitText": "night"
      }
    },
    {
      "@type": "Offer",
      "name": "Hotel Room",
      "description": "Comfortable hotel rooms at the lakeside resort",
      "url": "https://www.jarvisydan.com/en/accommodation/",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "unitText": "night"
      }
    },
    {
      "@type": "Offer",
      "name": "Villa Accommodation",
      "description": "Private villas with lake views and sauna, ideal for families and groups",
      "url": "https://www.jarvisydan.com/en/accommodation/",
      "priceCurrency": "EUR",
      "priceSpecification": {
        "@type": "UnitPriceSpecification",
        "unitText": "night"
      }
    }
  ]
}
</script>
```

> **Note:** Add specific `price` values to each Offer once confirmed (e.g., `"price": "264"` for the starting rate). Adjust room type names and descriptions to match exact categories on the website.

---

### Page 3: Spa (`/en/spa/` -- redirects to `/en/lomapaketit/spa-holiday/`)

#### Existing Schemas

| Schema Type | Status | Assessment |
|-------------|--------|------------|
| WebPage | Present | Basic -- no description |
| ImageObject | Present | OK |
| BreadcrumbList | Present | 3 items, but breadcrumb uses Finnish "Lomapaketit" in English URL path |
| WebSite | Present | Same basic version |
| Organization | Present | Same incomplete version |

#### Findings

- **🔴 Critical -- No HealthAndBeautyBusiness or DaySpa schema.** The Lake Spa is a flagship attraction but has zero structured data identifying it as a spa business. Google cannot generate spa-related rich results.

- **🟠 High -- Breadcrumb language mismatch.** The breadcrumb item "Lomapaketit" is Finnish but the page is served at an English URL path. This creates inconsistency for crawlers parsing the English version.

- **🟠 High -- Spa page redirects to a holiday package.** The `/en/spa/` URL does not serve a standalone spa page -- it redirects to a package offer. This limits schema opportunities and confuses the information architecture. A dedicated spa landing page would better serve structured data and user intent.

- **🟡 Medium -- No Offer schema for spa package.** The 2-night Spa Holiday package (from EUR 264/night) is not marked up as an Offer.

#### Missing Schemas for Spa

**🔴 HealthAndBeautyBusiness (Lake Spa)**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HealthAndBeautyBusiness",
  "@id": "https://www.jarvisydan.com/#lakespa",
  "name": "Lake Spa at Jarvisydan",
  "description": "A unique Lake Spa on the shores of Lake Saimaa featuring gentle saunas, heated Seal stones, indoor and outdoor pools, and yoga and wellbeing classes. Part of Hotel & Spa Resort Jarvisydan.",
  "url": "https://www.jarvisydan.com/en/spa/",
  "image": "https://www.jarvisydan.com/wp-content/uploads/2023/03/Spa-7-scaled.jpg",
  "telephone": "+358600413160",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 62.0456,
    "longitude": 28.3667
  },
  "priceRange": "$$$",
  "parentOrganization": {
    "@type": "Hotel",
    "@id": "https://www.jarvisydan.com/#hotel"
  },
  "amenityFeature": [
    { "@type": "LocationFeatureSpecification", "name": "Indoor Pool", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Outdoor Pool", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Sauna", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Heated Seal Stones", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Yoga Classes", "value": true },
    { "@type": "LocationFeatureSpecification", "name": "Wellbeing Treatments", "value": true }
  ],
  "makesOffer": {
    "@type": "Offer",
    "name": "2-Night Spa Holiday",
    "description": "Accommodation, buffet breakfast, spa entrance, and one activity included",
    "price": "264",
    "priceCurrency": "EUR",
    "priceSpecification": {
      "@type": "UnitPriceSpecification",
      "price": "264",
      "priceCurrency": "EUR",
      "unitText": "per night, minimum 2 nights"
    },
    "url": "https://www.jarvisydan.com/en/lomapaketit/spa-holiday/"
  }
}
</script>
```

> **Note:** Verify geo coordinates, confirm amenity list matches actual facilities, and update the price if it has changed. Add `openingHoursSpecification` once opening hours are confirmed.

---

### Page 4: Restaurants (`/en/restaurants/`)

#### Existing Schemas

| Schema Type | Status | Assessment |
|-------------|--------|------------|
| WebPage | Present | Basic -- no description |
| ImageObject | Present | OK |
| BreadcrumbList | Present | 2 items, proper hierarchy |
| WebSite | Present | Same basic version |
| Organization | Present | Same incomplete version |

#### Findings

- **🔴 Critical -- No Restaurant schema for any of the 6 dining venues.** This page describes Restaurant Solitary (ranked 9th best restaurant in Finland), Wine Cellar Fire Kitchen, Restaurant Piikatytto, Bistro a la Carte, Lotja Music Bar, and Savonian Kota Restaurant. None have Restaurant structured data. This is a major missed opportunity, especially for Solitary which has national recognition.

- **🟠 High -- No Menu schema.** Menu links exist (including external link to menus page) but are not marked up with structured data.

- **🟠 High -- No reservations action.** The restaurant uses bokabord.se for reservations but there is no `potentialAction` with ReserveAction schema.

- **🟡 Medium -- No price range indicators.** Restaurant Solitary shows prices (EUR 64-94 for 3/5-course menus) but these are not in structured data.

#### Missing Schemas for Restaurants Page

**🔴 Restaurant Schema -- Restaurant Solitary**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://www.jarvisydan.com/#solitary",
  "name": "Restaurant Solitary",
  "description": "Ranked 9th best restaurant in Finland. Fine dining experience offering 3-course and 5-course surprise menus featuring local and seasonal ingredients from the Finnish Lakeland.",
  "url": "https://www.jarvisydan.com/en/restaurants/",
  "image": "https://www.jarvisydan.com/wp-content/uploads/2024/03/Illallinen-tulikeittio.jpg",
  "telephone": "+358600413160",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 62.0456,
    "longitude": 28.3667
  },
  "servesCuisine": ["Finnish", "Nordic", "Fine Dining"],
  "priceRange": "$$$$",
  "menu": "https://www.jarvisydan.com/en/restaurants/menus/",
  "acceptsReservations": "True",
  "potentialAction": {
    "@type": "ReserveAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://app.bokabord.se/reservation/",
      "actionPlatform": [
        "http://schema.org/DesktopWebPlatform",
        "http://schema.org/MobileWebPlatform"
      ]
    }
  },
  "parentOrganization": {
    "@type": "Hotel",
    "@id": "https://www.jarvisydan.com/#hotel"
  },
  "hasMenu": {
    "@type": "Menu",
    "name": "Restaurant Solitary Menu",
    "hasMenuSection": [
      {
        "@type": "MenuSection",
        "name": "Surprise Menus",
        "hasMenuItem": [
          {
            "@type": "MenuItem",
            "name": "3-Course Surprise Menu",
            "offers": {
              "@type": "Offer",
              "price": "64",
              "priceCurrency": "EUR"
            }
          },
          {
            "@type": "MenuItem",
            "name": "5-Course Surprise Menu",
            "offers": {
              "@type": "Offer",
              "price": "94",
              "priceCurrency": "EUR"
            }
          }
        ]
      }
    ]
  }
}
</script>
```

> **Note:** Verify exact prices (may be seasonal). Add `openingHoursSpecification` when available. If Solitary has its own dedicated image, replace the generic restaurant page image.

**🔴 Restaurant Schema -- Wine Cellar Fire Kitchen**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://www.jarvisydan.com/#firecellar",
  "name": "Wine Cellar Fire Kitchen",
  "description": "Daily dinner service featuring local and seasonal ingredients prepared in an open fire kitchen at Hotel & Spa Resort Jarvisydan.",
  "url": "https://www.jarvisydan.com/en/restaurants/",
  "telephone": "+358600413160",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "servesCuisine": ["Finnish", "Nordic", "Open Fire Cooking"],
  "priceRange": "$$$",
  "acceptsReservations": "True",
  "parentOrganization": {
    "@type": "Hotel",
    "@id": "https://www.jarvisydan.com/#hotel"
  }
}
</script>
```

**🟠 Restaurant Schema -- Restaurant Piikatytto**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://www.jarvisydan.com/#piikatytto",
  "name": "Restaurant Piikatytto",
  "description": "Breakfast and lunch restaurant with summer terrace at Hotel & Spa Resort Jarvisydan on Lake Saimaa.",
  "url": "https://www.jarvisydan.com/en/restaurants/",
  "telephone": "+358600413160",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "servesCuisine": ["Finnish", "Breakfast", "Lunch"],
  "priceRange": "$$",
  "parentOrganization": {
    "@type": "Hotel",
    "@id": "https://www.jarvisydan.com/#hotel"
  }
}
</script>
```

**🟠 Restaurant Schema -- Bistro a la Carte**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "@id": "https://www.jarvisydan.com/#bistro",
  "name": "Bistro a la Carte",
  "description": "A la carte dining featuring Finnish forest and lake specialties at Hotel & Spa Resort Jarvisydan.",
  "url": "https://www.jarvisydan.com/en/restaurants/",
  "telephone": "+358600413160",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "servesCuisine": ["Finnish", "Nordic"],
  "priceRange": "$$$",
  "acceptsReservations": "True",
  "parentOrganization": {
    "@type": "Hotel",
    "@id": "https://www.jarvisydan.com/#hotel"
  }
}
</script>
```

**🟡 BarOrNightClub Schema -- Lotja Music Bar**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BarOrNightClub",
  "@id": "https://www.jarvisydan.com/#lotja",
  "name": "Lotja Music Bar",
  "description": "Bar and karaoke venue serving pasta, burgers, and salads at Hotel & Spa Resort Jarvisydan.",
  "url": "https://www.jarvisydan.com/en/restaurants/",
  "telephone": "+358600413160",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Porosalmentie 313",
    "addressLocality": "Rantasalmi",
    "postalCode": "58900",
    "addressCountry": "FI"
  },
  "priceRange": "$$",
  "parentOrganization": {
    "@type": "Hotel",
    "@id": "https://www.jarvisydan.com/#hotel"
  }
}
</script>
```

---

### Page 5: Activities (`/en/activities/`)

#### Existing Schemas

| Schema Type | Status | Assessment |
|-------------|--------|------------|
| WebPage | Present | Has `description` -- best of all pages |
| ImageObject | Present | OK -- 1920x1080 |
| BreadcrumbList | Present | 2 items, proper hierarchy |

#### Findings

- **🔴 Critical -- No TouristAttraction or TouristDestination schema.** Activities page describes numerous bookable experiences (seal watching, national park excursions, stargazing, yoga) but none are marked up. This is a major loss for tourism-related search visibility.

- **🟠 High -- No Offer schemas for individual activities.** Multiple activities with specific prices are listed (e.g., Seal Watching Trip EUR 89, National Park Excursion EUR 34.90, Stargazing EUR 59.90) but none are structured for rich results.

- **🟡 Medium -- No Event schema for seasonal activities.** Seasonal activities (summer cruises May-October, winter sleigh rides) could benefit from Event schema with date ranges.

#### Missing Schemas for Activities Page

**🔴 TouristDestination with TouristAttraction Items**

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TouristDestination",
  "@id": "https://www.jarvisydan.com/#destination",
  "name": "Jarvisydan Nature Activities, Lake Saimaa",
  "description": "Seasonal activities throughout the year in the Finnish Lakeland. Seal watching, national park excursions, stargazing tours, yoga, fishing safaris, and more on the shores of Lake Saimaa.",
  "url": "https://www.jarvisydan.com/en/activities/",
  "image": "https://www.jarvisydan.com/wp-content/uploads/2025/01/1920-Tahtitaivaan-rekiretki_16.jpg",
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 62.0456,
    "longitude": 28.3667
  },
  "touristType": ["Nature Lovers", "Wellness Travelers", "Adventure Seekers", "Families"],
  "includesAttraction": [
    {
      "@type": "TouristAttraction",
      "name": "Saimaa Seal Watching Trip",
      "description": "Guided boat trip to observe the endangered Saimaa ringed seal in its natural habitat on Lake Saimaa.",
      "touristType": "Nature Lovers",
      "offers": {
        "@type": "Offer",
        "price": "89",
        "priceCurrency": "EUR",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "89",
          "priceCurrency": "EUR",
          "unitText": "per adult"
        }
      }
    },
    {
      "@type": "TouristAttraction",
      "name": "Excursion to Linnansaari National Park",
      "description": "Guided nature excursion to Linnansaari National Park, one of the most beautiful natural areas in the Finnish Lakeland.",
      "touristType": "Nature Lovers",
      "offers": {
        "@type": "Offer",
        "price": "34.90",
        "priceCurrency": "EUR",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "34.90",
          "priceCurrency": "EUR",
          "unitText": "per adult"
        }
      }
    },
    {
      "@type": "TouristAttraction",
      "name": "Stargazing Hiking Tour",
      "description": "Guided evening hike through the Finnish forest with stargazing in one of Europe's darkest sky areas.",
      "touristType": "Nature Lovers",
      "offers": {
        "@type": "Offer",
        "price": "59.90",
        "priceCurrency": "EUR",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "59.90",
          "priceCurrency": "EUR",
          "unitText": "per adult"
        }
      }
    },
    {
      "@type": "TouristAttraction",
      "name": "Fishing Safari",
      "description": "Guided fishing experience on Lake Saimaa with professional equipment and local expertise.",
      "touristType": "Adventure Seekers",
      "offers": {
        "@type": "Offer",
        "price": "120",
        "priceCurrency": "EUR",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "120",
          "priceCurrency": "EUR",
          "unitText": "per person"
        }
      }
    },
    {
      "@type": "TouristAttraction",
      "name": "Yoga & Wellbeing at Kuru",
      "description": "Warm yoga, morning yoga, and siesta relaxation sessions in a peaceful lakeside setting.",
      "touristType": "Wellness Travelers",
      "offers": {
        "@type": "Offer",
        "price": "24",
        "priceCurrency": "EUR",
        "priceSpecification": {
          "@type": "UnitPriceSpecification",
          "price": "24",
          "priceCurrency": "EUR",
          "unitText": "per session"
        }
      }
    }
  ]
}
</script>
```

> **Note:** Verify all prices are current. Add seasonal availability if known (e.g., seal watching only May-September). Adjust activity names and descriptions to match exact wording on the website.

---

## Cross-Site Issues

### 🔴 Critical Issues (Affect All Pages)

1. **No Hotel/LodgingBusiness schema anywhere on the site.** Google has no structured way to identify this website as representing a hotel. This blocks eligibility for hotel-specific rich results, Google Hotels integration, and hospitality knowledge panels.

2. **Organization schema missing core properties.** Address, telephone, email, geo coordinates, and description are absent from the Organization entity that appears on every page. This weakens local SEO signals and knowledge graph matching.

3. **No Restaurant schema on any page.** Six dining venues including a nationally ranked fine dining restaurant have zero structured data. Google cannot surface restaurant information in search results.

### 🟠 High Issues

4. **WebSite schema lacks SearchAction.** The site is ineligible for Google's sitelinks search box feature, reducing SERP real estate.

5. **No spa/wellness schema.** The Lake Spa is a primary selling point but is invisible to structured data crawlers.

6. **No activity/attraction schemas.** Bookable experiences with specific prices are not machine-readable.

7. **Logo ImageObject has 1x1 dimensions.** While the SVG itself renders at any size, declaring 1x1 pixel dimensions may cause validation warnings and suboptimal display in rich results.

### 🟡 Medium Issues

8. **Breadcrumb language inconsistency.** The spa page breadcrumb uses Finnish "Lomapaketit" on an English-language URL path.

9. **Most WebPage entities lack `description`.** Only the activities page includes a description property. All other pages omit it.

10. **No `inLanguage` on all BreadcrumbList items.** While not required, declaring language helps multilingual site crawling.

### 🟢 Low Issues

11. **No `dateCreated` on Organization.** Adding founding information can enrich knowledge panel data.

12. **LinkedIn not included in sameAs on all pages.** The LinkedIn URL appears on the site footer but is missing from some page-level Organization sameAs arrays.

---

## Implementation Priority List

| Priority | Schema Type | Page(s) | Effort | Impact |
|----------|------------|---------|--------|--------|
| 1 | Hotel (with amenities, rooms, contact) | Homepage, Accommodation | High | 🔴 Critical -- unlocks hotel rich results |
| 2 | Organization (complete with address, geo, contact) | All pages (update existing) | Low | 🔴 Critical -- fixes local SEO foundation |
| 3 | Restaurant (Solitary with Menu) | Restaurants | Medium | 🔴 Critical -- nationally ranked restaurant |
| 4 | Restaurant (Wine Cellar, Piikatytto, Bistro) | Restaurants | Medium | 🟠 High -- additional dining venues |
| 5 | WebSite + SearchAction | Homepage | Low | 🟠 High -- sitelinks search box eligibility |
| 6 | HealthAndBeautyBusiness (Lake Spa) | Spa page | Medium | 🟠 High -- key differentiator |
| 7 | TouristDestination + TouristAttraction | Activities | Medium | 🟠 High -- tourism search visibility |
| 8 | BarOrNightClub (Lotja) | Restaurants | Low | 🟡 Medium -- completes venue coverage |
| 9 | Offer schemas for packages | Accommodation, Spa | Low | 🟡 Medium -- enables price rich results |
| 10 | Fix logo dimensions | All pages | Low | 🟢 Low -- validation cleanup |

---

## Technical Implementation Notes

### WordPress / Yoast SEO Context

The existing schemas are generated by Yoast SEO (or a similar WordPress SEO plugin) using the `@graph` pattern. When implementing custom schemas:

1. **Option A -- Extend the Yoast graph.** Use Yoast's Schema API (`woocommerce_structured_data` filter or `wpseo_schema_graph_pieces` filter) to add custom graph pieces. This keeps all structured data in one clean `@graph` array.

2. **Option B -- Add separate JSON-LD blocks.** Add custom `<script type="application/ld+json">` blocks via a custom plugin, theme functions.php, or a tag manager. The schemas above are written for this approach. Google handles multiple JSON-LD blocks per page correctly.

3. **Option C -- Use a dedicated schema plugin.** Plugins like "Schema Pro" or "WP Schema" can add business-specific schemas through a UI without code changes.

**Recommendation:** Option B is the most practical for a non-developer team -- the JSON-LD blocks above can be inserted via Google Tag Manager or a simple "insert headers/footers" WordPress plugin. However, Option A produces the cleanest technical result if developer resources are available.

### Validation

After implementation, validate all schemas using:
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema.org Validator](https://validator.schema.org/)
- Google Search Console "Enhancements" reports (monitor for 2-4 weeks after deployment)

### Important Caveats on Provided JSON-LD

All JSON-LD code blocks above are **ready-to-use templates** but require verification of:
- **Geo coordinates** -- approximate values (62.0456, 28.3667) were used. Confirm exact coordinates from Google Maps.
- **Prices** -- all prices were extracted from page content at audit time. Confirm they are current.
- **Check-in/check-out times** -- 15:00/11:00 are standard assumptions. Confirm actual times.
- **Number of rooms** -- estimated at 50. Replace with actual count.
- **Star rating** -- assumed 4 stars. Replace with official rating or remove if no official star classification.
- **Pet policy** -- assumed pet-friendly. Confirm or remove.
- **Opening hours** -- not included as they were not available on any page. Add `openingHoursSpecification` to Restaurant and Spa schemas once confirmed.

---

## Summary Scorecard

| What Google Can Currently Understand | Status |
|--------------------------------------|--------|
| This is a website | Yes |
| This is a hotel / accommodation business | No |
| This site has restaurants | No |
| This site has a spa | No |
| Business address and location | No |
| Business phone number | No |
| Room types and prices | No |
| Restaurant menus and prices | No |
| Activities and experiences | No |
| Breadcrumb navigation structure | Yes (partial) |
| Social media profiles | Yes |
| Site search capability | No |

**Bottom line:** Search engines currently see jarvisydan.com as a generic website with an organization name and social links. They cannot identify it as a hotel, cannot surface restaurant information, cannot show spa details, and cannot display activity pricing. Implementing the schemas above would transform this site's search presence from invisible to rich-result eligible across every major service category the resort offers.
