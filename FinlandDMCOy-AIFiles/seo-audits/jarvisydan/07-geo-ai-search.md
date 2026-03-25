# GEO & AI Search Readiness Audit: jarvisydan.com

**Audit Date:** 2026-02-11
**Auditor:** Claude Code (Opus 4.6) for Finland DMC Oy / 1658 Holdings Oy
**Site:** https://www.jarvisydan.com/en/
**Business:** Hotel & Spa Resort Jarvisydan, Rantasalmi, Lake Saimaa, Finnish Lakeland
**Pages Analyzed:**
- Homepage: `/en/`
- Activities: `/en/activities/`
- Restaurants: `/en/restaurants/`

---

## GEO Readiness Score: 34/100

| Category | Score | Status |
|----------|-------|--------|
| AI Crawler Access | 5/15 | Poor |
| llms.txt & AI Discoverability | 0/10 | Missing |
| Passage-Level Citability | 8/25 | Poor |
| Brand & Entity Presence | 10/20 | Mixed |
| Server-Side Rendering | 12/15 | Good |
| Platform-Specific Readiness | 7/15 | Needs Work |

---

## 1. AI Crawler Access Status

**robots.txt URL:** https://www.jarvisydan.com/robots.txt

**Current content:**
```
# This space intentionally left blank
User-Agent: *
```

### AI Bot Access Matrix

| Bot | Owner | Purpose | Status | Notes |
|-----|-------|---------|--------|-------|
| GPTBot | OpenAI | Training & search | Allowed (default) | No explicit rule |
| OAI-SearchBot | OpenAI | ChatGPT search | Allowed (default) | No explicit rule |
| ChatGPT-User | OpenAI | Live browsing | Allowed (default) | No explicit rule |
| ClaudeBot | Anthropic | Training | Allowed (default) | No explicit rule |
| PerplexityBot | Perplexity | Search engine | Allowed (default) | No explicit rule |
| Google-Extended | Google | Gemini training | Allowed (default) | No explicit rule |
| CCBot | Common Crawl | Web corpus | Allowed (default) | No explicit rule |
| Bytespider | ByteDance | Training | Allowed (default) | No explicit rule |
| Googlebot | Google | Search indexing | Allowed (default) | No explicit rule |

**Finding:** All bots are technically allowed because the robots.txt has no Disallow rules at all. However, this is accidental permissiveness, not intentional AI strategy. There are no explicit Allow directives for AI crawlers, no Sitemap reference, and no crawl-delay guidance.

- Severity: **High**
- The lack of a Sitemap directive means AI crawlers must discover pages through links alone, reducing the likelihood of comprehensive crawling.

### Recommended robots.txt for AI Search

```
User-Agent: *
Sitemap: https://www.jarvisydan.com/sitemap.xml

# AI Search Bots - Explicitly Welcome
User-Agent: GPTBot
Allow: /

User-Agent: OAI-SearchBot
Allow: /

User-Agent: ChatGPT-User
Allow: /

User-Agent: ClaudeBot
Allow: /

User-Agent: PerplexityBot
Allow: /

User-Agent: Google-Extended
Allow: /

# Block low-value paths
User-Agent: *
Disallow: /wp-admin/
Disallow: /wp-includes/
Disallow: /?s=
Disallow: /haku/
```

---

## 2. llms.txt Status

**URL checked:** https://www.jarvisydan.com/llms.txt
**Status:** 404 Not Found -- does not exist.

- Severity: **Critical**

### What is llms.txt?

The `llms.txt` standard (proposed by Jeremy Howard, llmstxt.org) provides a structured, plain-text summary of a website specifically for LLM consumption. It helps AI systems quickly understand what a business is, what it offers, and how to describe it accurately. Early adopters gain a significant advantage in AI-generated answers.

### Recommended llms.txt

