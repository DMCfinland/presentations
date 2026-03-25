# Prompt C: HHJ Best Practices + Kauppakamari Governance + Implementation Roadmap

**Target:** Claude Opus (Batch API)
**Focus:** What HHJ certification adds beyond OYL minimums, Kauppakamari governance code, vuosikello, implementation plan
**Batch ID:** prompt-C-hhj-roadmap
**Part:** 3 of 3 (merge with A + B after all complete)

---

# RESEARCH REQUEST: HHJ-Certified Governance Standards, Kauppakamari Best Practices & Implementation Roadmap

## CRITICAL INSTRUCTION

**Write the actual best practices tables, governance guidelines, vuosikello calendar, and implementation roadmap directly. Do NOT write meta-commentary. Do NOT describe what you would include. WRITE THE CONTENT.**

Every section must contain concrete, actionable content — specific HHJ recommendations, specific Kauppakamari guidelines, specific month-by-month calendar entries, specific implementation phases with tasks.

Your output will be merged with two other focused prompts:
- **Prompt A** covers Finnish law compliance matrix (OYL sections, legal requirements, validation checklists)
- **Prompt B** covers plugin architecture (command files, skill files, document templates)
- **This Prompt C** covers what certified governance excellence adds on top of legal minimums + how to build and deploy the system

## Context

Patrick Heiskanen, CEO of **1658 Holdings Oy** — Finnish family holding company, 10 portfolio companies, ~50 employees. Patrick holds **HHJ (Hyväksytty Hallituksen Jäsen)** certification from Suomen Kauppakamari.

Patrick is building a Cowork-style plugin (structured markdown) for Finnish corporate governance. The legal requirements come from Prompt A. The architecture comes from Prompt B. **This prompt defines the governance quality layer that sits on top of legal minimums.**

The HHJ certification is Patrick's professional credential. The document system must reflect certified board member governance quality — not just legal compliance, but demonstrated best practices. This is both a quality standard and a competitive advantage (most Finnish SME holding structures operate at bare legal minimum).

**Company structure:**
- 1658 Holdings Oy (parent, Patrick = CEO + sole board member in most companies)
- Finland DMC Oy (IT/marketing, 5 staff)
- Järvisydän Oy (resort, employees + kiinteistöyhtiöt property companies)
- Companies 3-10 (various industries, mix of active operations and holding/property)

**Key context:** Many of Patrick's companies are small (1-3 board members, sometimes Patrick as sole member). The HHJ best practices need to be adapted for this reality — not all best practices designed for 5-7 member boards apply, but the governance quality principles still do.

## Deliverable 1: HHJ Best Practices — What It Adds Per Document Type

The HHJ (Hyväksytty Hallituksen Jäsen) program, run by Suomen Kauppakamari, teaches governance practices that **exceed OYL legal minimums**. This is the key value layer.

For each document type, create a table showing what HHJ adds:

| Document Type | OYL Minimum (Legal Requirement) | HHJ Best Practice (Goes Beyond OYL) | Why It Matters |
|---|---|---|---|
| Board minutes | Must record decisions, attendees, signatures (6:6) | Record decision rationale, dissenting opinions, risk discussion, action items with deadlines and owners | Creates audit trail, demonstrates diligence, protects in disputes |
| ... | ... | ... | ... |

**Cover all 12 document types from Prompt A:**
1. Board meeting minutes
2. Shareholder meeting minutes
3. Board resolution without meeting
4. Articles of association
5. Shareholders' agreement
6. Inter-company service agreement
7. Annual report
8. Financial statements
9. Trade register filings
10. Dividend resolution
11. Employment contract
12. Power of attorney

For each: what does OYL require (minimum), what does HHJ recommend (better), and why the difference matters for governance quality.

## Deliverable 2: HHJ Curriculum Deep Dive

Research and document the **specific content of the HHJ certification program** that applies to document management and governance:

