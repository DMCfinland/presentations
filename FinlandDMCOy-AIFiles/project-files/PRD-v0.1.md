# Finland DMC — AI Operations Platform: Product Requirements Document

**Version:** 0.1 (baseline — pre-Word-doc-digestion)
**Date:** 2026-02-21
**Status:** DRAFT. Will be updated to v0.2 after Word document analysis (400 pages).
**Author:** Patrick Heiskanen + Claude Sonnet (session 42)
**Sources read (all fully read before writing):**
- `EMAIL-DRAFTER-DESIGN.md` v3.0 (741 lines, session 37, 2026-02-20)
- `opus-m365-architecture-design.md` (1,886 lines, Opus, 2026-02-12)
- `opus-build-execution-plan.md` (1,144 lines, Opus, 2026-02-12)
- `opus-design-improvements-addendum.md` (1,049 lines, Opus, 2026-02-12)
- `opus-swot-and-build-optimization.md` (1,018 lines, Opus, 2026-02-12)
- Mining sessions 1–6 + Proposals Second Brain (session 38)
- CURRENT-STATUS.md session logs 1–41

---

## Version History

| Version | Date | Change |
|---------|------|--------|
| 0.1 | 2026-02-21 | Baseline from all existing design documents. Architecture unified. |
| 0.1.1 | 2026-02-21 | Opus review corrections: A5 flagged open, DPIA elevated to blocking, Phase 1 go/no-go criteria added, Design Decisions Log added |
| 0.2 | TBD | After 400-page Word document digestion |

---

## 1. Executive Summary

Finland DMC Oy is a 5-person B2B destination management company. ~600 emails/month. Every proposal written from scratch. No institutional memory. When Janna Kankkunen (Head of Sales) left in August 2024, her client relationships — €633K+ in managed accounts — became orphaned with zero handover.

**The system being built** is two interlocking components sharing one backoffice:

| Component | What it does |
|-----------|-------------|
| **Second Brain** | Captures every client interaction via Teams, classifies it, stores structured intelligence, surfaces it automatically as daily digests, meeting prep briefs, and weekly reviews |
| **Email Drafter** | Generates complete email responses and proposals from that intelligence — staff paste an email, AI drafts the reply using real historical data about that client |

These are different products for different moments in the workflow. The Second Brain builds the knowledge base. The Email Drafter uses it. They share the same infrastructure so there is one thing to build, maintain, and replicate.

**Pilot:** Finland DMC is the test bed. Same platform, different data and prompts, deploys to Järvisydän, M/S Marival, and other 1658 Holdings companies.

**Current state:** Both systems fully designed. Neither built. Most immediate path: 5 Custom Instruction files for Claude Project (validates golden prompts this week, no infrastructure needed).

---

## 2. Problem Statement

### 2.1 The Business Problems Being Solved

| Problem | Evidence | Cost |
|---------|----------|------|
| No institutional memory | Janna left → Flash Pack (€558K), Delta Tour (€75K), Journey D.LUXE (€11K) orphaned, no handover | €633K+ at risk |
| Proposals written from scratch | Every inquiry = 60–120 min research + writing | Capacity bottleneck |
| Commission exceptions not enforced | Solitary restaurant = 0% commission, informal knowledge only | Revenue leakage |
| Response time window ignored | <24h = 71% conversion. >24h = 29%. No tracking. | Unknown leakage |
| Revenue concentration | AHI Travel = 75% of total revenue | Single-point failure |
| Missing key client | Wikinger Reisen (€317K) absent from email mining | Unknown relationship status |

### 2.2 The Staff This Serves

| Name | Role | Communication style | Key accounts |
|------|------|--------------------|-|
| Liisa Vihermaa | Product & Sales Manager | Structured, operational | Flash Pack, AHI, Fit4travel, Reset Holidays, Voyageurs |
| Laura Ilvonen | Group ops + Iceland FIT | Formal, thorough | Nordic Luxury, St. Olaf, AABEI |
| Reeta Vihavainen | Program ops + repeat accounts | Concise, operational | Repeat accounts, group ops |
| Sebastian Heiskanen | FIT/boutique | Enthusiastic, warm | Direct FIT, luxury |
| Piia Laitila | Product & Sales Manager | TBD | TBD |

---

## 3. Product Vision

**"An AI system that knows Finland DMC's clients, voice, and pricing better than any single staff member — and does the first draft of everything."**

### 3.1 Operating Principles

**Full automation with human approval, not half-automation.**
```
Old:              Staff constructs → staff checks → staff sends
Half-automation:  AI drafts → staff reconstructs mentally → staff sends
Full automation:  AI constructs → staff approves → system sends
```
Staff time freed entirely for the human layer: building trust, handling on-trip problems, cold acquisition.

**One behavior per component.** Second Brain: type in Teams. Email Drafter: paste email in UI. If the system requires more than one behavior, it's not a system — it's a self-improvement program.

**Run alongside the old workflow.** Always additive. Old way is always available as fallback.

**Trust through transparency.** Every AI suggestion shows WHY, sourced from Finland DMC's own data — not generic benchmarks.

**One platform, multiple companies.** Finland DMC is pilot. Same shared backoffice → Järvisydän → M/S Marival → all 1658 companies.

---

## 4. Architecture: Two Systems, One Backoffice

The two systems are different products but share the same infrastructure layer. This PRD **recommends** a unified shared backoffice. **Architecture Decision A5 (see Section 11) is still open:** the Second Brain Opus design documents used M365-native Power Automate throughout; this PRD proposes migrating to n8n for a unified backbone. That decision has not been validated against the 400-page Word documents and requires Patrick's explicit sign-off before Phase 1 begins.

