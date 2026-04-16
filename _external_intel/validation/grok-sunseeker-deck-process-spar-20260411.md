# Grok Spar — Sunseeker Deck Process (S178, 2026-04-11)

## Source
- Grok Expert result: `~/.claude/results/grok-yacht-fractional-20260402-193325.json` (April 2 spar, same topic)
- Gemini partial output: captured from run-gemini.sh stdout (background timeout — partial only)
- Session observation: S177-S178 build experience

---

## Grok Findings [Harper/Benjamin/Lucas]

### Financial Content Risks (from April 2 spar)
**[Lucas] — Personal use cost claim** (hardest): "0€ lisäkustannus" during personal weeks is credibility-damaging.
- 64ft motor yacht: 200–400L/hr diesel = €300–800+/hr fuel
- Buyer cruising full 4 weeks will see €2k–5k+/week extra invoices
- **Fix:** "Included in annual fixed costs. Fuel, provisioning, port fees during personal use are owner responsibility."

**[Harper/Lucas] — Charter income as implied forecast**: Even "conservative/realistic/optimistic" labels create EU legal risk. Must carry bold disclaimer: "Projections hypothetical; past performance not indicative; no guarantee."

**[Benjamin/Lucas] — H1/H2 split silence**: 25-30% / 70-75% seasonality means owners must fund ~€2k–3k/share reserve in low season or face special assessment. Omitting this kills trust when cash call arrives.

**Recommended framing (Grok):**
> "4 viikkoa personal use — included in your €7,000 annual fixed share cost. No extra management or operational fees from the syndicate. Effective all-in €3,000 per week (capital amortisation + fixed ops) versus €20,000–35,000 gross market charter rate."
> + one-line disclaimer on every financial slide.

---

## Gemini Findings (partial — process streamlining)

**[Harper/Lucas] — Financial Product Deck = distinct skill variant** (High Impact, High Effort)
- Legal Framework and Risks & Disclaimers slides are load-bearing, not cosmetic
- Recommended: 9-slide structure with explicit legal review checkpoint
- Separate from Investor Deck because: audience is buyer (not funder), financial data is binding (not aspirational)

**Process bottleneck identified (unanimous):**
- Biggest bottleneck = photo sourcing phase (no protocol for brokerage CDN discovery)
- Secondary: no standard compression budget decision at session start

---

## Process Observations (session experience)

| Item | Observation |
|------|-------------|
| Brokerage CDN | nettivene.com uses sequential numbering — discoverable. Pattern: `/fit-in/3840x2160/boat/{listing_id}/{hash}.jpg` |
| Wikimedia Commons | Reliable for location backgrounds. CC BY-SA 3.0 = attribution required. Query: `site:commons.wikimedia.org [location] panorama` |
| base64 compression | 1600px / JPEG 72 → ~92KB per slide bg. Total 6-slide deck = ~1.6MB. Acceptable for web, borderline for email. |
| GitHub API push | No clone needed — fast, reliable. Always read SHA before PUT. |
| PDF quality | 1920×1080 / quality 95 / Playwright = 885KB for 6 slides. Good quality. |
| Biggest time sink | Session 1: understanding CDN structure. Session 2: Grok spar architecture. Session 3: slide 6 sourcing. |

---

## Recommended Skill Updates

### html-presentation SKILL.md additions:
1. Add "Financial Product Deck" variant (9-slide structure + disclaimer protocol)
2. Add brokerage CDN discovery protocol to photo sourcing
3. Add Wikimedia Commons to photo-sources.md as standard location background source
4. Add compression budget decision step at session start
5. Add legal disclaimer block template for financial slides

### deck-template.md additions:
- Financial Product Deck slide sequence
- Standard disclaimer block HTML
- base64 compression guide

*Saved 2026-04-11, session S178*
