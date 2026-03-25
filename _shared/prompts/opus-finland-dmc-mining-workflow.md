# Opus Mining Workflow Design: Finland DMC Oy

**Date:** 2026-02-12
**Reviewer:** Claude Opus 4.6
**Project:** Finland DMC 2.0 - Custom Instructions via M365 Mining
**Status:** Pre-Mining Planning Phase

---

## EXECUTIVE CONTEXT

You are designing the complete mining workflow for Finland DMC Oy, a Finnish DMC (Destination Management Company) with 5 staff members. The CEO (Patrick) needs to mine years of client communications to build custom instructions for 4 Claude Projects.

**The Challenge:** Design a practical, secure, efficient workflow to extract strategic patterns from M365 data (emails, files, Teams chats) and transform them into high-quality custom instructions.

**The Blocker:** The primary data source is `sales@finland-dmc.com` mailbox, which is NOT a shared mailbox. Need to determine the best access method.

**The Goal:** A reusable mining workflow that works for all 10 portfolio companies.

---

## PROJECT OVERVIEW

### What We're Building

**4 Claude Projects for Finland DMC:**
1. **DMC Router** - Triage incoming inquiries, route to appropriate staff
2. **Client Communications** - Draft outbound emails, responses, follow-ups
3. **Proposals & Itineraries** - Create custom Finland travel proposals
4. **Pricing & Analysis** - Calculate pricing, analyze client requests

**Each Project needs:**
- Custom instructions file (personality, context, constraints)
- DOs/DON'Ts guide
- Tone guide (voice, style, examples)
- Best lines collection (proven phrases that work)
- Example outputs (high-quality reference samples)

### Mining Source Data

**Primary sources:**
- `sales@finland-dmc.com` mailbox (NOT shared mailbox)
- SharePoint: Finland DMC document libraries
- OneDrive: Company files and templates
- Teams: Internal conversations and decisions
- Excel: Client database, pricing sheets, supplier lists

**Data volume (estimated):**
- 5,000+ emails (2-3 years of client communications)
- 500+ client proposals and itineraries
- 100+ supplier agreements and notes
- Internal documentation and best practices

**Privacy considerations:**
- Client data (GDPR compliance)
- Supplier confidential information
- Pricing sensitive data
- Staff personal communications

---

## TECHNICAL ENVIRONMENT

### Available Tools

**Claude for Desktop (Cowork):**
- M365 MCP connector active (confirmed 2026-02-12)
- Can access: OneDrive, SharePoint, potentially Outlook
- **UNKNOWN:** Can it access `sales@finland-dmc.com` mailbox specifically?
- Best for: Interactive mining sessions, M365 queries

**Claude Code (VS Code extension):**
- No M365 API access (local files only)
- Can read: OneDrive-synced files at `~/Library/CloudStorage/`
- Best for: File organization, git, building final files

**OneDrive Sync:**
- Active and working (confirmed 2026-02-12)
- Syncs to: `~/Library/CloudStorage/OneDrive-*`
- Two-way sync to SharePoint

**File System:**
- Zone A (Workshop): `~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/`
- Zone B (Company Knowledge): OneDrive folder (to be created)
- Documents: `~/1658HoldingsOy-AIFiles/documents/finland-dmc-oy/`

### M365 Environment

**Subscription:** Microsoft 365 Business (confirmed)
**Admin access:** Patrick has Global Admin rights
**Email system:** Exchange Online
**Question:** Does Patrick's admin account have mailbox delegation for `sales@finland-dmc.com`?

---

## YOUR MISSION

Design a complete, practical, secure mining workflow that Patrick can execute immediately. Think like a systems architect: consider access permissions, data privacy, file handling, mining efficiency, and scalability to 10 companies.

### Core Questions to Answer

**1. EMAIL ACCESS STRATEGY**
- Can Claude Desktop M365 connector access `sales@finland-dmc.com` mailbox?
- If NO, what are the options?
  - Grant mailbox delegation to Patrick's admin account?
  - Export emails to PST/MSG files?
  - Forward emails to a dedicated mining folder?
  - Use Outlook rules to copy emails to SharePoint?
- What's the recommended approach? (most efficient, secure, maintainable)
- What permissions/setup are required?

