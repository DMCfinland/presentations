# Strategic Decision Prompt: Document Architecture for 1658 Holdings

**Target:** Claude Opus (claude.ai)
**Purpose:** Get a definitive architectural decision on where company documents should live
**Cost estimate:** ~$0.50 (small context, one-shot)
**Instructions:** Copy everything below the line into claude.ai as a single message.

---

# STRATEGIC DECISION REQUEST: Company Document Architecture

## Who You Are Advising

Patrick Heiskanen, CEO of **1658 Holdings Oy** — a Finnish family holding company with **10 portfolio companies** and ~50 employees total. Patrick is building an AI-powered knowledge management system using Claude Code (local file orchestration) and Claude Projects (team AI assistants via M365 connector).

## The Decision I Need

I'm about to import company documents for ALL 10 portfolio companies (contracts, corporate docs, financial statements, board minutes, property records, articles of association, etc.). These documents will be:

1. **Archived** with clear naming conventions
2. **Used as knowledge base** for an AI document drafter
3. **Referenced** to build corporate structure "WHO" story documents (visual/Canva-style overviews of each company)
4. **Source of truth** for fact-correct document generation

**The question:** Should documents live under each company's folder, OR in a central holdings-level folder?

## Current Architecture

### Two-Zone System (Already Built)

**Zone A (Workshop)** — `~/1658HoldingsOy-AIFiles/` — local Mac + Git
- Where Patrick builds things with Claude Code
- AI work products: mining outputs, custom instructions, audits, prompts
- NOT synced to cloud, NOT accessible to staff
- Version controlled via Git (local only)

**Zone B (Company Knowledge)** — `~/OneDrive - 1658 Holdings/AI Files/` — synced to SharePoint
- Final deliverables ONLY (custom instructions, tone guides, staff reference)
- Searchable by Claude AI via M365 connector
- Flat structure, clear naming, no drafts
- Accessible to staff (read-only)

### Current Zone A Folder Structure
```
~/1658HoldingsOy-AIFiles/
├── CLAUDE.md                          # Holdings-wide AI config
├── ROADMAP.md                         # Master progress tracker
├── MODEL-STRATEGY.md                  # Which AI model for which task
├── _shared/                           # Cross-company resources
│   ├── best-practices/                # Reusable guides (5 files, 50KB)
│   ├── prompt-library/                # (planned)
│   └── templates/                     # (planned)
├── FinlandDMCOy-AIFiles/              # Company 1: DMC (5 staff)
│   ├── CLAUDE.md
│   ├── finland-dmc-2.0/              # AI project: custom instructions
│   │   ├── mining-outputs/
│   │   ├── project-files/
│   │   ├── templates/
│   │   └── reference/
│   └── seo-audits/                   # SEO work (managed companies)
│       └── jarvisydan/               # 12 files, 200KB
├── YouTubeResearch-AIFiles/           # Research project (not a company)
│   └── knowledge-base/
│       ├── videos/                    # 195 analyzed videos
│       └── channels/
└── [Future companies 3-10]
```

### How Companies Relate

```
1658 Holdings Oy (parent)
├── Finland DMC Oy (DMC, 5 staff) — manages IT/marketing for other companies
├── Järvisydän Oy (resort operator, has employees)
│   └── [Multiple property companies] (kiinteistöyhtiöt, no employees)
├── [Company 3-10] (various industries, TBD)
```

Key: Finland DMC manages IT and marketing for Järvisydän and potentially other portfolio companies. But each is a separate legal entity with its own documents.

## The Two Options

### Option A: Per-Company (Distributed)
```
FinlandDMCOy-AIFiles/
├── documents/                    # Finland DMC corporate docs
│   ├── corporate/
│   ├── contracts/
│   └── financial/
├── finland-dmc-2.0/             # AI project (existing)
└── seo-audits/                  # SEO work (existing)

JarvisydanOy-AIFiles/
├── documents/                    # Järvisydän corporate docs
│   ├── corporate/
│   ├── property-companies/
│   └── operations/
└── [future AI projects]

[Company3]-AIFiles/
├── documents/
└── [future AI projects]
```

