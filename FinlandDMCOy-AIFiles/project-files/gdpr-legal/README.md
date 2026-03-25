# Finland DMC 2.0 — GDPR & Legal Branch

**Owner:** Patrick Heiskanen (acting DPO)
**Counsel:** TBD — Finnish GDPR-qualified legal counsel (to be engaged)
**Target:** DPIA + DPAs complete before Järvisydän B2C go-live

---

## Files in This Branch

| File | Status | Action |
|------|--------|--------|
| [counsel-brief-one-pager.md](../dmc-2.0-strategic-synthesis/counsel-brief-one-pager.md) | Ready to send | Send today — starts 6-8 week clock |
| jarvisydan-dpa-checklist.md | Not started | Draft after counsel engaged |
| anthropic-dpa-verification.md | Not started | Verify DPA + SCCs within 2 weeks |
| article-30-processing-record.md | Not started | Draft with counsel |
| dpia-draft.md | Not started | Counsel-led, weeks 1-8 |

---

## Scope of Legal Work

### 1. GDPR DPIA (Article 35) — MANDATORY before Zone 2 go-live
- **B2B trigger:** Second Brain RelationshipHealthScore = automated profiling of named contacts (Art 35(3)(a))
- **B2C trigger:** Finland Travel Assistant / Järvisydän Travel Assistant = systematic guest monitoring in resort (Art 35(3)(c))
- Lead time: 6-8 weeks
- Budget: €3,000-8,000

### 2. EU AI Act (Regulation (EU) 2024/1689) — Art 50 obligations from August 2026
- System classification: limited-risk chatbot
- Required: "You are talking to AI" disclosure, generated-content disclosure
- Confirm no high-risk elements (Mood Matrix profiling review)

### 3. Data Processing Agreements (DPAs, Article 28)
- **Anthropic DPA:** verify it satisfies Art 28 + Article 46 SCCs for US transfers
- **Järvisydän DPA:** Finland DMC as processor, Järvisydän as data controller for guest data
- **Supabase DPA + Hetzner DPA:** before first data load to Zone 1
- **Travel agency DPAs:** before B2B Partner Dashboard shares pseudonymized guest data

### 4. Article 30 Record of Processing Activities
- Document the Anthropic transfer mechanism decision (Option A: verify DPA + SCCs, or Option B: skip Claude Teams for PII)
- Document all 9 processing activities across Zone 1 + Zone 2

### 5. Liability
- Define liability chain for AI-generated advice (stale Safety Bulletin, accessibility recommendations)
- Allocate between Finland DMC (platform), Järvisydän (resort operator), and guest

---

## Critical Rules (from GDPR Section of Goal Document)

- Named B2B contact PII (names, emails, phones) MUST NOT enter Claude Teams until Anthropic DPA + Art 46 SCCs verified
- Supabase on Hetzner Frankfurt = only permissible production storage for named B2B contact PII
- No guest PII may cross Zone 1 / Zone 2 boundary in identifiable form
- Mood Matrix "Needs_Accessibility" tag MUST NOT be stored at launch (Art 9 health-adjacent data)
- DPIA mandatory before go-live with guest personal data

---

## Sequencing Logic

```
Week 1:     Send counsel brief → engage counsel
Week 1-2:   Verify Anthropic DPA + SCCs (can proceed with company-level non-PII in interim)
Week 1-8:   Zone 1 build (Email Drafter, Second Brain State A) — no DPIA needed for internal B2B tools
Week 2:     Execute Supabase DPA + Hetzner DPA (before first data load)
Week 2-8:   Counsel-led DPIA (runs parallel to Zone 1 build)
Week 4:     Draft Järvisydän DPA + guest privacy notice
Week 8:     DPIA completed, filed — Zone 2 build can proceed
Week 12-16: Zone 2 go-live (BP_08 + BP_11 complete + DPIA filed + all DPAs signed)
```

---

*Created: 2026-02-22 | Session 50*
