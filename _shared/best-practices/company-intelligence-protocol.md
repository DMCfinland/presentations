# Company Intelligence Protocol v1.0
**For:** 1658 Holdings portfolio companies (all 10)
**Last Updated:** 2026-02-21
**Validated by:** Järvisydän pilot (sessions 33-39)

---

## Purpose

Build CEO-level understanding of each portfolio company to support:
1. **Audit prep** — brief auditors on group structure, governance gaps, compliance status
2. **Owner/board briefings** — confident answers on debt, guarantees, financial position without digging
3. **Staff document drafting** — pre-filled governance templates so staff can draft board minutes, resolutions, and agreements without asking Patrick for company details
4. **Strategic decisions** — reliable foundation for investment, disposal, or operational decisions

**Core principle:** Questions first, documents second. Know what you need to answer before opening a single file.

---

## The 7 Layers

Work through layers in order. Each layer informs whether to proceed to the next.

---

### Layer 0 — Identity (External, Public)
**Cost:** $0 (subscription) | **Time:** 30-60 min | **Gate required:** No

**Sources:**
- Public registers: YTJ (ytj.fi), Kauppalehti, Asiakastieto, Proff.fi, Finder.fi
- Company website, LinkedIn
- Internal files: any existing SEO/GEO or onboarding data

**Questions to answer:**
- Who owns what percentage?
- Who is on the board? Since when?
- What does the company do (business description from public record)?
- Any active legal proceedings or payment defaults?
- Credit rating / luottoluokitus?
- Related companies (same owners, same board members)?
- Any recent news or PRH filings?

**Output:** `get-to-know/phase-0-identity/entity-profile.yaml`

Use the schema from `get-to-know-jarvisydan/phase-1-external-knowledge/ENTITY-SCHEMA.yaml`.
36+ fields: legal name, Y-tunnus, business ID, board, ownership %, auditor, accountant, fiscal year, articles of association date, revenue (public), employees.

**Decision gate:** If ownership is unclear after web research → Patrick interview before Layer 1.

---

### Layer 1 — Document Intelligence (Inventory, Not Content)
**Cost:** $0 (subscription) | **Time:** 30-60 min | **Gate required:** No

**Sources:** SharePoint/OneDrive — scan filenames and folder structure only (do NOT read full documents yet)

**Questions to answer:**
- What financial documents exist and for which years? (tilinpäätös, budgets, Excel models)
- Are board minutes complete? Which years are missing?
- What governance documents exist? (articles, shareholder register, trade register extract)
- What is the document quality? (native digital PDF vs scanned, Excel vs paper printouts)
- What is the OCR backlog? (scanned PDFs with no text layer = blocked for AI reading)
- What operational data exists? (PMS exports, CRM, pricing files)

**Output:** `get-to-know/phase-1-documents/DOCUMENT-INVENTORY.md`

Include:
- Count by category (governance, financial, operational, contracts, HR)
- Year coverage gaps (e.g., "Board minutes: 2022 missing")
- Quality flag per document type (✅ native / ⚠️ partial / 🔴 scanned-only)
- OCR backlog list (scanned PDFs that need manual extraction or OCR tool)
- Estimated total reading cost if all documents were extracted

**Decision gate:** If <10 readable documents exist → switch to Patrick interview mode, skip to Layer 7 synthesis with what you know.

**Cost note:** Layer 1 output is the shopping list for Layers 2-6. Use it to identify the 20-30 files worth reading — not as authorization to read everything. A company with 2,500 files should have a targeted reading plan of ~50 files maximum.

---

### Layer 2 — Governance Signal
**Cost:** $0 (subscription) | **Time:** 1-2 hours | **Gate required:** No

**Sources:** TTK audit reports (tilintarkastuskertomus), board minutes (hallituksen kokoukset), AGM minutes (yhtiökokoukset)

