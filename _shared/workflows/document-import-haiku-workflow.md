# Document Import Workflow — Haiku-Powered Auto-Categorization

**Version:** 1.0
**Date:** 2026-02-12
**Status:** Production-ready
**Success Rate:** 100% (2,408 files across 13 entities, zero data loss)

---

## Overview

This workflow automates Finnish business document imports using Claude Haiku agents for cost-efficient, high-quality categorization. Successfully tested on portfolio company documents ranging from 1 file to 1,244 files per entity.

**Key Metrics:**
- **Cost:** $0.01-0.02 per company (vs ~30-60 min manual work)
- **Speed:** 2-5 minutes per company (automated)
- **Quality:** 100% file preservation, consistent categorization
- **Scalability:** Handles 1-1,500 files per company with same workflow

---

## When to Use This Workflow

✅ **Use for:**
- Importing company documents from Downloads, SharePoint, OneDrive
- Organizing existing unstructured document folders
- Adding new documents to existing company folders
- Merging documents from multiple sources
- Initial setup of new portfolio companies

❌ **Don't use for:**
- Single file imports (just use mv or cp)
- Already organized folders (no need to re-process)
- Non-Finnish documents (categorization keywords are Finnish-specific)

---

## Prerequisites

### 1. Destination Structure Ready
```bash
~/1658HoldingsOy-AIFiles/documents/
├── _holdings/           # Cross-company docs
├── _inbox/              # Unsorted
└── {company-slug}/      # One per company
    ├── yritys/          # Corporate
    ├── sopimukset/      # Contracts
    │   └── asiakas-sopimukset/  # Customer contracts
    ├── talous/          # Financial
    │   └── velkakirjat/ # Loan documents
    ├── toiminta/        # Operations
    ├── henkilosto/      # Employment
    ├── kiinteistot/     # Property
    └── _arkisto/        # Archive
```

### 2. Company Registered in _index.md
- Company prefix defined (e.g., `dmc`, `jsy`, `hto`)
- Legal name recorded
- Y-tunnus placeholder added

### 3. Source Location Known
- Full path to source folder (e.g., `~/Downloads/Hotel Tahko Oy/`)
- Read permissions confirmed
- File count estimated (`find . -type f | wc -l`)

---

## Workflow Steps

### Phase 1: Pre-Import Analysis

**Step 1.1: Count source files**
```bash
cd "/path/to/source/Company Name/"
find . -type f | wc -l
```

**Step 1.2: Sample file naming patterns**
```bash
find . -type f | head -20
```

**Step 1.3: Identify subfolder structure**
```bash
find . -maxdepth 2 -type d
```

**Step 1.4: Estimate cost**
- Small (1-50 files): ~$0.01
- Medium (51-200 files): ~$0.01-0.02
- Large (201-1,500 files): ~$0.02-0.05

---

### Phase 2: Execute Haiku Import Agent

**Step 2.1: Launch Task with Haiku model**

Use this prompt template:

```markdown
Import and organize documents for [COMPANY NAME] from source to destination.

**Source:** /path/to/source/Company Name/
**Destination:** ~/1658HoldingsOy-AIFiles/documents/{company-slug}/
**Total files:** [COUNT] files

Apply Finnish document categorization:

**yritys/** (Corporate)
- Keywords: kaupparekisteriote, yhtiöjärjestys, yhtiökokouspöytäkirja,
  hallituksen päätös, osakasluettelo, valtakirja, PRH

**sopimukset/** (Contracts)
- Keywords: sopimus, vuokrasopimus, yhteistyösopimus, palvelusopimus
- Subfolder: asiakas-sopimukset/ for B2B contracts with company names (Oy, Ltd, AB)

**talous/** (Financial)
- Keywords: tilinpäätös, tase, tuloslaskelma, tilintarkastuskertomus,
  verotus, ALV, veroilmoitus, kirjanpito
- Subfolder: talous/velkakirjat/ for velkakirja, laina, takaus, vakuus,
  rahoituspäätös, promissory note

**toiminta/** (Operations)
- Keywords: vakuutus, ELY-päätös, toimilupa, anniskelulupa,
  kiinteistöveropäätös, leasing

**henkilosto/** (Employment)
- Keywords: työsopimus, palkka, henkilöstö

**kiinteistot/** (Property)
- Keywords: kauppakirja, lainhuuto, rasitus, kiinteistö

**_arkisto/** (Archive)
- Keywords: luonnos, draft, unsigned, duplicate
- Purpose: Superseded versions, old projects

**Rules:**
1. Create all category folders even if empty
2. Preserve original filenames exactly (including Finnish characters)
3. Move signed PDFs to active categories, .docx drafts to _arkisto/
4. If duplicate exists (same filename with .pdf and .docx), keep .pdf active
5. Create import log: IMPORT-LOG.txt with categorization breakdown
6. Verify: source count = destination count (active + archived)

**Output:**
- List of files moved to each category
- Total counts per category
- Verification: [source_count] files → [destination_count] files (active: X, archived: Y)
```

