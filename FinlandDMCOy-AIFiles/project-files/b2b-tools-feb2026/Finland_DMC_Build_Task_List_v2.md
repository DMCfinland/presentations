# Finland DMC — Company 2.0 Build Task List v2

**Status:** All documents created so far are EXAMPLES/TEMPLATES.  
**Principle:** Mine first, build final versions after. Every golden prompt is mined and refined individually.  
**Reference:** `Finland_DMC_Build_Manual.docx` = master structure doc (example quality, to be reworked).  
**Progress tracking:** Use this file as the single source of truth. See "How to Track Progress" section below.

---

## How to Track Progress with Claude

### The Problem
Claude conversations don't persist state. A checklist in one chat doesn't carry to the next.
Claude.ai Projects don't support writable files — you can't have Claude auto-update a checklist.

### The Solution: Task File as Living Document

**Your workflow for each session:**
1. Upload this .md file to the conversation (or paste it)
2. Tell Claude: "Here's my progress file. Items marked ✅ are done. Pick up from the first unchecked item."
3. Claude reads your progress, knows where you are, and continues from there
4. After each session: Claude generates an updated version of this file with boxes checked
5. You save the updated file (replace the old one)

**This is the pattern used by the best Claude Code practitioners** (ROADMAP.md / tasks.md approach).
The file IS the memory. You carry it between sessions. Claude reads it fresh each time.

### Why NOT Claude Code for This Build

Claude Code is for **writing software** — it manages code files, runs tests, makes git commits.
Your build is **configuring Claude Projects** — pasting text into web UI fields, uploading .txt files,
running mining conversations, and iterating on prompts interactively.

