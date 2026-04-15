---
session: 231
date: 2026-04-15
type: SESSION BRIDGE — Arctic Cruises Full-Pipeline Orchestrator
model_wrote: sonnet-4-6
model_executes: sonnet
priority: CRITICAL — autonomous build pipeline
chmod: 444
mode: bypassPermissions
supersedes: —
---

# SESSION BRIDGE S237
# ARCTIC CRUISES — AUTONOMOUS BUILD ORCHESTRATOR
# chmod 444 — älä muokkaa

---

## PURPOSE

This bridge runs the full Arctic Cruises document pipeline autonomously:
S232 → S233 → S234 → S235 → S236

Five deliverables. One orchestrator session. ~90-120 minutes total.
No human intervention required between builds.

**Run with:** `claude --dangerously-skip-permissions`

---

## ARCHITECTURE — WAVE BUILD WITH ROLLING JUDGE

```
Wave 1 (parallel):  [S232 B2B Flyer] + [S233 FAM Pack]
                         ↓                    ↓
                    Judge W1A              Judge W1B
                         ↓
Wave 2 (sequential): [S234 Operator PRD]  ← reads Wave 1 outputs
                         ↓
                    Judge W2
                         ↓
Wave 3 (sequential): [S235 Operations Brief]  ← reads S234
                         ↓
                    Judge W3
                         ↓
Wave 4 (sequential): [S236 Knowledge Bible]  ← compiles ALL
                         ↓
                    Final Gemini Audit
                         ↓
                    MANIFEST + Session End
```

---

## ORCHESTRATOR PROTOCOL — DDSC

### DECLARE (Turn 1)
Load this bridge. State the Phase Plan:
- Goal: 5 Arctic Cruises documents built, judged, committed
- Phases: 4 waves as above
- Turn budget: 12 (max 16)
- External calls: Gemini judge after Wave 4 (T3: ADVERSARIAL_JUDGE)
- Subagent plan: bypassPermissions on all build agents

### DELEGATE (Turn 2-8)
Launch ALL Wave 1 agents simultaneously. HOLD until both complete.
Then sequential Waves 2-4 with gate checks between each.

### SYNTHESIZE (Turn 9-11)
Orchestrator validates manifest. All files present? All pass judge?

### VALIDATE (Turn 12)
Gemini ADVERSARIAL_JUDGE on the complete output set.

### CLOSE (Turn 13)
Write MANIFEST.md. Commit all files. Session end.

---

## WAVE 1 — PARALLEL BUILD (target: ~20min)

### Subagent 1A: B2B FLYER

```
mode: bypassPermissions
isolation: worktree

TASK: Build the Arctic Cruises B2B tour operator sales flyer.

SOURCE OF TRUTH — read these files first:
- ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html (design reference)
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S232-ARCTIC-B2B-FLYER.md (full PRD)

OUTPUT FILE: ~/1658HoldingsOy-AIFiles/arctic-cruises-b2b-flyer.html

SPEC SUMMARY:
- A4 landscape HTML with print CSS (@page { size: A4 landscape; margin: 0; })
- Two <section class="flyer-page"> divs with page-break-after: always
- Same design tokens as B2C: --accent #2c6e4f, --gold #C49A6C, navy #1a2332
- Fonts: Playfair Display + Open Sans (same Google Fonts import)
- FRONT: Hero photo (saimaa-islands-summer-aerial.jpg) + headline + 3 USP pillars + product pricing table
- BACK: Commercial terms + booking process + FAM teaser band + partner logos
- Net rates in table: Day €320 / 3-night €960 / 7-night €2,080 (all 20% early partner)
- FAM: 31 Aug–3 Sep 2026, complimentary, apply by 15.07.2026, 50 operators max
- Contact: laura@finlanddmc.fi

SELF-CHECK before writing final file:
1. Both pages render correctly in print layout?
2. Net rates correct (€320/€960/€2,080)?
3. FAM date correct (31 Aug–3 Sep 2026)?
4. All photo src paths are local (ArticCruises-AIFiles/lovable-photos/)?
5. No external image URLs except gosaimaa.com if needed for specific known images

Write output to ~/1658HoldingsOy-AIFiles/arctic-cruises-b2b-flyer.html
On completion write: ~/1658HoldingsOy-AIFiles/_drafts/MANIFEST-S232.json
{"status": "complete", "file": "arctic-cruises-b2b-flyer.html", "lines": <N>}
```

