# Nate B Jones Substack Comments — Mining Addendum
**Source:** Open Brain article comments, batch 2
**Date mined:** 2026-03-11
**Scope:** Actionable findings only. Generic troubleshooting and non-Supabase implementations excluded.

---

## C1 — Security Audit (Robert MacNaughton)
**Priority:** CRITICAL — applies before Wave 1A goes live

Four vulnerabilities in the reference implementation:

1. **Auth key as URL query param** → gets logged in browser history, server logs, proxy logs. Anyone with the URL has full read/write access.
   - Fix: header-only auth (`Authorization: Bearer` or custom `x-brain-key` header — never query param)
   - Already in our design: WAVE-BUILD-AGENTS.md Wave 1A uses `x-brain-key` header pattern from Mads fix (batch 1)

2. **Single shared key across all clients** → one compromised config = rotate everything
   - Fix: per-client JWT tokens (our ai_reader/ai_writer JWT roles in D8 already handle this for AI pipeline)
   - For n8n/Teams webhook: use separate service credentials, not a shared key

3. **No rate limiting on MCP endpoint** → leaked key = unlimited extraction
   - Fix: Supabase Edge Function rate limiting or n8n rate cap
   - Add to Wave 2A (n8n workflow builder) requirements

4. **Thoughts routed through OpenRouter** → retention policies of third-party model providers not surfaced
   - For DMC: embeddings via OpenAI text-embedding-3-small (D1 uses OpenAI API for embeddings?)
   - GDPR implication: embedding model provider must have EU DPA — verify before Wave 1A goes live

**Decision needed:** D31 candidate — header-only auth + per-client keys for all ingest endpoints (applies to Teams webhook handler and MCP server)

---

## C2 — Teams Message Markup Poisoning Embeddings (EricJWi)
**Priority:** HIGH — affects semantic search quality

Raw Teams/Slack message text includes: `<@U12345>` mentions, `<https://url|label>` hyperlinks, `:emoji:` codes, `*bold*`/`_italic_` markdown.

This noise gets encoded into embedding vectors, degrading semantic search. A clean query won't reliably match a messily-encoded note even if the meaning is identical.

**Fix for our build (Wave 2A n8n workflow):**
- Strip Teams formatting markup BEFORE calling embedding model
- Store original text separately (for audit/display)
- Same applies to email body text before embedding (HTML tags, quoted email chains, signatures)

**Deduplication via event_id (same source):**
- Teams webhook retries if response > 3 seconds → duplicate entries
- Fix: unique index on `teams_message_id` in deal_embeddings (or thoughts table equivalent)
- Return 200 immediately → process async via n8n queue

---

## C3 — Emergent Auto-Save Behavior (Michael Faughn)
**Priority:** MEDIUM — design decision needed

Once MCP write is connected, Claude started auto-saving high-signal thoughts without being explicitly asked. Confirmed: "emergent behavior from Claude based on what it thinks I want."

**For DMC:**
- **Desirable:** Patrick/Sebastian in Claude Code sessions could auto-capture deal intelligence
- **Risk:** Claude might capture client PII, confidential pricing, or sensitive deal terms without explicit trigger
- **Mitigation:** Wave 2A n8n pipeline already has quarantine → validator → privileged flow (D8). MCP write should go through same validation, not bypass it.
- **GDPR note:** Auto-capture without explicit user action may require additional DPIA coverage

---

## C4 — Atomic Facts vs. Full Documents for Embedding (Nigel Burke → Nate's approach)
**Priority:** HIGH — affects D30 Phase 1 bulk-embed quality

Nate explicitly recommends: store **atomic facts**, not full documents.

For our D30 Phase 1 (bulk-embed 107 client profiles):
- DO NOT embed full 107-profile blobs
- Break each profile into atomic facts: "AHI Travel: senior Nordic traveler segment, 75% revenue, direct contact Jonas Schmidt" (one embedding)
- Each atomic fact = one row in deal_embeddings
- Result: semantic queries ("find clients who asked about budget Lapland options") return specific facts, not entire profiles

**Estimated output:** 107 profiles × 10-20 facts each = 1,070–2,140 embedding rows on Day 1
This is the right scale for semantic search to be useful.

---

## C5 — Thought Lifecycle Gap (Chris Maughan + Mark Madsen batch 1)
**Priority:** MEDIUM — design note

The reference implementation has no built-in way to:
- Mark a thought complete/stale
- Delete or update a thought
- Track temporal decay (permanent vs. working memory distinction)

**Mark Madsen's fix (batch 1):** Added `version` column + history table + `update_thought`/`delete_thought` MCP tools.

**For DMC:** Our deal_stage_history table already handles deal lifecycle. For captured thoughts/insights in deal_embeddings:
- Add `active boolean default true` column to deal_embeddings
- Soft-delete via `active = false` (never hard-delete — audit trail required for GDPR deletion log)
- Mark Madsen's gist: https://gist.github.com/mmadsen/4f1ff37f19af99ecf0bb6c1b100412df

**D31 candidate:** deal_embeddings gets `active boolean default true` + soft-delete logic. Hard-delete only via `erase_contact_pii()` GDPR function.

---

## C6 — Architecture Validation: Retrieval Is Semantic, Not Context Dump
**Priority:** CONFIRMS design — no action needed

Multiple comments confirm: Open Brain is NOT loaded into context window. Semantic search retrieves relevant passages only (like our contacts_ai_view + deal_embeddings semantic query).

This validates our architecture. No change needed.

---

## C7 — Dual-Brain Pattern: Vector vs. Encrypted Storage
**Priority:** CONFIRMS design — no action needed

Community pattern: general knowledge → vector space. Secrets → encrypted/separate storage.

Already handled in our design:
- `contacts_ai_view` strips email/phone/address for AI pipeline
- `contacts` table under RLS (D8) — ai_reader cannot access contacts.email
- deal_embeddings contain semantic content, not raw PII
- Design is correct. No change needed.

---

## C8 — capture_thought via MCP (Addendum to D28)
**Source:** Jay Smith + Jay Standish (batch 1), confirmed by Michael Faughn (batch 2)

MCP write path enables capture from Claude Code without switching to any channel:
- Jay Smith: added `capture_thought` tool to MCP, 4th tool (alongside 3 read tools)
- Fix for Claude Desktop transport: inject `Accept: application/json, text/event-stream` header for mcp-remote compatibility
- Jay Standish: Claude started auto-saving high-signal thoughts; built a Skill for this

**Implication for D28:** Teams `#crm-capture` = for staff. Claude Code MCP write = for Patrick/Sebastian.
Two-channel capture with one brain. No conflict.

---

## Summary: New Action Items for Other Files

| Item | File to update | Priority |
|------|---------------|----------|
| C1: Header-only auth + per-client keys | DECISIONS.md (D31) | CRITICAL |
| C1: Rate limiting on ingest endpoint | WAVE-BUILD-AGENTS.md Wave 2A | HIGH |
| C2: Strip Teams markup before embedding | WAVE-BUILD-AGENTS.md Wave 2A | HIGH |
| C2: Deduplication via teams_message_id | DECISIONS.md (add to D28) |  HIGH |
| C4: Atomic facts chunking for D30 | WAVE-BUILD-AGENTS.md Wave 4A notes | HIGH |
| C5: active boolean soft-delete on deal_embeddings | DECISIONS.md (D31 or D32) | MEDIUM |
| C3: Auto-capture GDPR risk note | WAVE-BUILD-AGENTS.md Wave 5A security checklist | MEDIUM |