```markdown
# Hotel & Spa Resort Jarvisydan

> Nature Hotel & Spa Resort Jarvisydan is a luxury lakeside hotel, spa,
> and nature experience resort on the shores of Lake Saimaa in Rantasalmi,
> Finnish Lakeland. Heritage dating to 1658. Adjacent to Linnansaari
> National Park.

## Location
- Address: Porosalmentie 313, 58900 Rantasalmi, Finland
- Region: Finnish Lakeland (Savonia), Eastern Finland
- Lake: Lake Saimaa (Europe's 4th largest lake)
- Nearest national park: Linnansaari National Park (adjacent)
- Nearest city: Savonlinna (45 min drive)
- Nearest airport: Savonlinna (SZL, seasonal) or Kuopio (KUO, 2h)

## Accommodation
- Experience Hotel: themed suites with lake views
- Kuru Resort: luxury adults-only villas, 800m from main resort
- Scenery Suites: panoramic lakeside suites
- Panorama Suites: elevated lake views
- Forest Suites: woodland setting
- Houseboats: floating accommodation on Lake Saimaa
- Log Villas: traditional Finnish villas

## Dining
- Wine Cellar Fire Menu: signature fire-kitchen dining, daily
- Restaurant Piikatytto: breakfast and lunch
- Bistro a la Carte: seasonal Finnish cuisine
- Lotja Music Bar: casual dining, live music, karaoke
- Restaurant Solitary (at Kuru): fine dining, 9th best restaurant in Finland 2025, 3-course (64 EUR) / 5-course (94 EUR) surprise menus
- Savonian Kota Restaurant: traditional group dining in forest teepee (24 seats)
- Forest Cafe: nature-based cafe experience

## Spa & Wellness
- Lake Spa: unique spa built over Lake Saimaa
- Day Spa: treatment packages
- Evening Spa: evening wellness sessions
- Rental Saunas: private sauna experiences
- Saunaworld: multiple sauna types
- Wellbeing classes: yoga (warm yoga at 32C), aerial yoga, Tibetan singing bowls

## Activities
- Linnansaari National Park trips
- Saimaa ringed seal watching (May-Aug, 89 EUR adult)
- E-Fatbike rentals and tours
- Cross-country skiing and snowshoeing (winter)
- Kicksled and sleigh rides (winter, 59.90 EUR adult)
- Fishing experiences
- Nature trails and hiking
- Equipment rental: Safari House (Mon-Sat 10-16)

## Key Facts
- Heritage: roots dating to 1658
- Awards: Finland's domestic tourism business of the year 2020
- Adults-only option: Kuru Resort (800m from main resort)
- Year-round operation: activities and accommodation all seasons
- Sustainability: committed to sustainable tourism practices

## Links
- Website: https://www.jarvisydan.com/en/
- Booking: https://book.jarvisydan.com/accommodation
- Kuru booking: https://book.kururesort.com/accommodation
- Facebook: https://www.facebook.com/Jarvisydan/
- Instagram: https://www.instagram.com/jarvisydan/
- YouTube: https://www.youtube.com/user/LomakylaJarvisydan
- LinkedIn: https://www.linkedin.com/company/holiday-resort-j-rvisyd-n
```

---

## 3. Passage-Level Citability Analysis

AI systems (ChatGPT, Perplexity, Gemini AI Overviews) cite content by extracting self-contained passages of approximately 134-167 words. These passages must contain a direct answer, specific facts, and stand alone without surrounding context.

### 3.1 Homepage (`/en/`)

**Citability Score: 3/10**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Self-contained answer blocks (134-167 words) | Weak | Main description is ~90 words, too short for optimal citation |
| Direct answers in first 40-60 words | Partial | "We invite you to visit us on the shores of Lake Saimaa, next to the Linnansaari National Park" -- good location anchor but uses "we" voice |
| Specific facts / data points | Moderate | 1658 heritage, 800m to Kuru, Lake Saimaa, prices from 240 EUR |
| Question-based headings | Missing | Zero question headings; all are marketing ("Sweet dreams in Jarvisydan") |
| Clean H1-H2-H3 hierarchy | Poor | H1 is a poetic tagline ("Stories to be saved in hearts"), not descriptive |
| Tables with comparative data | Missing | No comparison tables (e.g., accommodation types vs. features) |
| Specific claims with attribution | Weak | No citations, awards mentioned only in passing |

**Key Issues:**
- **H1 is unusable by AI** -- "Stories to be saved in hearts Experience the Savonian hospitality" is poetic but tells AI systems nothing about what this business is. Severity: **Critical**
- **No FAQ section** -- Homepage has no question-answer pairs that AI could directly cite. Severity: **High**
- **First-person marketing voice** -- "We invite you" is not citable; AI needs third-person factual statements. Severity: **High**
- **No accommodation comparison table** -- Missing a structured comparison of room types, capacity, prices. Severity: **Medium**

