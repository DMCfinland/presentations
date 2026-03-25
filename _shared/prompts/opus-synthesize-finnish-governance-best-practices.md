# Prompt: Synthesize Finnish Corporate Governance Best Practices

## Context

You are helping Patrick Heiskanen, CEO of 1658 Holdings Oy (10-company portfolio), create a comprehensive best practices document for Finnish corporate governance. Three Opus batch results have been completed covering:

1. **Legal compliance framework** (prompt-A-law-compliance.md, 57KB)
2. **Cowork plugin architecture** (prompt-B-plugin-templates.md, 61KB)
3. **HHJ standards and vuosikello** (prompt-C-hhj-roadmap.md, 77KB)

These contain deep Finnish legal research (OYL, KPL, TilintL) and HHJ best practices. Your task is to synthesize this into a single best practices document that matches the existing 1658 Holdings style while preserving legal accuracy.

---

## Files to Read

**Source Material (Finnish governance batch results):**
- `_shared/batch-results/finnish-governance/prompt-A-law-compliance.md`
- `_shared/batch-results/finnish-governance/prompt-B-plugin-templates.md`
- `_shared/batch-results/finnish-governance/prompt-C-hhj-roadmap.md`

**Style References (existing best practices):**
- `_shared/best-practices/document-architecture.md`
- `_shared/best-practices/ai-deployment-principles.md`

**Output Location:**
- `_shared/best-practices/finnish-corporate-governance-and-document-drafting.md`

---

## Task Breakdown

### Step 1: Analyze Existing Style
Read the two style reference files and identify patterns:
- Header structure (metadata: Decision/Author/Date/Status)
- Tone (direct, practical, no fluff)
- Formatting (numbered principles, blockquotes for insights, concrete examples)
- Application notes pattern ("For 1658 Holdings:" sections)
- Length and density (concise but comprehensive)

### Step 2: Extract Core Value from Batch Results
From the 195KB of Finnish governance content, identify:
- **Legal requirements** that are non-negotiable (OYL, KPL citations)
- **HHJ best practices** that add value beyond compliance
- **10-company holding structure** specific guidance
- **Document templates** and validation frameworks
- **Vuosikello** (annual calendar) structure
- **Practical workflows** (batch processing AGMs, dividend cascade, etc.)
- **Governance quality scorecard** and assessment framework

**What to exclude:**
- Verbose explanations already clear from context
- Redundant legal citations (cite once, reference elsewhere)
- Implementation details better suited for templates than principles
- Academic-style commentary or excessive justification

### Step 3: Find the Middle Ground
The batch results are **comprehensive and legally precise** but verbose.
The existing best practices are **concise and action-oriented** but lack legal depth.

