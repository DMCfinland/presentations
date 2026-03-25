# Excel Mining Protocol
**Version:** 2.0
**Validated on:** Järvisydän budget + cost structure (session 35) + Finland DMC proposals pipeline (session 38)
**Tool:** `_shared/scripts/excel-extract-smart.py`

---

## Why This Protocol Exists

Raw Excel dumps waste tokens and require chunked reads. A 19-sheet Excel extracted naively:
- Raw: 51KB = ~12,750 tokens, requires 2 read passes
- Smart: 44KB = ~11,000 tokens, single pass

More importantly: thematic analysis from clean data produces better insights than reading raw grids.

---

## ⚠️ MANDATORY PRE-CHECK — RUN BEFORE SMART EXTRACTOR

**The 16,383 column trap:** Excel's maximum column count is 16,383. If ANY cell in the far right columns has a value (even a space or a date in column AA), the smart extractor's "strip trailing empty columns" fails to strip anything, producing a file with 16,383 columns × N rows = potentially hundreds of MB.

**Rule: Always run a sniffer first on unknown files.**

```python
# Quick sniffer — paste this into a python3 shell
import openpyxl
wb = openpyxl.load_workbook("yourfile.xlsx", data_only=True, read_only=True)
ws = wb.active
# Get estimated column count and size
print(f"File size: {os.path.getsize('yourfile.xlsx')/1024:.0f}KB")
# Check row 1 for real column headers
headers = [(c.column, c.value) for c in next(ws.iter_rows(min_row=1, max_row=1)) if c.value]
print(f"Non-empty headers: {len(headers)}")
print(headers[:10])
wb.close()
```

**If non-empty headers < 50:** Use targeted extraction (specify `max_col` manually, not smart extractor).
**If non-empty headers 50-200:** Smart extractor is fine.
**If estimated tokens > 100K from smart extractor:** Stop. Do targeted extraction instead.

### Targeted extraction for wide/polluted Excels

When the file has data scattered in far-right columns (column AA+), write a bespoke script:
```python
# Extract only the columns you care about
for row in ws.iter_rows(min_row=8, max_row=400, max_col=21):  # max_col = last relevant column
    cells = {cell.column: cell.value for cell in row}
    ...
```

**The Finland DMC Proposals Excel (session 38) was this case:**
- File: 14.6MB, 16,383 columns reported, ~3.7M token estimate from smart extractor
- Reality: only 21 relevant columns (A–U), data scattered in X/Y/AA blocked stripping
- Solution: targeted extraction with `max_col=21` → 59KB clean output
- Smart extractor output: 14MB monster → deleted immediately

---

## THE 3-PHASE WORKFLOW

### Phase 1: Structure Map (free, ~1KB, instant)
**Run before anything else.**

```bash
python3 _shared/scripts/excel-extract-smart.py "<excel_file>" "output-smart-extract.md"
```

Read only the PHASE 1 section (first ~30 lines). You get:
- All sheet names
- Row counts per sheet
- Data row counts per sheet

**Decision gate:** After Phase 1, decide which sheets to prioritize. Skip sheets with 0 data rows entirely.

### Phase 2: Read the Full Smart Extract
The smart extract file is the primary working document. It's already cleaned — no empty rows, compact numbers.

Read it in one pass (should be ≤ 15K tokens for most business Excels).

If the file is still >20KB: read sheet-by-sheet using the structure map to pick themes:
- Cash flows first
- P&L / company budgets second
- Support data (restructuring, invoices) third

### Phase 3: Compile Analysis File
Write a `{TOPIC}-ANALYSIS.md` in the same folder as the smart extract. Sections:
1. Executive summary (what this file IS and what question it answers)
2. Headline numbers table
3. Key themes (one section per major topic)
4. Comparison to other known data (if available)
5. Open questions for Patrick

---

## FILE STRUCTURE STANDARD

Each Excel source document gets its own subfolder:

```
get-to-know-jarvisydan/
  phase-2-budget-excel/
    budget-smart-extract.md      ← Phase 1+2 output
    BUDGET-ANALYSIS.md           ← Phase 3 output
    raw-budget-all-sheets.md     ← OLD style (kept for reference, don't create new ones)
  phase-2-cost-structure/
    cost-structure-smart-extract.md
    COST-STRUCTURE-ANALYSIS.md
  phase-2-[next-topic]/
    [topic]-smart-extract.md
    [TOPIC]-ANALYSIS.md
```

**Naming rules:**
- Folder: `phase-N-{short-descriptor}/` (all lowercase, hyphens)
- Smart extract: `{descriptor}-smart-extract.md`
- Analysis: `{DESCRIPTOR}-ANALYSIS.md` (uppercase for analysis files — they are deliverables)
- No raw dumps unless explicitly needed for audit trail

---

## TOKEN BUDGET

| Excel complexity | Sheets | Smart extract size | Tokens | Notes |
|-----------------|--------|------------------|--------|-------|
| Simple (1-5 sheets) | 1 | ~10KB | ~2,500 | Easy single pass |
| Medium (5-15 sheets) | 10 | ~25KB | ~6,250 | Single pass, fine |
| Complex (15-25 sheets) | 19 | ~44KB | ~11,000 | Single pass possible |
| Very large (25+ sheets) | 25+ | ~60KB+ | ~15,000+ | Split by theme |

