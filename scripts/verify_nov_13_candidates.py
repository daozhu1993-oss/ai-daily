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
        "title": "字节跳动重拳出击协同生态：豆包工作全面开放模型接入，正面对决腾讯 WorkBuddy",
        "url": "https://www.woshipm.com/ai/6493081.html",
        "media": "https://tu.aixq.cc/wp-content/uploads/2026/11/WorkBuddy-01-18ee06c008.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "BAT 新旗舰大模型杀回第一阵营：从跑分虚火走向企业级生产落地的真实压力",
        "url": "https://www.woshipm.com/it/6493196.html",
        "media": "https://image.woshipm.com/2023/04/14/a1aa684c-da9e-11ed-af94-00163e0b5ff3.png",
        "source": "woshipm.com",
    },
    {
        "category": "AI 资讯",
        "title": "实测深度原理 Hydrogen-1.0：比 GPT-6Astra 更适合科研推理与文献跨越的新范式",
        "url": "https://www.woshipm.com/ai/6492556.html",
        "media": "https://image.woshipm.com/2023/09/26/150398ca-5c65-11ee-b266-00163e142b65.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "AI 资讯",
        "title": "Evolving Infra：Agent-Adaptive LLM Serving at Scale 动态自适应智能体长上下文推理基建",
        "url": "https://huggingface.co/papers/2611.12304",
        "media": "https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2611.12304/gradient.png",
        "source": "huggingface.co",
    },
    # AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "SafeScript：为大模型 Agent 执行不可信代码打造真正安全的 JavaScript 极简隔离子集",
        "url": "https://github.com/SafeScript/safescript",
        "media": "https://opengraph.githubassets.com/dfdd1d97d8fc541c6565ed431204dd3f19f4d20270c00ed99a48cadb26a07f68/SafeScript/safescript",
        "source": "github.com",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "Attention Queue（Aq）：为 tmux 中的 Claude Code 终端会话搭建注意力审查与分步确认队列",
        "url": "https://github.com/nodo-labs-uk/attention-queue",
        "media": "https://opengraph.githubassets.com/1536b5025a5fc59545e8559aa9cdc109b8a6d15ebc7fef691c51bccf8b580fec/nodo-labs-uk/attention-queue",
        "source": "github.com",
    },
    {
        "category": "AI 协作",
        "title": "腾讯 WorkBuddy 生产级 Agent 底牌拆解：从 REA 状态机到多 Agent 组织调度架构",
        "url": "https://www.woshipm.com/ai/6481849.html",
        "media": "https://image.woshipm.com/2023/04/14/89a13ea6-da9e-11ed-9b82-00163e0b5ff3.png",
        "source": "woshipm.com",
    },
    {
        "category": "AI 协作",
        "title": "Grok Bot 迎来大版本进化：异步协作军团全面进驻团队，AI 同事开始主动承包脏活",
        "url": "https://www.woshipm.com/ai/6492769.html",
        "media": "https://image.woshipm.com/2024/07/02/083e0566-386b-11ef-90af-00163e142b65.png",
        "source": "woshipm.com",
    },
    # 一人公司 (4)
    {
        "category": "一人公司",
        "title": "前 TikTok 核心成员转型 AI 原生单兵公司：月费 2500 美元驱动 Agent 军团承包 20 人产出",
        "url": "https://www.woshipm.com/chuangye/6492482.html",
        "media": "https://image.woshipm.com/wp-files/sha256/1a/22/1a22abb9bcbc7939409c7e7e82d609a6f8598a745276db3abfa11c299d187131.png",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "下一代反上瘾社交产品：不拼时长拼效率，想尽办法让用户用完即走",
        "url": "https://www.woshipm.com/chuangye/6493011.html",
        "media": "https://image.woshipm.com/2023/09/26/15020a50-5c65-11ee-bd4e-00163e142b65.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "一人公司",
        "title": "Term Sheet, Please：独立开发者像素级复刻“请出示文件”，把硅谷 VC 尽职调查做成高黏性互动游戏",
        "url": "https://termsheetplease.com/",
        "media": "https://termsheetplease.com/assets/social-preview.png?v=title-only-20261110",
        "source": "termsheetplease.com",
    },
    {
        "category": "一人公司",
        "title": "Litek8s：单个纯 Rust 二进制文件实现完整 Kubernetes API，空载仅占 23MB 内存",
        "url": "https://litek8s.dev/",
        "media": "https://litek8s.dev/og.png",
        "source": "litek8s.dev",
    },
    # 产品设计 (4)
    {
        "category": "产品设计",
        "title": "云风 CodingNow 动手魔改智能 ABC 输入法：在极简键盘交互与心流保护中找回纯粹手感",
        "url": "https://blog.codingnow.com/2026/11/abc_mod.html",
        "media": "https://iandaily.xyz/digest/2026-11-10-abcmod-2911678563c4.jpg",
        "source": "codingnow.com",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "Spirolo：用 Rust 打造的前端测试套件隐患静态扫描仪，极具质感的可视化报告设计",
        "url": "https://spirolo.com/",
        "media": "https://spirolo.com/brand/scenes/bug-in-a-jar.webp",
        "source": "spirolo.com",
    },
    {
        "category": "产品设计",
        "title": "Airgap-check：排查 AI 代码仓库在离线网络隔离（--network none）下的意外崩溃隐患",
        "url": "https://github.com/humanethq/airgap-check",
        "media": "https://opengraph.githubassets.com/dfee1c70941eeab8cdaed25aa890f5ca1dd16af2ee302da1eb0003d7b847a014/humanethq/airgap-check",
        "source": "github.com",
    },
    {
        "category": "产品设计",
        "title": "Safe Sand：基于 WebGL2 的超拟真流体沙粒物理交互，在浏览器端呈现极致顺滑质感",
        "url": "https://av.github.io/safe-sand/",
        "media": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
        "source": "av.github.io",
    },
    # 审美提升 (4)
    {
        "category": "审美提升",
        "title": "Minimal 推出 Pedal 4：将小型厢式货车与电动货运自行车美学融为一体的微出行创新",
        "url": "https://www.dezeen.com/2026/11/12/minimal-pedal-4-delivery-vehicle/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/pedal-4-cargo-vehicle-minimal-design_dezeen_2364_hero.jpg",
        "source": "dezeen.com",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Sony 经典 Walkman 橙色海绵耳机以 MDR-3R 重生：工业设计复古回潮与情怀极简克制",
        "url": "https://www.dezeen.com/2026/11/09/sony-walkman-headphones-mdr-3r/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/sony-mdr-3r-headphones_dezeen_2364_col_0.jpg",
        "source": "dezeen.com",
    },
    {
        "category": "审美提升",
        "title": "Dado 家具系列：仅凭单一机械卡榫咬合全套实木结构，结构即装饰的极致减法美学",
        "url": "https://www.dezeen.com/2026/11/06/dado-furniture-allen-kaufmann/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/hero3-designart-tokyo-highlights-c_dezeen_2364_col_0.jpg",
        "source": "dezeen.com",
    },
    {
        "category": "审美提升",
        "title": "Gustaf Westman 推出迪士尼联名全套家居：唐老鸭经典屁股书立与波浪曲面雕塑美学",
        "url": "https://www.dezeen.com/2026/11/10/gustaf-westman-full-disney-collection-donald-duck-bookstand/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/gustaf-westman-disney-collection_dezeen_2364_col_hero.jpg",
        "source": "dezeen.com",
    },
    # 产品营销 (4)
    {
        "category": "产品营销",
        "title": "20 元泡面与 399 羽绒服：山姆会员店如何用高反差爆款掌握大众情绪与流量主动权",
        "url": "https://www.woshipm.com/operate/6493004.html",
        "media": "https://image.woshipm.com/2023/04/13/bdb39b0e-d9e9-11ed-bd74-00163e0b5ff3.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "把外卖平台当“抖加”投流：餐饮商家借平台满减补贴撬动全城曝光的裂变新玩术",
        "url": "https://www.woshipm.com/it/6493087.html",
        "media": "https://image.woshipm.com/2023/04/13/ffdf9b9a-d9ee-11ed-a8b0-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品营销",
        "title": "门店攻防战役复盘：为什么盲目拼补贴容易“赢了表面市场份额，却输掉最忠诚的客户”？",
        "url": "https://www.woshipm.com/marketing/6492890.html",
        "media": "https://image.woshipm.com/2023/04/14/17ef0252-da8f-11ed-a86f-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品营销",
        "title": "你的经验可以被复制粘贴了：Agent Skills 规范正在引爆知识与行业资产化变现实践",
        "url": "https://www.woshipm.com/ai/6332345.html",
        "media": "https://image.woshipm.com/wp-files/2026/01/7zSBtlut3gN2b86biC4v.jpeg",
        "source": "woshipm.com",
    },
    # AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "AI 影视剧爆发元年：Seedance 跑通全流程数字人生成与高逼真长篇剧集交付",
        "url": "https://www.woshipm.com/it/6492533.html",
        "media": "https://image.woshipm.com/wp-files/2026/11/GMuk7hWSpezb9OEgyZJO.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "为什么专业设计师做 AI 漫剧生图就是比普通人高级？拆解视觉控制网与镜头语言鸿沟",
        "url": "https://www.woshipm.com/ai/6492976.html",
        "media": "https://image.woshipm.com/2023/04/13/9b6f47f6-d9de-11ed-8fc2-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "AI 漫剧",
        "title": "主流生图模型深度横评：MiniMax 与 Seedream 在漫剧分镜连贯性与角色保真上的路线抉择",
        "url": "https://www.woshipm.com/ai/6492564.html",
        "media": "https://image.woshipm.com/2023/07/07/4732f132-1c97-11ee-94c6-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "AI 漫剧",
        "title": "轻松玩转短剧分镜图生成：Lovart 接入 Midjourney 实现一站式漫剧生图与运镜推拉",
        "url": "https://www.woshipm.com/ai/6276556.html",
        "media": "https://image.woshipm.com/2025/10/04/22d73f26-a0cc-11f0-8601-00163e4b86a1.png",
        "source": "woshipm.com",
    },
    # 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "120 集女频穿书微短剧《穿成虐文炮灰千金，我不演了》：拒绝被规训的人设掀桌与爽点递进",
        "url": "https://www.wzbj1616.com/script_info/2261",
        "media": "https://www.wzbj1616.com/storage/script/20261015/416545932e38352e3214ab663c35e541.png",
        "source": "wzbj1616.com",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "甜宠萌宝微短剧《替嫁萌宝》全 120 集：先婚后爱母题下的极致反差萌与家庭情感张力",
        "url": "https://www.wzbj1616.com/script_info/2256",
        "media": "https://www.wzbj1616.com/storage/script/20261013/d355a9da9abe265865a3624d40d658b4.png",
        "source": "wzbj1616.com",
    },
    {
        "category": "编剧技巧",
        "title": "都市情感短剧剧本《她说没事》：职场讨好型人格觉醒与微表情因果冲突推演",
        "url": "https://www.wzbj1616.com/script_info/2264",
        "media": "https://www.wzbj1616.com/storage/script/20261016/b0b8a344f8f4f740c1b950c19683a0ed.png",
        "source": "wzbj1616.com",
    },
    {
        "category": "编剧技巧",
        "title": "奇幻轻喜剧剧本《月迷津渡》：微恐悬疑与轻喜甜宠双线交织的情绪波浪模型",
        "url": "https://www.wzbj1616.com/script_info/2265",
        "media": "https://www.wzbj1616.com/storage/script/20261015/4e3d2220841b7d89f651678aa58b4e91.png",
        "source": "wzbj1616.com",
    },
    # 产品经理 (4)
    {
        "category": "产品经理",
        "title": "从共情到决断：女性产品经理与复杂系统操盘者的核心进阶跃迁法则",
        "url": "https://www.woshipm.com/pmd/6487883.html",
        "media": "https://image.woshipm.com/2023/04/14/55f8cb98-da8d-11ed-96fe-00163e0b5ff3.png",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "回归常识本质：在 AI 席卷一切的当下重新审视产品经理不可替代的 5 大核心职责",
        "url": "https://www.woshipm.com/pmd/6472679.html",
        "media": "https://image.woshipm.com/2025/08/19/edd47568-7caf-11f0-a249-00163e09d72f.png",
        "source": "woshipm.com",
    },
    {
        "category": "产品经理",
        "title": "别总指望 AI 替你做产品定义：为什么真正艰难的商业权衡永远无法依靠提示词外包",
        "url": "https://www.woshipm.com/ai/6404370.html",
        "media": "https://image.woshipm.com/2024/02/05/88790cb0-c40a-11ee-a51d-00163e142b65.png",
        "source": "woshipm.com",
    },
    {
        "category": "产品经理",
        "title": "别急着算同比：数据产品经理在复杂业务周期与统计口径里踩过的隐蔽暗坑",
        "url": "https://www.woshipm.com/share/6319547.html",
        "media": "https://image.woshipm.com/2023/04/13/deb110a2-d9df-11ed-8fc2-00163e0b5ff3.jpg",
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
    for c in candidates:
        cats[c["category"]] = cats.get(c["category"], 0) + 1
    assert len(candidates) == 36 and len(cats) == 9 and all(v == 4 for v in cats.values()), cats

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
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_map = {executor.submit(check_url, u): (t, u) for t, u in urls_to_test}
        for future in concurrent.futures.as_completed(future_map):
            t, u = future_map[future]
            target, code = future.result()
            if code not in ["200", "301", "302", "308"]:
                print(f"FAIL [{t}] {code} -> {target}")
                all_ok = False

    if all_ok:
        print(f"SUCCESS: ALL {len(candidates)} items and their media returned HTTP 200/OK!")
    else:
        print("FAIL: Some endpoints failed verification.")


if __name__ == "__main__":
    main()
