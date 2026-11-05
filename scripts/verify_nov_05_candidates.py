# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Ripple 65B 开放权重与原生思维链：小算力集群的高性价比推理探索",
        "url": "https://www.ricursive.com/ripple",
        "media": "https://iandaily.xyz/digest/2026-11-05-ripple-b591e5b67fee.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Kimi K3.1 Pro 开放多模态模型权重：长上下文推理再升级",
        "url": "https://huggingface.co/moonshotai/Kimi-K3.1-Pro",
        "media": "https://iandaily.xyz/digest/2026-11-05-kimi-9f8b1677ba57.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Claude Code 优化后台任务状态流：降低长时间编程代理的通信损耗",
        "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.316",
        "media": "https://iandaily.xyz/digest/2026-11-05-claudecode-105ea9f203b2.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Phonon 浏览器端语音合成：逐词时间戳与零后端极低延迟播报",
        "url": "https://blixt.xyz/phonon/",
        "media": "https://iandaily.xyz/digest/2026-11-05-phonon-8c38648f3577.jpg"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "QAmcp 为 MCP 服务器提供集成测试与监控：智能体工具链稳健性保障",
        "url": "https://qamcp.dev/?from=hackernews",
        "media": "https://iandaily.xyz/digest/2026-11-05-qamcp-c20805d53e5d.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Atlas 给智能体一张独立的 macOS 虚拟桌面：后台运行不抢占鼠标键盘",
        "url": "https://atlas.insanearts.io/",
        "media": "https://iandaily.xyz/digest/2026-11-05-atlas-1708007e9dfc.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Fount 本地优先的 AI 驱动文档工作台：私密数据零泄漏的表格与笔记融合",
        "url": "https://www.fount.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-05-fount-e3fbd11f2925.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Screenplay 智能体自动编排录制产品演示：从脚本文案到视频交付",
        "url": "https://github.com/gmpetrov/agent-screenplay",
        "media": "https://iandaily.xyz/digest/2026-11-05-screenplay-7d8595f2bb0f.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "PC Deal Check 拆解整机真实配件价值：反向推导硬件折扣与防坑利器",
        "url": "https://pcdealcheck.com/",
        "media": "https://iandaily.xyz/digest/2026-11-05-pcdeal-841a0fa664c4.jpg"
    },
    {
        "category": "一人公司",
        "title": "Meshword 填字游戏与网格逻辑解谜合成：极简网页独立小游戏变现实验",
        "url": "https://meshword.org/",
        "media": "https://iandaily.xyz/digest/2026-11-05-meshword-252ff13037c1.jpg"
    },
    {
        "category": "一人公司",
        "title": "Pinery 将 WordPress 导出为高性能静态站点：独立开发者的极简托管方案",
        "url": "https://www.pinery.pro/en/",
        "media": "https://iandaily.xyz/digest/2026-11-05-pinery-23dc0d4b5754.jpg"
    },
    {
        "category": "一人公司",
        "title": "Spooler 超轻量级单文件消息队列：单兵云服务异步任务处理新基石",
        "url": "https://spooler.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-05-spooler-e612264e6dd8.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "OnCue 物理级倒计时任务看板：将日程安排具象化为沉浸式时间视觉流",
        "url": "https://www.oncueboard.com/",
        "media": "https://iandaily.xyz/digest/2026-11-05-oncue-c7dd5cd57418.jpg"
    },
    {
        "category": "产品设计",
        "title": "Ratio 文档内嵌动态数学与数据计算：消除文本与电子表格边界的交互革新",
        "url": "https://useratio.app/",
        "media": "https://iandaily.xyz/digest/2026-11-05-ratio-f52eebadb52d.jpg"
    },
    {
        "category": "产品设计",
        "title": "Mdview 原生轻量 Windows Markdown 查看器：毫秒级响应的纯粹阅读窗口",
        "url": "https://mdview.io/desktop",
        "media": "https://iandaily.xyz/digest/2026-11-05-mdview-a7aeaee63adf.jpg"
    },
    {
        "category": "产品设计",
        "title": "Md2Docx 将 Markdown 精确排版导出为 Word 文档：开发者告别格式对齐折磨",
        "url": "https://md2docx.js.org/",
        "media": "https://iandaily.xyz/digest/2026-11-05-md2docx-da44a5edca86.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Jakob Kudsk Steensen 地下水库深海光影装置：生命起源与多感官空间叙事",
        "url": "https://www.designboom.com/art/this-installation-by-jakob-kudsk-steensen-considers-the-origins-and-agency-of-life/",
        "media": "https://iandaily.xyz/digest/2026-11-05-jakob-9498e548cbf7.jpg"
    },
    {
        "category": "审美提升",
        "title": "Atelier Manferdini 像素陶瓷与折叠铝板艺术变电站：工业基础设施的公共美学重塑",
        "url": "https://www.designboom.com/architecture/pixelated-ceramic-tiles-folded-aluminum-electrical-substation-facade-virginia-atelier-manferdini-invisible/",
        "media": "https://iandaily.xyz/digest/2026-11-05-manferdini-1808b6091e26.jpg"
    },
    {
        "category": "审美提升",
        "title": "Abel Macias 巴黎古宅内的高饱和簇绒色彩装置：手工纺织与古典建筑的历史对话",
        "url": "https://www.dezeen.com/2026/11/04/scad-installation-design-miami-paris/",
        "media": "https://iandaily.xyz/digest/2026-11-05-scad-d35cbfbc28c0.jpg"
    },
    {
        "category": "审美提升",
        "title": "Jeju 岛原木柱承托的极简诗意餐厅空间：三根传统木构与海风光影的通透融合",
        "url": "https://www.dezeen.com/2026/11/04/jeju-restaurant-daughters/",
        "media": "https://iandaily.xyz/digest/2026-11-05-jeju-195a14e1d03d.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Cloudflare 针对 AI 个人代理的流量可视化与管控：新流量生态的站长防御盾",
        "url": "https://blog.cloudflare.com/personal-agents-visibility-control/",
        "media": "https://iandaily.xyz/digest/2026-11-05-cloudflare-1efc6b169107.jpg"
    },
    {
        "category": "产品营销",
        "title": "25posts 通过 LinkedIn 曝光猜谜反推内容获客逻辑：游戏化增长与算法探秘",
        "url": "https://25posts.com/play",
        "media": "https://iandaily.xyz/digest/2026-11-05-25posts-d5eedbeae84a.jpg"
    },
    {
        "category": "产品营销",
        "title": "Slashtrends 追踪 Reddit 细分社区受众热点：出海独立产品的社群冷启动罗盘",
        "url": "https://slashtrends.com/",
        "media": "https://iandaily.xyz/digest/2026-11-05-slashtrends-57a7d59f76b2.jpg"
    },
    {
        "category": "产品营销",
        "title": "RotateAd 独立开发者横幅与导航栏赞助互换：零预算流量互助联盟网络",
        "url": "https://rotate.ad/",
        "media": "https://iandaily.xyz/digest/2026-11-05-rotatead-8e68914f260f.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "跨模型生态协同：漫剧多模态视听管线的分工重组与平台壁垒打破",
        "url": "https://www.woshipm.com/ai/6488773.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "AI 眼镜与随身第一人称视角拍摄：沉浸漫剧新机位与具身叙事探索",
        "url": "https://www.woshipm.com/ai/6488630.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "大厂 AI 团队重组：视听创意工作室工业化制片流程与生产力重构",
        "url": "https://www.woshipm.com/ai/6488383.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "实测 DeepSeek“创造模式”：零门槛插件驱动漫剧分镜与动态特效生成",
        "url": "https://www.woshipm.com/ai/6488371.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《妖兽食堂》120 集微短剧：玄幻美食、治愈经营与反差反转的轻喜剧叙事",
        "url": "https://www.wzbj1616.com/script_info/2229",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《女将北征》120 集微短剧：古装女将从军与热血逆袭因果链构建",
        "url": "https://www.wzbj1616.com/script_info/2230",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《不死药》120 集微短剧：都市悬疑、长生执念与人性博弈的戏剧张力",
        "url": "https://www.wzbj1616.com/script_info/2231",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《乌合之众》120 集微短剧：都市现实、网络舆论风暴与反转真相的批判叙事",
        "url": "https://www.wzbj1616.com/script_info/2232",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "开源 3 年沉淀与数百个实战项目：AI 产品经理全景知识库与实操模型",
        "url": "https://www.woshipm.com/ai/6488632.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "给 AI 造上班前的仿真环境：智能体沙箱测试与产品形态演进推演",
        "url": "https://www.woshipm.com/chuangye/6488756.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "企业私有化 Agent 架构方案与落地推演：从研发增效到企业流程重构",
        "url": "https://www.woshipm.com/ai/6488290.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "Personal Agent 的交互重塑：从 Voice 语音切入的伴随式助理新范式",
        "url": "https://www.woshipm.com/ai/6488363.html",
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
    print("Starting parallel verification of Nov 05 (36 items) with 12 workers...")
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
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 05 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
