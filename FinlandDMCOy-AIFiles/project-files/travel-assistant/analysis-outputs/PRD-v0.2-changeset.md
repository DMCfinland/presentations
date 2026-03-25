# PRD v0.2 Change Set
Source: Cluster findings A–E (vision, technical core, developer briefs, execution, monster doc) + PRD v0.1.1
Produced: 2026-02-21

---

## TOP 3 MOST IMPORTANT CHANGES

**Change 1 — ADD PRODUCT 3: Finland DMC Personal Travel Assistant (FinnConcierge)**
PRD v0.1.1 describes two products (Second Brain, Email Drafter). The Word documents reveal a third product — a fully architected B2C guest-facing AI concierge — that is as developed or more developed than the other two. It has its own architecture (Full Azure Serverless), its own build methodology (Blueprint Driven Development + Python CLI Harness), and a different deployment target (Järvisydän pilot first, not Finland DMC). This is not a future item; it is a present, parallel workstream that must appear in the PRD. Expand in Section 1 and add full new sections.

**Change 2 — CONTRADICTON ON DEPLOYMENT SEQUENCE: Järvisydän is Travel Assistant pilot, NOT "after Finland DMC stable"**
PRD v0.1.1 Section 16 states: "Järvisydän — After Finland DMC stable." The Word documents (Cluster A Decision 6, Cluster C Evolution section, Cluster E Järvisydän vs Finland DMC section) explicitly make Järvisydän the FIRST deployment target for the Travel Assistant. The first customer deployment is Järvisydän customers receiving the travel assistant for free. This directly contradicts Section 16 and must be corrected throughout the PRD.

**Change 3 — ARCHITECTURE DECISION A5 IS NOW RESOLVABLE: Travel Assistant stack is entirely different from both options**
A5 in PRD v0.1.1 asks: "M365-native or unified with Email Drafter?" The Word documents reveal a third architecture — Full Azure Serverless (Functions + Event Grid + Cosmos DB + Azure SQL + Azure AI Search + Data Lake Gen2 + Next.js PWA) — for the Travel Assistant. This stack shares nothing with either A5 option. A5 remains open for Second Brain, but the PRD architecture section must now show THREE distinct stacks, not two.

---

## 1. PRODUCT MAP UPDATE

### Current state (PRD v0.1.1)
Two products: Second Brain (CRM intelligence) + Email Drafter (proposal automation). Section 4 shows a two-product diagram. Section 16 lists Järvisydän as a future replication target after Finland DMC.

### What must change

**Add Product 3: Finland DMC Personal Travel Assistant (FinnConcierge)**
- B2C guest-facing AI concierge — completely different audience, stack, and purpose from the B2B-facing Second Brain and Email Drafter
- Named "FinnConcierge" in execution documents (Cluster D, source: 11.12)
- Product promise: "The invisible guide in your pocket. Proactive, context-aware, and transactional." (confirmed by Word docs, Cluster B and E)
- Serves guests AFTER booking — from booking confirmation to homecoming
- Relationship to the other two products: parallel build, NOT dependent on Second Brain or Email Drafter being completed first

**Correct the relationship between the three products**

| Product | Audience | Stage | Stack | Pilot target |
|---------|----------|-------|-------|--------------|
| Second Brain | B2B: Finland DMC staff | Build | M365-native OR n8n/Supabase (A5 still open) | Finland DMC |
| Email Drafter | B2B: Finland DMC staff | Build | n8n + Supabase + Claude API | Finland DMC |
| Travel Assistant (FinnConcierge) | B2C: Guests post-booking | Build | Full Azure Serverless | Järvisydän (FIRST) |

The three products share the Azure hosting ecosystem and the principle of AI agents + human oversight, but they have separate stacks, separate data stores, separate audiences, and separate build timelines.

**Correct the deployment sequence**
- CONTRADICTION: PRD v0.1.1 Section 16 says Järvisydän gets the platform "after Finland DMC stable"
- CORRECTION (confirmed by Word docs): Järvisydän is the FIRST deployment for the Travel Assistant. Finland DMC customers (travel agency bookings) come AFTER the Järvisydän pilot proves the system.
- Why: Järvisydän has Oracle Opera + BookVisit webhook → direct API ingestion, no email parser needed. This makes Järvisydän technically simpler as MVP first target.
- The Second Brain + Email Drafter (B2B tools) remain Finland DMC-first and are a separate track.