**Middle ground criteria:**
- Legal accuracy preserved (all OYL/KPL/TilintL references accurate)
- Practical guidance emphasized (what to do, when, why it matters)
- Holding structure focus (10 companies, Patrick as sole board member)
- Scannable structure (someone can find answers in 30 seconds)
- Bilingual where it matters (Finnish legal terms with English translation)
- "Just strict enough" (Patrick's guidance: not overly rigid, but compliant)

### Step 4: Structure the Output Document

Use this structure:

```markdown
# Finnish Corporate Governance & Document Drafting
**Decision:** Synthesized from Opus batch results + HHJ certification standards
**Author:** Patrick Heiskanen
**Date:** 2026-02-11
**Status:** Living document — update as laws change or practice evolves

---

## Purpose

[1-2 paragraphs: Why this document exists, who it's for, what problems it solves]

---

## I. LEGAL FRAMEWORK OVERVIEW

### Core Finnish Corporate Laws
[Brief summary with citations: OYL, KPL, TilintL, TSL, KRL]

### Legal Minimum vs. Best Practice
[Table or framework showing the spectrum]

### For 1658 Holdings:
[Application notes for 10-company structure]

---

## II. ANNUAL GOVERNANCE CALENDAR (VUOSIKELLO)

### Calendar Structure
[Month-by-month overview, condensed from Prompt C]

### Critical Deadlines
[Quick reference table: month, deadline, consequence of missing]

### Batch Processing Strategy
[How to handle 10 companies efficiently]

### For 1658 Holdings:
[Specific calendar recommendations]

---

## III. DOCUMENT TYPES & REQUIREMENTS

### 1. Board Meeting Minutes (Hallituksen Pöytäkirja)
**Legal requirements:** [OYL citations]
**HHJ best practices:** [Key additions]
**Validation checklist:** [RED/YELLOW/GREEN items]
**Template location:** [Path]

[Repeat for all 12 document types from Prompt A]

---

## IV. HOLDING STRUCTURE GOVERNANCE

### Inter-Company Transactions
[Arm's length, transfer pricing, documentation]

### Dividend Cascade Strategy
[Tax optimization, timing, documentation]

### Esteellisyys (Conflict of Interest) Management
[OYL 6:16 compliance, related-party register]

### For 1658 Holdings:
[Specific workflows for 10-company coordination]

---

## V. GOVERNANCE QUALITY ASSESSMENT

### Scorecard Framework
[5 categories from Prompt C, condensed]

### Score Interpretation
[3.5-4.0 = Exemplary, etc.]

### Annual Review Process
[When, how, who]

### For 1658 Holdings:
[Self-assessment as sole board member]

---

## VI. IMPLEMENTATION ROADMAP

### Phase 1: Foundation (Month 1)
[Key actions from Prompt C conclusion]

### Phase 2: Systematize (Months 2-3)
[Template rollout, standardization]

### Phase 3: Optimize (Months 4-6)
[Batch processing, automation]

### Phase 4: Maintain (Ongoing)
[Continuous improvement]

---

## VII. QUICK REFERENCE TABLES

### Legal Deadline Summary
[All statutory deadlines in one table]

### Document Archive Requirements
[KPL retention periods]

### Shareholder Meeting Checklist
[Pre/during/post-meeting actions]

### Board Meeting Checklist
[Agenda, materials, minutes, follow-up]

---

## APPENDIX: LEGAL CITATIONS

[All OYL, KPL, TilintL references with English summaries]

---

## Document History

- 2026-02-11: Initial synthesis from Opus batch results (Prompts A, B, C)
- [Future updates here]
```

---

## Execution Instructions

### Style Guidelines
- **Headers:** Use markdown ##, ###, #### hierarchy clearly
- **Tone:** Direct, practical, no fluff. Patrick is an experienced CEO, not a novice.
- **Legal citations:** Format as `OYL 5:3` with English summary in same sentence
- **Bilingual:** Finnish term first, English in parentheses: "Pöytäkirja (board minutes)"
- **Examples:** Use "1658 Holdings" or "Patrick" as subject of examples
- **Blockquotes:** Use for key insights or warnings
- **Lists:** Bulleted for related items, numbered for sequential steps
- **Tables:** Use for comparative data, checklists, or reference lookups

### Compression Targets
- **Total length:** 30-50KB (down from 195KB source, but richer than typical best practices)
- **Each section:** Aim for 2-5KB depending on complexity
- **Remove:** Meta-commentary, verbose justifications, redundant explanations
- **Preserve:** Every legal requirement, every RED validation item, every statutory deadline

### Quality Gates
Before finalizing, verify:
- [ ] All OYL/KPL/TilintL citations are accurate
- [ ] All 12 month vuosikello entries included (compressed but complete)
- [ ] All 12 document types from Prompt A covered
- [ ] RED/YELLOW/GREEN validation framework explained
- [ ] Holding structure guidance integrated throughout
- [ ] Quick reference tables functional (can find answer in 30 seconds)
- [ ] "For 1658 Holdings:" notes in every major section
- [ ] Document scans well (clear hierarchy, easy to navigate)
- [ ] Bilingual where it matters (legal terms, official documents)
- [ ] Tone matches existing best practices (direct, practical)

---

## Special Instructions

1. **Don't oversimplify:** Patrick needs legal precision for 10 companies, 50+ employees, potential audits/due diligence
2. **Don't over-explain:** Patrick is smart and experienced, trusts you to be concise
3. **Balance compliance and pragmatism:** "Just strict enough" — follow the law, but optimize workflow
4. **Think holding structure first:** Every principle should consider "how does this scale to 10 companies?"
5. **Make it scannable:** Someone should be able to find "what's the AGM deadline?" in 10 seconds

---

## Output Format

Write the complete document directly in markdown. No scripts, no "I will create...", just write it.

Start with:
```markdown
# Finnish Corporate Governance & Document Drafting
**Decision:** Synthesized from Opus batch results + HHJ certification standards
**Author:** Patrick Heiskanen
**Date:** 2026-02-11
**Status:** Living document — update as laws change or practice evolves
```

End with:
```markdown
---

**Document synthesized by Claude Opus from 195KB of Finnish legal research and HHJ best practices.**
**Source files:** prompt-A-law-compliance.md, prompt-B-plugin-templates.md, prompt-C-hhj-roadmap.md
**Total compression:** 195KB → [final size]KB while preserving legal accuracy and practical value.
```

---

## Begin

Read the 5 files listed above, analyze the style, extract the value, find the middle ground, and write the best practices document.
