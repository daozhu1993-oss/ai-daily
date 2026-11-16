# -*- coding: utf-8 -*-
import os
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(_ROOT)
import subprocess
import json
import concurrent.futures
import time
import threading

IAN = "https://iandaily.xyz/digest/2026-11-15-"

candidates = [
    # AI 资讯
    {"category": "AI 资讯",
     "title": "格局打开：DeepSeek 正式开放全家桶 API，人人都能复刻 DeepSeek App",
     "url": "https://www.woshipm.com/ai/6493974.html",
     "media": "https://image.woshipm.com/2025/02/16/2f0f4a96-ec76-11ef-8495-00163e09d72f.png",
     "source": "woshipm.com", "pinned": True},
    {"category": "AI 资讯",
     "title": "MiniMax H3-Image 实测：开源、10 秒出 4K、超长文本的四类新玩法全拆解",
     "url": "https://www.woshipm.com/ai/6493967.html",
     "media": "https://image.woshipm.com/2023/04/17/77683736-dcf5-11ed-897e-00163e0b5ff3.png",
     "source": "woshipm.com"},
    {"category": "AI 资讯",
     "title": "「史上最严」湿实验预测基准发布：推理拉满、算力翻 5 倍也白搭",
     "url": "https://www.woshipm.com/ai/6493998.html",
     "media": "https://image.woshipm.com/2023/04/17/381527c4-dcf5-11ed-9781-00163e0b5ff3.png",
     "source": "woshipm.com"},
    {"category": "AI 资讯",
     "title": "Browser Whisper：把语音识别整条流水线搬进浏览器，模型下载后 WebGPU 本地转写",
     "url": "https://whisper.tanpreet.xyz/demo/",
     "media": IAN + "browser-whisper-d6de77a36024.webp?v=2026-11-15",
     "source": "whisper.tanpreet.xyz"},

    # AI 协作
    {"category": "AI 协作",
     "title": "Shotoku：在 Agent 执行路径上装预算闸门，每次工具调用都要留下收据",
     "url": "https://www.shotoku.dev/",
     "media": "https://shotoku.dev/assets/brand/shotoku-open-graph.png",
     "source": "shotoku.dev", "pinned": True},
    {"category": "AI 协作",
     "title": "Coppice：为每个 Agent 任务隔离独立工作树，先批计划再分派 CLI 执行",
     "url": "https://github.com/fertile-org/coppice",
     "media": "https://opengraph.githubassets.com/3bac27e2aa5cf843fd19f5a815f7d86916394532fb47b0649dffe5d61149027d/fertile-org/coppice",
     "source": "github.com"},
    {"category": "AI 协作",
     "title": "Cyberviber：一块 ESP32 桌面小屏，按紧急程度告诉你哪个 Claude 会话在等谁",
     "url": "https://cyberviber.de/",
     "media": IAN + "cyberviber-3397155c2eed.webp?v=2026-11-15",
     "source": "cyberviber.de"},
    {"category": "AI 协作",
     "title": "时间估算器：给编码任务报出 P10/P50/P90 概率区间，再用真实耗时反校",
     "url": "https://github.com/noambrand/ai-time-estimator",
     "media": IAN + "time-estimator-a32fe0fd0e13.webp?v=2026-11-15",
     "source": "github.com"},

    # 一人公司
    {"category": "一人公司",
     "title": "「卖 idea」卖出 400 万：国内两人团队的另类创业路径复盘",
     "url": "https://www.woshipm.com/share/6493912.html",
     "media": "https://image.woshipm.com/wp-files/sha256/d6/9d/d69d83357a6d52014004f13397fc25e85fc458e942385d865cb6ad251fc2c601.png",
     "source": "woshipm.com", "pinned": True},
    {"category": "一人公司",
     "title": "离开 Meta 后她做了一条会读情绪的 AI 项链，拿下 3300 万美元融资",
     "url": "https://www.woshipm.com/chuangye/6493062.html",
     "media": "https://image.woshipm.com/wp-files/sha256/86/b7/86b7527014dd6a723efec6b1b9c55a429da1aa5f47a46651d4a5e542a7e15492.jpg",
     "source": "woshipm.com"},
    {"category": "一人公司",
     "title": "Stripe AI 首席营收官：前 100 家 AI 公司收入涨近 200%，一半来自海外",
     "url": "https://www.woshipm.com/chuangye/6493970.html",
     "media": "https://image.woshipm.com/wp-files/sha256/11/ec/11eca9527bcb5ba39db9c18bb19991ff8514972a6f2df3d048df5659ee5d8125.jpg",
     "source": "woshipm.com"},
    {"category": "一人公司",
     "title": "Mopup：专治开发环境空间泄漏，把构建缓存、Agent 工作树与残留服务一次扫清",
     "url": "https://mopup.online/developers",
     "media": IAN + "mopup-282cc0fa24cd.webp?v=2026-11-15",
     "source": "mopup.online"},

    # 产品设计
    {"category": "产品设计",
     "title": "Lampka：让 PDF 暗色阅读只变暗文字、不动图片原色，长文档体验重做一遍",
     "url": "https://lampka.app/",
     "media": IAN + "lampka-e9b688307d7c.webp?v=2026-11-15",
     "source": "lampka.app", "pinned": True},
    {"category": "产品设计",
     "title": "Xdoc：浏览器里预览并导出 PPTX，整条渲染链留在本机不用装 Office",
     "url": "https://structurify.io/en/playground/",
     "media": "https://structurify.io/_astro/xdoc-runtime-social.B6sNECVw.png",
     "source": "structurify.io"},
    {"category": "产品设计",
     "title": "Wipe：把 LaMa 推理迁到自定义 WebGPU 实现，照片消除彻底留在浏览器内",
     "url": "https://wipe.photos/",
     "media": "https://wipe.photos/og-image.png",
     "source": "wipe.photos"},
    {"category": "产品设计",
     "title": "做智能硬件绕不开的 4 个真问题，与 4 条系统性的应对原则",
     "url": "https://www.woshipm.com/pd/6493466.html",
     "media": "https://image.woshipm.com/2023/08/23/872c240e-4184-11ee-9458-00163e0b5ff3.jpg",
     "source": "woshipm.com"},

    # 审美提升
    {"category": "审美提升",
     "title": "Daichi 森林桑拿：让树干穿过平台，玻璃房把人「化」进森林里",
     "url": "https://www.dezeen.com/2026/11/14/daichi-inc-silent-river-tree-sauna/",
     "media": "https://static-2026.dezeen.com/uploads/2026/11/daichi-silent-river-tree-sauna-daichi-architecture-sauna-japan-public-leisure_dezeen_2364_hero.jpg",
     "source": "dezeen.com", "pinned": True},
    {"category": "审美提升",
     "title": "Arudeko 把染色废羊毛织进透光纸材 Bianni：能弯成灯罩，也保留织物纹理",
     "url": "https://www.dezeen.com/2026/11/14/arudeko-bianni-waste-wool-paper-material/",
     "media": "https://static-2026.dezeen.com/uploads/2026/11/Bianni-Wool-Paper-by-Arudeko_dezeen_2364_col_10.jpg",
     "source": "dezeen.com"},
    {"category": "审美提升",
     "title": "C733 用干砌石墙划出 Jaguar 公园边界：石缝留给动物通行，游客设施收进已扰动区域",
     "url": "https://www.dezeen.com/2026/11/14/parque-del-jaguar-colectivo-c733-tulum-mexico-ecological-park/",
     "media": "https://static-2026.dezeen.com/uploads/2026/11/parque-del-jaguar-colectivo-c733-tulum-mexico-ecological-park-sq_dezeen_2364_col_0.jpg",
     "source": "dezeen.com"},
    {"category": "审美提升",
     "title": "Rune Bosse 把活树接上人工肺：透明膜随呼吸机鼓起收缩的生态崩溃预演",
     "url": "https://www.designboom.com/art/rune-bosse-living-lung-trees-life-support-ecological-collapse/",
     "media": "https://www.designboom.com/twitterimages/uploads/2026/11/rune-bosse-lung-trees-designboom-FB.jpg",
     "source": "designboom.com"},

    # 产品营销
    {"category": "产品营销",
     "title": "a16z 最新消费洞察：AI 真正的付费机会，藏在流量之外",
     "url": "https://www.woshipm.com/ai/6474232.html",
     "media": "https://image.woshipm.com/wp-files/sha256/df/56/df562d02a7c2d7dca0340260ea38ed1fe7e2a1409a937322558a74c4f14e5b96.png",
     "source": "woshipm.com", "pinned": True},
    {"category": "产品营销",
     "title": "Pricemend 把 595 家门店的退货与保价政策留下原句：没读过的条目明确标注待核",
     "url": "https://pricemend.com/retailers",
     "media": "https://pricemend.com/og-api.png",
     "source": "pricemend.com"},
    {"category": "产品营销",
     "title": "小红书爆款卖货观察 Vol.01：想出爆款，先想清楚这三件事",
     "url": "https://www.woshipm.com/share/6493903.html",
     "media": "https://image.woshipm.com/2023/04/13/240c5364-d9ef-11ed-9d7a-00163e0b5ff3.jpg",
     "source": "woshipm.com"},
    {"category": "产品营销",
     "title": "重新定义「承诺」：不卖牛排，卖烧烤牛排时的滋滋声",
     "url": "https://www.woshipm.com/share/6477142.html",
     "media": "https://image.woshipm.com/2023/04/17/1b28055a-dcf5-11ed-ab4d-00163e0b5ff3.png",
     "source": "woshipm.com"},

    # AI 漫剧
    {"category": "AI 漫剧",
     "title": "充了 1300 块实测即梦短剧工作室：钱花在哪、哪里还卡手",
     "url": "https://www.woshipm.com/ai/6493844.html",
     "media": "https://image.woshipm.com/2023/04/13/56b2f584-d9ef-11ed-889f-00163e0b5ff3.jpg",
     "source": "woshipm.com", "pinned": True},
    {"category": "AI 漫剧",
     "title": "劝爸妈别刷 AI 短剧，我太难了：一个内容分级与家庭沟通的真实难题",
     "url": "https://www.woshipm.com/ai/6493976.html",
     "media": "https://image.woshipm.com/wp-files/sha256/df/30/df3063345604e52b0c63e6f7e64ef9ba8882e29d203cfe97a7bf786ffd1bb205.jpg",
     "source": "woshipm.com"},
    {"category": "AI 漫剧",
     "title": "凌晨 3 点上班的 AI 漫剧公司：被算力价格逼出来的「错峰生产」",
     "url": "https://www.woshipm.com/ai/6367455.html",
     "media": "https://image.woshipm.com/2024/10/31/5301697a-972b-11ef-8da6-00163e142b65.jpg",
     "source": "woshipm.com"},
    {"category": "AI 漫剧",
     "title": "猫猫互扇耳光的 AI 短剧凭什么全球疯传：无对白内容的跨语言传播密码",
     "url": "https://www.woshipm.com/operate/6373912.html",
     "media": "https://image.woshipm.com/2026/04/09/d0811fa6-33bc-11f1-8d6c-00163e09d72f.png",
     "source": "woshipm.com"},

    # 编剧技巧
    {"category": "编剧技巧",
     "title": "《黑客帝国》中文剧本：世界观前置、信息释放节奏与「红蓝药丸」决策场景拆解",
     "url": "https://www.wzbj1616.com/script_info/2299",
     "media": "https://www.wzbj1616.com/storage/script/20261027/070ab6165eb445f89107b57fb1998002.png",
     "source": "wzbj1616.com", "pinned": True},
    {"category": "编剧技巧",
     "title": "《僵尸肖恩》中文版：把类型恐怖与英式日常幽默焊在一起的节奏配方",
     "url": "https://www.wzbj1616.com/script_info/2284",
     "media": "https://www.wzbj1616.com/storage/script/20261023/a724d094f77a8bdaae461c57915cd4c5.png",
     "source": "wzbj1616.com"},
    {"category": "编剧技巧",
     "title": "院线电影《智能木马》：犯罪悬疑外壳下切社会现实议题的剧作结构",
     "url": "https://www.wzbj1616.com/script_info/1670",
     "media": "https://www.wzbj1616.com/storage/script/20260131/61179c7cb85fe7f1346f58e2f61ada59.png",
     "source": "wzbj1616.com"},
    {"category": "编剧技巧",
     "title": "男频玄幻短剧《元婴落地，我不许你们跪着活》：开局受辱、越阶翻盘的爽点节拍表",
     "url": "https://www.wzbj1616.com/script_info/2324",
     "media": "https://www.wzbj1616.com/storage/script/20261103/e7869f8bb5af005d92fa528ddd09015d.png",
     "source": "wzbj1616.com"},

    # 产品经理
    {"category": "产品经理",
     "title": "AI 大厂集体转向：大模型迎来「杰文斯时刻」，便宜不等于用量下降",
     "url": "https://www.woshipm.com/ai/6429828.html",
     "media": "https://image.woshipm.com/2023/09/22/f7ee4342-5927-11ee-b1ec-00163e142b65.jpg",
     "source": "woshipm.com", "pinned": True},
    {"category": "产品经理",
     "title": "Agent 运作像开厨房：从点单到出菜，把不确定的智能体流程讲成可管理的工序",
     "url": "https://www.woshipm.com/ai/6489955.html",
     "media": "https://image.woshipm.com/2023/04/13/71644936-d9eb-11ed-a8b0-00163e0b5ff3.jpg",
     "source": "woshipm.com"},
    {"category": "产品经理",
     "title": "成为高阶产品经理：必懂的产品生命周期与阶段决策清单",
     "url": "https://www.woshipm.com/pmd/6190033.html",
     "media": "https://image.woshipm.com/2023/04/14/91d37828-da9e-11ed-95a1-00163e0b5ff3.png",
     "source": "woshipm.com"},
    {"category": "产品经理",
     "title": "未来设计的「双核大脑」：设计思维的感性与计算思维的理性如何协同",
     "url": "https://www.woshipm.com/share/6339734.html",
     "media": "https://image.woshipm.com/2024/06/20/f2ad3852-2ee7-11ef-90af-00163e142b65.png",
     "source": "woshipm.com"},
]

woshipm_lock = threading.Lock()


def check_url(target):
    if "woshipm.com" in target:
        with woshipm_lock:
            time.sleep(0.4)
            cmd = ["curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}",
                   "--max-time", "12", "--noproxy", "*",
                   "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36", target]
            try:
                return target, subprocess.run(cmd, capture_output=True, text=True, timeout=15).stdout.strip()
            except Exception as e:
                return target, f"ERR:{e}"
    cmd = ["curl", "-s", "-L", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", "12",
           "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"]
    if "wzbj1616.com" in target:
        cmd += ["--noproxy", "*"]
    cmd.append(target)
    try:
        return target, subprocess.run(cmd, capture_output=True, text=True, timeout=15).stdout.strip()
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
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
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
