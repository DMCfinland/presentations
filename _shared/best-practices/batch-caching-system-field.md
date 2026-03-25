# Batch Caching: Always Use System Field Separately
<!-- source: knowledge-management-research-2026.md Section 4 | session: 70 -->
<!-- created: 2026-03-12 | confidence: 0.8 | tier: B -->

**What:** In Batch API JSONL requests, always put static content (warm pack, instructions, extraction rules) in the `system` field as a SEPARATE top-level key — never concatenate it into the first user message.

**Why:** Prompt caching requires exact prefix matching across requests. The `system` field is cached independently and shared across all requests in a batch. If static content is concatenated into the `messages[0]` user field, the prefix changes per request and cross-request caching never fires. Batch API 50% discount + prompt caching = ~95% off static content from request #2 onward. Missed on our gold extraction batch ($3, 164 requests) — could have been ~$0.15.

**When to apply:** Before submitting ANY batch job. Quick pre-submit check (30 seconds): open the JSONL, confirm structure has both `"system": [...]` and `"messages": [...]` as separate top-level keys.

**Correct structure:**
```json
{
  "system": [{"type": "text", "text": "[warm pack + instructions]", "cache_control": {"type": "ephemeral"}}],
  "messages": [{"role": "user", "content": "[per-request variable content]"}]
}
```

**How to verify caching fired:** Check `cache_read_input_tokens` vs `cache_creation_input_tokens` in API response. On request #2+, `cache_read` should be large (the static portion), `cache_creation` should be near zero.
