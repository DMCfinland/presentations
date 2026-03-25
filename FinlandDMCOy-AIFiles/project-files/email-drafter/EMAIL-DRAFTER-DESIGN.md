# Finland DMC — AI Assistant: Full System Design

**Version:** 3.0 (complete formalization)
**Date:** 2026-02-20
**Author:** Patrick Heiskanen + Claude Sonnet (session 32)
**Status:** Approved for phased build — pilot with Liisa Vihermaa first
**Source data:** Mining sessions 1-6, TT research, email mining best practices research

---

## Philosophy

**Full automation with human evaluation, not half-automation.**

Half-automation forces staff to understand the full workflow while also supervising AI work — the worst of both worlds. Full automation + human approval at key checkpoints is cleaner:

```
Old model:          Staff constructs → staff checks → staff sends
Half-automation:    AI drafts → staff reconstructs mentally → staff sends
Full automation:    AI constructs → staff approves → system sends
```

Staff time is entirely freed for the **human layer**: building client trust, handling on-trip problems, cold acquisition, judgment calls. The AI handles everything that doesn't need a human.

**Run alongside the old workflow.** The new system is additive, never replacement. If the AI is down or wrong, staff can always work the old way. Pilot with Liisa Vihermaa before expanding to Laura, Reeta, Sebastian.

**Trust through transparency.** For every AI suggestion, show WHY it was recommended — based on Finland DMC's own confirmed booking data. Staff who understand the reasoning adopt the tool. Staff who get unexplained suggestions distrust it.

**One platform, multiple companies.** Finland DMC is the pilot. The same n8n backbone, golden prompts, and Second Brain architecture deploys to Järvisydän, M/S Marival, and other 1658 Holdings companies with different data and prompts.

---

## Architecture Overview

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 3 — FUTURE: Full Itinerary Automation
  AI generates complete itinerary → pushes to TT via API
  → TT renders viewable URL → email wrapper auto-drafted
  Prerequisites: TT write API confirmed, full Second Brain built

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 4 — FUTURE: Multi-Source Second Brain Synthesis
  Agent Teams orchestration (experimental, enable after all data loaded)
  Trigger: proposals pipeline + mass email mining + TT itinerary archive
  all available simultaneously (3 data sources, context limit exceeded)
  Agent A (proposals) + Agent B (emails) + Agent C (TT) → debate → unified profile
  Each agent owns one source; coordinator synthesises across context limits
  Prerequisites: Mass email mining complete, TT API access, Agent Teams stable

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 2 — NEXT: Component Recommender
  Staff profiles trip → AI recommends 8-12 components from
  1000+ library (ranked by Second Brain win rates + reasoning)
  → Staff selects/edits → builds in TT → paste URL into staff UI
  Prerequisites: TT component export, mass mining complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 1 — NOW: Email Drafter (build this weekend)
  Staff pastes incoming email → system auto-detects task
  → searches Second Brain → selects golden prompt → drafts response
  → staff reviews/edits → approves → sent
  Prerequisites: Sessions 1-6 data ← we have this

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOUNDATION: Second Brain
  Client profiles, component win rates, pricing patterns,
  staff style templates, conversion signals, TT itinerary archive
  Built from: mass email mining + TT URL scraping

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## The Full System Flow

