# Model Tracking System

## Problem

With videos analyzed by both Sonnet 4.5 and Opus 4.6, we need to:
- ✅ Track which model analyzed each video
- ✅ Upgrade Sonnet analyses to Opus without losing originals
- ✅ Search/filter by analysis model
- ✅ Maintain version history

## Solution: Metadata + Archive Strategy

### File Structure

```
knowledge-base/
├── videos/                           # 📁 CANONICAL (latest/best)
│   ├── 2025-12-19-video-title.md    # Opus or Sonnet (whichever is best)
│   └── ...
└── videos-archive/                   # 📦 HISTORY
    ├── sonnet/
    │   └── 2025-12-19-video-title-sonnet-v1-20260210.md
    └── opus/
        └── (future: if Opus gets upgraded to Opus 5)
```

**Principle:**
- `videos/` = Single source of truth (best available analysis)
- `videos-archive/` = Version history for reference/comparison

### Metadata Fields

Every video markdown file includes:

```yaml
---
title: Video Title
type: video-analysis
channel: ai-news-strategy-daily-nate-b-jones.md
video_id: ABC123xyz
video_url: https://www.youtube.com/watch?v=ABC123xyz
duration: 18:37
published: 2025-12-19
analyzed: 2026-02-10
analysis_model: claude-opus-4-6           # 🎯 NEW
analysis_version: 2                        # 🎯 NEW
previous_versions:                         # 🎯 NEW (if upgraded)
  - model: claude-sonnet-4-5
    date: 2026-02-10
    archived: videos-archive/sonnet/[filename]
tags: [ai-agents, productivity]
key_concepts: [delegation, reliability]
strategic_value: high
quality_score: 5
---
```

### Upgrade Flow

**When Opus analyzes a video that Sonnet already did:**

1. **Check** if file exists
2. **Archive** Sonnet version to `videos-archive/sonnet/[name]-sonnet-v1-[timestamp].md`
3. **Update** metadata: `analysis_version: 2`, add to `previous_versions`
4. **Save** Opus analysis as canonical in `videos/`

**Result:**
- Best analysis in main folder
- History preserved in archive
- Clear lineage tracked in metadata

## Usage

### Processing Results with Tracking

**Enhanced script:**
```bash
# Process Sonnet batch
python scripts/process-batch-results-with-tracking.py tier1

# Process Opus batch (auto-detects model, archives Sonnet)
python scripts/process-batch-results-with-tracking.py opus
```

**What it does:**
- Auto-detects model from tier name (opus = Opus 4.6, tier1/2/3 = Sonnet 4.5)
- Adds `analysis_model` metadata
- Archives existing versions before upgrading
- Tracks version history in frontmatter

### Finding Videos by Model

**List Opus-analyzed videos:**
```bash
python scripts/list-by-model.py opus
```

**List Sonnet-analyzed videos:**
```bash
python scripts/list-by-model.py sonnet
```

**Show statistics:**
```bash
python scripts/list-by-model.py stats
```

**Manual grep:**
```bash
# Find all Opus analyses
grep -l "analysis_model: claude-opus-4-6" knowledge-base/videos/*.md

# Find all Sonnet analyses
grep -l "analysis_model: claude-sonnet-4-5" knowledge-base/videos/*.md

# Count by model
grep "analysis_model:" knowledge-base/videos/*.md | cut -d: -f3 | sort | uniq -c
```

## Migration: Adding Metadata to Existing Files

If you already have videos without `analysis_model` metadata:

```bash
# Process existing files and add metadata
python scripts/add-model-metadata.py --model claude-sonnet-4-5 --dry-run

# Actually update files
python scripts/add-model-metadata.py --model claude-sonnet-4-5
```

## Examples

### Sonnet-Only Video

```yaml
---
title: Video About AI Agents
analyzed: 2026-02-10
analysis_model: claude-sonnet-4-5
analysis_version: 1
---
```

### Upgraded to Opus

**Original (archived):**
```yaml
# videos-archive/sonnet/2025-12-19-ai-agents-sonnet-v1-20260210.md
---
title: Video About AI Agents
analyzed: 2026-02-10
analysis_model: claude-sonnet-4-5
analysis_version: 1
---
```

**New canonical:**
```yaml
# videos/2025-12-19-ai-agents.md
---
title: Video About AI Agents
analyzed: 2026-02-11
analysis_model: claude-opus-4-6
analysis_version: 2
previous_versions:
  - model: claude-sonnet-4-5
    date: 2026-02-10
    archived: videos-archive/sonnet/2025-12-19-ai-agents-sonnet-v1-20260210.md
---
```

## Search Queries

### By Strategic Value (Opus only)
```bash
python scripts/list-by-model.py opus | grep "Strategic: high"
```

### Upgraded Videos (has version history)
```bash
grep -l "previous_versions:" knowledge-base/videos/*.md
```

### Count Each Model
```bash
echo "Opus: $(grep -l 'claude-opus-4-6' knowledge-base/videos/*.md | wc -l)"
echo "Sonnet: $(grep -l 'claude-sonnet-4-5' knowledge-base/videos/*.md | wc -l)"
```

## Best Practices

1. **Always use process-batch-results-with-tracking.py** for new batches
2. **Never delete archives** - disk space is cheap, lost data is expensive
3. **Check model before quoting** - Opus analyses are more reliable for strategic decisions
4. **Re-prioritize periodically** - After reading Sonnet analyses, you might find new gems for Opus upgrade
5. **Track costs** - Tag in ROADMAP which batches used which model

## Future: Opus 5 Upgrade Path

When Opus 5 comes out:

```
videos-archive/
├── sonnet/
│   └── [video]-sonnet-v1-[date].md
├── opus-4-6/
│   └── [video]-opus46-v2-[date].md
```

Same metadata pattern:
```yaml
analysis_model: claude-opus-5
analysis_version: 3
previous_versions:
  - model: claude-sonnet-4-5
    date: 2026-02-10
  - model: claude-opus-4-6
    date: 2026-02-11
```

## Summary

✅ **Single source of truth** - Best analysis in `videos/`
✅ **Version history** - Archives in `videos-archive/`
✅ **Clear metadata** - Know which model analyzed each video
✅ **Easy search** - Filter by model, strategic value, version
✅ **Future-proof** - Ready for future model upgrades
✅ **No data loss** - Old versions archived, not deleted
