---
name: Time-Boxed Integration Specs with PREREQUISITE Blocks
description: When time constraint is tight (≤5 min), separate one-time setup from per-session steps to avoid constraint failure
type: feedback
source: patrick + empirical (session 104 S3 Anti-Anchoring)
---

# Time-Boxed Integration Specs with PREREQUISITE Blocks

## Rule

Any integration spec with a per-session time constraint **≤5 minutes** MUST have a "PREREQUISITE (one-time setup)" section declared explicitly. This block is NOT counted in the per-session time total.

**Total time calculation:**
```
Total Time = PREREQUISITE setup time (one-time, amortized) + per-session steps total
Constraint applies to per-session steps only, not amortized setup.
```

## Why

Setup costs — locale configuration, environment variable validation, script install, test file creation — are real. But they happen ONCE per session, not per email. If you include them in the per-session time estimate, you guarantee failure on tight constraints.

**Session 104 example:** S3 Anti-Anchoring regex spec had a 5-minute per-session constraint. Integration spec included "export LANG=fi_FI.UTF-8" as Step 2. If counted in per-session time, total was 5:30 (FAIL). Moving locale setup to PREREQUISITE: 30 seconds one-time, then 4:00 per-session (PASS).

## How to Apply

In the "Integration into [Workflow]" section of your spec:

1. Add a `## PREREQUISITE (One-Time Setup)` header BEFORE the numbered steps
2. List all setup tasks with time estimates
3. Note that this section is completed once, not per-session
4. Then add `## Per-Session Steps` with the numbered steps
5. Calculate total as: PREREQUISITE + per-session

**Template:**

```markdown
### Integration into Mining Workflow

#### PREREQUISITE (One-Time Setup)
Complete this once before running the first mining session:

1. Enable UTF-8 encoding in Terminal
   - Edit ~/.zshrc: add `export LANG=fi_FI.UTF-8`
   - Test: run `echo "Äöå" | od -c` to verify UTF-8 survival
   - Time: 30 seconds

2. Install regex validator script
   - Copy `validate-patterns.sh` to ~/bin/
   - Chmod +x ~/bin/validate-patterns.sh
   - Time: 1 minute

**Total PREREQUISITE time: 1:30 (one-time, not per-session)**

#### Per-Session Steps (≤5 minutes)

1. Copy email from Outlook to temp file
   - Time: 30 seconds

2. Run validator + pattern strip
   - `bash ~/bin/validate-patterns.sh temp-email.txt > stripped.txt`
   - Time: 1 minute

3. Paste stripped output into claude.ai
   - Time: 30 seconds

4. Continue mining with debiasing prompt
   - Time: 2 minutes

**Total per-session time: 4:00** ✓ (under 5-minute constraint)

**Grand total: 1:30 (first session only) + 4:00 per session after**
```

## When to Apply

- Integration spec has per-session time constraint (e.g., "must complete in ≤5 min")
- Setup cost identified (environment variable, script install, file validation)
- Constraint is TIGHT (within 1 minute of the stated limit)

If constraint is loose (e.g., ≤30 minutes) and setup is <2 minutes, no need to separate. Keep clarity as the goal.

## Anti-Pattern

**Wrong — mixes setup and per-session:**
```
1. Set LANG=fi_FI.UTF-8 in Terminal (30s)
2. Copy email to temp file (30s)
3. Run validator (1m)
...
Total: 5:30 (FAIL — exceeds constraint)
```

**Right — separates them:**
```
PREREQUISITE: Set LANG=fi_FI.UTF-8 (one-time, 30s)

Per-session steps:
1. Copy email (30s)
2. Run validator (1m)
...
Total per-session: 4:00 (PASS)
```

## Source

Session 104, S3 Anti-Anchoring System Spec. Judge criterion C6 (integration ≤5 min) failed at 5:30 with locale setup included. Fix: move setup to PREREQUISITE. Total per-session then = 4:00. Pattern extracted because this constraint-fixing technique is reusable across all tight-timeline specs.