**2. DATA EXPORT & STAGING**
- If emails need to be exported, what format? (PST, MSG, EML, PDF, TXT?)
- Where should exported data be staged? (OneDrive folder, local temp, SharePoint library?)
- How to organize: By date? By client? By project? By topic?
- What's the cleanup strategy after mining?

**3. MINING WORKFLOW DESIGN**
- Step-by-step process from "raw M365 data" to "final custom instructions"
- Which tool for each step? (Desktop for mining, Code for organizing, etc.)
- How to capture patterns efficiently? (prompts, templates, checklists)
- How to validate mining quality? (spot checks, peer review, testing)
- How to handle sensitive data? (anonymization, deletion, access logs)

**4. SESSION STRUCTURE**
- How many mining sessions per Project? (5 sessions planned currently)
- Session duration? (2 hours suggested, realistic?)
- What to mine in each session? (breakdown by Project and source type)
- How to avoid fatigue and maintain quality?
- How to track progress across sessions?

**5. OUTPUT ORGANIZATION**
- Where do mining outputs go? (folder structure)
- File naming convention for outputs?
- How to distinguish: raw notes vs. processed insights vs. final files?
- How to track which sources have been mined?
- Version control for iterative mining?

**6. BUILDING CUSTOM INSTRUCTIONS**
- From mining notes to final custom instructions file - what's the process?
- Should each Project be built separately or batch-assembled?
- Quality gates before upload to Claude Projects?
- Testing strategy? (real queries, sample outputs, staff feedback)
- Iteration cycle? (how often to refine based on usage)

**7. PRIVACY & SECURITY**
- GDPR compliance for client data mining?
- How to handle sensitive pricing/supplier info?
- Should mining outputs be anonymized?
- Data retention: What to keep vs. delete after building custom instructions?
- Access control: Who can see mining outputs vs. final files?

**8. SCALABILITY TO 10 COMPANIES**
- What parts of this workflow are reusable?
- What needs to be customized per company?
- How to document the workflow for repeatability?
- Lessons learned capture process?
- Efficiency improvements for companies 2-10?

---

## DELIVERABLES REQUESTED

### 1. Email Access Decision (1-2 pages)

**Analysis:**
- Can Claude Desktop access `sales@finland-dmc.com` directly? (yes/no + evidence)
- If NO, compare 3-4 export/access methods:
  - Method name
  - Setup requirements (permissions, time, technical steps)
  - Pros/cons for mining use case
  - Ongoing maintenance burden
  - Privacy/security implications
  - Cost (time and money)

**Recommendation:**
- Chosen method with clear rationale
- Step-by-step setup instructions
- Expected setup time and prerequisites
- Testing criteria (how to validate it works)

### 2. Complete Mining Workflow (3-4 pages)

**Phase 1: Setup & Preparation**
- M365 access configuration (mailbox, SharePoint, Teams)
- Folder structure creation (Zone A, Zone B, staging areas)
- Permission verification checklist
- Test query to validate access

**Phase 2: Data Staging**
- Export process (if needed)
- File organization strategy
- Naming conventions
- Quality check (ensure completeness)

**Phase 3: Mining Sessions**
- Session structure template (pre-work, execution, post-work)
- Mining prompts by Project type
- Pattern capture method (notes, tags, examples)
- Session log format
- Progress tracking method

**Phase 4: Pattern Synthesis**
- Consolidate notes across sessions
- Identify recurring themes
- Extract best practices
- Build pattern library

**Phase 5: File Assembly**
- Custom instructions structure
- DOs/DON'Ts compilation
- Tone guide creation
- Best lines curation
- Example outputs selection

**Phase 6: Testing & Refinement**
- Upload to Claude Projects
- Test with real queries
- Staff feedback collection
- Iteration and refinement
- Final deployment

**Phase 7: Cleanup & Documentation**
- Archive or delete sensitive mining outputs
- Document lessons learned
- Update workflow for next company
- Knowledge transfer preparation

### 3. Session Breakdown (2-3 pages)

For each of the 5 planned mining sessions, specify:

**Session 1: Client Communications - Outbound**
- Data sources to mine (which emails, which date range)
- Key patterns to look for (tone, structure, common responses)
- Mining prompts to use
- Expected outputs (what files/notes to create)
- Time estimate
- Quality checks

**Session 2: Client Communications - Inbound**
- [Same structure as Session 1]

**Session 3: DMC Router**
- [Same structure]

**Session 4: Proposals & Itineraries**
- [Same structure]