**Pros:**
- Self-contained per company (everything in one place)
- Follows existing AIFiles pattern
- Natural boundary per legal entity
- Clear ownership

**Cons:**
- Document drafter needs to navigate 10 separate folders
- Cross-company patterns harder to see
- Naming conventions could drift per company
- Holdings-level documents (shareholder agreements, group financials) don't have a natural home

### Option B: Central Holdings Folder (Centralized)
```
1658HoldingsOy-AIFiles/
├── documents/                         # ALL company documents
│   ├── _holdings/                     # Holdings-level docs
│   │   ├── shareholder-agreements/
│   │   └── group-financials/
│   ├── finland-dmc-oy/
│   │   ├── corporate/
│   │   ├── contracts/
│   │   └── financial/
│   ├── jarvisydan-oy/
│   │   ├── corporate/
│   │   ├── property-companies/
│   │   │   ├── [kiinteistoyhtiö-1]/
│   │   │   └── [kiinteistoyhtiö-2]/
│   │   └── operations/
│   └── [company-3]/
├── FinlandDMCOy-AIFiles/              # AI work products (existing)
├── YouTubeResearch-AIFiles/           # Research (existing)
└── _shared/                           # Templates, best practices (existing)
```

**Pros:**
- Single root for document drafter to access everything
- Universal naming conventions enforced from one place
- Cross-company docs (holdings-level) have natural home
- Easy to build corporate structure overview
- Clear separation: `documents/` = source truth, `*-AIFiles/` = AI work products

**Cons:**
- Separates a company's documents from its AI work products
- Could grow very large as a single folder tree
- Need clear naming rules or it becomes a dump

## Context for Your Decision

### What the Document Drafter Needs
The document drafter will be an AI tool that:
- Takes a template (company-specific or universal)
- Pulls facts from the document archive (names, dates, addresses, registration numbers, board members)
- Generates fact-correct documents (board minutes, contracts, resolutions, annual reports)
- Needs to access documents across multiple companies (e.g., inter-company agreements)

### What the "WHO" Story Documents Need
Visual/Canva-style overviews showing:
- Each company's purpose, structure, key people
- How companies relate to each other
- Which property companies belong to which operator
- Key dates, registration numbers, contact info

### Future Evolution: Second Brain Architecture
We're studying Nate B Jones' AI-powered "second brain" system (capture → classify → surface loops). Key principles that may apply:

1. **Single capture point** — one place to drop everything, AI classifies automatically
2. **Structured storage** — consistent schemas make automation possible
3. **Audit trails** — every action logged for trust and debugging
4. **Proactive surfacing** — system pushes relevant info, not just stores it
5. **Confidence thresholds** — automated classification with human override

The document architecture should be "second brain compatible" — meaning it should work as a structured storage layer that AI can classify into and retrieve from programmatically.

### Constraints
- This is a Mac-based local filesystem (Zone A) — no database, no cloud API
- Documents will be .pdf, .docx, .xlsx primarily (scanned and digital)
- Need to work with Claude Code (reads files from disk)
- Must be simple enough that Patrick can maintain it manually
- Will eventually have hundreds of documents per company
- Must support Finnish and English documents
- Some documents span multiple companies (inter-company agreements, group financials)

## What I Need From You

1. **A definitive recommendation** — Option A, Option B, or a hybrid. Not "it depends."
2. **Folder structure** — Show me the exact folder tree with naming conventions
3. **Naming rules** — Universal file naming convention for documents
4. **Category taxonomy** — Standard document categories that work across all company types
5. **How cross-company documents are handled** — Where do inter-company agreements live?
6. **Second brain compatibility** — How does this architecture support future AI automation (capture → classify → surface)?
7. **Scaling assessment** — Will this still work with 10 companies × 200 docs each = 2,000 documents?

**Format:** Write your answer as a structured markdown document I can save as `_shared/best-practices/document-architecture.md`. Make it a best practices guide, not just an answer — this is a document we'll reference for years.

**Important:** Be decisive. Patrick needs a clear answer, not a list of trade-offs. Pick the best option and commit to it. If you need to create a hybrid, define it precisely.