**Reframe Section 16 (Portfolio Replication)**
Current Section 16 frames everything as "Finland DMC pilot → replicate to Järvisydän." Replace with:
- Track 1 (B2B tools): Finland DMC pilot → other 1658 companies
- Track 2 (Travel Assistant): Järvisydän pilot → Finland DMC travel agency bookings → KonTiki (B2B white label) → other 1658 companies → external licensing

---

## 2. NEW SECTIONS NEEDED

### New Section: Product 3 — Travel Assistant (FinnConcierge) Overview
**Why needed:** No coverage in PRD v0.1.1. Must be added at the same depth as Sections 5 and 6.
**Cover:**
- Core product promise and B2C use case (guest journey from booking confirmation to homecoming)
- Multi-agent architecture: Master Agent (Concierge), Mood Evaluator (Psychologist), Suggestion Chef (Salesman), Booking Specialist (Cashier) — confirmed across all 5 clusters
- Access model: Magic Link (cryptographically signed JWT, zero registration, zero passwords) — sent via booking confirmation webhook (Järvisydän) or confirmation email (travel agency bookings)
- White-label "Chameleon" model: single codebase, brand identity applied from `tenant_config.json` at runtime (CSS variables, persona name, tone of voice)
- Multi-tenancy from day one: adding a new resort = new row in tenant config DB, no code changes
- Sources: Cluster A (Decisions 10–12), Cluster B (Decisions 1–3), Cluster C (v0.7 Evolution), Cluster D (Decisions 4–5), Cluster E (all sections)

### New Section: Travel Assistant Architecture (Full Azure Serverless Stack)
**Why needed:** Entirely distinct from the Second Brain / Email Drafter stack. Not in PRD v0.1.1 at all.
**Cover:**
- Full confirmed stack: Azure Functions (Python/Node.js) as compute, Azure Event Grid as event bus, Azure OpenAI GPT-4o via Private Endpoint (Zero Data Retention), Cosmos DB (chat history + session state), Azure SQL (ledger + users + products), Azure AI Search (vector RAG), Data Lake Gen2 (cold analytics), Next.js PWA (frontend), Azure Maps API (geo-routing)
- Four RAG "shelves": Commercial Shelf, Cultural Shelf, Practical Shelf, Internal Shelf — agents access directly, not through Librarian intermediary for live queries
- GDPR note: Azure North Europe region (confirmed by Cluster C and E), NOT Sweden Central (contrast: Second Brain uses Sweden Central for CRM PII)
- Unresolved: Redis vs Pinecone for in-memory vector DB to meet 800ms Chef latency requirement
- Considered but deferred: Adyen vs Stripe Connect for Phase 2 payments (Adyen already used by Järvisydän), OpenAI Realtime API for voice in Phase 3
- Sources: Cluster B (Tech Choices 1–7), Cluster C (Tech Choices 1–9), Cluster D (Tech Choices 4–9), Cluster E (Tech Choices 1–12)

