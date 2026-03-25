---
name: spec-activation-engineering
description: Three-layer anchoring to make a spec discoverable from multiple entry points — prevents specs from dying in _drafts/
type: feedback
---

A spec in `_drafts/` is invisible. Good specs die there every session.

**The three-layer anchoring pattern:**

1. **Relocate** — move from `_drafts/` to the canonical project folder (`project-files/[project]/`)
2. **Cross-reference upstream** — add a "Next build layer" section to the upstream spec that triggered it (e.g., S3 spec gets a pointer to S5)
3. **Pipeline map** — create or update a `PIPELINE-MAP.md` in the design folder. ASCII diagram showing the full chain. This is the entry point new developers and future sessions hit first.
4. **Register in CORE-CONTEXT** — one entry in DMC-CORE-CONTEXT.md (or equivalent canonical reference file). File pointer + one-line description of what section to read for what purpose.

**Why:** Future sessions need to find the spec without knowing it exists. Pipeline map = passive discovery. Cross-reference = active discovery when reading adjacent specs. CORE-CONTEXT = explicit loading.

**When to apply:** Any spec that (a) took more than 30 min to produce, (b) has a build dependency chain, and (c) will be read by a developer who doesn't have session context.

**Source:** S102 (2026-03-20) — REGRESSION-FLYWHEEL-SPEC.md was in `_drafts/`, needed S5 developer session to find it.
