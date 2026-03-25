# Second Brain ERP&CRM — Extended Design v2.0

**Date:** 2026-03-10
**Base:** agent-1-second-brain.md (Second Brain Analyzer output, 2026-02-22)
**Extensions:** CRM-DECISION-SYNTHESIS.md, AGENT-2-TECHNICAL-ARCHITECT.md, AGENT-3-DMC-OPERATIONS.md
**Scope:** Original Second Brain design + Pipeline/CRM layer + Supplier management + Auto-pricing + Kanban + Morning dashboard + Relationship-deal integration + Stolen CRM features

---

## PART A — ORIGINAL SECOND BRAIN DESIGN (PRESERVED)

*Everything below in Part A is the original Agent 1 analysis, unchanged. Part B adds the CRM/pipeline extensions.*

---

### 1. What It Is (in plain language)

On a typical Tuesday, a Finland DMC staff member opens their phone between calls and types a two-sentence note into a Teams channel: "Spoke with Lars at Wikinger Reisen — they're planning a new January Aurora series, 22 pax, wants draft by March 15. Very positive." That's the entire staff-facing behavior. Second Brain receives that capture, classifies it (category: `client_interaction`; client: Wikinger Reisen; sentiment: Very Positive; opportunities: Aurora series proposal; next action: draft by March 15), and stores it. The next morning a 150-word digest arrives in their Teams DMs summarizing all open client threads, flagged next actions, and relationship alerts. When that same staff member opens a proposal for Wikinger an hour later, Claude retrieves the Wikinger profile — 4/4 proposals won, 100% win rate, €316,600 revenue, high margin, JS/Lapland preferred destinations — plus every interaction note from the last 24 months, and drafts a personalized email in their established tone. Second Brain is the institutional memory that makes every client interaction feel like the company remembers, even when the person who originally built the relationship is gone.

---

### 2. Data It Produces

All entities below are grounded in `proposals-data-summary.md` (schema section) and `second-brain-system-summary.md` (Data Architecture section).

**Client Record**
- What: Company-level CRM profile — canonical name, country, channel (Direct/GSA), segment (FIT/Group/Series/Incentive/MICE), revenue tier (Flagship/Reliable/Occasional/Dormant/New), annual revenue EUR, margin avg, RelationshipHealthScore (1-10 weighted composite)
- Owner: Patrick (master data); staff contribute via capture; updated continuously
- Updated: On every new captured interaction; RelationshipHealthScore recalculated weekly
- Retained: Indefinitely

**Contact Record**
- What: Named individual — FullName, Company (linked), Role, RelationshipStrength, DecisionMaker flag, PersonalNotes, PreferredLanguage
- Owner: Staff via capture; Patrick validates
- Updated: On each new capture that mentions a named individual
- Retained: Indefinitely
- Gap identified: `client-profiles.yaml` currently contains zero contact names or email addresses for any of its 107 company records; contact data exists only in email-mining outputs

**Interaction Record**
- What: Each client touchpoint — InteractionDate, Contact (linked), Company (linked), Type (Call/Email/Meeting/Event/Site Visit), Summary, RawCapture, Sentiment (Very Positive through Concerned), OpportunitiesIdentified, NextActions, NextActionDate, ConfidenceScore, Topics (max 5 per interaction)
- Owner: Generated automatically from each capture; human correction possible
- Updated: Per capture event (real-time)
- Retained: 24-month rolling window

**RelationshipHealthScore**
- What: Weighted composite per client — interaction frequency 30%, sentiment trend 25%, opportunity pipeline 20%, response time 15%, days since contact 10%
- Owner: Computed; no human authorship
- Updated: Weekly (recalculated across all interactions in 24-month window)
- Retained: Current score stored on Client Record; trend history via Interaction Records

**Growth Roadmap**
- What: Per-client strategic plan — CurrentState, TargetState, CurrentRevenueTier, TargetRevenueTier, KeyInitiatives, ConfidenceLevel, Status
- Owner: Patrick
- Updated: Quarterly or on major client event
- Retained: One active per client; previous versions archived

**Team Feedback Record**
- What: Staff sentiment capture — FeedbackDate, StaffMember (optional, blank = anonymous), Category, Theme, Sentiment, Status
- Owner: Staff; anonymous capture supported via `[anon]` prefix
- Updated: Per staff capture event
- Retained: No explicit retention window stated

**Weekly Win Record**
- What: WinDate, StaffMember, Achievement, Impact, Client (linked)
- Owner: Staff captures; Patrick may curate
- Updated: As wins occur
- Retained: Not explicitly defined

**A4 Client Insight Page**
- What: Auto-generated narrative briefing — 7 sections: Executive Summary, Relationship Status, Interaction History, Commercial Performance, Growth Opportunity, Risk Flags, Recommended Next Actions
- Owner: Generated; Patrick reviews Top 10 weekly
- Updated: Auto-generated weekly for Top 10 clients; on-demand for others
- Retained: Snapshot; replaces prior version weekly

**Daily Digest**
- What: Personalized per-staff morning briefing — open threads, next actions, relationship alerts, wins (format: under 150 words, structured sections, bilingual Finnish/English)
- Owner: Generated; staff consumes
- Updated: Each weekday 06:45 EET
- Retained: Ephemeral Teams DM

