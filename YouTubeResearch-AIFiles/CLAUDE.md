# YouTube Research Knowledge Base — Project Context

## What This Is
R&D project to build a custom, high-quality research knowledge base by mining YouTube channels at scale. Testing whether curated research can meaningfully boost LLM productivity across 1658 Holdings.

## Owner
Patrick Heiskanen, CEO — 1658 Holdings Oy

## Project Philosophy
- **Research first, build after** — study what works before committing to architecture
- **Flexible roadmap** — findings at each phase shape the next phase
- **Quality over quantity** — 10 deeply-analyzed channels beat 100 shallow ones
- **Cost-efficient** — use Batch API for heavy lifting, interactive sessions for analysis
- **Mineable output** — everything we build should be searchable and usable as LLM context

## Folder Structure
- `research-outputs/` — Raw research results per channel (Phase 2 output)
- `knowledge-base/` — Organized, cross-referenced knowledge (Phase 3 output)
- `prompts/` — Batch processing prompts and templates
- `reference/` — Patrick's original Excel + source materials

## Workflow
1. Foundation research (Phase 0) — understand the landscape
2. Patrick picks channels (Phase 1) — human curation drives selection
3. Batch research (Phase 2) — cheap, heavy transcript analysis
4. Analyze & archive (Phase 3) — quality pass, proper organization
5. Integration test (Phase 4) — does this actually help?

## Integration
- This project feeds into `_shared/` best practices when we learn what works
- Final knowledge base may eventually sync to Zone B (OneDrive) for M365 access
- Batch API prompts live in `prompts/` — designed for Anthropic Batch API

## Commands
| Command | Action |
|---------|--------|
| `status` | Show ROADMAP.md CURRENT STATUS block |
| `mark [task] done` | Update checkbox + add completion note |
| `new session` | Add new session log entry |
| `end session` | Summarize work, update ROADMAP.md |
