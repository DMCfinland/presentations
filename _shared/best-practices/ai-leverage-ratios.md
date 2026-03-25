# AI:Human Leverage Ratios — Production Reference
**Version:** 1.0
**Source:** Gemini Deep Research (2026-03-17) + Grok Heavy (session 77-78) cross-validation
**Status:** Tier B — directional benchmarks, not all sources independently verified

---

## Summary: What Ratios Are Actually Achievable

The maximum ratio for a given task depends on **epistemic legibility** — whether success can be defined by a machine-verifiable state. High ratios come from deterministic rules + execution volume. Low ratios come from judgment + taste + external reality correspondence.

**For a 1-operator holding company: the portfolio-wide weighted average is ~3:1 to 6:1 today.** Not 25:1 overall — that number applies only to Tier 1 volume tasks.

---

## Table 1: Documented Leverage Ratios by Task Tier

| Task Type | Sources | AI:Human Ratio | Key Enabler |
|-----------|---------|---------------|-------------|
| **Tier 1: Machine-Checkable** (IT tickets, code scaffolding, CRM data hygiene) | Kore.ai (2026), Salesforce (2025) | **16:1 to 25:1** | Self-service integration + deterministic rules |
| **Regulatory / Compliance Audit** (100% transaction coverage) | Finance/audit pilots (2026) | **4:1 (by volume)** | Continuous observability + signed evidence |
| **Software Refactoring** (long-running autonomous) | Rakuten/Anthropic (2025) | **7:1 (by hours)** | Sustained-performance models (Claude 4 Opus) |
| **Tier 2: Expert-Checkable** (B2B sales research, CRM enrichment, proposal synthesis) | MIT Brynjolfsson study (2023, benchmarked 2026) | **1.6:1 to 4:1** | Golden set calibration + search-augmented judges |
| **Tier 3: Genuine Judgment** (strategy, legal analysis, portfolio synergies) | PwC CEO Survey + Wharton (2025) | **1.1:1 to 1.3:1** | Recursive self-modeling + MAD debate |

**Source quality note:** MIT "1.6:1 to 4:1" likely refers to Brynjolfsson et al. 2023 professional writing study (40% faster + 18% quality gain). Kore.ai and Salesforce figures are vendor-reported — treat as upper bound. GEAP/MCP ROI numbers in Table 2 are Gemini synthesis estimates (no external citation) — directional only.

---

## Table 2: Architecture Upgrades — ROI Priority (1-Operator, No DevOps)

ROI = estimated increase in attributed_value_eur per hour of operator intervention. **Numbers are Gemini directional estimates, not measured figures.**

| Rank | Upgrade | ROI (Est.) | Implementation |
|------|---------|-----------|----------------|
| 1 | **Governance-as-Evidence (GEAP)** | 12.0x ⚠️ | Agents emit signed artifacts to Git log at every gate. Operator audits async, not real-time. |
| 2 | **Multi-Agent Debate (MAD) Wrapper** | 8.5x | Every Tier 2/3 output = 2 agents (proponent + opponent) reaching consensus from internal docs |
| 3 | **Circuit Breaker / Step Caps** | 7.2x | Hard-code termination after 5 steps or €2.00 API spend per autonomous run |
| 4 | **MCP Tool Scoping** | 6.8x | Research agents: read-only. Execution agents: write to specific low-risk endpoints only |
| 5 | **Algorithmic Resignation Logic** | 5.5x | Reward functions penalize hallucinated helpfulness; agent surfaces "I can't proceed + why" |
| 6 | **Recursive Self-Correction Gates** | 4.2x | Watcher agent monitors primary agent's reasoning for belief traps before final synthesis |

---

## Table 3: Write-Access Governance — Automate vs. Protect

Directly applicable to CRM Wave 2A and any future portfolio automation.

| Process | Automate (Write OK) | Protect (Human Required) | Logic |
|---------|--------------------|--------------------------|----|
| CRM Record Updates | Formatting, address sync, status: unverified | Changing deal status above €10K | Risk of irreversible revenue signaling |
| Financial Reconcile | Internal ledger matching | Executing external transfers | Zero Trust + compliance |
| Sales Email Drafts | Research-based drafting | Sending to primary contacts | Brand taste + relationship equity |
| Portfolio IT Setup | Provisioning dev/test environments | Modifying production firewall/config | Runaway agent risk |
| Content Creation | Drafts, research synthesis | Final public-facing publication | Consumer reaction to full automation |
| Employee Screening | Initial skill/data matching | Final hire/fire decision | Ethical requirement: human agency |

**CRM Wave 2A validation:** Our design is correct — auto-create deals with status:unverified ✅, autonomous email drafting ✅, staff approval click before send ✅, no deal status promotion above €10K without touch ✅.

---

## Confidence-Based Routing (HATL Mechanism)

Agents self-evaluate before acting. Enables "Human-above-the-Loop" at scale.