**AI-Feedback Record**
- What: Rating (1-4) + brief note per Claude task; stored in Teams #ai-feedback channel
- Owner: Staff
- Updated: Per task completion
- Retained: Searchable via M365 connector

---

### 3. Data It Needs (from other products)

**From Email Drafter (Product 2):** Proposal outcome (sent? replied? converted?), client name and deal context from each draft session.

**From Staff Dashboard (Product 3):** AI conversation outcomes, escalation frequency per client.

**From TT Itinerary Drafter (Product 4):** Supplier performance signals, itinerary generation time and complexity.

**From Travel Assistants (Products 5-6):** Phase 2 integration only. Aggregate B2C booking signals may flow to B2B profiles. Zone 1 data must NOT flow to Zone 2 (enforced at data layer).

---

### 4. What It Gives to Other Products

**To Email Drafter:** Client Record pull (name, tier, destinations, margins, win rate), interaction history (24 months), contact data, RelationshipHealthScore (below 6/10 triggers recovery-tone template).

**To Staff Dashboard:** FIRE RED escalation context (relationship tier, account owner, sentiment), NextActions queue, account health alerts (AHI concentration risk, Flash Pack orphan risk).

**To TT Itinerary Drafter:** Client preferences (preferred_destination, typical_pax_range, segment) for pre-population.

**To Travel Assistants (Products 5-6):** Nothing in Zone 1 -> Zone 2 direction during transition period.

---

### 5. Infrastructure — Decided vs Open

**Confirmed:** Claude Teams (5 seats, €125/mo), router + 3-4 execution projects, M365 connector read-only, Sonnet 4.5 default / Opus for complex, #ai-feedback channel, 4 content categories, 5-factor health score, 24-month interaction retention, Phase 0 Patrick-only.

**Open:** M365 connector search syntax, GDPR posture of Claude Teams, shared mailbox detection, Finnish-language search, structured storage replacement.

---

### 6. GDPR Analysis

Data classification: Tier 2 (B2B contact data, moderate sensitivity). Legal basis: Article 6(1)(f) Legitimate Interests. Minimum actions before launch: (1) Verify Anthropic DPA, (2) Document LIA, (3) Confirm DPIA requirement, (4) Implement data subject access/erasure mechanism.

---

### 7. Architecture Simplification Verdict

PRD v3 simplification is correct for transition period (5-person team, 107 clients, months 1-6). Will not scale to OTA-class volume. Plan migration to proper data layer when client count exceeds ~200 or GDPR data subject request arrives.

---

### 8. Top 3 Blocking Questions (from original analysis)

1. How does Second Brain maintain persistent, updatable client records without a database?
2. Does Anthropic's Claude Teams DPA satisfy GDPR Article 28 + 44-46?
3. When does the JK departure orphan problem become a system failure?

---

## PART B — CRM/PIPELINE EXTENSIONS

*Everything below is NEW — extending Second Brain with pipeline management, supplier tracking, auto-pricing, and the CRM features the team actually asked for.*

---

### 9. Pipeline/CRM Data Layer

Three new tables added to the existing Supabase schema. These sit alongside the Second Brain's clients, contacts, and interactions tables. RLS pattern identical: `company_id = current_setting('app.company_id')`.

#### Table 10: deals

The pipeline. Every active opportunity from inquiry through invoicing.

```sql
deals (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id      UUID NOT NULL,
  client_id       UUID REFERENCES clients(id),
  contact_id      UUID REFERENCES contacts(id),
  staff_owner_id  TEXT NOT NULL,                     -- assigned staff email
  title           TEXT NOT NULL,                     -- "AHI Travel — Northern Lights Feb 2027"
  stage           TEXT NOT NULL DEFAULT 'inquiry',
    -- inquiry | proposal_sent | revision | confirmed | operating | invoiced | won | lost
  value_eur       NUMERIC(12,2),
  pax_count       INTEGER,
  season          TEXT,                              -- summer | winter | shoulder
  arrival_date    DATE,
  departure_date  DATE,
  commission_pct  NUMERIC(5,2) DEFAULT 15.0,
  probability     INTEGER DEFAULT 50,               -- 0-100, AI-calculated
  last_activity   TIMESTAMPTZ DEFAULT NOW(),
  next_action     TEXT,
  next_action_due TIMESTAMPTZ,
  stale_days      INTEGER GENERATED ALWAYS AS
    (EXTRACT(EPOCH FROM (NOW() - last_activity)) / 86400) STORED,
  proposal_link   TEXT,                              -- TravelTree itinerary URL or SharePoint link
  lost_reason     TEXT,
  created_at      TIMESTAMPTZ DEFAULT NOW(),
  updated_at      TIMESTAMPTZ DEFAULT NOW()
);
```

#### Table 11: deal_activities

Activity log per deal. Most entries auto-created by n8n email mining; manual entries for calls/meetings.

```sql
deal_activities (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id      UUID NOT NULL,
  deal_id         UUID REFERENCES deals(id),
  activity_type   TEXT NOT NULL,
    -- email_sent | email_received | call | meeting | proposal_sent
    -- | proposal_viewed | revision | note
  subject         TEXT,
  body_summary    TEXT,             -- AI-generated summary, not full email
  performed_by    TEXT,             -- staff email or 'system'
  metadata        JSONB,           -- flexible: {message_id, tt_link, open_count}
  created_at      TIMESTAMPTZ DEFAULT NOW()
);
```

