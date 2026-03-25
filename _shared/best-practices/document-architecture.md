# Document Architecture for 1658 Holdings
<!-- last_updated: session-28 -->

**Decision:** Option B — Centralized `documents/` folder at holdings level
**Author:** Claude (strategic architecture decision)
**Date:** 2026-02-11
**Status:** Definitive — implement as described

---

## The Decision

All company documents live in a single `documents/` folder at the holdings root. AI work products stay in their existing `*-AIFiles/` folders. This gives you one place for truth and separate places for work.

The reasoning is straightforward: your document drafter needs to pull facts from any company at any time. Inter-company agreements, group financials, and shareholder docs need a natural home, and your document drafter needs one root to search — not ten. A distributed model forces your AI tools to search 10+ separate trees and leaves holdings-level documents homeless. A centralized model gives you one root to point any tool at, one naming convention to enforce, and one place to audit.

The concern about separating documents from AI work products is actually a feature. Documents are legal source material — they don't change based on what AI project you're running. AI work products are ephemeral outputs. Keeping them apart prevents accidental mixing of drafts with originals.

---

## Folder Structure

```
~/1658HoldingsOy-AIFiles/
│
├── CLAUDE.md
├── ROADMAP.md
├── MODEL-STRATEGY.md
│
├── documents/                                    # === SOURCE OF TRUTH ===
│   ├── _index.md                                 # Master document registry (auto-generated)
│   ├── _naming-rules.md                          # This file's naming section, standalone
│   │
│   ├── _holdings/                                # Holdings-level documents
│   │   ├── corporate/
│   │   │   ├── 1658-corp-articles-of-association-2024.pdf
│   │   │   └── 1658-corp-shareholder-agreement-2023.pdf
│   │   ├── financial/
│   │   │   ├── 1658-fin-group-annual-report-2024.pdf
│   │   │   └── 1658-fin-group-tax-filing-2024.pdf
│   │   └── inter-company/
│   │       ├── 1658-ico-dmc-jarvisydan-service-agreement-2024.pdf
│   │       └── 1658-ico-dmc-jarvisydan-marketing-sla-2024.pdf
│   │
│   ├── finland-dmc-oy/
│   │   ├── corporate/
│   │   │   ├── dmc-corp-articles-of-association-2020.pdf
│   │   │   ├── dmc-corp-trade-register-extract-2024.pdf
│   │   │   └── dmc-corp-board-minutes-2024-03.pdf
│   │   ├── contracts/
│   │   │   ├── dmc-con-office-lease-helsinki-2023.pdf
│   │   │   └── dmc-con-saas-hubspot-2024.pdf
│   │   ├── financial/
│   │   │   ├── dmc-fin-annual-report-2024.pdf
│   │   │   └── dmc-fin-vat-return-2024-q4.pdf
│   │   └── employment/
│   │       └── dmc-emp-template-employment-contract-2024.pdf
│   │
│   ├── jarvisydan-oy/
│   │   ├── corporate/
│   │   ├── contracts/
│   │   ├── financial/
│   │   ├── operations/
│   │   │   ├── jsy-ops-liquor-license-2024.pdf
│   │   │   └── jsy-ops-health-inspection-2024-06.pdf
│   │   └── property-companies/
│   │       ├── kiinteisto-abc-oy/
│   │       │   ├── kabc-corp-articles-of-association-2019.pdf
│   │       │   ├── kabc-prop-deed-of-sale-2019.pdf
│   │       │   └── kabc-prop-land-survey-2019.pdf
│   │       └── kiinteisto-xyz-oy/
│   │           ├── kxyz-corp-articles-of-association-2021.pdf
│   │           └── kxyz-prop-building-permit-2022.pdf
│   │
│   └── [company-slug-oy]/                        # Template for companies 3–10
│       ├── corporate/
│       ├── contracts/
│       ├── financial/
│       └── [industry-specific]/
│
├── _shared/                                      # Cross-company resources (existing)
│   ├── best-practices/
│   │   └── document-architecture.md              # THIS FILE
│   ├── prompt-library/
│   └── templates/
│       ├── board-minutes-template.md
│       └── contract-template.md
│
├── FinlandDMCOy-AIFiles/                         # AI work products (existing)
│   ├── CLAUDE.md
│   ├── finland-dmc-2.0/
│   └── seo-audits/
│
├── JarvisydanOy-AIFiles/                         # AI work products (new)
│   └── CLAUDE.md
│
└── YouTubeResearch-AIFiles/                      # Research (existing)
    └── knowledge-base/
```

---

## Naming Convention

### Folder Names

All lowercase, hyphens only, no spaces, no special characters. Finnish characters converted: `a→a`, `o→o`, `a→a`.

