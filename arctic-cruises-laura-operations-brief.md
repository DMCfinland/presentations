# Arctic Cruises — Laura's Operations Brief
## Complete Day-to-Day Operating Guide
### Version 1.0 · 2026-04-15

**For:** Laura Ilvonen — Arctic Cruises & Finland DMC
**Contact for changes:** Patrick Heiskanen

---

## Part 1: The Website

### What the Website Does

The B2C website presents Arctic Cruises to the public. It contains product descriptions, pricing, the route, the team, and an enquiry form.

**B2C URL:**
`https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html`

**How the enquiry form works:**
The form is a mailto form — when a visitor submits it, it opens their email client pre-filled and sends directly to `laura@finlanddmc.fi`. There is no backend database. Every enquiry arrives in Laura's inbox.

### What the Website Does Not Do

- It does not take payments
- It does not confirm bookings automatically
- It does not send autoresponders (Laura sends the response manually using the templates below)

### When to Request Website Updates

Email Patrick (`patrick@finlanddmc.fi`) to request changes for:

| Trigger | What to change |
|---------|---------------|
| Pricing changes | Update all three product prices |
| New season dates | Update 2028 season dates once confirmed |
| After FAM (September 2026) | Add 2–3 operator testimonials |
| New partnerships | Add resort partner logos or certifications |
| Any factual correction | Names, dates, capacity |

**Who makes changes:** Patrick and Claude Code handle all website changes. Laura does not need to edit the site directly.

---

## Part 2: Responding to Enquiries — Email Templates

### How to Use These Templates

- **B2C enquiry (individual traveller)** → Use Template A
- **Trade/operator enquiry** → Use Template B
- **FAM application received** → Use Template C
- **Booking confirmed, deposit required** → Use Template D
- **Balance reminder, 60 days before** → Use Template E

Always respond within **24 hours** of receiving an enquiry. If you are away, set an out-of-office.

---

### TEMPLATE A — B2C Enquiry Response

*Send within 24 hours of receiving an individual traveller enquiry.*

---

**Subject:** Your Arctic Cruises Enquiry — Lake Saimaa 2027

Dear [Name],

Thank you for your enquiry about the [Grand Cruise / Short Cruise / Day Cruise] on Lake Saimaa.

I am delighted to confirm that [preferred date] is currently available.

Attached: Full voyage details and pricing.

[If 7-night Grand Cruise:] The Grand Cruise (7 nights) is priced at €2,600 per person, full board. For a couple, that is €5,200 total — all accommodation at authentic Saimaa resorts, every meal included, smoke sauna, gala dinner, and our full expert team on board.

Bookings open formally January 2027. I can add you to our priority list now, which guarantees you first access to your preferred date when booking opens.

Would that be helpful?

With kind regards,
Laura Ilvonen
Arctic Cruises & Finland DMC
laura@finlanddmc.fi

---

**Notes for Laura:**
- Replace [Grand Cruise / Short Cruise / Day Cruise] with the product the person asked about
- Replace [preferred date] with the date they mentioned, or write "your preferred week"
- For 3-night Short Cruise: price is €1,200 per person. For Day Cruise: €400 per person.
- Include the B2C flyer PDF as the attachment ("Full voyage details and pricing")

---

### TEMPLATE B — Trade/Operator Enquiry Response

*Send when a travel agent, tour operator, or trade buyer makes contact.*

---

**Subject:** Arctic Cruises 2027 — Net Rate Sheet & Operator Information

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

---

**Notes for Laura:**
- Attach: Operator PRD PDF + Net Rate Sheet PDF
- Net rates: Day €320 · 3-night €960 · 7-night €2,080 (20% commission vs list price)
- Log the operator in Airtable Table 4 immediately after sending
- Add to FAM list if they express any interest

---

### TEMPLATE C — FAM Application Confirmation

*Send to every operator who applies for the FAM voyage.*

---

**Subject:** FAM Voyage 2026 — Application Received

Dear [Name],

Thank you for applying to the Arctic Cruises FAM voyage (31 Aug – 3 Sep 2026).

We are reviewing all applications and will confirm selected partners by 1 June 2026.

