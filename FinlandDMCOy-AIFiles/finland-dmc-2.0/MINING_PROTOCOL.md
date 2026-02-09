# Mining Session Protocol — Finland DMC 2.0

Standard process for all 5 mining sessions in claude.ai (Opus + M365 connector).

---

## Session Start

Paste this into a new Opus conversation at the start of every mining session:

```
I'm starting Mining Session [N]: [Topic].

Before we search anything, create a Mining Report document with these sections:

- SESSION INFO: date, session number, topic, model used
- SEARCH LOG: every search query tried + result quality (good/partial/empty)
- EXAMPLES FOUND: table of candidate emails/proposals with date, client, type, quality rating
- SELECTED EXAMPLES: the ones I chose as best (with full text saved)
- EXTRACTED LANGUAGE: best lines, phrases, patterns pulled from real emails
- PATTERNS IDENTIFIED: structural, tonal, content patterns across emails
- STATISTICS: counts, distributions, averages from the data
- DECISIONS MADE: choices about what to include/exclude and why
- GAPS & QUESTIONS: things we couldn't find or need to investigate
- RAW DATA CAPTURED: any important data points for later CRM/database use

Update this report after every search we do and every decision I make.
When I say "show report" — display the current state.
When I say "save checkpoint" — output the full report for me to copy/save.
```

---

## During Session

### After every M365 search:
- Log the query and result quality in SEARCH LOG
- Note: good (usable results), partial (some relevant), empty (nothing useful)

### After reviewing results:
- Update EXAMPLES FOUND table with candidates
- Rate each: 1 (weak) to 5 (excellent)

### After picking a winner:
- Move it to SELECTED EXAMPLES with full text preserved
- Tag it with type, client, date, and why it was selected

### After extracting language:
- Add best lines/phrases to EXTRACTED LANGUAGE
- Note which email they came from

### Every ~20 minutes:
- Claude should remind you: "Time for a checkpoint save?"
- Say "save checkpoint" to get the full report for copy/paste backup

---

## Session End

Paste this when done:

```
Session complete. Generate:

1. FINAL MINING REPORT — the complete updated report with all sections filled
2. EXTRACTED FILES — each selected example as a separate text block I can save
3. NEXT SESSION PREP — what the next mining session should look for based on gaps
4. RAW DATA EXPORT — any client names, dates, statistics worth capturing for CRM later

Format the final report so I can paste it directly into a file
in mining-outputs/session-[N]-[topic]/ on my computer.
```

---

## Per-Session Specific Additions

Each session adds tracking sections specific to its domain.

### Session 1: Client Communications — OUTBOUND

Add to the Mining Report:

```
- EMAIL TYPE TRACKER:
  | Type | Searched? | # Found | Best Example? | Quality |
  |------|-----------|---------|---------------|---------|
  | New inquiry response | | | | |
  | Follow-up | | | | |
  | Complaint response | | | | |
  | Cold outreach | | | | |
  | Returning client | | | | |
  | Booking confirmation | | | | |
  | Price quote | | | | |
  | Logistics/quick answer | | | | |
```

**Session 1 goal:** One excellent example email per type + tone guide + best lines library.

---

### Session 2: Inbound Emails

Add to the Mining Report:

```
- INQUIRY TYPE TAXONOMY:
  | Type | Count | % of Total | Example Client | Typical Ask |
  |------|-------|-----------|----------------|-------------|
  | Group leisure | | | | |
  | Corporate/incentive | | | | |
  | Tour operator/B2B | | | | |
  | Conference/MICE | | | | |
  | Individual/small group | | | | |
  | Repeat booking | | | | |
  | Complaint | | | | |
  | Logistics question | | | | |
  | Supplier comms | | | | |
  | Cold inbound | | | | |

- SOURCE MARKET BREAKDOWN:
  | Country/Region | Count | Language | Channel | B2B/B2C |
  |---------------|-------|----------|---------|---------|
  | | | | | |
```

**Session 2 goal:** Inbound email classification system + source market map + "always ask for" checklist.

---

### Session 3: DMC Router

Add to the Mining Report:

```
- TASK CLASSIFICATION TRACKER:
  | Email # | Date | From | Type | Routed To | Correct? | Notes |
  |---------|------|------|------|-----------|----------|-------|
  | 1 | | | | | | |
  | 2 | | | | | | |
  ...
  | 30 | | | | | | |

- CLASSIFICATION ACCURACY: __/30 correct on first pass
- MISSED CATEGORIES: types that don't fit current taxonomy
```

**Session 3 goal:** Validated task taxonomy + routing rules tested against 30 real emails.

---

### Session 4: Proposals & Itineraries

Add to the Mining Report:

```
- PROPOSAL STRUCTURE MATRIX:
  | Proposal | Client | Type | Sections | Length | Pricing Style | Result |
  |----------|--------|------|----------|--------|--------------|--------|
  | 1 | | | | | | Won/Lost |
  | 2 | | | | | | |
  ...

- WINNING PATTERNS: what do proposals that converted have in common?
- LOSING PATTERNS: what do rejected proposals share?
```

**Session 4 goal:** Proposal template from real winners + 2-3 example proposals + supplier rates reference.

---

### Session 5: Pricing & Analysis

Add to the Mining Report:

```
- RATE CARD INVENTORY:
  | Supplier/Service | Type | Season | Rate | Last Updated | Source File |
  |-----------------|------|--------|------|-------------|-------------|
  | | | | | | |

- MARGIN CALCULATION LOG:
  | Quote # | Client | Components | Cost | Quoted | Margin % | Notes |
  |---------|--------|-----------|------|--------|----------|-------|
  | | | | | | | |
```

**Session 5 goal:** Pricing logic documented + rate card inventory + margin guidelines validated.

---

## After Each Mining Session

Back in Claude Code, do the following:

1. Save the final mining report to `mining-outputs/session-[N]-[topic]/mining-report.md`
2. Save each extracted example as a separate file in the same folder
3. Update ROADMAP.md — mark mining tasks as complete
4. Review gaps — do we need to re-mine anything?
5. When ready: `build [project]` to start assembling final project files

---

## Quick Reference: Mining Commands (use in claude.ai)

| Say This | Claude Does This |
|----------|-----------------|
| "show report" | Display current mining report state |
| "save checkpoint" | Output full report for copy/paste backup |
| "rate this" | Add quality rating to current example |
| "pick this one" | Move current example to SELECTED EXAMPLES |
| "extract language" | Pull best lines from current example into EXTRACTED LANGUAGE |
| "what's missing?" | Check GAPS & QUESTIONS, suggest what to search next |
| "session complete" | Generate all final outputs (report, files, next session prep, raw data) |