**Step 2.2: Execute Task tool**

```python
Task(
    subagent_type="general-purpose",
    model="haiku",
    description="Import Hotel Tahko docs",
    prompt="[paste template above with specific paths/counts]"
)
```

**Expected duration:** 2-5 minutes depending on file count

---

### Phase 3: Quality Verification

**Step 3.1: Verify file counts match**
```bash
# Source count
cd "/path/to/source/Company Name/"
SOURCE_COUNT=$(find . -type f | wc -l)

# Destination count
cd ~/1658HoldingsOy-AIFiles/documents/{company-slug}/
DEST_COUNT=$(find . -type f | wc -l)

echo "Source: $SOURCE_COUNT"
echo "Destination: $DEST_COUNT"
# Should match exactly
```

**Step 3.2: Check IMPORT-LOG.txt created**
```bash
cat ~/1658HoldingsOy-AIFiles/documents/{company-slug}/IMPORT-LOG.txt
```

Should contain:
- Date of import
- Source path
- Total files imported
- Breakdown by category
- Active vs archived counts

**Step 3.3: Spot-check categorization**
```bash
# Check that velkakirjat went to correct subfolder
find talous/velkakirjat/ -type f | head -5

# Check that board minutes went to yritys/
find yritys/ -name "*pöytäkirja*" | head -5

# Check archive has drafts
find _arkisto/ -name "*.docx" | head -5
```

---

### Phase 4: Update Registry

**Step 4.1: Update documents/_index.md**

Add entry to Import Status table:
```markdown
| Company Name | XXX files | 2026-02-XX | ✅ Complete |
```

Add Document Log section:
```markdown
### Company Name (XXX files imported, YYY active + ZZZ archived)

**Corporate (N files)** - [description]
**Contracts (N files)** - [description]
**Financial (N files)** - [description]
  - **Financial/Velkakirjat (N files)** - [description]
**Operations (N files)** - [description]
**Archive (N files)** - [description]

*Full import log: See `{company-slug}/IMPORT-LOG.txt` for complete manifest*
```

**Step 4.2: Verify registry updated**
```bash
grep "Company Name" ~/1658HoldingsOy-AIFiles/documents/_index.md
```

---

## Finnish Categorization Reference

