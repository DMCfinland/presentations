# Finnish Governance Document Style Guide

**Purpose:** Canonical style reference for all Finnish corporate governance documents
**Author:** Extracted from 1658 Holdings best practices + Finnish governance batch results
**Date:** 2026-02-11
**Status:** Living document — update as new patterns emerge

---

## I. METADATA HEADER FORMAT

Every governance document starts with a metadata header using bold labels:

```markdown
**Decision:** [Brief description of what this document is]
**Author:** [Patrick Heiskanen or entity name]
**Date:** [YYYY-MM-DD]
**Status:** [Living document | Definitive | Draft | Archived]
```

**Example:**
```markdown
**Decision:** Synthesized from Opus batch results + HHJ certification standards
**Author:** Patrick Heiskanen
**Date:** 2026-02-11
**Status:** Living document — update as laws change or practice evolves
```

---

## II. DOCUMENT STRUCTURE HIERARCHY

### Section Headers

Use markdown `##`, `###`, `####` hierarchy:

```markdown
## I. MAJOR SECTION (ROMAN NUMERALS)

### Subsection Name

#### Detail Level

**Bold for emphasis within text**
```

### Horizontal Rules

Use `---` (three dashes) to separate major sections:

```markdown
---

## Next Major Section
```

---

## III. BILINGUAL FORMATTING

Finnish corporate governance requires bilingual Finnish/English presentation.

### Primary: Finnish Term + English in Parentheses

**Pattern:** `Finnish term (English translation)`

**Examples:**
- Hallituksen kokouksen pöytäkirja (board meeting minutes)
- Yhtiökokouksen pöytäkirja (shareholder meeting minutes)
- Päätös (decision)
- Esteellisyys (conflict of interest)
- Osingonjako (dividend distribution)
- Vastuuvapaus (discharge from liability)

### Side-by-Side Headers

For document templates, use both languages in the header:

```markdown
# HALLITUKSEN KOKOUKSEN PÖYTÄKIRJA / BOARD MEETING MINUTES
```

### Bilingual Section Labels

```markdown
## Kokoustiedot / Meeting Information
```

---

## IV. LEGAL CITATION FORMAT

### Finnish Law References

**Pattern:** `LAW #:#` or `LAW #:# §`

**Examples:**
- OYL 6:6 (Osakeyhtiölaki, Chapter 6, Section 6)
- KPL 3:6 (Kirjanpitolaki, Chapter 3, Section 6)
- TilintL 2:2 (Tilintarkastuslaki, Chapter 2, Section 2)
- TSL 1:3 § (Työsopimuslaki, Chapter 1, Section 3, § sign used when emphasizing section)
- VML 31 § (Verotusmenettelylaki, Section 31)

### In-Text Citation Style

**Pattern:** Cite law + brief English explanation in same sentence

**Examples:**
- "Board has quorum when more than half of members are present (OYL 6:3)."
- "AGM must be held within 6 months of financial year end (OYL 5:3)."
- "Financial statements must be signed by April 30 (KPL 3:6)."

### Multiple Citations

Use comma-separated list: `OYL 6:6, 6:3, 6:4`

---

## V. VALIDATION FRAMEWORK (RED/YELLOW/GREEN)

### Three-Tier System

Every document type uses this validation structure:

```markdown
**🔴 RED — Must include:**
- [Legal requirement 1]
- [Legal requirement 2]
- [Law reference in parentheses]

**🟡 YELLOW — HHJ standard:**
- [Best practice 1]
- [Best practice 2]

**🟢 GREEN — Excellence:**
- [Excellence standard 1]
- [Excellence standard 2]
```

### Severity Meanings

| Level | Meaning | Action |
|-------|---------|--------|
| 🔴 **RED** | Legal requirement — must pass | Fix before signing/filing |
| 🟡 **YELLOW** | HHJ best practice — should pass | Address to meet governance standard |
| 🟢 **GREEN** | Excellence standard — nice to have | Differentiates in due diligence |

---

