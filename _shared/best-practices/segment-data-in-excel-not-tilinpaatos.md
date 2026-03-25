# Pattern: Segment-Level Revenue Lives in Excel, Not Tilinpäätös

**Pattern name:** segment-data-in-excel-not-tilinpaatos
**Tier:** B
**Source session:** 53
**When to apply:** Analyzing revenue by location or business unit for a Finnish company

## What

Finnish tilinpäätös (financial statements) shows aggregate company totals only. Per-location or per-product-line revenue lives in separate Excel files — typically named "liiketoiminnan tunnusluvut" or similar.

## Example (Luonto 365 / session 53)

- Tilinpäätös 2024: only total liikevaihto = 744,854€ (useless for Koli vs. Järvisydän split)
- AMC liiketoiminnan tunnusluvut 2021-2023.xlsx: had exact segment split → Risteilyt Koli: 0 / 0 / 138k€

## When to Apply

- User asks "how much revenue came from [location X]?"
- Analyzing a multi-location or multi-product Finnish business
- Trying to understand when a new operation became profitable

## Action

1. First: look for `*tunnusluvut*.xlsx` or `*liikevaihto*.xlsx` in the company's hallinto/ or talous/ folder
2. If not found: look for Excel files with year ranges in the name
3. Only fall back to tilinpäätös if no Excel found — it gives aggregate only

## Notes

- The Excel may cover a different period than the latest tilinpäätös (e.g., tunnusluvut was 2021-2023, tilinpäätös covered 2024)
- For 2024+ segment data: need to ask the business manager directly (Petri in Koli's case)
