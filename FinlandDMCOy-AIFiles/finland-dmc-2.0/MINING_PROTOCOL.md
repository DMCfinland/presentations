# Mining Session Protocol — Finland DMC 2.0

Standard process for all 5 mining sessions. Each session produces TWO outputs:

1. **Email Drafter** — tone patterns, example emails, DOs/DONTs, best lines (for Claude Projects)
2. **Second Brain** — client names, contacts, interaction history, market data (for SharePoint Lists)

**Where mining happens:** Claude Code (with M365 MCP connector logged in as sales@Finland-dmc.com). Output files go to the same local folders either way.

---

## SESSION 1 CALIBRATION DATA (from 2026-02-18)

Use these benchmarks to calibrate expectations for all future sessions:

### What the mailbox actually contains
- **100% B2B** — tour operators, travel companies, DMC partners. Zero individual tourists.
- **Languages:** English dominant (~80%), Finnish (~15%), occasional German
- **Date range in results:** Heavy bias toward Dec 2025 (most recent). Older emails exist but require date-range splitting to surface.
- **Thread depth:** Some threads have 15+ messages (e.g., Nordic Luxury/Katerina). Read full threads — they contain complete inquiry lifecycles.

### Staff identified (as of Sessions 1-2)
- **Laura Ilvonen** — Primary client-facing, handles most outbound proposals and quotes. Warm, professional, uses 😊
- **Reeta Vihavainen** — Senior/pricing specialist, handles complex quotes and commission discussions
- **Liisa Vihermaa** — Operations/logistics + new partner development. Handles ITB meetings, Flash Pack allocation, new operator onboarding
- **Janna Kankkunen** — Former employee (pre-2025), similar tone patterns to Laura
- **Sebastian Heiskanen** — ⚠️ IDENTITY UNCONFIRMED. Appeared Session 2 in: DG Art of Travel (RQ TESTAI X9) and Volvo Trucks Italia quote. Confirm in Session 3 via `sender: "sebastian@finland-dmc.com"`. Likely new team member.

### M365 MCP connector quirks
- ⚠️ **`folderName: "Sent Items"` does NOT work** — returns `NOT_FOUND` for shared mailbox
- ✅ **Use `sender: "sales@finland-dmc.com"` instead** — equivalent to searching Sent Items
- ✅ **Use `recipient: "sales@finland-dmc.com"` for inbound** — equivalent to Inbox
- Search returns max ~20 results per query — use specific terms to get variety
- `read_resource` with `mail:///messages/{id}` gives full email body including thread history

### Search vocabulary that works (B2B DMC)
**DO use:** proposal, offer, quote, itinerary, program, commission, markup, net rate, booking confirmation, activity, transfer, accommodation, group, pax, FIT, agent, operator, DMC
**DON'T use:** inquiry response, thank you for reaching out, welcome email, customer service — these are B2C terms that return 0 results

### Yield per session
- Session 1 produced: 12 clients, 19 contacts, 10 interactions, 35+ best lines, 5 selected example emails (~70 emails, 5 searches)
- Session 2 produced: 15 new clients, 21 contacts, 11 interactions, 6/10 Session 1 clients enriched (~100 emails, 3 full threads)
- Expect ~15-20 new records per session; full thread reads are highest-yield (3 threads = 50% of Session 2 intelligence)

---

## SESSION 2 CALIBRATION DATA (Inbound, 2026-02-18)

### 100% B2B — definitively confirmed across Sessions 1 and 2
Zero individual consumers. All traffic is tour operators, corporate MICE, luxury agents, or DMC partners. Drop any B2C search vocabulary fallbacks permanently.

### Source markets (14 countries found)
USA, UK, Germany, Switzerland, Denmark, Italy, France, Belgium, Netherlands, Luxembourg, Estonia, Finland (local suppliers/guides)

