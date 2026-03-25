---
name: Compress Images Before Pushing to GitHub Pages
description: Run ffmpeg compression on all images before git push — target max 1200px, under 300KB per image
type: feedback
source: session-111
---

Always compress images before pushing to GitHub Pages presentations.

**Why:** Uncompressed images were 600KB–1.3MB each. With 16 slides × multiple photos, this caused slow loading. After ffmpeg compression: largest file dropped from 1.3MB → 297KB (4-5× faster).

**Command (batch compress all jpgs in folder):**
```bash
for f in images/**/*.jpg; do
  ffmpeg -y -i "$f" -vf "scale='min(1200,iw)':-2" -q:v 6 "${f%.jpg}_tmp.jpg" && mv "${f%.jpg}_tmp.jpg" "$f"
done
```

**How to apply:**
- Any new image added to a presentation → compress before staging
- Full batch compress before major pushes
- Target: max 1200px wide, under 300KB per image
- sips (macOS built-in) does NOT work reliably for this — use ffmpeg