**Rule:** If estimated tokens > 15,000, split Phase 2 into themed reads (cash flow / P&L / support data).

---

## WHAT THE SCRIPT DOES (AND DOESN'T DO)

### Does:
- Removes rows where ALL values are 0 or empty
- Compresses floats (1234567.00 → 1234567)
- Strips trailing empty columns
- Adds per-sheet row count context
- Works on any .xlsx file with openpyxl

### Doesn't:
- Handle merged cells (they may appear as empty in adjacent cells — expected)
- Interpret color/conditional formatting
- Read formulas (uses data_only=True — computed values only)
- Handle .xls files (old format) — convert to .xlsx first

---

## EXCEL TYPES — DIFFERENT ANALYSIS PRIORITIES

### Type A: Financial Excel (budget, P&L, cash flow forecast)
*Examples: Järvisydän budget, DMC Nordea forecast, LKJS loan calculator*

Prioritize in this order:
1. Revenue model — how does the company make money, what's the price/unit?
2. Cash flow — when does cash go negative? What's the buffer?
3. Cost structure — top 3 cost items by % of revenue?
4. Gap analysis — distance from current state to target state?
5. Dependencies — external events (loans, deals, filings)?

### Type B: CRM / Pipeline Excel (proposals, contacts, client list)
*Examples: Finland DMC Proposals 2024, any client contact sheet*

Prioritize in this order:
1. **Win rate** — overall and by segment (country, staff, venue, product type)
2. **Revenue concentration** — top 5 clients = what % of total?
3. **Staff performance** — who owns what, win rate per person, avg deal size
4. **Client segments** — which market/type has highest win rate + revenue combination?
5. **Anomalies** — markets with very high volume but very low win rate (something wrong)
6. **Active pipeline** — how many proposals currently in "on process" status?
7. **Second Brain gaps** — which top clients are NOT yet in the Second Brain?

### Type C: Operational tracking (schedules, inventories, supplier rates)
*Examples: supplier price lists, booking calendars*

Prioritize in this order:
1. Structure — how many items, what categories?
2. Pricing patterns — ranges, outliers, seasonal variation
3. Cross-reference — does this confirm or contradict what we know from email mining?

---

## COMMON PATTERNS IN JÄRVISYDÄN EXCELS

- Finnish headers, often abbreviated (LV = liikevaihto/revenue, KK = kuukausi/month, PV = päivä/day)
- Per-unit columns: /pax, /huone, /asiakas = per guest, per room, per customer
- Käyttöaste = occupancy rate (as decimal, e.g. 0.53 = 53%)
- Käyttökate = EBITDA
- Kassaennuste sheets = monthly cash flow forecasts
- Saneeraus sheets = restructuring data

---

## REUSABILITY

This protocol applies to any business Excel with:
- Budget/forecast data
- Multi-sheet P&L/cash flow structure
- Finnish or English headers

The script (`excel-extract-smart.py`) is generic. Copy it to any project.

**Cross-company use:** Finland DMC budgets, 1658 Holdings financing plan, any portfolio company Excel.

---

---

## THE DMC PROPOSALS EXCEL — SPECIFIC NOTES

File: `Downloads/1_Pending proposals 2024 (1).xlsx`
Type: CRM/Pipeline (Type B)
Clean extract: `FinlandDMCOy-AIFiles/finland-dmc-2.0/research/proposals-2024/proposals-clean-extract.md` (59KB)
Analysis: `FinlandDMCOy-AIFiles/finland-dmc-2.0/research/proposals-2024/PROPOSALS-ANALYSIS.md`

**Schema (columns A–U):**
- A: channel (Direct / GSA / Direct/GSA)
- B: country (Sveitsi, Saksa, UK, Italia...)
- C: staff (LV=Liisa, JK=Janna, RV=Reeta)
- D: business ID (format: 2-3043, 3-3128 etc.)
- E: company name
- F: RFQ date
- G: trip type / destination
- H: venue (JS / Kuru / Muu)
- I: pax count
- J: travel dates (text)
- K: year (2024/2025/2026)
- L: month (Finnish)
- M: travel date (datetime)
- N: proposal sent date
- O: invoiced (ok / date)
- P: status code (1=Confirmed, 2=On process, 3=Canceled)
- Q: status text
- R: revenue €
- S: margin €
- T: price/pax €
- U: notes / comments

**Key findings (session 38):**
- 393 proposals, 44% win rate, €5.87M confirmed revenue
- AHI Travel = 75% of revenue — extreme concentration risk
- JS venue = 73% win rate; Lapland/Helsinki "Muu" = 15% (but drives big revenue)
- Liisa: 57% win rate, 197 proposals — highest volume + conversion
- Italy: 35 proposals, 6% win rate — investigate
- Switzerland Kontiki: 52 proposals, 87% win rate — auto-process FIT partner

**When to re-run analysis:** When a newer proposals file appears (2025 version).
Load the clean extract for Second Brain work, NOT the raw Excel.

---

*Source sessions: 35 (financial Excels), 38 (CRM Excels, 16K column trap). Tool: `_shared/scripts/excel-extract-smart.py`*
