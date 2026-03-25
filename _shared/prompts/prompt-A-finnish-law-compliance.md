# Prompt A: Finnish Law Compliance Matrix & Validation Checklists

**Target:** Claude Opus (Batch API)
**Focus:** Legal requirements mapping — OYL, Kirjanpitolaki, Tilintarkastuslaki, Kaupparekisterilaki
**Batch ID:** prompt-A-law-compliance
**Part:** 1 of 3 (merge with B + C after all complete)

---

# RESEARCH REQUEST: Finnish Corporate Law Compliance Matrix for Document Drafting System

## CRITICAL INSTRUCTION

**Write the actual compliance matrix, validation checklists, and legal requirement tables directly. Do NOT write commentary about what they should contain. Do NOT describe what you would write. WRITE IT.**

Every section below must contain concrete, usable content — specific OYL section numbers, specific requirements, specific checklist items. If a section heading says "Compliance Matrix," write the matrix. Not a description of the matrix.

Your output will be merged with two other focused prompts into a single best-practices document. This session must produce standalone, complete legal reference material.

## Context

Patrick Heiskanen, CEO of **1658 Holdings Oy** — Finnish family holding company, 10 portfolio companies, ~50 employees. HHJ (Hyväksytty Hallituksen Jäsen) certified by Suomen Kauppakamari. Building a Finnish corporate governance document drafting system using Claude Code and Claude Cowork plugins (structured markdown architecture).

**The goal:** An AI system that drafts, reviews, and validates corporate documents for 10 companies following Finnish law. Every document must pass a compliance checklist before being finalized. This prompt defines what those checklists contain.

**Company structure:**
- 1658 Holdings Oy (parent)
- Finland DMC Oy (IT/marketing, 5 staff)
- Järvisydän Oy (resort, employees + kiinteistöyhtiöt)
- Companies 3-10 (various industries, some with employees, some shell/property)

## Deliverable 1: Master Compliance Matrix

Create a comprehensive matrix mapping **each document type** to its **specific legal requirements** from Finnish law. Use this exact format:

| Document Type | Finnish Name | Primary Law | Specific Sections | Required Elements | Filing Requirement |
|---|---|---|---|---|---|
| Board meeting minutes | Hallituksen kokouksen pöytäkirja | OYL 624/2006 | 6:6, 6:3, 6:4 | [list every required element] | Company archive, available to auditor |
| ... | ... | ... | ... | ... | ... |

**Document types to cover (minimum 12):**
1. Board meeting minutes (hallituksen kokouksen pöytäkirja)
2. Shareholder meeting minutes (yhtiökokouksen pöytäkirja)
3. Board resolution without meeting (hallituksen päätös ilman kokousta)
4. Articles of association (yhtiöjärjestys)
5. Shareholders' agreement (osakassopimus)
6. Inter-company service agreement (konserninsisäinen palvelusopimus)
7. Annual report / Board's report (toimintakertomus)
8. Financial statements (tilinpäätös)
9. Trade register filings (kaupparekisteri-ilmoitukset)
10. Dividend resolution (osingonjakopäätös)
11. Employment contract (työsopimus)
12. Power of attorney / proxy (valtakirja / prokuura)

For each document, cite the **specific law number and section** (e.g., "OYL 624/2006, 6:6 § 1 momentti").

## Deliverable 2: Law-by-Law Requirement Summary

For each of the following laws, write a practical summary of what it requires for corporate document management. Not a general overview — specific requirements that affect document drafting and archiving.

### Osakeyhtiölaki (OYL 624/2006)
Cover these chapters in detail:
- **Ch. 5 (Yhtiökokous):** Meeting notice requirements, agenda, voting, minutes (5:23), minutes reviewer, filing with PRH
- **Ch. 6 (Yhtiön johto):** Board composition, quorum (6:3), conflict of interest/esteellisyys (6:4), minutes (6:6), managing director duties
- **Ch. 8 (Osakkeet):** Share register requirements, transfer documentation
- **Ch. 13 (Varojen jakaminen):** Dividend decision requirements, distribution test, board proposal format
- **Ch. 14 (Yhtiön omat osakkeet):** If relevant to holding structure
- **Ch. 16 (Yhtiöjärjestys):** Articles of association requirements, amendment process
- **Ch. 20-21:** Restructuring, merger documentation requirements

