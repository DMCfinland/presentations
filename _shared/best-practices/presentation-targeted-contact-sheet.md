---
name: Targeted Contact Sheet for Presentations
description: Build a project-specific contact sheet (15–30 photos grouped by slide purpose) instead of using the generic folder-picker. Patrick-validated ★
type: feedback
source: patrick
session: 102
confidence: 0.9
---

# Targeted Contact Sheet — Build Project-Specific, Not Generic

Build a `contact-sheet-[project].html` with only the relevant candidate photos,
grouped by slide purpose, with one-click clipboard copy.

**Why:** Patrick explicitly said "Tykkäsin kuvan valitsija systeemistäsi!" (Loved the photo picker system). Generic contact sheet shows 100+ photos with no context. Targeted sheet shows 20–30 photos the AI already filtered, grouped by where they'll appear.

**How to apply:**
1. After reading the build prompt, identify ~20–30 candidate photos from the existing library
2. Group them by purpose: Cover / Key Metric / Activity / Boat/Transport / Closing / Neutral/Misc
3. Write `contact-sheet-[project].html` — clickable photo grid, green border on select, clipboard copy button
4. Open in browser (`open [file]`), ask Patrick to click and copy the list

**Template pattern** (from `contact-sheet-kulusiirto.html`):
- Photo cards: 280px min-width, 180px height, `object-fit: cover`
- Click to toggle: green border + "✓ VALITTU" badge
- Fixed bottom panel: textarea with selected filenames + "Kopioi lista" button
- Suggested use note under each photo: "Ehdotettu: Cover (Velimatti-deck)"

**When pool is insufficient:**
- Flag missing photos explicitly: "MS Puijo -kuvia ei löytynyt sopivaa"
- Claude picks up to 2 substitutes when user says "you can pick" — state which slides and why
- Never silently substitute without noting the gap

**When NOT to build targeted sheet:**
- New photo mining session where all 50–200 candidates are fresh (use generic folder picker)
- Quick single-photo swap iteration

**Source:** session 102, kulusiirto presentation build. Validated immediately by Patrick.
