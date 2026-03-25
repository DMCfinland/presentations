# Opus Review: Gold Extraction Pipeline — Critical Analysis

**Purpose:** You are reviewing a knowledge extraction workflow BEFORE we spend money executing it. Your job is to find problems, ask hard questions, and suggest improvements. Do NOT validate — challenge.

**Optimize for:** Affordability and performance. Every dollar matters. Every unnecessary step is waste.

**Your output:** Questions, concerns, alternative approaches, and specific recommendations. NOT a polished report — a working critique.

---

## Context

We have a YouTube research knowledge base:
- **196 video analyses** (35KB each, 6.9MB total) created by Haiku batch processing
- **32 deprecated** (news, model comparisons, low-value), **164 active**
- Each file has YAML frontmatter + 11-dimension structured analysis
- **Routing index built** (routing-index.yaml, 87KB, topic/pattern/concept maps)
- **Gold (compressed insights) NOT YET extracted** — this is what the pipeline is for

The pipeline was built by Sonnet in Claude Code. It has NOT been tested yet. We want your critical eye before spending ~$10 executing it.

---

## The Proposed Pipeline

### Stage 1: Haiku Compression (~$2)
**What:** Strip filler from 164 video analyses. Remove timestamps, generic sections, boilerplate, ads.
**Output:** Compressed text (~60% reduction, ~12-15KB each)
**Prompt approach:** Rules-based (REMOVE list + PRESERVE list). "When in doubt, keep it."

### Stage 2: Sonnet Gold Extraction (~$5)
**What:** Extract 3-7 actionable insights per compressed document.
**Output:** YAML-structured gold nuggets with type tags (FRAMEWORK, PATTERN, ANTI_PATTERN, METRIC, CONTRARIAN, TECHNIQUE, PREDICTION, TENSION)
**Prompt approach:** Variable-length extraction. "Quality over quantity. If nothing non-obvious, say NO GOLD."

### Stage 3: Opus Cross-Synthesis (~$3-5)
**What:** You (Opus) read all ~800+ gold nuggets and find cross-document patterns, contradictions, portfolio implications.
**Output:** Strategic synthesis — mega-patterns, tensions, priority stack, counter-narrative.

**Total estimated cost: ~$10**

---

## The Full Workflow Document

Below is the complete workflow as written. Read it critically.

```
WORKFLOW START
```

{WORKFLOW_CONTENT}

```
WORKFLOW END
```

---

## Sample Input Document

Below is ONE actual video analysis file — the type of document the pipeline will process. This is what Stage 1 receives.

```
SAMPLE START
```

{SAMPLE_DOCUMENT}

```
SAMPLE END
```

---

## What We Need From You

Answer EACH of these questions with honest analysis. If you don't know, say so. If you disagree with a premise, say that.

### A. Pipeline Architecture

1. **Is 3 stages the right number?** Could Stage 1 and 2 be combined into a single Sonnet pass (skip Haiku compression entirely)? What would we lose vs. gain? Show the math.

2. **Is Haiku actually the right model for Stage 1?** The documents are already structured (11-dimension framework output). Is "strip filler" actually mechanical, or does it require judgment about what's filler vs. what's insight? If Haiku removes something important, we won't know until Stage 2.

3. **Is the Stage 2 output format right?** We chose YAML with typed insight tags. Is YAML the best format for Stage 3 consumption? Would markdown be better for human review? Would JSON be better for programmatic use?

4. **Is Stage 3 actually feasible as a single query?** 164 docs × 5 insights × ~200 tokens = ~164K tokens input. Is this within productive context window size, or will we hit the same context rot we already proved exists?

5. **What's the weakest link in the pipeline?** Where is quality most likely to degrade?

### B. Prompt Quality

6. **Read the Stage 1 compression prompt.** Is the REMOVE/PRESERVE distinction clear enough for Haiku? Are there ambiguous cases that will cause inconsistent behavior across 164 documents?

7. **Read the Stage 2 gold extraction prompt.** The insight types (FRAMEWORK, PATTERN, etc.) — are 8 types too many? Too few? Will Sonnet consistently distinguish PATTERN from FRAMEWORK, or will it blur?

8. **The "NO GOLD" escape hatch** — is this actually safe? Will Sonnet be too eager to find gold (false positives) or too strict (missing real insights)? What percentage of 164 videos do you expect to yield "NO GOLD"?

### C. Cost & Alternatives

9. **Could we skip Stage 1 entirely?** Sonnet can read 35KB documents. Is Haiku compression saving us money or just adding a step? Calculate: Sonnet-only cost for 164 docs at 35KB each vs. Haiku+Sonnet at reduced input.

10. **Could Sonnet do both compression AND gold extraction in one pass?** "Read this document. Extract only the gold." — would this be cheaper and produce better results than two separate passes?

11. **Is Batch API the right execution path?** We have Claude Code with Opus 4.6 running. Could we use Task tool with parallel Sonnet subagents instead? What are the tradeoffs (cost vs. speed vs. quality control)?

### D. Skill & Reuse Architecture

12. **Should the full research-mining pipeline be one skill, or should we decompose it?** Patrick plans to reuse this for: (a) YouTube videos, (b) 2,408 business documents, (c) competitor research, (d) future corpora. What level of abstraction is right?

13. **Should "YouTube search + transcript extraction + batch analysis" be its own separate skill?** That's the INTAKE pipeline — getting raw content into the KB. The gold extraction pipeline is the PROCESSING pipeline. Are these naturally separate skills or parts of one workflow?

14. **Should "batch preparation and submission" be a standalone skill?** It's a pattern we use repeatedly: build JSONL → submit to Batch API → wait → retrieve → process results. Is this generic enough to abstract?

15. **What would the ideal skill decomposition look like?** Draw the map: which skills exist, what each does, how they connect.

### E. Quality & Risk

16. **What's our failure mode?** If we spend $10 and the output is mediocre, what went wrong and how would we know early? What's the cheapest way to validate before full execution?

17. **The 11-dimension framework produced structured but sometimes generic output.** Will the gold extraction prompt actually produce DIFFERENT results, or will Sonnet just repackage the same content in a different format?

18. **Training data contamination risk:** The video analyses were produced by Haiku from transcripts. Some of Haiku's analysis may include its own training knowledge "wearing the video's costume." Will gold extraction amplify this contamination or filter it out?

### F. The Big Question

19. **If you were designing this pipeline from scratch — knowing the input data, the budget (~$10), and the goal (actionable insights for a 10-company portfolio) — would you design the same 3-stage pipeline? Or something fundamentally different?**

20. **What question should we be asking that we haven't asked?**

---

## Constraints

- Budget: ~$10 for the full pipeline (164 videos)
- API key is available (Batch API operational)
- Source documents are structured markdown with YAML frontmatter
- End users: Patrick (CEO) and eventually 50 employees across 10 companies
- The routing index and cross-references are already built and good
- This pipeline should be reusable for future corpora (business docs, competitor research)

---

**Be honest. Be specific. If the pipeline is fundamentally flawed, say so now — not after we've spent $10. If it's solid, tell us WHERE it's solid and where it needs hardening. $10 is cheap to spend but expensive to waste if the output doesn't serve the goal.**
