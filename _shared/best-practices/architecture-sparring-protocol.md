---
name: architecture-sparring-protocol
description: How to use Grok + Gemini in parallel for architecture validation — gets independent perspectives that catch blind spots Claude misses
type: project
source: session-88
session: 88
---

# Architecture Sparring Protocol

## When to Use
Before locking any major technical architecture decision (>2 weeks of build work).
Especially when: schema design, backend technology choice, staff workflow design, data model.

## Protocol

### Round 1: Build the plan internally (Claude)
Draft the architecture. Document decisions and rationale.

### Round 2: Grok Heavy (4-agent)
- Use MAD 2-round iterative protocol
- Lucas = devil's advocate (highest value output)
- Ask: "What is the single assumption that collapses this if wrong?"
- Ask: "Walk me through Day 1, 09:00 — where does this break?"

### Round 3: Gemini (separate window, no prior context)
- Fresh window = no anchoring to Grok's conclusions
- Ask same core questions independently
- "Be contrarian. No validation."

### Round 4: Compare
- Where Grok and Gemini agree independently = high confidence finding
- Where they disagree = the real decision point, dig deeper
- Where both say "you're overbuilding" = listen carefully

---

## Session 88 Results — What the Protocol Caught

| Finding | Source | Value |
|---------|--------|-------|
| Passive Verification Collapse | Both unanimous | Prevented system that staff would never use |
| Unified interactions table | Both Geminis independently | Prevented 6-table schema nightmare |
| TypeScript > n8n when AI codes | Both unanimous | Prevented wrong backend choice |
| Shadow Mode (Outlook Categories) | Gemini 1 | Breakthrough — zero behavior change |
| Drafts Folder (no Add-in) | Gemini 2 | Saved 2-4 weeks of Add-in development |
| Graph webhook expires 3 days | All three | Prevented show-stopper production failure |
| Pre-LLM filter | Gemini Pro | Saves 40% Claude costs |

**6 sessions in one day = entire architecture validated before a single line of code was written.**

---

## Rules

- Never pre-load answers in prompts — Grok/Gemini must reason independently
- Fresh windows for each major question — prior context anchors responses
- "Contrarian only, no validation" produces 3x more value than "review this"
- Ask for Day-1 walkthrough — forces concrete failure mode identification
- Verify all numbers independently — Grok math errors are common
- Lucas's specific challenges are the highest-value output
- Where agents disagree = dig deeper, don't average
