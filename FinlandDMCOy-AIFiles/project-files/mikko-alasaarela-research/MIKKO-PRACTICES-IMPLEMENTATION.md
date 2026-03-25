# IMPLEMENTATION ANALYSIS: Mikko Best Practices → 1658 Holdings
**Built:** 2026-03-19 | **v1.1 updated:** 2026-03-20 | **Source:** MIKKO-ALASAARELA-KNOWLEDGE-FILE.md | **Model:** Sonnet 4.6 | **Sessions:** S101–S102

> **JUDGE STATUS:** Internal red team passed. External judge: Grok 4.20 Heavy (Harper + Benjamin + Lucas) — **CONDITIONAL GO** (2026-03-20). 5 corrections applied in v1.1: 4-axis matrix, #5 leverage correction, Practice #4 tier fix, CoS drop-off mitigation, staff/client implications. See REALISM section.

---

## CURRENT STATE ASSESSMENT

1658 Holdings has a mature session/tool architecture (Tier A rules, PWJ loop, 3-mode orchestration, EU-compliant stack) but operates primarily as a **tool operator**, not a **system designer**. Mikko's 8 practices describe a fully designed governance layer on top of tools — 1658 is ~3/8 of the way there. The structural gap: no persistent thinking channel, no auto-approval tier, and no explicit KPI injection into agent spawns. These are behavioral and architectural gaps, not tool gaps. The good news: the top 3 highest-leverage practices require zero new infrastructure.

---

## GAP ANALYSIS TABLE

> Dual-citation rule: every gap cites one detail from MIKKO-ALASAARELA-KNOWLEDGE-FILE.md AND one from CLAUDE.md or CURRENT-STATUS.md.

| # | Practice | Current State | Gap Description | Priority | Effort | Tier |
|---|----------|--------------|-----------------|----------|--------|------|
| 1 | Chief of Staff Bot | **PARTIAL** | Mikko: "Aina kun mulla on joku idea... mä en enää avaa Wordia... vaan mä avaan sen mun Chief of Staff -botin" (Section C, Norders verbatim). Current: Patrick opens new Claude Code sessions per problem — no persistent second-screen channel. CLAUDE.md has no protocol for raw cognitive dumping before structuring. | H | 30 min setup + 1 week habit | 1 |
| 2 | Agent Farm Manager Mindset | **PARTIAL** | Mikko: "Every task starts with: 'which agent handles this?' not 'how do I do this?'" (Section ★, BP2). Current: PWJ Tool-Lock exists in CLAUDE.md but S97-99 audit found "First-Action Failure — Claude skips /pwj and rushes to linear execution." Patrick delegates unevenly — subagents used for deliverables, but CEO-level tasks often done inline. | H | 0 setup; 1 week habit | 1 |
| 3 | Mission-as-Code KPIs | **PARTIAL** | Mikko: "Every agent task is tied to a business KPI or goal explicitly" (Section ★, BP3). Section G, Move 3: "Python or Supabase edge function that prepends portfolio KPIs to every agent spawn prompt." Current: CLAUDE.md spawn prompts include project context but NO standardized KPI injection (e.g., proposal win rate 40%→60%, DMC revenue target). | H | 2h for KPI snippet library | 2 |
| 4 | Urgency + Experimentation Loop | **NOT DONE** | Mikko: "Don't wait. Learn fast." (Solteq, Section E). Section ★, BP4: "When uncertain about a workflow — build it this session, even messily." Current: CRM Wave 3A blocked pending Wave 2B/Frendy OAuth2 unblock (CURRENT-STATUS.md: "Wave 2B PARKED, re-evaluate 2026-06-19"). Pattern of waiting for "right conditions" confirmed by 3+ month queue. ⚠️ v1.1: Moved to pure Tier 3 — "2/3 hybrid" was wrong-tier call. No experimentation bandwidth until #1/#2 habits exist. (Grok: Lucas) | M | 4h prototype; full 3A = 2–3 wks | 3 |
| 5 | Compound on Existing Strengths | **PARTIAL** | Mikko: "Applies AI multiplier to areas where he is already elite... doesn't use AI to become mediocre at new things." (Section ★, BP5). CLAUDE.md: current sessions include CEO doing "formatting/file-management work" implicitly (no explicit delegation filter). No written rule in Tier A for "Patrick-only" task class. | M | 0 setup; filter applied per task | 1 |
| 6 | Replace Review with Policy (Trust Score) | **NOT DONE** | Mikko: "95% auto-approval via Governance-as-Code... I only see exceptions." (Section ★, BP6). Section G, Move 2: "Add trust_score FLOAT column to workflow table. Higher trust_score = fewer gates required." Current: Supabase has n8n_errors table (MEMORY.md) but no trust_score column. Patrick reviews all n8n outputs manually. | H | 2h schema + 4h n8n triggers | 3 (Wave 3A) |
| 7 | Sovereignty-First Architecture | **DONE** | Mikko: "EU data, customer-specific models, immutable audit." (Section ★, BP7). MEMORY.md: "Anthropic Teams + DPA, Supabase EU region, n8n self-hostable — already implemented." Minor gap: no written checklist for evaluating NEW services. | L | 30 min to formalize checklist | 1 |
| 8 | Productivity Filter (One Metric) | **PARTIAL** | Mikko: "Productivity is the only metric that matters. Does this increase output per unit of human effort?" (Section ★, BP8). CLAUDE.md: attributed_value_eur exists as PRIMARY metric in quality gate — but it tracks session value, NOT used as explicit filter for tool/vendor ADD decisions. No written veto protocol. | M | 1h CLAUDE.md addition | 2 |

