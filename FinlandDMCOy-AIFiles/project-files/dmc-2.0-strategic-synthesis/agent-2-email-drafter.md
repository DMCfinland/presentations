## Email Drafter — Analysis

**Agent:** 2 — Email Drafter Analyzer
**Date:** 2026-02-22
**Sources consulted:** finland-dmc-prd-v3.txt, EMAIL-DRAFTER-DESIGN.md, session-1 patterns-identified.md, session-1 best-lines.md, session-2 patterns-identified.md

---

### 1. What It Is (in plain language)

Email Drafter is the workflow that removes the blank-page problem for Finland DMC staff responding to incoming client emails. A staff member receives an inquiry — from a luxury FIT agent in London, a group operator in Germany, a returning corporate client from Italy — and rather than constructing a reply from scratch, the system intercepts the incoming email, identifies the client from the Second Brain, classifies the task type (new inquiry, revision request, complaint, allocation release), selects the correct golden prompt, pulls in the right client history and rate card data, and generates a complete draft email with supporting context: suggested itinerary components ranked by historical win rate, a pricing block with commission exceptions flagged, and a progress checklist showing what the draft is still missing. The staff member reads the draft, makes edits if needed, and approves for send. The full system — from email arrival to draft ready for review — runs without staff initiating anything. The staff role shifts from author to editor and approver.

---

### 2. Data It Produces

Email Drafter generates and stores the following data types, per the EMAIL-DRAFTER-DESIGN.md system flow (Step 5 / NODE 8) and database schema:

**Drafts and sent email records**
- Email body text (versioned: v1, v2, v3 where feedback loops occur)
- Thread ID and email ID linking draft to originating inbound email
- TT itinerary URL (if proposal type, either pasted by staff in Stage 1 or auto-generated in Stage 2)
- Pricing block content: NET rates used, commission percentages applied, exceptions flagged

**Interaction log (written to `interactions` table in Supabase)**
- `client_id`, `contact_id`, `date`, `direction` (outbound), `task_type` (golden prompt ID)
- `staff_member` (who reviewed and approved)
- `outcome` (initially null; updated when staff marks Won/Lost/Still active)
- `proposal_value_eur` (if applicable)
- `tt_url` (if proposal)
- `conversion` (boolean, updated post-send)

**Feedback signals**
- Staff edit count per draft: "You changed the opening in 3 of your last 5 drafts" (EMAIL-DRAFTER-DESIGN.md, Lever 7)
- Regeneration count: how many feedback loops were needed before approval
- These are implicit quality signals stored per draft session

**Version sequences**
- Written to `version_sequences` table: `thread_id`, `version_number`, `components_added`, `components_removed`, `client_feedback_before`, `final_confirmed`
- This is the foundation of the itinerary win-rate engine

**Post-send conversion window tracking**
- System triggers a 48-hour alert if no client reply (EMAIL-DRAFTER-DESIGN.md, Lever 1: "48h after send: System reminds staff if no client reply")
- Alert state stored per interaction record

---

### 3. Data It Needs

**From Second Brain (Supabase database, NODE 2 — Second Brain Lookup)**

From the `clients` table:
- `company_name`, `domain`, `country`, `market_segment`
- `staff_owner` — determines which staff style template to use (Laura/Reeta/Liisa mode)
- `relationship_tier` — drives greeting register (Dear vs Hi) and emoji threshold
- `last_contact`, `booking_count`, `total_revenue_eur`

From the `contacts` table:
- `name`, `email`, `role`, `language_preference`, `communication_style`, `is_decision_maker`

From the `interactions` table:
- Last 5 significant interactions (EMAIL-DRAFTER-DESIGN.md, Lever 2: "3-year history → 5 most relevant signals shown")
- Prior `task_type` and `outcome` records — needed for urgency alerts ("pricing delay history — respond within 24h")
- Prior `proposal_value_eur` to set pricing context