*Opus review note (2026-02-21): The original v0.1 presented this as "already resolved." That was incorrect. The 4 Opus source documents (Feb 12) designed the Second Brain entirely on Power Automate + SharePoint + Azure OpenAI. The Email Drafter (Feb 20) designed on n8n + Supabase + Claude. Merging them onto one backbone is a valid approach but is a new architectural decision, not a synthesis of existing decisions.*

```
╔══════════════════════════════════════════════════════════════════╗
║  PRODUCT LAYER (user-facing, different per product)              ║
║                                                                  ║
║  ┌─────────────────────────┐   ┌──────────────────────────────┐  ║
║  │   SECOND BRAIN          │   │   EMAIL DRAFTER              │  ║
║  │   Teams #dmc-brain      │   │   Web UI (Retool → Next.js)  │  ║
║  │   capture + digests     │   │   draft + review + send      │  ║
║  └─────────────────────────┘   └──────────────────────────────┘  ║
╠══════════════════════════════════════════════════════════════════╣
║  SHARED BACKOFFICE LAYER (one thing to build, maintain, replicate)║
║                                                                  ║
║  Automation:     n8n (self-hosted, Hetzner VPS)                  ║
║  Intelligence DB: Supabase (PostgreSQL + pgvector)               ║
║  CRM Capture:    SharePoint Lists (M365-native, Teams-linked)    ║
║  Proposal AI:    Claude API (Haiku / Sonnet / Opus)              ║
║  CRM AI:         Azure OpenAI GPT-4o (EU-only, GDPR)            ║
║  Email:          M365 Graph API                                  ║
║  Hosting:        Hetzner VPS (EU, ~€20/month for both systems)   ║
╚══════════════════════════════════════════════════════════════════╝
```

### 4.1 Why This Stack

**n8n as unified automation backbone:**
Both systems need workflow orchestration. n8n runs on Hetzner (EU-hosted), connects to SharePoint, Supabase, Claude API, Azure OpenAI, M365 Graph API, and Travel Tree — all from one place. No per-run cost. One VPS. One tool to learn and maintain. Power Automate stays for Teams-native triggers (where it is genuinely better), but n8n handles everything beyond capture routing.

**Supabase as the shared intelligence database:**
The Email Drafter needs pgvector (semantic similarity for client matching), proper relational tables (version sequences, component win rates), and n8n-native integration. SharePoint Lists handle the CRM capture well but are too limited for the proposal intelligence data. Supabase gives both systems one place to query client profiles, component win rates, pricing, and interaction history. Free tier is generous. EU servers available. The Second Brain's SharePoint Lists sync key data to Supabase so the Email Drafter can access it.

**Split AI model strategy (intentional, not a compromise):**
- **Azure OpenAI GPT-4o (Sweden Central):** Processes raw client PII in the Second Brain capture flow. GDPR requires EU data residency for this data. Microsoft DPA + Data Zone Standard EUR = legally defensible.
- **Claude API (Haiku/Sonnet/Opus):** Handles all drafting, proposal generation, golden prompts, and task detection in the Email Drafter. Superior quality for nuanced communication. No EU residency needed here — prompts contain task context, not raw contact data.

**SharePoint Lists + Teams as capture interface:**
Staff live in Teams. The Second Brain's #dmc-brain channel is the zero-friction capture point. SharePoint Lists store the structured CRM data and feed back to Teams through Adaptive Card confirmations and digests. This stays M365-native and requires no new tool adoption.

---

## 5. Component 1: Second Brain (CRM Intelligence)

### 5.1 What It Does

```
CAPTURE  → Staff types anything in Teams #dmc-brain
           "Called Mika at Arctic Travel. Northern Lights. Follow up Friday."
           [10–15 seconds]

CLASSIFY → n8n trigger → Azure OpenAI GPT-4o (Sweden Central, GDPR)
           Extracts: client, contact, sentiment, opportunities, next actions
           Confidence score 0.0–1.0. Below 0.6 → human review.

STORE    → SharePoint Lists (structured CRM data)
           → Sync key data to Supabase (for Email Drafter queries)

SURFACE  → Daily digest 06:45 weekdays (personalized per staff)
           → Meeting prep: "prep: Arctic Travel" → brief in 30 seconds
           → Weekly review: Sunday 17:00 — patterns, wins, sentiment
           → Client A4 pages: Top 10 weekly, others on-demand
```

### 5.2 The 8 SharePoint Lists

| List | Purpose |
|------|---------|
| Clients | Master record — every company Finland DMC serves |
| Contacts | People at those companies, decision makers, preferences |
| Interactions | Every captured touchpoint — the raw data powering everything |
| Growth Roadmaps | Strategic plans for key clients |
| Team Feedback | Staff sentiment, ideas, challenges (anonymous option via bot DM) |
| Weekly Wins | Celebrations, progress tracking |
| Inbox Log | Full audit trail — every capture logged (GDPR Article 30) |
| Prompt Versions | Version control for AI classification prompts |

### 5.3 Key Design Decisions

**One behavior.** Type in #dmc-brain, press Enter. Everything else is automated. No forms, no tags, no routing decisions by staff.

**Two capture channels:**
- `#dmc-brain` (team channel, visible to all) — client interactions, wins, growth ideas
- Bot DM (private) — team feedback, personal concerns. No [anon] prefix needed.

**Confidence threshold 0.6.** Uncertain classifications → Patrick's review queue, not guessed. Builds trust.

**Correction mechanism.** Reply "fix: [correction]" in thread. 10 seconds. Updates record, logs in audit trail. "Fix" button on Adaptive Card (no typing needed).

