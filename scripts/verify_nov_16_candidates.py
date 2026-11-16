# -*- coding: utf-8 -*-
import os
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(_ROOT)
import subprocess
import json
import concurrent.futures
import time
import threading

candidates = [
    # AI 资讯
    {"category": "AI 资讯",
     "title": "黄仁勋的谢幕与 Neo Cloud 的黄昏：算力叙事进入权力交接期",
     "url": "https://www.woshipm.com/ai/6494217.html",
     "media": "https://image.woshipm.com/2023/04/13/d34ae8a8-d9e1-11ed-9d7a-00163e0b5ff3.jpg",
     "source": "woshipm.com", "pinned": True},
    {"category": "AI 资讯",
     "title": "一张图吓得研究员当场辞职：Anthropic 最疯的一张神图流出",
     "url": "https://www.woshipm.com/ai/6494223.html",
     "media": "https://image.woshipm.com/wp-files/sha256/93/8b/938b6a8e477107c5de9561fb93da8c6d031763c0fb7a9581fa9ca116fbf35ae3.png",
     "source": "woshipm.com"},
    {"category": "AI 资讯",
     "title": "Nano-Edge-TTS：把语音解码器压到 175 万参数，边缘设备也能跑 TTS",
     "url": "https://huggingface.co/drmhse/nano-edge-tts",
     "media": "https://cdn-thumbnails.huggingface.co/social-thumbnails/models/drmhse/nano-edge-tts.png",
     "source": "huggingface.co"},
    {"category": "AI 资讯",
     "title": "Raschka 拆解大模型位置编码：从位置嵌入讲到 RoPE，词序如何进入注意力",
     "url": "https://magazine.sebastianraschka.com/p/understanding-positional-embeddings",
     "media": "https://substackcdn.com/image/fetch/$s_!UHlM!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a036907-4c1e-473b-8d82-20f2c777df5f_2912x1632.png",
     "source": "sebastianraschka.com"},

    # AI 协作
    {"category": "AI 协作",
     "title": "Pizza：用不可变事件日志组织 Agent 每一轮工作，工作区靠 tell 通信",
     "url": "https://pizza.hertzbeat.com/",
     "media": "https://pizza.hertzbeat.com/media/pizza-studio.webp",
     "source": "pizza.hertzbeat.com", "pinned": True},
    {"category": "AI 协作",
     "title": "Canban：给命令行 Agent 加一块看板，任务与工作流放进统一工作台",
     "url": "https://canban.dev",
     "media": "https://canban.dev/og-image.png",
     "source": "canban.dev"},
    {"category": "AI 协作",
     "title": "Attest：把 Agent 的实测行为纳入评测，让测试走出回答文本",
     "url": "https://attest-framework.github.io/",
     "media": "https://attest-framework.github.io/og.png",
     "source": "attest-framework.github.io"},
    {"category": "AI 协作",
     "title": "MinePilot：把三维建造验收到游戏里，代码通过后还得看原生世界",
     "url": "https://www.bmpi.dev/dev/agent-3d-world-building/",
     "media": "https://img.bmpi.dev/agent-3d-world-building-3.webp",
     "source": "bmpi.dev"},

    # 一人公司
    {"category": "一人公司",
     "title": "5 个人零融资做到年入 700 万美元：小团队如何用 AI 放大 10 倍战斗力",
     "url": "https://www.woshipm.com/ai/6262646.html",
     "media": "https://image.woshipm.com/2024/04/13/66621a94-f980-11ee-b799-00163e142b65.png",
     "source": "woshipm.com", "pinned": True},
    {"category": "一人公司",
     "title": "33 天年收入从 100 万涨到 200 万美金：这个 AI 浏览器到底做对了什么",
     "url": "https://www.woshipm.com/chuangye/6494211.html",
     "media": "https://image.woshipm.com/wp-files/sha256/df/99/df99648c097a3d3a9daa3b96ebd0c1310cf4829fcd5e4130424ae0cee6213b9b.jpg",
     "source": "woshipm.com"},
    {"category": "一人公司",
     "title": "北大「浪漫极客」的 AI 相机，凭什么月入 129 万美元",
     "url": "https://www.woshipm.com/share/6494071.html",
     "media": "https://image.woshipm.com/wp-files/sha256/b7/df/b7dfcf73957e4e83506d87bf2bf73e6d265d8b7572e376a1544060302f6ee587.jpg",
     "source": "woshipm.com"},
    {"category": "一人公司",
     "title": "简造 ERP：从亲戚小厂的进销存起步，做给两三人家庭小仓的开源系统",
     "url": "https://github.com/Fawkes-hub/jianzao-erp-community",
     "media": "https://iandaily.xyz/digest/2026-11-16-erp-7f9d39e58ab1.jpg?v=2026-11-16",
     "source": "github.com"},

    # 产品设计
    {"category": "产品设计",
     "title": "Remindly：把提醒留进笔记里，按下 Esc 也不丢未提交草稿",
     "url": "https://www.remindly.com/",
     "media": "https://www.remindly.com/images/og-home.png",
     "source": "remindly.com", "pinned": True},
    {"category": "产品设计",
     "title": "Dynaura：把通知做成灵动岛，零依赖组件在胶囊与卡片之间弹性变形",
     "url": "https://dynaura.ashutoshswamy.in",
     "media": "https://dynaura.ashutoshswamy.in/opengraph-image.png",
     "source": "dynaura.ashutoshswamy.in"},
    {"category": "产品设计",
     "title": "SecondGlow：让 2015–2020 年的旧 iMac 变成 Apple 芯片 Mac 的外接屏",
     "url": "https://secondglow.app/",
     "media": "https://secondglow.app/og.png",
     "source": "secondglow.app"},
    {"category": "产品设计",
     "title": "VimPDF：用快捷键串起阅读与复习，高亮批注直连复习卡片",
     "url": "https://github.com/zhpencil/VimPDF",
     "media": "https://opengraph.githubassets.com/cfafe734c355c5d6b98a1b58a1a84198f4f3b6cee2054b44d4513c30a8bb03b5/zhpencil/VimPDF",
     "source": "github.com"},

    # 审美提升
    {"category": "审美提升",
     "title": "来杯 1087：用可拆家具接近唐代古建，让新增部分随时能撤回",
     "url": "https://www.dezeen.com/2026/11/15/tant-a-temps-design-tang-architecture-cafe-laibei-1087-china/",
     "media": "https://static-2026.dezeen.com/uploads/2026/11/tant-a-temp-design-laibei-1087-interior-cafe-sq_dezeen_2364_col_0.jpg",
     "source": "dezeen.com", "pinned": True},
    {"category": "审美提升",
     "title": "Mecanoo 把荷兰央行金库向公众打开：拆掉十四层后加圆塔，松开防御边界",
     "url": "https://www.dezeen.com/2026/11/15/netherlands-central-bank-renovation-mecanoo/",
     "media": "https://static-2026.dezeen.com/uploads/2026/11/mecanoo-de-nederlandsche-bank_dezeen_2364_sq_0.jpg",
     "source": "dezeen.com"},
    {"category": "审美提升",
     "title": "La Lenta：把人人心里的家用椅子拉长成海边公共长凳，取消分隔扶手",
     "url": "https://www.designboom.com/design/gio-tirotto-domestic-chair-public-bench-italy-gulf-poets-vita-lenta/",
     "media": "https://www.designboom.com/twitterimages/uploads/2026/11/la-lenta-chair-public-bench-vita-lenta-gio-tirotto-designboom-1200-1.jpg",
     "source": "designboom.com"},
    {"category": "审美提升",
     "title": "Funny Weather：把曼彻斯特的实时天气数据变成一场展览",
     "url": "https://www.designboom.com/art/bird-plane-funny-weather-theo-triantafyllidis/",
     "media": "https://www.designboom.com/twitterimages/uploads/2026/11/funny-weather-designboom-10.jpg",
     "source": "designboom.com"},

    # 产品营销
    {"category": "产品营销",
     "title": "a16z 合伙人最新分析：AI 应用该如何获得高溢价，而不是陷入价格战",
     "url": "https://www.woshipm.com/ai/6494227.html",
     "media": "https://image.woshipm.com/2023/04/14/89a386c0-da9e-11ed-aaf8-00163e0b5ff3.png",
     "source": "woshipm.com", "pinned": True},
    {"category": "产品营销",
     "title": "品牌如何优雅地「说谎」，或者正确地「讲真」",
     "url": "https://www.woshipm.com/share/6494231.html",
     "media": "https://image.woshipm.com/2023/04/14/85dbf876-daa1-11ed-9b82-00163e0b5ff3.png",
     "source": "woshipm.com"},
    {"category": "产品营销",
     "title": "DeclineKit：用开源回应支付信任问题，从免费诊断走向订阅恢复工具",
     "url": "https://github.com/jmcbca04/declinekit",
     "media": "https://iandaily.xyz/digest/2026-11-16-declinekit-9a13b19e2d28.jpg?v=2026-11-16",
     "source": "github.com"},
    {"category": "产品营销",
     "title": "GamiFied：把业务事件接成成长系统，经验值与徽章带幂等处理",
     "url": "https://gami.fied.cc/",
     "media": "https://gami.fied.cc/og/index.png",
     "source": "gami.fied.cc"},

    # AI 漫剧
    {"category": "AI 漫剧",
     "title": "若投 100 万复刻《持械入宋》：两大国产新图模，你会 Pick 谁？",
     "url": "https://www.woshipm.com/evaluating/6494225.html",
     "media": "https://image.woshipm.com/2023/07/07/4732f132-1c97-11ee-94c6-00163e0b5ff3.jpg",
     "source": "woshipm.com", "pinned": True},
    {"category": "AI 漫剧",
     "title": "我用 AI 做出 300 万播放爆款视频：完整制作流程逐环节拆给你看",
     "url": "https://www.woshipm.com/ai/6493996.html",
     "media": "https://image.woshipm.com/2023/04/14/2ecb8e6e-da8f-11ed-aeb8-00163e0b5ff3.jpg",
     "source": "woshipm.com"},
    {"category": "AI 漫剧",
     "title": "两个任务烧穿月度套餐：Fable 5.2 的规划能力到底强在哪、贵在哪",
     "url": "https://www.woshipm.com/evaluating/6494221.html",
     "media": "https://image.woshipm.com/2023/04/13/6ffba1d2-d9de-11ed-9d2f-00163e0b5ff3.jpg",
     "source": "woshipm.com"},
    {"category": "AI 漫剧",
     "title": "AI 艺人，你以为你有得选？虚拟形象与真人权益的灰色地带",
     "url": "https://www.woshipm.com/ai/6444818.html",
     "media": "https://image.woshipm.com/2023/04/20/2f924458-df4b-11ed-81f2-00163e0b5ff3.png",
     "source": "woshipm.com"},

    # 编剧技巧
    {"category": "编剧技巧",
     "title": "琼瑶《窗外》35 集电视剧改编：青春成长与年代情感的困境书写",
     "url": "https://www.wzbj1616.com/script_info/1671",
     "media": "https://www.wzbj1616.com/storage/script/20260203/ed95c5f7e5222b1d46f708c9cb616317.png",
     "source": "wzbj1616.com", "pinned": True},
    {"category": "编剧技巧",
     "title": "《黑客帝国 2》中文剧本：续作如何在不重复第一部的前提下抬高赌注",
     "url": "https://www.wzbj1616.com/script_info/2298",
     "media": "https://www.wzbj1616.com/storage/script/20261027/39c06c9661878d6c1f594d7a9fa3936c.png",
     "source": "wzbj1616.com"},
    {"category": "编剧技巧",
     "title": "玄幻短剧《玄天归尘：玉女心经》：男频爽剧的功法体系与身份反转设计",
     "url": "https://www.wzbj1616.com/script_info/2323",
     "media": "https://www.wzbj1616.com/storage/script/20261103/dccfda7b0e38b0e320fd0d8e4c913d16.png",
     "source": "wzbj1616.com"},
    {"category": "编剧技巧",
     "title": "《反诈使命 平安中国》200 集短剧：把反诈知识组织成可连载的单元结构",
     "url": "https://www.wzbj1616.com/script_info/1690",
     "media": "https://www.wzbj1616.com/storage/script/20260304/2b3b644f9eee5bd2f1aceaabcde43a83.png",
     "source": "wzbj1616.com"},

    # 产品经理
    {"category": "产品经理",
     "title": "AI 能帮人做出系统，接下来谁来管？交付之后的运维归属难题",
     "url": "https://www.woshipm.com/pd/6494104.html",
     "media": "https://image.woshipm.com/wp-files/2026/11/cAbVqGTjZ83w7V2TpdLq.png",
     "source": "woshipm.com", "pinned": True},
    {"category": "产品经理",
     "title": "GTM 和 PM 到底有什么差异，又该如何协同",
     "url": "https://www.woshipm.com/pmd/6276577.html",
     "media": "https://image.woshipm.com/2023/04/13/52817d8e-d9de-11ed-bd5e-00163e0b5ff3.jpg",
     "source": "woshipm.com"},
    {"category": "产品经理",
     "title": "AI 工程师产出翻八倍后，Anthropic 团队发现了新的协作难题",
     "url": "https://www.woshipm.com/share/6419345.html",
     "media": "https://image.woshipm.com/2025/08/26/0a65fb1a-823d-11f0-8601-00163e4b86a1.png",
     "source": "woshipm.com"},
    {"category": "产品经理",
     "title": "一个产品经理的生存报告：沟通、排雷，以及与自己和解",
     "url": "https://www.woshipm.com/ai/6452804.html",
     "media": "https://image.woshipm.com/2023/04/14/f097777a-da8e-11ed-b69c-00163e0b5ff3.jpg",
     "source": "woshipm.com"},
]

