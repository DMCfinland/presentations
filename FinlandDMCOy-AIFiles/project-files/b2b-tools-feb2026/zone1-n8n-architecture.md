# Zone 1 — n8n Architecture Design
**Zone:** Zone 1 (B2B, Hetzner Frankfurt)
**Stack:** n8n (self-hosted on Hetzner VPS) + Supabase PostgreSQL
**No Azure Event Grid. No Cosmos DB. Those are Zone 2 only.**

---

## What Zone 1 Does

Internal B2B workflow automation. Finland DMC staff tools.
Inbound B2B emails → AI-drafted proposals → staff review → send.
Second Brain context enrichment at every step.

---

## 8-Node Email Drafter Pipeline

```
INBOUND EMAIL
     ↓
NODE 1 — Parse & Route
  Input: Email webhook (Microsoft 365 webhook via n8n trigger)
  Action: Extract sender email, subject, body
  Output: {from_email, subject, body_raw, received_at}
  Note: Strip display names from headers for GDPR compliance

     ↓
NODE 2 — Identity Resolution (Supabase lookup)
  Input: from_email
  Action: SHA-256 hash email → Supabase lookup → return client_id + preferences
  Output: {client_id, client_company_id, preferences[], last_interactions[], history_summary}
  Note: Raw name stays in Supabase. Pipeline works with client_id from here.
  Latency: ~10-15ms. At B2B volumes (20-50/day): negligible.

     ↓
NODE 3 — Task Detection (Haiku)
  Input: body_raw (stripped of PII sender name)
  Action: Classify email → task_type (proposal_request | follow_up | inquiry | complaint | other)
  Model: Haiku (cheap, mechanical classification)
  Output: {task_type, urgency_flag, language_detected}

     ↓
NODE 4 — Context Assembly
  Input: client_id + task_type + preferences + history_summary
  Action: Build anonymized context packet for Claude
  Output: Structured JSON with pseudonymous IDs + context + task
  Example:
    {
      "client_id": 47,
      "client_company_id": 12,
      "preferences": ["winter_activities", "group_size_12", "luxury_tier_2"],
      "history_summary": "3 proposals sent, 2 converted, avg €2400/group",
      "task_type": "proposal_request",
      "anonymized_request": "[CLIENT_NAME] from [COMPANY] requests winter safari
                             for group of 12, budget €300pp, dates Jan 15-18."
    }

     ↓
NODE 5 — Draft Generation (Sonnet 4.6)
  Input: anonymized context packet + golden_prompt for task_type
  Action: Generate proposal draft
  Model: Sonnet 4.6 (default — matches B2B office productivity benchmark)
  Output: Draft text with [CLIENT_NAME], [COMPANY] placeholders
  Cost: ~$0.03-0.05 per draft at ~2K tokens

     ↓
NODE 6 — Reinsert PII (Supabase lookup #2)
  Input: draft_text + client_id
  Action: Supabase lookup client_id → real name + company → replace placeholders
  Output: Final personalized draft (real names, proper greeting)
  Note: This is the ONLY point where real names enter the draft
  Latency: ~10-15ms. Acceptable.

     ↓
NODE 7 — Staff Delivery
  Input: final_draft + metadata
  Action: Post to Staff Dashboard webhook OR Microsoft Teams notification
  Format: Draft + original email (for context) + quick-action buttons
  Output: Staff sees draft, can approve / edit / reject

     ↓
NODE 8 — Interaction Log (Supabase write)
  Input: {client_id, task_type, draft_sent_at, version_id}
  Action: Write interaction record to Supabase interactions table
  Note: Stores client_id, NOT the actual draft content (that stays in email)
  Output: version_sequence record for conversion tracking later
```

---

## Data Flow Rules

- **Raw PII (names, emails) stays in Supabase (Frankfurt, EU) at all times**
- **Claude API only receives: pseudonymous IDs + preferences + context**
- **PII reinserted ONLY at Node 6, immediately before delivery**
- **No interaction content stored in Supabase — only metadata (client_id, task_type, timestamp)**

---

## Anonymization Cost Analysis

| Step | Latency | Frequency | Cost |
|------|---------|-----------|------|
| Node 2: hash + lookup | ~15ms | Every email | Negligible at 50/day |
| Node 6: name reinsert | ~15ms | Every email | Negligible at 50/day |
| Sonnet draft | ~3-5s | Every email | ~$0.03-0.05 |
| Haiku classify | ~0.5s | Every email | ~$0.001 |

**The two Supabase lookups add ~30ms total to a process that takes 4-6 seconds anyway.**
No quality risk: Claude gets richer context with pseudonymous IDs + structured preferences
than it would with just raw email text. Quality is the same or better.

---

## Zone 1 Stack — No Azure Required

| Component | Tool | Why |
|-----------|------|-----|
| Workflow orchestration | n8n (self-hosted Hetzner) | No rate limits, full control, €15/mo |
| Database | Supabase PostgreSQL (Frankfurt) | EU-resident, pgvector, Row Level Security |
| Email trigger | Microsoft 365 webhook → n8n | Staff already use Outlook |
| Staff dashboard | Simple n8n webhook + HTML page | Phase 1 MVP, replace later |
| AI models | Claude API (Anthropic) | Sonnet for drafts, Haiku for classification |
| Event routing | n8n (internal, no Event Grid) | Event Grid is Zone 2 only |

**n8n rate limits:** Self-hosted on Hetzner = no rate limits. You own the server.
Cloud n8n = limits apply. Use self-hosted.

---

## Zone 1 vs Zone 2 Boundary

```
ZONE 1 (Hetzner, Frankfurt)          ZONE 2 (Azure, Ireland)
─────────────────────────────         ─────────────────────────────────
n8n                                   Azure Event Grid
Supabase PostgreSQL                   Cosmos DB
Email Drafter pipeline                Real-time guest chat
Second Brain (State A+B)              Master Agent / Mood Evaluator
Staff Dashboard (MVP)                 BP_08 Staff Dashboard (production)
Golden prompts store                  RAG indexes (Azure AI Search)
version_sequences                     Traveler PWA (Next.js)
booking_source_metadata               Shadow Ledger (Azure SQL)
```

The Staff Dashboard MVP (n8n webhook + HTML) monitors Zone 1 workflows.
BP_08 (full production) monitors Zone 2 guest conversations via Event Grid + Cosmos DB.
These are two different tools for two different phases.

---

## Second Brain State A → B Transition Trigger

State A (current): Manual copy-paste from M365 into Claude Teams for context
State B (target): n8n NODE 2 automatically pulls Supabase client context

**Trigger conditions for State B:**
1. All 9 Supabase tables have `company_id` column (multi-tenant ready)
2. Contact data imported from email mining sessions
3. Supabase DPA + Hetzner DPA executed (before first data load)

Until trigger: n8n NODE 2 returns empty context → NODE 5 uses task-only context (still works, just less personalized)

---

*Created: 2026-02-23 | Session 50*
