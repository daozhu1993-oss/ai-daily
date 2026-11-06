# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "ERNIE 5.5 Flash Base 开放预训练权重：端云协作高吞吐轻量推理新基座",
        "url": "https://ernie.baidu.com/release/ernie-5-5-flash-base/",
        "media": "https://iandaily.xyz/digest/2026-11-06-ernie-ce8c726afc6c.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Cursor 把内部应用从本地带到可分享网址：原型即交付的云端沙箱",
        "url": "https://cursor.com/changelog/build-live-apps",
        "media": "https://iandaily.xyz/digest/2026-11-06-cursor-a285c56a230c.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "OpenClaw Multiplayer 让多人共用代理现场：多开发者实时协同调试智能体",
        "url": "https://openclaw.ai/blog/shattering-silos-with-openclaw-multiplayer",
        "media": "https://iandaily.xyz/digest/2026-11-06-openclaw-7ba0e04a77ef.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Gemini Omni 1.2 Flash 延长原生视频生成：长程多模态连贯视听新突破",
        "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
        "media": "https://iandaily.xyz/digest/2026-11-06-gemini-6b7a905d9c11.jpg"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "EtherPK 把看板任务交给编程代理：卡片拖拽直连 Claude Code 自动化实施",
        "url": "https://blog.etherpk.com/hand-your-markdown-tasks-to-claude-code-from-a-kanban-board",
        "media": "https://iandaily.xyz/digest/2026-11-06-etherpk-f6c86d1fa0ad.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Lantern Lattice 让代理沿调用关系找代码：基于 AST 拓扑的有向图代码搜索",
        "url": "https://github.com/julymetodiev/lantern-lattice",
        "media": "https://iandaily.xyz/digest/2026-11-06-lantern-50c2fb53f684.jpg"
    },
    {
        "category": "AI 协作",
        "title": "thinker 把上下文账单拆给你看：精准追踪长程智能体每个 Prompt 的 Token 损耗",
        "url": "https://thinker.sh/how-it-works",
        "media": "https://iandaily.xyz/digest/2026-11-06-thinker-b2c3425a1a61.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Tokenome 让一行代码连回生成时的对话：智能体代码资产的可溯源版本化",
        "url": "https://tokenome.ai/",
        "media": "https://iandaily.xyz/digest/2026-11-06-tokenome-8b9207b4ab00.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "CalmCanary 先守住检测与提醒两件事：克制而高可用的一人服务监控小站",
        "url": "https://www.calmcanary.co/",
        "media": "https://iandaily.xyz/digest/2026-11-06-calmcanary-a7cc0225ff07.jpg"
    },
    {
        "category": "一人公司",
        "title": "这只虚拟鱼缸也得先养好硝化菌：极简黑白像素风网页生态模拟小游戏",
        "url": "https://fishtankatlas.com/play/aquarium/",
        "media": "https://iandaily.xyz/digest/2026-11-06-fishtank-96e7538d6068.jpg"
    },
    {
        "category": "一人公司",
        "title": "Droplis 把单次点击做成每日谜题：高留存的极简数字重力解谜独立站",
        "url": "https://droplis.lalo.li/",
        "media": "https://iandaily.xyz/digest/2026-11-06-droplis-e6b3dcbbe459.jpg"
    },
    {
        "category": "一人公司",
        "title": "Spaceguesser 把猜地点搬进太阳系：行星地理知识与游戏化结合的变现样本",
        "url": "https://spaceguesser.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-spaceguesser-d598bc0e8b15.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Detail Keeper 听一次就记住名字拼法与偏好：商务社交中的高保真细节管家",
        "url": "https://detailkeeper.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-detailkeeper-99d9957cf97d.jpg"
    },
    {
        "category": "产品设计",
        "title": "Climbing Guide 把动作串联做成可暂停的交互动图：空间体育的轻量可视化解析",
        "url": "https://scott1743.github.io/climbing-guide/",
        "media": "https://iandaily.xyz/digest/2026-11-06-climbing-1ff652dc3a0b.jpg"
    },
    {
        "category": "产品设计",
        "title": "aless 让不同数据文件共用一棵树：统一跨格式异构目录的极简文件浏览新范式",
        "url": "https://aless.tabnas.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-06-aless-4e5470090e43.jpg"
    },
    {
        "category": "产品设计",
        "title": "qodesign 把动效组件做成单文件纯净交付：告别臃肿第三方依赖的微前端组件库",
        "url": "https://teodoravadani.github.io/qodesign-free/",
        "media": "https://iandaily.xyz/digest/2026-11-06-qodesign-a15e7acd6640.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Gustaf Westman 把迪士尼米奇轮廓做成厚实雕塑家具：波普解构与童趣实体化",
        "url": "https://www.designboom.com/design/gustaf-westman-disney-mickey-mouse-chunky-colorful-furniture/",
        "media": "https://iandaily.xyz/digest/2026-11-06-westman-335e81e59d69.jpg"
    },
    {
        "category": "审美提升",
        "title": "Angelo Renna 提议让三十九棵树围出佛罗伦萨河畔浮岛：城市水域的生态漂浮森林",
        "url": "https://www.designboom.com/architecture/angelo-renna-floating-modular-island-39-tree-ring-florence-river-firenze-little-island/",
        "media": "https://iandaily.xyz/digest/2026-11-06-renna-315cc2c996b5.jpg"
    },
    {
        "category": "审美提升",
        "title": "PP-2 无唱臂光学黑胶唱机：整块阳极氧化铝与悬浮红外读取的极简仪式",
        "url": "https://www.designboom.com/technology/pp-2-turntable-reads-vinyls-without-tonearm-glass-listening-room-tokyo-waiting-for-ideas/",
        "media": "https://iandaily.xyz/digest/2026-11-06-pp2-29538c42d07d.jpg"
    },
    {
        "category": "审美提升",
        "title": "Linehouse 把杭州老工业丝绸厂区痕迹带进当代酒店：砖石锈迹与织物肌理的交融",
        "url": "https://www.dezeen.com/2026/11/05/linehouse-jen-hotel-hangzhou/",
        "media": "https://iandaily.xyz/digest/2026-11-06-linehouse-79e8ff3c782d.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "aireel 从产品落地页直接组织一支高转化宣传短片：将静态文案自动编排为动态叙事",
        "url": "https://aireel.tv/",
        "media": "https://iandaily.xyz/digest/2026-11-06-aireel-993cd87c0b09.jpg"
    },
    {
        "category": "产品营销",
        "title": "PitchFlip 把创业起点画成翻页故事：告别冰冷 PPT 的情绪化互动获客新载体",
        "url": "https://pitchflip.shiptiffin.app",
        "media": "https://iandaily.xyz/digest/2026-11-06-pitchflip-9904ad865da8.jpg"
    },
    {
        "category": "产品营销",
        "title": "PinSharing 把地图历史留存权写进分层定价：微型工具商业闭环与增值钩子设计",
        "url": "https://pinsharing.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-pinsharing-7cbdf192b1d1.jpg"
    },
    {
        "category": "产品营销",
        "title": "Trademark Screen 出海产品命名合规初筛：把高频法律避坑做成低摩擦引流利器",
        "url": "https://trademarkscreen.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-trademarkscreen-dd79237f8953.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "农学女博士穿越宋末崖门海战：AI 短剧工业化制作实录与历史漫剧叙事探索",
        "url": "https://www.woshipm.com/ai/6490063.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "腾讯微视靠短剧换种活法：大厂短剧生态转型与精品分账变阵策略",
        "url": "https://www.woshipm.com/share/6489983.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "红果短剧接入豆包大模型：免费短剧巨头的生成式 AI 视听重组与智能互动试验",
        "url": "https://www.woshipm.com/ai/6489655.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "ChatGPT 上线 Images 2.6 动图生成：漫剧关键帧与多视角动态视效进化",
        "url": "https://www.woshipm.com/ai/6489533.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《仙门第一关系户》120 集微短剧：仙侠轻松、废柴逆袭与人缘流因果冲突",
        "url": "https://www.wzbj1616.com/script_info/2233",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《农门灵泉小富婆》120 集微短剧：古装种田、空间金手指与女频经商致富律动",
        "url": "https://www.wzbj1616.com/script_info/2234",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《天工大明》120 集微短剧：古装工匠、硬核技术造物与工部智斗逆袭",
        "url": "https://www.wzbj1616.com/script_info/2235",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《寄生星图》120 集微短剧：硬科幻太空远航、未知星云与幽闭博弈悬疑",
        "url": "https://www.wzbj1616.com/script_info/2236",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "AI 产品经理转型指南：六大细分方向、核心能力模型与进阶图谱",
        "url": "https://www.woshipm.com/pmd/6490019.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "Claude Duet 主动运行后：企业 Agent 必须写入 Runtime 的四大安全边界",
        "url": "https://www.woshipm.com/ai/6490040.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "Agent 记忆系统设计实战：一张表、一个索引与三套分层淘汰策略",
        "url": "https://www.woshipm.com/ai/6489307.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "政务 AI 产品落地攻坚：业务场景设计、权限隔离与责任溯源机制",
        "url": "https://www.woshipm.com/pd/6489168.html",
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
    print("Starting parallel verification of Nov 06 (36 items) with 12 workers...")
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
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 06 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