### 3.2 Activities Page (`/en/activities/`)

**Citability Score: 3/10**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Self-contained answer blocks | Weak | Activity descriptions are 1-3 sentences each, far too short |
| Direct answers in first 40-60 words | Weak | Opens with marketing ("Explore Porosalmi trails!"), not factual summary |
| Specific facts / data points | Moderate | Prices (10-690 EUR), yoga at 32C, hours Mon-Sat 10-16 |
| Question-based headings | Missing | No "What activities..." or "Where to..." headings |
| Clean H1-H2-H3 hierarchy | Poor | Two H1 tags on the page (invalid HTML structure) |
| Tables with comparative data | Missing | No seasonal activity table or price comparison |
| Specific claims with attribution | Missing | No sourced claims |

**Key Issues:**
- **Duplicate H1 tags** -- Two H1 elements break heading hierarchy. AI parsers may misidentify the primary topic. Severity: **High**
- **Activity descriptions too thin** -- Each activity has only 1-3 sentences. AI needs 134-167 word passages to cite. Severity: **High**
- **No seasonal activity overview** -- Missing a structured summary of what is available by season (winter vs. summer). Severity: **Medium**
- **No "best of" or "top activities" anchor content** -- AI queries like "best activities Lake Saimaa" have nothing to cite from this page. Severity: **High**

### 3.3 Restaurants Page (`/en/restaurants/`)

**Citability Score: 4/10**

| Criterion | Status | Notes |
|-----------|--------|-------|
| Self-contained answer blocks | Partial | Solitary description approaches citable length (~100 words) |
| Direct answers in first 40-60 words | Partial | Piikatytto and Lotja sections open with clear function statements |
| Specific facts / data points | Good | Prices (64 EUR, 94 EUR), ranking (9th in Finland 2025), capacity (24 seats) |
| Question-based headings | Missing | No question-format headings |
| Clean H1-H2-H3 hierarchy | Acceptable | Single H1, clear H2 per restaurant, but no H3 sub-sections |
| Tables with comparative data | Missing | No restaurant comparison table (cuisine, price range, hours, reservation) |
| Specific claims with attribution | Partial | "9th best restaurant in Finland 2025" -- good but no source named |

**Key Issues:**
- **Best citable content on the site** -- Restaurant Solitary's ranking and pricing are the most AI-friendly data points found. Severity: N/A (positive)
- **Missing attribution for ranking** -- "9th best restaurant in Finland" should cite the source (which ranking/publication). Severity: **Medium**
- **No restaurant comparison table** -- A table with name, cuisine style, price range, reservation required, and hours would be highly citable. Severity: **High**
- **Fire Menu description is vague** -- Uses atmospheric language but no specific menu items, price range, or course count. Severity: **Medium**

---

## 4. Brand & Entity Presence Matrix

### 4.1 Knowledge Graph / Entity Status

| Platform | Status | Details |
|----------|--------|---------|
| Wikipedia (English) | Missing | No English Wikipedia article (404) |
| Wikipedia (Finnish) | Exists | Article at fi.wikipedia.org/wiki/Jarvisydan |
| Wikidata | Exists | Q112112665 -- "spa hotel in Rantasalmi, Finland" |
| Wikimedia Commons | Exists | Category:Jarvisydan |
| Google Knowledge Panel | Likely exists | Wikidata entity + GMB listing would generate one |

- Severity of missing English Wikipedia: **High** -- English-language AI systems (ChatGPT, Perplexity) rely heavily on English Wikipedia for entity grounding. Without it, the hotel is less likely to appear in English-language AI answers about Lake Saimaa or Finnish luxury hotels.

### 4.2 Wikidata Entity Details (Q112112665)

The Wikidata entry contains 16 properties including:
- Instance of (P31): 2 claims
- Country (P17): Finland
- Located in (P131): Rantasalmi
- Coordinates (P625): Present
- Official website (P856): 2 URLs
- Facebook ID (P2013): Present
- Instagram username (P2003): Present
- YouTube channel (P2397): Present
- Address (P6375): Present
- Body of water (P206): Lake Saimaa

**Assessment:** Wikidata entity is reasonably well-populated. This is a strong foundation but needs supplementation with an English Wikipedia article.

### 4.3 Social Media Profile Status

