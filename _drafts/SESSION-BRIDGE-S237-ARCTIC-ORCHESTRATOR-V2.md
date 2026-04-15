---
session: 231
date: 2026-04-15
type: SESSION BRIDGE — Arctic Cruises Full-Pipeline Orchestrator V2
model_wrote: sonnet-4-6
model_executes: sonnet
priority: CRITICAL — autonomous build pipeline
chmod: 444
mode: bypassPermissions
spar_results: "Grok+Gemini unanimous on 4 critical fixes. V2 applies all 4."
supersedes: SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR.md
---

# SESSION BRIDGE S237 — ORCHESTRATOR V2
# ARCTIC CRUISES AUTONOMOUS BUILD PIPELINE
# Sparred: Grok + Gemini · 4 critical fixes applied
# chmod 444 — älä muokkaa

---

## CRITICAL FIXES APPLIED (from Grok+Gemini spar, 2026-04-15)

| Fix | Problem | Solution |
|-----|---------|----------|
| **Shared data contract** | Pricing hallucinated per subagent → Bible ≈52% correct | Pre-flight writes `PRICING-MASTER.json` + `PRODUCT-BRIEF.md` before Wave 1 |
| **Progressive commits** | Wave 4 failure = zero committed output | Commit after EACH wave gate passes |
| **Structural gate checks** | Self-reported MANIFEST = theater | Orchestrator validates: file exists + size >5KB + required strings present |
| **Wave isolation** | Parallel write collisions possible | Wave-1a/ and Wave-1b/ separate output dirs |

---

## ARCHITECTURE V2

```
PREFLIGHT (orchestrator only):
  Write PRICING-MASTER.json
  Write PRODUCT-BRIEF.md
  ↓
Wave 1 (parallel):
  [output/wave-1a/] B2B Flyer
  [output/wave-1b/] FAM Invitation + Programme Brief
  ↓ gate check + git commit
Wave 2 [output/wave-2/] Tour Operator PRD
  ↓ gate check + git commit
Wave 3 [output/wave-3/] Operations Brief (booking PRD + Laura brief)
  ↓ gate check + git commit
Wave 4 [output/wave-4/] Knowledge Bible — compiles from output/wave-1..3/
  ↓ cross-doc consistency check (Gemini)
  ↓ git commit + MANIFEST-COMPLETE.md
```

---

## PREFLIGHT — BEFORE ANY WAVE (turn 1)

Orchestrator writes both files from source. No subagent inference.

### PRICING-MASTER.json
```json
{
  "version": "2026-04-15",
  "source": "confirmed by Patrick, session S231",
  "b2c_prices": {
    "day_cruise": { "list": 400, "description": "Day on the Water — 1 day" },
    "short_cruise": { "list": 1200, "nights": 3, "description": "Saimaa Short Cruise" },
    "grand_cruise": { "list": 2600, "nights": 7, "description": "Grand Cruise on Lake Saimaa" }
  },
  "b2b_net_rates": {
    "day_cruise": { "net": 320, "commission_pct": 20 },
    "short_cruise": { "net": 960, "commission_pct": 20 },
    "grand_cruise": { "net": 2080, "commission_pct": 20 }
  },
  "payment_terms": {
    "deposit_pct": 30,
    "balance_days_before": 60,
    "early_partner_deadline": "2026-07-15"
  },
  "fam": {
    "cost_to_operator": "complimentary",
    "max_operators": 50,
    "dates": "2026-08-31 to 2026-09-03",
    "apply_deadline": "2026-07-15",
    "apply_email": "laura@finlanddmc.fi"
  },
  "single_supplement_per_night": 50,
  "season": "2027-05 to 2027-09",
  "departures": "every Wednesday 09:00"
}
```

