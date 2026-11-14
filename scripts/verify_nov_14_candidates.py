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
        "title": "实测文心5.5 Flash Preview：侧重编码效率与低延迟推理的工程答卷",
        "url": "https://www.woshipm.com/ai/6493816.html",
        "media": "https://image.woshipm.com/2024/09/24/7300a312-7a66-11ef-b388-00163e142b65.png",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "高难盲测超越 GPT-6-Astra 与 Opus-5！无界前沿开源 Fx-Bio-1031，把 RSI 带进生命科学",
        "url": "https://www.woshipm.com/ai/6493529.html",
        "media": "https://image.woshipm.com/2023/04/14/91d2911a-da9e-11ed-95a1-00163e0b5ff3.png",
        "source": "woshipm.com",
    },
    {
        "category": "AI 资讯",
        "title": "谷歌今日换脑：轻量之王 Gemini 4 Hydrogen 反杀旗舰，端侧高频调用迎变局",
        "url": "https://www.woshipm.com/ai/6493404.html",
        "media": "https://image.woshipm.com/wp-files/sha256/c5/aa/c5aafb13f36058ab67c6a77adc7ee6ccfbdcfde0cbea4f880ac4eade2af45263.png",
        "source": "woshipm.com",
    },
    {
        "category": "AI 资讯",
        "title": "PhysLoop：利用大模型物理常识先验驱动视频生成的自我闭环演进架构",
        "url": "https://huggingface.co/papers/2611.16748",
        "media": "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2611.16748/gradient.png",
        "source": "huggingface.co",
    },

    # AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "Memro：为 Claude Code、Cursor 与 Codex 打造跨会话持久记忆与上下文演进层",
        "url": "https://github.com/memrohq/memro",
        "media": "https://opengraph.githubassets.com/89a84a3076132455df38fc7dbd175c1606837f283a83a0e64a849e5b674f14c7/memrohq/memro",
        "source": "github.com",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "AgentRun：开源自进化长流程托管 Agent 平台，实现端到端任务自治演进",
        "url": "https://github.com/Parcha-ai/agentrun",
        "media": "https://opengraph.githubassets.com/60f1467c486bfdf33f4c36ba410ae5cdff7cf36cc3c7209f8a40b1dd20215657/Parcha-ai/agentrun",
        "source": "github.com",
    },
    {
        "category": "AI 协作",
        "title": "Yogurt：纯本地私有化 AI 会议决策助手，无需云端同步的 Granola 开源硬核替代品",
        "url": "https://github.com/FrigadeHQ/yogurt",
        "media": "https://repository-images.githubusercontent.com/1453132706/355ef15b-b53b-4211-bd76-47cdaad9ef5b",
        "source": "github.com",
    },
    {
        "category": "AI 协作",
        "title": "重构团队信息流动：三条结构化提示词用企业微信 AI 接管日常日报周报流转",
        "url": "https://www.woshipm.com/ai/6464284.html",
        "media": "https://image.woshipm.com/2023/05/29/bcfce10c-fdc0-11ed-88d8-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },

    # 一人公司 (4)
    {
        "category": "一人公司",
        "title": "年入 40 亿美金的极简单兵财团：Bending Spoons 如何用 AI 系统化接管并购公司",
        "url": "https://www.woshipm.com/chuangye/6493395.html",
        "media": "https://image.woshipm.com/wp-files/sha256/a3/b1/a3b1f18c698a061c451bebfb44ecc33dfaef6c939e12af1cd4d20b97aaa5302b.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "22 岁登顶白手起家亿万富豪：从极小垂类痛点切入，一人公司如何撬动十倍级估值",
        "url": "https://www.woshipm.com/chuangye/6493393.html",
        "media": "https://image.woshipm.com/2023/05/06/a27d3370-ec01-11ed-bbb6-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "一人公司",
        "title": "Zigzag：不爽昂贵刺绣机软件强制订阅，极客用纯开源代码为创客手搓专业级排版工具",
        "url": "https://github.com/simpsoka/zigzag",
        "media": "https://opengraph.githubassets.com/7f8d1668bad088ceceab44cca465c833fbf432091fa9eef7abf5a2b58c2e490c/simpsoka/zigzag",
        "source": "github.com",
    },
    {
        "category": "一人公司",
        "title": "Anvil：单兵全栈重构交付体验，用自研 AI 工作流以传统外包 1/5 成本交付精品企业站",
        "url": "https://www.tryanvil.dev/",
        "media": "https://www.tryanvil.dev/og-image.png",
        "source": "tryanvil.dev",
    },

    # 产品设计 (4)
    {
        "category": "产品设计",
        "title": "Terminal borders that don't cost a cell：终端字符界面的无损边框排版哲学",
        "url": "https://www.joshka.net/cell-borders/",
        "media": "https://www.joshka.net/cell-borders/og.png",
        "source": "joshka.net",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "全美大停飞之夜：独立开发者连夜手搓的实时空域停航动态地图与极简数据交互",
        "url": "https://grounds.top/",
        "media": "https://grounds.top/og.png",
        "source": "grounds.top",
    },
    {
        "category": "产品设计",
        "title": "AI 落地前的脏活比模型本身多：一个企业级用户反馈闭环全流程工程拆解",
        "url": "https://www.woshipm.com/pd/6493736.html",
        "media": "https://image.woshipm.com/wp-files/2026/11/qHy6eNF7rqZDLdd16E0X.png",
        "source": "woshipm.com",
    },
    {
        "category": "产品设计",
        "title": "Ember：开源接管 MacBook 充电指示灯状态，把单调硬件信号改造成开发心流指示器",
        "url": "https://github.com/Getterbetter/ember",
        "media": "https://opengraph.githubassets.com/390dc47a71a3f13d451f0713684e1a1cf3d75c0d0884ed7201134e64ead2c783/Getterbetter/ember",
        "source": "github.com",
    },

    # 审美提升 (4)
    {
        "category": "审美提升",
        "title": "Polestar Formula 2030 概念赛车：将纯粹机械张力与数字空气动力学推向极简巅峰",
        "url": "https://www.dezeen.com/2026/11/13/polestar-formula-2030-concept-car/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/polestar-formula-2030-concept-car-sq_dezeen_2364_col_1.jpg",
        "source": "dezeen.com",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "V&A East 博物馆全新仓储导视：解构 Z 世代手机交互界面，赋能实体文化漫步",
        "url": "https://www.dezeen.com/2026/11/13/va-east-storehouse-wayfinding-graphics/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/sq-fieldwork-facility-va-east-storehouse-wayfinding_dezeen_2364_col_0.jpg",
        "source": "dezeen.com",
    },
    {
        "category": "审美提升",
        "title": "六款极致静谧的现代声学家具：用温暖织物与吸音几何重塑开放空间的心理庇护所",
        "url": "https://www.dezeen.com/2026/11/13/six-quietening-acoustic-products-booths-pods-dezeen-showroom/",
        "media": "https://static-2026.dezeen.com/uploads/2026/10/zonify-wall-zonify-table-zilenzio-dezeen-showroom-hero.jpg",
        "source": "dezeen.com",
    },
    {
        "category": "审美提升",
        "title": "德州 Marburger 古董设计展馆：用回收废旧工业材料再生构筑历史与现代的对话空间",
        "url": "https://www.dezeen.com/2026/11/13/marburger-farm-antique-design-show/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/Marburger_sq1.jpg",
        "source": "dezeen.com",
    },

    # 产品营销 (4)
    {
        "category": "产品营销",
        "title": "熊本熊之父水野学：23 条穿透周期的设计与品牌逻辑，如何把普通符号做成超级资产",
        "url": "https://www.woshipm.com/share/6493688.html",
        "media": "https://image.woshipm.com/2023/04/17/ab0d3726-dcf5-11ed-ab4d-00163e0b5ff3.png",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "大促心理博弈深水区：为什么哪怕到了双十一，头部品牌依然不肯交出真正的全网底价",
        "url": "https://www.woshipm.com/operate/6493527.html",
        "media": "https://image.woshipm.com/wp-files/sha256/ed/fc/edfce49cbce546e9ea9d8dd56d26e1f9e04f8535b511c40ee619cdb009b3ae53.png",
        "source": "woshipm.com",
    },
    {
        "category": "产品营销",
        "title": "英伟达商业模式画布深度拆解：纵横 20 年的算力豪赌，真正的杀手锏从来不是 GPU",
        "url": "https://www.woshipm.com/operate/6493525.html",
        "media": "https://image.woshipm.com/wp-files/sha256/bb/31/bb31159d1e9274b870f0a0b9cc07575b0b017125047c42856054000dd4a7bc86.png",
        "source": "woshipm.com",
    },
    {
        "category": "产品营销",
        "title": "TikTok Shop 美区黑五决战：跨境电商如何在算法洗牌与本土化仓配中斩获确定性结果",
        "url": "https://www.woshipm.com/share/6493714.html",
        "media": "https://image.woshipm.com/wp-files/2026/11/xlli69zymcdAyq9gM9UB.jpeg",
        "source": "woshipm.com",
    },

    # AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "短剧里一场属于普通人的文艺复兴：下沉视听狂欢背后的人性共鸣与情感补偿机制",
        "url": "https://www.woshipm.com/ai/6493539.html",
        "media": "https://image.woshipm.com/2023/04/13/1c1e533c-d9ea-11ed-a8b0-00163e0b5ff3.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "本地算力跑通漫剧工业化：用 WorkBuddy 本地私有化部署 MiniMax H3 开源生视频模型",
        "url": "https://www.woshipm.com/ai/6493828.html",
        "media": "https://image.woshipm.com/2023/04/13/723384dc-d9df-11ed-8fc2-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "AI 漫剧",
        "title": "WorldDraft：如果代码负责构建虚拟世界，视频生成模型能否直接渲染电影级漫剧新范式？",
        "url": "https://huggingface.co/papers/2611.16217",
        "media": "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2611.16217/gradient.png",
        "source": "huggingface.co",
    },
    {
        "category": "AI 漫剧",
        "title": "别急着用粗糙偏见判死刑：AI 短剧背后的技术微迭代与视听工业重组需要多一点耐心",
        "url": "https://www.woshipm.com/ai/6493322.html",
        "media": "https://image.woshipm.com/wp-files/sha256/6e/71/6e7197c0315aa5b55b9922d7dd69d2539ec8b66616248b376d8ceadbb7f1d66f.jpg",
        "source": "woshipm.com",
    },

    # 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "荒诞黑色喜剧《伊尼舍林的报丧女妖》：极简双人关系、无解绝交与微观环境绝望压迫感",
        "url": "https://www.wzbj1616.com/script_info/2295",
        "media": "https://www.wzbj1616.com/storage/script/20261027/ee7e66f8177768060db7b9768eaffad7.png",
        "source": "wzbj1616.com",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "心理悬疑神作《禁闭岛》中文文学剧本：不可靠第一人称叙事与闭合空间精神创伤推演",
        "url": "https://www.wzbj1616.com/script_info/2285",
        "media": "https://www.wzbj1616.com/storage/script/20261023/c924c138de6203b0f3b026ea7fe0a620.png",
        "source": "wzbj1616.com",
    },
    {
        "category": "编剧技巧",
        "title": "轻喜奇幻动作《废犬战神去补天》：草根神话颠覆重构与萌宠视角下的反英雄叙事节奏",
        "url": "https://www.wzbj1616.com/script_info/2334",
        "media": "https://www.wzbj1616.com/storage/script/20261107/787b0fc4d143e6581e1f93c2e390cf91.png",
        "source": "wzbj1616.com",
    },
    {
        "category": "编剧技巧",
        "title": "古风大女主仙侠短剧《灭门遗孤：花不语》：强情境仇恨锚定与章末钩子连环悬念技巧",
        "url": "https://www.wzbj1616.com/script_info/1973",
        "media": "https://www.wzbj1616.com/storage/script/20261110/391c692f56eb341032dfbd4b659f79bb.jpg",
        "source": "wzbj1616.com",
    },

    # 产品经理 (4)
    {
        "category": "产品经理",
        "title": "重新审视企业级架构命题：到底是 SaaS+AI 补丁赋能，还是从第一天起重写 AI+SaaS？",
        "url": "https://www.woshipm.com/pd/6493149.html",
        "media": "https://image.woshipm.com/2023/04/14/0d78bf02-da8f-11ed-a86f-00163e0b5ff3.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "「抄-超-钞」进阶三步曲：产品经理如何从功能像素级模仿跃迁至商业价值收割闭环",
        "url": "https://www.woshipm.com/pmd/6213202.html",
        "media": "https://image.woshipm.com/2023/07/07/45438cd8-1c97-11ee-816e-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品经理",
        "title": "面对老板的狂热大模型冲动：一个成熟产品经理为什么坚决按住了核心业务无脑接入",
        "url": "https://www.woshipm.com/ai/6429765.html",
        "media": "https://image.woshipm.com/2023/08/31/a3411c44-47b0-11ee-9de9-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品经理",
        "title": "巨头踩雷的前车之鉴：Salesforce 在 Agent 商业化上摔过的坑，国内 SaaS 为何还在重复踩？",
        "url": "https://www.woshipm.com/share/6486486.html",
        "media": "https://image.woshipm.com/2023/04/14/778caa90-daa1-11ed-aee8-00163e0b5ff3.png",
        "source": "woshipm.com",
    },
]

