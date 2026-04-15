# Arctic Cruises — Booking System PRD
## Version 1.0 · 2026-04-15 · Prepared for Laura Ilvonen

---

## Section 1: Current State + Goal

### Current State

The Arctic Cruises website contains an enquiry form that sends directly to `laura@finlanddmc.fi` via mailto. This is the right approach pre-launch: zero cost, zero infrastructure, and Laura sees every enquiry personally.

**The limitation:** Email alone does not scale past approximately 10 simultaneous enquiries without bookings falling through the cracks — no status tracking, no reminders, no departure capacity overview.

### Goal

Specify the simplest booking management system Laura can use from **January 2027** when the first commercial bookings open. The system must:

- Track enquiries from first contact to confirmed booking
- Show departure calendar capacity at a glance
- Store operator accounts with FAM and commission status
- Send automated payment reminders without manual effort
- Require no technical knowledge to operate

---

## Section 2: Options Evaluated

### Option A: Airtable — RECOMMENDED

**Cost:** Free tier up to 1,000 records (sufficient for Year 1). Pro plan €18/month if automation or more records needed.

**Strengths:**
- Four-table relational database: Enquiries, Confirmed Bookings, Departure Calendar, Operator Accounts
- Calendar view shows departure dates, pax count, and capacity at a glance
- Kanban view tracks enquiry → contacted → quoted → confirmed → complete pipeline
- Automation: balance reminder 60 days before departure, guest name request 30 days before
- Shareable with Patrick for oversight; no IT setup required
- Free tier covers all Year 1 volume (estimated 20–40 bookings)

**Weaknesses:**
- Requires one-time setup (3–4 hours with Patrick)
- Not a full invoicing system (invoices sent separately by email)

---

### Option B: Notion Database

**Cost:** Free tier available. Plus plan €8/month.

**Strengths:**
- Familiar interface for users already on Notion
- Good for notes, SOPs, and databases in one workspace
- Simple to set up quickly

**Weaknesses:**
- Limited native automation (requires Zapier or Make integration for email triggers)
- No native calendar view without workaround
- Less structured for relational data (enquiry → booking → operator linked records)

**Verdict:** Adequate if Laura already uses Notion heavily. Not recommended as a dedicated booking system.

---

### Option C: Google Sheets + Calendar

**Cost:** Zero.

**Strengths:**
- Zero setup cost, immediately familiar
- Google Calendar integration for departure dates
- Sufficient for fewer than 20 bookings per year

**Weaknesses:**
- Manual reminders only — high risk of human error as volume grows
- No relational linking between enquiries, bookings, and operators
- No pipeline view

**Verdict:** Acceptable as a temporary measure during pre-launch (now until December 2026). Replace with Airtable before January 2027.

---

### Recommendation

**Airtable (Option A).** Build the schema now so it is ready when bookings open in January 2027. Use Google Sheets as a stopgap if needed during the FAM period (August–September 2026) to track operator applications.

Activate Airtable: **October 2026.**

---

## Section 3: Airtable Schema — Complete Field Specifications

### Table 1 — ENQUIRIES

| Field | Type | Notes |
|-------|------|-------|
| Name | Single line text | First and last name |
| Email | Email | Primary contact |
| Country | Single line text | Country of residence |
| Party Size | Number | Number of guests |
| Product | Single select | AC-DAY / AC-3N / AC-7N |
| Preferred Date | Date | Requested departure date |
| Status | Single select | New / Contacted / Quoted / Dead |
| Notes | Long text | Free notes field |
| Date Received | Date | When enquiry arrived |
| Source | Single select | B2C / Trade / FAM / Referral |

---

### Table 2 — CONFIRMED BOOKINGS

| Field | Type | Notes |
|-------|------|-------|
| Booking ID | Single line text | Format: AC-0001, AC-0002, etc. |
| Client Name | Single line text | Lead guest name |
| Email | Email | Lead guest email |
| Phone | Phone number | Lead guest phone |
| Operator | Linked record | Link to Table 4 if via trade |
| Product Code | Single select | AC-DAY / AC-3N / AC-7N |
| Departure Date | Date | Wednesday departure |
| Return Date | Date | End of voyage |
| Party Size | Number | Total number of guests |
| Total List Price | Currency (€) | Full B2C price |
| Net Rate | Currency (€) | Trade net rate if applicable |
| Deposit Amount | Currency (€) | 30% of total |
| Deposit Paid Date | Date | When deposit received |
| Balance Amount | Currency (€) | 70% of total |
| Balance Due Date | Date | 60 days before departure |
| Balance Paid Date | Date | When balance received |
| Guest Names Received | Checkbox | Y/N — names list from client |
| Special Requirements | Long text | Accessibility, celebrations, etc. |
| Dietary Notes | Long text | All dietary requirements and allergies |
| Status | Single select | Confirmed / Deposit Paid / Balance Due / Complete / Cancelled |
| Notes | Long text | Internal notes |

