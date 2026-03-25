# De-Sloppify Mining — Separate Cleanup Pass

Source: ECC de-sloppify pattern, adapted for knowledge mining workflows
Quality gate: `quality-gates/mining-output-qg.md`

## The Principle

**Don't constrain the mining pass — add a separate cleanup pass.**

Negative instructions during extraction ("don't include duplicates", "keep it concise") cause the LLM to become hesitant and miss genuine insights. Instead:

1. **Mining pass:** Be thorough. Capture everything. Err on the side of inclusion.
2. **De-sloppify pass:** Compress, deduplicate, flag contradictions, structure.
3. **Build pass:** Assemble deliverable from cleaned data.

## Why This Works

| Approach | Problem |
|----------|---------|
| One-pass "extract + organize" | LLM tries to be thorough AND concise → does neither well |
| Negative instructions ("don't repeat") | LLM becomes hesitant, skips borderline-valuable insights |
| Two-pass (extract → cleanup) | Each pass is focused. Quality of both improves. |

This is the same reason your Session 38 proposals mining worked well — 4 subagents each focused on ONE extraction task, then synthesis was a separate pass.

## The De-Sloppify Prompt

Run this BETWEEN raw mining output and deliverable building:

```
Review the raw mining output below. Your job is cleanup, not new extraction.

1. DEDUPLICATE: Merge entries that say the same thing in different words. Keep the richer version.
2. COMPRESS: Reduce verbose passages to their core insight. Target 50% reduction without losing substance.
3. CONTRADICTIONS: Flag any two entries that disagree. Don't resolve — flag for human review.
4. STRUCTURE: Group related insights. Add section headers if missing.
5. GAPS: Note obvious holes — "Client X mentioned in 3 places but no contact details extracted."
6. CONFIDENCE: Mark each insight as HIGH (multiple sources), MEDIUM (single clear source), or LOW (inferred/ambiguous).

Do NOT add new insights. Do NOT remove anything just because it seems minor — that's Patrick's call.

Output: Cleaned version in the same format, with a CLEANUP SUMMARY at the top listing what was merged, flagged, or compressed.
```

## When to Use

- After every M365 mining session (emails, Teams, SharePoint)
- After every document batch extraction
- After Second Brain subagent runs (client-profiler, revenue-mapper, etc.)
- After any session that produced >500 lines of raw output
- Before building Custom Instructions, knowledge summaries, or any final deliverable

## Pipeline

```
M365 Mining (claude.ai)
    ↓ raw blocks transferred to Claude Code
De-Sloppify Pass (Claude Code, Sonnet)
    ↓ cleaned + structured output
Build Deliverable (Claude Code, using templates)
    ↓ quality gate checklist
Final File → project-files/
```

## Integration with Second Brain

When the Chief of Staff agent (TODO) feeds daily intelligence into the Second Brain, the de-sloppify pass runs automatically:

```
Daily M365 triage → raw signals (client mentions, pricing, decisions)
    ↓
De-sloppify: merge with existing client profiles, flag contradictions
    ↓
Update: client-profiles.yaml, revenue-intel, staff-map
    ↓
Second Brain grows incrementally, stays clean
```

## Anti-Patterns

- Running cleanup during mining (→ hesitant extraction)
- Skipping cleanup and building directly from raw output (→ duplicates, contradictions in final deliverable)
- Letting the cleanup agent ADD new insights (→ hallucination risk, scope creep)
- Removing "minor" items without Patrick's review (→ might be the one signal that matters)
