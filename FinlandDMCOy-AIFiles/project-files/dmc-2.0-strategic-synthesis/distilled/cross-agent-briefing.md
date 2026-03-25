# Cross-Agent Briefing
**Lead-authored | 2026-02-22 | For Agent 7 spawn prompt**
*Decision-relevant extracts from all 6 agents. NOT a synthesis — Patrick decides conflicts.*

---

## Agent 1 — Second Brain Analyzer

**Single most important conclusion:**
PRD v3 simplification is correct for the transition period (months 1–6) but will not scale to OTA-class volume. Build on Claude Teams now, plan migration at ~200 clients or first GDPR data subject rights request. The migration threshold is concrete and time-bound, not hypothetical.

**Top 3 Questions (verbatim):**
1. How does Second Brain maintain persistent, updatable client records without a database? Option A: Patrick manually curates a client-profiles.txt file updated on Fridays. Option B: Retain SharePoint Lists layer for structured storage only, with Claude Teams handling AI reasoning. Blocking for build sequence and GDPR compliance posture.
2. Does Anthropic's Claude Teams DPA satisfy GDPR Article 28 and Article 44–46 for an EU company? Option A: Verify Anthropic DPA and SCCs, proceed with Claude Teams. Option B: Use Azure Bedrock Claude with eu-west for personal data processing. Blocking for deployment with any named contact data.
3. When does the JK departure orphan problem become a system failure? Option A: Manually reassign all 130 JK accounts before launch (~3-4 hours). Option B: Build "no owner" queue state into schema, surface as a queue rather than silent failure. Blocking for system correctness from Day 1.

**Biggest concern about the transition model (2 sentences):**
Second Brain in PRD v3 state has no persistent updatable records — when a key staff member leaves and takes their in-context knowledge, the system loses exactly the institutional memory it was designed to protect. The JK departure proves this is not hypothetical: 130 accounts still show a departed staff member as owner 6 months after she left, with €633K in orphaned relationships and no automated detection.

---

## Agent 2 — Email Drafter Analyzer

**Single most important conclusion:**
PRD v3 applies to Second Brain only (Verdict B confirmed). Email Drafter keeps n8n/Supabase as production stack. PRD v3 Client Communications project is Email Drafter in its earliest manual form — it precedes the n8n automation, does not replace it. The two systems are sequential, not competing.

**Top 3 Questions (verbatim):**
1. What is the migration path from PRD v3 (Claude Teams) to Email Drafter (n8n/Supabase)? If staff generate feedback in Teams channels during the 4–12 week build period, does that interaction data populate the Supabase interactions table (via bridge) or is it a throwaway dataset? This choice affects the long-term value of early staff behavior data.
2. What is the staff review interface for Phase 2 (Teams message delivery)? Adaptive cards vs plain text determines Phase 2 build complexity. Adaptive cards require Teams bot development. Plain text allows faster Phase 2 launch. Must be decided before Phase 2 build starts.
3. How does the commission exception enforcement work? Option A: Hardcoded in rate_cards (reliable when data is clean, fails silently if wrong). Option B: Rule-encoded in golden prompts (resilient to data quality issues, adds prompt complexity). The two options cannot both be authoritative without creating conflicts.

**Biggest concern about the transition model (2 sentences):**
Email Drafter's value depends entirely on staff actually using it and rating drafts — the cultural shift from author to editor+approver requires deliberate change management that no technical architecture can substitute for. If staff continue writing proposals from scratch out of habit or distrust, the version_sequences data never builds and the proposal win-rate engine never improves — the system remains permanently at Phase 1 capability regardless of how much infrastructure is built.

---

## Agent 3 — Travel Assistant Vision Analyzer

**Single most important conclusion:**
The revenue model shift is structural, not incremental: 15% commission × OTA-scale volume eliminates the linear relationship between staff headcount and revenue. At 20 tenants × 3,000 guests × €150 AI-assisted spend × 15%, platform commission revenue reaches €1,350,000/year. The structural shift requires Finland DMC to care about guest NPS as its core business metric, not operator proposal win rate.

