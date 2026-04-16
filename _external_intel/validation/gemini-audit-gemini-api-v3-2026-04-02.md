# Gemini Audit — gemini-api v3.0 Implementation
**Date:** 2026-04-02
**Session:** S150
**Model:** gemini-2.5-flash (plain mode)
**Subject:** Schema-constrained output, thinking config, Pydantic integration

## Verdict: 2 fixes, 2 confirmed OK

### Q1 — response_schema API: CONFIRMED OK
`.model_json_schema()` is correct. google-genai SDK expects JSON Schema dict, not Pydantic class directly. Do not change.

### Q2 — Pro thinking_budget=-1: FIX NEEDED
`-1` is **not documented** for gemini-2.5-pro. Undocumented values may cause unpredictable behavior or future API errors.
**Fix:** Set `thinking_budget=None` for judge mode → existing `if thinking_budget is not None:` guard correctly omits thinking_config, enabling dynamic thinking. Applied immediately.

### Q3 — thinking_config + response_mime_type + response_schema: CONFIRMED OK
No known conflicts on Gemini 2.5 models. This combination is valid and beneficial — model reasons then formats.

### Q4 — Pydantic fallback silent degradation: FIX APPLIED
Silent `AuditResult = None` was "not ideal" — audit/judge modes become opaque failures. Applied `RuntimeError` in `call_gemini()` when `response_schema` requested but `_PYDANTIC_OK` is False.

## Applied fixes
1. `MODE_CONFIG["judge"]["thinking_budget"]`: `-1` → `None`
2. `call_gemini()`: added RuntimeError if pydantic missing and schema requested
