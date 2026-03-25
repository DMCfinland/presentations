# M365 Mining Prompt — Finland DMC Presentation Assets

**Use this prompt in Claude Desktop with M365 Connector.**
**Goal:** Download all brand assets and presentation source files from Finland DMC SharePoint/OneDrive to a local folder so Claude Code can use them to build new presentations.

---

## PROMPT (copy everything below this line)

---

I need you to find and download specific files from Finland DMC's M365 environment (SharePoint, OneDrive, Teams). Save everything to this local folder:

**Save location:** `~/Downloads/dmc-presentation-assets/`

Create these subfolders and put files in the right one:

### 1. `/brand/` — Brand assets
Find and download:
- Finland DMC logo files (all formats — PNG, SVG, AI, EPS, PDF)
- Any brand guidelines or style guide documents
- Brand color palette files
- Font files if stored anywhere
- The Viestintäkäsikirja (Communication Handbook) if there's a newer version than the local one

### 2. `/presentations/` — All existing presentation files
Find and download every .pptx, .key, or presentation PDF, including:
- "Introduction to Levi as a Destination.pdf" (the Levi Tour template we saw today)
- Finland DMC Investment offer
- Finland DMC Sijoitus esitys
- Finland DMC Parmaco esitys
- Finland DMC x Rantasalmen kunta
- DMC Strategia / Johtaminen / Toimeenpano
- DMC Myyntistrategia
- The Digital Pivot
- ANY other presentations or pitch decks I haven't listed

### 3. `/photos/` — High-quality photos for presentations
Find and download the best photos from Finland DMC's files, organized by destination:
- `/photos/lapland/` — Levi, Rovaniemi, Saariselkä, northern lights, snow activities
- `/photos/lakeland/` — Saimaa, Järvisydän, Rantasalmi, lake views, summer activities
- `/photos/helsinki/` — City, cathedral, market square, design district
- `/photos/activities/` — Husky safaris, snowmobiles, ice fishing, sauna, aurora, hiking
- `/photos/accommodation/` — Hotels, igloos, chalets, cabins, glass igloos
- `/photos/people/` — Team photos, staff at work, guests (if available)

Look in: SharePoint image libraries, OneDrive photo folders, Teams shared files, any marketing folders.

### 4. `/templates/` — PowerPoint/presentation templates
Find and download:
- Any .potx (PowerPoint template) files
- Master slide files
- Branded slide templates from Brande agency (the web/brand partner)

### 5. `/content/` — Text content for presentations
Find and download:
- Company description / boilerplate texts (EN + FI)
- Sales materials, brochures, marketing copy
- Client testimonials or case studies
- Destination descriptions (Lapland, Lakeland, Helsinki, etc.)
- Rate cards or pricing summary documents
- Supplier/partner lists

### 6. `/list/` — The presentation to-do list
Patrick mentioned there's a list of presentations to be made. Find:
- Any document listing planned presentations or pitch decks
- Meeting notes from today's Teams call about presentations
- Any task list, project plan, or to-do related to sales/marketing materials

---

## AFTER DOWNLOADING

When you're done, create a file called `DOWNLOAD-MANIFEST.md` in the `~/Downloads/dmc-presentation-assets/` folder that lists:

```
# DMC Presentation Assets — Download Manifest
Date: [today's date]
Source: Finland DMC M365

## Files Downloaded
### /brand/
- [filename] — [what it is] — [source location in M365]

### /presentations/
- [filename] — [what it is] — [source location in M365]

### /photos/
- [filename] — [destination category] — [source location in M365]

(etc. for all folders)

## Files NOT Found
- [what was looked for but doesn't exist in M365]

## Bonus Finds
- [anything useful you found that wasn't specifically requested]
```

This manifest helps Claude Code know exactly what's available for building the presentations.

---

## IMPORTANT NOTES
- Download the ACTUAL files, not just links
- If a file is too large, note it in the manifest with the file size and M365 location
- Prioritize high-resolution photos — we need them for presentations
- If you find the Levi Tour PDF ("Introduction to Levi as a Destination.pdf"), that's the template we want to replicate
- Check both Patrick's OneDrive AND any shared Finland DMC SharePoint sites