```
┌─────────────────────────────────────────────────────────────┐
│ INPUT — Staff pastes incoming email                         │
│  "Dear Finland DMC, we represent 15 luxury travelers        │
│   from Iceland looking for a Lake Saimaa programme..."      │
└───────────────────────────┬─────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 1: SECOND BRAIN SEARCH (Haiku, ~€0.001)               │
│  Scans: sender domain, company name, email content          │
│  Returns: full client profile automatically                 │
│                                                             │
│  ┌─ FOUND ──────────────────────────────────────────────┐  │
│  │ Nordic Luxury · Katerina Eremeeva · Iceland          │  │
│  │ Agent type: Luxury DMC / agency                      │  │
│  │ Staff owner: Laura Ilvonen                           │  │
│  │ Last contact: Jan 2026 — pricing delay, still active │  │
│  │ Signal: frustrated by pricing speed — act fast       │  │
│  │ Mode: → Agency B2B (Laura style)                    │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 2: TASK DETECTION (Haiku, automatic)                   │
│  Analyzed: email content + client history                   │
│                                                             │
│  Task: NEW INQUIRY — Agency B2B                            │
│  Golden prompt: #02 — Agency inquiry response              │
│  Model: Sonnet                                             │
│  Confidence: 96%                                           │
│  Alert: ⚠️ Pricing delay history — respond within 24h      │
└───────────────────────────┬─────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 3: DRAFT GENERATION (Sonnet executes golden prompt)    │
│                                                             │
│  ┌─ ITINERARY SUGGESTION (with reasoning) ─────────────┐   │
│  │ For this trip profile, based on 5 confirmed         │   │
│  │ bookings for similar clients:                       │   │
│  │                                                     │   │
│  │ ★★★★★ Smoke Sauna   — 5/5 confirmed, never removed  │   │
│  │ ★★★★★ Seal Safari   — 5/5 confirmed, never removed  │   │
│  │ ★★★★☆ Solitary      — 4/5 confirmed ⚠️ NO commission│   │
│  │ ★★★☆☆ E-fatbike     — 3/5 confirmed                 │   │
│  │ ★★☆☆☆ Putkisalo     — 2/5 (often removed in v2)     │   │
│  │                                                     │   │
│  │ Typical revision: yoga added in v2 (60% of cases)  │   │
│  │ → include as optional in v1                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─ EMAIL DRAFT ────────────────────────────────────────┐   │
│  │ "Dear Katerina,                                     │   │
│  │  Thank you for your detailed suggested program...   │   │
│  │                                                     │   │
│  │ [TT BLOCK — add link once built]                   │   │
│  │  Nordic Luxury [dates], [ref], [N] days - Travel   │   │
│  │  Tree                                              │   │
│  │                                                     │   │
│  │ [PRICING BLOCK — from rate card]                   │   │
│  │  Kuru NET rates: Double room €304/night            │   │
│  │  SUP trip: €59.90/pp (15% commission)              │   │
│  │  ⚠️ Solitary restaurant: NO commission             │   │
│  │                                                     │   │
│  │ [UPSELL BLOCK — drag/click to add]                 │   │
│  │  ★ Yoga session (add to v1 as optional)            │   │
│  │  ★ Wild herbs workshop                             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  Progress: ████████░░ 80%                                   │
│  ❌ Missing: Budget range question                           │
│  ❌ Missing: Preferred activity level question               │
└───────────────────────────┬─────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 4: HUMAN REVIEW + EDIT LOOP                           │
│                                                             │
│  Staff sees: full draft + Second Brain context + reasoning  │
│                                                             │
│  Options:                                                   │
│  [Edit inline]    → click any text, edit directly          │
│  [Add feedback]   → "make more formal" / "add aurora tour" │
│  [Regenerate]     → AI rewrites based on feedback          │
│  [Change mode]    → switch Laura → Sebastian style          │
│  [Edit in TT]     → opens TT in new tab (deep link)        │
│                                                             │
│  Feedback:                                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ "Add Helsinki pre-programme option for 2 nights"    │  │
│  │                              [Regenerate with this] │  │
│  └──────────────────────────────────────────────────────┘  │
└───────────────────────────┬─────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ STEP 5: COMMIT (staff decides)                             │
│                                                             │
│  ○ [Copy to Outlook]   → paste and send manually           │
│  ○ [Send via M365 API] → system sends automatically        │
│                                                             │
│  After commit:                                              │
│  → Second Brain updated: "Responded to Nordic Luxury       │
│    Feb 21, 2026 — new inquiry, 15 pax, Lake Saimaa"        │
└─────────────────────────────────────────────────────────────┘
```

---

## TT Integration: Three Stages

### Stage 1 (NOW): Deep Link
Staff builds TT manually → pastes URL into staff UI → email wrapper generated.
**Edit flow:** "Edit in TT" button opens TT in new tab. Staff edits, copies new URL back.
- Feasibility: Works today, zero build cost
- Friction: One tab switch

### Stage 2 (After TT API confirmed): Programmatic Create
AI outputs structured itinerary brief → n8n calls TT write API → TT generates URL automatically.
Staff sees URL in draft without opening TT at all.
- Requires: TT Pro plan + confirmed write API
- Friction: Zero for standard proposals

### Stage 3 (Full vision): Embedded TT or Component Editor
**Option A — Embedded TT iframe:** TT builder displayed directly inside staff UI.
- Feasibility: Depends on TT's iframe policy (many block for security reasons)
- Staff edits itinerary without leaving staff UI — most seamless