### PRODUCT-BRIEF.md (≤500 words, injected into EVERY subagent)
```
# Arctic Cruises — Product Brief (Single Source of Truth)
## Inject this into every subagent prompt. Do not invent product facts.

**Brand:** Arctic Cruises (operated by Finland DMC Oy)
**Sub-brand:** Grand Cruise on Lake Saimaa
**Vessel:** M/S Carelia — Finland's last classic lake passenger vessel. On Saimaa since 1969.
  200 passenger capacity. Day vessel — NO overnight cabins. All nights at resorts.
**Season:** May–September 2027. Every Wednesday departure 09:00 from Lappeenranta.
**Inaugural season:** 2027

**Team:**
- Saku Hyttinen (Founder, Arctic Cruises) — 20+ years on Finnish waters
- Laura Ilvonen (Guest Experience & Trade Relations) — laura@finlanddmc.fi
- The Captain (lifetime on Saimaa)
- Patrick Heiskanen (Partner, 12th generation Saimaa hospitality)
- FinnConcierge (AI + human assistant, DE/EN/FR/FI)

**Destination:** Lake Saimaa, UNESCO Global Geopark (designated 2021). Eastern Finland.
4,400 islands. 1,700 km² surface area. Freshwater — drinking quality.
Saimaa ringed seal: ~500 individuals. Found NOWHERE else on Earth.
CRITICAL: Never say "you will see a seal." Always say "possible natural observation."

**Flagship Route (7-night):**
Day 1 Wed: Lappeenranta → Sahanlahti Resort (Night 1)
Day 2 Thu: → Olavinlinna castle passage → Järvisydän Resort (Night 2)
Day 3 Fri: → Varkaus locks → Kuopio (Night 3)
Day 4 Sat: Kuopio full day — Puijo Tower (Night 4)
Day 5 Sun: → Järvisydän Resort, Gala dinner (Night 5)
Day 6 Mon: → Sahanlahti, farewell sauna (Night 6)
Day 7 Tue: → Lappeenranta, disembark by noon

**Resort partners:** Sahanlahti (Puumala) · Järvisydän (Heinävesi, Green Key) · Kuopio hotels
**Certifications:** UNESCO Geopark · Green Key (Järvisydän) · European Region of Gastronomy 2024

**Pricing (read from PRICING-MASTER.json — do not invent):**
Day: €400 list / €320 net | 3-night: €1,200 list / €960 net | 7-night: €2,600 list / €2,080 net
Commission: 20% early partner (apply before 15 Jul 2026)
Deposit: 30% at booking. Balance: 60 days before departure.

**FAM:** 31 Aug–3 Sep 2026 · Complimentary · 50 selected operators · Apply by 15 Jul 2026

**Target audience:** Affluent independent travellers, 50-68, DACH/UK/US primary
**Primary competitive frame:** NOT Norwegian fjords (crowded). NOT river cruises (€5k). 
Saimaa = last undiscovered freshwater cruise in Europe.
```

---

## WAVE 1 — PARALLEL (target: ~20min)

**Pre-wave:** Confirm PRICING-MASTER.json and PRODUCT-BRIEF.md exist. If missing, write them first.

