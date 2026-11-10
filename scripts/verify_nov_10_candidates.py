# -*- coding: utf-8 -*-
import subprocess
import json
import concurrent.futures
import time
import threading

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Sentinel Eval 揭示智能体长期记忆的安全泄漏风险：跨会话提示注入与隐私边界评测",
        "url": "https://github.com/harishbalasubramanian/sentinel-eval",
        "media": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
        "source": "github.com"
    },
    {
        "category": "AI 资讯",
        "title": "Meta 推出最小端侧模型 Muse Ember：聚焦 Agent 极速高频决策循环",
        "url": "https://research.meta.ai/blog/muse-ember",
        "media": "https://iandaily.xyz/digest/2026-11-10-metamuseember-5ee3db0e6036.jpg",
        "source": "research.meta.ai"
    },
    {
        "category": "AI 资讯",
        "title": "E-means 在保持等精度下将 K-Means 提速十倍：经典聚类算法的现代硬件极致重写",
        "url": "https://e-means.github.io/",
        "media": "https://iandaily.xyz/digest/2026-11-10-emeans10x-4e2521a0eedb.jpg",
        "source": "e-means.github.io"
    },
    {
        "category": "AI 资讯",
        "title": "Flide 将 Jev 风格决策模型的推理速度提升近十倍：复杂逻辑链实时端侧执行",
        "url": "https://github.com/OmniJev/Flide",
        "media": "https://iandaily.xyz/digest/2026-11-10-omnijevflide-b21e312fcf76.jpg",
        "source": "github.com"
    },
    # AI 协作
    {
        "category": "AI 协作",
        "title": "Thrum 把 Claude Code 与 Codex 编入同一支战队：多模型分工协同开发管线",
        "url": "https://thrum.team/",
        "media": "https://iandaily.xyz/digest/2026-11-10-thrumteam-9a1233874d49.jpg",
        "source": "thrum.team"
    },
    {
        "category": "AI 协作",
        "title": "Toolshed 用一套终端界面管理所有 MCP 服务：标准化模型上下文协议运维套件",
        "url": "https://toolshed.run",
        "media": "https://iandaily.xyz/digest/2026-11-10-toolshedrun-7766ba843e72.jpg",
        "source": "toolshed.run"
    },
    {
        "category": "AI 协作",
        "title": "MergeAtlas 以视觉化地图重塑拉取请求代码审查：多分支巨型 PR 依赖解耦",
        "url": "https://mergeatlas.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-10-mergeatlas-ca9b4f652a7c.jpg",
        "source": "mergeatlas.dev"
    },
    {
        "category": "AI 协作",
        "title": "Venzx 在 AI 触发危险工具前插入人工确认卡：确定性人机协同最后一道防火墙",
        "url": "https://venzx.com/try",
        "media": "https://iandaily.xyz/digest/2026-11-10-venzxtry-2bd465910cd4.jpg",
        "source": "venzx.com"
    },
    # 一人公司
    {
        "category": "一人公司",
        "title": "Foldable Flight 建立纸飞机折法终极档案：小众情怀长尾内容商业化标杆",
        "url": "https://www.foldableflight.com",
        "media": "https://iandaily.xyz/digest/2026-11-10-foldableflight-70cfd5f2ab34.jpg",
        "source": "foldableflight.com"
    },
    {
        "category": "一人公司",
        "title": "Deskland 让桌面壁纸随图标排布动态让位：macOS 原生轻量视觉小工具",
        "url": "https://deskland.app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-deskland-f09ed394f39b.jpg",
        "source": "deskland.app"
    },
    {
        "category": "一人公司",
        "title": "Kiiwi 把机械键盘清脆轴体音效带回电脑：纯粹物理手感与拟物音效变现",
        "url": "https://kiiwi.app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-kiiwiapp-0a5a01ece5df.jpg",
        "source": "kiiwi.app"
    },
    {
        "category": "一人公司",
        "title": "Logcrux 在本地用小模型诊断复杂服务日志：纯私有端侧排障利器",
        "url": "https://logcrux.com",
        "media": "https://iandaily.xyz/digest/2026-11-10-logcrux-d298456dee74.jpg",
        "source": "logcrux.com"
    },
    # 产品设计
    {
        "category": "产品设计",
        "title": "KetchUp 在浏览器里复活轻量 3D 建模：零门槛 WebGL 快速空间草图工具",
        "url": "https://ketchup3d.github.io/app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-ketchup3d-f084106221e7.jpg",
        "source": "ketchup3d.github.io"
    },
    {
        "category": "产品设计",
        "title": "MeowDisplay 把 Mac 画面反向镜像到手机：极简双屏与副屏扩展微创新",
        "url": "https://meowdisplay.app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-meowdisplay-f54bad69d1a9.jpg",
        "source": "meowdisplay.app"
    },
    {
        "category": "产品设计",
        "title": "Someone Was Here 记录离开电脑时的静默触碰：硬件级物理安全与防窥感知",
        "url": "https://someonewashere.app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-someonewashere-6c7044476e19.jpg",
        "source": "someonewashere.app"
    },
    {
        "category": "产品设计",
        "title": "Wimi 为 macOS 带来鼠标优先的窗口平铺：抛弃复杂快捷键的直觉布局",
        "url": "https://getwimi.app",
        "media": "https://iandaily.xyz/digest/2026-11-10-getwimi-9aaf62112a60.jpg",
        "source": "getwimi.app"
    },
    # 审美提升
    {
        "category": "审美提升",
        "title": "Balzar 在瓦伦西亚融合侘寂与十九世纪老宅：古朴石膏雕花与微水泥极简对话",
        "url": "https://www.designboom.com/architecture/balzar-arquitectos-19th-century-modernist-interiors-wabi-sabi-materiality-valencia-apartment-renovation-ciutat-vella-apartment/",
        "media": "https://iandaily.xyz/digest/2026-11-10-balzarvalencia-657e82770000.jpg",
        "source": "designboom.com"
    },
    {
        "category": "审美提升",
        "title": "吉萨金字塔脚下跌落金色门户与守护神雕塑：古埃及历史古迹与当代艺术碰撞",
        "url": "https://www.designboom.com/art/sculptural-portals-golden-guardians-giza-art-degypte-forever-now-06/",
        "media": "https://iandaily.xyz/digest/2026-11-10-gizaartportals-6937a436b868.jpg",
        "source": "designboom.com"
    },
    {
        "category": "审美提升",
        "title": "Pearce+ 用废弃旧木与帆布在伦敦搭起野性凉亭：都市废料与临时建筑的可持续诗学",
        "url": "https://www.designboom.com/architecture/pearce-plus-guerrilla-shading-pavilion-salvaged-timber-canvas-sails-camden-london/",
        "media": "https://iandaily.xyz/digest/2026-11-10-pearcecamden-9272c501e71d.jpg",
        "source": "designboom.com"
    },
    {
        "category": "审美提升",
        "title": "Casa Mouda 在拉各斯搭建当代非洲设计舞台：粗粝红土色彩与现代手工艺交融",
        "url": "https://www.wallpaper.com/design-interiors/casa-mouda-lagos",
        "media": "https://iandaily.xyz/digest/2026-11-10-casamouda-24bb15a9db1d.jpg",
        "source": "wallpaper.com"
    },
    # 产品营销
    {
        "category": "产品营销",
        "title": "Cloudflare 设立 Vite 生态发展专项基金：前端构建基础设施的生态投资战法",
        "url": "https://blog.cloudflare.com/launching-vite-ecosystem-fund/",
        "media": "https://iandaily.xyz/digest/2026-11-10-vitefundcf-8e1acd43f284.jpg",
        "source": "blog.cloudflare.com"
    },
    {
        "category": "产品营销",
        "title": "美国邮政公开全美精确邮编边界多边形：公共数据开放驱动物流 SaaS 创新",
        "url": "https://postalpro.usps.com/zcb",
        "media": "https://iandaily.xyz/digest/2026-11-10-uspszipcodes-b3916622038d.jpg",
        "source": "postalpro.usps.com"
    },
    {
        "category": "产品营销",
        "title": "H100 算力租金在不同云厂商间存在数倍价差：大模型底层基础设施套利空间分析",
        "url": "https://github.com/datareceipts/data-receipts/tree/main/109-gpu-pricing",
        "media": "https://iandaily.xyz/digest/2026-11-10-gpudisparity-e9870611d574.jpg",
        "source": "github.com"
    },
    {
        "category": "产品营销",
        "title": "白帽黑客披露全球某品牌汽车远程开锁漏洞：安全公关与漏洞透明披露的最佳实践",
        "url": "https://shubs.io/unlocking-any-car-from-x-brand-in-most-of-the-world/",
        "media": "https://iandaily.xyz/digest/2026-11-10-unlockanycar-839ca732b446.jpg",
        "source": "shubs.io"
    },
    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "AI 剪辑混战：制作要素重组与影视漫剧生产流水线大洗牌",
        "url": "https://www.woshipm.com/ai/6477303.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "GPT-image-2.6 动图功能实测：漫剧微表情与角色动态关键帧轻量化交付",
        "url": "https://www.woshipm.com/ai/6491509.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "数字员工与 AI Native 新流水线：漫剧工作室角色重构与降本实战",
        "url": "https://www.woshipm.com/ai/6491342.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "把 2400 年中国史装进一张网页：拖动时间轴看尽山河易主的交互式历史叙事",
        "url": "https://www.woshipm.com/ai/6491484.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《镜中人》微短剧 全本：都市灵异悬疑、刑侦画像师与心理侧写博弈",
        "url": "https://www.wzbj1616.com/script_info/2249",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《长生从种田开始》微短剧 全本：修仙种田、慢节奏发育与草根逆袭节奏",
        "url": "https://www.wzbj1616.com/script_info/2250",
        "media": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《零点急诊室》微短剧 全120集：夜班医院、都市灵异悬疑与温情反转",
        "url": "https://www.wzbj1616.com/script_info/2254",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《九二南下》微短剧 全120集：年代商战、退伍兵闯深圳与江湖热血恩仇",
        "url": "https://www.wzbj1616.com/script_info/2255",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    # 产品经理
    {
        "category": "产品经理",
        "title": "实测字节 TRAE 宝：大厂 Personal Agent 布局与从编程破局的战略逻辑",
        "url": "https://www.woshipm.com/ai/6491519.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "腾讯手中最硬的一张牌：Agent 时代社交基建与企业微信连接飞轮",
        "url": "https://www.woshipm.com/ai/6491490.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "端到端加密也挡不住 AI？Personal Agent 时代的产品隐私与合规边界",
        "url": "https://www.woshipm.com/ai/6491329.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "一轮 Agent 竞品分析后：为什么产品经理必须跳出‘对话框思维’",
        "url": "https://www.woshipm.com/ai/6381717.html",
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