**Session 5: Pricing & Analysis**
- [Same structure]

### 4. File Organization System (1 page)

```
FinlandDMCOy-AIFiles/
├── finland-dmc-2.0/                    # Project root
│   ├── mining-sessions/                # Raw mining outputs
│   │   ├── session-1-outbound/
│   │   │   ├── raw-notes.md
│   │   │   ├── patterns-identified.md
│   │   │   ├── examples-captured.md
│   │   │   └── session-log.md
│   │   ├── session-2-inbound/
│   │   └── [etc.]
│   ├── mining-outputs/                 # Processed insights
│   │   ├── client-comms-patterns.md
│   │   ├── router-decision-trees.md
│   │   ├── proposal-templates.md
│   │   └── pricing-guidelines.md
│   ├── project-files/                  # FINAL deliverables
│   │   ├── client-comms/
│   │   │   ├── custom-instructions.md
│   │   │   ├── dos-donts.md
│   │   │   ├── tone-guide.md
│   │   │   └── best-lines.md
│   │   ├── dmc-router/
│   │   ├── proposals/
│   │   └── pricing/
│   └── _meta/
│       ├── ROADMAP.md
│       ├── MINING_PROTOCOL.md
│       └── progress-tracker.md
```

Explain:
- Purpose of each folder
- What goes where
- When to move files between folders
- Cleanup rules

### 5. Privacy & Security Plan (1-2 pages)

**Data handling rules:**
- What data can be extracted vs. must stay in M365
- Anonymization requirements (client names, pricing, etc.)
- Storage rules (encrypted, access-controlled, temporary vs. permanent)
- Deletion timeline (when to delete raw mining outputs)
- Access logs (who accessed what, when)

