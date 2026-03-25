# Nate AI: Verifiability Spectrum + Harness Architecture
<!-- source: "What if AI is not jagged?" Nate AI Substack, March 11, 2026 | session: 71 -->
<!-- created: 2026-03-12 | confidence: 0.9 | tier: B -->

**What:** Framework for classifying work by verifiability tier, explaining why multi-agent harnesses beat single-shot AI — and why the improvement rate exceeds model curve predictions.

---

## The Core Finding: The Jagged Frontier Was Measurement Error

The "jagged frontier" was never a property of AI intelligence. It was an artifact of how work was structured:

**Single-shot, single-agent interaction removes all organizational structure from work.** When you ask a model for one answer in one turn, variance in task difficulty shows up as jaggedness in outcomes. Not because intelligence is jagged — because no competent human professional works by trying to solve every problem in 30 seconds with no notes, no colleagues, and no ability to try something, recognize it's not working, and try again.

We described a problem we accidentally created as a property of the AI.

---

## The Convergence: Four Organizations, Same Architecture

Anthropic, Google DeepMind, OpenAI Codex, and Cursor independently built multi-agent coordination systems. None coordinated. All four exhibit the same structural pattern:

**Decompose → Parallelize → Verify → Iterate**

Cursor's proof: A coding harness (no math-specific machinery) solved First Proof Problem 6 (spectral graph theory) after 4 days autonomous runtime, without human guidance. Improved the human-written solution: constant in the bound from 0.03 → 0.13, covered full vertex set. Used Marcus-Spielman-Srivastava interlacing polynomial method.

**Why this matters more than purpose-built math systems:** When a coding harness outperforms a domain-specific agent, you've learned something about harnesses, not math. The generalization is the finding.

**Cursor's architecture (Planner-Worker-Judge):**
- Flat coordination failed: agents held locks, became risk-averse, ground without progress
- Hierarchy fixed it: Planners explore + create tasks → Workers grind individual tasks in isolation → Judge evaluates, decides to continue or restart fresh
- "Many improvements came from removing complexity rather than adding it"
- The system's behavior is disproportionately determined by prompt design — not coordination machinery

---

## The Verifiability Spectrum

| Tier | Description | Examples | Harness-ready? |
|------|-------------|----------|---------------|
| **Tier 1** | Machine-checkable | Code compiles/fails, tests pass/fail, formal proofs | Yes — immediately |
| **Tier 2** | Expert-checkable with criteria | Informal proofs, engineering designs meeting specs, legal briefs, financial models | Yes — judge can evaluate |
| **Tier 3** | Genuinely judgment-dependent | Original theory-building, aesthetic choices, strategic decisions dependent on values | Not yet — human required |

**Critical insight:** A Tier 1 harness (coding) operated effectively in Tier 2 (mathematics). The Planner-Worker-Judge architecture generalized even though domain-specific verification machinery didn't exist.

What harnesses actually need: enough signal to distinguish progress from non-progress. They don't need machine-checkable verification at every step.

**The portion of work most people think is Tier 3 but is actually Tier 2 is much larger than they expect.** A large fraction of "expert work" involves executing arguments that are "involved but routine" — they require sophistication and knowledge, but they're not the creative leaps that constitute genuine discovery. Those leaps are Tier 3. The surrounding work is Tier 2.

---

## Why Smoothing Rate Beats Model Curve

Organizational architecture transfers across domains at near-zero marginal cost. This is qualitatively different from model improvement or cost decline:

- **Model improvement:** You get a capability increase, then wait for the next model.
- **Architectural insight transfer:** You get a capability increase essentially for free. Architectural advances don't depreciate.

Cursor didn't spend six weeks building a math harness. They pointed an existing harness at a math problem and ran it for four days.

**METR (arXiv 2503.14499):** Task completion horizons doubling approximately every 207 days (~7 months) since 2019, with apparent acceleration in 2024-2025 (p=0.006). Current frontier o3 has 50% completion horizon of ~110 minutes. This beats predictions based on model improvement alone — because it measures harness + model combined.

**Note on arXiv 2507.09089 (separate METR paper):** This RCT on real developers found AI tooling *increased* completion time by 19%. Measures adoption friction, not raw capability. Not a contradiction — different measurement of a different phenomenon.

---

## What Survives: Evaluation Meta-Skills

The skill that survives isn't doing the work. It's **evaluating whether the work is correct.**

Anthropic (2026 agentic coding trends): engineers delegating tasks where they "can relatively easily sniff-check on correctness." Not delegating easy work — delegating *verifiable* work.

**Per-domain question:** What does "sniff-checking" look like in your field?
- Coding: Is this architecture maintainable? Are these tests covering the important cases?
- Finance: Does this model's assumptions hold? Are the edge cases covered?
- Legal: Has this brief addressed the relevant precedents?
- Strategy: Does this output match the original done-criteria?

Engineers who can evaluate AI-produced code quickly and well are in an excellent position. Engineers who can't are not.

---

## Application to This System

This directly validates:
1. **Lead-agent-quality-gate.md** — the Judge role in our Planner-Worker-Judge loop
2. **Tier-balanced metrics** — Tier 1/2 sessions = routine, Tier 3 = genuine judgment. Most work is Tier 2.
3. **Structured intake (done-criteria upfront)** — defines the verifiability criteria that allow Tier 2 automation
4. **Verifiability spectrum = tier classification in session YAML** — session_tier maps to Tier 1/2/3

---

**When to apply:** When classifying new work for delegation. When setting ACCEPTANCE CRITERIA for subagent tasks. When explaining why multi-agent approach is worth the cost. When deciding what Patrick reviews vs what AI handles autonomously.
