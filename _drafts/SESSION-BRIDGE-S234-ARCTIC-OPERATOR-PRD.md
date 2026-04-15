---
session: 231
date: 2026-04-15
type: SESSION BRIDGE — Arctic Cruises Tour Operator PRD
model_wrote: sonnet-4-6
model_executes: sonnet
priority: MEDIUM
chmod: 444
supersedes: —
---

# SESSION BRIDGE S234
# ARCTIC CRUISES — TOUR OPERATOR PRODUCT & REQUIREMENTS DOCUMENT
# chmod 444 — älä muokkaa

---

## CONTEXT

B2C website COMPLETE (V3.3). B2B flyer built (S232). FAM pack built (S233).

**This session builds the Tour Operator PRD** — a formal product specification document that a tour operator needs to actually build and sell Arctic Cruises in their programme. This is what a product manager at TUI, Intrepid, G Adventures, or a boutique DACH operator needs before they can create an itinerary, get it approved, and list it.

Different from the flyer (which is a sales/marketing document) — this is an operational and commercial reference document.

---

## DELIVERABLE

**File:** `arctic-cruises-operator-prd.md` (also export as .pdf via print CSS if HTML)
**Format:** Structured document, ~10-15 pages when printed
**Audience:** Product managers and contracting teams at tour operators (DACH, UK, US, Australia)
**Tone:** Professional, precise, complete. Operators need facts, not marketing copy.

---

## DOCUMENT STRUCTURE

### 1. PRODUCT OVERVIEW

```
Product name: Grand Cruise on Lake Saimaa
Sub-brand: Arctic Cruises (operated by Finland DMC Oy)
Product type: Multi-day guided cruise with resort accommodation (NOT cruise-ship accommodation)
Location: Lake Saimaa, Finland — UNESCO Global Geopark
Season: May – September 2027 (inaugural international season)
Language: EN / DE / FR / FI (FinnConcierge on board)
Audience: Affluent independent travellers, nature/luxury segment, 45-65, DACH/UK primary
B2C URL: https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html
Booking contact: Laura Ilvonen · laura@finlanddmc.fi
```

### 2. PRODUCT VARIANTS

| Code | Name | Duration | Format |
|------|------|----------|--------|
| AC-DAY | Lake Day Cruise | 1 day | Day trip, no accommodation |
| AC-3N | Saimaa Short Cruise | 3 nights / 4 days | Lappeenranta → Puumala → Savonlinna → Järvisydän → return |
| AC-7N | Grand Cruise on Lake Saimaa | 7 nights / 8 days | Full closed loop — Lappeenranta → Kuopio → return |

### 3. PRICING — NET RATES (2027 Season)

All prices per person, EUR, double occupancy unless noted.

**Early Partner Programme (apply before 15 July 2026)**

| Product | List Price | Net Rate | Commission |
|---------|-----------|----------|------------|
| AC-DAY | €400 | €320 | 20% |
| AC-3N | €1,200 | €960 | 20% |
| AC-7N | €2,600 | €2,080 | 20% |

Single supplement: +€50/night (applies to all multi-night products)
Minimum group: No minimum. FIT welcome.
Group discount: Enquire direct for groups 10+ pax.

**Standard rates (after 15 July 2026)**
Early partner rate is a limited-availability incentive. Standard trade terms negotiated directly.

### 4. INCLUSIONS / EXCLUSIONS

**Included in all multi-night products:**
- All resort accommodation (Sahanlahti, Järvisydän, Kuopio hotels)
- Full board: all breakfasts at resort, all lunches on board (regional), all dinners (including gala with wine pairing)
- All on-board expert team: Captain, founder, local hosts/naturalist
- Smoke sauna at resort stops (both Sahanlahti and Järvisydän)
- FinnConcierge (AI + human personal assistant, DE/EN/FR/FI)
- All port transfers on embarkation day
- Castle passage briefing (Olavinlinna / Savonlinna)
- Kuopio Puijo Tower guided visit (7-night only)
- Conservation contribution (FANC Saimaa Seal LIFE project)

**Not included:**
- International flights to Helsinki (HEL)
- Transfer Helsinki → Lappeenranta (bookable via FinnConcierge)
- Travel insurance (mandatory — operator responsibility to advise clients)
- Single supplement (€50/night)
- Optional excursions: kayak hire, Olavinlinna castle entrance fee
- Personal drinks beyond gala wine pairing
- Gratuities (not customary in Finland; at guest discretion)

### 5. VESSEL SPECIFICATION

```
Name: M/S Carelia
Type: Day/excursion vessel (no overnight cabins)
Capacity: 200 passengers
Year: On Lake Saimaa since 1969
Refurbishment: Comprehensive refit completed ahead of 2027 season
Facilities: Main saloon + bar, regional lunch service daily, open top deck,
            sun deck forward, covered section, FinnConcierge station
Sauna: On board sauna (details TBC — resort saunas are primary programme element)
```

### 6. RESORT PORTFOLIO

Operators select from curated pool. Specific resort confirmed at booking based on availability and group size.

**Sahanlahti Resort** (Puumala archipelago)
- Position: Sheltered cove, direct lake access
- Rooms: Hotel rooms + cottages, all water-facing
- Sauna: Smoke sauna at lake's edge
- Kitchen: Local fish, chanterelles, cloudberries, rye
- Extras: Rowing boats, kayaks at dock
- Certification: Traditional Finnish lake resort

