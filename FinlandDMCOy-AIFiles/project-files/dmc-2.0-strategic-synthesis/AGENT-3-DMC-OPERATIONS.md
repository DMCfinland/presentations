## DMC Operations Analysis — CRM, Suppliers, and the Build-vs-Buy Decision

**Agent 3 — DMC Operations Specialist | 2026-03-10**
*Sources: PIPEDRIVE-RESEARCH-BRIEFING.md, agent-1-second-brain.md, agent-2-email-drafter.md, agent-5-integration-architect.md, agent-6-database-infrastructure.md, EMAIL-DRAFTER-DESIGN.md*

---

### 1. DMC Workflow Mapping — Full Lifecycle

A Finland DMC deal touches seven distinct phases. No single tool covers all of them. Here is what each phase requires and where the coverage gaps fall.

**Phase 1: Inquiry Qualification (Day 0)**
- Inbound email arrives at info@finlanddmc.fi. Staff must identify: new or existing client? What market segment (FIT, group, series, incentive, MICE)? What season? What pax range? Is this a serious buyer or a price-shopping pass?
- Pipedrive: Creates a deal manually. No auto-classification. Staff types everything.
- Moonstride: Has inquiry capture with some field auto-population from email. Not zero-entry.
- Our system: n8n NODE 1 parses the email, Haiku classifies task type, Second Brain looks up the client. Zero manual entry. This is our strongest advantage.

**Phase 2: Proposal Building (Days 1-5)**
- Staff builds an itinerary (in TravelTree), writes a pricing sheet (commission-aware), drafts a cover email matching client tone and relationship history.
- Pipedrive: Smart Docs can template proposals but has zero awareness of itineraries, seasonal rates, pax tiers, or commission exceptions. Staff still builds everything manually.
- Moonstride: Full itinerary builder with drag-and-drop components, live pricing from supplier rate cards, pax-tier calculations. This is Moonstride's core strength.
- Our system: Email Drafter generates the cover email with full personalization. TravelTree handles itinerary building. Pricing block auto-calculates from rate_cards table with commission exceptions flagged. The itinerary builder itself is TravelTree — we do not replicate it.

**Phase 3: Revision Management (Days 5-30)**
- Clients request changes: swap a hotel, add a day, change pax count, adjust budget. Average 1-3 revision rounds per deal. Each revision requires re-pricing.
- Pipedrive: Revision tracking via attachments/notes. No structural versioning. Staff manually updates deal value.
- Moonstride: Itinerary versioning with automatic re-pricing on component changes. This is genuinely hard to build.
- Our system: version_sequences table tracks component additions/removals per revision. Email Drafter generates revision responses referencing what changed. Pricing recalculates automatically. TravelTree handles the itinerary revision itself.

**Phase 4: Pricing (embedded in Phases 2-3)**
- Seasonal rates: summer (Jun-Aug) vs winter (Dec-Mar) vs shoulder seasons. Prices differ 20-40%.
- Pax-based tiers: 1-5 pax, 6-15, 16-30, 31+. Each tier has different per-person NET rates.
- NET vs GROSS: DMC buys at NET from suppliers, sells at GROSS to clients. Commission = GROSS - NET.
- Commission exceptions: Solitary restaurant (0%), yoga sessions (0%), catering fees (0%), Stay Longer/Early Bird online offers (0%). Default 15-20%.
- Pipedrive: No pricing engine. Deal value is a manual number field.
- Moonstride: Full seasonal/pax pricing engine with supplier NET rates. Commission tracking built in.
- Our system: rate_cards table stores NET rates with validity periods and commission percentages. Pricing block in Email Drafter auto-calculates GROSS from NET + commission%. Exception rules enforced at both database level (commission_pct = 0 on specific rate cards) and prompt level (golden prompt flags exceptions explicitly). Both layers must stay in sync — database is source of truth, prompt is safety net.

**Phase 5: Operations (Days 30-180, post-confirmation)**
- Supplier booking: confirm hotels, restaurants, activity providers, transport. Each needs a booking confirmation with dates, pax, special requirements.
- Guide assignment: match guide to group language, expertise, availability.
- Transport coordination: airport transfers, inter-city transport, activity transport.
- Daily program sheets: day-by-day operational document showing times, locations, contacts, emergency numbers. Given to guides and drivers.
- Pipedrive: Projects feature provides basic Kanban tasks. Not operations management.
- Moonstride: Full supplier booking management, guide database, transport scheduling, operational documents. This is where Moonstride earns its price.
- Our system: NOT YET DESIGNED. This is the biggest gap. Second Brain and Email Drafter handle pre-sale. Post-confirmation operations is an open field.

