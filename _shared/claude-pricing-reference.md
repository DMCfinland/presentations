# Claude API Pricing Reference
**Last verified:** 2026-02-21 (live from docs.anthropic.com/en/docs/about-claude/pricing)
**Purpose:** Internal cost calculations before running expensive queries

---

## Current Models — Standard Pricing (≤200K input tokens)

| Model | Input $/MTok | Output $/MTok | Notes |
|-------|-------------|--------------|-------|
| claude-opus-4-6 | **$5.00** | **$25.00** | ⚠️ 3× cheaper than old Opus 3 ($15/$75) |
| claude-sonnet-4-6 | $3.00 | $15.00 | Default for all session work |
| claude-haiku-4-5 | $1.00 | $5.00 | Batch classification, sorting, tagging |
| claude-haiku-3-5 | $0.80 | $4.00 | (older, slightly cheaper) |

**Revised ratios:**
- Opus 4.6 = **1.67× Sonnet cost** (was 5× with old Opus 3 — major change)
- Haiku 4.5 = 3× cheaper than Sonnet input, 3× cheaper output
- Old rule "Opus = 5× Sonnet" is NOW WRONG — update model strategy

---

## ⚠️ CRITICAL: Long Context Pricing — 200K Threshold

When the **total input tokens** (input + cache_creation + cache_reads) exceed 200K in a single request, **ALL tokens in that request** are charged at the premium rate:

| Model | ≤200K input | >200K input | Multiplier |
|-------|-------------|-------------|-----------|
| Sonnet 4.6 | $3 / $15 | **$6 / $22.50** | 2× input, 1.5× output |
| Opus 4.6 | $5 / $25 | **$10 / $37.50** | 2× input, 1.5× output |

**Key rule:** It's not just the tokens ABOVE 200K that cost more — if you cross 200K, ALL tokens in that call are charged at the higher rate. The threshold is all-or-nothing.

**Threshold check:** Sum input_tokens + cache_creation_input_tokens + cache_read_input_tokens. If total > 200,000 → entire request billed at 2× input rate.

**Note:** 1M context window currently in beta (usage tier 4+ only). If not on tier 4, max standard context applies.

### Practical implication for our workflows

A single session where main context grows past 200K (long conversation + large files) suddenly costs 2× per call. This makes parallel subagents (each with clean ~10-30K context) not just faster — **significantly cheaper** once main context approaches the threshold.

**200K policy (Patrick, 2026-02-21):**
- **Default:** Keep conversations to 50-95% of 200K. Short sessions, subagents for large tasks.
- **Exception:** Cross 200K intentionally on the most important projects when the value clearly justifies it (e.g., a €100K deal analysis, a full system architecture review with large context).
- **Never cross accidentally** — know before starting whether a task will exceed 200K. Calculate first.
- Rule of thumb: 200K tokens ≈ ~150KB of text. A long session with several large file reads can reach this.

Example — 4 analyses, context growing to 250K in single window:
- Single window (2 calls cross 200K): ~$1.68 × partial 2× penalty ≈ **~$2.50+**
- 4 parallel subagents (each ~15K): 4 × $0.33 = **$1.32**
- **Saving with parallel + pre-distill: ~47% cost reduction AND avoids the 200K trap**

---

## Prompt Caching

| Cache type | Sonnet 4.6 |
|-----------|------------|
| 5-min cache write | $3.75/MTok (1.25× base) |
| 1-hour cache write | $6.00/MTok (2× base) |
| Cache hit/read | **$0.30/MTok (0.1× base = 90% off)** |
| Min prefix | 1,024 tokens |

**Stack with Batch API:** 50% batch discount applies on top of cache reads.
Effective cached batch rate: $0.15/MTok input = **95% off standard.**

---

## Batch API

| Model | Batch input | Batch output |
|-------|-------------|-------------|
| Sonnet 4.6 | $1.50/MTok | $7.50/MTok |
| Opus 4.6 | $2.50/MTok | $12.50/MTok |
| Haiku 4.5 | $0.50/MTok | $2.50/MTok |

- 50% off standard pricing (automatic, no setup)
- Per-request size limit: **334KB** (bytes, not tokens — hard limit)
- custom_id max: **64 characters**
- Turnaround: up to 24 hours
- ⚠️ Fast mode NOT available with Batch API

---

## Fast Mode (Opus 4.6 only, research preview)

