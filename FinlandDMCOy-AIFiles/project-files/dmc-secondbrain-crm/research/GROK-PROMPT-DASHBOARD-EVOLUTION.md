# Grok Prompt — Staff Dashboard Evolution
**Date:** 2026-03-13
**Model:** Grok 4 Heavy (4-agent council)
**Purpose:** Validate and improve BP08 Staff Dashboard v2.0 based on Nate AI Open Brain research
**Paste to:** grok.com → Grok 4 Heavy mode → paste entire block below

> ⚠️ **PRE-SKILL-v1.2 PROMPT — DO NOT REUSE THIS PATTERN**
> This prompt contains pre-filled verdicts (A–E) in the "VERDICT FORMAT REQUIRED" section. That embedded the answers before Grok could reason independently — validation theater. Skill updated to v1.2 on 2026-03-13. Rebuild using open-question format before rerunning.

---

## PASTE START

**ROLE ASSIGNMENT — 4-AGENT COUNCIL:**

You are running as four specialized agents debating this question simultaneously. I need a structured council verdict, not a single answer.

- **Agent 1 — UX/Adoption Specialist:** Focus on staff behavior, adoption risks, interface design. What makes dashboards actually get used?
- **Agent 2 — Technical Architect:** Focus on implementation complexity, Supabase/n8n/Next.js feasibility, build cost vs value.
- **Agent 3 — DMC Operations Expert:** Focus on Finland DMC Oy specifically — 5-person travel DMC, B2B group sales, 107 clients, 6-stage pipeline, €1.25M in tracked deals.
- **Agent 4 — AI Systems Designer:** Focus on agent/human division of labor, memory architecture, pull/push patterns, the judgment line.

**DEBATE PROTOCOL:**
Each agent evaluates all 5 proposed improvements independently (A-E below). Then council votes: APPROVE / REJECT / MODIFY (with specific change). Final verdict per improvement: BUILD NOW / BUILD LATER / SKIP.

---

## CONTEXT: WHAT WE'VE BUILT

**Finland DMC Oy — 5-person destination management company**, Finnish travel B2B (group tours, corporate, leisure). 107 client profiles, €1.25M pipeline across 6 stages.

**Current Stack:**
- Supabase (Hetzner, eu-central-1) — 14 CRM tables, pgvector (text-embedding-3-small, 1536-dim), RLS, GDPR erase functions
- n8n (self-hosted) — email-to-deal automation via M365 Graph API
- Next.js PWA — Kanban board (drag-drop), deal cards with health scoring
- Wave 1A schema live. Wave 2A (email pipeline) in progress.

**Current BP08 Staff Dashboard features (already designed/building):**
- Kanban (6 stages: inquiry → invoiced, drag-drop, Supabase Realtime)
- Deal cards (health color, pax, value, days in stage, AI next-action suggestion)
- Morning dashboard (personalized, 3 priorities, overnight summary)
- Push notifications: 08:30 Teams briefing + stale deal alerts (7/14-day thresholds)
- Activity nudging: AI suggests next action → staff approves/edits/dismisses (ONE CLICK)
- Proposal tracking: SharePoint link + Graph API analytics → "client opened at 14:32"
- PWA: offline Kanban, push notifications, home screen install

**The judgment line (already designed):** Agent surfaces → human decides → agent executes. Medium-confidence stage transitions require staff approval. This is non-negotiable.

---

## RESEARCH INPUT: NATE AI OPEN BRAIN PRINCIPLES (March 13, 2026)

From: "You built an AI memory system. Now your agent needs hands." — natesnewsletter.substack.com

**Principle 1 — Two-Door Architecture**
Every surface needs both an agent door and a human door on the SAME data. Agent reads + writes (n8n automation). Human reads + writes (dashboard). Chat window alone is a keyhole. Visual layer is mandatory for spatial/scanning tasks.

**Principle 2 — Time-Bridging**
Agent memory doesn't decay. Surfaces historical connections humans miss: client inquired 2 years ago → agent bridges to current inquiry with context.

**Principle 3 — Cross-Category Reasoning**
Power is in connections BETWEEN tables. Staff workload + deal deadlines + seasonal windows = insights no single-table view produces.

**Principle 4 — Proactive Surfacing**
Design for what you want the agent to NOTICE, not just what staff will look up. Proactive > reactive.

**Principle 5 — The Judgment Line**
Agent surfaces, human decides, agent executes. Blur this = adoption failure. Hold this = trust builds.

**Principle 6 — Emotional Corrective**
Data corrects stress-induced narrative distortion. "You've advanced 7/10 similar deals at this stage" → prevents spiral when a deal goes cold.

**Principle 7 — Pull/Push Distinction**
Push = scheduled autonomous (cron). Pull = human opens interface. Same Supabase tables, different trigger. Both needed. Don't conflate.

---

## THE 5 IMPROVEMENTS TO EVALUATE

### Improvement A: Time-Bridging Panel on Deal Cards
**What:** When staff opens a deal, surface top 3 semantically similar historical closed deals: what we quoted, what closed, what the margin was.
**How:** pgvector similarity search on deal descriptions + destination + group profile → surface similar closed deals with outcomes.
**Value:** Staff gets institutional memory on first contact. No more "I think we quoted something like this last year..."
**Cost estimate:** 1 Supabase function (match_deals_similar()), 1 UI component on deal detail drawer. ~8-12h developer work.

### Improvement B: Cross-Category Staff Load View
**What:** A "capacity" panel showing each staff member's active deal count + total deal value in active stages + upcoming deadlines in next 14 days.
**How:** Aggregate query on deals table grouped by owner + join on deal_activities for deadline dates.
**Value:** Patrick and Janna (Head of Sales) see who is at capacity before assigning a new inquiry. Prevents overload. Enables proactive reassignment.
**Cost estimate:** 1 Supabase view (staff_load), 1 panel on morning dashboard + Kanban header. ~6-8h developer work.

