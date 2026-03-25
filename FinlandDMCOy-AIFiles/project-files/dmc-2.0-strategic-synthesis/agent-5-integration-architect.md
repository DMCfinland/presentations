## Integration Architecture Analysis

**Agent 5 — Integration Architect | 2026-02-22**
*Sources: wave1-cross-brief.md, finland-dmc-prd-v3.txt, traveltree-api-status.md*

---

### 1. The Integration Map (text diagram)

```
═══════════════════════════════════════════════════════════════════════════════
  ZONE 1 — B2B (Hetzner VPS + Claude Teams)     │  ZONE 2 — B2C (Azure North Europe)
═══════════════════════════════════════════════════════════════════════════════

  ┌──────────────────────────────────────┐       │  ┌──────────────────────────────┐
  │  P1: SECOND BRAIN                    │       │  │  P5: FINLAND TRAVEL ASSISTANT│
  │                                      │       │  │  (Azure Functions + Event    │
  │  STATE A: Claude Teams (now)         │       │  │   Grid + GPT-4o ZDR +        │
  │  • Teams channels as data sinks      │       │  │   Cosmos DB + Azure SQL +    │
  │  • M365 connector (read-only)        │       │  │   Azure AI Search)           │
  │  • No query API — manual M365 search │       │  │                              │
  │                                      │       │  │  INBOUND:                    │
  │  STATE B: Supabase (production)      │       │  │  POST /webhook/booking ←─────┼──── BookVisit (BLOCKER)
  │  • PostgreSQL + pgvector             │       │  │  GET  /welcome?token={jwt}   │
  │  • 8 tables (needs company_id)       │       │  │  POST /api/agent/process     │
  │  • query API via n8n NODE 2          │       │  │                              │
  └──────────────────────────────────────┘       │  │  OUTBOUND:                   │
       │ State A: manual staff query             │  │  → Oracle Opera ──────────── BLOCKER
       │ State B: n8n NODE 2 pull (on-demand)   │  │  → FMI weather API (hourly)  │
       │                                        │  │  → Kp-index aurora API       │
       ▼                                        │  │  → Adyen/Stripe Connect      │
  ┌──────────────────────────────────────┐       │  │    (UNRESOLVED)              │
  │  P2: EMAIL DRAFTER                   │       │  │  → SendGrid/SMS (Magic Link) │
  │  (n8n, Hetzner VPS)                  │       │  │  → Slack/Teams webhooks      │
  │                                      │       │  └──────────────────────────────┘
  │  • 8-node n8n pipeline               │       │       │                │
  │  • Claude API (Haiku/Sonnet/Opus)    │ ◄─────┤       │ booking        │ staff
  │  • Supabase (shared with P1 State B) │  booking source metadata       │ priority
  │                                      │  (anonymous, no guest PII)     │ queue
  │  TRIGGERS:                           │       │       │                │
  │  Email arrival → n8n node 1          │       │  ┌────▼───────────────▼─────────┐
  │                                      │       │  │  P3: STAFF DASHBOARD         │
  │  CONSUMES FROM P1:                   │       │  │  (Azure — NOT STARTED)       │
  │  • interaction_records (24-month)    │       │  │                              │
  │  • client tier, preferred dest       │       │  │  Traffic Light, Whisper,     │
  │  • RelationshipHealthScore           │       │  │  Takeover, God Mode,         │
  │  State A: staff pastes context       │       │  │  FIRE RED, Safety Net        │
  │  State B: automatic n8n NODE 2 pull  │       │  │                              │
  └──────────────────────────────────────┘       │  │  Staff-facing endpoints:     │
       │                                        │  │  POST /staff/whisper         │
       │ proposal data →                        │  │  POST /staff/takeover        │
       │ (State B only)                         │  │  POST /staff/teach           │
       ▼                                        │  │  POST /staff/god-mode        │
  ┌──────────────────────────────────────┐       │  │  POST /staff/fire-red        │
  │  P4: TT ITINERARY DRAFTER            │       │  └──────────────────────────────┘
  │  (Travel Tree Pro — API)             │       │
  │                                      │       │  ┌──────────────────────────────┐
  │  T1: Create itinerary via API — YES  │       │  │  P6: JÄRVISYDÄN TA           │
  │     (free, needs enabling now)       │       │  │  (First tenant of P5)        │
  │  T2: Read itinerary content — YES    │       │  │                              │
  │     (free, needs enabling now)       │       │  │  • Tenant config in Azure SQL│
  │  T3: Component library export —      │       │  │  • Booking source: BookVisit │
  │     PAID, scope TBD, needs call      │       │  │    + Järvisydän online store  │
  │                                      │       │  │  • DPA with Finland DMC      │
  │  CONSUMES FROM P1:                   │       │  │    required before launch    │
  │  • preferred destination defaults    │       │  └──────────────────────────────┘
  │  • group size (from client records)  │
  │  State A: staff pastes from M365     │
  │  State B: automatic n8n NODE 2 pull  │
  └──────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════════
  B2B PARTNER INTERFACE (crosses boundary — requires Article 28 DPA)
  GET /b2b/customers — travel agencies view guest satisfaction + upsell revenue
  Direction: PULL (agency pulls) | Frequency: on-demand | Legal: Article 28
═══════════════════════════════════════════════════════════════════════════════
```

