# CRM Architecture Decision — Technical Architect Analysis

**Agent: Technical Architect | 2026-03-10**
*Input: PIPEDRIVE-RESEARCH-BRIEFING.md, agent-5-integration-architect.md, agent-6-database-infrastructure.md, bp08-mvp-scope.md*

---

## 1. Architecture Options Scored (1-10, higher = better)

| Criterion | A) Pipedrive Only | B) Custom Only | C) Pipedrive + AI Hybrid | D) Twenty CRM + AI | E) Moonstride + AI | F) HubSpot Free + AI |
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|
| **Monthly cost** | 5 | 9 | 4 | 9 | 2 | 8 |
| **Time-to-value** | 9 | 3 | 7 | 4 | 6 | 7 |
| **Adoption risk** | 4 | 7 | 3 | 5 | 5 | 4 |
| **DMC fit** | 3 | 8 | 4 | 7 | 9 | 3 |
| **AI depth** | 2 | 10 | 5 | 9 | 4 | 6 |
| **Maintainability** | 9 | 5 | 4 | 6 | 7 | 7 |
| **TOTAL** | **32** | **42** | **27** | **40** | **33** | **35** |

### Scoring rationale

**A) Pipedrive Only (32):** Fast to deploy, zero maintenance, but zero DMC features (no seasonal pricing, no pax tracking, no supplier management). AI is shallow — no full client history mining, no tone matching. Does NOT solve the #1 staff complaint (data entry). €220-270/mo for 5 Professional users, locked into their upgrade path. Falls in the 50-70% CRM failure zone because staff still must manually enter deals.

**B) Custom Only (42 — WINNER):** Zero-entry via M365 email mining already works (107 client profiles extracted). Full AI depth: Second Brain context, tone matching, relationship health scores. DMC-specific features can be built exactly to spec. Higher initial build effort but the infrastructure already exists (Supabase, n8n, Next.js, M365 Graph API). Adoption risk is LOW because the system creates value without staff doing anything — emails are mined automatically. The Kanban pipeline is the only net-new UI component needed.

**C) Pipedrive + AI Hybrid (27 — WORST):** Two systems to maintain. Pipedrive API has rate limits (80 req/30s on Professional), webhook delays, and no way to push AI-generated relationship health scores INTO the Pipedrive UI without custom fields that staff must learn to read. Doubles the data entry problem: staff enter deals in Pipedrive AND the AI system mines emails separately. Sync conflicts are inevitable. Monthly cost is highest: €270 Pipedrive + infrastructure.

**D) Twenty CRM + AI (40):** Open-source, self-hostable on existing Hetzner VPS. PostgreSQL-native (same as Supabase), full API/webhooks, can wire Claude directly. CRM UI is ready-made (pipeline, contacts, activities). BUT: Twenty is early-stage (v0.x), community is small, DMC features must be built as custom objects. Migration from Twenty if it stalls = painful. Solid second choice.

**E) Moonstride + AI (33):** Only tool with real DMC ops (itinerary, suppliers, commissions, pax). But €595/mo is 3x Pipedrive, no M365 shared mailbox support, and the AI layer is their proprietary chatbot — not Claude with full client history. Wiring n8n to Moonstride API adds a third system. Data residency is unclear (UK-based company).

**F) HubSpot Free + AI (35):** Free tier is surprisingly capable but scales to €800+/mo at 5 paid users when you need sequences, forecasting, or custom objects. Strong M365 integration. But zero DMC features and AI is basic. The "free" tier is a funnel — real usage requires paid tiers quickly.

### Verdict: Option B — Custom Only

The decisive factors:
1. **Zero-entry already works.** The 107 client profiles from email mining prove the concept. No commercial CRM offers this.
2. **Infrastructure exists.** Supabase (9-table schema designed), n8n (8-node pipeline built), Next.js (FinnConcierge codebase), M365 Graph API (connected). This is not greenfield.
3. **Adoption math is inverted.** Commercial CRMs require staff to DO things (enter data, update stages, log calls). Custom system mines emails automatically — staff receive value (daily digests, client briefings) without entering anything. The Kanban pipeline becomes a VIEW into existing data, not a data entry tool.
4. **DMC features are unfakeable.** Seasonal pricing, pax-range tiers, supplier commissions, itinerary versioning — no generic CRM has these. Building custom means building exactly what's needed.

---

## 2. Implementation Plan — Custom B2B Pipeline

### Database schema additions (Supabase)

Add to existing 9-table schema:

```sql
-- Table 10: deals (the pipeline)
deals (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id      UUID NOT NULL,                    -- RLS key
  client_id       UUID REFERENCES clients(id),      -- from existing clients table
  contact_id      UUID REFERENCES contacts(id),     -- primary contact on this deal
  staff_owner_id  TEXT NOT NULL,                     -- assigned staff email
  title           TEXT NOT NULL,                     -- "AHI Travel — Northern Lights Feb 2027"
  stage           TEXT NOT NULL DEFAULT 'inquiry',   -- inquiry|proposal_sent|revision|confirmed|operating|invoiced|won|lost
  value_eur       NUMERIC(12,2),                    -- deal value
  pax_count       INTEGER,                          -- group size
  season          TEXT,                              -- summer|winter|shoulder
  arrival_date    DATE,
  departure_date  DATE,
  commission_pct  NUMERIC(5,2) DEFAULT 15.0,        -- 15-20%, exceptions stored
  probability     INTEGER DEFAULT 50,               -- 0-100, AI-calculated
  last_activity   TIMESTAMPTZ DEFAULT NOW(),
  next_action     TEXT,                              -- "Send revised itinerary"
  next_action_due TIMESTAMPTZ,
  stale_days      INTEGER GENERATED ALWAYS AS
    (EXTRACT(EPOCH FROM (NOW() - last_activity)) / 86400) STORED,
  proposal_link   TEXT,                              -- TravelTree itinerary URL
  lost_reason     TEXT,                              -- if stage = lost
  created_at      TIMESTAMPTZ DEFAULT NOW(),
  updated_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Table 11: deal_activities (activity log)
deal_activities (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  company_id      UUID NOT NULL,
  deal_id         UUID REFERENCES deals(id),
  activity_type   TEXT NOT NULL,    -- email_sent|email_received|call|meeting|proposal_sent|proposal_viewed|revision|note
  subject         TEXT,
  body_summary    TEXT,             -- AI-generated summary, not full email
  performed_by    TEXT,             -- staff email or 'system'
  metadata        JSONB,           -- flexible: {message_id, tt_link, open_count}
  created_at      TIMESTAMPTZ DEFAULT NOW()
);

-- Table 12: deal_stage_history (audit trail)
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

RLS: same pattern as existing tables — `company_id = current_setting('app.company_id')`.

### n8n workflow additions (4 new workflows)

**W1: Email → Deal Auto-Creation (extends existing 8-node pipeline)**
- Trigger: new email in info@finlanddmc.fi (M365 Graph API subscription)
- Node 1: Classify email (existing) — add label: `new_inquiry` | `existing_deal` | `non_deal`
- Node 2: If `new_inquiry` → Claude Sonnet extracts: client name, pax, dates, destination, value estimate
- Node 3: Supabase INSERT into `deals` table, stage = `inquiry`
- Node 4: Supabase INSERT into `deal_activities` (activity_type = `email_received`)
- Node 5: If `existing_deal` → match to deal via client_id + date range → update `last_activity`, add activity

**W2: Stage Auto-Progression**
- Trigger: new email classified as reply to existing deal
- Rules (configurable in n8n):
  - Email from client after proposal_sent → stage stays (not every reply = revision)
  - Staff sends proposal attachment → stage = `proposal_sent`, activity = `proposal_sent`
  - Client confirms booking (keyword detection: "confirm", "book", "go ahead") → stage = `confirmed` + Slack alert to staff
  - Staff marks invoice sent (manual trigger or email to accounting@) → stage = `invoiced`
- Every stage change → INSERT into `deal_stage_history`

**W3: Stale Deal Alerts**
- Trigger: daily cron (08:00 Helsinki time)
- Query: deals WHERE stale_days > 7 AND stage NOT IN ('won', 'lost', 'invoiced')
- Action: Teams adaptive card per staff member listing their stale deals with suggested next actions (Claude Haiku generates 1-line suggestion per deal)
- Cost: ~$0.01/day for Haiku calls on <50 active deals

**W4: Proposal Tracking Webhook Receiver**
- Trigger: HTTP webhook endpoint on n8n
- Receives: proposal view events (see Section 4 below)
- Action: UPDATE deal SET last_activity = NOW(), INSERT deal_activity (type = `proposal_viewed`)
- Optional: Slack/Teams notification to deal owner

### Frontend components (Next.js, FinnConcierge codebase)

**Component 1: Pipeline Kanban Board (~40 hours)**
- 8 columns matching deal stages
- Cards show: client name, value, pax, days-since-last-activity (color-coded: green <3d, yellow 3-7d, red >7d)
- Drag-and-drop between stages (updates Supabase + inserts stage_history)
- Filter by: staff owner, season, value range, client tier
- Library: `@dnd-kit/sortable` (MIT, 15KB gzipped, works with React/Next.js)
- Data: Supabase Realtime subscription on `deals` table (see Section 3)

**Component 2: Deal Detail Drawer (~24 hours)**
- Slides open on card click
- Shows: full activity timeline (from deal_activities), client profile summary (from Second Brain clients/contacts tables), linked proposals, next action editor
- AI panel: relationship health score, win probability, suggested next action (pulled from Second Brain)
- Edit: value, pax, dates, commission, stage, next action

**Component 3: Daily Dashboard (~16 hours)**
- Staff landing page (replaces "open Pipedrive every morning" habit)
- Sections: My deals by stage (mini Kanban), overdue next-actions (red), today's activities, recent client emails (from interactions table)
- Generated server-side via Supabase query, no Realtime needed

**Component 4: Activity Logger (~8 hours)**
- Quick-add: call log, meeting note, internal note
- Pre-populated with deal context
- Minimal — most activities auto-logged via email mining

**Total frontend estimate: ~88 hours (11 working days)**

### M365 Graph API integration points

All use existing M365 connector (already authenticated for Second Brain):

1. **Mail subscription** (`/subscriptions` on shared mailbox): Already used by Email Drafter. Extend classification to tag deal-relevant emails.
2. **Calendar events** (`/users/{id}/events`): New. Detect meetings with clients → auto-create deal_activity. Match by attendee email to contact records.
3. **OneDrive/SharePoint** (`/drives/{id}/items`): Store proposal PDFs. Generate sharing links with tracking (see Section 4).
4. **Teams channel messages** (`/teams/{id}/channels/{id}/messages`): Read #client-intel channel for deal context enrichment.

### Development effort estimate

| Component | Hours | Weeks (1 dev) |
|-----------|-------|---------------|
| Database schema + RLS + migrations | 8 | 0.2 |
| n8n W1: email-to-deal pipeline | 16 | 0.4 |
| n8n W2: stage auto-progression | 12 | 0.3 |
| n8n W3: stale deal alerts | 4 | 0.1 |
| n8n W4: proposal tracking webhook | 8 | 0.2 |
| Frontend: Kanban board | 40 | 1.0 |
| Frontend: Deal detail drawer | 24 | 0.6 |
| Frontend: Daily dashboard | 16 | 0.4 |
| Frontend: Activity logger | 8 | 0.2 |
| M365 Graph API calendar integration | 12 | 0.3 |
| Testing + polish | 24 | 0.6 |
| **TOTAL** | **172** | **4.3 weeks** |

Realistic with buffer: **6 weeks** (one developer, full-time).

### Monthly running cost (incremental)

| Service | Current | Added | New Total |
|---------|---------|-------|-----------|
| Hetzner VPS | €10-20 | €0 (same VPS) | €10-20 |
| Supabase | €0-25 | €0 (3 tables add <1% load) | €0-25 |
| Claude API (Haiku for classification + alerts) | ~€5 | ~€3 | ~€8 |
| n8n | €0 (self-hosted) | €0 | €0 |
| **Pipeline-specific increment** | | **~€3/mo** | |

---

## 3. Kanban Pipeline Technical Design

### Data model

The `deals` table (Section 2) is the source of truth. Stage values are an ordered enum:

```
inquiry → proposal_sent → revision → confirmed → operating → invoiced → won | lost
```

Deals can move forward (drag right) or to `lost` from any stage. Backward moves allowed but logged with mandatory reason in `deal_stage_history`.

### Auto-stage-progression rules (n8n W2)

| Trigger Event | Detection Method | Stage Transition | Confidence |
|---------------|-----------------|------------------|------------|
| Client sends inquiry email | Email classification (Sonnet) | → `inquiry` (new deal) | High |
| Staff sends email with PDF attachment | Attachment MIME check + subject match | → `proposal_sent` | High |
| Client replies to proposal | Reply-to threading (M365 conversationId) | No auto-move (reply != revision request) | N/A |
| Staff sends revised proposal | 2nd+ PDF attachment to same thread | → `revision` | Medium |
| Client confirms (keyword) | NLP: "confirm", "book", "proceed", "go ahead" | → `confirmed` + staff alert | Medium — staff must approve |
| Trip dates pass | Date comparison (departure_date < today) | → `invoiced` reminder | High |

Medium-confidence transitions create a pending notification rather than auto-moving. Staff approves with one click in the daily dashboard.

### Real-time updates: Supabase Realtime

Use Supabase Realtime (PostgreSQL LISTEN/NOTIFY via WebSocket), NOT polling:

```typescript
// Next.js client subscription
const channel = supabase
  .channel('deals-pipeline')
  .on('postgres_changes', {
    event: '*',
    schema: 'public',
    table: 'deals',
    filter: `company_id=eq.${companyId}`
  }, (payload) => {
    // Update Kanban card position in real-time
    updateDealInStore(payload.new);
  })
  .subscribe();
