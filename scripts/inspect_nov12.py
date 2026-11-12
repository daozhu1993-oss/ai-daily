# -*- coding: utf-8 -*-
import json, re

with open("scripts/all-used-urls.json") as f:
    used = set(json.load(f))
print(f"Total used URLs: {len(used)}")

# 1. Parse iandaily
with open("scripts/raw-ian-nov12.html", "r", encoding="utf-8") as f:
    html = f.read()

section_map = {
    'product': '产品设计',
    'indie': '一人公司',
    'taste': '审美提升',
    'marketing': '产品营销',
    'collab': 'AI 协作',
    'ai': 'AI 资讯'
}

idx = html.find('columns:$R')
ian_items = []
if idx != -1:
    chunk = html[idx:]
    section_positions = []
    for sec in section_map:
        pos = chunk.find(f'{sec}:$R')
        if pos != -1:
            section_positions.append((pos, sec))
    section_positions.sort()
    for i, (pos, sec) in enumerate(section_positions):
        end_pos = section_positions[i+1][0] if i+1 < len(section_positions) else len(chunk)
        sec_chunk = chunk[pos:end_pos]
        item_blocks = re.findall(r'\{eventId:"([^"]+)",title:"([^"]+)",url:"([^"]+)",judgment:"([^"]+)"(.*?)\}', sec_chunk)
        for m in item_blocks:
            eid, title, url, judgment, rest = m
            img_match = re.search(r'image:"([^"]+)"', rest)
            img = img_match.group(1) if img_match else ""
            ian_items.append({
                'section': sec,
                'category': section_map[sec],
                'title': title,
                'url': url,
                'judgment': judgment,
                'img': img
            })

with open("scripts/raw-ian-nov12.json", "w", encoding="utf-8") as f:
    json.dump(ian_items, f, ensure_ascii=False, indent=2)

fresh_ian = [x for x in ian_items if x["url"] not in used]
print(f"Fresh ian items: {len(fresh_ian)} / {len(ian_items)}")

by_cat = {}
for it in fresh_ian:
    by_cat.setdefault(it["category"], []).append(it)

for cat, lst in by_cat.items():
    print(f"\n=== ian: {cat} ({len(lst)}) ===")
    for i, it in enumerate(lst):
        print(f"  [{i+1}] {it['title']} | {it['url']}")
        print(f"      media: {it['img'][:70]}")

# 2. Extract woshipm
def extract_woshipm(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    matches = re.findall(r'href=["\'](https://www\.woshipm\.com/(?:ai|pmd|it|operate|evaluating)/\d+\.html)["\'][^>]*>(.*?)</a>', content, re.DOTALL)
    results = []
    seen = set()
    for url, title in matches:
        title = re.sub(r"<[^>]+>", "", title).strip()
        if not title or len(title) < 4:
            continue
        if url in used or url in seen:
            continue
        seen.add(url)
        results.append((url, title))
    return results

for label, fname in [("woshipm AI", "scripts/raw-woshipm-ai-nov12.html"), ("woshipm Home", "scripts/raw-woshipm-home-nov12.html"), ("woshipm PMD", "scripts/raw-woshipm-pmd-nov12.html"), ("woshipm Operate", "scripts/raw-woshipm-operate-nov12.html")]:
    print(f"\n=== {label} ===")
    for u, t in extract_woshipm(fname)[:12]:
        print(f"  {u} -> {t}")

# 3. Extract HN
print("\n=== HN Top Fresh ===")
with open("scripts/raw-hn-nov12.html", encoding="utf-8", errors="ignore") as f:
    hn = f.read()
hn_links = re.findall(r'class="titleline"><a href="(https?://[^"]+)"[^>]*>(.*?)</a>', hn)
for u, t in hn_links[:25]:
    if u not in used:
        print(f"  {t} | {u}")

# 4. Extract HF papers
print("\n=== HF Daily Papers Fresh ===")
with open("scripts/raw-hf-papers-nov12.html", encoding="utf-8", errors="ignore") as f:
    hf = f.read()
hf_links = re.findall(r'href="(/papers/(\d+\.\d+))"[^>]*>\s*(.*?)\s*</a>', hf, re.DOTALL)
seen_hf = set()
for p, pid, t in hf_links:
    t = re.sub(r"<[^>]+>", "", t).strip()
    u = f"https://huggingface.co{p}"
    if t and len(t) > 5 and u not in used and u not in seen_hf:
        seen_hf.add(u)
        print(f"  {t} | {u}")