**GDPR compliance checklist:**
- Legal basis for processing client data
- Data minimization (only extract what's needed)
- Purpose limitation (only use for custom instructions)
- Storage limitation (delete after project complete)
- Data subject rights (how to handle access/deletion requests)

**Security measures:**
- Who has access to mining outputs (Patrick only? Staff?)
- Encryption requirements
- Backup strategy
- Incident response (if sensitive data leaked)

### 6. Mining Prompt Library (2-3 pages)

Provide specific prompts Patrick can use in Claude Desktop during mining:

**For Client Communications:**
```
Prompt template for analyzing email tone, structure, common phrases
```

**For DMC Router:**
```
Prompt template for identifying inquiry types, routing logic, decision trees
```

**For Proposals:**
```
Prompt template for extracting proposal structures, winning patterns, client preferences
```

**For Pricing:**
```
Prompt template for identifying pricing strategies, margin patterns, discount rules
```

Include:
- When to use each prompt
- How to adapt for different data sources
- What outputs to expect
- Quality validation criteria

### 7. Testing & Validation Strategy (1 page)

**Quality gates before deploying custom instructions:**

1. **Completeness check:** Does custom instruction cover all key scenarios?
2. **Accuracy check:** Are patterns based on sufficient examples?
3. **Tone validation:** Does output match Finland DMC voice?
4. **Edge case testing:** How does it handle unusual requests?
5. **Staff feedback:** Do staff recognize the patterns as authentic?

**Testing protocol:**
- 10 test queries per Project (provide examples)
- Expected vs. actual output comparison
- Pass/fail criteria
- Iteration threshold (how many fails = need refinement)

### 8. Scalability Playbook (1-2 pages)

**Reusable across 10 companies:**
- Workflow steps that are identical for all companies
- Templates and checklists to copy
- Common pitfalls to avoid (learned from Finland DMC)

**Customizable per company:**
- What changes based on company type (DMC vs. hotel vs. restaurant)
- How to adapt mining prompts
- Company-specific privacy considerations

**Efficiency improvements:**
- Estimated time for Company 1 (Finland DMC): X hours
- Estimated time for Company 2-10 (with workflow): Y hours
- What infrastructure to build now vs. later
- When to automate parts of the workflow

### 9. Risk Assessment & Mitigation (1 page)

**Potential risks:**

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Can't access sales@ mailbox | Medium | High | [Your mitigation strategy] |
| Mining outputs too generic | Medium | High | [Strategy] |
| Privacy breach (client data leaked) | Low | Critical | [Strategy] |
| Staff rejects custom instructions | Medium | Medium | [Strategy] |
| Mining takes 3x longer than planned | Medium | Medium | [Strategy] |
| M365 connector loses access mid-project | Low | High | [Strategy] |

**Abort criteria:**
- When to stop and reassess approach
- Warning signs of workflow failure
- Minimum viable outcome if full plan fails

### 10. Executive Summary (1 page)

- **Workflow verdict:** Is this mining approach viable? (Grade: A/B/C/D/F)
- **Email access recommendation:** [Specific method chosen]
- **Time estimate:** Total hours to complete all 4 Projects
- **Cost estimate:** Time + any tools/subscriptions needed
- **Top 3 risks:** What could go wrong
- **Top 3 success factors:** What will make this work
- **Go/No-go recommendation:** Should Patrick proceed? Why or why not?

---

## REVIEW GUIDELINES

**Practical Focus**
- Patrick will execute this solo (no dedicated team)
- Solutions must be implementable by one person
- Prefer simple over sophisticated
- Automation where possible, manual where necessary
- Time-boxed: Each session should have a realistic end time

**Privacy-First**
- Client data protection is non-negotiable
- GDPR compliance is mandatory (Finland/EU market)
- When in doubt, over-redact or anonymize
- Deletion is preferred to indefinite storage

**Scalability Mindset**
- This workflow will be used 10 times (10 companies)
- Optimize for repeatability, not perfection
- Document lessons learned from Finland DMC
- Build infrastructure that compounds value

**Cost Discipline**
- Time is the primary cost (Patrick's hours)
- Minimize API costs where possible
- No expensive tools unless proven ROI
- Free/built-in solutions strongly preferred

**Quality Over Speed**
- Better to do 1 Project perfectly than 4 poorly
- Mining quality determines custom instruction quality
- Can iterate and improve across companies
- Success = staff actually use the Projects

---

## SUCCESS CRITERIA FOR YOUR DESIGN

Your workflow design succeeds if:

1. **Actionable:** Patrick can start mining tomorrow with clear instructions
2. **Complete:** Every step from M365 access to final files is covered
3. **Secure:** Privacy and GDPR compliance built-in, not bolted-on
4. **Realistic:** Time estimates match Patrick's capacity (not wishful thinking)
5. **Scalable:** Can be repeated for 9 more companies with less effort each time
6. **Quality-Focused:** Includes validation gates and testing protocols
7. **Risk-Aware:** Identifies failure modes and has backup plans
8. **Practical:** Solves the `sales@` mailbox blocker with a real solution

---

## ADDITIONAL CONTEXT

**Patrick's constraints:**
- Solo operator (CEO doing IT, document management, strategy)
- Limited time (maybe 10-15 hours total for Finland DMC mining)
- Non-technical staff (need simple, clear outputs for their use)
- Cost-conscious (prefers free/cheap solutions)
- Quality-focused (will not ship poor custom instructions)

**Finland DMC business context:**
- B2B travel company (serve tour operators, not direct tourists)
- High-touch service (custom itineraries, personal relationships)
- Email is primary communication channel
- Proposals are high-effort, high-value (need to be excellent)
- Competitive market (quality of communication = competitive advantage)

**Success looks like:**
- 4 Claude Projects staff actually use daily
- Response time reduced (faster email drafts, proposals)
- Quality maintained or improved (AI matches Finland DMC voice)
- Patrick freed up from email drafting
- Pattern captured for 9 more companies

---

## FORMATTING REQUIREMENTS

- Use markdown with clear heading hierarchy
- Include executive summary at top (decision-makers read this first)
- Use tables for comparisons, checklists, and workflows
- Use bullet points for lists (easier to scan)
- Bold key recommendations
- Include time estimates (hours) for all phases
- Cite specific tools/methods when referencing approaches
- Flag assumptions clearly (mark with "Assumption:")
- Highlight risks with ⚠️ emoji
- Highlight opportunities with 🎯 emoji
- Use blockquotes for critical warnings or key insights

**Target Length:** 12-18 pages total (comprehensive but scannable)

---

## FINAL NOTE

This mining workflow is the foundation for transforming 10 portfolio companies' operations with AI. Getting it right for Finland DMC means 9 more companies benefit from the learnings. Getting it wrong means wasted time and poor custom instructions that staff won't use.

Be honest. Be specific. Be practical. Design a workflow Patrick can execute with confidence tomorrow morning.

**Now begin your mining workflow design.**
