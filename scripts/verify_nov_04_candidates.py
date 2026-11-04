# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "OpenAI 对照安全评测与真实部署中的行为：揭示模型“对齐伪装”差距",
        "url": "https://alignment.openai.com/eval-production-behavior-gap/",
        "media": "https://iandaily.xyz/digest/2026-11-04-evalgap-12139bd60b29.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "NVIDIA 开源 Auto-ontology：给智能体自动补齐企业数据语义层",
        "url": "https://github.com/NVIDIA/auto-ontology",
        "media": "https://iandaily.xyz/digest/2026-11-04-autoontology-87d4f057f62a.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Neurolume 让 Mac 本地大模型微调过程逐层可见：端侧训练全景监控",
        "url": "https://github.com/Yiteng-CHEN/neurolume",
        "media": "https://iandaily.xyz/digest/2026-11-04-neurolume-1c45425e73b6.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Slopgrid 让自建模型安全评测不必先写代码：交互式提示词红队基准",
        "url": "https://slopgrid.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-slopgrid-7b4bb65f5950.jpg"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "Hyperiux 把交互动效作为源码交进项目：前端智能体动效工程化组件库",
        "url": "https://vault.hyperiux.com",
        "media": "https://iandaily.xyz/digest/2026-11-04-hyperiux-c0ac12d43fa0.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Hookdeck Inspect 让智能体等待异步 Webhook 回调：长流程测试调试利器",
        "url": "https://inspect.hookdeck.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-inspect-324570adc605.jpg"
    },
    {
        "category": "AI 协作",
        "title": "TextoCAD 生成能继续改尺寸的参数化模型：自然语言驱动 CAD 工程化建模",
        "url": "https://textocad.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-textocad-4aab7467bc2c.jpg"
    },
    {
        "category": "AI 协作",
        "title": "CleanSlop 给 AI 写的网站排定修复优先级：智能体代码异味与坏味道清洗",
        "url": "https://cleanslop.com",
        "media": "https://iandaily.xyz/digest/2026-11-04-cleanslop-b6585113786b.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "Kiri 用一个守护进程管理本地容器：单机轻量化 Docker 替代方案",
        "url": "https://runkiri.com",
        "media": "https://iandaily.xyz/digest/2026-11-04-kiri-65191ff4a439.jpg"
    },
    {
        "category": "一人公司",
        "title": "ReScreen 把录屏后的精剪完全留在本机：零云端依赖的隐私剪辑工具",
        "url": "https://rescreen.studio",
        "media": "https://iandaily.xyz/digest/2026-11-04-rescreen-03af72ca6e63.jpg"
    },
    {
        "category": "一人公司",
        "title": "拉面盈利模拟器给独立创业五十二周：量化单兵生死的现金流测算盘",
        "url": "https://ramenprofitable.dev",
        "media": "https://iandaily.xyz/digest/2026-11-04-ramen-1195188ed638.jpg"
    },
    {
        "category": "一人公司",
        "title": "Tiny Tally 把小生意账本收成单文件：无数据库无后端的极简记账单兵工具",
        "url": "https://apps.tarwin.art/tiny-tally/",
        "media": "https://iandaily.xyz/digest/2026-11-04-tinytally-c03c9112656a.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Peck 把社交帖子限制为微型像素画：反信息过载的低刺激表达社区",
        "url": "https://peck.pikju.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-peck-5a1d24138f6a.jpg"
    },
    {
        "category": "产品设计",
        "title": "Bundle 让稍后阅读无缝接上复习卡片：从收藏到内化的闭环交互设计",
        "url": "https://bundle.ink/",
        "media": "https://iandaily.xyz/digest/2026-11-04-bundle-cfdf88c5013f.jpg"
    },
    {
        "category": "产品设计",
        "title": "Zuno 把 API 请求存成纯文本版本管理文件：消除 GUI 客户端臃肿的新范式",
        "url": "https://zuno.devaryan.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-zuno-bfaf32569295.jpg"
    },
    {
        "category": "产品设计",
        "title": "Vectoys 用纯 SVG 画出屏幕可点的拟物立体设备：极轻量网页拟物交互艺术",
        "url": "https://vectoys.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-vectoys-dc52285a2a0d.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "JAWF 用液压把不锈钢胀成雕塑容器：工业成形力学与反光金属的张力诗学",
        "url": "https://www.designboom.com/design/hydromechanical-forming-reflective-stainless-steel-sculptural-objects-sarah-naghawi-jawf/",
        "media": "https://iandaily.xyz/digest/2026-11-04-jawf-e42b66050920.jpg"
    },
    {
        "category": "审美提升",
        "title": "Soft-pixel 让数码相机外壳长出菌丝质感：可降解生物材料重塑数码硬件",
        "url": "https://www.designboom.com/technology/compostable-mycelium-digital-camera-soft-pixel-sree-krishna-pillarisetti/",
        "media": "https://iandaily.xyz/digest/2026-11-04-softpixel-73a7cace3a47.jpg"
    },
    {
        "category": "审美提升",
        "title": "Hoop 灯具用厚实松木托起一圈透光薄木片：北欧天然木纹的温润雕塑光影",
        "url": "https://www.dezeen.com/2026/11/03/john-tree-sculptural-hoop-lamp-pine-vaarni/",
        "media": "https://iandaily.xyz/digest/2026-11-04-hoop-6be51dc2e33a.jpg"
    },
    {
        "category": "审美提升",
        "title": "Hey 诊所用浅黄乳胶与折叠钢板取代儿童装饰：以克制极简消解就医焦虑",
        "url": "https://www.dezeen.com/2026/11/03/batek-architekten-hey-orthodontic-clinic/",
        "media": "https://iandaily.xyz/digest/2026-11-04-heyclinic-4e2b7d3ce611.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Collabrun 给红人达人合作算一张净利润账：穿透中介溢价的达人 ROI 核算盘",
        "url": "https://www.collabrun.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-collabrun-f4bed66bdeb5.jpg"
    },
    {
        "category": "产品营销",
        "title": "Kicklace 把生命周期邮件画在客户完整路径上：可视化的旅程营销触达画布",
        "url": "https://www.kicklace.com/",
        "media": "https://iandaily.xyz/digest/2026-11-04-kicklace-e16bc15f88d2.jpg"
    },
    {
        "category": "产品营销",
        "title": "Kliqo 深度检查 AI 爬虫实际能读到什么：生成式引擎可见性体检工具",
        "url": "https://kliqo.ai/tools/ai-page-audit",
        "media": "https://iandaily.xyz/digest/2026-11-04-kliqo-6e353d6d0f09.jpg"
    },
    {
        "category": "产品营销",
        "title": "Ahrefs 详尽实测七种品牌提及对 AI 可见度影响：大模型引用算法规律深度复盘",
        "url": "https://ahrefs.com/blog/mention-types-ai-visibility/",
        "media": "https://iandaily.xyz/digest/2026-11-04-ahrefsmentions-1bb5e7ab8731.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "还剩什么真人短剧在对抗AI剧？生成式漫剧工业化冲击下的制作分水岭",
        "url": "https://www.woshipm.com/ai/6488281.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "爆款土甜短剧改长后又出圈：微短剧 IP 逆向长剧化与长尾叙事变现",
        "url": "https://www.woshipm.com/it/6488266.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "AI视频生成的下一场竞争：从单纯画质炫技走向多镜头连续性与剧组管线落地",
        "url": "https://www.woshipm.com/ai/6488246.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "Character.AI破产与虚拟陪伴的终局：漫剧团队打造虚拟人设的商业与合规警示",
        "url": "https://www.woshipm.com/ai/6488225.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《侯府嫡女她不认命》120 集古装宅斗短剧：退婚逆袭与女性主体意识觉醒节拍",
        "url": "https://www.wzbj1616.com/script_info/2225",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《冷宫废后她杀疯了》120 集宫廷复仇短剧：置之死地而后生的极致情绪钟摆编排",
        "url": "https://www.wzbj1616.com/script_info/2226",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《七品县令很忙》120 集古装轻喜断案短剧：小官大智的悬疑解构与市井喜剧因果",
        "url": "https://www.wzbj1616.com/script_info/2227",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《我躺平就成仙》120 集爆笑仙侠短剧：反内卷反套路修真与意外飞升的因果爽感",
        "url": "https://www.wzbj1616.com/script_info/2228",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "Codex 深度产品分析：从写代码的独立助手走向别人产品里的嵌入式零件",
        "url": "https://www.woshipm.com/evaluating/6488608.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "从单点工具调用到 Super Agent：多智能体系统的交互设计与控制流演进",
        "url": "https://www.woshipm.com/ai/6488579.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "金融 AI 产品落地实战：银行与证券智能体的业务场景设计与合规风险治理",
        "url": "https://www.woshipm.com/ai/6488219.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "Skill 路由优化实战：基于真实业务意图请求的 description 动态自进化",
        "url": "https://www.woshipm.com/ai/6488293.html",
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
    print("Starting parallel verification of Nov 04 (36 items) with 12 workers...")
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
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 04 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