---

### Table 3 — DEPARTURE CALENDAR

| Field | Type | Notes |
|-------|------|-------|
| Departure Date | Date | Every Wednesday, May–September 2027 |
| Day of Week | Single line text | Always Wednesday |
| Product | Single select | AC-DAY / AC-3N / AC-7N |
| Season Week # | Number | Week 1, 2, 3… of season |
| Capacity Total | Number | 200 pax (M/S Carelia max) |
| Bookings Confirmed | Number | Count of confirmed bookings |
| Pax Count | Number | Total passengers booked |
| Revenue Gross | Currency (€) | Gross revenue at list price |
| Status | Single select | Open / Limited (< 20 remaining) / Closed |
| Notes | Long text | Special notes, charter holds, etc. |

---

### Table 4 — OPERATOR ACCOUNTS

| Field | Type | Notes |
|-------|------|-------|
| Company Name | Single line text | Travel trade company name |
| Contact Name | Single line text | Primary contact at operator |
| Country | Single line text | Country of operator |
| Market | Single select | DACH / UK / US / AUS / Nordic / Other |
| Email | Email | Primary contact email |
| Phone | Phone number | Primary contact phone |
| Website | URL | Operator website |
| Early Partner | Checkbox | Confirmed before 15 July 2026 |
| Commission % | Number | 20% early partner; standard otherwise |
| FAM Applied | Checkbox | Has applied for FAM 2026 |
| FAM Confirmed | Checkbox | Selected and confirmed for FAM |
| FAM Attended | Checkbox | Attended FAM 31 Aug–3 Sep 2026 |
| First Enquiry Date | Date | When first contact made |
| First Booking Date | Date | Date of first confirmed booking |
| Total Bookings | Number | Running total bookings from this operator |
| Total Revenue | Currency (€) | Running total revenue (net) |
| Notes | Long text | Relationship notes, interests, priorities |

---

## Section 4: Automation Setup

Three automations to configure in Airtable (available on free tier with some limits; Pro plan unlocks full automation):

**Trigger 1 — Balance Reminder (60 days before departure)**
- Condition: Balance Due Date = TODAY + 60 days AND Status = "Deposit Paid"
- Action: Send email to Client Email
- Subject: `Balance Due — Arctic Cruises [Departure Date] · Booking Ref [Booking ID]`
- Body: Template E (see Laura Operations Brief)

**Trigger 2 — Guest Information Request (30 days before departure)**
- Condition: Departure Date = TODAY + 30 days AND Status = "Balance Due" OR "Complete"
- Action: Send email to Client Email
- Subject: `30 Days to Go — Guest Information Needed · Booking Ref [Booking ID]`
- Body: Request for guest names, nationalities, dietary requirements, special requests

**Trigger 3 — New Enquiry Alert (manual trigger — within 24 hours)**
- This is not automated — Laura responds manually to each new enquiry within 24 hours
- Use Template A (B2C) or Template B (Trade) from the Operations Brief
- Mark Status as "Contacted" after sending

---

## Section 5: Activation Timeline

| Date | Action |
|------|--------|
| **Now (April 2026)** | Patrick reviews this schema. Laura reviews for usability. |
| **July 2026** | FAM application deadline (15 Jul). Track 50 applications in Airtable Table 4 from this date. |
| **October 2026** | Full Airtable setup: create base, all 4 tables, configure automations, test with FAM data |
| **November 2026** | WTM London — use Airtable to log any operator contacts made at the show |
| **January 2027** | Bookings open. All enquiries and bookings enter Airtable from day one. |
| **Ongoing** | Monthly review of Departure Calendar table: pax count, revenue, capacity remaining |

---

*Document version 1.0 — 2026-04-15*
*Source: PRODUCT-BRIEF.md · PRICING-MASTER.json · SESSION-BRIDGE-S235*
*All pricing confirmed by Patrick, session S231*