**Top 3 Questions (verbatim):**
1. Who is legally liable when the AI gives dangerous advice based on a Safety Bulletin the AI judged current but wasn't? No current document defines the liability chain between Finland DMC (platform), Järvisydän (resort and data controller), and the guest. This is a blocking pre-go-live question, not a future consideration.
2. What is the minimum commission-bearing booking volume that makes the platform financially sustainable per tenant? No source document includes a platform operating cost model. Without this, there is no rational basis for setting the Järvisydän commission split, no minimum viable tenant size, and no pricing model for future white-label clients.
3. What prevents a resort from taking the platform's data and building its own solution after Year 1? Finland DMC's moat is the aggregate cross-resort dataset and trained recommendation weights — neither of which an individual tenant can take. But the contractual terms protecting this must be defined before Järvisydän signs the DPA.

**Biggest concern about the transition model (2 sentences):**
The transition model requires one Finland DMC staff member to monitor all AI guest conversations, but at 1,000+ simultaneous guests across multiple resort tenants during peak season, part-time monitoring becomes a full-time job — creating a new linear constraint the automation was supposed to eliminate. The platform may achieve its goal of removing staff from proposal writing while simultaneously trapping them in continuous AI conversation supervision, with no clear trigger for when monitoring intensity can be reduced.

---

## Agent 4 — Travel Assistant Technical Architect

**Single most important conclusion:**
Staff Dashboard (BP_08) is not started, rated XL complexity, and is a hard go-live blocker for the B2C Traveler PWA (BP_11). These two products must be built in parallel. BP_08's completion date — not BP_11's — determines the Järvisydän launch date. No Järvisydän IT contact has been made yet, which is the longest lead-time item on the critical path.