**Option B — Component list editor in staff UI:**
Staff sees structured component list (not full TT UI), edits by adding/removing/reordering.
Changes pushed to TT via API → new URL generated automatically.
- Doesn't replicate TT's visual richness, but enables full automation
- Best balance: familiar enough, fully automated

**Recommendation:** Stage 1 now. Ask TT about iframe embedding and write API in the same contact email. Stage 2 when API confirmed. Decide A vs B based on TT's iframe policy.

---

## TT as Pricing Layer: Both Attached and Standalone

TT has a Prices tab + dynamic calculator. Finland DMC currently excludes pricing from TT (commission sensitivity for B2B clients, format complexity).

**Design approach — dual use:**

```
ATTACHED (context-aware):
  When generating a proposal → pricing block auto-populated
  from rate card + component selection
  Shows: NET rates, commission structure, exceptions
  Linked to: specific TT itinerary being drafted

STANDALONE (analysis):
  Pricing database queryable independently:
  "Show all Kuru Resort rates we've quoted in the last 12 months"
  "Which activities have the highest commission margin?"
  "What's our average markup by client segment?"
  Feeds: Second Brain win/loss analysis, rate card updates
```

This gives both immediate proposal utility AND longer-term pricing intelligence.

---

## Psychology Levers: Applied to the Entire Workflow

These 7 levers are not just UI features — they should be embedded at every stage of the n8n workflow, the golden prompts, the Second Brain design, and the staff experience.

### Lever 1: Push, don't pull — at every node
**Principle:** Staff should never have to seek information. The system surfaces what's relevant automatically.

| Workflow stage | How lever applies |
|---|---|
| Email arrives | Second Brain lookup fires automatically — no "search" button |
| Task detected | Context card appears without prompting — staff sees client history before reading the full email |
| Itinerary suggested | Top 8 components surface with win rates — no scrolling through 1000 |
| After send | Second Brain updates automatically — no manual CRM logging |
| 48h after send | System reminds staff if no client reply (conversion window alert) |

### Lever 2: Curate, don't dump — filtering at source
**Principle:** Too much information is worse than too little. Every output should be the minimum needed for a confident decision.

| Workflow stage | How lever applies |
|---|---|
| Component recommendations | 1000 components → top 8 based on win rates for this profile |
| Client history | 3-year history → 5 most relevant signals shown |
| Golden prompt context | Full Second Brain → only the facts this task type needs injected |
| Upsell block | All activities → only those with ≥40% win rate for this segment |

### Lever 3: Progress signals — always show what's missing
**Principle:** Incomplete things create urgency to finish. A visible checklist prevents errors and builds momentum.

| Workflow stage | How lever applies |
|---|---|
| Draft review | Checklist: ✅ Opening ✅ TT link ❌ Payment terms ❌ Commission exception |
| Itinerary brief | "DAY 3 has no activity — typical for this segment: sauna on Day 3" |
| Post-send | "Proposal sent. No reply in 3 days. Conversion window closing." |
| Pilot tracking | Weekly: "8 proposals sent. 3 confirmed. 2 still in window. 3 closed." |

### Lever 4: Own-data proof — Finland DMC's numbers, not generic benchmarks
**Principle:** Staff trust data from their own experience over external statistics. Own-data proof is 3x more persuasive than industry benchmarks.

| Workflow stage | How lever applies |
|---|---|
| Response time alert | "Your proposals sent <24h convert at 71%. You're in the window — 19h left." |
| Component suggestion | "Smoke Sauna: confirmed in 5/5 of your Kuru Resort FIT bookings" |
| Mode selection | "Sebastian's FIT mode: last 7 FIT direct proposals = 4 confirmed (57%)" |
| Pricing format | "Itemized per-person format: used in all your confirmed FIT direct bookings" |
| After mass mining | "We found 47 confirmed proposals in your mailbox. Here's what they have in common." |

### Lever 5: Voice matching — staff hear themselves, not AI
**Principle:** Staff adopt tools that write in their voice. Rejected AI output = unrecognizable voice. Accepted AI output = "this sounds like me."

