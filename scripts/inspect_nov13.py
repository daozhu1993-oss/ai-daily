# -*- coding: utf-8 -*-
import json
import re
import html
from bs4 import BeautifulSoup

with open("scripts/all-used-urls.json", "r", encoding="utf-8") as f:
    used = set(json.load(f))

print(f"Total used URLs in history: {len(used)}")

# 1. Parse iandaily
ian_html = open("scripts/raw-ian-nov13.html", "r", encoding="utf-8", errors="ignore").read()
soup = BeautifulSoup(ian_html, "html.parser")
ian_items = []
# Each post usually in an article or div
for a in soup.find_all("a", href=True):
    href = a["href"].strip()
    if href.startswith("http") and not any(x in href for x in ["iandaily.xyz", "twitter.com", "github.com/ian"]):
        title = a.get_text(strip=True)
        if title and len(title) > 4:
            ian_items.append((title, href))

print(f"Found {len(ian_items)} raw external links from iandaily")

# Parse nextjs data or script json in iandaily if present
json_match = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', ian_html)
ian_records = []
if json_match:
    try:
        data = json.loads(json_match.group(1))
        # inspect structure
        posts = data.get("props", {}).get("pageProps", {}).get("posts", [])
        print(f"Parsed {len(posts)} posts from __NEXT_DATA__")
        for p in posts:
            ian_records.append(p)
    except Exception as e:
        print("NEXT_DATA parse err:", e)

# 2. Parse woshipm articles
def parse_woshipm(filename, tag):
    content = open(filename, "r", encoding="utf-8", errors="ignore").read()
    matches = re.findall(r'<h2[^>]*class=[\"\'][^\"\']*item-title[^\"\']*[\"\'][^>]*>\s*<a[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>', content, re.S)
    if not matches:
        matches = re.findall(r'<a[^>]*href=[\"\'](https?://www\.woshipm\.com/[^\"\']+\.html)[\"\'][^>]*>(.*?)</a>', content, re.S)
    print(f"=== WOSHIPM {tag} ===")
    seen = set()
    for u, t in matches:
        t = re.sub(r'<[^>]+>', '', t).strip()
        t = html.unescape(t)
        if u not in used and u not in seen and len(t) > 6 and not any(x in u for x in ["tag", "user", "author", "activity"]):
            seen.add(u)
            print(f"  {u} -> {t[:80]}")

parse_woshipm("scripts/raw-woshipm-ai-nov13.html", "AI")
parse_woshipm("scripts/raw-woshipm-home-nov13.html", "Home")
parse_woshipm("scripts/raw-woshipm-pmd-nov13.html", "PMD")
parse_woshipm("scripts/raw-woshipm-operate-nov13.html", "Operate")

# 3. Parse Hacker News
print("=== HN Fresh ===")
hn_html = open("scripts/raw-hn-nov13.html", "r", encoding="utf-8", errors="ignore").read()
for u, t in re.findall(r'<span class=\"titleline\"><a href=\"(http[^\"]+)\"[^>]*>(.*?)</a>', hn_html):
    if u not in used and "ycombinator.com" not in u:
        print(f"  {u} -> {html.unescape(t)}")

# 4. Parse HN Show
print("=== HN Show Fresh ===")
hn_show = open("scripts/raw-hn-show-nov13.html", "r", encoding="utf-8", errors="ignore").read()
for u, t in re.findall(r'<span class=\"titleline\"><a href=\"(http[^\"]+)\"[^>]*>(.*?)</a>', hn_show):
    if u not in used and "ycombinator.com" not in u:
        print(f"  {u} -> {html.unescape(t)}")

# 5. Parse HuggingFace Daily Papers
print("=== HF Daily Papers ===")
hf_html = open("scripts/raw-hf-papers-nov13.html", "r", encoding="utf-8", errors="ignore").read()
hf_matches = re.findall(r'<a[^>]*href=[\"\'](/papers/\d+\.\d+)[\"\'][^>]*>(.*?)</a>', hf_html, re.S)
seen_hf = set()
for p, t in hf_matches:
    u = f"https://huggingface.co{p}"
    t = re.sub(r'<[^>]+>', '', t).strip()
    t = html.unescape(t)
    if u not in used and u not in seen_hf and len(t) > 5:
        seen_hf.add(u)
        print(f"  {u} -> {t[:80]}")

# 6. Parse Dezeen Design
print("=== Dezeen Design ===")
dz_html = open("scripts/raw-dezeen-nov13.html", "r", encoding="utf-8", errors="ignore").read()
for u, t in re.findall(r'<h3[^>]*>\s*<a[^>]*href=[\"\'](https://www\.dezeen\.com/2026/[^\"\']+)[\"\'][^>]*>(.*?)</a>', dz_html, re.S):
    t = re.sub(r'<[^>]+>', '', t).strip()
    t = html.unescape(t)
    if u not in used:
        print(f"  {u} -> {t[:80]}")

# 7. Dump iandaily records if any
if ian_records:
    with open("scripts/raw-ian-nov13.json", "w", encoding="utf-8") as f:
        json.dump(ian_records, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(ian_records)} records to scripts/raw-ian-nov13.json")
