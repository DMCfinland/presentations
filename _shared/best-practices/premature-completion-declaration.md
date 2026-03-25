# Pattern: premature-completion-declaration
<!-- last_updated: session-28 -->
**Source:** Session 30 (2026-02-18) — Get to Know Järvisydän project
**Severity:** HIGH — cascading downstream impact

## What
Never declare a phase or milestone complete unless it meets its own defined success criteria. "Some work was done" is not the same as "phase complete." Partial outputs do not equal delivered outputs.

## Why
Downstream phases assume upstream phases delivered what they promised. If Phase 1 data is incomplete, Phase 2 builds on a weak foundation — and the gap compounds. It also creates false confidence: the team believes the work is done when it is not, so the gaps go unfixed and untracked.

## When to Apply
Any time you are about to mark a checkbox, write "COMPLETE," or close out a deliverable or phase. Apply the check before, not after.

## Rule
Before marking anything complete, re-read the success criteria for that phase. Ask: does every criterion pass? If any criterion fails, the status is "IN PROGRESS" or "PARTIAL" — never "COMPLETE." Partial credit is not completion.

## Evidence
Get to Know Järvisydän, Phase 1: profiles were declared COMPLETE when fill rate was 54-80% per company. The defined success criterion was "Patrick can explain what each company does in 2 minutes." Profiles had 16-28 unfilled gaps each, missing operational KPIs (room count, capacity), and zero governance fields filled. Phase 2 (knowledge hub) would have been built on that incomplete foundation.

Anti-pattern: checking off a phase because the template was created and partially filled, rather than because the exit criteria were met.

## Implementation
- Write the success criteria in the phase definition, before work begins
- At phase close: list each criterion, mark pass/fail explicitly
- Use status labels: COMPLETE / IN PROGRESS / PARTIAL / BLOCKED — never a binary
- If a phase is PARTIAL, document exactly what is missing and what remains to be done
