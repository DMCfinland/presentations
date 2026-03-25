# Session 78 Retrospective
**Date:** 2026-03-16 | **Session:** 78 | **Project:** DMC SecondBrain CRM — Wave 2A Pre-Build Validation
**Model:** Sonnet 4.6 | **Topic:** Azure OpenAI setup, multi-model validation (Grok + Gemini), RLS application, spawn prep

---

## Q&A Retrospective

### Phase 1 — Azure OpenAI Setup

**P:** [Navigating Azure portal to deploy text-embedding-3-small. Confusion between AI Foundry and direct Azure portal. Multiple failed attempts — eastus2 resource locked, North Europe standard not available, agents feature error.]

**C:** Guided step by step through region failures. Final solution: new project in Sweden Central → Data Zone Standard (GDPR compliant, EU zone). Deployment name: `FinlandDMC-CRM-text-embedding-3-small`. Endpoint: `https://FinlandDMC-CRM-resource.cognitiveservices.azure.com`. Guardrails: DefaultV2 (adds jailbreak detection on top of content filtering — correct for untrusted email ingestion). n8n credential: API Key, Resource Name `FinlandDMC-CRM-resource`, API Version `2024-02-01`, Allowed HTTP Request Domains blank.

---

### Phase 2 — Pre-Spawn Questions

**P:** are we using our systems newest things? are we sure our compact protocol will work and we are using the 200k context models. Have we updated our features lists and microtasks + evals? Also will I just open a new window... or just go for totally fresh session?

**C:** Yes to all — Sonnet 4.6 with 200K context, compact protocol active. Fresh session pointed at `~/Desktop/FinnConcierge` is correct. File is at `SPAWN-WAVE-2A.md`.

---

**P:** Does FinnConcierge need to include all our best practices? Are our large scale build plannings up to date? I guess retrying is fine but there's got to be some limit, reiterating makes better I think? Do we have a red team wave?

**C:** FinnConcierge has its own CLAUDE.md. Retry limit: same error twice = hard stop; quality iteration = encouraged (up to 3 rounds). Wave 5A is the Red Team wave. Build plan current.

---

### Phase 3 — Grok Spar R1

**P:** [Asked Grok Heavy to cross-validate the build plan.]

**C:** Grok verdict: CONDITIONAL GO with 6 mandatory conditions: (1) JWT rotation — 10-year expiry catastrophic, (2) advanced injection defenses + attachment/OCR, (3) full DPIA + EU AI Act conformity, (4) staging table + human verification queue, (5) n8n hardening — version pinning, isolation, (6) ROC calibration of 0.7 confidence + >5 volume heuristics.

---

### Phase 4 — Follow-Up Grok Questions (Q1–Q3)

**P:** Didn't ask yet about encouragement to reiterate NOR big build plan best practices. Provide follow-up questions now.

**C:** Built 3 follow-ups: Q1 = iteration path for the 6 conditions (bolt-on vs structural), Q2 = sequential wave architecture best practices, Q3 = EU AI Act practical burden for SME. Grok answered: JWT + staging are Wave 3 pre-reqs; sequential waves "no longer best practice" — LangGraph-style preferred, BUILD-STATE.md needs expansion; EU AI Act = LIMITED RISK Art. 50, pre-deployment memo + privacy notice required before first live email.

---

### Phase 5 — JWT Explanation + Q4

**P:** What is the 10-year JWT? Ask Grok for 1 more question.

**C:** JWT = JSON Web Token with baked-in expiry. 10-year = if n8n breached, attacker holds valid token until 2036. Fix = short-lived JWTs + auto-refresh. Q4 sent. Grok answer: minimum viable = n8n Cron every 45min via jose library, stores in service_tokens table; alternative = Supabase Edge Function with RS256 asymmetric keys. Blast radius: INSERT/UPDATE on 3 tables only — no DELETE. Timing: Wave 3 pre-req (not Wave 5), internal testing still pollutes prod.

---

### Phase 6 — Gemini Cross-Validation

**P:** Lets ask Gemini still. (Gemini has no context so make full comprehensive prompt)

**C:** Built full Gemini prompt with complete architecture context, 4 findings to cross-validate, Q5 (n8n Cron vs Edge Function), Q6 (status:unverified vs staging table). Gemini R1 (independent): STRONGLY DISAGREE on JWT catastrophic framing — n8n is self-hosted, JWT never publicly exposed; Grok applied Fortune 500 patterns to solo-dev. Recommends 1-year static + calendar reminder. Sequential waves: STRONGLY DISAGREE with Grok — BUILD-STATE.md is correct for AI-assisted dev. EU AI Act: minimal/zero risk. Q6: separate staging table IS safer — BI tool trap + trigger cascade failure modes confirmed.

---

**P:** [Pasted Gemini R2 — adversarially prompted by Grok.] Gemini R2 verdict: NO GO. HIGH RISK EU AI Act. 45-minute blast radius even with rotation. Frankenstein sequential waves.

**C:** Gemini R2 was adversarially instructed — lower weight. CVE numbers from both models likely hallucinated (verify at nvd.nist.gov). Key convergence: staging table safer than status:unverified. Key disagreement: JWT — Gemini pragmatic wins for solo-dev context. Sequential waves: Gemini R1 is right, keep BUILD-STATE.md.

---

### Phase 7 — Grok R2 + RLS SQL