**Phase 6: On-Trip Execution (during the trip)**
- Real-time coordination: guide check-ins, supplier confirmations, weather-based changes, emergency handling.
- Pipedrive: Nothing.
- Moonstride: Basic operational view. Not real-time coordination.
- Our system: Future B2C Travel Assistant (P5/P6) handles guest-facing. Staff-facing ops coordination is undesigned.

**Phase 7: Post-Trip (Days 1-30 after trip)**
- Client feedback collection, invoice reconciliation (supplier invoices vs client invoice), supplier payment processing, rebooking signals ("same group next year?"), win/loss recording for intelligence.
- Pipedrive: Basic deal closure + notes. No invoice reconciliation.
- Moonstride: Supplier payment tracking, invoice generation, basic rebooking flags.
- Our system: Interaction records capture post-trip feedback. Invoice reconciliation is undesigned. Rebooking signals feed Second Brain's relationship health score and component win-rate engine.

**Summary: Phases 1-4 are where our custom system wins. Phase 5 is where Moonstride wins. Phases 6-7 are partially covered by both.**

---

### 2. The 5 Most Valuable DMC Features to Build

Ranked by daily time savings for 4 sales staff handling ~20 proposals/month across 107 clients.

**Feature 1: Auto-Pricing Calculator with Commission Logic**
- What it does: Staff enters destination, season, pax count, and selected components. System pulls NET rates from rate_cards, applies correct commission percentage (with exceptions), calculates per-person and total GROSS prices, flags any missing rates or expired validity periods.
- Why staff needs it: Every proposal requires a pricing sheet. Currently built manually in Excel. Each revision requires recalculation. Commission exceptions are memorized, not systematized — risk of quoting 15% commission on a Solitary dinner (should be 0%).
- Time saved: ~45 minutes per proposal, ~15 hours/month across 20 proposals.
- Technical complexity: **Medium.** Rate_cards table already designed. Calculation logic is straightforward arithmetic. The hard part is data entry: populating 200+ supplier rate cards with seasonal variants. Estimate 2-3 days of data work plus 1-2 days of build.

**Feature 2: Intelligent Email Classification + Auto-Draft**
- What it does: Incoming email arrives → system identifies client, classifies task type (13 golden prompt categories), pulls relationship context, generates a complete draft with pricing block and itinerary references. Staff reviews and approves.
- Why staff needs it: The #1 staff complaint is "entering data into systems." This feature requires ZERO data entry — the email IS the input. Removes the blank-page problem that costs 20-40 minutes per complex proposal email.
- Time saved: ~30 minutes per response, ~10 hours/month at 20 proposals/month.
- Technical complexity: **High.** n8n 8-node pipeline, Claude API integration, Second Brain lookup, golden prompt selection. Already designed in EMAIL-DRAFTER-DESIGN.md. Build estimate: 4-6 weeks (Phase 1-2).

**Feature 3: Client Intelligence Dashboard (Pipeline View)**
- What it does: Visual Kanban showing all active deals by stage (Inquiry → Proposal Sent → In Revision → Confirmed → Operating → Completed). Each card shows: client name, pax, value, days in stage, staff owner, relationship health score. Stale deal alerts at 7/14/21 days.
- Why staff needs it: Currently no shared visibility into pipeline. Each staff member tracks their deals in email/memory. Patrick has no aggregate view. AHI Travel's 75% revenue concentration is invisible without this.
- Time saved: ~20 minutes/day per staff member (eliminates "what's the status of X?" conversations). ~7 hours/month across 4 staff.
- Technical complexity: **Medium.** Supabase query + Next.js frontend. The data exists in interactions and clients tables. The Kanban view is standard UI work. BP_08 was designed for B2C — this is the B2B equivalent.

