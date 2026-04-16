# Grok Expert Spar — Dashboard Plan
Date: 2026-04-11 | Model: Expert (spar mode)
Chat: https://grok.com/chat?rid=f1a7620c-ddc6-4a45-b6ff-7f13f824c7ca

## VERDICT: "Textbook spreadsheet-script Frankenstein"

## Kill Vectors Grok Identified (all lethal)

1. **Flask reads Excel on EVERY request** — openpyxl overhead on every tab switch. Needs in-memory model.
2. **Odottaa column missing** — first run crashes or silent None values. No migration path.
3. **Tilaushistoria date text parsing** — '13.-14.3.2026' Finnish ranges doom the classifier + traffic light. One malformed row = garbage decisions or silent exceptions.
4. **Excel open during /log_call** — PermissionError on macOS. Data loss. Silent failure. Rep thinks it saved. It didn't.
5. **pip3 install on every startup** — slow, version conflicts, pollutes global env.
6. **5-level traffic light + manual toggle** — CRM-level complexity for CRM-naive user. Will be ignored.
7. **No search/filter** — tabs alone insufficient.

## Additional Fatal Flaws
- No in-memory data model
- No error handling / user feedback (500 = white screen)
- No backup / versioning before writes
- No validation (bad dates, duplicates accepted silently)
- No column migration on first run
- No audit trail
- No config file — all hard-coded
- No tests for traffic light algorithm
- Business logic assumptions undefined (calendar vs work days, Finnish holidays, timezone)

## What Breaks First
1. Excel file lock on /log_call (daily occurrence)
2. Date parsing exceptions on real Tilaushistoria data
3. Rep confusion from 5-color + manual toggle

## Grok's Recommended Fix (VERDICT)
> "Load Excel ONCE at startup into pandas DataFrame. Run dashboard against in-memory data. Background thread auto-saves every 60s to backup Excel + timestamped versions. All writes queued with file-lock check + UI warning. Column migration on first run. V2.1: migrate to SQLite."

## What to Cut
- 7-category classifier (make read-only derived, don't trust for decisions)
- Drop to 3-color traffic lights
- Make whose-turn optional / auto-infer
- Drop Obsidian auto-note for V2 → copy-paste button instead
- Consider Streamlit instead of raw Flask + openpyxl

## Claude's Assessment
Grok is right on the data layer. The Excel-open-during-write problem WILL happen day 1. The fix (load once into memory, queued writer, file-lock warning) is the correct approach and adds ~1 hour to build time. Streamlit suggestion rejected (Patrick explicitly chose custom HTML). SQLite in V2.1 is a great idea — aligns with existing "Supabase when web-facing" plan.