## VI. PLACEHOLDER CONVENTIONS

### Curly Braces for Variables

Use `{Variable_Name}` format for fields to be filled:

**Examples:**
```markdown
{Company_Name}
{Y_tunnus}
{Meeting_Date}
{Meeting_Number}
{Chairman_Name}
{Board_Member_1_Name}
{Agenda_Item_Title}
{Decision_Text}
```

### Finnish Placeholders

For Finnish-language sections, use descriptive Finnish placeholders:

```markdown
{Yhtiön_nimi}
{Kokousnumero}
{Päivämäärä}
{Puheenjohtajan_nimi}
```

### Bracket Instructions

Use `[INSTRUCTION: action to take]` for procedural guidance within templates:

```markdown
[INSTRUCTION: List all board members present]
[INSTRUCTION: If quorum not met, stop here — meeting cannot proceed]
```

### Fill-in Prompts

Use `[TÄYTÄ: field description]` (Finnish) or `[FILL: field description]` (English):

```markdown
[TÄYTÄ: esityslistakohta 1]
[FILL: decision text here]
```

---

## VII. TABLE FORMATS

### Reference Tables

Use markdown tables for structured reference data:

```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data | Data | Data |
```

### Legal Deadline Tables

**Pattern:** Deadline | Date | Consequence | Law

```markdown
| Deadline | Date (Dec 31 FY) | Consequence of Missing | Law |
|----------|------------------|----------------------|-----|
| Financial statements signed | **30 April** | KPL breach; personal liability for board | KPL 3:6 |
| AGM held | **30 June** | OYL breach; resolutions challengeable | OYL 5:3 |
```

### Compliance Matrices

**Pattern:** Document Type | Finnish Name | Primary Law | Required Elements

```markdown
| # | Document Type | Finnish Name | Primary Law | Required Elements |
|---|---|---|---|---|
| 1 | Board minutes | Hallituksen kokouksen pöytäkirja | OYL 624/2006 | Date, attendees, quorum, decisions |
```

### Validation Checklists

Use checkbox format `☐` for incomplete, `✅` for complete:

```markdown
## Validation Checklist

### 🔴 RED Items (Legal Requirements)
☐ Sequential number present
☐ Date and place documented
☐ All attendees listed with roles
☐ Quorum confirmed (>50% present per OYL 6:3)

### 🟡 YELLOW Items (HHJ Best Practices)
☐ Agenda circulated 5+ days in advance
☐ Decision rationale documented
☐ Action items with owners and deadlines
```

---

## VIII. BLOCKQUOTE USAGE

### Key Insights

Use `>` blockquotes for critical guidance or warnings:

```markdown
> **For sole board member (Patrick):** Minutes discipline is MORE important, not less. No peer checks your work. The minutes are the only evidence of informed decision-making if liability questions arise.
```

### Legal Quotes

Use blockquotes for direct legal provisions:

```markdown
> OYL 6:4 — Esteellisyys: Board member may NOT participate in matters involving a contract between the member and the company.
```

---

## IX. PROFESSIONAL LEGAL TONE

### Writing Style

- **Direct and practical:** Get to the point quickly
- **Formal but accessible:** Professional without being stiff
- **Bilingual precision:** Finnish legal terms with English explanations
- **Action-oriented:** Tell the reader what to do, not just what the law says
- **Scannable:** Use bullets, tables, headers for quick reference

### Tone Examples

**Good:**
```markdown
Board has quorum when more than half of members are present (OYL 6:3). If 3 board members exist, minimum 2 must attend.
```

**Avoid (too academic):**
```markdown
The Finnish Companies Act, in its Chapter 6, Section 3, establishes a quorum requirement whereby the board of directors must have in attendance a majority of its duly appointed members in order for the meeting to be considered validly convened for the purposes of passing resolutions.
```

### "For 1658 Holdings:" Application Sections

After presenting general rules, add practical application:

```markdown
### For 1658 Holdings:

- **Schedule subsidiary AGMs before Holdings AGM** — dividend cascade requires subsidiaries to decide and pay first
- **Property companies** need only 2-4 board meetings/year — consolidate with operating company meetings
```

---

## X. DOCUMENT NAMING CONVENTIONS

### File Naming Pattern

From [document-architecture.md](../../best-practices/document-architecture.md):

```
{company-prefix}-{category}-{description}-{date}.{ext}
```

**Examples:**
```
dmc-corp-hallitus-ptk-1-2024-01-15.pdf
jsy-corp-yhtiokokous-ptk-2024-06-20.pdf
1658-corp-hallitus-paatos-2024-03-10.md
```

### Category Codes

| Code | Category | Finnish Equivalent |
|------|----------|--------------------|
| `corp` | Corporate | Hallinto/Yhtiöoikeus |
| `con` | Contracts | Sopimukset |
| `fin` | Financial | Talous |
| `emp` | Employment | Työsopimukset |
| `ops` | Operations | Toiminta |
| `prop` | Property | Kiinteistö |
| `ico` | Inter-company | Konserni |

---

## XI. SIGNATURE BLOCKS

### Board Minutes Signature Block

```markdown
---

**Allekirjoitukset / Signatures:**

Puheenjohtaja / Chairman:

_________________________________
{Chairman_Name}

Jäsen / Member:

_________________________________
{Board_Member_Name}

[INSTRUCTION: If sole board member, omit second signature]
```

### Shareholder Meeting Signature Block

```markdown
---

**Allekirjoitukset / Signatures:**

Kokouksen puheenjohtaja / Chairman of the meeting:

_________________________________
{Meeting_Chairman_Name}

Pöytäkirjantarkastaja / Minutes reviewer:

_________________________________
{Minutes_Reviewer_Name}

[INSTRUCTION: If sole shareholder, minutes reviewer not required]
```

---

## XII. TEMPLATE LOCATIONS

All Finnish governance templates stored in:

```
_shared/templates/finnish-governance/
```

**Naming pattern:**
```
{document-type-slug}-template.md
```

**Examples:**
- `board-minutes-template.md`
- `shareholder-meeting-minutes-template.md`
- `board-resolution-template.md`
- `agm-notice-template.md`
- `shareholder-resolution-template.md`

---

## XIII. VALIDATION CHECKLIST STRUCTURE

Every template ends with a validation checklist:

```markdown
---

## VALIDATION CHECKLIST

**Use this checklist before finalizing the document.**

### 🔴 RED — Legal Requirements (Must Pass)
☐ [Requirement 1 with OYL reference]
☐ [Requirement 2 with OYL reference]
☐ [Requirement 3 with OYL reference]

### 🟡 YELLOW — HHJ Best Practices (Should Pass)
☐ [Best practice 1]
☐ [Best practice 2]
☐ [Best practice 3]

### 🟢 GREEN — Excellence Standards (Nice to Have)
☐ [Excellence standard 1]
☐ [Excellence standard 2]

---

**Document Status:**
☐ Draft — not yet reviewed
☐ Ready for signature
☐ Signed and filed
```

---

## XIV. QUICK REFERENCE SECTIONS

Include "Quick Reference" sections for scannable lookup:

```markdown
## Quick Reference — AGM Statutory Deadlines

| Action | Deadline | Law |
|--------|----------|-----|
| AGM held | 6 months after FY end | OYL 5:3 |
| Financial statements signed | 4 months after FY end | KPL 3:6 |
| Notice sent | 1 week–2 months before meeting | OYL 5:19 |
| Financial statements available | 1 week before meeting | OYL 5:21 |
```

---

## XV. FINNISH LEGAL TERMINOLOGY INDEX

Common terms used throughout governance documents:

| Finnish | English | Context |
|---------|---------|---------|
| Hallitus | Board of directors | OYL Chapter 6 |
| Hallituksen kokous | Board meeting | Regular board meeting |
| Hallituksen päätös | Board resolution | Decision without formal meeting |
| Yhtiökokous | General meeting / Shareholder meeting | OYL Chapter 5 |
| Varsinainen yhtiökokous | Annual General Meeting (AGM) | OYL 5:3 |
| Ylimääräinen yhtiökokous | Extraordinary General Meeting (EGM) | OYL 5:3a |
| Pöytäkirja | Minutes | Written record of meeting |
| Päätös | Decision | Resolution or determination |
| Päätösvaltaisuus | Quorum | Minimum attendance for valid decisions |
| Esteellisyys | Conflict of interest / Disqualification | OYL 6:4 |
| Puheenjohtaja | Chairman | Meeting or board leader |
| Pöytäkirjantarkastaja | Minutes reviewer | Verifies accuracy of AGM minutes |
| Toimitusjohtaja | Managing Director (MD) | CEO equivalent, OYL 6:17-6:20 |
| Osingonjako | Dividend distribution | OYL Chapter 13 |
| Vastuuvapaus | Discharge from liability | AGM grants to board/MD |
| Tilinpäätös | Financial statements | Annual FS per KPL |
| Toimintakertomus | Board's report | Management commentary on FS |
| Yhtiöjärjestys | Articles of association | Company's constitutional document |
| Y-tunnus | Business ID | Finnish business identification number |
| PRH | Patent and Registration Office | Patentti- ja rekisterihallitus |
| Maksukykyisyys | Solvency | Ability to pay debts as they fall due |
| Tasetesti | Balance sheet test | OYL 13:2 distribution limit test |

---

## XVI. COMPLIANCE FOOTNOTES

When referencing legal requirements, use footnotes for full statutory citations:

```markdown
Board meeting minutes must include decisions, votes, and dissenting opinions.[^1]

[^1]: OYL 6:6 §: "Hallituksen päätöksistä on pidettävä pöytäkirjaa. Pöytäkirjaan on merkittävä päätökset ja äänestykset sekä eriävät mielipiteet."
```

---

## XVII. HOLDING STRUCTURE NOTES

For 10-company structure, include specific guidance:

```markdown
### For Holding Structures:

- **Inter-company transactions:** All agreements between portfolio companies require esteellisyys assessment and arm's length documentation (VML 31 §, OYL 6:4)
- **Dividend cascade:** Subsidiary AGMs must occur BEFORE Holdings AGM to enable dividend flow upward
- **Batch processing:** Coordinate similar governance activities (e.g., all April FS signings in one day)
```

---

## XVIII. DOCUMENT HISTORY SECTION

Every template should include a document history footer:

```markdown
---

## Document History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2026-02-11 | 1.0 | Initial template created from Finnish governance batch results | Patrick Heiskanen |
| [Date] | [Version] | [Changes made] | [Name] |
```

---

## XIX. CROSS-REFERENCE FORMAT

When referencing other documents or templates:

**Markdown link format:**
```markdown
See [document-architecture.md](../../best-practices/document-architecture.md) for naming rules.
```

**File path format:**
```markdown
**Template location:** `_shared/templates/finnish-governance/board-minutes-template.md`
```

---

## XX. CONDITIONAL SECTIONS

Use clear markup for conditional content:

```markdown
### [IF sole shareholder:]

Minutes reviewer (pöytäkirjantarkastaja) is NOT required per OYL 5:23 § 2 mom.

### [IF multiple shareholders:]

At least one minutes reviewer must be elected (OYL 5:23 §).
```

---

## STYLE GUIDE USAGE

When creating a new Finnish governance document or template:

1. ✅ Start with metadata header (Section I)
2. ✅ Use bilingual formatting (Section III)
3. ✅ Include RED/YELLOW/GREEN validation (Section V)
4. ✅ Use proper placeholders (Section VI)
5. ✅ Add "For 1658 Holdings:" application notes
6. ✅ Include validation checklist at end (Section XIII)
7. ✅ Add signature blocks (Section XI)
8. ✅ Use proper file naming (Section X)

---

**This style guide is the single source of truth for all Finnish corporate governance documents in the 1658 Holdings system.**