Claude Code cannot:
- Create or configure Claude Projects (no API for this)
- Paste custom instructions into claude.ai Project settings
- Upload files to Claude Projects
- Run M365 search mining sessions (that's a conversation, not code)
- Connect M365 accounts (that's clicking through web UI)

**Claude Code WILL be useful later for:**
- Building custom MCP servers (Phase 5+)
- Building the Client CRM / Second Brain database (Phase 5+)
- Automating data extraction or transformation pipelines
- Building dashboards or reporting tools
- Any custom software development for Company 2.0

### Tool Stack for This Build

| Tool | What For | When |
|------|----------|------|
| **claude.ai (web)** | Mining sessions, Project configuration, all prompt work | Phase 0-4 (now) |
| **Any text editor** | Editing .txt/.md files between sessions | Phase 0-4 (now) |
| **Microsoft Teams** | Channel setup, verify search works | Phase 0 |
| **Exchange Admin Center** | Shared mailbox permissions | Phase 0 |
| **This .md file** | Progress tracking across sessions | Always |
| **Claude Code** | Custom software, MCP servers, CRM database | Phase 5+ (later) |
| **Cursor/Cline** | Alternative to Claude Code for same purposes | Phase 5+ (optional) |

---

## PHASE 0: Platform Setup (Monday morning, ~45 min)

These tasks are independent of mining — do them first.

- [ ] **Sign up for Claude Teams** — claude.ai/teams, 5 seats, invite staff
- [ ] **Enable M365 connector** — Admin Settings → Connectors → Microsoft 365 → Add
- [ ] **Connect your M365 account** — Global Admin credentials, org-wide consent
- [ ] **Validate shared mailbox** — New chat: *"Search info@finlanddmc.fi for recent emails"*
  - [ ] If works → shared mailbox is primary source ✅
  - [ ] If fails → document the error, pivot to Teams channels as primary
- [ ] **Validate Teams search** — Post test message in a channel → wait 5 min → ask Claude to find it
- [ ] **Validate Excel search** — Upload a test .xlsx to SharePoint → ask Claude to find it
- [ ] **Create 4 Teams channels** (if they don't exist):
  - [ ] `#ai-feedback` — post purpose description
  - [ ] `#client-intel` — post purpose description
  - [ ] `#supplier-notes` — post purpose description
  - [ ] `#best-practices` — post purpose description
  - [ ] Add all 5 staff members to all channels
- [ ] **Create empty Claude Projects** (shells only — no custom instructions yet):
  - [ ] DMC Router
  - [ ] Client Communications
  - [ ] Proposals & Itineraries
  - [ ] Pricing & Analysis
- [ ] **Document M365 search findings**: What works, what doesn't, actual result quality
  - [ ] Which search queries return good results?
  - [ ] Does shared mailbox search work?
  - [ ] Do Teams channel searches work?
  - [ ] Do SharePoint Excel file searches work?
  - [ ] What's the typical result format and volume?

> **After Phase 0:** You have the platform running, M365 validated, empty projects ready. Now you mine.

---

## PHASE 1: Mining Sessions (One per project, ~1-2 hours each)

**How mining works:** Open a conversation with Opus. Use M365 search to dig through your real data. Extract patterns, best examples, actual language, real pricing logic. Then use what you find to write the FINAL golden prompt for that project.

Each mining session follows the same pattern:
1. Search your real data (shared mailbox, Teams, SharePoint)
2. Analyze what you find (patterns, best examples, gaps)
3. Draft the golden prompt based on real findings (not templates)
4. Test the golden prompt against a real task
5. Iterate until it works

---

### Mining Session 1: Client Communications — OUTBOUND (do first)

**What we're mining:** The best emails Finland DMC has SENT to clients.

**Reference examples (to be reworked, not copied):**
- `Client_Communications_Custom_Instructions.txt` — example structure
- `Email_Mining_Instructions.txt` — mining prompt sequence
- `Golden_Prompt_v4_Search_Block.txt` — example M365 search block

**What to mine:**
- [ ] Search shared mailbox for best SENT emails by type (use prompts from `Email_Mining_Instructions.txt`)
  - [ ] New inquiry responses
  - [ ] Follow-up emails
  - [ ] Complaint responses
  - [ ] Cold outreach
  - [ ] Returning client emails
  - [ ] Booking confirmations
  - [ ] Price quote emails
  - [ ] Logistics / quick answers
- [ ] For each type: pick the single best email → save as `Example_Email_[Type].txt`
- [ ] Extract best lines and phrases → populate `Best_Lines.txt`
- [ ] Analyze patterns → refine `DOs_and_DONTs.txt` with real rules from real data
- [ ] Analyze your actual greeting/closing/tone conventions → build real `Tone_Guide.txt`
- [ ] **Test the M365 search protocol**: which searches actually work? What returns good results?
  - [ ] Document which search queries work for client lookup
  - [ ] Document which data sources are most valuable
  - [ ] Note the actual result quality — snippets enough or need full retrieval?

**Build after mining:**
- [ ] Write FINAL `Client_Communications_Custom_Instructions.txt` based on what you actually found
- [ ] Write FINAL `DOs_and_DONTs.txt` from real pattern analysis
- [ ] Write FINAL `Tone_Guide.txt` from your actual email voice
- [ ] Write FINAL `Best_Lines.txt` from extracted real language
- [ ] Curate 8 `Example_Email_*.txt` files from your archive
- [ ] **Validation test:** Paste a real recent inquiry → does Claude draft something you'd actually send?

---

### Mining Session 2: Client Communications — INBOUND (what DMC receives)

**What we're mining:** The types of emails that arrive in the shared mailbox. This teaches Claude what to EXPECT and how to classify incoming requests instantly.

**Why this matters:** The Router and Client Comms projects need to recognize email types instantly. If Claude knows what a typical new inquiry from a Scandinavian tour operator looks like vs. a German corporate incentive request vs. a British wedding group inquiry — it classifies faster and drafts better.

**What to mine:**
- [ ] Search shared mailbox for RECEIVED emails from the past 2 years
- [ ] **Categorize by inquiry type** — what patterns emerge?
  - [ ] Group leisure inquiries (families, friend groups, celebrations)
  - [ ] Corporate/incentive group inquiries
  - [ ] Tour operator / B2B partner inquiries
  - [ ] Conference/MICE inquiries
  - [ ] Individual/small group inquiries
  - [ ] Repeat booking requests from returning clients
  - [ ] Complaints and issue reports
  - [ ] Logistics questions from confirmed bookings
  - [ ] Supplier communications (separate from client emails)
  - [ ] Cold inbound (people finding you via web/referral)
- [ ] **Analyze by source market** — where do inquiries come from?
  - [ ] Which countries/regions?
  - [ ] Which languages?
  - [ ] B2B vs B2C ratio?
  - [ ] Which referral channels (web, partner, trade show)?
- [ ] **Analyze what clients ask for** — recurring themes
  - [ ] Most requested activities/experiences
  - [ ] Most requested seasons
  - [ ] Typical group sizes
  - [ ] Typical budget ranges (if mentioned)
  - [ ] Common special requests
  - [ ] Common concerns/questions
- [ ] **Analyze email patterns** — what information do clients include vs. what's always missing?
  - [ ] What do you always need to ask for that clients never include?
  - [ ] What do clients over-explain that you don't need?
- [ ] **Find "golden inquiries"** — the best, most complete client emails that led to bookings
  - [ ] Save 3-5 as reference (Claude learns what a good lead looks like)

**Build after mining:**
- [ ] Create `Inbound_Email_Patterns.txt` — classification guide for Router
  - [ ] Email type taxonomy with examples of each
  - [ ] Source market patterns
  - [ ] "Always ask for" checklist (info clients typically omit)
  - [ ] "Good lead" signals vs. "tire kicker" signals
- [ ] Update Router custom instructions with real classification categories
- [ ] Update Client Comms instructions with "what to ask for" per inquiry type

---

### Mining Session 3: DMC Router

**Reference example:** `DMC_Router_Custom_Instructions.txt`

**What to mine:**
- [ ] Review 20-30 recent real tasks your team handled (search shared mailbox)
- [ ] Classify each one: what type was it? Which project would it route to?
- [ ] Identify the actual distribution: what % are emails vs. proposals vs. pricing?
- [ ] Use findings from Inbound Mining (Session 2) to refine task categories
- [ ] Check: are there task types the current categories miss?
- [ ] Identify what context the Router needs to extract from each email type
- [ ] Test: paste 5 real emails → does the Router classify correctly and prepare useful prompts?

**Build after mining:**
- [ ] Write FINAL `DMC_Router_Custom_Instructions.txt`
  - Task categories validated against real task distribution
  - Model recommendations based on what actually needs Opus vs. Sonnet
  - Prompt templates tuned to what the execution projects need as input
  - Inbound email classification from Session 2 integrated
- [ ] **Validation test:** Paste 5 different real tasks → does Router classify and prepare prompts correctly?

---

### Mining Session 4: Proposals & Itineraries

**Reference example:** `Proposals_Itineraries_Custom_Instructions.txt`

**What to mine:**
- [ ] Search SharePoint/shared mailbox for your best 5-10 past proposals
- [ ] Analyze proposal structure: what do your good proposals look like?
  - [ ] Sections, ordering, length, formatting
  - [ ] How do you present pricing within proposals?
  - [ ] How do you describe activities? Accommodation? Logistics?
- [ ] Search for client replies to proposals: what convinced clients to book?
- [ ] Search #supplier-notes for current supplier relationships and rates
- [ ] Identify your seasonal activity inventory (what do you actually offer per season?)
- [ ] Check: do you have proposal templates/formats you already use?

**Build after mining:**
- [ ] Write FINAL `Proposals_Itineraries_Custom_Instructions.txt`
- [ ] Write `Proposal_Structure_Template.txt` based on your actual format
- [ ] Curate 2-3 `Example_Proposal_*.txt` from your best real proposals
- [ ] Write `Supplier_Rates_Reference.txt` from current supplier data
- [ ] **Validation test:** Real client brief → does Claude produce a sendable proposal?

---

### Mining Session 5: Pricing & Analysis

**Reference example:** `Pricing_Analysis_Custom_Instructions.txt`

**What to mine:**
- [ ] Search SharePoint for your actual rate cards, pricing Excel files
- [ ] Search shared mailbox for recent pricing emails and quotes
- [ ] Analyze your actual pricing structure: components, markups, margins
- [ ] Search for pricing-related client pushback
- [ ] Identify seasonal pricing variations in your real data
- [ ] Check: what Excel files should live in SharePoint for Claude to search?

**Build after mining:**
- [ ] Write FINAL `Pricing_Analysis_Custom_Instructions.txt`
- [ ] Write FINAL `Pricing_Guidelines.txt` from real pricing logic
- [ ] Update `Supplier_Rates_Reference.txt` with current rates
- [ ] Organize SharePoint Pricing folder with current Excel files
- [ ] **Validation test:** Real group scenario → does the math work? Margins correct?

---

## PHASE 2: Assembly & Testing

- [ ] **Upload all FINAL files to each Claude Project** (in correct order):
  - [ ] DMC Router: Custom instructions + Inbound_Email_Patterns.txt
  - [ ] Client Communications: Custom instructions + DOs/DON'Ts + Tone Guide + Best Lines + 8 example emails
  - [ ] Proposals & Itineraries: Custom instructions + DOs/DON'Ts + Tone Guide + Best Lines + Proposal Template + 2-3 examples + Supplier Rates
  - [ ] Pricing & Analysis: Custom instructions + DOs/DON'Ts + Pricing Guidelines + Supplier Rates
- [ ] **End-to-end test (all 4 projects):**
  - [ ] Real inquiry → Router → Client Comms → draft email → rate it
  - [ ] Real proposal request → Router → Proposals → draft proposal → rate it
  - [ ] Real pricing question → Router → Pricing → calculate → verify
  - [ ] Returning client email → Router → Client Comms → personalized draft → rate it
- [ ] **Staff M365 connection:** Each staff member connects their M365 account
- [ ] **Staff test:** Each staff member runs one real task end-to-end

---

## PHASE 3: Training & Go-Live

- [ ] **Print staff quick reference** (rework Build Manual Section 10 based on final system)
- [ ] **Friday training session** (90 min):
  - [ ] Live demo: Router → Client Comms with real email
  - [ ] Hands-on: each staff member processes one real task
  - [ ] Practice: feedback posting to #ai-feedback
  - [ ] Practice: phone note posting to #client-intel
  - [ ] Q&A
- [ ] **System is live** — feedback flywheel starts

---

## PHASE 4: Week 2-4 Optimization Cycle

- [ ] **Friday Review #1** — use Friday Review Playbook (Build Manual Section 11)
  - [ ] Search #ai-feedback for week's ratings
  - [ ] Search shared mailbox for client replies
  - [ ] Cross-reference → identify top 3 improvements
  - [ ] Update DOs/DON'Ts, Best Lines, example files
  - [ ] Copy updated shared files to all projects
- [ ] **Friday Review #2** — repeat + deeper analysis
- [ ] **Friday Review #3** — system should be stabilizing
- [ ] **Friday Review #4 (Month 1 review):**
  - [ ] Which project needs the most iteration?
  - [ ] Are the golden prompts producing consistent quality?
  - [ ] Which email types still get low ratings?
  - [ ] Is the Router classifying correctly?
  - [ ] Decision: add Internal Ops project? Or not needed?

---

## PHASE 5: Personal Staff Mining & Style Files (Month 2)

**Goal:** Mine each staff member's personal mailbox to capture their individual communication style and fill knowledge gaps from the shared mailbox mining.

**Why:** The shared mailbox (info@finlanddmc.fi) captures the company voice. But individual staff have their own client relationships, personal style variations, and context stored in their personal work emails. Mining these creates richer data AND enables personal Claude Projects per staff member later.

### Per Staff Member (5 sessions, ~1 hour each):
- [ ] **Staff member 1: [Name]**
  - [ ] Search their personal mailbox for client emails they sent
  - [ ] Identify their personal style patterns (greeting style, sentence length, tone)
  - [ ] Extract client relationships not visible in shared mailbox
  - [ ] Create `Style_[Name].txt` — their personal voice profile
  - [ ] Note: any client context only in their personal mailbox → add to #client-intel
- [ ] **Staff member 2: [Name]** — repeat
- [ ] **Staff member 3: [Name]** — repeat
- [ ] **Staff member 4: [Name]** — repeat

**Build after personal mining:**
- [ ] 4 `Style_[Name].txt` personal voice files
- [ ] Decision: create personal Claude Projects per staff member? Or one shared project is enough?
- [ ] Fill any client history gaps found in personal mailboxes → post to #client-intel or update shared files
- [ ] Update DOs/DON'Ts with patterns found across all staff

---

## PHASE 6: Client Knowledge Base / Second Brain CRM (Month 2-3)

**Goal:** Build a structured, searchable archive of all ~1000 client contacts with their history, preferences, booking patterns, and relationship status.

**Why:** M365 search gives you real-time access to raw emails. But a structured CRM-like knowledge base gives Claude instant access to summarized, organized client intelligence without needing to search and parse through email threads every time.

### Design Decisions (research before building):
- [ ] **Where to store it?** Options:
  - [ ] SharePoint Excel file(s) — Claude can search and read via M365 connector
  - [ ] SharePoint/OneDrive as structured .md files (one per client) — searchable
  - [ ] Claude Project knowledge files (limited by 200K token window)
  - [ ] Custom database via Claude Code + MCP server (most powerful, most effort)
  - [ ] Wait for Anthropic's Knowledge Bases feature in Cowork (coming soon — leaked Jan 2026)
- [ ] **What to store per client?** Define the client card structure:
  - [ ] Company name, contacts, market/country
  - [ ] Communication language preference
  - [ ] Relationship status: hot / warm / cold / inactive
  - [ ] Booking history: dates, group sizes, programs, revenue
  - [ ] Preferences: activities liked, accommodation preferences, dietary needs
  - [ ] Communication notes: tone preferences, decision-making style, key contacts
  - [ ] Last contact date and next follow-up date
  - [ ] Source: how they found Finland DMC

### Build Options (pick one based on research):

**Option A: SharePoint Excel CRM (simplest, works now)**
- [ ] Create `Client_Database.xlsx` in SharePoint with columns for all fields above
- [ ] Populate from shared mailbox mining + personal mailbox mining
- [ ] Claude searches this via M365 connector before every email
- [ ] Staff update it manually (or Claude generates update suggestions)
- [ ] Limitation: Excel has 1M row limit but 1000 clients is fine

**Option B: SharePoint Markdown Files (richer, searchable)**
- [ ] Create a SharePoint folder: `Clients/[CompanyName].md`
- [ ] Each file is a structured client card in markdown
- [ ] Claude searches by client name, returns the whole card
- [ ] Richer than Excel — can include narrative notes, email excerpts
- [ ] Limitation: more manual to maintain, but Claude can generate update drafts

**Option C: Claude Code + Custom MCP Server (most powerful, Phase 6+)**
- [ ] Build a lightweight database (SQLite or Postgres)
- [ ] Build MCP server that Claude can query
- [ ] Claude searches by client name, gets structured data back
- [ ] Can include advanced features: similarity search, relationship graphs
- [ ] **This is where Claude Code / Cursor becomes the right tool**
- [ ] Limitation: requires development effort, hosting, maintenance

**Option D: Wait for Anthropic Knowledge Bases (coming soon)**
- [ ] Anthropic is building persistent, topic-specific Knowledge Bases for Claude Cowork
- [ ] Leaked January 2026, likely shipping Q1-Q2 2026
- [ ] Would auto-maintain and update client knowledge from conversations
- [ ] Could be the ideal solution if timing works
- [ ] Risk: unknown ship date, unknown feature scope

**Recommended approach:**
Start with **Option A** (SharePoint Excel) now — it works today, Claude can read it.
Plan for **Option C** or **Option D** as the long-term solution.
Use mining sessions to populate the initial data.

### Populating the Client Database:
- [ ] Export client list from shared mailbox (unique email domains / contacts)
- [ ] Mine shared mailbox for booking history per client
- [ ] Mine personal mailboxes for additional context
- [ ] Categorize: hot (active) / warm (inquired recently) / cold (no contact 6+ months)
- [ ] Claude assists: "Search all emails from [client domain]. Summarize our relationship."
- [ ] Repeat for top 50 clients first, then expand to all 1000

---

## File Reference (All are EXAMPLES to be reworked after mining)

| File | Status | When It Becomes Final |
|------|--------|----------------------|
| `Finland_DMC_Build_Manual.docx` | Example/reference structure | After all mining complete |
| `DMC_Router_Custom_Instructions.txt` | Example | After Mining Session 3 |
| `Client_Communications_Custom_Instructions.txt` | Example | After Mining Session 1 |
| `Proposals_Itineraries_Custom_Instructions.txt` | Example | After Mining Session 4 |
| `Pricing_Analysis_Custom_Instructions.txt` | Example | After Mining Session 5 |
| `Email_Mining_Instructions.txt` | Usable as-is (mining prompts) | Ready now |
| `DOs_and_DONTs_Starter.txt` | Starter template | After Mining Session 1 |
| `Tone_Guide_Template.txt` | Empty template | After Mining Session 1 |
| `Best_Lines_Starter.txt` | Empty template | After Mining Session 1 |
| `Golden_Prompt_v4_Search_Block.txt` | Example search protocol | After M365 validation |
| `M365_Research_and_Deliverables.md` | Research complete ✅ | Done — reference doc |

---

## Timeline Overview

| Phase | When | Duration | Tool |
|-------|------|----------|------|
| Phase 0: Platform Setup | Day 1 (Monday) | ~2 hours | claude.ai + Teams Admin |
| Phase 1: Mining Sessions 1-5 | Day 1-3 | ~6-8 hours total | claude.ai (Opus) |
| Phase 2: Assembly & Testing | Day 3-4 | ~2 hours | claude.ai |
| Phase 3: Training & Go-Live | Day 5 (Friday) | ~2 hours | In-person |
| Phase 4: Weekly Optimization | Weeks 2-4 | 15 min/week | claude.ai |
| Phase 5: Personal Staff Mining | Month 2 | ~5 hours | claude.ai (Opus) |
| Phase 6: Client CRM / Second Brain | Month 2-3 | ~10-20 hours | claude.ai → Claude Code |

---

## Upcoming Anthropic Features to Watch

These features are in development and may change how you build later phases:

| Feature | Status | Impact on Finland DMC |
|---------|--------|----------------------|
| **Cowork Knowledge Bases** | Leaked Jan 2026, in development | Could replace manual CRM. Auto-maintains client knowledge. |
| **Claude Memory (Teams plan)** | Rolling out Feb 2026 | Claude remembers across conversations without uploading files |
| **MCP Registry** | In development | Could enable dynamic connector management |
| **Cowork + Projects integration** | Not yet available | Currently Cowork can't use Projects — when it can, big upgrade |

**Action:** Don't wait for these. Build with what works today. Upgrade when features ship.
