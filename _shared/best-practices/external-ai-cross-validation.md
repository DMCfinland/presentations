# External AI Cross-Validation Pattern
**Tier:** B
**Source:** Session 49 (2026-02-22)
**Status:** First use — validate across 2 more sessions before Tier A promotion

---

## What
After completing an internal AI synthesis (e.g., 7-agent orchestrated run), send the primary deliverable to an external AI (e.g., Grok, GPT-4) for independent evaluation. Prompt it to challenge freely — no pre-answered questions.

## Why It Works
Internal synthesis agents share the same model family, same training priors, and same source documents. An external AI brings genuinely different priors and may flag compliance/regulatory gaps (EU AI Act, industry-specific laws) that the internal synthesis didn't index against. In the DMC 2.0 run, Grok identified EU AI Act Art 50 obligations and variable API cost modeling as gaps — both were validated as genuine additions.

## How to Prompt (Critical)
- Give the full deliverable document (Goal Document, synthesis output, etc.)
- Do NOT pre-answer questions in the prompt ("do you think X is a problem?")
- Say: "Challenge our course of action where you see risks, gaps, or wrong assumptions. Don't hold back."
- Ask for specific categories if needed: regulatory gaps, financial model gaps, timeline risks, missing architectural decisions, exit criteria

## After Getting the Response — Quality-Check Required
External AI outputs MUST be verified against source documents before use. Common failure modes found in session 49:
1. **Math errors** — Grok made a 10x error in financial projection (€1,875 vs €18,742). Always check formulas.
2. **Scope conflicts** — Grok's BP_08 scope excluded Whisper, which the Goal Document lists as required minimum. Cross-reference external AI recommendations against the internal synthesis decisions.
3. **Missing context** — Grok didn't know about 1658 Holdings portfolio as second-tenant pipeline, which made it overstate tenant acquisition risk. Provide org context upfront or push back explicitly.

## When to Apply
- After completing an orchestrated synthesis team run
- Before finalizing a strategic plan with real-world consequences (legal, financial, contracts)
- When internal analysis is high-confidence (≥4.0/5) — external validation is the final check, not a substitute for strong internal work

## When NOT to Apply
- Early exploration or first-draft synthesis — external AI will flag too much; internal coherence isn't established yet
- Routine operational tasks — cost/benefit is too low
- When source documents contain confidential PII — use anonymized summaries only per GDPR web search rule

---

*Pattern: external-ai-cross-validation | source: session 49 | 2026-02-22*
