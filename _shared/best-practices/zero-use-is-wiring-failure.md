# Pattern: Zero-Use Is Wiring Failure, Not Content Failure
<!-- last_updated: session-32 -->

**name:** zero-use-is-wiring-failure
**source:** patrick (Session 32, 2026-02-18)
**tier:** B

## What
A BP file with 0 uses should not default to "archive." The absence of use may reflect that the LLM has no activation path to the file — it was never linked in any warm pack Deep Dive or Knowledge Trigger.

## Why It's a Problem
Archiving a valuable file because it was never loaded treats a wiring failure as a content failure. The file may contain exactly the right knowledge — it just was never reachable. Archiving it confirms the failure rather than fixing it.

## The Check Before Archiving
1. Is the file referenced in any warm pack Deep Dive section?
2. Is it mentioned in any Knowledge Trigger?
3. Does `_index.yaml` have a clear `use_when` that matches a common project type?

If NO to all three: wire it in first (add to relevant Deep Dive sections). Observe 1-2 sessions. Then decide archive vs keep.

## When to Apply
Before any Opus Review recommendation to archive a BP file based solely on 0 uses count.

## Source Session
Session 32, 2026-02-18. Opus Review recommended archiving `kb-utilization-strategy.md` (0 uses). Patrick pointed out the Tier 1/2/3 decision map and grep keywords are genuinely useful — the file had simply never been linked in any warm pack's activation path. Fix: wired into 4 Deep Dive sections. Content preserved, problem solved.