### Subagent 1B: FAM INVITATION PACK

```
mode: bypassPermissions

TASK: Build the Arctic Cruises FAM invitation pack — 2 HTML documents.

SOURCE OF TRUTH — read these files first:
- ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html (route/resort/team detail)
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S233-ARCTIC-FAM-PACK.md (full PRD)

OUTPUT FILES:
1. ~/1658HoldingsOy-AIFiles/arctic-cruises-fam-invitation.html
2. ~/1658HoldingsOy-AIFiles/arctic-cruises-fam-programme.html

DOCUMENT 1 — FAM INVITATION (A4 portrait, 1 page):
- Full-bleed hero photo top 45% (saimaa-islands-summer-aerial.jpg)
- "An Invitation" in Playfair italic white over photo
- Body: exclusive, personal tone — "You are invited to be among the first 50 operators..."
- Bullet: what you experience (archipelago, seal sighting, smoke sauna, gala dinner, silence)
- Bullet: what you take home (experience, net rates, media pack, commercial agreement)
- Apply section: green band, "Apply to join · laura@finlanddmc.fi · Deadline: 15 July 2026"
- Partner logos strip at bottom

DOCUMENT 2 — FAM PROGRAMME BRIEF (A4 portrait, 2-3 pages):
- Day-by-day: 31 Aug (Day 1) through 3 Sep (Day 4) — see bridge for full programme
- Getting there: Helsinki → Lappeenranta (train 2.5h recommended)
- What to bring: smart casual, fleece, swimwear, binoculars
- What you take home: media pack, net rates, commercial agreement form
- Team on board: Saku, Laura, Captain, FinnConcierge
- Partner logos grid

FAM FACTS (confirmed):
- Dates: 31 Aug–3 Sep 2026
- Vessel: M/S Carelia
- Route: Lappeenranta → Puumala (Sahanlahti) → Savonlinna → Järvisydän → return
- Cost: Complimentary. All included.
- Max: 50 selected operators
- Apply: laura@finlanddmc.fi by 15 July 2026

SELF-CHECK before writing:
1. Invitation: exclusive tone, not mass-marketing tone?
2. FAM dates correct throughout both docs (31 Aug–3 Sep)?
3. Deadline consistent (15 July 2026)?
4. Programme: does Day 3 include the commercial briefing session on board?

On completion write: ~/1658HoldingsOy-AIFiles/_drafts/MANIFEST-S233.json
{"status": "complete", "files": ["arctic-cruises-fam-invitation.html", "arctic-cruises-fam-programme.html"]}
```

---

## WAVE 1 GATE CHECK (Orchestrator does this — not a subagent)

Before launching Wave 2:
1. Read MANIFEST-S232.json and MANIFEST-S233.json — both "complete"?
2. Check arctic-cruises-b2b-flyer.html exists and >200 lines
3. Check both FAM files exist
4. Quick scan: any "TODO" or "[placeholder]" left in files?
If gate fails → fix inline, do NOT relaunch subagent. Fix takes priority over speed.

---

## WAVE 2 — OPERATOR PRD (target: ~20min)

### Subagent 2: TOUR OPERATOR PRD

