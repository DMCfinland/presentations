# HTML Presentation Workflow — Lessons from Lakeland Summer Deck
source: patrick + session 61
status: Tier B (promote after reuse on Lapland/Helsinki decks)
use_when: building B2B sales presentations with real photos

## Architecture
- HTML + CSS + presentation mode JS — no PowerPoint, no PDF needed
- template-styles-v2.css = shared design system (Grok 4.20 research)
- Each deck = 1 HTML file with inline photo assignments + shared CSS
- Press P for fullscreen presentation mode (arrow keys navigate)

## Photo Workflow (CRITICAL — biggest time sink)
1. **Mine photos first** — WordPress REST API, kuvat.fi sitemap, PPTX extraction
2. **Open folder in Finder** — let Patrick pick photos by visual inspection
3. **Never guess photos by filename** — AI can't tell a ski boot room from a restaurant
4. **Assign in one pass** after Patrick confirms filenames
5. **Compress for sharing** — only include used images, resize to 1920px (12MB vs 52MB)

## Photo Sources (Finland DMC)
- PPTX unzip: rename .pptx → .zip, extract ppt/media/
- PDF extraction: `pdfimages -j` (PPM masks need sips conversion)
- WordPress REST API: `/wp-json/wp/v2/media?per_page=100&mime_type=image/jpeg`
- kuvat.fi media bank: sitemap.xml has all image URLs with `?img=img2048`
- Media bank RSS: `?img=full` gives print quality (9.6MB per photo)

## Sharing / Distribution
- **GitHub Pages** = best option (free, permanent, professional URL)
  - `gh repo create DMCfinland/[deck-name] --public --source=. --push`
  - Enable Pages via API: `gh api repos/.../pages --method POST --input - <<< '{"source":{"branch":"main","path":"/"}}'`
  - URL: `dmcfinland.github.io/[deck-name]`
- **Netlify Drop** = backup (drag folder, instant but temporary)
- **Zip** = offline sharing (include only used images)
- **PDF** = broken with Chrome headless for flex layouts — avoid unless PrinceXML

## PDF Print Issues (Unsolved)
- Chrome headless `--print-to-pdf` ignores `@page size: landscape`
- Grok's `.slide + .slide { page-break-before: always }` pattern helps but still splits
- `min-height: 100vh` works in browser, breaks in print (needs explicit 210mm)
- **Current workaround**: skip PDF, use HTML presentation mode instead

## Design System (Grok 4.20)
- Fonts: Cormorant Garamond headlines + Montserrat 300 body
- Palette: #F8F4ED cream, #D4AF37 gold accents, #1C1C1C charcoal
- 60px margins, 12-column CSS Grid
- Slide types: cover, stats, content-lr, content-rl, activities mosaic, product cards, map, impact, company
- `beforeprint` JS event to set clean PDF filename

## Naming Convention
- HTML title: `Finland DMC - [Destination] [Season]`
- GitHub repo: `DMCfinland/[deck-name]`
- PDF (if needed): `Finland DMC - Lakeland Summer.pdf`
- No special characters (em dash, pipe) — they break PDF filenames

## Deck Series
- 03-Lapland-Winter-v2.html (done, needs photo upgrades)
- 04-Lakeland-Summer.html (done, live on GitHub Pages)
- 05-Helsinki-Citybreak.html (photos ready, deck not built)
- 06-Finland-Overview.html (maps ready, deck not built)