From `components` table (for proposal task types):
- `win_rate` per component for matching `market_segment` and `destination`
- `removed_in_revision_rate`, `added_in_revision_rate`
- `has_commission`, `commission_pct`, `price_net_eur`
- `typical_day_position`

From `golden_prompts` table:
- `system_prompt`, `context_template` for the matched `task_type`
- `model_default`

**From rate_cards table (pricing block)**
- `service_name`, `price_net_eur`, `commission_pct`, `valid_from`, `valid_until`, `conditions`
- Commission exception rules: Solitary restaurant (0%), yoga sessions (0%), catering fees (0%), "Stay Longer"/"Early Bird" online offers (0%) — as documented in session-1 patterns-identified.md, Commission Rules section

**From Travel Tree (TT)**
- Stage 1: Staff pastes TT URL manually after building in TT (EMAIL-DRAFTER-DESIGN.md, TT Integration Stage 1)
- Stage 2 (future, pending TT API confirmation): n8n POSTs structured itinerary JSON to TT write API and receives URL automatically
- Component library: 1000+ components as JSON/CSV (requested but not yet confirmed)

**From inbound email parsing (NODE 1)**
- `sender_email`, `company_domain`, `subject`, `body`, `thread_id`
- Inbound urgency signals from session-2 patterns (e.g., Calendly link = same-day priority; trade fair context = window closing; corporate direct = no agent, higher margin)

**From Finland Travel Assistant (Product 5) — returning guests**
- Not yet applicable in B2B transition period. Products 5 and 6 generate B2C guest preference data (behavior, mood, activity choices). This data could in future enrich client profiles for operators who represent repeat guests, but no live data feed is specified in current design documents. This dependency is aspirational, not operational.

---

### 4. What It Gives to Other Products

**To Second Brain (Product 1)**

Every sent email produces an interaction record: client, date, task type, staff member, outcome, TT URL, proposal value. This is the primary mechanism by which Second Brain grows without manual CRM entry (EMAIL-DRAFTER-DESIGN.md, Step 5: "Second Brain updated: 'Responded to Nordic Luxury Feb 21, 2026 — new inquiry, 15 pax, Lake Saimaa'"). Over time:
- `conversion` outcomes feed component `win_rate` calculations
- Staff edit patterns improve golden prompt defaults ("You changed the opening in 3 of your last 5 drafts — should we update Laura's default?")
- Version sequences build the itinerary revision intelligence layer

The staff edit signal is particularly high-value: it reveals where AI drafts diverge from human judgment, which is exactly the data needed to improve golden prompts without formal feedback submission.

**To TT Itinerary Drafter (Product 4)**

Indirectly: sent proposals with TT URLs get outcome labels (Won/Lost). This outcome data, once in Second Brain, feeds the component win-rate calculations that Product 4 uses to auto-recommend itinerary components. Email Drafter is the upstream data source for Product 4's intelligence.

**To Finland Travel Assistant (Product 5)**

Not direct in current design. However, the behavioral patterns mined from B2B email communications — what luxury FIT agents request, what revisions clients ask for, what components get added in v2 — represent aggregate demand signal that could inform the Travel Assistant's recommendation logic. This would require a deliberate extraction and anonymization step not yet specified. No live data feed exists in current design.

**To future golden prompt improvement (self-reinforcing)**

The feedback loop within Email Drafter itself is its most important contribution to quality: staff ratings, regeneration count, edit patterns, and client reply rates all flow back through the Friday review cycle (PRD v3, Section 6.3) to update Project Knowledge files. This is the flywheel mechanism.

---

### 5. Infrastructure — Stack Verdict and PRD v3 Question

**Verdict: B — PRD v3 applies to Second Brain only. Email Drafter keeps its n8n/Supabase stack.**

The evidence is unambiguous on scope. PRD v3 opens with its change log: "Architecture reduced to 4–5 projects (not 10). One email project with 10 examples, not 10 email projects." Every decision table in PRD v3 refers to Claude Teams as a platform for staff-facing AI interaction — the Router, Client Communications, Proposals, and Pricing execution projects. The document describes a UI model where staff paste prompts, Claude responds in a conversation window, and M365 connector retrieves context dynamically. This is a human-in-the-loop conversation interface.

