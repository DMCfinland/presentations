# JS Excel Schema Spar — Gemini Response
**Date:** 2026-04-02
**Model:** Gemini (via run-gemini.sh)
**Prompt file:** /tmp/grok-spar-js-excel-schema-20260402.txt
**Mode:** Template 3 — Cross-Validation
**Grok Expert:** status=error (CDP degradation, session limit)

---

## schema_strengths

- [Lucas] Single source for company data (Asiakkaat as central register)
- [Harper] Automated extraction foundation (1,657 historical orders = huge head start)
- [Benjamin] Explicit relationships defined (Tunniste FK concept is sound even if fragile)
- [Lucas] Dedicated Pipeline sheet is good structural decision; Seuraava toimenpide/pvm essential

---

## structural_risks

**[Benjamin] PRIMARY KEY MUTABILITY — Tunniste drift = silent Power BI breakage**
- If Tunniste is updated in Asiakkaat (company renamed, slug regenerated), historical Tilaushistoria rows still point to old slug
- Power BI relationship breaks silently — no error, just missing data
- Failure scenario: "Total orders for New Company Name" returns 0 even though 10 historical orders exist under old slug
- **Fix:** Treat Tunniste as immutable once assigned, OR introduce a numeric auto-increment ID as true PK

**[Lucas] COMMA-SEPARATED MULTI-VALUE FIELDS — will choke Power BI within 90 days**
- Suosikkipalvelut, Palvelut lopullinen, Palvelut alkuperäinen are all comma-separated strings
- Power BI needs complex M-query (Text.Split + Table.ExpandListColumn) on every such field
- Manual entry variations: "Sauna", "sauna", "Sauna ", "Sauna,Lounas" → filtering impossible
- No referential integrity on service names (rename = manual cleanup of 908+ rows)
- **Fix:** Separate Palvelut lookup table + linking table. Or at minimum: controlled vocabulary via Excel dropdown

**[Lucas] PIPELINE MANUAL ENTRY — redundancy error amplification**
- Sebastian must manually enter Yritys + Yhteyshenkilö in Pipeline even though they exist in Asiakkaat
- Typos will create disconnected data; old contact info won't update when Asiakkaat changes
- **Fix:** Pipeline uses only Tunniste (FK) + deal fields; Yritys/contact populated via XLOOKUP formulas

**[Harper] MISSING DATA VALIDATION on categorical fields**
- Tyyppi, Sesonki, Asiakkuusvaihe, Luottamus are open-text (except Vaihe which now has dropdown)
- b2b / B2B / B2B / Corporate = 4 distinct Power BI categories
- **Fix:** Data Validation (List) for all categorical columns, pointing to lookup values

**[Harper] EXCEL→POWER BI REFRESH FRAGILITY**
- File path change = broken connection
- Mixed data types in Arvo (€) = Power Query infers text, breaks calculations
- File locked by Sebastian = Power BI refresh fails
- No concurrent access

---

## what_we_missed

- [Lucas] **No lead source tracking** — no field for how prospect entered CRM (cold call, referral, event). Critical for evaluating Sebastian's outbound effectiveness by April 25.
- [Benjamin] **No audit trail** — no way to know who changed what, when. Zero accountability during kill switch evaluation period.
- [Harper] **Single contact per company** — Yhteyshenkilö is one text string. No multi-contact support.
- [Lucas] **Luottamus (confidence) has no defined rules** — should "low confidence" orders be excluded from KPI totals? Undefined = different stakeholders interpret differently = inconsistent reporting.

---

## power_bi_issues

- [Benjamin] Tunniste mutability = silent data loss in aggregations (most dangerous)
- [Lucas] Comma-separated ETL = heavy M-query overhead, row inflation, performance degradation
- [Harper] File locking + path fragility = refresh failures
- No native referential integrity enforcement — bad Tunniste FK in Pipeline creates blank rows

---

## verdict

**Gemini verdict: CONDITIONAL GO with 3 mandatory fixes before week 1 ends.**

Single most dangerous decision: mutable Tunniste as PK + comma-separated multi-value fields (dual attack on integrity + analytics).

One design alternative missed: Microsoft Lists (SharePoint) or Airtable — enforces referential integrity, handles multi-select properly, provides audit trail, free for single user.

---

## Debrief notes

Lucas's highest-value challenge: Pipeline redundant manual entry will cause data drift within weeks. Fix via XLOOKUP is immediate.

Benjamin's most actionable finding: Tunniste immutability rule needs to be documented and enforced — a rebuild script that regenerates slugs will silently break history.

Harper's miss: Excel-to-Power BI via SharePoint (cloud Excel) solves the file-path fragility and adds version history. Worth switching before Sebastian starts.

Grok/Gemini agreement: unanimous on Tunniste drift risk and comma-separated field problem.
Divergence: none significant (Gemini only, so no cross-model divergence available this session).