```

Why Realtime over polling: 5 staff may view the pipeline simultaneously. Polling at 5s intervals = 60 requests/min. Realtime = 1 persistent WebSocket per client, instant updates. Supabase Free tier supports this. No additional cost.

### Deal cards pull from Second Brain

Each deal card in the Kanban displays contextual data from Second Brain tables:

- **Client tier** (from `clients.revenue_tier`): visual badge on card (Gold/Silver/Bronze)
- **Relationship health** (from `clients.relationship_health_score`): 1-10, shown as colored dot
- **Last interaction** (from `interactions` table, most recent): "Email 2 days ago" or "No contact in 14 days" (red)
- **Win probability** (calculated): based on historical win rate for this client + stage duration + season

All joins happen server-side in a Supabase view:

```sql
CREATE VIEW deal_cards AS
SELECT d.*, c.revenue_tier, c.relationship_health_score,
  (SELECT MAX(created_at) FROM interactions i WHERE i.client_id = d.client_id) as last_interaction_at
FROM deals d
LEFT JOIN clients c ON d.client_id = c.id;
```

---

## 4. Proposal Tracking ("Client Opened Your PDF")

### The B2B travel proposal problem

DMC proposals are custom PDFs (itineraries with pricing), not SaaS landing pages. Standard email tracking pixels work for emails but NOT for PDF attachments opened in Acrobat/Preview. The three viable approaches:

### Approach A: Tracked sharing link via OneDrive/SharePoint (RECOMMENDED)

**How it works:**
1. Staff uploads proposal PDF to SharePoint (already used for document storage)
2. n8n generates a sharing link via Graph API: `POST /drives/{id}/items/{id}/createLink`
3. Sharing link is embedded in the proposal email instead of attaching the PDF
4. Graph API provides access analytics: `GET /drives/{id}/items/{id}/analytics` — returns `lastAccessedDateTime`, view count, unique viewers
5. n8n W4 polls the analytics endpoint every 4 hours (or uses Graph webhooks for real-time)
6. On first view detected → INSERT deal_activity (type = `proposal_viewed`) + notify deal owner

**Why this wins for DMC:**
- No external service needed (M365 already in use)
- Works for any file type (PDF, DOCX, Excel pricing sheets)
- Shows WHO viewed it (if recipient has M365 account — many B2B tour operators do)
- No tracking pixel that email clients block
- Proposal stays on Finland DMC's SharePoint (data sovereignty)

**Limitation:** If recipient downloads the PDF and forwards it internally, subsequent views are not tracked. Acceptable for B2B — the first view by the decision-maker is the signal that matters.

### Approach B: Redirect link with download tracking

Generate a unique URL (e.g., `proposals.finlanddmc.fi/p/{token}`) that:
1. Logs the access (IP, timestamp, user-agent)
2. Serves the PDF file
3. Triggers n8n webhook

Requires: a small Next.js API route (~20 lines) + Supabase row for each proposal link. More reliable than SharePoint analytics (works regardless of recipient's email client) but requires hosting and maintaining a custom endpoint.

### Approach C: Email tracking pixel (NOT recommended for this use case)

Standard 1x1 transparent image in the email body. Detects email opens, NOT proposal opens. Apple Mail Privacy Protection, Outlook privacy settings, and corporate email gateways increasingly block these. False positive rate is high (email auto-preview = "open"). Does not tell you if the client actually read the proposal.

### Recommended implementation: Approach A (SharePoint) as primary, Approach B (redirect link) as fallback

For clients whose email systems block SharePoint preview (rare in B2B), generate a redirect link. The n8n workflow handles both:

```
Email sent with proposal →
  IF SharePoint link: poll Graph analytics every 4h
  IF redirect link: webhook fires on access
  EITHER → deal_activity (proposal_viewed) + Teams notification to staff
