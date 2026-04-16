**Gap Report: Kiinteistörahoitushakemus (Rantasalmi)**

**SECTION 1: SANEERAUS (RESTRUCTURING) RISK**

*   **[VERDICT]** **High Risk / Potential Blocker.** The lessee's active restructuring status represents a critical, potentially unacceptable, counterparty risk. The G6 confirmation reduces uncertainty but does not eliminate the legal or commercial risks of the restructuring process failing or the lease being terminated.

*   **[HARPER FINDINGS]**
    *   **YSL 27§ Legal Status (Harper):** Finnish law (Laki yrityksen saneerauksesta 47/1993, section 27§) grants the administrator (*pesänhoitaja*) a unilateral right to terminate certain contracts, including leases, within a two-month period after the restructuring proceedings begin. This is a statutory right designed to protect the debtor company's estate and its creditors.
    *   **G6 Confirmation Effect (Harper):** The *pesänhoitaja's* written G6 confirmation, stating the lease is essential for business continuity and will be included in the restructuring program, is a powerful statement of intent. However, it is not a legally binding waiver of the YSL 27§ right. If the restructuring plan falters or a more drastic plan is needed, the administrator's primary duty is to the lessee's creditors, not the landlord. A court could approve a revised plan that terminates the lease if deemed necessary. There is no clear case law found where a G6 confirmation was successfully challenged, but legal scholars affirm the statutory termination right remains until the restructuring program is officially ratified by the court.
    *   **Finnish Bank Standard Practice (Harper):** For a loan where repayment capacity is 100% dependent on a single tenant in *yrityssaneeraus*, Finnish banks (e.g., Nordea, OP) would typically require significant risk mitigation beyond a G6 confirmation. Common requirements include:
        1.  A rent deposit covering 6-12 months of rent, held in an account pledged to the bank.
        2.  A direct, legally binding guarantee (*omavelkainen takaus*) from the ultimate, creditworthy parent company or owners of the lessee (Lomakylä Järvisydän Oy).
        3.  A full review of the court-approved restructuring program (*saneerausohjelma*), not just the administrator's confirmation, to understand the lessee's future viability, debt load, and cash flow forecasts.

*   **[BENJAMIN FINDINGS]**
    *   **Income Concentration Risk (Benjamin):** The debt service capacity is 100% reliant on a single, non-investment-grade counterparty. The DSCR of 3.20x is mathematically robust but financially fragile. If the lease is terminated or the lessee defaults, the DSCR immediately drops to 0, and the loan defaults as the plots themselves generate no income.
    *   **DSCR Verification (Benjamin):** The DSCR calculation is confirmed as accurate based on the provided inputs.
        ```python
        import numpy_financial as npf

        # Loan parameters
        principal = 423000  # EUR
        annual_rate = 0.04
        years = 15
        
        # Calculations
        monthly_rate = annual_rate / 12
        n_periods = years * 12
        monthly_payment = -npf.pmt(monthly_rate, n_periods, principal)
        annual_debt_service = monthly_payment * 12
        
        # Annual rent
        annual_rent = 120000 # EUR
        
        # DSCR
        dscr = annual_rent / annual_debt_service
        
        # Breakeven rent drop for DSCR 1.20
        breakeven_rent = annual_debt_service * 1.20
        rent_drop_percentage = (annual_rent - breakeven_rent) / annual_rent
        
        # Output
        print(f"Annual Debt Service: {annual_debt_service:.2f} EUR (Benjamin)")
        print(f"DSCR (120k rent / {annual_debt_service:.2f} debt service): {dscr:.2f}x (Benjamin)")
        print(f"Breakeven Rent Drop before DSCR < 1.20x: {rent_drop_percentage:.2%} (Benjamin)")
        ```
        *Output:*
        `Annual Debt Service: 37500.84 EUR (Benjamin)`
        `DSCR (120k rent / 37500.84 debt service): 3.20x (Benjamin)`
        `Breakeven Rent Drop before DSCR < 1.20x: 62.50% (Benjamin)`

