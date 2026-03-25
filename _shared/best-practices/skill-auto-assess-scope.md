# Pattern: Skill Auto-Assess Scope (Don't Ask User to Pick)
<!-- last_updated: session-57 -->

**name:** skill-auto-assess-scope
**source:** patrick (Session 57, 2026-03-10)
**tier:** B
**confidence:** 0.7

## What
When a skill-creation skill presents scope options (Minimal / Balanced / Deep), the skill should auto-assess scope from the user's intent — not ask the user to pick A/B/C.

## Why
- Asking "pick A, B, or C" forces the user to understand your framework
- The skill has enough context from the request to determine complexity
- State your assessment and let user confirm or adjust: "This is Balanced because [reason]."

## When to Apply
- Any skill that has scope levels or complexity tiers
- Any HITL where the AI can infer the answer from context

## Source Session
Session 57: Patrick corrected /create-skill-bi — "the skill should identify the necessary scope"