**Questions to answer:**
- Are audit opinions clean (puhdas lausunto) or qualified (mukautettu)?
- Any going concern language or material weaknesses?
- What major decisions were made in the last 3 years?
- Any ownership changes? Board composition changes?
- Any extraordinary general meetings? What triggered them?
- Are required OYL-mandated resolutions present? (dividend, board appointment, auditor appointment)
- Any disputes, loans to board members, related-party transactions disclosed?

**Output:** `get-to-know/phase-2-governance/GOVERNANCE-ANALYSIS.md`

Structure: opinions table (year + auditor + clean/qualified), board events timeline, key resolutions summary, red flag list, governance gap checklist vs Finnish OYL requirements.

**Critical lesson from Järvisydän:**
- TTK reports contain OPINIONS ONLY — financial figures are not in TTK reports, they are in tilinpäätös.
- Board minutes reveal what public records do not: Patrick was removed from JS Oy board Aug 2023 (not visible anywhere else). Always read minutes for ownership events.
- Scanned PDFs may hide critical events — "the 33-day collapse" of LKJS was in a scanned PDF. Note OCR blockers immediately.

**Decision gate:** If qualified audit opinion or going concern found → flag immediately, do not proceed to financial layers without Patrick's awareness.

---

### Layer 3 — Financial History
**Cost:** $0 (subscription) | **Time:** 1-2 hours | **Gate required:** No