### Improvement C: Emotional Corrective — Pipeline Health Metric
**What:** On morning dashboard, a single line per staff member: "Your win rate this month: 6/9 (67%) — above team average (58%)." Also: "AHI Travel is on your deal record: 100% close rate over 3 years."
**How:** Query win/loss records from deal_stage_history. Calculate rate per staff + per client.
**Value:** Data corrects distortion during deal-loss stress. Maintains confidence and decision quality.
**Cost estimate:** 1 Supabase view (staff_win_rates + client_win_rates), 1 UI element. ~4-6h developer work. REQUIRES: deal outcome tracking (won/lost) already in schema (confirm).

### Improvement D: Proactive Seasonal Alerts
**What:** System surfaces pricing window closures before staff asks. Example: "Lapland aurora rates valid until March 31 — 3 deals in inquiry stage haven't received a proposal yet — [View these deals]"
**How:** rate_cards table has valid_until dates. n8n cron cross-references against deals in inquiry/proposal stage with matching destinations. Fires at T-14 days, T-7 days.
**Value:** Converts missed seasonal deadlines from a problem into a proactive system output. Prevents revenue loss from expired pricing.
**Cost estimate:** 1 n8n workflow (W5: Seasonal Window Monitor), 1 Teams adaptive card template, 1 dashboard alert type. ~8-10h developer work. REQUIRES: rate_cards table has destination + valid_until fields.

### Improvement E: Supplier Knowledge Door (Two-Door for Suppliers)
**What:** Agent writes supplier updates (new rates, capacity notes, booking conditions) extracted from supplier emails → staff reads current supplier context on deal cards.
**How:** n8n classifies supplier emails → extracts rate/availability → updates suppliers + rate_cards tables → deal cards show "current availability" panel for relevant suppliers.
**Value:** Supplier knowledge stops living in email threads. Rate card is always current. Staff sees it at deal level without leaving the dashboard.
**Cost estimate:** Extend n8n W1 (email classifier) to handle supplier email type, add supplier_updates extraction prompt, add supplier context to deal_cards view. ~12-16h developer work. REQUIRES: supplier email classification pattern defined.

---

## SPECIFIC QUESTIONS FOR EACH AGENT

**Agent 1 (UX/Adoption):**
- Which improvement has highest adoption risk? Which has lowest?
- Is the emotional corrective (C) motivating or patronizing in a small 5-person team?
- Should time-bridging (A) be automatic or opt-in per staff member?

**Agent 2 (Technical Architect):**
- Which improvements require schema changes not yet in Wave 1A?
- Is there a dependency order? (Must B land before D? Must deal outcome tracking exist for C?)
- Estimate build complexity: LOW (can do in Wave 2A) vs MEDIUM (Wave 3A) vs HIGH (Wave 4A+)

**Agent 3 (DMC Operations):**
- Does Finland DMC Oy actually track win/loss outcomes today, or is this net new data?
- Does the supplier email pattern exist in the shared mailbox (info@, groups@)?
- Is the Head of Sales (Janna) the primary user of the load view, or would all staff use it?
- Are there seasonal window deadlines that historically caused revenue loss?

**Agent 4 (AI Systems):**
- Time-bridging (A): Should this be pgvector similarity or structured query by destination + group size range?
- Proactive surfacing (D): Should the seasonal alert be push (Teams notification) or pull (badge on Kanban header)?
- Cross-category (B): Is staff load a dashboard view or a morning briefing element or both?
- Does improvement E (supplier door) risk overloading the email classifier? Current n8n W1 handles inquiry/deal/non-deal. Adding supplier email type = 4-way classification.

---

## VERDICT FORMAT REQUIRED

For each improvement (A-E), provide:

```
IMPROVEMENT [X]: [Name]
Agent 1 vote: APPROVE / REJECT / MODIFY — [1 sentence reason]
Agent 2 vote: APPROVE / REJECT / MODIFY — [complexity: LOW/MEDIUM/HIGH] — [1 sentence reason]
Agent 3 vote: APPROVE / REJECT / MODIFY — [1 sentence reason]
Agent 4 vote: APPROVE / REJECT / MODIFY — [1 sentence reason]
COUNCIL VERDICT: BUILD NOW (Wave 2A/3A) / BUILD LATER / SKIP
CONDITION (if any): [what must be true before building]
```

After all 5 verdicts:

**PRIORITY BUILD ORDER:** [ranked list of approved improvements]
**WAVE ASSIGNMENT:** [which wave each improvement lands in]
**SCHEMA GAPS:** [any Supabase tables/columns needed that aren't in current schema]
**ONE THING WE MISSED:** [what does this council think we haven't considered at all?]

---

## CONSTRAINTS

- 5 staff users (not 500). Don't overengineer.
- Zero data entry rule is sacred. Improvements can't introduce manual work.
- Judgment line is non-negotiable. Agent suggests, human approves.
- GDPR: all extracted data stays in our Supabase (Hetzner, EU). No data to US services without DPA.
- Budget: each improvement must justify build cost vs operational value. Small team = high bar.
- Timeline: Wave 2A in progress (email pipeline). Wave 2B planned (bulk embeddings). Don't delay Wave 2A.

## PASTE END

---

## After Running Grok

Save the full response as:
`FinlandDMCOy-AIFiles/project-files/dmc-secondbrain-crm/orchestration/GROK-DEBATE-DASHBOARD-EVOLUTION-RESULT.md`

Then update BP08-STAFF-DASHBOARD-v2.md with approved improvements (add as "Phase 4 — Intelligence Layer" or integrate into existing phases depending on Grok verdict).