**P:** [Pasted Grok R2 — responding to Gemini, including SQL RLS policies for 14-table schema.]

**C:** Saved SQL to `BUILD-ARTIFACTS/rls-policies-wave1a-addendum.sql`. Final JWT decision: annual rotation + calendar reminder (Gemini wins). EU AI Act: get legal counsel — 3 AI systems gave 3 different answers. Spawn prompt updated and ready.

---

### Phase 8 — RLS Application to Live DB

**P:** Ok I need the RLS prompt to paste to SQL editor.

**C:** Provided SQL. First attempt failed — service_tokens table doesn't exist yet. Second failed — audit_logs doesn't exist. Queried actual table list: 18 tables, real audit table is `ai_action_log`. Provided corrected SQL for all 18 tables. All confirmed `rowsecurity: true`. Fixed spawn prompt: `audit_log` → `ai_action_log` in Node 10 and Node 3c.

---

### Phase 9 — Meta-Reflection

**P:** Only 4-6 weeks? We should always put a lot of effort into the planning phase to boost output performance. Any other insights you can mine from our conversation? Should you spin subagent to write fallback analysis relearning possibility and save my answers + compacted your answer

**C:** Planning phase ROI: 3h pre-build caught 6 blockers — break-even at 1 blocker avoided. Additional insights mined: CVE hallucination is systematic in both Grok and Gemini; Grok-prompting-Gemini = lower signal (R1 vs R2 contradiction proves it); multi-model disagreements > consensus (JWT and sequential waves debates were highest-value exchanges); DB state verification is mandatory pre-flight — querying actual tables saved a spawn-time blocker; scale context is the #1 missing ingredient in Grok prompts (Fortune 500 defaults without it).

---

## INSIGHTS

- **Scale context is the #1 missing ingredient in Grok prompts.** Without it, Grok defaults to Fortune 500/enterprise architecture patterns (JWT rotation every 45 min, LangGraph orchestration) that are overkill for a solo-dev SME build. Always include: team size, deployment model (self-hosted vs cloud), and expected transaction volume in the opening context block.

- **CVE hallucination rule.** Both Grok and Gemini cited specific CVE numbers. These are likely hallucinated. Never act on a CVE reference without verifying at nvd.nist.gov. Add this to pre-flight checklist for any security-focused spar session.

- **Adversarial prompting = lower signal.** Gemini R2 (prompted adversarially by Grok) contradicted Gemini R1 on every point. Adversarially-framed prompts produce adversarial answers, not independent analysis. When cross-validating, always give the second model clean context — not the first model's conclusions.

- **Multi-model disagreements > consensus.** The two highest-value findings came from disagreements: JWT pragmatism (Gemini won) and sequential waves (Gemini R1 won). Pure consensus would have produced worse decisions. Design spar sessions to surface disagreements, not validate a pre-designed conclusion.

- **DB state verification is mandatory pre-flight.** The RLS application failed twice on non-existent tables (service_tokens, audit_logs). A 30-second `SELECT tablename FROM pg_tables` query before writing SQL would have eliminated both failures. Add as a required step in any DB migration or RLS session.

- **Planning phase ROI math.** 3 hours of pre-build validation caught 6 concrete blockers. Break-even is 1 blocker avoided. At Wave 2A scope (~4-6 weeks), catching a structural blocker post-spawn costs 10-40x more to fix than catching it now. The planning phase is the highest-leverage work in the build cycle.

- **JWT pragmatism — Gemini won over Grok for solo-dev context.** Grok's 45-minute rotation recommendation was correct for enterprise. Gemini's 1-year static + calendar reminder is correct for self-hosted n8n with no public JWT exposure. Decision: annual rotation. The key insight is that blast radius analysis (INSERT/UPDATE on 3 tables only, no DELETE, no other tables) is what makes the pragmatic path acceptable.

- **One-shot path retrospective.** This session used ~9 exchanges to reach the spawn-ready state. Optimal path: (1) single Grok spar with scale context pre-loaded, (2) single Gemini cross-validate with clean context, (3) DB state query before RLS SQL. That's 3 focused operations. The extra rounds came from missing scale context (Grok R1→R2) and missing DB state check (RLS failures).

---

## ONE-SHOT TEMPLATE — What to Do Differently Next Time

**For any multi-model pre-build validation session:**

1. **Open with scale context block** (always first, in every prompt): team size, self-hosted vs cloud, transaction volume, regulatory jurisdiction, build wave number.

2. **Grok spar — single round with full context.** Do not iterate unless Grok asks a clarifying question. Include: architecture summary, known risks, specific Q1-Q4 in one prompt. Expected output: CONDITIONAL GO / NO GO + numbered conditions.

3. **Gemini cross-validate — clean prompt only.** Never paste Grok's answer into the Gemini prompt. Give Gemini the same architecture context + ask it to evaluate the same conditions independently. This is what produces genuine R1 signal.

4. **DB state pre-flight before any SQL.** Run `SELECT tablename FROM pg_tables WHERE schemaname = 'public' ORDER BY tablename;` and paste real table list into the SQL-writing prompt.

5. **Decision log immediately after spar.** Write: agreed conditions, disagreements resolved, and who won each disagreement (Grok or Gemini) and why. This becomes the spawn prompt preamble.

**Expected outcome:** 3 operations, ~90 minutes, same decision quality as this session's 9 exchanges.