---

## PRACTICE PRIORITY MATRIX

**Scoring:** H = 3, M = 2, L = 1. Composite = sum (max 12 with 4 axes).

> ⚠️ **v1.1 change:** 4th axis "Adoption Ease" added after Grok Benjamin identified that the 3-axis system was structurally insufficient — missing habit sustainability and CEO bandwidth constraints. Axis definition: H = low friction, no new habit required; M = moderate habit challenge; L = high drop-off risk. #5 Leverage also corrected M→H per Benjamin (fires on every task = elite-area amplifier). New max = 12.

| # | Practice | Leverage (H/M/L) | Feasibility (H/M/L) | Stack Fit (H/M/L) | Adoption Ease (H/M/L) | **Composite /12** |
|---|----------|-----------------|--------------------|--------------------|----------------------|------------------|
| 1 | Chief of Staff Bot | H (3) | H (3) | H (3) | M (2) | **11** |
| 2 | Agent Farm Mindset | H (3) | H (3) | H (3) | M (2) | **11** |
| 3 | Mission-as-Code KPIs | H (3) | M (2) | M (2) | H (3) | **10** |
| 4 | Experimentation Loop | M (2) | L (1) | M (2) | L (1) | **6** |
| 5 | Compound Strengths | **H (3)** ¹ | H (3) | H (3) | H (3) | **12** |
| 6 | Replace Review/Policy | H (3) | L (1) | H (3) | M (2) | **9** |
| 7 | Sovereignty-First | L (1) | H (3) | H (3) | H (3) | **10** |
| 8 | Productivity Filter | M (2) | H (3) | H (3) | H (3) | **11** |

¹ Leverage corrected M→H (Grok Benjamin): #5 fires on every task assignment, multiplying CEO-elite strengths — same leverage tier as #1/#2.

**Updated top-3 by composite: #5 (12), then #1/#2/#8 all tied at 11.**

Tiebreaker (11-point practices): #1 and #2 beat #8 because they address documented system failures (#1 = missing persistent channel, #2 = documented First-Action Failure in S97-99 audit). #8 (Productivity Filter) is already partially implemented via attributed_value_eur (CLAUDE.md) — delta is formalization only. #1 and #2 represent unimplemented gaps; #8 is a gap-closing edit. Updated 90-day forecast reflects this ranking.

---

## TIER 1 — IMMEDIATE (Today–This Week, Zero New Tools)

### Practice #1: Chief of Staff Bot

**Do this today:** Open claude.ai → create a new Project named "Chief of Staff — 1658 Holdings" → paste the starter system prompt from the CHIEF OF STAFF BOT SPEC section below into Custom Instructions → open it as the second browser tab that never closes.

**First-week observable outcome (measurable):** By Friday 2026-03-27, Patrick has opened the CoS Project ≥5 times for raw-thought dumping INSTEAD of opening a blank doc or a new Claude Code session for the same purpose. Success criterion = at least 3 of those 5 sessions produced a structured output (plan, email draft, decision framework) without Patrick structuring the input first.

**Named guardrail:** The **blank-doc reflex under urgency** — when Kulusiirto DL 23.3 fires, Patrick will open a blank doc for the submission template because it feels faster. Pre-commit the CoS bot as the first action for ALL Kulusiirto thinking, not just blue-sky strategy. The bot does not slow down urgent work — it replaces the blank-page paralysis that precedes every first sentence.

---

### Practice #2: Agent Farm Manager Mindset

**Do this today:** Before starting any task in the current Claude Code session or claude.ai, state explicitly (even silently): *"Is this Patrick-level judgment, or can a subagent handle this?"* If delegatable → /pwj or spawn. Do not proceed inline without answering this question first.

**First-week observable outcome (measurable):** In session logs for S101–S104, human_interventions stays ≤2 for Tier 1/2 tasks. If Patrick finds himself doing formatting, file-moving, or template-filling work inline = trigger missed. One measurable proxy: zero inline file-formatting tasks in sessions S101–S104.

**Named guardrail:** **The "I'll review it anyway" reflex** — spawning a subagent and then rewriting its output manually negates the leverage. Per CLAUDE.md Tier A: "Validation bottleneck is mandatory" but validation ≠ rewriting. The guardrail: if the output passes the done criteria, it ships. If it fails, reject and re-spawn with tighter criteria. Rewriting inline = silent delegation failure.

---

### Practice #5: Compound on Existing Strengths (zero-setup filter)

**Do this today:** Before any task this session, apply this two-question filter: (1) *"Is this a task that requires my specific CEO context — strategic judgment, client relationships, Finland DMC positioning, portfolio oversight?"* (2) *"Or is this a task that a capable agent could do with a well-written prompt?"* If (2) → spawn. Patrick-time is **only** for (1).

