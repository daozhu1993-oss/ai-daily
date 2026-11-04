# -*- coding: utf-8 -*-
import re
import json

def parse_ian_nov4():
    with open('/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/raw-ian-nov4.html', 'r', encoding='utf-8') as f:
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
    if idx == -1:
        print("Could not find columns:$R in html")
        return

    chunk = html[idx:]

    section_positions = []
    for sec in ['product', 'indie', 'taste', 'marketing', 'collab', 'ai']:
        pos = chunk.find(f'{sec}:$R')
        if pos != -1:
            section_positions.append((pos, sec))

    section_positions.sort()

    all_items = []

    for i, (pos, sec) in enumerate(section_positions):
        end_pos = section_positions[i+1][0] if i+1 < len(section_positions) else len(chunk)
        sec_chunk = chunk[pos:end_pos]
        
        item_blocks = re.findall(r'\{eventId:"([^"]+)",title:"([^"]+)",url:"([^"]+)",judgment:"([^"]+)"(.*?)\}', sec_chunk)
        print(f"Section {sec} ({section_map[sec]}): found {len(item_blocks)} items")
        for m in item_blocks:
            eid, title, url, judgment, rest = m
            img_match = re.search(r'image:"([^"]+)"', rest)
            img = img_match.group(1) if img_match else ""
            all_items.append({
                'section': sec,
                'category': section_map[sec],
                'eventId': eid,
                'title': title,
                'url': url,
                'judgment': judgment,
                'img': img
            })

    print(f"Total extracted for Nov 4: {len(all_items)}")
    with open('/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/raw-ian-nov4.json', 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    parse_ian_nov4()