**Surfacing is the value.** The system is only as good as what it pushes to staff. Push, don't pull.

### 5.4 Proactive Surfacing

**Daily digest (06:45, Mon–Fri):**
- Today's follow-up actions (personalized per staff member)
- At-risk client signals (declining relationship health)
- Opportunities from this week's interactions
- Max 120 words. Strictly under 150. Readable in 2 minutes on a phone.

**Meeting prep (on-demand):**
- Type "prep: [client name]" in #dmc-brain
- Within 30 seconds: key people, last 3 interactions, what matters to them, open items, relationship score
- Delivered as Teams DM

**Weekly review (Sunday 17:00):**
- Week's numbers, client patterns (from 2+ clients), top 3 actions for next week, team sentiment (aggregate only, never individual), wins

**Client A4 pages:**
- Auto-generated weekly for Top 10 clients
- On-demand for others ("page: [client name]")
- Contains: company profile, 12-month relationship history, patterns, buying signals, seasonal rhythms, growth roadmap, next actions

### 5.5 Relationship Health Score (calculated weekly)

Weighted formula, 1–10 scale:
- Interaction frequency vs. expected cadence (30%)
- Sentiment trend over last 6 months (25%)
- Open opportunity pipeline (20%)
- Response time to proposals (15%)
- Days since last contact (10%)

---

## 6. Component 2: Email Drafter (Proposal Automation)

### 6.1 What It Does

```
INPUT    → Staff pastes incoming email into web UI
           [or system triggers from incoming sales@finland-dmc.com]

STEP 1   → Second Brain Lookup (Haiku, ~€0.001)
           Queries Supabase for client profile, history, alerts, staff owner
           Returns: "Nordic Luxury · Katerina Eremeeva · pricing delay history"

STEP 2   → Task Detection (Haiku, automatic)
           Task: NEW INQUIRY — Agency B2B
           Golden prompt: #02 — Agency inquiry response
           Model: Sonnet. Confidence: 96%.
           Alert: ⚠️ Pricing delay history — respond within 24h

STEP 3   → Draft Generation (Sonnet or Opus per task)
           Output: email body + TT block + pricing block + upsell suggestions
           + WHY each component was suggested (own-data proof)
           + Progress bar showing what's missing

STEP 4   → Human Review + Edit Loop (max 3 iterations)
           Staff: approve / edit inline / add feedback + regenerate

STEP 5   → Commit
           Copy to Outlook (always available)
           OR Send via M365 Graph API
           → Second Brain auto-updated with interaction logged
```

### 6.2 The 13 Golden Prompts

Auto-selected by task detection. Staff never chooses.

| # | Task | Trigger signals | Model | Cost |
|---|------|-----------------|-------|------|
| 01 | Draft proposal | TT link, itinerary request | Sonnet | €0.01 |
| 02 | Reply to new inquiry | First contact, no prior history | Sonnet | €0.01 |
| 03 | Send revision | "changes", "update", "version 2" | Sonnet | €0.01 |
| 04 | Confirm booking | "confirmed", deposit received | Haiku | €0.001 |
| 05 | Chase pending proposal | No reply 5+ days after proposal | Sonnet | €0.01 |
| 06 | Handle complaint/dispute | "problem", on-trip crisis | **Opus** | €0.05 |
| 07 | Supplier outreach | Known supplier, rate/availability request | Haiku | €0.001 |
| 08 | Re-engage warm lead | 30–90 days since contact | Sonnet | €0.01 |
| 09 | Internal brief handoff | Staff-to-staff, "brief for" | Haiku | €0.001 |
| 10 | Allocation management | Repeat operator, departure series | Sonnet | €0.01 |
| 11 | Service provider coordination | Hotels, logistics, post-booking ops | Haiku | €0.001 |
| 12 | Problem resolution | On-trip crisis, supplier failure | **Opus** | €0.05 |
| 13 | Cold outreach | No prior history, proactive campaigns | Sonnet | €0.01 |

**Cost per processed email:** €0.002–0.05 depending on task type.

### 6.3 4-Layer Product Roadmap

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 4 — FUTURE: Multi-Source Agent Teams Synthesis
  When: proposals + emails + TT all loaded simultaneously + context exceeded
  Agent A (proposals) + Agent B (emails) + Agent C (TT) → debate → unified profile
  Timeline: Month 6+. Prerequisite: 3+ months of real usage data.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 3 — FUTURE: Full Itinerary Automation
  AI generates complete itinerary → n8n calls TT write API → URL auto-generated
  Prerequisite: TT write API confirmed (awaiting response)
  Timeline: Month 4–6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 2 — NEXT: Component Recommender
  Top 8 components from 1000+ library, ranked by win rates for this client profile
  Prerequisite: TT component export + mass email mining complete
  Timeline: Month 2–3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LAYER 1 — NOW: Email Drafter
  Paste email → auto-detect → draft → review → send
  Prerequisite: Sessions 1–6 data (READY)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOUNDATION: Second Brain
  Client profiles, win rates, pricing, staff styles, TT archive

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.4 Travel Tree Integration (3 Stages)

| Stage | Status | What | Friction |
|-------|--------|------|----------|
| Stage 1: Deep Link | **Build now** | Staff builds TT → pastes URL → email wrapper auto-generated | One tab switch |
| Stage 2: Programmatic | After TT API confirmed | n8n calls TT write API → URL in draft automatically | Zero |
| Stage 3: Embedded/Component | Full vision | TT iframe embedded in UI or component editor → auto-push | Zero |

**Status:** Email sent to TT asking about write API + component export + iframe policy. Awaiting reply.