**Legend:**
- `→` Push (producer initiates)
- `←` Pull (consumer requests)
- `BLOCKER` = integration cannot proceed without external dependency resolved
- `UNRESOLVED` = internal decision pending, not external dependency

---

### 2. The Six Integration Seams — Detailed

**Seam 1: Second Brain (P1) → Email Drafter (P2)**
- Data flowing: interaction_records (24-month history), RelationshipHealthScore (1–10 weekly), client_tier, preferred_destination, staff_owner, margin_avg
- Producer: P1 (Second Brain)
- Consumer: P2 (Email Drafter n8n pipeline)
- Push vs pull: PULL (n8n NODE 2 queries Supabase on email arrival)
- Criticality: BLOCKING for personalization — without it, P2 produces generic proposals
- State A gap: In PRD v3 Claude Teams state, there is no query API. Staff manually pastes M365 search results into the Email Drafter prompt. This is the entire integration in State A — a human copy-paste bridge.
- State B: n8n NODE 2 lookup replaces the manual step. Automated pull on email arrival trigger.
- **Transition point:** Migration to State B is gated on Supabase schema loaded with `company_id` added to all 8 tables before first data load. This is a Day 1 data prerequisite, not a future cleanup.

**Seam 2: Second Brain (P1) → TT Itinerary Drafter (P4)**
- Data flowing: preferred destination, group size defaults, client segment (from client_records)
- Producer: P1
- Consumer: P4 (TT API integration)
- Push vs pull: PULL (P4 queries P1 on itinerary generation request)
- Criticality: nice-to-have in State A (staff knows client context); blocking for automation in State B
- State A: staff manually recalls and enters client context when using TT
- State B: n8n NODE 2 pre-populates TT API call parameters with client defaults

**Seam 3: TT (external) → Email Drafter (P2) and Travel Assistant (P5)**
- Data flowing: itinerary links (T1/T2 confirmed), component library (T3 — paid, scope TBD)
- Producer: Travel Tree API
- Consumer: P2 (proposal generation uses TT links), P5 (Commercial Shelf product catalog)
- Push vs pull: PUSH for T1 create (Finland DMC pushes data → gets link back); PULL for T2 read
- Criticality for P2: Email Drafter can embed TT links in proposals — T1 and T2 are free and available now, needs enabling. Unblocked.
- Criticality for P5: Commercial Shelf is empty without BookVisit product catalog feed AND TT component library (T3). T3 scope unknown — needs call with Ihor. This is a PARTIAL BLOCKER for P5 Chef scoring.
- Frequency: on-demand (per proposal / per guest request)

**Seam 4: BookVisit → Travel Assistant (P5)**
- Data flowing: booking webhook event (HMAC-signed), product catalog feed
- Direction: BookVisit PUSHES booking events to `POST /webhook/booking`
- Criticality: BLOCKER — machine-readable catalog feed not yet provided; without it, Commercial Shelf is empty and Chef cannot score products
- Frequency: booking events are push/real-time; catalog feed is periodic (likely daily)