**Top 3 Questions (verbatim):**
1. Oracle Opera API scope at Järvisydän: what does it actually expose for availability and booking? If Opera does not expose a REST API for the operations Booker Agent needs (common with older Opera versions), the only fallback is email-based Type B booking for all Järvisydän products — which eliminates real-time availability confirmation and degrades the guest experience. This must be answered before Booker Agent architecture is finalized.
2. Payment processor (Adyen vs Stripe Connect): the choice has Phase 2 virtual card consequences. If Adyen Issuing is chosen (aligning with Järvisydän's existing Adyen relationship), the MVP payment integration should be Adyen — not Stripe — to avoid a migration when Phase 2 begins. Decide before Phase 2 architecture.
3. Who owns BP_08 build and what is its timeline relative to B2C go-live? BP_08 is rated XL (Traffic Light, Whisper, Takeover, God Mode, FIRE RED, Dead Man's Switch, SOS, Teach buttons — a full product in its own right). The synthesis must explicitly sequence BP_08 relative to BP_11 and set a hard dependency gate.

**Biggest concern about the transition model (2 sentences):**
BP_08 Staff Dashboard is the central transition product and it has not been started — the entire 80/90-10/20 split between AI automation and human oversight cannot exist without it. Building the B2C Traveler PWA (BP_11) without a functioning Staff Dashboard is not a phased rollout strategy; it is deploying an AI assistant with no human safety net, which is categorically different from the transition model Patrick has approved.

---

## Agent 5 — Integration Architect

**Single most important conclusion:**
n8n (Zone 1 backbone) and Azure Event Grid (Zone 2 backbone) with no shared integration middleware. The clean zone separation is not a design preference — it is the GDPR Article 5(1)(b) purpose limitation principle made architectural. Two permitted data crossings only: anonymized booking source metadata (daily batch) and pseudonymized guest satisfaction via B2B Partner Dashboard.

**Top 3 Questions (verbatim):**
1. Is there a viable path to Staff Dashboard (BP_08) being ready for Järvisydän launch, given it is XL complexity and not started? If BP_08 cannot be delivered in parallel with BP_11, the B2C launch date is set by BP_08 completion, not BP_11. The synthesis must confront this directly.
2. What is the Järvisydän IT contact and Oracle Opera API engagement plan? Five blockers all require Järvisydän IT cooperation. Every week without contact is a week of Azure infrastructure built without knowing if Booker Agent BP_06 will work. The synthesis must identify who initiates contact and what the architecture fallback is if Oracle Opera API access takes months.
3. What is the Supabase State A → State B migration sequencing, and does it block anything? 107 client profiles with zero contact names means Email Drafter personalization is blind on the most valuable dimension. Three sequential prerequisites: (a) Anthropic DPA verified, (b) contact data imported, (c) company_id added to all 9 Supabase tables.

**Biggest concern about the transition model (2 sentences):**
The transition model assumes Finland DMC staff can intervene in escalated guest conversations within 30 minutes — but if Järvisydän staff (not Finland DMC staff) are also managing check-in desks, restaurant bookings, and activity coordination, the 30-minute SLA will be violated regularly and the guest experience degradation will be attributed to the AI platform. The transition works operationally only if Järvisydän commits a staff member to dashboard monitoring as a primary duty, not a secondary responsibility added to an existing full workload.

---

## Agent 6 — Database Architect

**Single most important conclusion:**
Option C Federated is the recommended architecture. Physical zone separation enforces the GDPR Article 5(1)(b) purpose limitation principle at infrastructure level at zero additional cost vs Option A (current architecture), while Option B (Unified Azure) increases cost by €150–400/month and increases GDPR risk with no offsetting benefit. Supabase needs a 9th table (booking_source_metadata) isolated by RLS for the daily boundary-crossing batch.

**Top 3 Questions (verbatim):**
1. Adyen vs Stripe Connect: GDPR preference is Adyen (EU-headquartered, stronger GDPR track record, no Article 46 SCC requirement). But Adyen has higher minimum volume thresholds and more complex onboarding. This is blocking the Shadow Ledger webhook schema design. Cannot remain open into Phase 2 build.
2. Anthropic DPA + Article 46 SCCs for Second Brain State A: Named B2B contact PII cannot enter Claude Teams until the Anthropic DPA is verified for GDPR Article 28 compliance and Article 46 SCCs are executed. The migration threshold to State B may arrive before the legal paperwork is complete. Is this a legal gap to close now or a deliberate delay decision?
3. DPIA scope and ownership: A Finnish GDPR-qualified legal counsel must be identified and engaged. The DPIA covers both B2B Second Brain (automated profiling — Article 35(3)(a)) and B2C Travel Assistant (systematic monitoring — Article 35(3)(c)). The DPIA alone may take 6–8 weeks and could result in required architectural changes before go-live.

**Biggest concern about the transition model (2 sentences):**
The DPIA is a legal prerequisite for go-live with named personal data in both the B2B Second Brain and the B2C Travel Assistant, but no Finnish GDPR-qualified legal counsel has been identified, engaged, or allocated budget — and a first-of-its-kind AI behavioral profiling system in Finnish hospitality law has no precedent to reference. A DPIA that reveals required architectural changes (such as excluding certain Mood Matrix features or limiting Second Brain scope) 6 weeks before planned launch would force a rebuild that delays the transition model's start date by months.

---

## All Conflicts Identified — Do NOT Resolve (Patrick decides)

| # | Conflict | Agent A Position | Agent B Position | Status |
|---|---|---|---|---|
| 1 | Second Brain storage architecture | A1: PRD v3 Teams channels = correct interim | A2: Supabase = production target, PRD v3 precedes it | RESOLVED BY AGENTS — sequential not competing |
| 2 | Zone 1/Zone 2 data boundary | A1: nothing from Zone 2 to Zone 1 in transition | A3: Shadow Ledger booking metadata flows Z2→Z1 | RESOLVED BY A5 — anonymized operator metadata only, no guest PII |
| 3 | Mood Matrix Article 9 | A3: flagged as health data risk | A4: documented schema without flagging GDPR concern | RESOLVED BY A5/A6 — exclude Needs_Accessibility at launch |
| 4 | Payment processor | A4+A5+A6: Adyen preferred (GDPR + existing Järvisydän relationship) | No counterposition | OPEN — Patrick must decide before Phase 2 architecture |
| 5 | Staff Dashboard build priority | A4+A5: BP_08 is go-live blocker, XL complexity | No counterposition — all agents agree | OPEN — who builds it, on what timeline? |
| 6 | DPIA ownership and timing | A6: 6-8 weeks, blocks go-live | No counterposition | OPEN — who commissions, when, budget? |

---

## Convergence: What All 6 Agents Agree On

1. **Staff Dashboard (BP_08) must be built before B2C go-live.** Not optional, not deferrable. Every agent that touched this question reached the same conclusion independently.
2. **Järvisydän IT contact is the longest lead-time item.** Oracle Opera API credentials, BookVisit catalog feed, webhook configuration, network path, DPA — all blocked until Finland DMC initiates contact.
3. **Supabase schema must have company_id on all 9 tables before first data load.** Retrofitting is painful and risks data integrity.
4. **DPIA is mandatory.** Multiple agents (A3, A5, A6) independently reached this conclusion. Not a future consideration — a go-live legal prerequisite.
5. **Zone 1 and Zone 2 must not share infrastructure.** Option C Federated is the right architecture. No agent proposed shared infrastructure.

---

*End of cross-agent-briefing.md | Lead: team-lead@dmc-synthesis | 2026-02-22*
