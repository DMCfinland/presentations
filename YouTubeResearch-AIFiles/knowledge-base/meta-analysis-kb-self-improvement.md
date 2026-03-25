# Meta-Analysis: What Our KB Says About Improving Our KB
**Date:** 2026-02-18 | **Source:** knowledge-rag.md (95), prompting-context.md (114), productivity-workflows.md (53)
**Purpose:** Find gaps between what we know and what we practice — use KB to improve KB system.

---

## Executive Summary

After reading all 262 insights across three files, the analysis surfaces four major themes where our own KB gives us better advice than our current system implements:

1. **Retrieval architecture** — we trigger on keywords; the KB says trigger on mode (planning vs. execution), stake level, and task type
2. **Self-improving loops** — our Opus review fires every 10 sessions; the KB describes continuous feedback mechanisms that fire after every task
3. **Context window discipline** — we load warm packs at session start; the KB says default context should contain nearly nothing, and retrieval should be an active agent decision
4. **Measurement** — we count KB activations; the KB describes multi-dimensional quality trajectory metrics that would catch gaming and mediocrity simultaneously

---

## Section 1: What We Are NOT Doing That Our KB Says We Should

### 1.1 Active Retrieval Instead of Passive Loading

**Insight (knowledge-rag.md, Technique):** "Default context should contain nearly nothing. I'm going to say it again because almost no one says this. Default context should contain nearly nothing — because more tokens does not necessarily mean you're going to get more clarity and it often means more distraction."

**Source:** Grab the Inside Scoop on How Google, Anthropic, and Manus Built Long-Running AI Agents

**How it applies:** Our warm packs are loaded at session start as a passive inheritance. Even a 35-line warm pack pins static context that may be irrelevant if the task shifts mid-session. The KB advises stripping defaults to minimal identity and making everything else a retrieval decision.

**Status: NOT DOING THIS.** We load warm packs at session start regardless of whether they match the actual work in that session. A Finland DMC session that pivots to document architecture still has the dmc-mining pack loaded.

**Proposed change:** Load only session identity (company, session number, current task) at start. Keep warm packs queryable. Trigger retrieval when task type becomes clear — not before.

---

### 1.2 Mode-Aware Retrieval (Planning vs. Execution)

**Insight (knowledge-rag.md, Anti Pattern):** "Mode aware context beats volume hands down — large context windows filled with unsorted information are worse than a tightly curated 10,000 token context because planning conversations need breadth while execution needs precision."

**Source:** AI's Memory Wall: Why Compute Grew 60,000x But Memory Only 100x

**How it applies:** Our warm packs are mode-agnostic. The same pack loads whether Patrick is deciding what to mine next (planning — needs breadth) or running a batch job (execution — needs precision constraints). The KB says these require different context shapes.

**Status: NOT DOING THIS.** We have one warm pack per project type. No distinction between planning mode and execution mode context.

**Proposed change:** Each warm pack should have two sub-sections: `### Planning Mode` (breadth: alternatives, risks, prior decisions) and `### Execution Mode` (precision: cost rules, model choices, batch format rules). Load the relevant subsection based on what Patrick signals he is doing.

---

### 1.3 Schema-Driven Compression Instead of Free-Form Session Logs

**Insight (prompting-context.md, Framework):** "Schema-driven summarization preserves essential semantics through structured, reversible compaction using templates and event types, enabling debuggability while preventing lossy compression that destroys signal."

**Source:** Grab the Inside Scoop on How Google, Anthropic, and Manus Built Long-Running AI Agents

**How it applies:** Our session logs are free-form prose. The instruction is 15-25 lines. Free prose compresses poorly — what gets included depends on recency bias and what seemed important in the moment. Schema-driven logs (structured event types: `task_completed`, `pattern_discovered`, `cost_incurred`, `file_created`, `decision_made`) would make logs machine-queryable and prevent lossy semantic compression.

**Status: PARTIALLY DOING THIS.** We have section headers (Accomplished, Files modified, Cost, KB consulted, Patterns harvested). But these are not typed event schemas — they are unstructured prose under labels.

