# Pattern: Mining Output Transfer — Avoid Double Context
<!-- last_updated: session-28 -->

**name:** mining-output-transfer
**source:** patrick (Session 29, 2026-02-18)
**tier:** B

## What
When pasting large mining output blocks from Claude Desktop into Claude Code for file-saving, you are loading 10K–30K tokens of raw data into Claude Code's context window unnecessarily. Claude Code only needs to write the file — it doesn't need to analyze the content.

## Why It's a Problem
- Each output block (MINING-REPORT, RATE-CARD, SUPPLIER-DATABASE) = ~5–15K tokens
- Pasting all 3 blocks into Claude Code = ~30–45K tokens consumed just for file saves
- Claude Code's context fills with mining data it won't reference again
- This doubles the cost of retrieval: once in Claude Desktop (mining), once in Claude Code (saving)

## Better Approaches (in order of preference)

**Option A — Save directly without pasting (best):**
Copy the output block text from Claude Desktop → open the target file in VS Code → paste directly → save. Claude Code is not involved. Zero context cost.

**Option B — Spawn a file-saver subagent (good):**
If you want Claude Code to handle the save, use a Haiku subagent (Task tool) with the content in the prompt. The main context stays clean. Cost: ~$0.001 per block.

**Option C — Paste into main context (current/acceptable):**
Acceptable for small blocks (<5K tokens) or when you need Claude Code to process/validate the content. Not ideal for pure save operations.

## When Option C IS acceptable
- You want Claude Code to verify structure, fix formatting, or merge with existing files
- The block is small (single table or short section)
- You're already in a long session and context cost is acceptable

## Rule of Thumb
**If the only action is "save this to a file" → don't paste into main context.**
**If Claude Code needs to do something with the content → paste is fine.**

## Source Session
Session 29, 2026-02-18. Patrick flagged after pasting Session 5 MINING-REPORT (~10K tokens) into Claude Code purely to save it to disk.
