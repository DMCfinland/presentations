# Finland DMC 2.0 — Strategic Synthesis Orchestration (Feb 22 v2)
## Agent Team Analysis: What Are We Actually Building?

**Purpose:** A Claude Code agent team with 7 specialist teammates analyses Finland DMC 2.0 from distinct perspectives. Teammates communicate directly with each other at key decision points. The team lead synthesizes all outputs into the Finland DMC 2.0 Goal Document.

**When to run:** Tell Claude Code: *"Create an agent team for Finland DMC 2.0 synthesis. Use this orchestration prompt."* Claude Code acts as team lead, spawns 7 specialist teammates, and coordinates via a shared task list.

**Output location:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/`

**Terminal mode:**
- **tmux (recommended for 7 teammates):** `tmux new -s dmc-team`, launch `claude` inside it. Each teammate gets its own pane.
- **In-process (VS Code fallback):** Use Shift+Down to cycle. VS Code integrated terminal does NOT support split-pane.
- Before running: set `"teammateMode": "tmux"` in `~/.claude/settings.json` if using standalone terminal.

**Model:** Sonnet for all Wave 1–2 teammates. Opus 4.6 for Wave 3 synthesis only (see Execution Guide for switch mechanism).

---

## ⚠️ CRITICAL UPDATES — ALL AGENTS READ BEFORE STARTING
**(Copy this entire section + Context for All Agents + Six Products verbatim into every spawn prompt.)**

### 1. B2B Architecture Decision (A5) — PARTIALLY RESOLVED
`Finland_DMC_PRD_v3.docx` (February 9, 2026) chose **Claude Teams only** for **Second Brain (Product 1)**. No custom infrastructure for Second Brain. **Email Drafter (Product 2) is a separate question:** PRD v3 simplified Second Brain's architecture, but Email Drafter's n8n/Supabase stack predates this decision and may be unaffected. **Agent 2 must clarify whether PRD v3 covers Email Drafter or only Second Brain.** Agent 1 and Agent 5 must evaluate what Claude Teams only means for Second Brain specifically.

### 2. Travel Assistant Codebase — SHELVED DRAFT
A working mock codebase **FinnConcierge** exists at `/Users/patrickheiskanen/Desktop/FinnConcierge/`. Built December 2025 with Cursor + Opus 3.5/4.0. Phase 1 complete (5 agents in mock mode, no real Azure, LLM stubbed). Stopped before Phase 2. **Treat as informational, not binding.** Redesign from first principles with Opus 4.6.

### 3. Files Available (all paths relative to FinlandDMCOy-AIFiles/)
- `project-files/b2b-tools-feb2026/` — PRD v3, Architecture Guide, Build Task List (Feb 2026)
- `project-files/travel-assistant/finnconcierge-reference/` — shelved codebase docs
- `finland-dmc-2.0/research/traveltree-api-status.md` — TT API facts (T1/T2/T3 **RESOLVED** — cite this, don't speculate)
- `project-files/dmc-2.0-strategic-synthesis/distilled/` — Lead's pre-distilled summaries (written in Wave 0)

### 4. Patrick's Explicit Decisions (2026-02-21) — All Agents Must Honor These

**A. PRD v3 (Claude Teams only for Second Brain):** PROVISIONAL — agents may challenge if evidence supports a different approach.

**B. Staff capacity:** One Finland DMC staff member dedicates meaningful part-time daily hours to monitoring AI guest conversations and handling escalations. Real cost. Factor into build sequence.

**C. Järvisydän IT:** NO contact with Järvisydän IT yet. Agents 3 and 4 must flag what conversations, evaluations, and legal agreements must happen BEFORE Travel Assistant build begins.

**D. Revenue model — THE KEY BUSINESS INSIGHT:**
> Finland DMC earns **15% commission on ALL bookings**, regardless of channel. The goal is not to build a better DMC — it is to become an OTA-class volume operator while keeping DMC quality and local knowledge.

### 5. Build Methodology (TA-A4) — RESOLVED
Standard 4-5 role pattern (PM-Initializer, Orchestrator, Sub-Boss, Coder, Tester) confirmed at 1/3 the cost of tournament/Darwinian models. Google/MIT (Dec 2025): >45% single-agent accuracy → adding more agents yields negative returns. 79% of multi-agent failures = spec/coordination. **Do NOT reopen this question.**

---

## WHAT MAKES THIS ANALYSIS CORRECT

A good output from this team must:
- [ ] Every architecture recommendation backed by a specific file reference (name + section)
- [ ] Every "confirmed" decision traceable to a source doc with date
- [ ] Every "open" question lists exactly 2 options with explicit trade-offs
- [ ] B2B/B2C data boundary drawn with GDPR article references, not vibes
- [ ] Build sequence justified by dependencies, not preferences
- [ ] North Star metric is quantifiable (not "better" — how much better, measured how?)
- [ ] Every agent's "Top 3 Questions" either answered in synthesis or escalated to Patrick
- [ ] Travel Tree API capability must cite `traveltree-api-status.md` — no speculation

A bad output: hedges on architecture without making a call; proposes a build sequence ignoring Järvisydän IT dependency; ignores the commission model in build prioritization; speculates about TT API when the answer file exists.

---

## Context for All Agents

Finland DMC Oy is a 5-person B2B destination management company (Helsinki). ~600 emails/month, every proposal written from scratch, no institutional memory. Patrick Heiskanen (CEO, 1658 Holdings Oy) is building an AI-native version of the company.

### THE MISSION

**Finland DMC is currently 100% B2B.** The end goal: fully automated B2C AI travel platform. The transition model: AI handles 80–90% of guest interactions automatically. Finland DMC humans serve as safety net, problem solvers, and interim bookers for the remaining 10–20%.

- Staff are being **repositioned**, not replaced (manual operators → quality control + exception handlers)
- **Staff Dashboard (Product 3)** is the central transition product
- **Järvisydän is the first live deployment** — not a test
- **North Star: "Finland DMC becomes the easiest, cheapest, fastest way to book Finland — fully automated, infinitely scalable"**

Six products in design or development:
1. **Second Brain** — Staff knowledge capture and relationship intelligence (B2B, transition period)
2. **Email Drafter** — AI proposal/email generation for staff (B2B, transition period)
3. **Staff Dashboard** — Monitor AI guest interactions, intervene when needed (key transition product)
4. **TT Itinerary Drafter** — AI-generated Travel Tree itineraries (reduces manual booking effort)
5. **Finland Travel Assistant** — B2C guest-facing AI concierge, multi-tenant Azure platform
6. **Järvisydän Travel Assistant** — First live deployment of Product 5

**Zone 1 (B2B):** Products 1-4, Finland DMC staff, client/contact PII (GDPR-sensitive), temporary.
**Zone 2 (B2C):** Products 5-6, end guests, behavior/mood data, EU-stored, anonymized, permanent.

Critical design question: **How do you build Zone 1 (transition) and Zone 2 (end-state) simultaneously without Zone 1 creating technical debt that blocks Zone 2?**

---

## The Six Products — Brief Reference

### Product 1: Second Brain
Staff knowledge capture → classified, stored as client profiles, interaction history, relationship health scores, weekly digests, A4 briefing sheets. **PRD v3 (Feb 9, 2026):** Simplified to Claude Teams Projects + M365 connector. Agent 1 must evaluate whether this meets original requirements.

### Product 2: Email Drafter
Staff selects customer + product + brief notes → AI produces complete personalized proposal using historical best lines, Second Brain client context, Travel Tree product data. **Stack (pre-PRD v3):** n8n (self-hosted, Hetzner VPS) + Supabase + Claude API. **Agent 2 must determine: does PRD v3 apply to Email Drafter stack too?**

### Product 3: Staff Dashboard
Key transition product. Traffic Light prioritization, Whisper Mode, Takeover, God Mode, FIRE RED, Safety Net bot-restore. Intervention rate declining week-over-week = transition success metric. Designed as part of Travel Assistant spec (BP_08). **Stack:** Part of Travel Assistant Azure infrastructure.

### Product 4: TT Itinerary Drafter
Travel Tree Pro (€75/month). AI auto-generates/pre-populates TT itineraries. **⚠️ TT API questions T1/T2/T3 are RESOLVED — read `finland-dmc-2.0/research/traveltree-api-status.md`. Do NOT speculate.**

### Product 5: Finland Travel Assistant (FinnConcierge)
B2C PWA via Magic Link. Multi-tenant "Chameleon" architecture. Agent network: Master Agent, Mood Evaluator, Suggestion Chef, Booking Agent, Shadow Ledger. **Stack:** Azure Functions (Python/Node.js), Azure Event Grid, Azure OpenAI GPT-4o (ZDR), Cosmos DB, Azure SQL, Azure AI Search, Data Lake Gen2, Next.js PWA.

### Product 6: Järvisydän Travel Assistant
First tenant of Product 5. Brown/gold theme, "Savolainen Isäntä" persona, Finnish/English. Järvisydän and Finland DMC are **different companies**. Finland DMC = platform owner; Järvisydän = first client.

---

## CONTEXT BUDGET — 200K CLIFF

**Rule:** When total input tokens in a single API call exceed 200K, ALL tokens cost 2x (all-or-nothing).

| Model | ≤200K | >200K | Multiplier |
|-------|-------|-------|-----------|
| Sonnet | $3/$15 per MTok | $6/$22.50 | 2x input, 1.5x output |

**Per-teammate estimate formula:**
```
Total = Base (15K) + Spawn (10K) + Σ files(KB × 1.2K) + messages_received(N × 3K)
Danger zone: >180K    Cliff: >200K (doubles ALL input cost)
```

**Designed budgets (post-distillation):**

| Agent | Estimated Input | Status |
|-------|----------------|--------|
| A1 Second Brain | ~103K | ✅ SAFE |
| A2 Email Drafter | ~111K | ✅ SAFE |
| A3 TA Vision | ~85K | ✅ SAFE |
| A4 TA Technical | ~144K | ✅ SAFE |
| A5 Integration | ~90K | ✅ SAFE (via cross-brief) |
| A6 Database | ~140K | ✅ SAFE (via cross-brief) |
| A7 Portfolio | ~65K | ✅ SAFE |

**These budgets depend on:** (a) Wave 0 distillation subagents completing, (b) output files ≤300 lines each for 7-section agents, ≤400 lines for 9-section agents (A4, A5), (c) Agent 4 skipping BLUEPRINTS_1_TO_10.md, (d) Agent 6 reading only specified sections of A4/A5 outputs, (e) Wave 1.75 cross-brief replacing full output reads for A5/A6.

---

## Agent Team Structure

### Inter-Agent Communication Protocol

**Structured message template (for challenges and cross-validation — not simple queries):**
```
To: @AgentX
Subject: [specific topic]