### New Section: Travel Assistant AI Agent Layer
**Why needed:** The multi-agent architecture with specific behavioral specifications (Mood Matrix, Suggestion Chef scoring formula, Safety guardrails, Staff Dashboard) is not in PRD v0.1.1 and represents significant design depth.
**Cover:**
- Orchestrator pattern: Master Agent is the only component that communicates with users. Specialist agents are background microservices returning JSON. Master Agent CANNOT invent prices or availability — hard-coded System Prompt rule.
- Context Backpack: short-term memory dropped immediately when conversation topic (Intent) changes — prevents token bloat
- Mood Evaluator: async listener (no delay to chat). 7-dimensional Mood Matrix (Energy, Hunger, Social_Battery, Luxury_Affinity, Nature_Rawness, Safety_Need, Foodie_Focus — each 0–100). Customers mapped to cluster archetypes (e.g., German_Active_Family) for statistical optimization.
- Suggestion Chef scoring formula: `Score = (Match×W1) + (Weather×W2) + (Value×W3) + (Margin×W4) + (Novelty×W5)`. Hard Filter before scoring: is it open? is there availability? does the customer have a car? Epsilon-Greedy 80/20 exploitation/exploration. 800ms latency hard limit, fallback to generic list if exceeded.
- Safety guardrail: ice safety / weather risks MUST query SafetyBulletin_Tool first. If data >24h old → immediate human handover. Northern lights: probability language only, never promise sightings.
- Staff Dashboard: Traffic Light (Green/Yellow/Red/FIRE RED), Whisper Mode (human injects instructions, customer does not see), Takeover (full handover to human), 10-minute auto-restore Safety Net, "God Mode" force-push button.
- Patience Meter: if < 30 → Silent Mode (no upsell). 4-hour cooldown after negative experience.
- Sources: Cluster A (Decisions 8–10), Cluster B (Decisions 6–12), Cluster C (all), Cluster D (Requirements 4–6), Cluster E (AI Layer section)

### New Section: Travel Assistant Build Phases (Järvisydän MVP → Scale)
**Why needed:** PRD v0.1.1 Build Phases (Section 9) cover only Second Brain and Email Drafter. The Travel Assistant has its own phase structure.
**Cover:**
- MVP scope (3 months from start): Järvisydän only, Finnish + English, Magic Link onboarding, basic RAG for Järvisydän FAQ, mood + suggestion logic with weather, hybrid booking (API + email fallback), Staff Dashboard v1 with traffic lights, Shadow Ledger with manual invoicing. No in-app card processing, no Holiday Builder, no voice calls.
- Phase 2 (post-MVP): Multi-language expansion (Italian, German minimum), Holiday Builder (pre-booking flow), Adyen/Stripe Connect payment integration, cashback mechanics, expanded partner network (KonTiki white label), Split Payment support
- Phase 3 (future): Voice AI via OpenAI Realtime API, full self-service Partner Portal, global licensing model
- Go/No-Go gate: Vertical Slice Mock MVP validates agent-to-agent context passing (Mood Matrix, User ID) and Shadow Ledger booking trigger BEFORE full blueprint generation
- Sources: Cluster A (Decision 11), Cluster C (v0.1 Evolution section), Cluster D (Decisions 4–7), Cluster E (Build Plan section)

### New Section: Build Methodology — Blueprint Driven Development + Python CLI Harness
**Why needed:** PRD v0.1.1 Section 9 describes phases and infrastructure but not the HOW of building. The Word documents contain a fully specified build methodology that applies to the Travel Assistant build.
**Cover in Section 7 below — see Build Methodology.**

### New Section: Shadow Ledger + Commission Accounting
**Why needed:** The Shadow Ledger is a first-class architectural component, not a footnote. Not in PRD v0.1.1.
**Cover:**
- All transactions logged with: flow_type (API/MANUAL/AFFILIATE), status, commission_pct, receivable_amount
- Three booking types: API (automated capture), Manual/Email (24h authorization timeout, auto-void if partner does not respond), Affiliate (signed tokens, `?source=kontiki` tamper-proof)
- Billing-ready from MVP: Contract Table calculates commission on booking (Sale 200€ × 15% = 30€ receivable)
- Phase 2: automated reconciliation. Phase 1 MVP: manual monthly reconciliation against partner affiliate reports
- Sources: Cluster B (Requirements 8), Cluster C (Decision 7), Cluster D (Requirement 8), Cluster E (Features section)

---

## 3. EXISTING SECTIONS TO UPDATE

### Section 1 (Executive Summary)
**What to change:** Summary describes "two interlocking components." Expand to three.
**What it should say instead:** Add a third row to the product table:
| Travel Assistant (FinnConcierge) | B2C guest-facing AI concierge. After a guest books Järvisydän or a Finland DMC trip, they receive a Magic Link that opens a personal AI travel assistant — no registration, no passwords. Proactive recommendations based on weather, mood, and itinerary gaps. Books activities, tracks commissions. 24/7 without staff intervention. |

Also update: "Pilot: Finland DMC is the test bed for Second Brain + Email Drafter. Järvisydän is the first pilot for the Travel Assistant." (new finding — contradicts current framing)

