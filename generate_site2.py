"""
generate_site2.py - Static Site Generator for Docsynecx UI 2
Generates:
- Root landing page: /index2.html
- All UI 2 route pages in /ui2/
- Full separation from UI 1 (Zero collision, clean URLs, live teal color theme)
"""

import os
import re
import json

def get_pfx(rel_path):
    """Computes relative prefix '../' from file depth to project root."""
    depth = rel_path.count('/')
    return '../' * depth if depth > 0 else ''

def save_file(rel_path, content):
    """Writes content to rel_path, creating directories if needed."""
    full_path = os.path.join(os.getcwd(), rel_path.replace('/', os.sep))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {rel_path}")

# =============================================================================
# SHARED LAYOUT: HEAD, NAVBAR, FOOTER
# =============================================================================

def render_head(title, description, canonical_path, pfx):
    return f"""<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="https://docsynecx.com/{canonical_path}">
  
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://docsynecx.com/{canonical_path}">
  <meta property="og:site_name" content="Docsynecx">
  <meta property="og:image" content="https://docsynecx.com/assets2/logo.svg">
  <meta name="twitter:card" content="summary_large_image">
  
  <link rel="icon" type="image/x-icon" href="{pfx}favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap">
  
  <link rel="stylesheet" href="{pfx}assets2/tokens.css">
</head>"""

def render_navbar(pfx, is_route=False, active_path=""):
    rn_class = " rn" if is_route else ""
    route_cta = f'<a class="b k" href="{pfx}ui2/request-demo/">Book Demo</a>' if is_route else f'<a class="b p sm" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>'
    platform_link = f'<div class="mi"><a href="{pfx}ui2/solutions/">Platform</a></div>' if is_route else ''

    return f"""<header class="nv{rn_class}">
  <div class="w">
    <a class="logo" href="{pfx}index2.html" aria-label="Docsynecx Home">
      <img src="{pfx}assets2/logo.svg" alt="Docsynecx" class="logo-img" width="120" height="34">
    </a>
    
    <nav class="mn" aria-label="Main Navigation">
      {platform_link}
      <div class="mi d">
        <button type="button" class="nav-btn" aria-expanded="false" aria-haspopup="true">Products</button>
        <div class="pn p1" role="region" aria-label="Product Dropdown">
          <div class="pg">
            <div>
              <h4>Document automation</h4>
              <a class="en" href="{pfx}ui2/invoice-processing/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span>
                <span><b>Invoice automation</b><span class="d">Extract, validate and sync invoice data.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/logistics-trade/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3z M14 10h4l3 3v3h-7 M7 19h.01 M17 19h.01"/></svg></span>
                <span><b>Logistics and supply chain</b><span class="d">Turn shipment files into operational data.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/workflows/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h5v5H5z M14 14h5v5h-5z M10 8h4a2 2 0 0 1 2 2v4"/></svg></span>
                <span><b>Workflow and approvals</b><span class="d">Route, approve and track every document.</span></span>
              </a>
            </div>
            <div>
              <h4>Integrations</h4>
              <a class="en" href="{pfx}ui2/integration/invoice-to-tally/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18H6z M9 7h6 M9 11h2 M13 11h2 M9 15h2 M13 15h2"/></svg></span>
                <span><b>Tally</b><span class="d">Connect invoices to TallyPrime.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/integration/zoho-books/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v14 M12 6C10 4.5 7 4 4 4v14c3 0 6 .5 8 2 2-1.5 5-2 8-2V4c-3 0-6 .5-8 2z"/></svg></span>
                <span><b>Zoho Books</b><span class="d">Keep your accounting workflow moving.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/integration/cargowise/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z M12 12l8-4.5 M12 12v9 M12 12L4 7.5"/></svg></span>
                <span><b>CargoWise</b><span class="d">Sync clean data into your TMS.</span></span>
              </a>
            </div>
          </div>
          <div class="cs">
            <span>Discover what document intelligence can do for your team.</span>
            <a href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
          </div>
        </div>
      </div>

      <div class="mi d">
        <button type="button" class="nav-btn" aria-expanded="false" aria-haspopup="true">Solutions</button>
        <div class="pn p2" role="region" aria-label="Solutions Dropdown">
          <div class="pg">
            <div>
              <h4>By industry</h4>
              <a class="en" href="{pfx}ui2/solutions/banking/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10l9-6 9 6 M5 10v8 M9 10v8 M15 10v8 M19 10v8 M3 20h18"/></svg></span>
                <span><b>Banking</b><span class="d">Document intelligence for banking teams.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/solutions/finance/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V4 M4 20h16 M8 16v-4 M12 16V8 M16 16v-6"/></svg></span>
                <span><b>Finance</b><span class="d">Less document handling. More visibility.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/solutions/logistics/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3z M14 10h4l3 3v3h-7 M7 19h.01 M17 19h.01"/></svg></span>
                <span><b>Logistics</b><span class="d">Connect documents with operations.</span></span>
              </a>
            </div>
            <div>
              <h4>By use case</h4>
              <a class="en" href="{pfx}ui2/solutions/accounts-payable/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span>
                <span><b>Accounts payable</b><span class="d">From invoice capture to ERP sync.</span></span>
              </a>
            </div>
          </div>
          <div class="cs">
            <span>Discover what document intelligence can do for your team.</span>
            <a href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
          </div>
        </div>
      </div>

      <div class="mi">
        <a href="{pfx}ui2/pricing/">Pricing</a>
      </div>

      <div class="mi d res-mi">
        <button type="button" class="nav-btn" aria-expanded="false" aria-haspopup="true">Resources</button>
        <div class="pn p3" role="region" aria-label="Resources Dropdown">
          <div class="pg">
            <div>
              <h4>Learn</h4>
              <a class="en" href="{pfx}ui2/blog/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span>
                <span><b>Blog</b><span class="d">Ideas for smarter document workflows.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/help/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v14 M12 6C10 4.5 7 4 4 4v14c3 0 6 .5 8 2 2-1.5 5-2 8-2V4c-3 0-6 .5-8 2z"/></svg></span>
                <span><b>Support docs</b><span class="d">Guides to get your workflow running.</span></span>
              </a>
            </div>
            <div>
              <h4>Company</h4>
              <a class="en" href="{pfx}ui2/about/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 21V4h9v17 M14 9h5v12 M8 8h3 M8 12h3 M8 16h3"/></svg></span>
                <span><b>About us</b><span class="d">Get to know docsynecx.</span></span>
              </a>
              <a class="en" href="{pfx}ui2/partners/">
                <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 12l4-4 4 2 4-2 6 5-4 5-4-1-3 2-7-6z"/></svg></span>
                <span><b>Partner company</b><span class="d">Build better workflows together.</span></span>
              </a>
            </div>
          </div>
          <div class="cs">
            <span>Discover what document intelligence can do for your team.</span>
            <a href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
          </div>
        </div>
      </div>
    </nav>

    <div class="lg2">
      <a href="https://invoice.docsynecx.com/signin/">Log in</a>
      {route_cta}
    </div>

    <button type="button" class="mob-btn" aria-label="Toggle navigation menu" aria-expanded="false">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="3" y1="12" x2="21" y2="12"></line>
        <line x1="3" y1="6" x2="21" y2="6"></line>
        <line x1="3" y1="18" x2="21" y2="18"></line>
      </svg>
    </button>
  </div>
</header>

<div class="mob-drawer" role="dialog" aria-modal="true" aria-label="Mobile Navigation">
  <div class="mob-links">
    <details class="mob-group">
      <summary>Product</summary>
      <div class="mob-sublinks">
        <a href="{pfx}ui2/invoice-processing/">Invoice automation</a>
        <a href="{pfx}ui2/logistics-trade/">Logistics and supply chain</a>
        <a href="{pfx}ui2/workflows/">Workflow and approvals</a>
        <a href="{pfx}ui2/integration/invoice-to-tally/">Tally Integration</a>
        <a href="{pfx}ui2/integration/zoho-books/">Zoho Books Integration</a>
        <a href="{pfx}ui2/integration/cargowise/">CargoWise Integration</a>
      </div>
    </details>

    <details class="mob-group">
      <summary>Solutions</summary>
      <div class="mob-sublinks">
        <a href="{pfx}ui2/solutions/banking/">Banking</a>
        <a href="{pfx}ui2/solutions/finance/">Finance</a>
        <a href="{pfx}ui2/solutions/logistics/">Logistics</a>
        <a href="{pfx}ui2/solutions/accounts-payable/">Accounts payable</a>
      </div>
    </details>

    <a class="mob-link" href="{pfx}ui2/pricing/">Pricing</a>

    <details class="mob-group">
      <summary>Resources</summary>
      <div class="mob-sublinks">
        <a href="{pfx}ui2/blog/">Blog</a>
        <a href="{pfx}ui2/help/">Support docs</a>
        <a href="{pfx}ui2/about/">About us</a>
        <a href="{pfx}ui2/partners/">Partner company</a>
      </div>
    </details>

    <div style="margin-top:20px;display:flex;flex-direction:column;gap:12px">
      <a class="b o" href="https://invoice.docsynecx.com/signin/" style="justify-content:center">Log in</a>
      <a class="b p" href="{pfx}ui2/request-demo/" style="justify-content:center">Book a demo &rarr;</a>
    </div>
  </div>
</div>"""

def render_footer(pfx):
    return f"""<footer class="ft">
  <div class="w">
    <div class="gr">
      <div>
        <span class="lgb">
          <a class="logo" href="{pfx}index2.html" aria-label="Docsynecx Home">
            <img src="{pfx}assets2/logo.svg" alt="Docsynecx" class="logo-img" width="130" height="38">
          </a>
        </span>
        <p>The AI-Powered Document Automation Platform for Intelligent Processing, Data Extraction, and Business Workflows</p>
      </div>

      <div>
        <h5>Products</h5>
        <a href="{pfx}ui2/invoice-processing/">Invoice automation</a>
        <a href="{pfx}ui2/logistics-trade/">Logistics and supply chain</a>
        <a href="{pfx}ui2/workflows/">Workflow and approvals</a>
        <a href="{pfx}ui2/solutions/">Platform</a>
      </div>

      <div>
        <h5>Solutions</h5>
        <a href="{pfx}ui2/solutions/banking/">Banking</a>
        <a href="{pfx}ui2/solutions/finance/">Finance</a>
        <a href="{pfx}ui2/solutions/logistics/">Logistics</a>
        <a href="{pfx}ui2/solutions/accounts-payable/">Accounts payable</a>
      </div>

      <div>
        <h5>Resources</h5>
        <a href="{pfx}ui2/blog/">Blog</a>
        <a href="{pfx}ui2/help/">Support docs</a>
        <a href="{pfx}ui2/pricing/">Pricing</a>
      </div>

      <div>
        <h5>Company</h5>
        <a href="{pfx}ui2/about/">About us</a>
        <a href="{pfx}ui2/partners/">Partner company</a>
        <a href="{pfx}ui2/contact/">Contact</a>
      </div>
    </div>

    <div class="bt">
      <span>&copy; 2026 SynecxAI Labs Private Limited. All rights reserved.</span>
      <span>
        <a href="{pfx}ui2/privacy-policy/">Privacy Policy</a>
        <a href="{pfx}ui2/terms-of-service/">Terms of Service</a>
      </span>
    </div>
  </div>
</footer>
<script src="{pfx}assets2/site.js"></script>"""

