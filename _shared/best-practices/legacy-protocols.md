---
name: legacy-protocols
description: Archived detail from session-bridge-protocol.md — full Cognitive Snapshot XML template, step-by-step bridge instructions, and token-management rationale from sessions 89-94. Load on demand only.
type: reference
---

# Legacy Protocols — Session Bridge Detail
<!-- Extracted from session-bridge-protocol.md at session-100 refactor -->
<!-- Active file: _shared/best-practices/session-bridge-protocol.md -->

---

## Why Session Bridge Beats /compact

/compact destroys:
- Intermediate reasoning chains (the "why" before the conclusion)
- Unresolved tensions (deferred decisions + their deferral logic)
- Rejected alternatives (what was tried and why it failed)

A fresh session with a 15K optimized warm pack + Cognitive Snapshot preserves all of this.
Cost delta: ~$0.075 — negligible. Quality delta: significant for strategic reasoning.

**Source:** session-length-strategy.md (Mistral-verified, 9.9/10 skepticism score)

---

## Cognitive Snapshot — Full XML Template

```xml
<cognitive_snapshot>
  <meta>
    <session_tokens_at_pivot>[N]K</session_tokens_at_pivot>
    <pivot_reason>[Yellow Zone / Architecture Pivot / 200K cliff / Manual trigger]</pivot_reason>
    <tokens_invested_in_planning>[N]K — DO NOT re-derive. Execute as follows.</tokens_invested_in_planning>
  </meta>

  <active_thought_train>
    <!-- Where we are in the problem space RIGHT NOW — one paragraph -->
    [Current position in the problem space]
    <next_immediate_step>[Exact first action the new session takes]</next_immediate_step>
  </active_thought_train>

  <execution_plan status="perfected">
    <!-- The Perfected Plan. Pre-derived. New session executes, does not re-plan. -->
    We spent [N]K tokens establishing this plan. Execute it via PWJ. Do not re-derive.
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]
    <!-- If PWJ is the execution strategy: include PWJ Done Criteria here -->
  </execution_plan>

  <reasoning_insurance>
    <!-- The WHY — the part /compact destroys -->
    <decision id="1">
      <what>[Decision made]</what>
      <why>[Reasoning chain — not just the conclusion]</why>
      <rejected_alternatives>[What was considered + why it lost]</rejected_alternatives>
    </decision>
    <!-- Repeat for every major decision. Min 3 entries for high-stakes sessions. -->
  </reasoning_insurance>

  <unresolved_tensions>
    <tension id="1">
      <what>[Open question or unresolved conflict]</what>
      <why_deferred>[Specific reason not yet resolved]</why_deferred>
      <resolve_trigger>[What event/info would resolve it]</resolve_trigger>
    </tension>
  </unresolved_tensions>

  <mental_model_anchors>
    <!-- The "biases" the new agent must inherit -->
    <anchor>[Assumption the new session must never question]</anchor>
  </mental_model_anchors>

  <files_state>
    <written>[Files that exist and contain validated work — do not re-create]</written>
    <pending>[Files that need to be created in the new session]</pending>
    <read_before_writing>[Files changed this session — read before touching]</read_before_writing>
  </files_state>

  <done_state>
    <!-- 100% complete looks like this — PWJ-style binary checkboxes -->
    - [ ] [Done criterion 1 — MECHANICAL]
    - [ ] [Done criterion 2 — MECHANICAL]
    - [ ] [Done criterion 3 — JUDGMENT, flag if uncertain]
  </done_state>
</cognitive_snapshot>
```

---

## Step 1 — Harvest (full detail)

```
1a. Pattern Harvest → _shared/best-practices/ + _index.yaml
    (write a 5-line note if anything new happened this session)

1b. Session Reasoning Harvest → append reasoning_harvest: YAML to session log
    Format: 3-5 compressed reasoning chains (the WHY, not decisions)
    Include MemPO Memory Decision Block per entry

1c. GEPA Correction Harvest → if Patrick made ANY correction this session
    → run gepa-correction-harvest.md → propose rule → add to _index.yaml

Why first: The bridge is only as good as the knowledge it incorporates.
A bridge generated before harvest = stale snapshot.
```

## Step 2 — Confidence Check (full detail)

```
For each major decision made this session:
  - Can I state the WHY clearly? (not just the conclusion)
  - Can I list what was rejected and why?

If ANY decision has blurry reasoning → STOP.
Flag: "I can see we decided [X] but the reasoning chain is unclear.
Patrick, confirm: why did we reject [alternative]?"
Wait for answer before proceeding.

LOW CONFIDENCE BRIDGE = worse than /compact. Never silently produce one.
```

## Steps 3-6 — Summary

See active file `session-bridge-protocol.md` for current condensed protocol.
Full detail archived here when needed for new-session orientation.

---

## What the Next Session Looks Like

The new session receives the Bridge Prompt and:
1. Reads the Cognitive Snapshot (not disk files — the snapshot IS the state)
2. Confirms all Mental Model Anchors
3. Checks unresolved tensions — resolves any it can before starting execution
4. Runs PWJ on the Execution Plan (Worker gets pre-derived plan, executes it)

**Result:** Pure Execution Engine. No re-planning. No re-deriving. Zero reasoning drop-off.

---

## Genius Check — Bridge Mode (full)

```
1. REASONING CONTINUITY
   Does the prompt capture the WHY behind ≥3 major decisions?
   FAIL: any decision stated without its rejection chain.

2. UNRESOLVED TENSION COVERAGE
   Are ALL deferred decisions listed with why_deferred + resolve_trigger?
   FAIL: any tension without both fields.

3. RE-DERIVATION RISK
   Could the new agent re-derive any decision differently?
   Find the 1 decision most at risk — flag it.
```

---

source: session-89 (original) | archived: session-100