### Section 3.1 (Operating Principles)
**What to change:** Principles currently describe B2B workflow automation. Add one Travel Assistant-specific principle.
**What to add:**
- "Proactive, not reactive." The Travel Assistant must anticipate guest needs based on weather, location, and personal preferences before the guest asks. Push value, do not wait for the guest to navigate a menu.
- Source: Cluster A (Requirement 1), Cluster B (Notable Quotes 2), confirmed by Cluster E.

### Section 4 (Architecture diagram)
**What to change:** Current diagram shows two products sharing one backoffice. This is now incomplete and misleading.
**What it should show:** Three-product map with three distinct stack zones:
```
ZONE 1 — B2B TOOLS (Finland DMC staff)
  Second Brain → M365-native (Power Automate / SharePoint / Azure OpenAI, A5 still open)
              OR → n8n + Supabase (if A5 resolved that way)
  Email Drafter → n8n + Supabase + Claude API

ZONE 2 — B2C GUEST CONCIERGE (Travel Assistant)
  FinnConcierge → Full Azure Serverless
  (Azure Functions + Event Grid + GPT-4o + Cosmos DB + Azure SQL + Azure AI Search + Data Lake Gen2 + Next.js PWA)
  Multi-tenant: same codebase → Järvisydän config / KonTiki config / Finland DMC config

ZONE 3 — SHARED INFRASTRUCTURE (optional, where stacks overlap)
  Azure OpenAI (both zones use this, different endpoints)
  M365 Graph API (Email Drafter + future Travel Assistant email ingestion)
```
- Source: PRD v0.1.1 + Cluster B (Tech Choices), Cluster E (Architecture section)
- Note: D3/D4/D5 architecture risks in Design Decisions Log (Section 17) are NOT affected by this change — they remain open for Zone 1 only.

### Section 9 (Build Phases)
**What to change:** Current phases describe only Second Brain and Email Drafter. Travel Assistant phases must be added as a parallel track.
**What it should say:** Add a clearly labeled track header:

Track 1 — B2B Tools (Finland DMC)
- Phase 0 through Phase 7 as currently written (no changes needed within phases)

Track 2 — B2C Travel Assistant (Järvisydän-first)
- Phase TA-0: Vertical Slice Mock MVP — thin functional slice through entire system (already done per Cluster D Decision 4). Go/No-Go: validate agent context passing + Shadow Ledger trigger before proceeding.
- Phase TA-1 (3 months): Järvisydän MVP — see New Sections above for scope
- Phase TA-2: Finland DMC travel agency bookings (email parser ingestion path, replaces webhook)
- Phase TA-3: B2B white-label (KonTiki first), Holiday Builder, payment integration
- Phase TA-4: Voice AI + global licensing

**Also update Phase 0 description:** Current text says "Validate golden prompts using claude.ai." This is correct for Track 1. Add note that Track 2 Phase TA-0 (Vertical Slice Mock MVP) is already complete.

### Section 11 (Open Questions — Technical)
**What to change:** Add new technical questions from the Word documents (see Section 5 of this change set). Also update A5 framing.
**A5 update:** Current A5 asks "M365-native vs. unified n8n/Supabase?" This framing is still correct for Zone 1 (Second Brain). Add a note: "A5 applies to Zone 1 (B2B tools) only. Zone 2 (Travel Assistant) uses Full Azure Serverless — this is not an open question, it is confirmed by Word docs across all 5 clusters."

### Section 13 (Risks)
**What to change:** Add Travel Assistant-specific risks confirmed by Word documents.
**What to add:**