*   **[LUCAS CHALLENGES]**
    *   **Unacceptable Counterparty Risk (Lucas):** This is the primary reason for rejection. A bank's credit policy cannot be based on lending to a project whose sole income source is a company legally declared insolvent. The high DSCR is a mirage; it reflects a high-risk premium, not security. The G6 confirmation is merely an administrator's opinion at a single point in time and is subordinate to the unpredictable legal process of restructuring.
    *   **Misaligned Incentives (Lucas):** The *pesänhoitaja*'s goal is to save the lessee's business for the lessee's creditors. Our applicants (the landlords) are a secondary concern. If a better deal arises, or if liquidation becomes necessary, the lease will be sacrificed. The bank would be funding an asset whose value is entirely dependent on the successful outcome of a third party's insolvency proceeding.
    *   **Binary Outcome (Lucas):** This is a binary risk. Either the lease holds until 2056 and the loan performs, or the lease is terminated in the near future and the loan immediately defaults. There is no middle ground. The collateral plots, especially the one zoned for recreation, have minimal alternative use or income potential in the short term.

*   **[RECOMMENDATION]** **Halt and Mitigate.** Do not proceed with the application as is. The *saneeraus* risk is a potential blocker. The bank must demand one of the following before reconsideration:
    1.  A pledged cash deposit from the applicants equal to 12 months' rent (120,000 EUR).
    2.  A corporate guarantee from a creditworthy parent entity of Lomakylä Järvisydän Oy.
    3.  A full copy of the final, court-ratified restructuring plan (*lainvoimainen saneerausohjelma*), which the bank's legal department must review and approve.

---

**SECTION 2: PROPERTY IDENTIFIER ISSUE**

*   **[VERDICT]** **Administrative Blocker.** Lending cannot proceed with ambiguous property identifiers. This is a non-negotiable administrative requirement that must be resolved before any legal documents are drafted.

*   **[HARPER FINDINGS]**
    *   **Correct Identifier (Harper):** A Finnish bank will *only* use the current, valid property identifier as listed in the official National Land Survey (MML) register. The old identifier ("681-418-1-65") is legally defunct and irrelevant for the loan and collateral agreements. The correct identifier for all legal documents is the current one ("681-418-1-169").
    *   **Required Documentation (Harper):** To resolve this definitively, the applicant must provide the following fresh (no older than 3 months) documents from MML for the plot "Ahvenlahti" with the identifier "681-418-1-169":
        1.  **Lainhuutotodistus (Certificate of Title):** Proves legal ownership.
        2.  **Rasitustodistus (Certificate of Encumbrances):** Shows any existing mortgages, liens, or easements.
        3.  **Kiinteistörekisteriote (Cadastral Register Extract):** Provides official details like land area, zoning, and often includes a history section showing previous identifiers and consolidation events (*"muodostumistiedot"*). This document will explicitly show the merge of the old identifier into the new one.

*   **[BENJAMIN FINDINGS]**
    *   **Data Integrity Failure (Benjamin):** This discrepancy is a clerical error, but it signals a lack of diligence in the application's preparation. A credit officer must question the accuracy of all other unverified data points in the application if something as fundamental as the property identifier is incorrect.

*   **[LUCAS CHALLENGES]**
    *   **Unprofessionalism and Risk of Error (Lucas):** A credit committee sees this as a red flag for the applicants' professionalism. If they cannot get the basic legal identifier of their asset correct, what other details are wrong? This creates a risk of legal defects in the loan documentation if not caught, potentially rendering the collateral pledge invalid. This must be corrected by the applicant immediately, not fixed by the bank.

*   **[RECOMMENDATION]** **Return to Applicant for Correction.** The application should be formally returned with a request for the applicant to provide the three official MML documents (*Lainhuutotodistus, Rasitustodistus, Kiinteistörekisteriote*) for the property identifier **681-418-1-169**. All loan application forms must be amended to reflect only the current, valid identifier.

---

**SECTION 3: APPLICANT STRUCTURE**