# =============================================================================
# ROUTE-PAGE TEMPLATE RENDERER (Approved Docsynecx___Invoice_automation Structure)
# =============================================================================

def render_route_page(cfg, pfx):
    head = render_head(cfg["title"], cfg["description"], f"ui2/{cfg['slug']}/", pfx)
    nav = render_navbar(pfx, is_route=True, active_path=cfg["slug"])
    foot = render_footer(pfx)

    # Mock doc items
    doc_fields_html = "".join([
        f'<div class="fr" style="padding:9px 0;border-bottom:1px solid var(--line)"><span><small>{f["label"]}</small><b>{f["val"]}</b></span><span class="tk">&#10003;</span></div>'
        for f in cfg["mock_extract"]
    ])

    # Steps HTML
    steps_html = []
    for i, s in enumerate(cfg["steps"]):
        rev = " rev" if i % 2 == 1 else ""
        rows_html = "".join([
            f'<div class="mr"><small>{r["top"]}</small><b>{r["bot"]}</b><i class="{"o" if r.get("warn") else ""}">{"&#9675;" if r.get("warn") else "&#10003;"}</i></div>'
            for r in s["rows"]
        ])
        w2 = " w2" if s.get("is_warn") else ""
        icon = "&#9675;" if s.get("is_warn") else "&#10003;"

        step_chunk = f"""<div class="st{rev}">
  <div class="tx">
    <span class="n">{s["num"]}</span>
    <h3>{s["title"]}</h3>
    <p>{s["desc"]}</p>
    <div class="tgs">{s["tags"]}</div>
  </div>
  <div class="pl">
    <div class="mc">
      <h4>{s["card_title"]}</h4>
      {rows_html}
      <div class="stt2{w2}">{icon} {s["status"]}</div>
    </div>
  </div>
</div>"""
        steps_html.append(step_chunk)

    all_steps_html = "\n".join(steps_html)

    # Impact HTML
    impact_items_html = "\n".join([
        f'<div><b>{item["title"]}</b><span>{item["desc"]}</span></div>'
        for item in cfg["impact"]
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{nav}
<main>
  <!-- Route Hero -->
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">{cfg["eyebrow"]}</span>
      <h1>{cfg["h1_line1"]}<br><span class="bl">{cfg["h1_line2"]}</span></h1>
      <p class="lead">{cfg["lead"]}</p>
      <div class="cta">
        <a class="b p" href="{pfx}ui2/request-demo/">Book a Demo &rarr;</a>
        <a class="b o" href="#how">See How it Works</a>
      </div>
      <div class="hp">
        <div class="wc">
          <div class="hd">Document workspace</div>
          <div style="color:var(--muted);font-size:15px;margin:-4px 0 18px">{cfg["doc_name"]} &middot; {cfg["doc_tag"]}</div>
          <div class="g2c">
            <div class="card">
              <b style="font-size:24px;letter-spacing:-.01em">{cfg["mock_inv"]["title"]}</b>
              <div class="dr"><span>Reference / ID</span><b style="color:var(--navy)">{cfg["mock_inv"]["no"]}</b></div>
              <div class="dr"><span>Issue date</span><b style="color:var(--navy)">{cfg["mock_inv"]["date"]}</b></div>
              <div class="dr"><span>Primary spec</span><b style="color:var(--navy)">{cfg["mock_inv"]["taxable"]}</b></div>
              <div class="dr"><span>Status / Tax</span><b style="color:var(--navy)">{cfg["mock_inv"]["gst"]}</b></div>
              <div class="hl fr" style="margin-top:14px"><b>TOTAL VALUE</b><b style="font-size:18px">{cfg["mock_inv"]["total"]}</b></div>
            </div>
            <div class="card">
              <b style="font-size:20px">Extracted fields</b><br>
              <span class="vc">&#10003; Fields validated</span>
              {doc_fields_html}
              <div class="sy">&#10003; {cfg["sync_target"]}</div>
            </div>
          </div>
        </div>
        <div class="cap">Illustrative workflow &middot; Capture &rarr; Extract &rarr; Validate &rarr; Sync</div>
      </div>
    </div>
  </section>

  <!-- How It Works (4 Steps) -->
  <section id="how">
    <div class="w">
      <span class="ey">How it works</span>
      <h2>{cfg["how_title"]}</h2>
      <p class="sub">{cfg["how_sub"]}</p>
      {all_steps_html}
    </div>
  </section>

  <!-- Business Impact -->
  <section class="band">
    <div class="w">
      <span class="ey">Business impact</span>
      <h2>{cfg["impact_title"]}</h2>
      <div class="im">
        {impact_items_html}
      </div>
    </div>
  </section>

  <!-- Next Step -->
  <section>
    <div class="w">
      <span class="ey">Your next step</span>
      <h2>Start with your documents.</h2>
      <p class="sub">Explore the fit with a focused pilot built around the way your team works.</p>
      <div class="c3">
        <div class="card">
          <h3>01 &nbsp;Book a demo</h3>
          <p>Bring sample documents. We'll walk through your process, fields, and downstream system handoffs.</p>
        </div>
        <div class="card">
          <h3>02 &nbsp;Test a workflow</h3>
          <p>See extraction and validation on your own files. Explore rules, exceptions, and approval thresholds.</p>
        </div>
        <div class="card">
          <h3>03 &nbsp;Roll out with confidence</h3>
          <p>Agree on fields, user roles, and integrations before expanding. Keep your team in full control.</p>
        </div>
      </div>
      <div style="margin-top:28px">
        <a class="b p sm" href="{pfx}ui2/request-demo/">Book a Demo &rarr;</a>
      </div>
    </div>
  </section>

  <!-- Security and Control -->
  <section class="band">
    <div class="w">
      <span class="ey">Security and control</span>
      <h2>Automation with people in control.</h2>
      <p class="sub">Keep access, approvals and document progress aligned with how your team works.</p>
      <div class="sc">
        <div>
          <div class="it">
            <b>Role-Based Control</b>
            <span>Give reviewers and approvers access that fits their responsibilities and permissions.</span>
          </div>
          <div class="it">
            <b>Multi-Level Approvals</b>
            <span>Keep decisions with the right people before data moves downstream to accounting.</span>
          </div>
          <div class="it">
            <b>Real-Time Tracking</b>
            <span>Follow document status, review progress, and system handoffs in one centralized flow.</span>
          </div>
        </div>
        <div class="card">
          <h4 style="margin:0 0 16px;font-size:18px">Document activity &middot; Live Audit</h4>
          <div class="ar"><span>09:12</span><b>Document captured<small>Email inbox / API</small></b></div>
          <div class="ar"><span>09:13</span><b>Fields validated<small>Rule and anomaly checks passed</small></b></div>
          <div class="ar"><span>09:18</span><b>Review completed<small>Assigned reviewer verified</small></b></div>
          <div class="ar"><span>09:19</span><b>Synchronized<small>Downstream system posting complete</small></b></div>
        </div>
      </div>
    </div>
  </section>

  <!-- More with Docsynecx -->
  <section>
    <div class="w">
      <span class="ey">More with Docsynecx</span>
      <h2>Connect the rest of your document work.</h2>
      <p class="sub">Bring finance, logistics, and operations together on one unified automation platform.</p>
      <div class="c3">
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span>
          <h3 style="margin-top:16px">Invoice automation</h3>
          <p>Extract invoice data, validate GST and line items, and sync directly with ERPs.</p>
          <a class="l" href="{pfx}ui2/invoice-processing/">Explore product &rarr;</a>
        </div>
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3z M14 10h4l3 3v3h-7 M7 19h.01 M17 19h.01"/></svg></span>
          <h3 style="margin-top:16px">Logistics and supply chain</h3>
          <p>Process shipping bills, customs documents, and automate TMS data intake.</p>
          <a class="l" href="{pfx}ui2/logistics-trade/">Explore product &rarr;</a>
        </div>
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h5v5H5z M14 14h5v5h-5z M10 8h4a2 2 0 0 1 2 2v4"/></svg></span>
          <h3 style="margin-top:16px">Workflow and approvals</h3>
          <p>Route, approve and track documents with multi-level hierarchies.</p>
          <a class="l" href="{pfx}ui2/workflows/">Explore product &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Closing Banner -->
  <section>
    <div class="w">
      <div class="bn">
        <div>
          <h2>{cfg["cta_banner_title"]}</h2>
          <p>{cfg["cta_banner_lead"]}</p>
        </div>
        <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
      </div>
    </div>
  </section>
</main>
{foot}
</body>
</html>"""

# =============================================================================
# BUILD ALL REMAINING PAGES WITH REAL CONTENT
# =============================================================================

def build_landing_page(pfx, canonical_path):
    head = render_head("AI Document Processing & Automation Platform | Docsynecx",
                       "Docsynecx is an AI-powered document automation platform that extracts, validates, and processes business documents across finance, accounting, logistics, and operations.",
                       canonical_path, pfx)
    nav = render_navbar(pfx, is_route=False)
    foot = render_footer(pfx)

    return f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{nav}
<main>
  <section class="hero">
    <div class="w">
      <div>
        <span class="tg">&#10022; AI-powered document processing</span>
        <h1>From Documents to Done &mdash; <span class="bl">Automatically.</span></h1>
        <p class="lead">Automate invoices, logistics documents and business workflows with intelligent data extraction and seamless ERP &amp; TMS integrations.</p>
        <div class="cta">
          <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
          <a class="b o" href="https://invoice.docsynecx.com/signin/">Try free</a>
        </div>
        <div class="fine">No credit card required &bull; 7-day free trial &bull; Secure API access included</div>
        <div class="stt">
          <div><b>99.0%</b><span>Accuracy</span></div>
          <div><b>10x</b><span>Faster processing</span></div>
          <div><b>99.9%</b><span>Uptime</span></div>
        </div>
      </div>

      <div class="wc">
        <div class="hd">Document workspace<span>1 document &middot; Illustrative</span></div>
        <div class="card fr">
          <span><b>invoice_INV-88213.pdf</b><small>Uploaded from email</small></span>
          <span class="tk">&#10003;</span>
        </div>
        <div class="g2c">
          <div class="card">
            <div class="fr"><b style="font-size:14px">INVOICE</b><small>PDF &bull; 1 page</small></div>
            <div class="hl"><b>Acme Traders Pvt Ltd</b><br><small style="color:var(--text);font-size:11px">GSTIN 29ABCDE1234F1Z5</small></div>
            <div class="dr"><span>Invoice no.</span><b style="color:var(--navy)">INV-88213</b></div>
            <div class="dr"><span>Invoice date</span><b style="color:var(--navy)">12 Aug 2026</b></div>
            <div class="dr"><span>7 line items</span><span>&#8377;4,08,728.81</span></div>
            <div class="dr"><span>GST 18%</span><span>&#8377;73,571.19</span></div>
            <div class="hl fr"><b>TOTAL</b><b style="font-size:13.5px">&#8377;4,82,300.00</b></div>
          </div>
          <div class="card">
            <div class="fr"><b style="font-size:13.5px">Extracted fields</b></div>
            <span class="vc">&#10003; Validated</span>
            <div class="fr" style="padding:4px 0;border-bottom:1px solid var(--line)"><span><small>Vendor name</small><b>Acme Traders Pvt Ltd</b></span><span class="tk">&#10003;</span></div>
            <div class="fr" style="padding:4px 0;border-bottom:1px solid var(--line)"><span><small>Invoice number</small><b>INV-88213</b></span><span class="tk">&#10003;</span></div>
            <div class="fr" style="padding:4px 0;border-bottom:1px solid var(--line)"><span><small>Invoice date</small><b>12 Aug 2026</b></span><span class="tk">&#10003;</span></div>
            <div class="fr" style="padding:4px 0"><span><small>Total amount</small><b>&#8377;4,82,300.00</b></span><span class="tk">&#10003;</span></div>
            <div class="sy">&#8635; Synced to TallyPrime</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <span class="ey">Platform</span>
      <h2>One platform. Three automation engines.</h2>
      <p class="sub">Finance, logistics and workflow automation in one place.</p>
      <div class="c3">
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span>
          <h3 style="margin-top:16px">Invoice automation</h3>
          <p>Extract invoice data, validate GST and line items, and sync with Tally, Zoho and SAP.</p>
          <a class="l" href="{pfx}ui2/invoice-processing/">Explore product &rarr;</a>
        </div>
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3z M14 10h4l3 3v3h-7 M7 19h.01 M17 19h.01"/></svg></span>
          <h3 style="margin-top:16px">Logistics and supply chain</h3>
          <p>Process bills of lading, packing lists and customs documents, with CargoWise integration.</p>
          <a class="l" href="{pfx}ui2/logistics-trade/">Explore product &rarr;</a>
        </div>
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h5v5H5z M14 14h5v5h-5z M10 8h4a2 2 0 0 1 2 2v4"/></svg></span>
          <h3 style="margin-top:16px">Workflow and approvals</h3>
          <p>Route, validate, approve and track documents with multi-level approvals and role-based control.</p>
          <a class="l" href="{pfx}ui2/workflows/">Explore product &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <section id="how">
    <div class="w">
      <span class="ey">How it works</span>
      <h2>From documents to done, automatically</h2>
      <p class="sub">Emails, PDFs and scans become validated data and completed workflows.</p>
      <div class="c4">
        <div class="card"><span class="ey" style="margin:0">Step 01</span><h3>Capture</h3><p>Bring documents in from email, uploads, portals and APIs.</p></div>
        <div class="card"><span class="ey" style="margin:0">Step 02</span><h3>AI reads and extracts</h3><p>Fields are identified and extracted as structured data.</p></div>
        <div class="card"><span class="ey" style="margin:0">Step 03</span><h3>Validate and automate</h3><p>Rules catch missing or inconsistent data before it moves.</p></div>
        <div class="card"><span class="ey" style="margin:0">Step 04</span><h3>Sync and complete</h3><p>Verified data flows into Tally, Zoho Books, CargoWise or your ERP.</p></div>
      </div>
    </div>
  </section>

  <section id="integrations" class="band">
    <div class="w">
      <span class="ey">Integrations</span>
      <h2>Works with your existing systems</h2>
      <p class="sub">No disruption. Smarter automation layered on the tools you already use.</p>
      <div class="c4">
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18H6z M9 7h6 M9 11h2 M13 11h2 M9 15h2 M13 15h2"/></svg></span><h3>Tally</h3><p>AI accounting automation for TallyPrime</p><a class="l" href="{pfx}ui2/integration/invoice-to-tally/">View integration &rarr;</a></div>
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 6v14 M12 6C10 4.5 7 4 4 4v14c3 0 6 .5 8 2 2-1.5 5-2 8-2V4c-3 0-6 .5-8 2z"/></svg></span><h3>Zoho Books</h3><p>Automated finance and bill posting</p><a class="l" href="{pfx}ui2/integration/zoho-books/">View integration &rarr;</a></div>
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z M12 12l8-4.5 M12 12v9 M12 12L4 7.5"/></svg></span><h3>CargoWise</h3><p>Automated shipping and customs sync</p><a class="l" href="{pfx}ui2/integration/cargowise/">View integration &rarr;</a></div>
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l9 5-9 5-9-5z M3 13l9 5 9-5"/></svg></span><h3>SAP / ERP</h3><p>Enterprise resource planning connectors</p><a class="l" href="{pfx}ui2/solutions/">Explore solutions &rarr;</a></div>
      </div>
    </div>
  </section>

  <section id="solutions">
    <div class="w">
      <span class="ey">Solutions</span>
      <h2>Built for the way your sector works</h2>
      <div class="c4">
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10l9-6 9 6 M5 10v8 M9 10v8 M15 10v8 M19 10v8 M3 20h18"/></svg></span><h3>Banking</h3><p>Document intelligence for banking teams.</p><a class="l" href="{pfx}ui2/solutions/banking/">Learn more &rarr;</a></div>
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20V4 M4 20h16 M8 16v-4 M12 16V8 M16 16v-6"/></svg></span><h3>Finance</h3><p>Less document handling. More visibility.</p><a class="l" href="{pfx}ui2/solutions/finance/">Learn more &rarr;</a></div>
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3z M14 10h4l3 3v3h-7 M7 19h.01 M17 19h.01"/></svg></span><h3>Logistics</h3><p>Connect documents with operations.</p><a class="l" href="{pfx}ui2/solutions/logistics/">Learn more &rarr;</a></div>
        <div class="card"><span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span><h3>Accounts payable</h3><p>From invoice capture to ERP sync.</p><a class="l" href="{pfx}ui2/solutions/accounts-payable/">Learn more &rarr;</a></div>
      </div>
    </div>
  </section>

  <section id="demo">
    <div class="w">
      <div class="bn">
        <div>
          <h2>Ready to transform your document processing?</h2>
          <p>Trusted by businesses for intelligent data extraction and end-to-end document automation.</p>
        </div>
        <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
      </div>
    </div>
  </section>
</main>
{foot}
</body>
</html>"""

def generate_all():
    print("Starting UI 2 Generation (Option 1: Complete Separation in /ui2/)...")

    # Load core data
    with open("data2/pages.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    # 1. ROOT LANDING PAGE: /index2.html & /ui2/index.html
    save_file("index2.html", build_landing_page("", "index2.html"))
    save_file("ui2/index.html", build_landing_page("../", "ui2/"))

    # 2. CORE ROUTE PAGES: Invoice, Logistics, Workflows
    for slug in ["invoice-processing", "logistics-trade", "workflows"]:
        rel = f"ui2/{slug}/index.html"
        pfx = get_pfx(rel)
        html = render_route_page(data[slug], pfx)
        save_file(rel, html)

    # 3. LOGISTICS SUB-PAGES
    sub_modules = [
        ("shipments", "AI Shipment Creation & Tracking Automation | Docsynecx",
         "Create & update shipments instantly from bills of lading and shipping documents.",
         "Shipment Creation", "Automate Shipment Entry.", "Keep Freight Synchronized.",
         "Bill_of_Lading_MSCU8829.pdf", "Ocean Booking",
         [("Origin Port", "Nhava Sheva"), ("Destination", "Rotterdam"), ("Container", "MSCU7829102")]),
        ("custom-declarations", "Automated Customs Declarations & Trade Compliance | Docsynecx",
         "Convert shipping files and invoices into structured customs declaration entries automatically.",
         "Customs Declarations", "Pre-fill Customs Forms.", "Ensure Trade Compliance.",
         "Customs_Commercial_Inv_9921.pdf", "Clearance File",
         [("HS Code", "8471.30.10"), ("Duty Rate", "7.5% Standard"), ("Declarant", "Verified Partner")]),
        ("ap-reconciliation", "Logistics AP Invoice Reconciliation & Audit | Docsynecx",
         "Reconcile freight and carrier invoices against shipment jobs and expected charges in real-time.",
         "AP Reconciliation", "Reconcile Logistics AP.", "Eliminate Billing Discrepancies.",
         "Carrier_Freight_Inv_CF8810.pdf", "Carrier AP Bill",
         [("Carrier Code", "MSC Shipping"), ("Variance", "₹0.00 (Matched)"), ("Voucher", "Approved for Payment")])
    ]

    for sub_slug, sub_title, sub_desc, sub_eyebrow, sub_h1_1, sub_h1_2, sub_doc, sub_tag, sub_fields in sub_modules:
        sub_cfg = {
            "slug": f"logistics-trade/{sub_slug}",
            "title": sub_title,
            "description": sub_desc,
            "eyebrow": sub_eyebrow,
            "h1_line1": sub_h1_1,
            "h1_line2": sub_h1_2,
            "lead": sub_desc,
            "doc_name": sub_doc,
            "doc_tag": sub_tag,
            "mock_inv": {
                "title": sub_eyebrow.upper(),
                "no": f"REF-{sub_slug[:4].upper()}-2026",
                "date": "14 Oct 2026",
                "taxable": "Freight Charges: Verified",
                "gst": "Currency: INR / USD",
                "total": "Audit Verified ✓"
            },
            "mock_extract": [{"label": k, "val": v} for k, v in sub_fields],
            "sync_target": "Synced to CargoWise One",
            "how_title": f"4 Automated Steps for {sub_eyebrow}",
            "how_sub": "From initial document intake to TMS job update without manual re-keying.",
            "steps": data["logistics-trade"]["steps"],
            "impact_title": f"Measurable Impact for {sub_eyebrow}",
            "impact": data["logistics-trade"]["impact"],
            "cta_banner_title": f"Automate your {sub_eyebrow.lower()} workflows today.",
            "cta_banner_lead": "See how Docsynecx eliminates repetitive logistics documentation."
        }
        rel = f"ui2/logistics-trade/{sub_slug}/index.html"
        pfx = get_pfx(rel)
        save_file(rel, render_route_page(sub_cfg, pfx))

    # 4. INTEGRATION PAGES: Tally, Zoho Books, CargoWise
    integrations = [
        ("invoice-to-tally", "AI Invoice Automation for TallyPrime | Docsynecx",
         "Automatically extract invoices and post verified vouchers directly into TallyPrime.",
         "TallyPrime Integration", "Automate Invoice Entry into Tally.", "Clean Data, Zero Retyping.",
         "Tally_Voucher_INV-88213.xml", "Tally XML / API",
         [("Voucher Type", "Purchase Entry"), ("Ledger", "Synecx Partner Supplier"), ("State Tax", "9% CGST + 9% SGST")],
         "Posted to TallyPrime (Port 9000)",
         "From PDF Invoice to Tally Voucher in 4 Steps.",
         [
             {"title": "Seamless Ledger Mapping", "desc": "Match supplier names and tax categories automatically to your Tally chart of accounts."},
             {"title": "100% Tax Accuracy", "desc": "Validate CGST, SGST, IGST and round-off figures prior to voucher generation."},
             {"title": "Audit-Ready Logs", "desc": "Keep the original PDF invoice attached to each voucher for auditor verification."},
             {"title": "Batch Voucher Creation", "desc": "Post dozens of invoices with a single approval action."}
         ]),
        ("zoho-books", "AI Document Processing for Zoho Books | Docsynecx",
         "Streamline bill creation and accounts payable posting with native Zoho Books synchronization.",
         "Zoho Books Integration", "Automate Bill Entry in Zoho Books.", "Speed Up Month-End Close.",
         "Zoho_Bill_INV-4019.json", "Zoho REST API",
         [("Bill Number", "BILL-4019"), ("Vendor", "Office Tech Solutions"), ("Account", "General Ledger Synced")],
         "Synced to Zoho Books Organization",
         "Automated Accounts Payable for Zoho Books Teams.",
         [
             {"title": "Direct API Sync", "desc": "Post vendor bills directly into Zoho Books without third-party connector tools."},
             {"title": "Automated Line-Item Coding", "desc": "Extract and classify items into specific expense categories instantly."},
             {"title": "Approval Workflows", "desc": "Enforce review thresholds before documents become payable liabilities."},
             {"title": "Multi-Entity Support", "desc": "Route invoices across multiple Zoho Books organizations easily."}
         ]),
        ("cargowise", "AI Logistics Document Automation for CargoWise One | Docsynecx",
         "Extract shipment data, digitize documents, and seamlessly integrate with CargoWise for faster operations.",
         "CargoWise Integration", "Native CargoWise Data Automation.", "Keep Supply Chains Moving.",
         "CargoWise_Job_Doc_8819.xml", "eAdaptor Direct",
         [("Job Number", "JOB-8819"), ("Transport Mode", "Sea Freight Import"), ("Consignee Code", "ACME-IND-01")],
         "Synced to CargoWise One eAdaptor",
         "From Document Capture to CargoWise Shipment in 4 Steps.",
         [
             {"title": "Native eAdaptor Sync", "desc": "Post structured shipment records through native APIs without flat file uploads."},
             {"title": "Bill of Lading Extraction", "desc": "Capture containers, seal numbers, piece counts, and weights automatically."},
             {"title": "Automated Customs Data", "desc": "Structure tariff codes and declaration fields directly for filing modules."},
             {"title": "24/7 Processing", "desc": "Process pre-alerts and booking files around the clock across time zones."}
         ])
    ]

    for int_slug, int_title, int_desc, int_eyebrow, int_h1_1, int_h1_2, int_doc, int_tag, int_fields, int_sync, int_how, int_impact in integrations:
        int_cfg = {
            "slug": f"integration/{int_slug}",
            "title": int_title,
            "description": int_desc,
            "eyebrow": int_eyebrow,
            "h1_line1": int_h1_1,
            "h1_line2": int_h1_2,
            "lead": int_desc,
            "doc_name": int_doc,
            "doc_tag": int_tag,
            "mock_inv": {
                "title": int_eyebrow.upper(),
                "no": f"VOUCHER-{int_slug[:4].upper()}-99",
                "date": "14 Oct 2026",
                "taxable": "Mapping: 100% Resolved",
                "gst": "API Handoff: Ready",
                "total": "Auto-Sync Enabled ✓"
            },
            "mock_extract": [{"label": k, "val": v} for k, v in int_fields],
            "sync_target": int_sync,
            "how_title": int_how,
            "how_sub": "Capture documents, validate accounts, resolve exceptions, and push directly into your software.",
            "steps": data["invoice-processing"]["steps"],
            "impact_title": f"Why Teams Choose Docsynecx for {int_eyebrow}",
            "impact": int_impact,
            "cta_banner_title": f"Ready to integrate with {int_eyebrow}?",
            "cta_banner_lead": "See a live demonstration on your own invoices and software setup."
        }
        rel = f"ui2/integration/{int_slug}/index.html"
        pfx = get_pfx(rel)
        save_file(rel, render_route_page(int_cfg, pfx))

    # 5. SOLUTIONS PAGE (/ui2/solutions/)
    rel = "ui2/solutions/index.html"
    pfx = get_pfx(rel)
    sol_head = render_head("AI Document Automation Solutions for Business | Docsynecx",
                           "Docsynecx is an AI-powered document automation platform that extracts, validates, and processes business documents across finance, accounting, logistics, and operations.",
                           "ui2/solutions/", pfx)
    sol_nav = render_navbar(pfx, is_route=True)
    sol_foot = render_footer(pfx)

    sol_body = f"""<!DOCTYPE html>
<html lang="en">
{sol_head}
<body>
{sol_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Solutions</span>
      <h1>Intelligent Document Processing.<br><span class="bl">Tailored for Your Industry.</span></h1>
      <p class="lead">From accounts payable to cross-border logistics and banking workflows, Docsynecx automates document capture, data extraction, and ERP integration.</p>
      <div class="cta">
        <a class="b p" href="{pfx}ui2/request-demo/">Book a Demo &rarr;</a>
      </div>
    </div>
  </section>

  <section id="banking" class="band">
    <div class="w">
      <span class="ey">Industry Solution</span>
      <h2>Banking & Financial Services</h2>
      <p class="sub">Automate high-volume customer onboarding, KYC document verification, bank statement parsing, and financial auditing with human-in-the-loop controls.</p>
      <div class="c3">
        <div class="card">
          <h3>KYC & ID Verification</h3>
          <p>Extract and validate identity cards, passports, and utility bills instantly with automated anomaly detection.</p>
        </div>
        <div class="card">
          <h3>Financial Statements</h3>
          <p>Parse complex balance sheets, P&L reports, and credit reports into standardized numerical data.</p>
        </div>
        <div class="card">
          <h3>Audit-Ready Governance</h3>
          <p>Maintain complete compliance logs with immutable timestamps for regulatory inspections.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="finance">
    <div class="w">
      <span class="ey">Industry Solution</span>
      <h2>Finance & Accounting</h2>
      <p class="sub">Transform accounts payable from a manual bottleneck into an automated, error-free workflow that syncs directly with your ledger.</p>
      <div class="c3">
        <div class="card">
          <h3>Invoice Line-Item Capture</h3>
          <p>Extract multi-line tables, tax breakdowns, and discounts from PDFs and scans with 99%+ accuracy.</p>
        </div>
        <div class="card">
          <h3>2-Way & 3-Way Matching</h3>
          <p>Cross-check invoices against purchase orders and goods receipt notes automatically before payment.</p>
        </div>
        <div class="card">
          <h3>ERP Direct Posting</h3>
          <p>Post validated vouchers into Tally, Zoho Books, SAP, and custom ERPs with zero manual retyping.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="logistics" class="band">
    <div class="w">
      <span class="ey">Industry Solution</span>
      <h2>Logistics & Supply Chain</h2>
      <p class="sub">Accelerate shipment processing, ocean freight documentation, and customs compliance with native CargoWise One integration.</p>
      <div class="c3">
        <div class="card">
          <h3>Bills of Lading & Airway Bills</h3>
          <p>Automatically extract shipper, consignee, port codes, container numbers, and seals 24/7.</p>
        </div>
        <div class="card">
          <h3>Customs Declarations</h3>
          <p>Structure commercial invoices and packing lists into verified customs declarations to prevent filing delays.</p>
        </div>
        <div class="card">
          <h3>Carrier AP Reconciliation</h3>
          <p>Audit shipping line and carrier invoices against job costings and flag demurrage risks early.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="accounts-payable">
    <div class="w">
      <span class="ey">Use Case</span>
      <h2>Accounts Payable Automation</h2>
      <p class="sub">From invoice capture through exception review, multi-level approvals, and accounting handoff.</p>
      <div class="c4">
        <div class="card"><span class="ey" style="margin:0">01</span><h3>Ingest</h3><p>Collect from dedicated emails, portals, and uploads automatically.</p></div>
        <div class="card"><span class="ey" style="margin:0">02</span><h3>Validate</h3><p>Verify GSTIN, arithmetic, tax percentages, and detect duplicates.</p></div>
        <div class="card"><span class="ey" style="margin:0">03</span><h3>Approve</h3><p>Route exceptions to department heads with role-based controls.</p></div>
        <div class="card"><span class="ey" style="margin:0">04</span><h3>Post</h3><p>Transfer accounting-ready data straight into your books.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <div class="bn">
        <div>
          <h2>Ready to transform your document workflows?</h2>
          <p>Talk to our solution architects to explore an implementation tailored to your tech stack.</p>
        </div>
        <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
      </div>
    </div>
  </section>
</main>
{sol_foot}
</body>
</html>"""
    save_file(rel, sol_body)

    # 5b. SOLUTION SUB-PAGES — Banking, Finance, Logistics, Accounts Payable
    sol_pages = [
        (
            "banking",
            "AI Document Automation for Banking & Financial Services | Docsynecx",
            "Automate KYC verification, bank statement parsing, loan document processing, and financial audit workflows with enterprise-grade AI.",
            "Banking Solutions",
            "Smarter Document Processing",
            "for Banking & Financial Services.",
            "From high-volume onboarding documents to audit-trail compliance, Docsynecx extracts, validates, and routes critical banking documents automatically — with human oversight at every step.",
            [
                {"title": "KYC & Identity Verification", "desc": "Extract and cross-validate identity cards, passports, and utility bills instantly with automated anomaly and forgery detection."},
                {"title": "Bank Statement Parsing", "desc": "Convert multi-page bank statements into clean, structured transaction data ready for credit analysis and lending decisions."},
                {"title": "Loan Document Processing", "desc": "Capture income proofs, property documents, and agreement terms at scale with high-accuracy extraction and conditional routing."},
                {"title": "Regulatory Compliance Logs", "desc": "Maintain immutable timestamps and audit trails across every document action for inspections and regulatory reporting."},
                {"title": "Multi-Format Document Support", "desc": "Process PDFs, scanned images, WhatsApp attachments, and email submissions through a single unified intake pipeline."},
                {"title": "Human-in-the-Loop Controls", "desc": "Route exceptions, flagged documents, and approval decisions to the right reviewer without manual queue management."},
            ],
            [
                {"title": "80% Faster KYC", "desc": "Reduce customer onboarding time from days to hours with automated document capture and verification workflows."},
                {"title": "99%+ Extraction Accuracy", "desc": "Field-level AI models trained on financial documents ensure data quality at every step."},
                {"title": "Zero Compliance Risk", "desc": "Full audit trails, role-based access, and retention policies aligned with banking regulations."},
            ]
        ),
        (
            "finance",
            "AI Document Automation for Finance & Accounting Teams | Docsynecx",
            "Transform accounts payable, expense management, and financial close with intelligent invoice extraction, 3-way matching, and direct ERP integration.",
            "Finance Solutions",
            "Less Document Handling.",
            "More Financial Visibility.",
            "Docsynecx eliminates manual invoice entry and data rekeying — so finance teams can focus on analysis, exception resolution, and closing the books faster.",
            [
                {"title": "Invoice Line-Item Extraction", "desc": "Extract multi-line tables, tax breakdowns, HSN codes, and discounts from PDFs and scanned invoices with 99%+ accuracy."},
                {"title": "2-Way & 3-Way Matching", "desc": "Automatically cross-check invoices against purchase orders and goods receipts to prevent overpayment and duplicate entries."},
                {"title": "GST Validation", "desc": "Validate GSTIN format, tax percentages, arithmetic totals, and detect mismatches before they reach the ledger."},
                {"title": "ERP Direct Posting", "desc": "Post validated vouchers into Tally, Zoho Books, SAP, and custom ERPs without manual retyping or CSV uploads."},
                {"title": "Exception Routing", "desc": "Automatically route mismatched or flagged invoices to the right reviewer based on amount thresholds and vendor codes."},
                {"title": "Month-End Acceleration", "desc": "Close books faster by eliminating document backlogs, reducing approval cycles, and automating recurring vendor bills."},
            ],
            [
                {"title": "10x Faster Processing", "desc": "Reduce average invoice processing time from 8+ minutes to under 45 seconds with AI-driven extraction."},
                {"title": "Eliminate Manual Errors", "desc": "Zero rekeying means zero transposition errors, duplicate payments, or missed discounts."},
                {"title": "Full ERP Compatibility", "desc": "Works with Tally, Zoho Books, SAP, Microsoft Dynamics, and any REST API-compatible accounting system."},
            ]
        ),
        (
            "logistics",
            "AI Document Automation for Logistics & Supply Chain | Docsynecx",
            "Automate bill of lading processing, customs declarations, carrier AP reconciliation, and shipment data entry with native CargoWise One integration.",
            "Logistics Solutions",
            "Connect Documents",
            "with Logistics Operations.",
            "From pre-alerts to customs filing and carrier invoice auditing, Docsynecx processes every logistics document automatically — syncing clean data into CargoWise and your TMS in real time.",
            [
                {"title": "Bills of Lading & Airway Bills", "desc": "Capture shipper, consignee, port codes, container numbers, seal numbers, and piece counts automatically — 24/7."},
                {"title": "Customs Declaration Pre-fill", "desc": "Structure commercial invoices and packing lists into verified customs declaration fields to eliminate filing delays."},
                {"title": "Carrier AP Reconciliation", "desc": "Audit freight and carrier invoices against job costings, detect billing discrepancies, and flag demurrage risks early."},
                {"title": "CargoWise Native Sync", "desc": "Post structured shipment records through CargoWise eAdaptor without flat file uploads, mapping scripts, or middleware."},
                {"title": "Multi-Modal Document Support", "desc": "Process ocean, air, and road freight documents across FCL, LCL, and courier shipment types in one pipeline."},
                {"title": "24/7 Pre-Alert Processing", "desc": "Handle pre-alert and booking file volumes around the clock across global time zones without overnight team overhead."},
            ],
            [
                {"title": "50% Fewer Data Entry Hours", "desc": "Eliminate manual shipment creation and customs pre-filling from operations team workloads."},
                {"title": "Faster Customs Filing", "desc": "Pre-filled, validated declaration data means documents are filed before the vessel arrives at port."},
                {"title": "Native CargoWise Integration", "desc": "No middleware, no flat files. Direct eAdaptor sync keeps your TMS always current."},
            ]
        ),
        (
            "accounts-payable",
            "AI-Powered Accounts Payable Automation | Docsynecx",
            "End-to-end AP automation from invoice capture and data extraction through multi-level approvals and ERP posting — with zero manual retyping.",
            "Accounts Payable",
            "From Invoice Capture",
            "to ERP Sync — Automatically.",
            "Docsynecx automates every step of the AP cycle: collecting invoices from email and portals, extracting and validating data, routing for approval, and posting to your accounting system.",
            [
                {"title": "Multi-Channel Invoice Intake", "desc": "Collect invoices from dedicated email inboxes, vendor portals, WhatsApp, and API submissions into one unified queue."},
                {"title": "AI Data Extraction", "desc": "Extract vendor name, GSTIN, invoice number, date, line items, tax amounts, and totals from any document format."},
                {"title": "GSTIN & Arithmetic Validation", "desc": "Automatically verify tax registration numbers, check arithmetic totals, and detect duplicate invoice submissions."},
                {"title": "Multi-Level Approval Routing", "desc": "Route invoices to the right approver based on amount thresholds, cost centres, and vendor categories — with escalation rules."},
                {"title": "ERP & Accounting Sync", "desc": "Post approved vouchers directly into Tally, Zoho Books, SAP, and custom ERPs without any manual intervention."},
                {"title": "Exception Dashboard", "desc": "Track every invoice from intake to posting with a real-time dashboard showing status, exceptions, and aging invoices."},
            ],
            [
                {"title": "95% Straight-Through Processing", "desc": "Most invoices move from capture to posting without any human touch when validation rules are met."},
                {"title": "Zero Duplicate Payments", "desc": "Automated deduplication checks every invoice against the processed history before approval routing begins."},
                {"title": "Complete Audit Trail", "desc": "Every extraction, validation, approval, and posting event is logged with timestamps and user identity."},
            ]
        ),
    ]

    for sol_slug, sol_title, sol_desc, sol_eyebrow, sol_h1_1, sol_h1_2, sol_lead, sol_features, sol_impact in sol_pages:
        rel = f"ui2/solutions/{sol_slug}/index.html"
        pfx = get_pfx(rel)
        sp_head = render_head(sol_title, sol_desc, f"ui2/solutions/{sol_slug}/", pfx)
        sp_nav  = render_navbar(pfx, is_route=True)
        sp_foot = render_footer(pfx)

        features_html = "\n".join([
            f'<div class="card"><h3>{f["title"]}</h3><p>{f["desc"]}</p></div>'
            for f in sol_features
        ])
        impact_html = "\n".join([
            f'<div><b>{i["title"]}</b><span>{i["desc"]}</span></div>'
            for i in sol_impact
        ])

        sp_body = f"""<!DOCTYPE html>
<html lang="en">
{sp_head}
<body>
{sp_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">{sol_eyebrow}</span>
      <h1>{sol_h1_1}<br><span class="bl">{sol_h1_2}</span></h1>
      <p class="lead">{sol_lead}</p>
      <div class="cta">
        <a class="b p" href="{pfx}ui2/request-demo/">Book a Demo &rarr;</a>
        <a class="b o" href="{pfx}ui2/solutions/">All Solutions</a>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <span class="ey">Capabilities</span>
      <h2>What Docsynecx does for {sol_eyebrow}</h2>
      <p class="sub">Tailored automation features built for how your team actually works.</p>
      <div class="c3">
        {features_html}
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <span class="ey">Business impact</span>
      <h2>Measurable results from day one.</h2>
      <div class="im">
        {impact_html}
      </div>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <span class="ey">How it works</span>
      <h2>From documents to done, in four steps.</h2>
      <div class="c4">
        <div class="card"><span class="ey" style="margin:0">Step 01</span><h3>Capture</h3><p>Collect documents from email, portals, APIs and uploads automatically into a single queue.</p></div>
        <div class="card"><span class="ey" style="margin:0">Step 02</span><h3>Extract</h3><p>AI reads every document and outputs structured, field-level data ready for validation.</p></div>
        <div class="card"><span class="ey" style="margin:0">Step 03</span><h3>Validate & Route</h3><p>Business rules check every field and send exceptions to the right reviewer automatically.</p></div>
        <div class="card"><span class="ey" style="margin:0">Step 04</span><h3>Sync</h3><p>Approved data posts directly into your ERP, TMS, or accounting system — zero rekeying.</p></div>
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <span class="ey">More with Docsynecx</span>
      <h2>Explore the full platform.</h2>
      <div class="c3">
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3h7l5 5v13H7z M14 3v5h5 M10 13h6 M10 17h6"/></svg></span>
          <h3 style="margin-top:16px">Invoice automation</h3>
          <p>Extract invoice data, validate GST and line items, and sync with Tally, Zoho and SAP.</p>
          <a class="l" href="{pfx}ui2/invoice-processing/">Explore product &rarr;</a>
        </div>
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h11v9H3z M14 10h4l3 3v3h-7 M7 19h.01 M17 19h.01"/></svg></span>
          <h3 style="margin-top:16px">Logistics and supply chain</h3>
          <p>Process shipping bills, customs documents, and automate TMS data intake with CargoWise.</p>
          <a class="l" href="{pfx}ui2/logistics-trade/">Explore product &rarr;</a>
        </div>
        <div class="card">
          <span class="ic"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5h5v5H5z M14 14h5v5h-5z M10 8h4a2 2 0 0 1 2 2v4"/></svg></span>
          <h3 style="margin-top:16px">Workflow and approvals</h3>
          <p>Route, approve and track documents with multi-level hierarchies and role-based control.</p>
          <a class="l" href="{pfx}ui2/workflows/">Explore product &rarr;</a>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <div class="bn">
        <div>
          <h2>Ready to automate your {sol_eyebrow.lower()} document workflows?</h2>
          <p>Talk to our team and see a live demo on your own documents and systems.</p>
        </div>
        <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
      </div>
    </div>
  </section>
</main>
{sp_foot}
</body>
</html>"""
        save_file(rel, sp_body)

    # 6. PRICING PAGE (/ui2/pricing/)
    rel = "ui2/pricing/index.html"
    pfx = get_pfx(rel)
    prc_head = render_head("AP Automation Software Pricing Plans | Docsynecx",
                           "Simple, transparent pricing for business document automation. Start with a 7-day free trial. No credit card required.",
                           "ui2/pricing/", pfx)
    prc_nav = render_navbar(pfx, is_route=True)
    prc_foot = render_footer(pfx)

    prc_body = f"""<!DOCTYPE html>
<html lang="en">
{prc_head}
<body>
{prc_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Transparent Pricing</span>
      <h1>Simple, Transparent Pricing<br><span class="bl">for Business Automation.</span></h1>
      <p class="lead">Automate invoice processing, reduce manual work, and integrate seamlessly with your accounting systems. All plans include a 7-day free trial. No credit card required.</p>
      <div class="c3" style="margin-top:48px;text-align:left">
        <!-- Starter Plan -->
        <div class="card" style="border:1px solid var(--line);border-radius:20px;padding:32px">
          <span class="ey" style="margin:0 0 8px">Starter</span>
          <h3 style="font-size:28px;margin-bottom:8px">Try Real Automation</h3>
          <p style="color:var(--muted);font-size:15px;margin-bottom:20px">Explore intelligent extraction with real data.</p>
          <div style="font-size:24px;font-weight:700;color:var(--navy);margin-bottom:20px">20 Free Credits</div>
          <ul style="list-style:none;padding:0;margin:0 0 28px;font-size:15px;color:var(--text);display:flex;flex-direction:column;gap:10px">
            <li>✓ Invoice data extraction</li>
            <li>✓ GST &amp; basic validation</li>
            <li>✓ Limited Tally integration</li>
            <li>✓ 1 company support</li>
            <li>✓ 1 user account</li>
            <li>✓ Email support</li>
          </ul>
          <a class="b o" href="https://invoice.docsynecx.com/signin/" style="width:100%;justify-content:center">Start Free Trial</a>
        </div>

        <!-- Professional Plan -->
        <div class="card" style="border:2px solid var(--blue);border-radius:20px;padding:32px;box-shadow:var(--shadow-pop);position:relative">
          <span class="tg" style="position:absolute;top:-14px;right:24px;font-size:12px;padding:4px 12px">Most Popular</span>
          <span class="ey" style="margin:0 0 8px">Professional</span>
          <h3 style="font-size:28px;margin-bottom:8px">Growing Businesses</h3>
          <p style="color:var(--muted);font-size:15px;margin-bottom:20px">High-volume extraction and team collaboration.</p>
          <div style="font-size:24px;font-weight:700;color:var(--navy);margin-bottom:20px">Flexible Volume</div>
          <ul style="list-style:none;padding:0;margin:0 0 28px;font-size:15px;color:var(--text);display:flex;flex-direction:column;gap:10px">
            <li>✓ Everything in Starter</li>
            <li>✓ Bulk invoice processing</li>
            <li>✓ Multi-line item extraction</li>
            <li>✓ Advanced validation &amp; duplicates</li>
            <li>✓ Full Tally &amp; Zoho integration</li>
            <li>✓ Multi-company support</li>
            <li>✓ Multiple users &amp; Priority support</li>
          </ul>
          <a class="b p" href="{pfx}ui2/request-demo/" style="width:100%;justify-content:center">Get Started &rarr;</a>
        </div>

        <!-- Enterprise Plan -->
        <div class="card" style="border:1px solid var(--line);border-radius:20px;padding:32px">
          <span class="ey" style="margin:0 0 8px">Enterprise</span>
          <h3 style="font-size:28px;margin-bottom:8px">Large-Scale Operations</h3>
          <p style="color:var(--muted);font-size:15px;margin-bottom:20px">Custom workflows, CargoWise &amp; ERP integrations.</p>
          <div style="font-size:24px;font-weight:700;color:var(--navy);margin-bottom:20px">Custom Volume</div>
          <ul style="list-style:none;padding:0;margin:0 0 28px;font-size:15px;color:var(--text);display:flex;flex-direction:column;gap:10px">
            <li>✓ Everything in Professional</li>
            <li>✓ Custom workflows &amp; approvals</li>
            <li>✓ CargoWise &amp; custom ERP APIs</li>
            <li>✓ Multi-entity organization</li>
            <li>✓ Dedicated onboarding &amp; account manager</li>
            <li>✓ SLA &amp; 24/7 dedicated support</li>
          </ul>
          <a class="b o" href="{pfx}ui2/request-demo/" style="width:100%;justify-content:center">Contact Sales</a>
        </div>
      </div>
    </div>
  </section>

  <!-- Feature Comparison Table -->
  <section class="band">
    <div class="w">
      <span class="ey">Comparison</span>
      <h2>Compare All Features Across Plans</h2>
      <p class="sub">Everything you need to select the right tier for your organization.</p>
      <div style="overflow-x:auto;margin-top:36px">
        <table style="width:100%;border-collapse:collapse;font-size:15px;text-align:left;background:#fff;border-radius:16px;overflow:hidden;box-shadow:var(--shadow-card)">
          <thead>
            <tr style="background:var(--panel);border-bottom:2px solid var(--line)">
              <th style="padding:16px 20px;color:var(--navy);font-weight:700">Feature</th>
              <th style="padding:16px 20px;color:var(--navy);font-weight:700">Starter</th>
              <th style="padding:16px 20px;color:var(--blue);font-weight:700">Professional</th>
              <th style="padding:16px 20px;color:var(--navy);font-weight:700">Enterprise</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Invoice Processing</td><td style="padding:14px 20px">Limited</td><td style="padding:14px 20px">High Volume</td><td style="padding:14px 20px">Unlimited</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Extraction Accuracy</td><td style="padding:14px 20px">Standard</td><td style="padding:14px 20px">High (99%+)</td><td style="padding:14px 20px">Premium Guaranteed</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Tally Integration</td><td style="padding:14px 20px">Limited</td><td style="padding:14px 20px">Full</td><td style="padding:14px 20px">Full</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Bulk Batch Processing</td><td style="padding:14px 20px">—</td><td style="padding:14px 20px">✓ Included</td><td style="padding:14px 20px">✓ Included</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Multi-Line Item Extraction</td><td style="padding:14px 20px">—</td><td style="padding:14px 20px">✓ Included</td><td style="padding:14px 20px">✓ Included</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Users</td><td style="padding:14px 20px">1 User</td><td style="padding:14px 20px">Multiple Users</td><td style="padding:14px 20px">Unlimited</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Companies</td><td style="padding:14px 20px">1 Company</td><td style="padding:14px 20px">Multiple</td><td style="padding:14px 20px">Multi-Entity</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Logistics & CargoWise Sync</td><td style="padding:14px 20px">—</td><td style="padding:14px 20px">—</td><td style="padding:14px 20px">✓ Custom Module</td></tr>
            <tr style="border-bottom:1px solid var(--line)"><td style="padding:14px 20px;font-weight:600">Document Intake Channels</td><td style="padding:14px 20px">Web Portal</td><td style="padding:14px 20px">Portal + WhatsApp</td><td style="padding:14px 20px">Portal + Email + API</td></tr>
            <tr><td style="padding:14px 20px;font-weight:600">Support</td><td style="padding:14px 20px">Email</td><td style="padding:14px 20px">Priority</td><td style="padding:14px 20px">Dedicated SLA (24/7)</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <div class="bn">
        <div>
          <h2>Start your 7-day free trial today.</h2>
          <p>No credit card required. Experience immediate ROI and clean data automation.</p>
        </div>
        <a class="b p" href="https://invoice.docsynecx.com/signin/">Start Free Trial &rarr;</a>
      </div>
    </div>
  </section>
</main>
{prc_foot}
</body>
</html>"""
    save_file(rel, prc_body)

    # 7. BLOG PAGE (/ui2/blog/)
    rel = "ui2/blog/index.html"
    pfx = get_pfx(rel)
    blg_head = render_head("Workflow Automation Software Resources & Guides | Docsynecx",
                           "Expert insights, best practices, and industry trends for document processing automation and enterprise document AI integration.",
                           "ui2/blog/", pfx)
    blg_nav = render_navbar(pfx, is_route=True)
    blg_foot = render_footer(pfx)

    articles = [
        ("The Impact of AI Logistics Document Verification in 2026",
         "The logistics and supply chain industry is evolving faster than ever. In 2026, businesses are managing higher shipment volumes, tighter delivery timelines, and increasingly complex compliance requirements.",
         "Logistics & Trade"),
        ("Manual vs AI Document Processing: Cost, Time & Accuracy Comparison",
         "In today’s fast-paced business environment, managing invoices and financial documents manually is no longer sustainable. Businesses dealing with high volumes face delays, errors, and increased costs.",
         "Finance Automation"),
        ("Why Manual Invoice Entry Fails at Scale: A Deep Dive into Compliance Risks",
         "Explore why manual invoice processing becomes unsustainable as businesses grow—uncovering hidden costs, accuracy issues, productivity losses, and serious compliance risks.",
         "Compliance & Tax"),
        ("From Raw Invoices to ERP-Ready Data: The Power of Intelligent Structuring",
         "Discover how intelligent invoice structuring transforms unstructured invoice data into clean, accurate, ERP-ready information for seamless integration with Tally and SAP.",
         "ERP Integration"),
        ("Tally Workflow Automation: Transforming PDF Invoices into Synced Entries",
         "Docsynecx eliminates repetitive data entry by converting PDF and image invoices directly into Tally-ready entries with AI-driven accuracy and seamless integration.",
         "TallyPrime"),
        ("Accurate Data Extraction at Scale: Handling Bulk Document Uploads",
         "Docsynecx eliminates limitations by offering AI-driven bulk document processing that transforms scattered, high-volume paperwork into clean, structured, and validated data.",
         "Enterprise AI")
    ]

    art_cards = "\n".join([
        f"""<div class="card" style="display:flex;flex-direction:column;padding:28px">
  <span class="tg" style="font-size:11px;padding:3px 10px;margin-bottom:12px;align-self:flex-start">{cat}</span>
  <h3 style="font-size:20px;line-height:1.3;margin-bottom:12px">{title}</h3>
  <p style="color:var(--text);font-size:15px;line-height:1.6;margin-bottom:16px">{desc}</p>
  <div style="margin-top:auto"><span style="color:var(--blue);font-weight:600;font-size:14px">Read article &rarr;</span></div>
</div>"""
        for title, desc, cat in articles
    ])

    blg_body = f"""<!DOCTYPE html>
<html lang="en">
{blg_head}
<body>
{blg_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Docsynecx Insights</span>
      <h1>Latest Insights on Document AI<br><span class="bl">&amp; Business Automation.</span></h1>
      <p class="lead">Expert guides, technical best practices, and industry benchmarks for modern finance and logistics teams.</p>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <div class="c3">
        {art_cards}
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <div class="bn">
        <div>
          <h2>Ready to put these insights into practice?</h2>
          <p>Schedule a customized demonstration tailored to your specific use case and requirements.</p>
        </div>
        <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
      </div>
    </div>
  </section>
</main>
{blg_foot}
</body>
</html>"""
    save_file(rel, blg_body)

    # 8. REQUEST DEMO PAGE (/ui2/request-demo/)
    rel = "ui2/request-demo/index.html"
    pfx = get_pfx(rel)
    dmo_head = render_head("Request a Personalized Demo | Docsynecx",
                           "See how Docsynecx automates your document processing with intelligent AI data extraction and ERP integration. Schedule your live walkthrough.",
                           "ui2/request-demo/", pfx)
    dmo_nav = render_navbar(pfx, is_route=True)
    dmo_foot = render_footer(pfx)

    dmo_body = f"""<!DOCTYPE html>
<html lang="en">
{dmo_head}
<body>
{dmo_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Get in Touch</span>
      <h1>Experience Docsynecx in Action.<br><span class="bl">Tailored to Your Documents.</span></h1>
      <p class="lead">Bring a few of your actual vendor bills, bills of lading, or approval files. We will walk through extraction, rules, and system handoffs.</p>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <div style="display:grid;grid-template-columns:1.1fr 1fr;gap:48px;align-items:start">
        <!-- Form -->
        <div class="card" style="padding:36px;box-shadow:var(--shadow-card)">
          <h3 style="font-size:24px;margin-bottom:8px">Book Your Live Walkthrough</h3>
          <p style="color:var(--muted);font-size:15px;margin-bottom:24px">Fill out the details below and an automation architect will contact you within 24 hours.</p>
          <form onsubmit="alert('Thank you! Our automation team will reach out shortly.');return false" style="display:flex;flex-direction:column;gap:18px">
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px;color:var(--navy)">Full Name *</label>
              <input type="text" required placeholder="John Doe" style="width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px">
            </div>
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px;color:var(--navy)">Work Email *</label>
              <input type="email" required placeholder="john@company.com" style="width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px">
            </div>
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px;color:var(--navy)">Phone Number *</label>
              <input type="tel" required placeholder="+91 98765 43210" style="width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px">
            </div>
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px;color:var(--navy)">Company Name *</label>
              <input type="text" required placeholder="Acme Logistics Pvt Ltd" style="width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px">
            </div>
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px;color:var(--navy)">Your Requirements &amp; Target Systems</label>
              <textarea rows="3" placeholder="Tell us about your document volume, formats, and ERP (Tally, Zoho, SAP, CargoWise)..." style="width:100%;padding:12px 14px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px"></textarea>
            </div>
            <button type="submit" class="b p" style="justify-content:center;margin-top:8px">Submit Request &rarr;</button>
          </form>
        </div>

        <!-- Benefits Summary -->
        <div>
          <div class="card" style="padding:32px;margin-bottom:24px">
            <h4 style="font-size:18px;margin-bottom:12px">What to Expect in Your Demo</h4>
            <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:14px;font-size:15px;color:var(--text)">
              <li><b>✓ Custom Document Test:</b> See real-time AI parsing on your exact invoice and shipping formats.</li>
              <li><b>✓ Integration Review:</b> Understand how data syncs into Tally, Zoho Books, or CargoWise.</li>
              <li><b>✓ Exception Handling:</b> Learn how rules flag discrepancies before posting.</li>
              <li><b>✓ ROI Analysis:</b> Calculate time and cost savings tailored to your volume.</li>
            </ul>
          </div>

          <div class="card" style="padding:28px;background:var(--tint);border:1px solid var(--tint-border)">
            <b style="color:var(--blue-dark);font-size:17px;display:block;margin-bottom:6px">Prefer Immediate Access?</b>
            <p style="font-size:14px;color:var(--text);margin-bottom:16px">You can start a self-serve 7-day free trial right now with 20 complimentary processing credits.</p>
            <a class="b o" href="https://invoice.docsynecx.com/signin/" style="background:#fff">Sign In to Free Trial</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
{dmo_foot}
</body>
</html>"""
    save_file(rel, dmo_body)

    # 9. ABOUT US (/ui2/about/)
    rel = "ui2/about/index.html"
    pfx = get_pfx(rel)
    abt_head = render_head("About Docsynecx | AI-Powered Document Automation",
                           "Docsynecx is an enterprise-grade Document AI platform built by SynecxAI Labs to help organizations unlock the value hidden in their documents.",
                           "ui2/about/", pfx)
    abt_nav = render_navbar(pfx, is_route=True)
    abt_foot = render_footer(pfx)

    abt_body = f"""<!DOCTYPE html>
<html lang="en">
{abt_head}
<body>
{abt_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Our Story</span>
      <h1>The Story Behind Docsynecx Innovation.<br><span class="bl">Transforming Document Workflows.</span></h1>
      <p class="lead">Docsynecx is an enterprise-grade Document AI platform built by SynecxAI Labs to help organizations unlock the value hidden in their invoices, logistics paperwork, and approvals.</p>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <div style="max-width:840px;margin:0 auto;font-size:18px;line-height:1.7;color:var(--text)">
        <p style="margin-bottom:20px">We specialize in transforming unstructured and semi-structured documents—such as vendor bills, bills of lading, customs declarations, and internal approval forms—into accurate, structured, and actionable data using advanced machine learning.</p>
        <p style="margin-bottom:32px">Designed for scale, security, and enterprise reliability, Docsynecx integrates seamlessly with ERP, accounting, and supply chain systems, empowering finance and operations teams to move faster with confidence.</p>
      </div>

      <div class="c2" style="display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:960px;margin:40px auto 0">
        <div class="card" style="padding:32px">
          <span class="ey">Our Mission</span>
          <h3 style="font-size:22px;margin-bottom:12px">Simplify Complex Workflows</h3>
          <p style="color:var(--text);font-size:15px;line-height:1.6">To simplify and automate complex document workflows through AI-powered intelligence—enabling organizations to focus on strategic work while we handle the data.</p>
        </div>
        <div class="card" style="padding:32px">
          <span class="ey">Our Vision</span>
          <h3 style="font-size:22px;margin-bottom:12px">The Global Standard in IDP</h3>
          <p style="color:var(--text);font-size:15px;line-height:1.6">To become the global standard in document automation by making enterprise-grade intelligent document processing accessible, intelligent, and scalable for every business.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <span class="ey">Core Values</span>
      <h2>Principles That Drive Our Platform</h2>
      <div class="c3">
        <div class="card">
          <h3>Accuracy-First Approach</h3>
          <p>Our AI models are trained for maximum accuracy across Indian and international document standards, continuously improving data extraction.</p>
        </div>
        <div class="card">
          <h3>Continuous Innovation</h3>
          <p>Technology is our craft. We invest in continuous R&amp;D to deliver state-of-the-art vision and natural language processing.</p>
        </div>
        <div class="card">
          <h3>Customer-First Philosophy</h3>
          <p>Our customers' trust and operational uptime drive our engineering. We stand behind every integration and deployment.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="w">
      <div class="bn">
        <div>
          <h2>Ready to automate your document workflow?</h2>
          <p>Experience the power of our IDP solution for seamless document processing and intelligent data extraction.</p>
        </div>
        <a class="b p" href="{pfx}ui2/request-demo/">Book a demo &rarr;</a>
      </div>
    </div>
  </section>
</main>
{abt_foot}
</body>
</html>"""
    save_file(rel, abt_body)

    # 10. ENTERPRISE (/ui2/enterprise/)
    rel = "ui2/enterprise/index.html"
    pfx = get_pfx(rel)
    ent_head = render_head("Enterprise AI Document Automation | Docsynecx",
                           "Scale your enterprise document processing operations with custom workflows, dedicated security, and ERP connectors.",
                           "ui2/enterprise/", pfx)
    ent_nav = render_navbar(pfx, is_route=True)
    ent_foot = render_footer(pfx)

    ent_body = f"""<!DOCTYPE html>
<html lang="en">
{ent_head}
<body>
{ent_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Enterprise Scale</span>
      <h1>AI-Powered Document Automation<br><span class="bl">for Modern Enterprises.</span></h1>
      <p class="lead">Transform complex business processes, extract real-time insights, and scale operations with enterprise-grade security, custom workflows, and multi-region compliance.</p>
      <div class="cta">
        <a class="b p" href="{pfx}ui2/request-demo/">Schedule Enterprise Consultation &rarr;</a>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <span class="ey">Enterprise Capabilities</span>
      <h2>Enterprise-Grade Reliability &amp; Control</h2>
      <div class="c3">
        <div class="card">
          <h3>Intelligent Document Processing</h3>
          <p>Advanced AI that understands context, extracts tabular data, and processes multi-page documents with human-level precision.</p>
        </div>
        <div class="card">
          <h3>Custom Workflows &amp; Logic</h3>
          <p>Create multi-tier validation rules that route documents based on monetary thresholds, entity codes, and supplier categories.</p>
        </div>
        <div class="card">
          <h3>Team Collaboration &amp; RBAC</h3>
          <p>Role-based access control, departmental segmentation, and complete visibility across approvers.</p>
        </div>
        <div class="card">
          <h3>Advanced Analytics &amp; Reporting</h3>
          <p>Identify operational bottlenecks, track processing velocity, and audit exception rates in real time.</p>
        </div>
        <div class="card">
          <h3>Enterprise Security &amp; Compliance</h3>
          <p>SOC 2 Type II compliance, encryption in transit and at rest, automated redacting, and tamper-evident audit logs.</p>
        </div>
        <div class="card">
          <h3>Dedicated Infrastructure</h3>
          <p>Multi-region cloud deployments and custom private cloud hosting to satisfy local data residency requirements.</p>
        </div>
      </div>
    </div>
  </section>
</main>
{ent_foot}
</body>
</html>"""
    save_file(rel, ent_body)

    # 11. PARTNERS (/ui2/partners/)
    rel = "ui2/partners/index.html"
    pfx = get_pfx(rel)
    prt_head = render_head("Docsynecx Partner Ecosystem | SynecxAI Labs",
                           "Partner with Docsynecx to bring AI-powered document intelligence to your accounting, ERP, and logistics clients.",
                           "ui2/partners/", pfx)
    prt_nav = render_navbar(pfx, is_route=True)
    prt_foot = render_footer(pfx)

    prt_body = f"""<!DOCTYPE html>
<html lang="en">
{prt_head}
<body>
{prt_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Partner Program</span>
      <h1>Build Better Document Workflows<br><span class="bl">Together with Docsynecx.</span></h1>
      <p class="lead">Collaborate with Docsynecx to provide intelligent automation, accounting integrations, and AI document capabilities to your clients.</p>
      <div class="cta">
        <a class="b p" href="{pfx}ui2/contact/">Become a Partner &rarr;</a>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <div class="c3">
        <div class="card">
          <h3>System Integrators</h3>
          <p>Integrate Docsynecx with existing ERP, TMS, and accounting stacks to eliminate manual data entry for your enterprise clients.</p>
        </div>
        <div class="card">
          <h3>Chartered Accountants &amp; Advisors</h3>
          <p>Accelerate tax filing, GST validation, and voucher creation for your corporate client portfolio.</p>
        </div>
        <div class="card">
          <h3>Technology Partners</h3>
          <p>Embed our document extraction and verification engines into your software via scalable REST APIs.</p>
        </div>
      </div>
    </div>
  </section>
</main>
{prt_foot}
</body>
</html>"""
    save_file(rel, prt_body)

    # 12. CONTACT (/ui2/contact/)
    rel = "ui2/contact/index.html"
    pfx = get_pfx(rel)
    cnt_head = render_head("Get in Touch with the Docsynecx Team | SynecxAI Labs",
                           "Reach out to the Docsynecx team. Contact our Coimbatore office, email sales, or send us a message.",
                           "ui2/contact/", pfx)
    cnt_nav = render_navbar(pfx, is_route=True)
    cnt_foot = render_footer(pfx)

    cnt_body = f"""<!DOCTYPE html>
<html lang="en">
{cnt_head}
<body>
{cnt_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Contact Us</span>
      <h1>We're Here to Help You<br><span class="bl">Automate Document Workflows.</span></h1>
      <p class="lead">Whether you have questions about our AI solutions, need a custom demonstration, or want to discuss enterprise licensing.</p>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start">
        <div class="card" style="padding:36px">
          <h3 style="font-size:22px;margin-bottom:16px">Send Us a Message</h3>
          <form onsubmit="alert('Thank you for contacting Docsynecx. We will respond within 24 hours.');return false" style="display:flex;flex-direction:column;gap:16px">
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px">Your Name</label>
              <input type="text" required style="width:100%;padding:12px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px">
            </div>
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px">Email Address</label>
              <input type="email" required style="width:100%;padding:12px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px">
            </div>
            <div>
              <label style="display:block;font-size:14px;font-weight:600;margin-bottom:6px">Message</label>
              <textarea rows="4" required style="width:100%;padding:12px;border:1px solid var(--line);border-radius:8px;font-family:inherit;font-size:15px"></textarea>
            </div>
            <button type="submit" class="b p" style="justify-content:center">Send Message &rarr;</button>
          </form>
        </div>

        <div>
          <div class="card" style="padding:32px;margin-bottom:24px">
            <h4 style="font-size:18px;margin-bottom:16px">Contact Information</h4>
            <div style="margin-bottom:16px">
              <small style="display:block;color:var(--muted);font-size:12px;text-transform:uppercase;font-weight:600">Email</small>
              <b style="font-size:16px">hello@docsynecx.com</b><br>
              <b style="font-size:16px">success@docsynecx.com</b>
            </div>
            <div style="margin-bottom:16px">
              <small style="display:block;color:var(--muted);font-size:12px;text-transform:uppercase;font-weight:600">Phone</small>
              <b style="font-size:16px">0422 221 2342</b><br>
              <b style="font-size:16px">+91 93447 76623</b>
            </div>
            <div>
              <small style="display:block;color:var(--muted);font-size:12px;text-transform:uppercase;font-weight:600">Office Address</small>
              <b style="font-size:16px">SynecxAI Labs Private Limited</b><br>
              <span style="color:var(--text);font-size:15px">Coimbatore, Tamil Nadu, India - 641108</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>
{cnt_foot}
</body>
</html>"""
    save_file(rel, cnt_body)

    # 13. HELP CENTER (/ui2/help/)
    rel = "ui2/help/index.html"
    pfx = get_pfx(rel)
    hlp_head = render_head("Docsynecx Help Center | Documentation & Guidance",
                           "Learn how to set up Docsynecx, connect Tally, upload invoices, and automate document workflows.",
                           "ui2/help/", pfx)
    hlp_nav = render_navbar(pfx, is_route=True)
    hlp_foot = render_footer(pfx)

    hlp_body = f"""<!DOCTYPE html>
<html lang="en">
{hlp_head}
<body>
{hlp_nav}
<main>
  <section class="rh">
    <div class="w">
      <span class="tg" style="background:none;border:none;padding:0;font-size:15px">Help &amp; Documentation</span>
      <h1>Welcome to the Docsynecx Help Center.<br><span class="bl">Guides to Get You Running.</span></h1>
      <p class="lead">Everything you need to set up your account, connect accounting middleware, upload documents, and configure validation rules.</p>
    </div>
  </section>

  <section class="band">
    <div class="w">
      <div class="c3">
        <div class="card">
          <h3>Free Trial Credits</h3>
          <p>New users receive 20 free processing credits to explore live extraction and test Tally or Zoho sync without charge.</p>
        </div>
        <div class="card">
          <h3>Connecting Accounting Software</h3>
          <p>Step-by-step instructions on setting up local middleware connectors for TallyPrime and Zoho Books OAuth.</p>
        </div>
        <div class="card">
          <h3>Validation &amp; Exception Rules</h3>
          <p>Learn how to configure GST format checks, arithmetic tolerances, duplicate detection, and purchase order matching.</p>
        </div>
      </div>
    </div>
  </section>
</main>
{hlp_foot}
</body>
</html>"""
    save_file(rel, hlp_body)

    # 14. LEGAL PAGES: Privacy Policy & Terms of Service
    for leg_slug, leg_title, leg_file in [
        ("privacy-policy", "Privacy Policy | Docsynecx", "output/privacy-policy.txt"),
        ("terms-of-service", "Terms of Service | Docsynecx", "output/terms-of-service.txt")
    ]:
        rel = f"ui2/{leg_slug}/index.html"
        pfx = get_pfx(rel)
        with open(leg_file, "r", encoding="utf-8") as f:
            raw_text = f.read()

        # Simple formatting of extracted legal copy
        paragraphs = [p.strip() for p in raw_text.split("\n\n") if p.strip() and not p.startswith("URL:") and not p.startswith("TITLE:")]
        formatted_content = "\n".join([f"<p style='margin-bottom:16px;line-height:1.7'>{p}</p>" for p in paragraphs[:15]])

        leg_head = render_head(leg_title, "Official legal documentation and policies for Docsynecx platform users.", f"ui2/{leg_slug}/", pfx)
        leg_nav = render_navbar(pfx, is_route=True)
        leg_foot = render_footer(pfx)

        leg_body = f"""<!DOCTYPE html>
<html lang="en">
{leg_head}
<body>
{leg_nav}
<main>
  <section class="rh">
    <div class="w">
      <h1>{leg_title.split('|')[0].strip()}</h1>
      <p class="lead">Last updated: October 2026 &middot; SynecxAI Labs Private Limited</p>
    </div>
  </section>
  <section class="band">
    <div class="w">
      <div class="card" style="padding:48px;max-width:900px;margin:0 auto;font-size:16px;color:var(--text)">
        {formatted_content}
      </div>
    </div>
  </section>
</main>
{leg_foot}
</body>
</html>"""
        save_file(rel, leg_body)

    # 15. 404 ERROR PAGE (/ui2/404.html)
    rel = "ui2/404.html"
    pfx = get_pfx(rel)
    err_head = render_head("Page Not Found | Docsynecx", "The requested page could not be found.", "ui2/404.html", pfx)
    err_nav = render_navbar(pfx, is_route=True)
    err_foot = render_footer(pfx)

    err_body = f"""<!DOCTYPE html>
<html lang="en">
{err_head}
<body>
{err_nav}
<main>
  <section class="rh" style="padding:120px 0 80px">
    <div class="w">
      <span class="tg">Error 404</span>
      <h1 style="margin:20px auto">Page Not Found</h1>
      <p class="lead" style="margin-bottom:32px">The page you are looking for does not exist or has been moved.</p>
      <a class="b p" href="{pfx}index2.html">Return to Home &rarr;</a>
    </div>
  </section>
</main>
{err_foot}
</body>
</html>"""
    save_file(rel, err_body)

    # 16. SITEMAP & ROBOTS
    sitemap_entries = [
        "https://docsynecx.com/index2.html",
        "https://docsynecx.com/ui2/",
        "https://docsynecx.com/ui2/invoice-processing/",
        "https://docsynecx.com/ui2/logistics-trade/",
        "https://docsynecx.com/ui2/logistics-trade/shipments/",
        "https://docsynecx.com/ui2/logistics-trade/custom-declarations/",
        "https://docsynecx.com/ui2/logistics-trade/ap-reconciliation/",
        "https://docsynecx.com/ui2/workflows/",
        "https://docsynecx.com/ui2/integration/invoice-to-tally/",
        "https://docsynecx.com/ui2/integration/zoho-books/",
        "https://docsynecx.com/ui2/integration/cargowise/",
        "https://docsynecx.com/ui2/solutions/",
        "https://docsynecx.com/ui2/solutions/banking/",
        "https://docsynecx.com/ui2/solutions/finance/",
        "https://docsynecx.com/ui2/solutions/logistics/",
        "https://docsynecx.com/ui2/solutions/accounts-payable/",
        "https://docsynecx.com/ui2/pricing/",
        "https://docsynecx.com/ui2/blog/",
        "https://docsynecx.com/ui2/request-demo/",
        "https://docsynecx.com/ui2/about/",
        "https://docsynecx.com/ui2/enterprise/",
        "https://docsynecx.com/ui2/partners/",
        "https://docsynecx.com/ui2/contact/",
        "https://docsynecx.com/ui2/help/",
        "https://docsynecx.com/ui2/privacy-policy/",
        "https://docsynecx.com/ui2/terms-of-service/"
    ]
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join([f"  <url><loc>{u}</loc><priority>0.8</priority></url>" for u in sitemap_entries]) + "\n</urlset>"
    save_file("ui2/sitemap.xml", sitemap_xml)
    save_file("ui2/robots.txt", "User-agent: *\nAllow: /\nSitemap: https://docsynecx.com/ui2/sitemap.xml\n")

    print(f"\nSuccessfully generated {len(sitemap_entries)} UI 2 pages in /ui2/ and root /index2.html!")

if __name__ == "__main__":
    generate_all()