| Risk | P | Impact | Mitigation |
|------|---|--------|------------|
| Hallucination on prices/availability | H | Very high | Hard-coded system prompt: Master Agent cannot confirm prices without tool call. Zero exceptions. (confirmed by Word docs) |
| Safety data staleness (ice, northern lights) | M | Very high | SafetyBulletin_Tool query mandatory; if data >24h old → human handover immediately. Northern lights: probability language only. |
| Over-interruption (Gap Finder) | M | Medium | Gate conditions: session active + gap + weather threshold + 08:00–22:00 window only. Internal Monologue logic checks before interrupting. |
| Oracle Opera integration complexity | H | High | Anti-corruption layer (adapter) between Booker Agent and Opera. Scope unknown until Järvisydän IT engaged. |
| Scoring formula cold start | H | Medium | Start with Tabula Rasa weights, let Optimizer converge over 90 days. Recommendations are suboptimal during this window. |
| Affiliate link commission fraud | L | Medium | Signed tokens (`?source=kontiki` tamper-proof). Manual monthly reconciliation in Phase 1. |
| Staff equity promise (organizational) | H | High | The "everyone builds this with us will own real equity" commitment (Cluster A Risk 2) requires concrete option program, phantom shares, or bonus pool announcement. Not doing this = fear wins over excitement. |

### Section 14 (What This PRD Does Not Yet Cover)
**What to change:** Several items in this section are now answered by the Word docs. Remove or mark resolved:
- "New requirements not yet captured" → now captured (Travel Assistant is the primary new requirement)
- "Architecture changes if Word docs contradict v0.1 decisions" → Architecture Decision A5 still open for Zone 1; Zone 2 architecture is now confirmed
- Remove item: "Järvisydän second system — does it get the same backoffice or variant?" → ANSWERED: Järvisydän gets Travel Assistant (Zone 2) as its primary system, NOT the B2B tools (Zone 1). These are not the same product. Järvisydän IT team participates in Travel Assistant development. (confirmed by Cluster E)

**What to keep as still-open:**
- Day 1 runbook for Patrick
- Staff onboarding protocol
- Rollback plan
- Commercial model for shared infrastructure
- Detailed acceptance tests per phase gate

### Section 16 (Portfolio Replication)
**CONTRADICTION — requires full rewrite of this section.**
Current table:
- "Järvisydän — After Finland DMC stable — Resort group sales + event automation"

Must be replaced with a two-track table:

Track 1 — B2B Tools (Second Brain + Email Drafter):
| Finland DMC | Pilot — this build | Now |
| M/S Marival | Cruise group sales | After Finland DMC stable |
| Other 1658 | Per company | Rolling |

Track 2 — Travel Assistant (FinnConcierge):
| Järvisydän | Resort post-booking assistant — FIRST PILOT | Now (parallel with B2B tools) |
| Finland DMC (agency bookings) | Travel agency booking confirmation path | After Järvisydän MVP |
| KonTiki (B2B white-label) | German tour operator guest concierge | Phase TA-3 |
| Other 1658 + external | Licensing model | Phase TA-4+ |

Source: Cluster A (Decision 6), Cluster C (Evolution section), Cluster E (Järvisydän vs Finland DMC section)

---

## 4. ARCHITECTURE DECISIONS — STATUS UPDATE

### A1 (Primary intelligence DB: Supabase vs SharePoint Lists only)
**Status:** Still open for Zone 1 (B2B tools). No change from PRD v0.1.1.
**Travel Assistant impact:** Irrelevant. Travel Assistant uses Cosmos DB (hot storage) + Azure SQL (relational) + Azure AI Search (vector). Supabase is not in the Travel Assistant stack at all. If A1 resolves to SharePoint-only for Second Brain, this has zero effect on Travel Assistant.

### A3 (Automation backbone: n8n vs Power Automate)
**Status:** Still open for Zone 1. No change from PRD v0.1.1.
**Travel Assistant impact:** Irrelevant. Travel Assistant uses Azure Functions + Azure Event Grid as its automation layer — not n8n and not Power Automate.

### A5 (Second Brain infrastructure: M365-native vs unified with Email Drafter)
**Status:** Still open for Zone 1.
**Key update:** The Word documents confirm that the Travel Assistant is a third product on a completely separate stack. This NEW information should make A5 EASIER to resolve, not harder. Patrick no longer needs to unify Second Brain with the Travel Assistant; that question was never on the table. A5 is purely: "Do I build Second Brain M365-native (as designed in the 4 Opus docs) or migrate it to n8n/Supabase (as this PRD recommends)?" The 400-page Word documents do not appear to resolve this directly — Patrick decision still required.