**Feature 4: Supplier Rate Card Manager**
- What it does: Centralized database of all supplier NET rates, organized by: supplier → service → season → pax tier. Shows validity dates, last-confirmed date, quality score, primary contact. Flags expired rates 30 days before expiry.
- Why staff needs it: Rate cards currently live in scattered Excel files, emails, and PDFs. When building a proposal, staff searches email for "Hotel X rates 2026" — often finding outdated information. Wrong rates = wrong margins.
- Time saved: ~15 minutes per proposal for rate lookups, ~5 hours/month.
- Technical complexity: **Low-Medium.** The rate_cards and suppliers tables are designed. UI is a CRUD interface. The hard part is initial data migration from scattered sources — estimate 3-5 days of data work.

**Feature 5: Proposal Win-Rate Engine**
- What it does: Tracks which itinerary components (Aurora hunting, ice swimming, smoke sauna, husky safari) win deals at what rate, for which market segments, in which seasons. When staff builds a proposal, the system ranks recommended components by historical win rate for that client's segment.
- Why staff needs it: Currently, component selection is based on individual staff experience. JK's departure took 130 accounts of institutional knowledge with him. The win-rate engine makes that knowledge permanent and data-driven.
- Time saved: Indirect — improves win rate from 44% rather than saving time directly. At €3.2M revenue and 44% win rate, even a 5-point improvement (~49%) represents ~€360K in additional annual revenue.
- Technical complexity: **High.** Requires version_sequences table populated with enough historical data (minimum 50-100 labeled outcomes) to produce statistically meaningful recommendations. Data mining from email archive is the bottleneck, not the build.

---

### 3. Supplier Management Design

**Data model per supplier (stored in `suppliers` + `rate_cards` tables):**

```
suppliers table:
  supplier_id, company_id, name, type (hotel/restaurant/activity/transport/guide),
  region (Lapland/Lake_Saimaa/Helsinki/Archipelago), primary_contact_name,
  primary_contact_email, primary_contact_phone, quality_score (1-10),
  reliability_score (1-10), last_booking_date, total_bookings_count,
  notes, commission_default_pct, payment_terms_days, vat_id

rate_cards table:
  rate_card_id, supplier_id, company_id, service_name, service_category,
  season (summer/winter/shoulder/year_round), pax_min, pax_max,
  price_net_eur, price_unit (per_person/per_group/per_hour/per_day),
  commission_pct, commission_exception_reason (null if standard),
  valid_from, valid_to, currency, conditions_text, last_confirmed_date,
  confirmed_by (staff_member)
```

**How supplier data feeds into proposal pricing:**

1. Staff selects components for an itinerary (or AI recommends based on win-rate engine).
2. Each component maps to a supplier + service in rate_cards.
3. System looks up: matching season (from trip dates) → matching pax tier (from group size) → current NET rate.
4. Commission applied: `gross = net / (1 - commission_pct/100)` — unless commission_exception_reason is set, in which case `gross = net` (0% commission, passed through at cost).
5. Total proposal value = sum of all component GROSS prices.
6. Pricing block displayed to staff with flags: expired rates (red), commission exceptions (yellow), missing rates (orange — manual lookup required).

**Commission calculation rules:**

| Scenario | Commission % | Enforcement |
|----------|-------------|-------------|
| Standard supplier service | 15-20% (varies by supplier agreement) | rate_cards.commission_pct per service |
| Solitary restaurant | 0% | commission_exception_reason: "Solitary — no commission agreement" |
| Yoga sessions | 0% | commission_exception_reason: "Yoga — no commission agreement" |
| Catering fees | 0% | commission_exception_reason: "Catering — pass-through cost" |
| Stay Longer / Early Bird online offers | 0% | commission_exception_reason: "Online offer — no commission on direct bookings" |
| New supplier (unconfirmed rate) | Flag for manual review | commission_pct = null triggers "RATE UNCONFIRMED" flag |

**Integration with Email Drafter commission rules:**
The Email Drafter's golden prompt references commission rules as a safety net: "If the component name contains Solitary restaurant, always set commission to 0 and flag this to staff." The database rate_cards.commission_pct = 0 is the source of truth. The prompt rule is the fallback for cases where rate card data is incomplete. Both layers must exist because: (a) new suppliers may be added to proposals before their rate cards are entered, and (b) staff may manually override prices — the prompt catches commission errors the database cannot prevent.

---

### 4. The TravelTree Integration Question

