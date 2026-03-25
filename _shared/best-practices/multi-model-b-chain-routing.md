# Multi-Model B-Chain Routing — Gemini→Grok→Claude

**Source:** Cursor Swarm Master-Skills v2.4 via S116, Grok-validated
**Type:** Orchestration pattern
**Confidence:** 0.7

---

## The Pattern

When a task requires multiple AI models, use a fixed sequential chain (B-model) rather than ad-hoc routing:

| Step | Model | Role | When |
|------|-------|------|------|
| 1 | **Gemini** | Research — facts, web search, context gathering | Always first when research is needed |
| 2 | **Grok** | Reasoning — logic checks, critique, stress-test | After research, before building |
| 3 | **Claude** | Design + Implementation — architecture, code, docs | Final execution stage |

**Competitive mode (use sparingly):** For critical decisions, give the same task to all three in parallel and take the best-of-N. Expensive — reserve for once-a-week reviews or architectural pivots.

---

## Why This Order

- **Gemini first** = broadest factual coverage, current web knowledge. Avoids Grok/Claude hallucinating facts.
- **Grok second** = strongest adversarial reasoning. Grok is optimized to find what Gemini missed or what's logically wrong.
- **Claude third** = execution. Claude builds on validated context, not raw assumptions.

Reversing the order means Claude builds on unvalidated input, and Grok challenges something that wasn't grounded first.

---

## What We Do Now (vs. This Pattern)

Current practice: ad-hoc per session. We choose which model to use based on intuition.
This pattern: explicit trigger per step. Reduces decision fatigue and inconsistency.

---

## When to Apply

- Any strategic research task with a deliverable (spec, architecture, decision)
- Multi-model sparring sessions (Grok spar, Gemini advisory)
- Before spawning a PWJ Worker for a novel task type

**Skip when:**
- Simple execution task (just use Claude)
- Grok-only validation already planned (Step 3.5 in PWJ)
- Time-constrained quick task

---

## Integration with PWJ

- Step 3.5 (Grok criteria stress-test) = B-chain Step 2 applied to done-criteria only
- If full B-chain needed for research before intake: run Gemini→Grok BEFORE opening PWJ loop
- Don't mix B-chain with PWJ Worker: B-chain is for BEFORE intake, not inside the loop

---

## Example: Transcript Pipeline Research (S113)

5-agent wave used this exact structure:
- Agents A/E = research (Gemini-role)
- Synthesis = cross-validation (Grok-role)
- Build Plan = Claude execution (S114)

The B-chain pattern is what made this work.