**Järvisydän Resort** (Heinävesi, Central route)
- Position: Long dock — ship ties directly
- Sauna: Smoke sauna + traditional
- Kitchen: European Region of Gastronomy 2024 — changes menu with the lake
- Certification: Green Key
- Notes: Gala dinner programme held here

**Kuopio Lakeside** (Kuopio, apex of route)
- Position: City waterfront, views over northern Saimaa
- Notes: Nights 3-4 on 7-night voyage; city hotel standard
- Extras: Puijo Tower (nearby, guided visit included), Kuopio market hall

**Alternative resorts (by availability):**
- Pistohiekka (Puumala, alternative to Sahanlahti)
- Okkolan Lomamökit (Puumala, most authentic/rustic option)

### 7. ROUTE DETAILS

**AC-7N Flagship Route**
- Day 1 (Wed): Lappeenranta → Imatra transit → Sahanlahti Resort (Night 1)
- Day 2 (Thu): → Savonlinna (Olavinlinna castle passage) → Järvisydän Resort (Night 2)
- Day 3 (Fri): → Varkaus canal locks → Kuopio (Night 3)
- Day 4 (Sat): Kuopio full day — Puijo Tower, market hall (Night 4)
- Day 5 (Sun): Kuopio → Järvisydän Resort, Gala dinner (Night 5)
- Day 6 (Mon): → Savonlinna → Sahanlahti Resort, farewell sauna (Night 6)
- Day 7 (Tue): Sahanlahti → Lappeenranta. Disembark by noon.

**AC-3N Short Route**
- Day 1 (Wed): Lappeenranta → Sahanlahti Resort (Night 1)
- Day 2 (Thu): → Olavinlinna castle → Järvisydän Resort, Gala dinner (Night 2)
- Day 3 (Fri): → Puumala area → Järvisydän Resort (Night 3)
- Day 4 (Sat): Return Lappeenranta by noon

**AC-DAY Route**
- Lappeenranta → Southern archipelago passages → Imatra → Return same day
- Departs 09:00, returns ~18:00

### 8. DEPARTURE SCHEDULE

Every Wednesday, May–September 2027
Total departures: ~21 Wednesdays

| Month | Wednesday dates |
|-------|----------------|
| May 2027 | 7, 14, 21, 28 |
| June 2027 | 4, 11, 18, 25 |
| July 2027 | 2, 9, 16, 23, 30 |
| August 2027 | 6, 13, 20, 27 |
| September 2027 | 3, 10, 17, 24 |

### 9. BOOKING PROCESS

1. Operator submits booking request: departure date + party size + product code
2. Laura confirms availability + issues proforma invoice
3. **Deposit: 30% due within 14 days of booking confirmation**
4. Guest names, dietary requirements, special requests: 30 days before departure
5. **Balance: 60 days before departure**
6. Cancellation policy: [to be confirmed — standard is 90% refund >60 days, 50% 30-60 days, 0% <30 days]

### 10. OPERATIONAL REQUIREMENTS FOR OPERATORS

**What operators must communicate to guests:**
- M/S Carelia is a day vessel — no overnight cabins. All nights at resorts.
- Smart casual dress code. No formal requirement.
- Travel insurance mandatory.
- Departs Lappeenranta harbour — not Helsinki. Transfer required.
- Optional activities (kayak, castle entry) not included; recommend budgeting €30-50.

**What operators must NOT promise guests:**
- Saimaa ringed seal sightings are possible, never guaranteed. Use: "You will cruise seal habitat."
- Exact resort at each stop — confirmed at booking, may vary by availability.
- Specific weather. September is crisp, August is warm. Both are excellent.

**Emergency contact:** Laura Ilvonen · laura@finlanddmc.fi · [phone TBC]

### 11. MARKETING ASSETS AVAILABLE

- High-resolution photography (50+ images, usage rights included)
- B2C website: https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html
- Route map (print-quality SVG available on request)
- Product descriptions in EN / DE on request
- FAM trip available for qualifying operators (31 Aug – 3 Sep 2026, complimentary)

### 12. CREDENTIALS & CERTIFICATIONS

- UNESCO Global Geopark Saimaa — route entirely within Geopark
- Järvisydän: Green Key certified · European Region of Gastronomy 2024
- FANC Saimaa Seal LIFE project partner
- Metsähallitus (National Parks Finland) environmental protocols
- Zero-discharge waste management on vessel

### 13. CONTACTS

| Role | Name | Email |
|------|------|-------|
| Trade Relations & Bookings | Laura Ilvonen | laura@finlanddmc.fi |
| Founder & Operations | Saku Hyttinen | [via Laura] |
| DMC Parent Company | Finland DMC Oy | info@finlanddmc.fi |

**Website:** https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html
**Early partner application:** laura@finlanddmc.fi · deadline 15 July 2026

---

## DESIGN NOTES

- Clean professional document — not a sales brochure
- Markdown → render as clean HTML or export PDF
- Tables for all structured data
- Arctic Cruises header/footer on each page
- Consider: also output as a `.docx`-style HTML so operators can print to PDF easily

---

## KEY FILES TO LOAD

```yaml
key_files:
  - ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html              # Route/resort/team detail
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S232-ARCTIC-B2B-FLYER.md
```

turn_budget: 4-6
external_calls: "Optional Grok spar on commercial terms completeness"
session_type: BUILD (document assembly)

---

*Bridge v1.0 — S231 2026-04-15*
*chmod 444*