**Proposed change:** Formalize session log schema. Each log entry should have typed events that can be grepped and counted, not just summarized prose.

---

### 1.4 Forgetting as Feature — Active Curation, Not Accumulation

**Insight (knowledge-rag.md, Contrarian):** "Forgetting is not a bug but an essential technology — AI systems fail precisely because they 'either accumulate or they purge, but they do not decay' like human memory does through lossy compression."

**Source:** AI's Memory Wall: Why Compute Grew 60,000x But Memory Only 100x

**How it applies:** Our warm packs and Tier B files grow but rarely shrink. The KB says random accumulation does not compound — it creates noise. We archive sessions every 5, but we never actively ask: what should decay from Tier A and Tier B?

**Status: PARTIALLY DOING THIS.** We archive session logs (compression). But we do not have active decay rules for knowledge content itself — triggers that never fire, BP files unused for 90 days, warm pack sections that have never been cited.

**Proposed change:** Add a Staleness Check to the Opus review: for each warm pack trigger and BP file, check last-cited date. Items with zero cites since last review get flagged. Patrick decides: deprecate, strengthen the trigger, or archive.

---

### 1.5 Principles-Based Guidance, Not Rules

**Insight (knowledge-rag.md, Anti Pattern):** "Rules-based guidance fails with AI systems because rules can't anticipate edge cases. When you give AI rigid rules like 'always log errors to this specific file,' you limit it to exactly that behavior. When you give it a principle like 'don't swallow errors,' it can figure out what that means in a hundred different situations."

**Source:** They Ignored My Tool Stack and Built Something Better — The 4 Patterns That Work

**How it applies:** Several of our Tier A Operational Rules are rigid rules, not principles. "Never load files >500KB without checking size first" is a rule. "Never glob-read entire directories" is a rule. These are right for the specific cases we have seen, but will fail at edge cases we have not anticipated. A principle would be: "Always estimate cost and scope before loading large datasets" — this scales to cases we have not seen.

**Status: PARTIALLY DOING THIS.** Some Tier A rules are principles ("Mine first, build after"), some are brittle rules ("Never load files >500KB"). The mix is uneven.

**Proposed change:** At next Opus review, audit each Tier A rule against this test: "Can an AI figure out what this means in 100 situations we did not anticipate?" If no, rewrite as principle. Keep specific rules only where determinism is required (cost thresholds, safety guards).

---

### 1.6 Conversation Threads as Primary Artifacts

**Insight (knowledge-rag.md, Anti Pattern):** "Treating files as the fundamental unit of AI work fails because the intelligence emerges from multi-turn conversations, not individual document interactions — this mismatch kills products designed around traditional file-based workflows."

**Source:** The 9 Hard Truths Killing AI Products Before They Ship

**How it applies:** We treat session logs as the artifact. But the session log is a summary of the conversation — the valuable thing is the multi-turn conversation that produced decisions. We lose the reasoning chain. When we look back at why a decision was made, we only have the outcome (what was built) not the path (what was considered and rejected).

**Status: NOT DOING THIS.** We produce session log summaries. The conversation context itself is discarded.

**Proposed change:** For high-value decisions (architecture choices, new company onboarding patterns, warm pack redesigns), preserve the key conversation thread or a structured reconstruction of it in `_archive/decision-threads/`. This is the "agent maintainability" pattern — the agent that built the system can return to it.

---

## Section 2: How Retrieval Should Work

### 2.1 Embed Retrieval Keys, Not Knowledge Dumps

**Insight (knowledge-rag.md, confirmed in CLAUDE.md Tier A):** "Embed retrieval keys, not knowledge dumps — trigger recall, don't preload."

**Source:** Already in our Tier A rules — this one we have right in principle.

**Status: PARTIALLY DOING THIS.** We say this in Tier A but our warm packs still contain knowledge dumps (What Works / What Fails sections). These are knowledge, not retrieval keys.