### 6.5 TT URL Mining Pipeline (builds component win rates)

```
1. Extract all TT URLs from mined emails (regex)
2. Playwright scrapes all TT pages (JS-rendered)
3. Group by thread_id → build version sequences (v1→v2→v3)
4. Cross-reference with confirmation emails → label outcomes
5. Calculate: component win rate, typical day position,
   removed-in-revision rate, added-in-revision rate
```

This dataset — every confirmed itinerary DMC has ever sent with revision history and outcome — does not exist in any commercial DMC tool. It's the recommendation engine's core.

### 6.6 UI Design

**Concept:** Finland DMC branding + VS Code-inspired controls (panels, split views, keyboard shortcuts, status bar). Professional, not "AI chatbot."

```
┌─ TOP BAR ────────────────────────────────────────────────────────┐
│  [🌲 Finland DMC AI]   Staff: Laura ▾   [⊕ New task]   [⚙]      │
└──────────────────────────────────────────────────────────────────┘
│ ┌─ LEFT SIDEBAR ──────────────┐  ┌─ MAIN PANEL ─────────────────┐│
│ │ CLIENT                       │  │ [Email draft — editable]     ││
│ │ Nordic Luxury                │  │                              ││
│ │ Katerina · Iceland · Agency  │  │ ┌─ TT BLOCK ───────────────┐ ││
│ │                              │  │ │ Paste TT link here       │ ││
│ │ HISTORY                      │  │ │ [Edit in TT ↗]           │ ││
│ │ • Jan 2026: pricing delay    │  │ └─────────────────────────┘ ││
│ │ • Dec 2025: Kuru proposal    │  │                              ││
│ │                              │  │ ┌─ PRICING BLOCK ──────────┐ ││
│ │ TASK DETECTED                │  │ │ Kuru NET: €304/night     │ ││
│ │ ■ New inquiry · Agency B2B   │  │ │ SUP: €59.90 ✓ 15%       │ ││
│ │   Sonnet · 96% confidence    │  │ │ ⚠️ Solitary: 0% commission│ ││
│ │                              │  │ └─────────────────────────┘ ││
│ │ ALERTS                       │  │                              ││
│ │ ⚠️ Pricing delay history     │  │ Progress: ███████░░░ 70%     ││
│ │ ⚠️ Respond within 24h        │  │ ❌ Missing: budget question  ││
│ │   (71% vs 29% conversion)    │  │ ❌ Missing: activity level   ││
│ └─────────────────────────────┘  └──────────────────────────────┘│
│ ┌─ BOTTOM PANEL ───────────────────────────────────────────────┐  │
│ │ Feedback: [Add notes...      ] [↺ Regen]                     │  │
│ │ [← Edit]  [⇄ Mode]  [📋 Copy]  [✈ Send]  [✓ Approve]        │  │
│ └──────────────────────────────────────────────────────────────┘  │
└─ STATUS BAR ─────────────────────────────────────────────────────┘
  Task #02 · Sonnet · 847 tokens · 2nd Brain: 12 records found · v1
```

### 6.7 Psychology Levers (embedded throughout both systems)

| Lever | How applied |
|-------|-------------|
| **Push, don't pull** | Context card appears before staff reads email. Second Brain lookup fires automatically. No "search" button. |
| **Curate, don't dump** | 1000+ components → top 8 based on win rates for this profile. 3-year history → 5 most relevant signals. |
| **Progress signals** | Checklist shows exactly what's missing in every draft. Post-send window timer visible. |
| **Own-data proof** | "Smoke Sauna confirmed in 5/5 of your Kuru Resort FIT bookings" — not generic industry stats. |
| **Voice matching** | Opening/closing phrases pulled verbatim from each staff member's confirmed emails. |
| **Trusted colleague** | "💡 Solitary dinner has no commission — worth flagging to Katerina" (not ⚠️ WARNING). |
| **Staff control** | AI proposes. Staff approves. Commit is always human. Never sends without explicit approval. |

---

## 7. Shared Intelligence Database (Supabase)

Both systems read from and write to the same Supabase instance. This is what makes them a platform, not two separate tools.

### 7.1 Core Schema

```sql
-- Shared by both systems
clients (
  id, company_name, domain, country, market_segment,
  staff_owner, relationship_tier, last_contact,
  booking_count, total_revenue_eur, notes,
  relationship_health_score, health_trend     -- updated by Second Brain weekly
)

contacts (
  id, client_id, name, email, role,
  language_preference, communication_style, is_decision_maker,
  last_interaction_date, interaction_count
)

interactions (
  id, client_id, contact_id, date, direction, type,
  summary, sentiment, opportunities, next_actions, next_action_date,
  task_type, outcome, proposal_value_eur, staff_member,
  email_id, thread_id, tt_url, conversion,
  raw_capture, confidence_score, source   -- "teams_capture" | "email_mining" | "manual"
)

-- Email Drafter-specific
components (
  id, name, category, destination, region,
  duration_hours, price_net_eur, commission_pct, has_commission,
  supplier_id, win_count, use_count, win_rate,
  typical_day_position, removed_in_revision_rate, added_in_revision_rate
)

itineraries (
  id, tt_itinerary_id, tt_url, version_number,
  email_id, thread_id, date_sent, client_id, staff_member,
  destination, duration_nights, pax_count, segment,
  outcome, component_list, raw_scraped_content
)

version_sequences (
  id, thread_id, version_number, itinerary_id,
  client_feedback_before, components_added, components_removed,
  final_confirmed
)

suppliers, rate_cards, golden_prompts, staff_profiles
```

### 7.2 SharePoint → Supabase Sync