### Subagent 1A — B2B Flyer
```
mode: bypassPermissions
output_dir: output/wave-1a/

INJECT THIS FIRST (verbatim):
[full contents of PRODUCT-BRIEF.md]

TASK: Build the Arctic Cruises B2B tour operator sales flyer.

READ THESE FILES:
- ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html (design reference — same CSS variables)
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S232-ARCTIC-B2B-FLYER.md (full PRD)
- ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json (pricing — use ONLY these numbers)

OUTPUT: ~/1658HoldingsOy-AIFiles/output/wave-1a/arctic-cruises-b2b-flyer.html

DESIGN SPEC:
- A4 landscape. @page { size: A4 landscape; margin: 0; } in @media print
- Two <section class="flyer-page"> with page-break-after: always between them
- CSS variables from B2C: --accent #2c6e4f, --gold #C49A6C, navy #1a2332
- Google Fonts: Playfair Display + Open Sans (same import as B2C site)
- Photos: ArticCruises-AIFiles/lovable-photos/ paths (local only)

PAGE 1 (FRONT — beauty + product):
- Header: dark navy bar. "Grand Cruise on Lake Saimaa · Arctic Cruises · 2027 Season"
- Hero: full-width photo (saimaa-islands-summer-aerial.jpg) with headline overlay
- Headline: "The European Nature Cruise Your Clients Are Looking For"
- Three USP columns: Endemic & Irreplaceable · Premium at Accessible Price · Discovery Advantage
- Pricing table: Day / 3-night / 7-night — list price AND net rate (from PRICING-MASTER.json)

PAGE 2 (BACK — commercial):
- Commercial terms: 20% commission · 30% deposit · 60-day balance · apply before 15 Jul 2026
- Inclusions list (7-night Grand Cruise)
- Booking process steps (numbered, 1-5)
- FAM teaser: full-width navy band "Be among the first 50 operators · 31 Aug–3 Sep 2026 · Complimentary · Apply: laura@finlanddmc.fi"
- Partner logos strip: GoSaimaa · Visit Finland · UNESCO Global Geopark · Green Key · etc.
- Footer: "Arctic Cruises Oy / Finland DMC Oy · laura@finlanddmc.fi"

CRITICAL RULES:
- Generate once, write once. Do NOT re-read and revise.
- All prices from PRICING-MASTER.json only. Zero exceptions.
- "Possible natural observation" for seal — never "see a seal"
- No external image URLs except gosaimaa.com if needed
```

### Subagent 1B — FAM Pack
```
mode: bypassPermissions
output_dir: output/wave-1b/

INJECT THIS FIRST (verbatim):
[full contents of PRODUCT-BRIEF.md]

TASK: Build 2 FAM documents.

READ THESE FILES:
- ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html (team/resort/route detail)
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S233-ARCTIC-FAM-PACK.md (full PRD)
- ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json

OUTPUTS:
1. ~/1658HoldingsOy-AIFiles/output/wave-1b/arctic-cruises-fam-invitation.html
2. ~/1658HoldingsOy-AIFiles/output/wave-1b/arctic-cruises-fam-programme.html

FAM FACTS (authoritative — do not deviate):
- Dates: 31 August – 3 September 2026 (4 days, 3 nights)
- Cost: Complimentary. All included.
- Max: 50 selected operators
- Apply: laura@finlanddmc.fi by 15 July 2026

DOC 1 — INVITATION (A4 portrait, 1 page):
- Exclusive, personal tone. NOT mass-marketing.
- Full-bleed hero: "An Invitation" Playfair italic white over saimaa-islands-summer-aerial.jpg
- Body: "You are invited to be among the first 50 operators..."
- What you experience (5 bullets) + What you take home (4 bullets)
- Green CTA band: "Apply to join · laura@finlanddmc.fi · Deadline 15 July 2026"

DOC 2 — PROGRAMME BRIEF (A4 portrait, 2-3 pages):
- Day-by-day: 31 Aug → 3 Sep (4 days)
- Day 3 MUST include commercial briefing session on board (net rates + agreements)
- Logistics: Helsinki → Lappeenranta (train 2.5h)
- What to bring + what you take home (media pack, net rates, commercial agreement)
- Team on board: Saku, Laura, Captain, FinnConcierge
- Partner logos grid

CRITICAL RULES: Generate once, write once. All dates from PRICING-MASTER.json.
```

---

## WAVE 1 GATE CHECK (orchestrator, not subagent)

