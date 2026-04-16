---
type: external-spar-result
source: Grok Auto
date: 2026-04-13
session: S201
prompt_file: karpathy-wiki-grok-prompt-S201.md
---

# Grok Auto — T3: ADVERSARIAL_JUDGE Result

## Context A — Full Portfolio
- Assumption 1 (BP=Wiki): **FALSE** — pattern-centric vs entity-centric semantic mismatch, "format fundamentally conflicts"
- Assumption 2 (single user): **Partially valid** — cron agents + Claude Desktop = real concurrency risk
- Assumption 3 (57% cheaper): **FALSE** — Holdings cross-reference use case re-synthesizes on query, erodes "pay once" claim
- **Fit: 4/10**
- **Hidden risk:** Hallucinated wiki synthesis becomes canonical truth, propagates silently across 10 companies

## Context B — DMC CRM
- Assumption 1 (Wiki=CRM): **FALSE** — no structured fields, degrades to glorified notes folder
- Assumption 2 (Excel+Obsidian sufficient): **FALSE** — 40-80 FAM pipeline already exceeds brittle threshold
- Assumption 3 (knowledge compounds): **FALSE** — B2B is temporal/commitment-based, wiki misses this dimension
- **Fit: 2/10**
- **Hidden risk:** Loss of actionability — wiki turns dynamic sales into static archive, missing deals

## Context C — Riikka
- Assumption 1 (fits in index): **FALSE** — 200 leads × 2000 tok = 400K, well above threshold
- Assumption 2 (replaces ChromaDB): **FALSE** — similarity search ≠ wiki lookup, breaks core query type
- Assumption 3 (reduces complexity): **FALSE** — doubles maintenance surface for sole maintainer
- **Fit: 1/10**
- **Hidden risk:** Pipeline breakage during migration, Riikka loses filtering capability

## Cross-context: Maturity
**FALSE** — 9-day-old framework, no production track record. Blast radius: corrupted knowledge, broken pipelines. Wait 60-90 days.

## Top 3 Recommendations (Grok)
1. Do NOT migrate 136 BP files wholesale — greenfield wiki for new material only
2. Prioritize structured DB (Supabase) for CRM/profile needs BEFORE wiki layer
3. Strict governance + git hooks + human review gates for all wiki writes

## Overall Portfolio Fit: 3/10
"Not worth Patrick's time right now. Re-evaluate Q3 2026."
