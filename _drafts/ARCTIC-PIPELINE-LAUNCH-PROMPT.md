# Arctic Cruises Pipeline — Initializer Launch Prompt
# Paste this into a new Claude Code session opened with: claude --dangerously-skip-permissions
# Or use: claude --dangerously-skip-permissions -p "$(cat ARCTIC-PIPELINE-LAUNCH-PROMPT.md)"

---

## PASTE THIS INTO A FRESH CLAUDE CODE SESSION:

```
You are the Arctic Cruises autonomous document pipeline orchestrator.

Your mission: build 7 commercial documents for Arctic Cruises (luxury Finland lake cruise) 
using the DDSC protocol. All work is autonomous — no human input required until MANIFEST-COMPLETE.md 
is written.

WORKING DIRECTORY: ~/1658HoldingsOy-AIFiles/

LOAD YOUR FULL BRIEF:
Read this file completely before any other action:
~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR-V2.md

EXECUTE:

TURN 1 — DECLARE:
- Confirm bridge loaded
- State the phase plan (4 waves + preflight + final validation)
- Confirm turn budget: 18 turns

TURN 2 — PREFLIGHT:
Create these two files from the bridge spec (exact content in bridge):
1. ~/1658HoldingsOy-AIFiles/output/PRICING-MASTER.json
2. ~/1658HoldingsOy-AIFiles/output/PRODUCT-BRIEF.md
Also create output/wave-1a/, output/wave-1b/, output/wave-2/, output/wave-3/, output/wave-4/ directories.

TURN 3 — DELEGATE WAVE 1 (both agents simultaneously, ONE message):
Launch TWO subagents in parallel:
- Agent 1A (mode: bypassPermissions): Build arctic-cruises-b2b-flyer.html → output/wave-1a/
- Agent 1B (mode: bypassPermissions): Build FAM invitation + programme → output/wave-1b/
Each subagent receives PRODUCT-BRIEF.md injected verbatim at the top of its prompt.
HOLD — do not process results until BOTH complete.

TURN 4 — WAVE 1 GATE CHECK:
Run bash checks (file size + required strings per bridge spec).
If any fail: fix inline with Edit tool. Mark as "FIXED W1".
Progressive commit: git add output/wave-1a/ output/wave-1b/ && git commit -m "Wave 1 complete"

TURN 5 — DELEGATE WAVE 2:
Launch subagent (mode: bypassPermissions): Build arctic-cruises-operator-prd.html → output/wave-2/
Subagent receives PRODUCT-BRIEF.md + reads PRICING-MASTER.json.
HOLD until complete.

TURN 6 — WAVE 2 GATE CHECK + COMMIT:
Check pricing consistency (grep). Fix if needed. Commit.

TURN 7 — DELEGATE WAVE 3:
Launch subagent (mode: bypassPermissions): Build booking PRD + operations brief → output/wave-3/
HOLD until complete.

TURN 8 — WAVE 3 GATE CHECK + COMMIT:
Check 5 email templates present. Check Airtable schema present. Fix if needed. Commit.

TURN 9 — DELEGATE WAVE 4:
Launch subagent (mode: bypassPermissions): Compile Knowledge Bible from ALL wave outputs → output/wave-4/
Subagent reads: wave-1a + wave-1b + wave-2 + wave-3 outputs + arctic-cruises-b2c.html.
Target: 8,000-12,000 words. HOLD until complete.

TURN 10 — FINAL VALIDATION:
Run cross-document consistency bash checks (pricing + FAM dates + seal language).
Then run Gemini cross-document audit:
  bash ~/run-gemini.sh --prompt-file /tmp/arctic-final-judge.txt --output-file /tmp/gemini-final-audit.txt

TURN 11 — APPLY GEMINI FIXES:
If Gemini returns CONFLICTS or MISSING → fix the specific files inline. Re-check.

TURN 12 — FINAL COMMIT:
Copy all outputs from output/wave-N/ to root directory.
git add all 7 final files + output/ + PRICING-MASTER.json + PRODUCT-BRIEF.md
git commit -m "Arctic Cruises: full launch document suite (autonomous pipeline S237)"

TURN 13 — WRITE MANIFEST-COMPLETE.md:
Document all 7 files with sizes, gate results, and Gemini audit score.
Write to ~/1658HoldingsOy-AIFiles/MANIFEST-COMPLETE.md

TURN 14 — DONE. Report: "Arctic Cruises pipeline complete. 7 documents built, validated, committed."

RULES:
- All pricing from PRICING-MASTER.json ONLY. Never invent prices.
- "possible natural observation" for seals. Never "will see a seal" or "guaranteed sighting."
- Seal language violations in any output = hard stop + immediate fix before proceeding.
- Progressive commits after each wave — never wait for all 4 to finish before first commit.
- If a wave subagent fails: restart that wave's subagent only (Waves 1-N-1 already committed).
```

---

## QUICK REFERENCE

| Output file | Wave | Size target |
|-------------|------|-------------|
| arctic-cruises-b2b-flyer.html | 1A | >5KB |
| arctic-cruises-fam-invitation.html | 1B | >2KB |
| arctic-cruises-fam-programme.html | 1B | >3KB |
| arctic-cruises-operator-prd.html | 2 | >8KB |
| arctic-cruises-booking-system-prd.md | 3 | >3KB |
| arctic-cruises-laura-operations-brief.md | 3 | >5KB |
| arctic-cruises-knowledge-bible.md | 4 | >40KB (~10K words) |

## GATE CHECK CHEATSHEET (bash, run in ~/1658HoldingsOy-AIFiles/)

```bash
# Wave 1 pricing check
grep -c "€320\|€960\|€2,080" output/wave-1a/arctic-cruises-b2b-flyer.html

# Wave 2 net rate consistency with Wave 1
diff <(grep -o "€[0-9,]*" output/wave-1a/arctic-cruises-b2b-flyer.html | sort) \
     <(grep -o "€[0-9,]*" output/wave-2/arctic-cruises-operator-prd.html | sort)

# Seal language violation check (must return 0 for all)
grep -ci "will see a seal\|guaranteed.*seal\|see a seal" output/wave-1a/*.html output/wave-1b/*.html output/wave-2/*.html

# FAM date consistency
grep -h "August\|September\|July" output/wave-1b/*.html | sort | uniq -c

# Wave 4 word count
wc -w output/wave-4/arctic-cruises-knowledge-bible.md
```

---

*Launch prompt v1.0 — S231 2026-04-15*
*Bridges: SESSION-BRIDGE-S237-ARCTIC-ORCHESTRATOR-V2.md (primary) + S232-S236 (wave specs)*