My evidence: [file + section + specific data or quote]
Challenge: [your claim appears to contradict because...]
Implication: [proposed resolution or question for synthesis]
```

**Lock-and-advance rule:** Once a Wave 1 output passes the lead's quality check, it is **LOCKED**. Wave 2 agents may send clarifying questions but **MAY NOT request rewrites**. Disagreements go into the Wave 2 agent's output for the synthesis lead to resolve.

**Agent 1 (Second Brain Analyzer):** After completing Section 4, flag to the lead: "For Agent 5 briefing — 3-bullet summary of data outputs Second Brain would expose to other products: [bullets]."

**Agent 2 (Email Drafter Analyzer):** After completing Section 5, flag to the lead: "For Agent 5 briefing — confirmed Email Drafter stack and any shared infrastructure constraints: [details]." After completing Section 4, flag to the lead: "For Agent 7 briefing — 2-sentence summary of conversion data Email Drafter could contribute: [sentences]."

**Agent 3 (TA Vision Analyzer):** After completing Section 2, flag to the lead: "For Agent 7 briefing — 3-sentence summary of revenue model shift: [sentences]."

**Agent 4 (TA Technical Architect):** After completing Section 2, message Agent 6 directly with full schema list and which Azure service stores each. After completing Section 5, message Agent 5 directly with the API surface area the Travel Assistant exposes.

**Agent 5 (Integration Architect):** May message Agent 1 or Agent 4 for clarifying questions (not rewrites). After reading Agent 1's output: **Challenge — "Your Section 4 says Second Brain exposes [X]. My integration design needs [Y]. If there's a gap, I'm flagging it in my Section 2."** After completing your draft, message Agent 6: "The B2B/B2C data boundary I've drawn is [description]. Consistent with your infrastructure plans?"

**Agent 6 (Database Architect):** After reading Agent 4's schema list: **Challenge — "Schema [X] stored in [service Y] — does this conflict with GDPR Article [N] data residency requirements? I'm noting the conflict in my Section 2 if so."** May message Agent 4 to confirm Azure region choices. After completing recommended architecture, message lead: "Recommendation: [Option A/B/C] because [one sentence]."

**Agent 7 (Portfolio Strategist, adversarial framing):** For every major recommendation from the 6 specialists, identify the strongest counter-argument before accepting it. You are a skeptic, not a summarizer. Does NOT send a live broadcast. The lead pre-collects transition model concerns during Wave 2.5. You receive them in your spawn prompt.

**All agents:** If you discover something contradicting another agent's likely conclusion, message them a proactive flag immediately.

### Task Wave System

```
WAVE 0 — LEAD LAUNCHES TWO DISTILLATION SUBAGENTS (parallel Task tool calls):
  DISTILL-A subagent (Sonnet): Reads 3 Second Brain system files (228KB total)
                                Writes distilled/second-brain-system-summary.md (~15KB)
  DISTILL-B subagent (Sonnet): Reads proposals-2024/SECOND-BRAIN/ folder (156KB)
                                Writes distilled/proposals-data-summary.md (~10KB)

  NOTE: Each subagent starts with FRESH context. They will cross the 200K cliff
  individually (~$1.60 each) but that cost is isolated. The lead's own context
  stays clean. Wave 0 total: ~$3.50 for both subagents.

WAVE 1 (spawn all 4 in a single message — start in parallel):
  Task A1: Second Brain Analyzer         → agent-1-second-brain.md
  Task A2: Email Drafter Analyzer        → agent-2-email-drafter.md
  Task A3: TA Vision Analyzer            → agent-3-travel-assistant-vision.md
  Task A4: TA Technical Architect        → agent-4-travel-assistant-technical.md

WAVE 1.5 — LEAD QUALITY CHECK:
  Lead scans all 4 outputs for:
    - Every section has specific content (no TBD, no placeholders)
    - Sections cite specific file sections, not just file names
    - Trade-offs state 2+ options, not "X is best" without evidence
    - Top 3 Questions are genuinely unresolved
    - No contradiction with CRITICAL UPDATES
    - Check self-check line at bottom of each output
  If any fail: message teammate → specific feedback → wait for revision → unblock
  Lead runs /compact AFTER quality check, BEFORE spawning Wave 2a.

WAVE 1.75 — LEAD LIGHT CROSS-BRIEF (after /compact):
  Lead creates distilled/wave1-cross-brief.md (~8-12KB):
    - 3-bullet key conclusions from each Wave 1 agent
    - All briefing flags received (A1 Section 4, A2 Sections 4+5, A3 Section 2)
    - Self-check highlights + assumptions validated per agent
    - Conflicts or tensions identified across Wave 1 outputs
    - Explicit "quality gate passed" confirmation per agent
  This replaces full-output reads for downstream agents (~30-35K savings each).
  Lead runs /compact AFTER writing cross-brief.

