# Grok Debate Result — Opportunity Engine + Long-Term Architecture
**Date:** 2026-03-13 | **Model:** Grok 4 Heavy (4-agent council)

> ⚠️ **VALIDATION THEATER — DO NOT USE AS EVIDENCE**
> This result was produced from a pre-loaded prompt (GROK-PROMPT-OPPORTUNITY-ENGINE.md) that embedded the expected answers in the "format" section. Grok echoed them back without independent reasoning. Skill updated to v1.2 on 2026-03-13 to prevent this. Rebuild this prompt using the corrected approach before relying on any finding here.
**Round:** 2 (follow-up to Dashboard Evolution D25-D33)
**Prompt:** `research/GROK-PROMPT-OPPORTUNITY-ENGINE.md`

---

## For Question 1 — Opportunity Signals

| Signal | Verdict | Rationale |
|--------|---------|-----------|
| Re-engagement (dormant high-value) | **INCLUDE** | Highest ROI on existing 107-client base; Flash Pack (€558K) is low-effort, high-trust win |
| Anniversary (same season last year) | **INCLUDE** | Perfectly aligned with Lapland/winter/summer cycles; time-bridging on past bookings, zero external data |
| Market signals (routes, competitors) | **EXCLUDE** | GDPR friction + unreliable feeds + cost unjustifiable for 5-person team; keep everything internal |
| Upsell on confirmed deals | **INCLUDE** | Leverages confirmed deals + cross-category similarity (city tour → archipelago add-on), zero extra entry |
| Referral (post-trip sentiment) | **INCLUDE** | Post-trip email sentiment extraction fits existing n8n classifier; turns happy clients into advocates |
| Lapsed proposal | **INCLUDE** | Combine with pricing-window checks (D approved) for "re-quote now" timing signal |

**Top 3 priority signals for Wave 3C:**
1. Anniversary signals (Lapland/winter/summer booking cycles)
2. Re-engagement — dormant high-value accounts (Flash Pack model)
3. Upsell on confirmed deals (cross-category similarity)

---

## For Question 2 — Strategy Generation

**Verdict:** LIMITED VERSION

**Minimum viable brief (Wave 3C):**
```
OPPORTUNITY: [Client] — [Signal type]
Context: [Last booking + value + route + pax + assigned staff]
Signal: [Why now — timing, anniversary, dormancy period]
Strategy options:
  A) [Option 1 — specific, Finnish B2B tone-appropriate]
  B) [Option 2]
  C) [Dismiss — low risk, they'll reach out]
Recommended: [X] — reason: [1-sentence rationale]
[Send A] [Send B] [Dismiss] [Edit strategy]
```

**Highest risk:** Tone mismatch in reserved Finnish B2B culture OR hallucinated context that damages long-term relationship. One bad email could lose a €200K client.

**Mitigation:** Agent generates options from verified deal_embeddings data only (no inference). Staff must read before sending. System logs which option was chosen (R signal for future improvement).

---

## For Question 3 — Long-Term Architecture

| Decision | Verdict | Notes |
|----------|---------|-------|
| Data ownership (own Supabase) | **APPROVE** | Still the only GDPR-safe, no-lock-in path in 2028. SaaS CRMs won't match full email + proposal + calendar memory. |
| Embedding model lock-in | **CHANGE NOW** | Add `raw_content` JSONB column alongside 1536-dim vector → re-embed any future model in one script run |
| n8n self-hosted | **FLAG** (risk 2027–2028) | Maintenance + security patching will exceed €200/mo TCO; monitor, be ready to flip to EU n8n Cloud |
| Model routing | **CHANGE NOW** | Add Supabase Edge Function router (Sonnet → classification, Haiku → extraction) — swap providers without touching workflows |
| Schema evolution (14 tables) | **APPROVE** | Current JSONB flexibility + pgvector views already supports TravelTree/HR/accounting additions |

**2 decisions to make before Wave 3C:**
1. Add `raw_content` column + one-time backfill script for all existing embeddings (D43)
2. Implement model-routing abstraction layer — 2-day task (D44)

---

## For Question 4 — What We're Missing

| Agent | Proposal |
|-------|----------|
| Agent 1 (UX) | Daily "Opportunity Briefing" panel on morning dashboard with one-click strategy approval |
| Agent 2 (Tech) | Automated re-embedding scheduler + vector-index health monitor |
| Agent 3 (DMC Ops) | **Client seasonal pattern miner** — extract per-client booking cadence from historical closed deals |
| Agent 4 (AI Systems) | Integrated client health score (recency + sentiment + value tier) to rank all signals |

**Council winner: Client seasonal pattern miner (Agent 3)**

> Rationale: In a Finnish travel DMC everything is seasonal. This single capability turns 5 years of history into predictive timing intelligence no human can maintain manually. It directly powers the top two Wave 3C signals (anniversary + re-engagement). Pure internal data, zero entry, compounds every year. Highest long-term leverage for a durable system.

---

## Second Brain CRM North Star

> "Every morning I open the PWA and the Second Brain has already prepared my day: three hot opportunities it spotted overnight — AHI Travel's Lapland anniversary window opens in 10 days with a ready strategy and email draft; Flash Pack is 8 months dormant but their 18-month pattern says now is perfect; plus two upsell chances on current groups drawn from identical past wins. I click into each card, review the three-option brief (recommended one highlighted with risk/reward), tweak one sentence if needed, hit Approve — the agent sends the perfectly personalised message, tracks opens, and only nudges me later if required. The system remembers every client interaction, seasonal cycle, supplier rate, and successful approach from the last five years better than any of us ever could, so our tiny 5-person team operates with the memory and foresight of a 50-person operation. It surfaces what matters, suggests without ever deciding, and lets us spend every minute on the relationships that actually close deals."

---

## Actions Applied

- [x] D43: raw_content column → DECISIONS.md
- [x] D44: Model routing abstraction → DECISIONS.md
- [x] D45: Client seasonal pattern miner → DECISIONS.md
- [x] D46: Opportunity signal priority locked → DECISIONS.md
- [x] D47: Strategy brief = limited version → DECISIONS.md
- [x] D48: Market signals excluded → DECISIONS.md
- [x] D49: Daily Opportunity Briefing on morning dashboard → DECISIONS.md
- [x] D50: North Star confirmed → DECISIONS.md + BP08-STAFF-DASHBOARD-v2.md header
- [x] Wave 3C: Opportunity Engine spawn prompt → WAVE-BUILD-AGENTS.md
