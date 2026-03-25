---
name: multi-model-architecture-validation
description: How to validate a technical build plan using Grok + Gemini before spawning agents — what each model adds, what can be one-shotted, and what requires iteration
type: project
source: session 78, 2026-03-16
---

# Multi-Model Architecture Validation
**Source:** Session 78 — DMC-SECONDBRAIN-CRM Wave 2A pre-build validation
**Time invested:** ~3 hours (Grok Q1-Q3 → Gemini R1 → Gemini R2 adversarial → Grok R2 → SQL fix)
**Value delivered:** 4 spawn prompt fixes, RLS policies applied to 18 tables, 2 architectural decisions locked

---

## What We Did (the full loop)

| Round | Tool | Prompt type | Key output |
|-------|------|-------------|------------|
| R1 | Grok Heavy | Cross-validate (Template 3) | 6 mandatory conditions, CONDITIONAL GO |
| R2 (Q1-Q3) | Grok Heavy | Follow-up on 6 conditions + wave architecture + EU AI Act | JWT timing, sequential waves defended, EU AI Act = LIMITED RISK |
| R3 (Q4) | Grok Heavy | JWT rotation deep-dive | RLS policies (SQL), blast radius math, rotation timing |
| R4 | Gemini | Independent peer review (full context, no prior) | Pragmatic counter: JWT over-engineering, BUILD-STATE.md is fine, Zero/Minimal EU AI Act risk |
| R5 | Gemini | Adversarial (Grok-prompted) | NO GO verdict — but adversarially instructed, lower weight |
| R6 | Grok | Response to Gemini | CONDITIONAL GO tightened, SQL RLS policies confirmed |

**Total rounds:** 6. **Rounds that changed the design:** 3 (R1 for architecture gaps, R3 for RLS SQL, R4 for JWT pragmatism).

---

## What Each Model Actually Contributed

**Grok Heavy:**
- Best for: surfacing genuine security gaps with math (blast radius, JWT window), generating actionable SQL, multi-perspective agent debate (Harper/Benjamin/Lucas)
- Weakness: enterprise-projection bias — applies Fortune 500 patterns to solo-dev setups. Confidently recommends over-engineering.
- Unique value: Benjamin's blast radius math on the RLS 14-table schema was the highest-value single output of the entire loop

**Gemini (independent):**
- Best for: pragmatic pushback on over-engineering, scale-appropriate reality checks
- Weakness: contradicted itself between Round 1 (pragmatic) and Round 2 (adversarially prompted). Adversarial prompting made it find problems to satisfy the instruction.
- Unique value: "Enterprise architecture projection" framing — correctly identified that Grok was applying wrong scale. JWT rotation = over-engineering for self-hosted solo-dev. Sequential waves = fine for AI-assisted development (not production agentic systems).

**Key lesson:** Gemini Round 1 > Gemini Round 2. Adversarial prompting forces the model to find problems regardless of whether they exist. Weight independently-prompted reviews higher.

---

## What Changed the Spawn Prompt

| Finding | Source | Change made |
|---------|--------|-------------|
| Attachment silent failure | Grok R1 | Added Node 3c (attachment guard → dead-letter) |
| `status:unverified` design rationale | Grok R1 + Gemini R1 | Added explicit comment explaining soft staging gate |
| JWT = security debt, not Wave 2A work | Gemini R1 | Changed END OF SESSION to document-only, not implement |
| EU AI Act pre-deployment memo | Grok Q3 | Added as Patrick action in LOCKED DECISIONS |
| n8n version pin + decision rationale log | Grok Q2 | Added to END OF SESSION |
| `audit_log` → `ai_action_log` (wrong table name) | RLS verification | Fixed Node 10 table reference |

**Most impactful single action:** Running the Supabase table list query. Caught that `audit_logs` didn't exist — would have been a Wave 2A blocker discovered mid-build.

---

## What Could Have Been One-Shotted

**If we had run this upfront before any Grok rounds:**
1. Query Supabase for actual table names → would have caught `ai_action_log` vs `audit_logs` immediately
2. Check RLS status on all tables → would have surfaced the missing policies
3. Single Grok Heavy cross-validate with explicit scale context: "solo dev, self-hosted n8n, 6 staff, internal-only phase for 4-6 weeks"

**The scale context was the key missing piece.** Grok's enterprise-projection bias fired because we didn't explicitly anchor it to solo-dev + self-hosted + internal-only. Adding `SCALE CONTEXT: solo developer, self-hosted n8n on single server, 6 staff internal tool, no external traffic for 4-6 weeks` to the CONTEXT block would have short-circuited the JWT rotation debate and the sequential-waves debate in Round 1.

**Estimated one-shot reduction:** 6 rounds → 2 rounds (1 Grok cross-validate with scale context + 1 Gemini independent check).

---

## One-Shot Template for Future Architecture Validation

Use this structure before spawning any build agent on a security-sensitive pipeline:

```
SCALE CONTEXT (add to every CONTEXT block):
- Team: [N staff], [internal/external users]
- Infrastructure: [self-hosted/cloud, single-server/distributed]
- Phase: [internal testing / staff pilot / production / external traffic]
- Developer: [solo / small team / enterprise]
- Timeline to external traffic: [X weeks]

PRE-FLIGHT CHECKS (do before any Grok round):
1. Query actual database for table names — never trust spec doc names
2. Verify RLS status on all tables
3. Check actual credential expiry (paste JWT at jwt.io)
4. Confirm n8n version running

GROK PROMPT ADDITIONS:
- Add scale context block first
- Add explicit: "Do not recommend solutions that require a dedicated ops engineer or >4 hours/month maintenance for a solo developer"
- Add: "Flag over-engineering explicitly — solo-dev budget and maintenance constraint is real"
```

---

## Patterns for `_index.yaml`

- `multi-model-architecture-validation` — use when validating a technical build plan before spawning agents
- Key rule: Scale context in CONTEXT block prevents enterprise-projection bias in Grok
- Key rule: Adversarial-prompted Gemini rounds have lower signal than independent rounds
- Key rule: Always verify actual database state before finalizing spawn prompts

**Why:** Session 78 spent ~2 hours on JWT rotation debate that resolved to "annual manual rotation" — entirely caused by missing scale context in the initial Grok prompt.