**Current state:** TravelTree Pro handles itinerary building — the visual, client-facing document showing day-by-day programs with images, maps, and descriptions. Finland DMC is on the Pro plan (price locked January 2026).

**API capabilities (confirmed via Ihor Kucher, 2026-02-21):**
- T1 — Create itinerary via API: YES, free, available now. Needs enabling.
- T2 — Read itinerary content via API: YES, free, available now. Needs enabling.
- T3 — Export component library as data: PAID, scope and cost TBD. Needs call with Ihor.

**The boundary:**

| Function | TravelTree | Our System |
|----------|-----------|------------|
| Itinerary visual rendering (client-facing PDF/link) | TT owns this | Does not replicate |
| Component library (1000+ activities/hotels/restaurants) | TT stores these | Mirrors pricing data in rate_cards, not descriptions |
| Itinerary versioning (visual) | TT handles v1/v2/v3 | Tracks what changed per version (version_sequences) for analytics |
| Client pricing sheet | Does not do this | Auto-generates from rate_cards + commission logic |
| CRM / client intelligence | Does not do this | Second Brain + Email Drafter |
| Proposal email with context | Does not do this | Email Drafter with golden prompts |
| Supplier relationship management | Does not do this | suppliers table + quality/reliability scores |
| Win-rate analytics | Does not do this | component win-rate engine from version_sequences |

**Data flows:**

TT → Our system:
- Itinerary links (T1/T2): embed in proposal emails. Email Drafter includes TT URL in every proposal.
- Component metadata (T3, if purchased): service names, descriptions, images. Populates our component reference table for win-rate matching.
- View notifications (Q6 unanswered): if TT notifies when client opens itinerary link, this feeds Email Drafter follow-up automation ("client viewed your proposal 2 hours ago — no reply yet").

Our system → TT:
- Itinerary creation requests (T1): AI recommends components → system creates itinerary in TT via API → receives link back.
- Client context: group size, destination, season, budget range → pre-populates TT itinerary parameters.

**Can TravelTree's API provide supplier rates for auto-pricing?**
No. TT stores component descriptions and visual content, not NET supplier rates or commission percentages. Pricing lives in our rate_cards table. TT is the presentation layer; our system is the pricing and intelligence layer.

**Should we replace TravelTree or integrate?**
Integrate. Building an itinerary renderer (with maps, images, responsive design, client-facing URLs, mobile view) is 3-6 months of frontend work that TT already does well. TT costs are included in the existing Pro plan. The ROI of replacing TT is negative. The ROI of integrating (T1 + T2 APIs, free) is immediate. T3 component export is the only paid decision — defer until we understand actual usage patterns from mining TT links in the email archive.

---

### 5. Moonstride Honest Assessment

**What Moonstride does at €595/month:**
- CRM pipeline with Kanban view
- Full itinerary builder with drag-and-drop components
- Supplier management with NET rate cards
- Seasonal pricing engine with pax tiers
- Commission tracking (default + exceptions)
- Booking management (supplier confirmations, vouchers)
- Guide and transport assignment
- Invoice generation
- AI profiling + chatbot + content writer/translator
- Multi-currency support

**What is genuinely hard to build (that Moonstride already has):**

1. **Itinerary builder with live pricing:** Drag a component, prices recalculate instantly across the full itinerary, respecting season and pax tier. Building this UI from scratch: 4-8 weeks. But TravelTree already handles itinerary building, and our pricing calculator handles the math. The integrated "drag and price updates" experience is what is hard — neither TT nor our system does it in one view today.

2. **Supplier booking workflow:** Confirm → send voucher → track supplier response → flag unconfirmed bookings → generate operational documents. This is Phase 5 operations — our system's biggest gap. Building this: 3-5 weeks of workflow design + build.

3. **Invoice reconciliation:** Match supplier invoices against booking confirmations, flag discrepancies, track payment status. Accounting-adjacent work that requires precision. Building this: 2-3 weeks plus integration with accounting software.

**What Moonstride does NOT do that our AI system provides:**

1. **Zero-entry CRM from email mining.** Moonstride requires manual data entry for every deal. Our system mines info@finlanddmc.fi automatically. This is the #1 staff complaint solved.