**Recommendation for PRD v0.2:** Retain A5 as the highest-priority open decision for Phase 1 (Zone 1). Add a note that it is NOW isolated — the Travel Assistant stack does not affect or constrain A5 in either direction.

### New Architecture Decision Emerged: TA-A1 — In-memory vector DB for Suggestion Chef latency
**Status: OPEN**
- Requirement: Chef query must complete in under 800ms
- Option 1: Redis (in-memory key-value + vector)
- Option 2: Pinecone (managed vector DB)
- Source: Cluster B (Open Question 1), Cluster D (Tech Choice 11), Cluster E (Tech Choice 11)
- Blocks: Phase TA-1 infrastructure build
- Owner: Patrick + technical lead (Cursor / AI dev team)

### New Architecture Decision Emerged: TA-A2 — Payment processor for Phase 2
**Status: OPEN, not MVP-blocking**
- Option 1: Adyen (Järvisydän already uses it — lower integration friction)
- Option 2: Stripe Connect (better multi-party payment splitting, more developer-friendly)
- Adyen Issuing vs Stripe Issuing for virtual wallet / cashback mechanics
- GDPR note: if building virtual wallet / e-money features, DMC may need e-money license
- Source: Cluster E (Tech Choice 10, Open Question 2)
- Blocks: Phase TA-2 payment integration — NOT MVP

### New Architecture Decision Emerged: TA-A3 — Azure region for Travel Assistant
**Status: CLARIFICATION NEEDED**
- Word documents consistently say "North Europe" for Travel Assistant
- Second Brain uses "Sweden Central" for GDPR CRM PII compliance
- Cluster B flags: are North Europe and Sweden Central equivalent legal regions for GDPR?
- Source: Cluster B (Open Question 2)
- Resolution needed: Confirm with legal / DPA whether North Europe is sufficient for Travel Assistant guest PII, or if Sweden Central is required here too

### New Architecture Decision Emerged: TA-A4 — Build methodology for Travel Assistant (Darwinian League vs simpler hierarchy)
**Status: OPEN — under research**
- The Word documents describe a "Darwinian/Tournament" multi-agent coding model (1 Leader + 3 Competitor Coders + Red Team adversarial gate)
- Explicitly costs 3x inference vs simpler hierarchical model (Microsoft AutoGen, ChatDev, MetaGPT)
- Research was in progress at time of Word doc authorship — a "Bible of Agentic Coding" comparative analysis was commissioned
- Source: Cluster D (Decision 9, Open Question 2, Risk 4)
- Does not block Travel Assistant product design, but blocks choice of HOW to build it via the Python CLI Harness

---

## 5. NEW OPEN QUESTIONS

### Blocking questions (must resolve before Phase TA-1 build begins)

| # | Question | Source | Blocks |
|---|----------|--------|--------|
| TA-T1 | Oracle Opera anti-corruption layer scope: API complexity unknown until Järvisydän IT team engaged. Adapter layer planned but scope undefined. | Cluster E (Open Questions 1) | Phase TA-1 booking integration |
| TA-T2 | Redis vs Pinecone for in-memory vector DB: 800ms latency requirement cannot be met without resolving this. | Cluster B (OQ 1), Cluster E (Tech 11) | Phase TA-1 Suggestion Chef |
| TA-T3 | Azure region (North Europe vs Sweden Central) for Travel Assistant guest PII: legal clarification needed. | Cluster B (OQ 2) | Phase TA-1 infrastructure |
| TA-T4 | Järvisydän IT team engagement: BookVisit webhook API access, Oracle Opera API access, BookVisit product catalog export for Commercial Shelf. None of this can proceed without Järvisydän IT on board. | Cluster E (Architecture + Integration sections) | Phase TA-1 entirely |
| TA-T5 | Vertical Slice Mock MVP Go/No-Go: three specific validation questions (a) did agents pass context without losing state? (b) did Shadow Ledger capture booking triggers correctly? (c) which blueprints were ignored or hacked to make the test pass? | Cluster D (Open Question 1) | Phase TA-1 scale-up |

### Informational questions (do not block build, but need tracking)

