# Session 79 Retrospective
**Date:** 2026-03-16–17 | **Session:** 79 | **Project:** DMC SecondBrain CRM — Wave 2A Security Hardening + Pre-Spawn Final
**Model:** Sonnet 4.6 | **Topic:** Constitutional Principles expansion, CVE validation, schema prioritization (Grok R3), pre-spawn audit

---

## What Happened (Chronological)

### Phase 1 — Constitutional Principles Debrief
**P:** Dead-letter queue? What is the full workflow? Should we run Constitutional Principles through Grok/Gemini?

**C:** Dead-letter queue = low-confidence emails stored in `failed_emails` for manual staff review (NOT deleted). Existing 6 principles had gaps: no injection audit logging, no credential isolation rule, no artifact integrity check, no XSS guard, no payload-splitting defense. Ran Gemini (cybersecurity focus) then Grok Heavy (2 rounds + CVE research).

**Result:** 6 Constitutional Principles → 11. Three new principles from Grok:
- P8: Credential Isolation (Hybrid) — placeholder substitution before any file write
- P9: Generated Artifact Integrity — node allowlist, self-audit before export
- P10: Output Sanitization Mandate — HTML-escape all Supabase writes, XSS detection
- P11: Multi-Message Assembly Guard — payload splitting defense

Existing principles strengthened:
- P3: Added ai_action_log requirement + defense-in-depth note
- P4: Added "when in doubt, read-only" clause
- P5: Restricted to NEXT SESSION block only; added `# PATRICK-SIGNED:` requirement for schema changes
- P7: Added required fields (confidence_score, extraction_model) to audit log

---

### Phase 2 — CVE Research + n8n Version Confirmation
**P:** n8n version is 2.11.4. Only supabase-ai-writer JWT + azure-openai-embeddings in n8n. No service_role.

**C:** Background research verified all CVEs (NVD-confirmed):
- CVE-2026-21858 "Ni8mare" CVSS 10.0 — unauthenticated RCE via webhook. Fixed: 1.121.0 ✅
- CVE-2025-68613 CVSS 9.9 — expression injection RCE, fires on ANY workflow execution. Fixed: 1.120.4 ✅
- CVE-2025-68949 — SSRF + data exfil. Fixed: 2.2.0 ✅
- n8n 2.11.4 patches all. No version action needed.
- Supply chain attack (Jan 2026): malicious npm community nodes. Defense: audit on every upgrade.
- Flag: CVE-2026-25049 cited by Grok R3 — UNVERIFIED. Check nvd.nist.gov before citing.

---

### Phase 3 — Data Architecture Clarification
**P:** What is "Supabase mining"? When will sent emails be ingested?

**C:** Architecture clarified:
- Wave 2A: ongoing inbound email ingestion (automated, permanent)
- Wave 2B: one-time bulk-embed of 107 client profiles from mining outputs
- Wave 2B.2 (NEW): one-time import of historical deals from M365 mining sessions 1-5 (~107 deals backfill), ~2h TypeScript script
- Wave 2C: Sent Items ingestion + follow-up scheduler
- Future claude.ai mining sessions: remain valuable for deep analysis; outputs semi-auto imported via Wave 2B.2 pattern
- Supabase = database only, not a mining tool

---

### Phase 4 — Schema Prioritization (Grok R3)
**P:** What schema fields will we regret not adding before first email? Make Grok prompt.

**C:** Evaluated 8 candidate fields. Grok Heavy MAD 2-round response:

| Field | Decision | Reason |
|-------|----------|--------|
| deleted_at (soft delete) | NOW | GDPR Art.17, 4h retrofit cost |
| email_message_id unique index | NOW | Dedup baseline |
| next_follow_up_date | NOW | High regret, trivial |
| special_requirements | NOW | Zero extraction cost, high ops value |
| Audit trail enrichment (ai_action_log) | BEFORE-PILOT | Art.22 compliance |
| Staff assignment (assigned_to) | BEFORE-PILOT | Workflow essential |
| Staff notes | BEFORE-PILOT | Relationship context |
| ai_decision_rationale | BEFORE-PILOT | Art.22/15 explanation |
| GDPR fields (consent_timestamp, legal_basis) | BEFORE-PILOT | Insurance columns |
| Optimistic locking (version) | CAN-WAIT | Premature for 50-200/mo |
| Circuit breaker (failed_emails) | CAN-WAIT | Premature |
| Proposal link tracking | CAN-WAIT | Operational |

Benjamin math: $9K cost exposure from 1M spam emails (our $3K estimate was 3× low).
Key finding: Microsoft Defender already active in M365 Business by default — primary spam control is free.

**Schema SQL written:** `BUILD-ARTIFACTS/schema-additions-pre-wave2a.sql`
- Section 1 (applied 2026-03-16): deleted_at, email_message_id, next_follow_up, special_requirements
- Section 2 (BEFORE-PILOT): audit enrichment, assigned_to, staff_notes, ai_decision_rationale, GDPR fields, pre-Wave-3 fields

---

### Phase 5 — Volume/Security/Enrichment Grok Round
**P:** What if we get 1M spam emails?

**C:** Grok Heavy response:
- Benjamin verified: $9K flood cost at scale (not $3K)
- Harper: no documented email-flooding incidents on AI pipelines (confirmed "none found")
- Defender pre-filter > daily n8n cap as primary control
- Quarterly JWT rotation (not annual) — GDPR + n8n RCE incident data
- n8n CISA KEV monitoring every 4-8 weeks