| Workflow stage | How lever applies |
|---|---|
| Mode auto-selection | "Agency B2B detected → Laura mode" |
| Opening line | Verbatim from Laura's confirmed emails — not AI-invented language |
| Upsell language | Sebastian's exact phrases: "whatever you have on your mind... fulfill your dreams" |
| Commission exception | Laura's exact phrasing: "NO commission on Solitary restaurant" |
| Closing | Staff-specific: Sebastian = "Let me know if you have any questions!" / Laura = "I look forward to hearing your feedback!" |
| Golden prompt design | Each prompt built from real email analysis — every phrase traceable to a real sent email |

### Lever 6: Trusted colleague feel — not a warning system, a colleague
**Principle:** Systems that warn and caution feel like surveillance. Systems that remind and suggest feel like support. Same information, very different tone.

| Wrong (surveillance) | Right (colleague) |
|---|---|
| "⚠️ Commission exception detected for Solitary restaurant" | "💡 Solitary dinner is in here — remember it has no commission, worth flagging to Katerina" |
| "⚠️ No response to this proposal in 5 days" | "💡 Karu.io hasn't replied to your proposal — Sebastian had a similar case, he sent 'did you find what you were looking for?' and it reopened the conversation" |
| "⚠️ Missing payment terms" | "💡 Add payment terms — AABEI needed 20% deposit 3 months out, probably similar for this client" |

### Lever 7: Staff control — AI proposes, staff own
**Principle:** Automation fails when staff feel replaced. Automation succeeds when staff feel amplified. The commit decision is always human.

| Workflow stage | How lever applies |
|---|---|
| Draft generated | "Draft ready for your review. 0 changes made by you yet." |
| Feedback loop | Staff adds note → AI rewrites → staff sees exactly what changed |
| Commit options | Staff always chooses: copy to Outlook OR system sends — never automatic without approval |
| Version control | "This is version 2 of this proposal. Version 1 sent Feb 12." |
| Outcome recording | "Mark as: Won / Lost / Still active" — staff decides outcome, not AI inference |
| Improvement loop | "You changed the opening in 3 of your last 5 drafts. Should we update Laura's default?" |

### Where each lever lives in the stack

| Layer | Lever 1 | Lever 2 | Lever 3 | Lever 4 | Lever 5 | Lever 6 | Lever 7 |
|---|---|---|---|---|---|---|---|
| n8n workflow | ★ automatic trigger | ★ context filter | ★ progress calc | ★ win rate query | ★ mode select | | |
| Golden prompts | | ★ inject only what's needed | ★ checklist in prompt | ★ own-data in context | ★ staff style in system prompt | ★ colleague framing | ★ "suggest don't decide" |
| Second Brain DB | ★ pushes automatically | ★ stores ranked data | ★ tracks completeness | ★ stores real outcomes | ★ stores verbatim language | ★ stores history signals | ★ stores staff edits |
| UI | ★ surfaces on load | ★ shows top 8 | ★ progress bar | ★ shows real stats | ★ mode label | ★ conversational alerts | ★ approve/edit/reject |

---

## Trust-Building: The Reasoning Layer

For every AI suggestion, show WHY — based on Finland DMC's own data:

```
┌─ WHY WE SUGGEST SMOKE SAUNA ──────────────────────────────┐
│                                                           │
│ Based on your confirmed bookings:                        │
│                                                           │
│ ✓ Used in 5/5 confirmed Lake Saimaa FIT direct bookings  │
│ ✓ Never removed in any client revision (for this segment)│
│ ✓ Mentioned positively in 3 client confirmation emails:  │
│   "The smoke sauna was the highlight of the trip"        │
│ ✓ Commission applies (€85/session, 15%)                  │
│                                                           │
│ Confidence: Very high — core non-negotiable component    │
│ for luxury FIT sauna retreats                            │
└───────────────────────────────────────────────────────────┘
```

```
┌─ WHY WE SUGGEST ADDING YOGA AS OPTIONAL ──────────────────┐
│                                                           │
│ Based on revision patterns in similar bookings:          │
│                                                           │
│ ✓ Added in v2 in 60% of confirmed FIT direct bookings    │
│ ✓ Clients request it themselves — we can preempt in v1   │
│ ✓ Positions you as thoughtful: "anticipates what we need"│
│ ⚠️ NO commission on yoga sessions — flag in pricing      │
│                                                           │
│ Recommendation: List as "Optional add-on" in v1          │
│ → reduces chance of v2 revision needed                   │
└───────────────────────────────────────────────────────────┘
```

This transforms the AI from a "black box" into a "knowledgeable colleague explaining their thinking." Staff adoption is dramatically higher when they understand the reasoning.