The Second Brain captures in SharePoint Lists (for M365/Teams native integration). Key data syncs to Supabase so the Email Drafter can query it without touching SharePoint directly.

Sync flow (n8n, triggered on SharePoint change):
- New client interaction in SharePoint → syncs to Supabase `interactions`
- Updated client health score → syncs to Supabase `clients`
- New contact created → syncs to Supabase `contacts`

This keeps Teams-side CRM capture in its natural M365 home while giving the Email Drafter fast relational + vector queries against the same data.

### 7.3 Current Data Assets (ready to load into Supabase)

| Asset | Size | Status |
|-------|------|--------|
| 107 client profiles | 87KB (`client-profiles.yaml`) | ✅ Ready |
| Revenue intelligence | 20KB (`revenue-intelligence.yaml`) | ✅ Ready |
| Staff account map | 13KB (`staff-account-map.yaml`) | ✅ Ready |
| Second Brain gap report | 30KB (orphaned accounts, alerts) | ✅ Ready |
| Session 5 pricing data | Rate cards, 13 suppliers, 30 rates | ✅ Ready |
| Component win rates | From TT URL scraping | ⏳ Needs Azure AD + TT scraper |
| Full interaction history | 3+ years of sales@ emails | ⏳ Needs Azure AD Graph API |
| TT itinerary archive | All past proposals + version sequences | ⏳ Needs mass mining + TT scraper |

### 7.4 Priority Actions (revenue at risk now)

| Account | Issue | Revenue | Action |
|---------|-------|---------|--------|
| Flash Pack | Orphaned Aug 2024 (Janna) | €558K | Assign to Liisa → reintroduction email |
| Delta Tour | Orphaned Aug 2024 | €75K | Assign to Reeta → reintroduction email |
| Journey D.LUXE | Orphaned Aug 2024 | €11K | Assign |
| Wikinger Reisen | Missing from email mining entirely | €317K | Investigate before assigning |
| AHI Travel | 75% revenue concentration | €4.4M | Active diversification plan needed |

---

## 8. n8n Workflow (Shared Backbone)

Both systems run on the same n8n instance. Flows are logically separated by namespace but share connectors and environment.

### 8.1 Second Brain Flows

```
[SECOND BRAIN FLOWS]

Flow 1: Classify & Route
  Trigger: New message in Teams #dmc-brain
  → Parse text → Azure OpenAI classify → confidence check
  → Route to SharePoint list → sync to Supabase → Adaptive Card reply in thread

Flow 2: Fix Handler
  Trigger: Reply in #dmc-brain containing "fix:" or "korjaa:"
  → Re-classify with correction → update record → log correction

Flow 3: Meeting Prep
  Trigger: "prep: [client]" in #dmc-brain
  → Query Supabase for client data → Claude generates brief → DM to requester

Flow 4: Daily Digest
  Schedule: 06:45 weekdays (Mon–Fri)
  → Query Supabase per staff member → Claude generates personalized digest
  → Teams DM with Adaptive Card (Mark Done + Snooze buttons)

Flow 5: Weekly Review
  Schedule: Sunday 17:00
  → Aggregate week's data → Claude generates review → Teams DM to all staff

Flow 6: A4 Page Generator
  Trigger: "page: [client]" OR weekly schedule for Top 10
  → Query full client history from Supabase → Claude generates A4 → DM as PDF

Flow 7: Health Check
  Schedule: 07:00 daily
  → Verify digest ran successfully → alert Patrick if not

Flow 8: SharePoint → Supabase Sync
  Trigger: SharePoint list item created/modified
  → Write to Supabase (interactions, clients, contacts tables)
```

### 8.2 Email Drafter Flows

```
[EMAIL DRAFTER FLOWS]

Flow 1: Email Parser
  Trigger: Staff pastes email into web UI (HTTP webhook from Retool/Next.js)
    OR: New incoming email in sales@finland-dmc.com (Outlook trigger, Phase 2)
  → Extract: sender, domain, subject, body, thread_id

Flow 2: Second Brain Lookup
  → Query Supabase: clients + contacts + interactions by domain/email
  → Return: profile, history, staff owner, alerts

Flow 3: Task Detector
  → Claude Haiku: classify email → {task_type, golden_prompt_id, model, confidence}
  → Cost: ~€0.001

Flow 4: Context Assembly
  → Load golden_prompts from Supabase
  → Inject: client profile + rate card + staff style template + relevant history

Flow 5: Draft Generator
  → Claude Sonnet or Opus (per task_type)
  → Output: email body + itinerary_brief + pricing_block + upsell + missing_items + reasoning
  IF proposal AND TT API available → call TT API → inject URL

Flow 6: Human Review Loop
  → Deliver draft to web UI via webhook response
  → Staff actions: approve / edit+feedback / regenerate / change mode / edit in TT
  → IF feedback: Claude rewrites (max 3 iterations)

Flow 7: Commit
  → Send via M365 Graph API OR return copy-ready text
  → Log interaction to Supabase
  → Update TT booking status (if applicable)
  → Record outcome for learning loop
```

---

## 9. Build Phases

### Phase 0 (NOW, no infrastructure needed): Claude Project MVP

Validate golden prompts using claude.ai. Staff use a Claude Project with the custom instruction files. This is the fastest path to delivering value.

**5 Custom Instruction files to build this week:**

