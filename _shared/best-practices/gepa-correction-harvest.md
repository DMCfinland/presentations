---
name: gepa-correction-harvest
description: Turn every mid-session correction into an auto-generated Tier-B rule — prevents the same correction class from recurring
type: feedback
---

# GEPA-Style Correction Harvest

## What
Inspired by DSPy's GEPA optimizer (2025), which converts human text feedback into automatic prompt rewrites.
Applied here as a manual pattern: every correction Patrick makes becomes a proposed Tier-B rule.

The correction → rule loop:
1. Mid-session correction occurs (Patrick says "no, Teams not Slack")
2. At session END, run the GEPA reflection block (below)
3. Claude proposes the rule text
4. Patrick approves → file written to `_shared/best-practices/`
5. After 3 confirmed uses → promote to CLAUDE.md Tier A

## Why
Without this, the same class of assumption error recurs in future sessions because:
- The correction is stored in session logs (not searchable at session start)
- The next session starts cold and re-derives the same wrong default

With this, each correction pays dividends across all future sessions on the same topic.
Estimated leverage gain: corrections per session 3→1 = ~10-12 min saved, 6-8× → ~11× ratio.

## The GEPA Reflection Block (run at session END if any correction occurred)

```
## CORRECTION HARVEST (run if any mid-session correction occurred)

List every correction made this session. For each:

**Correction [N]:**
- Assumption error: [What did Claude default to? E.g. "Slack as capture channel"]
- Company reality: [What is correct? E.g. "DMC uses Teams/M365, Slack not installed"]
- Root cause: [Why did Claude make this assumption? E.g. "External source used Slack; no context card loaded"]
- Proposed Tier-B rule (one sentence): [E.g. "DMC capture channel = Teams #crm-capture; never recommend Slack"]
- Applies to: [all portfolio / DMC only / specific project]
- Proposed file name: [e.g. "dmc-stack-overrides.md"]

OUTPUT: Draft rule text ready for Patrick to approve or edit.
```

## Where proposals go
- Write proposed rule text to `_shared/best-practices/gepa-proposals.md` (running list, append-only)
- Patrick reviews at next Opus session or when proposals exceed 5 items
- Approved rules → new Tier B file + _index.yaml entry
- 3 confirmed uses → promote to Tier A (CLAUDE.md)

## Difference from session-reasoning-harvest
- **session-reasoning-harvest:** captures WHY decisions were made (architectural reasoning for spawn prompts)
- **gepa-correction-harvest:** captures WHAT was wrong (assumption errors, company-specific overrides)
Both run at session end. Different outputs, different files.

## Status
Tier B (new — session 64, Grok 4-agent validation). First application: session 65.

## Source
session: 64, source: grok-4-agent-debate (GEPA-style correction loop)
research_basis: DSPy GEPA optimizer (Stanford, 2025) — human text feedback → automatic prompt rewrite
applies_to: all portfolio companies