---

## The 13 Golden Prompts

System auto-detects task from email content + Second Brain. Staff never selects.

| # | Task | Trigger signals | Model | Notes |
|---|---|---|---|---|
| 01 | **Draft proposal** | TT link available, pricing data, itinerary request | Sonnet | Core workflow |
| 02 | **Reply to new inquiry** | First contact, no prior history, "looking for DMC" | Sonnet | Qualify + tone |
| 03 | **Send revision** | "changes", "update", "version 2", client edits | Sonnet | Acknowledge + reframe |
| 04 | **Confirm booking** | "confirmed", deposit received, "go ahead" | Haiku | Structured, operational |
| 05 | **Chase pending proposal** | No reply 5+ days, proposal previously sent | Sonnet | Soft, no pressure |
| 06 | **Handle complaint/dispute** | "problem", "issue", allocation dispute, on-trip | Opus | High stakes |
| 07 | **Supplier outreach** | Known supplier domain, rate/availability request | Haiku | Structured, brief |
| 08 | **Re-engage warm lead** | 30-90 days since contact, positive prior signals | Sonnet | Relationship |
| 09 | **Internal brief handoff** | Staff-to-staff, "can you handle", "brief for" | Haiku | Structured data transfer |
| 10 | **Allocation management** | Repeat operator, departure series, block bookings | Sonnet | Volume account |
| 11 | **Service provider coordination** | Hotels, suppliers, logistics, operational ops | Haiku | Post-booking ops |
| 12 | **Problem resolution** | On-trip crisis, supplier failure, client emergency | Opus | Highest stakes |
| 13 | **Cold outreach** | No prior history, new market, proactive campaigns | Sonnet | Acquisition |

**Model routing logic:**
- **Haiku:** Mechanical, structured, known format — confirmations, supplier emails, handoffs (~€0.001)
- **Sonnet:** Relational, tone-sensitive, judgment required — proposals, inquiries, follow-ups (~€0.01)
- **Opus:** Crisis, strategic, high-stakes — disputes, emergencies, complex resolutions (~€0.05)

---

## n8n Workflow (The Backbone)

```
TRIGGER: New email arrives in sales@finland-dmc.com (Outlook node)
  │
  ▼
NODE 1 — Email Parser
  Extract: sender email, company domain, subject, body, thread_id
  │
  ▼
NODE 2 — Second Brain Lookup (Supabase node)
  Query clients + interactions tables by domain/email
  Returns: profile, history, staff owner, relationship signals, alerts
  │
  ▼
NODE 3 — Task Detector (Claude Haiku)
  Input: email body + client profile summary
  Output: {task_type, golden_prompt_id, model, confidence, alerts}
  Cost: ~€0.001 per email
  │
  ▼
NODE 4 — Golden Prompt + Context Assembly
  Load: prompts/{golden_prompt_id}.txt from n8n variables
  Inject: client profile + rate card + staff style template
  │
  ▼
NODE 5 — Draft Generator (Sonnet or Opus per task)
  Output: {email_body, itinerary_brief, pricing_block,
           upsell_suggestions, missing_items, reasoning}
  │
  ├── IF task = proposal AND TT API available ────────────────┐
  │                                                           ▼
  │                                              NODE 5a — TT API
  │                                                POST itinerary JSON
  │                                                Returns: TT URL
  │                                                Inject into draft
  │   ◄───────────────────────────────────────────────────────┘
  │
  ▼
NODE 6 — Draft Assembler
  Combine: email body + TT link + pricing block + upsell block
  Add: progress checklist + reasoning layer
  │
  ▼
NODE 7 — Human Review Interface
  Delivery: Web UI (Phase 3) or Teams message (Phase 2)
  Staff sees: full draft + context card + reasoning + progress
  Actions: [Approve] [Edit + feedback] [Regenerate] [Edit in TT]
  │
  ├── IF feedback provided ──────────────────────────────────┐
  │                                                          ▼
  │                                             NODE 7a — Feedback loop
  │                                               Sonnet rewrites with edit
  │                                               Max 3 iterations
  │   ◄──────────────────────────────────────────────────────┘
  │
  ▼
NODE 8 — Commit
  ├── Send email via M365 Graph API
  ├── Log interaction to Second Brain (Supabase insert)
  ├── Update TT booking status (if applicable)
  └── Record outcome for learning loop
```