**Seam 5: Travel Assistant (P5) → Staff Dashboard (P3)**
- Data flowing: Staff Priority Queue (conversation_id, urgency_score, assigned_staff), FIRE RED alerts, SLA breach notifications
- Direction: P5 PUSHES to P3 via Cosmos DB (live queue) and Slack/Teams webhooks (emergency)
- Criticality: HARD BLOCKER for B2C go-live — P3 not started (BP_08 XL complexity). Traveler PWA (BP_11) cannot launch without P3. Staff monitoring of 80–90% AI conversations requires P3 to be in place.
- Frequency: real-time (urgency scoring on each conversation turn)

**Seam 6: Shadow Ledger (P5) → Second Brain (P1)**
- Data flowing: booking source metadata (operator reference: which B2B partner sent the guest)
- Direction: P5 PUSHES aggregate/anonymized metadata to P1
- Criticality: nice-to-have — identifies which B2B operators (travel agencies, tour operators) generate high-value guests
- Legal constraint: ONLY booking source metadata (operator_id, revenue_tier classification) may cross Zone 1/Zone 2 boundary. Named guest data, Mood Matrix, and behavioral logs must not cross. See Section 4.
- Frequency: daily batch (not real-time)

**Critical gap flagged against A1:** A1 confirms 107 client profiles have zero contact names. P2 Email Drafter personalization (Seam 1) specifically requires contact names for "your Aurora series last January" references to work. This gap blocks the highest-value personalization in Flagship client proposals (AHI Travel, Wikinger Reisen). Contact data import is Day 1 work, not optional.

---

### 3. Travel Tree as the Central Dependency

Citing `traveltree-api-status.md` (WhatsApp answers from Ihor Kucher, 2026-02-21):

**T1 — Create itinerary via API (send data → get link):** YES, free setup, available NOW — just needs enabling. Finland DMC already on Pro plan (auto-upgraded, price locked January 2026). This unblocks the core Email Drafter → TT workflow immediately. Email Drafter (P2) can generate TT itinerary links programmatically in proposals.

**T2 — Read itinerary content via API:** YES, can build, free setup, available NOW — just needs enabling. This enables Travel Assistant (P5) to retrieve current itinerary state (for guest context in conversations) and Staff Dashboard (P3) to display live itinerary details. No blocker.

**T3 — Export component library as data:** Paid feature, scope TBD, needs call with Ihor. This is the key dependency for pre-populating Commercial Shelf (P5 Chef scoring) with TT products. Until T3 scope and cost are resolved, the Commercial Shelf must be seeded manually or via BookVisit catalog alone. TT Itinerary Drafter (P4) can still generate itineraries using T1/T2 without T3, but without bulk component export, P4 cannot use component library data programmatically — staff must select components manually in TT Pro interface.

**Downstream impact by product:**
- P2 Email Drafter: UNBLOCKED — T1 and T2 sufficient for proposal link generation
- P4 TT Itinerary Drafter: PARTIALLY BLOCKED — T1/T2 enable create and read; T3 blocks automated component pre-selection. Manual component selection remains feasible. Recommend mining TT links from email archive (Phase 1 in traveltree-api-status.md) before booking T3 call — understand actual usage patterns first.
- P5 Travel Assistant: PARTIALLY BLOCKED on TT side — T3 needed for Commercial Shelf TT product data. BookVisit catalog is the parallel path; TT component export is additive. The bigger P5 blocker is Oracle Opera API scope (unknown) and BookVisit catalog feed (not yet provided).

**Open item from traveltree-api-status.md:** Q6 (does TT send notifications when client views itinerary?) is unanswered. This matters for P3 Staff Dashboard engagement tracking and P2 follow-up automation. Must be asked on TT call.

---

### 4. The B2B / B2C Data Boundary

The legal boundary is not a technical line — it is a purpose limitation line under GDPR Article 5(1)(b).