| Confidence | Action | Human Role |
|-----------|--------|-----------|
| >98% | Execute autonomously | Audits retrospectively |
| 85-97% | Route to Approval Queue, continue parallel work | Clears queue in 1 session/day |
| <85% | Resign: surface summary of why + what data is missing | Decides whether to unblock or accept |

**Implementation:** Add confidence self-assessment to every agent spawn prompt. Resignation = not failure — it's the safety valve.

**⚠️ Lucas challenge (Grok session 82):** Confidence routing at 85-97% may create a false safety floor. "New Agentic Confidence Calibration research" shows agents are overconfident in flawed trajectories — routing errors forward increases review load, not autonomy. The threshold is not self-calibrating; an agent can route HIGH-confidence garbage to the approval queue. Mitigation: combine with explicit acceptance criteria (not just confidence score) before routing.

---

## Epistemic Closure Fix (No External APIs Required)

Lucas's root diagnosis from Grok session 77-78: PWJ loop optimizes for internal coherence only — zero mechanism for external reality correspondence on subjective B2B tasks.

**Fix without external APIs — Recursive Structural Modeling:**
1. **Pre-Mortem generation:** Agent must generate "why this synthesis might be wrong" BEFORE finalizing output. Forces engagement with alternative hypotheses.
2. **Scale-Coherence check:** Insight must survive translation across zoom levels (single company → holding portfolio). If it doesn't, it's an artifact of the framing, not a real finding.
3. **Explicit falsifiers:** Every strategic claim must name the specific evidence that would change the agent's conclusion. Claims without falsifiers = rejected by Judge, not debated.
4. **Reflexive gate:** Judge tracks whether agent's internal coherence is outrunning fresh data. If yes → auto-escalate to Patrick, do not iterate further.

**What this does NOT fix:** Global misalignment with external market reality (missing a competitor move, regulatory change). For that, tool-augmented judge or periodic external data injection is required.

---

## Async Human Anchoring Cadence

Production-validated rhythm for maintaining quality without becoming a bottleneck:

| Frequency | Action | What to Look For |
|-----------|--------|-----------------|
| **Weekly** | Audit 50-example golden set (random sample from prior week) | Agent operating at target tier level? Quality drift? |
| **Monthly** | Retrospective quality assurance on all autonomous writes | Long-tail failures — subtle errors that only emerge over weeks |
| **Quarterly** | Governance metric review | Clause Coverage (business rules met), Waiver Hygiene (how often agent escalated) |

**Long-tail failure note (Gemini + Grok confirmed):** B2B errors surface months after execution (relationship damage, missed signals). Weekly spot-checks catch execution errors. Monthly retrospectives catch pattern failures. Quarterly catches architectural drift.

---

## Minimum Viable Implementation (MVI) — 3 Changes for 80% Gain

Immediately implementable by 1 operator, no DevOps team:

1. **Constrained Autonomy via MCP:** Deploy task-specific agents (CRM Sync Agent, B2B Researcher) with strict tool boundaries. Eliminate monolithic planner with full system access. Reduces cognitive monitoring load and runaway agent risk.

2. **Evidence Backbone (GEAP):** Replace real-time PWJ rounds with Git-based log of all Conformity Bundles. Moves operator from "turn-based gatekeeper" to "async auditor." Single highest-ROI architectural change.

3. **Multi-Agent Debate for Tier 2/3:** Add mandatory proponent/opponent debate round to all strategic synthesis outputs before presenting to operator. Catches "coherent-but-wrong" errors without requiring tool augmentation on every query.

---

## What This Doesn't Solve

- **D5 gap (Agent Teams vs PWJ+subagents):** Not directly addressed. Gemini's "MAD Wrapper" is closest but doesn't compare architectures head-to-head. Needs dedicated Grok prompt if Patrick wants direct comparative analysis.
- **Tier 3 ceiling:** 1.1:1 to 1.3:1 is structural. No architecture upgrade breaks this for pure strategic judgment — the ceiling is the nature of the task, not the tooling.
- **k factor discrepancy:** Benjamin's p_catch sensitivity table (4.6× vs 6.50× at p=0.70) still unresolved. Defer file update until resolved.

---

**⚠️ GEAP ROI (12.0x) challenged (Grok session 82, Lucas):** "GEAP adds compliance overhead for a solo operator without solving the trust/autonomy core problem. Distracts from external verification, which is the real gap." Number is a Gemini directional estimate — treat as aspirational upper bound, not confirmed ROI. Same-model self-critique (Table 2, Rank 6) also challenged: Lucas cites Snorkel/arXiv showing same-model review degrades performance on high-quality outputs (98%→57% when hallucinating errors) and is vulnerable to misleading feedback. Use diverse-model or structured-criteria review instead.

*Sources: Gemini Deep Research 2026-03-17 (primary), Grok Heavy sessions 77-78 (cross-validation), Grok Heavy session 82 (Lucas challenges). ROI figures in Table 2 are Gemini directional estimates — not independently verified measurements. MIT ratio from Brynjolfsson et al. 2023. Kore.ai/Salesforce figures are vendor-reported upper bounds.*