#### Table 12: deal_stage_history

Audit trail for every stage transition. Required for pipeline analytics and GDPR accountability.

```sql
deal_stage_history (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id      UUID NOT NULL,
  deal_id         UUID REFERENCES deals(id),
  from_stage      TEXT,
  to_stage        TEXT NOT NULL,
  changed_by      TEXT NOT NULL,    -- staff email or 'n8n-auto'
  reason          TEXT,
  created_at      TIMESTAMPTZ DEFAULT NOW()
);
```

#### Stage progression model

```
inquiry -> proposal_sent -> revision -> confirmed -> operating -> invoiced -> won
                                                                              |
                               (any stage) --------------------------------> lost
```

Deals move forward (drag right on Kanban) or to `lost` from any stage. Backward moves allowed but logged with mandatory reason in deal_stage_history.

---

### 10. Supplier Management Layer

Two new tables for supplier data and rate cards. These feed the auto-pricing calculator and proposal building.

#### Table 13: suppliers

```sql
suppliers (
  id                      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id              UUID NOT NULL,
  name                    TEXT NOT NULL,
  type                    TEXT NOT NULL,
    -- hotel | restaurant | activity | transport | guide
  region                  TEXT,
    -- Lapland | Lake_Saimaa | Helsinki | Archipelago
  primary_contact_name    TEXT,
  primary_contact_email   TEXT,
  primary_contact_phone   TEXT,
  quality_score           NUMERIC(3,1),    -- 1-10
  reliability_score       NUMERIC(3,1),    -- 1-10
  last_booking_date       DATE,
  total_bookings_count    INTEGER DEFAULT 0,
  notes                   TEXT,
  commission_default_pct  NUMERIC(5,2) DEFAULT 15.0,
  payment_terms_days      INTEGER DEFAULT 30,
  vat_id                  TEXT,
  created_at              TIMESTAMPTZ DEFAULT NOW(),
  updated_at              TIMESTAMPTZ DEFAULT NOW()
);
```

#### Table 14: rate_cards

```sql
rate_cards (
  id                          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  supplier_id                 UUID REFERENCES suppliers(id),
  company_id                  UUID NOT NULL,
  service_name                TEXT NOT NULL,
  service_category            TEXT,
  season                      TEXT NOT NULL,
    -- summer | winter | shoulder | year_round
  pax_min                     INTEGER,
  pax_max                     INTEGER,
  price_net_eur               NUMERIC(12,2) NOT NULL,
  price_unit                  TEXT NOT NULL,
    -- per_person | per_group | per_hour | per_day
  commission_pct              NUMERIC(5,2),
    -- NULL = unconfirmed (triggers review flag)
  commission_exception_reason TEXT,
    -- NULL if standard commission; reason if 0%
  valid_from                  DATE NOT NULL,
  valid_to                    DATE NOT NULL,
  currency                    TEXT DEFAULT 'EUR',
  conditions_text             TEXT,
  last_confirmed_date         DATE,
  confirmed_by                TEXT,
  created_at                  TIMESTAMPTZ DEFAULT NOW(),
  updated_at                  TIMESTAMPTZ DEFAULT NOW()
);
```

#### Supplier-to-deal relationship

Suppliers connect to deals through rate_cards used in proposal pricing. The link is: `deals.id` -> proposal components (stored in deal_activities metadata as JSONB) -> `rate_cards.id` -> `suppliers.id`. No separate junction table needed at this scale; the JSONB metadata on deal_activities of type `proposal_sent` stores an array of rate_card_ids used.

---

### 11. Auto-Pricing Calculator

The pricing engine that replaces manual Excel calculations. Core logic:

#### Calculation flow

1. **Input:** destination, season (derived from trip dates), pax_count, selected components (list of service_names or rate_card_ids)
2. **Rate lookup:** For each component, find matching rate_card WHERE `supplier_id` matches AND `season` matches AND `pax_min <= pax_count <= pax_max` AND `valid_from <= arrival_date <= valid_to`
3. **Commission application:**
   - If `commission_exception_reason IS NOT NULL` -> commission = 0%, GROSS = NET (pass-through)
   - If `commission_pct IS NULL` -> flag "RATE UNCONFIRMED" for manual review
   - Otherwise -> `GROSS = NET / (1 - commission_pct / 100)`
4. **Aggregation:** Total proposal value = SUM of all component GROSS prices. Per-person = total / pax_count (when price_unit = per_group, divide first).
5. **Output:** Pricing block with per-component breakdown, flags for issues

#### Commission exception rules (hardcoded in rate_cards)

| Supplier / Service | Commission % | Exception Reason |
|---|---|---|
| Standard supplier service | 15-20% (per agreement) | NULL (standard) |
| Solitary restaurant | 0% | "Solitary — no commission agreement" |
| Yoga sessions | 0% | "Yoga — no commission agreement" |
| Catering fees | 0% | "Catering — pass-through cost" |
| Stay Longer / Early Bird online | 0% | "Online offer — no commission on direct bookings" |
| New supplier (unconfirmed) | NULL | Triggers "RATE UNCONFIRMED" flag |

#### Dual-layer enforcement