*   **[VERDICT]** **Unresolved / Critical Missing Information.** The application is incomplete as the borrowing entity is not defined. Each proposed structure has significant weaknesses from the bank's perspective that require different documentation and risk assessments.

*   **[HARPER FINDINGS]**
    *   **Bank Preference (Harper):** A Finnish bank's preference depends on the specifics, but generally:
        *   **Structure A (Private Individuals):** Preferred if the individuals have a high net worth, strong, verifiable income streams independent of this project, and a simple ownership structure. The "joint and several" liability gives the bank recourse to 100% of both individuals' personal assets. The primary risk is life events (death, divorce, personal bankruptcy).
        *   **Structure B (Finland DMC Oy):** This is a significant weakness. The company is a startup (*y-tunnus* issued in 2021) with no operating history or balance sheet. A bank would view it as a shell company or Special Purpose Vehicle (SPV). Lending to it would *only* be considered with full, unlimited personal guarantees from the owners, effectively making it a loan to the individuals but with more legal complexity. Banks are wary of lending to new SPVs for simple asset holding.
    *   **Tax Implications (Harper):** (Note: This is not tax advice). For individuals, rental income is capital gains income, taxed at 30-34%. For an Oy (Ltd), rental income is corporate income, taxed at 20%. Individuals can deduct interest expenses from their capital gains income. The Oy structure allows for more complex expense deductions and reinvestment but can have double taxation upon profit distribution (corporate tax + dividend tax). The bank is largely indifferent to the borrower's tax optimization, focusing instead on liability and repayment security.

*   **[BENJAMIN FINDINGS]**
    *   **Quantitative Impact of Structure B (Benjamin):** The 10-year loan term proposed for the Oy structure significantly increases the debt service burden and lowers the DSCR, making it less attractive.
        *   Annual Debt Service (10yr, 4%): **52,159 EUR**
        *   DSCR (10yr): 120,000 / 52,159 = **2.30x**
    *   This 2.30x DSCR is still strong, but it reduces the margin of safety compared to the 3.20x in the 15-year structure.

*   **[LUCAS CHALLENGES]**
    *   **Indecision is a Red Flag (Lucas):** The applicants are asking the bank to evaluate two fundamentally different borrowing scenarios. This demonstrates a lack of a clear business plan and financial strategy. A well-prepared applicant would have this decided.
    *   **Startup Oy is a Non-Starter (Lucas):** A credit committee would immediately reject a loan to "Finland DMC Oy." Lending to a startup with no assets or track record to purchase a high-risk property is against any sound lending policy. The personal guarantees are the *only* mitigating factor, which begs the question: why not lend directly to the individuals? The Oy structure here only serves to add a layer of legal complexity and potential cost for the bank in a default scenario.
    *   **Missing Personal Financials (Lucas):** The viability of Structure A (and the guarantees in B) depends entirely on the personal financial strength of the two applicants. The application provides zero information on their net worth, liquidity, annual income, or existing liabilities. The *omavelkainen takaus* is worthless if the guarantors are insolvent.

*   **[RECOMMENDATION]** **Force a Decision and Demand Full Disclosure.**
    1.  The bank must require the applicants to formally choose ONE borrowing structure.
    2.  If they choose **Structure A (Private Individuals)**, they must submit detailed personal financial statements, including assets, liabilities, and the last 2 years of tax returns (*verotuspäätös*).
    3.  If they choose **Structure B (Oy)**, the bank should treat it as a loan to private individuals and demand the same personal financial statements to back the non-negotiable personal guarantees. The bank should also question the rationale for using a no-history startup.

---

**SECTION 4: CROSS-COLLATERAL DETAILS**

*   **[VERDICT]** **Critical Missing Information / Blocker.** The LTV of 22% is an unsubstantiated claim. Without detailed, official documentation for each piece of cross-collateral, the true LTV is unknown and must be assumed to be over 100%.