| Platform | URL | HTTP Status | In Schema sameAs |
|----------|-----|-------------|-----------------|
| Facebook | facebook.com/Jarvisydan/ | 200 (Active) | Yes |
| Instagram | instagram.com/jarvisydan/ | 200 (Active) | Yes |
| YouTube | youtube.com/user/LomakylaJarvisydan | 200 (Active) | Yes (different URL in schema*) |
| LinkedIn | linkedin.com/company/holiday-resort-j-rvisyd-n | 999 (Blocked**) | Not in schema |
| X (Twitter) | x.com/jarvisydan | Present in schema | Yes |

*Note: Schema sameAs uses `youtube.com/c/jarvisydan` but the actual footer link uses `youtube.com/user/LomakylaJarvisydan`. These should be consistent.

**Note: LinkedIn returns 999 (bot protection), but this is standard LinkedIn behavior for curl requests. The profile likely exists.

**Issues Found:**
- **LinkedIn missing from Organization schema sameAs** -- LinkedIn is linked in the footer but not included in JSON-LD sameAs array. Severity: **Medium**
- **YouTube URL mismatch** -- Schema has one URL, footer links another. AI systems may not connect these as the same entity. Severity: **Medium**
- **Schema logo is 1x1px** -- Organization schema references a logo with 1x1 pixel dimensions. AI systems using schema data will get a broken logo reference. Severity: **Low**

### 4.4 Organization Schema Quality

The site uses Yoast SEO's default Organization schema. Current implementation:

```json
{
  "@type": "Organization",
  "name": "Hotel & Spa Resort Jarvisydan",
  "url": "https://www.jarvisydan.com/",
  "logo": { "width": 1, "height": 1 },
  "sameAs": [
    "https://www.facebook.com/Jarvisydan/",
    "https://x.com/jarvisydan",
    "https://www.instagram.com/jarvisydan/",
    "https://www.youtube.com/c/jarvisydan"
  ]
}
```

**Missing from schema:**
- `@type` should include `LodgingBusiness` or `Hotel` (not just `Organization`)
- `address` with full postal address
- `geo` coordinates
- `telephone`
- `priceRange`
- `starRating` (if applicable)
- `amenityFeature` (spa, restaurant, activities)
- `numberOfRooms`
- LinkedIn in `sameAs`
- Proper logo dimensions

Severity: **Critical** -- Using generic `Organization` instead of `Hotel` or `LodgingBusiness` means AI systems cannot properly categorize this entity as accommodation.

---

## 5. Server-Side Rendering Check

### SSR Verification Results

| Content Element | Present in Raw HTML | SSR Status |
|----------------|-------------------|------------|
| "Lake Saimaa" | Yes | Server-rendered |
| "Linnansaari" | Yes | Server-rendered |
| "1658" (heritage) | Yes | Server-rendered |
| "Rantasalmi" | Yes | Server-rendered |
| "Porosalmentie 313" | Yes | Server-rendered |
| "Experience Hotel" | Yes | Server-rendered |
| "Lake Spa" | Yes | Server-rendered |
| "Kuru" | Yes | Server-rendered |
| H1 tags | Yes | Server-rendered |
| H2 tags | Yes | Server-rendered |
| JSON-LD schema | Yes | Server-rendered |

**Total HTML size:** 149,585 characters (1,932 lines)

**Assessment:** Content is fully server-side rendered via WordPress. All critical text, headings, and structured data are present in the initial HTML response. AI crawlers that do not execute JavaScript (GPTBot, ClaudeBot, PerplexityBot) will see all content.

- Score: **12/15** -- Excellent SSR. Minor deductions for heavy JavaScript payload (booking widgets, analytics, sliders) that could slow Time to Interactive, though this does not affect AI crawling.

---

## 6. Platform-Specific Readiness Assessment

### 6.1 Google AI Overviews

**Score: 4/10**

| Factor | Status |
|--------|--------|
| Traditional SEO foundation | Moderate (see 01-technical.md: 48/100) |
| Passage optimization for featured snippets | Poor -- no passages at optimal 134-167 word length |
| Question-answer content | Missing -- no FAQ schema, no question headings |
| Schema markup depth | Poor -- Organization only, no Hotel/LodgingBusiness |
| E-E-A-T signals | Weak -- no author attribution, no expert citations |
| Structured comparison data | Missing -- no tables |