| File | Content | Source data |
|------|---------|-------------|
| `Proposals_Itineraries_Custom_Instructions.txt` | Golden prompt #01 — full proposal drafting | Sessions 1–6 + proposals Second Brain |
| `Client_Communications_Custom_Instructions.txt` | Golden prompts #02, #05, #08, #13 | Sessions 1–3 |
| `Pricing_Analysis_Custom_Instructions.txt` | Commission rules, rate cards, exceptions | Session 5 |
| `DMC_Router_Custom_Instructions.txt` | Task detection + routing logic | Session 3 |
| `Staff_Profiles_Custom_Instructions.txt` | 4 staff modes: Laura / Reeta / Liisa / Sebastian | Sessions 1–3 |

**Also this week: Janna orphaned account emails**
- Flash Pack → from Liisa Vihermaa
- Delta Tour → from Reeta Vihavainen
- Journey D.LUXE → TBD

**Acceptance criteria:** Staff drafts 5 different email types in correct voice with correct pricing within 2 minutes of pasting an incoming email.

---

### Phase 1 (Weeks 1–4): Second Brain Foundation (Patrick-only pilot)

Infrastructure built. Patrick captures daily for 4 weeks alone. Validates before staff onboarding.

**6 increments, each with validation gate:**

| Increment | Scope | Hours | Model |
|-----------|-------|-------|-------|
| 1. Foundation | Azure + SharePoint + Supabase + Hetzner VPS + #dmc-brain | 3–4h | Sonnet |
| 2. Classification Flow | n8n trigger + Azure OpenAI classify + SharePoint route + Supabase sync | 4–5h | **Opus** |
| 3. Correction Flow | Fix handler | 2–3h | Sonnet |
| 4. Daily Digest | 06:45 scheduled, personalized, Adaptive Card | 3–4h | Split |
| 5. Meeting Prep | "prep:" trigger, 30-second brief | 2–3h | Sonnet |
| 6. Weekly Review + Integration test | Full end-to-end | 4–5h | Opus |

**Phase 1 prerequisites (not yet complete):**
- [ ] Azure OpenAI tenant access confirmed
- [ ] Power Automate Premium license OR n8n Teams connector tested
- [ ] Hetzner VPS provisioned
- [ ] Supabase project created

**Phase 1 go/no-go (Week 4):** All 6 must be "yes" before staff onboarding:

| # | Question | Target |
|---|----------|--------|
| G1 | Have I captured on >80% of working days in the last 2 weeks? | >80% |
| G2 | Is classification accuracy >85%? (inferred from correction rate <15%) | >85% |
| G3 | Would I miss the system if it stopped working tomorrow? | Yes |
| G4 | Am I actively reading the daily digest? | >55% of days |
| G5 | Has the weekly review surfaced at least one insight I didn't already know? | Yes |
| G6 | Is the fix rate below 5% of captures? (system classifying well, not guessing) | <5% |

---

### Phase 2 (Weeks 2–4, parallel with Phase 1): Email Drafter Layer 1

n8n email drafter flow + Retool frontend. Liisa Vihermaa pilot (highest volume, operations-heavy).

**Prerequisites:** Supabase populated with existing Second Brain data, Hetzner VPS from Phase 1.

**Acceptance criteria:** Liisa processes 5 consecutive real emails with AI drafts. Time from paste to send ≤ 10 minutes (vs. current ~60 min).

---

### Phase 3 (Weeks 5–10): Mass Mining + Component Recommender

Full email export via Graph API → Haiku classification (~$1–2) → Sonnet extraction (~$10–15) → TT URL scraping → component win rates calculated → Layer 2 (Component Recommender) built.

**Prerequisites:** Azure AD app registration approved (email sent, pending).

---

### Phase 4 (Weeks 8–12): Full Custom UI + TT API Integration

Next.js frontend with Finland DMC branding. TT write API integration (if confirmed). Expand to all 5 staff.

---

### Phase 5 (Month 4–6): Full Itinerary Automation

Layer 3: AI generates full itinerary → n8n pushes to TT via API. Opus orchestrated prompt review after 3+ months of real usage data.

---

### Phase 6 (Month 6+): Multi-Source Agent Teams

Layer 4: When all 3 data sources (proposals + emails + TT) are loaded and context limits are exceeded — Agent Teams orchestration for cross-source synthesis.

---

### Phase 7 (Ongoing): Portfolio Replication

Järvisydän → M/S Marival → other 1658 companies. ~2–3 weeks per company. New data, same backoffice.

---

## 10. Cost Model

### Shared Backoffice Infrastructure

| Component | Monthly | Notes |
|-----------|---------|-------|
| Hetzner VPS (shared) | €10–20 | Runs n8n + Playwright scraper for both systems |
| Supabase (shared) | €0–25 | Free tier generous; Pro if data grows |
| Azure OpenAI GPT-4o | €9 | Second Brain classification only (~600 captures/month) |
| Power Automate Premium (1 license) | €15 | Teams trigger for Second Brain capture. **Contingent on A5:** if n8n Teams connector replaces PA, this drops to €0. If M365-native (Opus docs) approach chosen, PA Premium is required. |
| Travel Tree Pro | €75 | Itinerary tool (existing, staff already use) |
| **Total shared backoffice** | **€109–144/month** | |

### Per-Use Costs (Claude API)

| Use | Cost per event | Monthly est. (600 emails) |
|-----|----------------|--------------------------|
| Task detection (Haiku) | €0.001 | €0.60 |
| Standard drafts (Sonnet) | €0.01 | €6 |
| High-stakes (Opus) | €0.05 | Occasional |
| Daily digests (5 staff, 20 days) | €0.01 each | €1 |
| Meeting prep (2/day avg) | €0.01 each | €0.40 |
| **Total Claude API** | | **~€10–15/month** |

**Total monthly (both systems running):** ~€120–160/month
**First year total:** ~€1,440–1,920 including setup
**Break-even:** Preventing 1 lost Flash Pack follow-up covers 3+ years of costs

