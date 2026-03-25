# Prompt B: Cowork Plugin Architecture + Bilingual Document Templates

**Target:** Claude Opus (Batch API)
**Focus:** Plugin file structure, command definitions, skill definitions, configuration template, 8 document templates
**Batch ID:** prompt-B-plugin-templates
**Part:** 2 of 3 (merge with A + C after all complete)

---

# RESEARCH REQUEST: Finnish Corporate Governance Cowork Plugin — Architecture & Templates

## CRITICAL INSTRUCTION

**Write the actual plugin files, command definitions, skill documents, and document templates directly as usable markdown files. Do NOT write commentary about what they should contain. Do NOT describe templates — WRITE THEM.**

Every command definition must be a complete markdown file with YAML frontmatter and full workflow steps. Every skill must be a complete SKILL.md. Every template must be a fillable document with all required fields. If it says "template," write the template, not a description of the template.

Your output will be merged with two other focused prompts into a single best-practices document. This session must produce standalone, complete plugin architecture artifacts.

## Context

Patrick Heiskanen, CEO of **1658 Holdings Oy** — Finnish family holding company, 10 portfolio companies, ~50 employees. HHJ certified. Building a Finnish corporate governance document drafting system using Claude Code and Claude Cowork plugins.

**Company structure:**
- 1658 Holdings Oy (parent)
- Finland DMC Oy (IT/marketing, 5 staff)
- Järvisydän Oy (resort, employees + kiinteistöyhtiöt)
- Companies 3-10 (various industries)

**Document architecture (already built):**
- Centralized `documents/` folder with 7 categories: corp, con, fin, emp, ops, prop, ico
- Naming: `{prefix}-{cat}-{description}-{date}.{ext}`
- Three-tier indexing: routing index → compressed digests → full files

## The Anthropic Cowork Plugin Architecture (Reference)

This is the actual architecture from `github.com/anthropics/knowledge-work-plugins` — our plugin must follow this EXACTLY.

### File Structure
```
legal/
├── .claude-plugin/
│   └── plugin.json          # {"name": "legal", "version": "1.0.0", "description": "...", "author": "Anthropic"}
├── .mcp.json                # MCP server connections (Slack, Box, M365, etc.)
├── README.md                # Plugin overview + quick start
├── CONNECTORS.md            # Supported integrations
├── commands/                # One .md file per slash command
│   ├── review-contract.md   # /review-contract
│   ├── triage-nda.md        # /triage-nda
│   └── ...
└── skills/                  # One SKILL.md per skill directory
    ├── contract-review/SKILL.md
    ├── nda-triage/SKILL.md
    └── ...
```

### Command File Format (from Anthropic's /review-contract)
```markdown
---
description: Review a contract against your organization's negotiation playbook
argument-hint: "<contract file or text>"
---

# /review-contract -- Contract Review Against Playbook

## Workflow
### Step 1: Accept the Contract
Accept the contract document — file upload, URL, or pasted text.

### Step 2: Gather Context
Ask the user: Which side are we on? Deadline? Focus areas? Deal context?

### Step 3: Load the Playbook
Read the organization's contract positions from legal.local.md.

### Step 4: Clause-by-Clause Analysis
Review 12 clause categories with specific key review points for each.

### Step 5: Flag Deviations
Use GREEN/YELLOW/RED severity system for deviations from playbook.

### Step 6: Generate Redline Suggestions
Provide specific alternative language for YELLOW and RED flags.

### Step 7: Business Impact Summary
Summarize top 3-5 issues with negotiation strategy recommendations.

### Step 8: CLM Routing
If connected via MCP, route approved contracts to CLM system.
```

### Skill File Format (from Anthropic's contract-review/SKILL.md)
```markdown
---
name: contract-review
description: Review contracts against your organization's negotiation playbook
---

# Contract Review Skill

You are a contract review assistant for an in-house legal team...

## Playbook-Based Review Methodology
[Detailed methodology]

## Common Clause Analysis
[Specific review points per clause type — Limitation of Liability, Indemnification, IP, Data Protection, Term/Termination, Governing Law]

## Deviation Severity Classification
- GREEN: Within acceptable range — no action needed
- YELLOW: Outside preferred range but negotiable — flag for review
- RED: Outside acceptable range or missing critical protection — must address

## Negotiation Priority Framework
- Tier 1 (Must-Haves): [examples]
- Tier 2 (Should-Haves): [examples]
- Tier 3 (Nice-to-Haves): [examples]
```

### Configuration File (legal.local.md)
Organization-specific positions and preferences. NOT shipped with the plugin — created per organization.

## Deliverable 1: Complete Plugin Specification

Write the full file structure for our Finnish corporate governance plugin:

```
finnish-corporate-governance/
├── .claude-plugin/plugin.json
├── .mcp.json
├── README.md
├── CONNECTORS.md
├── commands/
│   ├── draft-poytakirja.md      # /draft-poytakirja (board minutes)
│   ├── draft-paatos.md          # /draft-paatos (board resolution)
│   ├── review-sopimus.md        # /review-sopimus (contract review)
│   ├── check-oyl.md             # /check-oyl (compliance check)
│   ├── brief-yhtiokokous.md     # /brief-yhtiokokous (AGM preparation)
│   └── vuosikello.md            # /vuosikello (annual calendar check)
└── skills/
    ├── board-governance/SKILL.md
    ├── shareholder-meetings/SKILL.md
    ├── contract-review-fi/SKILL.md
    ├── financial-compliance/SKILL.md
    ├── corporate-records/SKILL.md
    └── property-company/SKILL.md
```

### 1a: plugin.json
Write the complete manifest file.

### 1b: README.md
Write the full plugin README following Anthropic's format — overview, quick start, commands list, skills list, setup instructions.