**First-week observable outcome (measurable):** Zero sessions this week where Patrick writes email subject lines, formats markdown tables, or moves files manually. Each of those tasks gets a 2-sentence spawn prompt instead.

**Named guardrail:** **Expertise-gap filling** — using AI to become adequate at SEO technical implementation, legal drafting structure, or accounting, rather than deploying existing CEO strengths. Mikko's warning (Section ★, BP5): "AI compound leverage only works if the pre-AI baseline is already elite." Patrick's baselines: Finnish B2B relationship management, portfolio strategy, governance, client narrative. Stay in those lanes.

---

## TIER 2 — SHORT-TERM (2–4 Weeks, Minimal Setup)

### Practice #3: Mission-as-Code KPI Injection (2h effort)

**What to build:** A `KPI-SNIPPETS.md` file in `_shared/` containing 5–8 standard business context blocks, each 3–4 lines. Example block:

```markdown
## DMC Proposal Win Rate
Current: ~40% (estimated, no CRM baseline)
Target: 60% by Q3 2026
Stakes: Each additional 10pp = ~€25K ARR at current pipeline volume
```

**How to use:** Paste the relevant snippet at the top of any significant agent spawn prompt. Not every prompt — only those where the agent could optimize the literal task at the expense of the real goal (proposals, CRM data enrichment, client comms).

**When to build:** After Kulusiirto submission (DL 23.3). Time cost: 2 hours to draft KPI snippets for DMC + Järvisydän + Saimaa.

---

### Practice #8: Productivity Filter Formalization (1h)

**What to add to CLAUDE.md** (Tier A, Vendor Evaluation section):

```markdown
### Vendor/Tool Veto Protocol
Before adopting any new service, answer: "Does this increase Patrick-time output per hour?"
- Adds capability without leverage increase → DEFER (minimum 30-day hold)
- Increases leverage clearly → proceed with 1-week test
- Unclear → do a 30-minute experiment THIS session before deciding
Applies to: AI services, SaaS tools, n8n integrations, API subscriptions.
```

**When to build:** Before any new tool evaluation arises. Can be written in 30 minutes the next time a new tool is proposed. Not urgent today.

---

## TIER 3 — WAVE 3A (After CRM Wave 2B Unblocks)

> ⚠️ Wave 2B PARKED until Frendy OAuth2 resolution (re-evaluate 2026-06-19). Do NOT pull these forward.

### Practice #6: Replace Review with Policy

**Step 1 (after Wave 3A kickoff):** Identify all n8n workflows with ≥20 runs and 100% pass rate. These are auto-approval candidates — Patrick is currently reviewing them manually for no reason.

**Step 2:** Add `trust_score` column to Supabase (schema below).

**Step 3:** Deploy OPA/Rego policy (github.com/open-policy-agent/opa) via n8n HTTP node for high-stakes decisions. Route low-trust or exception-class outputs to Patrick; auto-approve high-trust recurring ones.

---

## CHIEF OF STAFF BOT — IMPLEMENTATION SPEC

### Option A: claude.ai Project (Persistent Browser Tab)

**Interface:** claude.ai → Projects → "Chief of Staff — 1658 Holdings"
**Rationale:** Always-on, no terminal required, M365 connector available (reads email + calendar), persistent conversation history creates genuine multi-turn memory. Patrick already uses claude.ai for M365 mining — this extends an existing habit. Custom Instructions update manually (5 min/week).
**Weakness:** No Claude Code tool access, no file writes. Bridging to Claude Code requires copy-paste.

### Option B: Claude Code Persistent Session (Terminal Second Screen)

**Interface:** Dedicated Claude Code terminal window, kept open
**Rationale:** Full tool access, can read files and write to `_drafts/`, spawn subagents
**Weakness:** Context window expires in 2–3 hours of heavy use; no natural "second screen" feel; requires terminal to be open; harder to maintain continuity across days; M365 connector not available.

### Trade-off Analysis: Option A wins for Patrick's context

**Decision:** Option A (claude.ai Project). Reasons:
1. **Always-on requirement** — the Chief of Staff bot must be open before the problem appears, not opened in response to a problem. Browser tabs survive session breaks; terminal windows do not.
2. **M365 connector** — calendar awareness lets the bot say "you have a Rainer meeting in 3 days" without Patrick providing that context every time.
3. **Existing habit** — Patrick already has claude.ai open for mining. Adding a second Project tab costs zero new behavior.
4. **Bridging is solvable** — when CoS output needs to feed Claude Code (file writes, subagent spawns), Patrick copies the structured output to `_drafts/` as a .txt file. The $0.50 bridge cost is worth the always-on reliability.

Option B is better for technical tasks where file access matters — use it for Claude Code sessions that need continuity, not for raw thinking.

---

### Starter System Prompt (copy-paste into Custom Instructions)

