# Multi-LLM Design Cycle — Pattern

**Discovered:** 2026-03-17 | **Source:** Patrick session 85 (Mistral Judge design)
**When to use:** Designing any high-stakes prompt, system architecture, or critical workflow

---

## What it is

A structured cycle using 3 different AI families as independent specialists to design, validate, and harden a system — without any one model being able to confirm its own output. Each model contributes what it's best at.

---

## The Cycle (as executed in session 85)

```
Step 1: DECISION RESEARCH (Grok Heavy — 4-agent council)
  → Open question: which model/approach/architecture is best?
  → Harper finds live data, Benjamin models costs, Lucas argues against consensus
  → Output: decision with benchmark evidence

Step 2: CROSS-VALIDATION (Gemini Deep Research)
  → Same question, zero context from Grok's answer
  → Independent verdict + any NEW insights Grok missed
  → Output: confirmed decision OR genuine disagreement to analyze

Step 3: DESIGN (Gemini — first domain expert)
  → Give Gemini the confirmed decision + ask it to design the system/prompt/architecture
  → Output: v1 design artifact

Step 4: STRESS-TEST (Grok Heavy — adversarial)
  → Give Grok the v1 design: "find every failure mode"
  → Harper finds real-world attack patterns, Benjamin models failure math, Lucas finds the single patch that breaks the whole system
  → Output: hardened v2 design + anti-patterns documented

Step 5: PATCH + INTEGRATE (Gemini — follow-up)
  → Give Gemini Grok's failure modes: "patch these and add integration code"
  → Output: v2 design + implementation artifacts (code, shell scripts)

Step 6: DOCUMENT (Claude Code — this system)
  → Synthesize all outputs into permanent reference files
  → Index in _index.yaml, wire into /pwj SKILL.md or relevant skill
```

---

## Why it works

| Role | Model | Why |
|------|-------|-----|
| Decision arbiter | Grok Heavy | Multi-agent debate, live data via Harper, math via Benjamin, devil's advocate via Lucas |
| Cross-validator | Gemini Deep Research | Independent family, web search, catches what Grok missed |
| System designer | Gemini | Strong at structured prompt design + integration code |
| Adversarial tester | Grok Heavy | Lucas finds the single patch that breaks everything — best red-team |
| Synthesizer | Claude Code | Persistent files, indexing, wiring into skills |

Each model has genuine blind spots. No single model red-teams itself effectively.

---

## Results from session 85 application

**Subject:** Mistral Large 3 Judge system prompt for PWJ loop

| Round | Action | Key output |
|-------|--------|-----------|
| Grok R1 | API privacy research | All paid-tier APIs exclude training by default |
| Grok R2 | EU model availability | Vertex AI = MED risk (CLOUD Act), Mistral = LOW risk |
| Gemini R1 | Cross-validation | Independently confirmed Mistral. New: "sycophancy bias" in Flash |
| Grok R3 | Flash vs Mistral benchmarks | Mistral Elo 1428 vs Flash 1412, composite 81.2 vs 78.4 |
| Gemini R2 | System prompt v1 | Zero-trust + JSON + skepticism_score (1-10 subjective) |
| Grok R4 | Stress-test v1 | 6 failure modes found. Skepticism score → formula. Master-key exploit. Rating indeterminacy. |
| Gemini R3 | Revision prompt + shell loop | Worker revision protocol + agent_loop.sh + Criteria Hardener offer |

**Total cost:** Grok free tier + Gemini free tier + ~$2 Claude Code = near-zero for a production-quality Judge system

---

## When to use this cycle

- Designing a critical prompt that will run autonomously (Judge, planner, evaluator)
- Choosing between two technical options with EU compliance implications
- Building any system where Claude's own blind spots could cause failures
- Any "meta" work: improving the improvement system itself

## When NOT to use

- Routine tasks (use /pwj alone)
- Time-sensitive work (cycle takes 1-2 hours of human facilitation)
- Tasks where you already have 3+ validated LESSONS entries with the same tags

---

## Anti-patterns

- **Circular validation:** Asking Grok to research "what Gemini says" → Grok simulates Gemini's opinion. Fix: Harper uses web_search for real papers, not model opinions.

- **Same-model PWJ theater (BAD EXAMPLE — session 89, 2026-03-18):** PWJ loop run entirely within one Claude Code session. Lead played Planner + Worker + Judge. Worker self-reported "all 7 criteria PASS on round 1." No Grok stress-test (Step 3.5 skipped). No Mistral Judge call made. Result: theatrical compliance — criteria satisfied on paper, but Criterion 6 ("thresholds grounded in session log data") accepted on assertion, logs never read. Logic Refresh forced by Patrick → Grok found 5 real criteria gaps → Mistral Large 3 Judge gave 9.9/10 skepticism score on the corrected run. **Rule:** When you see PWJ producing all-PASS on round 1 with no external model involvement, that is the anti-pattern, not the result. External model at Step 3.5 OR Step 5 is mandatory for Standard+ tasks.
- **Pre-loading conclusions:** If you tell Gemini "we already chose Mistral, validate it" → you get validation theater. Give each model the open question.
- **Single-family confirmation:** Two Claude subagents confirming each other = same training data, same blind spots. Cross-family validation is the whole point.
- **Skipping the adversarial step (Grok stress-test):** Gemini v1 was good but had 6 exploitable gaps. The stress-test found all of them.

---

## Grok vs Gemini debate (future use)

Patrick idea (session 85): put Grok and Gemini in direct debate — give both the same question and have them respond to each other's arguments. Not implemented yet. Potential format:
1. Grok R1 → paste to Gemini: "Here is Grok's analysis. What did it get wrong?"
2. Gemini response → paste to Grok: "Gemini challenges these points. Defend or concede."
3. Synthesize final verdict from the disagreements.

---

## Files produced in session 85

- `cross-llm-judge-gdpr.md` — model decision record
- `mistral-judge-system-prompt.md` — full Judge system + Revision Prompt + shell loop
