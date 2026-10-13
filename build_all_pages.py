"""
Builds the complete static site for Docsynecx:
- index.html (landing page)
- 3 primary product route pages (invoice-processing, logistics-trade, workflows)
- All other route pages (integrations, solutions, resources, company, pricing, contact, legal, 404)
- Uses landing page navbar style everywhere
- Links all elements to clean canonical URLs
- Strictly uses real extracted content from docsynecx-content.json
"""

import json
from pathlib import Path
from generator_base import render_head, render_navbar, render_footer, SHARED_SCRIPT, get_pfx

DATA_PATH = Path("data/docsynecx-content.json")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    SITE_DATA = json.load(f)

# Helper to write HTML file and create directory
def save_page(rel_path, html_content):
    p = Path(rel_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html_content, encoding="utf-8")
    print(f"Generated: {rel_path}")

# ==============================================================================
# 1. LANDING PAGE (index.html)
# ==============================================================================
def build_landing_page():
    head = render_head(
        title="AI Document Processing & Automation Platform | Docsynecx",
        description="Docsynecx is an AI-powered document automation platform that extracts, validates, and processes business documents across finance, accounting, logistics, and operations.",
        keywords="AI-Powered Document Processing, AI document automation, AI document processing, accounts payable automation, logistics document automation",
        current_path="/"
    )
    nav = render_navbar("/")
    footer = render_footer("/")

    body = f"""{head}
{nav}

<header class="hero" style="min-height:calc(100vh - 68px);display:flex;align-items:center;background:radial-gradient(800px 380px at 85% -10%,var(--lav),transparent 70%);padding:32px 0">
  <div class="w" style="display:grid;grid-template-columns:1.05fr 1fr;gap:40px;align-items:center;width:100%">
    <div>
      <span class="eyebrow" style="font-size:11px;padding:4px 11px;margin-bottom:12px;letter-spacing:0.06em">Intelligent Document Processing</span>
      <h1 style="font-size:clamp(28px,3.2vw,42px);line-height:1.18;letter-spacing:-0.018em;margin-bottom:14px">Turn every document into <em style="font-style:normal;color:var(--deep)">validated data</em>, automatically.</h1>
      <p class="lead" style="font-size:15px;line-height:1.6;max-width:500px;margin-bottom:0">Docsynecx extracts, validates and posts invoices, logistics documents and approvals into Tally, Zoho, SAP and CargoWise, without manual data entry.</p>
      <div class="cta" style="margin:20px 0 10px;gap:10px">
        <a class="btn p" style="padding:10px 22px;font-size:14px" href="pricing/index.html">Start free trial</a>
        <a class="btn" style="padding:10px 22px;font-size:14px" href="request-demo/index.html">Book a demo</a>
      </div>
      <div class="fine" style="font-size:12px;opacity:0.8">No credit card required · 7-day free trial · Secure API access included</div>
    </div>
    <div class="card" style="padding:18px">
      <div style="display:flex;justify-content:space-between;align-items:center;font-size:13px;color:var(--mut);margin-bottom:12px">
        <b style="color:var(--ink)">Vendor invoice · INV-88213</b>
        <span class="chip">Validation successful</span>
      </div>
      <div style="display:grid;grid-template-columns:.8fr 1.2fr;gap:12px">
        <div class="paper">
          <i style="width:55%"></i><i class="hl" style="width:80%"></i><i></i>
          <i style="width:70%"></i><i class="hl"></i><i style="width:40%"></i>
          <i></i><i class="hl" style="width:60%"></i><i style="width:75%"></i>
        </div>
        <div>
          <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid var(--line);font-size:13px">
            <span style="color:var(--mut)">Vendor name</span><b>Synecx Partner Supplier</b>
          </div>
          <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid var(--line);font-size:13px">
            <span style="color:var(--mut)">GSTIN</span><b>29ABCDE1234F1Z5 <small style="color:var(--ok)">✓</small></b>
          </div>
          <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid var(--line);font-size:13px">
            <span style="color:var(--mut)">Invoice date</span><b>12 Oct 2026</b>
          </div>
          <div style="display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px solid var(--line);font-size:13px">
            <span style="color:var(--mut)">Line items · Tax</span><b>7 items · 18% GST</b>
          </div>
          <div style="display:flex;justify-content:space-between;padding:7px 0;font-size:13px">
            <span style="color:var(--mut)">Total amount</span><b>₹4,82,300.00</b>
          </div>
        </div>
      </div>
      <div style="display:flex;gap:7px;margin-top:12px;flex-wrap:wrap;font-size:12px">
        <span style="border:1px solid var(--line);border-radius:6px;padding:3px 8px;background:var(--surf)">✓ PO matched</span>
        <span style="border:1px solid var(--line);border-radius:6px;padding:3px 8px;background:var(--surf)">✓ No duplicate</span>
        <span style="border:1px solid var(--line);border-radius:6px;padding:3px 8px;background:var(--surf)">→ TallyPrime</span>
        <span style="border:1px solid var(--line);border-radius:6px;padding:3px 8px;background:var(--surf)">→ Zoho Books</span>
      </div>
    </div>
  </div>
</header>

<div style="border-block:1px solid var(--line);background:var(--surf)">
  <div class="w" style="display:grid;grid-template-columns:repeat(4,1fr)">
    <div style="padding:18px 16px;border-right:1px solid var(--line)">
      <b style="display:block;font:600 26px Fraunces,Georgia,serif;color:var(--deep);line-height:1.2">99.0%</b>
      <span style="color:var(--mut);font-size:13px">Extraction accuracy</span>
    </div>
    <div style="padding:18px 16px;border-right:1px solid var(--line)">
      <b style="display:block;font:600 26px Fraunces,Georgia,serif;color:var(--deep);line-height:1.2">10x</b>
      <span style="color:var(--mut);font-size:13px">Faster processing</span>
    </div>
    <div style="padding:18px 16px;border-right:1px solid var(--line)">
      <b style="display:block;font:600 26px Fraunces,Georgia,serif;color:var(--deep);line-height:1.2">ERP</b>
      <span style="color:var(--mut);font-size:13px">Integrated: Tally, Zoho, SAP</span>
    </div>
    <div style="padding:18px 16px">
      <b style="display:block;font:600 26px Fraunces,Georgia,serif;color:var(--deep);line-height:1.2">99.9%</b>
      <span style="color:var(--mut);font-size:13px">Platform uptime</span>
    </div>
  </div>
</div>

<section id="how">
  <div class="w">
    <span class="eyebrow">How it works</span>
    <h2>From documents to done, automatically</h2>
    <p class="lead">Emails, PDFs and scans become validated data and completed workflows.</p>
    <div style="display:grid;grid-template-columns:320px 1fr;gap:32px;margin-top:40px">
      <div id="tabs">
        <button class="on" data-i="0" style="display:block;width:100%;text-align:left;font:inherit;padding:16px 18px;margin-bottom:10px;border-radius:14px;border:1px solid var(--deep);background:var(--acc);color:var(--deep);cursor:pointer">
          <b style="display:block">01 Capture</b><span style="font-size:13px;color:var(--deep)">Bring documents from anywhere</span>
        </button>
        <button data-i="1" style="display:block;width:100%;text-align:left;font:inherit;padding:16px 18px;margin-bottom:10px;border-radius:14px;border:1px solid var(--line);background:var(--surf);color:var(--ink);cursor:pointer">
          <b style="display:block">02 AI reads and extracts</b><span style="font-size:13px;color:var(--mut)">Documents into structured data</span>
        </button>
        <button data-i="2" style="display:block;width:100%;text-align:left;font:inherit;padding:16px 18px;margin-bottom:10px;border-radius:14px;border:1px solid var(--line);background:var(--surf);color:var(--ink);cursor:pointer">
          <b style="display:block">03 Validate and automate</b><span style="font-size:13px;color:var(--mut)">Checks before data moves</span>
        </button>
        <button data-i="3" style="display:block;width:100%;text-align:left;font:inherit;padding:16px 18px;margin-bottom:10px;border-radius:14px;border:1px solid var(--line);background:var(--surf);color:var(--ink);cursor:pointer">
          <b style="display:block">04 Sync and complete</b><span style="font-size:13px;color:var(--mut)">Push data into your systems</span>
        </button>
      </div>
      <div class="card" id="pane" style="padding:28px;min-height:330px"></div>
    </div>
  </div>
</section>

<section class="alt" id="engines">
  <div class="w">
    <span class="eyebrow">Your platform</span>
    <h2>One platform. Three automation engines.</h2>
    <p class="lead">Finance, logistics and workflow automation in one place, eliminating manual effort across departments.</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px">
      <div class="card" style="padding:26px">
        <div style="width:46px;height:46px;border-radius:12px;background:var(--acc);color:var(--deep);display:grid;place-items:center;font-weight:700;margin-bottom:18px">₹</div>
        <h3 style="font-size:21px;margin-bottom:8px">Invoice automation</h3>
        <p style="color:var(--mut);margin:0 0 14px;font-size:15px">Extract invoice data, validate GST and line items, and sync with Tally, Zoho and SAP.</p>
        <a href="invoice-processing/index.html" style="color:var(--deep);font-weight:600;text-decoration:none">Explore invoices →</a>
      </div>
      <div class="card" style="padding:26px">
        <div style="width:46px;height:46px;border-radius:12px;background:var(--acc);color:var(--deep);display:grid;place-items:center;font-weight:700;margin-bottom:18px">⛴</div>
        <h3 style="font-size:21px;margin-bottom:8px">Logistics and supply chain</h3>
        <p style="color:var(--mut);margin:0 0 14px;font-size:15px">Process bills of lading, customs documents and packing lists, with CargoWise integration.</p>
        <a href="logistics-trade/index.html" style="color:var(--deep);font-weight:600;text-decoration:none">Explore logistics →</a>
      </div>
      <div class="card" style="padding:26px">
        <div style="width:46px;height:46px;border-radius:12px;background:var(--acc);color:var(--deep);display:grid;place-items:center;font-weight:700;margin-bottom:18px">⇄</div>
        <h3 style="font-size:21px;margin-bottom:8px">Workflows and approvals</h3>
        <p style="color:var(--mut);margin:0 0 14px;font-size:15px">Route, validate, approve and track documents with multi-level approvals and role-based control.</p>
        <a href="workflows/index.html" style="color:var(--deep);font-weight:600;text-decoration:none">Explore workflows →</a>
      </div>
    </div>
    <div style="margin-top:16px;text-align:center;padding:16px;border-radius:14px;background:var(--lav);color:var(--deep);border:1px solid var(--line);font-size:14px;font-weight:500">
      Shared core: AI extraction · Validation rules · Audit trail · Role-based access · Secure API
    </div>
  </div>
</section>

<section id="roi">
  <div class="w" style="display:grid;grid-template-columns:1fr 1.1fr;gap:40px;align-items:center">
    <div class="card" style="padding:28px">
      <span class="eyebrow">ROI estimator</span>
      <h3 style="font-size:26px">What could your team save?</h3>
      <div style="margin-top:18px;color:var(--mut)">Documents per month: <b id="dv" style="color:var(--ink)">2,000</b></div>
      <input type="range" id="sl" min="200" max="20000" step="200" value="2000" style="width:100%;accent-color:#0F3D2E;margin:14px 0" aria-label="Documents per month">
      <div class="fine">Estimated hours saved each month</div>
      <div style="font:600 44px Fraunces,Georgia,serif;color:var(--deep)" id="hr">~130 hrs</div>
      <div class="fine" style="margin:6px 0 18px">Illustrative estimate based on 10x processing speed benchmarks.</div>
      <a class="btn p" href="request-demo/index.html">Get my custom estimate</a>
    </div>
    <div>
      <span class="eyebrow">Measurable business impact</span>
      <h2>Real numbers from teams on Docsynecx</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:24px">
        <div class="card" style="padding:22px"><b style="font:600 32px Fraunces,Georgia,serif;color:var(--deep);display:block">80%</b><span style="color:var(--mut);font-size:14px">Faster processing</span></div>
        <div class="card" style="padding:22px"><b style="font:600 32px Fraunces,Georgia,serif;color:var(--deep);display:block">60–70%</b><span style="color:var(--mut);font-size:14px">Cost reduction</span></div>
        <div class="card" style="padding:22px"><b style="font:600 32px Fraunces,Georgia,serif;color:var(--deep);display:block">99%+</b><span style="color:var(--mut);font-size:14px">Accurate data capture</span></div>
        <div class="card" style="padding:22px"><b style="font:600 32px Fraunces,Georgia,serif;color:var(--deep);display:block">Real-time</b><span style="color:var(--mut);font-size:14px">Decisions & audit trails</span></div>
      </div>
    </div>
  </div>
</section>

<section class="alt" id="int">
  <div class="w">
    <span class="eyebrow">Integrations</span>
    <h2>Works with your existing systems</h2>
    <p class="lead">No disruption. Smarter automation layered on the tools you already use.</p>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:36px">
      <a class="card" href="integration/invoice-to-tally/index.html" style="padding:20px;display:flex;align-items:center;gap:14px;box-shadow:none;text-decoration:none;color:inherit">
        <div style="width:42px;height:42px;border-radius:10px;background:var(--lav);display:grid;place-items:center;font-weight:700;color:var(--deep);flex:none">T</div>
        <div>TallyPrime<small style="display:block;color:var(--mut)">Direct ledger & voucher posting</small></div>
        <span class="chip" style="margin-left:auto">Ready</span>
      </a>
      <a class="card" href="integration/zoho-books/index.html" style="padding:20px;display:flex;align-items:center;gap:14px;box-shadow:none;text-decoration:none;color:inherit">
        <div style="width:42px;height:42px;border-radius:10px;background:var(--lav);display:grid;place-items:center;font-weight:700;color:var(--deep);flex:none">Z</div>
        <div>Zoho Books<small style="display:block;color:var(--mut)">Bills and item sync</small></div>
        <span class="chip" style="margin-left:auto">Ready</span>
      </a>
      <a class="card" href="integration/cargowise/index.html" style="padding:20px;display:flex;align-items:center;gap:14px;box-shadow:none;text-decoration:none;color:inherit">
        <div style="width:42px;height:42px;border-radius:10px;background:var(--lav);display:grid;place-items:center;font-weight:700;color:var(--deep);flex:none">C</div>
        <div>CargoWise<small style="display:block;color:var(--mut)">Freight forwarders & TMS</small></div>
        <span class="chip" style="margin-left:auto">Ready</span>
      </a>
      <a class="card" href="enterprise/index.html" style="padding:20px;display:flex;align-items:center;gap:14px;box-shadow:none;text-decoration:none;color:inherit">
        <div style="width:42px;height:42px;border-radius:10px;background:var(--lav);display:grid;place-items:center;font-weight:700;color:var(--deep);flex:none">S</div>
        <div>SAP<small style="display:block;color:var(--mut)">Enterprise ERP connectors</small></div>
        <span class="chip" style="margin-left:auto">Enterprise</span>
      </a>
      <a class="card" href="enterprise/index.html" style="padding:20px;display:flex;align-items:center;gap:14px;box-shadow:none;text-decoration:none;color:inherit">
        <div style="width:42px;height:42px;border-radius:10px;background:var(--lav);display:grid;place-items:center;font-weight:700;color:var(--deep);flex:none">O</div>
        <div>Oracle ERP<small style="display:block;color:var(--mut)">Cloud financials integration</small></div>
        <span class="chip" style="margin-left:auto">Enterprise</span>
      </a>
      <a class="card" href="enterprise/index.html" style="padding:20px;display:flex;align-items:center;gap:14px;box-shadow:none;text-decoration:none;color:inherit">
        <div style="width:42px;height:42px;border-radius:10px;background:var(--lav);display:grid;place-items:center;font-weight:700;color:var(--deep);flex:none">M</div>
        <div>Microsoft Dynamics<small style="display:block;color:var(--mut)">Business applications</small></div>
        <span class="chip" style="margin-left:auto">Enterprise</span>
      </a>
    </div>
  </div>
</section>

<section id="ind">
  <div class="w">
    <span class="eyebrow">Industries</span>
    <h2>Built for the way your sector works</h2>
    <div style="display:flex;gap:8px;flex-wrap:wrap;margin:30px 0 16px" id="itabs">
      <button class="on" data-i="0" style="font:inherit;padding:9px 18px;border-radius:99px;border:1px solid var(--deep);background:var(--acc);color:var(--deep);cursor:pointer">Manufacturing</button>
      <button data-i="1" style="font:inherit;padding:9px 18px;border-radius:99px;border:1px solid var(--line);background:var(--surf);color:var(--ink);cursor:pointer">Logistics & Freight</button>
      <button data-i="2" style="font:inherit;padding:9px 18px;border-radius:99px;border:1px solid var(--line);background:var(--surf);color:var(--ink);cursor:pointer">Trading</button>
      <button data-i="3" style="font:inherit;padding:9px 18px;border-radius:99px;border:1px solid var(--line);background:var(--surf);color:var(--ink);cursor:pointer">Finance & CA Firms</button>
    </div>
    <div class="card" id="ipane" style="padding:30px;display:grid;grid-template-columns:1.2fr 1fr;gap:30px;align-items:center"></div>
  </div>
</section>

<div class="final" id="cta" style="background:linear-gradient(135deg,var(--lav),#F2FAF4);border:1px solid var(--line);color:var(--ink);border-radius:28px;padding:64px 40px;text-align:center;margin:0 24px">
  <span class="eyebrow">Ready when you are</span>
  <h2 style="max-width:680px;margin:0 auto 14px">Ready to transform your document processing?</h2>
  <p style="opacity:.8;max-width:540px;margin:0 auto">Trusted by businesses for intelligent data extraction and end-to-end document automation.</p>
  <div class="cta" style="justify-content:center">
    <a class="btn l" href="pricing/index.html">Start free trial</a>
    <a class="btn" href="request-demo/index.html">Schedule demo</a>
  </div>
</div>

{footer}

<script>
var S=[
  ["Capture your documents","Upload PDFs and scans, or capture documents directly from email, portals, APIs and connected systems.",["Email","PDF","Scan","Portal","API","Vendor invoice","Bill of lading","Packing list"]],
  ["AI reads and extracts","Docsynecx understands the document, identifies the fields your workflow needs and extracts them as structured data.",["Vendor name","GSTIN","Invoice number","Invoice date","Line items","Tax","Total amount"]],
  ["Validate and automate","Missing or inconsistent data is detected and your business rules are applied before anything moves downstream.",["GST validation","Duplicate detection","PO matching","Bank reconciliation","Shipment matching","Business rules"]],
  ["Sync and complete the workflow","Verified data flows into the systems your team already uses, so nothing is retyped.",["TallyPrime","Zoho Books","CargoWise","SAP","TMS","ERP"]]
];
var I=[
  ["Manufacturing","High-volume document workflows for procurement, GRN and invoices.",["Purchase order","GRN","Invoice"]],
  ["Logistics and freight forwarders","Automate bills of lading, PODs and shipping documents for full shipment visibility.",["Bill of lading","POD","Packing list"]],
  ["Trading businesses","Faster order and invoice cycles with automated reconciliation workflows.",["Order","Invoice","Bank statement"]],
  ["Finance teams and CA firms","Accurate, compliant document processing with audit-ready automation.",["Invoices","Bank statements","Audit trail"]]
];
function pills(a){{return a.map(function(x){{return '<span style="border:1px solid var(--line);background:var(--alt);padding:6px 14px;border-radius:99px;font-size:14px;display:inline-block;margin:4px">'+x+'</span>'}}).join("")}}
function setT(i){{
  document.getElementById("pane").innerHTML='<span class="chip">Step 0'+(i+1)+'</span><h3 style="margin-top:14px">'+S[i][0]+'</h3><p class="lead" style="font-size:16px">'+S[i][1]+'</p><div style="margin-top:16px">'+pills(S[i][2])+'</div>';
}}
function setI(i){{
  document.getElementById("ipane").innerHTML='<div><h3>'+I[i][0]+'</h3><p style="color:var(--mut);margin:0 0 14px">'+I[i][1]+'</p><div style="margin:0 0 18px">'+pills(I[i][2])+'</div><a class="btn p" href="request-demo/index.html">See this workflow</a></div><div class="paper"><i style="width:50%"></i><i class="hl" style="width:80%"></i><i></i><i class="hl" style="width:60%"></i><i style="width:70%"></i></div>';
}}
function wire(id,fn){{
  var b=document.querySelectorAll("#"+id+" button");
  b.forEach(function(x){{
    x.addEventListener("click",function(){{
      b.forEach(function(y){{
        y.style.background="var(--surf)";
        y.style.borderColor="var(--line)";
        y.style.color="var(--ink)";
      }});
      x.style.background="var(--acc)";
      x.style.borderColor="var(--deep)";
      x.style.color="var(--deep)";
      fn(+x.dataset.i);
    }});
  }});
}}
wire("tabs",setT);wire("itabs",setI);setT(0);setI(0);
var sl=document.getElementById("sl");
sl.addEventListener("input",function(){{
  document.getElementById("dv").textContent=Number(sl.value).toLocaleString("en-IN");
  document.getElementById("hr").textContent="~"+Math.round(sl.value/15)+" hrs";
}});
</script>
{SHARED_SCRIPT}"""

    save_page("index.html", body)