---

## 11. Open Questions (Decision Log)

### Technical (blocking specific phases)

| # | Question | Owner | Status | Blocks |
|---|----------|-------|--------|--------|
| T1 | TT write API: can we POST an itinerary and get a URL? | Patrick → TT | Awaiting | Layer 2/3 |
| T2 | TT component export: JSON/CSV of 1000+ components? | Patrick → TT | Awaiting | Layer 2 |
| T3 | TT iframe policy? | Patrick → TT | Awaiting | Stage 3 UI |
| T4 | Azure AD app registration approved? | Patrick → IT admin | Email sent, pending | Mass mining |
| T5 | Azure OpenAI tenant access? (may need separate application) | Patrick | Not checked | Phase 1 |
| T6 | n8n Teams connector: can it trigger on new channel messages? | Patrick to test | Not tested | Phase 1 (alternative to Power Automate) |
| **T7** | **DPIA (Data Protection Impact Assessment, GDPR Article 35): automated profiling of clients/contacts triggers mandatory DPIA before go-live. Not optional — legally required for any system doing systematic automated evaluation of personal data.** | Patrick + legal counsel | Not started | **Go-live gate — all phases. Must be completed before staff onboarding.** |

### Architecture Decisions — Resolved (Patrick-approved or uncontested in source docs)

| # | Decision | Resolution |
|---|----------|------------|
| A2 | Claude vs Azure OpenAI as unified AI? | **Split by data sensitivity:** Azure OpenAI for CRM PII (GDPR), Claude for all drafting. Consistent across all source docs. |
| A4 | One integrated product vs two separate tools? | **Two products, one backoffice.** Different UIs, shared infrastructure. Consistent with Patrick's clarification 2026-02-21. |

### Architecture Decisions — OPEN (require Patrick decision before Phase 1)

