# Session-Bridge Protocol — The 140K Pivot
<!-- created: session-89 | updated: session-100 | legacy detail: legacy-protocols.md -->

## What
At 140K tokens: harvest session learnings → generate Cognitive Snapshot → build Bridge Prompt
→ validate → open fresh session. Result: 100% reasoning fidelity at only 15K tokens.

**Full rationale + Cognitive Snapshot XML template:** `_shared/best-practices/legacy-protocols.md`

---

## Trigger Logic

```
< 120K   → continue; /compact optional at phase break
120-140K → YELLOW ZONE: flag + suggest Session Bridge soon
> 140K   → TRIGGER this protocol
> 180K   → FORCE bridge (200K pricing cliff 20K away — no exceptions)

Architecture Pivot (≥12 human interventions OR paradigm shift in last 20K tokens):
> 100K   → ESCALATE: "Pivot detected — recommend Session Bridge now"
```

---

## The Protocol: 6 Steps

**Step 1 — Harvest first**
Pattern harvest → `_shared/best-practices/` + `_index.yaml`. GEPA correction harvest if Patrick corrected anything. Bridge quality depends on harvest quality.

**Step 2 — Confidence check (human gate)**
For each major decision: state WHY + what was rejected? If blurry → STOP. Ask Patrick.
LOW CONFIDENCE BRIDGE = worse than /compact. Never silently produce one.

**Step 3 — Generate Cognitive Snapshot**
Preserve: active thought train, execution plan (pre-derived), reasoning insurance (WHY for
≥3 decisions), unresolved tensions (with why_deferred + resolve_trigger), mental model anchors,
files state. Full XML template: `legacy-protocols.md`.

**Step 4 — Build Bridge Prompt via `/prompt-creator --bridge`**
Skip disk cold-load — Snapshot IS the context. PWJ Planner Gate still runs. Genius Check
runs in `--mode bridge`.

**Step 5 — Genius Check (bridge mode)**
(1) Reasoning continuity: WHY captured for ≥3 major decisions?
(2) Unresolved tension coverage: all deferred decisions have why_deferred + resolve_trigger?
(3) Re-derivation risk: flag the 1 decision most at risk of being re-derived differently.

**Step 6 — Deliver and close**
Deliver as single copy-paste block. Update CURRENT-STATUS.md. Close old session.

---

## Bridge Prompt Quality Standard

All bridge prompts MUST comply with the **Search & Destroy** standards in:
`_shared/best-practices/pwj-bridge-prompt-quality.md`

Key rules (non-exhaustive):
- Done criteria must test production failure, not presence
- Judge prompt must contain exact phrase: "You CANNOT PASS until you have attempted to break this with an edge case"
- **First-pass PASS with zero contradictions = judging failure** — embed in every Judge prompt

---

## PWJ Bridge Prompt Self-Check
<!-- 6-item binary checklist — primary verification tool — run BEFORE submitting any bridge prompt -->

All items are binary (yes/no by inspection — no judgment required).

- [ ] **1. DMC context by path:** Bridge references `DMC-CORE-CONTEXT.md` by exact path
  (`_shared/DMC-CORE-CONTEXT.md`), not embedded. Embedding = inflation risk.

- [ ] **2. Production failure criterion:** At least one Done criterion tests production failure
  (not presence). e.g., "Show 2 traces where output DIFFERS" — not "include a section."

- [ ] **3. CANNOT PASS phrase:** Judge prompt contains exact phrase:
  "You CANNOT PASS until you have attempted to break this with an edge case"
  Paraphrase does not satisfy this item.

- [ ] **4. Interface Spec for coupled sessions:** If this bridge triggers work another session
  depends on — explicit Interface Specification section documents the upstream/downstream contract.

- [ ] **5. Signal-based criteria:** Time-based triggers paired with statistical floor:
  Clopper-Pearson / Bootstrap 95% CI, N≥99 per subclass, upper bound <3%.

- [ ] **6. Bridge prompt length:** Bridge prompt file under 150 lines.
  (Assumes DMC context loaded via `/read`, not embedded.)
  Flag as technical debt if over 150 — do not reject.

---

## Anti-Patterns

- **Silent low-confidence bridge:** Never generate when reasoning chains are blurry.
- **Bridge before harvest:** Always harvest FIRST. Bridge quality depends on it.
- **Bridge without Execution Plan:** Summary-only bridge = worse version of /compact.
- **Ignoring Unresolved Tensions:** Not captured = re-derived differently = silent regression.

---

## Source
session: 89 (2026-03-18) | updated: session-100 (2026-03-19)
designed_with: Gemini + Grok + Claude Code | applies_to: all portfolio companies, any session >120K
tier: A (promoted from B, Opus Review 7)