**Gap:** Knowledge Triggers (one-line action principles) are retrieval keys. The 4-5 paragraph "What Works" sections are knowledge dumps. The KB says the keys are more valuable than the dumps.

**Proposed change:** Reduce "What Works" sections in warm packs. Expand Knowledge Triggers. A well-formed trigger is: `[condition] → [action] → [why] (source-file)`. The trigger fires a retrieval if needed; the dump forces reading regardless.

---

### 2.2 Two-Stage Retrieval with Verification

**Insight (knowledge-rag.md, Technique):** "Retrieval requires two-stage verification (recall candidates via semantic search, then verify against ground truth) because LLMs 'optimize for continuity' and will hallucinate plausible facts to keep conversations flowing."

**Source:** AI's Memory Wall: Why Compute Grew 60,000x But Memory Only 100x

**How it applies:** When a Knowledge Trigger fires during work, we currently assume the insight recalled is accurate and complete. But the trigger is a one-line compression. If the situation is high-stakes (cost decision, architecture choice), the one-liner is not sufficient — we should retrieve the full insight from the source file.

**Status: NOT DOING THIS EXPLICITLY.** Our triggers point to source files (`source: topics/knowledge-rag.md`) but there is no protocol for when to retrieve the full source vs. act on the trigger.

**Proposed change:** Add stake-level guidance to trigger notation. Low-stakes: act on trigger. High-stakes (cost > $5, architecture change, new pattern to Tier A): read the source file before deciding. Format: `[trigger text] → [action] (source: file.md, stake: high)`.

---

### 2.3 Database Keys Mental Model — Design for Retrieval Paths

**Insight (knowledge-rag.md, Technique):** "Memory retrieval is recovering access paths (keys) not the memories themselves. When humans say 'I can't remember,' they mean 'I can't access the key.' This explains why prompting works — it provides keys."

**Source:** AI's Memory Wall: Why Compute Grew 60,000x But Memory Only 100x

**How it applies:** Our warm pack triggers need better "keys" — consistent terminology, explicit tags, and structured metadata that create retrieval paths. Right now a trigger fires if the right concept appears in the conversation. But if different sessions use different words for the same concept ("session log" vs. "work log" vs. "notes"), the trigger misses.

**Status: NOT DOING THIS.** No explicit key design. Triggers rely on organic matching.

**Proposed change:** Add synonym/alias terms to each trigger. For the compression trigger: aliases = [session log, compress, archive, session end]. For the cost trigger: aliases = [cost, spend, expense, batch, tokens, $]. This expands retrieval surface.

---

### 2.4 Proactive Recall Beats Generation

**Insight (productivity-workflows.md, Contrarian):** "Proactive recall beats generation for knowledge work. When organizations already possess extensive documented knowledge, AI that resurfaces existing context at the right moment delivers more value than AI that generates novel content on demand."

**Source:** Why the Best AI Tools Look NOTHING Like ChatGPT

**How it applies:** In sessions, we tend to generate new solutions to problems we may have already solved. The KB says the right move for organizations with extensive documented knowledge (which we now have — 1,331 insights, 13 BP files, 7 warm packs) is proactive surfacing of what already exists.

**Status: NOT DOING THIS RELIABLY.** Session start includes reading CURRENT-STATUS.md and loading warm pack. But mid-session, when a new problem arises, there is no protocol to check what we already know before generating a new answer.

**Proposed change:** Add a mid-session check: before solving a new problem that feels like it has architectural implications, ask "Is this pattern documented in _index.yaml?" before generating. This is already in the anti-pattern notes but is not wired into the session protocol as a decision gate.

---

### 2.5 Spaces with Standing Instructions as Institutional Knowledge

**Insight (knowledge-rag.md, Framework):** "Spaces with standing instructions create institutional knowledge by capturing successful search patterns as repeatable workflows. This transforms individual skill (knowing good prompts) into organizational capability."

**Source:** Master Perplexity Prompting

**How it applies:** Our warm packs are exactly this pattern — standing instructions for recurring project types. We are doing this right. But the KB says the key metric for these spaces is whether patterns compound: "organizational search capability that compounds as patterns improve." We do not currently measure whether warm packs compound (get measurably better over time).

