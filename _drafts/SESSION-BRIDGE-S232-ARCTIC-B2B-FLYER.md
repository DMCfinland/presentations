---
session: 231
date: 2026-04-15
type: SESSION BRIDGE — Arctic Cruises B2B Tour Operator Flyer
model_wrote: sonnet-4-6
model_executes: sonnet
priority: HIGH
chmod: 444
supersedes: —
---

# SESSION BRIDGE S232
# ARCTIC CRUISES — B2B TOUR OPERATOR SALES FLYER
# chmod 444 — älä muokkaa

---

## CONTEXT — WHERE WE ARE

B2C website V3.3 is COMPLETE and live at:
https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html

Commercial terms are locked in: `_drafts/arctic-b2b-commercial-brief.md`

**This session builds the B2B sales flyer** — the document Laura emails to tour operators when they express interest or when she does cold outreach at trade shows (ITB, WTM, Nordic Visit orgs).

---

## DELIVERABLE

**File:** `arctic-cruises-b2b-flyer.html`
**Format:** A4 landscape, HTML with print CSS → PDF via Cmd+P
**Style:** Same design system as arctic-cruises-b2c.html (Playfair/Open Sans, --accent #2c6e4f, --gold #C49A6C, dark navy #1a2332)
**Sides:** 2-sided (Front = beauty + product, Back = commercial terms + booking)

---

## FRONT SIDE CONTENT

### Header bar (top full-width, dark navy #1a2332)
- Left: "Grand Cruise on Lake Saimaa" (Playfair serif, white)
- Right: "arctic-cruises.fi · laura@finlanddmc.fi" (small, muted)
- Sub: "OPERATOR INFORMATION · EARLY PARTNER PROGRAMME 2027"

### Hero area (left 55%, photo right 45%)
- **Photo:** `ArticCruises-AIFiles/lovable-photos/saimaa-islands-summer-aerial.jpg`
- **Eyebrow:** SAIMAA UNESCO GLOBAL GEOPARK · FINLAND · 2027 INAUGURAL SEASON
- **Headline:** "The European Nature Cruise Your Clients Are Looking For"
- **Sub:** 7 nights aboard a classic Finnish vessel through 4,400-island UNESCO Saimaa Lakeland. Endemic wildlife. Drinkable freshwater. Pristine unbuilt shores. The product that hasn't appeared in your catalog yet — because it hasn't existed until now.

### Three USP pillars (below hero, 3 columns)
1. **Endemic & Irreplaceable** — The Saimaa ringed seal exists nowhere else on Earth. No competitor can put this in their program.
2. **Premium at Accessible Price** — European river cruises average €4,000–€8,000 pp/7 nights. We are €2,600 list. Your margin is built in.
3. **Discovery Advantage** — Saimaa will be on every major travel list within 3 years. First-mover operators lock the best allocations and commissions.

### Product summary table (3 columns, styled cards)

| | Day Cruise | Short Cruise | Grand Cruise |
|---|---|---|---|
| Duration | 1 day | 3 nights | 7 nights |
| List price pp | €400 | €1,200 | €2,600 |
| **Your net rate** | **€320** | **€960** | **€2,080** |
| Commission | 20% | 20% | 20% |
| Included | Lunch · Team · Passages | Full board · 3 resorts · Sauna | Full board · 7 resorts · Full programme |

*Note: 20% early partner rate for operators who confirm before 15 July 2026*

---

## BACK SIDE CONTENT

### Commercial terms (left column)

**Early Partner Programme**
- Commission: **20%** on all products (limited window)
- Apply before: **15 July 2026**
- Pricing model: Net rate (you sell at your own margin)
- Deposit: 30% at booking
- Balance: 60 days before departure
- Currency: EUR

**What's included (7-night Grand Cruise)**
- 7 nights authentic Saimaa resort accommodation
- Full board — every meal included
- Gala dinner with wine pairing
- All expert team (Captain, founder, local hosts)
- Smoke sauna at both resorts
- FinnConcierge AI & human assistant (DE/EN/FR/FI)
- Castle passage briefing · Kuopio Puijo Tower visit
- Conservation contribution (FANC Saimaa Seal LIFE)

**Season & Departures**
- Every Wednesday, May–September 2027
- Bookings open January 2027
- Early enquiries welcome — priority allocation for confirmed early partners

### Booking process (right column, steps visual)
1. Request net rate sheet + booking form → laura@finlanddmc.fi
2. Select departure date(s) + party size
3. 30% deposit invoice issued
4. Guest names/dietary 30 days before
5. Balance due 60 days before departure

### FAM invitation teaser (full-width band, dark navy background)
> **Be among the first 50 operators to experience Saimaa.**
> Inaugural FAM voyage: 31 August – 3 September 2026 · Complimentary · Apply before 15 July 2026
> [Apply: laura@finlanddmc.fi]

### Partner logos strip (bottom)
GoSaimaa · Visit Finland · UNESCO Global Geopark Saimaa · Green Key · European Region of Gastronomy 2024 · FANC Saimaa Seal LIFE · Järvisydän Resort · Sahanlahti Resort · M/S Carelia

### Footer bar
"Arctic Cruises Oy / Finland DMC Oy · Lappeenranta, Finland · laura@finlanddmc.fi · 2027 Season"

---

## DESIGN NOTES

- Print CSS: `@media print { @page { size: A4 landscape; margin: 0; } }`
- Two `<section class="flyer-page">` divs, each `height: 100vh` on screen, `height: 297mm; width: 210mm` in print (A4 landscape = 297×210mm)
- Use `page-break-after: always` between pages
- Fonts: same Google Fonts import as B2C site
- Green accent (#2c6e4f), gold (#C49A6C), navy (#1a2332) — exact same variables
- Photo in header: no external URLs — use local `ArticCruises-AIFiles/lovable-photos/` paths

---

## KEY FILES TO LOAD

```yaml
key_files:
  - ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md    # All commercial terms
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html                   # Copy/style reference
  - ~/1658HoldingsOy-AIFiles/ArticCruises-AIFiles/lovable-photos/       # Photos
```

turn_budget: 4-6
external_calls: "Gemini judge after build (score target ≥85/100)"
session_type: BUILD (one-shot)

---

*Bridge v1.0 — S231 2026-04-15*
*chmod 444*
