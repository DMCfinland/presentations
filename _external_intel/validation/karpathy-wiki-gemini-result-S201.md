---
type: external-spar-result
source: Gemini
date: 2026-04-13
session: S201
note: "Gemini ei tiennyt koko portfolio-kontekstia — tulokset ovat kuitenkin samansuuntaisia Grokin kanssa"
---

# Gemini — T3: ADVERSARIAL_JUDGE Result

## Context A — Full Portfolio
- Assumption 1 (BP=Wiki): **FALSE** — normative (policy manual) vs descriptive (encyclopedia), total structural rewrite needed
- Assumption 2 (single user): **Partially valid** — multi-agent entry points create race conditions without locking
- Assumption 3 (57% cheaper): **FALSE** — "Synthesis Tax" on complex cross-portfolio queries burns tokens repeatedly
- **Fit: 6/10** (Gemini hieman optimistisempi kuin Grok 4/10)
- **Hidden risk:** "Stale Synthesis" — wiki drift from raw/ creates silent governance failures

## Context B — DMC CRM
- Assumption 1 (Wiki=CRM): **FALSE** — relational/tabular vs flat-file, data integrity nightmare
- Assumption 2 (Excel+Obsidian sufficient): **Partially valid** — "Translation Tax" between Excel+Markdown fragile as soon as column changes
- Assumption 3 (knowledge compounds): **FALSE** — CRM is temporal (timeline), wiki is spatial (structure), "graveyard of old meeting notes"
- **Fit: 3/10**
- **Hidden risk:** Schema Drift — LLM invents fields inconsistently, CRM unparseable in 6 months

## Context C — Riikka
- Assumption 1 (fits in index): **FALSE** — 3000+ tok/profile realistic, 200 leads = 600K tok
- Assumption 2 (replace ChromaDB): **FALSE** — similarity ≠ lookup, functional downgrade
- Assumption 3 (reduces complexity): **FALSE** — "Complexity Bomb" for sole maintainer
- **Fit: 2/10**
- **Hidden risk:** Inference latency — Riikka waits too long, bypasses system entirely

## Cross-context: Maturity
**FALSE** — "hobbyist move, not a CEO move." 9-day-old Gist, alpha software. No enterprise recovery path.

## Top 3 Recommendations (Gemini)
1. Isolate experiment: deploy wiki ONLY to Context A as read-only trial
2. Keep Supabase + ChromaDB as authoritative layers — wiki = volatile view only
3. Human-in-the-loop sync — Patrick manually triggers + reviews wiki updates, no automation yet

## Overall Portfolio Fit: 4/10
"Only as a weekend research project. Not ready as backbone of 1658 Holdings."