**Status: DOING THIS, BUT NOT MEASURING IT.** Warm packs exist. No metric for whether they improve.

**Proposed change:** At Opus review, compare warm pack trigger count and specificity against prior review. Did triggers increase (more captured)? Did any get promoted to Tier A? Did any fire in session logs (activation)? Track these three numbers per pack.

---

## Section 3: Systems That Improve Themselves

### 3.1 Adaptive Context Engineering (ACE) — Self-Improving Agent Instructions

**Insight (prompting-context.md, Technique):** "Enable self-improving agents through Adaptive Context Engineering (ACE) — allowing agents to update strategies, memories, and instructions through execution feedback via small structured increments rather than human tinkering or wholesale overwrites."

**Source:** Grab the Inside Scoop on How Google, Anthropic, and Manus Built Long-Running AI Agents

**How it applies:** This is the exact design intent of our Opus review — the system should improve its own instructions based on what works. But we implement it as a human-orchestrated review every 10 sessions. The KB describes this as a continuous mechanism: execution feedback → structured increments → instruction updates.

**Status: PARTIALLY DOING THIS.** Opus review captures the mechanism but fires infrequently (every 10 sessions). Between reviews, nothing is self-correcting.

**Proposed change:** Add a lightweight mid-cycle feedback mechanism. After each session, one forced question: "Did any Tier A rule behave wrong, or did any pattern feel like it should be documented?" This is not pattern harvest (which we already have) but rule-validity feedback. If a Tier A rule was wrong or missing, log it immediately rather than waiting for session 30.

---

### 3.2 Memory Advantage Compounds — Start Now, No Gaps

**Insight (knowledge-rag.md, Framework):** "Memory advantage compounds over 10-20 years — starting structured memory architecture now versus waiting creates non-recoverable gaps because 'random accumulation actually does not compound, it just creates noise.'"

**Source:** AI's Memory Wall: Why Compute Grew 60,000x But Memory Only 100x

**How it applies:** Our KB is 28 sessions old and already has 1,331 insights organized by topic. This is a compounding asset. But the KB warns that random accumulation creates noise, not compound advantage. The question is: are our insights organized in a way that compounds, or are they accumulating?

**Status: PARTIALLY DOING THIS.** Insights are organized by topic (good). Warm packs compress them into actionable triggers (good). But we have no explicit quality-of-compression metric — are the 1,331 insights getting more actionable over time, or are we just adding more?

**Proposed change:** Track "trigger density" per topic file: (number of Knowledge Triggers) / (number of raw insights). A topic with 95 insights but only 4 triggers is undercompressed. A topic with 20 insights but 15 triggers may be over-triggered. Target ratio: 1 trigger per 7-10 insights for high-relevance topics.

---

### 3.3 The Specification Mastery Flywheel — Compound Prompt Libraries

**Insight (prompting-context.md, Framework):** "The Specification Mastery Flywheel — write spec → model executes fast → confidence in clarity → invest in prompt library → reusable specs improve → faster execution enables more attempts → better specification skill — creates compound advantages through behavioral iteration."

**Source:** Inside ChatGPT-5's Brain: System Prompt Secrets for First Movers

**How it applies:** Our warm packs are prompt libraries. But we do not track reuse rate. A warm pack trigger that fires 0 times in 10 sessions is not compounding — it is noise. A trigger that fires 5 times and leads to correct behavior each time is genuine IP.

**Status: PARTIALLY DOING THIS.** We have the library (warm packs + BP files). We do not track reuse rate per trigger.

**Proposed change:** Already noted in Opus review protocol. This confirms it is the right metric: count trigger activations per session log. The Specification Mastery Flywheel only works if you measure whether the specs are being used.

---

### 3.4 Proprietary Rubrics as Moat

**Insight (knowledge-rag.md, Contrarian):** "The real moat isn't AI tools or processes — it's proprietary rubrics capturing what quality looks like in your specific context. These rubrics encode years of accumulated wisdom that competitors starting from zero cannot quickly replicate, making institutional knowledge executable."

