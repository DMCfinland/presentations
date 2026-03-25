# Grok Round 2 — Compound Leverage + Open Source Repos
# Date: 2026-03-18 | Model: Grok Heavy (4-agent)
# Prompt: GROK-PROMPT-MIKKO-ALASAARELA-FOLLOWUP.txt

## KEY FINDING: 3 of 5 repos were hallucinated
- open-policy-agent/opa ✅ Real (8.9k stars, CNCF project)
- vorionsys/vorion ✅ Real (~300 stars, MLOps orchestration)
- microsoft/agent-governance-toolkit ❌ DOES NOT EXIST
- eqtylab/cupcake ❌ DOES NOT EXIST
- deeplearning-ai/sc-agent-governance ❌ DOES NOT EXIST

## (1) Compound leverage model
[Benjamin] Table (compound = baseline × ai_multiplier):

| Pre-AI Baseline | AI 1.3× | AI 3× | AI 5× | AI 10× |
|----------------|---------|-------|-------|--------|
| 1× (median)    | 1.3×    | 3×    | 5×    | 10×    |
| 2×             | 2.6×    | 6×    | 10×   | 20×    |
| 5× (elite)     | 6.5×    | 15×   | 25×   | 50×    |
| 10× (top 1%)   | 13×     | 30×   | 50×   | 100×   |

200×/250× require extreme tails (10× pre × 20× AI) — outside observed distributions.

[Harper] Empirical support thin: Mollick/BCG 2025 shows power users achieve ~1.3–1.7× effective overall. No sustained 5-10× AI multiplier for individuals documented.

[Lucas] PATRICK CORRECTION APPLIED: Lucas's "selection bias" argument was incomplete. Correct model = COMPOUND: elite pre-AI operators (5-10×) get ANOTHER 5-10× from AI → 25-250× vs baseline. At 10× pre × 10× AI = 100×. Makes 200× claim mathematically plausible for right operator.

## (2) Real open-source governance-as-code landscape
Real repos confirmed by Gemini (verified after Grok hallucinations):
- guardrails-ai/guardrails — 2.9k stars — Python validators for LLM output
- NVIDIA/NeMo-Guardrails — 3.2k stars — Colang DSL for dialogue control
- open-policy-agent/opa — 8.9k stars — general policy engine (Rego language)

## (3) Mikko's company history
- Gamelion (pre-2013): mobile software, sold to BLStream (CONFIRMED EXIT #1)
- Linko Inc. (2013-14): mobile AI CRM, $2.6M seed, short-lived, possible loose exit (UNCONFIRMED)
- Inbot (2013/14-2019): AI chatbot + InToken crypto, explicit shutdown Oct 2019 (NOT an exit)
- Equel Social (~2021-24): community app, de-listed from stores (NOT an exit)
- Atlan (Chairman): limited data
- Nokia Bell Labs EIR (~2023-25): not a company, productization role
- Agion (2024-present): current

## (4) Agion open-source footprint
ZERO. No GitHub, no SDK, no public policy examples, no developer docs.
[Lucas] Major red flag: closed-source for a product claiming sovereignty and transparency.

## (5-6) Lucas's updated challenges
1. Compound works at 25× (5×pre × 5×AI) but breaks before 200× for solo: cognitive ceiling, verification drag
2. 10× AI multiplier not realistic sustained: Mollick tops 36% in narrow tasks
3. Rego maintainable for 5-10 rules, becomes liability at scale
4. Zero open-source = implementation maturity question mark

## (7) Three builds confirmed
1. OPA + Rego gate in git (n8n HTTP call)
2. Supabase trust_score column
3. Mission-as-Code KPI injector
Expected lift: 15-30× at N=50-100 agents
