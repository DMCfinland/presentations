# Research Prompt: Document Handling & Drafting System with Finnish Corporate Governance

**Target:** Claude Opus (claude.ai)
**Purpose:** Design a Finnish corporate governance plugin following Anthropic's Cowork architecture
**Cost estimate:** ~$5-8 (large context, one-shot, complex synthesis)
**Instructions:** Copy everything below the line into claude.ai as a single message.

---

# RESEARCH REQUEST: Finnish Corporate Governance Document System — Cowork Plugin Architecture

## Who You Are Advising

Patrick Heiskanen, CEO of **1658 Holdings Oy** — a Finnish family holding company with **10 portfolio companies** and ~50 employees total. Patrick holds the **HHJ (Hyväksytty Hallituksen Jäsen)** certification from Suomen Kauppakamari (Finnish Chamber of Commerce).

Patrick is building an AI-powered document management and drafting system using:
- **Claude Code** (local file orchestration on Mac)
- **Claude Cowork** (Anthropic's desktop agent — launched Jan 2026, plugins released Jan 30)
- **Claude Projects** (team AI assistants via M365 connector)
- **Structured markdown workflows** following the exact architecture Anthropic uses for its open-source Cowork plugins

## The Goal: Why We're Doing This Research

Patrick runs a 10-company holding structure where **corporate document management is a massive, recurring time sink**. Every company needs:
- Board meetings → minutes → filing → archive (multiple times per year)
- Shareholder meetings → minutes → trade register filings
- Contracts between portfolio companies → review → sign → archive
- Financial statements → board reports → auditor coordination
- Employment contracts, licenses, permits, property deeds

**Currently this is done manually** — by Patrick, by lawyers (expensive), or by accountants (also expensive). For 10 companies, that's hundreds of documents per year, each needing to be legally correct, properly archived, and retrievable.

**The vision:**
1. **Build a Finnish corporate governance Cowork plugin** that can draft, review, and validate corporate documents following OYL, HHJ, and Kauppakamari standards
2. **Reduce dependency on external lawyers** for routine corporate documents (board minutes, resolutions, standard contracts) — saving thousands of euros per year across 10 companies
3. **Ensure higher governance quality** than manual processes — the AI checks every OYL requirement, every HHJ best practice, every time. No human forgets a compliance checkbox.
4. **Create a reusable system** — build once, deploy across all 10 companies with per-company configuration files
5. **Enable staff to draft documents** without deep legal expertise — the plugin guides them through the process with slash commands and validation checklists
6. **Demonstrate HHJ-certified governance** — Patrick's board member credential means the document system should reflect certified professional standards, not just legal minimums

**The business case is simple:** If external legal fees for routine corporate documents are €5,000-15,000/year across 10 companies, and this system costs ~$10 to build (one-time Opus research + Claude Code implementation), the ROI is measured in days, not months.

**The broader strategic context:** Patrick is building AI-first infrastructure across all portfolio companies. This document system is a foundational layer — it demonstrates what "rebuilding around AI" looks like in practice, not just bolting AI onto existing processes. This is exactly the distinction Nate B Jones draws in his SaaSpocalypse analysis.

## Why This Matters: The SaaSpocalypse Context

On January 30, 2026, Anthropic released 11 open-source Cowork plugins. The legal contract review plugin — roughly 200 lines of structured markdown prompts — triggered a **$285 billion single-session sell-off** across enterprise software stocks. Thomson Reuters dropped 18%, LegalZoom 20%, RELX 14%.

**Key insight from Nate B Jones's analysis:**
> "The markdown file didn't cause this. It revealed it. The per-seat SaaS licensing model — the financial bedrock that the entire enterprise software economy has been built on for twenty years — was already cracking."

**What survived:** Proprietary data edges and accountability ("the single wringable neck" — SLAs, vendor liability, someone to call at 2 AM). **What died:** The per-seat pricing model sitting on top of those edges.

**The KPMG precedent:** KPMG pressured Grant Thornton UK to cut audit fees by 14% ($416K → $357K) by arguing AI changes the economics. They didn't automate their audit — they used AI's *existence* as negotiation leverage. This playbook is now spreading to legal fees, consulting fees, and all professional services.

**What this means for us:** We are building the Finnish equivalent of what caused a $285B repricing. Not as a SaaS product — as an internal system for 10 portfolio companies. The architecture is proven. The question is: can we build a Finnish corporate governance version that meets Finlex compliance standards AND follows Anthropic's enterprise patterns?

## The Actual Cowork Plugin Architecture (From GitHub)

We have extracted the complete architecture from Anthropic's open-source repository at `github.com/anthropics/knowledge-work-plugins`. Here is exactly how it works:

### Plugin File Structure
```
legal/
├── .claude-plugin/
│   └── plugin.json                    # Manifest: name, version, description, author
├── .mcp.json                          # MCP server connections (Slack, Box, M365, etc.)
├── README.md                          # Plugin overview + quick start
├── CONNECTORS.md                      # Full list of supported integrations
├── commands/                          # SLASH COMMANDS (one .md file per command)
│   ├── review-contract.md             # /review-contract
│   ├── triage-nda.md                  # /triage-nda
│   ├── vendor-check.md               # /vendor-check
│   ├── brief.md                      # /brief (daily, topic, incident)
│   └── respond.md                    # /respond (templated responses)
└── skills/                           # SKILLS (one SKILL.md per skill directory)
    ├── contract-review/SKILL.md      # Playbook-based contract analysis methodology
    ├── nda-triage/SKILL.md           # NDA screening criteria + routing
    ├── compliance/SKILL.md           # GDPR, CCPA, DPA review
    ├── canned-responses/SKILL.md     # Template management + escalation
    ├── legal-risk-assessment/SKILL.md # Risk severity framework
    └── meeting-briefing/SKILL.md     # Meeting prep + action items
```

### How Commands Work (Example: /review-contract)

Each command is a markdown file with YAML frontmatter and a detailed workflow:

```markdown
---
description: Review a contract against your organization's negotiation playbook
argument-hint: "<contract file or text>"
---

# /review-contract -- Contract Review Against Playbook

## Workflow
### Step 1: Accept the Contract (file, URL, or pasted text)
### Step 2: Gather Context (which side, deadline, focus areas, deal context)
### Step 3: Load the Playbook (from legal.local.md configuration)
### Step 4: Clause-by-Clause Analysis (12 clause categories with key review points)
### Step 5: Flag Deviations (GREEN/YELLOW/RED severity system)
### Step 6: Generate Redline Suggestions (specific alternative language)
### Step 7: Business Impact Summary (top issues + negotiation strategy)
### Step 8: CLM Routing (if connected via MCP)
```

### How Skills Work (Example: contract-review/SKILL.md)

Each skill is a comprehensive methodology document:

```markdown
---
name: contract-review
description: Review contracts against your organization's negotiation playbook
---

# Contract Review Skill

You are a contract review assistant for an in-house legal team...

## Playbook-Based Review Methodology
## Common Clause Analysis (with specific review points per clause type)
## Deviation Severity Classification (GREEN/YELLOW/RED with examples)
## Redline Generation Best Practices
## Negotiation Priority Framework (Tier 1 Must-Haves → Tier 3 Nice-to-Haves)
```

### How Configuration Works (legal.local.md)

The playbook is a local markdown configuration file defining the organization's standard positions:

```markdown
# Legal Playbook Configuration

## Contract Review Positions

### Limitation of Liability
- Standard position: Mutual cap at 12 months of fees paid/payable
- Acceptable range: 6-24 months of fees
- Escalation trigger: Uncapped liability, consequential damages inclusion

### Indemnification
- Standard position: Mutual indemnification for IP infringement and data breach
- Acceptable: Indemnification limited to third-party claims only
- Escalation trigger: Unilateral indemnification obligations

[... more clause positions ...]
```

### All 11 Plugin Domains
```
knowledge-work-plugins/
├── legal/              # Contract review, NDA triage, compliance
├── finance/            # Financial analysis, data processing
├── sales/              # CRM integration, sales process
├── marketing/          # Campaign management, content
├── customer-support/   # Support workflows
├── enterprise-search/  # Internal knowledge retrieval
├── data/               # Data analysis operations
├── product-management/ # Product workflows
├── productivity/       # General workflow enhancement
├── bio-research/       # Biology research
└── cowork-plugin-management/  # Meta: managing plugins
```

## What We Already Have (Our Architecture)

### Centralized Document System (Built)
```
~/1658HoldingsOy-AIFiles/
├── documents/                           # CENTRALIZED SOURCE OF TRUTH
│   ├── _index.md                        # Master registry (company prefixes + document log)
│   ├── _naming-rules.md                 # {prefix}-{cat}-{description}-{date}.{ext}
│   ├── _inbox/                          # Capture zone (second brain compatible)
│   ├── _holdings/                       # Holdings-level: corporate, financial, inter-company
│   ├── finland-dmc-oy/                  # corporate, contracts, financial, employment
│   ├── jarvisydan-oy/                   # corporate, contracts, financial, operations, property-companies
│   └── [companies 3-10]/
```

### 7-Category Taxonomy: corp, con, fin, emp, ops, prop, ico

### Three-Tier Indexing (Designed)
routing index (YAML, ~30KB) → compressed digests (~300KB) → full files (on demand)
Cost reduction: ~96% per query ($25 → ~$1)

### Company Structure
```
1658 Holdings Oy (parent, Patrick = CEO + board)
├── Finland DMC Oy (5 staff, manages IT/marketing for portfolio)
├── Järvisydän Oy (resort operator, has employees)
│   └── [Multiple kiinteistöyhtiöt] (property companies, no employees)
└── [Companies 3-10, various industries]
```

## WHAT WE NEED YOU TO RESEARCH AND DESIGN

### Stream 1: Finnish Corporate Governance Plugin (Cowork Architecture)

Design a complete Cowork plugin following the exact architecture above. Our plugin should be:

```
finnish-corporate-governance/
├── .claude-plugin/plugin.json
├── .mcp.json
├── README.md
├── CONNECTORS.md
├── commands/                          # Finnish corporate slash commands
│   ├── draft-poytakirja.md           # /draft-poytakirja (board minutes)
│   ├── draft-paatos.md               # /draft-paatos (board resolution)
│   ├── review-sopimus.md             # /review-sopimus (contract review)
│   ├── check-oyl.md                  # /check-oyl (OYL compliance check)
│   ├── brief-yhtiokokous.md          # /brief-yhtiokokous (AGM preparation)
│   ├── vuosikello.md                 # /vuosikello (annual calendar check)
│   └── [more commands as needed]
└── skills/
    ├── board-governance/SKILL.md      # Board meeting methodology per OYL Ch. 6
    ├── shareholder-meetings/SKILL.md  # AGM/EGM methodology per OYL Ch. 5
    ├── contract-review-fi/SKILL.md    # Finnish contract law + sopimusoikeus
    ├── financial-compliance/SKILL.md  # Kirjanpitolaki + tilintarkastus
    ├── corporate-records/SKILL.md     # PRH filings, trade register
    └── property-company/SKILL.md     # Asunto-osakeyhtiölaki / kiinteistöyhtiö specific
```

**For each command:** Define the YAML frontmatter, workflow steps, validation criteria, and output format — following Anthropic's exact patterns.

**For each skill:** Define the methodology, Finnish law requirements, severity classification, and best practices — the way Anthropic's contract-review/SKILL.md does it.

### Stream 2: Finnish Corporate Law & Governance Requirements (Finlex)

Research and document the legal requirements for each document type. **Cite specific law sections.**

#### Key Laws (Finlex.fi)
- **Osakeyhtiölaki (OYL 624/2006)** — Finnish Companies Act
  - Ch. 5: Yhtiökokous (Shareholder meetings) — required resolutions, voting, minutes (5:23)
  - Ch. 6: Yhtiön johto (Board and management) — board duties, meetings, minutes (6:6), quorum (6:3)
  - Ch. 8: Osakkeet (Shares) — share register, transfers
  - Ch. 13: Varojen jakaminen (Distribution of assets) — dividends, requirements
  - Ch. 20-21: Yhtiömuodon muuttaminen, sulautuminen (Restructuring, mergers)
- **Kirjanpitolaki (1336/1997)** — Accounting Act — financial statements, record-keeping
- **Tilintarkastuslaki (1141/2015)** — Auditing Act — audit requirements, thresholds
- **Kaupparekisterilaki (129/1979)** — Trade Register Act — registration, filing duties
- **Laki vaihtoehtorahastojen hoitajista** — if applicable to holding structures
- **Työsopimuslaki (55/2001)** — Employment Contracts Act — for employment document templates

#### HHJ (Hyväksytty Hallituksen Jäsen) Best Practices
The HHJ program teaches certified board members governance that exceeds legal minimums:
- Board's role vs. management's role (clear separation)
- Good corporate governance principles for **unlisted companies** (listaamaton yhtiö)
- Financial oversight: understanding kirjanpito, tilinpäätös, tilintarkastus
- Risk management and internal control
- Board evaluation and development
- Conflict of interest (esteellisyys) handling per OYL 6:4
- Board chair (puheenjohtaja) responsibilities
- Documentation requirements — what HHJ standards say about pöytäkirja quality

**Research question:** What does the HHJ curriculum specifically recommend for document quality, meeting protocols, and governance documentation beyond OYL minimums?

#### Suomen Kauppakamari Governance Guidelines
- **Corporate Governance Code for unlisted companies** (Kauppakamarin suositus hyvästä hallinnoinnista)
- Standard board meeting agenda (asialuettelo) format
- Minutes (pöytäkirja) recommended structure
- Board annual calendar (vuosikello) template
- Board self-evaluation practices

### Stream 3: Configuration File — Finnish Governance Playbook

Design a `finnish-governance.local.md` configuration file (following Anthropic's `legal.local.md` pattern) that encodes:

```markdown
# Finnish Corporate Governance Playbook

## Company Profile
- Company name: [legal name]
- Y-tunnus: [business ID]
- Company type: [Oy/Oyj/Osk]
- Board members: [names, roles]
- Managing director (toimitusjohtaja): [name]
- Auditor (tilintarkastaja): [name/firm]
- Financial year: [dates]

## Board Meeting Positions
### Quorum Requirements
- Standard: Per OYL 6:3 (majority of members present)
- Our practice: [may exceed OYL minimum per HHJ guidance]

### Minutes Requirements
- Language: [Finnish / bilingual FI+EN]
- Distribution: [who receives copies, when]
- Storage: [digital archive + physical if required]
- Signature: [digital or handwritten — per company policy]

### Conflict of Interest (Esteellisyys)
- Per OYL 6:4: [board member must recuse when personal interest]
- Our practice: [document recusal in minutes, separate record]

## Contract Review Positions (Finnish law context)
### Governing Law
- Standard position: Finnish law, Helsinki District Court
- Acceptable: Finnish law, agreed arbitration (Finland Chamber of Commerce)
- Escalation: Foreign law, unfavorable jurisdiction

### Limitation of Liability
- Standard position per Finnish sopimusoikeus: [...]
- [More positions adapted from Anthropic's pattern for Finnish context]

## Compliance Calendar
- January: [required actions]
- February: [required actions]
- [... full vuosikello]
```

### Stream 4: Document Templates (OYL-Compliant, Bilingual)

Design templates for 8 priority document types. Each template must include:
1. Required elements per Finnish law (with Finlex section references)
2. HHJ/Kauppakamari best practice additions (marked as "BP:" to distinguish from legal requirements)
3. AI-drafting instructions (what inputs the system needs)
4. Validation checklist (compliance checks before finalizing)

**Templates needed:**

| # | Document | Finnish | Key Law |
|---|----------|---------|---------|
| 1 | Board meeting minutes | Hallituksen kokouksen pöytäkirja | OYL 6:6 |
| 2 | Shareholder meeting minutes | Yhtiökokouksen pöytäkirja | OYL 5:23 |
| 3 | Board resolution (without meeting) | Hallituksen päätös | OYL 6:3 |
| 4 | Articles of association | Yhtiöjärjestys | OYL 2:3 |
| 5 | Shareholders' agreement | Osakassopimus | Sopimusoikeus |
| 6 | Inter-company service agreement | Konserninsisäinen palvelusopimus | OYL 1:7, siirtohinnoittelu |
| 7 | Annual report / Board's report | Toimintakertomus | Kirjanpitolaki 3:1a |
| 8 | Board annual calendar | Hallituksen vuosikello | HHJ best practice |

**Template format (bilingual example for board minutes):**

```markdown
# Hallituksen kokouksen pöytäkirja / Board Meeting Minutes
<!-- Template: board-minutes | Version: 1.0 | OYL: 6:6 -->

## Pöytäkirja nro {number} / Minutes No. {number}

**Yhtiö / Company:** {company_name} ({y_tunnus})
**Aika / Date and time:** {date} klo {time}
**Paikka / Place:** {location}

### Läsnä / Present:
{board_members_present}

### Kokouksen avaaminen / Opening of the Meeting
[OYL 6:3: Quorum confirmed — {count} of {total} members present]
[BP: Note chair opens meeting and confirms quorum before any business]

### Pöytäkirjan tarkastaja / Reviewer of the Minutes
{reviewer_name}

### Asiat / Agenda Items

#### § {number}: {agenda_item_title_fi} / {agenda_item_title_en}
**Esittely / Presentation:** {summary}
**Päätös / Decision:** {decision}
[OYL: If related-party matter, record recusal per 6:4]
[BP: Record vote if not unanimous — note dissenting opinions per HHJ guidance]

### Kokouksen päättäminen / Closing of the Meeting
Puheenjohtaja päätti kokouksen klo {time}.
The chair closed the meeting at {time}.

### Allekirjoitukset / Signatures
[OYL 6:6: Minutes signed by chair + at least one member or reviewer]

________________________          ________________________
{chair_name}                      {reviewer_name}
Puheenjohtaja / Chair             Pöytäkirjan tarkastaja / Reviewer
```

### Stream 5: Validation & Compliance Checklists

For each template, create a validation checklist that the AI runs before finalizing. Following Anthropic's GREEN/YELLOW/RED pattern:

```markdown
## Board Minutes Compliance Checklist

### OYL Requirements (RED if missing — legally invalid)
- [ ] Company name and Y-tunnus recorded
- [ ] Date, time, and place recorded
- [ ] Quorum confirmed (OYL 6:3 — majority present)
- [ ] All board members listed (present and absent)
- [ ] Each decision clearly recorded
- [ ] Signed by chair + reviewer (OYL 6:6)
- [ ] Conflict of interest recusals documented (OYL 6:4)

### HHJ Best Practices (YELLOW if missing — governance quality concern)
- [ ] Agenda distributed in advance
- [ ] Previous minutes approved
- [ ] Dissenting opinions recorded
- [ ] Action items assigned with deadlines
- [ ] Financial review included (if applicable)
- [ ] Next meeting date confirmed

### Excellence Standards (GREEN — recommended but not required)
- [ ] Bilingual (FI/EN) format used
- [ ] Decision rationale briefly documented
- [ ] Supporting documents referenced by name
- [ ] Distribution list noted
```

### Stream 6: Implementation Roadmap

Design the build order:

1. What to build first (highest impact, lowest cost)
2. What depends on what (prerequisites)
3. What to build when documents are imported
4. How to test and validate
5. How to scale from 3 companies to 10

## Constraints

- **Language:** Documents bilingual (Finnish primary, English secondary)
- **Legal jurisdiction:** Finnish law only (Finlex.fi = authoritative source)
- **No cloud database:** Local Mac filesystem + OneDrive sync
- **Tools:** Claude Code + Claude Cowork + Claude Projects
- **Budget:** One-time template investment; per-query costs under $2
- **Scale:** 10 companies × 200+ documents = 2,000+ documents
- **Format:** Markdown → PDF/DOCX export via pandoc
- **Holding structure:** Parent company + operating companies + property companies (kiinteistöyhtiöt)

## What I Need From You — Deliverables

Write a comprehensive markdown document I can save as `_shared/best-practices/finnish-corporate-governance-and-document-drafting.md`. Include:

1. **Cowork Plugin Specification** — Complete file structure for `finnish-corporate-governance/` plugin with all commands and skills defined
2. **Finnish Law Compliance Matrix** — Every document type mapped to specific Finlex sections, with required vs. recommended elements
3. **HHJ Best Practices Layer** — What the HHJ certification adds beyond OYL minimums for each document type
4. **Governance Playbook Template** — Complete `finnish-governance.local.md` configuration file
5. **8 Document Templates** — Bilingual, OYL-compliant, AI-ready, with validation checklists
6. **Board Annual Calendar (Vuosikello)** — Month-by-month required actions with deadlines and responsible parties
7. **Slash Command Library** — All `/command` definitions with YAML frontmatter and workflows
8. **Implementation Roadmap** — Build order, dependencies, testing strategy

## Quality Requirements

- **Legally precise** — cite specific OYL chapter:section numbers, law numbers from Finlex
- **Practically useful** — templates must be fillable, not just descriptive
- **Governance-aware** — exceed OYL minimums where HHJ/Kauppakamari recommend
- **AI-native** — designed for Claude to draft, not for humans to type from scratch
- **Architecture-aligned** — follow Anthropic's Cowork plugin patterns exactly
- **Decisive** — pick the best approach, commit to it

## Reference Sources

1. **Finlex.fi** — Official Finnish legal database
2. **OYL (624/2006)** — Osakeyhtiölaki / Finnish Companies Act
3. **Kirjanpitolaki (1336/1997)** — Accounting Act
4. **Tilintarkastuslaki (1141/2015)** — Auditing Act
5. **Kaupparekisterilaki (129/1979)** — Trade Register Act
6. **Työsopimuslaki (55/2001)** — Employment Contracts Act
7. **Suomen Kauppakamari** — Corporate governance guidelines for unlisted companies
8. **HHJ curriculum** — Hyväksytty Hallituksen Jäsen certification standards
9. **PRH.fi** — Finnish Patent and Registration Office
10. **github.com/anthropics/knowledge-work-plugins** — Cowork plugin architecture (open-source)

---

**Note to Opus:** This is a strategic infrastructure investment for a 10-company holding structure. The system will be used for 5+ years across all portfolio companies. Finnish law compliance is non-negotiable. The HHJ certification is Patrick's credential — the system must demonstrate certified board member governance quality. Follow Anthropic's enterprise plugin architecture exactly — we are building the Finnish corporate governance equivalent of the legal plugin that triggered a $285 billion market repricing. Make it worthy of that standard.