### Staff routing — emerging map (Session 3 will validate)
| Staff | Role pattern found in emails |
|-------|------------------------------|
| Liisa Vihermaa | New partner development, allocation disputes, ITB meetings, prospect follow-up |
| Laura Ilvonen | Primary outbound — most proposals, confirmations, standard correspondence |
| Reeta Vihavainen | Complex pricing, commission negotiations, margin discussions |
| Sebastian Heiskanen | Custom program quotes (DG Art of Travel, Volvo Trucks Italia) — role unconfirmed |

### Critical issues from Session 2 (still unresolved)
- Flash Pack allocation dispute — CRITICAL — Judi Mouton — call this week
- Neubauer Touristik ITB appointment — HIGH — Liisa
- Volvo Trucks Italia quote — HIGH — Sebastian handling

---

## DUAL-PROJECT OUTPUT FORMAT

Every mining session saves files to TWO output paths:

```
mining-outputs/session-[N]-[topic]/
├── EMAIL-DRAFTER/                    # → project-files/ → Claude Projects
│   ├── patterns-identified.md        # Tone, structure, language patterns
│   ├── examples-captured.md          # Best email examples (full text)
│   ├── best-lines.md                 # Extracted phrases and sentences
│   └── session-log.md               # Search log, gaps, decisions
│
└── SECOND-BRAIN/                     # → SharePoint Lists (Clients, Contacts, Interactions)
    ├── clients-found.md              # Company names, markets, segments, status
    ├── contacts-found.md             # People names, roles, emails, preferences
    ├── interactions-log.md           # Date, type, outcome, follow-up needed
    └── relationship-signals.md       # Satisfaction, loyalty, risk, opportunity flags
```

---

## Session Start

Paste this into a new conversation at the start of every mining session:

```
I'm starting Mining Session [N]: [Topic].

This session produces outputs for TWO projects:
- EMAIL DRAFTER: tone patterns, example emails, best lines for Claude Projects
- SECOND BRAIN: client/contact data, interaction history for SharePoint CRM

Before we search anything, create a Mining Report document with these sections:

=== EMAIL DRAFTER SECTIONS ===
- EXAMPLES FOUND: table of candidate emails with date, client, type, quality rating
- SELECTED EXAMPLES: the ones I chose as best (with full text saved)
- EXTRACTED LANGUAGE: best lines, phrases, patterns pulled from real emails
- PATTERNS IDENTIFIED: structural, tonal, content patterns across emails

=== SECOND BRAIN SECTIONS ===
- CLIENTS DISCOVERED: company name, country, segment (B2B/B2C), inquiry type, status
- CONTACTS DISCOVERED: person name, company, role, email, language, preferences
- INTERACTIONS LOGGED: date, client, type (inquiry/follow-up/booking/complaint), channel, outcome
- RELATIONSHIP SIGNALS: satisfaction indicators, loyalty markers, churn risk, growth opportunities

=== SHARED SECTIONS ===
- SESSION INFO: date, session number, topic, model used
- SEARCH LOG: every search query tried + result quality (good/partial/empty)
- STATISTICS: counts, distributions, averages from the data
- DECISIONS MADE: choices about what to include/exclude and why
- GAPS & QUESTIONS: things we couldn't find or need to investigate

Update this report after every search we do and every decision I make.
When I say "show report" — display the current state.
When I say "save checkpoint" — output the full report for me to copy/save.
```

---

## During Session

### M365 Search Tips (learned from Session 1)
- **Outbound:** Use `sender: "sales@finland-dmc.com"` (NOT `folderName:`)
- **Inbound:** Use `recipient: "sales@finland-dmc.com"` (NOT `folderName:`)
- **Max ~20 results per search** — use specific query terms to get variety across types
- **Date range splitting:** Add `beforeDateTime`/`afterDateTime` to avoid recency bias
- **Read full threads:** Use `read_resource` with `mail:///messages/{id}` — threads contain 15+ messages
- **B2B vocabulary only:** proposal, offer, quote, itinerary, program, commission, group, pax, operator, DMC

