---
name: Show Before Push — Local Review First
description: When Patrick says "show me first" or "before committing", always open locally and wait for approval before any git push
type: feedback
source: patrick
---

Never push to GitHub before Patrick has reviewed the change locally.

**Why:** Live presentations can break mid-meeting. Patrick had Sebastian live and the first push broke the map slide (QR code instead of map image). Even a correct change needs approval first — he may want tweaks.

**How to apply:**
- "show me", "näytä ensin", "before committing", "push to me" = `open [file]` locally → wait
- Only run `git push` after explicit approval ("hienoa", "push it", "go ahead", "pusketaan")
- If unsure: open locally AND ask "Haluatko että pusken GitHubiin?"
