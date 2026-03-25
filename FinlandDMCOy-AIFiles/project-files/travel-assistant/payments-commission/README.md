# Payments & Commission — Personal Travel Assistant
**Branch under:** Personal Travel Assistant (Zone 2, B2C)
**Status:** Design phase — discuss before building
**Key principle:** Finland DMC never touches guest payment data

---

## Core Model: Affiliate + Referral (No Payment Processing)

Guests pay partners directly. Finland DMC tracks commissions via Shadow Ledger.
Finland DMC earns 15% commission (already established at Järvisydän).

```
Guest clicks AI recommendation
→ Opens partner webshop (new tab / in-app browser inside PWA)
→ Guest pays partner directly (Adyen, Nets, or partner's own system)
→ Referral code / UTM tracked by Shadow Ledger
→ Partner reports confirmed sale (webhook or monthly statement)
→ Shadow Ledger marks AFFILIATE → SETTLED
→ Finland DMC invoices or nets commission per agreement
```

---

## Three Flow Types (Already Built in BP_07 Shadow Ledger)

| Flow | How it works | GDPR | Commission tracking |
|------|-------------|------|-------------------|
| **AFFILIATE** | AI recommends → guest clicks referral link → pays partner | No payment data to DMC | UTM params + partner webhook |
| **MANUAL** | AI recommends → staff contacts partner → staff confirms booking | No payment data to DMC | Staff input to Shadow Ledger |
| **API** | AI books directly via partner API | No payment data to DMC | API confirmation → Shadow Ledger |

Phase 1: AFFILIATE + MANUAL only.
Phase 3: API flow (requires Opera/BookVisit API access).

---

## Referral Tracking Toolset (By Partner Capability)

Not all partners have the same technical capability. Tiered approach:

| Tier | Partner capability | Tracking method | Reconciliation |
|------|-------------------|----------------|----------------|
| **Tier 1** | Has webhook API | `?ref=dmc_{partner_id}&session={uuid}` UTM + partner webhook fires on confirmed booking | Automatic (Shadow Ledger) |
| **Tier 2** | Has webshop, no webhook | UTM params + partner provides monthly report | Semi-manual (Shadow Ledger import) |
| **Tier 3** | No webshop, no API | AI recommends → staff calls/emails partner → staff logs in Shadow Ledger | Manual (MANUAL flow) |

Finland DMC supports all tiers. Enforcement: stop routing guests to non-paying partners.

---

## Järvisydän (Phase 1) — Special Case

- Already 15% commission on all webshop purchases (existing commercial relationship)
- Shadow Ledger already has `provider_jarvisydan` with 12% partner default (needs updating to 15%)
- Webshop uses Adyen — Finland DMC does NOT need separate Adyen account for Phase 1
- Referral tracking: UTM params + monthly reconciliation with Järvisydän finance team
- Phase 2 target: Järvisydän fires webhook on booking confirmation → automatic Shadow Ledger update

---

## WhatsApp Channel

- Guest cannot complete payment within WhatsApp (no embedded payment flow)
- AI sends recommendation via WhatsApp → includes link to partner webshop → guest pays there
- Shadow Ledger tracks the click-through (if UTM params are preserved in the link)
- Same AFFILIATE flow as PWA

---

## Payment Architecture Decisions (Patrick to decide)

### Decision 1: Adyen account structure
- **Option A:** Single Adyen account (Järvisydän's) — no new onboarding, limited to Järvisydän pilot
- **Option B:** Finland DMC gets own Adyen merchant account — enables marketplace model at scale, required for multi-tenant
- **Recommendation: Option A for Phase 1, Option B before second tenant**

### Decision 2: Commission invoicing model
- **Option A:** Monthly invoice — Finland DMC invoices each partner for confirmed referrals
- **Option B:** Net-down — partner pays net of commission (partner keeps 85%, sends 15% separately)
- **Option C:** Escrow via Adyen Marketplace — Adyen splits payment automatically at checkout
- **Recommendation: Option A for Phase 1 (simple), Option C long-term**

### Decision 3: Dispute handling
- What happens if partner disputes a booking claim?
- Shadow Ledger audit trail is the evidence (booking_ref + UTM + timestamp)
- Need contractual "stop routing" enforcement clause with all partners

---

## Shadow Ledger Integration (BP_07 — Already Built)

The mock implementation at `Desktop/FinnConcierge/services/finance/shadow_ledger.py` already supports:
- ✅ Three flow types (API, MANUAL, AFFILIATE)
- ✅ Waterfall commission logic (product-specific → seasonal → partner default)
- ✅ ACID transaction integrity (mock, needs Azure SQL migration)
- ✅ Audit trail (no deletions, only VOID)
- ✅ Decimal precision (financial-safe calculations)

**Fix needed before production:** `provider_jarvisydan` rule shows 12% — should be 15% to match existing agreement.

---

## GDPR Note

Finland DMC does not process guest payment data in any flow.
- AFFILIATE: guest pays partner, we get UTM confirmation
- MANUAL: staff confirms with partner, we log booking reference only
- API: partner API returns booking confirmation, we log reference only

No PCI-DSS compliance needed for Finland DMC (we never handle card data).
Partners are responsible for their own PCI-DSS compliance.

---

## Next Steps for This Branch

- [ ] Confirm 15% commission rate with Järvisydän (update Shadow Ledger default)
- [ ] Define UTM parameter scheme (`?ref=dmc&partner=jarvisydan&session={uuid}&product={product_id}`)
- [ ] Agree on monthly reconciliation process with Järvisydän finance (Phase 1)
- [ ] Draft partner onboarding agreement template (commission terms + UTM tracking requirement + "stop routing" clause)
- [ ] Plan Adyen Finland DMC merchant account application (before second tenant)
- [ ] Design booking_source_metadata table integration (Shadow Ledger → Zone 1 Supabase batch)

---

*Created: 2026-02-23 | Session 50*
