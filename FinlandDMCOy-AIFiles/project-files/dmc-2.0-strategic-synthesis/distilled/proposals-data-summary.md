# Proposals Data Summary — SECOND-BRAIN Distillation
<!-- DISTILL-B output | Source: proposals-2024/SECOND-BRAIN/ | Generated: 2026-02-22 -->
<!-- Used by: Agent 1 (Second Brain Analyzer) in Wave 1 -->

---

## File Inventory

| Filename | Format | Size / Records | Contents |
|---|---|---|---|
| `client-profiles.yaml` | YAML | 107 client records (~2,000 lines) | Per-company CRM profiles sorted by revenue_confirmed descending; includes win rates, revenue, margin, staff ownership, tier, alerts |
| `staff-account-map.yaml` | YAML | 4 staff cards + account health map + Janna transition note (~350 lines) | Staff portfolio metrics, account health ratings, orphaned account list, transition priority order |
| `revenue-intelligence.yaml` | YAML | 4 sections (~520 lines): concentration, market, pricing, pipeline | Revenue concentration card, 13-country market analysis, destination/market pricing benchmarks, 6-proposal pipeline assessment |
| `second-brain-gap-report.md` | Markdown | ~500 lines, 3 main sections | Cross-reference of proposals data vs email-mined contacts: enrichment available, new clients to add, email-only contacts, name disambiguation |

**Data provenance:** All files share the same source — 393 proposals (2022–2024 RFQ dates) from `proposals-clean-extract.md`. Session 38, generated 2026-02-21. 174 confirmed deals. 107 unique companies.

---

## Data Schema (field-level)

### client-profiles.yaml — per client record

```
company:             # Display name (may differ from canonical)
canonical_name:      # Deduplicated name (resolves variants like "Arca Tour" / "Arca Tours")
country:             # English country name
channel:             # Direct | GSA | Direct/GSA
segment:             # FIT | Group | Series | Incentive | MICE
typical_pax_range:   # 1-5 | 6-20 | 21-50 | 50-100 | 100+
preferred_destination: # JS | Kuru | Lapland | Helsinki | Mixed
proposals_total:     # Integer count
wins:                # Integer count
win_rate:            # Percentage string (or null for On Process records)
revenue_confirmed:   # Integer euros (0 for non-wins)
margin_avg:          # Percentage integer (null for non-wins; one anomalous 90% value)
staff_owner:         # Staff initials: LV | JK | RV | JK/RV | LV/JK | RV/LV | etc.
relationship_tier:   # Tier1-flagship | Tier2-reliable | Tier3-occasional | Tier4-one-off
alert:               # CRITICAL | HIGH | WATCH | null
notes:               # Free text — 1-3 sentences, actionable
```

### staff-account-map.yaml — staff_portfolio per record

```
staff:               # Initials
full_name:           # Full name
role:                # Job title string
status:              # Present only for departed staff (JK): "DEPARTED"
proposals_owned:     # Integer
win_rate:            # Percentage string
revenue_generated:   # Euro string
avg_deal_size:       # Euro integer
margin_avg:          # Percentage integer
top_clients:         # List of strings (company + revenue + win data)
portfolio_health:    # strong | adequate | thin
flags:               # List of free-text observations
```

### staff-account-map.yaml — account_health per record

```
company:             # Company name or market aggregate
country:             # Country or "Italy/Czech market (aggregate)"
staff:               # Owner initials
proposals:           # Integer
won:                 # Integer
win_rate:            # Percentage string
revenue:             # Euro string
health_status:       # healthy | at-risk | problem
reason:              # Multi-line YAML block scalar
action_needed:       # yes | no
action:              # Multi-line YAML block scalar
```

### revenue-intelligence.yaml — market_intelligence per record

