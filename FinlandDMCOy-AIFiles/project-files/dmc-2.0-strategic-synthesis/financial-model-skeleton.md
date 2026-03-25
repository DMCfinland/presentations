# Financial Model Skeleton — Finland DMC 2.0 Platform
**Status:** Corrected — math error from Grok draft fixed (€1,875 → €18,742)
**Date:** 2026-02-22
**Pending:** Plug in actual DMC current revenue + dev quotes when available

---

## Tab 1: Assumptions & Scenarios

| Item | Low | Base | High | Source |
|------|-----|------|------|--------|
| Annual guests (Järvisydän pilot Year 1) | 5,000 | 10,000 | 20,000 | Section 1 |
| Monthly guests (÷12) | 417 | 833 | 1,667 | Derived |
| Avg AI-assisted spend per guest | €100 | €150 | €200 | Section 1 |
| Platform commission | 15% | 15% | 15% | Section 1 |
| Infra cost/mo (Zone 1+2 live) | €800 | €922 | €1,045 | Section 3 |
| Claude API variable cost/mo | €500 | €1,200 | €2,200 | Multi-turn RAG estimate |
| Other variable (Adyen/Stripe fees etc.) | €300 | €500 | €800 | Estimate |
| Fixed build cost (BP_08 MVP + BP_11) | €8,000 | €12,000 | €18,000 | Pending quotes |
| Monthly burn during transition (6 mo) | €4,000 | €5,500 | €7,500 | Staff + misc |
| **Break-even guests per tenant (monthly)** | **180** | **116** | **78** | Formula below |

**Break-even formula:** Total monthly costs ÷ (Avg spend × 15%)
- Base: €2,622 ÷ (€150 × 15%) = €2,622 ÷ €22.50 = **116 guests/month**

---

## Tab 2: Monthly P&L (Base Scenario)

| Month | Guests | Commission Revenue | Total Costs | Cumulative Cash | AI % of Total Revenue |
|-------|--------|-------------------|-------------|----------------|----------------------|
| 1–6 (build) | 0 | €0 | €5,500 | -€33,000 | 0% |
| 7 (go-live) | 833 | **€18,742** | €2,622 | -€16,880 | 5% target |
| 8 | 833 | €18,742 | €2,622 | +€2,240 | — |
| 12 | 833 | €18,742 | €2,622 | **+€52,000** | 25% target |
| 12 (20 tenants) | 16,660 | €374,840 | ~€22,000 | +€352,840/mo | — |

**⚠️ Fix applied:** Original Grok draft showed €1,875 for Month 7. Correct calculation:
- 833 guests × €150 avg spend × 15% commission = **€18,742/month**
- That was a 10x error. The corrected figure changes the business case materially.

### Key Formulas
```
Monthly commission  = Guests × Avg spend × 15%
Total monthly costs = Infra + API + Other variable
Break-even guests   = Total monthly costs ÷ (Avg spend × 15%)
Cumulative cash     = previous + (revenue – costs)
```

---

## Tab 3: Sensitivity (add data tables)

| Variable | -50% | Base | +50% | Impact |
|----------|------|------|------|--------|
| API cost | €600 | €1,200 | €1,800 | Break-even 101 → 116 → 129 guests |
| Guest uptake | 417/mo | 833/mo | 1,250/mo | Cash-positive month 10 → 8 → 6 |
| Avg spend per guest | €100 | €150 | €200 | Commission €12,500 → €18,742 → €25,000 |
| Tenant #2 signs at month 9 | | | | Doubles monthly revenue with minimal cost increase |

---

## Next Steps for Model
1. Add Finland DMC current B2B revenue as baseline (existing business)
2. Plug in actual dev quotes for BP_08 MVP + BP_11 build costs
3. Add tenant acquisition scenario (1658 Holdings portfolio = 4+ potential tenants)
4. Add EU AI Act compliance one-time cost (~€3k–8k counsel brief) to months 1–6 burn

---

*Financial model skeleton | Session 49 | 2026-02-22*