**Zone 1 data (B2B — what it is and its legal basis):**
- Client company records: revenue tier, preferred destination, staff_owner, margin, commission rates
- Contact records: named individuals at B2B partner companies (travel agencies, tour operators)
- Interaction records: 24-month history of communication with B2B partners
- RelationshipHealthScore: account health indicators derived from B2B relationship data
- Legal basis: Article 6(1)(b) (contract performance with B2B clients) and Article 6(1)(f) (legitimate interests in business relationship management)
- Retention: 24-month rolling window (confirmed in Second Brain system summary, per A1)
- Controller: Finland DMC Oy

**Zone 2 data (B2C — what it is and its legal basis):**
- Guest profiles: name, language, trip details, booked items (Context Briefcase)
- Mood Matrix: 8 behavioral dimensions (energy, hunger, social_battery, luxury_affinity, nature_rawness, safety_need, foodie_focus, price_sensitivity) + tags
- Behavioral logs: conversation events, product impressions, conversion signals (Data Lake Gen2, SHA-256 hashed user_id)
- Booking transactions: Shadow Ledger entries with guest user_id, booking_ref, amounts
- Legal basis: Article 6(1)(b) (contract performance — guest has booked a stay) for transaction data; Article 6(1)(a) (consent) for Mood Matrix behavioral profiling beyond what is strictly necessary for service delivery
- Storage: Azure North Europe, EU-resident
- Controller: Finland DMC Oy (platform owner) / Processor for Järvisydän Oy guest data under Article 28 DPA

**What can legally cross the boundary:**

1. **Booking source metadata (Shadow Ledger → Second Brain):** The operator_id (which B2B partner referred the guest) and aggregate revenue classification (high-value / standard) can cross from Zone 2 to Zone 1. Condition: must be anonymized or aggregated — no guest_id, no name, no behavioral data crosses. Legal basis: Article 6(1)(f) legitimate interest (understanding which B2B partners generate high-value bookings is a legitimate business intelligence purpose). This must be documented in the Article 30 Record of Processing Activities.

2. **B2B Partner Dashboard (`GET /b2b/customers`):** Travel agencies can view their referred customers' satisfaction scores and upsell revenue. This crosses Zone 2 guest data to Zone 1 B2B partners. Legal constraints:
   - The travel agency viewing its customer's data is acting as a data controller for that customer relationship. Finland DMC is sharing that guest's data with the referring agency.
   - Requires: (a) transparent disclosure to guests under Article 13 that satisfaction data may be shared with the referring travel agency; (b) Article 28 Data Processing Agreement between Finland DMC and each travel agency acting as a data processor accessing the dashboard; (c) if the travel agency is itself a controller (not just a processor), this is a third-party data transfer requiring legal basis.
   - Minimum viable approach: Guest-level satisfaction scores must be pseudonymized or aggregated at the cohort level before reaching the B2B dashboard unless explicit Article 6(1)(a) consent is obtained from each guest at booking time disclosing this specific sharing.

3. **Nothing else crosses.** Mood Matrix dimensions, conversation logs, Context Briefcase contents, and raw behavioral data must not leave Zone 2. Zone 1 personalization (Email Drafter) uses B2B contact history, not guest behavioral data.

**Mood Matrix — Article 9 health data risk (flagged by A3):**
The "Needs_Accessibility" tag in the Mood Matrix schema is health-adjacent. Under GDPR Article 9(1), processing of "data concerning health" of a natural person is prohibited unless an Article 9(2) exception applies. Disability and accessibility needs are explicitly health-adjacent under Article 4(15) definition of health data ("physical or mental health").

Consequences if "Needs_Accessibility" = Article 9 health data:
- Article 9(2)(a): Requires explicit, specific, informed consent (separate from general Terms of Service acceptance — a distinct consent act)
- Article 35(3)(b): Mandatory Data Protection Impact Assessment (DPIA) for large-scale processing of Article 9 data — this triggers even for Järvisydän's first deployment
- The DPIA is also independently mandatory under Article 35(3)(c) for systematic monitoring of individuals in a publicly accessible area (the resort AI assistant monitoring all guest interactions)