2. **Personalized email drafting with full relationship context.** Moonstride has a generic content writer. Our Email Drafter knows Laura writes formally, Reeta writes warmly, that Wikinger Reisen prefers Aurora programs, and that Nordic Luxury had a pricing delay frustration in January.

3. **Component win-rate intelligence.** No commercial DMC tool tracks which itinerary components win deals for which market segments. This is proprietary competitive intelligence.

4. **Relationship health scoring.** Second Brain's 5-factor weighted score (interaction frequency, sentiment trend, opportunity pipeline, response time, days since contact) with automated alerts for at-risk accounts. Moonstride has basic CRM fields.

5. **M365 integration depth.** Our system reads the shared mailbox, Teams channels, and SharePoint natively via M365 connector. Moonstride requires email forwarding or manual entry.

**The verdict: Do not buy Moonstride. Build custom with TravelTree integration.**

The reasoning:

- Moonstride's primary value is in Phase 5 (operations) and the integrated pricing/itinerary builder. But TravelTree already handles itinerary building, and our pricing calculator handles pricing logic. Moonstride's unique contribution narrows to: supplier booking workflow + invoice reconciliation + operational documents.

- Moonstride's CRM is inferior to our email-mined Second Brain. Buying Moonstride means staff must enter data into TWO systems (Moonstride for ops + our system for AI intelligence) or abandon one. Neither outcome is acceptable.

- €595/month = €7,140/year. The custom build cost for the Phase 5 operations gap (supplier booking workflow, operational documents, basic invoice tracking) is estimated at 6-8 weeks of development. At one-time build cost, the system pays for itself within 12-18 months and is infinitely customizable after that.

- The critical advantage: our system's intelligence layer (win-rate engine, relationship health, personalized drafting) cannot be replicated in Moonstride. Moonstride's operations layer CAN be replicated in our system — it is structured workflow, not AI innovation.

**Build sequence for operations gap:**
1. First: Rate Card Manager (Feature 4) — foundation for all pricing. 1-2 weeks.
2. Second: Auto-Pricing Calculator (Feature 1) — enables proposal pricing. 1 week.
3. Third: Pipeline Kanban (Feature 3) — gives Patrick visibility. 1-2 weeks.
4. Fourth: Supplier Booking Workflow — post-confirmation operations. 3-4 weeks.
5. Fifth: Operational Document Generator (daily program sheets) — 1-2 weeks.
6. Total: 7-11 weeks for the complete operations layer that makes Moonstride unnecessary.

The Email Drafter (Feature 2) and Win-Rate Engine (Feature 5) are already in the build plan and proceed in parallel.

---

### Recommendation

**Build everything custom, integrated with TravelTree.**

- Enable TT APIs T1 + T2 immediately (free, contact Ihor).
- Defer T3 component export decision until email archive mining reveals actual usage patterns.
- Build the 5 features in priority order: Rate Card Manager → Pricing Calculator → Pipeline Kanban → Email Drafter → Supplier Booking Workflow.
- Phase 5 operations (supplier booking, guide assignment, operational docs) is the last build priority — it only matters after deals are confirmed, and the pre-sale tools (pricing, drafting, pipeline) have higher daily impact.
- Do not buy Pipedrive (data entry problem unsolved). Do not buy Moonstride (CRM layer inferior, operations layer buildable, €7K/year ongoing cost for something that should be owned).

The competitive moat is in the intelligence layer: zero-entry CRM, personalized drafting, win-rate analytics, relationship health scoring. No commercial tool provides this. Build it, own it, and extend it across the portfolio.

---

## Self-check

5 sections completed. All sections meet the specificity requirement — pricing rules cite exact commission exceptions, TT integration cites confirmed API capabilities with source (Ihor Kucher WhatsApp, 2026-02-21), Moonstride assessment includes specific cost comparison.

Feature ranking justified by: time saved per month (quantified), technical complexity (rated), and relevance to Finland DMC's specific context (107 clients, 4 staff styles, AHI 75% concentration, JK departure knowledge loss).

Build-vs-buy verdict is clear and actionable: build custom, with specific build sequence and week estimates.

TravelTree boundary defined: TT = presentation layer, our system = pricing + intelligence layer. No replication of TT functionality.

Moonstride assessment acknowledges genuine strengths (Phase 5 ops, integrated itinerary pricing) while identifying why the custom path is superior for this specific company.