We aim to select 50 operators from across DACH, UK, US, Australia, and the Nordic region.

In the meantime, please feel free to visit our website for full product information:
https://dmcfinland.github.io/presentations/arctic-cruises-b2c.html

With kind regards,
Laura Ilvonen
Arctic Cruises & Finland DMC
laura@finlanddmc.fi

---

**Notes for Laura:**
- Send this within 24 hours of receiving every FAM application
- Mark "FAM Applied = Yes" in the operator's Airtable record immediately
- You do not need to pre-approve — this is acknowledgement only
- Confirmations go out by 1 June 2026

---

### TEMPLATE D — Booking Confirmation + Deposit Invoice

*Send when a booking is ready to be confirmed and a deposit invoice is attached.*

---

**Subject:** Booking Confirmed — [Product] · [Date] · Booking Ref [AC-XXXX]

Dear [Name],

Your [Grand Cruise / Short Cruise] on [date] is confirmed.

Booking Reference: AC-[XXXX]
Party: [N] guests
Departure: [Date], 09:00, Lappeenranta Harbour
Return: [Date], ~12:00, Lappeenranta Harbour
Total: €[X] (per attached invoice)

DEPOSIT DUE: €[30% amount] — please pay within 14 days.
BALANCE DUE: €[70% amount] — due by [60 days before departure date].

[Payment details: bank name, IBAN, BIC, reference: Booking Ref]

I will contact you 30 days before departure for:
- Guest names and nationalities
- Dietary requirements and allergies
- Special requests

If you have any questions before then, I am here.

With kind regards,
Laura Ilvonen
Arctic Cruises & Finland DMC
laura@finlanddmc.fi

---

**Notes for Laura:**
- Assign a Booking ID before sending (AC-0001, AC-0002, etc.)
- Deposit = 30% of total price. Example: 7-night for 2 guests = €5,200 total → deposit €1,560
- Balance = remaining 70%. Due 60 days before departure.
- Attach the invoice as a PDF
- Update Airtable Table 2 Status to "Confirmed" after sending

---

### TEMPLATE E — Balance Reminder (60 Days Before Departure)

*Send automatically via Airtable automation, or manually 60 days before each departure.*

---

**Subject:** Balance Due — Arctic Cruises [Date] · Booking Ref [AC-XXXX]

Dear [Name],

Your Arctic Cruises voyage on [date] is now 60 days away.

BALANCE DUE: €[amount] · Due by [date].

[Payment details: bank name, IBAN, BIC, reference: Booking Ref]

Also: I will contact you again in 30 days to collect guest names, dietary requirements, and special requests.

Excited to welcome you on board!

With kind regards,
Laura Ilvonen
Arctic Cruises & Finland DMC
laura@finlanddmc.fi

---

**Notes for Laura:**
- Airtable will trigger this automatically once set up (October 2026)
- Until then, check the Departure Calendar each Monday and send manually for any bookings with balance due within 60 days
- Update Airtable Status to "Balance Due" after sending

---

## Part 3: FAM Workflow 2026 — Key Dates Timeline

The FAM voyage is the most important commercial event of 2026. Every operator who attends and signs a commercial agreement is a sales channel for 2027.

### Timeline

| Date | Action |
|------|--------|
| **Now → 15 July 2026** | Receive FAM applications by email. Send Template C to every applicant within 24h. Log all applicants in Airtable Table 4. |
| **15 July 2026** | FAM application deadline. Early partner commission deadline (20% rate). Close both simultaneously. |
| **1 June 2026** | Send confirmation to 50 selected operators. This is earlier than the deadline — confirm as soon as you have 50 strong applications, do not wait until July. |
| **August 2026** | Send programme brief and logistics pack to all 50 confirmed FAM guests. Include: itinerary by day, meeting point (Lappeenranta Harbour), what to bring, accommodation details. |
| **30 August 2026** | Final reminder to all 50 guests: meeting point, departure time (09:00), what to bring, weather forecast, emergency contacts. |
| **31 Aug – 3 Sep 2026** | FAM voyage. Laura is on board as host. Collect business cards. Note who expresses strong interest in commercial partnership — these are your Day 7 priority list. |
| **4 September 2026** | Within 24 hours of disembarkation: send media pack + commercial agreement form to all 50 operators. |
| **7 September 2026** | Send commercial agreement to operators who expressed interest on board. Follow up by phone if possible. |
| **14 September 2026** | First follow-up call with top 10 priority operators. Goal: move from "interested" to "agreement signed." |
| **30 September 2026** | Review: how many commercial agreements signed? Target: 15 or more. |
| **15 October 2026** | Activate website testimonials from FAM guests (request photo + 2-sentence quote from each guest by email). |

