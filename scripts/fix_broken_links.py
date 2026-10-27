# -*- coding: utf-8 -*-
import json
import re

# Fallback high quality themed Unsplash images for text-only items
THEME_FALLBACKS = {
    # 2026-10-27 text-only
    "https://github.com/sturnus-dev/sturnus": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80", # server gateway
    "https://github.com/XLongLink/uncode": "https://images.unsplash.com/photo-1589254065878-42c9da997008?w=800&auto=format&fit=crop&q=80", # voice assistant
    "https://cohere.com/blog/concerning-behaviour-popular-open-weight-ai-model": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800&auto=format&fit=crop&q=80", # security
    "https://www.lennysnewsletter.com/p/why-reddit-built-its-own-ai-prototyping": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80", # UI design prototype
    # 2026-10-26 text-only
    "https://huggingface.co/destined/hurston-1": "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80", # voice audio
    "https://api.saanora.com/docs": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80", # probability / charts
    "https://www.lennysnewsletter.com/p/an-86-minute-guide-to-finding-pmf": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80", # market research
    # 2026-10-25 text-only
    "https://github.com/xetdata/xet-server": "https://images.unsplash.com/photo-1544197150-b99a580bb7a8?w=800&auto=format&fit=crop&q=80", # cloud storage server
}

def fix_file(day):
    date = f"2026-10-{day}"
    md_path = f"/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/{date}.md"
    raw_path = f"/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/raw-ian-{day}.json"
    
    raw_items = json.load(open(raw_path, encoding="utf-8"))
    url_map = {it["url"]: it.get("img") for it in raw_items if "url" in it}
    title_map = {it["title"]: it.get("img") for it in raw_items if "title" in it}
    
    lines = open(md_path, encoding="utf-8").readlines()
    new_lines = []
    
    current_url = None
    current_title = None
    fixes_count = 0
    
    for line in lines:
        url_match = re.search(r'^\s*url:\s*"?([^"\n]+)"?', line)
        if url_match:
            current_url = url_match.group(1).strip()
            
        title_match = re.search(r'^\s*title:\s*"?([^"\n]+)"?', line)
        if title_match:
            current_title = title_match.group(1).strip()
            
        media_match = re.search(r'^(\s*media:\s*)"?([^"\n]+)"?', line)
        if media_match and ("iandaily.xyz" in media_match.group(2)):
            prefix = media_match.group(1)
            old_media = media_match.group(2).strip()
            
            # Find real image
            real_img = url_map.get(current_url) or title_map.get(current_title)
            
            if real_img and real_img.strip():
                new_media = f"https://iandaily.xyz{real_img}"
            else:
                new_media = THEME_FALLBACKS.get(current_url, "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80")
                
            if old_media != new_media:
                fixes_count += 1
                line = f"{prefix}{new_media}\n"
                
        new_lines.append(line)
        
    open(md_path, "w", encoding="utf-8").writelines(new_lines)
    print(f"[{date}.md] Fixed {fixes_count} media links.")

for d in [25, 26, 27]:
    fix_file(d)
