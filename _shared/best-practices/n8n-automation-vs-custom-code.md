# n8n vs Custom Code — Automation Architecture Decision

**Source:** Session 96 (2026-03-19) — n8n error handler build + Grok Heavy validation
**Confidence:** 0.8 (Grok 4-agent council validated, Benjamin LOC numbers verified independently)

---

## The Rule

**Use HYBRID for any stack that includes Microsoft Graph API webhooks.**
n8n for email ingestion only. Custom code (TypeScript/Supabase) for everything else.

**Never go full-code on Graph API webhooks in serverless.** Silent drop risk is existential for businesses where missed inbound emails = lost deals.

---

## Why (Grok-validated 2026-03-19)

### Microsoft Graph API webhook failure modes in serverless

- Endpoint must return `2xx` in **<10 seconds** or marked "slow"
- >10% of requests >10s in 10-minute window → **10-second notification delays**
- >15% drops → **silent notification blackout up to 10 minutes** — zero error on subscription status
- Vercel/Supabase Edge cold start (200-400ms Deno 2) + async Supabase insert → easily pushes past 10s
- Real incidents: 1-1.5h email blackouts reported March 2026 (Microsoft Q&A)

### LOC comparison (Benjamin estimate, independently verified)

| Approach | Effort | Maintenance surface |
|----------|--------|---------------------|
| n8n (8 nodes) | ~0 custom code | Low — visual debug, no deploys |
| Next.js API route + Supabase Edge | 280-600 LOC | 4-5× higher + external queue needed |

Custom code for Graph webhooks requires: validation handshake + decryption + clientState + lifecycle events + subscription renewal cron + queue fallback + logging circuit breaker.

### n8n "visual debt" is real but scope-dependent

SMB teams with >5-7 complex CRM workflows abandon pure n8n (2025-2026 reports: Reddit r/n8n, Medium). BUT for a single-purpose email ingestion pipeline, the visual canvas is a debugging advantage, not a liability. 6-person teams can't diagnose a 400 LOC webhook handler at 2am.

---

## Decision Matrix

| Use-case | Recommendation | Key risk if wrong |
|---|---|---|
| Email ingestion (Graph API webhooks) | **n8n** | Silent email drops → lost B2B deals |
| Deal stage automation (DB-triggered) | **Full code** — Supabase triggers | None material |
| Stale deal alerts (scheduled) | **Full code** — pg_cron | Edge CPU limits on complex logic |
| Proposal tracking | **Full code** | None material |
| Error monitoring for n8n itself | **n8n** (Global Error Handler) | |

---

## Security: Never hardcode API keys in n8n JSON

n8n workflow JSON exported from UI contains credential IDs — not actual keys (when using n8n credential store). Never paste raw API keys into JSON files — use n8n Credentials UI instead. Keys in JSON = keys in Git.

**Supabase in n8n:** Use native Supabase node (not HTTP Request) — credential stored encrypted in n8n, no API key in workflow JSON.

---

## What to Preserve from n8n Work (Reuse Checklist)

When moving away from n8n to custom code, these patterns are 90% portable:

| Asset | Reuse format |
|---|---|
| `n8n_errors` Supabase schema | ✅ Copy SQL directly — table structure is platform-agnostic |
| Circuit breaker logic | ✅ Port to TypeScript shared lib — same COUNT + threshold pattern |
| Error categorization (error_type field) | ✅ Use as enum in TypeScript types |
| Deduplication (execution_id UNIQUE) | ✅ Constraint already in schema |
| Payload truncation guards (50KB / 2000 chars) | ✅ Copy as constants to TS error handler |

**What is throwaway:** n8n visual sub-workflow orchestration, node connection wiring.

---

## The n8n Error Handler Files (in _drafts/)

- `n8n-global-error-handler.json` — 8-node workflow, circuit breaker, Supabase logging, Teams notify
- `n8n-meta-error-handler.json` — catches errors in the error handler itself
- `n8n-errors-schema.sql` — 15-column schema, UNIQUE on execution_id, ON CONFLICT DO NOTHING

**Status:** Supabase schema deployed and verified. JSON files ready to import — need credential IDs from n8n UI before import. Teams node disabled pending Frendy OAuth2 admin consent.

**Deployment trigger:** When email ingestion pipeline (Graph API → Supabase) is built.

---

## Named Alternative Not Considered

**Pipedream** — developer-first serverless with native Graph webhook source, built-in queuing, TypeScript steps, generous free tier. Better than n8n for teams already coding in TS/Next.js. BUT: adds third vendor — risky for 6-person DMC already on Next.js + Supabase. Evaluate if n8n self-hosted becomes a burden.

**Self-hosted n8n on Hetzner:** €6-10/mo, free license, full reuse of existing JSON files. Zero new infrastructure — routes clean events to Supabase via single HTTP call.

---

## When to Apply This Pattern

- Any project with Microsoft Graph API webhook ingestion
- Any SMB team (< 10 people) choosing between automation platform and custom code
- Any "we should go full-code" refactor decision where Graph/external webhooks are involved
