---
session: 239
date: 2026-04-16
type: SESSION BRIDGE — Operator Website Research → Arctic B2C Improvements
model_wrote: sonnet-4-6
model_executes: sonnet
priority: HIGH — website improvement sprint
chmod: 444
---

# SESSION BRIDGE S240
# HOW TOP CRUISE OPERATORS SELL — APPLY TO ARCTIC B2C WEBSITE
# chmod 444 — älä muokkaa

---

## MISSION

Study how the 5 Tier-1 operators sell and market their cruise products online.
Extract patterns. Apply specifically to arctic-cruises-b2c.html.

Output: 1 research synthesis doc + 1 prioritised improvement spec for the website.

Turn budget: 8. Mode: bypassPermissions recommended.

---

## PIPELINE STATE

```yaml
arctic_b2c_url: https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html
arctic_b2c_local: ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
operator_target_list: ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/operator-target-list.md
pricing_master: ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json
product_brief: ~/1658HoldingsOy-AIFiles/output/PRODUCT-BRIEF.md
```

---

## PHASE 1: PARALLEL OPERATOR RESEARCH (5 subagents)

Launch all 5 simultaneously. HOLD until ALL complete before reading results.

### Research prompt template (use for each operator):

```
Visit [OPERATOR_URL] and study how they sell their cruise product.

Extract:
1. HOMEPAGE STRUCTURE — above-the-fold hook, hero message, first CTA
2. DESTINATION VS SHIP FRAMING — do they lead with the destination or the vessel?
3. PRICING PRESENTATION — do they show price upfront or hide it? How do they anchor?
4. PRODUCT PAGE — how is a single voyage structured (inclusions, itinerary, what's highlighted)?
5. URGENCY / CONVERSION MECHANICS — early-bird, limited availability, countdown, social proof
6. CONSERVATION / SUSTAINABILITY — where does it appear, how prominent?
7. TRADE / B2B SECTION — is there a separate operator portal? How is it accessed?
8. TRUST SIGNALS — awards, press logos, certifications shown
9. KEY COPY PATTERNS — 3 phrases or sentences that best represent their brand voice
10. WHAT THEY DO BETTER THAN MOST — one thing this site does that others don't

Output as a structured 200-word summary. No waffle.
```

### 5 Agents:

**Agent 1 — Abercrombie & Kent**
URL: https://www.abercrombiekent.com/cruises/luxury-expedition-cruises
Focus extra: how they present "exclusive access" and wildlife encounters

**Agent 2 — Hapag-Lloyd Cruises**
URL: https://www.hl-cruises.com (MS EUROPA 2 product pages)
Focus extra: how they handle German luxury + discovery voyage framing

**Agent 3 — Saga Cruises**
URL: https://travel.saga.co.uk/cruises/river.aspx and one product page
Focus extra: how they present 50+ audience value (not "old people" framing)

**Agent 4 — PONANT**
URL: https://www.ponant.com/en (and one Norwegian fjord voyage page)
Focus extra: how they present the "discovered by few" positioning and conservation

**Agent 5 — Scenic Cruises**
URL: https://www.scenic.eu (Scenic Eclipse product page)
Focus extra: how they justify ultra-premium pricing and "Space-Ship" concept

---

## PHASE 2: READ OUR WEBSITE

One subagent reads arctic-cruises-b2c.html in full and returns:
- Current above-the-fold hook + hero message
- Current pricing presentation approach
- Current conservation/seal story placement
- Current trade section (if any)
- Current CTAs and their placement
- Identified weaknesses vs. luxury cruise standard

---

## PHASE 3: SYNTHESIS + IMPROVEMENT SPEC

Main thread synthesises all 6 agent outputs:

1. What do ALL 5 operators do that we don't?
2. What does our site do that they don't (potential advantages)?
3. Rank top 8 improvements by impact × effort

Format improvements as:
```
IMPROVEMENT N: [title]
Current state: [what the site does now]
Best practice: [what operators do, with example]
Recommended change: [specific edit to arctic-cruises-b2c.html]
Effort: Low / Medium / High
Impact: Low / Medium / High
```

Write synthesis to:
~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/website-improvement-spec.md

---

## ARCTIC B2C CONTEXT (for subagents)

Product: Arctic Cruises — 7-night lake cruise on Lake Saimaa, Finland. UNESCO Geopark.
USP: Unbuilt wilderness. Saimaa ringed seal (~400-530 individuals, endemic). Multi-day cruise route (Lappeenranta → Puumala → Savonlinna → Järvisydän) not operated since bankruptcy ~50 years ago.
Vessel: M/S Carelia, 1969, max 100 guests.
Price: €2,600 list / €2,080 net (7-night). €400 / €1,200 day + 3-night.
Launch: May 2027. FAM trip 31 Aug–3 Sep 2026.
Audience: 50-68, €150k+ HHI, DACH + UK primary, post-achievement travelers.
Contact: laura@finlanddmc.fi

Key constraint: ✓ checkmarks in CSS should be replaced with brand-appropriate icons
(lake land 2.0 brand guide to be sourced from Patrick — flag if icons are needed)

---

## KEY FILES FOR THIS SESSION

```yaml
read_first:
  - ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/operator-target-list.md
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
  - ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json

write_to:
  - ~/1658HoldingsOy-AIFiles/output/arctic-cruises-outreach/website-improvement-spec.md
  - (optional) apply highest-impact Low-effort improvements directly to arctic-cruises-b2c.html
```

---

## SESSION START PROTOCOL

1. Confirm operator-target-list.md exists
2. Read arctic-cruises-b2c.html to understand current state
3. DECLARE: 8-turn budget
4. Turn 1: Launch all 5 operator research agents + 1 B2C audit agent = 6 parallel subagents. HOLD until ALL complete.
5. Turn 2: Read all results in one batch
6. Turn 3: Synthesis + write website-improvement-spec.md
7. Turn 4: Apply the top 3 Low-effort/High-impact improvements directly to arctic-cruises-b2c.html
8. Turn 5: Commit changes
9. Turn 6: Session bridge / harvest

---

## FAILURE HANDLING

| Failure | Response |
|---------|----------|
| Operator website blocks scraping | Use cached/known info from operator target list research |
| Fewer than 3 operators complete | Proceed with what completed, note gaps |
| Improvement spec too vague | Add "specific line to change in arctic-cruises-b2c.html" field |

---

*Bridge v1.0 — S239 2026-04-16*
*chmod 444*
