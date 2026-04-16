# Gemini 2.5 Pro — Dashboard Plan Audit
Date: 2026-04-11 | Model: gemini-2.5-pro | Mode: Plan audit

## 1. Architectural Risks

1. **Excel as database (core risk):** Flask writing while reading = file locking → data corruption or crash. Race condition almost guaranteed: load dashboard (read) → log call (write) → auto-refresh (read). If write fails silently, Sebastian loses the log entry without knowing.

2. **Fragile date parsing:** Tilaushistoria dates are text strings like '13.-14.3.2026'. Custom parser required. Single-day entries ('13.3.2026') or 3-day ranges will break the parser → deal detail view crashes.

3. **Multiple sources of truth:** company-aggregates.json has revenue, Pipeline.Arvo is NULL. Dashboard will show inconsistent data unless one source is designated authoritative.

## 2. Missing Specs

1. **Odottaa write-back mechanism:** How exactly does openpyxl write this without corrupting other sheets/formulas? What happens on write failure?
2. **Date range logic:** For traffic light "days since activity" — use start or end date of the range?
3. **Traffic light thresholds:** Exact numbers per level not specified in plan (Claude has them, but plan file doesn't).
4. **Segment classifier rules:** 7 tags listed but not the exact logic/thresholds per tag.

## 3. Simplifications Recommended

1. **3 traffic lights not 5:** For 20 deals, 5 levels is cognitive overkill. Green/Yellow/Red is faster to interpret.
2. **Auto-add Odottaa column:** Don't ask Patrick to add it manually — Flask auto-adds on first write, defaults to 'me'.
3. **No caching for V2.0:** 20 rows reads in milliseconds. Skip cache complexity — file locking is the real risk, not read speed.

## 4. Defer to V2.1+

1. **KPI calculations:** KPIt sheet is NULL. Skip the header for V2.0.
2. **Segment classifier:** Depends on fragile Tilaushistoria parsing. Nice-to-have, not core.
3. **Email drafter:** V2.1 as planned. Mailto approach is fine.

## 5. Week-1 Most Likely Failure

**Silent write failure during log_call.** Sebastian submits the form thinking the call is logged → Flask crashes or file is locked → Excel not updated → data lost → he doesn't notice until the next morning when the dashboard shows wrong state.

## Claude's Assessment

Gemini's concerns are valid. Key fixes to make before building:
- Write-back safety: open Excel with `keep_vba=True`, save to temp then rename (atomic write pattern)
- Date parsing: extract first date from range, graceful fallback for unknown format
- Simplify traffic lights: 3 levels for V2.0, 5 levels after Sebastian is comfortable (V2.1)
- Defer segment classifier to V2.1
- Odottaa: auto-add column on first write, default 'me'