```python
# Structural validation — NOT self-reported manifest
def wave1_gate():
    checks = [
        # File existence + minimum size
        ("output/wave-1a/arctic-cruises-b2b-flyer.html", 5000),  # >5KB
        ("output/wave-1b/arctic-cruises-fam-invitation.html", 2000),
        ("output/wave-1b/arctic-cruises-fam-programme.html", 3000),
    ]
    required_strings = {
        "arctic-cruises-b2b-flyer.html": ["€320", "€960", "€2,080", "15 July 2026", "laura@finlanddmc.fi"],
        "arctic-cruises-fam-invitation.html": ["31 August", "3 September", "50", "15 July 2026"],
        "arctic-cruises-fam-programme.html": ["31 Aug", "3 Sep", "laura@finlanddmc.fi"],
    }
    # All checks must pass before proceeding
```

In practice (no Python in Claude Code): orchestrator uses Bash:
```bash
# Size check
wc -c output/wave-1a/arctic-cruises-b2b-flyer.html | awk '{if($1<5000) exit 1}'
# Required strings
grep -c "€320\|€960\|€2,080" output/wave-1a/arctic-cruises-b2b-flyer.html
grep -c "15 July 2026" output/wave-1a/arctic-cruises-b2b-flyer.html
```

If any check fails → orchestrator fixes inline (targeted edit, not rebuild). Mark as "FIXED W1" in commit message.

**Progressive commit after gate pass:**
```bash
git add output/wave-1a/ output/wave-1b/
git commit -m "Arctic Pipeline Wave 1: B2B flyer + FAM pack (gate passed)"
```

---

## WAVE 2 — TOUR OPERATOR PRD (target: ~20min)

### Subagent 2
```
mode: bypassPermissions

INJECT THIS FIRST: [full contents of PRODUCT-BRIEF.md]

TASK: Build the Tour Operator PRD.

READ:
- ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json (pricing master)
- ~/1658HoldingsOy-AIFiles/output/wave-1a/arctic-cruises-b2b-flyer.html (consistency check)
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S234-ARCTIC-OPERATOR-PRD.md (full spec)

OUTPUT: ~/1658HoldingsOy-AIFiles/output/wave-2/arctic-cruises-operator-prd.html

13-section PRD per bridge spec. Key data from PRICING-MASTER.json only.
CRITICAL: Net rate table must match flyer exactly (grep both after writing).
Generate once, write once.
```

**Wave 2 gate check:**
```bash
grep -c "€320\|€960\|€2,080" output/wave-2/arctic-cruises-operator-prd.html
grep -c "laura@finlanddmc.fi" output/wave-2/arctic-cruises-operator-prd.html
grep -c "possible natural observation\|possible.*sighting" output/wave-2/arctic-cruises-operator-prd.html
```

**Progressive commit:**
```bash
git add output/wave-2/
git commit -m "Arctic Pipeline Wave 2: Tour Operator PRD (gate passed)"
```

---

## WAVE 3 — OPERATIONS BRIEF (target: ~20min)

### Subagent 3
```
mode: bypassPermissions

INJECT THIS FIRST: [full contents of PRODUCT-BRIEF.md]

TASK: Build booking system PRD + Laura operations brief.

READ:
- ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S235-ARCTIC-OPERATIONS.md (full spec)
- ~/1658HoldingsOy-AIFiles/output/wave-2/arctic-cruises-operator-prd.html (process consistency)

OUTPUTS:
1. ~/1658HoldingsOy-AIFiles/output/wave-3/arctic-cruises-booking-system-prd.md
2. ~/1658HoldingsOy-AIFiles/output/wave-3/arctic-cruises-laura-operations-brief.md

Include all 5 email templates + Airtable schema (4 tables with full field lists) +
FAM workflow key dates + post-FAM 30-day action plan.
Generate once, write once.
```

**Wave 3 gate check:**
```bash
grep -c "Template\|template" output/wave-3/arctic-cruises-laura-operations-brief.md  # ≥5 templates
grep -c "Airtable\|Table " output/wave-3/arctic-cruises-booking-system-prd.md        # Airtable schema present
```

