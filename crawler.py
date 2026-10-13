"""
Docsynecx.com Web Crawler
=========================
Crawls every page on https://docsynecx.com/ using Playwright (headless Chromium),
extracts clean text content, and saves one .txt file per page.

Usage:
    python crawler.py

Requirements:
    pip install -r requirements.txt
    playwright install chromium
"""

import asyncio
import re
import time
import logging
from pathlib import Path
from urllib.parse import urlparse, urljoin, urlunparse
from collections import deque

from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
from bs4 import BeautifulSoup, Tag

# ──────────────────────────────────────────────────────────────────────────────
# Configuration
# ──────────────────────────────────────────────────────────────────────────────

BASE_URL = "https://docsynecx.com"
BASE_DOMAIN = "docsynecx.com"
OUTPUT_DIR = Path("output")

# Known routes to seed the queue (in addition to discovery)
SEED_PATHS = [
    "/",
    "/solutions",
    "/pricing",
    "/blog",
    "/request-demo",
    "/invoice-processing",
    "/logistics-trade",
    "/logistics-trade/shipments",
    "/logistics-trade/custom-declarations",
    "/logistics-trade/ap-reconciliation",
    "/workflows",
    "/integration/invoice-to-tally",
    "/integration/zoho-books",
    "/integration/cargowise",
    "/about",
    "/enterprise",
    "/partners",
    "/contact",
    "/privacy-policy",
    "/terms-of-service",
    "/help",
]

# Extensions to skip
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".zip", ".tar", ".gz",
    ".mp4", ".mp3", ".wav", ".avi", ".mov", ".woff", ".woff2", ".ttf", ".eot", ".css", ".js",
}

# Subdomains / external domains to skip
SKIP_DOMAINS = {
    "invoice.docsynecx.com",
    "www.linkedin.com", "linkedin.com",
    "www.instagram.com", "instagram.com",
    "www.facebook.com", "facebook.com",
    "www.youtube.com", "youtube.com",
    "twitter.com", "x.com",
}

DELAY_BETWEEN_REQUESTS = 1.0   # seconds
MAX_RETRIES = 2
NETWORK_IDLE_TIMEOUT = 20_000  # ms

# ──────────────────────────────────────────────────────────────────────────────
# Logging
# ──────────────────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("crawler")

# ──────────────────────────────────────────────────────────────────────────────
# URL helpers
# ──────────────────────────────────────────────────────────────────────────────

def normalize_url(url: str, base: str = BASE_URL) -> str | None:
    """
    Resolve relative URL, strip fragments, query strings, trailing slashes.
    Returns None for URLs we should skip.
    """
    try:
        url = url.strip()
        if not url or url.startswith("mailto:") or url.startswith("tel:") or url.startswith("javascript:"):
            return None

        parsed = urlparse(urljoin(base, url))

        # Must be http/https
        if parsed.scheme not in ("http", "https"):
            return None

        domain = parsed.netloc.lower().removeprefix("www.")

        # Must be on our domain (not a subdomain we skip)
        if domain != BASE_DOMAIN and parsed.netloc.lower() in SKIP_DOMAINS:
            return None
        if domain != BASE_DOMAIN:
            return None

        # Skip asset files
        path_lower = parsed.path.lower()
        if any(path_lower.endswith(ext) for ext in SKIP_EXTENSIONS):
            return None

        # Rebuild: scheme + netloc + path (strip trailing slash unless root)
        clean_path = parsed.path.rstrip("/") or "/"
        clean = urlunparse((parsed.scheme, parsed.netloc, clean_path, "", "", ""))
        return clean
    except Exception:
        return None


