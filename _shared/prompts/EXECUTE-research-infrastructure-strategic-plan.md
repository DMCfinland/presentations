# How to Execute: Research Infrastructure Strategic Plan
## Opus Strategic Review — Three Options

---

## Option A: claude.ai Projects (RECOMMENDED) ✅

**Best for:** Interactive session, can ask follow-ups, refine recommendations

**Time:** 1-2 hours (interactive)
**Cost:** $3-6 (Opus with RAG retrieval)
**Quality:** Highest (can iterate)

### Step-by-Step

**1. Create New Project in claude.ai**
- Go to claude.ai → Projects
- Create new Project: "Research Infrastructure Strategic Plan"
- Select Opus 4.6 model

**2. Upload Files (10 files, ~500KB total)**

Upload these files to Project Knowledge:

**Infrastructure docs (5 files):**
- `_shared/best-practices/knowledge-base-indexing.md`
- `_shared/best-practices/research-chunking-and-cost-optimization.md`
- `_shared/best-practices/context-window-failure-modes.md`
- `_shared/workflows/WORKFLOW-DECISION-FRAMEWORK.md`
- `MODEL-STRATEGY.md`

**YouTube KB indexes (4 files):**
- `YouTubeResearch-AIFiles/knowledge-base/_index/routing-index.yaml`
- `YouTubeResearch-AIFiles/knowledge-base/_index/topic-map.yaml`
- `YouTubeResearch-AIFiles/knowledge-base/_index/pattern-map.yaml`
- `YouTubeResearch-AIFiles/knowledge-base/_index/greatest-hits-10.md`

**Reference (1 file):**
- `YouTubeResearch-AIFiles/batch-results/youtube-kb-strategic-review.md`

**3. Paste the Prompt**

Copy entire contents of:
`_shared/prompts/opus-research-infrastructure-strategic-plan.md`

Paste into conversation.

**4. Interact & Refine**

After Opus delivers the strategic plan:
- Ask follow-up questions
- Request elaboration on specific gaps
- Challenge priorities if needed
- Ask "which should I build first?"

**5. Download Results**

When satisfied:
- Copy/paste full response into:
  `_shared/batch-results/research-infrastructure-strategic-plan.md`
- Delete Project files (avoid future RAG charges)

---

## Option B: Batch API (MOST COST-EFFICIENT) 💰

**Best for:** Can wait 6-24h, don't need iteration, want 50% discount

**Time:** 10 min setup + 6-24h wait
**Cost:** $1.50-3.00 (50% discount)
**Quality:** High (but no iteration)

### Step-by-Step

**1. Build Batch Request**

Create file: `batch-research-infrastructure-plan.jsonl`

```jsonl
{
  "custom_id": "research-infrastructure-plan-001",
  "params": {
    "model": "claude-opus-4-6",
    "max_tokens": 16000,
    "messages": [
      {
        "role": "user",
        "content": [PASTE FULL PROMPT HERE INCLUDING ALL FILES AS TEXT]
      }
    ]
  }
}
```

**2. Include Files in Prompt**

You need to concatenate all files into the prompt. Build a combined context:

```
[Paste opus-research-infrastructure-strategic-plan.md prompt]

---
FILES PROVIDED:
---

FILE: _shared/best-practices/knowledge-base-indexing.md
[paste full contents]

FILE: _shared/best-practices/research-chunking-and-cost-optimization.md
[paste full contents]

... [repeat for all 10 files]
```

**3. Submit Batch**

```bash
# Load API key
source ~/.zshrc && load-keys

# Submit batch
python3 _shared/scripts/submit-batch.py \
  batch-research-infrastructure-plan.jsonl \
  research-infrastructure-plan

# Save batch ID
# msgbatch_XXXXX
```

**4. Wait & Retrieve**

```bash
# Check status (6-24h later)
python3 _shared/scripts/check-batch-status.py msgbatch_XXXXX

# When complete, retrieve
python3 _shared/scripts/retrieve-batch-results.py msgbatch_XXXXX
```

**5. Process Results**

Results saved to:
`_shared/batch-results/research-infrastructure-strategic-plan.md`

---

## Option C: Claude Code with Task Tool (HYBRID) 🔧

**Best for:** Want to stay in Claude Code, use local files

**Time:** 30-60 min (interactive)
**Cost:** $3-6 (Opus direct)
**Quality:** High (no RAG, direct file reading)

### Step-by-Step

**1. In Claude Code**

Ask:
```
"I need you to execute an Opus strategic review.

Read the prompt file:
_shared/prompts/opus-research-infrastructure-strategic-plan.md

Then read all the files listed in section 7 of that prompt.

Execute the strategic review as specified in the prompt.

Use Opus model for this task."
```

