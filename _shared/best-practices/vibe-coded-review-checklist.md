# Pattern: Vibe-Coded Mock Code Review Checklist
**Tier:** B (load on demand)
**When to apply:** When Patrick has built mock implementations in Cursor/Gemini before production wiring
**Source session:** 51 (FinnConcierge review)

---

## The Pattern

AI-assisted vibe-coding produces surprisingly good mock architectures but consistently fails on the same 5 production-readiness issues. Check these before any production wiring effort begins — catching them at review costs nothing; finding them mid-integration costs hours.

---

## Checklist (read the code files before assessing)

### 1. GDPR Data Model — PII and hashes separated correctly?
- Raw names (first_name, last_name) should NOT be stored in the same table/object as the SHA-256 hashes used for identity resolution
- In production: hashes go in index column (lookup), raw PII goes in encrypted column (display only)
- **FinnConcierge finding:** `User` dataclass stores both `first_name`/`last_name` AND `email_hash`. Fine for mock. In production Azure SQL: PII in encrypted column, hashes in separate index.

### 2. Wrong AI Model in TODOs
- Cursor/Gemini default to `GPT-4o` or `Claude Opus` in TODO comments
- Find all `TODO` comments mentioning an AI model
- Update to Sonnet 4.6 for standard tasks, Haiku for classification — per model strategy
- **FinnConcierge finding:** `mood_evaluator.py` had `TODO: GPT-4o/Claude Opus` → should be `Claude Sonnet 4.6`

### 3. Mock Auth Tokens
- Vibe-coded JWT is always a fake string like `jwt_mock_{user_id}_{random}`
- Production needs real PyJWT with: `{user_id, tenant_id, session_id, exp, iss}` signed with Azure Key Vault secret
- **FinnConcierge finding:** `create_session()` generates `f"jwt_mock_{user.user_id}_{uuid.uuid4().hex[:8]}"` — 1 ministep to replace

### 4. Signature Validation Bypasses
- `validate_webhook_signature()` almost always returns `True` in mock mode
- Production needs real HMAC validation using shared secret per source (BookVisit, TAC, etc.)
- Get the actual HMAC signing spec from the partner's webhook documentation
- **FinnConcierge finding:** Explicit `# TODO: Implement HMAC validation` comment — well-flagged

### 5. In-Memory Storage → Azure SQL Migration Path
- `MOCK_USERS_DB: Dict[str, User] = {}` is in-memory, lost on restart
- Check that every mock dict has a corresponding comment explaining the production table/collection target
- **FinnConcierge finding:** All 3 mock dicts (users, itinerary, sessions) have production comments → clean

---

## Positive Signals (Things That Carry Over to Production)

- ✅ Architecture alignment with design: does the code match the agreed architecture?
- ✅ Separation of concerns: is the code organized by function (ingestion, finance, UI)?
- ✅ Type hints throughout: Python type hints + TypeScript types = fewer integration bugs
- ✅ Decimal for financial math: float arithmetic causes €0.01 errors in commission calculations
- ✅ Audit trail (never delete, only VOID): Shadow Ledger pattern is correct by default in FinnConcierge
- ✅ Error handling and logging: look for try/except + logger.info throughout

---

## When to Rewrite vs Extend

**Extend (use as-is):** Architecture matches design, mock→production migration path documented, GDPR issues are data-model-level only (not architectural)

**Rewrite:** Architecture fundamentally mismatched with Zone design, GDPR issues are structural (PII crossing zone boundaries in the code logic), or the code has no type hints and no error handling (indicates rushed generation with no quality guidance)

**FinnConcierge verdict:** Extend. 7/11 BPs in mock-functional state, all architecture correct, all 5 issues above are implementation-level not architectural.

---

## Related Files
- Zone 1 n8n architecture: `FinlandDMCOy-AIFiles/project-files/b2b-tools-feb2026/zone1-n8n-architecture.md`
- FinnConcierge code: `Desktop/FinnConcierge/` (see FINAL_CHECKLIST.md for blueprint status)
- BP_08 scope (what to build next): `FinlandDMCOy-AIFiles/project-files/dmc-2.0-strategic-synthesis/bp08-mvp-scope.md`