**Progressive commit:**
```bash
git add output/wave-3/
git commit -m "Arctic Pipeline Wave 3: Operations Brief + Booking PRD (gate passed)"
```

---

## WAVE 4 — KNOWLEDGE BIBLE (target: ~25min)

### Subagent 4
```
mode: bypassPermissions

INJECT THIS FIRST: [full contents of PRODUCT-BRIEF.md]

TASK: Compile the Arctic Cruises Master Knowledge Document from all wave outputs.

COMPILE FROM (read all):
- ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json
- ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
- ~/1658HoldingsOy-AIFiles/output/wave-1a/arctic-cruises-b2b-flyer.html
- ~/1658HoldingsOy-AIFiles/output/wave-1b/arctic-cruises-fam-invitation.html
- ~/1658HoldingsOy-AIFiles/output/wave-1b/arctic-cruises-fam-programme.html
- ~/1658HoldingsOy-AIFiles/output/wave-2/arctic-cruises-operator-prd.html
- ~/1658HoldingsOy-AIFiles/output/wave-3/arctic-cruises-laura-operations-brief.md
- ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S236-ARCTIC-KNOWLEDGE-BIBLE.md (structure)

OUTPUT: ~/1658HoldingsOy-AIFiles/output/wave-4/arctic-cruises-knowledge-bible.md

8-part structure per bridge. Target: 8,000-12,000 words.
DO NOT SUMMARIZE. SYNTHESIZE.
For each section: extract facts from source files → cross-reference → write authoritative prose.
If any conflict found between wave outputs: use PRICING-MASTER.json as tiebreaker.
Generate once, write once.
```

---

## FINAL VALIDATION (orchestrator, after Wave 4)

### Step 1: Cross-document consistency check

Extract key claims from all 7 output files and check for contradictions:

```bash
echo "=== PRICING CONSISTENCY ===" && \
grep -h "€320\|€960\|€2,080\|€2,600\|€1,200\|€400" \
  output/wave-1a/arctic-cruises-b2b-flyer.html \
  output/wave-2/arctic-cruises-operator-prd.html \
  output/wave-4/arctic-cruises-knowledge-bible.md | sort | uniq -c

echo "=== FAM DATE CONSISTENCY ===" && \
grep -h "31 Aug\|3 Sep\|15 Jul\|15 July" \
  output/wave-1b/arctic-cruises-fam-invitation.html \
  output/wave-1b/arctic-cruises-fam-programme.html \
  output/wave-4/arctic-cruises-knowledge-bible.md | sort | uniq

echo "=== SEAL LANGUAGE ===" && \
grep -c "will see a seal\|guaranteed.*seal\|see.*seal" \
  output/wave-1a/arctic-cruises-b2b-flyer.html \
  output/wave-1b/arctic-cruises-fam-invitation.html \
  output/wave-2/arctic-cruises-operator-prd.html
# Any count > 0 = FAIL — fix that file before commit
```

### Step 2: Gemini cross-document judge

```bash
cat > /tmp/arctic-final-judge.txt << 'PROMPT'
You are auditing a set of 3 commercial documents for Arctic Cruises (luxury Finland lake cruise).
Check for contradictions and completeness across these documents.

Extract and compare: all prices, all dates, all contact emails, any promises about seal sightings.
Flag any contradiction between documents as CONFLICT.
Flag any missing required element as MISSING.

Required in ALL commercial docs: net rate (€320/€960/€2,080), FAM date (31 Aug-3 Sep 2026), apply deadline (15 Jul 2026), contact (laura@finlanddmc.fi)
Prohibited: "will see a seal", "guaranteed sighting"

[PASTE: output/wave-1a/arctic-cruises-b2b-flyer.html excerpt]
[PASTE: output/wave-2/arctic-cruises-operator-prd.html excerpt]
[PASTE: output/wave-4/arctic-cruises-knowledge-bible.md excerpt]

Return: CONFLICTS: [list] | MISSING: [list] | PASS/FAIL
PROMPT
bash ~/run-gemini.sh --prompt-file /tmp/arctic-final-judge.txt --output-file /tmp/gemini-final-pipeline-audit.txt
```

