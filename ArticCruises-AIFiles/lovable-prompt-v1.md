# Saimaa Islands — Lovable Prompt v1
**Status:** Ready to paste
**Photos folder:** `~/1658HoldingsOy-AIFiles/ArticCruises-AIFiles/lovable-photos/` (10 files)
**Upload:** Two batches of 5 — wait for confirmation between batches
**Select in Lovable UI:** React + Vite + Tailwind + Supabase

---

## MAIN PROMPT (paste first, then upload photos)

```
Build a single-page scroll investor website for "Saimaa Islands" — a private island investment concept on Lake Saimaa, Finland.

---

TYPOGRAPHY
- Headings: Playfair Display (install via @fontsource/playfair-display)
- Body: Inter (install via @fontsource/inter)
- Never use Google Fonts CDN — use @fontsource packages only

---

IMAGE PERFORMANCE — APPLY TO EVERY IMAGE ON THE SITE
- Convert all uploaded JPGs to WebP on build (vite.config: add vite-plugin-imagemin with webp output)
- Every <img> tag: loading="lazy" sizes="(max-width:768px) 100vw, 50vw"
- Target file size: <180KB per image after optimization
- Store all images in /public/assets/
- This block applies globally — no exceptions

---

BRAND COLORS
- Forest green: #2C4A2E
- Copper brown: #8B4513
- Cream: #F8F4ED
- Medium green: #5C7A5C
- Dark text: #1A2A1A
- Use cream as page background; forest green for section backgrounds; copper brown for CTAs and accents

---

NAVIGATION
- Sticky top nav, forest green background, cream text
- Logo left: "SAIMAA ISLANDS" in Playfair Display, small "LAKE SAIMAA · FINLAND" subtitle
- Nav links center: Why Saimaa · Summer · Winter · Islands · Investment · Contact
- Language toggle top-right: 🇬🇧 🇩🇪 (see i18n section at end of this prompt)
- Mobile: hamburger menu

---

IMAGE ASSIGNMENT TABLE
Use these uploaded photos in these exact sections:

| Photo filename | Section | Usage |
|---|---|---|
| saimaa-islands-autumn-aerial.jpg | Hero background | Full-width hero backdrop |
| saimaa-islands-summer-aerial.jpg | Why Saimaa section | Right-side image |
| saimaa-seal.jpg | Why Saimaa section | Conservation callout card |
| kayaking-couple-2.jpg | Summer section | Hero image of section |
| evening-campfire.jpg | Summer section | Second image |
| snowshoeing-frozen-lake.jpg | Winter section | Hero image of section |
| ice-fishing-lakeland.jpg | Winter section | Second image |
| safarihouse-1.jpg | Island Portfolio | First island card |
| ms-puijo-exterior.jpg | Ecosystem section | Fleet/vessel image |
| resort-autumn.jpg | Investment Structure | Background/mood image |

---

SECTION 1 — HERO
- Full-viewport height
- Background: saimaa-islands-autumn-aerial.jpg (cover, darkened overlay 40% black)
- Headline (Playfair Display, 64px, cream): "Own a Private Island on Europe's Most Pristine Lake"
- Subhead (Inter, 20px, cream 80% opacity): "Lake Saimaa · Finland · Private Island Investments"
- Two CTA buttons: "Explore the Islands" (forest green, scroll to #islands) and "Investment Overview" (outlined copper brown, scroll to #investment)
- Scroll-down arrow animation

---

SECTION 2 — WHY SAIMAA
- Two-column layout: left = text, right = saimaa-islands-summer-aerial.jpg
- Headline: "Europe's Largest Inland Archipelago"
- Body: Lake Saimaa covers 4,400 km² with over 13,000 islands — more than any inland lake in Europe. Its 98% wilderness shoreline, world-class salmon and pike fishing, and complete absence of mass tourism make it unique at a global scale.
- Three stat cards (forest green background, cream text):
  - "13,000+" / Islands in the archipelago
  - "98%" / Wilderness shoreline
  - "4,400 km²" / Total lake area
- Conservation callout card (copper brown border): Photo: saimaa-seal.jpg. Caption: "The Saimaa ringed seal is strictly protected; our operations support the ongoing conservation programme." Text small, italic.

---

SECTION 3 — SUMMER EXPERIENCE
- Forest green background section
- Headline (cream): "The Summer Experience"
- Subhead: "June through September — midnight sun, pristine water, absolute privacy"
- Two images side by side: kayaking-couple-2.jpg (left, larger) + evening-campfire.jpg (right, smaller)
- Experience cards row (cream cards, dark text):
  - 🚣 Private Kayak Expeditions
  - 🎣 Nordic Fly Fishing
  - 🏄 Wild Swimming & SUP
  - 🔥 Island Campfire Evenings
  - ⛵ Sailing the Archipelago
- "7 nights from €4,900 per island" pricing note (small, copper brown)

---

SECTION 4 — WINTER EXPERIENCE
- Cream background section
- Headline: "The Winter Experience"
- Subhead: "December through March — frozen lake, aurora season, Nordic silence"
- Two images side by side: snowshoeing-frozen-lake.jpg (left) + ice-fishing-lakeland.jpg (right)
- Experience cards row (forest green cards, cream text):
  - ❄️ Ice Fishing Expeditions
  - 🏔️ Snowshoe Treks
  - 🌌 Aurora Watching
  - 🧖 Lakeside Sauna & Ice Swimming
  - 🍽️ Winter Foraging Dinners
- "7 nights from €3,900 per island" pricing note (small, copper brown)

---

SECTION 5 — ISLAND PORTFOLIO (id="islands")
- Headline: "The Islands"
- Subhead: "Three private islands — each with distinct character"
- Three cards in a row. Each card: photo (safarihouse-1.jpg on first card, use resort-autumn.jpg thumbnail on second, placeholder forest green on third), island name, size, status badge, short description, "Learn More" button.

Card 1 — HAUKKASAARI
- Photo: safarihouse-1.jpg
- Size: 2.3 ha · Capacity: 8 guests
- Status badge (green): "Available"
- Description: "The flagship island. Safari lodge architecture with panoramic decks, private dock, and forested trails. Certified carbon-neutral operations."

Card 2 — LEHTISAARI
- Photo: resort-autumn.jpg
- Size: 1.1 ha · Capacity: 6 guests
- Status badge (copper): "Under development"
- Description: "A sheltered bay island ideal for families. Planned for traditional log cabin construction with a private sauna pavilion."

Card 3 — PIRTTISAARI
- Photo: (use saimaa-islands-summer-aerial.jpg cropped thumbnail)
- Size: 0.8 ha · Capacity: 4 guests
- Status badge (grey): "Pre-acquisition"
- Description: "The most remote of the three. Suitable for ultra-exclusive retreats with minimal development footprint."

---

SECTION 6 — THREE PRODUCTS
- Headline: "Three Ways to Invest"
- Three product columns (alternating forest green and cream):

Column 1 — ISLAND OWNERSHIP
- Own your island outright
- Freehold title to the island property
- Annual revenue share from managed rentals
- Private use: 4 weeks/year included
- Price from: €490,000
- CTA: "Request Details"

Column 2 — ISLAND PARTNERSHIP (highlighted as "Most Popular")
- Co-ownership with 2–4 partners
- Fractional freehold title (25–50%)
- Full managed rental programme
- Private use: pro-rata weeks
- Price from: €149,000
- CTA: "Request Details"

Column 3 — INVESTMENT SHARE
- Capital participation only
- No ownership responsibilities
- Quarterly revenue distribution
- Minimum 5-year horizon
- Price from: €50,000
- CTA: "Request Details"

---

SECTION 7 — ECOSYSTEM
- Headline: "The Saimaa Islands Ecosystem"
- Body: Our vertically integrated model means investors own a complete value chain — not just a property. Island guests arrive on our vessels, stay in our lodges, and book through our operator network.
- Photo: ms-puijo-exterior.jpg (full-width)
- Four ecosystem pillars in a row (icons + labels):
  - 🚢 Fleet — Private vessel transfers
  - 🏡 Lodges — Managed island accommodation
  - 🎿 Activities — Four-season experience programme
  - 🤝 Sales — DMC operator distribution network

---

SECTION 8 — INVESTMENT STRUCTURE (id="investment")
- Background: resort-autumn.jpg with 50% dark overlay
- Headline (cream): "Investment Structure"
- Four metric cards (semi-transparent cream):
  - Target IRR: 12–16%
  - Hold Period: 5–7 years
  - Current Phase: Seed Round
  - Minimum: €50,000
- Timeline row — three phases:
  - Phase 1 (2026): Island acquisition + Haukkasaari fit-out
  - Phase 2 (2027): Lehtisaari development + fleet expansion
  - Phase 3 (2028): Full portfolio + exit optionality
- Legal note (small, cream, italic): "This website is for information purposes only and does not constitute a prospectus or public offering. Investment in early-stage real assets carries risk including illiquidity and loss of capital. Available to professional and qualified investors only under applicable Finnish and EU law."

---

SECTION 9 — TEAM
- Headline: "The Team"
- Three team cards (clean, minimal):
  - Placeholder for 3 team members — name, title, 2-line bio
  - Use initials avatar placeholder (forest green circle with cream initials) — no stock photos
- Note under cards (italic): "Backed by 1658 Holdings Oy, a Finnish family holding company with operations across hospitality, tourism, and lake transport."

---

SECTION 10 — CONTACT (id="contact")
- Headline: "Express Interest"
- Subhead: "We respond within 48 hours. All enquiries are strictly confidential."
- Contact form fields:
  - Full Name (required)
  - Email (required)
  - Country of Residence (required)
  - Investment Interest: [dropdown: Island Ownership / Island Partnership / Investment Share / General Enquiry]
  - Message (optional textarea)
  - Checkbox (required): "I understand this is an early-stage investment enquiry. I confirm I am a professional or qualified investor as defined under applicable law. I consent to Saimaa Islands / 1658 Holdings Oy contacting me by email."
  - Submit button (copper brown): "Send Enquiry"
- Form backend:
  - Submit to Supabase edge function called `contact-form`
  - The edge function uses Resend to email enquiry to hello@articislands.com
  - Log to Supabase table `contact_enquiries` with fields: id, created_at, name, email, country, investment_interest, message, consent_given (boolean), ip_hash (anonymized)
  - On success: show green confirmation message "Thank you — we will be in touch within 48 hours."
  - On error: show red message "Something went wrong — please email us directly."
- Below form: two contact alternatives
  - 📧 hello@articislands.com
  - 📍 Registered: Helsinki, Finland

---

FOOTER
- Forest green background, cream text
- Left: "SAIMAA ISLANDS" logo text + "Lake Saimaa · Finland"
- Center: Privacy Policy link (placeholder page) | Cookie Policy link
- Right: © 2026 Saimaa Islands / 1658 Holdings Oy. All rights reserved.
- Very bottom: "Investment in real assets involves risk. Past performance is not indicative of future results."

---

TECHNICAL REQUIREMENTS
- React + Vite + Tailwind CSS
- vite.config.js: add vite-plugin-imagemin (webp: {quality:80}, mozjpeg:{quality:75})
- All images in /public/assets/ folder
- Smooth scroll behaviour (scroll-behavior: smooth in CSS)
- Framer Motion: fade-in-up on each section as it enters viewport (staggered 0.15s)
- Mobile-first responsive: 1 column on mobile, 2 on tablet, full layout on desktop
- Export to GitHub (create public repo "artic-islands-website")
- No placeholder lorem ipsum text anywhere — use the copy I provided above

---

IMAGE ASSIGNMENT TABLE (REPEATED — apply this)

| Photo filename | Section | Usage |
|---|---|---|
| saimaa-islands-autumn-aerial.jpg | Hero background | Full-width hero backdrop |
| saimaa-islands-summer-aerial.jpg | Why Saimaa section | Right-side image |
| saimaa-seal.jpg | Why Saimaa section | Conservation callout card |
| kayaking-couple-2.jpg | Summer section | Hero image of section |
| evening-campfire.jpg | Summer section | Second image |
| snowshoeing-frozen-lake.jpg | Winter section | Hero image of section |
| ice-fishing-lakeland.jpg | Winter section | Second image |
| safarihouse-1.jpg | Island Portfolio | First island card |
| ms-puijo-exterior.jpg | Ecosystem section | Fleet/vessel image |
| resort-autumn.jpg | Investment Structure | Background/mood image |
```

