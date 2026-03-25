---
name: n8n-small-vps-production-risk
description: n8n queue mode on ≤4GB VPS fails under real webhook+LLM load — upgrade server and verify CVE before production
type: feedback
---

n8n queue mode on a ≤4GB RAM VPS is NOT production-ready for webhook→LLM→DB pipelines.

**Why:** Grok Heavy Q2 (session 114, Harper + Lucas agreement): n8n v2.x has documented queue stall failures on small VPS under concurrent load. Graph API webhooks require 10-second response — if the worker is busy with a 45s Claude extraction, incoming webhooks are dropped silently. CVE-2026-21858 (unverified — check nvd.nist.gov before building) flagged for unauthenticated RCE in webhook handling.

**How to apply:**
- Before any n8n production webhook build: upgrade Hetzner to CPX31 (4vCPU/16GB RAM, ~€18/mo)
- Verify CVE-2026-21858 at nvd.nist.gov — patch before first webhook activation
- D53 (PostgreSQL for n8n internals) + D55 (queue mode + Redis) are necessary but NOT sufficient on 4GB RAM
- Trigger.dev is a viable alternative if n8n proves unreliable, but adds TypeScript code complexity

**Source:** Grok Heavy 4-agent council Q2, session 114. Harper + Lucas both flagged independently.