- **Database layer (source of truth):** `rate_cards.commission_pct` and `commission_exception_reason` enforce correct commission per service.
- **Prompt layer (safety net):** Email Drafter golden prompt includes commission rules as fallback for cases where (a) new suppliers are added before rate cards are entered, or (b) staff manually overrides prices. Both layers must stay in sync.

#### Flag system in pricing output

| Flag | Color | Trigger | Action Required |
|---|---|---|---|
| Expired rate | Red | `valid_to < arrival_date` | Update rate card or get new quote |
| Commission exception | Yellow | `commission_exception_reason IS NOT NULL` | Informational — no commission on this line |
| Missing rate | Orange | No matching rate_card found | Manual lookup required |
| Unconfirmed commission | Orange | `commission_pct IS NULL` | Confirm commission % with supplier |
| Pax out of range | Orange | pax_count outside all rate_card pax bands | Request custom quote |

#### Seasonal pricing logic

Seasons are defined per rate_card, not globally. This handles supplier-specific season definitions:
- Hotels may define winter as Nov-Mar while activities define it as Dec-Feb
- Each rate_card row specifies its own `valid_from` / `valid_to` dates
- Multiple rate_cards for the same service with overlapping seasons resolve by: most specific pax range wins, then most recent `last_confirmed_date`

---

### 12. Kanban Pipeline Integration

How Second Brain feeds the visual pipeline board.

#### Data flow: Email -> Deal -> Kanban Card

```
info@finlanddmc.fi (inbound email)
  |
  v
n8n W1: Email-to-Deal Pipeline
  |-- Classify: new_inquiry | existing_deal | non_deal
  |-- If new_inquiry:
  |     Claude Sonnet extracts: client, pax, dates, destination, value estimate
  |     -> INSERT deals (stage = 'inquiry')
  |     -> INSERT deal_activities (type = 'email_received')
  |     -> Match to clients table via company name / email domain
  |-- If existing_deal:
  |     Match to deal via client_id + date range
  |     -> UPDATE deals.last_activity
  |     -> INSERT deal_activities
  |
  v
Supabase Realtime (WebSocket push)
  |
  v
Next.js Kanban Board (live update, no polling)
```

#### Kanban card data (from deal_cards view)

Each card on the board pulls from both the deals table AND Second Brain tables:

```sql
CREATE VIEW deal_cards AS
SELECT
  d.*,
  c.revenue_tier,
  c.relationship_health_score,
  c.segment,
  co.full_name AS contact_name,
  (SELECT MAX(created_at) FROM interactions i
   WHERE i.client_id = d.client_id) AS last_interaction_at,
  (SELECT COUNT(*) FROM deal_activities da
   WHERE da.deal_id = d.id) AS activity_count
FROM deals d
LEFT JOIN clients c ON d.client_id = c.id
LEFT JOIN contacts co ON d.contact_id = co.id;
```

#### Card visual encoding

| Element | Source | Display |
|---|---|---|
| Client tier badge | `clients.revenue_tier` | Gold / Silver / Bronze / New |
| Health dot | `clients.relationship_health_score` | Green (7-10), Yellow (4-6), Red (1-3) |
| Staleness | `deals.stale_days` | Green (<3d), Yellow (3-7d), Red (>7d) |
| Value | `deals.value_eur` | EUR formatted |
| Pax | `deals.pax_count` | Number with group icon |
| Season | `deals.season` | Snowflake / Sun / Leaf icon |
| Staff owner | `deals.staff_owner_id` | Avatar or initials |
| Next action | `deals.next_action` | Text, red if overdue |

#### Auto-stage-progression rules (n8n W2)

| Trigger Event | Detection | Stage Transition | Confidence |
|---|---|---|---|
| Client sends inquiry email | Email classification (Sonnet) | -> `inquiry` (new deal) | High |
| Staff sends email with PDF | Attachment MIME + subject match | -> `proposal_sent` | High |
| Client replies to proposal | Reply-to threading (M365 conversationId) | No auto-move | N/A |
| Staff sends revised proposal | 2nd+ PDF to same thread | -> `revision` | Medium |
| Client confirms | NLP: "confirm", "book", "proceed" | -> `confirmed` + staff alert | Medium (staff approves) |
| Trip dates pass | `departure_date < today` | -> `invoiced` reminder | High |

Medium-confidence transitions create a pending notification. Staff approves with one click in the daily dashboard.

#### Realtime updates

```typescript
const channel = supabase
  .channel('deals-pipeline')
  .on('postgres_changes', {
    event: '*',
    schema: 'public',
    table: 'deals',
    filter: `company_id=eq.${companyId}`
  }, (payload) => {
    updateDealInStore(payload.new);
  })
  .subscribe();
```

5 staff viewing simultaneously: 1 persistent WebSocket each, instant updates. No polling. Supabase Free tier supports this.

---

### 13. Morning Dashboard Data Model

The daily briefing is Second Brain's core adoption driver. Here is what data feeds each section, per staff member.

#### Dashboard generation: server-side Supabase queries at 06:45 EET

**Section 1: My Deals Today**

```sql
-- Deals owned by this staff member, active stages only
SELECT d.*, c.revenue_tier, c.relationship_health_score
FROM deals d
JOIN clients c ON d.client_id = c.id
WHERE d.staff_owner_id = :staff_email
  AND d.stage NOT IN ('won', 'lost')
ORDER BY
  CASE WHEN d.next_action_due <= CURRENT_DATE THEN 0 ELSE 1 END,
  d.next_action_due ASC NULLS LAST;
```