| Level | Pattern | Example |
|-------|---------|---------|
| Company | `{legal-name-slug}/` | `jarvisydan-oy/` |
| Category | `{category}/` | `corporate/` |
| Property sub-company | `{slug}/` under `property-companies/` | `kiinteisto-abc-oy/` |

### File Names

```
{company-prefix}-{category}-{description}-{date}.{ext}
```

| Component | Rule | Examples |
|-----------|------|----------|
| **company-prefix** | 2–4 letter code, unique per entity | `1658`, `dmc`, `jsy`, `kabc` |
| **category** | 3-letter code from taxonomy below | `corp`, `con`, `fin`, `emp`, `ops`, `prop`, `ico` |
| **description** | Lowercase, hyphens, specific enough to identify | `articles-of-association`, `board-minutes`, `office-lease-helsinki` |
| **date** | `YYYY` or `YYYY-MM` or `YYYY-MM-DD` | `2024`, `2024-03`, `2024-03-15` |
| **ext** | Original format | `.pdf`, `.docx`, `.xlsx` |

### Company Prefix Registry

Maintain this in `documents/_index.md`:

| Prefix | Company | Business ID |
|--------|---------|-------------|
| `1658` | 1658 Holdings Oy | [Y-tunnus] |
| `dmc` | Finland DMC Oy | [Y-tunnus] |
| `jsy` | Jarvisydan Oy | [Y-tunnus] |
| `kabc` | Kiinteisto ABC Oy | [Y-tunnus] |
| ... | ... | ... |

### Examples

```
dmc-corp-articles-of-association-2020.pdf
dmc-corp-board-minutes-2024-03.pdf
dmc-con-office-lease-helsinki-2023.pdf
dmc-fin-annual-report-2024.pdf
jsy-ops-liquor-license-2024.pdf
1658-ico-dmc-jarvisydan-service-agreement-2024.pdf
1658-fin-group-annual-report-2024.pdf
kabc-prop-deed-of-sale-2019.pdf
```

---

## Document Category Taxonomy

These seven categories cover all document types across any company type (service company, resort operator, property company, holding company).

| Code | Category | What Goes Here |
|------|----------|----------------|
| `corp` | Corporate | Articles of association, trade register extracts, board minutes, shareholder resolutions, powers of attorney, company formation docs |
| `con` | Contracts | Leases, service agreements, vendor contracts, SaaS subscriptions, NDAs, partnership agreements |
| `fin` | Financial | Annual reports, tax filings, VAT returns, auditor reports, bank statements, budgets, invoices (key ones only) |
| `emp` | Employment | Employment contracts, salary structures, benefit agreements, termination records, collective bargaining agreements |
| `ops` | Operations | Licenses, permits, inspections, certifications, insurance policies, safety records |
| `prop` | Property | Deeds, land surveys, building permits, zoning decisions, maintenance records, tenant agreements |
| `ico` | Inter-company | Agreements between portfolio companies, transfer pricing docs, management fee agreements, intra-group loans |

**Rules:**

- If a document fits two categories, use the primary purpose. A lease for an office is `con` (contract). A property deed is `prop`.
- Inter-company documents (`ico`) always live in `_holdings/inter-company/`, never in individual company folders, even if only two companies are involved. This prevents duplication and conflicting versions.
- Board minutes are always `corp`, even if they approve a financial matter.

---

## Cross-Company Document Handling

### Rule: Single Source, Never Duplicate

Every document has exactly one canonical location. Cross-references are handled by naming convention, not symlinks or copies.

| Document Type | Lives In | Why |
|---------------|----------|-----|
| Service agreement between DMC and Jarvisydan | `_holdings/inter-company/` | Involves multiple entities |
| Group consolidated financials | `_holdings/financial/` | Holdings-level scope |
| Shareholder agreement | `_holdings/corporate/` | Holdings-level governance |
| DMC's own annual report | `finland-dmc-oy/financial/` | Single-entity scope |
| Property deed for a kiinteistoyhtiö | `jarvisydan-oy/property-companies/{slug}/` | Belongs to that entity |

### The Naming Convention Does the Linking

Inter-company documents use the naming pattern:

```
1658-ico-{party1}-{party2}-{description}-{date}.{ext}
```

The document drafter can find all agreements involving DMC by searching for filenames containing `dmc` within `_holdings/inter-company/`. No database needed — the filesystem is the index.

---

## Document Registry (`_index.md`)

Create and maintain `documents/_index.md` as a machine-readable registry. This is the "single capture point" for the second brain.

