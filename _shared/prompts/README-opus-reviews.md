# Opus Review Prompts — How to Use

This folder contains ready-to-use Opus prompts for strategic reviews and analysis.

---

## Available Prompts

### 1. Sensitive Team SEO Handoff Review
**File:** `opus-sensitive-team-seo-handoff-review.md`

**When to use:** Before handing off technical work to a team that might feel nervous or overwhelmed.

**What it does:**
- Reviews materials from a nervous team member's perspective
- Checks for anxiety triggers and overwhelming language
- Validates time estimates (catches optimistic estimates)
- Suggests tone improvements and simplifications
- Scores "confidence building" vs "anxiety inducing"

**How to use:**
```bash
cd ~/1658HoldingsOy-AIFiles

# Option 1: Run via Python script (coming soon)
python3 _shared/scripts/run-opus-review.py sensitive-team-seo

# Option 2: Manual (copy prompt + materials to claude.ai)
# 1. Copy prompt: opus-sensitive-team-seo-handoff-review.md
# 2. Attach: WORDPRESS-PLAYBOOK.md + supporting guides
# 3. Send to Opus
```

**Cost:** ~$1-2 per review (20K-30K tokens in, 4K-8K tokens out)

---

## Running Opus Reviews Locally

### Prerequisites
- API key stored in Keychain (run: `bash _shared/scripts/store-api-key.sh`)
- Python 3.12+ with anthropic SDK (`pip install anthropic`)

### Quick Command
```bash
# Load API key
export ANTHROPIC_API_KEY=$(security find-generic-password -a "anthropic" -s "ANTHROPIC_API_KEY" -w)

# Run review (example)
python3 _shared/scripts/run-opus-review.py sensitive-team-seo \
  --playbook JarvisydanOy-AIFiles/WORDPRESS-PLAYBOOK.md \
  --output _shared/batch-results/opus-sensitive-team-review.md
```

---

## Best Practices

### When to Use Opus Reviews
- ✅ Strategic decisions (architecture, approach, communications)
- ✅ Human-facing materials (handoffs, documentation, training)
- ✅ Quality checks before expensive actions (large rollouts, team presentations)
- ✅ Emotional intelligence needs (team dynamics, sensitive topics)

### When NOT to Use Opus
- ❌ Simple factual lookups (use Sonnet or grep)
- ❌ Code generation (use Sonnet)
- ❌ Bulk processing (use Batch API with Haiku)
- ❌ Quick iterations (save Opus for final review)

### Cost Management
- Opus: $15/M input, $75/M output
- A typical review: 20K-30K in, 4K-8K out = $1-2
- Budget: Use Sonnet for drafts, Opus for final quality check

---

## Prompt Design Principles

Good Opus prompts:
1. **Specific perspective:** "Review as if you're a nervous team member"
2. **Clear output format:** Structured sections, scores, recommendations
3. **Honest assessment:** "Be honest, not polite" instruction
4. **Actionable fixes:** Not just "this is bad" but "change X to Y"
5. **Context-rich:** Include background, constraints, success criteria

---

## Adding New Prompts

When creating a new Opus review prompt:

1. **Name it clearly:** `opus-[purpose]-review.md`
2. **Include context section:** Who, what, why, constraints
3. **Define the perspective:** "Review as if you're..."
4. **Specify output format:** Sections, scores, recommendations
5. **Add it to this README:** Update the list above
6. **Test it once:** Validate it produces useful output

---

## Saved Reviews

Completed reviews are saved in: `_shared/batch-results/`

Naming: `opus-[topic]-[date].md`

Example:
- `opus-jarvisydan-playbook-review-2026-02-11.md`
- `opus-finnish-governance-merge-2026-02-11.md`

---

*Last updated: 2026-02-11*