Display: Mini Kanban grouped by stage. Overdue next-actions highlighted red.

**Section 2: Overdue Actions (red zone)**

```sql
-- Next actions past due date
SELECT d.title, d.next_action, d.next_action_due,
       c.canonical_name AS client_name,
       d.stale_days
FROM deals d
JOIN clients c ON d.client_id = c.id
WHERE d.staff_owner_id = :staff_email
  AND d.next_action_due < CURRENT_DATE
  AND d.stage NOT IN ('won', 'lost')
ORDER BY d.next_action_due ASC;
```

Display: Red cards with "X days overdue" badge. Maximum urgency.

**Section 3: Stale Deal Alerts**

```sql
-- Deals with no activity in 7+ days
SELECT d.title, d.stale_days, d.stage, d.value_eur,
       c.canonical_name AS client_name
FROM deals d
JOIN clients c ON d.client_id = c.id
WHERE d.staff_owner_id = :staff_email
  AND d.stale_days > 7
  AND d.stage NOT IN ('won', 'lost', 'invoiced')
ORDER BY d.stale_days DESC;
```

Display: Yellow/red cards with AI-generated 1-line suggestion per deal (Claude Haiku, ~$0.01/day for <50 deals).

**Section 4: Yesterday's Activities**

```sql
-- What happened on this staff member's deals in the last 24h
SELECT da.activity_type, da.subject, da.body_summary,
       d.title AS deal_title, da.performed_by
FROM deal_activities da
JOIN deals d ON da.deal_id = d.id
WHERE d.staff_owner_id = :staff_email
  AND da.created_at > NOW() - INTERVAL '24 hours'
ORDER BY da.created_at DESC;
```

Display: Timeline of activities. Includes auto-detected emails, proposal views, and colleague notes.

**Section 5: Client Emails Received (from Second Brain interactions)**

```sql
-- Recent interaction records from the past 24h for this staff's clients
SELECT i.interaction_date, i.summary, i.sentiment,
       i.next_actions, c.canonical_name
FROM interactions i
JOIN clients c ON i.company_id = c.id
JOIN deals d ON d.client_id = c.id
WHERE d.staff_owner_id = :staff_email
  AND i.interaction_date > NOW() - INTERVAL '24 hours'
ORDER BY i.interaction_date DESC;
```

Display: Incoming client signals that may not yet be linked to a deal.

**Section 6: Relationship Alerts**

```sql
-- Clients with declining or critical health scores
SELECT c.canonical_name, c.relationship_health_score,
       c.revenue_tier, c.annual_revenue_eur
FROM clients c
JOIN deals d ON d.client_id = c.id
WHERE d.staff_owner_id = :staff_email
  AND c.relationship_health_score < 5
GROUP BY c.id
ORDER BY c.annual_revenue_eur DESC;
```

Display: Red/yellow alerts. Flagship clients with low health score = top priority.

**Section 7: Wins & Positive Signals**

```sql
-- Recent wins and positive sentiment interactions
SELECT w.win_date, w.achievement, w.impact, c.canonical_name
FROM weekly_wins w
LEFT JOIN clients c ON w.client_id = c.id
WHERE w.staff_member = :staff_email
  AND w.win_date > NOW() - INTERVAL '7 days'
UNION ALL
SELECT i.interaction_date, i.summary, NULL, c.canonical_name
FROM interactions i
JOIN clients c ON i.company_id = c.id
JOIN deals d ON d.client_id = c.id
WHERE d.staff_owner_id = :staff_email
  AND i.sentiment IN ('Very Positive', 'Positive')
  AND i.interaction_date > NOW() - INTERVAL '48 hours'
ORDER BY 1 DESC LIMIT 5;
```

Display: Green section. Morale boost. "Your proposal to Wikinger was opened 3 times yesterday."

#### Dashboard delivery

- **Primary:** Next.js dashboard page (staff landing page, replaces "open CRM every morning")
- **Secondary:** Teams adaptive card via n8n at 06:45 EET (150-word summary, bilingual FI/EN)
- **Data:** All queries run server-side. Dashboard page loads in <2s. No client-side data fetching for sensitive data.

---

### 14. Relationship Health Score Integration with Deals

The RelationshipHealthScore (Section 2, original design) was client-level only. With the pipeline layer, deal status becomes a direct input to health scoring, and health scores feed back into deal prioritization.

#### Updated health score formula

| Factor | Weight | Source | Deal Integration |
|---|---|---|---|
| Interaction frequency | 25% (was 30%) | interactions table | Deal activities count as interactions automatically |
| Sentiment trend | 25% | interactions.sentiment | Deal-linked emails inherit sentiment classification |
| **Active deal pipeline** | **20% (NEW)** | **deals table** | **Clients with active deals in stages inquiry-confirmed score higher** |
| Response time | 15% | interactions + deal_activities | Time between email_received and email_sent on same deal |
| Days since contact | 15% (was 10%) | MAX(interactions.date, deals.last_activity) | Deal activity resets the "days since contact" clock |

Changes from original:
- "Opportunity pipeline" (20%) replaced by "Active deal pipeline" — now backed by real deal data instead of inferred from interactions
- Interaction frequency reduced from 30% to 25% — deal pipeline carries some of this signal
- Days since contact increased from 10% to 15% — deal staleness is a stronger signal than originally modeled

