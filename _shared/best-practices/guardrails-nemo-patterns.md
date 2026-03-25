# Open-Source Guardrails Patterns — Mined 2026-03-19
**Source:** guardrails-ai/guardrails + NVIDIA/NeMo-Guardrails
**When to use:** When implementing Governance-as-Code for Claude+n8n+Supabase stack

## Key Finding: OPA is overkill for solo operator. Two lighter options:

### Guardrails AI — for output validation
- Python validators chained with `.use()`, each has `on_fail` action (8 options incl. CUSTOM)
- CUSTOM handler can POST to n8n webhook → Supabase escalations table
- Auto audit trail (Call history stack, in-memory, must persist manually)
- HTTP server mode: n8n calls `POST /guards/{name}/validate`

### NeMo Guardrails — for dialogue flow control
- Colang DSL (text files, non-code), defines intent→flow routing
- Custom Python actions bridge to n8n webhooks
- Native LangChain+Supabase vector store integration
- No built-in audit trail — wrap `rails.generate()` manually

## Minimum Viable Setup (solo, no DevOps)
1. `pip install guardrails-ai` — run in n8n Code node OR as HTTP server
2. Supabase tables: `escalations` + `audit_log` (deal_id, violation, auto_fix, approval_needed)
3. n8n → Guardrails validate → CUSTOM handler → n8n approval webhook → Supabase

## Hallucinated repos (from Grok round 2 — do not use):
- microsoft/agent-governance-toolkit — DOES NOT EXIST
- eqtylab/cupcake — DOES NOT EXIST
- deeplearning-ai/sc-agent-governance — DOES NOT EXIST

## Real repos confirmed:
- open-policy-agent/opa — 8.9k stars, real, overkill for solo
- guardrails-ai/guardrails — 2.9k stars, right tool
- NVIDIA/NeMo-Guardrails — 3.2k stars, right tool for dialogue
- vorionsys/vorion — ~300 stars, MLOps platform (not governance)
