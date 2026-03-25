# Finnish Corporate Governance Templates

**Created:** 2026-02-11
**Author:** Patrick Heiskanen
**Source:** Finnish governance batch results + HHJ best practices + 1658 Holdings style guide

---

## Template Overview

This folder contains 5 core Finnish corporate governance document templates in both Markdown (.md) and Word (.docx) formats. All templates follow OYL (Companies Act 624/2006), KPL (Accounting Act 1336/1997), and HHJ (Hyväksytty Hallituksen Jäsen) best practices.

---

## Available Templates

### 1. Board Minutes (Hallituksen pöytäkirja)

**Files:**
- `board-minutes-template.md`
- `board-minutes-template.docx`

**When to use:**
- Regular board meetings
- Required for all significant board decisions
- Mandatory for OYL 6:6 compliance

**Key features:**
- Full bilingual format (Finnish/English)
- RED/YELLOW/GREEN validation checklist
- Esteellisyys (conflict of interest) section
- Action items tracking
- Sole board member notes

**Legal basis:** OYL 6:6, 6:3, 6:4

---

### 2. Shareholder Meeting Minutes (Yhtiökokouksen pöytäkirja)

**Files:**
- `shareholder-meeting-minutes-template.md`
- `shareholder-meeting-minutes-template.docx`

**When to use:**
- Annual General Meetings (AGM) — mandatory by June 30 (OYL 5:3)
- Extraordinary General Meetings (EGM)
- Any formal shareholder meeting

**Key features:**
- Complete AGM agenda with all OYL 5:3 mandatory items
- Shareholder attendance table with shares/votes
- Dividend distribution section with maksukyky assessment
- Board and auditor election sections
- PRH filing instructions

**Legal basis:** OYL 5:23, 5:3, KPL 3:6

---

### 3. Board Resolution (Hallituksen päätös ilman kokousta)

**Files:**
- `board-resolution-template.md`
- `board-resolution-template.docx`

**When to use:**
- Simple, urgent, or routine board decisions
- When convening a meeting is impractical
- Board unanimity can be confirmed in writing

**Key features:**
- Opportunity to participate documentation (OYL 6:3 § 2 critical requirement)
- All members' positions recorded
- Guidance on when to use vs. formal meeting
- Sole board member simplified format

**Legal basis:** OYL 6:3 § 2 mom.

---

### 4. AGM Notice (Yhtiökokouskutsu)

**Files:**
- `agm-notice-template.md`
- `agm-notice-template.docx`

**When to use:**
- Before every AGM (mandatory notice period: 1 week – 2 months, OYL 5:19)
- Before every EGM
- To formally convene shareholders

**Key features:**
- Complete statutory agenda for AGM (OYL 5:3)
- Board's proposals for all agenda items
- Document availability information (OYL 5:21)
- Participation and registration instructions
- Proxy form instructions

**Legal basis:** OYL 5:19, 5:20, 5:16

---

### 5. Shareholder Resolution (Osakkeenomistajan päätös)

**Files:**
- `shareholder-resolution-template.md`
- `shareholder-resolution-template.docx`

**When to use:**
- Patrick as sole shareholder making any shareholder-level decision
- Faster alternative to formal AGM/EGM
- Can replace AGM (but June 30 deadline still applies)

**Key features:**
- Complete AGM decision section (adopt FS, dividends, discharge, elections)
- Simplified format for sole shareholder
- PRH filing instructions
- Numbering guidance (counts as shareholder meeting minutes)

**Legal basis:** OYL 5:4 §

---

## Usage Instructions

### For All Templates:

1. **Open the .docx file** in Microsoft Word
2. **Fill in all placeholders** (marked with `{Variable_Name}` or `[TÄYTÄ:]`)
3. **Complete the validation checklist** before signing
4. **Sign and date** the document
5. **Save as PDF** with proper filename per document architecture
6. **Archive** in `documents/{company-slug}/corporate/`

### Placeholder Format:

- `{Company_Name}` — Replace with actual company name
- `{Y_tunnus}` — Replace with Business ID (e.g., 1234567-8)
- `{Date}` — Replace with actual date (YYYY-MM-DD or DD.MM.YYYY)
- `[TÄYTÄ: description]` — Fill in described content
- `[FILL: description]` — English equivalent

### Conditional Sections:

Templates include conditional sections marked with:
- `[IF sole board member:]` — Only include if sole board member
- `[IF multiple shareholders:]` — Only include if multiple shareholders
- `[IF AGM:]` — Only include for Annual General Meetings
- `[IF dividend:]` — Only include if dividend decision made

Delete sections that don't apply to your situation.

---

## Validation Framework

All templates include a **RED/YELLOW/GREEN validation checklist**:

| Level | Meaning | Action |
|-------|---------|--------|
| 🔴 **RED** | Legal requirement — MUST pass | Fix before signing/filing — non-compliance risk |
| 🟡 **YELLOW** | HHJ best practice — SHOULD pass | Address to meet governance standard |
| 🟢 **GREEN** | Excellence standard — NICE to have | Differentiates in due diligence/audits |

**Always complete all RED items.** YELLOW and GREEN items improve governance quality but are not legally mandatory.

---

## 1658 Holdings Specific Notes

All templates include "For 1658 Holdings" sections addressing:

### Patrick as Sole Board Member:
- Simplified signature requirements (no second signature needed)
- Minutes discipline MORE important (no peer review)
- Esteellisyys critical for holding structure
- Action items track YOUR commitments

### Patrick as Sole Shareholder:
- Notice requirements simplified (deemed given to yourself)
- Minutes reviewer not required (OYL 5:23 § 2 mom.)
- AGM can be brief but maintain structure for audit trail
- Sole shareholder decisions (OYL 5:4 §) fastest for any shareholder decision

### Holding Structure (10 Companies):
- Dividend cascade: subsidiaries AGM → Holdings AGM
- Batch processing strategy (e.g., all AGMs in May-June)
- Inter-company transaction documentation
- Transfer pricing arm's length requirements

---

## Critical Deadlines

| Deadline | Date (Dec 31 FY) | Consequence | Law |
|----------|------------------|-------------|-----|
| Financial statements signed | **30 April** | KPL breach; board liability | KPL 3:6 |
| AGM held | **30 June** | OYL breach; resolutions challengeable | OYL 5:3 |
| PRH FS filing | **2 months after AGM** | Registration default | OYL 8:10 |
| AGM notice | **1 week – 2 months before** | Meeting invalid | OYL 5:19 |
| FS available to shareholders | **1 week before AGM** | Notice violation | OYL 5:21 |

---

## Document Naming Convention

Follow 1658 Holdings document architecture:

```
{company-prefix}-{category}-{description}-{date}.{ext}
```

**Examples:**
- `dmc-corp-hallitus-ptk-3-2026-01-15.pdf` — Board minutes #3
- `jsy-corp-yhtiokokous-ptk-2026-06-20.pdf` — AGM minutes
- `1658-corp-hallitus-paatos-2026-03-10.pdf` — Board resolution
- `dmc-corp-yhtiokokouskutsu-2026-05-15.pdf` — AGM notice
- `jsy-corp-osakkeenomistaja-paatos-2026-06-20.pdf` — Shareholder resolution

---

## Style Guide Reference

For detailed style guidelines, see:
[`STYLE-GUIDE.md`](./STYLE-GUIDE.md)

Covers:
- Metadata header format
- Bilingual formatting rules
- Legal citation format (OYL 6:6, KPL 3:6)
- Placeholder conventions
- Table formats
- Signature block format
- Professional legal tone

---

## Related Documents