**Why this matters:** Google AI Overviews pull from pages with strong passage-level content, clear hierarchies, and rich schema. Jarvisydan's marketing-heavy prose and thin schema make it unlikely to be featured in AI Overview answers for queries like "best lakeside hotels in Finland" or "luxury spa resorts Lake Saimaa."

### 6.2 ChatGPT Web Search

**Score: 3/10**

| Factor | Status |
|--------|--------|
| Entity presence in training data | Moderate -- Finnish Wikipedia exists, no English |
| Wikidata entity | Good -- Q112112665 with 16 properties |
| Authoritative third-party mentions | Unknown -- no visible TripAdvisor/Booking.com integration |
| Content specificity | Weak -- marketing prose, few hard facts |
| llms.txt | Missing |
| Citable passages | Poor -- see Section 3 |

**Why this matters:** ChatGPT relies on entity recognition and authoritative sources. Without an English Wikipedia article or llms.txt, ChatGPT may describe Jarvisydan with outdated or generic information. The Finnish Wikipedia article notably contains negative content (legionella incident, labor investigation, financial difficulties) that could influence AI-generated descriptions.

### 6.3 Perplexity

**Score: 3/10**

| Factor | Status |
|--------|--------|
| Community validation (Reddit mentions) | Unknown -- not verified |
| YouTube presence | Exists but channel name is legacy ("LomakylaJarvisydan") |
| Blog / editorial content | Exists (blog section on site) but thin |
| Third-party review sites | Not integrated into site |
| Data-rich citable content | Poor |
| Source diversity | Weak -- most signal comes from own site |

**Why this matters:** Perplexity prioritizes diverse source types (forums, videos, reviews, news). A single-source signal (own website only) limits visibility. The legacy YouTube channel name does not match the current brand name, reducing entity connection.

---

## 7. Top 5 Highest-Impact GEO Changes

### 1. Create and Deploy llms.txt -- CRITICAL

**Impact:** Immediately improves AI systems' ability to accurately describe the hotel.
**Effort:** Low (1-2 hours)
**Action:** Create `/llms.txt` at the root domain using the recommended content in Section 2 above. Deploy as a static text file.

### 2. Rewrite Key Pages with AI-Citable Passages -- CRITICAL

**Impact:** Enables citation in Google AI Overviews, ChatGPT, and Perplexity answers.
**Effort:** Medium (4-8 hours)
**Action:**
- Replace poetic H1 on homepage with descriptive H1: "Hotel & Spa Resort Jarvisydan -- Luxury Lakeside Resort on Lake Saimaa, Finland"
- Write 134-167 word factual overview paragraphs for homepage, activities, restaurants, and spa pages
- Use third-person voice for key descriptive passages ("Jarvisydan is..." not "We invite you...")
- Add question-based H2/H3 headings: "What makes Jarvisydan unique?", "What activities are available at Jarvisydan?", "Where is Jarvisydan located?"
- Add FAQ sections with structured FAQ schema markup

### 3. Upgrade Schema to Hotel/LodgingBusiness -- CRITICAL

**Impact:** AI systems will correctly categorize the entity as a hotel, enabling inclusion in accommodation queries.
**Effort:** Low-Medium (2-4 hours)
**Action:**
- Change `@type` from `Organization` to `["Hotel", "LodgingBusiness"]`
- Add `address`, `geo`, `telephone`, `priceRange`, `amenityFeature`, `numberOfRooms`
- Fix logo dimensions (replace 1x1px reference)
- Add LinkedIn to sameAs
- Align YouTube URL in sameAs with actual channel URL
- Add `Restaurant` schema for each restaurant (especially Solitary with its ranking)
- Add `FAQ` schema on pages with question-answer content

### 4. Create English Wikipedia Article -- HIGH

**Impact:** Establishes authoritative entity presence for English-language AI systems.
**Effort:** High (requires notability evidence, community review, 10-20 hours)
**Action:**
- Draft Wikipedia article with verifiable facts: location, history (1658 heritage), awards (2020 tourism business of year), Solitary ranking
- Gather reliable third-party sources (news articles, tourism board references, award announcements)
- Note: The Finnish Wikipedia article contains negative content. An English article should be factual and balanced, per Wikipedia's neutral point of view policy. The negative content in the Finnish article (legionella, labor issues, restructuring) will be visible to AI systems reading Finnish Wikipedia regardless.

### 5. Add Structured Comparison Tables -- HIGH

