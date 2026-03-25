---
name: Verify Image Files Visually Before Using
description: Always Read-tool any image file to visually confirm content before referencing it in a presentation
type: feedback
source: patrick
---

Before using any image file: run `Read` on it to see the actual content, not just the filename.

**Why:** `finland-stadia-dark.png` was named like a map but was a 15KB QR code icon (512×512px). It went live and broke slide 2 in front of Sebastian. A single Read call would have caught it immediately.

**How to apply:**
- New image file (copied, downloaded, or unknown source) → Read it first
- Check: does the visual match the filename? Is it the right dimensions (not tiny)?
- `file` command gives dimensions but not content — only Read gives the visual
- Exception: files already used in the repo with known good history
