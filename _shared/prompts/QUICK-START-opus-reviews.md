# Quick Start: Get Opus to Review Your Handoff Materials

**Goal:** Before handing SEO work to your team, have Opus check if the materials will work well for people who might feel nervous about technical tasks.

---

## Step 1: Make Sure API Key is Loaded

Open Terminal and run:

```bash
cd ~/1658HoldingsOy-AIFiles
export ANTHROPIC_API_KEY=$(security find-generic-password -a "anthropic" -s "ANTHROPIC_API_KEY" -w)
```

You should see no errors. If you get an error, the key isn't stored yet. Run:

```bash
bash _shared/scripts/store-api-key.sh
```

---

## Step 2: Run the Review

```bash
python3 _shared/scripts/run-opus-review.py sensitive-team-seo \
  --playbook JarvisydanOy-AIFiles/WORDPRESS-PLAYBOOK.md \
  --action_plan JarvisydanOy-AIFiles/seo-audits/jarvisydan/ACTION-PLAN.md
```

**What happens:**
- Script loads the playbook + action plan + supporting guides
- Sends to Opus with the "sensitive team" review prompt
- Opus reviews from a nervous team member's perspective
- Compares simplified playbook vs full 40-item action plan
- You see the review streaming in real-time (2-3 minutes)
- Saves result to: `_shared/batch-results/opus-sensitive-team-seo-review-[date].md`

**Cost:** ~$1-2

---

## Step 3: Read the Review

Open the saved file. Opus will tell you:

✅ **What works well** (keep these parts)
⚠️ **What might cause anxiety** (fix these parts)
🔧 **Specific improvements** (exact changes to make)
📊 **Confidence scores** (will the team succeed?)
⏱️ **Time estimate reality check** (are your estimates honest?)
📋 **Playbook vs Action Plan decision** (which document to share with team?)

---

## Step 4: Improve & Re-Review (Optional)

If Opus finds issues:

1. Fix the playbook based on recommendations
2. Run the review again
3. Compare scores (did confidence improve?)
4. Repeat until Opus says "Ready to hand off"

---

## What If It Doesn't Work?

### "API key not found"
Run: `bash _shared/scripts/store-api-key.sh` first

### "File not found"
Make sure you're in the right directory: `cd ~/1658HoldingsOy-AIFiles`

### "Authentication error"
The stored key might be wrong. Delete and re-store:
```bash
security delete-generic-password -a "anthropic" -s "ANTHROPIC_API_KEY"
bash _shared/scripts/store-api-key.sh
```

### Want to see available reviews?
```bash
python3 _shared/scripts/run-opus-review.py --list
```

---

## Example: Full Run

```bash
# 1. Go to project folder
cd ~/1658HoldingsOy-AIFiles

# 2. Load API key
export ANTHROPIC_API_KEY=$(security find-generic-password -a "anthropic" -s "ANTHROPIC_API_KEY" -w)

# 3. Run review
python3 _shared/scripts/run-opus-review.py sensitive-team-seo \
  --playbook JarvisydanOy-AIFiles/WORDPRESS-PLAYBOOK.md \
  --action_plan JarvisydanOy-AIFiles/seo-audits/jarvisydan/ACTION-PLAN.md

# 4. Read result
open _shared/batch-results/opus-sensitive-team-seo-review-2026-02-11.md
```

That's it! 🎉

---

**Pro tip:** Run this review BEFORE presenting to your team. It's much easier to fix materials now than to deal with confused or overwhelmed staff later.

**Cost-conscious?** One $2 review can save weeks of team confusion and resistance. High ROI.

---

*Need help? Check the full README: `_shared/prompts/README-opus-reviews.md`*