woshipm_lock = threading.Lock()


def check_url(target):
    if "woshipm.com" in target:
        with woshipm_lock:
            time.sleep(0.7)
            cmd = ["curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}",
                   "--max-time", "22", "--noproxy", "*",
                   "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36", target]
            try:
                return target, subprocess.run(cmd, capture_output=True, text=True, timeout=40).stdout.strip()
            except Exception as e:
                return target, f"ERR:{e}"
    cmd = ["curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "22",
           "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"]
    if "wzbj1616.com" in target:
        cmd += ["--noproxy", "*"]
    cmd.append(target)
    try:
        return target, subprocess.run(cmd, capture_output=True, text=True, timeout=40).stdout.strip()
    except Exception as e:
        return target, f"ERR:{e}"


def main():
    print(f"Total candidates: {len(candidates)}")
    cats, pinned = {}, {}
    for c in candidates:
        cats[c["category"]] = cats.get(c["category"], 0) + 1
        if c.get("pinned"):
            pinned[c["category"]] = pinned.get(c["category"], 0) + 1
    assert len(candidates) == 36, len(candidates)
    assert len(cats) == 9 and all(v == 4 for v in cats.values()), cats
    assert all(pinned.get(k) == 1 for k in cats), pinned

    used = set(json.load(open("scripts/all-used-urls.json")))
    dups = [c["url"] for c in candidates if c["url"] in used]
    if dups:
        print("ERROR duplicates:")
        for d in dups:
            print("  DUP:", d)
        return
    print("PASS: 0 duplicates against global used database.")

    endpoints = []
    for c in candidates:
        endpoints.append(("URL", c["url"]))
        endpoints.append(("MEDIA", c["media"]))
    print(f"Verifying {len(endpoints)} endpoints...")
    ok = True
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        fm = {ex.submit(check_url, u): (t, u) for t, u in endpoints}
        for f in concurrent.futures.as_completed(fm):
            t, u = fm[f]
            target, code = f.result()
            if code not in ("200", "301", "302", "308"):
                print(f"FAIL [{t}] {code} -> {target}")
                ok = False
    print(f"SUCCESS: ALL {len(candidates)} items and their media returned HTTP 200/OK!" if ok else "FAIL: some endpoints failed.")


if __name__ == "__main__":
    main()
