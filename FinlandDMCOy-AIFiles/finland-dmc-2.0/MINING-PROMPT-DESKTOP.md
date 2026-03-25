# Claude Desktop Mining Prompt

Use this prompt when mining in Claude Desktop with M365 connector.
Paste the SESSION START block at the beginning of each mining session.
Paste the SESSION END block when finishing.

---

## SESSION START — Paste This First

```
I'm starting Mining Session [N]: [Topic] for Finland DMC Oy.

CONTEXT:
- Finland DMC is a 5-person destination management company in Finland
- Shared sales mailbox: sales@Finland-dmc.com
- I need to mine our real email data for TWO projects:
  1. EMAIL DRAFTER: Build tone patterns, example emails, best lines for Claude Projects
  2. SECOND BRAIN: Extract client/contact data and interaction history for a CRM system

MINING REPORT — Create this document now and update it after every search:

=== EMAIL DRAFTER SECTIONS ===
- EXAMPLES FOUND: table with columns: date | client | email type | quality (1-5)
- SELECTED EXAMPLES: chosen best emails with FULL TEXT preserved
- EXTRACTED LANGUAGE: best lines, phrases, patterns from real emails
- PATTERNS IDENTIFIED: tone, structure, greeting/closing conventions

=== SECOND BRAIN SECTIONS ===
- CLIENTS DISCOVERED: for each unique company found, log:
  - company_name, country, language, segment (B2B/B2C/tour_operator/corporate)
  - inquiry_types (what they typically ask for)
  - status (active/inactive/one-time)
- CONTACTS DISCOVERED: for each person found, log:
  - name, company, role, email, language, last_contact_date
- INTERACTIONS LOGGED: for each email thread, log:
  - date, client, type (inquiry/follow-up/booking/complaint/feedback)
  - channel (email/teams/phone), outcome, follow_up_needed
- RELATIONSHIP SIGNALS: satisfaction markers, repeat booking indicators,
  churn risk flags, upsell opportunities

=== SHARED SECTIONS ===
- SESSION INFO: date, session number, topic
- SEARCH LOG: every search query + result quality (good/partial/empty)
- STATISTICS: counts, distributions, averages
- GAPS & QUESTIONS: what we couldn't find or need to investigate

RULES:
1. After EVERY search, update the SEARCH LOG immediately
2. When I say "show report" → display current report state
3. When I say "save checkpoint" → output the FULL report for copy/paste
4. Every ~20 minutes, remind me: "Time for a checkpoint save?"
5. Use YAML format for Second Brain data (easy to parse later)
6. Anonymize sensitive data: use [CLIENT-A], [CLIENT-B] etc. for company names in examples,
   but keep REAL names in the Second Brain sections (those are for our internal CRM)

Let's begin. What should we search first for Session [N]?
```

---

## PER-SESSION SEARCH PLANS

### Session 1: Client Communications — OUTBOUND

First searches to try:
1. "Search sales@Finland-dmc.com SENT items from 2024-2025. Find replies to client inquiries about Finland travel. Show 20 results with subject, recipient, date."
2. "From those results, show the 5 best-written client responses. Quote key paragraphs."
3. "Search sent items for emails handling: delays, price objections, bad news. How does Finland DMC deliver difficult messages?"
4. "Search sent items for booking confirmations and logistic emails. Show 5 examples."
5. "Search sent items for cold outreach or returning client emails. Show examples."

### Session 2: Client Communications — INBOUND

First searches to try:
1. "Search sales@Finland-dmc.com INBOX for initial inquiry emails from 2024-2025. Show 30 results with subject, sender, date."
2. "Categorize the inquiries by type: group leisure, corporate/incentive, tour operator, conference, individual, repeat booking, complaint."
3. "Map source markets: which countries/regions do inquiries come from? What languages?"
4. "Find follow-up questions from clients after receiving proposals. What do they ask about most?"
5. "Find positive feedback emails, booking confirmations, satisfaction messages."

### Session 3: DMC Router

First searches to try:
1. "Search sales@ inbox for 30 recent emails from different clients. Show subject, sender, date, and first 2 lines."
2. "For each of those 30 emails, classify: what type is it? Where should it be routed?"
3. "Search Teams messages about work assignment, who handles what, priorities."
4. "Find emails that don't fit standard categories — edge cases."

### Session 4: Proposals & Itineraries

First searches to try:
1. "Search SharePoint/OneDrive for files with 'proposal' or 'itinerary' or 'tarjous' in filename. List 20 most recent."
2. "Open the 5 most recent proposals. Analyze structure: sections, order, length."
3. "Compare 3 similar proposals (same trip type). What's template vs. personalized?"
4. "Search sent emails for proposal follow-ups. Which proposals led to bookings?"

### Session 5: Pricing & Analysis

First searches to try:
1. "Search SharePoint for Excel files about pricing, rates, margins, hinnat."
2. "Open the most recent rate card. Describe structure and pricing model."
3. "Search sales@ for pricing discussions with clients — quotes, negotiations."
4. "Search Teams for internal pricing discussions, margin rules, discount decisions."

---

## SESSION END — Paste This When Done

```
Session complete. Generate FOUR output blocks:

1. EMAIL DRAFTER OUTPUT
   Format as markdown. Include:
   - patterns-identified: all tone/structure/language patterns
   - examples-captured: full text of 5-10 best emails
   - best-lines: extracted phrases sorted by use case (greetings, closings, selling, problem-solving)

2. SECOND BRAIN OUTPUT
   Format as YAML. Include:
   - clients: list of all companies discovered with fields:
     name, country, language, segment, inquiry_types, status, first_seen, last_seen
   - contacts: list of all people discovered with fields:
     name, company, role, email, language, last_contact
   - interactions: list of logged interactions with fields:
     date, client, contact, type, channel, subject, outcome, follow_up
   - signals: relationship health indicators with fields:
     client, signal_type (satisfaction/loyalty/risk/opportunity), evidence, date

3. SESSION REPORT
   - Complete search log with all queries and results
   - Statistics (counts, distributions)
   - Decisions made and why
   - Gaps found

4. NEXT SESSION PREP
   - What gaps need filling in the next session
   - Suggested search queries for next session
   - Clients/contacts to look for more data on

Format everything so I can paste each block directly into a file.
```

---

## QUICK COMMANDS (during session)

| Say This | Claude Does This |
|----------|-----------------|
| "show report" | Display current mining report |
| "save checkpoint" | Output full report for copy/paste |
| "rate this" | Add quality rating to current example |
| "pick this one" | Move to SELECTED EXAMPLES |
| "extract language" | Pull best lines to EXTRACTED LANGUAGE |
| "log client" | Add current email's client to CLIENTS DISCOVERED |
| "log interaction" | Add current email thread to INTERACTIONS LOGGED |
| "what's missing?" | Check gaps, suggest next search |