EMAIL-DRAFTER-DESIGN.md describes something structurally different: an automated workflow engine. Its core is an n8n pipeline (NODE 1 through NODE 8) that triggers on new email arrival, executes a Supabase lookup, runs Haiku task detection, assembles a context-rich prompt, calls Claude API (Sonnet or Opus depending on task), assembles a draft with modular blocks (TT, pricing, upsell, reasoning), and delivers to a staff review interface. The staff review interface is either a Teams message (Phase 2) or a custom Next.js UI (Phase 3). The Claude interaction is not a conversation — it is a single-shot API call within a larger orchestrated workflow.

PRD v3 explicitly uses "Claude Teams" as the data layer for what it calls Second Brain: Teams channels (#ai-feedback, #client-intel, #supplier-notes) serve as structured data sinks, with Claude searching them via M365 connector on Friday (PRD v3, Section 5.3). Email Drafter-DESIGN.md's Second Brain is a Supabase PostgreSQL database with a fully specified schema (clients, contacts, interactions, components, itineraries, version_sequences, suppliers, rate_cards, golden_prompts tables). These are two different conceptions of Second Brain — one lean (Teams channels + M365), one structured (relational database + vector search).

The resolution: PRD v3 represents a "this weekend" MVP path — Claude Projects set up quickly with minimal infrastructure, usable by staff in days. EMAIL-DRAFTER-DESIGN.md represents the full build — n8n + Supabase + custom UI — taking 4–12 weeks across three phases. PRD v3 does not cancel Email Drafter's stack; it provides an interim foundation while the full system is built. The PRD v3 Client Communications project IS Email Drafter running in its earliest form (staff manually paste emails, Claude drafts responses), and the EMAIL-DRAFTER-DESIGN.md n8n workflow is what that Claude Project becomes when automated.

The critical implication: the Supabase Second Brain (with its 8-table schema and win-rate calculation engine) is categorically more powerful than the Teams channels Second Brain. The transition from PRD v3 Teams-channel data sinks to Supabase structured storage is planned in EMAIL-DRAFTER-DESIGN.md Build Sequence ("Populate Supabase Second Brain database" — listed after mass email mining, not before). PRD v3 does not replace this — it precedes it.

---

### 6. GDPR Analysis

**Classification: B2B client data, lower sensitivity than B2C, but not exempt**

The data processed by Email Drafter includes:
- Contact names, email addresses, phone numbers, roles (stored in `contacts` table)
- Interaction history: who emailed whom, when, about what trip, at what budget
- Relationship signals: notes on frustration, urgency, preferences, communication style
- Staff assignment: which staff member owns each client relationship

This is personal data under GDPR (Article 4(1)) — named individuals in a business context are natural persons. Processing requires a legal basis. The most applicable is Article 6(1)(b) — processing necessary for the performance of a contract — since Email Drafter's core function is managing B2B contract relationships, or Article 6(1)(f) — legitimate interests — for relationship intelligence that does not fall under direct contract performance.

**Compared to Second Brain's obligations:** The obligations are substantially identical, since both systems process the same underlying contact and interaction data. The key distinction is infrastructure: PRD v3's Second Brain stores data in Microsoft Teams channels and SharePoint (within M365 ecosystem, covered by Microsoft's existing DPA and EU data processing commitments). EMAIL-DRAFTER-DESIGN.md's Supabase deployment on Hetzner VPS or Railway.app requires a separate GDPR compliance chain:

- Hetzner is a German provider — EU data residency is native, favorable for GDPR Article 44+ transfer restrictions
- Railway.app has EU regions but check whether the Finland DMC deployment is configured for EU hosting specifically
- Supabase requires a DPA; Supabase has a GDPR-compliant data processing agreement available
- n8n self-hosted eliminates a cloud DPA requirement for the orchestration layer

**Practical obligations unique to Email Drafter:**
- The `interactions` table stores email thread IDs and email body references. Depending on what "email_id" links to, this may constitute processing of email content, which requires the same legal basis as the M365 mailbox access already required
- The `version_sequences` table stores client feedback text between proposal versions ("client said X") — this is processed opinion/preference data, requires the same basis
- Outcome labels ("Won/Lost/Still active") are commercial judgments, not personal data in isolation — low sensitivity
- Staff edit patterns are internal operational data, not personal data

The MEMORY.md GDPR guidance applies: "DO: Use anonymized or summarized data in AI prompts. AI doesn't need raw names/contacts to do its job." For Email Drafter golden prompts, this means client names should be injected at the prompt assembly stage (NODE 4) with full context, but the golden prompt templates themselves should use placeholders, not hardcoded real names.

---

### 7. Shared Infrastructure Compatibility

**Verdict: Feasible, recommended, but requires deliberate schema partitioning.**

EMAIL-DRAFTER-DESIGN.md explicitly states the portfolio replication intent: "One platform, multiple companies. Finland DMC is the pilot. The same n8n backbone, golden prompts, and Second Brain architecture deploys to Järvisydän, M/S Marival, and other 1658 Holdings companies with different data and prompts." (Philosophy section). The replication estimate is "2–3 weeks once the Finland DMC platform is stable."

For Second Brain and Email Drafter to share a Supabase instance, the schema needs a `company_id` foreign key added to all tables. Current schema (EMAIL-DRAFTER-DESIGN.md, Second Brain Database Schema section) does not include a multi-tenancy field. Every table — `clients`, `contacts`, `interactions`, `components`, `itineraries`, `version_sequences`, `suppliers`, `rate_cards`, `golden_prompts` — would need `company_id` added to prevent cross-contamination.

**Schema conflicts:** None that cannot be resolved. The schema is generalized enough that Järvisydän's group sales interactions and Finland DMC's DMC proposal interactions share the same structural shape. `market_segment`, `destination`, `staff_owner` fields are all company-relative — they work for any company if `company_id` isolation is enforced.

**Row-Level Security (RLS):** Supabase supports PostgreSQL Row-Level Security natively. A policy enforcing `company_id = current_company_id` on all tables would prevent n8n workflows for one company from reading another company's data. This is the correct isolation mechanism.

**What would break without it:** If Second Brain data for Finland DMC and Järvisydän occupied the same tables without isolation, component win-rate calculations would mix DMC wilderness safari data with Järvisydän resort activity data — producing meaningless recommendations for both. This is the primary functional risk.

**Decision:** Share one Supabase instance with RLS-enforced `company_id` isolation. Do not run separate Supabase instances per company — the operational overhead (multiple connection strings, multiple backups, multiple pgvector indexes) is not justified at current scale. Add `company_id` to all tables at schema design time, not retrofitted after data is loaded.

---

### 8. Top 3 Questions for the Synthesis

**Q1: What is the migration path from PRD v3 (Claude Teams) to Email Drafter (n8n/Supabase)?**

PRD v3 establishes Claude Projects as the immediate working system. EMAIL-DRAFTER-DESIGN.md establishes n8n/Supabase as the mature system. These must coexist during the transition. The specific open question: when staff start using PRD v3's Client Communications project and posting feedback to #ai-feedback, where does that interaction data go? If it stays in Teams channels (the PRD v3 model), it never populates the Supabase `interactions` table that Email Drafter's win-rate engine depends on. Either a bridge is needed (periodic export from Teams to Supabase), or the PRD v3 feedback data is accepted as a throwaway dataset used only for prompt improvement — not for longitudinal client intelligence. This choice affects what value staff-generated data has during the 4–12 week build period.

**Q2: What is the staff review interface for Phase 2 (Teams message delivery)?**

EMAIL-DRAFTER-DESIGN.md describes Phase 2 delivery as "Teams message" (NODE 7). This is listed before the custom Retool and Next.js frontends. The design document does not specify what a Teams-delivered draft review looks like: is it a message card with Approve/Edit/Reject buttons (requires Teams adaptive card development), a plain text message with instructions to reply, or something else? The staff review interface determines how feedback data is captured and how edit loops work in Phase 2. If adaptive cards are required, Phase 2 build complexity increases substantially. If plain-text Teams messages are acceptable, Phase 2 can launch much faster. This needs a specific decision before Phase 2 build starts.

**Q3: How does the commission exception enforcement work in the pricing block?**

Session-1 patterns-identified.md documents commission exceptions: no commission on Solitary restaurant, yoga sessions, catering fees, "Stay Longer"/"Early Bird" online booking offers. EMAIL-DRAFTER-DESIGN.md shows the pricing block surfacing these exceptions with visual flags ("Solitary: NO commission"). The open question is how these exceptions are stored and applied programmatically. Option A: exceptions are hardcoded in the `rate_cards` table via `commission_pct = 0` for specific services, relying on correct data entry and maintenance. Option B: exceptions are rule-encoded in the golden prompt as explicit logic ("If the component name contains 'Solitary restaurant', always set commission to 0 and flag this to staff"), treating the AI as the exception-enforcer. Option A is reliable when data is clean but fails silently if rate cards are wrong. Option B is resilient to data quality issues but adds prompt complexity and may miss new exceptions not yet codified. The system currently cannot guarantee both options are in sync.

---

## Self-check

8 sections completed. Shortest section is Section 1 at 11 lines.

5 file references with section citations. 3 trade-offs with dual options stated (Section 5: Claude Teams vs n8n stack; Section 6: Hetzner vs Railway for EU hosting; Section 7: shared vs separate Supabase instances; Section 8 Q1: bridge vs throwaway for PRD v3 data; Section 8 Q3: hardcoded vs rule-encoded commission exceptions).

PRD v3 verdict on stack: confirmed n8n — PRD v3 covers Second Brain MVP only; Email Drafter keeps n8n/Supabase as the full build target. PRD v3 Client Communications project is Email Drafter in manual mode, not a replacement for it.

Assumptions validated: PRD v3 scope for Email Drafter checked in Section 5 — PRD v3 change log, Section 1 executive summary, and Section 5.3 (Teams channels as data sinks) reviewed and found to address Second Brain interim state only, not Email Drafter automation stack.

Context load: light (<100K). Five files read. No additional files consulted.

---

## BRIEFING FLAG FOR LEAD — Agent 5 Spawn

For Agent 5 spawn — confirmed Email Drafter stack: n8n (self-hosted, Hetzner VPS, ~€10/month) orchestrates an 8-node workflow triggered on new email arrival. Supabase (PostgreSQL + pgvector) stores Second Brain data across 8 tables. Claude API called directly (not through Teams): Haiku for task detection (~€0.001/email), Sonnet for most drafts (~€0.01), Opus for complaints/emergencies (~€0.05). PRD v3 Claude Teams is the interim manual-mode predecessor, not the production stack. Open question for Agent 5: schema needs `company_id` multi-tenancy field added to all 8 tables before first data load. Phase 2 delivery interface (Teams message vs Retool) is unresolved and affects build timeline.

## BRIEFING FLAG FOR LEAD — Agent 7 Spawn

For Agent 7 briefing — conversion/send signal data Email Drafter could contribute: Every sent proposal writes an interaction record with `proposal_value_eur`, `tt_url`, `task_type`, and eventually a `conversion` boolean and `outcome` label (Won/Lost/Still active) set by staff after client response. The version_sequences table additionally captures what components were added or removed between proposal versions, cross-referenced against final outcome — making it possible to identify exactly which itinerary changes correlate with booking confirmation, a conversion signal of exceptional quality unavailable in any commercial DMC tool.
