# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import sys

candidates = [
    # 1. AI 资讯 (4)
    {
        "cat": "AI 资讯",
        "url": "https://github.com/kerlenton/bootgpt",
        "media": "https://iandaily.xyz/digest/2026-11-01-bootgpt-c816d1d067f3.jpg"
    },
    {
        "cat": "AI 资讯",
        "url": "https://github.com/shakewingo/Tadpole",
        "media": "https://iandaily.xyz/digest/2026-11-01-tadpole-a1db258d99f2.jpg"
    },
    {
        "cat": "AI 资讯",
        "url": "https://aaivu.github.io/KuralHub/datasets.html",
        "media": "https://iandaily.xyz/digest/2026-11-01-kuralhub-22707b0e68bb.jpg"
    },
    {
        "cat": "AI 资讯",
        "url": "https://www.wiz.io/blog/black-october-for-ai-developer-platforms",
        "media": "https://iandaily.xyz/digest/2026-11-01-wiz-120482e4bbe3.jpg"
    },

    # 2. AI 协作 (4)
    {
        "cat": "AI 协作",
        "url": "https://clawdline.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-clawdline-c877a45fdf4f.jpg"
    },
    {
        "cat": "AI 协作",
        "url": "https://www.enclyralabs.com",
        "media": "https://iandaily.xyz/digest/2026-11-01-enclyra-1dfdb2dd1d66.jpg"
    },
    {
        "cat": "AI 协作",
        "url": "https://www.fastbrowse.ai/",
        "media": "https://iandaily.xyz/digest/2026-11-01-fastbrowse-af2c3920dd7f.jpg"
    },
    {
        "cat": "AI 协作",
        "url": "https://github.com/tapaskar/archwhere",
        "media": "https://iandaily.xyz/digest/2026-11-01-archwhere-9ef998db5da9.jpg"
    },

    # 3. 一人公司 (4)
    {
        "cat": "一人公司",
        "url": "https://subfaro.com/en/",
        "media": "https://iandaily.xyz/digest/2026-11-01-subfaro-0d24c2cc3bc8.jpg"
    },
    {
        "cat": "一人公司",
        "url": "https://classicalbot.com/api/docs",
        "media": "https://iandaily.xyz/digest/2026-11-01-classicalbot-c37bd4363fb0.jpg"
    },
    {
        "cat": "一人公司",
        "url": "https://upclabelmaker.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-upclabelmaker-d3bf6402d6ad.jpg"
    },
    {
        "cat": "一人公司",
        "url": "https://everydaytoolz.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-everydaytoolz-77034055692e.jpg"
    },

    # 4. 产品设计 (4)
    {
        "cat": "产品设计",
        "url": "https://bbrouter.com/bbrouter/ben-eater-sap-1",
        "media": "https://iandaily.xyz/digest/2026-11-01-bbrouter-a924ae9aa97c.jpg"
    },
    {
        "cat": "产品设计",
        "url": "https://citellm.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-citellm-6d257774f78b.jpg"
    },
    {
        "cat": "产品设计",
        "url": "https://www.jointter.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-jointter-d116fb8df3db.jpg"
    },
    {
        "cat": "产品设计",
        "url": "https://getwoodshed.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-woodshed-58902daeae10.jpg"
    },

    # 5. 审美提升 (4)
    {
        "cat": "审美提升",
        "url": "https://www.designboom.com/design/wololow-2-0-1960s-space-age-architecture-elliptical-bedside-light-arthur-koshatahyan-kostya-trunov/",
        "media": "https://iandaily.xyz/digest/2026-11-01-wololow-e48bc7eac0dc.jpg"
    },
    {
        "cat": "审美提升",
        "url": "https://www.designboom.com/design/woven-bamboo-armchair-uv-reactive-crocheted-blooms-dark-peiyang-camille-li/",
        "media": "https://iandaily.xyz/digest/2026-11-01-blooms-abd6cc86a797.jpg"
    },
    {
        "cat": "审美提升",
        "url": "https://www.dezeen.com/2026/10/31/libreria-valladolid-mexico-city-bar-em-estudio/ ",
        "media": "https://iandaily.xyz/digest/2026-11-01-libreria-8fd25dfee3cf.jpg"
    },
    {
        "cat": "审美提升",
        "url": "https://www.dezeen.com/2026/10/31/osullivan-skoufoglou-architects-garden-studio/",
        "media": "https://iandaily.xyz/digest/2026-11-01-gardenstudio-1cabba1de736.jpg"
    },

    # 6. 产品营销 (4)
    {
        "cat": "产品营销",
        "url": "https://www.getpublishub.com",
        "media": "https://iandaily.xyz/digest/2026-11-01-publishub-905e89ac3757.jpg"
    },
    {
        "cat": "产品营销",
        "url": "https://yogawritecode.com",
        "media": "https://iandaily.xyz/digest/2026-11-01-yogawritecode-169453a13b32.jpg"
    },
    {
        "cat": "产品营销",
        "url": "https://nomoat.app/",
        "media": "https://iandaily.xyz/digest/2026-11-01-nomoat-c298528678e8.jpg"
    },
    {
        "cat": "产品营销",
        "url": "https://www.gallerismuseum.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-galleris-598c4c2450a6.jpg"
    },

    # 7. AI 漫剧 (4)
    {
        "cat": "AI 漫剧",
        "url": "https://www.woshipm.com/ai/6487447.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "AI 漫剧",
        "url": "https://www.woshipm.com/operate/6487378.html",
        "media": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "AI 漫剧",
        "url": "https://www.woshipm.com/it/6486814.html",
        "media": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "AI 漫剧",
        "url": "https://www.woshipm.com/ai/6486531.html",
        "media": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80"
    },

    # 8. 编剧技巧 (4)
    {
        "cat": "编剧技巧",
        "url": "https://www.wzbj1616.com/script_info/2212",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "编剧技巧",
        "url": "https://www.wzbj1616.com/script_info/2213",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "编剧技巧",
        "url": "https://www.wzbj1616.com/script_info/2215",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "编剧技巧",
        "url": "https://www.wzbj1616.com/script_info/2216",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80"
    },

    # 9. 产品经理 (4)
    {
        "cat": "产品经理",
        "url": "https://www.woshipm.com/evaluating/6487428.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "产品经理",
        "url": "https://www.woshipm.com/ai/6487459.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "产品经理",
        "url": "https://www.woshipm.com/evaluating/6486885.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "cat": "产品经理",
        "url": "https://www.woshipm.com/ai/6487433.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    }
]

def check_single_url(target_url):
    target_url = target_url.strip()
    args = ["curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}", "--connect-timeout", "15", "--max-time", "25"]
    if "wzbj1616.com" in target_url:
        args.extend(["--noproxy", "*"])
    args.append(target_url)
    try:
        res = subprocess.run(args, capture_output=True, text=True, timeout=30)
        return res.stdout.strip()
    except Exception as e:
        return "TIMEOUT"

def verify_item(item):
    u_code = check_single_url(item["url"])
    m_code = check_single_url(item["media"])
    return item, u_code, m_code

print(f"Starting parallel verification of Nov 1 ({len(candidates)} items) with 12 workers...")

with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
    results = list(executor.map(verify_item, candidates))

failed = []
for i, (item, u_code, m_code) in enumerate(results):
    ok = (u_code == "200" and m_code == "200")
    status_str = "OK" if ok else "FAIL"
    print(f"[{i+1}/36] {status_str} | {item['cat']} | URL:{u_code} | MEDIA:{m_code} | {item['url']}")
    if not ok:
        failed.append((item, u_code, m_code))

if failed:
    print(f"\nFAILED: {len(failed)} items")
    sys.exit(1)
else:
    print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 1 RETURNED HTTP 200 OK!")