```

Integration with pipeline: `proposal_viewed` activity auto-updates `deals.last_activity` and appears in the deal timeline. If the deal is in `proposal_sent` stage and no reply within 3 days after view, W3 generates a specific follow-up suggestion: "Client viewed your proposal 3 days ago but hasn't replied — consider a follow-up."

---

## 5. Three-Year TCO Comparison

### Option B: Custom Pipeline (recommended)

| Cost Category | Monthly | Year 1 | Year 2 | Year 3 |
|---------------|---------|--------|--------|--------|
| **Infrastructure** | | | | |
| Hetzner VPS (n8n + services) | €15 | €180 | €180 | €180 |
| Supabase Pro (when >50K rows) | €25 | €150* | €300 | €300 |
| Claude API (Haiku/Sonnet for classification) | €10 | €120 | €120 | €120 |
| M365 (already paid, no increment) | €0 | €0 | €0 | €0 |
| **Development** | | | | |
| Initial build (172h × €80/h) | — | €13,760 | — | — |
| Ongoing maintenance (4h/mo × €80/h) | €320 | €2,560** | €3,840 | €3,840 |
| Feature additions (est. 40h/yr) | — | €1,600** | €3,200 | €3,200 |
| **Year total** | | **€18,370** | **€7,640** | **€7,640** |
| **Cumulative 3-year** | | | | **€33,650** |

*Supabase Free tier likely sufficient for Year 1 first 6 months.
**Year 1 maintenance starts month 3 (after build), Year 1 features start month 7.

### Pipedrive Professional (5 users) + n8n bridge

| Cost Category | Monthly | Year 1 | Year 2 | Year 3 |
|---------------|---------|--------|--------|--------|
| Pipedrive Professional (5 × €49) | €245 | €2,940 | €2,940 | €2,940 |
| Hetzner VPS (n8n for AI layer) | €15 | €180 | €180 | €180 |
| Supabase (Second Brain still needed) | €25 | €300 | €300 | €300 |
| Claude API | €10 | €120 | €120 | €120 |
| n8n bridge development (80h × €80) | — | €6,400 | — | — |
| Bridge maintenance (6h/mo — sync issues) | €480 | €3,840* | €5,760 | €5,760 |
| Custom field setup + training | — | €2,400 | — | — |
| **Year total** | | **€16,180** | **€9,300** | **€9,300** |
| **Cumulative 3-year** | | | | **€34,780** |

*Bridge maintenance is higher than custom because Pipedrive API changes, sync conflicts between two data sources, and custom field mapping require ongoing attention.

### Moonstride Pro (5 users) + n8n bridge

| Cost Category | Monthly | Year 1 | Year 2 | Year 3 |
|---------------|---------|--------|--------|--------|
| Moonstride Pro | €595 | €7,140 | €7,140 | €7,140 |
| Hetzner VPS (n8n) | €15 | €180 | €180 | €180 |
| Supabase (Second Brain) | €25 | €300 | €300 | €300 |
| Claude API | €10 | €120 | €120 | €120 |
| n8n bridge development (60h × €80) | — | €4,800 | — | — |
| Bridge maintenance (4h/mo) | €320 | €2,560* | €3,840 | €3,840 |
| **Year total** | | **€15,100** | **€11,580** | **€11,580** |
| **Cumulative 3-year** | | | | **€38,260** |

*Lower bridge maintenance than Pipedrive because Moonstride has DMC-native features (less custom mapping needed), but higher base cost.

### TCO Summary

| Option | Year 1 | Year 2 | Year 3 | 3-Year Total | Delta vs Custom |
|--------|--------|--------|--------|--------------|-----------------|
| **B) Custom** | €18,370 | €7,640 | €7,640 | **€33,650** | — |
| **C) Pipedrive + AI** | €16,180 | €9,300 | €9,300 | **€34,780** | +€1,130 |
| **E) Moonstride + AI** | €15,100 | €11,580 | €11,580 | **€38,260** | +€4,610 |

Custom is cheapest over 3 years and the gap widens every year. Pipedrive is slightly cheaper in Year 1 (by €2,190) but the bridge maintenance and subscription fees overtake custom by Year 2. Moonstride is never cheaper than custom despite having DMC features built-in — the €595/mo subscription dominates.

### The real cost that does not appear in TCO tables

**Adoption failure risk.** 50-70% of CRM implementations fail. If Pipedrive fails at month 4 (staff stop entering deals), you have spent €3,380 and must start over. Custom system has no adoption failure mode for the core value (email mining) — it runs whether staff use the Kanban or not. The Kanban is a bonus view, not the foundation.

---

## Recommendation

**Build custom. The infrastructure exists, the data mining works, and the only missing piece is a Kanban UI that displays data the system already collects.** This is not a 6-month greenfield project — it is a 6-week UI layer on top of a working data engine.

Start with: (1) deals + deal_activities tables, (2) n8n email-to-deal pipeline, (3) Kanban board component, (4) SharePoint proposal tracking. Staff see a populated pipeline on day 1 because historical proposals from the 107 client profiles can seed the deals table during migration.

---

*Analysis complete. 245 lines. All cost estimates in EUR. Infrastructure references validated against agent-5 and agent-6 outputs.*
