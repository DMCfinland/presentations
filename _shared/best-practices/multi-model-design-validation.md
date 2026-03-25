# Multi-Model Design Validation Pattern
**Name:** multi-model-design-validation
**Type:** Process pattern — skill design + architecture decisions
**Source:** Sessions 82-83, 2026-03-17 (PWJ skill design cycle)
**Status:** Tier B — 1 confirmed use (PWJ skill design, session 83)

---

## What It Is

A 3-round validation workflow for architectural design decisions before building. Uses Claude (internal synthesis) → Grok Heavy 4-agent (adversarial research) → Gemini thinking (quick soundness check) in sequence, each with a distinct role.

---

## The Pattern

### Round 1 — Internal synthesis (Claude)
Build the plan using all available KB. Write explicit design decisions with rationale. Identify open questions.

### Round 2 — Grok Heavy (adversarial research + simulation)
Use `/grok-spar` skill. Purpose: find what's WRONG, not validate what's right. Grok's value is:
- Harper: live data, real production systems, X/LinkedIn signals
- Benjamin: quantitative simulation (code_execution) to stress-test claims
- Lucas: devil's advocate — highest-value output, not the synthesis

**Anti-pattern:** Asking Grok to validate a pre-designed conclusion (produces zero value — echoes back what you gave it). See `/grok-spar` Rule #1.

### Round 3 — Gemini thinking (quick, no deep research)
Purpose: solo-operator sanity check. Gemini's distinct value: practical friction analysis ("automation tax"), Debugging Paradox, adoption failure modes that Grok Heavy misses (Grok skews toward theoretical completeness, Gemini skews toward practical abandonment risk).

**When to use thinking vs deep research:** Thinking for soundness check on specific decisions. Deep research only when you need exhaustive citation search.

---

## What Each Model Catches That Others Miss

| Model | Typical blind spots caught |
|-------|---------------------------|
| Claude (internal) | Spec completeness, cross-file consistency, KB alignment |
| Grok Heavy | Production precedents, quantitative risks, regulatory angles |
| Gemini thinking | Solo-operator adoption friction, "you'll never maintain this", Debugging Paradox |

**The Debugging Paradox (Gemini session 83):** When an agentic loop fails, you debug the loop instead of the task. For solo operators without DevOps, this kills adoption within weeks. Fix: minimize loop complexity, maximize Judge judgment autonomy within a simple cap.

---

## When to Apply This Pattern

- Designing a new skill or workflow that will run repeatedly
- Architectural decisions with >€500 downstream impact
- Any system with a self-improvement loop (highest failure risk)

**When NOT to apply:** Single-use deliverables, routine task execution, decisions reversible within one session.

---

## Session 83 Learnings — PWJ Skill Design

**5 design decisions improved through 3-round validation:**

1. **Tag-based LESSONS > tier-split** — Gemini identified false dichotomy in technical/strategic split. Single file with grep-filter avoids context poisoning without DevOps overhead.

2. **Mission-criticality cap (3-12) > tier-based caps** — Patrick's decision. Mission criticality is a better axis than task type because the same task type can be high- or low-stakes depending on context.

3. **State Delta > hash check for Silent Drift** — Gemini: hash check breaks on comment edits → interaction fatigue → safety check ignored. Delta with line-count threshold is surgical.

4. **Divorce Rule opt-in** — Both Grok and Gemini converged: mandatory cross-family = adoption killer for solo operator. Persona Shifting (Red Team system prompt) is accessible layer-1 defense. Cross-family is layer-2 upgrade.

5. **Judge judgment stop > fixed cap** — Gemini's Optimistic Hallucination concern (Judge+Worker agree on broken solution to close loop) is mitigated by Judge explicitly stating its stopping signal each round. Cap is ceiling, not target.

**Meta-learning: When to stop the validation loop**
Three rounds was right for this design. Grok added quantitative risk data. Gemini added adoption friction angle. A 4th round would have produced diminishing returns — the remaining decisions were Patrick's judgment calls, not researchable questions. Stop when the open questions are preference/tradeoff calls, not factual gaps.

---

## Cost Reference (session 83)
- Grok Heavy spar: ~0 (free tier)
- Gemini thinking: ~0 (free tier)
- Claude internal synthesis: ~$0.50-1.00 (session context)
- Total: ~$0.50-1.00 for a fully cross-validated architectural decision

*Source: session 83, 2026-03-17. Patrick + Grok session 83 + Gemini thinking session 83.*