**Cost per processed email:** €0.002–0.05 depending on task (Haiku detection + Sonnet/Opus draft).

---

## Second Brain Database Schema

```sql
clients (
  id, company_name, domain, country, market_segment,
  staff_owner, relationship_tier, last_contact,
  booking_count, total_revenue_eur, notes
)

contacts (
  id, client_id, name, email, role,
  language_preference, communication_style, is_decision_maker
)

interactions (
  id, client_id, contact_id, date, direction,
  task_type, outcome, proposal_value_eur, staff_member,
  email_id, thread_id, tt_url, conversion
)

components (                    ← populated from TT export + URL scraping
  id, name, category, destination, region,
  duration_hours, price_net_eur, commission_pct, has_commission,
  supplier_id, win_count, use_count,
  win_rate,                     ← calculated: win_count / use_count
  typical_day_position,         ← 1=Day 1, 2=Day 2 etc from sequence analysis
  removed_in_revision_rate,     ← how often clients ask to remove this
  added_in_revision_rate        ← how often clients ask to add this later
)

itineraries (                   ← scraped from TT links found in emails
  id, tt_itinerary_id, tt_url, version_number,
  email_id, thread_id, date_sent,
  client_id, staff_member, destination,
  duration_nights, pax_count, segment,
  outcome,                      ← confirmed / lost / pending
  component_list,               ← JSON array of component IDs
  raw_scraped_content           ← full scraped HTML for reanalysis
)

version_sequences (             ← tracks v1→v2→v3 evolution
  id, thread_id, version_number,
  itinerary_id, client_feedback_before,
  components_added, components_removed,
  final_confirmed               ← boolean
)

suppliers (
  id, name, category, location,
  contact_email, commission_model, notes, last_rate_update
)

rate_cards (
  id, supplier_id, service_name, season,
  price_net_eur, commission_pct, valid_from, valid_until,
  currency, conditions
)

golden_prompts (
  id, task_type, version, model_default,
  system_prompt, context_template,
  active, performance_score, last_updated
)
```

---

## TT URL Mining Pipeline

After mass email mining, extract and analyse all TT links ever sent:

```
STEP 1 — Extract all TT URLs from mined emails
  Regex: https://traveltree\.app/en/itinerary_view/\?itinerary_id=([a-f0-9]{32})
  Match to: email_id, thread_id, date, staff_sender, client_recipient

STEP 2 — Scrape all TT pages (Playwright — needed for JS rendering)
  Per URL: scrape Itinerary tab, Prices tab, Contacts tab
  Extract: days, components, activities, hotels, durations, pricing (if populated)
  Cost: negligible (own URLs, public pages)

STEP 3 — Build version sequences
  Group by thread_id + sort by date → identify v1→v2→v3 chains
  Cross-reference with client feedback emails between versions
  Map: "client said X → component Y was added/removed in next version"

STEP 4 — Label outcomes
  Cross-reference with confirmation emails → mark each thread:
  CONFIRMED / LOST / PENDING

STEP 5 — Calculate win rates + revision patterns
  Component win rate: confirmed bookings containing component / total uses
  Revision pattern: what changes between versions + direction
  Sequence pattern: typical day position for each component

OUTPUT — The recommendation engine's training data:
  Every confirmed itinerary Finland DMC has ever sent
  + the revision history showing how clients shaped it
  + the outcome (won or lost)
  This data does not exist in any commercial DMC tool
```

---

## UI Design Specification

### Concept: Finland DMC branding + VS Code controls

**Visual language:** Finland DMC website colours/fonts. Professional, not "AI chatbot."
**Controls:** VS Code-inspired — panels, split views, keyboard shortcuts, status bar at bottom. Familiar to power users, does not intimidate.