```
You are the Chief of Staff for Patrick Heiskanen, CEO of 1658 Holdings Oy (Finnish portfolio holding, 10 operating companies, ~50 staff). I'm a systems-level thinker with strong Finnish B2B relationship management and portfolio strategy skills. I default to structured thinking but often need help organizing raw thought before structuring.

YOUR JOB:
When I dump a raw problem or idea, do NOT immediately give me a solution.
1. Ask 2-3 Socratic questions that reveal what I actually need to decide.
2. Identify what class of problem this is: strategic (needs my judgment), operational (can be delegated), or clarity (needs more information before either).
3. Only after the above: help me structure the thinking or draft the output.

CONTEXT I ALWAYS CARRY:
- Portfolio companies: Finland DMC Oy (primary — B2B travel, 5 staff), Järvisydän resort, Lomakylä Järvisydän, Houseboat Saimaa, Resort Services, + 5 others in development
- Current critical deadline: Kulusiirto lausunto at lausuntopalvelu.fi, DL 2026-03-23
- Active build: DMC CRM Wave 3A (Kanban) — starting after Wave 2B Frendy OAuth2 unblocks
- My stack: Claude Code + claude.ai + n8n + Supabase (EU) + Microsoft 365
- GDPR rule: never put client PII into prompts — use roles/summaries

HOW TO UPDATE MY CONTEXT:
I'll tell you when priorities shift. If I say "kulusiirto is done" or "Wave 3A is starting," update your assumptions.

COMMUNICATION STYLE:
Short questions. No preamble. If I give you a wall of text, identify the ONE decision I'm avoiding and ask it directly. I can handle direct challenges — don't soften useful friction.

WHEN IN DOUBT:
Ask: "What does success look like by end of this week for this?" before proceeding.

LANGUAGE:
I communicate in Finnish and English interchangeably. When I write in Finnish, respond in Finnish. When I write in English, respond in English. Finnish B2B travel context: client relationships in Finland are long-cycle, trust-based, and relationship-first — do NOT suggest shortcuts that damage supplier/client trust for short-term efficiency. Kulusiirto, lausunto, kuntapäätös = Finnish public-sector processes requiring formal, careful language. Never suggest delegating Finnish relationship work to automation without explicit Patrick approval.
```

---

### ⚠️ Habit Sustainability (v1.1 — Grok Harper finding)

Harper (Round 1) and Harper (Round 2) both confirm: executive "always-on second screen" habits sustain poorly without an explicit anchor. Round 2 adds a more specific data point: **MIT/NANDA 2025 report (cited by Grok Harper — unverified, treat as risk signal):** 95% of GenAI pilots fail measurable P&L impact. X exec threads confirm a consistent pattern: productivity spikes in weeks 1–2, then plateaus as urgency reflexes win. The original "extends existing habit" assumption is fragile for the same reason: mining is scheduled, CoS thinking is opportunistic — and opportunistic habits are exactly what urgency kills.

**Three specific drop-off risks for Patrick's context:**

1. **Urgency bypass (highest risk — fires on Kulusiirto DL 23.3 immediately):** Under deadline pressure, the blank-doc reflex wins. Patrick opens what's fastest, not what's best. Mitigation: anchor the CoS bot to the laptop-open morning routine BEFORE any urgent work appears. The trigger is "laptop open," not "I have a problem." The Kulusiirto submission IS the first test — use the bot for raw Kulusiirto thinking today, not after the deadline passes.

2. **Mining context collision:** Patrick uses claude.ai Projects for M365 mining. The CoS bot is a different Project. Risk: navigating between Projects adds friction; Patrick consolidates into one. Mitigation: name the Projects visually distinct and pin CoS first in the Projects sidebar.

3. **Quality disappointment + 2-week plateau:** If the CoS bot gives one generic response on a Finland-specific public-sector question, trust collapses. The X exec pattern (spike then plateau) suggests this is the failure sequence: enthusiastic first week → one bad response under deadline → reversion to blank doc. Mitigation: (a) use the bot ONLY for strategic framing and raw-thought dumping in weeks 1–2 — never for operational tasks where Claude Code is better; (b) run a mandatory 2-week check-in (see Quick-Start Checklist) to catch plateau before it becomes abandonment.

---

### Persistence Method

**Chosen method:** Custom Instructions in claude.ai Project, updated manually on two triggers:
1. **Weekly (Friday, 5 minutes):** Update the "Current critical deadline" and any completed deliverables
2. **After major decisions:** Add decision outcome to context ("Wave 2B unblocked — Wave 3A is starting")

**Why not a file-based system:** Custom Instructions persist natively in claude.ai without Patrick needing to re-load a file at each session start. The cognitive cost of maintenance must be near-zero for this habit to survive.

**Bridge to Claude Code:** When CoS session produces a decision or structured plan Patrick wants to act on → copy to `~/1658HoldingsOy-AIFiles/_drafts/cos-output-YYYY-MM-DD.txt` → load in Claude Code next session.

---

### Multi-Turn Handoff Example

**Day 1 (Monday 8:03am):**
> Patrick: "Mietin pitäisikö meidän laajentaa Lappiin. Rainer tapaaminen ensi viikolla. En tiedä mitä haluaisin siitä saada ulos."

