---
name: Multi-Model Research Pipeline — Claude→Grok→Gemini→Build→Grok
description: Reusable research pipeline assigning each AI model to its comparative advantage — broad search, cross-validation, specialist deep-dive, build, final validation
type: workflow
confidence: 0.7
uses: 1
last_used: session-111
source: session-111 (CoS bot research)
---

## The Pattern

When building a novel system (no prior template exists), run research through 4 model stages before building:

```
Stage 1 — Claude Code (broad search)
  Agent: general-purpose with web search
  Task: 25-40 searches across all research blocks
  Output: comprehensive research report (~500-700 lines)
  Why Claude: large context, structured output, file write

Stage 2 — Grok Heavy (cross-validation)
  Template: Cross-Validation (Template 3)
  Task: challenge every hypothesis in Stage 1 output
  Output: Gap report — confirmed / questionable / missing / agent conflicts
  Why Grok: independent 4-agent council, live web search, Benjamin verifies numbers

Stage 3 — Gemini (specialist deep-dive)
  Task: one focused question where Gemini has unique depth
  Why Gemini: strongest on product specifics, platform documentation, EU regulation
  Output: structured answer with step-by-step guidance

Stage 4 — Claude.ai (build)
  Task: synthesize all 3 prior stages into deliverable
  Why claude.ai: Projects + web search + longest context for synthesis

Stage 5 — Grok Heavy (deliverable validation)
  Template: Cross-Validation (Template 3) on the deliverable
  Task: challenge the actual system prompt / spec / plan before deploying
```

## When to Apply

- Building a new persistent system with no prior template (first AI assistant, new workflow, new architecture)
- Any research question where single-model bias is a real risk
- When citations need independent verification (Grok's Benjamin runs code on numbers)
- When the topic spans domains (cognitive science + product + compliance = S111)

## Why Not One Model for Everything

Each model has a blind spot:
- Claude Code: no independent challenge of its own output
- Grok: weaker on structured file output, no Project context
- Gemini: weaker on strategic synthesis across many sources
- Claude.ai: no live web search by default in Projects

The pipeline exploits comparative advantage, not model ranking.

## Cost Estimate

Stage 1 (Claude Code agent, 35 searches): ~$3-5
Stage 2 (Grok, free tier Heavy): $0
Stage 3 (Gemini Advanced): $0
Stage 4 (Claude.ai, ~$0.10 session): ~$0.10
Stage 5 (Grok, free tier): $0
Total: ~$3-5 for a comprehensive research + build cycle

## Evidence

Applied: CoS bot research (S111). Output: 710-line research report → Grok found 3 questionable hypotheses + 2 missing angles → Gemini confirmed native memory is project-scoped → claude.ai built Session 2 prompt → Grok validated system prompt through 4 additional rounds (S112-S115). End result: CoS bot v0.5 deployed.

## Anti-patterns

- Don't run all 5 stages for simple single-domain questions (overkill)
- Don't skip Stage 2 (Grok cross-val) — that's where hidden assumptions surface
- Don't pre-load Grok with preferred conclusions (Template 3 anti-pattern: validation theater)
- Stage 3 (Gemini) should be ONE focused question, not everything
