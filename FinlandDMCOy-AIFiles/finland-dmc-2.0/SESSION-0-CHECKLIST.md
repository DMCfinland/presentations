# Session 0 — "Open the Mine" Setup Checklist

**Date:** 2026-02-18
**Purpose:** Validate M365 access and prepare infrastructure for 5 coordinated mining sessions
**Time estimate:** 30-45 minutes
**Outputs:** Confirmed access + folder structure + test results

---

## DECISION: Mining Happens in Claude Desktop

**Access confirmed:** Patrick has sales@Finland-dmc.com login credentials.
**Claude Code M365 access:** Patrick's personal mailbox only (no client emails there).
**SharePoint access from Claude Code:** Yes — board minutes, weekly meeting notes, proposals.

**Workflow:**
1. **Claude Desktop** — log in with sales@ credentials, enable M365 connector, mine emails
2. **Claude Code** — receives pasted outputs, saves to correct files, organizes data
3. **SharePoint docs** — Claude Code can pull these directly (proposals, meeting notes)

---

## STEP 1: Set Up Claude Desktop for Mining (10 min)

1. Open Claude Desktop app
2. Go to Settings → Integrations → Microsoft 365
3. **Sign in with:** sales@Finland-dmc.com (NOT Patrick's personal account)
4. Grant the M365 connector access to search emails
5. Test with a simple query:
   ```
   Search my inbox for emails from the past 30 days. Show 5 results with subject, sender, date.
   ```
6. If results appear → move to Step 2

**Troubleshooting:**
- If M365 connector not available → check Claude Desktop version (needs latest)
- If sign-in fails → verify sales@ credentials are correct
- If no results → try broader search: "Show my most recent 10 emails"

---

## STEP 3: Create Local Folder Structure (5 min)

Run in Claude Code or terminal:

```
mining-outputs/
├── session-0-setup/
│   └── session-log.md
├── session-1-client-comms-outbound/
│   ├── EMAIL-DRAFTER/
│   └── SECOND-BRAIN/
├── session-2-inbound-emails/
│   ├── EMAIL-DRAFTER/
│   └── SECOND-BRAIN/
├── session-3-router/
│   ├── EMAIL-DRAFTER/
│   └── SECOND-BRAIN/
├── session-4-proposals/
│   ├── EMAIL-DRAFTER/
│   └── SECOND-BRAIN/
└── session-5-pricing/
    ├── EMAIL-DRAFTER/
    └── SECOND-BRAIN/
```

---

## STEP 4: Run Test Queries (15 min)

Test 5 queries to validate search quality. Log results in session-0 session-log.md.

### Query 1: Basic email search
```
Search sales@Finland-dmc.com for sent emails from 2025 containing "proposal"
```
Expected: Proposal emails to clients

### Query 2: Inbound inquiries
```
Search sales@Finland-dmc.com inbox for emails received in 2024-2025
about "group tour" or "incentive trip"
```
Expected: Client inquiry emails

### Query 3: SharePoint documents
```
Search SharePoint for files containing "proposal" or "itinerary" or "tarjous"
```
Expected: Proposal documents (.docx, .pdf)

### Query 4: Teams messages
```
Search Teams messages in Finland DMC channels about pricing or suppliers
```
Expected: Internal team discussions

### Query 5: Excel files
```
Search SharePoint for Excel files related to pricing, rates, or budget
```
Expected: Rate cards, pricing sheets

### Scoring
| Query | Result | Quality |
|-------|--------|---------|
| 1. Sent proposals | | good/partial/empty |
| 2. Inbound inquiries | | good/partial/empty |
| 3. SharePoint docs | | good/partial/empty |
| 4. Teams messages | | good/partial/empty |
| 5. Excel files | | good/partial/empty |

**Go/No-Go:** At least Query 1 AND Query 2 must return "good" results. If not, troubleshoot access before starting Session 1.

---

## STEP 5: Estimate Data Volume (10 min)

Get rough counts for mining planning:

```
How many emails are in the sales@ inbox from the past 2 years?
How many sent emails from the past 2 years?
How many unique client email addresses appear in sent emails?
```

Log results:
- Total inbox emails (2yr): ___
- Total sent emails (2yr): ___
- Unique client contacts: ___
- Most active months: ___

This tells us mining density and which sessions will be richest.

---

## STEP 6: Verify OneDrive Sync (5 min)

- [ ] OneDrive app running on Mac
- [ ] Finland DMC site synced to local Finder
- [ ] Path confirmed: ~/OneDrive - 1658 Holdings/FinlandDMCOy/AI-Knowledge/
- [ ] Test: create a file locally, verify it appears in SharePoint within 5 min

---

## GO/NO-GO DECISION

| Requirement | Status | Notes |
|-------------|--------|-------|
| Email search works (sent) | [ ] | |
| Email search works (inbox) | [ ] | |
| SharePoint search works | [ ] | |
| Local folders created | [ ] | |
| Mining tool decided (Code vs Desktop) | [ ] | |
| OneDrive sync verified | [ ] | |

**All green → Start Session 1**
**Email access blocked → Troubleshoot delegation / try Desktop fallback**
**SharePoint blocked → Sessions 1-3 can proceed (email-only), Sessions 4-5 need SharePoint**

---

## SESSION 0 OUTPUT

Save to `mining-outputs/session-0-setup/session-log.md`:
- Access method chosen (Code or Desktop)
- Test query results (5 queries)
- Data volume estimates
- Any blockers discovered
- Confirmed ready for Session 1: YES/NO