woshipm_lock = threading.Lock()


def check_url(target):
    if "woshipm.com" in target:
        with woshipm_lock:
            time.sleep(0.4)
            cmd = [
                "curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}",
                "--max-time", "12", "--noproxy", "*",
                "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                target,
            ]
            try:
                res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
                return target, res.stdout.strip()
            except Exception as e:
                return target, f"ERR:{e}"

    cmd = [
        "curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}",
        "--max-time", "12",
        "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    ]
    if "wzbj1616.com" in target:
        cmd += ["--noproxy", "*"]
    cmd.append(target)
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return target, res.stdout.strip()
    except Exception as e:
        return target, f"ERR:{e}"


def main():
    print(f"Total candidates: {len(candidates)}")
    cats = {}
    pinned_count = {}
    for c in candidates:
        cats[c["category"]] = cats.get(c["category"], 0) + 1
        if c.get("pinned"):
            pinned_count[c["category"]] = pinned_count.get(c["category"], 0) + 1

    assert len(candidates) == 36, f"Expected 36 items, got {len(candidates)}"
    assert len(cats) == 9, f"Expected 9 categories, got {len(cats)}"
    assert all(v == 4 for v in cats.values()), f"Each category must have 4 items: {cats}"
    assert all(pinned_count.get(k) == 1 for k in cats.keys()), f"Each category must have exactly 1 pinned: {pinned_count}"

    with open("scripts/all-used-urls.json") as f:
        used = set(json.load(f))

    dups = [c["url"] for c in candidates if c["url"] in used]
    if dups:
        print(f"ERROR: {len(dups)} duplicate URLs found in history!")
        for d in dups:
            print("  DUP:", d)
        return
    print("PASS: 0 duplicates against global used database.")

    urls_to_test = []
    for c in candidates:
        urls_to_test.append(("URL", c["url"]))
        urls_to_test.append(("MEDIA", c["media"]))

    print(f"Starting parallel GET curl verification for {len(urls_to_test)} endpoints...")
    all_ok = True
    failed = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_map = {executor.submit(check_url, u): (t, u) for t, u in urls_to_test}
        for future in concurrent.futures.as_completed(future_map):
            t, u = future_map[future]
            target, code = future.result()
            if code not in ["200", "301", "302", "308"]:
                print(f"FAIL [{t}] {code} -> {target}")
                all_ok = False
                failed.append((t, code, target))

    if all_ok:
        print(f"SUCCESS: ALL {len(candidates)} items and their media returned HTTP 200/OK!")
    else:
        print(f"FAIL: {len(failed)} endpoints failed verification.")
        for t, code, target in failed:
            print(f"   [{t}] {code} -> {target}")


if __name__ == "__main__":
    main()
