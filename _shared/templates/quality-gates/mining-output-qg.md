# Quality Gate: Mining Output / Second Brain Data

Run this checklist AFTER de-sloppify pass, BEFORE building final deliverables.

## Completeness
- [ ] All requested searches/extractions were completed (no skipped searches)
- [ ] Output blocks from mining session match the expected count
- [ ] No "I'll continue in the next message" loose ends
- [ ] Gap report exists — what was NOT found is documented

## Deduplication
- [ ] No duplicate entries saying the same thing in different words
- [ ] Client profiles don't have the same contact listed twice
- [ ] Revenue figures appear once per time period (not duplicated across sources)
- [ ] Staff assignments are consistent (no conflicting role descriptions)

## Contradiction Check
- [ ] No two entries disagree without being flagged
- [ ] Revenue figures from different sources are reconciled
- [ ] Client contact details are consistent across mentions
- [ ] Dates and timelines are consistent

## Confidence Marking
- [ ] Each insight marked HIGH / MEDIUM / LOW confidence
- [ ] HIGH = multiple independent sources
- [ ] MEDIUM = single clear source
- [ ] LOW = inferred or ambiguous
- [ ] LOW-confidence items flagged for Patrick's review

## Structure
- [ ] Insights grouped by logical category (not dump order)
- [ ] Section headers present and descriptive
- [ ] Cross-references to source files included
- [ ] CLEANUP SUMMARY present (what was merged, flagged, compressed)

## Second Brain Ready
- [ ] Format compatible with target Second Brain files (YAML for profiles, MD for narratives)
- [ ] New entries have all required fields (name, source, date, confidence)
- [ ] Updates to existing entries are merge-safe (won't overwrite good data)
- [ ] Orphaned references flagged (mentions without corresponding profiles)