```
country:             # English
country_fi:          # Finnish (source language in original data)
proposals:           # Integer
won:                 # Integer
win_rate:            # Percentage string
revenue_confirmed:   # Euro string
avg_deal_size:       # Euro string
margin_pattern:      # "high >=15%" | "medium 10-14%" | "low <10%"
market_verdict:      # grow | maintain | investigate | avoid
verdict_reason:      # Multi-line block scalar
```

### revenue-intelligence.yaml — pricing_benchmarks.by_destination per record

```
destination:         # JS | Kuru | Lapland (Winter) | Helsinki
full_name:           # Full location description
win_rate:            # Percentage
proposals_total:     # Integer
typical_nights:      # Range string
margin_pattern:      # Category string
price_pax_segments:  # Nested: fit_small_group / standard_group / premium_group / etc.
  typical_range:     # Euro range string
  examples:          # Comma-separated deal examples with actual figures
  note:              # Optional
blended_avg_price_pax: # Single value with ~ prefix
pricing_note:        # Multi-line block scalar
```

### second-brain-gap-report.md — enrichment_available per record

```
company:             # Company name
country:             # Country
second_brain_has:    # List of contacts and relationship notes from email mining
proposals_adds:      # List of financial/commercial data not yet in Second Brain
priority:            # high | medium | low
notes:               # Free text synthesis
```

---

## Key Data Patterns

### Revenue — Top Clients

| Rank | Company | Country | Revenue | Share | Win Rate | Margin | Tier |
|---|---|---|---|---|---|---|---|
| 1 | AHI Travel | USA | €4,381,000 | 75.0% | 80% (4/5) | 13% | Flagship |
| 2 | Flash Pack | UK | €558,480 | 9.5% | 67% (2/3) | **5% (anomalous)** | Flagship |
| 3 | Wikinger Reisen | Germany | €316,600 | 5.4% | 100% (4/4) | 11% | Flagship |
| 4 | Delta Tour | Poland | €75,000 | 1.3% | 100% (1/1) | 17% | Reliable |
| 5 | Supernet Tours | USA | €58,000 | 1.0% | 100% (2/2) | 13% | Reliable |

- **Top 5 combined:** €5,389,080 = 91.8% of all confirmed revenue
- **All other 102 clients combined:** €482,064 = 8.2%
- **Total confirmed:** €5,871,144 across 174 wins from 393 proposals (44% overall win rate)
- **Average confirmed deal:** €35,368 (heavily distorted by AHI; median would be much lower)

### Revenue by Volume vs Value — Key Tension

- **Highest proposal volume:** Kontiki/Kontiki Reisen (52 proposals, 45 confirmed, 87% win rate, €40,199 total) — tiny individual deals averaging ~€893 each
- **Highest single-deal value:** AHI Travel (~€1.1M average per confirmed deal)
- **Highest margin individual deal:** Savor Travels (20%), McGeehee Cruise (20%), Fora Travel single win (21%), Finnature (22%), O-Nord (90% — data error flagged in notes)

### Staff Assignment Patterns

| Staff | Proposals Owned | Win Rate | Revenue Generated | Avg Deal Size | Margin |
|---|---|---|---|---|---|
| LV (Liisa Vihermaa) | 197 | 57% | €1,177,734 | €10,423 | 9% |
| JK (Janna Kankkunen — departed Aug 2024) | 130 | 33% | €2,334,949 | €54,300 | 13% |
| RV (Reeta Vihavainen) | 60 | 27% | €158,461 | €9,904 | 15% |
| RV/LV joint | 2 | 100% | €2,200,000 (AHI share) | €1,100,000 | 13% |

- LV carries 50% of all proposals by volume (197/393)
- JK generated €2.33M revenue despite 33% win rate — large-deal focus, not poor performance
- RV has the highest margin (15%) with the lowest proposal volume (60) — pricing discipline model
- Multi-owner notation (LV/JK, RV/LV, etc.) is common — 15+ clients show shared initials

### Account Concentration Risk Signals