**Impact:** Tables are highly citable and preferred by AI for comparative queries.
**Effort:** Low (2-3 hours)
**Action:**
- Homepage: Accommodation comparison table (type, capacity, price from, features, season)
- Restaurants page: Restaurant comparison table (name, cuisine, price range, hours, reservation required)
- Activities page: Seasonal activity table (activity, season, duration, price, booking required)
- Spa page: Treatment comparison table

---

## 8. Additional Findings

### 8.1 Finnish Wikipedia Risk -- HIGH

The Finnish Wikipedia article (fi.wikipedia.org/wiki/Jarvisydan) contains significant negative content:
- Legionella bacteria found in pools (August 2025), spa closed for 3 weeks
- Police investigation into treatment of Ukrainian and Thai workers
- Pattern of delayed invoice payments requiring legal collection
- EUR 9.8 million in public subsidies (2015-2023) to group companies
- Siemens Financial Services filed for corporate restructuring (January 2026)
- Lomakyla Jarvisydan Oy bankruptcy petition (January 2026)

**Why this matters for GEO:** AI systems read Wikipedia in all languages. ChatGPT, Perplexity, and Gemini may surface this negative information when answering queries about Jarvisydan, especially in Finnish-language responses but potentially in English translations too.

**Recommendation:** This cannot be "fixed" by editing Wikipedia (that would violate Wikipedia policies). The best defensive strategy is to:
1. Ensure your own website has strong, factual, positive content that AI systems can cite
2. Create the llms.txt with accurate current information
3. Generate positive third-party coverage (press releases, travel blog features, award submissions)
4. Ensure Google Business Profile is up-to-date with recent positive reviews

### 8.2 Meta Description Gaps -- MEDIUM

Homepage and restaurants page lack explicit meta descriptions. AI systems sometimes use meta descriptions as summary source material.

### 8.3 No FAQ Schema Anywhere -- HIGH

Not a single page uses FAQ structured data. FAQ schema is one of the most effective ways to get content into AI answers, as it pre-formats question-answer pairs that AI systems can directly cite.

### 8.4 Brand Name Inconsistency -- MEDIUM

The brand appears as multiple variants across web properties:
- "Hotel & Spa Resort Jarvisydan" (website)
- "Nature Hotel & Spa Resort Jarvisydan" (Wikidata, some pages)
- "Holiday Resort Jarvisydan" (LinkedIn URL slug)
- "Lomakyla Jarvisydan" (YouTube legacy URL)

AI systems may treat these as separate entities. Consolidate to one canonical brand name across all platforms.

---

## Summary

| # | Finding | Severity | Section |
|---|---------|----------|---------|
| 1 | No llms.txt file | Critical | 2 |
| 2 | Homepage H1 is poetic, not descriptive | Critical | 3.1 |
| 3 | Schema uses Organization, not Hotel/LodgingBusiness | Critical | 4.4 |
| 4 | No FAQ schema on any page | High | 8.3 |
| 5 | No English Wikipedia article | High | 4.1 |
| 6 | No self-contained citable passages (134-167 words) | High | 3 |
| 7 | No question-based headings on any page | High | 3 |
| 8 | No comparison tables on any page | High | 3 |
| 9 | Activities page has duplicate H1 tags | High | 3.2 |
| 10 | Finnish Wikipedia contains significant negative content | High | 8.1 |
| 11 | Restaurant ranking lacks source attribution | Medium | 3.3 |
| 12 | LinkedIn missing from schema sameAs | Medium | 4.3 |
| 13 | YouTube URL mismatch (schema vs. footer) | Medium | 4.3 |
| 14 | Brand name inconsistency across platforms | Medium | 8.4 |
| 15 | Missing meta descriptions (homepage, restaurants) | Medium | 8.2 |
| 16 | robots.txt has no Sitemap directive | Medium | 1 |
| 17 | Schema logo is 1x1px | Low | 4.3 |
| 18 | First-person marketing voice reduces citability | Low | 3.1 |

**Bottom line:** Jarvisydan's website is built for human visitors, not AI consumption. The content is marketing-oriented prose that AI systems struggle to parse, cite, or accurately summarize. The most impactful quick wins are deploying an llms.txt file, rewriting the H1 and key paragraphs for citability, and upgrading schema from Organization to Hotel. The English Wikipedia gap is a significant long-term disadvantage for international AI search visibility.
