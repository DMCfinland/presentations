# Grok Deep Research: CRM Landscape Beyond Pipedrive

**Instructions:** Paste into Grok 4.20 (Deep Research mode). This completes our CRM research before making a build/buy/hybrid decision.

---

## Context

I run Finland DMC Oy, a 5-person B2B destination management company (incoming tourism to Finland). 107 clients, €3.2M revenue. We already researched Pipedrive deeply — now I need to know what ELSE is out there. I'm building a custom AI-powered CRM (Claude AI + Supabase + n8n) and need to know if any existing tool does what we need better than building from scratch.

**Our 5 non-negotiable requirements:**
1. Minimal manual data entry (staff hates it — this killed previous CRM attempts)
2. B2B travel/DMC workflow (seasonal pricing, itineraries, suppliers, commissions, pax)
3. Visual pipeline/Kanban (this is what excites our sales team)
4. M365 integration (shared mailbox, Teams, SharePoint)
5. AI-powered intelligence (client profiling, proposal drafting, relationship health)

## Research Questions

### Part 1: Travel/DMC-Specific CRM Tools (deep dive)

1. **Lemax:** Full feature breakdown for a 5-person DMC. Does it handle: itinerary building, supplier management, commission tracking, pax/group management, seasonal pricing, proposal generation, client CRM, pipeline view? What does the sales workflow look like? Pricing for 5 users? API capabilities? Can it replace BOTH our CRM and our itinerary software (TravelTree)?

2. **Tourwriter:** Same questions as Lemax. Specifically: how is their CRM module vs their itinerary module? Is it a real CRM or just contact management bolted onto tour operations? Pipeline view? Email integration?

3. **TourPlan:** Same questions. This is enterprise-grade — is it overkill for 5 people? Pricing? Minimum company size?

4. **Moonstride:** Newer travel CRM — what does it offer? Is it a viable option for a small European DMC?

5. **Travel/DMC CRM landscape summary:** Are there ANY tools that combine real CRM (pipeline, activities, email sync) with real tour operations (itinerary, suppliers, commissions, pax)? Or is the travel industry still stuck choosing between "generic CRM + manual ops" or "tour ops tool + no real CRM"?

### Part 2: AI-First / Modern CRM Tools (2025-2026)

6. **Attio:** "The CRM that builds itself." How does auto-enrichment work? Does it really minimize data entry? Pipeline view? AI features? M365 integration? Pricing for 5 users? How would it handle a DMC workflow?

7. **Folk CRM:** "CRM for people who hate CRMs." How does it auto-populate contacts from email? Pipeline management? Automation? Pricing? M365 support? Travel/DMC fit?

8. **Clay:** AI-powered data enrichment platform. Could it serve as a CRM layer? Or is it only enrichment? How would it integrate with our custom system?

9. **HubSpot Free/Starter:** The elephant in the room. How does HubSpot's free tier compare to Pipedrive Professional for a 5-person team? What's actually free vs what costs money? Pipeline, email, AI features, M365 integration, reporting?

10. **Twenty (open-source CRM):** Self-hosted, open-source alternative to Salesforce/HubSpot. Could we self-host this on our existing Hetzner infrastructure alongside Supabase? API extensibility? How hard to customize for DMC needs?

### Part 3: Lightweight / No-Code Pipeline Tools

11. **Monday Sales CRM:** How does it compare to Pipedrive for visual pipeline? Automation capabilities? M365 integration? Better or worse for data entry burden?

12. **Airtable as CRM:** Can Airtable's interface layer (Kanban views, forms, automations) serve as a lightweight CRM? API for integration with our AI system? Pricing?

13. **Notion as CRM:** Some teams use Notion databases as CRM. Viable for 107 clients? Pipeline view? Automation? How does it compare to purpose-built CRM?

### Part 4: The Feature Matrix

14. **Comparison matrix** for all tools above. Columns:
    - Tool name
    - Monthly cost (5 users)
    - Visual pipeline (Kanban)
    - Email sync (M365 shared mailbox)
    - AI features (drafting, enrichment, scoring)
    - Travel/DMC features (itinerary, suppliers, commissions, pax)
    - Data entry burden (1-10, where 1 = most manual, 10 = zero entry)
    - API quality (for custom integration)
    - Mobile app quality
    - Self-hostable (yes/no)
    - Time to value (days to productive)

15. **Best-in-class features to steal:** From ALL tools reviewed, what are the top 10 individual features that we should build into our custom system? Not which tool to buy — which IDEAS are worth copying regardless of tool.

## Output Format

Clear headers per question. Honest assessment — no marketing language. For each tool, state clearly: "would work for DMC" or "not suitable because [reason]."

End with **"If You're Building Custom, Steal These Ideas"** — the 10 best features from across all tools that a custom AI-powered DMC CRM should include.
