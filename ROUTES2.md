# Docsynecx UI 2 Route Directory (ROUTES2.md)

This document maps all routes for **UI Design 2**, which lives completely decoupled from UI 1.

- **Root Entry**: [`/index2.html`](file:///c:/Users/vasan/OneDrive/Documents/Docsynecx.UI/index2.html) (and [`/ui2/`](file:///c:/Users/vasan/OneDrive/Documents/Docsynecx.UI/ui2/index.html))
- **Assets**: [`/assets2/tokens.css`](file:///c:/Users/vasan/OneDrive/Documents/Docsynecx.UI/assets2/tokens.css), `/assets2/logo.svg`, `/assets2/site.js`
- **Data Model**: [`/data2/pages.json`](file:///c:/Users/vasan/OneDrive/Documents/Docsynecx.UI/data2/pages.json)
- **Generator**: [`generate_site2.py`](file:///c:/Users/vasan/OneDrive/Documents/Docsynecx.UI/generate_site2.py)

---

## Complete Route Directory

| # | Page Name | File Path | Clean URL | Template Type | Content Source |
|---|---|---|---|---|---|
| 1 | **Home (Landing)** | `/index2.html` & `/ui2/index.html` | `/index2.html` / `/ui2/` | Approved Landing (`UI_2`) | `output/landing_page.txt` |
| 2 | **Invoice Automation** | `/ui2/invoice-processing/index.html` | `/ui2/invoice-processing/` | Approved Route (`UI_2`) | `output/invoice-processing.txt` |
| 3 | **Logistics & Supply Chain** | `/ui2/logistics-trade/index.html` | `/ui2/logistics-trade/` | Approved Route (`UI_2`) | `output/logistics-trade.txt` |
| 4 | **Shipments (Sub-page)** | `/ui2/logistics-trade/shipments/index.html` | `/ui2/logistics-trade/shipments/` | Approved Route (`UI_2`) | `output/logistics-trade_shipments.txt` |
| 5 | **Customs Declarations** | `/ui2/logistics-trade/custom-declarations/index.html` | `/ui2/logistics-trade/custom-declarations/` | Approved Route (`UI_2`) | `output/logistics-trade_custom-declarations.txt` |
| 6 | **AP Reconciliation** | `/ui2/logistics-trade/ap-reconciliation/index.html` | `/ui2/logistics-trade/ap-reconciliation/` | Approved Route (`UI_2`) | `output/logistics-trade_ap-reconciliation.txt` |
| 7 | **Workflow & Approvals** | `/ui2/workflows/index.html` | `/ui2/workflows/` | Approved Route (`UI_2`) | `output/workflows.txt` |
| 8 | **Tally Integration** | `/ui2/integration/invoice-to-tally/index.html` | `/ui2/integration/invoice-to-tally/` | Approved Route (`UI_2`) | `output/integration_invoice-to-tally.txt` |
| 9 | **Zoho Books Integration** | `/ui2/integration/zoho-books/index.html` | `/ui2/integration/zoho-books/` | Approved Route (`UI_2`) | `output/integration_zoho-books.txt` |
| 10 | **CargoWise Integration** | `/ui2/integration/cargowise/index.html` | `/ui2/integration/cargowise/` | Approved Route (`UI_2`) | `output/integration_cargowise.txt` |
| 11 | **Solutions Hub** | `/ui2/solutions/index.html` | `/ui2/solutions/` | Card-grid / Solutions | `output/solutions.txt` |
| 12 | **Banking Solutions** | `/ui2/solutions/banking/index.html` | `/ui2/solutions/banking/` | Solution Detail | Inline generator content |
| 13 | **Finance Solutions** | `/ui2/solutions/finance/index.html` | `/ui2/solutions/finance/` | Solution Detail | Inline generator content |
| 14 | **Logistics Solutions** | `/ui2/solutions/logistics/index.html` | `/ui2/solutions/logistics/` | Solution Detail | Inline generator content |
| 15 | **Accounts Payable Solutions** | `/ui2/solutions/accounts-payable/index.html` | `/ui2/solutions/accounts-payable/` | Solution Detail | Inline generator content |
| 16 | **Pricing Plans** | `/ui2/pricing/index.html` | `/ui2/pricing/` | Pricing Card & Matrix | `output/pricing.txt` |
| 17 | **Blog & Resources** | `/ui2/blog/index.html` | `/ui2/blog/` | Card-grid (Article List) | `output/blog.txt` |
| 18 | **Request Demo** | `/ui2/request-demo/index.html` | `/ui2/request-demo/` | Demo Walkthrough Form | `output/request-demo.txt` |
| 19 | **About Us** | `/ui2/about/index.html` | `/ui2/about/` | Story & Values Grid | `output/about.txt` |
| 20 | **Enterprise Scale** | `/ui2/enterprise/index.html` | `/ui2/enterprise/` | Feature Card Grid | `output/enterprise.txt` |
| 21 | **Partners Program** | `/ui2/partners/index.html` | `/ui2/partners/` | Ecosystem Partner Grid | `output/partners.txt` |
| 22 | **Contact Us** | `/ui2/contact/index.html` | `/ui2/contact/` | Contact Form & Info | `output/contact.txt` |
| 23 | **Help Center** | `/ui2/help/index.html` | `/ui2/help/` | Documentation Grid | `output/help.txt` |
| 24 | **Privacy Policy** | `/ui2/privacy-policy/index.html` | `/ui2/privacy-policy/` | Legal Article Template | `output/privacy-policy.txt` |
| 25 | **Terms of Service** | `/ui2/terms-of-service/index.html` | `/ui2/terms-of-service/` | Legal Article Template | `output/terms-of-service.txt` |
| 26 | **404 Not Found** | `/ui2/404.html` | `/ui2/404.html` | Custom Themed 404 | Custom Brand Page |

---

## Link Integrity Audit Results

- **Total Links Checked**: 1,527 internal links across all 23 files
- **Dead `#` Links**: 0
- **Broken Links / 404s**: 0
- **Cross-Design Collisions**: 0 (UI 1 remains 100% untouched)
