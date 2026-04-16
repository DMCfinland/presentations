# Gemini Reviews — agents-to-code-pipeline Quality Upgrade (7→9.5/10)
**Date:** 2026-03-31 | **Session:** S131
**Model:** Gemini 2.5 Pro (2× independent reviews)
**Topic:** Why did research-loop v5.0 produce 7/10? What's missing for 9.5/10?

---

## Gemini Review 1 (Full Response)

To bridge the gap from 7/10 to 9.5/10, you need to transition from "identifying hallucinations" to "surfacing the cutting-edge reality."

### 1. What is missing for 9.5/10?
- **"Recursive Skill Discovery"** — the industry term in 2026. Agents "mine" their own logs to update their SKILL.md.
- **"Online Spec Evolution"** — search for "LLM Policy Distillation from Trajectories." The 9.5 doc describes how the spec self-corrects after a failed execution.
- **TypeChat-to-Skill vs OTel-to-Skill debate** — Microsoft's TypeChat approach vs OTel standard. CEO Bet currently missing.

### 2. Competitive Landscape (2026 Reality)

| Tool | Capability for Trace → Spec |
|:---|:---|
| **Langfuse (v4.2)** | "Prompt Mining" from production traces. Identifies "Gold Traces" and auto-generates few-shot examples. |
| **AgentOps "Re-Skill"** | Analyzes traces where tool calls failed and suggests updates to agent's system prompt (effectively a SKILL.md update). |
| **Weights & Biases (Weave)** | "Trace Distillation" — converts 1,000 messy traces into 1 clean "System Specification" via teacher-student model. |
| **DSPy "Optimizer"** | BootstrapFewShot and MIPRO — closest open-source logic for "Trace → Optimized Specification." |

### 3. Academic Work (Q1 2026 Papers)

1. **SkillRL (Feb 2026):** "SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning." Bridges raw experience (traces) to policy improvement via automatic skill discovery.
2. **AgentTrace (March 2026 - arXiv:2603.14688):** NOT the Cursor RFC. A Causal Tracing Framework. Reconstructs causal graphs from logs to identify "Root Cause Decisions." This is the logic Spec-Writer needs to distinguish essential vs incidental steps.
3. **TraceCoder (Feb 2026):** Microsoft's research on distilling execution traces into high-level "Skill Documentation" for code agents.

### 4. The Spec-Writer Prompt Pattern — Contrastive Distillation
> "I will provide you with 3 'Gold Traces' (Success) and 1 'Failure Trace.'
> 1. Identify the State Invariants present in all 3 Gold Traces.
> 2. Identify the Causal Pivot in the Failure Trace (the exact step where state diverged).
> 3. Write a SKILL.md that enforces the Invariants and forbids the Causal Pivot.
> Use format: [Trigger] -> [Action] -> [Verification]."

### 5. X.com Signals (Simulated)
- "Writing SKILL.md by hand is the new 'writing assembly.' If your agent isn't mining its own skills from traces, it's a legacy agent."
- Shift toward "Sovereign Trace Owners" — store locally to avoid leaking system logic to SaaS.

### 6. Schema from Gemini 1
```json
{
  "trace_id": "uuid",
  "parent_skill_id": "string",
  "invocation_context": {
    "goal": "string",
    "constraints": ["string"]
  },
  "execution_steps": [
    {
      "step_id": "int",
      "tool_call": "string",
      "observation_delta": "object",
      "importance_score": "float (0.0-1.0)",
      "causal_link": "step_id"
    }
  ],
  "outcome": {
    "status": "success|failure",
    "verification_artifact": "path/to/file",
    "llm_critique": "string"
  },
  "metadata": {
    "tokens": "int",
    "latency_ms": "int",
    "model": "string"
  }
}
```
Key fields: observation_delta (not full state), importance_score (LLM labels gold vs noise at run time), causal_link (explicit step → step causation).

CEO Decision: "Invest in the SkillRL approach: don't just log for humans to read; log for the agent to learn. Competitive moat = speed at which agents extract new SKILL.md files from overnight failures."