```
mode: bypassPermissions

TASK: Build the Arctic Cruises Tour Operator Product & Requirements Document.

SOURCE OF TRUTH — read these files first:
- ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S234-ARCTIC-OPERATOR-PRD.md (full PRD)
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2b-flyer.html (use for pricing consistency check)

OUTPUT FILE: ~/1658HoldingsOy-AIFiles/arctic-cruises-operator-prd.html

FORMAT: Clean HTML document, A4 portrait print layout, professional/operational tone
STRUCTURE (13 sections per bridge):
1. Product overview · 2. Product variants · 3. Pricing (net rates table)
4. Inclusions/exclusions · 5. Vessel spec · 6. Resort portfolio
7. Route details (AC-DAY, AC-3N, AC-7N) · 8. Departure schedule (full 2027 calendar)
9. Booking process · 10. Operational requirements · 11. Marketing assets
12. Credentials/certifications · 13. Contacts

KEY DATA:
- Net rates: Day €320 / 3N €960 / 7N €2,080 (20% early partner, before 15.07.2026)
- Deposit: 30% at booking, balance 60 days before departure
- What NOT to promise: seal sightings, exact resort at each stop
- Season: Every Wednesday May–Sep 2027

SELF-CHECK:
1. Does net rate table match exactly what's in B2B flyer (consistency)?
2. Is booking process complete (deposit % + balance timeline)?
3. "What NOT to promise" section present?
4. All 3 product variants (DAY, 3N, 7N) fully documented?

On completion write: ~/1658HoldingsOy-AIFiles/_drafts/MANIFEST-S234.json
{"status": "complete", "file": "arctic-cruises-operator-prd.html"}
```

---

## WAVE 2 GATE CHECK
1. MANIFEST-S234.json complete?
2. Net rates in PRD match net rates in flyer? (grep both files for "€320" — must appear in both)

---

## WAVE 3 — OPERATIONS BRIEF (target: ~20min)

### Subagent 3: OPERATIONS BRIEF

```
mode: bypassPermissions

TASK: Build the Arctic Cruises booking system PRD and Laura operations brief.

SOURCE OF TRUTH:
- ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S235-ARCTIC-OPERATIONS.md (full PRD)
- ~/1658HoldingsOy-AIFiles/arctic-cruises-operator-prd.html (for process consistency)

OUTPUT FILES:
1. ~/1658HoldingsOy-AIFiles/arctic-cruises-booking-system-prd.md (Airtable schema + recommendation)
2. ~/1658HoldingsOy-AIFiles/arctic-cruises-laura-operations-brief.md (5 email templates + FAM workflow)

BOOKING SYSTEM:
- Recommend Airtable (free tier Year 1)
- 4 tables: Enquiries / Confirmed Bookings / Departure Calendar / Operator Accounts
- Include complete field schemas for each table
- Include automation triggers: 60-day balance reminder, 30-day guest names reminder

LAURA OPERATIONS BRIEF:
- 5 email templates: B2C enquiry / Trade enquiry / FAM application confirmation / Booking confirmation / Balance reminder
- FAM workflow with key dates (now → 15.07 → 1.06 confirmed → 30.08 logistics → post-FAM 30 days)
- Trade show recommendations: ITB Berlin, WTM London, Nordic Visit orgs
- Cold outreach sequence (3-step)
- Post-FAM 30-day action plan

On completion write: ~/1658HoldingsOy-AIFiles/_drafts/MANIFEST-S235.json
{"status": "complete", "files": ["arctic-cruises-booking-system-prd.md", "arctic-cruises-laura-operations-brief.md"]}
```

---

## WAVE 4 — KNOWLEDGE BIBLE (target: ~25min)

### Subagent 4: KNOWLEDGE BIBLE

```
mode: bypassPermissions

TASK: Compile the Arctic Cruises Master Knowledge Document from all previous outputs.

DO NOT RECREATE FROM SCRATCH. Compile and synthesize from:
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html (destination + product + team copy)
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2b-flyer.html (commercial terms)
- ~/1658HoldingsOy-AIFiles/arctic-cruises-operator-prd.html (full operational spec)
- ~/1658HoldingsOy-AIFiles/arctic-cruises-laura-operations-brief.md (operations)
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S236-ARCTIC-KNOWLEDGE-BIBLE.md (structure)

OUTPUT FILE: ~/1658HoldingsOy-AIFiles/arctic-cruises-knowledge-bible.md

STRUCTURE (8 parts per bridge):
Part 1: The Destination (Saimaa geography, UNESCO, wildlife, history)
Part 2: The Company (who we are, team, vessel, resorts, local producers)
Part 3: The Products (AC-DAY, AC-3N, AC-7N — full specs)
Part 4: Competitive Positioning (vs fjords, river cruises; irreplaceable differentiator)
Part 5: Market & Positioning (target audience, trade channels, 2027 launch strategy)
Part 6: Sustainability & Conservation (FANC, UNESCO protocols, certifications)
Part 7: Press & Media Kit (5 angles, key facts, press contact)
Part 8: Commercial Terms (complete table)
Appendices: Glossary, Key dates, All contacts & links

QUALITY GATE (self-check before writing):
1. Does the document answer every question a journalist, product manager, and new team member would have?
2. Is the competitive positioning section specific (numbers, not just "we're better")?
3. Are all net rates consistent with operator-prd.html?
4. Is the press kit section ready to send to a travel journalist?
5. Word count target: 8,000-12,000 words

On completion write: ~/1658HoldingsOy-AIFiles/_drafts/MANIFEST-S236.json
{"status": "complete", "file": "arctic-cruises-knowledge-bible.md", "word_count": <N>}
```

