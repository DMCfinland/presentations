---
name: llm-reasoning-action-divergence
description: Chain-of-thought reasoning traces are structurally unreliable as explanations of LLM decisions. Output often contradicts reasoning. Fix is architectural, not prompt-based.
type: feedback
confidence: 0.7
source: nate-jones-mount-sinai-study (session 97)
---

# LLM Reasoning-Action Divergence

Chain-of-thought faithfulness is structurally unreliable. An LLM can correctly identify a risk or classification in its reasoning trace and then output something that contradicts it. This is not a prompt engineering problem — it is a property of how LLMs generate outputs.

**Evidence:**
- Mount Sinai ChatGPT Health study (Nature Medicine, Feb 2026): system identified "early respiratory failure" in reasoning → output "schedule in 24-48h"
- Research: models failed to update answers >50% of the time when their own reasoning changed significantly
- Oxford AI Governance Initiative: chain-of-thought is fundamentally unreliable as explanation of model decision process
- When incorrect reasoning chains are inserted, models still produce correct answers a significant fraction of the time

**Why:** The reasoning trace and final output operate as semi-independent processes. Output is often anchored to an earlier decision state (base rate), not the reasoning just completed.

**How to apply:**
- Never validate agent decisions by having the same model review its own reasoning ("check if this is correct")
- Add deterministic if-then rules OUTSIDE the LLM that validate action matches stated intent
  - Example: "If reasoning trace contains pricing escalation flag AND output classification is low-priority → override to human review"
- This is why HYBRID architecture (n8n ingestion + full TypeScript CRM logic) is correct — CRM logic in deterministic code is the external validation layer
- Do NOT let scope creep push business logic back into LLM-driven n8n workflows

**Applies to:** All agent deployments — CRM, email triage, lead scoring, proposal tracking