WAVE 2a — Agent 5 only (depends on A1, A4 via cross-brief):
  Task A5: Integration Architect         → agent-5-integration-architect.md
           Pre-work: read distilled/wave1-cross-brief.md →
           deep-read specific A1/A4 sections only if needed → plan approval → write.

WAVE 2.5a — Agent 5 quality check:
  Lead checks Agent 5 output against quality criteria.
  Lead runs /compact after quality check.

WAVE 2b — Agent 6 only (depends on A4, A5 via cross-brief):
  Task A6: Database Architect            → agent-6-database-infrastructure.md
           Pre-work: read distilled/wave1-cross-brief.md +
           read A4/A5 sections as specified → plan approval → write.

WAVE 2.5b — Lead Cross-Agent Briefing (all 6 outputs now available):
  Lead reads all 6 outputs (scan for key conclusions and conflicts).
  Asks each teammate: "2-sentence biggest concern about the transition model?"
  Writes distilled/cross-agent-briefing.md (~15KB).
  Lead runs /compact after writing briefing.

WAVE 2c — Agent 7 (depends on cross-agent briefing):
  Task A7: Portfolio Strategist          → agent-7-portfolio-strategist.md
           Pre-work: read cross-agent-briefing.md → plan approval → write.

WAVE 3 — Lead synthesis (after all 7 complete):
  Lead runs /compact BEFORE reading output files.
  Reads all 7 outputs. Writes GOAL-DOCUMENT-finland-dmc-2.0.md.
  Use Opus 4.6 (see Execution Guide for model switch).
```

---

## Wave 0: Distillation Subagents

**Lead spawns these as two parallel Task subagents (not Agent Team teammates). Each starts with fresh context.**

### DISTILL-A Subagent Prompt (Sonnet)

```
Read these 3 files in order:
1. /Users/patrickheiskanen/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/
   project-files/second-brain-system/opus-m365-architecture-design.md (84KB)
2. project-files/second-brain-system/opus-build-execution-plan.md (68KB)
3. project-files/second-brain-system/opus-swot-and-build-optimization.md (76KB)

Write a compressed summary (target 15KB) to:
project-files/dmc-2.0-strategic-synthesis/distilled/second-brain-system-summary.md

Include only: architectural decisions made, key design choices (with file source),
open questions left unresolved, what changed across versions, SWOT conclusions.
No prose sections — extract decisions and conclusions only. Write markdown directly.
```

### DISTILL-B Subagent Prompt (Sonnet)

```
Read all files in:
/Users/patrickheiskanen/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/
finland-dmc-2.0/mining-outputs/proposals-2024/SECOND-BRAIN/

Write a compressed summary (target 10KB) to:
project-files/dmc-2.0-strategic-synthesis/distilled/proposals-data-summary.md

Include: data structure, key client/revenue patterns, what data exists, quality
assessment, gaps identified. This represents what real Second Brain data looks like.
Write markdown directly.
```

---

## Wave 1: Four Independent Specialists

**Spawn all 4 in a single message to maximize parallelism. Output constraint: 250–350 lines for 7-section agents (A1, A2, A3), 300–400 lines for 9-section agents (A4).**

**All agents:** Write markdown directly — no scripts, no summaries of what you're about to write. Self-check at the end of your output (see "Done when" per agent below).

---

### AGENT 1 — Second Brain Analyzer

**Model:** Sonnet

**Role:** Deeply understand what Second Brain was designed to be, then analyze its role in the Finland DMC 2.0 ecosystem.

**NOT your job:** Don't analyze Email Drafter or Travel Assistant in detail. Don't recommend specific GDPR solutions — flag the obligation and leave the ruling to synthesis. Don't re-analyze PRD v3 architecture choice (just evaluate whether the simplification is correct).

**CORRECTNESS CRITERIA:**
- Every architecture claim cites specific file + section
- Every "confirmed" decision references source doc with date
- Every "open" question lists exactly 2 options with trade-offs
- If data is missing, say "data not found in [file]" — don't guess

**Done when:** Every section has specific content (no TBD). Section 2 lists specific data entities (names, not categories). Section 7 makes a clear recommendation on PRD v3 simplification. Section 8 lists 3 genuinely open questions.

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
[N] file references with section citations. [N] trade-offs with dual options.
Top 3 Questions are [genuinely blocking / rhetorical].
Assumptions validated: [list key assumptions checked against files, e.g., "PRD v3 scope confirmed in Section X"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**Read these files (in order):**
1. `FinlandDMCOy-AIFiles/project-files/b2b-tools-feb2026/finland-dmc-prd-v3.txt` (40KB) ← PRIMARY
2. `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/distilled/second-brain-system-summary.md` (~15KB) ← DISTILLED from 3 system files
3. `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/distilled/proposals-data-summary.md` (~10KB) ← DISTILLED from real Second Brain data

**⚠️ Context budget:** ~103K estimated. Do not read additional files.

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-1-second-brain.md`