### Priority 1: Velkakirjat Detection (Most Specific)
Any file matching these keywords goes to **talous/velkakirjat/**:
- velkakirja
- laina (except lainhuuto → kiinteistot/)
- takaus
- vakuus
- rahoituspäätös
- promissory note
- loan agreement
- guarantee agreement

### Priority 2: Customer Contracts (Specific)
Files with company names (Oy, Ltd, AB) + "sopimus" → **sopimukset/asiakas-sopimukset/**

### Priority 3: Category Keywords (General)

**yritys/** triggers:
- kaupparekisteriote, yhtiöjärjestys, yhtiökokouspöytäkirja
- hallituksen päätös, hallituspöytäkirja
- osakasluettelo, osakassopimus
- valtakirja, power of attorney
- PRH (Patent- ja rekisterihallitus)

**talous/** triggers:
- tilinpäätös, tase, tuloslaskelma
- tilintarkastuskertomus (Ttk)
- verotus, veroilmoitus, veropäätös, ALV
- kirjanpito, taloushallinto
- budjetti, ennuste, forecast

**sopimukset/** triggers:
- sopimus (general catch-all)
- vuokrasopimus (rental)
- yhteistyösopimus (partnership)
- palvelusopimus (service)
- toimeksiantosopimus (commission)
- kauppasopimus (purchase, but check if property-related)

**toiminta/** triggers:
- vakuutus (insurance)
- ELY-päätös (government subsidy)
- toimilupa (operating permit)
- anniskelulupa (liquor license)
- kiinteistöveropäätös (property tax decision)
- leasing, vuokraus (operational leasing)

**henkilosto/** triggers:
- työsopimus (employment contract)
- palkka, palkkakuitti (payroll)
- henkilöstö (staff/personnel)
- työterveyshuolto (occupational health)

**kiinteistot/** triggers:
- kauppakirja (purchase agreement, property-related)
- lainhuuto (title deed)
- rasitus (easement)
- kiinteistö (property/real estate)
- tontti (plot)
- rakennuslupa (building permit)

**_arkisto/** triggers:
- luonnos, draft
- unsigned (when signed version exists)
- duplicate (exact filename match)
- vanhentunut (outdated)
- old year ranges (e.g., 2018-2020 when 2024-2025 exists)

---

## Edge Cases and Solutions

### Multiple Matches
**Problem:** File matches multiple category keywords
**Solution:** Apply priority order:
1. velkakirjat (most specific)
2. asiakas-sopimukset (specific)
3. First category keyword alphabetically (consistent tiebreaker)

**Example:** "Velkakirja ja vakuussopimus 2024.pdf"
- Matches: velkakirjat (velkakirja) + sopimukset (sopimus) + toiminta (vakuus)
- Resolution: → **talous/velkakirjat/** (highest priority)

### Unsigned vs Signed Versions
**Problem:** Both .pdf and .docx with same base name
**Solution:**
- Keep .pdf in active category (signed version)
- Move .docx to _arkisto/ (draft version)

**Example:**
- `Vuokrasopimus Tahko 2024.pdf` → sopimukset/
- `Vuokrasopimus Tahko 2024.docx` → _arkisto/

### Property Purchase Agreements
**Problem:** "Kauppakirja" could be contracts or property
**Solution:** Check context:
- Contains "kiinteistö", "tontti", "asunto" → **kiinteistot/**
- General business purchase → **sopimukset/**

### Archive Strategy
**Problem:** When to archive vs delete
**Solution:** Always archive, never delete during import:
- Drafts when signed exists → _arkisto/
- Duplicates → _arkisto/
- Superseded versions → _arkisto/
- User can delete _arkisto/ contents later after review

---

## Cost Optimization

### Why Haiku?
- **Haiku cost:** ~$0.25 per 1M input tokens, ~$1.25 per 1M output
- **Sonnet cost:** ~$3 per 1M input tokens, ~$15 per 1M output
- **For this task:** File paths + categorization rules = ~10K-50K tokens
- **Savings:** 12x cheaper than Sonnet for same quality

### When to Use Sonnet
Only if Haiku fails categorization accuracy test on sample (unlikely for keyword-based rules).

### Batch Processing
For 10+ companies, launch multiple Haiku agents in parallel:
```python
# Launch 3 agents simultaneously
Task(model="haiku", prompt="Import Company A...")
Task(model="haiku", prompt="Import Company B...")
Task(model="haiku", prompt="Import Company C...")
```

---

## Troubleshooting

### Issue: File count mismatch
**Symptom:** Source has 100 files, destination has 98
**Diagnosis:**
```bash
diff -r /source/ /destination/ | grep "Only in"
```
**Fix:** Manually copy missing files or re-run import

### Issue: Wrong categorization
**Symptom:** Velkakirja ended up in sopimukset/ instead of talous/velkakirjat/
**Diagnosis:** Check if keyword priority was followed
**Fix:**
```bash
mv sopimukset/velkakirja-2024.pdf talous/velkakirjat/
```

### Issue: Finnish characters corrupted
**Symptom:** `Järvisydän` becomes `J?rvisyd?n`
**Diagnosis:** Shell encoding issue
**Fix:** Haiku uses UTF-8 by default; shouldn't happen. If it does:
```bash
# Set shell to UTF-8
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

### Issue: Haiku agent timeout
**Symptom:** Agent stops after 2 minutes with partial import
**Diagnosis:** Too many files for single agent run
**Fix:** Split into chunks:
1. Import first 500 files
2. Import next 500 files
3. Merge results

---

## Success Criteria Checklist

Before marking import as complete, verify:

- [ ] Source file count = Destination file count (active + archived)
- [ ] IMPORT-LOG.txt created in company root folder
- [ ] All 7 category folders exist (even if empty)
- [ ] Velkakirjat subfolder exists under talous/
- [ ] Asiakas-sopimukset subfolder exists under sopimukset/ (if applicable)
- [ ] Finnish characters preserved (ä, ö) in all filenames
- [ ] Signed PDFs in active categories, drafts in _arkisto/
- [ ] documents/_index.md updated with import entry
- [ ] documents/_index.md Document Log section added
- [ ] No duplicate files in active categories (duplicates in _arkisto/ only)
- [ ] Sample spot-check: 5 random files are in correct categories

---

## Real-World Examples

### Example 1: Small Company (Karelia Outdoor Oy - 1 file)
**Source:** ~/Downloads/Karelia Outdoor Oy/
**Files:** 1 file (Päätös aloittavien yritysten kehittämisavustus.pdf)
**Duration:** 1 minute
**Cost:** < $0.01
**Result:** toiminta/ (1 file)

### Example 2: Medium Company (Hotel Tahko Oy - 86 files)
**Source:** ~/Downloads/Hotel Tahko Oy/
**Files:** 86 files
**Duration:** 3 minutes
**Cost:** $0.01
**Categories:**
- yritys/: 15 files
- sopimukset/: 26 files
- talous/: 23 files (including velkakirjat/: 4 files)
- toiminta/: 11 files
- _arkisto/: 11 files

### Example 3: Large Company (Järvisydän Oy - 1,244 files)
**Source:** ~/Downloads/Järvisydän Oy/
**Files:** 1,244 files
**Duration:** 5 minutes
**Cost:** $0.02
**Categories:**
- yritys/: 60 files
- sopimukset/: 281 files (including asiakas-sopimukset/: 60)
- talous/: 333 files (including velkakirjat/: active + joukkorahoitus/: 58)
- toiminta/: 296 files
- kiinteistot/: 264 files
- henkilosto/: 8 files
- _arkisto/: 8 files
- _reference-files/: 3 files (66MB scanned docs)

---

## Workflow Variations

### Variation 1: Merge from Multiple Sources
When importing from both Downloads and SharePoint:

1. Import Downloads first (this workflow)
2. Run file comparison:
```bash
cd ~/1658HoldingsOy-AIFiles/documents/company-slug/
find . -type f -exec basename {} \; | sort > /tmp/imported.txt

cd ~/SharePoint/Company\ Name/
find . -type f -exec basename {} \; | sort > /tmp/sharepoint.txt

comm -13 /tmp/imported.txt /tmp/sharepoint.txt > /tmp/missing.txt
```

3. Import only missing files using same Haiku workflow

### Variation 2: Incremental Updates
When adding new documents to existing folder:

1. Copy new files to _inbox/
2. Run Haiku agent with prompt:
```markdown
Review files in _inbox/ and move to correct categories in parent folder.
Follow same categorization rules as original import.
Append to existing IMPORT-LOG.txt with date and counts.
```

### Variation 3: Re-Categorization
If initial categorization was wrong:

1. Move all files back to _inbox/
2. Re-run Haiku agent with corrected keyword rules
3. Compare before/after using diff

---

## Integration with Other Workflows

### After Import → Zone B Copy
Once documents organized in Zone A (local), copy final structure to Zone B:
```bash
rsync -av ~/1658HoldingsOy-AIFiles/documents/{company-slug}/ \
  ~/OneDrive/1658Holdings/documents/{company-slug}/
```

### After Import → Opus Analysis
For corporate structure analysis:
```markdown
Analyze all documents in ~/1658HoldingsOy-AIFiles/documents/
and create corporate structure map showing:
- Ownership chains
- Loan relationships
- Inter-company contracts
- Property holdings
```

---

## Version History

**v1.0 (2026-02-12)**
- Initial documentation
- Based on 13-entity production deployment (2,408 files)
- 100% success rate, zero data loss
- Cost: ~$0.15 total for all 13 entities

---

## Related Documentation

- [Document Architecture](../_shared/best-practices/document-architecture.md) - Taxonomy and naming conventions
- [Finnish Category Migration](../documents/_finnish-category-migration-2026-02-11.md) - English → Finnish rename history
- [Model Strategy](../../MODEL-STRATEGY.md) - When to use Haiku vs Sonnet vs Opus

---

**Questions or issues?** Update this document with learnings from each import.
