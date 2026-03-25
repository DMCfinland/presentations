# Pattern: mid-session-checkpoint
<!-- last_updated: session-28 -->
**Source:** Session 27 (2026-02-18)
**Validated:** Referenced in sessions 27 and context pack; applicable to all mining sessions

## What
In sessions longer than 30 minutes, save intermediate results to files at natural breakpoints rather than waiting until session end. Long mining sessions (60-90 min) risk losing all progress if context runs out, the browser crashes, or the session is interrupted. Files written mid-session survive any interruption; context window contents do not.

## When to Apply
Any mining session expected to run more than 30 minutes. Any session doing multi-search extraction (more than 3-4 distinct searches). Any session where re-running the work would cost more than $1 or take more than 15 minutes.

## Evidence
Session 27 (Finland DMC mining): a 75-minute session produced 6 search passes worth of results. Natural checkpoint: after each search pass, paste results to a `mining-outputs/session-N/checkpoint-{search}.md` file. If the session had crashed at minute 60, the first 5 passes would have been recoverable. Without checkpoints, total loss.

Anti-pattern: treating a long mining session as a single atomic unit. Sessions are not atomic — context windows close, browsers crash, API timeouts happen.

## Implementation
- Save after every major search pass to `mining-outputs/session-N/checkpoint-{N}.md`
- Use a minimal format: paste raw results, add a one-line label
- Do not wait to "clean up" before saving — dirty checkpoints are better than lost work
- At session end, compile checkpoints into the final `mining-report.md`
- Keep checkpoint files until the session is fully compiled and committed