**Source:** The AI Trick That Finally Made Me Better at My Job

**How it applies:** Our warm packs contain quality heuristics embedded in "What Works / What Fails" sections. But they are not formalized as rubrics (scored dimensions). A rubric for "is this a good session log?" would be: (1) cost recorded, (2) files listed, (3) pattern harvest explicit, (4) KB consulted noted, (5) next tasks clear. We informally apply these but do not score them.

**Status: NOT DOING THIS EXPLICITLY.** Quality standards exist but are not rubric-formalized and not tracked over time.

**Proposed change:** Not urgent, but worth noting for Opus review: consider creating a session log rubric (5 dimensions, 3-point scale). Opus can score the last 5 logs at each review to see whether log quality is improving. Artifact Quality Trajectory = rising scores + fewer omissions.

---

### 3.5 Intent as Living Document — Version Separately from Implementation

**Insight (prompting-context.md, Technique):** "Intent as Living Document — version intent specifications separately from implementation so understanding can evolve without rewriting agent logic, creating organizational learning layer."

**Source:** The AI Failure Mode Nobody Warned You About

**How it applies:** CLAUDE.md is both intent (what we want to achieve) and implementation (how sessions work). When we learn something new about how sessions should work, we rewrite CLAUDE.md. The KB suggests separating intent (strategy: "we want a self-improving knowledge system") from implementation (protocol: "here are the 4 session-end steps"). Intent should be stable; implementation should update frequently based on feedback.

**Status: NOT DOING THIS.** CLAUDE.md conflates intent and implementation. When something does not work, we rewrite both together.

**Proposed change:** Consider a `_shared/system-intent.md` — a short document (1 page) that captures the strategic goals of the whole system. "Why does this system exist? What does success look like? What are we optimizing for?" This would be stable across many sessions and give future Opus reviews something to check implementation against.

---

## Section 4: Context Window Optimization

### 4.1 Longer Context Makes Things Worse Without Intent Structure

**Insight (prompting-context.md, Contrarian):** "Longer context windows made agent performance worse, not better, because attention became scarce and irrelevant history drowns out critical signals — the problem intensified rather than resolved despite 1M+ token windows."

**Source:** Grab the Inside Scoop on How Google, Anthropic, and Manus Built Long-Running AI Agents

**How it applies:** Our target is to keep session context to ~10% of total context. But we do not have attention management rules. If a session runs long, context accumulates. The KB says this actively degrades performance — the more context, the less signal.

**Status: PARTIALLY DOING THIS.** We have the 10% target. We do not have mid-session context trimming rules.

**Proposed change:** Add a mid-session reset rule: if a session has been running for more than 90 minutes or has produced more than 4 output blocks, re-anchor with a fresh summary of current state before proceeding. Do not let context drift.

---

### 4.2 Four-Tier Memory Architecture

**Insight (prompting-context.md, Framework):** "AI agent memory should be architected as a four-tier system (Working Context / Sessions / Memory / Artifacts) that mirrors traditional computer architecture (cache / RAM / disk), where context becomes 'compiler output' dynamically generated per-call rather than accumulated transcript."

**Source:** Grab the Inside Scoop on How Google, Anthropic, and Manus Built Long-Running AI Agents

**How it applies:** Our system has three tiers (Tier A in CLAUDE.md / Tier B in _shared/ / Tier C in _archive/). The KB describes four tiers with different memory types and lifecycles. We are missing an explicit "Working Context" tier — the dynamically compiled, session-specific context that gets generated fresh each call.

**Status: PARTIALLY DOING THIS.** We have Tier A/B/C for patterns. We do not have an explicit Working Context tier that is freshly compiled per session from the other tiers.

**Proposed change:** Formalize the Context Pack (bottom of CURRENT-STATUS.md) as the "Working Context tier" — the dynamically compiled output of all other tiers. It already functions this way. Making it explicit helps Opus review assess whether the compilation is working.

---