- **CRITICAL:** AHI Travel = 75% of revenue; any disengagement = existential threat; 2-hour response SLA
- **HIGH (orphan risk):** Flash Pack = €558K, sole owner was JK (departed Aug 2024); no formal handover confirmed; 5% margin requires renegotiation
- **HIGH (orphan risk):** Delta Tour = €75K, 17% margin, JK sole owner, contact unknown since departure
- **MEDIUM:** Journey D.LUXE = JK sole owner, €11K revenue, requires new owner assignment
- **SYSTEMIC PROBLEM:** Italy market = 35 proposals, 2 wins, 6% win rate, €35,652 revenue — worst-performing market; flagged to pause outreach
- **SYSTEMIC PROBLEM:** Czech Republic = 13 proposals, 1 win, 8% win rate, €9,255 revenue

### Active Pipeline

- 6 On Process proposals identified:
  - Walks Worldwide (UK, JS)
  - My Own Travel (Germany, Kuru)
  - TeaHuntress (USA, Kuru, 12 pax)
  - Stranalandia (Italy, Pyhä, €7,544 entered)
  - Evolution Travel (Italy, Muu)
  - Voyage Prive (France, JS/Kuru)
- Pipeline assessed as "critical" — dangerously thin at 6 active proposals
- Realistic conversion value: €50,000–€100,000

---

## Data Completeness Assessment

### Well-Captured Fields (high fill rate across 107 records)

- `company`, `canonical_name`, `country` — 107/107, consistent
- `channel` — 107/107 (Direct | GSA | Direct/GSA)
- `segment` — 107/107 (FIT | Group | Series | Incentive | MICE)
- `proposals_total`, `wins`, `win_rate` — 107/107; win_rate = null only for "On Process" status
- `revenue_confirmed` — 107/107 (0 for non-wins, not null)
- `staff_owner` — 107/107 (multi-owner notation consistent; departed JK flagged)
- `relationship_tier` — 107/107 (Tier1 through Tier4)
- `notes` — 107/107 (always present, actionable, 1-3 sentences)

### Sparse or Unreliable Fields

- `margin_avg` — present for wins but **null for all 0-revenue records**; also one obvious data error (O-Nord: 90% margin where revenue=€608 and cost=€547)
- `typical_pax_range` — categorical ranges only (1-5, 6-20, etc.), not actual pax counts from proposals; precision lost in aggregation
- `preferred_destination` — derived from pattern, not from explicit field in source; "Mixed" used when >1 destination
- `alert` — sparse (CRITICAL=1, HIGH=2, WATCH=4, null=100); most risks are in notes not alerts

### Absent Entirely (Expected CRM Data Not Present)

- **No contact names or emails** — zero contact data in client-profiles.yaml; contact data lives only in second-brain-gap-report.md from email mining sessions
- **No last-contact date** — no `last_contact`, `last_activity_date`, or recency field; only qualitative "2024" strings in gap report
- **No proposal dates** — individual RFQ dates not in profiles; only data range stated in file header (2022–2024)
- **No cancellation reasons** — why 219 proposals were lost is not captured; only outcomes (Confirmed/Canceled)
- **No contract terms** — no payment terms, contract start/end dates, exclusivity, SLA commitments
- **No next-action or follow-up dates** — CRM workflow fields (next call, renewal date, proposal due) absent
- **No supplier information** — which local suppliers (hotels, guides, transport) serve which client not stored
- **No communication history** — email thread summaries, sentiment, relationship tone not in profiles (partially in gap report from email mining)
- **No client-side contact hierarchy** — who is decision-maker vs ops contact not captured in profiles

---

## Quality Assessment

### Data Consistency

- **Mostly consistent** across 107 records; YAML structure is uniform
- **Revenue figures are integers** (no cents), consistent throughout
- **Staff initials** are consistent (LV, JK, RV) with occasional multi-owner (LV/JK, RV/LV, JK/RV)
- **One confirmed data error:** O-Nord margin_avg=90% (margin field shows €547 cost vs €608 revenue — likely a data entry mistake in source Excel)
- **One inconsistency:** Delta of Scandinavia noted as appearing in both "Tanska" (Denmark) and "Italia" country columns in source — flagged in notes as data issue in row 77
- **Segment inconsistency:** "FIT" vs "Group" vs "Series" is applied at the company level, not the deal level — one company can have proposals across multiple segments