---

## ADDENDUM — LANGUAGE TOGGLE (paste as follow-up after first build)

```
Add bilingual English/German support using react-i18next.

SETUP
- Install: react-i18next, i18next
- Create /src/locales/en.json and /src/locales/de.json
- Default language: English
- Persist selection in localStorage

LANGUAGE TOGGLE IN NAV
- Top-right of sticky nav, next to the existing nav links
- Two flag buttons: 🇬🇧 EN and 🇩🇪 DE
- Active language: solid forest green background, cream text
- Inactive: transparent, cream text, hover effect
- Mobile: include in hamburger menu

GERMAN TRANSLATIONS — use the register of a premium investment prospectus, not casual marketing

Hero:
- Headline: "Besitzen Sie eine Privatinsel auf Europas unberührtestem See"
- Subhead: "Saimaa-See · Finnland · Privatinsel-Investments"
- CTA 1: "Die Inseln entdecken"
- CTA 2: "Investment-Überblick"

Why Saimaa section heading: "Europas größtes Binnenarchipel"
Summer section heading: "Das Sommererlebnis"
Winter section heading: "Das Wintererlebnis"
Island Portfolio heading: "Das Inselportfolio"
Three Products heading: "Drei Wege zu investieren"
  - Column 1 title: "Inseleigentum"
  - Column 2 title: "Inselpartnerschaft"
  - Column 3 title: "Investitionsanteil"
  - Column 2 badge: "Beliebteste Wahl"
Ecosystem heading: "Das Artic-Islands-Ökosystem"
Investment Structure heading: "Investitionsstruktur"
  - Phase labels: "Phase 1 (2026): Inselerwerb & Haukkasaari-Ausbau" / "Phase 2 (2027): Lehtisaari-Entwicklung & Flottenausbau" / "Phase 3 (2028): Gesamtportfolio & Exit-Optionen"
  - Legal note: "Diese Website dient ausschließlich Informationszwecken und stellt weder einen Prospekt noch ein öffentliches Angebot dar. Investitionen in Sachwerte im Frühstadium sind mit Risiken verbunden, einschließlich eingeschränkter Liquidität und Kapitalverlust. Ausschließlich für professionelle und qualifizierte Anleger gemäß geltendem finnischem und EU-Recht."
Team heading: "Das Team"
Contact heading: "Interesse bekunden"
Contact subhead: "Wir antworten innerhalb von 48 Stunden. Alle Anfragen werden streng vertraulich behandelt."

Form fields:
- "Vollständiger Name"
- "E-Mail-Adresse"
- "Wohnsitzland"
- Investment interest dropdown: "Inseleigentum / Inselpartnerschaft / Investitionsanteil / Allgemeine Anfrage"
- "Nachricht (optional)"
- Consent checkbox: "Ich verstehe, dass es sich hierbei um eine Investitionsanfrage in der Frühphase handelt. Ich bestätige, dass ich ein professioneller oder qualifizierter Anleger im Sinne des geltenden Rechts bin. Ich stimme zu, dass Saimaa Islands / 1658 Holdings Oy mich per E-Mail kontaktiert."
- Submit button: "Anfrage senden"

Footer:
- Copyright: "© 2026 Saimaa Islands / 1658 Holdings Oy. Alle Rechte vorbehalten."
- Legal footer: "Investitionen in Sachwerte sind mit Risiken verbunden. Vergangene Wertentwicklungen sind kein verlässlicher Indikator für künftige Ergebnisse."

For all remaining body text not listed above: translate to German using investment prospectus register — formal, precise, no marketing fluff.
```