### 4.3 Stable Prefixes for Caching

**Insight (prompting-context.md, Metric):** "Proper caching discipline through prefix stability can reduce latency by 10x, dropping response times from 200 milliseconds to 20 milliseconds per step."

**Source:** Grab the Inside Scoop on How Google, Anthropic, and Manus Built Long-Running AI Agents

**How it applies:** We use the Anthropic Batch API with prompt caching (`system` field caching = 90% discount after first request). The KB confirms the underlying mechanism: stable prefixes enable cache hits. Our CLAUDE.md structure (with stable sections at the top and variable session content at the bottom) is already designed correctly for this.

**Status: DOING THIS.** Our system prompt architecture already implements stable prefix + variable suffix. Confirming this is intentional and correct.

---

### 4.4 Positional Reinforcement — Repeat Critical Constraints

**Insight (prompting-context.md, Technique):** "Positional Reinforcement at ~500-token intervals — systematically repeat critical constraints throughout long prompts to counter attention degradation, treating it as architectural necessity rather than redundancy."

**Source:** 7 Prompting Strategies from Claude 4's System Prompt Leak

**How it applies:** CLAUDE.md is ~200+ lines. The most critical Tier A rules appear once, at the top. By the time the model processes session-specific context, the early rules may have degraded in attention weight. The KB says repeat critical constraints every 500 tokens.

**Status: NOT DOING THIS.** CLAUDE.md states rules once. No repetition. The Context Pack at the bottom of CURRENT-STATUS.md could function as a positional reinforcer — but it does not currently echo the most critical rules.

**Proposed change:** The Context Pack should include a 3-5 line "Critical Rules Reminder" that echoes the most important Tier A rules. Not all of them — just the ones most likely to be violated in the upcoming session based on the active task type.

---

### 4.5 Goldilocks Prompting — 80% of Tasks Need Mid-Altitude Context

**Insight (prompting-context.md, Framework):** "Goldilocks prompting — there exists an optimal level of prompt specificity between over-constraining (burns tokens, kills creativity) and under-constraining (produces generic outputs). 80% of use cases benefit from mid-altitude prompting."

**Source:** How I Improved AI Output Quality 10X With One Prompting Shift

**How it applies:** Our warm packs vary in specificity. The DMC mining pack is highly specific (includes exact search strings, cost benchmarks, batch parameters). The system-meta pack is more principled. The KB says 80% of tasks benefit from mid-altitude — but 20% of tasks (batch jobs, document processing, schema building) genuinely need high specificity.

**Status: PARTIALLY DOING THIS.** Some packs over-specify, some under-specify. No explicit altitude calibration per pack.

**Proposed change:** Each warm pack should include one line: `Prompting altitude: [high-specificity | mid-altitude | principles-only]`. High-specificity packs: batch jobs, document workflows. Mid-altitude: mining sessions, SEO content. Principles-only: architecture, Opus review.

---

## Section 5: Measuring Whether Knowledge Is Actually Being Used

### 5.1 Artifact Quality Trajectory — The Right Health Metric

**Insight (knowledge-rag.md, Metric):** "The optimal system health metric is 'Artifact Quality Trajectory' — specifically measuring whether rubric scores increase WHILE revision cycles decrease over time. Quality rising alone suggests gaming the rubric; efficiency rising alone suggests faster mediocrity."

**Source:** The AI Trick That Finally Made Me Better at My Job

**How it applies:** Our current health metric is activation rate: did KB get consulted? Did patterns get harvested? The KB says the right metric is trajectory: are outputs getting better AND faster? A KB that gets consulted more is useless if outputs are not improving. A system that produces outputs faster is useless if quality is dropping.

**Status: NOT DOING THIS.** We count activations (KB consulted: yes/no). We do not track quality trajectory.

**Proposed change:** At Opus review, score the last 5 final deliverables on 3 dimensions: (1) did it need major rework, (2) was it produced within expected cost, (3) did Patrick explicitly approve without change requests. Track these across reviews. If scores plateau, the KB is not compounding — it is coasting.