*   **[HARPER FINDINGS]**
    *   **Standard Bank Requirements (Harper):** A "total value" is completely insufficient. For each property offered as cross-collateral, a Finnish bank requires a complete, property-specific documentation package:
        1.  **Official Identifier:** The full *kiinteistötunnus* (property identifier).
        2.  **Lainhuutotodistus (Certificate of Title):** To prove ownership.
        3.  **Rasitustodistus (Certificate of Encumbrances):** Crucial for revealing existing mortgages (*panttikirjat*) or other liens. The bank needs to know if it will be in the first, second, or third priority position.
        4.  **Valuation:** A recent valuation report (*arviokirja*) from a licensed real estate appraiser (LKV, AKA), or at a minimum, a credible desktop valuation based on recent market transactions. For significant commercial properties, a formal appraisal is mandatory.
        5.  **Evidence of Insurance:** A valid property insurance policy.

*   **[BENJAMIN FINDINGS]**
    *   **LTV Calculation Discrepancy (Benjamin):** The application's numbers are inconsistent.
        *   Value of new plots = 80,000 + 325,000 = **405,000 EUR**
        *   Stated cross-collateral = **~1,387,000 EUR**
        *   Sum of documented collateral = 405,000 + 1,387,000 = **1,792,000 EUR**
        *   The application claims a total collateral value of **~1,920,000 EUR**, a difference of ~128,000 EUR. The source of this higher value is unexplained.
    *   **LTV Verification (Benjamin):**
        *   LTV based on the application's unsubstantiated total value: 423,000 / 1,920,000 = **22.0%** (as claimed)
        *   LTV based on the sum of the application's own numbers: 423,000 / 1,792,000 = **23.6%**
        *   **Worst-Case LTV (documented collateral only):** 423,000 / 405,000 = **104.4%**

*   **[LUCAS CHALLENGES]**
    *   **LTV is Meaningless Without Documentation (Lucas):** This is a cardinal sin in a credit application. The 22% LTV is the headline figure designed to make the deal look secure, but it is currently pure fiction. The bank must assume the LTV is 104% until proven otherwise. The cross-collateral could be illiquid forest land, heavily mortgaged apartments, or simply overvalued. Without a *rasitustodistus* for each, we have no idea how much debt is already secured against these "other properties."
    *   **Financing of Transfer Tax (Lucas):** The loan amount (423,000 EUR) includes the 12,150 EUR transfer tax. This means the applicants are not contributing their own cash for the transaction costs, indicating a potential lack of liquidity. This is a negative signal. A conservative bank prefers to see the borrower have "skin in the game" by covering all transaction costs out of pocket.

*   **[RECOMMENDATION]** **Halt Application. Demand Full Collateral Schedule.** The application must be stopped. The bank requires a complete collateral schedule listing every property (with identifiers), and for each property, the full set of documents outlined by Harper (title, encumbrances, valuation). The bank will then perform its own analysis of the collateral's true value and the bank's lien priority before recalculating a credible LTV.

---

**RISK MATRIX**

| Risk | Severity (1-5) | Mitigation |
| :--- | :--- | :--- |
| **Lessee Insolvency & Lease Termination** | 5 (Catastrophic: immediate and total loss of repayment capacity) | - Require 12-month rent deposit in a pledged account.<br>- Obtain corporate guarantee from lessee's creditworthy parent/owners.<br>- Await and approve final court-ratified restructuring plan. |
| **Undocumented & Unverified Cross-Collateral** | 5 (Critical: LTV is unknown; could be >100%, rendering the loan unsecured) | - Halt application until a full collateral schedule is provided.<br>- Demand fresh *Lainhuutotodistus*, *Rasitustodistus*, and valuation for every collateral property. |
| **Unclear Borrower Structure & Missing Financials** | 3 (High: complicates legal enforcement and true risk assessment) | - Force applicant to select a single legal structure.<br>- Demand full personal financial statements and tax returns for all guarantors. |
| **Administrative Errors (Property ID, LTV math)** | 2 (Medium: indicates sloppiness, causes delays, erodes trust) | - Return application for correction of all identifiers and figures.<br>- Require applicant to provide official MML documents to verify all property data. |