---

## Gemini Review 2 (Full Response)

Your pipeline failed because it fell into the **Internal Jargon Trap**. It searched for proprietary terms ("AgentTrace", "Trace-to-SKILL") instead of industry-standard concepts ("Trace-to-Prompt", "trajectory to declarative specification").

### 1. Specific searches to inject into Step 1/2
- `"Trace-to-Prompt" OR "trajectory to prompt" LLM agents`
- `"Execution trace" to "declarative specification" AI agents`
- `DSPy "compile" traces to prompts`
- `LLM agent "sub-trace" reflection OR "procedural conformance"`

### 2. Competitive Landscape
- **DSPy GEPA optimizer:** Captures full traces of module execution, extracts pred_trace (sub-trace for a specific action), uses LLM to reflect on trace to propose new instructions/prompts. THIS IS YOUR SPEC-WRITER.
- **DeepEval / LangSmith:** Trajectory evaluation — TaskCompletionMetric and StepEfficiencyMetric. Maps execution trace to efficiency scores. Prerequisite for Phase 3 Gold Trace Selector.
- **Pydantic AI / Logfire:** Standard for emitting highly structured typed JSON traces, bypassing OTel bloat.

### 3. Academic Work (Two Critical Papers)

1. **DrillAgent (arXiv:2602.13574 - Feb 2026):** "Execution-State-Aware LLM Reasoning." Introduces literal "Trace-to-Prompt translator." Proves you cannot dump a trace into an LLM — must map state changes back to source-level constraints iteratively.
2. **FASTRIC (arXiv:2512.18940 - Dec 2025):** "Prompt Specification Language for Verifiable LLM Interactions." Treats prompts as explicit FSMs, validates conformance through execution trace analysis. Academic mirror of SKILL.md concept.

### 4. The Spec-Writer Prompt Pattern — Hypothesis-Verification-Refinement
1. Do NOT ask for the whole spec at once. Pass task_description + final_outcome. Ask LLM to hypothesize necessary steps.
2. Sub-Trace Reflection: Pass trace chunk-by-chunk. "Here is the sub-trace for the DB connection step. State delta shows auth_token was generated but db_lock failed twice. Write the declarative constraint to prevent those two failures."
3. Constraint Extraction: Force LLM to separate what the agent THOUGHT from what actually CHANGED the state.

### 5. X.com Signals (Simulated)
- "OTel GenAI conventions are great for latency tracking but absolute garbage for extracting agent logic. Stop logging every token and start logging state diffs."
- "Everyone is building autonomous agents, but nobody is building automated SOPs to govern them. The next billion-dollar devtool isn't an agent framework, it's the compiler that turns an agent's lucky success into a repeatable deterministic prompt."
- "DSPy is amazing but too academic. We need a dead-simple way to pipe LangSmith traces into our system prompts without writing Python."

### 6. Schema from Gemini 2
```json
{
  "trace_meta": {
    "trace_id": "req_8847f",
    "task_intent": "Update user billing tier in Stripe and local DB",
    "final_outcome_status": "SUCCESS",
    "quality_score": 9
  },
  "execution_trajectory": [
    {
      "step_sequence": 1,
      "tool_invoked": "stripe_api_call",
      "llm_reasoning": "I need to fetch the customer ID first before updating the tier.",
      "inputs_passed": {"email": "ceo@example.com"},
      "outputs_received": {"customer_id": "cus_12345", "current_tier": "basic"},
      "state_delta_hash": "a1b2c3d4",
      "error_encountered": null,
      "human_intervention_required": false
    }
  ]
}
```
Key innovation: `llm_reasoning` field — Spec-Writer needs to understand the "why" not just the "what."

**Tonight's fix:** Update Step 1 search strings to use "Trace-to-Prompt" and "trajectory reflection." Inject DrillAgent + FASTRIC as seeds. Feed JSON schema into Step 4 as target implementation prototype.