### Board Chair Responsibilities (Puheenjohtajan tehtävät)
- What HHJ teaches about the chair's role in meetings
- Chair's responsibility for minutes quality
- Chair's role in agenda setting and meeting preparation
- Chair's duty in conflict of interest situations

### Board Member Duties (Hallituksen jäsenen velvollisuudet)
- Duty of care (huolellisuusvelvollisuus) — OYL 1:8
- Duty of loyalty (lojaliteettivelvollisuus)
- Information duty — what the board must document and why
- How HHJ defines "competent board member" behavior beyond legal minimum

### Financial Oversight (Talouden valvonta)
- Board's role in financial monitoring per HHJ
- What financial information should be reviewed at each board meeting
- How to document financial oversight decisions
- Risk management and internal control (sisäinen valvonta)

### Board Evaluation (Hallituksen itsearviointi)
- HHJ recommendation for annual board self-evaluation
- What the evaluation covers
- How to document it
- Adaptation for 1-3 member boards (Patrick's reality)

### Conflicts of Interest (Esteellisyys)
- OYL 6:4 defines the minimum (recusal when personal interest)
- HHJ best practices for handling and documenting conflicts
- Proactive conflict register vs. reactive recusal
- Documentation requirements beyond OYL

## Deliverable 3: Suomen Kauppakamari Governance Code

Research and document the **Kauppakamarin hallinnointikoodi** (Governance Code) for unlisted companies. This is separate from the Securities Market Association's code for listed companies.

### What the Code Recommends
- Board composition guidelines for unlisted companies
- Meeting frequency and preparation standards
- Documentation and archiving standards
- Transparency recommendations (even for private companies)
- Shareholder communication standards

### Recommended Board Meeting Structure
Write the Kauppakamari-recommended standard agenda format:

```
1. Kokouksen avaaminen / Opening
2. Kokouksen laillisuus ja päätösvaltaisuus / Legality and quorum
3. Pöytäkirjan tarkastajan valinta / Selection of minutes reviewer
4. Edellisen kokouksen pöytäkirjan hyväksyminen / Approval of previous minutes
5. [standard agenda items in recommended order]
...
N. Seuraavan kokouksen ajankohta / Next meeting date
N+1. Kokouksen päättäminen / Closing
```

### Recommended Minutes Structure
Write the Kauppakamari-recommended format for board minutes — not just what OYL requires, but what professional governance looks like.

### Recommended Annual Reporting Cycle
How the Kauppakamari recommends structuring board's annual work cycle.

## Deliverable 4: Board Annual Calendar (Vuosikello)

Create a **complete 12-month board annual calendar** for a Finnish Oy in a holding structure. This is one of the most practically valuable outputs.

**Format:** Month-by-month, with:
- Required legal deadlines (with law references)
- HHJ/Kauppakamari recommended activities
- Document outputs (what gets produced)
- Responsible parties

**Assumptions:**
- Financial year: January 1 — December 31 (most common)
- AGM deadline: June 30 (within 6 months of financial year end per OYL 5:3)
- Board meets formally 4-6 times per year (minimum, more for active companies)
- Some companies are holding/property companies with minimal activity

```
## January
### Legal Deadlines
- [deadline] — [description] — [law reference]

### Recommended Board Actions
- [action] — [HHJ/Kauppakamari reference]

### Document Outputs
- [document] — [template reference from Prompt B]

### Notes
- [practical guidance for holding structure]

## February
...
```

Write ALL 12 months completely. Include:
- Financial statement preparation timeline
- Auditor coordination milestones
- AGM preparation and execution
- Trade register filings
- Tax-related deadlines (corporate tax, VAT annual if applicable)
- Board evaluation timing
- Budget/plan cycle
- Dividend decision timeline

## Deliverable 5: Governance Quality Scoring Framework

Create a scoring framework that measures governance quality per company. This helps Patrick track which companies are at legal minimum vs. HHJ standard vs. excellence.

| Category | Score 1 (Legal Minimum) | Score 2 (Good Practice) | Score 3 (HHJ Standard) | Score 4 (Excellence) |
|---|---|---|---|---|
| Board minutes quality | Contains required elements per OYL 6:6 | Plus decision rationale | Plus dissent records, risk notes, action items | Plus financial review notes, strategic context |
| Meeting preparation | No formal preparation | Agenda distributed | Materials distributed 3+ days early | Plus pre-read requirements, questions collected |
| ... | ... | ... | ... | ... |

**Cover at least 10 governance categories.**

## Deliverable 6: Implementation Roadmap

Design the build order for the complete Finnish corporate governance system. This is the practical "how do we actually build this" guide.

### Phase 1: Foundation (Week 1-2)
What to build first, why, and what it depends on.

### Phase 2: Core Documents (Week 3-4)
Which templates and commands to build first (highest impact, most frequently used).

### Phase 3: Full Coverage (Week 5-8)
Remaining templates, skills, and validation systems.

### Phase 4: Multi-Company Rollout (Week 9-12)
How to scale from pilot (1658 Holdings + Finland DMC + Järvisydän) to all 10 companies.

**For each phase, specify:**
- Tasks (specific, actionable)
- Dependencies (what must come first)
- Testing strategy (how to validate)
- Success criteria (how to know it works)
- Estimated effort (in hours, not days — this is a markdown project, not software)

### Build Order Priority Matrix

| Priority | Component | Impact | Effort | Dependencies |
|---|---|---|---|---|
| 1 | [component] | [why high impact] | [hours] | [none / list] |
| 2 | ... | ... | ... | ... |

### Testing Strategy
- How to validate Finnish law compliance (against Finlex.fi)
- How to test templates produce legally valid documents
- How to verify HHJ/Kauppakamari best practices are captured
- Who reviews (Patrick as HHJ holder is the quality validator)

### Scaling Strategy
- How per-company configuration works (one .local.md per company)
- What's shared vs. company-specific
- How property companies (kiinteistöyhtiöt) differ from operating companies
- How to handle companies with different financial year ends

## Deliverable 7: Adaptation Guide for Small / Solo Boards

Many of Patrick's companies have 1-3 board members (sometimes Patrick as sole member). HHJ and Kauppakamari best practices are often written for 5-7 member boards. Write a practical adaptation guide:

- Which HHJ practices apply to sole-member boards and which don't
- How to maintain governance quality with minimal board composition
- When a sole board member should still document decisions formally
- The holding structure advantage: Patrick sits on all boards, so institutional knowledge compounds
- Risk: single point of failure — how to mitigate through documentation

## Constraints

- HHJ content should reflect the actual certification program, not generic governance advice
- Kauppakamari guidelines should reference the specific code for unlisted companies
- Vuosikello must include specific dates/deadlines, not vague "Q1" references
- Adaptation for small boards is critical — don't assume 5+ member boards
- Implementation roadmap should be realistic for one person (Patrick) with AI assistance
- All governance recommendations must be proportional to company size

## Reference Sources

1. **Suomen Kauppakamari** — HHJ certification program materials
2. **Kauppakamarin hallinnointikoodi** — Governance code for unlisted companies
3. **Boardman** — Finnish board governance training and research
4. **Directors' Institute Finland (DIF)** — Board best practices
5. **OYL 624/2006** — For comparison: what's legal minimum vs. what's best practice
6. **Finlex.fi** — Finnish legal database
7. **PRH.fi** — Trade register deadlines and requirements
8. **Vero.fi** — Tax deadlines relevant to governance calendar

---

**Remember: Write the actual calendar entries, scoring matrices, implementation phases, and adaptation guides. Not descriptions. Not "this would typically include..." — write the content itself. Patrick will use this document daily for 5+ years across 10 companies. Every month of the vuosikello needs specific content. Every phase of the roadmap needs specific tasks. Make it the kind of practical governance guide that makes an HHJ-certified CEO say "this is exactly what I needed."**