#### How deal status affects health score

| Deal State | Health Score Impact |
|---|---|
| Active deal in `inquiry` or `proposal_sent` | +1.0 bonus (opportunity in motion) |
| Active deal in `confirmed` or `operating` | +1.5 bonus (revenue committed) |
| Deal moved to `won` in last 30 days | +2.0 bonus (recent success, decays over 90 days) |
| Deal moved to `lost` in last 30 days | -1.5 penalty (recent failure, decays over 90 days) |
| All deals stale >14 days | -1.0 penalty (engagement gap) |
| No active deals AND no interaction in 60 days | -2.0 penalty (dormancy signal) |
| Multiple concurrent deals | +0.5 per additional active deal (growing relationship) |

#### How health score affects deal prioritization

The pipeline Kanban uses health score for visual urgency and AI recommendations:

- **Score 8-10 (Green):** Strong relationship. AI suggests maintaining momentum: "Send program update" / "Share new product."
- **Score 5-7 (Yellow):** Attention needed. AI suggests re-engagement: "Schedule call" / "Send personalized update referencing last interaction."
- **Score 1-4 (Red):** At risk. AI suggests recovery: "Escalate to Patrick" / "Send recovery email with special offer." If the client is Flagship tier, this triggers a Teams alert to Patrick.

#### Feedback loop: deals inform health, health informs deal strategy

```
Email arrives -> deal_activity created -> interaction record updated
  -> health score recalculates (weekly batch or on-demand)
  -> Kanban card health dot updates
  -> AI next-action recommendation adjusts tone/urgency
  -> Staff acts on recommendation
  -> New deal_activity created -> cycle repeats
```

---

### 15. Ten "Stolen Features" from the CRM Landscape

Each feature below was identified from the CRM landscape research (Pipedrive, HubSpot, Attio, Folk, Monday, Moonstride, Twenty). For each: what the commercial tool does, how Second Brain implements it natively, and why the native version is better for a DMC.

#### Feature 1: Auto-Enrichment + Magic Fields (from Attio/Folk)

**What they do:** Attio and Folk auto-populate company and contact records from web scraping — LinkedIn profiles, company size, industry, social links. "Magic fields" that fill themselves.

**Second Brain equivalent:** Email mining via n8n extracts client name, contact name, role, company, pax, dates, destination, segment — all from the email body. No web scraping needed because DMC clients reveal everything in their inquiry emails. The 107 client profiles already extracted from the email archive prove this works.

**Why ours is better for DMC:** Commercial auto-enrichment pulls generic business data (company size, LinkedIn headline). DMC needs travel-specific data: preferred destinations, typical pax range, margin tolerance, booking patterns, seasonal preferences. This only exists in email correspondence, not on LinkedIn.

#### Feature 2: Next-Activity Forcing with AI Recommendations (from Pipedrive philosophy)

**What they do:** Pipedrive's core philosophy: always have a next activity scheduled. If a deal has no next activity, it surfaces as a warning.

**Second Brain equivalent:** `deals.next_action` and `deals.next_action_due` fields, enforced by: (a) n8n W3 stale alerts for deals with no next action, (b) morning dashboard Section 2 showing overdue actions, (c) Claude Haiku generating 1-line suggestions for stale deals.

**Why ours is better for DMC:** Pipedrive requires staff to manually set the next activity after every interaction. Second Brain auto-suggests next actions based on deal stage, client history, and email content. Staff reviews and approves rather than inventing from scratch.

#### Feature 3: Deal Rotting + Stale Alerts (from HubSpot)

**What they do:** HubSpot's "deal rot" feature highlights deals that have been in a stage too long. Configurable thresholds per stage.

**Second Brain equivalent:** `deals.stale_days` is a computed column that updates automatically. n8n W3 runs daily at 08:00 Helsinki, queries deals with stale_days > 7, and sends Teams adaptive cards per staff member. Kanban cards color-code: green (<3 days), yellow (3-7 days), red (>7 days).

**Why ours is better for DMC:** HubSpot stale alerts are generic. Second Brain's alerts include AI-generated context: "AHI Travel proposal viewed 5 days ago, no reply — consider calling Lars directly. Historical pattern: AHI responds within 3 days 80% of the time, this is unusual."

#### Feature 4: Pax + Seasonal Pricing Calculator (from Moonstride)

**What they do:** Moonstride has a built-in pricing engine with seasonal rates, pax tiers, and supplier NET/GROSS calculations.

**Second Brain equivalent:** Auto-pricing calculator (Section 11) with rate_cards table, seasonal lookups, pax-tier matching, commission logic with exception handling, and a flag system for expired/missing rates.

**Why ours is better for DMC:** Moonstride's pricing is locked inside Moonstride. Our pricing calculator feeds directly into Email Drafter proposals, integrates with TravelTree itineraries via API, and generates pricing blocks that match each staff member's email style. The pricing data also feeds the win-rate engine — we know which price points win for which market segments.

#### Feature 5: AI Proposal Draft with Full Context (from Folk + Claude)

**What they do:** Folk has basic email templates with merge fields. Some users wire Folk to Claude for drafting.

