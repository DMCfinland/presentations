# Finland DMC — Company 2.0 Build Roadmap

---

## CURRENT STATUS

| Field            | Value                                      |
|------------------|--------------------------------------------|
| **Current Phase** | Phase 0: Platform Setup                   |
| **Next 3 Tasks** | 1. Sign up for Claude Teams               |
|                  | 2. Enable M365 connector                   |
|                  | 3. Connect M365 account                    |
| **Blockers**     | M365 admin on holiday this week — Phase 0 M365 tasks blocked until next week |
| **Last Session** | 2026-02-09 — Deep research on Claude Code orchestration, two-zone architecture, CLAUDE.md hierarchy, custom subagents |

---

## PHASE 0: Platform Setup (~2 hours)

- [ ] Sign up for Claude Teams — claude.ai/teams, 5 seats, invite staff
- [ ] Enable M365 connector — Admin Settings → Connectors → Microsoft 365 → Add
- [ ] Connect M365 account — Global Admin credentials, org-wide consent
- [ ] Validate shared mailbox — Search info@finlanddmc.fi for recent emails
  - [ ] If works → shared mailbox is primary source
  - [ ] If fails → document the error, pivot to Teams channels
- [ ] Validate Teams search — Post test message → wait 5 min → ask Claude to find it
- [ ] Validate Excel search — Upload test .xlsx to SharePoint → ask Claude to find it
- [ ] Create 4 Teams channels (if they don't exist):
  - [ ] `#ai-feedback` — post purpose description
  - [ ] `#client-intel` — post purpose description
  - [ ] `#supplier-notes` — post purpose description
  - [ ] `#best-practices` — post purpose description
  - [ ] Add all 5 staff members to all channels
- [ ] Create empty Claude Projects (shells only):
  - [ ] DMC Router
  - [ ] Client Communications
  - [ ] Proposals & Itineraries
  - [ ] Pricing & Analysis
- [ ] Document M365 search findings:
  - [ ] Which search queries return good results?
  - [ ] Does shared mailbox search work?
  - [ ] Do Teams channel searches work?
  - [ ] Do SharePoint Excel file searches work?
  - [ ] What's the typical result format and volume?

> **After Phase 0:** Platform running, M365 validated, empty projects ready. Now you mine.

---

## PHASE 1: Mining Sessions (~6-8 hours total)

### Mining Session 1: Client Communications — OUTBOUND

**What:** Best emails Finland DMC has SENT to clients.

**Mine:**
- [ ] Search shared mailbox for best SENT emails by type:
  - [ ] New inquiry responses
  - [ ] Follow-up emails
  - [ ] Complaint responses
  - [ ] Cold outreach
  - [ ] Returning client emails
  - [ ] Booking confirmations
  - [ ] Price quote emails
  - [ ] Logistics / quick answers
- [ ] For each type: pick single best email → save as `Example_Email_[Type].txt`
- [ ] Extract best lines and phrases → populate `Best_Lines.txt`
- [ ] Analyze patterns → refine `DOs_and_DONTs.txt` with real rules
- [ ] Analyze greeting/closing/tone conventions → build real `Tone_Guide.txt`
- [ ] Test M365 search protocol:
  - [ ] Document which search queries work for client lookup
  - [ ] Document which data sources are most valuable
  - [ ] Note actual result quality

**Build:**
- [ ] Write FINAL `Client_Communications_Custom_Instructions.txt`
- [ ] Write FINAL `DOs_and_DONTs.txt` from real pattern analysis
- [ ] Write FINAL `Tone_Guide.txt` from actual email voice
- [ ] Write FINAL `Best_Lines.txt` from extracted real language
- [ ] Curate 8 `Example_Email_*.txt` files from archive
- [ ] Validation test: paste real inquiry → does Claude draft something you'd send?

---

### Mining Session 2: Client Communications — INBOUND

**What:** Types of emails arriving in shared mailbox. Teaches classification.

**Mine:**
- [ ] Search shared mailbox for RECEIVED emails (past 2 years)
- [ ] Categorize by inquiry type:
  - [ ] Group leisure inquiries
  - [ ] Corporate/incentive group inquiries
  - [ ] Tour operator / B2B partner inquiries
  - [ ] Conference/MICE inquiries
  - [ ] Individual/small group inquiries
  - [ ] Repeat booking requests
  - [ ] Complaints and issue reports
  - [ ] Logistics questions (confirmed bookings)
  - [ ] Supplier communications
  - [ ] Cold inbound (web/referral)
- [ ] Analyze by source market:
  - [ ] Which countries/regions?
  - [ ] Which languages?
  - [ ] B2B vs B2C ratio?
  - [ ] Which referral channels?
- [ ] Analyze what clients ask for:
  - [ ] Most requested activities/experiences
  - [ ] Most requested seasons
  - [ ] Typical group sizes
  - [ ] Typical budget ranges
  - [ ] Common special requests
  - [ ] Common concerns/questions
- [ ] Analyze email patterns:
  - [ ] What do you always need to ask for?
  - [ ] What do clients over-explain?
- [ ] Find "golden inquiries" — best, most complete emails that led to bookings (save 3-5)

**Build:**
- [ ] Create `Inbound_Email_Patterns.txt` — classification guide for Router
- [ ] Update Router custom instructions with real classification categories
- [ ] Update Client Comms instructions with "what to ask for" per inquiry type

---

### Mining Session 3: DMC Router

**What:** Task classification and routing logic from real data.

**Mine:**
- [ ] Review 20-30 recent real tasks (search shared mailbox)
- [ ] Classify each: what type? Which project routes to?
- [ ] Identify actual distribution: what % emails vs proposals vs pricing?
- [ ] Use Session 2 findings to refine task categories
- [ ] Check: are there task types the current categories miss?
- [ ] Identify what context Router needs to extract per email type
- [ ] Test: paste 5 real emails → does Router classify correctly?

**Build:**
- [ ] Write FINAL `DMC_Router_Custom_Instructions.txt`
- [ ] Validation test: 5 different real tasks → correct classification + prompts?

---

### Mining Session 4: Proposals & Itineraries

**What:** Proposal structure, content patterns, what converts.

**Mine:**
- [ ] Search for best 5-10 past proposals
- [ ] Analyze proposal structure:
  - [ ] Sections, ordering, length, formatting
  - [ ] How pricing is presented
  - [ ] How activities/accommodation/logistics are described
- [ ] Search for client replies: what convinced clients to book?
- [ ] Search #supplier-notes for current supplier relationships/rates
- [ ] Identify seasonal activity inventory
- [ ] Check: existing proposal templates/formats?

**Build:**
- [ ] Write FINAL `Proposals_Itineraries_Custom_Instructions.txt`
- [ ] Write `Proposal_Structure_Template.txt`
- [ ] Curate 2-3 `Example_Proposal_*.txt` from real proposals
- [ ] Write `Supplier_Rates_Reference.txt`
- [ ] Validation test: real client brief → sendable proposal?

---

### Mining Session 5: Pricing & Analysis

**What:** Pricing logic, rate cards, margins from real data.

**Mine:**
- [ ] Search SharePoint for actual rate cards, pricing Excel files
- [ ] Search shared mailbox for recent pricing emails/quotes
- [ ] Analyze actual pricing structure: components, markups, margins
- [ ] Search for pricing-related client pushback
- [ ] Identify seasonal pricing variations
- [ ] Check: what Excel files should live in SharePoint for Claude?

**Build:**
- [ ] Write FINAL `Pricing_Analysis_Custom_Instructions.txt`
- [ ] Write FINAL `Pricing_Guidelines.txt` from real pricing logic
- [ ] Update `Supplier_Rates_Reference.txt` with current rates
- [ ] Organize SharePoint Pricing folder
- [ ] Validation test: real group scenario → math works? Margins correct?

---

## PHASE 2: Assembly & Testing (~2 hours)

- [ ] Upload all FINAL files to each Claude Project:
  - [ ] DMC Router: Custom instructions + Inbound_Email_Patterns.txt
  - [ ] Client Communications: Custom instructions + DOs/DON'Ts + Tone Guide + Best Lines + 8 example emails
  - [ ] Proposals & Itineraries: Custom instructions + DOs/DON'Ts + Tone Guide + Best Lines + Template + 2-3 examples + Supplier Rates
  - [ ] Pricing & Analysis: Custom instructions + DOs/DON'Ts + Pricing Guidelines + Supplier Rates
- [ ] End-to-end test (all 4 projects):
  - [ ] Real inquiry → Router → Client Comms → draft email → rate it
  - [ ] Real proposal request → Router → Proposals → draft proposal → rate it
  - [ ] Real pricing question → Router → Pricing → calculate → verify
  - [ ] Returning client email → Router → Client Comms → personalized draft → rate it
- [ ] Staff M365 connection: each staff member connects their M365 account
- [ ] Staff test: each staff member runs one real task end-to-end

---

## PHASE 3: Training & Go-Live (~2 hours)

- [ ] Print staff quick reference (rework Build Manual Section 10)
- [ ] Friday training session (90 min):
  - [ ] Live demo: Router → Client Comms with real email
  - [ ] Hands-on: each staff member processes one real task
  - [ ] Practice: feedback posting to #ai-feedback
  - [ ] Practice: phone note posting to #client-intel
  - [ ] Q&A
- [ ] System is live — feedback flywheel starts

---

## PHASE 4: Week 2-4 Optimization Cycle

- [ ] Friday Review #1:
  - [ ] Search #ai-feedback for week's ratings
  - [ ] Search shared mailbox for client replies
  - [ ] Cross-reference → identify top 3 improvements
  - [ ] Update DOs/DON'Ts, Best Lines, example files
  - [ ] Copy updated shared files to all projects
- [ ] Friday Review #2 — repeat + deeper analysis
- [ ] Friday Review #3 — system should be stabilizing
- [ ] Friday Review #4 (Month 1 review):
  - [ ] Which project needs most iteration?
  - [ ] Are golden prompts producing consistent quality?
  - [ ] Which email types still get low ratings?
  - [ ] Is Router classifying correctly?
  - [ ] Decision: add Internal Ops project?

---

## PHASE 5: Personal Staff Mining & Style Files (Month 2)

- [ ] Staff member 1: [Name]
  - [ ] Search personal mailbox for client emails sent
  - [ ] Identify personal style patterns
  - [ ] Extract client relationships not in shared mailbox
  - [ ] Create `Style_[Name].txt`
  - [ ] Add any unique client context to #client-intel
- [ ] Staff member 2: [Name] — repeat
- [ ] Staff member 3: [Name] — repeat
- [ ] Staff member 4: [Name] — repeat

**Build after personal mining:**
- [ ] 4 `Style_[Name].txt` personal voice files
- [ ] Decision: create personal Claude Projects per staff member?
- [ ] Fill client history gaps → #client-intel or shared files
- [ ] Update DOs/DON'Ts with cross-staff patterns

---

## PHASE 6: Client Knowledge Base / Second Brain CRM (Month 2-3)

### Design Decisions:
- [ ] Choose storage option:
  - [ ] Option A: SharePoint Excel CRM (simplest, recommended start)
  - [ ] Option B: SharePoint Markdown files (richer)
  - [ ] Option C: Claude Code + Custom MCP Server (most powerful)
  - [ ] Option D: Wait for Anthropic Knowledge Bases
- [ ] Define client card structure (company, contacts, market, status, history, preferences, notes)

### Build (Option A — SharePoint Excel, recommended):
- [ ] Create `Client_Database.xlsx` in SharePoint
- [ ] Populate from shared mailbox mining + personal mining
- [ ] Test: Claude searches this via M365 before every email
- [ ] Staff update workflow defined

### Populate:
- [ ] Export client list from shared mailbox (unique contacts)
- [ ] Mine shared mailbox for booking history per client
- [ ] Mine personal mailboxes for additional context
- [ ] Categorize: hot / warm / cold / inactive
- [ ] Top 50 clients first, then expand to all ~1000

---

## FILE REFERENCE

| File | Status | When Final |
|------|--------|------------|
| `Finland_DMC_Build_Manual.docx` | Example/reference | After all mining |
| `DMC_Router_Custom_Instructions.txt` | Example | After Session 3 |
| `Client_Communications_Custom_Instructions.txt` | Example | After Session 1 |
| `Proposals_Itineraries_Custom_Instructions.txt` | Example | After Session 4 |
| `Pricing_Analysis_Custom_Instructions.txt` | Example | After Session 5 |
| `Email_Mining_Instructions.txt` | Usable as-is | Ready now |
| `DOs_and_DONTs_Starter.txt` | Starter template | After Session 1 |
| `Tone_Guide_Template.txt` | Empty template | After Session 1 |
| `Best_Lines_Starter.txt` | Empty template | After Session 1 |
| `Golden_Prompt_v4_Search_Block.txt` | Example search protocol | After M365 validation |
| `M365_Research_and_Deliverables.md` | Research complete | Done |

---

## SESSION LOG

### Session 2026-02-09 | Phase 0 | Duration: ~15min

**Accomplished:**
- Created finland-dmc-2.0 project structure (all directories)
- Created CLAUDE.md (Claude Code configuration)
- Created ROADMAP.md (this file)
- Created MINING_PROTOCOL.md (standard mining session process)

**Decisions made:**
- Using Claude Code as the organization layer; mining happens in claude.ai
- Incremental mining report approach for all 5 sessions
- Folder structure finalized with mining-outputs, project-files, templates, reference

**Next session:**
- Begin Phase 0: Sign up for Claude Teams, enable M365 connector
- Validate shared mailbox search works
- Create empty Claude Projects

---

### Session 2026-02-09 (continued) | Phase 0 | Duration: ~2h

**Accomplished:**
- Deep research: Claude Code orchestration patterns for multi-company holdings (2 rounds)
- Established two-zone file architecture: Workshop (local+Git) vs. Company Knowledge (OneDrive→SharePoint)
- Created CLAUDE.md hierarchy: user-level → holdings-level → company-level → project-level
- Created 3 custom subagents: mining-organizer, company-setup, file-builder
- Created _shared/ folder structure for cross-company resources
- Initialized Git repository with first commit
- Installed GitHub CLI (gh)
- Created GitHub account: patrick.heiskanen@finland-dmc.com
- Moved 11 reference/template files from Downloads into project
- Installed VS Code recommendation noted (not yet done)

**Decisions made:**
- Two-zone architecture: Workshop files stay local+Git, Company Knowledge goes to OneDrive for M365 access
- Local Git + OneDrive sync = sufficient, no GitHub push needed
- VS Code recommended as editor (free, Microsoft ecosystem, Claude Code extension)
- Agent Teams available but overkill now — start with custom subagents
- M365 admin blocker: use this week for research and fundamentals instead of Phase 0 M365 tasks

**Blockers:**
- M365 account admin on holiday this week — cannot set up M365 connector until next week
- OneDrive sync folder not yet configured on Mac — need to sign in and set up sync

**Next session:**
- Set up OneDrive sync on Mac → create Zone B folder structure
- Install VS Code + Claude Code extension
- Continue AI best practices research for holdings-wide use
- Phase 0 M365 tasks resume when admin returns