| # | Question | Source |
|---|----------|--------|
| TA-I1 | "Täti's Customer Timeline" — Patrick's domain expert was assigned to write the canonical perfect guest journey timeline for Järvisydän. This is the source of truth for the Trigger Engine and proactive messaging. Status unknown. | Cluster E (Open Question 3) |
| TA-I2 | Scoring formula initial weights (W1–W5): plan is Tabula Rasa defaults, Optimizer converges over 90 days. Confirm this is acceptable — recommendations will be suboptimal during this window. | Cluster B (OQ 2), Cluster D (OQ 4), Cluster E (OQ 5) |
| TA-I3 | Staff equity/incentive structure: the commitment to equity for staff who build the Travel Assistant pivot was left as "details next week." Not a technical question but a blocking organizational question for staff retention during build. | Cluster A (OQ 1, Risk 2) |
| TA-I4 | B2B white-label commercial model: pricing for white-label tier, target number of B2B partners at launch, onboarding process not defined. | Cluster B (OQ 5), Cluster C (OQ 8) |
| TA-I5 | Instant B2B Demo (Puppeteer scraping partner URL in 5 seconds) — MVP scope or post-MVP? | Cluster C (OQ 6) |
| TA-I6 | "Sissi-coefficient" (outdoor hardiness/tolerance): referenced in weather scoring but not defined. How is it measured or set per customer? | Cluster A (OQ 8) |
| TA-I7 | Mystery Shopper data weight decay function: exact formula for reducing synthetic data weight as real data accumulates — plan is manual step-down at 100, 500, and 1,000 real user milestones. No formula defined yet. | Cluster E (OQ 6) |
| TA-I8 | Darwinian/Tournament build model vs simpler hierarchy: "Bible of Agentic Coding" comparative analysis was commissioned. What was the outcome? Does it affect which harness to use for Travel Assistant build? | Cluster D (Decision 9, OQ 2) |

---

## 6. WHAT TO REMOVE OR ARCHIVE

### Remove from Section 14 (What This PRD Does Not Cover)
Remove: "Järvisydän second system — does it get the same backoffice or variant?"
Reason: ANSWERED. Järvisydän is the Travel Assistant's first pilot. It uses Zone 2 (Full Azure Serverless) not Zone 1 (B2B tools). These are confirmed separate products. Not a "variant" question — they are categorically different systems serving different users.

Remove: "New requirements not yet captured (the primary reason for Word doc digestion)"
Reason: Now captured. The Travel Assistant is the primary new requirement. This item was a placeholder; replace with specific tracked items.

### Archive from Section 14
Move to "resolved" status (no longer open):
- "Architecture changes if Word docs contradict v0.1 decisions" → Zone 2 architecture is now confirmed. Zone 1 decisions (A3, A5) remain open but are not "unknown" anymore.
- "n8n Teams connector capability" → Still relevant for A3, but now clearly scoped to Zone 1 only. Not a general unknown.

### Retain but reframe
Section 17 (Design Decisions Log): D3, D4, D5 (the n8n/Supabase unification risks) should be reframed to note they apply to Zone 1 only. Travel Assistant (Zone 2) does not depend on these decisions. This reduces the architectural risk profile somewhat — Zone 2 can proceed regardless of how A5 resolves.

### No sections to remove
All existing sections remain valid for Zone 1. None contradict the new material strongly enough to require removal — only expansion and qualification.

---

## 7. BUILD METHODOLOGY

### What the Word documents describe
The execution documents (Cluster D) define a complete build methodology that applies specifically to the Travel Assistant. This methodology does not appear in PRD v0.1.1 at all.

**Blueprint Driven Development (BDD)**
- No code written without a `.md` Blueprint that defines logic, data contracts, and interfaces
- Architect (Patrick + Claude) creates the Blueprint → Code Agent (Cursor) reads it and implements automatically
- Quote: "This is critical to understand. We do not code anything without a Blueprint." (Cluster D, confirmed by Word docs)
- Not the same as Phase 0 Claude Project MVP in PRD v0.1.1. That validates prompts. BDD governs all infrastructure code.