**Communication:** After completing Section 4, flag to the lead (the lead will include this in Agent 5's spawn prompt): "3-bullet summary of data outputs Second Brain would expose to other products."

**Write these sections:**

```
## Second Brain — Analysis

### 1. What It Is (in plain language)
One paragraph. What does Second Brain do for a Finland DMC staff member on a typical Tuesday?

### 2. Data It Produces
List every data entity: what is it, who owns it, how often updated, how long retained.
Ground in proposals-data-summary evidence. Use specific entity names, not categories.

### 3. Data It Needs (from other products)
What information from Email Drafter / Travel Assistant / TT would make Second Brain smarter?

### 4. What It Gives to Other Products
What data/intelligence should Email Drafter query? What should Staff Dashboard display?
What (if anything) flows to Travel Assistant?

### 5. Infrastructure — What's Decided vs Open
What is confirmed (stack, GDPR region, data classification)? What is still unresolved?
Cite which file said what, with section reference.

### 6. GDPR Analysis
B2B personal data. What GDPR obligations apply? What data classification tier?
What retention/deletion rules are explicit? Cite GDPR Articles.

### 7. Architecture Simplification — Verdict on PRD v3
PRD v3 chose Claude Teams Projects over a custom M365 stack for Second Brain.
What capabilities does the simpler approach LOSE? What does it GAIN?
Make a clear call: is the simplification correct given the OTA-scale goal? (No hedging.)

### 8. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

### AGENT 2 — Email Drafter Analyzer

**Model:** Sonnet

**Role:** Understand what Email Drafter was designed to be, then analyze its role in the Finland DMC 2.0 ecosystem. **Critical question to resolve: Does PRD v3 (Claude Teams only for Second Brain) apply to Email Drafter's n8n/Supabase stack, or does Email Drafter keep its own infrastructure?**

**NOT your job:** Don't analyze Second Brain architecture. Don't write actual email templates. Don't evaluate B2C products. Focus on Email Drafter only.

**CORRECTNESS CRITERIA:**
- Section 5 must reach a verdict on the PRD v3 question (not leave it open)
- Stack decisions must cite PRD v3 or EMAIL-DRAFTER-DESIGN.md specifically
- Integration dependencies must be specific (field names, not "client data")

**Done when:** Section 5 delivers a clear verdict on whether n8n/Supabase stack is confirmed, revised, or replaced by PRD v3. Section 7 makes a clear call on Supabase sharing feasibility. Section 8 lists 3 genuinely open questions.

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
[N] file references with section citations. [N] trade-offs with dual options.
PRD v3 verdict on stack: [confirmed n8n / replaced by Claude Teams / still open — requires Patrick decision].
Assumptions validated: [list, e.g., "PRD v3 scope for Email Drafter checked in Section X"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**Read these files (in order):**
1. `FinlandDMCOy-AIFiles/project-files/b2b-tools-feb2026/finland-dmc-prd-v3.txt` (40KB) ← CHECK FIRST for Email Drafter stack decision
2. `FinlandDMCOy-AIFiles/project-files/email-drafter/EMAIL-DRAFTER-DESIGN.md` (44KB)
3. `FinlandDMCOy-AIFiles/finland-dmc-2.0/mining-outputs/session-1-client-comms-outbound/EMAIL-DRAFTER/patterns-identified.md` (8KB)
4. `FinlandDMCOy-AIFiles/finland-dmc-2.0/mining-outputs/session-1-client-comms-outbound/EMAIL-DRAFTER/best-lines.md` (8KB)
5. `FinlandDMCOy-AIFiles/finland-dmc-2.0/mining-outputs/session-2-inbound-emails/EMAIL-DRAFTER/patterns-identified.md` (8KB)

**⚠️ Context budget:** ~120K estimated. Do not read additional files.

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-2-email-drafter.md`

**Communication:**
- After completing Section 5, flag to the lead: "For Agent 5 spawn — confirmed Email Drafter stack: [stack details and open questions]."
- After completing Section 4, flag to the lead: "For Agent 7 briefing — conversion/send signal data Email Drafter could contribute: [2 sentences]."

**Write these sections:**

```
## Email Drafter — Analysis

### 1. What It Is (in plain language)
One paragraph. What does Email Drafter do for a Finland DMC staff member writing a proposal?

### 2. Data It Produces
What data does Email Drafter generate? Drafts, sent confirmations, feedback signals,
conversion outcomes? What gets stored and where?

### 3. Data It Needs
From Second Brain (client history), from TT (product info), from Travel Assistant
(returning guest preferences)? Be specific — which fields, which calls.

### 4. What It Gives to Other Products
Does a sent email provide useful signal for Second Brain? For the Travel Assistant?
For future drafts?

### 5. Infrastructure — Stack Verdict and PRD v3 Question
This is the critical section. Does PRD v3 (Claude Teams only for B2B) override the
n8n/Supabase stack? State your finding as one of:
  A. PRD v3 replaces n8n/Supabase — Email Drafter also runs on Claude Teams
  B. PRD v3 applies to Second Brain only — Email Drafter keeps n8n/Supabase
  C. Open — requires Patrick to decide (explain what's missing from the files)
Cite evidence from PRD v3 and EMAIL-DRAFTER-DESIGN.md.

### 6. GDPR Analysis
B2B client data in draft content. What classification applies? Any difference from
Second Brain's obligations?

### 7. Shared Infrastructure Compatibility
What would it take for Second Brain to share the Supabase instance? Schema conflicts?
Isolation requirements? Clear call: feasible or not?

### 8. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

### AGENT 3 — TA Vision Analyzer

**Model:** Sonnet

**Role:** Understand the B2C vision, business model, and relationship to Finland DMC's B2B business.

**NOT your job:** Don't evaluate technical feasibility — that's Agent 4. Don't write marketing copy. Don't assess B2B products in detail. Focus on the B2C vision and business model only.

**CORRECTNESS CRITERIA:**
- Revenue model shift must be quantified (15% × volume, not just "more scale")
- Järvisydän pre-go-live requirements must be specific non-technical items
- GDPR analysis must cite Article numbers, not just "compliant"

**Done when:** Section 2 explains the OTA-scale commission model clearly. Section 6 lists specific pre-go-live requirements (not technology). Section 8 lists 3 genuinely open questions.

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
[N] file references with section citations. Revenue model: quantified or not.
GDPR citations: [N] Article references.
Assumptions validated: [list, e.g., "commission model confirmed in cluster-a Section X"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**Read these files (in order):**
1. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/cluster-a-vision-findings.md` (12KB)
2. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/cluster-c-devbrief-findings.md` (20KB)
3. `FinlandDMCOy-AIFiles/project-files/PRD-v0.1.md` — **Sections 1–3 and Section 16 only** (48KB total — read specified sections only)

**⚠️ Context budget:** ~85K estimated. PRD-v0.1.md is 48KB — read specified sections only.

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-3-travel-assistant-vision.md`

**Communication:** After completing Section 2, flag to the lead: "For Agent 7 briefing — 3-sentence revenue model shift summary: [sentences]."

**Write these sections:**

```
## Travel Assistant — Vision Analysis

### 1. What It Is (in plain language)
One paragraph. What does a Järvisydän guest experience from Magic Link receipt to end of holiday?

### 2. Why This Is a Different Business Model
15% commission × OTA-scale volume vs 15% × ~100 group bookings/year. Who are the real
customers? What changes in the business when volume goes from 100 → 10,000 bookings/year?

### 3. Relationship to Finland DMC B2B Tools
Where do B2B and B2C worlds intersect? Where must they stay separate?

### 4. Data the Travel Assistant Produces
What does this corpus become at scale? What is its commercial value beyond booking commissions?

### 5. What B2B Products Could Learn From Travel Assistant Data
What's allowed vs. what's a GDPR violation? Cite Article numbers.

### 6. The Järvisydän Deployment — Pre-Go-Live Requirements
What does Järvisydän need before go-live that isn't about technology?
(Content, legal agreements, IT integration with Oracle Opera, staff training?)

### 7. The "Chameleon" / White-Label Model
If this becomes a platform licensed to multiple resorts and OTAs, what does that mean
for Finland DMC's identity and revenue model?

### 8. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

### AGENT 4 — TA Technical Architect

**Model:** Sonnet

**Role:** Understand the full Azure stack, agent network, data schemas, and integration requirements. Treat FinnConcierge (shelved Dec 2025 codebase) as informational only.

**NOT your job:** Don't reopen the tournament/Darwinian build methodology — it's resolved (Critical Update #5). Don't write code. Don't recommend B2B product changes.

**CORRECTNESS CRITERIA:**
- Section 1 explicitly flags each tech choice as "confirmed" vs "mentioned"
- Section 2 lists every schema with its Azure service (table format)
- Section 8 references coding-project-preflight.md Section 1 for team composition

**Done when:** Section 1 distinguishes confirmed vs mentioned. Section 2 lists all schemas with Azure services. Section 5 lists Järvisydän IT technical prerequisites (Oracle Opera integration, network access, data feeds) as critical path blockers. Section 8 references build methodology. Section 9 lists 3 genuinely open questions.

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
[N] tech choices classified confirmed/mentioned. [N] schemas listed with Azure service.
Context budget: BLUEPRINTS [read/skipped]. Coding preflight: [read Section 1 only].
Assumptions validated: [list, e.g., "Azure region confirmed in cluster-b Section X"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**⚠️ CONTEXT BUDGET: ~144K without BLUEPRINTS. Read files in order. After reading file 6 (preflight), check: if context is at 130K+, SKIP file 7 entirely.**

**Read these files (in order):**
1. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/monster-compressed.md` (40KB)
2. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/cluster-b-technical-findings.md` (12KB)
3. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/cluster-e-monster-findings.md` (16KB)
4. `FinlandDMCOy-AIFiles/project-files/travel-assistant/finnconcierge-reference/FINAL_CHECKLIST.md` (16KB)
5. `FinlandDMCOy-AIFiles/project-files/travel-assistant/finnconcierge-reference/MASTER_MAP.md` (8KB)
6. `_shared/best-practices/coding-project-preflight.md` — **Section 1 only (~3KB — stop after team composition section)** ⚠️ This file is at the HOLDINGS ROOT, not inside FinlandDMCOy-AIFiles/
7. `FinlandDMCOy-AIFiles/project-files/travel-assistant/finnconcierge-reference/BLUEPRINTS_1_TO_10.md` (72KB) — **SKIP IF CONTEXT IS AT 130K+ AFTER FILE 6**

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-4-travel-assistant-technical.md`

**Communication:**
- After completing Section 2, message Agent 6 directly with full schema list and which Azure service stores each.
- After completing Section 5, message Agent 5 directly with the API surface area the Travel Assistant exposes.

**Write these sections:**

```
## Travel Assistant — Technical Analysis

### 1. Confirmed Tech Stack
List every technology choice. Column 1: tech. Column 2: role. Column 3: confirmed or mentioned (with source).

### 2. Data Schemas Defined
Table: Schema name | Contents (key fields) | Azure service storing it.

### 3. Agent Network Architecture
Master Agent, Mood Evaluator, Suggestion Chef, Booking Agent, Shadow Ledger —
what does each do, what data does each read/write, how do they communicate?

### 4. GDPR and EU Data Residency
North Europe vs Sweden Central — which is chosen and why? What is ZDR?
What gets anonymized and when? Cite Azure documentation where available.

### 5. Integration APIs and External Dependencies
What APIs does the Travel Assistant expose? What does it need from external systems?
Specific endpoints or webhook patterns where documented.
**Critical:** What must Järvisydän IT provide (Oracle Opera API access, network connectivity,
data feeds, legal agreements) BEFORE Travel Assistant build can begin? Flag as critical path blockers.

### 6. Shared Infrastructure — B2B vs B2C
Can Supabase/n8n (B2B) and Azure (B2C) share anything? If yes: what, at what cost, with what GDPR risk?

### 7. Build Status — What Was Built and Why It Stopped
What Phase 1 of FinnConcierge achieved, the 3 real blockers that stopped it,
and what that tells us about Phase 2 complexity.

### 8. Redesign With Opus 4.6
Which architectural choices would you reconsider? What was over-engineered for Dec 2025
model capabilities? Reference team composition from coding-project-preflight.md Section 1.
Note: tournament/Darwinian model is RESOLVED — do not reopen.

### 9. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

## Wave 2a: Agent 5 (after Wave 1.5 quality check)

*Blocked until Wave 1.5 passes. Spawn after lead runs /compact following quality check.*

---

### AGENT 5 — Integration Architect

**Model:** Sonnet

**Role:** Map how all 6 products connect — data flows, APIs, events, shared state, integration seams.

**NOT your job:** Don't design the databases — that's Agent 6. Don't evaluate individual product quality. Don't redesign B2B or B2C products. Don't speculate about TT API capability — cite traveltree-api-status.md.

**CORRECTNESS CRITERIA:**
- Section 1 must have a complete diagram with every arrow labeled (data, direction, frequency)
- Section 3 must cite traveltree-api-status.md with specific T1/T2/T3 findings
- Section 4 must use GDPR Article citations for every legal statement

**Done when:** Section 1 has complete labeled diagram. Section 3 cites traveltree-api-status.md. Section 4 draws the B2B/B2C boundary with GDPR Article citations. Section 8 makes one clear recommendation (no hedging).

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
Integration diagram: [complete / missing arrows].
TT API citation: [cited traveltree-api-status.md / speculated].
GDPR Articles cited: [N].
Challenge flagged vs Agent 1: [gap found / no gap].
Assumptions validated: [list, e.g., "TT API T1/T2/T3 confirmed via status file"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**Pre-work (do before writing):**
1. Read `project-files/dmc-2.0-strategic-synthesis/distilled/wave1-cross-brief.md` (~10KB) — your PRIMARY context for Wave 1 findings
2. Read the context Agent 1 and Agent 4 sent the lead (included in your spawn prompt)
3. If cross-brief raises questions needing deeper verification: read specific sections of agent-1-second-brain.md (Sections 2, 3, 4 only) or agent-4-travel-assistant-technical.md (Sections 2, 5, 6 only)
4. **Cross-validation challenge:** Compare what Agent 1 says Second Brain exposes (Section 4) against what your integration design needs. If there's a gap, flag it explicitly in your Section 2.
5. Message Agent 1: "Confirm: does Second Brain expose a query API for client history, or is data access manual?"
6. Check Agent 4's message about Travel Assistant APIs — incorporate.
7. Check Agent 2's stack note included in your spawn prompt.
8. Send lead your 5-bullet plan. Wait for approval.

**Then read:**
1. `FinlandDMCOy-AIFiles/project-files/b2b-tools-feb2026/finland-dmc-prd-v3.txt` (40KB) ← PRIMARY
2. `FinlandDMCOy-AIFiles/finland-dmc-2.0/research/traveltree-api-status.md` (4KB) ← cite, don't speculate

**⚠️ Context budget:** ~90K estimated (via cross-brief instead of full A1/A4 outputs). Do NOT read PRD-v0.1.md or PRD-v0.2-changeset.md — PRD v3 is current and sufficient.

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-5-integration-architect.md`

**Communication:** After completing your draft, message Agent 6: "B2B/B2C data boundary I've drawn: [description]. Consistent with your infrastructure plans?"

**Output constraint: 300–400 lines.**

**Write these sections:**

```
## Integration Architecture Analysis

### 1. The Integration Map (text diagram)
Plain-text diagram: all 6 products as boxes, all data flows as labeled arrows.
Label each arrow: what data flows | direction (push/pull) | estimated frequency.

### 2. The Six Integration Seams — Detailed
For each connection: what flows, who produces, who consumes, push vs pull, blocking vs nice-to-have.
Flag any gaps between what Second Brain exposes and what integration requires.

### 3. Travel Tree as the Central Dependency
Cite traveltree-api-status.md for T1/T2/T3 answers. Given TT's actual API capabilities,
what happens to all three dependent products?

### 4. The B2B / B2C Data Boundary
Where exactly does B2B data end and B2C data begin? What can legally cross it? What cannot?
GDPR Article citations required. No vibes.

### 5. Architecture Decisions Still Blocking Integration
Every open decision blocking a specific integration — what it blocks and why.

### 6. The Minimum Viable Integration
Simplest possible integration for all 6 products. What is manual vs automated?

### 7. PRD v3 Simplification Impact
Claude Teams Projects for B2B: what does this mean for integration? Does Claude Teams
have outbound webhook/API capability? Or does B2B/B2C become a clean manual handoff?

### 8. Recommended Integration Backbone
One recommendation. What single integration layer serves as the nervous system?

### 9. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

## Wave 2b: Agent 6 (after Agent 5 quality check)

*Blocked until Agent 5 output passes quality check and lead runs /compact.*

---

### AGENT 6 — Database Architect

**Model:** Sonnet

**Role:** Design the shared data architecture for all 6 products — which databases, who owns what, GDPR separation, EU compliance.

**NOT your job:** Don't redesign the products — only the data layer. Don't make business model recommendations. Don't reopen settled Azure region choices without new evidence from the files.

**CORRECTNESS CRITERIA:**
- Section 3 must be a table with every data entity, its storage location, and GDPR legal basis
- Section 4 must present all 3 options with specific cost estimates (not just "higher/lower")
- Section 6 must make a clear recommendation (not "it depends")

**Done when:** Section 3 is a complete data residency table. Section 4 presents 3 options with cost/risk/complexity. Section 6 makes a clear recommendation. Section 7 lists 3 genuinely open questions.

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
Data residency table: [N] entities mapped. GDPR Articles cited: [N].
Recommendation: [Option A / B / C].
Challenge vs Agent 4: [GDPR conflict found / no conflict].
Assumptions validated: [list, e.g., "Azure region choice confirmed in A4 Section 4"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**Pre-work (do before writing):**
1. Read `project-files/dmc-2.0-strategic-synthesis/distilled/wave1-cross-brief.md` (~10KB) — Wave 1 findings summary
2. Check Agent 4's schema message included in your spawn prompt.
3. Check Agent 5's boundary message.
4. If cross-brief raises questions needing deeper verification: read agent-4-travel-assistant-technical.md Sections 1, 2, 4 only
5. Read `project-files/dmc-2.0-strategic-synthesis/agent-5-integration-architect.md`
   **— Sections 1, 4 only** (Agent 5's output needed for GDPR boundary alignment)
6. **Cross-validation challenge:** For each schema Agent 4 listed, check: is the storage service consistent with GDPR data residency for that data type? Flag any conflict explicitly in your Section 2.
7. Message Agent 4: "What Azure region is confirmed for Cosmos DB and Azure SQL?"
8. Message Agent 5: "Is your B2B/B2C boundary consistent with separating Supabase (B2B) from Azure (B2C) entirely?"
9. Send lead your 5-bullet plan. Wait for approval.

**Then read:**
1. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/cluster-b-technical-findings.md` (12KB — TECH CHOICES section)
2. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/monster-compressed.md` (40KB — Appendix/database schemas section only)
3. `FinlandDMCOy-AIFiles/project-files/PRD-v0.1.md` — **Sections 9, 10, 11 only** (48KB total — specified sections only)

**⚠️ Context budget:** ~140K estimated (via cross-brief for A4). If A5 output file is >350 lines, read only the specified sections as noted in pre-work. Do not read additional files.

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-6-database-infrastructure.md`

**Communication:** After completing your recommended architecture, message the lead: "Recommendation: [Option A/B/C] because [one sentence]."

**Write these sections:**

```
## Database and Infrastructure Analysis

### 1. Current Database Decisions — What's Chosen
Every confirmed database/storage choice across all products. Flag conflicts or ambiguity.

### 2. The Core GDPR Problem
B2B (CRM-class PII) vs B2C (guest behavior, mood profiles, booking data).
Different retention rules, consent frameworks, breach notification timelines.
Can they share a database? What does the law require? Cite GDPR Articles.
Flag any schema conflicts identified from Agent 4's list.

### 3. EU Data Residency Map
Table: data entity | storage location | GDPR legal sufficiency (EEA/adequate/SCC needed) | ZDR coverage.

### 4. Three Infrastructure Options
Option A: Fully Separate — B2B on M365/Supabase, B2C on Azure.
Option B: Unified Azure — everything to Azure.
Option C: Federated — B2B on Supabase (Zone 1), B2C on Azure (Zone 2), shared product catalog.

For each: cost estimate (€/month), GDPR risk, migration effort, operational complexity.

### 5. B2C Guest Data Anonymization Strategy
What must be anonymized? When? What can be retained for analytics?
Schema-level enforcement mechanisms.

### 6. Recommended Architecture
One clear recommendation. No hedging. Cite the decisive reason.

### 7. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

## Wave 2.5b: Lead Cross-Agent Briefing

*Run after Agent 6 output passes quality check. Before spawning Agent 7.*

**Lead scans all 6 output files** (focus on self-check lines and Top 3 Questions sections — don't deep-read)

**Lead writes** `project-files/dmc-2.0-strategic-synthesis/distilled/cross-agent-briefing.md` (~15KB):

```
Include per agent:
- Their Section 8/9 "Top 3 Questions" (verbatim)
- Their single most important recommendation or conclusion (1 sentence)
- Any cross-validation challenges they flagged (from self-check lines)

Plus:
- All conflicts identified across agents (list, don't resolve)
- Transition model concerns (ask each teammate: "2 sentences — biggest concern
  about humans-as-safety-net"). Embed all 6 responses verbatim.

Target: 15KB. NOT a synthesis — decision-relevant extracts only.
```

After writing: **run `/compact` before spawning Agent 7**.

---

## Wave 2c: Agent 7 (after cross-agent briefing)

---

### AGENT 7 — Portfolio Strategist (Adversarial)

**Model:** Sonnet

**Role:** Step back from all technical detail and answer: what is Finland DMC 2.0, really? What is the unified value proposition? What is the North Star? **Your primary job is skepticism, not summary.** For every major recommendation from the 6 specialists, identify the strongest counter-argument before accepting it. If you can't find a counter-argument, the recommendation is underexplored.

**NOT your job:** Don't replicate what the 6 specialists wrote. Don't write technical specifications. Don't resolve conflicts between agents — list them for Patrick. Don't create marketing materials.

**CORRECTNESS CRITERIA:**
- Section 6 North Star must be a quantifiable metric (not "better" — how much better, measured how?)
- Section 7 must make a clear call: bridge or trap (not "it could go either way")
- For every recommendation you cite from the 6 agents, you must also state its strongest counter-argument

**Done when:** Section 2 tells a coherent flywheel story an investor would understand. Section 6 defines a specific quantifiable North Star metric. Section 7 makes a clear call on transition model. Section 9 lists 3 genuinely open questions.

**Before marking complete, write a self-check at the end of your output:**
```
Self-check: [N] sections completed. Shortest section is [N] lines.
Counter-arguments: [N] specialist recommendations stress-tested.
North Star metric: [specific and quantifiable / still vague].
Transition model verdict: [bridge / trap / depends — if depends, explain what would make it flip].
Assumptions validated: [list, e.g., "revenue model confirmed in briefing, commission % verified"].
Context load: [light (<100K) / medium (100-160K) / heavy (160K+)].
```

**Pre-work (do before writing):**
1. Read `project-files/dmc-2.0-strategic-synthesis/distilled/cross-agent-briefing.md` — your PRIMARY reading. Contains all 6 agents' key conclusions, Top 3 Questions, cross-validation conflicts, and transition model concerns.
2. Send lead your 5-bullet plan. Wait for approval.

**Then read:**
1. `FinlandDMCOy-AIFiles/project-files/travel-assistant/analysis-outputs/cluster-a-vision-findings.md` (12KB) — vision layer context

**⚠️ Context budget:** ~65K estimated. The cross-agent briefing replaces reading all 6 full output files. Do NOT read the individual agent output files directly.**

**Write to:** `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/agent-7-portfolio-strategist.md`

**Write these sections:**

```
## Product Portfolio Strategy Analysis

### 1. The Core Problem Being Solved
Knowledge loss (Janna left with €633K in accounts), productivity (600 emails/month from scratch),
growth opportunity (B2C AI travel for Finnish resorts doesn't exist at scale).
Are these three separate problems or one unified one?

### 2. The Six Products — A Coherent Story
Tell the story to a sophisticated investor. How do the products reinforce each other? Is there a flywheel?
For each product's role, state the strongest counter-argument for why it might not matter.

### 3. Who Pays for What
Map each product's revenue/cost role. Which products generate revenue and when?
Strongest counter-argument: which product looks like revenue but might be a cost center longer than planned?

### 4. The Sequencing Question
If Patrick can only build ONE product first, which one creates the most durable foundation?
Make a case. Strongest counter-argument: why the obvious choice might be wrong.

### 5. The 1658 Holdings Multiplier
Finland DMC as the pilot for all 10 portfolio companies. What changes in product design
if it becomes the operating system for the whole group?

### 6. The North Star
One paragraph. Three quantifiable success metrics with current → 12-month targets.
(Not "better" — specific numbers: conversion rate, booking volume, intervention rate.)

### 7. The Transition Model — Bridge or Trap?
Draw on the transition model concerns pre-loaded in your spawn prompt.
Make a clear call: bridge or trap. What's the specific trigger that signals
"automation is reliable enough to reduce human oversight"? Name the metric.

### 8. The Biggest Risk — Not Technical
The biggest risk to Finland DMC 2.0 is probably not a database choice. What is it?
Strongest counter-argument: why your answer might be wrong.

### 9. Top 3 Questions for the Synthesis

[Self-check block here]
```

---

## Wave 3: Lead Synthesis

*After all 7 teammate outputs complete. Run `/compact` BEFORE reading output files.*

**Model switch for synthesis:** Before Wave 3, either:
- Run `/model opus` in the lead session, OR
- Spawn synthesis as a Task subagent: `"Spawn a Sonnet agent... no, spawn this with Opus 4.6"` (provides clean context too)

**Read these files:**
1. `project-files/dmc-2.0-strategic-synthesis/agent-1-second-brain.md`
2. `project-files/dmc-2.0-strategic-synthesis/agent-2-email-drafter.md`
3. `project-files/dmc-2.0-strategic-synthesis/agent-3-travel-assistant-vision.md`
4. `project-files/dmc-2.0-strategic-synthesis/agent-4-travel-assistant-technical.md`
5. `project-files/dmc-2.0-strategic-synthesis/agent-5-integration-architect.md`
6. `project-files/dmc-2.0-strategic-synthesis/agent-6-database-infrastructure.md`
7. `project-files/dmc-2.0-strategic-synthesis/agent-7-portfolio-strategist.md`

**Write to:** `project-files/dmc-2.0-strategic-synthesis/GOAL-DOCUMENT-finland-dmc-2.0.md`

**Synthesis mandate — do these 5 things:**
1. **Apply evidence weighting** — when agents disagree, weigh by source quality. An agent citing specific file+section outweighs one making general claims. Example: "Agents 1 and 4 disagree. Agent 4 cites cluster-b Section 2 with specific data. Recommendation: Agent 4's position."
2. **Resolve conflicts** — state both positions AND make an evidence-weighted call (or explicitly escalate to Patrick)
3. **Fill gaps** — if Agent 3 raised a question that Agent 5 answered, connect them
4. **Eliminate redundancy** — 7 agents will repeat the same point; consolidate into 1 strong statement
5. **Elevate the non-obvious** — the most valuable insight is usually buried in one agent's analysis, contradicting the majority view. Surface it.

**Assumption audit:** Before writing Section 7 (Build Sequence), cross-check each agent's key assumptions against the self-check "Assumptions validated" lines. Any unvalidated assumption must be flagged in Section 11.

**Anti-patterns to avoid:** Copy-pasting agent sections without integration. "Agent 1 says X, Agent 2 says Y" without resolution. Dropping questions that don't fit the narrative. Making synthesis shorter but thinner.

**Synthesis sections:**

```
# Finland DMC 2.0 — Goal Document
## Version 0.1 | Synthesized from 7 specialist agents | 2026-02-21

## 0. Correctness Boundaries & Synthesis Methodology
### Synthesis methodology:
- Evidence weighting applied: agent claims with file+section citations outweigh general claims
- All conflicts resolved or explicitly escalated to Patrick
- Assumptions audited across all 7 agents' self-check lines
- Non-obvious insights elevated; redundancy eliminated
### Fatal errors (destroy trust, must never happen):
(populate from agent analyses)
### Acceptable uncertainty (system may express honestly):
(populate from agent analyses)
### Evidence requirements:
- Architecture recommendations cite: [file + section]
- Price/availability claims cite: [source + date]
- B2B/B2C boundary uses: GDPR Article references
- TT API capabilities cite: traveltree-api-status.md only

## 1. What Finland DMC 2.0 Is (Executive Definition)
Three paragraphs max. Non-technical person understands what, for whom, and why. No acronyms.

## 2. The Six Products — Roles and Relationships
For each product: one paragraph on role + one sentence on primary integration dependency.
| Product | Zone | Serves | Produces | Needs From | Owned By |
(fill in the table)

## 3. Shared Data Architecture — Recommendation
Pick ONE from Agent 6's three options. State clearly. Justify in 5 sentences.
Plain-text data flow diagram. GDPR boundary line explicit with Article citations.

## 4. Integration Architecture — The Nervous System
One recommended integration backbone with plain-text diagram. Flag each flow:
- Required Day 1
- Required before Travel Assistant go-live
- Nice-to-have
- Deferred (manual until volume justifies)

## 5. GDPR and EU Compliance — Clear Rules
5 explicit rules (not recommendations):
1. [data type] MUST be stored in [region/service] because [GDPR Article]
...

## 6. Open Architecture Decisions — Resolved vs. Remaining
For each open decision: resolved by synthesis or escalated to Patrick.
If escalated: one clear question, two options, the key trade-off.

## 7. Recommended Build Sequence
| Phase | Product | What Gets Built | Why This Order |
| Phase 0 (Now) | | | |
| Phase 1 (Month 1–2) | | | |
| Phase 2 (Month 2–4) | | | |
| Phase 3 (Month 4–8) | | | |

## 8. The North Star
One paragraph Patrick reads weekly.
Three quantifiable success metrics: current → 12-month targets.

## 9. The Five Biggest Risks (Ranked)
| # | Risk | Probability | Impact | Mitigation |
(5 rows)

## 10. Conflicts and Disagreements Between Agents
List every conflict with both positions. State resolution or escalate.
Do NOT resolve conflicts silently.

## 11. What This Document Does NOT Answer
Every question remaining open. These become the agenda for Patrick's next decision session.
```

---

## Execution Guide

### Pre-Run Checklist

```bash
# Verify settings.json
cat ~/.claude/settings.json | grep -E "model|teammateMode|EXPERIMENTAL"
# Should show: "model": "sonnet", agent teams enabled, teammates mode set

# Create distilled/ directory
mkdir -p /Users/patrickheiskanen/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/distilled/

# Pre-approve permissions (copy to ~/.claude/settings.json before run):
# "Read(*)", "Write(FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/*)",
# "Glob(*)", "Grep(*)", "Edit(FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/*)"
# This eliminates ~35 permission prompts = saves 10-15 min.
```

### How to Start

**Terminal setup:**
```bash
tmux new -s dmc-team
# Update settings.json: "teammateMode": "tmux"
# Then launch claude inside tmux
```

**Tell Claude Code:**
> *"Create an agent team for the Finland DMC 2.0 strategic synthesis. Read the orchestration prompt at `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/ORCHESTRATION-PROMPT.md`. Follow the wave structure defined there. Use Sonnet for all Wave 1-2 teammates. Use Opus 4.6 for Wave 3 synthesis only."*

### What the Lead Does (Step by Step)

**Lead operates in delegate mode (Shift+Tab) throughout.** Coordinate only — do NOT write analysis yourself.

1. `/compact` for fresh context.
2. **Wave 0:** Spawn DISTILL-A and DISTILL-B as two parallel Task subagents (NOT Agent Team teammates). Wait for both to complete.
3. **Wave 1:** Spawn Agents 1, 2, 3, 4 in a **single message** (all 4 in parallel). Each spawn prompt must include full CRITICAL UPDATES + THE MISSION + Six Products context block + agent-specific section.
4. **Wave 1.5:** Scan all 4 outputs using the quality criteria and self-check lines. Message for revisions if needed.
4b. **Wave 1.75:** `/compact`, then write `distilled/wave1-cross-brief.md` (~10KB): 3-bullet conclusions per agent, all briefing flags, key assumptions, conflicts identified. `/compact` again after writing.
5. **Wave 2a:** Spawn Agent 5 with plan approval required. Include A1 and A2 briefing flags in spawn prompt. Review and approve Agent 5's 5-bullet plan before they write.
6. **Wave 2.5a:** Quality check Agent 5 output. `/compact`.
7. **Wave 2b:** Spawn Agent 6 with plan approval required. Include A4 schema message and A5 boundary message in spawn prompt. Review and approve Agent 6's plan.
8. **Wave 2.5b:** After Agent 6 passes quality check — scan all 6 outputs for self-check lines and Top 3 Questions. Ask each teammate for 2-sentence transition concern. Write cross-agent briefing. `/compact`.
9. **Wave 2c:** Spawn Agent 7 with plan approval required. Include briefing + transition concerns in spawn prompt.
10. **Wave 3:** After Agent 7 completes, `/compact`. Switch to Opus (run `/model opus` or spawn as Opus subagent). Read all 7 outputs. Write Goal Document.

### Key Spawn Prompt Elements (every teammate must have ALL of these)

1. Full CRITICAL UPDATES block (copy verbatim)
2. Full THE MISSION + Six Products block (copy verbatim)
3. Agent's specific Role + reading list + write destination + communication protocol
4. Correctness criteria (from the agent's section above)
5. Non-goals and "Done when" criteria
6. Self-check template
7. Model: "Use Sonnet for this task."
8. "Write markdown directly — no scripts, no summaries of what you're about to write."
9. "Write only to your designated output file. Do not modify other agents' files."

### Lead Response Templates (keep short to save context)

```
Quality pass:   "Output approved. Wave 2a unblocked."
Quality fail:   "Section 3 needs depth — add specific schema names from the file. Revise."
Plan approved:  "Plan approved. Proceed."
Plan rejected:  "Assumption 2 is wrong — PRD v3 covers Second Brain only, not Email Drafter. Revise plan."
```

### Error Recovery

**Teammate stopped:** Check output file. Partial? Message: "Continue from Section [N]. Your partial output is saved." File path error? Correct and re-send. Context filled? "Skip [lowest-priority file]. Continue without it."

**Dependency deadlock:** Lead writes a 10-line stub → saves to expected output path → Wave 2 agent reads stub → proceeds. Flag in synthesis: "Section based on lead stub."

**Lead context overflow:** `/compact` immediately. All analysis is in files.

**Agent outputs conflict:** List in Goal Document Section 10. Patrick decides, not the lead.

**After team completion:** `tmux ls` → `tmux kill-session -t dmc-team`. Verify all output files exist.

**Revision budget:** Round 1 revision always worth it. Round 2 only if same section is still shallow. If 3+ sections are weak, the spawn prompt was underspecified — fix the prompt and respawn rather than iterating.

### File Paths (Absolute)

```
Base: /Users/patrickheiskanen/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/

Pre-distilled (Wave 0 / Wave 1.75 / Wave 2.5b):
project-files/dmc-2.0-strategic-synthesis/distilled/
  ├── second-brain-system-summary.md     (~15KB — DISTILL-A)
  ├── proposals-data-summary.md          (~10KB — DISTILL-B)
  ├── wave1-cross-brief.md              (~10KB — Wave 1.75)
  └── cross-agent-briefing.md            (~15KB — Wave 2.5b)

Agent outputs:
project-files/dmc-2.0-strategic-synthesis/
  ├── agent-1-second-brain.md
  ├── agent-2-email-drafter.md
  ├── agent-3-travel-assistant-vision.md
  ├── agent-4-travel-assistant-technical.md
  ├── agent-5-integration-architect.md
  ├── agent-6-database-infrastructure.md
  ├── agent-7-portfolio-strategist.md
  └── GOAL-DOCUMENT-finland-dmc-2.0.md

Source files (sizes):
project-files/b2b-tools-feb2026/
  ├── finland-dmc-prd-v3.txt                (40KB — A1, A2, A5)
  └── finland-dmc-architecture-guide.txt    (44KB — Wave 0 DISTILL-A only)
project-files/second-brain-system/         (Wave 0 DISTILL-A ONLY — not read by agents)
  ├── opus-m365-architecture-design.md      (84KB)
  ├── opus-build-execution-plan.md          (68KB)
  └── opus-swot-and-build-optimization.md  (76KB)
project-files/email-drafter/EMAIL-DRAFTER-DESIGN.md  (44KB — A2)
project-files/PRD-v0.1.md                  (48KB — A3 sections 1-3/16; A6 sections 9-11)
project-files/travel-assistant/
  finnconcierge-reference/
    ├── MASTER_MAP.md                       (8KB — A4)
    ├── FINAL_CHECKLIST.md                  (16KB — A4)
    └── BLUEPRINTS_1_TO_10.md               (72KB — A4 SKIP IF HEAVY)
  analysis-outputs/
    ├── cluster-a-vision-findings.md        (12KB — A3, A7)
    ├── cluster-b-technical-findings.md     (12KB — A4, A6)
    ├── cluster-c-devbrief-findings.md      (20KB — A3)
    ├── cluster-e-monster-findings.md       (16KB — A4)
    └── monster-compressed.md              (40KB — A4, A6 appendix only)
finland-dmc-2.0/
  ├── research/traveltree-api-status.md     (4KB — A5)
  ├── mining-outputs/proposals-2024/SECOND-BRAIN/  (156KB — Wave 0 DISTILL-B only)
  └── mining-outputs/
      session-1.../EMAIL-DRAFTER/
        ├── patterns-identified.md          (8KB — A2)
        ├── best-lines.md                   (8KB — A2)
      session-2.../EMAIL-DRAFTER/
        ├── patterns-identified.md          (8KB — A2)
../../../_shared/best-practices/coding-project-preflight.md   (24KB — A4 Section 1 only — AT HOLDINGS ROOT, not inside FinlandDMCOy-AIFiles/)

SHELVED CODEBASE (do not move or modify):
/Users/patrickheiskanen/Desktop/FinnConcierge/
```

### Cost and Time Estimate

| Component | Cost |
|-----------|------|
| Wave 0: 2 distillation subagents (cross 200K individually) | ~$3.50 |
| Wave 1: 4 specialists × avg $0.80 | ~$3.20 |
| Wave 2a/b/c: 3 specialists × avg $1.00 | ~$3.00 |
| Wave 3: Opus synthesis | ~$3–5 |
| Output tokens (all agents) | ~$4–6 |
| **Total** | **~$17–21 USD** |

**Time:**
- Wave 0 pre-distillation: ~10 min
- Wave 1 parallel: ~25 min (A4 bottleneck)
- Wave 1.5 quality check: ~5 min
- Wave 1.75 cross-brief + /compact: ~5 min
- Wave 2a (A5): ~20 min + 2 min approval
- Wave 2.5a quality check + /compact: ~5 min
- Wave 2b (A6): ~20 min + 2 min approval
- Wave 2.5b briefing + /compact: ~8 min
- Wave 2c (A7): ~15 min + 2 min approval
- /compact + Wave 3 synthesis: ~20 min
- **Total: ~135–150 min**

---

### Post-Run Evaluation

After the synthesis is written but before team cleanup, the lead writes:
`project-files/dmc-2.0-strategic-synthesis/POST-RUN-EVALUATION.md`

Answer these 6 questions:

1. **Quality score (1–5):** Rate the Goal Document against the "WHAT MAKES THIS ANALYSIS CORRECT" checklist at the top of this prompt. Score each criterion, then average.

2. **What the team structure added:** List 2–3 specific insights or connections that ONLY emerged because multiple agents analyzed different sources. Example: "Agent 4's schema list revealed a conflict with Agent 6's GDPR data residency requirement — neither agent reading alone would have caught this." If you can't list at least 2, the task probably didn't need a team.

3. **Communication value:** For each inter-agent message that was sent during the run, state: who sent it, who received it, and whether it changed the recipient's output (yes/no). Messages that changed nothing = wasted context tokens. Recommend which messages to remove from the communication protocol if this prompt is reused.

4. **Quality gate effectiveness:** How many Wave 1 outputs needed revision during Wave 1.5? How many Wave 2 plans were redirected? Were agent self-checks accurate? If zero revisions were needed, flag whether that means agents performed perfectly or the quality gate was too lenient.

5. **Cost-benefit:** Report actual cost vs the $17–21 estimate. Did any agent cross the 200K cliff? Estimate what a single Opus session reading all source files would have cost. Was the team premium justified by the quality score?

6. **Pattern harvest:** What worked well (keep for next orchestrated run), what failed or underperformed (change), what to try next time (experiment).

**Decision framework:** Quality ≥4 + ≥2 unique team insights + ≥50% messages useful = JUSTIFIED. Quality <3 or 0 unique insights = use single agent next time.