Spawn prompt changes: JWT debt note updated to quarterly. `special_requirements` added to Node 4 extraction.

---

### Phase 6 — Pre-Spawn Audit
**C found and fixed 6 bugs in spawn prompt:**
1. Node 1: added INBOX FOLDER ONLY + junk explanation
2. Node 5: explicit schema field list including special_requirements(array)
3. Node 8: email_message_id write made explicit (dedup index was useless without it)
4. Node 8: ON CONFLICT (email_message_id) DO NOTHING — prevents overwriting verified records
5. Node 8: next_follow_up_date = now() + 14 days (column existed but was never SET)
6. Bulk-embed idempotency: content_text hash, not deal_id (profiles have no deal_id yet)

Additional additions:
- Node 1b: Working hours filter (Mon-Fri 07:00-16:00 Helsinki time) — saves ~60% Claude API calls
- Wave 2C scope note in END OF SESSION block (Sent Items, follow-up scheduler, Wave 2B.2)
- PRE-FLIGHT NOTE: verify failed_emails table exists before building error workflow

---

### Phase 7 — EU AI Act Memo
**C wrote:** `docs/eu-ai-act-risk-classification-memo.md`
- Classification: LIMITED RISK (Article 50 transparency only)
- Not Annex III high-risk
- Pre-deployment actions confirmed complete
- Patrick: read and sign before first live email

---

## SPAWN PROMPT FINAL STATE
**File:** `~/Desktop/FinnConcierge/SPAWN-WAVE-2A.md`
**Status:** READY TO SPAWN
**Nodes:** 1, 1b, 2, 3, 3b, 3c, 4, 5, 6, 7, 8, 9, 10, Error Workflow
**Constitutional Principles:** 11 (validated: Grok Heavy 2r + Gemini 2r + NVD CVE research)
**Schema Section 1:** Applied to Supabase 2026-03-16

---

## PATRICK ACTIONS BEFORE FIRST LIVE EMAIL
1. ✅ Apply Section 1 SQL — DONE 2026-03-16
2. ✅ Defender anti-spam — already active in M365 Business by default
3. ✅ EU AI Act memo — written, needs Patrick signature
4. ✅ Privacy notice — updated 2026-03-16
5. ✅ DPIA addendum — signed 2026-03-16
6. ⬜ n8n plan upgrade — 14 days left on trial, upgrade before going live
7. ⬜ Anthropic SCC (Standard Contractual Clauses) — privacy notice references SCCs with Anthropic; verify DPA exists or request one from Anthropic

---

## INSIGHTS

- **Email deduplication requires explicit column write.** The unique index on `email_message_id` in the deals table does nothing if Node 8 never writes the column. Schema + index are necessary but not sufficient — the workflow must explicitly populate the column from Outlook trigger metadata (not from extracted JSON). Add "write X column" explicitly to every node spec that introduces a new column.

- **ON CONFLICT key must be explicit for every upsert.** "Upsert deals table" is ambiguous. Without specifying the conflict key, the Postgres node can't resolve duplicates. For this system: ON CONFLICT (email_message_id) DO NOTHING is safer than DO UPDATE (prevents overwriting verified records).

- **Default values for new columns must be in the workflow spec, not just the schema.** `next_follow_up_date` was added to the schema with no instruction for what value to write. The Wave 2A agent would have left it NULL. Every new column added by schema migration needs a corresponding "what does the workflow write here" note in the node spec.

- **Working hours filter is high ROI, near-zero cost to add.** Node 1b saves ~60% of Claude API calls and prevents out-of-hours Teams notifications. B2B clients don't expect overnight response. Add working-hours filter to every non-critical n8n polling workflow by default.

- **Bulk-embed idempotency: content_text hash, not FK.** When embedding pre-deal entities (client profiles, research notes), there's no deal_id to match against. The idempotency check must be content-based (hash of content_text) not relationship-based. Confirm FK constraints in deal_embeddings before running any bulk insert script.

- **failed_emails table existence is an unverified assumption.** The error workflow writes to `failed_emails` but this table was part of Wave 1A migrations. Always add existence checks for error-path tables in the startup sequence — a missing table in the happy path is caught immediately; a missing table in the error path is discovered only when something goes wrong.

- **Research done when gold stops coming (confirmed).** 4 rounds of multi-model validation each produced genuine new findings. Round 5 showed diminishing returns (Lucas "none found" on real incidents). The decision to stop was correct. See `_shared/best-practices/research-done-when-gold-stops.md`.

---

## NEXT SESSION START INSTRUCTIONS

1. Check Wave 2A output: read `~/Desktop/FinnConcierge/BUILD-STATE.md` NEXT SESSION block
2. Check `~/Desktop/FinnConcierge/BUILD-ARTIFACTS/email-ingestion-workflow.json` exists
3. Check `~/Desktop/FinnConcierge/BUILD-ARTIFACTS/bulk-embed-107-profiles.ts` exists
4. Patrick: sign EU AI Act memo at `docs/eu-ai-act-risk-classification-memo.md`
5. Patrick: upgrade n8n plan before trial expires
6. Apply Section 2 SQL (BEFORE-PILOT fields) at sprint end
7. Plan Wave 2B + Wave 2C scope