**2. Claude Code Will:**
- Read the prompt file
- Read all 10 referenced files
- Execute the strategic review
- Deliver results in conversation

**3. Save Results**

Ask Claude Code:
```
"Save your strategic review to:
_shared/batch-results/research-infrastructure-strategic-plan.md"
```

---

## Recommended Approach: **Option A** (claude.ai Projects)

**Why:**
1. **Interactive** — You can ask follow-ups ("why is Gap 1 more important than Gap 3?")
2. **Refinement** — Can challenge priorities, request alternatives
3. **Strategic work** — This IS the kind of decision that benefits from conversation
4. **Cost-effective** — $3-6 for iterative strategic planning is worth it

**When to use Option B (Batch API):**
- You're confident in the prompt and don't need iteration
- Can wait 6-24h
- Want 50% savings

**When to use Option C (Claude Code):**
- Want to stay in VS Code
- Want local file control
- Don't need RAG benefits

---

## After Execution: What to Do With Results

### Immediate Actions (Within 24h)

**1. Review Tier 1 Priorities**
- Do you agree with Opus's prioritization?
- Are there blocking dependencies?
- Can any be automated with Sonnet?

**2. Pick ONE Quick Win**
- What's the fastest Tier 1 item to build? (<2 hours)
- Build it immediately
- Validate it works (use it for your 2-4 item project)

**3. Schedule Tier 1 Builds**
- Calendar block: When will you build each Tier 1 item?
- Can any run in parallel (Batch API while you work on others)?

### Within 7 Days

**1. Complete All Tier 1 Builds**
- Execute the plan
- Track actual time vs estimated
- Track actual cost vs estimated

**2. Use New Infrastructure**
- Apply to your 2-4 item project RIGHT NOW
- Note what works, what's missing

**3. Update ROADMAP.md**
- Mark Tier 1 items complete
- Add Tier 2 items to backlog

### Within 30 Days

**1. Tier 2 Decision Gate**
- Did Tier 1 infrastructure get used?
- Did it deliver value?
- Should we proceed to Tier 2?

**2. Success Metrics Check**
- How many times was new infrastructure referenced?
- Did it save time or prevent mistakes?
- What's the actual ROI so far?

---

## Files You'll Generate

```
_shared/batch-results/
├── research-infrastructure-strategic-plan.md     (Opus's full review)

_shared/best-practices/                           (New builds from Tier 1)
├── research-design-methodology.md                (if Opus recommends)
├── research-quality-gates.md                     (if Opus recommends)
└── research-synthesis-workflow.md                (if Opus recommends)

_shared/workflows/                                (New builds from Tier 1)
└── research-integration-playbook.md              (if Opus recommends)

_shared/prompts/research/                         (New prompt library)
├── mining-extract-insights.md
├── compression-create-digest.md
├── synthesis-find-patterns.md
├── validation-quality-check.md
├── honesty-check-coverage.md
└── one-line-summary-generation.md
```

---

## Cost Breakdown by Option

| Option | Setup Time | Wait Time | Cost | Can Iterate? |
|--------|-----------|-----------|------|--------------|
| **A: Projects** | 15 min | None | $3-6 | ✅ Yes |
| **B: Batch API** | 10 min | 6-24h | $1.50-3 | ❌ No |
| **C: Claude Code** | 2 min | None | $3-6 | ✅ Yes |

---

## Quality Checklist

After receiving Opus's strategic plan, verify:

- [ ] All 8 gaps addressed
- [ ] YouTube KB consulted (specific video IDs cited)
- [ ] Priority matrix includes impact + effort scores
- [ ] Tier 1 items have 5-section outlines
- [ ] Success criteria are observable
- [ ] Resource allocation is realistic
- [ ] Dependencies identified
- [ ] Quick wins highlighted

**If any missing:** Ask Opus to elaborate on that section.

---

## Ready to Execute?

**Recommended next step:**

1. **Right now:** Open claude.ai → Projects
2. **15 minutes:** Upload 10 files, paste prompt
3. **1 hour:** Review Opus's strategic plan, ask follow-ups
4. **Today:** Pick ONE Tier 1 quick win and build it
5. **This week:** Complete all Tier 1 builds
6. **Use immediately:** Apply to your 2-4 item project

**This strategic review will guide your research infrastructure for the next 12 months across 10 companies. Worth doing right.** 🎯

---

**Choose your option and execute. Then come back with Opus's recommendations and we'll build Tier 1 together.**
