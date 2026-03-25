# Q10: Sonnet Compression Prompt Design

**Source:** Opus claude.ai Project (195 video analyses, 1.7M tokens loaded via RAG)
**Date:** 2026-02-11
**Cost context:** Cheap follow-up (files deleted from Project, conversation history retained)
**Build impact:** Directly produces the Step 2 compression prompt for digest generation

---

## 1. Filler Patterns Safe to Remove

| Filler Pattern | Why Safe to Cut |
|---------------|-----------------|
| **Section headers and framework labels** ("## 6. Moats & Time Horizon") | Structural, not content. Compress to tags. |
| **"How to Apply to 1658 Holdings" boilerplate** | Speculative Sonnet-generated applications, not video content. Same principles repeat across 195 videos. Compress to 1-2 sentences. |
| **Repeated qualification language** ("This represents a fundamental shift...", "For business leaders, this signals...") | Sonnet's analytical padding. Cut. |
| **Metric formulas and tracking guidance** in "System Health Metric" sections | Sonnet-generated frameworks, not Nate's content. Keep only if named metric or novel insight. |
| **"When to Use / When NOT to Use" sections** | Often 60-70% padding. Keep only specific trigger conditions and red flags, compress to bullets. |
| **Quality Assessment sections** | Describe analysis quality, not video content. Remove entirely. |
| **Generic ethical considerations** | "AI may displace jobs, privacy concerns" repeated across dozens. Compress to tag unless insight is specific and novel. |

## 2. Content Patterns That MUST Be Preserved

| Content Pattern | Why It Must Survive |
|----------------|---------------------|
| **Named frameworks and coined terms** | Every instance of specific named concepts (e.g., "Ferrari failure mode," "intelligence-resistant problems"). These are the routing vocabulary. |
| **Quantified claims** | Specific numbers (15-20% hallucination rate, 5-hour threshold, 10x compute demand, $4.5T gap). Verifiable and decision-relevant. |
| **Contrarian / counterintuitive insights** | Anything against conventional wisdom. "80% reliability with zero burden beats 100% with overwhelming burden." |
| **Direct quotes from Nate** | Memorable encapsulations of key insights. "You cannot hold the design of the cathedral in your head while laying a single brick." |
| **Specific tool/model recommendations** | When Nate names specific tools for specific use cases (o3 Pro for strategy, non-thinking mode for rapid iteration). |
| **Anti-patterns and warnings** | Every "don't do this" is high-value. Preserve all. |
| **Temporal markers** | When something became possible, when thresholds crossed. "Images went from unsolved to solved in 6 months." |

## 3. What Gets Lost in Compression That Shouldn't

1. **The reasoning chain behind conclusions.** Sonnet will preserve "simplicity beats infrastructure" but lose WHY — platform consolidation absorbs middleware, natural language iteration outperforms scaffolding because iteration is cheap while upfront precision is hard. The "why" makes insights transferable.

2. **Cross-video connections.** When Video A's framework explains Video B's observation, that connection only exists in full-context reading. Compression creates isolated summaries.

3. **Nuanced conditions.** "Use tiger teams" is compressed. "Use tiger teams for execution BUT preserve structured reporting for regulatory contexts where audit trails matter" is the actually useful version. Conditions are the first casualty of compression.

4. **Speaker's evolution over time.** Early videos emphasize tool demos; later videos emphasize organizational strategy. This arc tells you where the field is heading. Compression flattens temporal development.

## 4. Draft Compression Prompt (Opus-Designed, 200 words)

```
You are compressing a video analysis document into a ~1.5KB digest. Preserve ONLY:

MUST KEEP:
- Named frameworks and coined terms (exact vocabulary, e.g., "Ferrari failure mode")
- Quantified claims (specific numbers, percentages, dollar amounts)
- Contrarian/counterintuitive insights (anything that challenges conventional wisdom)
- Anti-patterns and specific warnings ("don't do X because Y")
- The ONE core strategic insight the video offers
- Temporal markers (when capabilities crossed thresholds)
- Specific tool/model recommendations with use cases

SAFE TO CUT:
- Section headers and framework labels
- "How to Apply to 1658 Holdings" sections (keep only if uniquely insightful)
- Quality Assessment sections
- Generic ethical considerations
- Repeated qualification language ("This represents a fundamental shift...")
- Detailed metric formulas unless they contain a named metric
- "When to Use / When NOT to Use" unless conditions are specific and surprising

FORMAT: YAML front matter (title, date, tags, key_concepts) + prose digest.
Start with the one-sentence core insight. Then frameworks/vocabulary.
Then anti-patterns. Then quantified claims. End with the single most
memorable quote.

CRITICAL: If unsure whether to keep something, keep named terms and cut
generic analysis.
```
