# -*- coding: utf-8 -*-
import subprocess
import concurrent.futures
import json

candidates = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "HyperFlow H3 Flash 把同步音画压到极少步生成：端侧音视频一体化扩散新突破",
        "url": "https://github.com/Video-Rebirth/hyperflow-h3-flash",
        "media": "https://iandaily.xyz/digest/2026-11-08-hyperflow-eb072ad07d46.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Cinnamon 把家庭共享与个人隐私上下文严格隔离：多角色家庭智能体系统",
        "url": "https://getcinnamon.ai/",
        "media": "https://iandaily.xyz/digest/2026-11-08-cinnamon-d0c4eb99cdea.jpg"
    },
    {
        "category": "AI 资讯",
        "title": "Jacq 从可读模型描述直接编译出高吞吐 CUDA 推理代码：消除框架抽象开销",
        "url": "https://github.com/ImpossibleComputing/jacq",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 资讯",
        "title": "Laplace’s Scissors 在保护既有高频知识下定向手术式修改模型参数：模型剪枝与遗忘控制",
        "url": "https://github.com/Miyamoto-Renya/LaplacesScissors",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "KeyContain 按请求内容细粒度动态分配代理 API 权限：零信任智能体网关",
        "url": "https://keycontain.com",
        "media": "https://iandaily.xyz/digest/2026-11-08-keycontain-6b9ce8064221.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Good First Token 把闲置算力额度导流给开源待办：智能体众包协同新范式",
        "url": "https://goodfirsttoken.org/",
        "media": "https://iandaily.xyz/digest/2026-11-08-goodtoken-3ebeedae517c.jpg"
    },
    {
        "category": "AI 协作",
        "title": "Vondet 让多轮长程对话持续在同一张敏捷计划板上演进：动态结构化任务画布",
        "url": "https://vondet.com/en?ref=hn",
        "media": "https://iandaily.xyz/digest/2026-11-08-vondet-83fa70d54f33.jpg"
    },
    {
        "category": "AI 协作",
        "title": "offstage 给智能体一台随时可运行 Xcode 与移动端构建的云端 Mac：端侧研发 Agent 基础设施",
        "url": "https://offstage.cloud/",
        "media": "https://iandaily.xyz/digest/2026-11-08-offstage-a8739c9ed740.jpg"
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "Atlas Streak 让你亲手把国家拼回世界地图：极简地理轮廓拼图小游戏",
        "url": "https://crux.quest/atlas/",
        "media": "https://iandaily.xyz/digest/2026-11-08-atlasstreak-5f4a164025a1.jpg"
    },
    {
        "category": "一人公司",
        "title": "Quiz Toolkit 把手机秒变现场互动抢答器：无 App 免下载的轻量聚会神器",
        "url": "https://quiztoolkit.com/",
        "media": "https://iandaily.xyz/digest/2026-11-08-quiztoolkit-3200fc20d242.jpg"
    },
    {
        "category": "一人公司",
        "title": "Spiral Nest 把蚁群觅食轨迹化为物理粒子螺旋气泡室：生成式数学艺术实验",
        "url": "https://johnveds15-spiral-nest.static.hf.space/index.html",
        "media": "https://iandaily.xyz/digest/2026-11-08-spiralnest-7e7b7862e318.jpg"
    },
    {
        "category": "一人公司",
        "title": "Kantamigo 让全屋人的歌词跟着领唱者麦克风精准滚动：极简聚会 K 歌伴侣",
        "url": "https://kantamigo.com",
        "media": "https://iandaily.xyz/digest/2026-11-08-kantamigo-d8996756818d.jpg"
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Spot 把电脑操作流程逐步摊在眼前：可视化步骤指引与低心智交互记录",
        "url": "https://spot.deemwar.com",
        "media": "https://iandaily.xyz/digest/2026-11-08-spot-afaa29199cc6.jpg"
    },
    {
        "category": "产品设计",
        "title": "MacGet 在服务器限流后自动渐进回退并发连接：克制优雅的原生下载器",
        "url": "https://macget.suryansh.work/",
        "media": "https://iandaily.xyz/digest/2026-11-08-macget-90eff18c0f31.jpg"
    },
    {
        "category": "产品设计",
        "title": "Twombly 把代理的多屏幕界面探索摆上同一张无限画布：多 Agent 可视化推演台",
        "url": "https://twombly.app/",
        "media": "https://iandaily.xyz/digest/2026-11-08-twombly-29fd432d790f.jpg"
    },
    {
        "category": "产品设计",
        "title": "Solous 让未来的自己回复今天的日记：跨越时空的内省对话心理工具",
        "url": "https://solous.net/",
        "media": "https://iandaily.xyz/digest/2026-11-08-solous-2229336fa644.jpg"
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Julia Lohmann 用天然海带薄皮围合出先锋异形骨架：生物材质雕塑的未来美学",
        "url": "https://www.designboom.com/design/julia-lohmann-otherworldly-kelp-sculptures-future-beyond-human/",
        "media": "https://iandaily.xyz/digest/2026-11-08-kelp-b567aaa802db.jpg"
    },
    {
        "category": "审美提升",
        "title": "Atelier GABU 用木质网格与半透薄布回应法国山坡石塔：轻盈消解厚重历史的构筑物",
        "url": "https://www.designboom.com/architecture/atelier-gabu-observation-tower-french-hillside-timber-translucent-fabric-brunebasse/",
        "media": "https://iandaily.xyz/digest/2026-11-08-brunebasse-eb00e96cfa9a.jpg"
    },
    {
        "category": "审美提升",
        "title": "Studio Ruei 让香港工业区咖啡空间围着经典汽车展陈展开：清水混凝土与拉丝金属的秩序",
        "url": "https://www.designboom.com/architecture/concrete-brushed-metal-hybrid-automotive-gallery-cafe-hong-kong-macchina-studio-ruei/",
        "media": "https://iandaily.xyz/digest/2026-11-08-macchina-94c8eb667240.jpg"
    },
    {
        "category": "审美提升",
        "title": "SABO Project 用圆角木隔墙打通曼哈顿微型公寓：极简空间柔性划分新范本",
        "url": "https://www.dezeen.com/2026/11/07/sabo-project-soft-divisions-apartment-renovation-lower-east-side/",
        "media": "https://iandaily.xyz/digest/2026-11-08-sabo-f9b368b76e91.jpg"
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "LaunchZone 把多平台目录代投变成可追踪订单：独立出海产品的冷启动代办管家",
        "url": "https://submit.launchzone.co",
        "media": "https://iandaily.xyz/digest/2026-11-08-launchzone-475c6e0791da.jpg"
    },
    {
        "category": "产品营销",
        "title": "MailDignity 在冷邮件发出前自动挑出冒犯感与说教味：高转化销售拓客的情绪质检员",
        "url": "https://maildignity.com/",
        "media": "https://iandaily.xyz/digest/2026-11-08-maildignity-85221539c8b0.jpg"
    },
    {
        "category": "产品营销",
        "title": "journalistic.tech 将媒体采访问题交给受访者异步回答：低摩擦数字 PR 传播网络",
        "url": "https://journalistic.tech/",
        "media": "https://iandaily.xyz/digest/2026-11-08-journalistic-07c1204ae0a2.jpg"
    },
    {
        "category": "产品营销",
        "title": "TRACE 将各大抓取接口的反爬延迟与成功率做成每周公开评测：以客观基准撬动开发者信任",
        "url": "https://trace.context.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-08-trace-7266a346366c.jpg"
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "GPT Image 2.6 动图生成与多场景分镜实操：连续动作流转与动态表情关键帧提效",
        "url": "https://www.woshipm.com/ai/6490532.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "端侧声音克隆与配音工作流：零成本批量生成漫剧多角色音色资产",
        "url": "https://www.woshipm.com/ai/6490530.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "多模态自我递归提升与资产自生成：从手工调提示词走向自动化漫剧制片探索",
        "url": "https://www.woshipm.com/ai/6490475.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "AI 漫剧",
        "title": "办公协作智能体与多模态创作管线融合：大厂生态战下创作者工具链的解耦变局",
        "url": "https://www.woshipm.com/ai/6455160.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《归途》微短剧 全本：都市现实、公路温情与底层小人物的救赎因果",
        "url": "https://www.wzbj1616.com/script_info/2241",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《忏悔录》微短剧 全本：都市悬疑、旧罪揭晓与人性道德底线的心理博弈",
        "url": "https://www.wzbj1616.com/script_info/2242",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《最后的审判》微短剧 全本：都市医疗急诊室、生死决择与人性伦理张力",
        "url": "https://www.wzbj1616.com/script_info/2243",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "编剧技巧",
        "title": "《欲望之渊》微短剧 全本：都市现实阶层跃迁、权欲陷阱与命运因果反噬",
        "url": "https://www.wzbj1616.com/script_info/2244",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80"
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "智能体‘做梦’机制产品架构：让长程 Agent 在空闲期反思沉淀记忆索引",
        "url": "https://www.woshipm.com/ai/6490415.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "智能体测试缰绳（Harness）架构实践：严密约束 Agent 行为边界与交付质量",
        "url": "https://www.woshipm.com/ai/6490470.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "开源大模型企业商业化下半场：从算力独占到巨头分成模式的产品定价思考",
        "url": "https://www.woshipm.com/it/6490454.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80"
    },
    {
        "category": "产品经理",
        "title": "从单兵 Agent 走向组织级协同：企业多智能体网状协作系统产品演进推演",
        "url": "https://www.woshipm.com/ai/6490314.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80"
    }
]

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
    print("Starting parallel verification of Nov 08 (36 items) with 12 workers...")
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
        print("\nALL 36 ITEMS AND 36 MEDIA URLS FOR NOV 08 RETURNED HTTP 200 OK!")
    else:
        print(f"\n{len(failed)} items failed verification:")
        for it, uc, mc in failed:
            print(f"FAILED: {it['category']} -> URL:{uc} MEDIA:{mc} | {it['url']} | {it['media']}")

if __name__ == '__main__':
    main()
