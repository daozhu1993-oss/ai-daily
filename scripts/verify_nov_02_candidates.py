# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Memdoor 公开小模型协作解题记录：轻量智能体集群决策实录",
        "url": "https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve",
        "media": "https://iandaily.xyz/digest/2026-11-02-memdoor-f6592e79c88f.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "RE-USE 降噪演示在浏览器本地运行：纯端侧音频智能修复",
        "url": "https://re-use-demo.geronimo-labs.com",
        "media": "https://iandaily.xyz/digest/2026-11-02-reuse-eae1576a30df.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Mwmbl 开放搜索索引完整快照：去中心化去算法霸权的公共网络索引",
        "url": "https://mwmbl.org/dumps",
        "media": "https://iandaily.xyz/digest/2026-11-02-mwmbl-3e2cfe75a036.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Hushkey 实验用无声口型输入文字：视觉言语识别前沿探索",
        "url": "https://github.com/amirrsyed/hushkey",
        "media": "https://images.unsplash.com/photo-1589254065878-42c9da997008?w=800&auto=format&fit=crop&q=80"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "Bowerbird 给回答中的引语逐条验出处：严苛证据溯源代理",
        "url": "https://github.com/jolovicdev/bowerbird",
        "media": "https://iandaily.xyz/digest/2026-11-02-bowerbird-4e7f5854ac19.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Sweet-search 让代理先查索引再读代码：降低 Context 膨胀的检索增强",
        "url": "https://github.com/mrsladoje/sweet-search",
        "media": "https://iandaily.xyz/digest/2026-11-02-sweet-5bce6b0cd5a4.jpg"
    },
    {
        "category": "AI 协作",
        "title": "SpecGuardian 用状态规格检查 AI 实现：以形式化规约约束代码生成",
        "url": "https://github.com/mrasu/spec-guardian",
        "media": "https://iandaily.xyz/digest/2026-11-02-spec-6a09bcf3026d.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Castov 把本地小工具接进 CLI 与 MCP：统一模型交互协议",
        "url": "https://castov.com",
        "media": "https://iandaily.xyz/digest/2026-11-02-castov-b1b38866a1d4.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "Folio 清理重复照片前先解释保留原因：有温度的本地隐私相册清理",
        "url": "https://caddora.ie/folio",
        "media": "https://iandaily.xyz/digest/2026-11-02-folio-94b34ae92c1a.jpg"
    },
    {
        "category": "一人公司",
        "title": "Shroom 把录屏费用交回自己的云账号：自带 S3 存储的单兵录屏 SaaS",
        "url": "https://shroom.am",
        "media": "https://iandaily.xyz/digest/2026-11-02-shroom-59c64c97ff6d.jpg"
    },
    {
        "category": "一人公司",
        "title": "PixelShrink 在浏览器本地压缩图片：纯客户端 Canvas 批量无损压缩",
        "url": "https://compress-image.uk/",
        "media": "https://iandaily.xyz/digest/2026-11-02-pixel-8ae7f22844fc.jpg"
    },
    {
        "category": "一人公司",
        "title": "TariffPedia 从商品编码查起进口成本：跨境出海关税与合规垂直查询字典",
        "url": "https://tariffpedia.com/",
        "media": "https://iandaily.xyz/digest/2026-11-02-tariff-4ef881541af2.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Type It Big 把屏幕变成大字手牌：即开即用零多余步骤的纯粹表达",
        "url": "https://typeitbig.com/",
        "media": "https://iandaily.xyz/digest/2026-11-02-typeitbig-212a337e437c.jpg"
    },
    {
        "category": "产品设计",
        "title": "Crosswalk 给每个终端留一行任务备注：解决并发窗口认知负荷的设计",
        "url": "https://wareshq.com/crosswalk",
        "media": "https://iandaily.xyz/digest/2026-11-02-crosswalk-3ba2516defe8.jpg"
    },
    {
        "category": "产品设计",
        "title": "LanesMac 让窗口沿横向长桌展开：突破传统全屏与虚拟桌面的横向物理手感",
        "url": "https://lanesmac.com",
        "media": "https://iandaily.xyz/digest/2026-11-02-lanes-07dc46914291.jpg"
    },
    {
        "category": "产品设计",
        "title": "Bobby 按依赖关系安排代码审阅：拓扑时序驱动的代码审查微体验",
        "url": "https://bobby.viraj.computer/",
        "media": "https://iandaily.xyz/digest/2026-11-02-bobby-b8102f35b647.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "澳门水边茶渣板竹塔：非遗脚手架搭接与再生农业茶渣材料的诗意融合",
        "url": "https://www.designboom.com/architecture/traditional-bamboo-scaffolding-tea-waste-panels-impromptu-projects-pagoda-macau/",
        "media": "https://iandaily.xyz/digest/2026-11-02-bamboo-416911e2e1be.jpg"
    },
    {
        "category": "审美提升",
        "title": "Buoy 把废旧船绳打印成摇摆凳：海洋渔具废弃物与机械臂 3D 打印的律动雕塑",
        "url": "https://www.dezeen.com/2026/11/01/buoy-stools-the-new-raw/",
        "media": "https://iandaily.xyz/digest/2026-11-02-buoy-1151dee535ab.jpg"
    },
    {
        "category": "审美提升",
        "title": "伊斯坦布尔 Rami 图书馆彩色模块游园亭：现代模数游乐构件激活古建庭院",
        "url": "https://www.designboom.com/architecture/chromatic-pavilions-modular-play-structures-historic-istanbul-rami-library-milimetrik-architects/",
        "media": "https://iandaily.xyz/digest/2026-11-02-rami-c9cde8aef6d1.jpg"
    },
    {
        "category": "审美提升",
        "title": "Supremath 用几何规则生成至上主义构成画：数学算法与马列维奇艺术的当代回响",
        "url": "https://supremath.art/",
        "media": "https://iandaily.xyz/digest/2026-11-02-supremath-0d7760225ddf.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Winch 让智能体自主接管商店 SEO：中小商户自动化转化率优化",
        "url": "https://getwinch.app/",
        "media": "https://iandaily.xyz/digest/2026-11-02-winch-5ae3b64de0c0.jpg"
    },
    {
        "category": "产品营销",
        "title": "Overhear 把舆情监测改为按需扫描：拒绝高昂月租的单兵轻量声誉雷达",
        "url": "https://overhear.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-02-overhear-572a0f5d0c1e.jpg"
    },
    {
        "category": "产品营销",
        "title": "Citeon 监控品牌在 AI 回答里的引用占有率：生成式引擎时代的内容护城河",
        "url": "https://citeon.dev",
        "media": "https://iandaily.xyz/digest/2026-11-02-citeon-91f66afa2896.jpg"
    },
    {
        "category": "产品营销",
        "title": "SiteOne 把整站 SEO 体检交成可读报告：全栈式单机开源爬虫诊断利器",
        "url": "https://crawler.siteone.io/",
        "media": "https://iandaily.xyz/digest/2026-11-02-siteone-edaa65bc9bf4.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "即梦短剧工作室实操测评：双十一每秒低至0.16元背后的视听工业化降本",
        "url": "https://www.woshipm.com/ai/6487529.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "短剧火爆出圈呼唤独立评价体系：从低质下沉到精品化评分的生态进阶",
        "url": "https://www.woshipm.com/it/6487413.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "“字节时间”到底是不是“垃圾时间”？微短剧连续刷屏背后的大众心理透视",
        "url": "https://www.woshipm.com/it/6487537.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "声音直播与虚拟偶像的情绪经济学：微短剧团队跨界音频赛道变现洞察",
        "url": "https://www.woshipm.com/it/6486483.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《冰封方舟》120 集末日微短剧：极致生存困境与人性救赎弧线设计",
        "url": "https://www.wzbj1616.com/script_info/2217",
        "media": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《湮灭舰队》120 集太空科幻微短剧：舰队战绝境推进与悬疑危机层层加码",
        "url": "https://www.wzbj1616.com/script_info/2218",
        "media": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《天劫代打》120 集仙侠微短剧：荒诞脑洞与渡劫反差爽感的戏剧张力编排",
        "url": "https://www.wzbj1616.com/script_info/2219",
        "media": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《环宇公约》120 集硬科幻微短剧：文明初接触博弈与规则博弈的高潮构建",
        "url": "https://www.wzbj1616.com/script_info/2220",
        "media": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "AI 办公智能体赛道深度拆解：从「能生成」到「能交付、可治理、可复用」",
        "url": "https://www.woshipm.com/evaluating/6486874.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "设计师与产品经理的协作快照：状态流转、用户对象与闭环反馈设计",
        "url": "https://www.woshipm.com/ai/6487586.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "兼具 Agent、多模态与具身经验的复合架构师：下一代产品经理的能力全景",
        "url": "https://www.woshipm.com/ai/6487591.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "硅谷前沿与下一代 Agent 落地实践：产品化架构演进与商业闭环深度复盘",
        "url": "https://www.woshipm.com/ai/6487545.html",
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
    print("Starting parallel verification of Nov 02 (36 items) with 12 workers...")
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
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 02 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
