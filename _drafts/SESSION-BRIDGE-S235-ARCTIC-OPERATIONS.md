---
session: 231
date: 2026-04-15
type: SESSION BRIDGE — Arctic Cruises Booking System + Operations Brief
model_wrote: sonnet-4-6
model_executes: sonnet
priority: MEDIUM
chmod: 444
supersedes: SESSION-BRIDGE-S231-ARCTIC-LAUNCH.md (S234 booking PRD portion)
---

# SESSION BRIDGE S235
# ARCTIC CRUISES — BOOKING SYSTEM PRD + LAURA OPERATIONS BRIEF
# chmod 444 — älä muokkaa

---

## CONTEXT

By S235, we have:
- B2C website LIVE (V3.3)
- B2B flyer BUILT (S232)
- FAM invitation pack BUILT (S233)
- Operator PRD BUILT (S234)

**This session builds the operational layer** — how Laura actually runs the business day-to-day: booking management system recommendation, communication templates, and her operating brief.

---

## DELIVERABLE 1: BOOKING SYSTEM PRD

**File:** `arctic-cruises-booking-system-prd.md`

### Context
Current state: Inquiry form on website → mailto → email only.
This is adequate pre-launch but will not scale past 10 active enquiries simultaneously.
Goal: Recommend and specify the simplest system Laura can use to manage bookings.

### Evaluate 3 Options

**Option A: Airtable (recommended for Year 1)**
- Free tier: up to 1,000 records, sufficient for Year 1
- Tables: Enquiries · Confirmed Bookings · Departure Calendar · Operator Accounts
- Views: Calendar view (departures + pax count), Kanban (enquiry → confirmed → invoiced → complete)
- Automation: Email reminder 60 days before (balance due), 30 days before (guest names)
- Cost: Free–€18/month

**Option B: Notion Database**
- Simpler to set up, less powerful automation
- Good if Laura already uses Notion
- No native calendar view without workaround

**Option C: Google Sheets + Calendar**
- Zero cost, maximum simplicity
- Manual reminders only — risk of human error at scale
- Acceptable for <20 bookings/year

**Recommendation:** Airtable (Option A) — build the schema now, set up when bookings open Jan 2027.

### Airtable Schema

**Table 1: Enquiries**
Fields: Name · Email · Country · Party Size · Product · Preferred Date · Status [New/Contacted/Quoted/Dead] · Notes · Date Received

**Table 2: Confirmed Bookings**
Fields: Booking ID · Client Name · Email · Operator (if via trade) · Product Code · Departure Date · Party Size · Total (list) · Net (if trade) · Deposit Paid · Deposit Date · Balance Due Date · Balance Paid · Guest Names Received · Special Requirements · Status [Confirmed/Deposit Paid/Balance Due/Complete/Cancelled]

**Table 3: Departure Calendar**
Fields: Departure Date · Product · Capacity Available · Bookings Confirmed · Pax Count · Revenue (gross) · Status [Open/Limited/Closed]

**Table 4: Operator Accounts**
Fields: Company · Contact Name · Country · Email · Market · Early Partner (Y/N) · Commission % · FAM Attended · First Booking Date · Total Bookings · Notes

### Communication Templates (see Deliverable 2)

---

## DELIVERABLE 2: LAURA OPERATIONS BRIEF

**File:** `arctic-cruises-laura-operations-brief.md`
**Audience:** Laura Ilvonen — her complete guide to running Arctic Cruises trade relations and booking management

### Structure

**Part 1: The Website — What It Does and Doesn't Do**
- B2C URL: https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html
- Forms go to: laura@finlanddmc.fi (mailto form)
- When to update: pricing changes, new season dates, after FAM (add testimonials)
- Who makes changes: Patrick/Claude Code — email Patrick to request

**Part 2: Responding to Enquiries**

Template A — B2C Enquiry Response (within 24 hours):
```
Subject: Your Arctic Cruises Enquiry — Lake Saimaa 2027

Dear [Name],

Thank you for your enquiry about the [Grand Cruise / Short Cruise / Day Cruise] on Lake Saimaa.

I am delighted to confirm that [preferred date] is currently available.

Attached: Full voyage details and pricing.

[If 7-night:] The Grand Cruise (7 nights) is priced at €2,600 per person, full board. For a couple, that is €5,200 total — all accommodation at authentic Saimaa resorts, every meal included, smoke sauna, gala dinner, and our full expert team on board.

Bookings open formally January 2027. I can add you to our priority list now, which guarantees you first access to your preferred date when booking opens.

Would that be helpful?

With kind regards,
Laura Ilvonen
Arctic Cruises & Finland DMC
laura@finlanddmc.fi
```