---

### 5.2 AI Value Extraction Velocity (AVEV)

**Insight (knowledge-rag.md, Framework):** "The AI Value Extraction Velocity (AVEV) metric — measure organizational AI maturity not by which models you use, but by time from model access to measurable business value in production. Organizations with strong foundations see AVEV accelerate over time; those chasing models see AVEV stagnate."

**Source:** ChatGPT 5 Won't Save You: 10 Reasons Why Your AI Strategy is Failing

**How it applies:** Our system has been running for 28 sessions. AVEV for us = time from project start to first usable deliverable. Session 1 (email mining) took several sessions to produce first output. Would it take fewer sessions now? If our KB + warm packs are working, they should compress time-to-value. We have never measured this.

**Status: NOT DOING THIS.** We track cost. We do not track time-to-first-deliverable per project.

**Proposed change:** At Opus review, ask: for the last 2 completed projects, how many sessions from kickoff to first usable output? Track this across reviews. If AVEV is declining (fewer sessions per deliverable), the system is maturing. If flat or rising, something is wrong.

---

### 5.3 First-Turn Usefulness Rate

**Insight (prompting-context.md, Framework):** "First-Turn Usefulness Rate (percentage of prompts producing 80%+ useful output on initial response) serves as a health metric for prompting effectiveness."

**Source:** ChatGPT-5 Prompting is Too Hard: This Video Makes it Easy for You

**How it applies:** In our sessions, we often iterate on prompts — Patrick gives a direction, the output needs adjustment, we refine. How often does the first output nail it? If our warm packs and Knowledge Triggers are working, first-turn usefulness should be improving over time. A declining rate signals our context preparation is deteriorating.

**Status: NOT DOING THIS.** We do not track revision cycles per session.

**Proposed change:** Add one line to session log: `First-turn quality: [high | medium | low]` — subjective but trackable. High = Patrick accepted first output without major changes. Medium = one round of clarification. Low = multiple revisions needed. Opus review aggregates this across sessions.

---

### 5.4 Task-Model Match Rate

**Insight (productivity-workflows.md, Framework):** "The Task-Model Match Rate metric — track the percentage of atomic tasks executed by the empirically optimal model for that task type, targeting 70%+ as indicator of AI fluency."

**Source:** The AI Prompting Mistake Costing You Hours Every Week

**How it applies:** Our model strategy (Opus/Sonnet/Haiku decision tree) is documented in Tier A. But we do not track whether we follow it. Are we using Sonnet for execution tasks? Are we using Haiku for mechanical work? The KB says 70%+ match rate indicates maturity.

**Status: NOT DOING THIS.** We have the rule. We do not track whether sessions comply.

**Proposed change:** Session logs already record cost. Add one field: `Model used: [Opus/Sonnet/Haiku/mixed]`. Opus review checks distribution: what % of sessions used the right model for the task type? If Opus is being used for execution work, it signals the rule is not firing.

---

### 5.5 Staleness as a Failure Mode — The Wiki Trap

**Insight (knowledge-rag.md, Metric):** "RAG systems fail due to staleness — 'When was the last time you updated your wiki?' Most documentation-based retrieval pulls information that's months or years outdated, with update mechanisms being harder than initial storage."

**Source:** AI's Memory Wall: Why Compute Grew 60,000x But Memory Only 100x

**How it applies:** Our warm packs have `last_curated` timestamps. Our BP files do not. If a BP file was written in session 5 and it is now session 28, is its guidance still accurate? The KB says staleness is one of the primary failure modes for RAG-style knowledge systems.

**Status: PARTIALLY DOING THIS.** Warm packs have timestamps. BP files do not. No automatic staleness checking.

**Proposed change:** Add `last_updated: [session-N]` to each BP file header. Opus review flags any BP file where (current_session - last_updated) > 15 sessions. Patrick decides: still valid, update, or archive.

---

## Section 6: High-Priority Gaps (What to Fix First)

Ranked by impact vs. effort to implement:

### Priority 1 — Immediate (can do this session or next)

