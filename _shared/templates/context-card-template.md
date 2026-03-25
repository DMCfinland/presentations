---
company: [Company Name]
warm_pack_id: [strategic-research|crm-build|seo-geo|m365-mining]
last_updated: YYYY-MM-DD
---

# [Company Name] — Context Card

Load this at session START before any external source mining.
It overrides generic assumptions from external articles, tutorials, and community posts.

---

## Tech Stack (overrides source defaults)

| External default | [Company] reality |
|-----------------|-------------------|
| Slack | [e.g. Microsoft Teams (M365)] |
| Google Workspace | [e.g. Microsoft 365] |
| Zapier | [e.g. n8n (self-hosted)] |
| Firebase | [e.g. Supabase] |
| Stripe | [e.g. custom invoicing] |
| Any email provider | [e.g. Microsoft Outlook / Exchange] |
| OpenAI GPT | Claude (Sonnet 4.6 default) |

**Flag any recommendation that contradicts this card before applying it.**

---

## Staff (roles relevant for system + adoption context)

| Name | Role | AI adoption profile |
|------|------|---------------------|
| [Name] | [Role] | [Profile note] |

---

## Standing Overrides (common source conflicts)

- **"[Generic term]"** = [Company-specific meaning]
- **"[Generic term]"** = [Company-specific meaning]

---

## Locked Decisions (do not relitigate without a D-number)

- D[N]: [Decision summary]

Full decisions: `project-files/[project]/DECISIONS.md`

---

## GDPR + Legal Context

- Jurisdiction: [Finnish law + EU GDPR / other]
- Data residency: [Supabase Frankfurt (EU) / other]
- Key requirement: [DPIA status / other]

---

## Project Context (active [date])

- **Active project:** [Project name + current phase]
- **Status:** [One-line status]
- **Next gate:** [What needs to happen before the next step]
- **Key file:** `[path/to/HANDOFF-NEXT-WINDOW.md or equivalent]`
