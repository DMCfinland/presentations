# Project: Teams Meeting Transcription → Second Brain Pipeline

## Status: NOT STARTED — URGENT
- **Created:** 2026-03-10
- **Owner:** Patrick Heiskanen
- **Scope:** All 1658 Holdings portfolio companies (~50 employees, 10 companies)

---

## The Problem

Every Teams meeting across 10 portfolio companies is lost knowledge. Live captions are ON but captions ≠ transcription. Captions disappear when the call ends. Nothing is stored.

### Evidence (2026-03-10 audit)
- Zero recordings found in OneDrive/SharePoint
- Zero transcripts (.vtt or .docx) anywhere in M365
- Zero Copilot recaps
- Meetings ARE happening (DMC Strategia, Finanssitaito, board meetings — all confirmed in calendar)
- **Every past meeting is unrecoverable**

---

## The Fix: Enable Auto-Transcription

### Teams Admin Center Settings Required

| Setting | Path | Value |
|---------|------|-------|
| Transcription | Meeting policies → Global | **On** |
| Recording | Meeting policies → Global | **On** |
| Auto-recording | Meeting policies → Global | **On** |
| Copilot | Copilot policies | **On with transcription** |

### Pre-requisites
- Identify M365 admin (Patrick? Sebastian? External IT?)
- Confirm Microsoft 365 license tier supports transcription (Business Basic does NOT — needs Business Standard, E3, or E5)
- Confirm Copilot license if Copilot recaps are wanted (separate add-on)

### Output After Fix
- Every meeting auto-records to OneDrive → Recordings/
- Transcript saved as .vtt alongside recording
- Copilot generates meeting recap (summary, action items, follow-ups)
- All searchable from Teams Recap tab

---

## Why This Is Gold: The Second Brain CRM Vision

### The Knowledge Loss Today

Right now, critical business intelligence lives ONLY in people's heads:
- Client preferences discussed in sales calls — forgotten
- Strategic decisions made in board meetings — no searchable record
- Pricing negotiations — remembered differently by each participant
- Partner feedback — lost after the call ends
- Onboarding knowledge shared verbally — never captured

With ~50 employees across 10 companies, this is **hundreds of meetings per month** of lost institutional knowledge.

### The Multiplier: Transcripts + Second Brain CRM

When meeting transcripts flow into a centralized knowledge system (Second Brain / CRM), the impact compounds:

**1. Automatic Client Intelligence**
- Every client call automatically feeds the CRM with preferences, pain points, pricing history
- Sales team doesn't need to manually log notes — the system captures everything
- New team members can read the full history of any client relationship in minutes
- Finland DMC guides discussing tour feedback → automatically tagged to the client profile

**2. Cross-Company Knowledge Sharing**
- A Järvisydän restaurant guest mentions interest in DMC tours → captured, routed
- Arctic Cruises prospect asks about land packages → DMC gets notified
- Holdings-level patterns emerge: "3 companies reported the same supplier issue this month"
- Board meeting decisions automatically visible to relevant operating company managers

**3. Decision Archaeology**
- "Why did we change the pricing model in Q2?" → Search transcripts, get the exact conversation
- "What did the client say about the aurora package?" → Full context, not someone's memory
- Reduces repeated discussions — the answer already exists in the system
- New employees ramp up 3-5x faster with searchable meeting history

**4. AI-Powered Synthesis**
- Feed transcripts to Claude/Copilot → automatic action item extraction
- Weekly digest: "Here's what happened across all 10 companies this week"
- Pattern detection: "Client complaints about X increased 40% this quarter"
- Meeting prep: "Here's everything discussed with Client Y in the last 6 months"

**5. Compliance & Governance**
- Board meeting records automatically archived and searchable
- HR conversations documented (with appropriate privacy controls)
- Financial discussions with Finanssitaito preserved for audit trail
- GDPR note: internal meeting transcripts are legitimate interest, but inform participants

### The Flywheel Effect

```
Meetings happen naturally (no behavior change needed)
    ↓
Auto-transcribed + auto-recorded
    ↓
AI extracts: action items, decisions, client intel, patterns
    ↓
Flows into Second Brain CRM (tagged by company, client, topic)
    ↓
Team searches & discovers knowledge they didn't know existed
    ↓
Better decisions, less repeated work, faster onboarding
    ↓
Compounds over time — 6 months of transcripts = massive knowledge base
```

### Cost vs Value

- **Cost:** Included in M365 Business Standard/E3 (transcription). Copilot add-on ~$30/user/month if wanted.
- **Value:** Even capturing ONE lost client preference per week that leads to a sale pays for the entire system annually.
- **Risk of NOT doing this:** Every day without transcription = permanently lost knowledge. This compounds negatively.

---

## Implementation Phases

### Phase 1: Turn It On (Week 1)
- [ ] Identify M365 admin
- [ ] Verify license tier supports transcription
- [ ] Enable transcription + recording in Teams Admin Center
- [ ] Enable auto-recording policy
- [ ] Test with one meeting
- [ ] Inform team (GDPR: "meetings will be recorded and transcribed")

### Phase 2: Organize (Week 2-3)
- [ ] Set up OneDrive/SharePoint folder structure for recordings
- [ ] Create retention policy (how long to keep recordings vs transcripts)
- [ ] Test transcript download workflow → Claude/AI processing
- [ ] Build first "meeting → insights" pipeline with Claude

### Phase 3: Second Brain Integration (Month 2+)
- [ ] Design CRM/Second Brain schema for meeting intelligence
- [ ] Build automated transcript → CRM pipeline
- [ ] Cross-company tagging system (client names, topics, action items)
- [ ] Weekly AI-generated digest across all companies
- [ ] Team training on searching and using the knowledge base

---

## Related Files
- `CURRENT-STATUS.md` — session tracking
- `_shared/best-practices/` — pattern library
- Finland DMC board meeting agendas found in SharePoint (Hallituksen kokousten pöytäkirjat/)

## Notes
- Past meetings are UNRECOVERABLE — every day of delay = more lost knowledge
- This is a holdings-level project benefiting ALL 10 companies
- Privacy: Finnish law requires informing participants about recording. Add notice to meeting invites.