### Step 3: Copy outputs to main directory + final commit

```bash
# Copy final outputs to root
cp output/wave-1a/arctic-cruises-b2b-flyer.html ./
cp output/wave-1b/arctic-cruises-fam-invitation.html ./
cp output/wave-1b/arctic-cruises-fam-programme.html ./
cp output/wave-2/arctic-cruises-operator-prd.html ./
cp output/wave-3/arctic-cruises-booking-system-prd.md ./
cp output/wave-3/arctic-cruises-laura-operations-brief.md ./
cp output/wave-4/arctic-cruises-knowledge-bible.md ./

git add arctic-cruises-b2b-flyer.html arctic-cruises-fam-invitation.html \
  arctic-cruises-fam-programme.html arctic-cruises-operator-prd.html \
  arctic-cruises-booking-system-prd.md arctic-cruises-laura-operations-brief.md \
  arctic-cruises-knowledge-bible.md output/ PRICING-MASTER.json PRODUCT-BRIEF.md

git commit -m "Arctic Cruises: full launch document suite (S237 autonomous pipeline)"
```

### Step 4: Write MANIFEST-COMPLETE.md

```markdown
# Arctic Cruises Document Pipeline — COMPLETE
Date: [today] | Session: S237 | Pipeline: V2 (Grok+Gemini sparred)

| File | Size | Gate | Status |
|------|------|------|--------|
| arctic-cruises-b2b-flyer.html | [N]KB | W1 ✅ | ✅ |
| arctic-cruises-fam-invitation.html | [N]KB | W1 ✅ | ✅ |
| arctic-cruises-fam-programme.html | [N]KB | W1 ✅ | ✅ |
| arctic-cruises-operator-prd.html | [N]KB | W2 ✅ | ✅ |
| arctic-cruises-booking-system-prd.md | [N]KB | W3 ✅ | ✅ |
| arctic-cruises-laura-operations-brief.md | [N]KB | W3 ✅ | ✅ |
| arctic-cruises-knowledge-bible.md | [N] words | W4 ✅ | ✅ |

Gemini cross-doc audit: PASS
Git commit: [hash]
Pipeline complete. Arctic Cruises launch-ready.
```

---

## FAILURE HANDLING V2

| Failure | Response |
|---------|----------|
| Gate check fails (size/string) | Orchestrator targeted fix (1-2 edits), mark "FIXED", proceed |
| Gemini finds CONFLICT | Orchestrator resolves from PRICING-MASTER.json (authoritative), fix files |
| Gemini finds MISSING | Orchestrator adds missing element inline |
| Wave 4 fails completely | Waves 1-3 already committed. Restart Wave 4 only with fresh subagent. |
| Any file writes to wrong path | Move file, do not rebuild |

---

## KEY FILES (load at session start)

```yaml
preflight_write:
  - output/PRICING-MASTER.json    # Write from PRODUCT-BRIEF content
  - output/PRODUCT-BRIEF.md       # Write from bridge specs + memory

key_files:
  - ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S232-ARCTIC-B2B-FLYER.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S233-ARCTIC-FAM-PACK.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S234-ARCTIC-OPERATOR-PRD.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S235-ARCTIC-OPERATIONS.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S236-ARCTIC-KNOWLEDGE-BIBLE.md
```

turn_budget: 18 (max 22 — realistic after spar feedback)
mode: bypassPermissions
external_calls: "Gemini cross-doc consistency check (mandatory, Wave 4)"
session_type: ORCHESTRATOR (DDSC, bypassPermissions)

---

*Bridge v2.0 — S231 2026-04-15 — Grok+Gemini sparred, 4 critical fixes applied*
*chmod 444*