---

## FINAL VALIDATION — ORCHESTRATOR

After Wave 4:

1. **Read all 5 manifests** — all "complete"?
2. **Pricing consistency check:**
   ```bash
   grep -n "€320\|€960\|€2,080\|€2,600\|€1,200" arctic-cruises-b2b-flyer.html arctic-cruises-operator-prd.html arctic-cruises-knowledge-bible.md
   ```
   All prices must be consistent across all files.
3. **Gemini judge on knowledge bible** (the master document judges the entire body of work):
   ```bash
   bash ~/run-gemini.sh --mode judge --file arctic-cruises-knowledge-bible.md --output-file /tmp/gemini-bible-judge.txt
   ```
   Target: ≥85/100. If FAIL → apply FIX_PRIORITY inline.

4. **Git commit all outputs:**
   ```bash
   git add arctic-cruises-b2b-flyer.html arctic-cruises-fam-invitation.html arctic-cruises-fam-programme.html arctic-cruises-operator-prd.html arctic-cruises-booking-system-prd.md arctic-cruises-laura-operations-brief.md arctic-cruises-knowledge-bible.md
   git commit -m "Arctic Cruises: full launch document suite (S232-S236 pipeline)"
   ```

5. **Write MANIFEST-COMPLETE.md:**
   ```
   # Arctic Cruises Document Pipeline — COMPLETE
   Date: [today]
   Session: S237
   
   | File | Lines/Words | Status |
   |------|-------------|--------|
   | arctic-cruises-b2b-flyer.html | [N] | ✅ |
   | arctic-cruises-fam-invitation.html | [N] | ✅ |
   | arctic-cruises-fam-programme.html | [N] | ✅ |
   | arctic-cruises-operator-prd.html | [N] | ✅ |
   | arctic-cruises-booking-system-prd.md | [N] | ✅ |
   | arctic-cruises-laura-operations-brief.md | [N] | ✅ |
   | arctic-cruises-knowledge-bible.md | [N] words | ✅ |
   
   Gemini final audit: [score]/100
   Git commit: [hash]
   Pipeline complete. Arctic Cruises launch-ready.
   ```

---

## FAILURE HANDLING

| Failure | Response |
|---------|----------|
| Subagent output <50 lines | Orchestrator rebuilds inline (don't relaunch) |
| Manifest missing | Check if file exists — if yes, write manifest manually |
| Gate check fails | Orchestrator fixes inline, marks as "FIXED by orchestrator" |
| Gemini judge FAIL | Apply FIX_PRIORITY inline, re-run judge once |
| Git commit blocked | Write files, skip commit, note in MANIFEST-COMPLETE.md |

---

## KEY FILES (load at session start)

```yaml
key_files:
  - ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md     # Commercial terms
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S232-ARCTIC-B2B-FLYER.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S233-ARCTIC-FAM-PACK.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S234-ARCTIC-OPERATOR-PRD.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S235-ARCTIC-OPERATIONS.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S236-ARCTIC-KNOWLEDGE-BIBLE.md
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
```

turn_budget: 14 (max 16)
mode: bypassPermissions
external_calls: "Gemini judge after Wave 4 (mandatory)"
session_type: BUILD PIPELINE (DDSC orchestrator)

---

*Bridge v1.0 — S231 2026-04-15*
*chmod 444*
