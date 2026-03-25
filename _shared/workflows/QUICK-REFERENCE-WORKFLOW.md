# Workflow Quick Reference (ONE PAGE)

**Print this. Keep it on your desk. Use it for every task.**

---

## The Only Question That Matters: HOW MANY ITEMS?

```
   1-10 items  →  Load directly ($0.05-0.30, 2 min)
  10-50 items  →  Batch API ($1-5, wait 6-24h)
 50-500 items  →  Build 3-tier index ($8-15, use forever)
   >500 items  →  Split indexes / Vector DB ($20-200)
```

---

## Your Current Task: 2-4 items, 300 words each

### ✅ DO THIS:
1. Open Claude Code
2. Ask: "Read these 2 files and analyze for [question]"
3. Get answer
4. Done.

**Cost:** $0.05
**Time:** 2 minutes

### ❌ DON'T DO THIS:
- Build an index (overkill)
- Use Batch API (setup > processing)
- Create complex workflow (direct is faster)

---

## Model Selection (3 seconds)

| Task Type | Model | Cost |
|-----------|-------|------|
| **Strategic decision** | Opus | $0.60-2.00 |
| **Daily work/analysis** | Sonnet | $0.10-0.30 |
| **Simple/bulk tasks** | Haiku | $0.02-0.05 |

**Rule:** Default to Sonnet. Upgrade to Opus only for strategic/critical decisions.

---

## Interface Selection (3 seconds)

| Context | Use |
|---------|-----|
| **Local files** | Claude Code |
| **M365 mining (email/SharePoint)** | Claude for Desktop |
| **RAG/follow-ups/sharing** | claude.ai Projects |
| **Bulk processing (10+)** | Batch API |

---

## Tool Selection in Claude Code

| Task | Tool | Not |
|------|------|-----|
| "Read config.json" | Read tool | Task tool |
| "How does auth work?" | Task(Explore) | Grep manually |
| "Build implementation plan" | Task(Plan) | Direct prompt |
| "SEO audit for site X" | Task(seo-audit) | Manual tools |

**Rule:** Use Task tool for complex multi-step work. Use direct tools for simple operations.

---

## Batch API Checklist

**Use Batch API when:**
- ✅ 10+ items, same analysis each
- ✅ Can wait 6-24h
- ✅ Each item <334KB

**Steps:**
1. **PILOT** with 5-10 items first
2. Validate quality
3. Refine prompt if needed
4. Scale to full batch
5. Wait & retrieve

**Savings:** 50% off (Haiku $0.40/M, Sonnet $1.50/M, Opus $7.50/M)

---

## Red Flags (STOP IMMEDIATELY)

🚨 **Loading >200K tokens** (LLM only reads 6.5%)
🚨 **Building index for <50 items** (costs more than processing)
🚨 **Using Opus for tasks Sonnet handles** (5x cost, not 5x better)
🚨 **Skipping pilot on batch jobs** (can't fix prompts mid-flight)
🚨 **Uploading duplicates to Projects** ($25/query wasted)

---

## Cost Per Query (After Building Index)

| Context Size | Old Way | New Way | Savings |
|-------------|---------|---------|---------|
| 2-4 items (your task) | $0.05 | $0.05 | 0% (already optimal) |
| 50 items | $2.50 | $0.50 | 80% |
| 200 items | $10.00 | $1.00 | 90% |
| 500 items | $25.00 | $1.50 | 94% |

**Break-even:** Query 1 (index build = $8-15)

---

## Orchestration Patterns

**Pattern 1: Opus Plans → Sonnet Executes** (85% savings)
```
Opus: Design strategy ($5)
Sonnet (×10): Build tools ($1.50)
Opus: Review & adjust ($2)
Total: $8.50 vs $55 all-Opus
```

**Pattern 2: Sonnet Gathers → Opus Synthesizes** (79% savings)
```
Sonnet batch: Analyze 189 items ($20)
Human: Prioritize top 20
Opus: Deep analysis of top 20 ($16)
Total: $36 vs $170 all-Opus
```

**Pattern 3: Progressive Filtering** (94% savings)
```
Haiku: Filter 1000 → 200 ($1)
Sonnet: Analyze 200 → 50 ($3)
Opus: Deep dive on 50 ($5)
Total: $9 vs $150 all-Opus
```

---

## Before Every Task (30-second checklist)

- [ ] Count items
- [ ] Calculate size (1KB ≈ 4 pages ≈ 250 tokens)
- [ ] Strategic? → Opus. Execution? → Sonnet.
- [ ] Local/M365/Projects/Batch?
- [ ] >10 items + same analysis? → Consider Batch API
- [ ] >50 items + 20+ queries? → Consider index
- [ ] Pilot first if batch or index
- [ ] Track actual cost

---

## Emergency Decision Tree (10 seconds)

```
Is it strategic/critical?
  ├─ YES → Opus
  └─ NO  → Sonnet

How many items?
  ├─ <10   → Load directly
  ├─ 10-50  → Batch API
  ├─ 50-500 → Build index
  └─ >500   → Vector DB / Split

Where's the data?
  ├─ Local files      → Claude Code
  ├─ M365             → Claude for Desktop
  ├─ Need RAG/sharing → claude.ai Projects
  └─ Bulk processing  → Batch API

Done. Execute.
```

---

## Full Documentation

See [WORKFLOW-DECISION-FRAMEWORK.md](WORKFLOW-DECISION-FRAMEWORK.md) for complete details.

---

**Keep this visible. Use it every time. Update when patterns change.**
