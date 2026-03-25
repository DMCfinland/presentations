---
name: Presentations Photo Library — Two Locations
description: Presentation photos exist in two places — main images/ repo AND presentations subfolder untracked archive
type: reference
source: session-111
---

When searching for photos for presentations, check BOTH locations:

**Location 1 (in git, production-ready):**
`~/1658HoldingsOy-AIFiles/images/lakeland/`
`~/1658HoldingsOy-AIFiles/images/general/`
`~/1658HoldingsOy-AIFiles/images/helsinki/`

**Location 2 (untracked archive, larger selection):**
`~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/project-files/presentations/images/lakeland/`
`~/1658HoldingsOy-AIFiles/FinlandDMCOy-AIFiles/project-files/presentations/images/general/`

Location 2 contains dozens of additional photos (xc-ski-mining subfolder, vl-* series, etc.) not yet promoted to main repo. Search here when Location 1 doesn't have what you need.

**Search pattern:**
```bash
find ~/1658HoldingsOy-AIFiles -name "*keyword*" | grep -v node_modules | grep -v .git
```

**Photo selection workflow:**
1. Search both locations
2. Read each candidate visually (Read tool)
3. Show Patrick all options
4. Copy chosen photo to images/lakeland/ (or general/)
5. Compress with ffmpeg before commit
6. Push only after Patrick approves locally
