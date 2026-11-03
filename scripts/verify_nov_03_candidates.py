# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "权重编程实验让大模型直接改小模型参数：神经网络权重空间可微编辑",
        "url": "https://rikiyat.github.io/blog/weight-space-programming/",
        "media": "https://iandaily.xyz/digest/2026-11-03-weightspace-15d0f144ae9f.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "tinywmcraft 把小型世界模型放到手机上玩：端侧神经游戏引擎",
        "url": "https://maharishiva.github.io/tinywmcraft/",
        "media": "https://iandaily.xyz/digest/2026-11-03-tinywm-1d3952b69294.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "LiteMoE 把大模型推理拆到一千六百行：极简 Mixture of Experts 交互可视化",
        "url": "https://zhulinsen.github.io/LiteMoE/visualizer/?lang=zh",
        "media": "https://iandaily.xyz/digest/2026-11-03-litemoe-b29e44ae5899.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "OpenAI 用内部激活监测模型正在做什么：表征工程对齐监控前沿",
        "url": "https://alignment.openai.com/training-activation-classifiers/",
        "media": "https://iandaily.xyz/digest/2026-11-03-probes-a6c6b3b1e3c7.jpg"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "Deedglass 比对代理说法和数据库实变：智能体执行真实因果对账",
        "url": "https://deedglass.com/play",
        "media": "https://iandaily.xyz/digest/2026-11-03-deedglass-825d5a75bc05.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Intent-lens 在执行前翻译代理的工具调用：人类可读的意图透镜插件",
        "url": "https://github.com/Dhananjay-JSR/claude-mods/tree/main/plugins/intent-lens",
        "media": "https://iandaily.xyz/digest/2026-11-03-intent-c2e0418ae3f9.jpg"
    },
    {
        "category": "AI 协作",
        "title": "ArchDocs 把设计计划和已做改动并排看：智能体架构设计与代码一致性看板",
        "url": "https://archdocs.io",
        "media": "https://iandaily.xyz/digest/2026-11-03-archdocs-e9e83adce14c.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Smalt 让双手敲代码时也能指挥代理：语音与键盘并行结对协作",
        "url": "https://getsmalt.com/",
        "media": "https://iandaily.xyz/digest/2026-11-03-smalt-1dab00f7b305.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "八美元咖啡把线上感谢送进信箱：开源维护者实体明信片赞助平台",
        "url": "https://maintainers.coffee/",
        "media": "https://iandaily.xyz/digest/2026-11-03-coffee-092d29abc508.jpg"
    },
    {
        "category": "一人公司",
        "title": "Devpush 让自己的服务器接上推送部署：极轻量单机 Git 钩子自动化",
        "url": "https://devpu.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-03-devpush-1c07a073555f.jpg"
    },
    {
        "category": "一人公司",
        "title": "Gridmino 用免费日题带出小额年订阅：几何拼图微型 SaaS 变现样本",
        "url": "https://gridmino.com/",
        "media": "https://iandaily.xyz/digest/2026-11-03-gridmino-36b1a95f75ea.jpg"
    },
    {
        "category": "一人公司",
        "title": "CampPowerCalc 把露营用电算到每件设备：垂直利基用电测算工具站",
        "url": "https://camppowercalc.com/en/calculator/battery-runtime/",
        "media": "https://iandaily.xyz/digest/2026-11-03-camppower-d8ca64ead1c1.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Affinity 把绘图、修图和排版搬上 iPad：无订阅买断制桌面级移动套件",
        "url": "https://www.affinity.studio/ipad-app",
        "media": "https://iandaily.xyz/digest/2026-11-03-affinity-57efab71b002.jpg"
    },
    {
        "category": "产品设计",
        "title": "Cross Lyrics 让 iPad 跟着电脑唱：跨设备伴侣屏幕的纯粹微交互",
        "url": "https://crosslyrics.com/",
        "media": "https://iandaily.xyz/digest/2026-11-03-crosslyrics-cb9e67cbc2b8.jpg"
    },
    {
        "category": "产品设计",
        "title": "Sizewise 把不同品牌的尺码缝成标签：消除网购服装尺码混乱的极简设计",
        "url": "https://sizewise.franzonlabs.se",
        "media": "https://iandaily.xyz/digest/2026-11-03-sizewise-01513c107b21.jpg"
    },
    {
        "category": "产品设计",
        "title": "Meeple Scan 拍一层桌游就能查评分：移动端即拍即识的桌游选品助手",
        "url": "https://meeple-scan.com/?ref=hn",
        "media": "https://iandaily.xyz/digest/2026-11-03-meeple-15b94f85c4f9.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "废弃旧皮椅拆解为九件日常器物：解构主义与材料循环的手工诗学",
        "url": "https://www.designboom.com/design/discarded-leather-armchair-nine-functional-domestic-objects-jan-micha-gamer/",
        "media": "https://iandaily.xyz/digest/2026-11-03-armchair-cb8f2e328540.jpg"
    },
    {
        "category": "审美提升",
        "title": "Neri Oxman 让细菌在蚕丝上慢慢生长出颜色：生物色素与活体织物的先锋实验",
        "url": "https://www.dezeen.com/2026/11/02/neri-oxman-vigils-fabric-silk-pigment/",
        "media": "https://iandaily.xyz/digest/2026-11-03-vigils-1ada14619c65.jpg"
    },
    {
        "category": "审美提升",
        "title": "Corkinho 用整块软木围出冥想静室：原生态多孔材料雕琢的感官庇护所",
        "url": "https://www.dezeen.com/2026/11/02/still-room-casa-no-tempo-corkinho/",
        "media": "https://iandaily.xyz/digest/2026-11-03-stillroom-9cc805629e7f.jpg"
    },
    {
        "category": "审美提升",
        "title": "瑞士邮政新定制字体：在严谨现代主义网格中注入温暖人性的字形细节",
        "url": "https://www.creativeboom.com/work/swiss-typefaces-crafts-a-warmer-friendlier-custom-font-for-swiss-post/",
        "media": "https://iandaily.xyz/digest/2026-11-03-swisspost-a84041dff56e.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "AtelierLab 把图纸交付和收款接成一步：垂直独立设计工作室的闭环交付 SaaS",
        "url": "https://www.atelierlab.in",
        "media": "https://iandaily.xyz/digest/2026-11-03-atelier-7eefa2985277.jpg"
    },
    {
        "category": "产品营销",
        "title": "Trustmebro 把社区真实评价拆回具体讨论上下文：反虚假水军的社交证据罗盘",
        "url": "https://www.trustmebro.reviews/r/hackernews",
        "media": "https://iandaily.xyz/digest/2026-11-03-trustmebro-5dc0c447107b.jpg"
    },
    {
        "category": "产品营销",
        "title": "Shortener.dev 把链接追踪放进浏览器侧边栏：单兵出海敏捷投放利器",
        "url": "https://shortener.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-03-shortener-1247f2855210.jpg"
    },
    {
        "category": "产品营销",
        "title": "HackerBlogs 从分享历史反查高质量读者常看谁：极客社群自然增长发现引擎",
        "url": "https://hackerblogs.app",
        "media": "https://iandaily.xyz/digest/2026-11-03-hackerblogs-be9d6c8d22a8.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "千亿市场之后短剧生意开始变了：从狂野买量收割走向精品内容与私域生态",
        "url": "https://www.woshipm.com/it/6487982.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "大厂抢夺大众时间背后谁在买单：竖屏漫剧注意力经济的商业真相与暗流",
        "url": "https://www.woshipm.com/it/6487971.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "打开红果短剧看懂大众生活：下沉市场情感代偿与爆款漫剧的叙事底层逻辑",
        "url": "https://www.woshipm.com/ai/6487957.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "“不塌房”只是AI明星的谎言：虚拟演员人设信任与漫剧制作团队的合规防线",
        "url": "https://www.woshipm.com/ai/6487901.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《归墟坐标》120 集硬科幻微短剧：黑洞视界边缘的时空悬疑与因果闭环构建",
        "url": "https://www.wzbj1616.com/script_info/2221",
        "media": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《镜界殖民》120 集硬科幻微短剧：平行宇宙资源倾轧与双重身份对抗节拍",
        "url": "https://www.wzbj1616.com/script_info/2222",
        "media": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《孤独星球》120 集都市情感微短剧：都市孤岛心理投射与治愈叙事弧线编排",
        "url": "https://www.wzbj1616.com/script_info/2223",
        "media": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《地府快递员》120 集灵异喜剧微短剧：现代职场痛点与荒诞阴阳因果反转技巧",
        "url": "https://www.wzbj1616.com/script_info/2224",
        "media": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "Muse 深度产品拆解：把 Agent 做成一台全权限云电脑后的系统级架构取舍",
        "url": "https://www.woshipm.com/evaluating/6487122.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "企业级 Agent 赛道分水岭已至：从通用 Bot 玩具走向深度业务工作台的残酷淘汰",
        "url": "https://www.woshipm.com/ai/6487641.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "让 Super-agent 真正成为团队同事：LobeHub 组织协同实验与权限边界设计",
        "url": "https://www.woshipm.com/ai/6487620.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "企业私有化 Agent 平台选型指南：开源部署陷阱、安全沙箱与运维成本全景复盘",
        "url": "https://www.woshipm.com/ai/6488040.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80"
    }
]