**Recommendation:** Do not tag "Needs_Accessibility" in the Mood Matrix at launch. Collect accessibility requirements through a separate, explicit channel (e.g., pre-arrival form with Article 9(2)(a) consent), outside the behavioral profiling system. If Mood Matrix behavioral signals happen to correlate with accessibility needs, ensure the data science layer does not derive or infer Article 9 categories from Zone 2 behavioral data. The Data Lake Gen2 "event_type" logs must not record inferred health categories.

**GDPR Articles cited in this section:** 4(15), 5(1)(b), 6(1)(a), 6(1)(b), 6(1)(f), 9(1), 9(2)(a), 9(2)(b), 13, 28, 30, 35(3)(b), 35(3)(c).

---

### 5. Architecture Decisions Still Blocking Integration

| Blocking Decision | What It Blocks | Why |
|---|---|---|
| Oracle Opera API scope unknown | P5 Booker Agent (BP_06) cannot be architected | Cannot design reservation creation flow without knowing API endpoint structure, auth method, rate limits, or whether on-prem network path to Azure is required |
| BookVisit product catalog feed format unknown | P5 Commercial Shelf is empty | Chef Agent cannot score products that don't exist in Azure AI Search index |
| Adyen vs Stripe Connect unresolved | P5 Phase 2 virtual card feature and revenue reconciliation | Each has different webhook structure, settlement timing, and virtual card issuance API — integration design diverges at the payment layer |
| Staff Dashboard (BP_08) not started | P5/P6 B2C go-live | Hard safety blocker — FIRE RED and Takeover cannot exist without BP_08; Traveler PWA (BP_11) cannot launch without it |
| No Järvisydän IT contact yet | All P6 Azure integration | Oracle Opera API credentials, BookVisit webhook, booking store integration — all require Järvisydän IT cooperation |
| TT component library (T3) cost and scope unknown | P4 automated component selection, P5 Commercial Shelf TT product data | Cannot plan TT-sourced product ingestion pipeline without T3 answer |
| Phase 2 Email Drafter delivery interface (Teams adaptive cards vs plain text) | P2 build timeline | Adaptive cards require different n8n node design than plain text; choice affects build scope |
| Anthropic Claude Teams — no EU data residency | P1 State A cannot hold contact PII legally | Article 44–46 transfer mechanism must be established before any named contact data enters Claude Teams (A1 finding). Blocks Second Brain from being a functional contact intelligence layer until DPA is verified. |
| `company_id` not yet added to Supabase schema | P1 → P2 Seam 1 (State B) | Retrofitting multi-tenancy after data load is painful — this must be done before any data is imported |

---

### 6. The Minimum Viable Integration

For all 6 products to function simultaneously at minimum viable level:

**What is manual (State A, today):**
- P1 → P2 seam: Staff manually searches M365 (via Claude Teams M365 connector), copies relevant client context, pastes into Email Drafter prompt. One human copy-paste step per proposal.
- P1 → P4 seam: Staff manually knows client preferences, enters group size and destination when using TT Pro interface.
- P4 TT integration: Enable T1 and T2 APIs (free, contact Ihor). Staff triggers TT itinerary creation from Email Drafter workflow. Paste TT link into proposal draft.
- P3 Staff Dashboard: Cannot be minimum viable — it is a hard go-live blocker. Build BP_08 in parallel with BP_11 (Traveler PWA). No workaround.
- Shadow Ledger → Second Brain metadata flow: batch daily export, manual review acceptable at Järvisydän launch volume.

**What is automated (minimum viable for B2C):**
- P5 booking webhook (`POST /webhook/booking` from BookVisit) triggers Magic Link generation and guest onboarding automatically
- P5 chat endpoint (`POST /api/agent/process`) handles guest conversations autonomously
- P5 weather and aurora APIs (FMI + Kp-index) integrate automatically — no dependencies on Finland DMC or Järvisydän
- P5 SendGrid/SMS delivers Magic Link automatically
- P5 → P3 Slack/Teams alert webhooks for FIRE RED and SLA breaches

**What must be deferred (not minimum viable):**
- Oracle Opera reservation creation (P5 Booker Agent BP_06) — defer until API credentials and scope confirmed
- B2B Partner Dashboard (`GET /b2b/customers`) — defer until Article 13 guest disclosure and Article 28 agency DPA are in place
- Mood Matrix accessibility tag — exclude at launch (Article 9 risk)
- n8n automated P1 → P2 query (State B) — requires Supabase schema loaded with company_id and contact data imported first

