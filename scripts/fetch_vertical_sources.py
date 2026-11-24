#!/usr/bin/env python3
# coding: utf-8
"""
Reusable vertical source fetcher for AI 漫剧 & 编剧技巧.
Pulls fresh articles from verified high-quality RSS/HTML sources, deduplicates against
scripts/all-used-urls.json, extracts real og:image / cover media, and verifies HTTP 200 GET
for both article URL and image/* media.

Usage:
  python3 scripts/fetch_vertical_sources.py --out /tmp/vertical_candidates.json --per-source 12
"""
import argparse
import concurrent.futures
import html as html_lib
import json
import re
import subprocess
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

VERTICAL_SOURCES = {
    "AI 漫剧": [
        {"name": "AIbase", "type": "aibase", "url": "https://news.aibase.com/zh/news", "noproxy": True, "lang": "zh"},
        {"name": "QbitAI", "type": "rss", "url": "https://www.qbitai.com/feed", "noproxy": True, "lang": "zh"},
        {"name": "AWN", "type": "rss", "url": "https://www.awn.com/rss.xml", "noproxy": False, "lang": "en"},
        {"name": "AnimationMagazine", "type": "rss", "url": "https://www.animationmagazine.net/feed/", "noproxy": False, "lang": "en"},
        {"name": "BeforesAndAfters", "type": "rss", "url": "https://beforesandafters.com/feed/", "noproxy": False, "lang": "en"},
        {"name": "CineD", "type": "rss", "url": "https://www.cined.com/feed/", "noproxy": False, "lang": "en"},
        {"name": "Ifanr", "type": "rss", "url": "https://www.ifanr.com/feed", "noproxy": True, "lang": "zh"},
    ],
    "编剧技巧": [
        {"name": "NoFilmSchool", "type": "rss", "url": "https://nofilmschool.com/rss.xml", "noproxy": False, "lang": "en"},
        {"name": "GoIntoTheStory", "type": "rss", "url": "https://gointothestory.blcklst.com/feed", "noproxy": False, "lang": "en"},
        {"name": "StudioBinder", "type": "studiobinder", "url": "https://www.studiobinder.com/blog/screenwriting/", "noproxy": False, "lang": "en"},
        {"name": "IndustrialScripts", "type": "rss", "url": "https://industrialscripts.com/feed/", "noproxy": False, "lang": "en"},
        {"name": "JohnAugust", "type": "rss", "url": "https://johnaugust.com/feed", "noproxy": False, "lang": "en"},
        {"name": "IndieWire", "type": "rss", "url": "https://www.indiewire.com/c/film/feed/", "noproxy": False, "lang": "en"},
        {"name": "GCORES", "type": "rss", "url": "https://www.gcores.com/rss", "noproxy": True, "lang": "zh"},
    ],
}


def norm_url(u: str) -> str:
    return u.strip().rstrip("/").replace("http://", "https://")


def curl_get(url: str, noproxy: bool = False, timeout: int = 18) -> str:
    cmd = ["curl", "-sSL", "--max-time", str(timeout), "--retry", "1", "-A", UA, url]
    if noproxy:
        cmd[1:1] = ["--noproxy", "*"]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 10)
    return r.stdout if r.returncode == 0 else ""


