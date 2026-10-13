# Docsynecx Website

AI-powered document processing and automation platform for invoices, logistics documents, and approval workflows.

---

## Project Architecture & Design System

1. **Design System & Tokens:**
   - Central CSS design token file: [`css/tokens.css`](css/tokens.css).
   - Single source of truth for colors (`--bg`, `--surf`, `--alt`, `--ink`, `--mut`, `--line`, `--deep`, `--acc`, `--lav`, `--ok`, `--warn`), typography (`Fraunces` headings, `Inter` body/UI), pill buttons, 18px card radii, and focus outlines.
   - **Unified Navbar:** The landing page navbar layout and styling is used uniformly across the entire site, including on all product, integration, solution, resource, and legal route pages.

2. **Data-Driven Architecture:**
   - Content extracted from live site: [`data/docsynecx-content.json`](data/docsynecx-content.json).
   - Python generator scripts:
     - [`generator_base.py`](generator_base.py) — Header, unified landing-style navbar, footer components.
     - [`build_all_pages.py`](build_all_pages.py) — Route page template engines.
     - [`generate_site.py`](generate_site.py) — Multi-page build script.

---

## How to Run the Website Locally

Since the site is standard static multi-page HTML/CSS/JS, no heavy node server is required:

```powershell
# Option 1: Python built-in HTTP server
python -m http.server 8080

# Option 2: Run directly in browser
# Open index.html in any modern web browser
```

---

## How to Add a New Page

1. Open [`generate_site.py`](generate_site.py).
2. Call `build_route_page({...})` with your page parameters:
   ```python
   build_route_page({
       "rel_path": "new-category/my-page/index.html",
       "canonical": "/new-category/my-page",
       "title": "Page Title | Docsynecx",
       "description": "Meta description...",
       "eyebrow": "Category",
       "h1": "Main Headline",
       "lead": "Subheading description",
       "mock_title": "Visual Title",
       "mock_fields": [("Field 1", "Value 1"), ("Field 2", "Value 2")],
       "features": [("Feature A", "Description A")]
   })
   ```
3. Re-run:
   ```powershell
   python generate_site.py
   ```
4. The page is automatically generated at its clean URL path and linked into [`sitemap.xml`](sitemap.xml).

---

## Quality & Acceptance Verifications

- **Link Audit:** Checked across all 38 generated HTML pages (1,810 links verified):
  - **Broken Internal Links:** 0
  - **Placeholder `#` Links:** 0
- **Responsive Testing:** Tested and verified across Mobile (390px), Tablet (768px), and Desktop (1440px) with screenshots saved in [`screenshots/`](screenshots/).
- **Fact Integrity:** Adheres strictly to [`data/docsynecx-content.json`](data/docsynecx-content.json). All missing assets and omitted prototype videos/claims are documented in [`MISSING_CONTENT.md`](MISSING_CONTENT.md).