---

### 7. PRD v3 Simplification Impact on Integration

PRD v3's Claude Teams architecture has no outbound webhook or API capability. This is not a limitation to design around — it is the correct architectural choice for the B2B transition period.

**What Claude Teams can do for integration:**
- M365 connector provides read-only search across Outlook shared mailbox, SharePoint, and Teams channels — this IS the query API for State A. It is manual (staff-initiated in conversation), not programmatic.
- #client-intel, #supplier-notes, and #ai-feedback channels serve as structured data sinks that are M365-searchable — this creates a lightweight intelligence layer with zero infrastructure cost.
- Claude Teams cannot push data anywhere. It has no outbound webhooks, no database write access, no event triggers. Every integration FROM Claude Teams requires staff to manually extract output and paste it elsewhere.

**B2B / B2C becomes a clean manual handoff in State A:**
Zone 1 (B2B) operates entirely within Claude Teams + M365 ecosystem. Zone 2 (B2C) operates entirely within Azure. There is no programmatic link between them in State A — and this is architecturally correct. The Staff Dashboard (P3) bridges Zone 1 staff into Zone 2 conversations via explicit staff endpoints (Whisper, Takeover), but that bridge runs from Azure P3 to Azure P5, not from Claude Teams to Azure.

The PRD v3 simplification eliminates 12–16 weeks of infrastructure build for B2B tooling and removes the GDPR exposure risk of automated pipeline processing of B2B contact PII. The trade-off is that P1 → P2 and P1 → P4 seams are human-mediated in State A. This is acceptable for current 5-person DMC volume (estimated <20 proposals/month).

**State A → State B migration trigger:** When Supabase schema is loaded with company_id on all 8 tables AND contact data is imported (currently 0 contacts in 107 profiles), the n8n NODE 2 automated pull replaces the manual copy-paste bridge. This is the single integration inflection point. Everything else in the architecture works in both states.

---

### 8. Recommended Integration Backbone

**Recommendation: n8n as the Zone 1 integration backbone, Azure Event Grid as the Zone 2 integration backbone. The two zones do not share an integration layer.**

Rationale:

**n8n (Zone 1 backbone):**
n8n is already confirmed as the Email Drafter (P2) production stack on Hetzner VPS. It is self-hosted, already provisioned, already designed for Claude API direct calls (Haiku/Sonnet/Opus). Extending n8n to orchestrate P4 TT Itinerary Drafter (TT API T1/T2 calls are simple REST — n8n has native HTTP nodes) and to serve as the Supabase query layer (n8n NODE 2) requires no new infrastructure decisions. The weekly Second Brain Friday review (feeding best lines, updated DO's/DON'Ts back into Claude Teams projects) can also be n8n-orchestrated. Cost: ~€10/month for the VPS already allocated.

Alternatives considered: Azure Logic Apps could serve Zone 1, but would require Azure provisioning for what is fundamentally B2B staff tooling that must remain separated from Zone 2 infrastructure for GDPR boundary clarity. Microsoft Power Automate was explicitly rejected in PRD v3 (single Premium license risk). n8n is the only option that is already confirmed, already deployed, and has no new licensing surface.

**Azure Event Grid (Zone 2 backbone):**
Azure Event Grid is already confirmed in the P5 stack for the booking webhook → Magic Link pipeline and internal agent orchestration (Master Agent → sub-agents). All Zone 2 products (P5 Finland TA, P6 Järvisydän TA) are Azure-native. Cosmos DB handles real-time session state and Staff Priority Queue. Azure AI Search indexes all four RAG shelves. Event Grid is the correct nervous system for event-driven Azure workloads.