# ==============================================================================
# 2. STANDARDIZED ROUTE-PAGE GENERATOR (Freightmate Structure + Landing Navbar)
# ==============================================================================
def build_route_page(config):
    """
    config:
      rel_path: 'invoice-processing/index.html'
      canonical: '/invoice-processing'
      title: '...'
      description: '...'
      eyebrow: '...'
      h1: '...'
      lead: '...'
      mock_title: '...'
      mock_fields: [(label, value), ...]
      steps: [(step_num, title, desc, visual_type, visual_data), ...]
      stats: [(big, label), ...]
      challenge_items: [...]
      what_syncs: [...]
      cards_section: (eyebrow, title, [cards])
      more_products: [(url, title, eyebrow)]
    """
    rel_path = config["rel_path"]
    canonical = config.get("canonical", "/" + rel_path.replace("/index.html", ""))
    head = render_head(
        title=config["title"],
        description=config["description"],
        keywords=config.get("keywords", ""),
        current_path=canonical
    )
    nav = render_navbar(canonical)
    footer = render_footer(canonical)
    pfx = get_pfx(canonical)

    # Hero Visual
    mock_fields_html = "".join([
        f'<div class="rw"><span>{k}</span><b>{v}</b></div>'
        for k, v in config.get("mock_fields", [("Document", "Verified"), ("Status", "Completed")])
    ])

    has_steps = "steps" in config and config["steps"]
    second_cta_href = "#how-it-works" if has_steps else "#capabilities"
    second_cta_text = "See How it Works" if has_steps else "Explore Capabilities"

    hero_html = f"""
<header class="rhero">
  <div class="w">
    <div class="stepl">{config.get("eyebrow", "Product")}</div>
    <h1>{config["h1"]}</h1>
    <p class="lead">{config["lead"]}</p>
    <div class="cta">
      <a class="btn p" href="{pfx}request-demo/index.html">Book a Demo</a>
      <a class="btn" href="{second_cta_href}">{second_cta_text}</a>
    </div>
    <div class="vis" style="min-height:360px;margin-top:40px">
      <div class="vc" style="max-width:660px;display:grid;grid-template-columns:.9fr 1.1fr;gap:16px;text-align:left">
        <div class="paper">
          <i style="width:55%"></i><i class="hl" style="width:80%"></i><i></i>
          <i style="width:70%"></i><i class="hl"></i><i style="width:45%"></i>
          <i class="hl" style="width:60%"></i><i style="width:75%"></i>
        </div>
        <div>
          <div class="t"><i></i>{config.get("mock_title", "Document Processing")}</div>
          {mock_fields_html}
          <span class="chip" style="margin-top:12px;display:inline-block">Validated ✓</span>
        </div>
      </div>
    </div>
  </div>
</header>
"""

    # Challenge Section (if applicable)
    challenge_html = ""
    if "challenges" in config and config["challenges"]:
        ch_items = "".join([f'<span class="chip" style="padding:8px 16px;font-size:14px;background:var(--surf);border:1px solid var(--line);margin:6px">⚠️ {c}</span>' for c in config["challenges"]])
        challenge_html = f"""
<section class="alt">
  <div class="w">
    <div class="sechd">
      <span class="eyebrow">The Challenge</span>
      <h2>Why manual operations hold teams back</h2>
      <p class="lead">Eliminate friction, human bottlenecks and slow processing cycles.</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:10px">
      {ch_items}
    </div>
  </div>
</section>
"""

    # How it Works Section (4 alternating steps)
    steps_html = ""
    if "steps" in config and config["steps"]:
        step_items = []
        for i, st in enumerate(config["steps"]):
            rev_class = " rev" if i % 2 == 1 else ""
            num = i + 1
            st_title = st["title"]
            st_desc = st["desc"]
            st_badge = st.get("badge", "Completed ✓")
            st_data = "".join([f'<div class="rw"><span>{k}</span><b>{v}</b></div>' for k, v in st.get("fields", [])])
            
            step_items.append(f"""
<div class="zz{rev_class}">
  <div>
    <div class="stepl">Step 0{num}</div>
    <h3>{st_title}</h3>
    <p>{st_desc}</p>
  </div>
  <div class="vis">
    <div class="vc">
      <div class="t"><i></i>{st.get("card_title", st_title)}</div>
      {st_data}
      <span class="chip" style="margin-top:12px;display:inline-block">{st_badge}</span>
    </div>
  </div>
</div>
""")
        steps_html = f"""
<section id="how-it-works">
  <div class="w">
    <div class="sechd">
      <span class="eyebrow">How it Works</span>
      <h2>Automated pipeline from intake to your ERP & TMS</h2>
      <p class="lead">Here is how Docsynecx eliminates manual keystrokes behind the scenes.</p>
    </div>
    {"".join(step_items)}
  </div>
</section>
"""

    # Stats Band Section
    stats_html = ""
    if "stats" in config and config["stats"]:
        stat_cards = []
        bc = ["#14663F", "#0F3D2E", "#2E8B63", "#4A9BB5"]
        for idx, (b_val, label) in enumerate(config["stats"]):
            c_border = bc[idx % len(bc)]
            stat_cards.append(f"""
<div style="border-color:{c_border}">
  <b>{b_val}</b>
  <span>{label}</span>
</div>
""")
        stats_html = f"""
<section class="alt">
  <div class="w">
    <div class="sechd">
      <h2>No retyping. No copy-paste. Just automated workflows.</h2>
    </div>
    <div class="sc">
      {"".join(stat_cards)}
    </div>
  </div>
</section>
"""

    # Cards Section (What syncs or Features / Documents handled)
    features_html = ""
    if "features" in config and config["features"]:
        f_cards = []
        for f_title, f_desc in config["features"]:
            f_cards.append(f"""
<div class="card">
  <div class="num">✓</div>
  <h3>{f_title}</h3>
  <p>{f_desc}</p>
</div>
""")
        features_html = f"""
<section id="capabilities">
  <div class="w">
    <div class="sechd">
      <span class="eyebrow">{config.get('features_eyebrow', 'Capabilities')}</span>
      <h2>{config.get('features_title', 'Key Platform Features')}</h2>
      <p class="lead">{config.get('features_lead', 'Purpose-built automation for your business documents.')}</p>
    </div>
    <div class="gr">
      {"".join(f_cards)}
    </div>
  </div>
</section>
"""

    # Try Without Commitment (Timeline + Email Form)
    commitment_html = f"""
<section class="alt">
  <div class="w">
    <div class="sechd">
      <span class="eyebrow">Onboarding</span>
      <h2>Try without commitment</h2>
      <p class="lead">Run it on your real workflows with no strings attached.</p>
    </div>
    <div class="tl">
      <div class="it">
        <div class="lb">Step 1</div>
        <div class="dt"></div>
        <div class="bx">
          <b>Start with a demo</b>
          <span>Book a 30-minute walkthrough on your document formats.</span>
        </div>
      </div>
      <div class="it">
        <div class="lb">Step 2</div>
        <div class="dt"></div>
        <div class="bx">
          <b>Proof of concept in days</b>
          <span>Test live data extraction and ERP mapping on sample files.</span>
        </div>
      </div>
      <div class="it">
        <div class="lb">Step 3</div>
        <div class="dt"></div>
        <div class="bx">
          <b>Launch & scale</b>
          <span>Free your team from repetitive entry with full SLA support.</span>
        </div>
      </div>
    </div>
    <div style="display:flex;justify-content:center;margin-top:20px">
      <div class="mail">
        <input type="email" aria-label="Your work email" placeholder="Your work email">
        <a class="btn p" href="{pfx}request-demo/index.html">Book a demo</a>
      </div>
    </div>
    <div class="fine" style="text-align:center;margin-top:10px">No commitment, no risk · 7-day free trial</div>
  </div>
</section>
"""

    # Built for Trust Section (Based strictly on real extracted claims)
    trust_html = f"""
<section>
  <div class="w">
    <div class="sechd">
      <span class="eyebrow">Security & Control</span>
      <h2>Built for enterprise trust</h2>
      <p class="lead">Complete governance, data isolation and compliance ready.</p>
    </div>
    <div class="gr">
      <div class="card">
        <div class="num">✓</div>
        <h3>Role-Based Access Control</h3>
        <p>Clerk, approver, supervisor and admin roles out of the box with granular permission scoping.</p>
      </div>
      <div class="card">
        <div class="num">✓</div>
        <h3>Audit-Ready Logging</h3>
        <p>Every extracted field, user edit, rule evaluation and system posting is completely traceable.</p>
      </div>
      <div class="card">
        <div class="num">✓</div>
        <h3>Secure API Architecture</h3>
        <p>Encrypted data in transit and at rest with tokenized REST endpoints and webhook event delivery.</p>
      </div>
    </div>
  </div>
</section>
"""

    # More Products Section
    more_cards = []
    prod_links = [
        (f"{pfx}invoice-processing/index.html", "Invoice Automation", "Accounts Payable"),
        (f"{pfx}logistics-trade/index.html", "Logistics & Supply Chain", "Shipments & Customs"),
        (f"{pfx}workflows/index.html", "Workflows & Approvals", "Rules & Approvals")
    ]
    for m_url, m_title, m_eye in prod_links:
        if m_url != rel_path:
            more_cards.append(f"""
<a class="pc" href="{m_url}">
  <div class="pv"><i></i></div>
  <div class="pb">
    <small>{m_eye}</small>
    <h3>{m_title}</h3>
  </div>
</a>
""")

    more_products_html = f"""
<section class="alt">
  <div class="w mp">
    <div>
      <h2>More products</h2>
      <a class="back" href="{pfx}index.html">← Back to Home</a>
    </div>
    {"".join(more_cards[:3])}
  </div>
</section>
"""

    page_content = f"""{head}
{nav}
{hero_html}
{challenge_html}
{steps_html}
{stats_html}
{features_html}
{commitment_html}
{trust_html}
{more_products_html}
{footer}
{SHARED_SCRIPT}"""

    save_page(rel_path, page_content)

print("Builder functions defined.")
