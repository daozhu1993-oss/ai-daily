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
        "title": "Google 发布 Gemini Decisions API：单次调用完成千级多模态校准决策",
        "url": "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/",
        "media": "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini__decisions__blog-header_2784x1566.width-1300.png",
        "source": "blog.google",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "谷歌 Gemini 4 Carbon 全面开放实测：基准拉满之外的真实交互落差",
        "url": "https://www.woshipm.com/ai/6492919.html",
        "media": "https://image.woshipm.com/wp-files/sha256/6d/2e/6d2e30e4c89ecbb72efbead75b77da102d721888ca385dec2e764e983702ceb7.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "AI 资讯",
        "title": "实测 Qwen 4 Max Preview：代码与 3D 能力明显跃升，前端审美仍追赶 Fable 5.2",
        "url": "https://www.woshipm.com/ai/6492783.html",
        "media": "https://image.woshipm.com/2023/04/14/91d2911a-da9e-11ed-95a1-00163e0b5ff3.png",
        "source": "woshipm.com",
    },
    {
        "category": "AI 资讯",
        "title": "微信开源 WeVisOne-VL：把找人、点货、识字与发丝级抠图合成单一视觉工作流",
        "url": "https://www.woshipm.com/ai/6492755.html",
        "media": "https://image.woshipm.com/2024/11/04/17386a7a-9a81-11ef-b0e5-00163e142b65.jpg",
        "source": "woshipm.com",
    },
    # AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "Claude Bulkhead：阻断并发编程代理互相 pkill 开发服务器与抢占 Git 暂存区",
        "url": "https://github.com/dooly6276/claude-bulkhead",
        "media": "https://repository-images.githubusercontent.com/1416425499/75ea6f9c-2793-4b23-ae00-c229a2fa03da",
        "source": "github.com",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "Attentry：在本地实时拦截并逐条审查代码代理的文件系统篡改操作",
        "url": "https://github.com/Aarv-1o/Attentry",
        "media": "https://iandaily.xyz/digest/2026-11-10-attentrycheck-fcd714e96447.jpg",
        "source": "github.com",
    },
    {
        "category": "AI 协作",
        "title": "Smarchone Docs：让文档服务端读取行内批注并自动完成定稿修订",
        "url": "https://smarchone.github.io/docs/",
        "media": "https://iandaily.xyz/digest/2026-11-10-smarchonedocs-56f6da992812.jpg",
        "source": "smarchone.github.io",
    },
    {
        "category": "AI 协作",
        "title": "Jane Street 开源 Agent Skills（含 Socratic Tutor）：用苏格拉底式提问防大脑外包",
        "url": "https://github.com/janestreet/agent_skills",
        "media": "https://opengraph.githubassets.com/c3d1a16b5499ab11be3de6f802ccadf0673c6b9008056e6aad824a55aad7533a/janestreet/agent_skills",
        "source": "github.com",
    },
    # 一人公司 (4)
    {
        "category": "一人公司",
        "title": "a16z 合伙人提出 B2A 经济：B2B、B2C 之后，你的下一个大客户可能不是人",
        "url": "https://www.woshipm.com/ai/6492839.html",
        "media": "https://image.woshipm.com/wp-files/sha256/03/4b/034b5a69f69efa99c1bb95a7eb883d8c679951e5caac7bb2351d4a8c1ace50c2.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "MFlare：把 Cloudflare 额度预警与 Workers 构建状态搬进 macOS 菜单栏的精致小工具",
        "url": "https://mflare.yuy1n.io/",
        "media": "https://mflare.yuy1n.io/og.png",
        "source": "mflare.yuy1n.io",
    },
    {
        "category": "一人公司",
        "title": "FloodRoute：拖动时间轴在地图上精确回放历史洪涝淹水街区",
        "url": "https://floodroute.com",
        "media": "https://iandaily.xyz/digest/2026-11-10-floodroute-edec8f0cee6e.jpg",
        "source": "floodroute.com",
    },
    {
        "category": "一人公司",
        "title": "Deedbell：每天清晨只推送一条微小的日常善意行动提示",
        "url": "https://deedbell.com/today",
        "media": "https://iandaily.xyz/digest/2026-11-10-deedbell-85e422f308da.jpg",
        "source": "deedbell.com",
    },
    # 产品设计 (4)
    {
        "category": "产品设计",
        "title": "Watched Earth：输入任意坐标即刻追踪本周飞越头顶的人造卫星与实景航拍",
        "url": "https://www.watched.earth",
        "media": "https://iandaily.xyz/digest/2026-11-10-watchedearth-171207557bdc.jpg",
        "source": "watched.earth",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "Spektrafilm Negs：在浏览器里实时模拟传统物理胶片的光谱响应曲线",
        "url": "https://getnegs.com/try/",
        "media": "https://iandaily.xyz/digest/2026-11-10-getnegs-0f913616ab6e.jpg",
        "source": "getnegs.com",
    },
    {
        "category": "产品设计",
        "title": "Rat Race TS：将 1994 年 Mac 经典 68k 迷宫老鼠屏保逐帧复活到浏览器",
        "url": "https://rat-race.heyitsjam.es/",
        "media": "https://iandaily.xyz/digest/2026-11-10-ratracets-6cbc402f7bf3.jpg",
        "source": "heyitsjam.es",
    },
    {
        "category": "产品设计",
        "title": "Face Analysis：全程本地浏览器运算的人脸几何美学测算，隐私零上传",
        "url": "https://faceanalysis.app/",
        "media": "https://iandaily.xyz/digest/2026-11-10-faceanalysis-168e1b7beac5.jpg",
        "source": "faceanalysis.app",
    },
    # 审美提升 (4)
    {
        "category": "审美提升",
        "title": "Steven Holl 操刀 Cauny 雕塑感腕表：建筑师把光影体积语言戴上手腕",
        "url": "https://www.dezeen.com/2026/11/12/steven-holl-cauny-watch-tribute-alvaro-siza/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/steven-holl-cauny-watch-tribute-alvaro-siza_dezeen_2364_sq_21-1024x1024.jpg",
        "source": "dezeen.com",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Licht Kunst Licht 点亮科隆大教堂：700 盏隐形灯具重构百年哥特石雕夜色",
        "url": "https://www.dezeen.com/2026/11/12/licht-kunst-licht-cologne-cathedral/",
        "media": "https://static-2026.dezeen.com/uploads/2026/11/hero-licht-kunst-licht-cologne-cathedral_dezeen_2364_col_0.jpg",
        "source": "dezeen.com",
    },
    {
        "category": "审美提升",
        "title": "Oshinówò 为塞拉利昂搬运兵团设计玻璃棱镜纪念碑：轻盈折射沉重历史",
        "url": "https://www.dezeen.com/2026/11/09/freetown-memorial-sierra-leone-carrier-corps-tosin-oshinowo/",
        "media": "https://iandaily.xyz/digest/2026-11-10-oshinowomemorial-fea83a342351.jpg",
        "source": "dezeen.com",
    },
    {
        "category": "审美提升",
        "title": "Studio Aslak 打造药剂师专用 Aurum 3D 制药机：消除医疗硬件的冰冷压迫感",
        "url": "https://www.dezeen.com/2026/11/09/studio-aslak-curifylabs-pharmaprinter-aurum-empower-pharmacists/",
        "media": "https://iandaily.xyz/digest/2026-11-10-aurumprinter-f4b86fc25501.jpg",
        "source": "dezeen.com",
    },
    # 产品营销 (4)
    {
        "category": "产品营销",
        "title": "从 OpenClaw 霸榜 80+ 热搜复盘：流量潮水退去后，谁能被持续讨论？",
        "url": "https://www.woshipm.com/operate/6359632.html",
        "media": "https://image.woshipm.com/2023/09/12/c2e5f596-5116-11ee-b8bc-00163e142b65.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "中国硬件团队横扫海外社媒：创始人全英文零下 20 度硬核拆机评测出圈样本",
        "url": "https://www.woshipm.com/operate/6484706.html",
        "media": "https://image.woshipm.com/2023/04/13/1011f38c-d9ea-11ed-a8b0-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品营销",
        "title": "淘宝闪购、美团闪购、京东秒送：双 11 即时零售三强的心智争夺与履约博弈",
        "url": "https://www.woshipm.com/it/6492829.html",
        "media": "https://image.woshipm.com/2023/10/31/971ffb1a-77e9-11ee-be6e-00163e142b65.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品营销",
        "title": "Simon Willison 谈协作传播克制感：把 AI 生成的冗长 PR 说明折叠进 details 标签",
        "url": "https://simonwillison.net/2026/Nov/9/details-summary/",
        "media": "https://static.simonwillison.net/static/2026/details-summary-card.webp",
        "source": "simonwillison.net",
    },
    # AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "可灵估值飙上 180 亿美元后实测横评：现在做 AI 视频与漫剧该选哪款模型？",
        "url": "https://www.woshipm.com/evaluating/6492915.html",
        "media": "https://image.woshipm.com/2023/04/14/2ecb8e6e-da8f-11ed-aeb8-00163e0b5ff3.jpg",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "AI 屠杀传统短剧：视频消耗占走 55% 算力，一场没有讣告的产能替换",
        "url": "https://www.woshipm.com/ai/6492578.html",
        "media": "https://image.woshipm.com/2023/04/14/98e5280c-daa1-11ed-aaf8-00163e0b5ff3.png",
        "source": "woshipm.com",
    },
    {
        "category": "AI 漫剧",
        "title": "单条 163 万赞的 AI 猫咪 IP“咪的妙脆角”：爆款短剧终究赢在角色跨集一致性",
        "url": "https://www.woshipm.com/ai/6492777.html",
        "media": "https://image.woshipm.com/2023/04/13/ca8623fc-d9de-11ed-9d2f-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "AI 漫剧",
        "title": "Codex + Blender 自动化搭建可漫游 3D 世界：打通漫剧固定场景复用的工程路径",
        "url": "https://www.woshipm.com/ai/6492854.html",
        "media": "https://image.woshipm.com/wp-files/sha256/5a/07/5a076795d764cf0544764c580c93ef51688f73d6962ea2e8ecba655d8f722170.png",
        "source": "woshipm.com",
    },
    # 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "海外 AI 短剧剧本范本《领主大人：请指教》：狼族流亡女侍潜伏古堡的强强复仇拉扯",
        "url": "https://www.wzbj1616.com/script_info/2266",
        "media": "https://www.wzbj1616.com/storage/script/20261016/3fc788696fc338da185f5a7dab5f9b6a.png",
        "source": "wzbj1616.com",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "职场科技悬疑《芯片泄密那天，全公司都说是我》：4 小时日志时间差如何构筑精准反转",
        "url": "https://www.wzbj1616.com/script_info/2267",
        "media": "https://www.wzbj1616.com/storage/script/20261017/125d4afe22f8e445d18e909192c6475a.jpg",
        "source": "wzbj1616.com",
    },
    {
        "category": "编剧技巧",
        "title": "120 集末世重生短剧《重生回末世前，我囤空了全城》：倒计时囤货爽点节奏拆解",
        "url": "https://www.wzbj1616.com/script_info/2260",
        "media": "https://www.wzbj1616.com/storage/script/20261015/02b412424e40480b1054c86e0c8fdc19.png",
        "source": "wzbj1616.com",
    },
    {
        "category": "编剧技巧",
        "title": "玄学直播微短剧《我在殡仪馆夜班算命》全120集：极高反差场景与黑市暗线双驱动",
        "url": "https://www.wzbj1616.com/script_info/2259",
        "media": "https://www.wzbj1616.com/storage/script/20261015/18f07c3711a9bb4ae5736fc51b7c2267.png",
        "source": "wzbj1616.com",
    },
    # 产品经理 (4)
    {
        "category": "产品经理",
        "title": "面完上百位 AI 产品经理后：决定能否拿到 Offer 的 4 项硬核底层能力",
        "url": "https://www.woshipm.com/pmd/6282137.html",
        "media": "https://image.woshipm.com/2024/10/30/478842f4-9694-11ef-8da6-00163e142b65.png",
        "source": "woshipm.com",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "AI 产品经理三类岗位能力图谱：业务深耕、模型评测与平台工程化该如何选型",
        "url": "https://www.woshipm.com/pmd/6058206.html",
        "media": "https://image.woshipm.com/2023/08/22/2b5c181e-40df-11ee-9458-00163e0b5ff3.jpg",
        "source": "woshipm.com",
    },
    {
        "category": "产品经理",
        "title": "当传统满意度指标在 AI 产品中失灵：重新标定“预期—感知落差”度量模型",
        "url": "https://www.woshipm.com/operate/6484321.html",
        "media": "https://image.woshipm.com/2026/01/13/bc2e2836-f047-11f0-b1b9-00163e4b86a1.png",
        "source": "woshipm.com",
    },
    {
        "category": "产品经理",
        "title": "AI 产品经理必修的算法边界课：摸清大模型与多模态落地时什么能做、什么不能做",
        "url": "https://www.woshipm.com/ai/6321654.html",
        "media": "https://image.woshipm.com/2023/04/14/89a13ea6-da9e-11ed-9b82-00163e0b5ff3.png",
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