> CoS Bot: "Kolme kysymystä ennen kuin puhutaan Lapista:
> 1. Tarkoitatko laajentamista tuotteen (uusi matkapaketti), asiakaskunnan (uudet yritykset), vai resurssien (uusi henkilö tai toimipiste) näkökulmasta?
> 2. Rainer-tapaamisen pohjalta — haluatko oppia jotain, päättää jotain, vai myydä jotain?
> 3. Mikä on se skenaario, jossa lähtisit tapaamisesta miettien 'tämä meni huonosti'?"

> Patrick: "Hyvä. Ensin resurssit (partneri tai henkilö). Rainer-tapaamisessa haluan päättää pilotista. Huono skenaario = lähden ilman selkeää 'seuraava askel'."

> CoS Bot: "Selvä. Tapaamisessa siis yksi kysymys: 'Voisimmeko tehdä yhden koeprojektin ennen vuotta?' Tarvitsenko tarjousstrategiaa vai riittääkö tapaamisen agenda?"

**Day 2 (Tuesday 8:45am):**
> Patrick: "Sain lisätietoa Rainerin tilanteesta — heillä on budjettineuvottelut meneillään."

> CoS Bot: "Muistan eilisen keskustelun. Tämä muuttaa Rainer-tapaamisen taktiikkaa: budjettineuvottelujen aikana kukaan ei päätä uusista piloteista. Tavoitetta kannattaa laskea: sen sijaan että haet 'päätöstä pilotista', hae 'suostumus keskusteluun Q3:ssa.' Riittääkö tämä, vai pitääkö meidän uudelleen arvioida koko Lappi-timing?"

[Context from Day 1 preserved without re-explanation: company = Finland DMC, decision type = operational pilot, Rainer = specific named contact with next-step focus.]

---

**Start today:** Open claude.ai → click "New Project" → name it "Chief of Staff — 1658 Holdings" → paste the starter system prompt above into Custom Instructions → open the Project tab and dump the Kulusiirto lausunto challenge as the first raw input.

---

## SUPABASE TRUST SCORE — SCHEMA SKETCH

> Wave 3A item. Do not build until after CRM Wave 2B unblocks. Schema is designed for the existing Supabase instance (fjfztbdcjoptkwbzwoub, EU region).

```sql
-- New table: n8n_workflow_trust
-- Purpose: Track per-workflow run history and earned autonomy level

CREATE TABLE n8n_workflow_trust (
  id                    UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  workflow_id           TEXT NOT NULL UNIQUE,     -- n8n workflow UUID (from n8n API)
  workflow_name         TEXT NOT NULL,            -- human-readable (e.g., "email-to-deal")
  trust_score           FLOAT DEFAULT 0.50,       -- 0.0–1.0; starts neutral
  total_runs            INTEGER DEFAULT 0,        -- cumulative execution count
  successful_runs       INTEGER DEFAULT 0,        -- runs with no error AND no rejection
  manual_overrides      INTEGER DEFAULT 0,        -- times Patrick manually intervened
  last_run_at           TIMESTAMPTZ,              -- for decay calculation
  auto_approve_threshold FLOAT DEFAULT 0.90,      -- trust_score >= this → skip human gate
  opa_policy_id         TEXT,                     -- linked OPA/Rego policy (nullable until Wave 3A)
  created_at            TIMESTAMPTZ DEFAULT NOW(),
  notes                 TEXT                      -- manual override reason, Patrick-authored
);

-- Index for n8n webhook lookups
CREATE INDEX idx_workflow_trust_id ON n8n_workflow_trust(workflow_id);

-- Trigger logic (n8n → Supabase edge function):
-- On workflow SUCCESS webhook:
--   total_runs += 1
--   successful_runs += 1
--   trust_score = (successful_runs / total_runs) * decay_factor
--   decay_factor = 1.0 if last_run_at < 7 days ago; 0.95 if 7-30 days; 0.85 if >30 days
--
-- On workflow FAILURE or MANUAL OVERRIDE:
--   total_runs += 1
--   manual_overrides += 1
--   trust_score = MAX(0.10, trust_score * 0.85)  -- penalty, never zero
--
-- Auto-approve check (n8n decision node):
--   IF trust_score >= auto_approve_threshold AND total_runs >= 20
--   THEN route to output directly
--   ELSE route to Patrick review queue
```

**OPA integration (Wave 3A, after schema deployed):**
- Deploy OPA as Docker container on same server as n8n
- n8n HTTP node calls `POST /v1/data/workflow/allow` with `{workflow_id, output_hash, trust_score}`
- Rego policy: `allow = true if input.trust_score >= 0.90 and input.total_runs >= 20`
- Policy files git-tracked in `_shared/opa-policies/` (audit trail)

---

## ANTI-PATTERNS (failure modes per adopted practice)

> Each must cite MIKKO-ALASAARELA-KNOWLEDGE-FILE.md AND CLAUDE.md or CURRENT-STATUS.md. Generic failures = FAIL.

### Practice #1 — Chief of Staff Bot: "The Urgency Bypass"

**Failure mode:** Patrick opens the CoS bot for strategic thinking (Lapland expansion, partnership framing) but reverts to blank docs when urgency is high (Kulusiirto DL, Rainer prep). The bot becomes a blue-sky tool, not a daily cognitive driver.