---

## VISUAL EDITS PROMPT (paste after reviewing first build)

```
Visual polish pass:

1. Hero overlay: reduce to 35% opacity (currently too dark — let the aerial photo breathe)
2. Stat cards (Why Saimaa): add subtle copper brown bottom border (2px) to each card
3. Section transitions: add a thin copper brown horizontal rule (1px, 60% width, centered) between each major section
4. CTA buttons: add 0.3s hover transition — forest green fills to copper brown on hover
5. Island portfolio cards: add box-shadow on hover (0 8px 32px rgba(0,0,0,0.12)) with 0.2s ease transition
6. Mobile hero: reduce headline to 40px on mobile (currently too large on small screens)
7. Footer: add top border 1px cream at 20% opacity
```

---

## PHOTO UPLOAD ORDER

**Batch 1 (upload first, wait for confirmation):**
1. saimaa-islands-autumn-aerial.jpg
2. saimaa-islands-summer-aerial.jpg
3. saimaa-seal.jpg
4. kayaking-couple-2.jpg
5. evening-campfire.jpg

**Batch 2 (upload after Batch 1 confirmed):**
6. snowshoeing-frozen-lake.jpg
7. ice-fishing-lakeland.jpg
8. safarihouse-1.jpg
9. ms-puijo-exterior.jpg
10. resort-autumn.jpg

Photos are in: `~/1658HoldingsOy-AIFiles/ArticCruises-AIFiles/lovable-photos/`
