# Opus Prompt: Best Practices Operationalization Plan

**Purpose:** Ask Opus to design a plan that embeds our accumulated DOs and DON'Ts into daily workflow and decision-making, so they're impossible to skip.
**Estimated cost:** ~$3-5 (single query, substantial context)
**Where to send:** claude.ai (new Project or conversation)

---

## Context to paste BEFORE the question

Paste the contents of these two files as context:
1. `_shared/best-practices/ai-deployment-principles.md` (~180 lines — 18 principles + 18 anti-patterns)
2. `_shared/best-practices/context-window-failure-modes.md` (~100 lines — 4 failure modes + decision framework)

---

## The Prompt

```
You are helping design an operationalization plan for a family portfolio holding company (1658 Holdings Oy, Finland). The CEO manages 10 companies with ~50 employees total. He uses Claude Code as his daily AI orchestration tool.

PROBLEM:
We have accumulated valuable best practices and anti-patterns from mining 195 YouTube AI strategy videos. They're documented in files. But best practices in files = shelf dust. Nobody reads them at the right moment. We need to make them structurally impossible to skip.

CURRENT ARCHITECTURE:
- CLAUDE.md files load automatically on every Claude Code session (this is the enforcement point)
- Holdings-level CLAUDE.md: loaded on every session across all companies
- Company-level CLAUDE.md: loaded when working on that specific company
- _shared/best-practices/ folder: 9 files of documented patterns (only read if explicitly told to)
- _shared/prompts/ folder: ready-to-send prompts for claude.ai mining sessions

THE ASSETS TO OPERATIONALIZE:
[The two files I pasted above contain:]
- 18 positive principles (AI deployment DOs)
- 18 anti-patterns (DON'Ts that prevent $50K mistakes)
- 4 context window failure modes with evidence
- A decision framework for context window sizing
- Company-specific applicability matrix (CEO / DMC team / Hotel ops / All)

THE CONSTRAINT:
CLAUDE.md files must stay concise. They're loaded on EVERY session. We can't paste 180 lines of principles into every CLAUDE.md — that wastes context on routine tasks. But we need the right principles to surface at the right moment.

WHAT I NEED FROM YOU:
Design a complete operationalization plan that answers:

1. TRIGGER-BASED LOADING: How should principles load contextually?
   - What goes into CLAUDE.md permanently (the 5 most universal rules)?
   - What gets loaded conditionally (e.g., "before any new AI initiative, read X")?
   - How do company-specific CLAUDE.md files get their relevant subset?

2. DECISION GATES: What checkpoints should exist?
   - Before starting a new AI project/initiative
   - Before an expensive query (>$5)
   - Before deploying AI to staff
   - Before making architectural decisions
   - What does each gate look like? (checklist? prompt? file to read?)

3. ANTI-PATTERN EARLY WARNING: How do we catch ourselves falling into anti-patterns?
   - Can Claude Code detect when we're about to commit an anti-pattern?
   - What phrases/patterns in our requests should trigger warnings?
   - Example: "Let's load all 195 files" → trigger context-window-failure-modes.md

4. PROGRESSIVE INTEGRATION: What's the rollout sequence?
   - Phase 1: What to add now (this week)?
   - Phase 2: What to add after testing (next month)?
   - Phase 3: What to add when onboarding new companies?

5. COMPANY-SPECIFIC RULES: Using the applicability matrix from the principles doc, draft:
   - 5-7 lines to add to the Holdings CLAUDE.md (universal rules)
   - 5-7 lines to add to Finland DMC CLAUDE.md (team-specific rules)
   - Template for future company CLAUDE.md files

6. MEASUREMENT: How do we know this is working?
   - What signals indicate principles are being applied?
   - What signals indicate they're being ignored?
   - How do we update/retire principles that prove wrong?

DELIVERABLE FORMAT:
Write the plan as a structured markdown document with clear sections, specific file paths, and copy-paste-ready CLAUDE.md additions. Include the exact text to add to each file — don't just describe it, write it.

IMPORTANT CONSTRAINTS:
- This is a prompt/config file project, NOT software. All outputs are .md files.
- Don't propose building apps, dashboards, or monitoring tools.
- The enforcement mechanism is CLAUDE.md files + human discipline.
- Keep CLAUDE.md additions SHORT. If it's more than 10 lines, it's too long.
- Principles must earn their place — only include what prevents real mistakes.
```

---

## Expected Output
A plan document (~2000-3000 words) with:
- Copy-paste-ready CLAUDE.md additions for holdings and DMC
- Decision gate checklists
- Anti-pattern trigger patterns
- Rollout timeline
- Measurement criteria

## After Receiving the Answer
1. Save to `_shared/best-practices/operationalization-plan.md`
2. Review the proposed CLAUDE.md additions
3. Implement Phase 1 immediately (add rules to CLAUDE.md files)
4. Test for one week, then implement Phase 2
