"""
Live SHL catalog scraper.
Fetches all Individual Test Solutions from https://www.shl.com/products/product-catalog/
Falls back to static catalog if scraping fails.
"""

import re
import json
import time
import logging
import os
from typing import List, Dict, Optional

logger = logging.getLogger("shl_scraper")

BASE_URL = "https://www.shl.com"
CATALOG_URL = f"{BASE_URL}/products/product-catalog/"
TOTAL_PAGES = 32


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


def parse_individual_tests_from_html(html: str) -> List[Dict]:
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        return []

    soup = BeautifulSoup(html, "html.parser")
    results = []
    tables = soup.find_all("table")

    for table in tables:
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if not cells:
                continue
            link = cells[0].find("a", href=True)
            if not link:
                continue
            name = link.get_text(strip=True)
            href = link["href"]
            url = href if href.startswith("http") else BASE_URL + href
            if "shl.com" not in url:
                continue
            remote = len(cells) > 1 and bool(cells[1].get_text(strip=True))
            adaptive = len(cells) > 2 and bool(cells[2].get_text(strip=True))
            test_types = []
            if len(cells) > 3:
                test_types = [c for c in cells[3].get_text(strip=True) if c in "ABCDEKPS"]
            if name:
                results.append({
                    "name": name,
                    "url": url,
                    "remote_testing": remote,
                    "adaptive_irt": adaptive,
                    "test_types": test_types,
                    "description": f"SHL assessment: {name}. Types: {', '.join(test_types) or 'unspecified'}."
                })
    return results


def scrape_catalog(cache_file: str = "catalog_live.json") -> Optional[List[Dict]]:
    """Scrape all pages; cache results for 24h."""
    try:
        import requests
    except ImportError:
        return None

    if os.path.exists(cache_file):
        if time.time() - os.path.getmtime(cache_file) < 86400:
            try:
                with open(cache_file) as f:
                    data = json.load(f)
                logger.info(f"Loaded cached catalog: {len(data)} items")
                return data
            except Exception:
                pass

    session = requests.Session()
    session.headers.update(HEADERS)
    all_items, failed = [], 0

    for page in range(TOTAL_PAGES):
        url = f"{CATALOG_URL}?start={page * 12}&type=1"
        try:
            resp = session.get(url, timeout=15)
            resp.raise_for_status()
            items = parse_individual_tests_from_html(resp.text)
            all_items.extend(items)
            logger.info(f"Page {page+1}: {len(items)} items")
            time.sleep(0.3)
        except Exception as e:
            logger.warning(f"Page {page+1} failed: {e}")
            failed += 1
            if failed > 5:
                break

    if not all_items:
        return None

    seen, deduped = set(), []
    for item in all_items:
        if item["url"] not in seen:
            seen.add(item["url"])
            deduped.append(item)

    logger.info(f"Scraped {len(deduped)} unique items")
    try:
        with open(cache_file, "w") as f:
            json.dump(deduped, f, indent=2)
    except Exception:
        pass
    return deduped


def get_catalog_with_fallback() -> List[Dict]:
    live = scrape_catalog()
    if live and len(live) > 50:
        return live
    logger.info("Falling back to static catalog")
    from catalog_data import get_catalog
    return get_catalog()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    catalog = get_catalog_with_fallback()
    print(f"Catalog: {len(catalog)} items")
