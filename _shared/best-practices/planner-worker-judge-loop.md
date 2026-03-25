# Planner-Worker-Judge Loop

**Type:** Orchestration pattern
**Source:** Session 73, 2026-03-13 (validated on CRM BUILD-STATE.md + consistency check task)
**Grok validation:** Session 77, 2026-03-16 — Heavy 4-agent council (Harper/Benjamin/Lucas). "Emerging practitioner reality, not theory." Evidence scarce for pure knowledge work (Lucas). No large academic studies. Closest cases: Zac Harris content machine, Fujitsu 67% time savings on sales proposals (cited by Harper, NOT verified by real tools — treat as directional).
**Grok validation 2:** Session 78, 2026-03-16 — fresh window, real tools fired. Harper: exhaustive search including LinkedIn, X/@alasaarela, full podcast transcript. Benjamin: code_execution Monte Carlo (10K sims). Production examples found: Rany ElHousieny CWIC Flow (Clearwater Analytics — Researcher→Critic→Writer, iterative loops); Kizen Critic Agent for strategic plans; Eugene Yan LLM-evaluators guide. Pattern IS documented in non-code knowledge work, but still no published production throughput/accuracy numbers for strategy/CRM deliverables.
**Gemini Deep Research validation:** Session 78, 2026-03-17 — confirmed Epistemic Closure diagnosis, added confidence-based routing (>98%/85-97%/<85% routing mechanism), confirmed n=50 power ~0.35-0.45 (Benjamin's "definitive proof" claim was overstated), added Pre-Mortem as internal-only Epistemic Closure fix.
**Grok session 82 + Gemini cross-validation:** 2026-03-17 — Grok Heavy 4-agent (Harper/Benjamin/Lucas) raw research on judge/evaluator best practices 2025-2026. Gemini synthesis. Verdict: Architectural separation MANDATORY for non-trivial tasks (10-25% self-preference inflation verified, ~5pp false PASS on marginals, shared blind spots Z). Tier 1 Gate exception confirmed. Task-tier iteration caps introduced (replaces flat "max 3"). Initializer Asking Mode: 4 human-pause triggers documented. 4 Operating Rules added.
**Grok session 83 + Gemini thinking cross-validation:** 2026-03-17 — 5 design decisions finalized for /pwj skill. (1) Mission-criticality cap (3–12, set by Planner) replaces tier-based caps — Judge uses judgment to stop early within range. (2) Tag-based LESSONS (single file, grep-filtered) replaces tier-split files — avoids false dichotomy + context poisoning. (3) State Delta check replaces hash check for Silent Drift (5th Initializer trigger). (4) Divorce Rule reclassified as recommended opt-in for Tier-2/3 — Persona Shifting as default layer-1 defense. (5) Gemini's Debugging Paradox + Optimistic Hallucination = confirmed risk of unmaintained auto-loop; mitigated by Judge judgment stop + mission-criticality cap.
**Status:** Tier B — promoted to Tier A after 3 confirmed uses (1 confirmed: session 73)
**Attribution:** Do NOT attribute to Mikko Alasaarela. Harper (Grok session 78) verified exhaustively — his public work contains zero mention of worker/judge/harsh-judge/initializer patterns. His documented claims are "200IQ thinking" + custom Neo4j agent platform. The broader pattern (Researcher→Critic→Writer) is documented by Rany ElHousieny (CWIC Flow, Clearwater Analytics) and Eugene Yan — cite those instead.

---

## What It Is

A 3-role agentic loop for producing and verifying deliverables without constant human oversight:

1. **Planner (Lead):** Defines the task + explicit acceptance criteria + spawns Worker
2. **Worker (subagent):** Executes the task, reads all required files, produces the deliverable
3. **Judge (Lead):** Checks Worker output against acceptance criteria — approves or rejects (max 3 rounds)

The Lead plays both Planner and Judge. The Worker is a subagent with fresh context.

---

## Two Judge Modes

**Mode 1 — Gate Judge (current default):**
- PASS when all acceptance criteria met. Stop on first clean round.
- Use for: code, migrations, consistency checks, any deliverable with a clear binary done state.

**Mode 2 — Improvement Judge (planning, research, reasoning):**
- PASS when marginal improvement falls below a threshold — not when "perfect."
- Judge always asks: "Would a domain expert say this is as thorough as the source material allows? Is the plan actually going to achieve the stated goal?"
- If no → REJECT with the specific gap. If yes → PASS.
- Iteration cap set by Planner based on mission criticality — see **Mission-Criticality Iteration Cap** section below. Default: `max_iter: 5` (standard). Stopping condition = diminishing returns (Judge judgment), NOT hitting the cap.
- **Why "keep disapproving if it keeps getting better" needs a ceiling:** Without a delta threshold, the Judge runs to max rounds on every task, burning cost without convergence. The right stopping signal is "this round's improvement was smaller than the cost of another round" — not "I found nothing to improve."

| Task Type | Judge Mode | Judge asks |
|-----------|-----------|-----------|
| Code / migrations | Gate | All criteria PASS? Binary. |
| Consistency check | Gate | All cross-references correct? Binary. |
| **Plan review** | Improvement | Does this plan actually achieve the stated goal? Missing steps/dependencies? |
| **Research synthesis** | Improvement | Is any major angle uncovered? Would an expert call this incomplete? |
| **Reasoning trace** | Improvement | Are all assumptions named? Any unjustified logic step? |
| **Strategy brief** | Improvement | Contradicts any source doc? Missing the main counter-argument? |
| **"Is this thorough enough?"** | Improvement | What would need to be true for this to be materially better? |

---

## Mission-Criticality Iteration Cap

**Source:** Patrick decision, session 83, 2026-03-17. Replaces task-tier iteration caps (Grok session 82). Motivation: tier-based caps were rigid; mission criticality is a better axis because a Tier-1 code task can be high-stakes (production SQL migration) and a Tier-2 research task can be low-stakes (exploratory draft).

**How it works:**
- Planner sets `max_iter` at spawn based on mission criticality of the specific task (not its type)
- Judge uses judgment to stop early within the range: "Would another round produce material improvement?" If no → STOP and explain why. Cap is the **ceiling**, not the target.
- Judge must state its stopping signal explicitly each round: either "continuing — gap is [X]" or "stopping early — marginal gain below cost of next round."

| Mission Criticality | Example | `max_iter` |
|---------------------|---------|-----------|
| **Routine** | Formatting, draft brainstorm, routine research | 3 |
| **Standard** | CRM deliverables, B2B proposals, session summaries | 5 |
| **High-stakes** | Client relationship decisions, strategy pivots, financial synthesis | 8 |
| **Critical** | Legal analysis, multi-year contracts, irreversible architectural decisions | 12 |

**Default for 1-operator systems:** `max_iter: 5` (standard). Override at spawn with explicit justification if higher.

**"Logic Refresh" — ShopForge Evolve Pattern (fires when cap is hit without PASS):**
When Judge reaches `max_iter` without PASS: don't retry same prompt.
1. Collect the Judge failure trace (exact FAIL criterion + evidence quoted)
2. Append to `_shared/best-practices/pwj-lessons.md` with task tags (see LESSONS File Pattern section)
3. Planner re-inits with: lessons file grep-filtered for matching tags + backtrack to last successful step + rewritten acceptance criterion
4. If Planner cannot rewrite the criterion without human input → trigger Initializer Asking Mode (Step 1b trigger #1: Ambiguity)

Source: ShopForge (Etsy production, Bryce Watson 2026) — Metacognition/Evolve layer; AOI cloud ops (2025). Both document failure trace → LESSONS append → trajectory re-plan, NOT same-prompt retry.

---

## When to Use

- Producing a deliverable from multiple source files (synthesis tasks)
- Verifying consistency across a complex document set
- Any task where "did it actually work?" can be tested against specific conditions
- Tasks that benefit from a fresh-context reader (catches stale assumptions)
- **Planning tasks:** Is this plan complete? Does it actually achieve the goal?
- **Research tasks:** Is this thorough enough? Are there key angles not covered?
- **Reasoning tasks:** Is the logic sound? Are the assumptions named?

## When NOT to Use

- Single-file edits (just use Edit tool directly)
- Tasks needing live credentials or external API access (Worker can't auth)
- ~~Pure research without a clear deliverable~~ ← UPDATED: use Improvement Judge mode instead

---

## The Pattern

### Step 1 — Initializer defines acceptance criteria (BEFORE spawning)

Write 5-8 specific, verifiable conditions the output must satisfy. Binary PASS/FAIL only — no 1-5 scales.

**Always include a Judgment Flag criterion (mandatory):**
> "If legal nuance, stakeholder politics, or unquantifiable taste appears — FLAG FOR HUMAN REVIEW and do not auto-pass."

This lets the loop auto-approve mechanical passes and only surface items that genuinely need human judgment.

**Good criteria:**
- "All 5 Wave 0 gates listed with status symbols ✅/🔄/❌/🔴"
- "Gate 2 marked BLOCKED with KC1 constraint detail"
- "A consistency check section lists any gaps found"

**Bad criteria:**
- "Should be complete and accurate"
- "Must be good quality"

**Lucas's kill shot (Grok session 77):** If Initializer criteria design takes 10–15 min per novel task, the loop does NOT save net time. Fix: build reusable criteria templates per deliverable type. Once templates exist, Initializer drops to 2–3 min. Template creation is the real unlock — do this before running the loop at scale.

**Counterintuitive finding (Grok session 78, Q5):** The primary value of the loop is criteria articulation, not Judge harshness. Writing verifiable rubrics forces precision the human Initializer would otherwise skip — this alone raises output quality before any iteration happens. The judge round is secondary. Implication: if the loop consistently produces better outputs even when Judge PASSes every round, the rubric discipline is doing the work.

**Criteria template starter (works for most knowledge deliverables):**
1. Completeness: [specific sections or elements that must be present]
2. Cross-file consistency: [specific cross-references that must be correct]
3. Strategic alignment: [which source doc defines the goal — output must not contradict it]
4. No unsubstantiated claims: Quote exact text from source files for every factual claim, or say "source not found"
5. Tone/stakeholder fit: [audience — e.g. "written for Patrick, not a staff member"]
6. Judgment Flag: If legal, political, or taste judgment required → FLAG, do not auto-pass

**Rubric Library — 4 production-validated dimensions (ResearchRubrics 2025 + Microsoft LLM-Rubric):**
Use these as the base dimensions for Improvement Judge rubrics on B2B knowledge work. Add/remove per task. Force JSON output + CoT on each (Microsoft LLM-Rubric reduces RMS error <0.5 vs. improvised rubrics).

| Dimension | Binary PASS/FAIL test | Use for |
|-----------|----------------------|---------|
| **Evidence faithfulness** | Every strategic claim traces to a specific source quote. No claim without grounding. | Research synthesis, strategy briefs, CRM proposals |
| **Logical consistency** | No two claims contradict each other. If tension exists, it's named and resolved explicitly. | Plans, reasoning traces, decision documents |
| **Actionability** | Output contains at least [N] specific next actions with owner and timeframe. Generic advice = FAIL. | Strategy briefs, plans, research outputs |
| **Tone/stakeholder fit** | Output is written for [specific audience]. Test: would [person] need to translate this before using it? | Client-facing, staff-facing, Patrick-only |

**Anti-judge-hallucination pattern:** Include 1-2 "failure examples" in each rubric criterion. E.g. for Evidence faithfulness: "FAIL example: 'AHI Travel is our largest client' without citing source." Few-shot failure examples reduce judge hallucination on rubric application (ResearchRubrics 2025 finding).

### Step 1b — Initializer Asking Mode (run before spawning)

**Source:** Grok session 82 + Gemini synthesis, 2026-03-17. Production: medical/strategic agent systems pause before spawn on these triggers.

Before spawning the Worker, check all 5 triggers. If ANY fires → pause and ask the human before proceeding.

| # | Trigger | Symptom | Ask |
|---|---------|---------|-----|
| **1. Ambiguity** | Criteria lack a "ground truth" or are subjective ("sound professional", "be thorough") | Can't write a binary PASS/FAIL criterion | "Define success in one sentence: what would a domain expert say makes this DONE?" |
| **2. Novelty** | Task falls outside any existing KB template or past example | Novel domain not covered by current acceptance criteria templates | "This is outside our templates — do you have a specific quality bar or example I should match?" |
| **3. Conflict** | Two acceptance criteria pull in opposite directions (speed vs. accuracy, completeness vs. conciseness) | Can't optimize both simultaneously | "These two criteria conflict — which takes priority: [A] or [B]?" |
| **4. Max-Retry Alert** | Loop has hit mission-criticality cap without passing | Judge keeps FAILing same criterion | Surface the specific FAIL with evidence and ask: "Should I accept this output as-is, rewrite the criterion, or try a different approach?" |
| **5. Silent Drift** | Source files in Worker reading list have changed since acceptance criteria were written | `git diff` or `stat` on reading list shows changes >10 lines or touches a protected file | "Source files updated since criteria were set — confirm criteria still apply, or rewrite?" |

**Silent Drift detection (practical):** Before spawning, run `stat -f "%m %N"` (macOS) or `git diff --stat HEAD` on the Worker's reading list. If any file shows mtime newer than criteria-writing time AND delta >10 lines → trigger. Single-line changes (comments, whitespace) are ignored. Protected files (e.g. DECISIONS.md, CLAUDE.md) trigger on ANY change.

**When NOT to pause:** If all 5 triggers are clear, spawn immediately — don't ask for permission when the task is well-defined. Asking mode = safety valve, not default mode.

**Cost justification for Initializer pause:** One clarifying question before spawn saves 1-3 full iteration rounds (cost: near-zero; savings: $0.40-$1.20 per loop + quality impact).

---

### Step 2 — Worker spawn prompt structure

```
You are a Worker agent in a Planner-Worker-Judge loop.
Task: [one sentence]

Files to read (read ALL before writing):
1. [path] — [why needed]
2. [path] — [why needed]
...

Output: Write to [exact file path]

Acceptance criteria (the Judge will check these):
1. [specific verifiable condition]
2. [specific verifiable condition]
...

[any extra instructions — consistency checks, format requirements]
```

### Step 3 — Judge evaluation

For each acceptance criterion: PASS / FAIL (binary — no PARTIAL)
**Mandatory for FAIL:** Quote exact evidence ("Worker wrote X; correct is Y") — no vague critique.
**For Judgment Flags:** Do NOT evaluate. Surface to human immediately with context.

For additional findings not in criteria:
- REAL — fix it
- WORKER ERROR — Worker misread; verify before acting
- REJECT — confirmed incorrect claim

**Judge discipline rules:**
1. Never act on a HIGH-severity finding without independently verifying it
2. "File not found" claims need glob verification — the file may exist
3. "Spec mismatch" claims need source document comparison — context matters
4. If Worker accuracy < 50%, flag as KC in project progress file
5. Judge is NOT the primary bottleneck — if output is garbage, check whether Initializer criteria were vague (Grok session 77, Lucas)

**Benjamin cost model (real code_execution, Grok session 78, 10K Monte Carlo sims):**
- p_catch range: **0.70 (knowledge work realism) → 0.95 (code/eval optimistic)** — source: Meta DevAI Agent-as-Judge benchmark via Grok. No published p_catch for strategy/CRM deliverables — 0.70 is the honest knowledge-work estimate.
- p=0.95, 2 errors: expected 1.11 rounds, P(≤3)=100%
- p=0.70, 3 errors: expected 2.02 rounds, P(≤3)=92.1%
- Budget at $0.40/iteration: <$0.90 even with false positives
- Default cap: `max_iter: 5` (standard). See Mission-Criticality Iteration Cap section. If not passing by cap, trigger Logic Refresh — do not retry same prompt.
- **⚠️ k factor discrepancy unresolved:** Prior session uses 6.50× at p=0.70; Grok session 78 new model gives 4.6× (k=4.55). Different baseline reference. Do NOT update sensitivity table until resolved.
- **n=50 power caveat (Gemini session 78):** Power analysis at n=50 = ~0.35-0.45. Gemini's "definitive proof" claim was overstated. N=50 audits are directional signal, not statistical proof. Requires n>200 for adequate power on B2B quality detection.

---

## Lessons from Session 73 Test Run

**Task:** Produce BUILD-STATE.md + consistency check across 7 CRM orchestration files

**Worker accuracy:** 2/6 real findings (33%)

| Finding | Verdict | Lesson |
|---------|---------|--------|
| CONSISTENCY-1: FINNCONCIERGE-CODEBASE-MAP.md missing | ✅ REAL | File didn't exist — valid |
| CONSISTENCY-2: Wave 2B spawn prompt missing | ❌ WORKER ERROR | File exists at line 422 |
| CONSISTENCY-3: No Wave 0 in QUALITY-GATES.md | ✅ REAL | Real gap — fixed |
| CONSISTENCY-4: D39-D42 missing from DECISIONS.md | ❌ WORKER ERROR | Gap is intentional (like D34-D35) |
| CONSISTENCY-5: bulk-embed wave mismatch (HIGH) | ❌ REJECT | Misread wave sequencing |
| CONSISTENCY-6: Wave 4B spawn prompt missing | ❌ WORKER ERROR | File exists at line 885 |

**Key insight:** Same-model Workers confuse "this file will be created later" with "this file is missing." A file manifest (list of expected files per wave) prevents false positives.

**Worker was still valuable:** BUILD-STATE.md produced correctly. 2 real gaps found that would have blocked Wave 1A and 2A agents. Worth running despite 33% accuracy.

---

## Autowork Upgrade (Grok session 77 consensus)

The loop's natural evolution is **Autowork**: auto-approve mechanical PASS criteria, surface only Judgment Flags + FAILs. Human review becomes a 5-min triage, not a full read.

Implementation:
1. Tag every criterion as `[MECHANICAL]` or `[JUDGMENT]` in the Initializer step
2. Judge auto-approves all `[MECHANICAL]` PASSes — no human needed
3. Judge surfaces all `[JUDGMENT]` items + all FAILs for human 5-min review
4. Goal: 80–90% of criteria auto-approved; human time only where irreplaceable

Not yet tested — design from Grok council R3. Test before promoting to default.

---

## Epistemic Closure — Root Diagnosis and Fix

**Root cause (Lucas, Grok session 77-78; confirmed Gemini session 78):** The PWJ loop optimizes for internal coherence only. It has zero mechanism for external reality correspondence on subjective B2B tasks. A synthesis can pass ALL criteria and still be globally wrong — because the criteria only measure consistency within the document set, not correspondence with the market/client reality outside it.

**The "criteria primacy" caveat:** Grok session 78 claimed "criteria articulation is the primary value driver." arXiv Agent-as-a-Judge survey (Jan 2026) contradicts this for subjective tasks — plain rubric judges are insufficient; tool-augmented judges are the actual reliability driver. **Do not treat critera articulation as a full fix for Epistemic Closure.** It prevents mechanical errors. It does not prevent "coherent-but-wrong" synthesis.

**Fix for internal document synthesis (no external APIs):**
1. **Pre-Mortem step (mandatory on Tier 2/3 synthesis):** Before finalizing output, Worker must generate "why this synthesis might be wrong" — alternative explanations, data that contradicts the conclusion, scenarios where the recommendation fails. This forces engagement with alternative hypotheses the original documents might not contain.
2. **Explicit falsifiers rule:** Every strategic claim must name the specific evidence that would change the conclusion. Claims without falsifiers are rejected by Judge (not debated).
3. **Scale-Coherence check:** Insight must survive translation across zoom levels. If a finding holds at company level but contradicts portfolio-level constraints, it's an artifact of framing.
4. **Reflexive gate:** If the system's internal coherence is outrunning fresh external data (no new inputs in N rounds), Judge triggers automatic escalation — do not iterate further.

**What this does NOT fix:** Global misalignment with external market reality (competitor moves, regulatory changes, client relationship signals). For that, tool-augmented judge or periodic external data injection is required.

---

## Confidence-Based Routing

**Source:** Gemini Deep Research, session 78. Enables "Human-above-the-Loop" — maximizes autonomous stretches while ensuring human review where it matters.

| Agent Confidence | Action | Human Role |
|-----------------|--------|-----------|
| >98% | Execute autonomously | Audits retrospectively (weekly batch) |
| 85-97% | Route to Approval Queue; continue parallel work | Clears queue once/day (~30 min) |
| <85% | Resign: surface "can't proceed + what data is missing" | Decides whether to unblock |

**How to add to spawn prompts:** Include a "CONFIDENCE SELF-ASSESSMENT" block. Agent must output: `confidence: [0-100]` and `routing: [autonomous / approval_queue / resign]` at the end of every deliverable. If <85%, the deliverable is NOT written — only a resignation note.

---

## 4 Operating Rules (Grok session 82 + Gemini synthesis — universalized spec)

These four rules consolidate the cross-validated findings into enforceable system defaults. Copy into spawn prompts for Judge agents.

**Rule 1 — The Divorce Rule (Recommended for Tier-2/3):**
Self-preference bias is real (10-25% inflation, ~5pp false PASS on marginals — Snorkel/arXiv). The bias is minimized by structured binary PASS/FAIL criteria even with same-model Judge. Cross-family Judge is the quality upgrade, not the baseline requirement.

**Layer 1 (default — always apply):** Use a "Red Team" system prompt for the Judge regardless of model family. Example: *"You are a cynical senior architect who defaults to NO. Find three specific ways this output will fail before considering PASS. Do not mirror the Worker's framing."* This alone reduces same-model self-preference significantly.

**Layer 2 (recommended for Standard/High-stakes/Critical tasks):** Cross-family Judge. Claude Worker + Grok Judge (free tier) OR Claude Worker + Gemini Judge (free tier) = $0 marginal cost. 6–10s round-trip latency is the real cost — acceptable for `max_iter: 5+`, friction for `max_iter: 3`. Documented pairings: Digits (accounting B2B) and Ramp (financial agents) both deploy cross-family in 2025 production.

**Layer 1 only (same-model permitted) when ALL 4 conditions apply — Hamel 2026:**
1. Criteria type = binary PASS/FAIL only (no subjective dimensions)
2. Human calibration run on held-out set (TPR/TNR ≥ 0.92)
3. Judge task distinctly different from generate task at prompt level
4. Task is Routine (`max_iter: 3`) or low-stakes

**Tier 1 Gate Exception (unchanged):** Same-model evaluation always permitted for syntax validation, formatting checks, binary safety filters, SQL structure checks — objective truth, self-preference cannot change the result.

**Rule 2 — Binary-First Rule:**
All Judge rubrics must start with a Tier 1 Gate check (binary PASS/FAIL: format correct? safety check passed? structure complete?) before applying Tier 2 nuanced scoring. Gate checks block the nuanced round if they fail. Never skip straight to judgment-level review.

**Rule 3 — Mission-Criticality Circuit Breaker:**
Planner sets `max_iter` at spawn (3/5/8/12 per mission-criticality table). Judge stops early when marginal gain < cost of next round — must state stopping signal explicitly. Hitting `max_iter` without PASS → Logic Refresh (ShopForge pattern), NOT same-prompt retry. See Mission-Criticality Iteration Cap section for full table.

**Rule 4 — Confidence Floor:**
Any Judge output with confidence <80% — or characterized by "judge uncertainty" (criteria don't cleanly apply, novel domain, conflicting source documents) — must trigger Initializer Asking Mode (Step 1b) instead of proceeding to the next iteration. Judge uncertainty is not a reason to try again; it's a reason to ask the human.

---

## Anti-Patterns

**Anti-pattern 1: Vague acceptance criteria**
"The output should be complete" → Judge can't verify this. Requires specific conditions.

**Anti-pattern 2: Trusting HIGH-severity findings without verification**
Worker labeled CONSISTENCY-5 HIGH. It was a misread. HIGH labels from Workers need extra scrutiny, not automatic action.

**Anti-pattern 3: Worker checking file existence without a manifest**
Workers will call files "missing" if they don't appear in the source files they're reading, even if the files exist. Fix: include a file manifest in key spawn prompts.

**Anti-pattern 4: Treating Worker accuracy as binary**
33% accuracy on consistency findings ≠ failure. The BUILD-STATE.md was produced correctly. Separate the quality of the deliverable from the quality of the meta-analysis.

**Anti-pattern 5: Rubric gaming (no monitoring layer)**
Workers learn to satisfice rubric style — mirroring the Judge's verbosity preferences, padding structure, checking boxes — rather than producing genuine quality. Deliverables drift toward judge-pleasing instead of stakeholder value. In a 5-person no-DevOps team this goes undetected. Fix: occasionally compare a loop output directly against the underlying goal (not just the rubric). If a document passes all criteria but feels wrong to a human reader, the criteria have drifted. Source: Lucas challenge + Eugene Yan calibration guide (leniency/verbosity/position bias documented).

**Anti-pattern 7: Same-model self-critique as quality gate**
Using the same model as both Worker and Judge degrades performance on high-quality outputs — Snorkel/arXiv research (cited by Lucas, Grok session 82) shows same-model review can degrade from 98%→57% accuracy. Grok session 82 + Gemini synthesis (2026-03-17) confirmed via Harper/Benjamin/Lucas: self-preference bias 10-25% inflation (Benjamin sim: ~5pp false PASS on marginals), shared blind spots Z (zero additional signal on correlated errors), position/verbosity/perplexity bias, 57.2pt accuracy collapse on novel prompts (safety judges). CourtEval/ChatEval 2025: multi-agent (different families) +10-16% human correlation vs. single-model judge.

**The Divorce Rule (updated session 83 — Recommended, not Mandatory for Tier-2/3):** Self-preference bias is real but structured PASS/FAIL criteria + Red Team system prompt is the accessible first-line fix. Cross-family Judge is the upgrade path, not the baseline requirement. Solo-operator friction (6-10s latency, two auth flows) kills adoption if made mandatory. See Rule 1 for full layered approach.

**Tier 1 Gate Exception (unchanged):** Same-model always permitted for syntax, formatting, binary safety filters — objective truth, bias cannot change the result.

Fix priority order: (1) Red Team system prompt on Judge (always), (2) structured binary PASS/FAIL criteria (always), (3) cross-family Judge for Standard/High-stakes/Critical tasks (recommended). Source: Lucas challenge Grok session 82; Gemini thinking session 83.

**Anti-pattern 6: No long-tail failure detection**
B2B errors surface months after execution — a wrong strategy brief damages a 10-year client relationship long after the PWJ round closed. Weekly spot-checks catch execution errors. Monthly retrospectives catch pattern failures (systematic bias across multiple outputs). Quarterly catches architectural drift. Fix: treat "passed PWJ" as a start state, not an end state. Schedule monthly retrospective audits of all autonomous writes. Source: Gemini Deep Research, session 78.

---

## LESSONS File Pattern — Self-Improvement Mechanism

**Source:** ShopForge (Etsy production, Bryce Watson 2026) + AOI cloud ops (2025). Grok session 82 Q1+Q5. Updated session 83: tag-based architecture replaces tier-split files (Gemini thinking validation).

**What it is:** A persistent log of Judge failure traces that feeds back into the loop via tag-based grep-filtering. Zero additional API cost — it's a file write. Every failure is a synthetic training example for the next spawn prompt.

**Architecture:** Single file `_shared/best-practices/pwj-lessons.md` with task tags. Planner grep-filters to matching tags before spawning — only loads relevant lessons, not the full file. Avoids context window poisoning and false dichotomy of tier-split files. No manual cleanup needed.

**Entry format per failure:**
```
## [date] Task: [one-sentence task description]
Tags: #[domain] #[task-type] #[output-type]  ← used for grep-filtering
Criticality: [routine/standard/high-stakes/critical] | Iterations: [N] | Outcome: [PASS/FAIL/ESCALATED]
FAIL criterion: [exact criterion text that failed]
Evidence: [Judge's exact quote of what went wrong]
Root cause: [Ambiguity / Novelty / Conflict / Worker Error / Criteria drift / Silent Drift]
Fix applied: [Criteria rewrite / Human input / Logic Refresh / Accepted as-is]
---
```

**Tag examples:** `#crm #strategy-brief #b2b-proposal` | `#sql-migration #code #schema` | `#research-synthesis #market-analysis`

**How it feeds back:**
1. **Next spawn prompt** — Planner grep-filters pwj-lessons.md for matching tags, includes 3 most recent FAIL examples as few-shot anti-examples in Judge rubric
2. **Logic Refresh (at cap)** — Planner re-inits with tag-filtered lessons + backtrack to last successful step + rewritten criterion
3. **Skill update** — After 5+ tagged entries in a domain: review patterns → update rubric templates

**Noise protection (Gemini + Grok session 83):** Strategic tasks produce noisy failure data. Monthly Patrick review — archive entries that produced bad regenerations. Planner must NOT auto-inject lessons without verifying the fix was confirmed by a human (check `Fix applied` field — "Accepted as-is" entries are lowest confidence).

---

## File Manifest Pattern (prevents false "file missing" claims)

Add to spawn prompts for agents doing consistency checks:

```
KNOWN FILES MANIFEST — these files exist and are expected:
- FINNCONCIERGE-CODEBASE-MAP.md (created Wave 0)
- BUILD-STATE.md (created Wave 0, in FinnConcierge repo)
- WAVE-BUILD-AGENTS.md waves: 0, 1A, 1B, 2A, 2B, 3A, 3B, 4A, 4B, 5 (all 10 exist)
Do not flag these as missing. Only flag files that SHOULD exist per spec but DO NOT.
```

---

## Cost Reference

- BUILD-STATE.md test run: ~$0.10-0.15 (subagent, 7 file reads + 1 write)
- FINNCONCIERGE codebase map: ~$0.30-0.40 (Explore subagent, 36 tool uses)
- Total loop cost for this session: ~$0.50
