# Cold Start Discovery Mode

**Name:** cold-start-discovery-mode
**Source:** session 92 (2026-03-18) | source: patrick
**Type:** Tier B (new — validate over 3+ uses before Tier A)

## What

When a new session opens WITHOUT a Bridge Prompt, force "Discovery Mode" BEFORE any file reads.
Three strategic questions (one per message), locked into an immutable Session DNA block:

1. **Purpose** — Mikä on tämän uuden ikkunan tarkka tarkoitus?
2. **Business Goal** — Mitkä ovat strategiset syyt ja tavoitteet?
3. **Definition of Done** — Milloin työ on 100% valmis? (2-4 binary criteria)

## Why

Without Discovery Mode, session goal is inferred from CURRENT-STATUS.md "Next 3 Tasks" —
a lagging indicator. ~30% of CRM sessions (79-88) drifted from actual user intent within
5 turns because CURRENT-STATUS.md said "CRM Wave 2B" but user wanted something else.

**Discovery BEFORE file reads:** User intent must frame which files are relevant, not vice
versa. Loading 10-15K tokens of wrong-domain context creates stale framing that subtly
influences all subsequent questions.

**Session DNA is immutable:** A DoD that changes mid-session = no measurable DoD at all.
Judge agents cannot evaluate against a moving acceptance criterion.

## When to Apply

- Any time /prompt-creator runs WITHOUT a Bridge Prompt being received
- Any cold start (new window, no cognitive snapshot)
- NOT for Bridge Mode (Skip — Cognitive Snapshot IS the context)
- NOT for known continuation with explicit task reference in first message (Warm Start shortcut — TBD, see Tension A in technical-dna-report-session-92.md)

## Session DNA Format (canonical)

```yaml
session_dna:
  purpose: "[Exact reason this window was opened — 1 sentence]"
  business_goal: "[Strategic value this session delivers — 1 sentence]"
  definition_of_done:
    - "[Binary criterion 1 — YES/NO]"
    - "[Binary criterion 2 — YES/NO]"
  topic_signal: "[keywords for warm pack routing]"
  locked_at: "Step 0"
  mutable: false
```

## Open Questions (validate in sessions 93-95)

- Tension A: Should explicit task reference in first message skip Discovery? Risk of recreating drift.
- Tension B: Provisional DoD for Tier 3 exploratory sessions — sound or not?
- Use /grok-spar to stress-test Tension A before promoting to Tier A.