### Data Reliability

- **Revenue figures are confirmed deals only** — not pipeline estimates, not proposals; explicitly labeled `revenue_confirmed`
- **Win rate calculations match** proposal counts in spot-checks (Kontiki 45/52 = 87%, AHI 4/5 = 80%)
- **Margin figures are averages** across confirmed deals, not individual deal margins; variation within a client is hidden
- **AHI Travel revenue (€4,381,000)** is stated as "confirmed" but represents a series contract — may reflect contracted value rather than fully invoiced and collected revenue

### Recency

- **Source data range:** 2022–2024 RFQ dates; travel dates extend to 2026
- **Critical recency gap:** JK departed August 2024; 6+ months of post-departure account activity not reflected
- **Pipeline section** captures only 6 "On Process" proposals — no 2025 pipeline data is present; file header notes this as a gap
- **Gap report** includes email-mined contacts from 2026 bookings (Emile Weber Oct 2026, Tour Partner Group 2026) — more current than proposals data

---

## "What Second Brain Actually Is" — Plain Language

Based on the actual data in these four files, Second Brain as it exists today is primarily a **proposals-derived intelligence layer** — a structured extraction from an Excel proposals tracking sheet, not a living CRM. It contains strong commercial performance data (win rates, revenue, margin by client and market) and reasonable market-level patterns, but almost no relational contact data: there are no email addresses, no named contacts, no last-contact dates, and no communication history in the client profiles themselves. The contact layer exists separately in email mining outputs (Sessions 1-3), and the gap report is the only place where proposals data and contact data are cross-referenced. Second Brain as designed was meant to be a complete client intelligence system; what exists today is the financial/commercial skeleton without the relationship tissue. The pipeline section reveals the system's forward-looking limitations — only 6 active proposals are tracked, the data ends at 2024, and the most time-sensitive risk (JK departure, orphaned accounts) is documented but not yet remediated in the account ownership fields.

---

## Critical Gaps for Agent 1

1. **Contact data is absent from client profiles.** `client-profiles.yaml` contains zero email addresses or named contacts for any of the 107 companies. The Second Brain spec presumably calls for contact enrichment — but what exists today requires a separate email mining layer (Sessions 1-3) to supply any contact data at all. The spec and the reality are structurally separated.

2. **JK departure created an unresolved ownership gap across ~130 proposals.** Flash Pack (€558K), Delta Tour (€75K), Journey D.LUXE (€11K) are flagged as orphaned but `staff_owner` in client-profiles.yaml still shows "JK" — the data has not been updated to reflect post-departure reassignments. Any Second Brain system surfacing `staff_owner` as a routing field will route to a departed employee.

3. **Italy and Czech Republic patterns indicate the Second Brain currently stores information about markets that should be paused, not grown.** 48 proposals to Italy and Czech Republic combined produced 3 wins and €44,907 revenue. If Second Brain is used to prioritize outreach, these markets are over-represented relative to their actual value.

4. **No temporal data in client profiles.** Without last-contact date or proposal dates, Second Brain cannot distinguish a client that converted in 2022 and has been silent since from one that converted last month. The gap report provides some recency signals through email mining, but client-profiles.yaml itself is temporally flat — all records look equally current.

5. **The gap report identifies 14 companies with active email relationships that have no client-profiles.yaml entry** (Wikinger Reisen, Kontiki, Delta Tour, Detours, etc. — all flagged as "new clients to add"). These are confirmed revenue clients, not prospects. Second Brain is missing entries for its 3rd through 5th highest-revenue clients (Wikinger, Delta Tour, Supernet Tours), meaning the system cannot route queries about them to any profile.