**Second Brain equivalent:** Email Drafter (Product 2) pulls full client context from Second Brain: 24-month interaction history, relationship health score, preferred language, staff writing style, commission rules, seasonal pricing. Generates complete proposal emails, not templates with merge fields.

**Why ours is better for DMC:** Folk's integration is generic — Claude sees company name and recent emails. Our Email Drafter sees the entire relationship: "Wikinger Reisen, 4/4 proposals won, 100% win rate, €316,600 revenue, prefers Aurora programs in Lapland, contact Lars at decision-maker level, last interaction was positive about January series." The proposal practically writes itself.

#### Feature 6: Auto-Moving Kanban Based on Email Activity (from Monday + automation)

**What they do:** Monday.com + integrations can move cards between columns based on email events (sent, received, opened).

**Second Brain equivalent:** n8n W2 auto-stage-progression. Email classification detects: proposal sent (attachment MIME check), client reply (threading), confirmation keywords (NLP), and moves deals between stages automatically. High-confidence moves happen silently; medium-confidence moves create pending notifications for staff approval.

**Why ours is better for DMC:** Monday requires custom automations per scenario. Our n8n pipeline understands DMC-specific email patterns: "A client reply to a proposal is NOT automatically a revision request" (many CRMs get this wrong). The classification model knows that travel industry email patterns differ from SaaS sales patterns.

#### Feature 7: Commission + Supplier Bookkeeping (from Moonstride)

**What they do:** Moonstride tracks supplier NET rates, calculates commissions, and manages supplier payments.

**Second Brain equivalent:** suppliers + rate_cards tables (Section 10) with commission tracking per service, exception rules, and validity periods. Supplier bookkeeping flows: rate_cards feed pricing calculator -> pricing calculator feeds proposal -> proposal outcome feeds deal -> deal confirmation triggers supplier booking workflow (Phase 5 build).

**Why ours is better for DMC:** Moonstride's commission tracking is isolated inside Moonstride. Our commission data feeds the win-rate engine (which commission levels win deals?), the relationship health score (are we pricing competitively for this client?), and the Email Drafter (auto-include correct commission in pricing blocks). Data flows everywhere it is needed.

#### Feature 8: Trackable Proposal Links with Open Notifications (from Pipedrive Smart Docs)

**What they do:** Pipedrive Smart Docs generates trackable links. Staff gets notified when the client opens the document.

**Second Brain equivalent:** SharePoint sharing links via M365 Graph API (primary) + custom redirect URLs as fallback. n8n W4 polls Graph analytics or receives webhook on access. Creates deal_activity (type = `proposal_viewed`) and notifies deal owner via Teams.