---

## Part 4: Trade Shows and Cold Outreach

### Priority Events

**WTM London — November 2026**
- Attend as visitor (no booth required in year 1)
- Bring 50 copies of the B2B flyer
- Target: DACH, UK, and US operators with Scandinavia/nature programmes
- Collect business cards → log in Airtable Table 4 → send Template B within 48 hours of returning

**ITB Berlin — March 2027**
- Book a booth if budget allows (ask Patrick by October 2026 for budget decision)
- Attend as visitor in 2026 if not exhibiting
- Target: German-speaking market — primary revenue target for Year 1

**Nordic Visit Organisations**
- Visit Finland, Visit Lappeenranta, Visit Saimaa — maintain active relationships
- These organisations refer international operators to Finnish products
- Send updated product information at the start of each season

### Cold Outreach Sequence

Use this 3-step sequence for any operator you identify but who has not yet contacted you:

**Step 1 — Initial Email**
Send B2B flyer as attachment + a personal note of maximum 3 sentences. Keep it short.

Example note:
> "Dear [Name], I am reaching out about Arctic Cruises — Finland's first dedicated lake cruise product on Lake Saimaa, launching 2027. I am attaching our operator brief and would love to discuss whether this fits your programme. Our 2026 FAM voyage (31 Aug – 3 Sep, complimentary) may be the easiest way to experience it first-hand."

**Step 2 — Follow-Up (Day 7)**
If no reply after 7 days:

> "Dear [Name], I wanted to follow up on my note about Lake Saimaa. Did it reach you? Happy to send a shorter summary if easier."

**Step 3 — FAM Invitation (if interest shown)**
If they reply with any interest, immediately send Template B and offer a call.

### Target Operator Profile

Focus outreach on operators who already sell:
- Scandinavia (Norway fjords, Sweden, Iceland)
- Nature-based luxury (safari, wilderness lodges)
- River or lake cruising in Europe
- Mature traveller segments (50–68 age group)

---

## Part 5: After FAM — 30-Day Action Plan

The 30 days after FAM are the highest-leverage commercial period of the year. Operators are still enthusiastic. Momentum must be converted to signed agreements before it fades.

| Day | Action | Target |
|-----|--------|--------|
| **Day 1–3** | Send media pack to all 50 operators | 50/50 delivered |
| **Day 7** | Send commercial agreement to operators who expressed interest on board | Top 20 priority operators |
| **Day 14** | First follow-up call with top 10 priority operators | 10 calls completed |
| **Day 21** | Second call or email to operators who did not sign at Day 7 | Continue pipeline |
| **Day 30** | Review: commercial agreements signed | Target: 15+ signed |
| **Day 45** | Activate website testimonials | 3–5 quotes live on site |

### What is in the Media Pack (send Day 1–3)

The media pack goes to all 50 FAM guests and contains:
- High-resolution photos from the voyage (Patrick will arrange photographer on board)
- Fact sheet: product summary, pricing, booking contact
- Commercial agreement form (PDF — fillable or print/sign/scan)
- Laura's direct contact for any questions

### After Day 30

Once 15+ agreements are signed, update Patrick with a summary:
- Number of agreements signed
- Geographic breakdown (DACH / UK / US / AUS / Nordic)
- Estimated first-year booking volume from agreements
- Any operators who said "not yet" but showed strong interest (keep warm for 2028 FAM)

---

*Document version 1.0 — 2026-04-15*
*Source: PRODUCT-BRIEF.md · PRICING-MASTER.json · SESSION-BRIDGE-S235*
*For questions or updates: patrick@finlanddmc.fi*