```markdown
# Document Registry — 1658 Holdings

Last updated: 2026-02-11

## Company Prefixes
| Prefix | Legal Name | Y-tunnus | Status |
|--------|-----------|----------|--------|
| 1658 | 1658 Holdings Oy | 1234567-8 | Active |
| dmc | Finland DMC Oy | 2345678-9 | Active |
| jsy | Jarvisydan Oy | 3456789-0 | Active |

## Document Log
| Filename | Path | Category | Entities | Language | Added |
|----------|------|----------|----------|----------|-------|
| dmc-corp-articles-of-association-2020.pdf | finland-dmc-oy/corporate/ | corp | dmc | fi | 2026-02-11 |
| 1658-ico-dmc-jsy-service-agreement-2024.pdf | _holdings/inter-company/ | ico | dmc, jsy | en | 2026-02-11 |
```

This registry serves three purposes: the document drafter queries it to find facts, the "WHO" story builder uses it to map corporate structure, and future AI automation uses it as a classification index.

---

## Second Brain Compatibility

This architecture maps directly to the capture → classify → surface pattern:

### Capture
Drop new documents into the correct company folder with the correct filename. If unsure of category, drop into a `_inbox/` folder at the `documents/` root:

```
documents/
├── _inbox/                    # Temporary landing zone
│   └── scan-2026-02-11.pdf    # Unclassified document
```

A future Claude Code script can read `_inbox/`, analyze the document, suggest a filename and location, and move it with your approval.

### Classify
The naming convention IS the classification. Each filename encodes: entity, category, description, and date. The `_index.md` registry adds: language, related entities, and ingestion date. No separate database needed at this scale.

### Surface
The document drafter queries by: company prefix (all DMC docs), category code (all contracts), date range (all 2024 financials), or cross-reference (all documents mentioning Jarvisydan). All of these are simple filename/path searches on disk.

### Automation Path

When ready to automate, the progression is:

1. **Now:** Manual filing with naming convention. `_index.md` maintained by hand.
2. **Next:** Claude Code script that validates filenames, updates `_index.md`, and flags violations.
3. **Later:** OCR + AI classification pipeline that reads `_inbox/`, extracts metadata, proposes filename/location, and waits for approval.
4. **Eventually:** Proactive surfacing — "Board meeting for Jarvisydan next week. Here are the relevant documents from last quarter."

The architecture supports all four stages without restructuring.

---

## Scaling Assessment

At 10 companies × 200 documents = 2,000 files:

| Concern | Assessment |
|---------|------------|
| **Folder depth** | Maximum 4 levels (`documents/jarvisydan-oy/property-companies/kiinteisto-abc-oy/`). Manageable. |
| **Files per folder** | ~200 per company spread across 4–7 categories = 30–50 files per category folder. Well within filesystem comfort. |
| **Filename uniqueness** | Company prefix + category + description + date guarantees uniqueness across the entire tree. |
| **Search speed** | `find documents/ -name "*dmc*fin*"` returns in milliseconds on 2,000 files. `grep` across `_index.md` is instant. |
| **Claude Code compatibility** | Claude Code reads local files. A flat-ish structure with predictable paths means you can reference files by pattern, not memorized paths. |
| **Manual maintainability** | One person (Patrick) can maintain this with the naming convention as the only rule to follow. No tooling required, though tooling helps. |

At 10,000 documents (long-term), the `_index.md` approach starts to strain and you'd want a SQLite database or similar. But that's a problem for 2028, not 2026.

---

## Implementation Checklist

1. Create `documents/` folder at `~/1658HoldingsOy-AIFiles/documents/`
2. Create subfolders: `_holdings/`, `_inbox/`, `finland-dmc-oy/`, `jarvisydan-oy/`
3. Create category subfolders within each company folder
4. Create `_index.md` with company prefix registry
5. Create `_naming-rules.md` (extract naming section from this document)
6. Begin importing documents, starting with holdings-level and DMC
7. Update `_index.md` as each document is filed
8. Add property company subfolders under `jarvisydan-oy/property-companies/` as needed
9. Create placeholder folders for companies 3–10 as they're onboarded

---

## Quick Reference Card

```
WHERE does it go?
  Involves multiple companies? → documents/_holdings/inter-company/
  Holdings-level scope?        → documents/_holdings/{category}/
  Single company scope?        → documents/{company-slug}/{category}/
  Property company doc?        → documents/{parent}/property-companies/{slug}/
  Don't know yet?              → documents/_inbox/

HOW do I name it?
  {prefix}-{cat}-{description}-{date}.{ext}
  dmc-corp-board-minutes-2024-03.pdf

WHAT category?
  corp = governance    con = agreements    fin = money
  emp = people         ops = licenses      prop = real estate
  ico = between companies
```