| # | Question | Option 1 | Option 2 | Blocks |
|---|----------|----------|----------|--------|
| A1 | Primary intelligence DB? | **Supabase** — pgvector, relational, n8n-native. Requires SharePoint→Supabase sync layer. | **SharePoint Lists only** — M365-native, Teams-linked, already designed in Opus docs. No sync layer needed. | Phase 1 infrastructure |
| A3 | Automation backbone? | **n8n** (self-hosted, Hetzner, free) — one tool for both systems, no PA Premium license. Teams connector capability unverified. | **Power Automate** (€15/month, M365-native) — 7+ flows already fully designed in Opus docs. Teams triggers native. | Phase 1 infrastructure |
| **A5** | **Second Brain infrastructure: M365-native or unified with Email Drafter?** | **M365-native (Opus docs):** Power Automate + SharePoint Lists + Azure OpenAI. 4 detailed design documents, 7 PA flows, 8 SharePoint list schemas. GDPR-certified path. | **Unified n8n/Supabase (this PRD's recommendation):** One backbone for both systems. Less proven for Second Brain. Email Drafter already on this stack. | Phase 1 — this is the highest-impact decision in the document |

**Note on A5:** The 4 Opus documents represent ~5,000 lines of detailed M365-native design. The unified approach in this PRD is a new recommendation, not validated by that prior work. Migrating Second Brain to n8n saves €15/month PA Premium but requires rebuilding 7 designed PA flows and validating n8n Teams connector functionality (T6 above). The 400-page Word documents may contain Patrick's intent on this.

---

## 12. Success Metrics

### Email Drafter (operational)

| Metric | Current | Phase 2 Target | Phase 4 Target |
|--------|---------|----------------|----------------|
| Time: inquiry → proposal sent | 60–120 min | 30 min | 10 min |
| Revision rounds per proposal | 3+ | 2 | 1–2 |
| Commission exceptions missed | Frequent | Tracked | 0 |
| Response time <24h rate | Unknown | Tracked | >90% |

### Second Brain (adoption)

| Metric | 3-Month Target | 6-Month Target |
|--------|---------------|----------------|
| Staff capture rate | >70% of staff, 3+ days/week | >85%, 4+ days/week |
| Classification accuracy | >85% | >92% |
| Daily digest read rate | >55% | >60% |
| Meeting prep usage | >10 requests/month | >20/month |
| Patrick captures daily (Phase 0) | >80% of working days | — |

### Business outcomes

| Metric | Target |
|--------|--------|
| Orphaned accounts re-engaged | Flash Pack, Delta Tour, Journey D.LUXE within 30 days |
| Proposals/month | +50% without new hire (after Phase 2) |
| AHI concentration | Reduced from 75% to <60% (12-month target) |

---

## 13. Risks

| Risk | P | Impact | Mitigation |
|------|---|--------|------------|
| Staff don't adopt Second Brain | M | High | Patrick models behavior 4 weeks alone before onboarding staff. One behavior. No guilt. |
| Architecture decisions in Word docs contradict v0.1 | H | Medium | That's expected — this PRD is v0.1. v0.2 updates post-digestion. |
| TT write API not available | M | Medium | Stage 1 (deep link) works without it. Layer 3 deferred. |
| Azure AD access delayed | H (current) | Medium | Phase 0 (Claude Project) and Phase 1 (Second Brain) don't require it. |
| AHI concentration | H (already real) | Very high | Orphaned account recovery + active diversification are first actions. |
| GDPR: Claude API for raw client PII | M | High | Use Azure OpenAI for CRM capture. Claude only for drafting (contains task context, not raw PII). |
| Patrick overload during Phase 0+1 | H | Medium | Phase 0 = 15 min/day max. Block calendar. Batch low-confidence reviews weekly. |

---

## 14. What This PRD Does NOT Yet Cover (v0.2 items)

Known gaps that the 400-page Word document analysis may fill:

- **New requirements** not yet captured (the primary reason for the Word doc digestion)
- **Architecture changes** if the Word docs contradict or improve on v0.1 decisions
- **n8n Teams connector** capability — can it replace Power Automate for Second Brain capture?
- **Day 1 runbook** for Patrick — exact daily routine for Phase 0
- **Staff onboarding protocol** — 30-minute live demo script
- **DPIA** (Data Protection Impact Assessment, required by GDPR before go-live) — **moved to Section 11 T7, blocking gate, not a v0.2 item**
- **Rollback plan** — how to pause system without losing data
- **Järvisydän second system** — does it get the same backoffice or variant?
- **Commercial model** — who pays for the shared infrastructure? Holdings overhead?
- **Detailed acceptance tests** per phase gate

---

## 15. Reference: Staff Map (do not re-mine)

| Staff | Email | Phone | Role |
|-------|-------|-------|------|
| Liisa Vihermaa | liisa.vihermaa@finland-dmc.com | +358 40 5540979 | Product & Sales Manager |
| Laura Ilvonen | laura.ilvonen@finland-dmc.com | +358 44 750 3395 | Group ops + Iceland FIT |
| Reeta Vihavainen | reeta.vihavainen@finland-dmc.com | +358 40 583 1665 | Program ops + repeat accounts |
| Sebastian Heiskanen | sebastian.heiskanen@finland-dmc.com | — | FIT/boutique |
| Piia Laitila | piia.laitila@finland-dmc.com | +358 40 9320 795 | Product & Sales Manager |

---

## 16. Portfolio Replication

Finland DMC is the pilot. Same backoffice, different data + prompts:

| Company | Use Case | Key Difference | Est. Time |
|---------|----------|----------------|-----------|
| Finland DMC | DMC proposal + email automation | Pilot — this build | Now |
| Järvisydän | Resort group sales + event automation | Resort suppliers, different golden prompts | After Finland DMC stable |
| M/S Marival | Cruise group sales — potentially agentic | More autonomous (structured cruises) | After Järvisydän |
| Other 1658 | Per company needs | Same backoffice | Rolling |

Replication per company: ~2–3 weeks once Finland DMC platform stable.

---

---

## 17. Design Decisions Log (Where This PRD Diverged From Source Documents)

Transparency about what Sonnet synthesized vs. what it invented. Added in v0.1.1 following Opus review.

| # | What the PRD changed | Source doc position | Why PRD changed it | Validation status |
|---|---------------------|--------------------|--------------------|-------------------|
| D1 | **Phase 0 = Claude Project MVP** (5 custom instruction files, no infrastructure) | Opus docs: Phase 0 = 4-week capture-only pilot. Infrastructure built first. | Faster path to value for Patrick. Validates golden prompts this week vs. waiting 4 weeks. | **Intact** — good change. Low risk. Does not conflict with Phase 1. |
| D2 | **Two products, one backoffice** (unified framing) | Source docs don't explicitly frame it this way. Each document designed one system independently. | Patrick's explicit instruction 2026-02-21: "they work together, similar backoffice life." | **Patrick-validated.** |
| D3 | **n8n as unified automation backbone for both systems (A3)** | Opus docs: Second Brain runs on Power Automate (7 flows designed in detail). Email Drafter design: n8n. | One tool to learn, one VPS, saves €15/month PA Premium. | **OPEN — A3/A5 in Section 11. Not validated. 400-page Word docs may resolve this.** |
| D4 | **Supabase as shared intelligence DB (A1)** | Opus docs: SharePoint Lists as the Second Brain's data store (8 lists, 200+ fields designed). Email Drafter: Supabase. | pgvector for semantic similarity, relational for version sequences, n8n-native. | **OPEN — A1 in Section 11. Adds sync layer complexity vs. pure M365.** |
| D5 | **SharePoint→Supabase sync layer** | Not in any source document. Pure PRD invention. | Required consequence of D4 — Second Brain captures in SharePoint, Email Drafter queries Supabase. | **Unvalidated.** Sync reliability and latency not modeled. |
| D6 | **7 Power Automate flows → n8n** (Second Brain flows) | Opus docs: PA flows for Classify & Route, Fix Handler, Daily Digest, Meeting Prep, Weekly Review, A4 Generator, Health Check — all fully designed. | Follows from D3 (n8n as backbone). | **OPEN — contingent on A5. If M365-native chosen, these flows exist in detail in opus-m365-architecture-design.md.** |
| D7 | **Relationship Health Score formula** (Section 5.5) | Present in Opus docs — weight distribution may differ. PRD version: interaction 30%, sentiment 25%, pipeline 20%, response time 15%, days since contact 10%. | Preserved from source docs (no significant change). | **Consistent with sources.** |
| D8 | **Azure OpenAI retained for CRM PII classification** | Explicitly designed this way in all Opus docs (Sweden Central, Data Zone Standard EUR). | GDPR compliance — the single most important legal constraint in the system. | **Consistent. Not changed.** |

**Bottom line on architecture risk:** D3, D4, D5 are the unknowns. If the 400-page Word documents indicate Patrick already decided on M365-native, Section 4.1 should be reverted and the Opus build execution plan (86 microtasks, 6 increments) reinstated as the build guide. If Word docs confirm n8n/Supabase, this PRD's Section 8 flows are the right starting point.

---

*PRD v0.1.1 — Opus review corrections applied 2026-02-21.*
*Architecture Decision A5 is the single most important unresolved question in this document.*
*Next: v0.2 after digesting 400-page Word documents.*