**Sources:** Tilinpäätökset (annual financial statements), toimintakertomus (board of directors' report), 3-5 years minimum

**Questions to answer:**
- Revenue trajectory (3-5 years)?
- Gross margin and EBITDA trends?
- Equity position and changes (positive → negative = warning)?
- External debt levels and changes?
- Cash flow pattern (operating CF vs investing vs financing)?
- Any restatements or prior year corrections?
- Any going concern language in toimintakertomus?
- Inter-company balances visible in notes?

**Output:** `get-to-know/phase-3-financial-history/TILINPAATOS-ANALYSIS.md`

Structure: revenue table by year, margin table by year, equity table, debt table, notable events by year, trend narrative (3 sentences).

**Tooling:** Use `_shared/scripts/excel-extract-smart.py` for Excel-format tilinpäätös. See `_shared/best-practices/excel-mining-protocol.md` for the sniffer-first protocol (prevents 16K column trap).

---

### Layer 4 — Forward-Looking Financials
**Cost:** $0 (subscription) | **Time:** 1-2 hours | **Gate required:** No

**Sources:** Budget Excel, 3-year forecasts, bank loan submissions, investor presentations

**Questions to answer:**
- What are the 1-3 year revenue and EBITDA targets?
- What assumptions drive the model? (occupancy, ADR, staffing ratios, capex)
- Where are the cash crunch points? (month-by-month cash flow)
- What investments are planned? Capex pipeline?
- What scenarios are modeled? (base / upside / downside)
- What is the breakeven occupancy / revenue figure?
- Are targets realistic given Layer 3 history?

**Output:** `get-to-know/phase-4-forecast/BUDGET-ANALYSIS.md`

**Note:** Ask Patrick explicitly if a budget Excel exists before assuming it doesn't — it may not be in SharePoint yet.

**Decision gate after Layer 4:** If the company is simple, stable, and the financial picture is clear → skip Layers 5-6, proceed directly to Layer 7 synthesis. Layers 5-6 are optional for stable holding companies and small subsidiaries.

---

### Layer 5 — Operational Intelligence ⚠️ CHECKPOINT REQUIRED
**Cost:** $0 (subscription, M365 connector in claude.ai) | **Time:** 3-5 hours | **Gate: Yes — confirm with Patrick (time investment, not money)**

**Sources:** PMS/Opera, booking system exports, pricing documents, supplier contracts, customer contracts, CRM data (Travel Tree for Finland DMC)

**Questions to answer:**
- What drives revenue? (channels, customer segments, seasonality)
- Unit economics: ADR, occupancy %, RevPAR, booking lead time, cancellation rate?
- Who are the top 10 customers? What is the concentration risk?
- Who are the key suppliers? Any expiring contracts or single-source risks?
- What are the key contractual obligations? (lease terms, management agreements, exclusivities)
- What is the pricing structure? Any commission, revenue-share, or margin agreements?
- What operational systems are in use? (PMS, ERP, accounting software)

**Output:** `get-to-know/phase-5-operations/OPERATIONS-ANALYSIS.md`

**Mining note:** This layer requires M365 mining in claude.ai. Use the M365 connector. Prepare MINING-PROMPT-DESKTOP.md before starting the claude.ai session.

---

### Layer 6 — People Intelligence
**Cost:** $0 (subscription) | **Time:** 1-2 hours | **Gate required:** No

**Sources:** HR records, org chart, email mining (M365 connector), LinkedIn

**Questions to answer:**
- Who does what? (role, responsibilities, accounts/clients they own)
- Which staff roles are single-person dependencies? (key person risk)
- Any recent departures or planned departures?
- Orphaned accounts: customers/suppliers who had a single point of contact who left?
- Culture signals visible in email communication patterns?
- What decisions require Patrick directly vs. can be delegated?

**Output:** `get-to-know/phase-6-people/PEOPLE-ANALYSIS.md` + `staff-map.yaml`

**Lesson from Finland DMC:** Flash Pack (€558K, CRITICAL) was orphaned after Janna Kankkunen left August 2024 with no handover. Layer 6 catches this.

---

### Layer 7 — Synthesis (CEO Briefing Pack)
**Cost:** $0 (subscription) | **Time:** 30-60 min | **Gate required:** No

**Sources:** All outputs from Layers 0-6 + Patrick's input on open questions

**Questions to answer (synthesize, do not re-extract):**
- What are the top 3 risks?
- What are the top 3 opportunities?
- What does Patrick need to know that he may not know yet?
- What questions remain unanswered?

**Outputs:**
1. `get-to-know/KNOWLEDGE-SUMMARY.md` — A4 CEO briefing (2-4 pages)
2. `get-to-know/inter-company-relationships.yaml` — financial relationship map (loans, guarantees, collateral, ownership)
3. `get-to-know/OPEN-QUESTIONS.md` — for Patrick to resolve
4. `get-to-know/governance-templates/` — pre-filled board minute, AGM, resolution templates (Finnish, one per company)

**A4 Summary structure:**
1. Company Overview (1 paragraph — legal, ownership, core business)
2. Financial Snapshot (YAML — latest year-end figures, external debt, inter-company flows)
3. Governance Status (traffic lights — ✅ Green / ⚠️ Yellow / 🔴 Red per document type)
4. Top Risks + Opportunities (3-5 bullets each)
5. Key Notes (anything unusual or requiring attention)
6. Open Questions (items needing Patrick input)

---

## Standard Folder Structure per Company

```
[CompanyName]-AIFiles/
  get-to-know/
    phase-0-identity/
      entity-profile.yaml
    phase-1-documents/
      DOCUMENT-INVENTORY.md
    phase-2-governance/
      raw-governance-extract.md      ← raw extraction (don't lose)
      GOVERNANCE-ANALYSIS.md
    phase-3-financial-history/
      raw-tilinpaatokset-extract.md  ← raw extraction (don't lose)
      TILINPAATOS-ANALYSIS.md
    phase-4-forecast/
      raw-budget-extract.md          ← raw extraction (don't lose)
      BUDGET-ANALYSIS.md
    phase-5-operations/
      OPERATIONS-ANALYSIS.md
    phase-6-people/
      PEOPLE-ANALYSIS.md
      staff-map.yaml
    governance-templates/
      [slug]-board-minutes-template.md
      [slug]-agm-template.md
      [slug]-board-resolution-template.md
    KNOWLEDGE-SUMMARY.md             ← THE deliverable
    inter-company-relationships.yaml ← machine-readable
    OPEN-QUESTIONS.md
```

**Note:** Always save the raw extraction file before writing the analysis. Raw = unedited AI output. Analysis = synthesized, structured. If extraction fails, you still have the raw.

---

## Company Type Matrix

Different companies need different layer depths:

| Company Type | L0 | L1 | L2 | L3 | L4 | L5 | L6 | L7 |
|---|---|---|---|---|---|---|---|---|
| **Holding/investment** | ✅ | ✅ | ✅ | ✅ | – | – | – | ✅ |
| **Hospitality/resort** (Järvisydän group) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Service/tour operator** (Finland DMC) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Asset/property company** (LKJS, vessel) | ✅ | ✅ | ✅ | ✅ | ✅ | – | – | ✅ |
| **Small/simple** (<5 staff, <€500K revenue) | ✅ | ✅ | ✅ | ✅ | – | – | – | ✅ |
| **Dormant/holding shell** | ✅ | – | ✅ | ✅ | – | – | – | ✅ |

---

## Document Reading Strategy (Cost-Conscious)

A typical portfolio company has 500–2,500 files in SharePoint. **Reading them all is not the goal and not necessary.**

**The rule: read documents that answer open questions. Stop when questions are answered.**

Järvisydän Oy has 2,528 files. We've read ~40. The remaining ~2,450 break down as:

| Folder | Files | Read? | Why |
|--------|-------|-------|-----|
| sopimukset/ | 526 | 6 of 526 | Read the 6 customer contracts. Skim property lease index. Skip historical deeds. |
| luvat-ja-vakuutukset/ | 942 | ~10 targeted | Opera folder (67) = likely setup docs not booking exports. Read credit rating + key permits only. |
| kiinteistot/ | 396 | 0 | Skip unless specific property question arises. 162 sale deeds = historical, one-time events. |
| henkilosto/ | 16 | 0 | Read only if people question arises. |
| talous/ remaining | ~100 | 5 targeted | **2025 trial balances (Aug–Dec) = highest priority.** Related-party entities xlsx. |

**~20-30 targeted files from 2,450 will give 80% of remaining value.**

**Priority reads for Järvisydän (do these next, in order):**
1. `Trial Balance 31.8–31.12.2025` (5 files) — most current financials, right up to saneeraus filing
2. `Järvisydän Oy omistusyhteysyritykset 31.12.2024.xlsx` — related party entities (⭐)
3. `Luotettava_Kumppani_raportti_2025-10-15.pdf` — credit rating Oct 2025
4. `Osakasluettelo Järvisydän Oy.xlsx` — shareholder register (confirms ownership %)
5. `asiakas-sopimukset/` (6 files) — customer contract terms
6. Opera PMS folder (spot-check 5 files) — confirm if booking exports or setup docs only
7. Finnvera/Nordea/Siemens presentations (Aug 2022, 3 files) — financing structure

**Documents to skip for Järvisydän:**
- `kauppakirjat/` (162 deeds) — historical property transactions, not ongoing obligations
- `tuet/` (129 grants) — unless specific grant obligation question arises
- `anniskelulupa/` (12 alcohol licenses) — routine permits
- `kalustoluettelot/` (43 equipment inventories) — low strategic value
- Most of `Vuokrasopimukset-kiinteistöt/` (27 leases) — read INDEX only unless lease renewal is imminent

---

## Cost Model

**API cost:** $0 for file-reading work. All reading runs in Claude Code (subscription).

**Real costs:**
- **Subscription** — Claude Pro/Teams requires extra usage purchase when the base quota is exceeded. File-heavy sessions (reading 20+ documents) burn usage. Budget ~1 unit of extra usage per document-reading session.
- **Patrick's time** — the actual gate. Each targeted document = 10-20 minutes. Reading 20 priority files = ~4 hours total. Reading 2,450 files = ~400 hours. Never read exhaustively.
- **Batch API** — only if explicitly running a batch job (e.g., mass classification). Confirm cost estimate before any batch run.

**Järvisydän pilot actual API spend (sessions 33-39):** $0.00

---

## Decision Gates Summary

| After Layer | Gate Question | If No → |
|---|---|---|
| Layer 0 | Ownership clear? | Patrick interview before Layer 1 |
| Layer 1 | >10 readable documents? | Switch to Patrick interview mode, skip to Layer 7 |
| Layer 2 | Any qualified audit or going concern? | Flag to Patrick before proceeding |
| Layer 4 | Meaningful operational gap? | Skip Layers 5-6, go to Layer 7 |
| Before Layer 5 | Patrick approves $10-30 spend? | Skip Layer 5 |

---

## Lessons from the Järvisydän Pilot (Sessions 33-39)

These saved significant time or revealed critical information:

1. **TTK ≠ financial figures.** Audit reports contain opinions only. All financial figures are in tilinpäätös. Don't try to extract numbers from TTK.

2. **Board minutes reveal hidden events.** Patrick's removal from JS Oy board (Aug 2023) was not in any public register. Board minutes are often the only source of ownership and governance events.

3. **Sniffer-first for Excel.** Always run the sniffer script before full extraction. The budget Excel had 19 sheets and potential 16K column traps. See `excel-mining-protocol.md`.

4. **Scanned PDFs hide critical information.** The trigger for LKJS saneeraus (the 33-day collapse) is in a scanned PDF. Note OCR blockers in Layer 1 immediately and build an OCR backlog list.

5. **Fiscal year ≠ calendar year.** LKJS has a non-standard fiscal year. Always check before comparing companies.

6. **Two legal entities can look like one business.** LKJS Oy and JS Oy look like the same business but have separate financials, separate credit ratings, and separate governance status. Always work at the legal entity level.

7. **Ask Patrick: "Does a budget Excel exist?"** It may not be in SharePoint. Järvisydän's budget was found only because Patrick mentioned it.

8. **"Clean opinion" ≠ "healthy company."** LKJS had a clean TTK in Nov 2024 and filed for saneeraus in Jan 2025. Board minutes + tilinpäätös are the real signal.

9. **The 8 OCR-blocked PDFs.** If critical decisions (like the saneeraus trigger) are in scanned PDFs, they must go into an explicit backlog — don't silently skip them.

10. **Raw extracts are insurance.** Always save raw extraction before writing analysis. If the analysis session crashes or the wrong question was asked, the raw extraction is still there.

---

## Validation — When Is a Company "Known"?

A company is sufficiently known when Patrick can:
- [ ] Explain what it does in 2 minutes without notes (Layer 0)
- [ ] Locate any critical document in under 1 minute (Layer 1)
- [ ] State the audit opinion for the last 3 years from memory (Layer 2)
- [ ] State revenue, EBITDA, and equity for the last 3 years from memory (Layer 3)
- [ ] Identify the top 3 financial risks without searching (Layer 4)
- [ ] Brief auditors or a bank on group structure without preparation (Layer 7)
- [ ] Hand a governance template to a staff member and know they can fill it in correctly (Layer 7)

---

## Replication Order — Suggested Sequence for All 10 Companies

Complete one company end-to-end before starting the next. The pilot validated the template — do not try to parallelize too early.

**Priority order (suggested):**
1. ✅ Järvisydän Oy — pilot complete (Layers 0-4 done, Layers 5-6 pending)
2. Lomakylä Järvisydän Oy — entity profile exists, document inventory next
3. Finland DMC Oy — entity profile + email mining data already exists (rich)
4. Houseboat Saimaa Oy — entity profile exists, small company (Layers 0-4 sufficient)
5. RS Resort Services Oy — entity profile exists, minimal documents
6-10. Companies 7-10 — to be identified and onboarded

---

*Source: 1658 Holdings pilot — Järvisydän sessions 33-39. Pattern: company-intelligence-protocol. Tier B. Propose Tier A after 3 successful full-company runs.*