def url_to_filename(url: str) -> str:
    """Convert a URL to a safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip("/")

    if not path:
        return "landing_page.txt"

    # blog articles get blog_ prefix
    if path.startswith("blog/"):
        slug = path[len("blog/"):].replace("/", "_")
        return f"blog_{slug}.txt"

    # Replace slashes with underscores
    name = path.replace("/", "_")
    return f"{name}.txt"


# ──────────────────────────────────────────────────────────────────────────────
# HTML → text extraction
# ──────────────────────────────────────────────────────────────────────────────

# Tags whose inner text we want to extract as structured content
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}

# Tags that form a natural block break
BLOCK_TAGS = {"p", "li", "td", "th", "dt", "dd", "figcaption", "blockquote", "caption"}

# Tags that are always skipped during body extraction
ALWAYS_SKIP = {"script", "style", "noscript", "head", "meta", "link", "template", "svg", "path"}


def _soup_text(tag: Tag) -> str:
    """Return inner text of a BS4 tag, collapsing whitespace."""
    return re.sub(r"\s+", " ", tag.get_text(separator=" ")).strip()


def extract_nav_footer(soup: BeautifulSoup) -> str:
    """Extract text from nav and footer elements."""
    parts = []
    for sel in ["nav", "header", "footer", '[role="navigation"]']:
        for el in soup.select(sel):
            txt = _soup_text(el)
            if txt:
                parts.append(txt)
    return "\n\n".join(dict.fromkeys(parts))  # dedupe preserving order


def extract_body_content(soup: BeautifulSoup) -> str:
    """
    Extract main page content excluding nav/header/footer.
    Preserves heading hierarchy and reading order.
    """
    # Remove nav, header, footer, and utility tags
    for tag in soup.find_all(["nav", "header", "footer", "script", "style",
                               "noscript", "svg", "path", "link", "meta", "template"]):
        tag.decompose()

    lines = []

    def walk(node):
        if not isinstance(node, Tag):
            return
        tag_name = node.name.lower() if node.name else ""

        if tag_name in ALWAYS_SKIP:
            return

        if tag_name in HEADING_TAGS:
            txt = _soup_text(node)
            if txt:
                level = int(tag_name[1])
                prefix = "#" * level
                lines.append(f"\n{prefix} {txt}")
            return  # don't recurse into heading again

        if tag_name == "table":
            _extract_table(node, lines)
            return

        if tag_name == "ul" or tag_name == "ol":
            for li in node.find_all("li", recursive=False):
                txt = _soup_text(li)
                if txt:
                    lines.append(f"  • {txt}")
            return

        if tag_name in ("p", "blockquote", "figcaption"):
            txt = _soup_text(node)
            if txt:
                lines.append(txt)
            return

        if tag_name in ("a", "button", "span") and node.get("class"):
            # Capture CTA / button text when it's a standalone element
            classes = " ".join(node.get("class", []))
            if any(kw in classes.lower() for kw in ("btn", "button", "cta", "link")):
                txt = _soup_text(node)
                if txt:
                    lines.append(f"[CTA] {txt}")
                return

        # Recurse into children
        for child in node.children:
            walk(child)

    # Find main content area; fall back to body
    main = (
        soup.find("main")
        or soup.find(id=re.compile(r"(content|main|app)", re.I))
        or soup.find(attrs={"role": "main"})
        or soup.find("body")
    )

    if main:
        walk(main)

    # Clean up: collapse blank lines
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text


def _extract_table(table_tag: Tag, lines: list[str]):
    """Convert an HTML table into readable rows."""
    rows = table_tag.find_all("tr")
    for row in rows:
        cells = [_soup_text(c) for c in row.find_all(["td", "th"])]
        if any(cells):
            lines.append(" | ".join(cells))


# ──────────────────────────────────────────────────────────────────────────────
# Meta extraction
# ──────────────────────────────────────────────────────────────────────────────

def extract_meta(soup: BeautifulSoup, url: str) -> dict:
    title_tag = soup.find("title")
    title = _soup_text(title_tag) if title_tag else ""

    desc_tag = soup.find("meta", attrs={"name": re.compile(r"^description$", re.I)})
    description = desc_tag.get("content", "").strip() if desc_tag else ""

    kw_tag = soup.find("meta", attrs={"name": re.compile(r"^keywords$", re.I)})
    keywords = kw_tag.get("content", "").strip() if kw_tag else ""

    return {"url": url, "title": title, "description": description, "keywords": keywords}


# ──────────────────────────────────────────────────────────────────────────────
# Link discovery
# ──────────────────────────────────────────────────────────────────────────────

def discover_links(soup: BeautifulSoup, current_url: str) -> list[str]:
    """Find all internal links on a page."""
    links = []
    for a in soup.find_all("a", href=True):
        normalized = normalize_url(a["href"], base=current_url)
        if normalized:
            links.append(normalized)
    return links


def discover_blog_pagination(soup: BeautifulSoup, current_url: str) -> list[str]:
    """Look for blog pagination links like /blog?page=2."""
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "page=" in href or "page/" in href:
            normalized = normalize_url(href, base=current_url)
            if normalized:
                links.append(normalized)
    return links


# ──────────────────────────────────────────────────────────────────────────────
# Page fetcher
# ──────────────────────────────────────────────────────────────────────────────

async def fetch_page(page, url: str) -> str | None:
    """Navigate to URL and return full HTML after rendering. Returns None on failure."""
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            # Try networkidle with reasonable timeout
            try:
                await page.goto(url, wait_until="networkidle", timeout=12_000)
            except PlaywrightTimeoutError:
                # If networkidle hangs (e.g. persistent WebSocket/analytics), fallback to domcontentloaded
                await page.goto(url, wait_until="domcontentloaded", timeout=15_000)
            
            # Wait for SPA hydration / DOM rendering
            await page.wait_for_timeout(2000)
            return await page.content()
        except PlaywrightTimeoutError:
            log.warning(f"Timeout on {url} (attempt {attempt})")
            if attempt <= MAX_RETRIES:
                await asyncio.sleep(2)
        except Exception as e:
            log.warning(f"Error fetching {url} (attempt {attempt}): {e}")
            if attempt <= MAX_RETRIES:
                await asyncio.sleep(2)
    return None


# ──────────────────────────────────────────────────────────────────────────────
# Main crawl loop
# ──────────────────────────────────────────────────────────────────────────────

async def crawl():
    OUTPUT_DIR.mkdir(exist_ok=True)

    visited: set[str] = set()
    queue: deque[str] = deque()
    crawl_results: list[dict] = []   # {url, filename, status}
    failed_urls: list[dict] = []
    nav_footer_texts: list[str] = []
    nav_footer_captured = False

    # Seed the queue
    for path in SEED_PATHS:
        url = normalize_url(path)
        if url and url not in visited:
            queue.append(url)
            visited.add(url)

    async with async_playwright() as pw:
        # Use the full Chrome binary (headless shell failed to download due to network)
        chrome_path = (
            Path.home() / "AppData" / "Local" / "ms-playwright"
            / "chromium-1243" / "chrome-win64" / "chrome.exe"
        )
        launch_kwargs = {"headless": True}
        if chrome_path.exists():
            launch_kwargs["executable_path"] = str(chrome_path)
        browser = await pw.chromium.launch(**launch_kwargs)
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
        )
        page = await context.new_page()

        # Block heavy assets to speed up crawl
        await page.route(
            re.compile(r"\.(png|jpg|jpeg|gif|webp|woff2?|ttf|eot|mp4|mp3)$"),
            lambda route: route.abort(),
        )

        pages_crawled = 0

        while queue:
            url = queue.popleft()
            log.info(f"[{pages_crawled+1}] Crawling: {url}")

            html = await fetch_page(page, url)

            if html is None:
                log.error(f"FAILED: {url}")
                failed_urls.append({"url": url, "reason": "fetch failed after retries"})
                crawl_results.append({"url": url, "filename": None, "status": "FAILED"})
                await asyncio.sleep(DELAY_BETWEEN_REQUESTS)
                continue

            soup = BeautifulSoup(html, "lxml")

            # ── Extract nav/footer once ──
            if not nav_footer_captured:
                nav_footer_text = extract_nav_footer(soup)
                if nav_footer_text:
                    nav_footer_texts.append(nav_footer_text)
                    nav_footer_captured = True

            # ── Discover new links ──
            new_links = discover_links(soup, url)
            new_links += discover_blog_pagination(soup, url)
            for link in new_links:
                if link not in visited:
                    visited.add(link)
                    queue.append(link)
                    log.debug(f"  Queued: {link}")

            # ── Extract metadata & content ──
            meta = extract_meta(soup, url)
            body_text = extract_body_content(soup)

            # ── Build file content ──
            header_lines = [
                f"URL: {meta['url']}",
                f"TITLE: {meta['title']}",
                f"META DESCRIPTION: {meta['description']}",
            ]
            if meta["keywords"]:
                header_lines.append(f"META KEYWORDS: {meta['keywords']}")
            header_lines.append("=" * 60)

            file_content = "\n".join(header_lines) + "\n\n" + body_text

            # ── Save file ──
            filename = url_to_filename(url)
            filepath = OUTPUT_DIR / filename
            # Handle duplicates by appending a counter
            if filepath.exists():
                stem = filepath.stem
                counter = 1
                while filepath.exists():
                    filepath = OUTPUT_DIR / f"{stem}_{counter}.txt"
                    counter += 1
                filename = filepath.name

            filepath.write_text(file_content, encoding="utf-8")
            log.info(f"  → Saved: {filename} ({len(body_text):,} chars)")

            pages_crawled += 1
            crawl_results.append({"url": url, "filename": filename, "status": "OK"})

            await asyncio.sleep(DELAY_BETWEEN_REQUESTS)

        await browser.close()

    # ── Write common_navbar_footer.txt ──
    if nav_footer_texts:
        nav_footer_path = OUTPUT_DIR / "common_navbar_footer.txt"
        nav_footer_path.write_text(
            "SHARED NAVBAR / FOOTER CONTENT\n" + "=" * 60 + "\n\n" +
            "\n\n---\n\n".join(nav_footer_texts),
            encoding="utf-8",
        )
        log.info("Saved: common_navbar_footer.txt")

    # ── Write sitemap.txt ──
    sitemap_lines = ["SITEMAP\n" + "=" * 60]
    for r in crawl_results:
        fname = r["filename"] or "N/A"
        sitemap_lines.append(f"{r['status']:6}  {r['url']}  →  {fname}")
    (OUTPUT_DIR / "sitemap.txt").write_text("\n".join(sitemap_lines), encoding="utf-8")
    log.info("Saved: sitemap.txt")

    # ── Write crawl_log.txt ──
    if failed_urls:
        log_lines = ["CRAWL FAILURES\n" + "=" * 60]
        for f in failed_urls:
            log_lines.append(f"FAILED  {f['url']}  |  {f['reason']}")
        (OUTPUT_DIR / "crawl_log.txt").write_text("\n".join(log_lines), encoding="utf-8")
    else:
        (OUTPUT_DIR / "crawl_log.txt").write_text(
            "CRAWL FAILURES\n" + "=" * 60 + "\n\nNo failures! All pages crawled successfully.",
            encoding="utf-8",
        )
    log.info("Saved: crawl_log.txt")

    # ── Summary ──
    ok = sum(1 for r in crawl_results if r["status"] == "OK")
    fail = len(failed_urls)
    total_files = len(list(OUTPUT_DIR.glob("*.txt")))
    print("\n" + "=" * 60)
    print("CRAWL SUMMARY")
    print("=" * 60)
    print(f"  Pages crawled successfully : {ok}")
    print(f"  Pages failed               : {fail}")
    print(f"  Total .txt files created   : {total_files}")
    print(f"  Output directory           : {OUTPUT_DIR.resolve()}")
    if failed_urls:
        print("\n  Failed URLs:")
        for f in failed_urls:
            print(f"    ✗  {f['url']}  ({f['reason']})")
    print("=" * 60)


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    asyncio.run(crawl())
