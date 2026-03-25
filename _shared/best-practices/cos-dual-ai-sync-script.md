---
name: Dual-AI A→B Sync via Local Script
description: Replace manual context sync between two AI systems with a local Python script — reads source file, redacts GDPR terms, writes to target. Eliminates manual maintenance burden.
type: feedback
---

When running two AI systems (workshop AI + conversational CoS bot), manual context sync creates a maintenance burden that kills adoption within 2-3 weeks (Grok validated: 42% dual-AI failure rate).

Replace with a local script (`sync-cos.py`):
1. Reads master status file (CURRENT-STATUS.md)
2. Extracts relevant sections (current phase, blockers, next tasks)
3. Redacts GDPR-sensitive terms (client names, HR data) via configurable list
4. Writes formatted output to CoS Project File (weekly-context.md)
5. Shows preview + requires explicit confirmation before writing

Result: 15 min Monday curation → 30 seconds.

**Why:** Manual sync is the #1 abandonment trigger in dual-AI setups. Friction compounds faster than value. Automation removes friction without removing human oversight (preview + confirm step stays).

**How to apply:** Any time two AI systems share context via files. Build the script when the dual-AI system is designed, not after abandonment starts. GDPR redaction list is configurable — start conservative.

**Reference implementation:** `~/1658HoldingsOy-AIFiles/_shared/sync-cos.py` (session 115, 2026-03-25)

**Source:** Gemini architecture analysis + Grok Round 4 risk identification (session 115)