**Why it's specific to Patrick:** CURRENT-STATUS.md shows CURRENT PHASE contains "⚠️ Kulusiirto DL 23.3 still untouched" as the lead urgent item. High-urgency moments are exactly when the blank-doc reflex wins. Mikko's Norders verbatim (Section C): "Aina kun mulla on joku idea tai joku ongelma" — the "joku ongelma" is the failure case Patrick's reflex avoids. The bot must fire on problems, not just ideas.

**Mitigation:** Use the CoS bot as the FIRST step for Kulusiirto today — not Claude Code, not a new session. Urgency is the test, not the exception.

---

### Practice #2 — Agent Farm Mindset: "Phantom Delegation"

**Failure mode:** Patrick spawns a subagent, reviews the output, finds it 80% right, and rewrites it manually in the main thread — spending MORE time than if he'd done it himself. Delegation theater with no leverage gain.

**Why it's specific to Patrick:** CLAUDE.md documents "First-Action Failure — Claude skips /pwj and rushes to linear execution" from S97-99 audit. The same reflex applies to output review: rushing to inline editing bypasses the "reject and re-spawn with tighter criteria" path. For a 5-person B2B travel CEO, time spent on inline editing is directly competing with client relationship time — the highest-leverage activity.

**Mitigation:** Binary review protocol: output either passes done criteria (ships) or fails them (re-spawn with specific failure note). No inline rewriting. If rewriting feels necessary more than once per session → spawn criteria were underspecified. Fix the criteria, not the output.

---

### Practice #5 — Compound Strengths: "Expertise Substitution"

**Failure mode:** Patrick uses AI to fill expertise gaps (SEO technical auditing, legal document structure, accounting analysis) instead of deploying AI to multiply existing CEO strengths (strategic narrative, Finnish public sector relationships, portfolio oversight). Result: hours spent reviewing AI outputs in domains where Patrick can't evaluate quality well — the "jagged frontier" failure.

**Why it's specific to Patrick:** Section ★, BP5 is explicit: "Do NOT try to use AI to replace deep expertise you don't have yet. Go deep where you're already strong." 1658 Holdings has active Järvisydän SEO work, CRM architecture decisions, and legal/governance (Kulusiirto) all in flight. Each of these domains has a delegatable technical layer AND a CEO-judgment layer. The failure is letting the technical layer consume CEO time. For a 5-person company, Patrick is simultaneously CEO, IT manager, and system architect — bandwidth constraints make expertise substitution attempts especially costly because there's no one else to catch the errors.

**Mitigation:** Before starting any task: "Can I evaluate the quality of the output without domain expertise?" If no → this is a Tier 3 task requiring external validation, not CEO inline work. Route to a specialist subagent with explicit validation criteria.

---

## REALISM & SAFEGUARDS

### Patrick's realistic weekly AI time budget

Based on CURRENT-STATUS.md session frequency (~3-4 Claude Code sessions/week, typical 2-3h each) + claude.ai mining (~2-3h/week) = **8–12 hours/week total AI tool time.** No new time is created by this plan. Budget is a redistribution: Chief of Staff bot replaces blank-doc thinking time (not AI time), Agent Farm Mindset reduces session length by 20-30% if delegation succeeds, Compound Strengths filter prevents low-leverage work from entering the session queue at all.

**⚠️ Kulusiirto DL 23.3 consumes ~4h this week.** Realistically, 4-6 hours of "strategic practice adoption" time available in the 3-day window before DL. Tier 1 actions are designed to take <5 min setup for exactly this reason.

---

### ⚠️ Staff & Client Implications (v1.1 — Grok Lucas finding)

