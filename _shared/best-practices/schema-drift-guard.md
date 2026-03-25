---
name: schema-drift-guard
description: Replace silent fallback (??/||) with explicit SchemaDriftError when reading upstream schema fields. Prevents invisible production failures when upstream systems change their output.
type: pattern
tier: B
source: session-109 (Gemini Q4 audit on S5 resolveRule6Priority)
---

# Schema Drift Guard Pattern

## Rule

Never use `?? ''` or `|| ''` as a fallback for fields that come from an upstream system's output schema. Silent fallbacks hide schema changes.

**Wrong:**
```typescript
const raw = output.email_body_raw ?? '';
```
If S4 drops `email_body_raw`, this silently passes `''` and bypasses all downstream logic with zero error signal.

**Correct:**
```typescript
if (output.email_body_raw === null || output.email_body_raw === undefined) {
  throw new SchemaDriftError(
    'S4 schema drift: email_body_raw missing — update this function before redeploying.'
  );
}
const raw = output.email_body_raw;
```

## Why

Upstream systems (S4, n8n workflows, external APIs) change their output schemas. A silent fallback:
1. Produces no error, no log, no escalation
2. Returns wrong data that passes all downstream validation
3. Corrupts CRM/database with plausible-but-wrong records
4. Is never caught until a human notices a pattern weeks later

## When to apply

- Any function that reads a field from an upstream system's output contract
- Any TypeScript function with `??` or `||` on an interface field (not on a user-input field)
- Especially: priority resolution, routing, classification functions

## When NOT to apply

- User-input fields (legitimately optional)
- Internal computed fields where null is a valid state

## Implementation

1. Wire the SchemaDriftError into the flywheel/alert channel so Patrick sees it immediately
2. Document which upstream contract the field comes from (e.g., "S4Output.email_body_raw — defined in S4-PROGRESSIVE-AUTONOMY-SPEC.md")
3. In the error message: name the field, name the upstream system, give the fix action

**Why:** Discovered when Gemini found that resolveRule6Priority() in S5 would silently bypass all Rule 6 enforcement if S4 dropped email_body_raw. The `?? ''` fallback made it look correct. No test would catch it.
