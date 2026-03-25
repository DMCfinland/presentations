# Next Session Handoff — YouTube Knowledge Base Build

**Context:** Patrick asked Opus (in an expensive claude.ai Project that had analyzed all 195 videos) 6 follow-up questions (Q1-Q6). He'll bring back the answers. Here's what to do with them.

## Files to Read First
1. `COMPRESSION-AND-INDEX-PLAN.md` — the build plan (three-tier architecture)
2. `_shared/best-practices/knowledge-base-indexing.md` — Opus research on indexing (33KB)

## When Patrick Provides Q1-Q6 Answers

### Save them
Create `opus-project-followups/` folder, save each answer as:
- `q1-topic-clusters.md`
- `q2-compression-priorities.md`
- `q3-holdings-applicability.md`
- `q4-missing-gaps.md`
- `q5-context-rot-assessment.md`
- `q6-retrieval-quality-test.md`

### Use them to improve the build
- **Q1 (topic clusters)** → Use as seed for `topic-map.yaml` — Opus already grouped videos by theme
- **Q2 (compression priorities)** → Flag top-20 irreplaceable videos for human review after digest generation
- **Q3 (applicability map)** → Add `applicability` field to routing index entries
- **Q4 (missing gaps)** → Note in YouTube ROADMAP as future research directions
- **Q5-Q6 (context rot)** → Document findings in `_shared/best-practices/` as evidence for RAG approach

## Build Execution (after Q1-Q6 are processed)

1. **Step 1: Routing Index** — Read 195 files in `knowledge-base/videos/`, extract frontmatter, generate `one_line` summaries. Output: `knowledge-base/_index/routing-index.yaml`
2. **Step 2: Digests** — Process 195 files through Sonnet. Output: `knowledge-base/_digests/digest-{id}.md`
3. **Step 3: Cross-References** — Build inverted indexes from routing index. Output: topic-map.yaml, pattern-map.yaml, concept-map.yaml
4. **Step 4: Validate** — Run 10 test queries

**IMPORTANT:** Do NOT read all 195 video files into context at once. Process them individually or in small batches.