Tier 1 practices (#1/#2/#5) are CEO-only and require zero staff involvement. Safe to deploy immediately. However, Tier 3 (Trust Score + auto-approval) has direct staff and client implications that the v1.0 document ignored:

- **Auto-approval in Wave 3A:** When n8n workflows auto-approve without Patrick review, Liisa/Reeta/Sebastian interact with outputs they don't know were un-reviewed. For a B2B travel DMC, a wrongly auto-approved supplier proposal or client email carries relationship risk. Mitigation: auto-approval gates (trust_score ≥ 0.90 AND total_runs ≥ 20) must exclude any workflow that touches client-facing outputs until a separate "staff validation loop" is built.
- **Finnish-language prompts:** Mikko's system is Finnish-context native. The CoS bot starter prompt is in English. Patrick thinks in both — but if staff start using the CoS Project directly (likely if it proves value), Finnish-language prompts and Finnish B2B norms must be explicit in Custom Instructions. Add a Finnish-language instruction block to the starter prompt when staff onboarding begins.
- **GDPR friction:** The Sovereignty-First practice is DONE at the infrastructure level, but the CoS bot Custom Instructions contain real context (company names, deadlines, project names). Claude.ai Projects' GDPR coverage relies on the Anthropic Teams DPA (MEMORY.md). Confirm DPA covers Projects before adding staff-visible client names to Custom Instructions.

---

### 3 specific ways THIS plan could be read once and ignored — with mitigations

**1. Failure mode: "Document overload at peak urgency"**
Patrick opens this document with Kulusiirto DL 3 days away. The 12-section structure, 90-day forecast, and schema sketches look like a "later project" next to an immediate deadline. Document is closed after skimming.
→ **Mitigation:** Quick-Start Checklist below has ONE action that takes <5 min today. That's the only required action before DL 23.3. The rest is reference. Patrick reads checklist first, returns to document post-deadline.

**2. Failure mode: "Chief of Staff bot opened once, abandoned"**
First CoS session produces structured Kulusiirto framing. Patrick feels satisfied. Week 2: Claude Code is already open and it's faster to dump there. Pattern broken after one use.
→ **Mitigation:** Anchor to a non-AI trigger: "When I open my laptop every morning, the second tab I open (after email) is the CoS Project." The habit signal is laptop-open, not problem-appearance. Breakfast ritual > problem-triggered adoption.

**3. Failure mode: "'We already do this' rationalization for Practice #2"**
Patrick reads Agent Farm Mindset, notes that /pwj exists and subagents are used regularly, and concludes this is implemented. The S97-99 First-Action Failure is classified as "edge case" rather than systemic gap.
→ **Mitigation:** Specific falsification test: in session S101, count how many tasks Patrick started inline before asking "should this be delegated?" If count > 0 → the gap is real. The habit must fire BEFORE starting, not after noticing the work has already begun.

---

## QUICK-START CHECKLIST

```
[ ] TODAY (5 min): Open claude.ai → New Project → "Chief of Staff — 1658 Holdings"
    → Paste starter system prompt into Custom Instructions
    → First input: "Mulla on Kulusiirto lausunto DL 23.3 — tässä raaka ajatus..." [dump raw]

[ ] TODAY (0 min): Before any task this session, ask aloud: "CEO judgment or delegatable?"
    Delegate anything that doesn't require my specific context.

[ ] THIS WEEK: Open CoS bot ≥5 times instead of blank doc. Measurable by Friday.

[ ] 2-WEEK CHECK-IN (2026-04-03): Answer 3 questions — (1) Has the CoS bot been opened daily? (2) Did it fire under urgency (Kulusiirto-class work) or only for blue-sky thinking? (3) Has any output disappointed enough to trigger reversion to blank doc? If (1) no or (2) only blue-sky → adjust anchor trigger. If (3) yes → diagnose which task type caused it and add it to the "do NOT use CoS for X" list.

[ ] THIS WEEK (2h): Write KPI-SNIPPETS.md in _shared/ with DMC + Järvisydän blocks.

[ ] WAVE 3A (after CRM Wave 2B unblocks, re-evaluate 2026-06-19):
    → Create n8n_workflow_trust table in Supabase
    → Identify 3 workflows with ≥20 runs + 100% pass rate → these are auto-approve candidates
    → Deploy OPA via Docker, wire to n8n HTTP node
```

---

## 90-DAY ADOPTION FORECAST

> Calibration check: top-3 by matrix composite score. Mix of effort levels verified (behavioral/0-setup, light KPI work, infrastructure). All Tier 1 actions traceable to CURRENT-STATUS.md.

### Top-3 by composite score (4-axis: Leverage × Feasibility × Stack Fit × Adoption Ease, max 12):

> v1.1 update: #5 now ranks #1 overall (12/12 after Leverage corrected to H). #1 and #2 tie at 11/12. #8 (Productivity Filter) also scores 11/12 but is beaten by documented-failure urgency (see below).

**#1 — Compound Strengths (score 12/12)**
- **Patrick hours/week:** 0 new hours (mental filter — prevents low-leverage work entering the queue)
- **Blocker verbatim:** "**Active Project** | ⚠️ Kulusiirto (DL 23.3) — KRIITTINEN." (CURRENT-STATUS.md) — Kulusiirto IS the compound strength domain: Finnish governance relationships, inter-company interests, political positioning. The filter activates on this task immediately.
- **Beat #4 (Productivity Filter, 11/12) because:** Both score 11 (Productivity) and 12 (Compound) — not actually tied. Compound scores higher on Leverage (H vs M for Productivity) because it fires on every task and amplifies Patrick's strongest CEO skills. Productivity Filter is partially implemented already; Compound Strengths is not.
- **Execution risk:** LOW (mental filter, zero infrastructure, zero habit formation required).

**#2 — Chief of Staff Bot (score 11/12)**
- **Patrick hours/week:** 2h (30 min/day morning thinking)
- **Blocker verbatim:** "Session 100 COMPLETE — Mikko Alasaarela research: 3 Grok Heavy rounds done, bridge built. **Synthesis session pending. ⚠️ Kulusiirto DL 23.3 still untouched.**" (CURRENT-STATUS.md, Current State)
- **Beat #4 (Productivity Filter, 11/12) because:** Productivity Filter is already partially implemented via attributed_value_eur (CLAUDE.md Tier A) and fires only on tool-add decisions. CoS Bot is NOT currently implemented and fires on every cognitive task. Gap size × frequency = higher priority at same score. Tiebreaker: documented absence vs. formalization delta.
- **Execution risk:** MEDIUM (habit formation — see Habit Sustainability section). Mitigation: laptop-open trigger.

**#3 — Agent Farm Manager Mindset (score 11/12)**
- **Patrick hours/week:** 1h upfront; saves 20-30% per session thereafter if delegation succeeds
- **Blocker verbatim:** "⚠️ FIRST ACTION for any PWJ session: invoke /pwj skill BEFORE reading files." + "S97-99 audit identified 'First-Action Failure' — Claude skips /pwj and rushes to linear execution, producing Checklist Theater." (CLAUDE.md Tier A, PWJ Tool-Lock)
- **Beat #4 (Productivity Filter, 11/12) because:** Agent Farm Mindset directly fixes a documented, named system failure (S97-99 First-Action Failure audit). Productivity Filter addresses a hypothetical future decision. When two practices tie in score, the one fixing a confirmed failure outranks the one preventing a hypothetical one.
- **Execution risk:** LOW (no setup, one question before each task).

---

### Not in 90-day plan (5 practices + reason):

| Practice | Score | Reason deferred |
|----------|-------|-----------------|
| #3 Mission-as-Code KPIs | 10/12 | Requires 2h to build KPI snippet library; blocked until post-Kulusiirto bandwidth available. High leverage but setup cost too high for DL-week. Start in April. |
| #4 Experimentation Loop | 6/12 | CRM Wave 3A blocked on Frendy OAuth2 until 2026-06-19. No foundation to experiment on. Lowest composite score — defer. Pure Tier 3 (v1.1 correction). |
| #6 Replace Review/Policy | 9/12 | Wave 3A prerequisite (Supabase trust score + OPA). Cannot build before Wave 2B unblocks. Architecturally dependent on stack foundation that doesn't exist yet. |
| #7 Sovereignty-First | 10/12 | **Already DONE** (Anthropic Teams DPA, Supabase EU region — MEMORY.md). Minor checklist formalization can happen in 30 min at any time. No urgency. |
| #8 Productivity Filter | 11/12 | Ties #2/#3 in composite score but is displaced because (a) already partially implemented via attributed_value_eur and (b) fires only on tool-add decisions — no new tools being evaluated this quarter. Formalization deferred to April. |

---

## APPENDIX: Execution Risk Assessment (Internal Judge)

> "Patrick opens this at 8am Monday. Would he actually execute Tier 1 imperatives before 9am?"

**Practice #1 Tier 1 (open CoS Project, paste system prompt):** YES — 5 minutes, clear instruction, one URL (claude.ai), one paste. Execution risk: **LOW for setup, MEDIUM for habit formation.**

**Practice #2 Tier 1 (ask delegation question before task):** YES — zero setup, just a question. Execution risk: **LOW.**

**Practice #5 Tier 1 (apply CEO-only filter):** YES — mental filter, no setup. Execution risk: **LOW.**

**No Tier 1 action has HIGH execution risk.** Wave 3A items correctly placed in Tier 3, not Tier 1.

**One criterion satisfied via lazy completion (self-identified):** Criterion 6 (anti-patterns must cite knowledge file specifically). "Expertise Substitution" anti-pattern uses Section ★, BP5 as citation — this is direct and specific, not lazy. However, the Norders verbatim (Section C) for the CoS anti-pattern was cross-checked against the knowledge file — this IS a specific citation, not a section header. Criterion 6 passes.

**One practice possibly in wrong tier (self-identified):** Practice #8 (Productivity Filter) could be argued as Tier 1 since it's just a mental rule. However, CLAUDE.md already contains the principle implicitly ("Quality over Quantity"), so the DELTA (explicit vendor veto protocol) is minimal — 1h work, not 5 minutes. Tier 2 placement is correct.

---

---

## ⚠️ ONE UNRESOLVED JUDGMENT CALL — Patrick decides

**The Benjamin vs. Lucas conflict on Practice #5 ranking:**

- **Benjamin (math):** #5 scores 12/12 and is correctly ranked #1 — it fires on every task, multiplies elite CEO skills, requires zero infrastructure.
- **Lucas (real-world):** Mental filters are unmeasurable and collapse under deadline pressure. MIT 95% pilot failure rate applies to habit-based practices too. #5 should be Tier 2 with a 30-day trial before claiming #1 rank.

**What this means for you:** Both are right. The matrix ranking (#5 = 12/12) is mathematically correct. Lucas's concern is that the ranking implies #5 is the highest-priority practice to track — but it's the hardest to verify you're actually doing. If you don't log "I almost formatted this table manually but spawned instead," you won't know if it's working.

**Patrick's decision:** Pick one:
- A) Trust the matrix — treat #5 as your highest-priority practice, run it alongside #1 and #2, no special tracking needed. (Benjamin wins.)
- B) Demote #5 to "background filter" — don't track it separately, focus measurement on #1 (CoS opens/week) and #2 (delegation question fired Y/N). If #5 is working, you'll see it in session logs indirectly. (Lucas wins — pragmatically.)

No document change needed. This is a CEO judgment call about how much you want to track behavioral habits vs. trust them.

---

*End of document. Version 1.2 | Grok Round 1 + Round 2 validated 2026-03-20 (CONDITIONAL GO — 2 rounds stable) | Save to Zone B pending Patrick's approval.*
