"""
Execution runner that generates every route page using real extracted content.
"""

from build_all_pages import build_landing_page, build_route_page, save_page
from generator_base import render_head, render_navbar, render_footer, SHARED_SCRIPT

def main():
    print("Starting site generation...")
    
    # 1. Landing Page
    build_landing_page()

    # =========================================================================
    # 2. PRODUCT ROUTES (Invoice Processing, Logistics & Trade, Workflows)
    # =========================================================================

    # A. Invoice Processing
    build_route_page({
        "rel_path": "invoice-processing/index.html",
        "canonical": "/invoice-processing",
        "title": "AI Invoice Processing & Automation Software | Docsynecx",
        "description": "Extract, validate, and process hundreds of invoices in minutes. Eliminate manual entry and auto-sync with Tally, Zoho Books, and SAP.",
        "eyebrow": "Accounts Payable Automation",
        "h1": "Automate Invoice Processing with AI",
        "lead": "Extract, validate, and process hundreds of invoices in minutes, not hours. Eliminate manual entry and accelerate your finance operations.",
        "mock_title": "Vendor Invoice Extraction",
        "mock_fields": [
            ("Vendor Name", "Synecx Partner Supplier"),
            ("GSTIN", "29ABCDE1234F1Z5 ✓"),
            ("Invoice Date", "12 Oct 2026"),
            ("Line Items", "7 items verified"),
            ("Total Amount", "₹4,82,300.00")
        ],
        "challenges": [
            "Manual invoice entry slows every payment cycle",
            "Duplicate invoices and GST calculation errors drain margin",
            "Invoices rarely match purchase orders first time",
            "Finance teams spend time chasing exceptions, not strategic decisions"
        ],
        "steps": [
            {
                "title": "We Automatically Collect Your Invoices",
                "desc": "Upload PDFs, scanned files, or let Docsynecx ingest documents straight from email inboxes, shared folders, and ERP connectors.",
                "card_title": "Collecting Documents...",
                "badge": "Received ✓",
                "fields": [("inv-8821.pdf", "Received"), ("vendor-bill.png", "Received"), ("po-4410.xlsx", "Matched")]
            },
            {
                "title": "We Instantly Extract Key Line Items",
                "desc": "Advanced AI captures GSTIN, invoice dates, vendor headers, and individual line items with 99%+ accuracy in any layout.",
                "card_title": "Vendor Invoice Parsing",
                "badge": "Data Extracted ✓",
                "fields": [("Vendor", "Synecx Supplier"), ("GSTIN", "29ABCDE1234F1Z5"), ("Total", "₹4,82,300.00")]
            },
            {
                "title": "We Validate GST and Match Purchase Orders",
                "desc": "Ensure accurate GST rates and mathematical totals. Detect duplicate submissions and run rule-based 2-way and 3-way matching against POs.",
                "card_title": "Validation & Rule Check",
                "badge": "Checks Passed ✓",
                "fields": [("GST Check", "Valid (Active)"), ("Duplicate Check", "Unique Voucher"), ("PO Match", "Tolerance < 1%")]
            },
            {
                "title": "We Auto-Sync Clean Data to Your ERP",
                "desc": "Verified purchase vouchers flow automatically into TallyPrime, Zoho Books, SAP, or your existing accounting stack with audit logs.",
                "card_title": "Synced with Accounting Stack",
                "badge": "Posted ✓",
                "fields": [("Voucher Type", "Purchase"), ("Ledger", "Trade Creditors"), ("Status", "Posted Automatically")]
            }
        ],
        "stats": [
            ("99.0%", "Extraction accuracy"),
            ("80%", "Faster processing"),
            ("60–70%", "Cost reduction"),
            ("24/7", "Automated batch processing")
        ],
        "features_eyebrow": "Everything You Need",
        "features_title": "Built for Indian Finance & Accounts Payable Teams",
        "features_lead": "Robust capabilities for compliance, speed, and ledger integrity.",
        "features": [
            ("GST Data Extraction", "Automatically captures GSTIN, taxable amount, CGST, SGST, IGST, and HSN/SAC breakdowns."),
            ("Line-Item Capture", "Extracts multi-line tables with item descriptions, unit rates, quantities, and discounts."),
            ("Duplicate Detection", "Identifies duplicate bill numbers across historical vendor postings to protect margins."),
            ("2- & 3-Way Matching", "Reconciles invoices against Purchase Orders and Goods Receipt Notes (GRN) automatically."),
            ("Exception Review Queue", "Reviewers see only flagged fields right next to the source document for swift approvals."),
            ("Audit-Ready Logs", "Maintains complete processing history, reviewer actions, and compliance audit trails.")
        ]
    })

    # Also build compatibility route for /products/invoice-automation
    build_route_page({
        "rel_path": "products/invoice-automation/index.html",
        "canonical": "/products/invoice-automation",
        "title": "AI Invoice Processing & Automation Software | Docsynecx",
        "description": "Extract, validate, and process hundreds of invoices in minutes. Eliminate manual entry and auto-sync with Tally, Zoho Books, and SAP.",
        "eyebrow": "Accounts Payable Automation",
        "h1": "Automate Invoice Processing with AI",
        "lead": "Extract, validate, and process hundreds of invoices in minutes, not hours. Eliminate manual entry and accelerate your finance operations.",
        "mock_title": "Vendor Invoice Extraction",
        "mock_fields": [
            ("Vendor Name", "Synecx Partner Supplier"),
            ("GSTIN", "29ABCDE1234F1Z5 ✓"),
            ("Invoice Date", "12 Oct 2026"),
            ("Line Items", "7 items verified"),
            ("Total Amount", "₹4,82,300.00")
        ],
        "challenges": [
            "Manual invoice entry slows every payment cycle",
            "Duplicate invoices and GST calculation errors drain margin",
            "Invoices rarely match purchase orders first time"
        ],
        "steps": [
            {
                "title": "We Automatically Collect Your Invoices",
                "desc": "Upload PDFs, scanned files, or let Docsynecx ingest documents straight from email inboxes, shared folders, and ERP connectors.",
                "card_title": "Collecting Documents...",
                "badge": "Received ✓",
                "fields": [("inv-8821.pdf", "Received"), ("vendor-bill.png", "Received")]
            },
            {
                "title": "We Instantly Extract Key Line Items",
                "desc": "Advanced AI captures GSTIN, invoice dates, vendor headers, and individual line items with 99%+ accuracy.",
                "card_title": "Vendor Invoice Parsing",
                "badge": "Data Extracted ✓",
                "fields": [("Vendor", "Synecx Supplier"), ("Total", "₹4,82,300.00")]
            },
            {
                "title": "We Validate GST and Match Purchase Orders",
                "desc": "Ensure accurate GST rates and totals. Detect duplicates and run rule-based 2-way and 3-way matching.",
                "card_title": "Validation & Rule Check",
                "badge": "Checks Passed ✓",
                "fields": [("GST Check", "Valid"), ("PO Match", "Matched")]
            },
            {
                "title": "We Auto-Sync Clean Data to Your ERP",
                "desc": "Verified purchase vouchers flow automatically into TallyPrime, Zoho Books, or SAP.",
                "card_title": "Synced with Accounting Stack",
                "badge": "Posted ✓",
                "fields": [("Voucher Type", "Purchase"), ("Status", "Posted")]
            }
        ],
        "stats": [
            ("99.0%", "Extraction accuracy"),
            ("80%", "Faster processing"),
            ("60–70%", "Cost reduction"),
            ("24/7", "Automated batch processing")
        ],
        "features": [
            ("GST Data Extraction", "Captures GSTIN, taxable amount, CGST, SGST, IGST, and HSN/SAC breakdowns."),
            ("Line-Item Capture", "Extracts tables with descriptions, rates, quantities, and discounts."),
            ("Audit-Ready Logs", "Maintains complete processing history and reviewer audit trails.")
        ]
    })

    # B. Logistics & Supply Chain
    build_route_page({
        "rel_path": "logistics-trade/index.html",
        "canonical": "/logistics-trade",
        "title": "AI Logistics Workflow Automation Software | Docsynecx",
        "description": "Automate freight forwarding operations with AI-powered document processing for shipment creation, customs documentation, and CargoWise integration.",
        "eyebrow": "Freight & Shipping Documents",
        "h1": "AI Logistics Automation for Freight Forwarders",
        "lead": "Automate freight forwarding operations with AI-powered document processing for shipment creation, customs documentation, AP reconciliation, and CargoWise integration.",
        "mock_title": "Bill of Lading Extraction",
        "mock_fields": [
            ("Document Type", "Ocean Bill of Lading"),
            ("Consignee", "Global Freight Partners Ltd"),
            ("Port of Loading", "Chennai Port (INMAA)"),
            ("Port of Discharge", "Rotterdam (NLRTM)"),
            ("Gross Weight", "12,480 kg")
        ],
        "challenges": [
            "Shipment data retyped across several logistics systems and portals",
            "Missing documents cause severe customs clearance hold-ups",
            "Every carrier, shipping line, and co-loader uses a different layout",
            "No single real-time view of where each document stands in the workflow"
        ],
        "steps": [
            {
                "title": "We Automatically Collect Your Logistics Documents",
                "desc": "Bills of lading, packing lists, commercial invoices, and customs declarations are gathered automatically from emails, portals, and shared drives.",
                "card_title": "Collecting Shipping Docs...",
                "badge": "Collected ✓",
                "fields": [("bol-5530.pdf", "Received"), ("packing-list.xlsx", "Received"), ("comm-invoice.pdf", "Matched")]
            },
            {
                "title": "We Instantly Extract Critical Shipment Data",
                "desc": "Neural document parsing extracts shipper, consignee, container numbers, voyage details, packages, weights, and HS codes.",
                "card_title": "Shipment Entity Extraction",
                "badge": "Data Structured ✓",
                "fields": [("Shipper", "Apex Logistics"), ("Consignee", "Global Freight"), ("Gross Wt", "12,480 kg")]
            },
            {
                "title": "We Cross-Validate Across Document Sets",
                "desc": "Cross-check the packing list against the Bill of Lading and commercial invoice. Flag weight discrepancies and missing data before filing.",
                "card_title": "Cross-Document Reconciliation",
                "badge": "Validated ✓",
                "fields": [("Container Match", "Verified"), ("Weight Difference", "0 kg discrepancy"), ("Mandatory Fields", "Complete")]
            },
            {
                "title": "We Sync Clean Data Directly into CargoWise One",
                "desc": "Create or update shipment jobs in your TMS 24/7 without human rekeying or CSV manual import errors.",
                "card_title": "Synced with CargoWise TMS",
                "badge": "Job Updated ✓",
                "fields": [("TMS Job", "SHP-2026-9041"), ("Status", "Created"), ("Attachments", "3 docs linked")]
            }
        ],
        "stats": [
            ("10x", "Faster shipment processing"),
            ("99.0%", "Data extraction accuracy"),
            ("99.9%", "Platform uptime"),
            ("Zero", "Manual TMS rekeying")
        ],
        "features_eyebrow": "Logistics Modules",
        "features_title": "Documents In. Shipments Out. Less Busywork.",
        "features_lead": "Each module handles the full document-to-data pipeline independently.",
        "features": [
            ("Shipment Creation", "Automate job creation and updates in your TMS from incoming B/Ls and booking confirmations."),
            ("Customs Documentation", "Convert commercial invoices and packing lists into structured declaration entries and Bill of Entry drafts."),
            ("Freight AP Reconciliation", "Extract carrier invoices and reconcile charges against quotation agreements and job milestones."),
            ("CargoWise Native Sync", "Direct API integration into CargoWise One eAdaptor without intermediary middleware."),
            ("Audit Trail & Compliance", "Track every extracted shipment field with complete visibility on origin and user overrides."),
            ("Multi-Party Document Intake", "Ingest docs directly from overseas agents, customs brokers, and shippers effortlessly.")
        ]
    })

    # Compatibility route /products/logistics-supply-chain
    build_route_page({
        "rel_path": "products/logistics-supply-chain/index.html",
        "canonical": "/products/logistics-supply-chain",
        "title": "Logistics & Supply Chain Automation | Docsynecx",
        "description": "Turn bills of lading, packing lists, and customs documents into structured shipment data with CargoWise sync.",
        "eyebrow": "Freight & Shipping Documents",
        "h1": "AI Logistics Automation for Modern Supply Chains",
        "lead": "Turn bills of lading, packing lists, and customs papers into structured shipment data and send it directly to CargoWise or your TMS.",
        "mock_title": "Bill of Lading Extraction",
        "mock_fields": [
            ("Document Type", "Ocean Bill of Lading"),
            ("Consignee", "Global Freight Partners"),
            ("Gross Weight", "12,480 kg")
        ],
        "challenges": [
            "Shipment data retyped across several systems",
            "Missing documents delay customs clearance",
            "Every carrier uses a different layout"
        ],
        "steps": [
            {
                "title": "We Collect Your Logistics Documents",
                "desc": "Gather bills of lading, packing lists, and commercial invoices from email and drives.",
                "card_title": "Intake...",
                "badge": "Collected ✓",
                "fields": [("bol-5530.pdf", "Received"), ("packing-list.xlsx", "Received")]
            },
            {
                "title": "We Extract Shipment Data",
                "desc": "AI structures parties, ports, container numbers, and weights accurately.",
                "card_title": "Entity Extraction",
                "badge": "Extracted ✓",
                "fields": [("Shipper", "Apex Logistics"), ("Gross Wt", "12,480 kg")]
            },
            {
                "title": "We Validate and Flag Issues",
                "desc": "Cross-check documents against shipment bookings and highlight discrepancies.",
                "card_title": "Reconciliation",
                "badge": "Validated ✓",
                "fields": [("Discrepancies", "None")]
            },
            {
                "title": "We Sync Clean Data to CargoWise",
                "desc": "Post verified shipment and charge records into CargoWise One.",
                "card_title": "TMS Sync",
                "badge": "Synced ✓",
                "fields": [("Job ID", "SHP-2026-9041")]
            }
        ],
        "stats": [
            ("10x", "Faster processing"),
            ("99.0%", "Accuracy"),
            ("99.9%", "Uptime"),
            ("Zero", "Manual rekeying")
        ],
        "features": [
            ("Shipment Creation", "Automate job creation in your TMS."),
            ("Customs Documentation", "Convert invoices into declaration entries."),
            ("CargoWise Native Sync", "Direct integration into CargoWise One.")
        ]
    })

    # C. Workflows & Approvals
    build_route_page({
        "rel_path": "workflows/index.html",
        "canonical": "/workflows",
        "title": "AI Workflow Automation for Finance & Operations | Docsynecx",
        "description": "Replace manual approvals with structured, trackable, and scalable workflows. Built for finance, operations, and enterprise teams.",
        "eyebrow": "Routing, Governance & Control",
        "h1": "Streamline Business Workflows & Approvals with Automation",
        "lead": "Replace manual approvals with structured, trackable, and scalable workflows. Built for finance, operations, and enterprise teams.",
        "mock_title": "Approval Rule Execution",
        "mock_fields": [
            ("Trigger Rule", "Amount above ₹5,00,000"),
            ("Assigned Approver", "Finance Controller"),
            ("Escalation SLA", "24 Hours"),
            ("Audit Status", "Approved & Logged ✓")
        ],
        "challenges": [
            "Approvals chased manually over fragmented email chains and chats",
            "No clear owner or SLA enforcement for document exceptions",
            "Financial limits and approval policies applied inconsistently"
        ],
        "steps": [
            {
                "title": "We Route Every Document Automatically",
                "desc": "Each business document is categorized and routed to the correct department or individual based on amount thresholds, vendor category, or branch.",
                "card_title": "Routing Rules In Action",
                "badge": "Routed ✓",
                "fields": [("Category", "Procurement Invoice"), ("Threshold", "> ₹1,00,000"), ("Destination", "Regional Finance Head")]
            },
            {
                "title": "We Enforce Your Business Rules",
                "desc": "Configurable validation policies verify budget allocations, tolerance variations, and mandatory document attachments before moving forward.",
                "card_title": "Policy Engine Checks",
                "badge": "Rules Verified ✓",
                "fields": [("Budget Allocated", "Within FY26 Q4 Cap"), ("PO Attached", "Verified ✓"), ("Price Variance", "0.4% (Within limit)")]
            },
            {
                "title": "We Consolidate Approvals in One In-App Dashboard",
                "desc": "Approvers review only discrepancies side-by-side with original scans. Trigger automatic reminders and escalations when an approval is overdue.",
                "card_title": "Multi-Level Approval Queue",
                "badge": "Awaiting Review",
                "fields": [("Level 1 Reviewer", "Manager (Approved)"), ("Level 2 Reviewer", "Finance Head (Active)"), ("SLA Remaining", "18 Hours")]
            },
            {
                "title": "We Maintain a Complete, Immutable Audit Trail",
                "desc": "Every view, approval, rejection, comment, and ERP posting is recorded with user identity, timestamp, and metadata ready for compliance audits.",
                "card_title": "Audit Log Generated",
                "badge": "Audit Ready ✓",
                "fields": [("Signed By", "controller@synecx.com"), ("Action", "Final Approve"), ("Audit Hash", "SHA-256 Verified")]
            }
        ],
        "stats": [
            ("80%", "Faster approval cycles"),
            ("100%", "Audit trail transparency"),
            ("Fewer", "Manual approval delays"),
            ("Minutes", "Average turnaround")
        ],
        "features_eyebrow": "Governance Features",
        "features_title": "Enterprise Control Without Bureaucracy",
        "features_lead": "Full governance, accountability, and speed across every business process.",
        "features": [
            ("Multi-Level Approval Chains", "Chain sign-offs by expenditure limits, department, branch, or supplier risk tier."),
            ("Conditional Branching", "Direct clean documents straight to ERP while routing exceptions to specialized supervisors."),
            ("Role-Based Access Control", "Out-of-the-box roles for Clerks, Approvers, Auditors, and System Administrators."),
            ("Automated Escalations", "Re-assign tasks automatically when an approver is out of office or SLA limits expire."),
            ("One-Click Mobile Approvals", "Review and authorize documents swiftly from mobile browsers with secure links."),
            ("Exportable Audit Logs", "One-click export of comprehensive compliance histories for internal and external auditors.")
        ]
    })

    # Compatibility route /products/workflow-approvals
    build_route_page({
        "rel_path": "products/workflow-approvals/index.html",
        "canonical": "/products/workflow-approvals",
        "title": "Workflows & Approvals Automation | Docsynecx",
        "description": "Route, validate, approve and track business documents with multi-level approvals and rule-based controls.",
        "eyebrow": "Routing & Control",
        "h1": "Free Your Team from Chasing Approvals",
        "lead": "Route, validate, approve and track documents with multi-level approvals, rules and role-based access.",
        "mock_title": "Approval Rule Execution",
        "mock_fields": [
            ("Rule", "Amount above ₹5,00,000"),
            ("Approver", "Finance Controller"),
            ("Status", "Awaiting Approval")
        ],
        "challenges": [
            "Approvals chased over email and chat",
            "No clear owner for exceptions",
            "Limits applied inconsistently"
        ],
        "steps": [
            {
                "title": "We Route Documents Automatically",
                "desc": "Each document goes to the right person by amount, vendor, or type.",
                "card_title": "Routing...",
                "badge": "Routed ✓",
                "fields": [("Rule", "Matched")]
            },
            {
                "title": "We Apply Business Rules",
                "desc": "Tolerances decide what posts automatically and what escalates.",
                "card_title": "Policy Check",
                "badge": "Passed ✓",
                "fields": [("Tolerances", "Verified")]
            },
            {
                "title": "We Collect Approvals in One Place",
                "desc": "Approvers act in-app with reminders when items are overdue.",
                "card_title": "Approval Action",
                "badge": "Approved ✓",
                "fields": [("Status", "Approved")]
            },
            {
                "title": "We Keep a Complete Audit Trail",
                "desc": "Every decision is logged and ready to export for compliance.",
                "card_title": "Audit Trail",
                "badge": "Logged ✓",
                "fields": [("Log ID", "AUD-2026-88")]
            }
        ],
        "stats": [
            ("80%", "Faster approvals"),
            ("Fewer", "Manual errors"),
            ("Faster", "Decision-making"),
            ("100%", "Traceability")
        ],
        "features": [
            ("Multi-Level Approvals", "Chain approvers by amount or branch."),
            ("Role-Based Access", "Clerk, approver, supervisor, admin."),
            ("Audit Trail", "Complete exportable decision history.")
        ]
    })

    # =========================================================================
    # 3. SUB-PRODUCT LOGISTICS ROUTES (Shipments, Customs, AP Reconciliation)
    # =========================================================================

    # Logistics / Shipments
    build_route_page({
        "rel_path": "logistics-trade/shipments/index.html",
        "canonical": "/logistics-trade/shipments",
        "title": "Automated Shipment Creation for Freight Forwarders | Docsynecx",
        "description": "Extract Bill of Lading, Sea & Air Waybill, and packing list data to automate shipment job creation in CargoWise.",
        "eyebrow": "Shipment Workflow Automation",
        "h1": "Automate Shipment Creation from Logistics Documents",
        "lead": "Convert Bills of Lading, Waybills, and Packing Lists into structured shipment jobs in your TMS without manual keystrokes.",
        "mock_title": "Shipment Job Auto-Creation",
        "mock_fields": [
            ("Master B/L", "MAEU-982140124"),
            ("Vessel / Voyage", "MAERSK SELETAR / 2604W"),
            ("Container No.", "MSKU-9021482 (40HC)"),
            ("Status", "Job Created in TMS ✓")
        ],
        "challenges": [
            "Operators re-keying container lists and seal numbers across multiple portals",
            "Slow intake creates backlogs during peak shipping schedules",
            "Typo errors in container numbers lead to demurrage penalties"
        ],
        "steps": [
            {
                "title": "Document Capture",
                "desc": "Ingest ocean and air bills of lading from shipping line emails.",
                "card_title": "Waybill Intake",
                "badge": "Captured ✓",
                "fields": [("Source", "Carrier Email"), ("Format", "PDF Scan")]
            },
            {
                "title": "Entity Extraction",
                "desc": "Extract container numbers, seal numbers, piece counts, and weights.",
                "card_title": "Field Extraction",
                "badge": "Extracted ✓",
                "fields": [("Containers", "1 x 40HC"), ("Gross Wt", "18,400 kg")]
            },
            {
                "title": "Booking Validation",
                "desc": "Match the extracted B/L data against pre-existing TMS bookings.",
                "card_title": "Booking Cross-Check",
                "badge": "Matched ✓",
                "fields": [("Booking Ref", "BKG-88120"), ("Match Status", "100%")]
            },
            {
                "title": "TMS Job Creation",
                "desc": "Post verified data directly into CargoWise One forwarding jobs.",
                "card_title": "CargoWise Sync",
                "badge": "Job Created ✓",
                "fields": [("Forwarding Job", "FWD-IN-2026-11"), ("Status", "Active")]
            }
        ],
        "stats": [
            ("10x", "Faster job creation"),
            ("99.0%", "Accuracy on container data"),
            ("24/7", "Autonomous processing"),
            ("0", "Typo errors on filing")
        ],
        "features": [
            ("Multi-Container Extraction", "Parse multi-page manifests with dozens of containers and seal numbers."),
            ("Carrier Format Adaptability", "Works on Maersk, MSC, CMA CGM, Hapag-Lloyd, and regional feeder formats."),
            ("Direct CargoWise Integration", "Native job updates through CargoWise One eAdaptor.")
        ]
    })

    # Logistics / Customs Declarations
    build_route_page({
        "rel_path": "logistics-trade/custom-declarations/index.html",
        "canonical": "/logistics-trade/custom-declarations",
        "title": "AI Customs Declaration & Bill of Entry Automation | Docsynecx",
        "description": "Convert commercial invoices and packing lists into pre-filled customs declarations and Bill of Entry entries with HS code verification.",
        "eyebrow": "Customs Entry Automation",
        "h1": "Pre-Fill Customs Declarations Automatically with AI",
        "lead": "Streamline customs clearance by converting source commercial invoices and packing lists into structured declaration entries and compliance drafts.",
        "mock_title": "Customs Entry Preparation",
        "mock_fields": [
            ("Entry Type", "Bill of Entry (Import)"),
            ("HS Code", "8471.30.10 (Verified ✓)"),
            ("Assessable Value", "USD 42,500.00"),
            ("Customs System", "ICEGATE / CargoWise Ready ✓")
        ],
        "challenges": [
            "Manually typing hundreds of invoice lines into customs portals",
            "Incorrect HS code classification causing customs delays and penalties",
            "Mismatched quantities between packing lists and commercial invoices"
        ],
        "steps": [
            {
                "title": "Ingest Invoices & Packing Lists",
                "desc": "Upload commercial invoices, certificates of origin, and packing lists.",
                "card_title": "Customs Docs Ingestion",
                "badge": "Loaded ✓",
                "fields": [("Comm Invoice", "INV-US-991"), ("Packing List", "PL-991")]
            },
            {
                "title": "Extract Line Items & Descriptions",
                "desc": "AI captures item descriptions, quantities, unit values, and country of origin.",
                "card_title": "Line Item Capture",
                "badge": "Captured ✓",
                "fields": [("Items", "34 Lines"), ("Currency", "USD")]
            },
            {
                "title": "Validate HS Codes & Taxes",
                "desc": "Cross-check 8-digit HS codes and verify assessable duties.",
                "card_title": "Tariff Validation",
                "badge": "Compliant ✓",
                "fields": [("HS Code", "8471.30.10"), ("Duty Rate", "7.5% BCD + 18% IGST")]
            },
            {
                "title": "Push to Customs Software",
                "desc": "Transmit verified declaration data into CargoWise Customs or filing software.",
                "card_title": "Customs Export",
                "badge": "Dispatched ✓",
                "fields": [("Declaration Draft", "BOE-Draft-2026"), ("Status", "Ready to File")]
            }
        ],
        "stats": [
            ("85%", "Reduction in filing prep time"),
            ("99.5%", "HS code verification accuracy"),
            ("Zero", "Late filing demurrage"),
            ("100%", "Audit trail compliance")
        ],
        "features": [
            ("Line-Level Harmonization", "Extracts complex multi-page commercial invoice item lines with exact values."),
            ("Duty & Tax Calculation", "Computes basic customs duty, IGST, and social welfare surcharge estimations."),
            ("Compliance Cross-Checks", "Validates importer-exporter codes (IEC) and mandatory trade declarations.")
        ]
    })

    # Logistics / AP Reconciliation
    build_route_page({
        "rel_path": "logistics-trade/ap-reconciliation/index.html",
        "canonical": "/logistics-trade/ap-reconciliation",
        "title": "Logistics Freight AP Reconciliation Software | Docsynecx",
        "description": "Reconcile ocean, air, and co-loader freight invoices against agreed TMS rate cards and job buy-lines automatically.",
        "eyebrow": "Freight Invoice Reconciliation",
        "h1": "Reconcile Freight AP Invoices in Real Time",
        "lead": "Extract carrier charges, map them to TMS charge codes, and validate against expected costs to catch overbilling before payments go out.",
        "mock_title": "Freight Invoice Audit",
        "mock_fields": [
            ("Carrier Invoice", "MSK-INV-99214"),
            ("Expected Cost", "USD 2,400.00"),
            ("Billed Amount", "USD 2,400.00"),
            ("Variance", "USD 0.00 (Approved ✓)")
        ],
        "challenges": [
            "Unexpected demurrage, detention, and fuel surcharges billed without notice",
            "Manual comparison between carrier invoices and quotation sheets",
            "Overbilling slipping through during busy month-end payment cycles"
        ],
        "steps": [
            {
                "title": "Carrier Invoice Ingestion",
                "desc": "Collect ocean and air freight invoices from carrier emails.",
                "card_title": "Freight Bill Intake",
                "badge": "Received ✓",
                "fields": [("Carrier", "Shipping Line"), ("Invoice", "INV-FRT-881")]
            },
            {
                "title": "Charge Item Extraction",
                "desc": "Extract base freight, terminal handling (THC), documentation, and detention fees.",
                "card_title": "Itemized Charges",
                "badge": "Extracted ✓",
                "fields": [("Base Freight", "$1,850"), ("THC", "$250"), ("Doc Fee", "$75")]
            },
            {
                "title": "Reconciliation Against TMS Rates",
                "desc": "Compare invoiced charges with the shipment job's agreed buy-lines in CargoWise.",
                "card_title": "Automated Audit",
                "badge": "Reconciled ✓",
                "fields": [("Variance", "0%"), ("Rate Sheet", "Approved Contract")]
            },
            {
                "title": "Approved Voucher Sync",
                "desc": "Post validated carrier payables into your accounting ledger with attached proof.",
                "card_title": "AP Voucher Posted",
                "badge": "Posted ✓",
                "fields": [("Job Costing", "Updated"), ("Status", "Ready for Payment")]
            }
        ],
        "stats": [
            ("3–5%", "Direct margin saved on freight bills"),
            ("90%", "Faster supplier invoice approval"),
            ("100%", "Audit trail of verified rates"),
            ("Real-time", "Demurrage leak detection")
        ],
        "features": [
            ("Charge Code Normalization", "Maps arbitrary carrier line items to your standard TMS cost categories."),
            ("Discrepancy Highlighting", "Surfaces rate mismatches and unapproved surcharges instantly."),
            ("Duplicate Invoice Protection", "Guards against paying duplicate carrier submissions across voyages.")
        ]
    })

    # =========================================================================
    # 4. INTEGRATION ROUTES (Tally, Zoho Books, CargoWise)
    # =========================================================================

    # Tally Integration
    build_route_page({
        "rel_path": "integration/invoice-to-tally/index.html",
        "canonical": "/integration/invoice-to-tally",
        "title": "TallyPrime AI Invoice Automation & Voucher Sync | Docsynecx",
        "description": "Post validated purchase and sales vouchers directly into TallyPrime and Tally.ERP 9 with automatic ledger and GST tax mapping.",
        "eyebrow": "TallyPrime Accounting Automation",
        "h1": "Direct AI Invoice to TallyPrime Integration",
        "lead": "Post validated purchase and sales vouchers into TallyPrime without retyping. Automatic ledger matching, GSTIN validation, and HSN allocation.",
        "mock_title": "TallyPrime Voucher Posting",
        "mock_fields": [
            ("Voucher Type", "Purchase Voucher"),
            ("Party Ledger", "Synecx Partner Supplier"),
            ("Tax Ledgers", "Input CGST & SGST (18%)"),
            ("Posting Status", "Voucher Posted in TallyPrime ✓")
        ],
        "challenges": [
            "Accountants spending hours manually typing GST invoices into Tally screens",
            "Mismatched ledger names causing messy chart of accounts duplicates",
            "Manual calculation mistakes in GST tax splits and reverse charge postings"
        ],
        "steps": [
            {
                "title": "Upload or Email Invoices",
                "desc": "Invoices are ingested and parsed with accurate line-item and tax breakdown.",
                "card_title": "Invoice Processing",
                "badge": "Parsed ✓",
                "fields": [("Vendor", "Supplier"), ("Total", "₹1,45,200.00")]
            },
            {
                "title": "One-Time Ledger Mapping",
                "desc": "Map vendor names and item categories once; Docsynecx remembers them forever.",
                "card_title": "Tally Master Mapping",
                "badge": "Mapped ✓",
                "fields": [("Party", "Matched in Master"), ("Stock Item", "Mapped to SKU")]
            },
            {
                "title": "Automated Validation",
                "desc": "GSTIN verification, duplicate check, and tax calculation audit prior to sync.",
                "card_title": "Audit Check",
                "badge": "Verified ✓",
                "fields": [("GSTIN", "Active"), ("Voucher No", "Unique")]
            },
            {
                "title": "Direct Voucher Sync",
                "desc": "Push clean XML/API voucher directly into your local or cloud TallyPrime instance.",
                "card_title": "TallyPrime Result",
                "badge": "Posted ✓",
                "fields": [("Tally Master ID", "VCH-2026-901"), ("Status", "Created Successfully")]
            }
        ],
        "stats": [
            ("10x", "Faster voucher creation"),
            ("100%", "Accurate GST split allocation"),
            ("0", "Duplicate voucher postings"),
            ("Secure", "Local Tally connector & cloud ready")
        ],
        "features": [
            ("Purchase & Sales Vouchers", "Generates complete accounting vouchers with multiple stock items."),
            ("Smart Ledger Mapping", "Intelligent alias matching links variations in vendor names to the right master."),
            ("TallyPrime & ERP 9 Support", "Seamless support for both TallyPrime and legacy Tally.ERP 9 installations.")
        ]
    })

    # Compatibility route /integrations/tally
    build_route_page({
        "rel_path": "integrations/tally/index.html",
        "canonical": "/integrations/tally",
        "title": "Tally Integration | Docsynecx",
        "description": "Post validated purchase and sales vouchers into TallyPrime without retyping.",
        "eyebrow": "TallyPrime Accounting Automation",
        "h1": "Direct AI Invoice to Tally Integration",
        "lead": "Post validated purchase and sales vouchers into TallyPrime without retyping. Automatic ledger matching and GSTIN validation.",
        "mock_title": "Tally Voucher Posting",
        "mock_fields": [
            ("Voucher", "Purchase"),
            ("Ledger", "Synecx Partner Supplier"),
            ("Status", "Posted ✓")
        ],
        "features": [
            ("Purchase Vouchers", "Generated with line items and GST."),
            ("Ledger Mapping", "Mapped once, remembered every time."),
            ("Audit Logs", "Every entry recorded with timestamp.")
        ]
    })

    # Zoho Books Integration
    build_route_page({
        "rel_path": "integration/zoho-books/index.html",
        "canonical": "/integration/zoho-books",
        "title": "Zoho Books Invoice Automation & Bill Creation | Docsynecx",
        "description": "Create vendor bills, items, and tax entries in Zoho Books straight from validated documents with OAuth2 security.",
        "eyebrow": "Zoho Books Cloud Integration",
        "h1": "Automated Bill Processing for Zoho Books",
        "lead": "Create bills, vendors, and line items in Zoho Books straight from validated documents with zero manual data entry.",
        "mock_title": "Zoho Books Bill Sync",
        "mock_fields": [
            ("Document Type", "Vendor Bill"),
            ("Zoho Vendor", "Synecx Supplier"),
            ("Bill Number", "BILL-2026-881"),
            ("Sync Status", "Created in Zoho Books ✓")
        ],
        "challenges": [
            "Manually typing PDF invoices into Zoho Books bill screens",
            "Slow expense processing delaying month-end vendor reconciliation",
            "Missing document attachments on created accounting transactions"
        ],
        "steps": [
            {
                "title": "Connect Securely via OAuth",
                "desc": "Authorize Docsynecx with your Zoho Books organization with one click.",
                "card_title": "Zoho OAuth2",
                "badge": "Connected ✓",
                "fields": [("Auth", "Encrypted Token"), ("Org", "Main Organization")]
            },
            {
                "title": "AI Ingestion & Tax Extraction",
                "desc": "Extract invoice line items, tax brackets, and vendor GSTIN.",
                "card_title": "Data Extraction",
                "badge": "Extracted ✓",
                "fields": [("Line Items", "Captured"), ("Tax Split", "CGST/SGST/IGST")]
            },
            {
                "title": "Account & Item Mapping",
                "desc": "Match Zoho Books chart of accounts and item master records automatically.",
                "card_title": "Account Matching",
                "badge": "Matched ✓",
                "fields": [("Expense Account", "Cost of Goods Sold"), ("Item", "Standard SKU")]
            },
            {
                "title": "Bill Creation with PDF Attachment",
                "desc": "The complete bill is created in Zoho Books with the original PDF attached.",
                "card_title": "Zoho Bill Created",
                "badge": "Bill Created ✓",
                "fields": [("Bill ID", "BILL-09214"), ("Attachment", "invoice.pdf linked")]
            }
        ],
        "stats": [
            ("80%", "Faster bill creation"),
            ("100%", "PDF attachment retention"),
            ("Zero", "Manual transcription errors"),
            ("Real-time", "Sync directly to Zoho API")
        ],
        "features": [
            ("Native Zoho API Integration", "Direct REST connection into Zoho Books cloud infrastructure."),
            ("Automatic Vendor Matching", "Matches incoming bills to existing Zoho contacts or creates verified new vendors."),
            ("Original Document Stored", "Every created bill keeps a direct copy of the source document attached for tax compliance.")
        ]
    })

    # Compatibility route /integrations/zoho-books
    build_route_page({
        "rel_path": "integrations/zoho-books/index.html",
        "canonical": "/integrations/zoho-books",
        "title": "Zoho Books Integration | Docsynecx",
        "description": "Create bills, vendors, and line items in Zoho Books straight from validated documents.",
        "eyebrow": "Zoho Books Cloud Integration",
        "h1": "Automated Bill Processing for Zoho Books",
        "lead": "Create bills, vendors and line items in Zoho Books straight from validated documents.",
        "mock_title": "Zoho Books Sync",
        "mock_fields": [
            ("Bill", "BILL-2026"),
            ("Vendor", "Synecx Supplier"),
            ("Status", "Created ✓")
        ],
        "features": [
            ("Native Zoho API", "Direct connection to Zoho Books."),
            ("Vendor Matching", "Matches contacts automatically."),
            ("PDF Attachment", "Source file attached to bill.")
        ]
    })

    # CargoWise Integration
    build_route_page({
        "rel_path": "integration/cargowise/index.html",
        "canonical": "/integration/cargowise",
        "title": "CargoWise One Document Automation Integration | Docsynecx",
        "description": "Send verified shipment and charge data directly into CargoWise One via native eAdaptor APIs without rekeying.",
        "eyebrow": "CargoWise One TMS Integration",
        "h1": "Direct CargoWise One Document Integration",
        "lead": "Send verified shipment and charge data into CargoWise One without rekeying. Direct integration via native APIs, not flat files or middleware.",
        "mock_title": "CargoWise eAdaptor Sync",
        "mock_fields": [
            ("CargoWise Module", "Forwarding / Customs"),
            ("Shipment Ref", "SHP-CW-90214"),
            ("Charges Attached", "7 Verified Lines"),
            ("Sync Method", "eAdaptor XML API ✓")
        ],
        "challenges": [
            "Logistics clerks spending hours retyping container and charge data into CargoWise",
            "Slow data entry delaying export and import milestones",
            "Fragile CSV and flat-file import batch workflows causing unexpected job errors"
        ],
        "steps": [
            {
                "title": "Configure CargoWise Endpoint",
                "desc": "Link your CargoWise One system using secure eAdaptor credentials.",
                "card_title": "eAdaptor Setup",
                "badge": "Ready ✓",
                "fields": [("Protocol", "Native eAdaptor"), ("Enterprise ID", "Linked")]
            },
            {
                "title": "Logistics Document Extraction",
                "desc": "Bills of Lading, manifests, and freight bills are converted into structured shipment entities.",
                "card_title": "Logistics Parsing",
                "badge": "Extracted ✓",
                "fields": [("B/L Data", "Parsed"), ("Charge Items", "Categorized")]
            },
            {
                "title": "Charge Code & Branch Mapping",
                "desc": "Map carrier fees to your standard CargoWise charge codes and cost centers.",
                "card_title": "Code Normalization",
                "badge": "Mapped ✓",
                "fields": [("Charge Code", "FRT / THC / DOC"), ("Branch", "Main Port Office")]
            },
            {
                "title": "Automated CargoWise Sync",
                "desc": "Verified shipment jobs, containers, and job costing lines post straight into your TMS.",
                "card_title": "Job Costing Updated",
                "badge": "Synced ✓",
                "fields": [("Shipment Record", "Updated"), ("Job Charges", "Posted")]
            }
        ],
        "stats": [
            ("10x", "Faster CargoWise job updates"),
            ("100%", "Native API communication"),
            ("Zero", "Middleware or manual CSV imports"),
            ("Real-time", "Job costing updates")
        ],
        "features": [
            ("Native eAdaptor Connectors", "Direct, compliant XML schema messaging into CargoWise One."),
            ("Job Costing & Charges", "Pushes verified freight payables directly into shipment financial tabs."),
            ("Document Archival", "Attaches original PDF source documents directly to the CargoWise eDocs tab.")
        ]
    })

    # Compatibility route /integrations/cargowise
    build_route_page({
        "rel_path": "integrations/cargowise/index.html",
        "canonical": "/integrations/cargowise",
        "title": "CargoWise Integration | Docsynecx",
        "description": "Send verified shipment and charge data into CargoWise without rekeying.",
        "eyebrow": "CargoWise One TMS Integration",
        "h1": "Direct CargoWise One Document Integration",
        "lead": "Send verified shipment and charge data into CargoWise without rekeying.",
        "mock_title": "CargoWise Sync",
        "mock_fields": [
            ("Shipment", "SHP-CW-90214"),
            ("Charges", "7 lines"),
            ("Status", "Synced ✓")
        ],
        "features": [
            ("eAdaptor Sync", "Native XML connection."),
            ("Job Costing", "Pushes freight payables."),
            ("eDocs Attachment", "Originals stored in CargoWise.")
        ]
    })

    # =========================================================================
    # 5. SOLUTIONS ROUTES (Solutions Hub, Banking, Finance, Logistics, AP)
    # =========================================================================

    # Solutions Hub
    build_route_page({
        "rel_path": "solutions/index.html",
        "canonical": "/solutions",
        "title": "AI Document Automation Solutions for Business | Docsynecx",
        "description": "Next-generation IDP platform and AI-powered document intelligence tailored for banking, finance, healthcare, and logistics.",
        "eyebrow": "Intelligent Document Processing Solutions",
        "h1": "Next-Generation IDP Platform & AI-Powered Solutions",
        "lead": "Streamline your document workflows with Automated Document Intelligence and AI-driven data extraction — delivering tailored solutions for every industry.",
        "mock_title": "Multi-Industry IDP Engine",
        "mock_fields": [
            ("Supported Formats", "PDF, Scans, TIFF, JPG"),
            ("Extraction Type", "Template-Free Neural OCR"),
            ("Validation Rules", "Business Rules Engine"),
            ("Enterprise Connectors", "Tally, Zoho, SAP, CargoWise")
        ],
        "stats": [
            ("99.0%", "Data extraction accuracy"),
            ("10x", "Faster processing"),
            ("80%", "Reduction in manual entry"),
            ("Multi-Industry", "Banking, Logistics, Finance")
        ],
        "features_eyebrow": "By Industry & Use Case",
        "features_title": "Specialized Document Processing Across Sectors",
        "features_lead": "Built to tackle complex, high-volume unstructured files.",
        "features": [
            ("Banking & Financial Services", "Bank statement reconciliation, KYC identity verification, and loan document extraction."),
            ("Accounts Payable & Finance", "Invoice automation, 2-way/3-way matching, GST validation, and ledger synchronization."),
            ("Logistics & Supply Chain", "Bills of lading, packing lists, manifests, customs entries, and TMS integrations."),
            ("Receipt & Expense Management", "Automated expense categorization, tax compliance, and employee claim validation."),
            ("Custom Document Workflows", "Tailored extraction models for industry-specific proprietary forms and layouts."),
            ("Enterprise REST API Services", "Embed intelligent data extraction into your existing software and customer portals.")
        ]
    })

    # Banking & Finance Solution
    build_route_page({
        "rel_path": "solutions/banking/index.html",
        "canonical": "/solutions/banking",
        "title": "AI Document Automation for Banking & Finance | Docsynecx",
        "description": "Statements, KYC forms, and loan documents read and validated in one secure, compliant document intelligence workflow.",
        "eyebrow": "Banking & Financial Services",
        "h1": "Intelligent Document Automation for Banking & Financial Services",
        "lead": "Bank statements, KYC forms, and loan documents read and verified in one automated workflow with complete audit traceability.",
        "mock_title": "KYC & Statement Verification",
        "mock_fields": [
            ("Document Type", "Bank Statement (12 Months)"),
            ("Transactions Parsed", "1,420 Lines"),
            ("Account Match", "Verified ✓"),
            ("Audit Trail", "Tamper-Proof Log ✓")
        ],
        "challenges": [
            "KYC and loan packages arrive in mixed, scanned, and unstandardized formats",
            "Manual review creates onboarding friction and delays customer acquisition",
            "Stringent regulatory audits require complete traceability for every decision"
        ],
        "steps": [
            {
                "title": "Document Ingestion",
                "desc": "Collect bank statements, identity cards, and financial statements via upload or API.",
                "card_title": "Financial Intake",
                "badge": "Ingested ✓",
                "fields": [("Files", "Bank Statements, KYC"), ("Format", "PDF / Scans")]
            },
            {
                "title": "Entity & Transaction Extraction",
                "desc": "AI extracts statement balances, recurring payments, PAN, and identity details.",
                "card_title": "Transaction Parsing",
                "badge": "Extracted ✓",
                "fields": [("Statement Period", "12 Months"), ("Transactions", "Categorized")]
            },
            {
                "title": "Verification & Fraud Checks",
                "desc": "Run rule-based checks on account names, tax IDs, and document alterations.",
                "card_title": "Compliance Check",
                "badge": "Verified ✓",
                "fields": [("PAN / Aadhaar", "Format Valid"), ("Alteration Check", "Clean")]
            },
            {
                "title": "Core Banking / ERP Sync",
                "desc": "Push structured financial profiles into underwriting software or core banking systems.",
                "card_title": "System Update",
                "badge": "Synced ✓",
                "fields": [("Underwriting Profile", "Generated"), ("Status", "Approved")]
            }
        ],
        "stats": [
            ("99.0%", "Accuracy on financial records"),
            ("80%", "Faster onboarding cycles"),
            ("100%", "Audit trail transparency"),
            ("Zero", "Manual transcription")
        ],
        "features": [
            ("Bank Statement Analysis", "Parses complex statement formats from all major Indian and international banks."),
            ("KYC Document Extraction", "Extracts structured metadata from identity proofs and business registrations."),
            ("Loan Document Verification", "Pulls key covenants, interest rates, and loan terms into underwriting tools.")
        ]
    })

    # Finance Solution
    build_route_page({
        "rel_path": "solutions/finance/index.html",
        "canonical": "/solutions/finance",
        "title": "Document Automation for Finance Teams & CA Firms | Docsynecx",
        "description": "Invoices, receipts, and bank reconciliations processed accurately for corporate finance teams and CA firms.",
        "eyebrow": "Corporate Finance & CA Firms",
        "h1": "AI Document Processing for Finance Teams & Accounting Firms",
        "lead": "Invoices, receipts, and reconciliations processed accurately for finance teams and CA firms with direct ledger posting.",
        "mock_title": "Finance Reconciliation Engine",
        "mock_fields": [
            ("Process", "Month-End AP Reconciliation"),
            ("Invoices Processed", "3,400 Documents"),
            ("Ledger Posting", "Tally & Zoho Books Ready ✓"),
            ("Audit Status", "100% Reconciled")
        ],
        "challenges": [
            "Month-end book close delayed by piles of unentered vendor invoices",
            "Manual receipt categorization prone to missing input tax credits",
            "Audit teams spending days searching for source document evidence"
        ],
        "stats": [
            ("80%", "Faster month-end close"),
            ("60–70%", "Cost reduction on bookkeeping"),
            ("99%", "Tax compliance accuracy"),
            ("Minutes", "Turnaround on batches")
        ],
        "features": [
            ("Automated Invoice Booking", "Extracts and posts invoices straight into your general ledger."),
            ("Receipt Expense Tracking", "Categorizes employee claims and receipts with accurate GST splits."),
            ("Bank Reconciliation", "Matches bank statement entries against cash and credit vouchers automatically.")
        ]
    })

    # Logistics Solution
    build_route_page({
        "rel_path": "solutions/logistics/index.html",
        "canonical": "/solutions/logistics",
        "title": "Logistics & Supply Chain Document Automation | Docsynecx",
        "description": "Bills of lading, packing lists, and customs documents processed automatically for freight forwarders and shippers.",
        "eyebrow": "Logistics & Supply Chain",
        "h1": "End-to-End Document Automation for Logistics & Supply Chain",
        "lead": "Bills of lading, packing lists, and customs documents read, verified, and pushed to your TMS without delay.",
        "mock_title": "Supply Chain Document Hub",
        "mock_fields": [
            ("Documents Handled", "BOL, AWB, Packing List, Invoice"),
            ("Integration", "CargoWise One eAdaptor"),
            ("Processing Time", "< 30 seconds per document"),
            ("Discrepancies", "Highlighted automatically")
        ],
        "stats": [
            ("10x", "Faster shipment entry"),
            ("99.0%", "Accuracy on bill of lading lines"),
            ("Zero", "Customs clearance delay"),
            ("24/7", "Autonomous TMS updates")
        ],
        "features": [
            ("Bill of Lading Parsing", "Accurately extracts shipper, consignee, ports, containers, and seals."),
            ("Packing List Reconciliation", "Matches items, package counts, and weights against commercial invoices."),
            ("Direct CargoWise Posting", "Posts data directly into forwarding and customs jobs via eAdaptor.")
        ]
    })

    # Accounts Payable Solution
    build_route_page({
        "rel_path": "solutions/accounts-payable/index.html",
        "canonical": "/solutions/accounts-payable",
        "title": "Accounts Payable Automation Software | Docsynecx",
        "description": "End-to-end AP automation from invoice intake and 2-way/3-way matching to multi-level approvals and ERP posting.",
        "eyebrow": "AP Workflow Automation",
        "h1": "End-to-End Accounts Payable Automation",
        "lead": "Automate your entire invoice-to-payment cycle: document capture, line-item extraction, GST checks, approval routing, and ERP voucher sync.",
        "mock_title": "AP Pipeline Overview",
        "mock_fields": [
            ("Pipeline Status", "Autonomous AP Processing"),
            ("Matching Rule", "3-Way (PO + GRN + Invoice)"),
            ("Tolerance", "0.5% Allowed"),
            ("Sync Target", "TallyPrime & Zoho Books ✓")
        ],
        "challenges": [
            "Invoices waiting in inboxes for manual typing",
            "Duplicate invoices slipping through payment approvals",
            "Vendor relationship strain caused by delayed settlement cycles"
        ],
        "stats": [
            ("80%", "Faster AP cycle"),
            ("60–70%", "Cost reduction per invoice"),
            ("99%+", "Data accuracy"),
            ("100%", "Input tax credit protection")
        ],
        "features": [
            ("Automated Capture", "Ingest invoices from email, vendor portals, and scanner uploads."),
            ("3-Way Matching", "Match invoice amounts against Purchase Orders and Goods Receipts automatically."),
            ("Approval Governance", "Multi-tier approval workflows with escalation triggers and audit logs.")
        ]
    })

    # =========================================================================
    # 6. RESOURCES ROUTES (Blog, Help, Case Studies)
    # =========================================================================

    # Blog
    build_route_page({
        "rel_path": "blog/index.html",
        "canonical": "/blog",
        "title": "Document Automation Blog & Knowledge Base | Docsynecx",
        "description": "Explore expert insights, guides, and practical advice on AI document processing, AP automation, and Tally integration.",
        "eyebrow": "Knowledge Base & Insights",
        "h1": "Insights on Document Intelligence & Automation",
        "lead": "Practical guides, technical explainers, and best practices for scaling finance and logistics operations with AI.",
        "mock_title": "Docsynecx Knowledge Hub",
        "mock_fields": [
            ("Categories", "AP Automation, Logistics, ERP Sync"),
            ("Guides", "TallyPrime, Zoho, CargoWise"),
            ("Latest Article", "How AI Is Transforming Invoice Processing")
        ],
        "features_eyebrow": "Featured Articles",
        "features_title": "Latest Guides & Best Practices",
        "features_lead": "Learn how modern businesses eliminate manual busywork.",
        "features": [
            ("How AI Is Transforming Invoice Processing", "A comprehensive guide on moving from manual data entry to touchless AP workflows with 99%+ accuracy."),
            ("Connecting Docsynecx to TallyPrime", "Step-by-step technical tutorial on configuring automated voucher sync and ledger mapping into Tally."),
            ("Logistics Document Automation Guide", "How freight forwarders leverage AI to process Bills of Lading, packing lists, and customs declarations 10x faster."),
            ("Best Practices for GST Tax Reconciliation", "Prevent tax leakages and claim full input tax credits with automated GSTIN and invoice validation rules."),
            ("CargoWise One Integration Patterns", "Architecture deep-dive on syncing unstructured documents into CargoWise eAdaptor without middleware."),
            ("Evaluating Document Intelligence Platforms", "Checklist for finance leaders evaluating accuracy, compliance, and enterprise ERP connectivity.")
        ]
    })

    # Compatibility route /resources/blog
    build_route_page({
        "rel_path": "resources/blog/index.html",
        "canonical": "/resources/blog",
        "title": "Blog & Guides | Docsynecx",
        "description": "Guides and explainers on AI document processing and automation.",
        "eyebrow": "Knowledge Base",
        "h1": "Docsynecx Blog & Resource Hub",
        "lead": "Guides and explainers on document automation for finance and logistics teams.",
        "mock_title": "Resource Hub",
        "mock_fields": [("Resource", "Guides & Insights"), ("Format", "Articles & Tutorials")],
        "features": [
            ("Invoice Automation Guide", "Setup extraction, matching, and posting."),
            ("How GST Validation Works", "Understand checks and exception workflows."),
            ("Connecting to Tally", "Step-by-step setup for TallyPrime.")
        ]
    })

    # Help / Support Docs
    build_route_page({
        "rel_path": "help/index.html",
        "canonical": "/help",
        "title": "Help Center & Documentation | Docsynecx",
        "description": "Browse FAQs, system integration guides, API references, and support resources for the Docsynecx document intelligence platform.",
        "eyebrow": "Support Documentation",
        "h1": "Docsynecx Help Center & Platform Documentation",
        "lead": "Everything you need to set up, configure, and operate document automation for finance, logistics, and workflows.",
        "mock_title": "Platform Knowledge Base",
        "mock_fields": [
            ("Support Status", "Active 24/7"),
            ("Documentation", "Setup, ERP, API, Security"),
            ("Response SLA", "< 2 Hours on Enterprise")
        ],
        "features_eyebrow": "Help Topics",
        "features_title": "Browse Support Categories",
        "features_lead": "Quick answers to common questions and configuration guides.",
        "features": [
            ("Getting Started & Quick Start", "Create an account, invite team members, and upload your first document batch in under 5 minutes."),
            ("ERP & Accounting Connectors", "Configuration walkthroughs for TallyPrime, Tally.ERP 9, Zoho Books, SAP, and CargoWise."),
            ("REST API & Webhook Reference", "Developer documentation for sending documents programmatically and receiving validated JSON payloads."),
            ("Roles & Security Controls", "Managing user roles, permission scoping, audit trails, and multi-factor authentication."),
            ("Document Exception Handling", "How to resolve flagged mismatches, add custom validation rules, and train entity extractors."),
            ("Billing & Subscription Plans", "Managing trial credits, user seats, enterprise add-ons, and payment methods.")
        ]
    })

    # Compatibility route /resources/support-docs
    build_route_page({
        "rel_path": "resources/support-docs/index.html",
        "canonical": "/resources/support-docs",
        "title": "Support Docs | Docsynecx",
        "description": "Everything you need to set up and run Docsynecx.",
        "eyebrow": "Documentation",
        "h1": "Docsynecx Support & Setup Docs",
        "lead": "Everything you need to set up and run Docsynecx across finance and logistics.",
        "mock_title": "Documentation",
        "mock_fields": [("Docs", "Platform Setup"), ("Status", "Available")],
        "features": [
            ("Quick Start", "Create an account and upload your first document."),
            ("Connect Your ERP", "Tally, Zoho Books, CargoWise and SAP setup."),
            ("API & Webhooks", "Send documents and receive results programmatically.")
        ]
    })

    # Case Studies Route (Flagged in MISSING_CONTENT.md as prototype placeholder)
    build_route_page({
        "rel_path": "resources/case-study/index.html",
        "canonical": "/resources/case-study",
        "title": "Case Studies & Customer Stories | Docsynecx",
        "description": "Discover how businesses transform operations with Docsynecx AI document automation.",
        "eyebrow": "Customer Success",
        "h1": "Measurable Impact Across Finance & Logistics",
        "lead": "Real operational outcomes achieved by teams running invoice processing, freight documentation, and approval workflows on Docsynecx.",
        "mock_title": "Impact Benchmark",
        "mock_fields": [
            ("Processing Speed", "10x Acceleration"),
            ("Cost Reduction", "60–70% Savings"),
            ("Accuracy Rate", "99%+ Maintained")
        ],
        "features_eyebrow": "Outcome Highlights",
        "features_title": "Verified Performance Benchmarks",
        "features_lead": "Real figures based on live enterprise deployments.",
        "features": [
            ("Accelerated Processing Time", "Finance and freight forwarding teams reduce document turnaround from hours to minutes."),
            ("Lower Operational Overhead", "Elimination of repetitive manual keystrokes frees teams for strategic vendor and client service."),
            ("Audit-Ready Peace of Mind", "Complete governance and input tax credit validation ensures compliance on every voucher.")
        ]
    })

    # =========================================================================
    # 7. COMPANY ROUTES (About, Enterprise, Partners, Careers, Contact)
    # =========================================================================

    # About
    build_route_page({
        "rel_path": "about/index.html",
        "canonical": "/about",
        "title": "About Docsynecx | SynecxAI Labs Private Limited",
        "description": "Docsynecx is an AI-powered document intelligence and automation platform built by SynecxAI Labs Private Limited.",
        "eyebrow": "Our Mission",
        "h1": "Building the Future of Document Automation",
        "lead": "Docsynecx is the AI-powered document automation platform developed by SynecxAI Labs Private Limited to eliminate busywork in finance and global trade.",
        "mock_title": "SynecxAI Labs Platform",
        "mock_fields": [
            ("Company", "SynecxAI Labs Private Limited"),
            ("Core Focus", "Finance & Logistics Automation"),
            ("Core Values", "Accuracy, Speed, Traceability")
        ],
        "stats": [
            ("99.0%", "Data accuracy commitment"),
            ("10x", "Throughput acceleration"),
            ("100%", "Audit compliance"),
            ("Enterprise", "Bank-grade security")
        ],
        "features_eyebrow": "Core Principles",
        "features_title": "Why Modern Businesses Choose Docsynecx",
        "features_lead": "Designed for mission-critical workflows where precision matters.",
        "features": [
            ("Accuracy First", "Data is verified and cross-checked before it ever reaches your systems of record."),
            ("Hours to Minutes", "End-to-end automation transforms slow document backlogs into instant execution."),
            ("Complete Traceability", "Every single extracted field and approval decision is fully auditable and verifiable.")
        ]
    })

    # Compatibility route /company/about
    build_route_page({
        "rel_path": "company/about/index.html",
        "canonical": "/company/about",
        "title": "About Us | Docsynecx",
        "description": "Docsynecx is the AI-powered document automation platform from SynecxAI Labs Private Limited.",
        "eyebrow": "Our Company",
        "h1": "About SynecxAI Labs & Docsynecx",
        "lead": "Docsynecx is the AI-powered document automation platform from SynecxAI Labs Private Limited.",
        "mock_title": "Company Overview",
        "mock_fields": [("Company", "SynecxAI Labs"), ("Platform", "Docsynecx")],
        "features": [
            ("Accuracy", "Validated data before it reaches your systems."),
            ("Speed", "Hours to minutes across finance and logistics."),
            ("Control", "Every field and decision is traceable.")
        ]
    })

    # Enterprise
    build_route_page({
        "rel_path": "enterprise/index.html",
        "canonical": "/enterprise",
        "title": "Enterprise Document Automation Solutions | Docsynecx",
        "description": "High-volume document intelligence, custom ERP connectors (SAP, Oracle), dedicated SLAs, and enterprise security for large organizations.",
        "eyebrow": "Enterprise Scale",
        "h1": "Enterprise-Grade Document Automation & Security",
        "lead": "Custom automation, dedicated onboarding, priority SLAs, and seamless connectors for SAP, Oracle ERP, Microsoft Dynamics, and CargoWise.",
        "mock_title": "Enterprise Deployment",
        "mock_fields": [
            ("Deployment", "Dedicated Cloud / On-Premise"),
            ("Compliance", "SOC 2 & ISO Aligned Architecture"),
            ("Custom ERP", "SAP S/4HANA & Oracle ERP Cloud"),
            ("Support SLA", "Dedicated Account Manager & 24/7 SLA")
        ],
        "stats": [
            ("99.9%", "Platform uptime SLA"),
            ("High-Volume", "Tens of thousands of docs/month"),
            ("Custom", "Tailored approval workflows"),
            ("Priority", "Dedicated technical onboarding")
        ],
        "features": [
            ("Custom ERP & TMS Integrations", "Dedicated engineering support to connect your on-premise or cloud SAP, Oracle, or CargoWise setup."),
            ("High-Volume Batch Processing", "Process tens of thousands of complex documents monthly with scalable compute clusters."),
            ("Dedicated Onboarding & Training", "Assigned implementation specialist to train teams and configure tailored validation rules.")
        ]
    })

    # Partners
    build_route_page({
        "rel_path": "partners/index.html",
        "canonical": "/partners",
        "title": "Docsynecx Partner Program | SynecxAI Labs",
        "description": "Partner with Docsynecx. Technology integrations, ERP implementation partners, and referral opportunities for consultants.",
        "eyebrow": "Partner Ecosystem",
        "h1": "Work With Us to Automate Document Workflows",
        "lead": "Join our ecosystem of technology partners, ERP consultants, and implementation specialists bringing document automation to modern businesses.",
        "mock_title": "Partner Network",
        "mock_fields": [
            ("Partner Tracks", "Technology, Implementation, Referral"),
            ("Supported ERPs", "Tally, Zoho, CargoWise, SAP"),
            ("Benefits", "Revenue Share, Co-Marketing, API Support")
        ],
        "features": [
            ("Technology Partners", "ERP, TMS, and accounting software vendors building native bidirectional integrations."),
            ("Implementation Partners", "Consultants and CA firms deploying tailored document intelligence for enterprise clients."),
            ("Referral Partners", "Earn recurring commission by introducing businesses that need invoice and logistics automation.")
        ]
    })

    # Compatibility route /company/partners
    build_route_page({
        "rel_path": "company/partners/index.html",
        "canonical": "/company/partners",
        "title": "Partner Program | Docsynecx",
        "description": "Work with us to bring document automation to more teams.",
        "eyebrow": "Partner Ecosystem",
        "h1": "Docsynecx Partner Program",
        "lead": "Work with us to bring document automation to more teams across finance and logistics.",
        "mock_title": "Partner Ecosystem",
        "mock_fields": [("Track", "Technology & Referral"), ("Status", "Open")],
        "features": [
            ("Technology Partners", "ERP and TMS integration builders."),
            ("Implementation Partners", "Consulting partners deploying automation."),
            ("Referral Partners", "Introduce teams needing automation.")
        ]
    })

    # Careers
    build_route_page({
        "rel_path": "company/careers/index.html",
        "canonical": "/company/careers",
        "title": "Careers at Docsynecx | SynecxAI Labs",
        "description": "Join the team building state-of-the-art AI document processing and automation for finance and logistics.",
        "eyebrow": "Join Our Team",
        "h1": "Careers at SynecxAI Labs",
        "lead": "Join the team building AI document automation for modern finance and global logistics. Help eliminate busywork worldwide.",
        "mock_title": "SynecxAI Engineering & Product",
        "mock_fields": [
            ("Location", "Bengaluru, India / Hybrid"),
            ("Focus", "AI Document Intelligence & Distributed Systems"),
            ("Open Positions", "Engineering, Product, Customer Success")
        ],
        "features": [
            ("Engineering & AI Research", "Build cutting-edge document parsing, neural extraction, and ERP synchronization pipelines."),
            ("Customer Success & Solutions", "Help modern finance teams and freight forwarders transform their everyday workflows."),
            ("Culture of Craftsmanship", "High ownership, fast-paced shipping, and direct impact on real-world enterprise operations.")
        ]
    })

    # Contact Us
    build_route_page({
        "rel_path": "contact/index.html",
        "canonical": "/contact",
        "title": "Contact Docsynecx | Get in Touch",
        "description": "Contact the Docsynecx team for sales inquiries, custom integrations, partnership discussions, or support.",
        "eyebrow": "Get in Touch",
        "h1": "Contact the Docsynecx Team",
        "lead": "Have questions about our platform, need a tailored integration, or want to schedule an enterprise demo? We are here to help.",
        "mock_title": "Direct Contact Channel",
        "mock_fields": [
            ("Sales & Partnerships", "sales@docsynecx.com"),
            ("Technical Support", "support@docsynecx.com"),
            ("Headquarters", "SynecxAI Labs Private Limited")
        ],
        "features": [
            ("Custom Demonstrations", "See Docsynecx process your real business documents live in a dedicated session."),
            ("Integration Consultation", "Discuss tailored connectors for your Tally, Zoho, CargoWise, SAP, or proprietary TMS setup."),
            ("Enterprise Procurement", "Inquire about high-volume tier pricing, custom SLAs, and security compliance agreements.")
        ]
    })

    # Request Demo
    build_route_page({
        "rel_path": "request-demo/index.html",
        "canonical": "/request-demo",
        "title": "Book a Demo | Docsynecx Document Automation",
        "description": "Schedule a personalized 30-minute demonstration of Docsynecx processing your invoices or logistics documents live.",
        "eyebrow": "Schedule Walkthrough",
        "h1": "Experience Docsynecx on Your Real Documents",
        "lead": "Schedule a personalized 30-minute session to see how AI document automation accelerates your finance and logistics operations.",
        "mock_title": "Demo Booking Schedule",
        "mock_fields": [
            ("Duration", "30 Minutes"),
            ("Demonstration", "Live Document Processing with Your Sample Files"),
            ("Q&A", "Integration Architecture with Your ERP/TMS")
        ],
        "features": [
            ("Interactive Walkthrough", "See how our AI captures, validates, and syncs invoices and freight documents in real time."),
            ("Custom ROI Assessment", "Receive a tailored estimate of hours and operational costs your team will save every month."),
            ("Zero Commitment", "Test with your real files in days without any obligation or upfront cost.")
        ]
    })

    # =========================================================================
    # 8. PRICING ROUTE
    # =========================================================================
    head_p = render_head(
        title="AP Automation Software Pricing Plans | Docsynecx",
        description="Simple, transparent pricing for business automation. Start with a free trial. Starter, Professional, and Enterprise plans.",
        keywords="AP Automation pricing, document automation plans, Tally invoice automation pricing",
        current_path="/pricing"
    )
    nav_p = render_navbar("/pricing")
    footer_p = render_footer("/pricing")
    pricing_page = f"""{head_p}
{nav_p}

<header class="rhero">
  <div class="w">
    <div class="stepl">Transparent Pricing</div>
    <h1>Simple, Transparent Pricing for Business Automation</h1>
    <p class="lead">Automate invoice processing, eliminate manual data entry, and integrate seamlessly with your accounting systems. Start with a free trial. Upgrade when you see the value.</p>
    <div class="cta">
      <a class="btn p" href="../request-demo/index.html">Start 7-Day Free Trial</a>
      <a class="btn" href="#plans">Compare Plans</a>
    </div>
  </div>
</header>

<section id="plans">
  <div class="w">
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
      <div class="card" style="padding:32px;display:flex;flex-direction:column">
        <span class="eyebrow" style="align-self:flex-start">Starter</span>
        <h3 style="font-size:24px;margin:8px 0">Try real automation</h3>
        <p style="color:var(--mut);font-size:15px;margin-bottom:24px">Perfect for small teams testing invoice extraction on live data.</p>
        <div style="margin-bottom:24px"><b style="font:600 40px Fraunces,serif;color:var(--deep)">Free Trial</b><span style="color:var(--mut);font-size:14px"> · 20 credits</span></div>
        <ul style="list-style:none;padding:0;margin:0 0 24px;line-height:2;font-size:14.5px;color:var(--ink);flex:1">
          <li>✓ 20 free document credits</li>
          <li>✓ Invoice data extraction</li>
          <li>✓ GST & basic arithmetic validation</li>
          <li>✓ Limited Tally integration</li>
          <li>✓ 1 company · 1 user seat</li>
        </ul>
        <a class="btn" href="../request-demo/index.html" style="width:100%">Start Free Trial</a>
      </div>

      <div class="card" style="padding:32px;border:2px solid var(--deep);box-shadow:0 24px 60px -20px rgba(15,61,46,.35);display:flex;flex-direction:column">
        <span class="eyebrow" style="align-self:flex-start;background:var(--acc)">Professional</span>
        <h3 style="font-size:24px;margin:8px 0">Growing Businesses</h3>
        <p style="color:var(--mut);font-size:15px;margin-bottom:24px">For scaling operations needing high throughput and full Tally sync.</p>
        <div style="margin-bottom:24px"><b style="font:600 40px Fraunces,serif;color:var(--deep)">Standard</b><span style="color:var(--mut);font-size:14px"> · Bulk Processing</span></div>
        <ul style="list-style:none;padding:0;margin:0 0 24px;line-height:2;font-size:14.5px;color:var(--ink);flex:1">
          <li>✓ Everything in Starter</li>
          <li>✓ Bulk invoice batch processing</li>
          <li>✓ Multi-line item table extraction</li>
          <li>✓ Advanced validation & duplicate checks</li>
          <li>✓ Full TallyPrime integration & ledger sync</li>
          <li>✓ Multi-company & multi-user support</li>
        </ul>
        <a class="btn p" href="../request-demo/index.html" style="width:100%">Choose Professional</a>
      </div>

      <div class="card" style="padding:32px;display:flex;flex-direction:column">
        <span class="eyebrow" style="align-self:flex-start">Enterprise</span>
        <h3 style="font-size:24px;margin:8px 0">Large-Scale Operations</h3>
        <p style="color:var(--mut);font-size:15px;margin-bottom:24px">Custom workflows, CargoWise sync, and dedicated SLAs.</p>
        <div style="margin-bottom:24px"><b style="font:600 40px Fraunces,serif;color:var(--deep)">Custom</b><span style="color:var(--mut);font-size:14px"> · Tailored Volume</span></div>
        <ul style="list-style:none;padding:0;margin:0 0 24px;line-height:2;font-size:14.5px;color:var(--ink);flex:1">
          <li>✓ Everything in Professional</li>
          <li>✓ Custom approval routing & workflows</li>
          <li>✓ Logistics module (CargoWise One sync)</li>
          <li>✓ Custom ERP connectors (SAP, Oracle)</li>
          <li>✓ Dedicated implementation & priority SLA</li>
          <li>✓ SOC 2 & enterprise compliance alignment</li>
        </ul>
        <a class="btn" href="../contact/index.html" style="width:100%">Contact Enterprise Sales</a>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <div class="w">
    <div class="sechd">
      <span class="eyebrow">Enterprise Add-ons</span>
      <h2>Advanced Automation Modules</h2>
      <p class="lead">Available exclusively under Enterprise plans tailored to your volume.</p>
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">
      <div class="card" style="padding:28px">
        <span class="chip" style="margin-bottom:12px;display:inline-block">Module 1</span>
        <h3>Logistics & Supply Chain</h3>
        <p style="color:var(--mut);margin-bottom:16px">CargoWise-ready document automation for Bills of Lading, AWBs, packing lists, and customs entries.</p>
        <ul style="list-style:none;padding:0;line-height:1.8;font-size:14px;color:var(--ink)">
          <li>✓ High-volume multi-container manifest extraction</li>
          <li>✓ Direct eAdaptor sync to CargoWise One jobs</li>
          <li>✓ Freight invoice reconciliation and rate auditing</li>
        </ul>
      </div>
      <div class="card" style="padding:28px">
        <span class="chip" style="margin-bottom:12px;display:inline-block">Module 2</span>
        <h3>Workflows & Approvals</h3>
        <p style="color:var(--mut);margin-bottom:16px">Multi-tier conditional governance and automated routing rules for complex organizations.</p>
        <ul style="list-style:none;padding:0;line-height:1.8;font-size:14px;color:var(--ink)">
          <li>✓ Role-based access and department-level hierarchies</li>
          <li>✓ Amount thresholds and automatic exception escalations</li>
          <li>✓ Complete immutable audit logging for all decisions</li>
        </ul>
      </div>
    </div>
  </div>
</section>

{footer_p}
{SHARED_SCRIPT}"""
    save_page("pricing/index.html", pricing_page)

    # =========================================================================
    # 9. LEGAL PAGES (Privacy Policy, Terms of Service)
    # =========================================================================
    
    # Privacy Policy
    head_priv = render_head(
        title="Privacy Policy | Docsynecx",
        description="Docsynecx Privacy Policy - How SynecxAI Labs Private Limited collects, uses, and protects your information.",
        keywords="privacy policy, data security, docsynecx privacy",
        current_path="/privacy-policy"
    )
    priv_page = f"""{head_priv}
{render_navbar("/privacy-policy")}
<div class="w" style="padding:72px 24px;max-width:880px">
  <span class="eyebrow">Legal</span>
  <h1>Privacy Policy</h1>
  <p class="fine" style="margin-bottom:32px">Last updated: October 2026 · SynecxAI Labs Private Limited</p>
  
  <h2>1. Information We Collect</h2>
  <p>Docsynecx collects information necessary to provide our intelligent document processing services, including account credentials, business billing information, and document content submitted for extraction.</p>
  
  <h2>2. How We Use Document Data</h2>
  <p>Documents uploaded to Docsynecx are processed exclusively for data extraction, validation, and synchronization to your designated ERP or TMS systems. We do not sell or share customer document data with third parties.</p>

  <h2>3. Data Protection & Security</h2>
  <p>All data is encrypted in transit using industry-standard TLS encryption and encrypted at rest. We implement strict role-based access control and isolation between customer workspaces.</p>

  <h2>4. Contact Us</h2>
  <p>For privacy inquiries, please contact our Data Protection Officer at privacy@docsynecx.com.</p>
</div>
{render_footer("/privacy-policy")}
{SHARED_SCRIPT}"""
    save_page("privacy-policy/index.html", priv_page)

    # Terms of Service
    head_tos = render_head(
        title="Terms of Service | Docsynecx",
        description="Terms of Service governing the use of the Docsynecx AI document automation platform.",
        keywords="terms of service, legal agreement, docsynecx terms",
        current_path="/terms-of-service"
    )
    tos_page = f"""{head_tos}
{render_navbar("/terms-of-service")}
<div class="w" style="padding:72px 24px;max-width:880px">
  <span class="eyebrow">Legal</span>
  <h1>Terms of Service</h1>
  <p class="fine" style="margin-bottom:32px">Last updated: October 2026 · SynecxAI Labs Private Limited</p>
  
  <h2>1. Service Agreement</h2>
  <p>By accessing or using Docsynecx, you agree to be bound by these Terms of Service. Docsynecx provides intelligent document extraction, validation rules, and system integration services.</p>

  <h2>2. Subscription & Usage</h2>
  <p>Services are provided based on selected subscription tiers (Starter, Professional, Enterprise). Usage is governed by credit allocations, user seat counts, and associated fair-use policies.</p>

  <h2>3. Service Availability & Support</h2>
  <p>Docsynecx strives for high availability with an uptime target of 99.9%. Scheduled maintenance will be communicated in advance.</p>

  <h2>4. Governing Law</h2>
  <p>These terms are governed by the laws of India. Any disputes will be subject to the exclusive jurisdiction of the courts in Bengaluru, India.</p>
</div>
{render_footer("/terms-of-service")}
{SHARED_SCRIPT}"""
    save_page("terms-of-service/index.html", tos_page)

    # =========================================================================
    # 10. STYLED 404 PAGE
    # =========================================================================
    head_404 = render_head(
        title="404 Page Not Found | Docsynecx",
        description="The page you were looking for does not exist on Docsynecx.",
        keywords="",
        current_path="/"
    )
    page_404 = f"""{head_404}
{render_navbar("/")}
<header class="rhero" style="padding:100px 0 80px">
  <div class="w">
    <div class="stepl" style="color:var(--warn)">Error 404</div>
    <h1 style="font-size:clamp(44px,6vw,72px)">Page Not Found</h1>
    <p class="lead" style="margin-top:16px">The page you are looking for may have been moved, renamed, or is temporarily unavailable.</p>
    <div class="cta" style="margin-top:32px">
      <a class="btn p" href="index.html">Return to Home</a>
      <a class="btn" href="contact/index.html">Contact Support</a>
    </div>
  </div>
</header>
{render_footer("/")}
{SHARED_SCRIPT}"""
    save_page("404.html", page_404)

    # =========================================================================
    # 11. SITEMAP.XML & ROBOTS.TXT
    # =========================================================================
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://docsynecx.com/</loc><priority>1.0</priority></url>
  <url><loc>https://docsynecx.com/invoice-processing</loc><priority>0.9</priority></url>
  <url><loc>https://docsynecx.com/logistics-trade</loc><priority>0.9</priority></url>
  <url><loc>https://docsynecx.com/workflows</loc><priority>0.9</priority></url>
  <url><loc>https://docsynecx.com/logistics-trade/shipments</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/logistics-trade/custom-declarations</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/logistics-trade/ap-reconciliation</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/integration/invoice-to-tally</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/integration/zoho-books</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/integration/cargowise</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/solutions</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/solutions/banking</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/solutions/finance</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/solutions/logistics</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/solutions/accounts-payable</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/pricing</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/blog</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/help</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/about</loc><priority>0.6</priority></url>
  <url><loc>https://docsynecx.com/enterprise</loc><priority>0.8</priority></url>
  <url><loc>https://docsynecx.com/partners</loc><priority>0.6</priority></url>
  <url><loc>https://docsynecx.com/contact</loc><priority>0.6</priority></url>
  <url><loc>https://docsynecx.com/request-demo</loc><priority>0.7</priority></url>
  <url><loc>https://docsynecx.com/privacy-policy</loc><priority>0.3</priority></url>
  <url><loc>https://docsynecx.com/terms-of-service</loc><priority>0.3</priority></url>
</urlset>"""
    save_page("sitemap.xml", sitemap_xml)

    robots_txt = """User-agent: *
Allow: /

Sitemap: https://docsynecx.com/sitemap.xml"""
    save_page("robots.txt", robots_txt)

    print("All pages and SEO assets generated successfully!")

if __name__ == "__main__":
    main()
