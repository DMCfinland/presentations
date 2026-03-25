# Document Import — Quick Reference Card

**For full details:** See [document-import-haiku-workflow.md](./document-import-haiku-workflow.md)

---

## 30-Second Checklist

```bash
# 1. Count source files
cd "/path/to/source/Company Name/" && find . -type f | wc -l

# 2. Launch Haiku agent
Task(model="haiku", prompt="Import [Company] from [source] to documents/{slug}/...")

# 3. Verify counts match
find /source/ -type f | wc -l
find documents/{company}/ -type f | wc -l

# 4. Update _index.md
echo "| Company | XXX files | 2026-02-XX | ✅ Complete |" >> documents/_index.md
```

---

## Category Keywords

| Folder | Keywords | Priority |
|--------|----------|----------|
| **talous/velkakirjat/** | velkakirja, laina, takaus, vakuus, rahoituspäätös | 🔴 Highest |
| **sopimukset/asiakas-sopimukset/** | sopimus + (Oy, Ltd, AB) | 🟠 High |
| **yritys/** | kaupparekisteriote, yhtiöjärjestys, pöytäkirja, hallitus, osakasluettelo | 🟡 Normal |
| **talous/** | tilinpäätös, tase, tuloslaskelma, tilintarkastus, verotus, ALV | 🟡 Normal |
| **sopimukset/** | sopimus, vuokrasopimus, yhteistyö, palvelu | 🟡 Normal |
| **toiminta/** | vakuutus, ELY, toimilupa, anniskelulupa, leasing | 🟡 Normal |
| **henkilosto/** | työsopimus, palkka, henkilöstö | 🟡 Normal |
| **kiinteistot/** | kauppakirja (property), lainhuuto, rasitus, kiinteistö | 🟡 Normal |
| **_arkisto/** | luonnos, draft, unsigned, duplicate, old versions | 🟢 Archive |

---

## Haiku Prompt Template

```markdown
Import and organize [COMPANY] documents.

Source: /path/to/source/
Destination: ~/1658HoldingsOy-AIFiles/documents/{company-slug}/
Files: [COUNT] files

Apply Finnish categorization:
- yritys/ → kaupparekisteriote, yhtiöjärjestys, pöytäkirja, hallitus
- sopimukset/ → sopimus (general)
  - asiakas-sopimukset/ → contracts with company names (Oy, Ltd)
- talous/ → tilinpäätös, tase, verotus, ALV
  - velkakirjat/ → velkakirja, laina, takaus, vakuus
- toiminta/ → vakuutus, ELY, toimilupa, anniskelulupa
- henkilosto/ → työsopimus, palkka
- kiinteistot/ → kauppakirja, lainhuuto, kiinteistö
- _arkisto/ → luonnos, draft, unsigned, duplicates

Rules:
1. Create all folders even if empty
2. Preserve Finnish characters (ä, ö)
3. PDFs active, .docx drafts to _arkisto/
4. Create IMPORT-LOG.txt with breakdown
5. Verify: source count = dest count

Output: File counts per category + verification
```

---

## Archive Rules (PDF vs DOCX)

| Scenario | Active Folder | Archive Folder |
|----------|--------------|----------------|
| Only PDF exists | ✅ PDF → category/ | - |
| Only DOCX exists | ✅ DOCX → category/ | - |
| Both PDF + DOCX | ✅ PDF → category/ | ❌ DOCX → _arkisto/ |
| Two PDFs same name | ✅ Newer → category/ | ❌ Older → _arkisto/ |
| Draft markers | - | ❌ luonnos/draft → _arkisto/ |

---

## Cost Guide

| Files | Duration | Cost | Model |
|-------|----------|------|-------|
| 1-50 | 1-2 min | $0.01 | Haiku |
| 51-200 | 2-3 min | $0.01-0.02 | Haiku |
| 201-1,000 | 3-5 min | $0.02-0.04 | Haiku |
| 1,001-1,500 | 5-7 min | $0.04-0.05 | Haiku |

**Never use Sonnet/Opus for imports** (12x more expensive, same result)

---

## Troubleshooting

**File count mismatch?**
```bash
diff -r /source/ /destination/ | grep "Only in"
```

**Wrong category?**
```bash
# Move manually
mv sopimukset/file.pdf talous/velkakirjat/
```

**Finnish characters broken?**
```bash
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
```

---

## After Import

- [ ] Update `documents/_index.md` Import Status table
- [ ] Add Document Log section to `_index.md`
- [ ] Spot-check 5 random files in correct categories
- [ ] Copy to Zone B if needed: `rsync -av documents/{company}/ ~/OneDrive/.../`

---

## Real Examples

**Small:** Karelia Outdoor (1 file) → 1 min, $0.01
**Medium:** Hotel Tahko (86 files) → 3 min, $0.01
**Large:** Järvisydän (1,244 files) → 5 min, $0.02

**Success rate:** 100% across 13 entities (2,408 files, zero data loss)

---

**Full documentation:** [document-import-haiku-workflow.md](./document-import-haiku-workflow.md)