```
┌─ TOP BAR ──────────────────────────────────────────────────────────┐
│  [🌲 Finland DMC AI]   Staff: Laura ▾   [⊕ New task]   [⚙ Settings]│
└────────────────────────────────────────────────────────────────────┘
│                                                                      │
│ ┌─ LEFT SIDEBAR (Context) ──────┐  ┌─ MAIN PANEL (Draft) ──────────┐│
│ │                               │  │                                ││
│ │ CLIENT                        │  │ [Email draft — editable]       ││
│ │ Nordic Luxury                 │  │                                ││
│ │ Katerina · Iceland · Agency   │  │ ┌─ TT BLOCK ─────────────────┐ ││
│ │ ★★★★☆ Relationship            │  │ │ Paste TT link here:        │ ││
│ │                               │  │ │ [                        ] │ ││
│ │ HISTORY                       │  │ │ Auto-formats anchor text   │ ││
│ │ • Jan 2026: pricing delay     │  │ │ [Edit in TT ↗]             │ ││
│ │ • Dec 2025: Kuru proposal     │  │ └───────────────────────────┘ ││
│ │ • Sep 2025: first inquiry     │  │                                ││
│ │                               │  │ ┌─ PRICING BLOCK ────────────┐ ││
│ │ TASK DETECTED                 │  │ │ Kuru NET rates:            │ ││
│ │ ■ New inquiry                 │  │ │ Double: €304/night         │ ││
│ │   Agency B2B mode             │  │ │ SUP: €59.90/pp ✓ 15%      │ ││
│ │   Sonnet · 96% confidence     │  │ │ ⚠️ Solitary: 0% commission │ ││
│ │                               │  │ └───────────────────────────┘ ││
│ │ ALERTS                        │  │                                ││
│ │ ⚠️ Pricing delay history      │  │ ┌─ UPSELL BLOCK ─────────────┐ ││
│ │ ⚠️ Respond within 24h         │  │ │ Drag to add to email:      │ ││
│ │   (71% vs 29% conversion)     │  │ │ ★★★ Smoke Sauna [+]        │ ││
│ │                               │  │ │ ★★★ Seal Safari [+]        │ ││
│ │ ITINERARY SUGGESTIONS         │  │ │ ★★☆ E-fatbike   [+]        │ ││
│ │ ★★★★★ Smoke Sauna (5/5)      │  │ │ [why?] shown on hover      │ ││
│ │   → never removed             │  │ └───────────────────────────┘ ││
│ │ ★★★★★ Seal Safari  (5/5)     │  │                                ││
│ │ ★★★★☆ Solitary     (4/5)     │  │ Progress: ███████░░░ 70%       ││
│ │   → [why?]                    │  │ ❌ Missing: budget question    ││
│ └───────────────────────────────┘  │ ❌ Missing: activity level     ││
│                                    └────────────────────────────────┘│
│                                                                       │
│ ┌─ BOTTOM PANEL (Review + Commit) ─────────────────────────────────┐ │
│ │                                                                   │ │
│ │ Feedback: [Add your notes...                        ] [↺ Regen]  │ │
│ │                                                                   │ │
│ │ [← Edit inline]  [⇄ Change mode]  [📋 Copy]  [✈ Send]  [✓ Approve]│
│ └───────────────────────────────────────────────────────────────────┘ │
└─ STATUS BAR ──────────────────────────────────────────────────────────┘
  Task #02 · Sonnet · 847 tokens · 2nd Brain: 12 records found · v1.0
```

---

## Technology Stack

| Layer | Tool | Rationale |
|---|---|---|
| AI models | Claude API (Haiku/Sonnet/Opus) | Best quality, we know it, batch pricing |
| Workflow logic | n8n (self-hosted, small VPS ~€10/month) | No per-run cost, connects everything, Visual, versionable JSON |
| Frontend (Phase 2) | Retool | Fast to build internal tools, ~2 weeks |
| Frontend (Phase 3) | Next.js + Tailwind | Finland DMC branding, full control, ~6 weeks |
| Second Brain storage | Supabase (PostgreSQL + pgvector) | Free tier generous, vector search for similarity |
| Email sending | M365 Graph API | Already have, programmatic Outlook |
| Itinerary | Travel Tree Pro (€75/month) | Reliable, staff know it, API on Pro |
| TT scraping | Python + Playwright | Handles JS-rendered pages |
| Deployment | Hetzner VPS or Railway.app | Cheap, reliable, EU hosted (GDPR) |

---

## Pilot Plan: Liisa First

**Why Liisa:**
- Handles highest volume of accounts (Flash Pack, AHI, Fit4travel, Reset Holidays, Voyageurs du Monde)
- Manages allocation accounts (structured, repeatable — easiest AI assist)
- Confirmation emails and supplier coordination = Haiku tasks (low risk, high frequency)

**Phase A — Liisa only (weeks 1-4):**
- New system runs alongside old workflow
- Liisa uses staff UI for incoming emails — reviews AI drafts before sending
- Old workflow always available as fallback
- Track: time per task, satisfaction, error rate vs. old method