**Python CLI Harness (not Cursor GUI chat)**
- Problem: Cursor chat window cannot manage 1000-task state — context fills, hallucinations occur
- Solution: Custom Python CLI Harness:
  - `initializer.py`: reads MASTER_MAP.md, generates TASKS.json with 500+ microtasks via Claude 3.5 Sonnet API
  - `orchestrator.py`: reads JSON tasks, runs loop, calls agent instances via API, writes files to disk
  - Task state stored in JSON/SQLite on disk — NOT in chat history. "Eternal memory."
  - Up to 10 parallel agent threads for independent tasks
  - DAG structure in TASKS.json enables parallel execution without dependency conflicts
- Source: Cluster D (Decisions 6–7, Tech Choices 10–11)
- Status as of Word doc authorship: Harness designed, Vertical Slice Mock MVP already built with Cursor as proof-of-concept

**Agentic coding team topology**
- Patrick's role: non-technical founder. Never touches code or terminal. All interaction via Claude chat or Slack. All code execution delegated to agents. (confirmed by Word docs — Cluster D Decision 3)
- Dev team: AI Junior Developers (Cursor/Copilot) handle 70–80% of boilerplate. Human Lead Developer (if any) is architect only — approves structure, reviews security, handles Oracle Opera legacy integration (Cluster E Constraint 11)
- Quality gate: adversarial Red Team agent attacks code before any commit. No code enters codebase without passing Red Team. (Cluster D Requirement 10)
- Error loop: agent reads stderr, queries Senior Dev Agent (NOT human), retries. 3-strike rule escalates to human alert. (Cluster D Requirement 11)

**Does this affect PRD v0.1.1 Section 9 (Build Phases)?**
YES — in two ways:

1. The Phase structure is correct but missing the methodology layer. Add a section before Phase 0 (or as Phase 0 amendment) describing:
   - Before any infrastructure code is written: MASTER_MAP.md is produced (full system decomposed into 400–600 atomic tasks)
   - Before MASTER_MAP.md: all relevant Blueprints (.md) must exist and be reviewed
   - The harness (initializer.py + orchestrator.py) is built FIRST before Travel Assistant code — it is the build tool, not a deliverable
   - Vertical Slice Mock MVP was the proof-of-concept; it validates the approach but its blueprints may have been "hacked to make the test pass" (Cluster D Risk 6 — explicit warning from the source docs themselves)

2. The Patrick role in PRD v0.1.1 is described implicitly as "builds the system." The Word documents make this explicit and operational:
   - Patrick is the Architect — decides WHAT, not HOW
   - Patrick approves Blueprints, reviews security decisions, owns Go/No-Go gates
   - Patrick does not write code or run terminals
   - PRD v0.1.1 Phase tables show "Hours" estimates and "Model" columns — this is correct framing, but v0.2 should clarify these hours are Claude/Cursor agent hours, not Patrick hours
   - Source: Cluster D (Decision 3, Requirement 1), confirmed by Cluster E (Constraint 11)

**Implications for existing Phase 1 table (Section 9)**
Current table shows increments with "3–4h", "4–5h" estimates and "Opus/Sonnet" model columns. These estimates were written as if Patrick is the builder. They should be reframed as:
- "Build time": estimated wall-clock time for agentic coding session
- "Patrick time": review + approval only (much lower than build time)
- Explicit note: "Patrick approves Blueprints. Agents build. Patrick reviews output before phase gate."

**Darwinian League / Tournament model**
The SYSTEM_CONTEXT_v2.2 documents (Cluster B) describe a more advanced agentic coding model (ELO ranking, competitive agents, GEPA prompt evolution, Vault security). This is described as a meta-framework that Patrick developed independently. Whether this is the intended build methodology for the Travel Assistant itself is explicitly flagged as unresolved in Cluster B (Open Questions 3 and 4). Do NOT incorporate this into the PRD build phases until Patrick confirms intent. Flag as an open question (TA-I8 above).

---

*Change set complete. Next step: apply these changes to PRD v0.1.1 to produce PRD v0.2.*
*Total estimated new content: 4–5 sections, ~800–1,200 lines of PRD text.*
*Architecture Decision A5 remains the highest-priority Zone 1 decision. TA-T4 (Järvisydän IT engagement) is the highest-priority Zone 2 unblock.*