### After every M365 search:
- Log the query and result quality in SEARCH LOG
- Note: good (usable results), partial (some relevant), empty (nothing useful)
- If 0 results: adapt vocabulary (B2B not B2C) before trying again

### After reviewing results:
- Update EXAMPLES FOUND table with candidates
- Rate each: 1 (weak) to 5 (excellent)

### After picking a winner:
- Move it to SELECTED EXAMPLES with full text preserved
- Tag it with type, client, date, and why it was selected
- Anonymize client names in examples (use [Client Company], [Contact Name])

### After extracting language:
- Add best lines/phrases to EXTRACTED LANGUAGE
- Note which email they came from
- Categorize by use case (greeting, pricing, logistics, closing, etc.)

### Mandatory checkpoint at Search 3 of 5:
After completing Search 3, ALWAYS say "save checkpoint" before continuing to Search 4.
- Long sessions (5 searches + full thread reads) accumulate context burden — early findings get compressed
- Copy the checkpoint to Claude Code BEFORE Search 4 if the session feels heavy
- This is not optional: every session misses a checkpoint is a session with recoverable but wasted work

### Every ~20 minutes:
- Claude should remind you: "Time for a checkpoint save?"
- Say "save checkpoint" to get the full report for copy/paste backup

---

## Session End

Paste this when done:

> ⚠️ **Claude Code handles extraction.** Do NOT generate the output files in this Desktop session. Paste the full MINING-REPORT.md into Claude Code — it will extract all blocks. Your only job at session end is to ensure MINING-REPORT.md is complete and saved.

```
Session complete. Generate FOUR output blocks I can save as separate files:

1. EMAIL DRAFTER OUTPUT — for mining-outputs/session-[N]-[topic]/EMAIL-DRAFTER/
   - patterns-identified.md: all tone, structure, language patterns found
   - examples-captured.md: full text of selected best emails
   - best-lines.md: extracted phrases and sentences by use case

2. SECOND BRAIN OUTPUT — for mining-outputs/session-[N]-[topic]/SECOND-BRAIN/
   - clients-found.md: YAML list of companies discovered (name, country, segment, status)
   - contacts-found.md: YAML list of people discovered (name, company, role, email)
   - interactions-log.md: YAML list of interactions (date, client, type, outcome)
   - relationship-signals.md: satisfaction, loyalty, churn risk, opportunities

3. SESSION REPORT — mining-outputs/session-[N]-[topic]/session-report.md
   - Complete search log, statistics, decisions, gaps

4. NEXT SESSION PREP — what the next mining session should look for based on gaps

Use YAML format for Second Brain data (easy to parse into SharePoint Lists later).
Format so I can paste each block directly into the correct file on my computer.
```

---

## Per-Session Specific Additions

Each session adds tracking sections specific to its domain.

### Session 1: Client Communications — OUTBOUND ✅ COMPLETE

**Completed:** 2026-02-18 | **Emails reviewed:** ~70 | **Output:** 824-line MINING-REPORT.md

**What worked:**
- `sender: "sales@finland-dmc.com"` for outbound (NOT `folderName: "Sent Items"`)
- Reading full email threads via `read_resource` — single threads contain 15+ messages with complete lifecycle
- Adapted search vocabulary from B2C → B2B after Search 2 returned 0 results

**What didn't work:**
- `folderName: "Sent Items"` → NOT_FOUND error
- B2C search terms ("thank you for your inquiry") → 0 results
- No date range splitting → results clustered in Dec 2025

**Gaps to fill in later sessions:**
- Complaint handling (only 1 complaint reference found, "Palautetta" thread unread)
- Price objection responses
- Cancellation/change handling
- Older relationships (pre-2025)
- Rachel's company, Lorrie's company, Silvia's real company name

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