def check_url(target_url):
    args = ['curl', '-s', '-L', '-o', '/dev/null', '-w', '%{http_code}', '--connect-timeout', '10', '--max-time', '20']
    if 'wzbj1616.com' in target_url:
        args.extend(['--noproxy', '*'])
    args.append(target_url)
    try:
        res = subprocess.run(args, capture_output=True, text=True, timeout=25)
        return res.stdout.strip()
    except Exception as e:
        return f"ERR:{e}"

def verify_item(idx, item):
    u_code = check_url(item['url'])
    m_code = check_url(item['media'])
    ok = (u_code == '200') and (m_code == '200')
    status_str = "OK" if ok else "FAIL"
    print(f"[{idx+1}/36] {status_str} | {item['category']} | URL:{u_code} | MEDIA:{m_code} | {item['url']}")
    return ok, item, u_code, m_code

def main():
    print("Starting parallel verification of Nov 03 (36 items) with 12 workers...")
    all_ok = True
    failed = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
        futures = {executor.submit(verify_item, i, item): i for i, item in enumerate(candidates)}
        for f in concurrent.futures.as_completed(futures):
            ok, item, u_code, m_code = f.result()
            if not ok:
                all_ok = False
                failed.append((item, u_code, m_code))

    if all_ok:
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 03 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