**Why ours is better for DMC:** Pipedrive tracks opens of Pipedrive-hosted documents. Our system tracks opens of SharePoint-hosted proposals (data sovereignty — proposals stay on Finland DMC's infrastructure) AND TravelTree itinerary links (if TT implements view notifications). "Client viewed your proposal 3 days ago but hasn't replied" is a specific, actionable signal that feeds the stale deal alert system.

#### Feature 9: Mobile Offline Updates (from Pipedrive/Monday)

**What they do:** Pipedrive and Monday have native mobile apps with offline support. Staff can update deals from a taxi between client meetings.

**Second Brain equivalent:** PWA (Progressive Web App) — same Next.js codebase, works on mobile browsers, supports offline via service worker. Deal updates (stage change, quick note, next action) cached locally and synced when online.

**Why ours is better for DMC:** Native apps require App Store approval, separate codebase, and update cycles. PWA ships instantly with web updates. For a 5-person team, a PWA is the correct mobile strategy. The key mobile action for DMC staff is reading the morning dashboard and adding quick notes — not complex deal editing.

#### Feature 10: Self-Hosted Data Layer (from Twenty CRM)

**What they do:** Twenty is open-source, self-hostable CRM. All data on your own server. No vendor lock-in.

**Second Brain equivalent:** Supabase (self-hostable PostgreSQL) on Hetzner VPS. All client data, deals, interactions, supplier rates — owned and hosted on European infrastructure. No data in Pipedrive's servers, no data in Monday's servers, no vendor lock-in. Export = `pg_dump`.

**Why ours is better for DMC:** Twenty gives you a CRM UI but requires building all DMC-specific features as custom objects. Our system gives you the same data sovereignty PLUS all 9 features above built specifically for DMC workflows. The database is portable; the intelligence layer is proprietary.

---

### 16. n8n Workflow Additions (4 new workflows)

These extend the existing 8-node email pipeline.

**W1: Email -> Deal Auto-Creation**
- Trigger: new email in info@finlanddmc.fi (M365 Graph API subscription)
- Classify email: `new_inquiry` | `existing_deal` | `non_deal`
- If `new_inquiry`: Claude Sonnet extracts client, pax, dates, destination, value estimate -> INSERT deals + deal_activities
- If `existing_deal`: match to deal via client_id + date range -> UPDATE last_activity, INSERT activity

**W2: Stage Auto-Progression**
- Trigger: new email classified as reply to existing deal
- Rules: staff sends PDF -> `proposal_sent`; 2nd+ PDF -> `revision`; client confirms -> `confirmed` (pending approval); trip dates pass -> `invoiced` reminder
- Every stage change -> INSERT deal_stage_history

**W3: Stale Deal Alerts**
- Trigger: daily cron 08:00 Helsinki
- Query: deals WHERE stale_days > 7 AND stage NOT IN (won, lost, invoiced)
- Action: Teams adaptive card per staff member with AI-generated suggestions (Haiku, ~$0.01/day)

**W4: Proposal Tracking Webhook Receiver**
- Trigger: HTTP webhook or Graph API poll every 4h
- Receives: SharePoint sharing link access events or custom redirect URL hits
- Action: UPDATE deals.last_activity, INSERT deal_activity (proposal_viewed), notify deal owner

---

### 17. Frontend Components (Next.js)

Four components added to the FinnConcierge codebase.

| Component | Effort | Description |
|---|---|---|
| Pipeline Kanban Board | ~40h | 8 columns, drag-and-drop (@dnd-kit/sortable), Supabase Realtime, filters by staff/season/value/tier |
| Deal Detail Drawer | ~24h | Slides open on card click. Activity timeline, client profile, AI panel (health + probability + next action), edit fields |
| Daily Dashboard | ~16h | Staff landing page. 7 sections (Section 13 above). Server-side generated. |
| Activity Logger | ~8h | Quick-add for calls, meetings, notes. Pre-populated with deal context. Minimal — most activities auto-logged. |
| **Total** | **~88h** | **11 working days** |

---

### 18. Development Effort & Cost Summary

#### Build estimate (1 developer, full-time)

| Component | Hours | Weeks |
|---|---|---|
| Database schema + RLS + migrations (tables 10-14) | 12 | 0.3 |
| n8n W1: email-to-deal pipeline | 16 | 0.4 |
| n8n W2: stage auto-progression | 12 | 0.3 |
| n8n W3: stale deal alerts | 4 | 0.1 |
| n8n W4: proposal tracking webhook | 8 | 0.2 |
| Frontend: Kanban board | 40 | 1.0 |
| Frontend: Deal detail drawer | 24 | 0.6 |
| Frontend: Daily dashboard | 16 | 0.4 |
| Frontend: Activity logger | 8 | 0.2 |
| Rate card manager UI (CRUD) | 16 | 0.4 |
| Auto-pricing calculator logic | 12 | 0.3 |
| M365 Graph API calendar integration | 12 | 0.3 |
| Testing + polish | 24 | 0.6 |
| **TOTAL** | **204** | **5.1 weeks** |

Realistic with buffer: **7 weeks** (one developer, full-time). This includes supplier management tables and pricing calculator beyond Agent 2's original 172h estimate.

#### 3-Year TCO (Custom path)

| Cost Category | Year 1 | Year 2 | Year 3 | 3-Year Total |
|---|---|---|---|---|
| Infrastructure (Hetzner + Supabase + Claude API) | €450 | €600 | €600 | €1,650 |
| Initial build (204h x €80/h) | €16,320 | - | - | €16,320 |
| Ongoing maintenance (4h/mo x €80/h) | €2,560 | €3,840 | €3,840 | €10,240 |
| Feature additions (est. 40h/yr) | €1,600 | €3,200 | €3,200 | €8,000 |
| **Year total** | **€20,930** | **€7,640** | **€7,640** | **€36,210** |

vs Pipedrive (€34,780 3yr) — Custom is €1,430 cheaper at 3 years despite higher Year 1 investment, and solves data entry.
vs Moonstride (€38,260 3yr) — Custom saves €2,050 over 3 years and avoids dual-system data entry.

#### Recommended build sequence

| Phase | Weeks | What Ships |
|---|---|---|
| Phase 1 | Week 1 | Temp Kanban in Microsoft Planner (Day 1 visibility) |
| Phase 2 | Weeks 2-3 | Database tables + n8n email-to-deal + morning Teams digest |
| Phase 3 | Weeks 3-4 | Rate card manager + auto-pricing calculator |
| Phase 4 | Weeks 4-5 | Kanban board + deal drawer (replaces Planner) |
| Phase 5 | Weeks 5-6 | Proposal tracking + stale alerts + daily dashboard |
| Phase 6 | Week 7 | PWA + testing + polish |
| Phase 7 | Month 3 | Checkpoint: if >=3/5 staff use daily -> continue. If <2/5 -> feedback + Moonstride fallback. |

---

### 19. Complete Schema Overview (14 tables)

For reference, the full Supabase schema after all additions:

| # | Table | Origin | Purpose |
|---|---|---|---|
| 1-9 | (existing Second Brain tables) | Original design | Clients, contacts, interactions, etc. |
| 10 | **deals** | CRM extension | Pipeline deals with stage tracking |
| 11 | **deal_activities** | CRM extension | Activity log per deal |
| 12 | **deal_stage_history** | CRM extension | Stage transition audit trail |
| 13 | **suppliers** | Supplier mgmt | Supplier profiles with quality/reliability scores |
| 14 | **rate_cards** | Supplier mgmt | Seasonal/pax pricing with commission rules |

All tables use `company_id` for RLS. All new tables reference existing tables (clients, contacts) via foreign keys. No breaking changes to existing schema.

---

*Extended design complete. 19 sections. Original Second Brain design preserved in Part A (Sections 1-8). CRM/pipeline extensions in Part B (Sections 9-19). All pricing, schema, and workflow designs sourced from Agent 2 (Technical Architect) and Agent 3 (DMC Operations) analyses.*