**Session 1 goals:**
- **Email Drafter:** One excellent example email per type + tone guide + best lines library
- **Second Brain:** Extract every client name, company, country, and email from outbound correspondence. Log interaction types (inquiry response, follow-up, etc.) with dates.

---

### Session 2: Inbound Emails

**Search strategy (updated from Session 1 learnings):**
- Use `recipient: "sales@finland-dmc.com"` (NOT `folderName: "Inbox"`)
- Split into date ranges to avoid recency bias: try `beforeDateTime: "2025-07-01"` and `afterDateTime: "2025-07-01"` separately
- Use B2B vocabulary: "request for proposal", "group request", "looking for DMC", "Finland program", "cooperation", "partner"
- Prioritize finding: complaints/difficult emails, price objection handling, cancellation language, new operator first-contact emails
- Cross-reference against Session 1 clients — enrich existing records, don't duplicate

**Known clients from Session 1 (watch for inbound from these):**
AHI Travel, Flash Pack, Nordic Luxury, Trade Travel, AABEI, Best Served Scandinavia, Lloyd Touristik, Fit4travel, Baltic Travel Company, GALL

Add to the Mining Report:

```
- INQUIRY TYPE TAXONOMY (updated for B2B reality):
  | Type | Count | % of Total | Example Client | Typical Ask |
  |------|-------|-----------|----------------|-------------|
  | Tour operator RFP | | | | |
  | Corporate/incentive | | | | |
  | New partner inquiry | | | | |
  | Repeat booking request | | | | |
  | Complaint/issue | | | | |
  | Price objection/negotiation | | | | |
  | Cancellation/change | | | | |
  | Logistics question | | | | |
  | Supplier comms | | | | |
  | Cold inbound/new operator | | | | |

- SOURCE MARKET BREAKDOWN:
  | Country/Region | Count | Language | Channel | B2B/B2C |
  |---------------|-------|----------|---------|---------|
  | | | | | |

- SESSION 1 CROSS-REFERENCE:
  | Client | New info found? | Records enriched? |
  |--------|----------------|-------------------|
  | AHI Travel | | |
  | Flash Pack | | |
  | Nordic Luxury | | |
  ...
```

**Session 2 goals:**
- **Email Drafter:** Inbound email classification system + source market map + "always ask for" checklist + complaint/difficult email handling patterns (gap from Session 1)
- **Second Brain:** Build client/contact database from inbound inquiries. Map source markets (country, language, B2B/B2C). Track inquiry → booking conversion signals. Log relationship start dates. Enrich Session 1 client records with inbound data. Find the "Palautetta" complaint thread (flagged gap from Session 1).

**Session 2 specific searches (5 searches):**
1. **Broad inbound scan:** `recipient: "sales@finland-dmc.com"`, query: `*`, limit 20 — baseline of what comes in
2. **New partner/operator inquiries:** query: `"looking for" OR "cooperation" OR "partner" OR "DMC services"`, recipient: sales@
3. **Complaints & difficult emails:** query: `"complaint" OR "problem" OR "issue" OR "disappointed" OR "palautetta" OR "cancellation"`, recipient: sales@
4. **Price negotiations inbound:** query: `"too expensive" OR "budget" OR "discount" OR "lower price" OR "competitive"`, recipient: sales@
5. **Older date range:** Same as search 1 but with `beforeDateTime: "2025-07-01"` — surface older relationships

---

### Session 3: DMC Router

**Goal:** Email routing/classification — which emails go to whom, by what signals, with what urgency.
**Secondary:** Surface remaining Session 1 gaps (Nordic Luxury, Trade Travel, Best Served Scandinavia, GALL). Confirm Sebastian Heiskanen's role.

**Ready-to-paste context block:** See `mining-outputs/session-2-inbound-emails/next-session-prep.md`

