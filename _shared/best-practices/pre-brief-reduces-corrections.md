---
name: pre-brief-reduces-corrections
description: Capture standing company context at session START to eliminate mid-session correction rounds
type: feedback
---

# Pre-Brief Reduces Corrections

## What
Before mining any external source, include a 5-line company context brief in the session opener:
- Which tools are in use (e.g. Teams not Slack, M365 not Google)
- Staff names and roles relevant to this session
- Any standing overrides from prior corrections (e.g. "memory migration = email mining of existing DMC data")
- Locked decisions that might conflict with source recommendations

## Why
External sources (Substack articles, community comments, tutorials) use generic stack assumptions. Without company context, Claude defaults to those assumptions and produces output that needs correction. Each correction = re-read + re-write + approval round.

In session 63-64 (DMC CRM mining), 3 corrections occurred:
- Teams not Slack (source recommended Slack; DMC is M365)
- Memory migration framing (source used generic phrasing; DMC-specific = email mining of existing profiles)
- Staff adoption punchline (Patrick's own language needed saving verbatim)

All three corrections were AFTER outputs were drafted. Pre-brief would have prevented all three.

## When to apply
Any session where you're mining an external source (Substack, YouTube, community comments, docs).
Any session where source recommendations might conflict with existing company decisions.

## Expected gain
2-3 fewer correction rounds per mining session = ~15-20 min saved, cleaner first-draft outputs.
Estimated leverage improvement: 6-8x → 8-12x (same AI actions, fewer human re-review cycles).

## Format — Short version (inline in session opener)
Add after "status" but before paste:
```
COMPANY CONTEXT (overrides source defaults):
- Tools: [Teams/M365, not Slack/Google. n8n, not Zapier. Supabase, not Firebase.]
- Staff: [names + roles if relevant]
- Standing overrides: [any prior corrections that apply to this source]
- Locked decisions: [D-numbers that might conflict with source]
Flag any recommendation in the source that contradicts this card before applying it.
```

## Format — Full version (load context card file)
Each company has a `_context-card.md` at the company folder root. Load it at session START:
```
Read [CompanyName]-AIFiles/_context-card.md first.
Flag any assumption from the external source that contradicts that card before applying it.
```

Company context cards:
- `FinlandDMCOy-AIFiles/_context-card.md` — tech stack, staff, locked decisions, GDPR, standing overrides
- Template: `_shared/templates/context-card-template.md` (create per new company during onboarding)

## Source
session: 64, source: patrick (implied by correction pattern), confirmed by leverage analysis
upgrade: session 64, Grok 4-agent debate — full context card + flagging instruction added
applies_to: all portfolio companies