Template B — Trade/Operator Enquiry Response:
```
Subject: Arctic Cruises 2027 — Net Rate Sheet & Operator Information

Dear [Name],

Thank you for your interest in Arctic Cruises, Lake Saimaa.

Please find attached:
1. Operator Product & Requirements Document (full product spec)
2. Net Rate Sheet 2027

Summary: We are offering 20% commission (net rate basis) to early partners who confirm before 15 July 2026. After that date, standard terms apply.

I would also like to invite you to consider joining our inaugural FAM voyage:
31 August – 3 September 2026 · Complimentary · 50 places only
Please reply with your interest by 15 July 2026.

I am available for a call this week if you would like to discuss. Which time works for you?

With kind regards,
Laura Ilvonen
Arctic Cruises & Finland DMC
laura@finlanddmc.fi
```

Template C — FAM Application Confirmation:
```
Subject: FAM Voyage 2026 — Application Received

Dear [Name],

Thank you for applying to the Arctic Cruises FAM voyage (31 Aug – 3 Sep 2026).

We are reviewing all applications and will confirm selected partners by [date: 1 June 2026].

We aim to select 50 operators from across DACH, UK, US, Australia, and the Nordic region.

In the meantime, please feel free to visit our website for full product information:
https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html

With kind regards,
Laura Ilvonen
```

Template D — Booking Confirmation + Deposit Invoice:
```
Subject: Booking Confirmed — [Product] · [Date] · Booking Ref [AC-XXXX]

Dear [Name],

Your [Grand Cruise / Short Cruise] on [date] is confirmed.

Booking Reference: AC-[XXXX]
Party: [N] guests
Departure: [Date], 09:00, Lappeenranta Harbour
Return: [Date], ~12:00, Lappeenranta Harbour
Total: €[X] (per attached invoice)

DEPOSIT DUE: €[30% amount] — please pay within 14 days.
BALANCE DUE: €[70% amount] — due by [60 days before date].

[Payment details]

I will contact you 30 days before departure for:
- Guest names and nationalities
- Dietary requirements and allergies
- Special requests

If you have any questions before then, I am here.

With kind regards,
Laura
```

**Part 3: FAM Workflow (2026)**

Key dates:
- Now → 15 July: Receive applications, respond with confirmation email
- 15 July: Application deadline
- 1 June: Target — confirm 50 selected operators, send confirmation
- August: Send programme brief + logistics pack to confirmed FAM guests
- 30 Aug (day before): Send final reminder with meeting point, what to bring
- 31 Aug–3 Sep: FAM voyage
- 4 Sep onwards: Follow up with media pack + commercial agreement form

**Part 4: Trade Show & Cold Outreach**

Priority events for Laura/Patrick to attend with B2B flyer:
- ITB Berlin (March 2027 — book booth if budget allows; attend as visitor 2026)
- WTM London (November 2026)
- Nordic Visit organisations — direct relationship building
- DACH specialist tour operators — cold email with flyer + PRD

Cold outreach sequence:
1. Email: B2B flyer + personal note (max 3 sentences)
2. Follow-up if no response after 7 days: "Did you get my note about Lake Saimaa?"
3. FAM invitation if interest shown

**Part 5: After FAM — The Critical 30 Days**

- Day 1-3 after FAM: Send media pack to all 50 operators
- Day 7: Send commercial agreement to operators who expressed interest on board
- Day 14: First follow-up call with top 10 priority operators
- Day 30: Review: how many commercial agreements signed? Target: 15+
- Day 45: Activate website testimonials from FAM guests

---

## KEY FILES TO LOAD

```yaml
key_files:
  - ~/1658HoldingsOy-AIFiles/_drafts/arctic-b2b-commercial-brief.md
  - ~/1658HoldingsOy-AIFiles/_drafts/SESSION-BRIDGE-S234-ARCTIC-OPERATOR-PRD.md
  - ~/1658HoldingsOy-AIFiles/arctic-cruises-b2c.html
```

turn_budget: 4-6
external_calls: "None required — operational document, no external spar needed"
session_type: BUILD (2 documents)

---

*Bridge v1.0 — S231 2026-04-15*
*chmod 444*