**Pre-planned searches (5):**
1. **Staff routing signals:** `recipient: "sales@finland-dmc.com"` + `"for your attention" OR "Liisa" OR "Laura" OR "Reeta" OR "Sebastian"`
2. **VIP/priority signals:** `recipient: "sales@finland-dmc.com"` + `"VIP" OR "urgent" OR "high importance" OR "asap" OR "priority"`
3. **Missing Session 1 clients:** `recipient: "sales@finland-dmc.com"` + `"Nordic Luxury" OR "Trade Travel" OR "Best Served" OR "GALL"`
4. **Sebastian identity:** `sender: "sebastian" OR "sebastian@finland-dmc.com"`
5. **Complex routing threads:** `recipient: "sales@finland-dmc.com"` + `"fwd" OR "fw" OR "please handle" OR "as discussed"` (split pre/post July 2025)

Add to the Mining Report:

```
- ROUTING MATRIX (build from real examples):
  | Email Type | Signal Words | Assigned To | Urgency | Notes |
  |-----------|-------------|-------------|---------|-------|
  | New partner inquiry | | | | |
  | Corporate direct | | | | |
  | Allocation dispute | | | | |
  | VIP group request | | | | |
  | Logistics change | | | | |
  | Price negotiation | | | | |

- TASK CLASSIFICATION TRACKER:
  | Email # | Date | From | Type | Routed To | Correct? | Notes |
  |---------|------|------|------|-----------|----------|-------|
  | 1 | | | | | | |
  ...
  | 30 | | | | | | |

- STAFF ASSIGNMENT MAP (validate/update from Sessions 1-2 draft):
  | Staff | Handles | Doesn't Handle | Average Response Tone |
  |-------|---------|---------------|----------------------|
  | Liisa | | | |
  | Laura | | | |
  | Reeta | | | |
  | Sebastian | | | |

- CLASSIFICATION ACCURACY: __/30 correct on first pass
- MISSED CATEGORIES: types that don't fit current taxonomy
```

**Session 3 goals:**
- **Email Drafter:** Routing rules + validated taxonomy + VIP handling patterns
- **Second Brain:** Enrich existing records with routing assignments. Confirm Sebastian's role. Fill 4 missing Session 1 clients.

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

**Session 4 goals:**
- **Email Drafter:** Proposal template from real winners + 2-3 example proposals + supplier rates reference
- **Second Brain:** Log proposal outcomes (won/lost/pending) per client. Extract trip preferences, budget ranges, group sizes. Map client → supplier relationships. Build Growth Roadmap seeds (upsell opportunities spotted in proposals).

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

**Session 5 goals:**
- **Email Drafter:** Pricing logic documented + rate card inventory + margin guidelines validated
- **Second Brain:** Map supplier rates to services. Build supplier contact database. Log pricing negotiations and outcomes per client. Identify margin patterns by client segment and season.

---

## After Each Mining Session

Back in Claude Code, do the following:

### Email Drafter Files
1. Save patterns to `mining-outputs/session-[N]-[topic]/EMAIL-DRAFTER/patterns-identified.md`
2. Save examples to `mining-outputs/session-[N]-[topic]/EMAIL-DRAFTER/examples-captured.md`
3. Save best lines to `mining-outputs/session-[N]-[topic]/EMAIL-DRAFTER/best-lines.md`

### Second Brain Files
4. Save client data to `mining-outputs/session-[N]-[topic]/SECOND-BRAIN/clients-found.md`
5. Save contact data to `mining-outputs/session-[N]-[topic]/SECOND-BRAIN/contacts-found.md`
6. Save interactions to `mining-outputs/session-[N]-[topic]/SECOND-BRAIN/interactions-log.md`
7. Save signals to `mining-outputs/session-[N]-[topic]/SECOND-BRAIN/relationship-signals.md`

### Housekeeping
8. Save session report to `mining-outputs/session-[N]-[topic]/session-report.md`
9. Update CURRENT-STATUS.md — mark session complete in Active Deliverables, update Company Status Matrix for Finland DMC
10. Review gaps — do we need to re-mine anything?
11. When ready: `build [project]` to start assembling final project files

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
