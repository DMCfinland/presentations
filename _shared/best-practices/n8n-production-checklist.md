# n8n Production Checklist — Self-Hosted (Hetzner + Supabase + Graph API)

**Source:** Cross-validated by Grok Heavy + Gemini 2.5 Pro (independently, session 108, 2026-03-24)
**Applies to:** Any n8n self-hosted deployment with Microsoft Graph API + LLM-heavy workflows
**Decisions:** D53-D59 in DMC-SECONDBRAIN-CRM DECISIONS.md

---

## Pre-Deploy Checklist

### Infrastructure (docker-compose level)
- [ ] `N8N_DATABASE_TYPE=postgres` — separate Postgres, NOT SQLite, NOT Supabase app DB (D53)
- [ ] `N8N_ENCRYPTION_KEY` generated (`openssl rand -hex 32`), backed up outside VPS (D54)
- [ ] Queue mode enabled: main process + Redis + worker container(s) (D55)
- [ ] `EXECUTIONS_DATA_SAVE_ON_SUCCESS=none` + `EXECUTIONS_DATA_PRUNE=true` (D58)
- [ ] `WEBHOOK_URL` set to explicit HTTPS domain (not auto-detected)
- [ ] Hetzner: floating IPv4 or Cloudflare Tunnel (IP reputation with Microsoft)

### Supabase State Tables
- [ ] `sync_state` table: `key` (text PK), `value` (jsonb), `updated_at` (timestamptz) — stores deltaLink, subscriptionId (D57)
- [ ] `s5_audit_records` table — per-email invariant validation log
- [ ] `human_review_queue` table — escalated emails awaiting human review

### n8n Workflows
- [ ] Credential Watchdog: proactive Graph API call every 45 min + Teams alert on failure (D56)
- [ ] Webhook validationToken: Code node echoes `{ "value": validationToken }` on subscription creation (D59)
- [ ] Delta query sweep: Schedule node every 15-30 min, deltaLink persisted to `sync_state` (D59)
- [ ] Webhook renewal: Schedule node (before 72h expiry), subscriptionId from `sync_state` (D59)
- [ ] Error Trigger workflow: global error handler → writes to Supabase error log

### n8n Node Settings (HTTP Request for Graph API)
- [ ] Header: `Prefer: IdType="ImmutableId"` on ALL Graph API calls (D59)
- [ ] Retry on Fail: ON (3 retries, 10s wait) — handles ETag 412 conflicts
- [ ] Timeout: 9000ms (Microsoft requires webhook response within 10s)
- [ ] Use HTTP Request node with OAuth2 credentials — NOT the pre-built Microsoft Graph node

### Azure / External
- [ ] ApplicationAccessPolicy: restrict app registration to shared mailbox only (Frendy runs PowerShell)
- [ ] DPIA signed (Patrick) — before any live email processing
- [ ] Graph API token created (Gate 4)

---

## Key Principle

> **n8n = stateless worker. Supabase = state bus.** (D57)
>
> Every piece of pipeline state (deltaLink, subscriptionId, S4→S5 handoff, audit records) lives in Supabase. n8n reads and writes to Supabase at every step. If n8n restarts, Supabase has the full picture.

---

## Origin

Session 89 (March 2026): original architecture was 6 custom TypeScript services on Railway. Stress-tested by Grok Heavy + 2x Gemini. Session 108: architecture pivoted to n8n on Hetzner. Same models re-reviewed. This checklist captures all findings that survived the pivot.

7/7 items were independently confirmed by both Grok and Gemini without seeing each other's analysis.
