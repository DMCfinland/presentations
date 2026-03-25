# Autoresearch Protocol — Skill Self-Improvement Operating Procedure

**Purpose:** Define exactly when to write skill feedback, in what format, how to trigger the harvest
scan, and which of Patrick's 10 skills to improve first.

**Problem solved:** Skills were built with good design but never systematically improve. Feedback is
ad-hoc and manual, so high-signal corrections disappear between sessions.

**Grok council validation (session 84):** Architecture validated. NO per-use or per-failure
auto-update (statistical threshold not reached — see Anti-patterns). YES to structured feedback
capture → AI-assisted batch proposal at /harvest-cycle → human gate before applying.

---

## Pre-Mortem (documented — do not remove)

Two risks considered before writing this version:

1. **Criteria gaming on the ranking mechanism.** The Judge requested "trigger hit-rate × downstream
cost." No actual hit-rate data exists yet. Risk: invent plausible numbers to satisfy the criterion.
Resolution: state the formula, use transparent estimation for current ranks, flag where real data
would change the order. Fake precision is worse than honest estimation.

2. **Trigger 4 over-constraining.** Rewriting "outside documented scope" too narrowly (e.g. only
flags gaps if the scope section existed and was explicit) would miss real gaps in skills with thin
documentation. Resolution: anchor the test to observable behavior (did Claude Code improvise or ask
for guidance?), not to whether the SKILL.md anticipated the situation.

---

## 1. When to Write Feedback — Trigger Conditions

Write a feedback file when ANY of the following is true. Each condition is a binary YES/NO test.
No subjective judgment required. If unsure whether a trigger fires, it did not fire.

### Trigger 1: Patrick Made a Correction
**Test:** Did Patrick correct a skill output, a process step, or a rule during this session?

YES → write feedback immediately before the session ends.
NO → skip this trigger.

This is the highest-signal input. One correction = one feedback file. Do not batch across sessions —
the context is freshest now and is degraded within 1-2 sessions.

### Trigger 2: A Numbered Process Step Was Absent from the Output
**Test:** Look at the skill's Process section. Is there a numbered step that should have produced
visible output or a visible decision — and that step produced no output or decision in this session?

YES → write feedback naming the step number and what output was missing.
NO → skip this trigger.

Concrete examples of YES: /pwj Step 2 (structured intake) produced no 6-question block. /html-presentation
Step 4 (photo slot assignment) produced no assignment log. /m365-mine Step 3 (search confirmation)
produced no results count before proceeding.

Concrete examples of NO: A step was done faster than documented but produced its required output.
A step was reordered but nothing was omitted. Patrick explicitly said "skip X this time."

This trigger is about absence of documented output, not about speed or style variation.

### Trigger 3: Output Required More Than 2 Back-and-Forth Rounds
**Test:** Did Patrick send 3 or more correction messages before the output was accepted?

YES → write feedback. Multiple rounds = criteria were unclear, a rule was missing, or a reference
file needs updating.
NO → skip this trigger.

If Patrick accepted output after 2 messages or fewer, this trigger does not fire — even if the
first output was imperfect.

### Trigger 4: Claude Code Improvised Where the Skill Should Have Guided
**Test:** Did Claude Code ask Patrick for guidance, make a judgment call, or produce a workaround
during a step that the skill claims to cover — with no documented fallback in the skill for that situation?