For each chapter: What documents are required? What must they contain? Who signs? Where are they filed? What happens if requirements are not met?

### Kirjanpitolaki (1336/1997)
- Financial statements requirements (Ch. 3)
- Record retention periods (Ch. 2:10)
- Board's report (toimintakertomus) requirements and thresholds
- Small company exemptions (when do they apply to Patrick's companies?)
- Digital archiving requirements

### Tilintarkastuslaki (1141/2015)
- Audit requirement thresholds (when is audit mandatory?)
- Auditor's report requirements
- Board's obligation to provide information to auditor
- What documents the auditor needs access to

### Kaupparekisterilaki (129/1979)
- What must be registered with PRH
- Filing deadlines (after AGM, after board changes, after articles amendment)
- Required attachments for each filing type
- Digital filing via PRH.fi / YTJ.fi

### Työsopimuslaki (55/2001)
- Employment contract required elements
- Written vs. oral contract rules
- Mandatory terms to include
- Non-compete clause restrictions (2022 amendment)

## Deliverable 3: Per-Document Validation Checklists

For each of the 12 document types, create a validation checklist using the **RED / YELLOW / GREEN severity system:**

- **RED (OYL/law requirement):** If missing, the document is legally deficient or invalid. Must fix before finalizing.
- **YELLOW (HHJ/Kauppakamari best practice):** Not legally required, but recommended by professional governance standards. Missing = governance quality concern.
- **GREEN (Excellence standard):** Best-in-class practice. Recommended but absence is acceptable.

**Format for each checklist:**

```
## [Document Type] — Validation Checklist

### RED — Legal Requirements (must pass)
- [ ] [Specific requirement] — [Law reference, e.g., OYL 6:6]
- [ ] [Specific requirement] — [Law reference]
...

### YELLOW — Governance Best Practices (should pass)
- [ ] [Specific practice] — [HHJ/Kauppakamari reference]
...

### GREEN — Excellence Standards (nice to have)
- [ ] [Specific standard]
...
```

Write the **complete** checklist for all 12 document types. Not abbreviated. Not "similar to above." Every document gets its own full checklist.

## Deliverable 4: Filing Requirements & Deadlines

Create a reference table of all mandatory filing requirements:

| Event | Filing Destination | Deadline | Required Documents | Law Reference |
|---|---|---|---|---|
| AGM held | PRH (trade register) | 2 months after AGM | Minutes extract, financial statements | OYL 5:23, KRL |
| Board member change | PRH | Without delay | Board minutes, acceptance | KRL 14 § |
| ... | ... | ... | ... | ... |

Include all filing events relevant to a 10-company holding structure.

## Deliverable 5: Record Retention Requirements

| Document Type | Minimum Retention | Law Reference | Notes |
|---|---|---|---|
| Financial statements | 10 years | Kirjanpitolaki 2:10 | From end of financial year |
| Board minutes | [research] | [cite] | |
| Employment contracts | [research] | [cite] | After employment ends |
| ... | ... | ... | ... |

## Constraints

- Finnish law ONLY — cite Finlex.fi as authoritative source
- Specific section numbers required — not "per OYL" but "per OYL 6:6 § 1 mom."
- Bilingual terminology: Finnish primary, English in parentheses
- Focus on Oy (private limited company), not Oyj (public)
- Include small company exemptions where relevant (most of Patrick's 10 companies are small/micro by Kirjanpitolaki thresholds)

## Reference Sources

1. **Finlex.fi** — Official Finnish legal database (authoritative)
2. **OYL 624/2006** — Osakeyhtiölaki
3. **Kirjanpitolaki 1336/1997** — Accounting Act
4. **Tilintarkastuslaki 1141/2015** — Auditing Act
5. **Kaupparekisterilaki 129/1979** — Trade Register Act
6. **Työsopimuslaki 55/2001** — Employment Contracts Act
7. **PRH.fi** — Patent and Registration Office
8. **YTJ.fi** — Business Information System

---

**Remember: Write the actual tables, matrices, and checklists. Not descriptions. Not commentary. Not "this section would contain..." — write the content itself. Every checkbox, every law reference, every deadline. This is a reference document that will be used for 5+ years across 10 companies.**
