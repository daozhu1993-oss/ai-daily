# -*- coding: utf-8 -*-
import subprocess
import json
import concurrent.futures
import time
import threading

candidates = [
    # AI 资讯 (4)
    {
        "category": "AI 资讯",
        "title": "DeepMind 推出 AlphaProof Code：形式化数学验证与可靠代码生成融合突破",
        "url": "https://deepmind.google/blog/introducing-alphaproof-code/",
        "media": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&auto=format&fit=crop&q=80",
        "source": "deepmind.google"
    },
    {
        "category": "AI 资讯",
        "title": "Apple 筹备全新原生 Mac 应用：大幅降低普通用户本地运行大模型的门槛",
        "url": "https://9to5mac.com/2026/11/10/apple-has-new-mac-app-coming-to-make-running-local-ai-models-easy/",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "source": "9to5mac.com"
    },
    {
        "category": "AI 资讯",
        "title": "Evidence-Linked Memory：证据链记忆机制缓解长程 Agent 退化与幻觉污染",
        "url": "https://huggingface.co/papers/2611.14320",
        "media": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
        "source": "huggingface.co"
    },
    {
        "category": "AI 资讯",
        "title": "下一概念建模（LCM）：将文本生成从逐字 Token 推向高维并行推理",
        "url": "https://arxiv.org/abs/2610.14162",
        "media": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800&auto=format&fit=crop&q=80",
        "source": "arxiv.org"
    },
    # AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "Loopt 允许用任意编程语言撰写 GitHub Actions：打破 YAML 脚本流束缚",
        "url": "https://github.com/preloopdev/loopt",
        "media": "https://iandaily.xyz/digest/2026-11-10-prelooploopt-7d5809232666.jpg",
        "source": "github.com"
    },
    {
        "category": "AI 协作",
        "title": "Desk 为命令行代码代理搭建原生 macOS 工作台：多并发终端代理调度中枢",
        "url": "https://github.com/s-nish/desk",
        "media": "https://iandaily.xyz/digest/2026-11-10-snishdesk-37fd09746d45.jpg",
        "source": "github.com"
    },
    {
        "category": "AI 协作",
        "title": "FMP Plugins 让智能体记住改 Bug 的真实解法：自愈型工程排错经验沉淀",
        "url": "https://github.com/GDM-Digital-Media-Group/fmp-plugins",
        "media": "https://iandaily.xyz/digest/2026-11-10-fmpplugins-9dab984458ea.jpg",
        "source": "github.com"
    },
    {
        "category": "AI 协作",
        "title": "Google Chrome 开源 Modern Web Guidance：让编程 Agent 直接对齐现代 Web 标准",
        "url": "https://github.com/GoogleChrome/modern-web-guidance",
        "media": "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&auto=format&fit=crop&q=80",
        "source": "github.com"
    },
    # 一人公司 (4)
    {
        "category": "一人公司",
        "title": "Rollare 为草根线下赛设计极简对阵签表：轻量化体育赛事组织工具变现",
        "url": "https://rollare.com/",
        "media": "https://iandaily.xyz/digest/2026-11-10-rollare-e6daaea92ab2.jpg",
        "source": "rollare.com"
    },
    {
        "category": "一人公司",
        "title": "SteamPunk 用滑动卡片探索 Steam 游戏库：游戏库存清理与趣味推荐小产品",
        "url": "https://steampunk.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-10-steampunksh-8a1ce859a997.jpg",
        "source": "steampunk.sh"
    },
    {
        "category": "一人公司",
        "title": "Lampjack 随音频律动生成实时三维声波空间：浏览器端沉浸式音乐可视化",
        "url": "https://lampjack.app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-lampjack-4b9cc398ee26.jpg",
        "source": "lampjack.app"
    },
    {
        "category": "一人公司",
        "title": "Black Friday for Developers 汇总工程师专属折扣：高纯度垂直流量导购站点",
        "url": "https://www.blackfriday.dev",
        "media": "https://iandaily.xyz/digest/2026-11-10-blackfridaydev-8c8a6331e133.jpg",
        "source": "blackfriday.dev"
    },
    # 产品设计 (4)
    {
        "category": "产品设计",
        "title": "Jot 双击 Shift 将选中文字归入 Markdown：极致丝滑的系统级剪贴捕获交互",
        "url": "https://sayjot.xyz/",
        "media": "https://iandaily.xyz/digest/2026-11-10-sayjot-906dea141867.jpg",
        "source": "sayjot.xyz"
    },
    {
        "category": "产品设计",
        "title": "Velorki 只靠一部手机完成骑行路线指引：极端场景下反冗余的极简交互界面",
        "url": "https://velorki.com",
        "media": "https://iandaily.xyz/digest/2026-11-10-velorki-95b1dd7d9ca1.jpg",
        "source": "velorki.com"
    },
    {
        "category": "产品设计",
        "title": "WithIcons 用 34 种视觉质感绘制同一图标库：风格化 UI 组件材质实验矩阵",
        "url": "https://withicons.com/",
        "media": "https://iandaily.xyz/digest/2026-11-10-withicons-b3ca68e6468b.jpg",
        "source": "withicons.com"
    },
    {
        "category": "产品设计",
        "title": "iPhone-use-app 让大模型直接操作真机界面：无障碍 API 驱动移动自动化新交互",
        "url": "https://github.com/EliotAndres/iphone-use-app",
        "media": "https://iandaily.xyz/digest/2026-11-10-iphoneuseapp-073ade3333c3.jpg",
        "source": "github.com"
    },
    # 审美提升 (4)
    {
        "category": "审美提升",
        "title": "Dezeen Awards 奖杯回归天然软木材质：有机可再生材料的极简雕塑感平衡",
        "url": "https://www.dezeen.com/2026/11/09/dezeen-awards-2026-trophy-cork-amorim-corticeira/",
        "media": "https://iandaily.xyz/digest/2026-11-10-dezeencorktrophy-76892df77a9b.jpg",
        "source": "dezeen.com"
    },
    {
        "category": "审美提升",
        "title": "Carsten Höller 在墨西哥城盘旋立起巨型滑梯：建筑物理尺度内的游乐场荒诞诗学",
        "url": "https://www.dezeen.com/2026/11/09/carsten-holler-mexico-city/",
        "media": "https://iandaily.xyz/digest/2026-11-10-carstenholler-e66f13d13f1a.jpg",
        "source": "dezeen.com"
    },
    {
        "category": "审美提升",
        "title": "EBBA 将康沃尔旧农用谷仓化作静谧避难所：波纹金属外皮与温润胶合板的反差",
        "url": "https://www.dezeen.com/2026/11/09/ebba-architects-dutch-barn/",
        "media": "https://iandaily.xyz/digest/2026-11-10-ebbadutchbarn-66f592c118da.jpg",
        "source": "dezeen.com"
    },
    {
        "category": "审美提升",
        "title": "John Lautner 洛杉矶经典住宅 Baldwin 挂牌：有机主义建筑巨擘的空间几何遗产",
        "url": "https://www.wallpaper.com/architecture/residential/baldwin-residence-john-lautner-for-sale",
        "media": "https://iandaily.xyz/digest/2026-11-10-baldwinresidence-a25ac16e71d7.jpg",
        "source": "wallpaper.com"
    },
    # 产品营销 (4)
    {
        "category": "产品营销",
        "title": "Matalan 广告以时装周真假混剪完成亲民反转：用错位反差撬动大众情绪共鸣",
        "url": "https://www.creativeboom.com/news/ozos-campaign-for-matalan-pulls-off-a-clever-catwalk-switcheroo/",
        "media": "https://iandaily.xyz/digest/2026-11-10-matalanswitch-dcad44722f98.jpg",
        "source": "creativeboom.com"
    },
    {
        "category": "产品营销",
        "title": "从一条 HN 评论推导出极为精准的客户触达路线：手工冷启动时代的极高转化技巧",
        "url": "https://joshstrange.com/2026/11/09/i-saw-your-hn-comment/",
        "media": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&auto=format&fit=crop&q=80",
        "source": "joshstrange.com"
    },
    {
        "category": "产品营销",
        "title": "Val Town 宣布逐步关停服务：开发者基础设施创业的商业周期与平台化警钟",
        "url": "https://blog.val.town/winding-down",
        "media": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80",
        "source": "blog.val.town"
    },
    {
        "category": "产品营销",
        "title": "小红书生活服务增长复盘：告别传统线索广告，重构本地内容交易闭环",
        "url": "https://www.woshipm.com/operate/6492093.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    # AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "Few-Step Streaming Video Generation：极少步条件漂移实现流畅流式长视频分镜",
        "url": "https://huggingface.co/papers/2611.14033",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "source": "huggingface.co"
    },
    {
        "category": "AI 漫剧",
        "title": "PhysOPSD：以代码约束实现符合真实物理规律的视频生成，告别人物动作穿模",
        "url": "https://huggingface.co/papers/2611.12411",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "source": "huggingface.co"
    },
    {
        "category": "AI 漫剧",
        "title": "谷歌最强多模态 Gemini 4 Carbon 全球解禁实测：再现人类登月级的视听质变",
        "url": "https://www.woshipm.com/ai/6492155.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "用 Grok Bot 搭建 7×24 小时自动创作与选品分析小组：个人工作室自动化流",
        "url": "https://www.woshipm.com/ai/6492254.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    # 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "《全球直播》微短剧 全120集：科幻悬疑、元叙事真人秀与多层命运反转结构",
        "url": "https://www.wzbj1616.com/script_info/2258",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《凶案现场，我看见死者最后十分钟》微短剧 全120集：记忆回溯金手指与连环案钩子",
        "url": "https://www.wzbj1616.com/script_info/2263",
        "media": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《八零后妈她不装了》微短剧 全120集：年代市井烟火气、女性清醒反击与逆袭节奏",
        "url": "https://www.wzbj1616.com/script_info/2262",
        "media": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《隐世老祖》微短剧 全120集：修仙错位喜剧、扮猪吃虎反差与高密喜剧设计",
        "url": "https://www.wzbj1616.com/script_info/2257",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    # 产品经理 (4)
    {
        "category": "产品经理",
        "title": "AI 时代的浪花：Coze 从开源到下线没撑过一年，平台型工具兴衰的商业底层复盘",
        "url": "https://www.woshipm.com/ai/6492136.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "实测 Gemini 4 Carbon：Google 如何借多模态深水能力与生态连接悄然重回牌桌",
        "url": "https://www.woshipm.com/evaluating/6492242.html",
        "media": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "Claude 上线白板与表格协作套件：大模型直接侵入日常核心办公资产与交付标准",
        "url": "https://www.woshipm.com/ai/6492246.html",
        "media": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "2026 AI 应用钱都流向了哪里？穿透过剩泡沫看真实企业买单痛点与死穴",
        "url": "https://www.woshipm.com/ai/6492158.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    }
]

woshipm_lock = threading.Lock()

def check_url(target):
    if "woshipm.com" in target:
        with woshipm_lock:
            time.sleep(0.4)
            cmd = [
                "curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}",
                "--max-time", "12",
                "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
            ]
            cmd.append(target)
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                return target, res.stdout.strip()
            except Exception as e:
                return target, f"ERR:{e}"

    cmd = [
        "curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}",
        "--max-time", "12",
        "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    if "wzbj1616.com" in target:
        cmd += ["--noproxy", "*"]
    cmd.append(target)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        code = res.stdout.strip()
        return target, code
    except Exception as e:
        return target, f"ERR:{e}"

def main():
    print(f"Total candidates: {len(candidates)}")
    with open("scripts/all-used-urls.json") as f:
        used = set(json.load(f))
    
    dups = [c["url"] for c in candidates if c["url"] in used]
    if dups:
        print(f"ERROR: {len(dups)} duplicate URLs found in history!")
        for d in dups:
            print("  DUP:", d)
        return
    else:
        print("PASS: 0 duplicates against global used database.")

    urls_to_test = []
    for c in candidates:
        urls_to_test.append(("URL", c["url"]))
        urls_to_test.append(("MEDIA", c["media"]))

    print(f"Starting parallel GET curl verification for {len(urls_to_test)} endpoints...")
    all_ok = True
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_map = {executor.submit(check_url, u): (t, u) for t, u in urls_to_test}
        for future in concurrent.futures.as_completed(future_map):
            t, u = future_map[future]
            target, code = future.result()
            if code not in ["200", "301", "302", "308"]:
                print(f"FAIL [{t}] {code} -> {target}")
                all_ok = False
            else:
                pass

    if all_ok:
        print(f"SUCCESS: ALL {len(candidates)} items and their media returned HTTP 200/OK!")
    else:
        print("FAIL: Some endpoints failed verification.")

if __name__ == "__main__":
    main()