### 1c: .mcp.json
Define connections for: M365 (OneDrive/SharePoint for document storage), PRH/YTJ (if API available), and any other relevant Finnish services.

## Deliverable 2: All 6 Command Definitions

Write the **complete markdown file** for each command. Follow Anthropic's exact format: YAML frontmatter + workflow steps + validation + output format.

### Command 1: /draft-poytakirja (Board Meeting Minutes)
Full command file. Workflow must include:
- Accept meeting details (date, attendees, agenda)
- Load company profile from finnish-governance.local.md
- Check quorum per OYL 6:3
- Draft bilingual minutes with all OYL 6:6 required elements
- Run validation checklist (RED/YELLOW/GREEN)
- Output formatted document

### Command 2: /draft-paatos (Board Resolution Without Meeting)
Full command file for decisions made without a formal meeting (OYL 6:3 allows this).

### Command 3: /review-sopimus (Contract Review — Finnish Context)
Full command file adapted from Anthropic's /review-contract but for Finnish law context (sopimusoikeus, Finnish governing law positions, Finnish dispute resolution).

### Command 4: /check-oyl (OYL Compliance Check)
Full command file. Input: any corporate document. Output: compliance check against relevant OYL sections with RED/YELLOW/GREEN flags.

### Command 5: /brief-yhtiokokous (AGM Preparation)
Full command file. Generates AGM preparation package: notice, agenda, proposals, proxy forms. Per OYL Ch. 5.

### Command 6: /vuosikello (Annual Calendar Check)
Full command file. Input: current date + company profile. Output: what's due this month, what's coming, what's overdue.

## Deliverable 3: All 6 Skill Definitions

Write the **complete SKILL.md** for each skill. Follow Anthropic's format: YAML frontmatter + methodology + classification + best practices.

1. **board-governance/SKILL.md** — Board meeting methodology per OYL Ch. 6, HHJ standards
2. **shareholder-meetings/SKILL.md** — AGM/EGM methodology per OYL Ch. 5
3. **contract-review-fi/SKILL.md** — Finnish contract law, sopimusoikeus, common clause types
4. **financial-compliance/SKILL.md** — Kirjanpitolaki, tilintarkastus, financial oversight
5. **corporate-records/SKILL.md** — PRH filings, trade register, corporate lifecycle
6. **property-company/SKILL.md** — Asunto-osakeyhtiölaki / kiinteistöyhtiö specifics

## Deliverable 4: Configuration Template (finnish-governance.local.md)

Write the complete configuration template that each company fills in. Must include:
- Company profile (name, Y-tunnus, type, board, MD, auditor, financial year)
- Board meeting positions (quorum, minutes language, distribution, signatures)
- Conflict of interest handling (esteellisyys per OYL 6:4)
- Contract review positions (governing law, liability, indemnification — adapted for Finnish sopimusoikeus)
- Compliance calendar positions (which months have which obligations)
- Company-specific overrides (e.g., some companies have different financial year ends)

Write it as a fillable template with `{placeholder}` fields AND example values for a fictional "Malli Oy."

## Deliverable 5: Eight Bilingual Document Templates

Write **complete, fillable templates** for all 8 document types. Each template must:
1. Be bilingual: Finnish primary, English secondary (side by side or inline translations)
2. Include all legally required elements with specific law references in comments
3. Mark HHJ/Kauppakamari best practice additions with `[BP:]` tags
4. Include `{placeholder}` fields for AI drafting inputs
5. Include HTML/markdown comments with drafting instructions for the AI

### Template 1: Hallituksen kokouksen pöytäkirja / Board Meeting Minutes
Per OYL 6:6. Include: company info, date/time/place, present/absent, quorum confirmation, agenda items with decisions, dissenting opinions, signatures.

### Template 2: Yhtiökokouksen pöytäkirja / Shareholder Meeting Minutes
Per OYL 5:23. Include: notice verification, share representation, agenda per OYL 5:3, voting records, protest notations.

### Template 3: Hallituksen päätös / Board Resolution (Without Meeting)
Per OYL 6:3. Include: resolution text, all board member confirmations, date, rationale.

### Template 4: Yhtiöjärjestys / Articles of Association
Per OYL 2:3. Include: minimum required provisions + common optional provisions for Oy.

### Template 5: Osakassopimus / Shareholders' Agreement
Key clauses for Finnish Oy context: transfer restrictions, tag-along/drag-along, board composition, dividend policy, non-compete, dispute resolution.

### Template 6: Konserninsisäinen palvelusopimus / Inter-Company Service Agreement
Transfer pricing considerations (OYL 1:7, OECD principles). Include: service description, pricing mechanism, arm's length documentation, term, termination.

### Template 7: Toimintakertomus / Board's Report (Annual Report)
Per Kirjanpitolaki 3:1a. Include all required disclosures. Note small company exemptions.

### Template 8: Hallituksen vuosikello / Board Annual Calendar
Month-by-month template with required actions, deadlines, responsible parties.

## Constraints

- Follow Anthropic's Cowork architecture EXACTLY — same file formats, YAML patterns, folder structure
- Finnish law compliance (Finlex.fi = authoritative)
- Bilingual: Finnish primary, English secondary
- Focus on Oy (private limited), not Oyj (public)
- Templates must be AI-fillable with `{placeholder}` syntax
- Include law references as markdown comments: `<!-- OYL 6:6 -->`
- Designed for Claude to draft, not humans to type from scratch

---

**Remember: Write every command file, every SKILL.md, every template, every configuration field in full. Not summaries. Not "similar to above." Not "additional clauses as needed." Complete, usable files that could be dropped into a Cowork plugin folder and work. This is the Finnish equivalent of what triggered a $285 billion market repricing. Make it that good.**
