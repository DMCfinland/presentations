# Next Session Prompts

## PROMPT 1: Build Results Processor (30 min)

**When to run:** Next Claude Code session

**Copy-paste this:**

```
Build the process-batch-results.py script to convert Anthropic Batch API results into our markdown knowledge base.

REQUIREMENTS:
1. Read JSONL results files from batch-jobs/results/
2. Extract video analyses from Batch API response format
3. Convert each to markdown with YAML frontmatter (use our existing video templates as reference)
4. Save to knowledge-base/videos/ folder
5. Handle errors gracefully (log failed conversions)
6. Show progress and summary stats

REFERENCE FILES:
- Look at existing videos in knowledge-base/videos/ for format
- Use video-analysis-template.md from prompts/ folder
- Follow the YAML frontmatter structure we've been using

OUTPUT:
- Script: YouTubeResearch-AIFiles/scripts/process-batch-results.py
- Should be ready to run as soon as batch results are downloaded
```

---

## PROMPT 2: Knowledge Strategy Session (20 min)

**When to run:** After batch results are processed (2-3 days from now)

**Copy-paste this:**

```
Now that we have 189 comprehensive video analyses in our knowledge base, let's build a strategy for how to USE this knowledge effectively.

DISCUSSION TOPICS:
1. **Search & Discovery:**
   - How will I find relevant insights when I need them?
   - Should we build a simple search script?
   - Cross-reference by concept, pattern, or company application?

2. **Integration with Finland DMC:**
   - How do these AI/strategy insights inform the DMC project?
   - Which videos are most relevant for travel industry + AI adoption?
   - Should we create a curated subset for DMC team?

3. **Knowledge Maintenance:**
   - How often should we update with new videos?
   - Should we process Tier 4 (266 videos)?
   - Other channels to add (Founders Podcast, etc.)?

4. **Practical Applications:**
   - Weekly review routine?
   - Pre-meeting prep (search for relevant insights)?
   - Share with 1658 Holdings companies?

OUTPUT:
- Knowledge base usage plan
- Search/discovery tools (if needed)
- Integration strategy with existing workflows
```

---

## PROMPT 3: Interesting Projects Discussion (30 min)

**When to run:** Any time while waiting for batch results

**Copy-paste this:**

```
I mentioned I have some interesting projects I'd like to work on. Let's discuss them and prioritize.

CONTEXT:
- We have 12-24h before YouTube batch results are ready
- Finland DMC Phase 0 is blocked until M365 admin returns
- Good time to explore other opportunities

TELL ME ABOUT:
1. What are these interesting projects?
2. Are they related to:
   - 1658 Holdings companies?
   - AI/automation workflows?
   - Personal/side projects?
   - Something else entirely?
3. Which ones are time-sensitive?
4. Which align with the current AI infrastructure we're building?

LET'S:
- Map out these projects
- Identify which ones we can start now
- Figure out if any share infrastructure with what we've built (two-zone architecture, custom subagents, batch processing, etc.)
- Prioritize based on ROI and dependencies
```

---

## Quick Commands Reference

**Check batch status:**
```bash
cd /Users/patrickheiskanen/1658HoldingsOy-AIFiles/YouTubeResearch-AIFiles
python scripts/check-batch-status.py
```

**Download results when ready:**
```bash
cd /Users/patrickheiskanen/1658HoldingsOy-AIFiles/YouTubeResearch-AIFiles
python scripts/download-batch-results.py all
```

**Process results (after building the script):**
```bash
cd /Users/patrickheiskanen/1658HoldingsOy-AIFiles/YouTubeResearch-AIFiles
python scripts/process-batch-results.py
```

---

## Recommended Next Session Plan

1. **Start:** Run PROMPT 1 to build the results processor (~30 min)
2. **Check:** Run batch status check to see progress
3. **Explore:** Run PROMPT 3 to discuss interesting projects (~30 min)
4. **Later:** When batches complete, run PROMPT 2 for knowledge strategy
