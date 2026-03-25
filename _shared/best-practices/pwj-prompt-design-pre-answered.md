---
name: pwj-prompt-design-pre-answered
description: PWJ execution prompts must contain all 6 Planner intake answers pre-filled from the planning session. Session N plans → Session N+1 executes Worker immediately. Prompts without pre-answered intake cause theater or mid-session Planner re-runs.
type: feedback
confidence: 0.8
source: session-99 (patrick correction — PWJ theater audit)
---

# PWJ Prompt Design: Pre-Answered Intake

Planning happens in Session N. Execution happens in Session N+1. The bridge prompt IS the completed plan.

**The rule:** Every session prompt that calls for PWJ execution must contain all 6 intake answers pre-filled. Session N+1 starts with a brief confirm/adjust check (≤3 questions), then immediately spawns Worker. No intake re-run.

**Why:** This session ran PWJ theater because the bridge prompt had acceptance criteria but was missing tier, constraints, output format, and escalation trigger. Worker ran without a complete spec. Grok cross-validation caught 3 critical bugs (Rule 10 ordering, Rule 8 data corruption, stopping-vs-correction ambiguity) that self-declared PASS missed.

**How to apply:**

Every PWJ session prompt must contain:
```
## PWJ EXECUTION — [TASK NAME]

## PLANNER ANSWERS (confirmed S[N] — adjust only if scope has changed)
1. Goal: [one sentence]
2. Done criteria:
   - [ ] Criterion A (verifiable)
   - [ ] Criterion B
   - [ ] Criterion C — including: [specific output types, e.g. execution traces]
3. Tier: [1/2/3 + rationale]
4. Constraints: [numbered list]
5. Output format: [exact structure — sections, not content]
6. Escalation trigger: [specific condition → specific action]

## SOURCE FILES (Worker reads all before starting)
1. ~/full/path/to/file1.md

## COGNITIVE SNAPSHOT (key facts Worker needs)
[2-4 bullet points of non-obvious context]

## JUDGE PROMPT (copy-paste to Grok/Mistral after Worker completes)
[pre-written external judge prompt]

---
Session start: confirm planner answers or flag any scope change. Then immediately spawn Worker.
```

**Reference implementation:** `~/1658HoldingsOy-AIFiles/_drafts/SESSION-99-PROMPT.md`
This file has all 6 answers pre-filled, source files listed, Judge prompt ready to copy-paste.

**Anti-pattern to avoid:** Session bridge with acceptance criteria only. Missing tier = no safety framing. Missing output format = Worker guesses structure. Missing Judge prompt = theater risk at session end.

**Applies to:** All session prompts designed for PWJ execution (any project type).