**A. Add "Critical Rules Reminder" block to Context Pack**
The context pack already exists. Adding 3-5 lines echoing the most critical Tier A rules for the upcoming task costs nothing and directly implements positional reinforcement. Estimated effort: 5 minutes per session.

**B. Add `Model used:` field to session logs**
One additional line per session log. Enables Task-Model Match Rate tracking in Opus review. Costs nothing, builds data immediately.

**C. Add `First-turn quality:` field to session logs**
Same as above. One line. Tracks quality trajectory without rubrics.

**D. Add `last_updated: session-N` to BP file headers**
Grep all files in `_shared/best-practices/`, add one metadata line each. Staleness becomes visible. 15-minute task.

### Priority 2 — Next Opus Review (Session 30)

**E. Mode-aware warm pack sections (Planning vs. Execution)**
Restructure each warm pack to have Planning Mode and Execution Mode sub-sections. Requires ~30 minutes to restructure all 7 packs. Would immediately improve context relevance.

**F. Rubric for session log quality (5 dimensions, 3-point scale)**
Draft a simple rubric. Opus reviews last 5 logs against it at Session 30. Establishes quality baseline.

**G. Trigger density audit**
For each topic file: count raw insights and Knowledge Triggers. Flag under-compressed topics (high insights, low triggers). Identify the highest-value insights not yet captured as triggers.

**H. AVEV baseline measurement**
At Session 30, measure time-to-first-deliverable for the last 3 completed projects. This establishes the baseline for tracking whether the system is maturing.

### Priority 3 — Design Phase (requires more thought)

**I. Principles-based rewrite of brittle Tier A rules**
Takes careful judgment. Each rule must be tested: "Does this scale to 100 situations we have not anticipated?" Low urgency but compounds over time.

**J. Decision thread archive**
For significant architectural choices, preserve a structured reconstruction of the reasoning. Would improve system self-repair capability. Higher effort, high long-term value.

**K. System intent document**
A 1-page `system-intent.md` that is stable across sessions. Gives Opus reviews an anchor: is the system still serving its original purpose?

---

## Section 7: Insights We Are Already Doing Well

These are KB insights that our system implements correctly. Confirming them validates that our approach is grounded.

| What the KB says | What we do | Assessment |
|---|---|---|
| Mode-aware context beats volume | Warm packs over raw dumps | Correct, but not mode-split yet |
| Principles-based guidance scales; rules-based breaks | CLAUDE.md has mix of both | Right direction, needs refinement |
| Embed retrieval keys, not knowledge dumps | Knowledge Triggers are keys | Correct |
| Human judgment is irreplaceable for compression | Patrick's corrections → Tier A | Correct |
| Vendor-neutral memory formats prevent lock-in | Everything in markdown + git | Correct |
| Memory advantage compounds — start now | 28 sessions of structured memory | Correct |
| Stable prefixes for caching | CLAUDE.md structure | Correct |
| Shorter outputs at optimal altitude outperform exhaustive prompts | 500-token budget rule | Correct |
| Forgetting as feature — active curation | Session compression every 5 | Partially correct |
| 80/20 flip — 80% monitoring, 20% pre-launch | Post-session review pattern | Correct |
| Right model for right task | Opus/Sonnet/Haiku decision tree | Correct in theory |

---

## Appendix: Insights Not Relevant to KB Meta-System

The following insight categories from the three files were read fully but are not actionable for KB system improvement (they address different use cases):

- Adversarial prompting / institutional disputes (8 Ways to Use AI series) — relevant for vendor negotiations, not KB design
- Relationship management / LinkedIn export analysis — not applicable
- Software agent deployment / enterprise AI ROI — relevant as analogies but not directly applicable to our file-based system
- Visual prompt engineering / JSON schemas for image generation — not applicable
- Medical billing / regulatory compliance use cases — not applicable

These were read, assessed, and determined to be out of scope for this meta-analysis. They remain in the KB for their original intended uses.

---

*Written: 2026-02-18 | Read all 262 insights across 3 files before writing | No scripts used*