**The integration boundary between Zone 1 and Zone 2:**
There is no integration middleware connecting n8n (Zone 1) to Azure Event Grid (Zone 2). The only permitted data crossing the boundary is:
1. Anonymized booking source metadata: daily batch export from Shadow Ledger (Azure SQL) written to a Zone 1 Supabase table — this is a scheduled n8n workflow that reads an aggregate API endpoint from P5, not a direct Supabase → Azure connection
2. B2B Partner Dashboard: a read-only Azure SQL endpoint with guest data pseudonymized at the API layer, not a Zone 1 system accessing Zone 2 infrastructure

This clean separation is not a design preference — it is the GDPR boundary made architectural.

---

### 9. Top 3 Questions for the Synthesis

**Q1: Is there a viable path to P3 Staff Dashboard (BP_08) being ready for Järvisydän launch, given it is XL complexity and not started?**
This is the hardest constraint in the entire architecture. P5 Traveler PWA (BP_11) cannot launch without BP_08. Patrick has confirmed one staff member dedicates meaningful part-time daily hours to monitoring AI guest conversations. That staff member needs BP_08 to do that work. If BP_08 cannot be delivered in parallel with BP_11, the B2C launch date is set by BP_08 completion, not BP_11. The synthesis must confront this directly.

**Q2: What is the Järvisydän IT contact and Oracle Opera API engagement plan?**
Five blockers (Oracle Opera credentials + endpoint docs + sandbox, BookVisit product catalog, booking webhook, on-prem network path, Article 28 DPA) all require Järvisydän IT cooperation. Patrick has confirmed no IT contact has been made yet. Every week without this contact is a week of Azure infrastructure being built without knowing if Booker Agent (BP_06) will work. The synthesis must identify who initiates contact, what they ask for, and what the architecture fallback is if Oracle Opera API access takes months (it may — hotel PMS integrations are notoriously slow).

**Q3: What is the Supabase State A → State B migration sequencing, and does it block anything before contact data import is complete?**
107 client profiles with zero contact names means P2 Email Drafter personalization is operating blind on the most valuable dimension (named relationship history). State B migration requires: (a) Anthropic DPA verified for GDPR Article 44–46 transfer mechanism, (b) contact data imported from email mining sessions, (c) company_id added to all 8 Supabase tables before first data load. These three prerequisites are sequential. The synthesis should confirm the order and assign ownership.

---

## Self-check

9 sections completed. Shortest section is Section 7 (22 lines).
Integration diagram: complete — all 6 products shown as boxes, all major arrows labeled with data type, direction, and frequency note. Both Second Brain states shown explicitly.
TT API citation: cited traveltree-api-status.md with T1/T2/T3 specific findings (Section 3).
GDPR Articles cited: 14 articles cited by number — 4(15), 5(1)(b), 6(1)(a), 6(1)(b), 6(1)(f), 9(1), 9(2)(a), 9(2)(b), 13, 28, 30, 35(3)(b), 35(3)(c), 44–46.
Challenge flagged vs Agent 1: gap found — 107 client profiles with zero contact names blocks P2 highest-value personalization seam (named relationship history). Flagged in Seam 1 and Section 9 Q3.
Assumptions validated: Two-state Second Brain confirmed (A2 cross-brief); n8n/Supabase stack confirmed (A2); TT API answers from traveltree-api-status.md (not speculated); Article 9 Mood Matrix risk confirmed from A3; BP_08 not started confirmed from A4.
Context load: light (<100K) — read 3 files (cross-brief 211 lines, PRD v3 40KB, TT status 56 lines).

---

## Briefing Flag for Lead — Agent 6 Spawn

"B2B/B2C data boundary I've drawn: Zone 1 (n8n/Hetzner/Supabase) and Zone 2 (Azure North Europe) do not share integration middleware. The only permitted data crossing is (1) anonymized booking source metadata (operator_id + revenue tier, no guest PII) via daily batch from Shadow Ledger to Supabase, and (2) pseudonymized guest satisfaction via B2B Partner Dashboard API endpoint. Mood Matrix 'Needs_Accessibility' tag excluded at launch (Article 9 risk). All Zone 2 data stays in Azure SQL / Cosmos DB / Data Lake Gen2. Consistent with your infrastructure plans? Specifically: does the Supabase schema need a dedicated table for the daily booking source metadata batch from Azure, and should that table be isolated by RLS from the main 8-table Second Brain schema?"
