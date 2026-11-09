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
        "title": "MEI 将模型工程表现与使用成本并排：大模型部署 ROI 决策评估",
        "url": "https://git-aarvin.github.io/mei/",
        "media": "https://iandaily.xyz/digest/2026-11-09-mei-c140d2266489.jpg",
        "source": "git-aarvin.github.io"
    },
    {
        "category": "AI 资讯",
        "title": "MAPLE 用专家裁剪压低本地模型体积：端侧轻量化自适应稀疏剪枝",
        "url": "https://amsach.github.io/maple/",
        "media": "https://iandaily.xyz/digest/2026-11-09-maple-a73c7acc6486.jpg",
        "source": "amsach.github.io"
    },
    {
        "category": "AI 资讯",
        "title": "ModelRefs 把模型选择连到可追溯证据：基于真实用例的选型实证雷达",
        "url": "https://modelrefs.com/",
        "media": "https://iandaily.xyz/digest/2026-11-09-modelrefs-1ea3fd99094f.jpg",
        "source": "modelrefs.com"
    },
    {
        "category": "AI 资讯",
        "title": "OfflineVault 将资料库与本地问答打包：零网络依赖的私有化知识库",
        "url": "https://offlinevault.dev",
        "media": "https://iandaily.xyz/digest/2026-11-09-offlinevault-ad9599ffd343.jpg",
        "source": "offlinevault.dev"
    },
    # AI 协作
    {
        "category": "AI 协作",
        "title": "APC 在本地试验工具调用的权限规则：细粒度 Agent 执行权限沙箱",
        "url": "https://playground.alephapc.com/",
        "media": "https://iandaily.xyz/digest/2026-11-09-apclab-5bfeaa1a112f.jpg",
        "source": "playground.alephapc.com"
    },
    {
        "category": "AI 协作",
        "title": "Plannotator 用收件箱接住代理的待办：人机异步交接与决策看板",
        "url": "https://plannotator.ai/inbox/",
        "media": "https://iandaily.xyz/digest/2026-11-09-plannotator-1867a718f218.jpg",
        "source": "plannotator.ai"
    },
    {
        "category": "AI 协作",
        "title": "Psi 把编码代理装进可携带的小程序：模块化端侧智能体运行微内核",
        "url": "https://psicode.ai/",
        "media": "https://iandaily.xyz/digest/2026-11-09-psi-080c126e5420.jpg",
        "source": "psicode.ai"
    },
    {
        "category": "AI 协作",
        "title": "Codend 把编码任务串到预览与拉取请求：端到端自主代码交付管线",
        "url": "https://codend.dev",
        "media": "https://iandaily.xyz/digest/2026-11-09-codend-f8a81e4cc255.jpg",
        "source": "codend.dev"
    },
    # 一人公司
    {
        "category": "一人公司",
        "title": "Chiptunes 用一个链接分享八位音乐：极简 Web 音频轻量创作工具",
        "url": "https://chiptunes.studio/",
        "media": "https://iandaily.xyz/digest/2026-11-09-chiptunes-9d730b76c50c.jpg",
        "source": "chiptunes.studio"
    },
    {
        "category": "一人公司",
        "title": "DoShare 探索个人云盘的买断方案：自建存储基础设施与单次付费",
        "url": "https://getcloud.doshare.me/",
        "media": "https://iandaily.xyz/digest/2026-11-09-doshare-629f6af3ffab.jpg",
        "source": "getcloud.doshare.me"
    },
    {
        "category": "一人公司",
        "title": "FuelPriceAtlas 汇总各国官方油价：微型垂直数据聚合与出海工具变现",
        "url": "https://fuelpriceatlas.com/",
        "media": "https://iandaily.xyz/digest/2026-11-09-fuelatlas-8bc2f94b17b8.jpg",
        "source": "fuelpriceatlas.com"
    },
    {
        "category": "一人公司",
        "title": "Kindle 摘录整理器把修改保留在浏览器：纯本地离线阅读批注管理",
        "url": "https://kindleclippings.pages.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-09-kindleclip-af8274fc6702.jpg",
        "source": "kindleclippings.pages.dev"
    },
    # 产品设计
    {
        "category": "产品设计",
        "title": "Tab-league 给关闭标签页留条退路：防误关浏览历史快速挽回交互",
        "url": "https://github.com/Shann5/tab-league",
        "media": "https://iandaily.xyz/digest/2026-11-09-tableague-f7907148295e.jpg",
        "source": "github.com"
    },
    {
        "category": "产品设计",
        "title": "Notekpr 把协作笔记加密后再同步：端到端零知识安全笔记体验",
        "url": "https://notekpr.md",
        "media": "https://iandaily.xyz/digest/2026-11-09-notekpr-61235978c7e4.jpg",
        "source": "notekpr.md"
    },
    {
        "category": "产品设计",
        "title": "Just a Pause 在你转头时模糊屏幕：基于视线感知的物理防窥交互设计",
        "url": "https://justapause.com",
        "media": "https://iandaily.xyz/digest/2026-11-09-justpause-59e5c1b1e31b.jpg",
        "source": "justapause.com"
    },
    {
        "category": "产品设计",
        "title": "Emcee 让窗口分组可以自由拖动：多任务平铺式原生窗口管理工作区",
        "url": "https://fuzzyfoundry.com/emcee",
        "media": "https://iandaily.xyz/digest/2026-11-09-emcee-70e8dedbfab8.jpg",
        "source": "fuzzyfoundry.com"
    },
    # 审美提升
    {
        "category": "审美提升",
        "title": "Raw Apartment 保留混凝土的原始肌理：粗野主义与温润木质共存的萨格勒布公寓",
        "url": "https://www.designboom.com/architecture/raw-concrete-steel-stripped-back-1960s-apartment-zagreb-simple-architecture/",
        "media": "https://iandaily.xyz/digest/2026-11-09-rawapartment-02bdd60dc816.jpg",
        "source": "designboom.com"
    },
    {
        "category": "审美提升",
        "title": "ZAO 将混凝土切口嵌进日照山坡：依山就势的纯粹雕塑感艺术中心",
        "url": "https://www.designboom.com/architecture/sweeping-concrete-zao-art-center-rizhao-china/",
        "media": "https://iandaily.xyz/digest/2026-11-09-rizhao-6497eca33bad.jpg",
        "source": "designboom.com"
    },
    {
        "category": "审美提升",
        "title": "SKNYPL 在拆迁现场架起观察座席：将城市废墟转化为建筑观察剧场",
        "url": "https://www.designboom.com/art/scaffolding-safety-mesh-observation-platforms-lugano-demolition-sites-sit-for-a-while-sknypl/",
        "media": "https://iandaily.xyz/digest/2026-11-09-sknypl-cd618936c012.jpg",
        "source": "designboom.com"
    },
    {
        "category": "审美提升",
        "title": "Angelo Lelii 的灯具把工程感做得轻巧：意大利战后现代主义灯光设计巡礼",
        "url": "https://www.wallpaper.com/design-interiors/lighting/angelo-lelii-guide-arredoluce-lighting-design",
        "media": "https://iandaily.xyz/digest/2026-11-09-lelii-b40d981be652.jpg",
        "source": "wallpaper.com"
    },
    # 产品营销
    {
        "category": "产品营销",
        "title": "Recap 自动把产品录屏的重点放大：无感聚焦的高转化产品 Demo 剪辑",
        "url": "https://recap.studio/",
        "media": "https://iandaily.xyz/digest/2026-11-09-recap-570ac1779e9b.jpg",
        "source": "recap.studio"
    },
    {
        "category": "产品营销",
        "title": "Aircheck 在发送前排齐代理写的帖子：社交矩阵多平台文案质量巡检门禁",
        "url": "https://aircheck.dev",
        "media": "https://iandaily.xyz/digest/2026-11-09-aircheck-86a670649793.jpg",
        "source": "aircheck.dev"
    },
    {
        "category": "产品营销",
        "title": "AIDA 从真实应用制作用户使用指南：自动化软件实操文档与高留存 Onboarding",
        "url": "https://github.com/tryaida/aida",
        "media": "https://iandaily.xyz/digest/2026-11-09-aida-302e248e5c22.jpg",
        "source": "github.com"
    },
    {
        "category": "产品营销",
        "title": "Shutdown Watch 提醒产品停服与导出期限：数字服务生命周期监测与防踩坑资产备份",
        "url": "https://shutdownwatch.com/",
        "media": "https://iandaily.xyz/digest/2026-11-09-shutdown-bcabd1b4de83.jpg",
        "source": "shutdownwatch.com"
    },
    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "专访《持械入宋》主创：非科班、无投流，草根团队如何做出120亿播放品质爆款",
        "url": "https://www.woshipm.com/ai/6490565.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "实时视频里参与剧情：Prelulu 探索可自由语音对话的沉浸式互动短剧",
        "url": "https://www.woshipm.com/ai/6490593.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "短剧出海泰国商业复盘：重走移动梦网短信代扣与本地化分发老路",
        "url": "https://www.woshipm.com/it/6490886.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "AI 漫剧",
        "title": "Codex + Obsidian + Skill：搭建一套个人专属的漫剧剧情与分镜生成工作台",
        "url": "https://www.woshipm.com/ai/6490727.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《正义的边界》微短剧 全本：都市律政悬疑、法律盲区与道德复仇博弈",
        "url": "https://www.wzbj1616.com/script_info/2245",
        "media": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《江湖镖局少年行》微短剧 全本：传统古装武侠情怀与草根少年群像成长",
        "url": "https://www.wzbj1616.com/script_info/2246",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《第七封印》微短剧 全本：悬疑棋局解谜、生死契约与哲学式命运反转",
        "url": "https://www.wzbj1616.com/script_info/2247",
        "media": "https://images.unsplash.com/photo-1529699211952-734e80c4d42b?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    {
        "category": "编剧技巧",
        "title": "《读书成圣》微短剧 全本：国风儒道修仙、书生逆袭与爽点节奏拆解",
        "url": "https://www.wzbj1616.com/script_info/2248",
        "media": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80",
        "source": "wzbj1616.com"
    },
    # 产品经理
    {
        "category": "产品经理",
        "title": "腾讯云 ADP 深度复盘：企业级 Service Agent 平台从「搭 Agent」到「管 Agent」",
        "url": "https://www.woshipm.com/evaluating/6490871.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "字节 AI 业务架构重整反思：为什么单点 Agent 工具必须融入业务死穴",
        "url": "https://www.woshipm.com/ai/6490861.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "生产级 Agent 为什么不是一个对话机器人，而是一套严密的业务运营系统",
        "url": "https://www.woshipm.com/ai/6447479.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "source": "woshipm.com"
    },
    {
        "category": "产品经理",
        "title": "从功能型 PM 转向 FDE（前向部署工程师）：直面客户泥泞战壕的破局之道",
        "url": "https://www.woshipm.com/pmd/6471893.html",
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
                # print(f"OK   [{t}] {code} -> {target}")
                pass

    if all_ok:
        print(f"SUCCESS: ALL {len(candidates)} items and their media returned HTTP 200/OK!")
    else:
        print("FAIL: Some endpoints failed verification.")

if __name__ == "__main__":
    main()
