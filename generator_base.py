"""
Docsynecx Static Site Generator
Builds the landing page and all route pages according to the approved route template,
using the landing page navbar and tokens.css design system.
"""

import json
from pathlib import Path

# Paths
DATA_FILE = Path("data/docsynecx-content.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    RAW_DATA = json.load(f)

# Navigation HTML Component (Landing Style for All Pages)
def get_pfx(current_path="/"):
    cleaned = current_path.strip("/")
    if not cleaned:
        return ""
    # Each segment in cleaned represents a subfolder level (since each route is folder/index.html)
    parts = cleaned.split("/")
    return "../" * len(parts)

def render_navbar(current_path="/"):
    pfx = get_pfx(current_path)

    def is_curr(p):
        return ' aria-current="page"' if current_path == p else ""

    return f"""<nav>
  <div class="w">
    <a class="logo" href="{pfx}index.html"><img src="{pfx}images/logo.svg" alt="Docsynecx" class="logo-img" width="130" height="38"></a>
    <div class="nav-links" id="menu">
      <div class="dd">
        <button type="button" aria-expanded="false" aria-haspopup="true">Products</button>
        <div class="panel">
          <div>
            <a href="{pfx}invoice-processing/index.html">Invoice automation<span class="sub">Extract, validate & post invoices</span></a>
            <a href="{pfx}logistics-trade/index.html">Logistics and supply chain<span class="sub">Process BOLs, packing lists & customs</span></a>
            <a href="{pfx}workflows/index.html">Workflow and approvals<span class="sub">Multi-level approvals & business rules</span></a>
          </div>
          <div>
            <span class="ph">Integrations &#9656;</span>
            <a href="{pfx}integration/invoice-to-tally/index.html">TallyPrime<span class="sub">Direct ledger & voucher posting</span></a>
            <a href="{pfx}integration/zoho-books/index.html">Zoho Books<span class="sub">Automated bills & line items</span></a>
            <a href="{pfx}integration/cargowise/index.html">CargoWise<span class="sub">Shipments & customs eAdaptor</span></a>
          </div>
        </div>
      </div>
      <div class="dd">
        <button type="button" aria-expanded="false" aria-haspopup="true">Solutions</button>
        <div class="panel">
          <div>
            <span class="ph">By Industry</span>
            <a href="{pfx}solutions/banking/index.html">Banking & Finance<span class="sub">Statements, KYC & loan documents</span></a>
            <a href="{pfx}solutions/logistics/index.html">Logistics & Supply Chain<span class="sub">Air waybills, sea freight & manifests</span></a>
          </div>
          <div>
            <span class="ph">Use Cases</span>
            <a href="{pfx}solutions/accounts-payable/index.html">Accounts Payable<span class="sub">2-way/3-way matching & GST validation</span></a>
            <a href="{pfx}solutions/index.html">All Solutions<span class="sub">Browse full IDP capabilities</span></a>
          </div>
        </div>
      </div>
      <div class="dd">
        <button type="button" aria-expanded="false" aria-haspopup="true">Resources</button>
        <div class="panel">
          <div>
            <span class="ph">Learn</span>
            <a href="{pfx}blog/index.html">Blog & Guides<span class="sub">IDP best practices & automation tips</span></a>
            <a href="{pfx}help/index.html">Support Docs & FAQ<span class="sub">Setup guides & platform help</span></a>
          </div>
          <div>
            <span class="ph">Company</span>
            <a href="{pfx}about/index.html">About us<span class="sub">SynecxAI Labs mission & team</span></a>
            <a href="{pfx}enterprise/index.html">Enterprise<span class="sub">High-volume SLAs & compliance</span></a>
            <a href="{pfx}partners/index.html">Partner Program<span class="sub">ERP & implementation partners</span></a>
          </div>
        </div>
      </div>
      <a href="{pfx}pricing/index.html"{is_curr("/pricing")}>Pricing</a>
    </div>
    <div class="nav-cta">
      <a class="login-link" href="https://invoice.docsynecx.com/">Login</a>
      <a class="demo-pill" href="{pfx}request-demo/index.html">Book Demo</a>
      <button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation menu">&#9776;</button>
    </div>
  </div>
</nav>"""

# Footer HTML Component
def render_footer(current_path="/"):
    pfx = get_pfx(current_path)

    return f"""<footer>
  <div class="w">
    <div class="g">
      <div>
        <a class="logo" href="{pfx}index.html"><img src="{pfx}images/logo.svg" alt="Docsynecx" class="logo-img" width="143" height="42"></a>
        <p style="margin-top:12px;max-width:320px;line-height:1.5">The AI-powered document automation platform for intelligent processing, data extraction and business workflows.</p>
        <div class="mail" style="margin-top:18px">
          <input type="email" aria-label="Your work email" placeholder="Your work email">
          <a class="btn p" href="{pfx}request-demo/index.html">Book a demo</a>
        </div>
      </div>
      <div>
        <b>Products</b>
        <a href="{pfx}invoice-processing/index.html">Invoice Automation</a>
        <a href="{pfx}logistics-trade/index.html">Logistics & Supply Chain</a>
        <a href="{pfx}workflows/index.html">Workflows & Approvals</a>
        <a href="{pfx}logistics-trade/shipments/index.html">Shipments Automation</a>
        <a href="{pfx}logistics-trade/custom-declarations/index.html">Customs Declarations</a>
      </div>
      <div>
        <b>Integrations</b>
        <a href="{pfx}integration/invoice-to-tally/index.html">TallyPrime</a>
        <a href="{pfx}integration/zoho-books/index.html">Zoho Books</a>
        <a href="{pfx}integration/cargowise/index.html">CargoWise</a>
        <a href="{pfx}enterprise/index.html">SAP & Enterprise ERP</a>
      </div>
      <div>
        <b>Solutions</b>
        <a href="{pfx}solutions/accounts-payable/index.html">Accounts Payable</a>
        <a href="{pfx}solutions/logistics/index.html">Logistics</a>
        <a href="{pfx}solutions/banking/index.html">Banking & Finance</a>
        <a href="{pfx}pricing/index.html">Pricing Plans</a>
      </div>
      <div>
        <b>Company</b>
        <a href="{pfx}about/index.html">About Us</a>
        <a href="{pfx}blog/index.html">Blog</a>
        <a href="{pfx}partners/index.html">Partners</a>
        <a href="{pfx}contact/index.html">Contact Us</a>
        <a href="{pfx}help/index.html">Help & FAQs</a>
      </div>
    </div>
    <div class="copy" style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:12px">
      <div>&copy; 2026 SynecxAI Labs Private Limited. All rights reserved.</div>
      <div style="display:flex;gap:18px">
        <a href="{pfx}privacy-policy/index.html">Privacy Policy</a>
        <a href="{pfx}terms-of-service/index.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>"""

# Shared Head Template
def render_head(title, description, keywords, current_path="/"):
    pfx = get_pfx(current_path)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  {f'<meta name="keywords" content="{keywords}">' if keywords else ''}
  <link rel="canonical" href="https://docsynecx.com{current_path}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:wght@500;600&family=Inter:wght@400;500;600&display=swap">
  <link rel="icon" type="image/png" href="{pfx}images/favicon.png">
  <link rel="stylesheet" href="{pfx}css/tokens.css">
</head>
<body>"""

# Shared Footer Script for interactive elements (dropdowns, mobile toggle)
SHARED_SCRIPT = """<script>
(function() {
  var dds = document.querySelectorAll(".dd");
  function closeAll() {
    dds.forEach(function(d) {
      d.classList.remove("open");
      var btn = d.querySelector("button");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  }
  dds.forEach(function(d) {
    var b = d.querySelector("button");
    if (!b) return;
    b.addEventListener("click", function(e) {
      e.stopPropagation();
      var o = d.classList.contains("open");
      closeAll();
      if (!o) {
        d.classList.add("open");
        b.setAttribute("aria-expanded", "true");
      }
    });
  });
  document.addEventListener("click", closeAll);
  document.addEventListener("keydown", function(e) {
    if (e.key === "Escape") closeAll();
  });

  // Mobile menu toggle
  var mt = document.getElementById("menuToggle");
  var mn = document.getElementById("menu");
  if (mt && mn) {
    mt.addEventListener("click", function(e) {
      e.stopPropagation();
      var isOpen = mn.style.display === "flex";
      mn.style.display = isOpen ? "none" : "flex";
      mn.style.flexDirection = "column";
      mn.style.position = "absolute";
      mn.style.top = "68px";
      mn.style.left = "0";
      mn.style.width = "100%";
      mn.style.background = "var(--surf)";
      mn.style.padding = "20px";
      mn.style.borderBottom = "1px solid var(--line)";
      mn.style.boxShadow = "0 10px 30px rgba(0,0,0,0.1)";
    });
  }
})();
</script>
</body>
</html>"""

print("Generator module components loaded.")