| Document | Location | Purpose |
|----------|----------|---------|
| Finnish Corporate Governance Best Practices | `_shared/best-practices/finnish-corporate-governance-and-document-drafting.md` | Comprehensive legal requirements and HHJ standards |
| Document Architecture | `_shared/best-practices/document-architecture.md` | File naming, folder structure, archiving rules |
| Style Guide | `_shared/templates/finnish-governance/STYLE-GUIDE.md` | Formatting and style standards |
| Batch Results (Source) | `_shared/batch-results/finnish-governance/` | Original Opus research (prompt-A, B, C) |

---

## Template Maintenance

### When to Update Templates:

1. **Finnish law changes** — monitor OYL, KPL, TilintL amendments
2. **HHJ standard updates** — Kauppakamari releases new guidance
3. **1658 Holdings practice evolution** — as governance matures
4. **User feedback** — if templates prove unclear or incomplete

### Version Control:

Each template includes a "Document History" section at bottom. When updating:
1. Increment version number (1.0 → 1.1 for minor, 1.0 → 2.0 for major)
2. Document what changed
3. Update date
4. Update both .md and .docx files

---

## Quick Start Guide

**New to Finnish corporate governance?**

1. **Read first:**
   - [`finnish-corporate-governance-and-document-drafting.md`](../../best-practices/finnish-corporate-governance-and-document-drafting.md) — understand requirements
   - [`STYLE-GUIDE.md`](./STYLE-GUIDE.md) — understand formatting

2. **Use templates in this order:**
   - **Board Minutes** — for regular board meetings (6-12/year for operating cos)
   - **AGM Notice** — send 1-2 weeks before AGM (by June)
   - **Shareholder Meeting Minutes** OR **Shareholder Resolution** — for AGM itself
   - **Board Resolution** — for urgent/simple decisions between meetings

3. **Common mistakes to avoid:**
   - Missing April 30 FS signing deadline
   - Missing June 30 AGM deadline
   - Not documenting esteellisyys (conflict of interest)
   - Not giving all board members opportunity to participate (OYL 6:3 § 2)
   - Not completing RED validation items

4. **For holding structures:**
   - Subsidiaries AGM BEFORE Holdings AGM (dividend cascade)
   - Document all inter-company transactions at arm's length
   - Maintain related-party register

---

## Support

**Questions about templates?**

1. Check [`finnish-corporate-governance-and-document-drafting.md`](../../best-practices/finnish-corporate-governance-and-document-drafting.md) for legal guidance
2. Check [`STYLE-GUIDE.md`](./STYLE-GUIDE.md) for formatting questions
3. Consult with Finnish corporate lawyer for legal advice
4. Consult with HHJ-certified board professional for best practice guidance

**Technical issues?**

- Templates not opening: Install Microsoft Word or LibreOffice
- Formatting broken: Use .docx version (markdown is source, Word is final)
- Placeholders not replaced: Search for `{` in Word to find all placeholders

---

## License and Disclaimer

**These templates are provided for 1658 Holdings Oy internal use.**

- Based on Finnish law as of 2026-02-11
- Synthesized from OYL 624/2006, KPL 1336/1997, TilintL 1141/2015, and HHJ best practices
- Not a substitute for legal advice from qualified Finnish corporate lawyer
- Always verify current legal requirements before use
- Author assumes no liability for incorrect use or outdated information

**When in doubt, consult a Finnish corporate lawyer.**

---

## Template Statistics

| Template | Word Count | Pages (est.) | Completion Time (est.) |
|----------|-----------|--------------|----------------------|
| Board Minutes | ~2,500 | 6-8 | 30-45 min |
| Shareholder Meeting Minutes | ~3,000 | 8-10 | 45-60 min |
| Board Resolution | ~1,800 | 5-6 | 20-30 min |
| AGM Notice | ~2,200 | 5-7 | 30-40 min |
| Shareholder Resolution | ~2,000 | 5-7 | 25-35 min |

**Total:** 5 templates, ~11,500 words, ~35 pages, ~3 hours to complete all (if doing simultaneously)

---

**Templates ready for use across all 10 companies in 1658 Holdings portfolio.**
