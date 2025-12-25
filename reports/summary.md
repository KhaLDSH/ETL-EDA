# Week 2 Summary — ETL + EDA

## Key findings
- **AE Leads Revenue:** The **UAE (AE)** market is the primary revenue driver, generating approximately **$325k** in total revenue, followed by Kuwait at $310k.
- **Monthly Volatility:** Revenue peaked in **January 2025 at ~$107k**. Sales remained relatively stable between $85k–$95k from July through November before a sharp year-end decline.

- **Market Spending Parity:** Statistical testing (Bootstrap) confirms **no significant difference** in average spend between Saudi Arabia and the UAE (95% CI: -0.017 to 0.059), meaning growth in AE is driven by volume, not higher price points.


## Definitions
- **Revenue** = `sum(amount)` over the specific dimension (Country or Month).
- **Refund rate** = `refunds / total orders`, where refund is defined by `status_clean == "refund"`.
- **Time window** = January 2025 – December 2025.

## Data quality caveats
- **Missingness:** The precipitous drop in December suggests the dataset is **incomplete** for the final reporting period rather than a genuine business failure.
- **Duplicates:** Standard deduplication was applied; no significant issues with double-counted order IDs.
- **Join coverage:** High coverage across GCC countries; revenue is well-distributed among the four primary country codes (AE, KW, QA, SA).
- **Outliers:** Extreme values were handled via **Winsorization at $500**, resulting in a uniform distribution that prevents high-value outliers from skewing the mean.


## Next questions
- **Customer Acquisition:** Since average order value (AOV) is identical in SA and AE, what specific campaigns are driving the higher transaction volume in the UAE?
- **December Validation:** Can we pull the remaining December logs to confirm if the revenue drop is a data-sync lag or a seasonal trend?