Significantly faster output, **6× premium pricing:**
- Input: $30/MTok | Output: $150/MTok
- Includes full 1M context window at no additional long context charge
- Stacks with prompt caching and data residency multipliers
- NOT available with Batch API

---

## Cost Calculation Formula

```
cost = (input_tokens / 1,000,000 × input_price) + (output_tokens / 1,000,000 × output_price)

Quick estimates (Sonnet 4.6, standard):
  10K in + 5K out   = $0.030 + $0.075 = $0.105  (typical analysis call)
  50K in + 20K out  = $0.150 + $0.300 = $0.450  (heavy subagent)
  200K in + 50K out = $0.600 + $0.750 = $1.350  (approaching threshold)
  250K in + 50K out = $1.500 + $1.125 = $2.625  (crossed 200K → 2× input rate)
```

---

## Parallel Subagents vs Single Window — Full Cost Model

**With 200K threshold factored in:**

```
Scenario: 4 analyses on proposals data (Sonnet 4.6)

Single window (sequential, context grows):
  Call 1: 10K in + 20K out           = $0.33
  Call 2: 30K in + 20K out           = $0.39
  Call 3: 50K in + 20K out           = $0.45
  Call 4: 70K in + 20K out           = $0.51
  Total input across session: 160K   = $1.68 (under 200K threshold, safe)

  BUT if conversation history + system prompt + files push any call above 200K:
  That call's input doubles → adds ~$0.30-0.60 penalty per crossing

4 parallel subagents (clean context each, pre-distilled 10K input):
  Each: 10K in + 20K out = $0.33
  Total: 4 × $0.33 = $1.32
  All 4 calls stay well under 200K threshold → no penalty risk

Saving: 21% fewer tokens + zero 200K penalty risk
Pre-distillation adds 87% input reduction per agent (8K vs 60K total)
Combined saving vs naive approach: ~60-70% total cost
```

---

## Key Cost Rules (battle-tested + updated)

- **Check cost BEFORE any query >$1.** Calculate input × output + 200K risk.
- **Watch main session context length** — if approaching 200K, prefer subagents to avoid 2× penalty
- **Opus 4.6 = 1.67× Sonnet** (not 5×) — reconsider when to use Opus vs Sonnet
- **Haiku 4.5 for mechanical work** — 3× cheaper than Sonnet input/output
- **Batch API for volume** (>10 similar requests) — automatic 50% discount
- **Prompt caching for repeated system prompts** — cache `system` field for 90% off
- **Pre-distill before subagents** — reduce input tokens 70-90% before spawning
- **Agent Teams costs significantly more** — each teammate = full Claude instance + overhead

---

## Model Strategy Update (2026-02-21)

⚠️ **Old Opus cost assumption is obsolete.** CLAUDE.md says "Opus = 5× Sonnet" — this was true for Opus 3 ($15 vs $3). With Opus 4.6 at $5/$25:

| Comparison | Old (Opus 3 vs Sonnet 4) | New (Opus 4.6 vs Sonnet 4.6) |
|-----------|--------------------------|-------------------------------|
| Input ratio | 5× more expensive | **1.67× more expensive** |
| Output ratio | 5× more expensive | **1.67× more expensive** |

**Implication:** The delegation threshold (3+ tool calls) still makes sense for avoiding Opus doing Sonnet's work. But the penalty for occasional Opus use is much lower. Strategic decisions that previously felt too expensive for Opus are now viable at 1.67× Sonnet cost.

---

## Reference: Session Cost History

| Session | Work | Cost |
|---------|------|------|
| 38 | 4× Sonnet subagents (proposals Second Brain, ~15K each) | ~$0.50 |
| 23 | YouTube KB batch (164 Sonnet requests) | ~$3 |
| 17 | Järvisydän SEO 4× Opus parallel | ~$15-20 (old Opus 3 prices) |
| 8 | 5× Opus research agents | ~$8-12 (old Opus 3 prices) |

**Cumulative project cost through session 38:** ~$116-131

---

## Additional Charges to Remember

- **Web search tool:** $10 per 1,000 searches (+ standard token costs)
- **Web fetch tool:** No additional charge (standard token costs only)
- **US-only inference** (`inference_geo` parameter): 1.1× multiplier on all token costs
- **Tool use overhead:** ~346 tokens per request for tool system prompt

---

*Source: [Anthropic pricing docs](https://platform.claude.com/docs/en/docs/about-claude/pricing) — verified 2026-02-21*