YES → write feedback describing what guidance was needed and what the skill's Process or Rules
section says (or doesn't say) about that case.
NO → skip this trigger.

The test is observable: did something happen that required improvisation or a Patrick decision, on
a task the skill nominally covers? If yes, there is a gap — either the skill needs a new rule, or
the scope section needs tightening to exclude that case explicitly.

This is NOT triggered by: new task types clearly outside the skill's stated purpose, tasks Patrick
assigned without invoking a skill, or exploratory work where no skill applies.

### Trigger 5: A Reference File Was Missing or Wrong
**Test:** Did the skill reference a file that didn't exist, was outdated, or gave wrong guidance?

YES → write feedback flagging the specific file path and what was wrong or missing.
NO → skip this trigger.

---

### What NOT to Write Feedback For

- The skill worked as designed and Patrick accepted the output in 1-2 rounds
- Patrick stated a one-session preference ("use this phrasing just for today") — not reusable
- The session used a skill in an exploratory way with no specific deliverable

Zero feedback in a session is a correct and legitimate outcome if no trigger fired. Do not write
feedback to satisfy the protocol. Junk entries inflate the harvest-cycle scanner's frequency counts
and push real signals below the threshold.

---

## 2. Feedback Format Template

Copy-paste this block. Complete in under 60 seconds. All 6 fields are required — leave none blank.

```
skill: [skill-name]
date: YYYY-MM-DD
trigger: [1-correction | 2-step-absent | 3-multi-round | 4-improvised | 5-reference-missing]
type: [process-wrong | need-more-info | recurring-bad-output | tool-integration]
description: [1-3 sentences: what happened, what the correct behavior should be]
proposed-fix: [specific: which SKILL.md line / which reference file / which rule — or "needs Patrick input: [question]"]
```

**Filled example (Trigger 1, html-presentation):**

```
skill: html-presentation
date: 2026-03-17
trigger: 1-correction
type: recurring-bad-output
description: Patrick corrected photo assignment in Step 4 — I assigned a portrait-format photo to
  a full-bleed landscape slot. The SKILL.md Step 4 says "assign photos to slots" but does not
  require checking aspect ratio before assignment.
proposed-fix: Add rule in Step 4: "Verify aspect ratio (landscape vs portrait) matches slot type
  before assignment. If mismatch: ask Patrick for replacement — do not resize or crop."
```

**Filled example (Trigger 2, pwj):**

```
skill: pwj
date: 2026-03-17
trigger: 2-step-absent
type: process-wrong
description: Step 2 structured intake (6 questions) produced no visible block — proceeded
  directly to execution. Output required 3 correction rounds. Missing intake = missing acceptance
  criteria = wasted work.
proposed-fix: Add to Step 2: "HARD STOP — do not proceed to Step 3 until 6-question intake block
  is written and confirmed. Output the block explicitly even for familiar task types."
```

**Field guidance:**

`trigger` — the number from Section 1 that caused this file.

`type` — pick the type that determines where the fix will land:
- `process-wrong` → SKILL.md Process section needs an edit
- `need-more-info` → a new reference file is needed (name it in proposed-fix)
- `recurring-bad-output` → a new rule is needed in the Rules section
- `tool-integration` → a reference doc or MCP guide needs updating

`description` — describe the actual event, not a vague summary. Name the step number, the
specific output that was wrong or absent, and what the correct behavior should have been.

`proposed-fix` — be specific. "Add rule: check aspect ratio before assignment" is actionable.
"Improve photo handling" is not. If you don't know the fix: write "needs Patrick input: [question]."
The harvest-cycle scanner passes this field directly to Patrick as the proposed edit.

**Save path:** `~/.claude/skills/[skill-name]/feedback/YYYY-MM-DD.md`

If multiple triggers fire in one session for the same skill, write one file with multiple entries.
Use `---` as a separator between entries. Repeat all 6 fields for each entry.

---

## 3. Priority Order — All 10 Skills Ranked

### Ranking Mechanism

Formula: **Estimated trigger hit-rate × downstream workflow cost per misfire**

- **Trigger hit-rate** = estimated fraction of uses that would generate a feedback entry, based on
  observed corrections, known rule complexity, and number of documented edge cases. No actual
  per-session tracking exists yet — these are calibrated estimates. Patrick's real corrections data
  overrides any rank below.
- **Downstream workflow cost** = estimated time or money cost when the skill misfires. Client-facing
  output = higher cost (rework + relationship risk). Internal planning = lower cost.
- Skills that score high on BOTH factors rank first.

This produces a Pareto-style prioritization: fixing the top 3 skills covers the majority of total
misfire cost. Lower-ranked skills are not ignored — they just benefit less from active monitoring
until the top 3 are stable.

**Note:** Once /harvest-cycle has 5+ sessions of real feedback data, replace these estimates with
observed trigger hit-rates and re-rank. The formula stays the same; the inputs improve.

---

### Ranked Skills

**Priority 1: /html-presentation**
Ranking signal: High hit-rate (24+ documented rules, photo assignment and focal-point rules are
precision-sensitive and frequently edge-case) × High downstream cost (client-facing decks; a broken
deck requires manual rebuild by Patrick).
Rationale: Single highest-cost misfire in the portfolio. Any photo slot error, overlay text
collision, or slide structure deviation produces a deliverable Patrick cannot send.

**Priority 2: /pwj**
Ranking signal: Moderate-high hit-rate (intake step is easy to skip under time pressure; cross-family
Judge rule and Logic Refresh hard stop are recent additions) × High downstream cost (misfires
propagate into every skill output pwj validates; error amplification 17.2× without orchestrator
review, per CLAUDE.md).
Rationale: Failure here multiplies into all downstream work. The validation backbone cannot have
unmonitored gaps.

**Priority 3: /grok-spar**
Ranking signal: Moderate hit-rate (validation theater anti-pattern has already fired once; pre-loading
verdicts in format blocks is a structural temptation) × High downstream cost (a Grok spar that
pre-loads the conclusion produces zero research value — Patrick cannot use the output).
Rationale: One confirmed Patrick correction (session 73) = fast-track. The failure mode is
invisible (output looks correct but is not) which makes it the highest-risk unflagged gap.

**Priority 4: /design-teams**
Ranking signal: Moderate hit-rate (20-question intake, 3-round Red Team debate, domain adapter table
are all precision-sensitive) × High downstream cost (a wasted agent-team run costs $8-35 + 30-60
minutes of Patrick review time).
Rationale: Lower frequency than P1-P3 but each misfire is expensive. The intake step is the
single highest-leverage gate — skipping it wastes everything downstream.

**Priority 5: /agent-teams**
Ranking signal: Moderate hit-rate (200K token cliff easy to miscalculate; voting round is recent and
may be inconsistently applied; simulation detection gate is new) × Moderate downstream cost (wasted
agent run + rework, but usually catchable before client delivery).
Rationale: Frequently used. Token cliff miscalculation doubles session cost silently. Needs
active monitoring until voting round and simulation gate have 10+ confirmed applications.

**Priority 6: /m365-mine**
Ranking signal: Moderate hit-rate (MCP tool behavior changes silently; pagination rules and
compact-after-5-documents threshold are operationally precise) × Moderate downstream cost (a missed
document means incomplete mining output, which propagates to downstream build work).
Rationale: Silent drift risk — Anthropic MCP updates can change tool behavior without notification.
Feedback needed to detect when documented behavior diverges from actual behavior.

**Priority 7: /harvest-cycle**
Ranking signal: Lower hit-rate (the skill itself is simple; the failure mode is skipping the run
entirely, not misapplying it) × High downstream cost (if harvest-cycle is not run, ALL other
feedback is wasted).
Rationale: Meta-infrastructure. Not in the original 10 but included here because harvest-cycle
failure silently kills the entire autoresearch loop. Monitor for: run cadence (is it happening
every 5-10 sessions?), scanner producing zero proposals (possible sign of empty feedback folder or
scanner prompt drift).

**Priority 8: /create-skill-bi**
Ranking signal: Low-moderate hit-rate (2KB SKILL.md limit and scope-assessment step most likely to
be skipped under time pressure) × Moderate downstream cost (a poorly structured new skill propagates
errors into all future uses of that skill — compounding over time).
Rationale: Each misfire here creates a new source of future misfires. Lower immediate cost but
higher long-term compounding risk.

**Priority 9: /service**
Ranking signal: Low hit-rate (new skill, limited real-world runs) × Moderate downstream cost (service
setup errors can block infrastructure; error diagnostic patterns may be incomplete for services
beyond n8n/Supabase).
Rationale: Low frequency means low absolute misfire count, but the pattern library is incomplete
by design. Feedback here expands coverage rather than fixing known errors.

**Priority 10: /task-complete**
Ranking signal: Low hit-rate (self-critique checklist is structurally hard to misapply) × Low
downstream cost (main failure mode is skipping the skill entirely, caught by Trigger 2).
Rationale: Simple skill. Rarely misfires. The only active risk is complete omission, which
Trigger 2 covers.

**Priority 11: /load-context**
Ranking signal: Low hit-rate (decision table with clear binary rules) × Low downstream cost (main
failure mode is over-loading context, caught by session cost feedback before it compounds).
Rationale: Least likely to misfire. Monitor passively; no active feedback investment needed until
Tier A skills are stable.

---

## 4. Quality Bar — Measurable Before/After Test

### The Core Test

When an edit is applied to a SKILL.md based on a feedback pattern, record the baseline in the
feedback file before applying the edit:

> "Feedback type [type] fired [N] times in [M] uses = [baseline %]. Target: <20% over next 10 uses."

**PASS:** The same trigger type does not fire again within 10 uses after the edit was applied
(misfire rate drops to <1 in 10 for that pattern = <10%).

**FAIL:** The same trigger type fires again within 5 uses after the edit was applied.

A FAIL means the proposed fix did not address the root cause. Write a new feedback file and
escalate to Patrick with the pattern history.

### Why 10 Uses and Not Benjamin's 700-900

Benjamin's threshold (700-900 trials for 5% signal reliability in benchmark performance) applies
to detecting subtle continuous improvements. Here the question is binary: "Did a specific documented
step produce its required output — yes or no?" Ten binary observations are sufficient to detect
systematic non-compliance. These are not performance benchmarks; they are compliance checks.

### Specific Measurable Tests by Skill

**html-presentation:** PASS = no photo aspect-ratio corrections in 5 consecutive deck builds.
FAIL = any "wrong slot type" Patrick correction after the aspect-ratio check rule is applied.

**pwj:** PASS = 6-question intake block appears in output for 5 consecutive Standard/High/Critical
tasks. FAIL = intake block absent on any non-Routine task after the hard-stop rule is applied.

**grok-spar:** PASS = zero pre-loaded verdicts in OUTPUT FORMAT block across 5 consecutive Grok
prompts. FAIL = any Patrick correction for validation theater in that window.

**agent-teams:** PASS = voting round documented in output for all multi-wave team launches across
5 consecutive runs. FAIL = voting round omitted on any multi-wave run after the rule is applied.

**design-teams:** PASS = Step 0 intake (all 20 questions) completed before Wave 1 launch for
3 consecutive runs. FAIL = intake abbreviated or skipped on any run after the rule is applied.

---

## 5. Integration with /harvest-cycle Step 1b

### When Step 1b Runs

Step 1b (AI-assisted feedback scan) runs at the start of every /harvest-cycle call, before the
main PENDING-PATTERNS review, whenever feedback files exist in any skill's feedback/ directory.

### The Scan Prompt

The Sonnet subagent spawned in Step 1b reads all feedback files and produces:

| skill | pattern | frequency | tag | proposed-edit |

Tags:
- `monitor-only` — fired fewer than 3 times for this skill
- `propose-edit` — fired 3 or more times → present to Patrick for approval
- `flag-for-human` — judgment required (cannot be auto-proposed; present as a question)

### Adjusted Threshold for Low-Frequency Skills

For skills used fewer than 15 times total (likely: create-skill-bi, design-teams, service):
- 1 fire + `source: patrick` tag → `propose-edit` immediately (Patrick corrections are highest signal)
- 2 fires of same type + no Patrick tag → `propose-edit`
- 1 fire + no Patrick tag → `monitor-only`

This prevents the scanner from ignoring high-signal corrections in rarely-used skills because the
denominator is small.

### How the Scanner Routes Fixes

The scanner reads the `type:` field to route the proposed edit:
- `process-wrong` → proposes a specific SKILL.md Process section edit
- `need-more-info` → proposes a new reference file name and purpose
- `recurring-bad-output` → proposes a new rule for the Rules section
- `tool-integration` → proposes an update to a specific reference file

The `proposed-fix:` field content is passed directly to Patrick as the proposed edit text. If the
field says "needs Patrick input: [question]", the scanner tags it `flag-for-human` and presents
the question first.

### After Patrick Approves

Apply the edit to SKILL.md. Archive processed feedback files to:
`~/.claude/skills/[skill]/feedback/archived/YYYY-MM-DD.md`

`monitor-only` entries stay in the active feedback folder until they either reach the threshold
or Patrick explicitly discards them.

### Cadence

Run /harvest-cycle every 5-10 sessions. Feedback files may accumulate for up to 10 sessions before
being scanned. This is by design — the goal is human-gated batch improvement, not per-session
micro-edits.

---

## 6. Anti-Patterns

### Anti-Pattern 1: Per-Use Auto-Update (Benjamin's 700-900 Trial Threshold)

**What it is:** Editing a SKILL.md after every use where something went slightly wrong, without
waiting for a pattern to emerge.

**Why it fails:** Benjamin's math (Grok council, session 84) shows 700-900 trials are needed to
detect a 5% improvement in benchmark performance with statistical reliability. Patrick has 5-50 uses
per skill — well below this threshold. Per-use auto-update produces a SKILL.md that reflects the
last session's idiosyncrasies, not genuine improvement patterns. A skill updated after every use
oscillates instead of improving.

**The right behavior:** Capture feedback immediately (high signal), propose edits in batch at
/harvest-cycle (low noise), apply only after Patrick approval (human gate).

### Anti-Pattern 2: The Closed-Loop Trap (Lucas's Closed-Loop Trap)

**What it is:** A system that only learns from its own outputs — Claude Code writes feedback,
Claude Code scans the feedback, Claude Code proposes edits, Claude Code applies them — with no
external signal breaking the loop.

**Why it fails:** Lucas's finding (Grok council, session 84) is that a closed loop amplifies the
system's existing biases rather than correcting them. If Claude Code consistently makes the same
type of error (e.g. skipping intake steps under time pressure), its feedback normalizes that error
rather than flags it — because the scanner has no ground truth. The loop becomes self-reinforcing
around whatever the model does by default.

**The right behavior:** The human gate at /harvest-cycle is not overhead — it IS the signal that
breaks the closed loop. Patrick's approval or rejection of a proposed edit is the external reference
the scanner cannot provide. This is why Patrick corrections are tagged `source: patrick` and
fast-tracked to Tier A after 1 confirmation. Do not skip the human gate even when the proposed
edit seems obvious.

### Anti-Pattern 3: Feedback Written Too Late

**What it is:** Waiting until a future /harvest-cycle session to write feedback about a correction
that happened several sessions ago.

**Why it fails:** Context collapses. The specific step that failed, the exact wording Patrick used,
and the reason the current rule was insufficient — all available immediately, degraded within 1-2
sessions. Late feedback produces "photo step was wrong" instead of "assigned portrait photo to
full-bleed landscape slot because SKILL.md Step 4 has no aspect ratio check."

**The right behavior:** Write feedback before the session ends. Trigger 1 (Patrick correction)
must fire within the same session.

### Anti-Pattern 4: Feedback Without a Proposed Fix

**What it is:** Writing feedback that describes what went wrong but leaves `proposed-fix` blank
or vague ("improve this section").

**Why it fails:** The harvest-cycle scanner cannot propose an edit without a starting point. Vague
feedback → vague proposed edit → Patrick rejects or ignores → no improvement. The scanner is a
frequency counter and presentation layer, not a diagnosis engine.

**The right behavior:** Every entry must have a specific proposed fix, even if imperfect.
"Add rule: verify aspect ratio before slot assignment in Step 3" is proposable.
"needs Patrick input: should this check happen in Step 3 or Step 2?" routes to Patrick as a question.
"Improve photo step" is not acceptable.

### Anti-Pattern 5: Writing Feedback to Satisfy the Protocol

**What it is:** Writing near-empty or low-quality feedback entries because the session "should"
have one.

**Why it fails:** Junk entries inflate the scanner's frequency counts, pushing real signals below
the `propose-edit` threshold. Zero feedback in a session is the correct and legitimate outcome
when no trigger fires.

**The right behavior:** Only write when a trigger fires (Section 1). Quality signal, not volume.

---

## 7. Skill Registry

All skills with feedback path and current monitoring priority:

| Priority | Skill | Feedback Path | Self-Improvement Block in SKILL.md |
|----------|-------|---------------|------------------------------------|
| 1 | /html-presentation | `~/.claude/skills/html-presentation/feedback/` | Yes |
| 2 | /pwj | `~/.claude/skills/pwj/feedback/` | Yes |
| 3 | /grok-spar | `~/.claude/skills/grok-spar/feedback/` | Yes |
| 4 | /design-teams | `~/.claude/skills/design-teams/feedback/` | Yes |
| 5 | /agent-teams | `~/.claude/skills/agent-teams/feedback/` | Not documented — add minimal block |
| 6 | /m365-mine | `~/.claude/skills/m365-mine/feedback/` | Yes |
| 7 | /harvest-cycle | `~/.claude/skills/harvest-cycle/feedback/` | Meta — monitor cadence, not content |
| 8 | /create-skill-bi | `~/.claude/skills/create-skill-bi/feedback/` | Yes (abbreviated) |
| 9 | /service | `~/.claude/skills/service/feedback/` | Yes |
| 10 | /task-complete | `~/.claude/skills/task-complete/feedback/` | Not documented — add minimal block |
| 11 | /load-context | `~/.claude/skills/load-context/feedback/` | Not documented — add if needed |

Skills without a self-improvement block (/agent-teams, /task-complete) cannot route feedback
through the harvest-cycle scanner until a minimal block is added. Copy the format from
`~/.claude/skills/pwj/SKILL.md` self-improvement section. Add before next /harvest-cycle run.

---

## Appendix: Trigger Decision Tree (quick reference)

```
Session ended. Did any of these happen?

1. Patrick corrected a skill output, step, or rule?      → YES: write feedback (Trigger 1)
2. A numbered Process step produced no visible output?   → YES: write feedback (Trigger 2)
3. Patrick sent 3+ correction messages before accept?    → YES: write feedback (Trigger 3)
4. Claude Code improvised or asked for guidance on a     → YES: write feedback (Trigger 4)
   step the skill claims to cover?
5. A skill reference file was missing or wrong?          → YES: write feedback (Trigger 5)

None of the above? → Write nothing. Zero is correct.
```

---

Version: 2.0 | Rewritten: 2026-03-17
Source: PWJ loop Worker Round 2 — Judge fail analysis applied
Architecture validated: Grok council session 84 (Benjamin threshold + Lucas closed-loop)
Judge fail fixes: Template shown with filled examples (F1), ranking mechanism explicit (F2),
Trigger 2 rewritten to "numbered step absent from output" (F3a), Trigger 4 rewritten to
"improvised where skill claims to cover" (F3b).