def clean_text(s: str) -> str:
    s = html_lib.unescape(s or "")
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def domain_of(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.lower()
    return host[4:] if host.startswith("www.") else host


def parse_rss_items(xml_text: str, limit: int) -> list:
    items = []
    # Regex fallback is resilient against minor XML quirks in third-party feeds
    blocks = re.findall(r"<item\b[^>]*>(.*?)</item>", xml_text, re.S)
    for b in blocks[:limit]:
        t_m = re.search(r"<title[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", b, re.S)
        l_m = re.search(r"<link[^>]*>(?:<!\[CDATA\[)?\s*(https?://[^<\s]+)\s*(?:\]\]>)?</link>", b, re.S)
        d_m = re.search(r"<pubDate[^>]*>(.*?)</pubDate>", b, re.S)
        desc_m = re.search(r"<description[^>]*>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</description>", b, re.S)
        # Look for media image directly inside RSS item
        img = None
        for pat in [
            r'<media:content[^>]+url=["\'](https?://[^"\']+\.(?:jpg|jpeg|png|webp)[^"\']*)["\']',
            r'<media:thumbnail[^>]+url=["\'](https?://[^"\']+)["\']',
            r'<enclosure[^>]+url=["\'](https?://[^"\']+)["\'][^>]+type=["\']image/',
            r'<img[^>]+src=["\'](https?://[^"\']+)["\']',
        ]:
            m = re.search(pat, b, re.I)
            if m:
                img = html_lib.unescape(m.group(1))
                break
        if t_m and l_m:
            items.append({
                "title": clean_text(t_m.group(1)),
                "url": html_lib.unescape(l_m.group(1).strip()),
                "pub_date": clean_text(d_m.group(1)) if d_m else "",
                "summary": clean_text(desc_m.group(1))[:320] if desc_m else "",
                "rss_media": img,
            })
    return items


def parse_aibase(html_text: str, limit: int) -> list:
    soup = BeautifulSoup(html_text, "html.parser")
    items = []
    seen = set()
    for a in soup.find_all("a", href=re.compile(r"^/zh/news/\d+")):
        href = "https://news.aibase.com" + a["href"].split("?")[0]
        if href in seen:
            continue
        title = clean_text(a.get_text(" ", strip=True))
        if len(title) < 8:
            # Try heading inside or parent
            h = a.find(["h2", "h3", "h4", "p"])
            if h:
                title = clean_text(h.get_text(" ", strip=True))
        if len(title) < 8:
            continue
        seen.add(href)
        img = None
        img_el = a.find("img") or (a.parent.find("img") if a.parent else None)
        if img_el:
            src = img_el.get("src") or img_el.get("data-src")
            if src and src.startswith("http"):
                img = src
        items.append({"title": title[:120], "url": href, "pub_date": "", "summary": "", "rss_media": img})
        if len(items) >= limit:
            break
    return items


def parse_studiobinder(html_text: str, limit: int) -> list:
    soup = BeautifulSoup(html_text, "html.parser")
    items = []
    seen = set()
    for a in soup.find_all("a", href=re.compile(r"^https://www\.studiobinder\.com/blog/[a-z0-9-]+/?$")):
        href = a["href"].strip()
        if any(skip in href for skip in ["/category/", "/author/", "/page/", "/screenwriting/", "/directing/", "/cinematography/"]):
            continue
        if href in seen:
            continue
        title = clean_text(a.get("title") or a.get_text(" ", strip=True))
        if len(title) < 12:
            continue
        seen.add(href)
        items.append({"title": title[:140], "url": href, "pub_date": "", "summary": "", "rss_media": None})
        if len(items) >= limit:
            break
    return items


def verify_and_enrich(task):
    cat, src_cfg, item = task
    url = item["url"]
    noproxy = src_cfg.get("noproxy", False)
    try:
        # 1. Fetch article HTML via GET (verifies HTTP 200 and lets us read og:image + meta description)
        cmd = ["curl", "-sSL", "--max-time", "20", "--retry", "1", "-A", UA, "-w", "\n__META__%{http_code}\t%{url_effective}", url]
        if noproxy:
            cmd[1:1] = ["--noproxy", "*"]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if r.returncode != 0 or "\n__META__" not in r.stdout:
            return None
        body, meta_str = r.stdout.rsplit("\n__META__", 1)
        code, final_url = (meta_str.split("\t", 1) + [""])[:2]
        if code != "200" or len(body) < 1000:
            return None

        soup = BeautifulSoup(body, "html.parser")
        # Extract best image: og:image -> twitter:image -> rss_media
        media_candidates = []
        for prop in [("meta", {"property": "og:image"}), ("meta", {"name": "twitter:image"}), ("meta", {"property": "og:image:secure_url"})]:
            el = soup.find(*prop)
            if el and el.get("content"):
                media_candidates.append(el["content"].strip())
        if item.get("rss_media"):
            media_candidates.append(item["rss_media"])

        # Normalize relative media URLs
        valid_media = None
        for m in media_candidates:
            if m.startswith("//"):
                m = "https:" + m
            elif m.startswith("/"):
                m = urllib.parse.urljoin(final_url or url, m)
            if not m.startswith("http"):
                continue
            # Skip tiny tracking pixels / svg placeholders
            if any(bad in m.lower() for bad in ["1x1", "pixel", "avatar", ".svg"]):
                continue
            cmd_m = ["curl", "-sSL", "--max-time", "15", "--retry", "1", "-A", UA, "-o", "/dev/null", "-w", "%{http_code}\t%{content_type}", m]
            if noproxy:
                cmd_m[1:1] = ["--noproxy", "*"]
            rm = subprocess.run(cmd_m, capture_output=True, text=True, timeout=25)
            m_parts = rm.stdout.split("\t", 1)
            if rm.returncode == 0 and m_parts[0] == "200" and len(m_parts) > 1 and m_parts[1].startswith("image/"):
                valid_media = m
                break

        if not valid_media:
            return None

        # Enrich description if missing
        summary = item.get("summary", "")
        if len(summary) < 40:
            d_el = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", property="og:description")
            if d_el and d_el.get("content"):
                summary = clean_text(d_el["content"])[:320]

        # Extract cleaner h1 title if needed
        title = item["title"]
        if src_cfg["type"] == "aibase":
            h1 = soup.find("h1")
            if h1 and len(clean_text(h1.get_text())) >= 6:
                title = clean_text(h1.get_text())

        return {
            "category": cat,
            "source_name": src_cfg["name"],
            "source": domain_of(url),
            "lang": src_cfg["lang"],
            "title": title,
            "url": url,
            "media": valid_media,
            "pub_date": item.get("pub_date", ""),
            "summary": summary,
        }
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--per-source", type=int, default=15, help="Max items to inspect per source")
    parser.add_argument("--out", type=str, default="/tmp/vertical_candidates.json")
    args = parser.parse_args()

    used = json.loads((ROOT / "scripts/all-used-urls.json").read_text())
    used_set = {norm_url(u) for u in used}

    tasks = []
    seen_batch = set()
    for cat, sources in VERTICAL_SOURCES.items():
        for src in sources:
            raw = curl_get(src["url"], noproxy=src.get("noproxy", False), timeout=18)
            if not raw or "aliyun_waf" in raw:
                print(f"[WARN] Skipped/WAF feed: {src['name']} ({src['url']})", flush=True)
                continue
            if src["type"] == "rss":
                parsed = parse_rss_items(raw, args.per_source)
            elif src["type"] == "aibase":
                parsed = parse_aibase(raw, args.per_source)
            elif src["type"] == "studiobinder":
                parsed = parse_studiobinder(raw, args.per_source)
            else:
                parsed = []
            fresh_count = 0
            for it in parsed:
                nu = norm_url(it["url"])
                if nu in used_set or nu in seen_batch:
                    continue
                seen_batch.add(nu)
                tasks.append((cat, src, it))
                fresh_count += 1
            print(f"[FEED] {cat} | {src['name']:18s}: parsed {len(parsed):2d}, fresh {fresh_count:2d}", flush=True)

    print(f"\nVerifying {len(tasks)} fresh candidate articles + media...", flush=True)
    results = {"AI 漫剧": [], "编剧技巧": []}
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        for res in pool.map(verify_and_enrich, tasks):
            if res:
                results[res["category"]].append(res)

    for cat, lst in results.items():
        print(f"=== VERIFIED {cat}: {len(lst)} items ===", flush=True)

    Path(args.out).write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved verified candidates to {args.out}")


if __name__ == "__main__":
    main()
