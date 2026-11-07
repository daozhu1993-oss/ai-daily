# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Meta 将专用模型送进 Muse 与 Meta AI：垂直场景小模型高效分工协作",
        "url": "https://research.meta.ai/blog/specialized-models-for-muse-and-metaai",
        "media": "https://iandaily.xyz/digest/2026-11-07-metaspecial-3aede16eeb7d.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "OpenClaw 把模型目录与客户端发版拆开：动态协议驱动的热插拔模型接入架构",
        "url": "https://openclaw.ai/blog/use-new-models-in-openclaw-without-an-update",
        "media": "https://iandaily.xyz/digest/2026-11-07-clawcatalog-4c411f218df5.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "OpenRouter 推出 Auto Code 专属路由：针对编程场景的动态模型分流与性价比优化",
        "url": "https://openrouter.ai/blog/announcements/auto-and-auto-code-routers/",
        "media": "https://iandaily.xyz/digest/2026-11-07-router-8a98429f3722.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "pico-WAM 拆开动作提案与世界模型评分：具身智能体的解耦分层规划范式",
        "url": "https://www.keivalya.com/pico-wam/",
        "media": "https://iandaily.xyz/digest/2026-11-07-picowam-104adae88d63.jpg"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "ViewFit 按网页实际渲染尺寸动态压缩图像：前端性能优化的高效自动化智能体",
        "url": "https://github.com/andrea-bonacci/viewfit",
        "media": "https://iandaily.xyz/digest/2026-11-07-viewfit-8d43e5d91245.jpg"
    },
    {
        "category": "AI 协作",
        "title": "ldraw-mecha 让智能体推断乐高齿轮传动再做动画：机械约束下的物理级运动生成",
        "url": "https://github.com/anteloc/ldraw-mecha/tree/v0.5.0",
        "media": "https://iandaily.xyz/digest/2026-11-07-ldraw-474ce55268e0.jpg"
    },
    {
        "category": "AI 协作",
        "title": "EasyRunCraft 将十三种流行编辑器无缝接入智能体：跨 IDE 的统一代码补全与调度通道",
        "url": "https://easyruncraft.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-easyrun-e3c541fecd5a.jpg"
    },
    {
        "category": "AI 协作",
        "title": "KeepPlain 让每一行提交代码都能追溯当时的代理对话：透明化上下文追溯版本系统",
        "url": "https://keepplain.com",
        "media": "https://iandaily.xyz/digest/2026-11-07-keepplain-195ba4a8a628.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "Word Spies 让朋友与不同 AI 模型混队猜词：多模型人格与派对猜谜的独立站变现实验",
        "url": "https://wordspies.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-wordspies-9eaa864bf207.jpg"
    },
    {
        "category": "一人公司",
        "title": "Tell the Sky 让虚拟纸灯笼沿真实地球风向漂流：浪漫慢交互与情绪寄托微产品",
        "url": "https://tellthesky.com",
        "media": "https://iandaily.xyz/digest/2026-11-07-sky-28e087df6cbd.jpg"
    },
    {
        "category": "一人公司",
        "title": "Dub Digger 为小众电子乐打造专属虚拟听音室：垂直黑胶与数字厂牌的利基索引",
        "url": "https://dubdigger.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-dubdigger-217bcdbe23bd.jpg"
    },
    {
        "category": "一人公司",
        "title": "Math Paradoxes 让经典数学与概率悖论动态仿真跑一遍：极简教育科普网站的自传播",
        "url": "https://mathparadoxes.com/en/",
        "media": "https://iandaily.xyz/digest/2026-11-07-math-bbbfb4d46238.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Infinity 让单一回答长出多条对话分支：树状分支思维与多轮推演的画布交互革新",
        "url": "https://infinitychat.app/",
        "media": "https://iandaily.xyz/digest/2026-11-07-infinity-24a98a1b26fc.jpg"
    },
    {
        "category": "产品设计",
        "title": "DrawDock 把 Android 平板变成桌面电脑的原生批注层：低延迟跨设备微交互工具",
        "url": "https://github.com/MikeCer/DrawDock",
        "media": "https://iandaily.xyz/digest/2026-11-07-drawdock-0903904a51a8.jpg"
    },
    {
        "category": "产品设计",
        "title": "Rindraw 让矢量笔触在反复修改后仍保持优雅路径：设计师手绘与矢量对齐的轻量工具",
        "url": "https://rindraw.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-rindraw-4957a75f5518.jpg"
    },
    {
        "category": "产品设计",
        "title": "Checkered Chat 让二维码本身成为离线消息信使：去中心化近场通信的极客设计",
        "url": "https://honeywired.com/apps/checkered-chat/",
        "media": "https://iandaily.xyz/digest/2026-11-07-checkered-cbb4c0e5cb58.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Ondu 3D 打印褶边与棋盘格陶瓷灯具：复古拉夫领与参数化制造的奇幻重构",
        "url": "https://www.designboom.com/design/3d-printed-ruffled-collars-top-checkerboard-lamps-vases-and-candle-holders-in-ondu-wonderland-gliese-design/",
        "media": "https://iandaily.xyz/digest/2026-11-07-ondu-5a9b941fe80d.jpg"
    },
    {
        "category": "审美提升",
        "title": "Carsten Höller 在墨西哥城高楼间架起四条巨型金属滑梯：城市公共空间的体验雕塑",
        "url": "https://www.designboom.com/art/carsten-holler-people-together-four-giant-slides-mexico-city-arte-abierto-polanco-soma-sordo-madaleno-antara/",
        "media": "https://iandaily.xyz/digest/2026-11-07-slides-86f141142034.jpg"
    },
    {
        "category": "审美提升",
        "title": "Maison Margiela 用牙签蘸墨手绘东京旗舰店故事：极简漫画背后的解构主义美学",
        "url": "https://www.designboom.com/art/toothpick-drawn-manga-celebrates-maison-martin-margiela-tokyo-flagship-anniversary-takehito-moriizumi-ebisu/ ",
        "media": "https://iandaily.xyz/digest/2026-11-07-margiela-010bd4097895.jpg"
    },
    {
        "category": "审美提升",
        "title": "Demi Nguyen 将现代金融科技系统界面与古老活字档案并置：字体排印历史的当代转译",
        "url": "https://www.designboom.com/readers/demi-nguyen-corporate-branding-fintech-systems-typographic-archives/",
        "media": "https://iandaily.xyz/digest/2026-11-07-demi-cd04d3f779f1.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Per Frame 按单张快门成本精算胶卷真实花销：利基社群工具的精准心智占领",
        "url": "https://perframe.app/",
        "media": "https://iandaily.xyz/digest/2026-11-07-perframe-f4447c351a4d.jpg"
    },
    {
        "category": "产品营销",
        "title": "The Map Challenge 把网站展示接上全球地图积分打卡：游戏化自裂变外链与获客网络",
        "url": "https://themapchallenge.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-mapchallenge-04a193ef1b6e.jpg"
    },
    {
        "category": "产品营销",
        "title": "utmSnap 在外链生成前锁死渠道命名规范：数据归因治理从源头消灭混乱",
        "url": "https://utmsnap.com",
        "media": "https://iandaily.xyz/digest/2026-11-07-utmsnap-c4c6b9de8934.jpg"
    },
    {
        "category": "产品营销",
        "title": "ReachMap 把冷启动推广渠道研究变成一份分步待办：出海独立产品的 GTM 极简路线图",
        "url": "https://reachmap.app/",
        "media": "https://iandaily.xyz/digest/2026-11-07-reachmap-e445797eedbb.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "两名 00 后手搓 AI 短剧获 1.4 亿播放：高概念青春校园题材与工业化制作实录",
        "url": "https://www.woshipm.com/ai/6481139.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "《反正你也没时间活》两天播放破亿：AI 漫剧不再卷纯画质、转向人性与情绪穿透",
        "url": "https://www.woshipm.com/ai/6454826.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "从‘拍段子’到‘扛剧集’：头部博主转型短剧的工业化流水线与生产力重构",
        "url": "https://www.woshipm.com/operate/6490351.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "复杂游戏规则一键生成动态动画：Agent 驱动的 MG 动画生成与分镜自动化实操",
        "url": "https://www.woshipm.com/ai/6490339.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《寒门帝师》120 集微短剧：古装权谋、寒门学子与帝王之师的成长因果链",
        "url": "https://www.wzbj1616.com/script_info/2237",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《开局一座破道观》120 集微短剧：仙侠经营、收徒兴观与轻松反套路幽默",
        "url": "https://www.wzbj1616.com/script_info/2238",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《神医农妃惹不起》120 集微短剧：古装女频、神医医术与甜宠逆袭的爽感节拍",
        "url": "https://www.wzbj1616.com/script_info/2239",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《大宋第一皇商》120 集微短剧：古装经商、信息差商战与穿越致富的因果闭环",
        "url": "https://www.wzbj1616.com/script_info/2240",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "企业 AI 转型落不了地？一张清单说清组织侧 7 步核心路径与产品边界设计",
        "url": "https://www.woshipm.com/pd/6490135.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "打通企业应用孤岛：多办公 App 统一互联架构与工作流智能体设计",
        "url": "https://www.woshipm.com/ai/6490335.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "AI 时代产品经理人才面试逻辑重构：从功能画图转向系统边界与不确定性把控",
        "url": "https://www.woshipm.com/class/6490194.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "把多智能体连成网状协作：跨系统 Agent 协议互联与调度产品架构实践",
        "url": "https://www.woshipm.com/ai/6490031.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80"
    }
]

# Note: clean trailing spaces in urls if any
for item in candidates:
    item['url'] = item['url'].strip()

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
    print("Starting parallel verification of Nov 07 (36 items) with 12 workers...")
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
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 07 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