**Phase B — Expand to Laura (weeks 5-8):**
- Laura handles complex proposals — tests the Agency B2B mode deeply
- Nordic Luxury, St. Olaf type clients = real stress test of proposal drafting

**Phase C — Reeta + Sebastian (weeks 9-12):**
- Reeta: group operations, itinerary-only mode
- Sebastian: FIT direct, enthusiastic tone, draft itinerary mode

**Metrics to track:**
- Time from inquiry received → proposal sent (target: 30 min → 10 min)
- Revision rounds per proposal (target: 3 → 1-2)
- Commission exceptions missed (target: current rate → 0)
- Staff satisfaction score (simple 1-5 survey weekly)

---

## Build Sequence

### This Weekend: Claude Project MVP
- [ ] `Proposals_Itineraries_Custom_Instructions.txt` — golden prompt #01
- [ ] `Client_Communications_Custom_Instructions.txt` — golden prompts #02, #05, #08, #13
- [ ] `Pricing_Analysis_Custom_Instructions.txt` — pricing + commission rules
- [ ] `DMC_Router_Custom_Instructions.txt` — task detection + routing
- [ ] Contact TT: write API + component export + iframe embedding question

### After Azure Access (mass mining, ~$15-30)
- [ ] Export full sales@ mailbox via Graph API export script
- [ ] Haiku classification batch (~$1-2)
- [ ] Sonnet extraction batch (~$10-15)
- [ ] Extract all TT URLs from mined emails
- [ ] Scrape all TT pages via Playwright
- [ ] Build version sequence dataset
- [ ] Populate Supabase Second Brain database
- [ ] Request TT component export (1000+ components as JSON/CSV)

### Phase 2 Build (n8n + basic UI, 2-4 weeks)
- [ ] Deploy n8n on Hetzner VPS
- [ ] Build core n8n workflow (nodes 1-8)
- [ ] Connect Claude API, M365 API, Supabase
- [ ] Simple Retool frontend for Liisa pilot
- [ ] Run Liisa pilot — measure and iterate

### Phase 3 Build (full custom UI, 6-10 weeks)
- [ ] Next.js frontend — Finland DMC branding + VS Code controls
- [ ] Modular block system (TT, Pricing, Upsell, Reasoning blocks)
- [ ] TT API integration (write itineraries programmatically)
- [ ] Full M365 send integration
- [ ] Expand to Laura, Reeta, Sebastian

### Orchestrated Team Refinement (after 3+ months of data)
- Once the system has processed hundreds of real proposals and has outcome data
- Opus orchestrator + Sonnet analysis team audits golden prompt performance
- Identifies which prompts underperform, which patterns aren't being captured
- Upgrades prompts based on real usage patterns
- This is Session 7+ territory — not needed now, powerful when data-rich

---

## Portfolio Replication Map

Finland DMC is the pilot. Same architecture, different data + prompts:

| Company | AI Use Case | Key difference from Finland DMC |
|---|---|---|
| Finland DMC | DMC proposal + operations email automation | Pilot — this build |
| Järvisydän | Group sales + event offer automation | Different golden prompts, Järvisydän suppliers + rates |
| M/S Marival | Cruise group sales agent — potentially agentic | More autonomous (cruise bookings are structured) |
| Other 1658 companies | Per company needs | Same n8n backbone, new Second Brain data |

**Replication time per company:** ~2-3 weeks once the Finland DMC platform is stable. Most of the infrastructure (n8n, Supabase, Claude API connection) is reused. New work = new golden prompts + new mining session + new Second Brain data.

---

## Open Questions (Action Items)

| Question | Who | When |
|---|---|---|
| TT write API: can we POST an itinerary and get a URL back? | Patrick → TT | This week |
| TT component export: can we download 1000+ components as JSON/CSV? | Patrick → TT | This week |
| TT iframe embedding: does TT allow embedding their builder in our UI? | Patrick → TT | This week |
| TT pricing tab via API: can we write pricing fields programmatically? | Patrick → TT | This week |
| Azure AD app registration: admin approval from IT | Patrick → IT admin | Pending (sent) |
| Which VPS provider for n8n? | Patrick | When Phase 2 starts |

---

*Design document captures full conversation from session 32 (2026-02-20/21).*
*Next: build `Proposals_Itineraries_Custom_Instructions.txt` — the first golden prompt.*
