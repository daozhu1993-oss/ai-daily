# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-15': {
        'title': '10 月 15 日 · 交互重塑与长时记忆：从基座做题家到真实业务履约',
        'highlights': '全网 9 大领域 36 篇高密度精选：Grok Voice 3.0 实时语音交互打响低价战、LangChain 推出 Deep Agents 探索长记忆文件架构、Lovable 补齐 GTM 获客工具链、从 Gemini 4 Argon 评测高分反思真实业务交付壁垒、ComfyUI IP-Adapter 锁定漫剧角色一致性。',
        'epigraph': '做题得满分容易，但在满地泥泞的真实工厂与业务系统里交付一个闭环，比在跑分榜单上拿第一难上一千倍。',
        'lead': '10 月 15 日，AI 行业的关注焦点正从“参数刷榜”进一步下沉到“长周期任务的真实交付力”。在基座模型与语音交互端，x.ai 正式推送 Grok Voice 3.0，以极具攻击性的原价策略直逼低延迟实时语音交互市场，而开源端 SPEV 模型则尝试从声学特征直接判断对话打断时机；在智能体与协作基础设施端，LangChain 深度拆解 Deep Agents 上下文工程，将多步长任务的执行记忆持久化到结构化文件中，标志着 Agent 架构正从单次会话拼装转向受控的状态机管理；在商业与产品落地一线，行业开始冷静反思“基座做题家”与“工业现场交付”之间的巨大鸿沟——从机器视觉验收时 99% 实验室指标到了量产线直接缩水为 95%，到企业端真实业务流程的极其复杂的例外处理，无一不在证明：单纯的模型能力已经平权，真正能筑起壁垒的，是对垂直业务边界的深刻敬畏与端到端履约闭环；在内容与影视工业端，ComfyUI IP-Adapter Plus 与 Video Helper Suite 构筑起多镜头角色一致性与音视频合成流水线，120 集 AI 辅助硬科幻微短剧《环宇公约》全本交付，展现了算法与人工打磨协同下的内容产能跃升。',
        'scene': '「现在的模型连最难的代码和物理题都能拿满分，客户为什么还不买单？」「因为客户要的从来不是考试状元。客户要的是系统每天早上 8 点准时吐出报表，出错时能查到责任人，网络抖动时不会把数据库删库。那些才是真实世界的考卷。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周四。

今天整理完这 36 篇一手精选，我一直在想一个词：**“做题家陷阱”**。

这几个月来，几乎每周都有新的大模型宣布在各种评测集上“超越上一代”、“屠榜多模态”。
但当你去跟一线工厂厂长、企业财务总监、或者独立开发团队聊一聊时，你会发现大家的痛点惊人一致：
模型做题很聪明，但一到真实业务系统里，只要遇到一个未见过的例外情况，它就会卡壳甚至产生幻觉；
在实验室验收时准确率能做到 99%，到了光照不稳定的真实车间，直接跌到 95% 导致整条产线停摆。

这恰恰是留给所有产品人、工程师和独立造物者最大的机会。

不要被大厂宏大的跑分发布会震慑。
大厂负责把大模型这个“做题家”培养出来，
而你的使命，是给这个做题家配上严谨的业务防错网、清晰的数据接口、长任务持久化记忆、以及能抗住物理世界冲击的履约管道。

把精力从追逐最新模型，转移到深耕业务场景的真实泥泞里。
那些巨头看不上、模型摸不着的细碎壁垒，才构成了你最坚固的商业底盘。

祝你今天产出满满。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI IP-Adapter Plus：多镜头漫剧角色一致性与面部特征高精度锁定',
                'note': '漫剧工业化不可或缺的角色锚定中枢：全面增强 IP-Adapter 在多重特征提取与分层权重融合下的表现，支持精准固定剧本主角面部特征、服饰与发色，杜绝换镜变脸。',
                'so_what': '角色一致性是连载漫剧的命门；掌握分层嵌入特征锁定技术，才能让 AI 从散乱抽卡蜕变为工业化叙事生产力。',
                'source': 'github.com',
                'url': 'https://github.com/cubiq/ComfyUI_IPAdapter_plus',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI Video Helper Suite：漫剧视听流水线视频合并与音画同步导出中枢',
                'note': '漫剧工程化交付的底层粘合剂：提供高吞吐的音视频流加载、帧序列批量合并与外部配音对齐输出，打通从扩散模型生成到可剪辑工程文件的最后一环。',
                'so_what': '单点出图容易，管线整合成难；完善的工作流节点套件能极大减少中间环节的文件反复搬运损耗。',
                'source': 'github.com',
                'url': 'https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '用 Claude Opus 5.5 做视频堪称一绝：大模型直接编排 SVG 与代码动态生成漫剧分镜',
                'note': '海外高阶视听创作流派实测复盘：绕过大显存视频扩散模型，直接利用顶尖推理模型编写交互式动画代码与动态 SVG 分镜，生成极致清晰且体积极小的动态镜头。',
                'so_what': '跳出扩散模型的算力内卷；用代码与矢量动画重构动态分镜，为极低成本漫剧出海开辟了全新的轻量化路径。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473114.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《环宇公约》硬科幻文明接触微短剧 全 120 集：AI 辅助创作与竖屏短剧工业化交付',
                'note': '商业短剧市场硬科幻题材交付实案：全 120 集每集 1 分钟竖屏剧本，经 AI 辅助构筑 77 种外星异种语言翻译冲突，并由资深编剧逐集精修，实现全本商业交割。',
                'so_what': 'AI 辅助不仅能写快餐甜宠，也能搭建宏大硬科幻世界观；关键在于让人工专注于戏剧张力与情绪支点的深度把控。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1759',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《好东西》年度现象级剧本深度拆解：轻巧对话、女性互助与反套路人物关系',
                'note': '口碑票房双丰收剧作样本复盘：打破传统叙事中的撕扯狗血与男权说教，用生活流轻盈对白、真诚生活褶皱与反刻板印象的角色互动，重构当代都市情感母题。',
                'so_what': '好故事不必剑拔弩张；捕捉真实生活中的微小尴尬与善意温情，往往比人为堆砌的阶层冲突更能引发普遍共情。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1729',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《天劫代打》修仙脑洞爽剧剧本拆解：高概念设定与逆境反转的情绪爽点设计',
                'note': '免费短剧头部赛道爆款法则剖析：将现代商业外包服务概念嫁接入传统修仙语境，前三集迅速建立“替人渡雷劫”的硬核反差，用持续的生命博弈拉满追剧黏性。',
                'so_what': '高概念是短剧穿透圈层的核武器；把现代行业痛点置换进奇幻世界观，能在第一秒抓住受众注意力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1758',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '第十一届中国戏剧奖·曹禺剧本奖申报启事：严肃戏剧文学母题与现实主义叙事价值',
                'note': '中国戏剧文学最高奖申报导向拆解：重申对时代脉搏与人民现实处境的深刻关照，鼓励创作者走出快餐速成泥潭，以严密的话剧文学台词功底雕琢传世精品。',
                'so_what': '热点会过时，文学性永存；编剧在顺应商业快节奏的同时，不能放弃对深层人性和社会肌理的严肃洞察。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/art_info/960',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '“好戏青岛”新创戏剧剧本征集启事：地域文化资源挖掘与舞台剧本结构把控',
                'note': '地方文旅与舞台艺术深度融合创作导引：如何将城市百年工业历史、滨海人文特色转化为舞台场面调度，平衡地域真实风物与普适戏剧冲突。',
                'so_what': '立足特定风土讲好中国故事；挖掘具有独特文化辨识度的地方资产，是新锐编剧切入官方资助与院团排演的捷径。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1766',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '谷歌推出了个“做题家”：Gemini 4 Argon 屠榜，但干活差点意思',
                'note': '前沿基座评测与真实工作流落差反思：在标准基准集上得分惊艳的模型，一旦接入包含上下文污染、模糊需求与系统工具链调用的真实业务，往往表现出不可控的脆弱。',
                'so_what': '跑分高不等于能干活；产品经理选型时必须以私有业务真实测试集为准绳，绝不能盲信公开排行榜。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473077.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '我所了解的机器视觉检测产品应用：验收的 99%，量产怎么就成了 95%？',
                'note': '硬核工业场景落地血泪史：从静态白盒测试环境到工厂动态振动、温差与油污现场，指标跳水背后暴露出纯算法团队对物理世界工程复杂度的致命忽视。',
                'so_what': '工业 AI 的壁垒全在产线泥泞里；只有深扎物理现场做容错补偿与标定治理，才能跨越致命的交付死亡谷。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473696.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'Muse 爆火，大厂急了：视听多模态基座引爆全网后，超级平台的防守落位与生态卡位',
                'note': '生成式多模态产业格局推演：小团队开源模型凭借极致手感与无缝工作流出圈，倒逼大厂在算力壁垒与应用商店渠道上筑起防线，生态博弈进入深水区。',
                'so_what': '技术单点惊艳只能赢一时；谁能迅速抢占专业创作者的工作流插件位，谁才能在平台封锁下建立真正护城河。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6472757.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': 'DeepSeek Harness 为什么要兼容 Claude Code Mods：开源生态在开发者工作流层面的兼容与借势',
                'note': '开源基座生态扩张心法拆解：不盲目自立协议标准，而是主动对齐已被头部产品验证并广泛普及的开发者插件生态，以极低迁移成本实现用户爆发。',
                'so_what': '兼容成熟生态是最高效的增长杠杆；尊重开发者的肌肉记忆，借力打力才能在巨头林立的赛道中极速突围。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473810.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-15.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Select curated items for the 6 ian categories
curated_ian_picks = {
    'AI 资讯': [
        'https://x.ai/news/grok-voice-3',
        'https://huggingface.co/SpragAI/SPEV',
        'https://research.google/blog/analyzing-technical-documents-with-deep-review/',
        'https://modal.com/blog/1-billion-annualized-run-rate-series-d'
    ],
    'AI 协作': [
        'https://www.langchain.com/blog/context-engineering-deep-agents-remember',
        'https://daily.dev/marketplace',
        'https://specreel.dev/',
        'https://runnersh.dev/'
    ],
    '一人公司': [
        'https://clova.email/',
        'https://code198x.com/',
        'https://www.acenow.app/',
        'https://approximatr.com/?src=y'
    ],
    '产品设计': [
        'https://rambox.app/',
        'https://www.calendar0.app',
        'https://flowwish.app/',
        'https://pericentre.com/'
    ],
    '审美提升': [
        'https://www.designboom.com/art/inflatable-pavilion-pneuhaus-dragonfly-compound-vision-221-camera-obscuras-compound-camera-no-3/',
        'https://www.wallpaper.com/architecture/tag-christof-exhibition-herman-miller-palm-springs-usa',
        'https://www.designboom.com/design/art-everywhere-yinka-ilori-chairman-community-center-london-exhibition-interview/',
        'https://www.creativeboom.com/work/how-two-simple-dots-gave-pictoplasma-a-face-after-20-years-of-neutral-design/'
    ],
    '产品营销': [
        'https://lovable.dev/blog/introducing-growth-tools',
        'https://www.pkazantsev.com/writing/promise-diff/',
        'https://confidence.spotify.com/',
        'https://launchvideos.gallery/'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://x.ai/news/grok-voice-3': '实时语音大模型进入平价走量阶段；低延迟、低成本的自然对话接口将快速重塑智能硬件与客服交互。',
    'https://huggingface.co/SpragAI/SPEV': '端到端语音交互打断判断进入开源轻量化期；让智能体学会“听话音知停顿”，是人机拟真交互的关键进化。',
    'https://research.google/blog/analyzing-technical-documents-with-deep-review/': '专业论文与工程规范审阅从纯生成转向结构化推理校验；让大模型充当严格的“同行评审”，大幅降低逻辑翻车风险。',
    'https://modal.com/blog/1-billion-annualized-run-rate-series-d': 'Serverless AI 容器算力迎风起飞；按秒计费的灵活架构让中小团队无需维护昂贵固定 GPU 集群也能承接高并发。',
    'https://www.langchain.com/blog/context-engineering-deep-agents-remember': '长周期任务智能体进入“文件驱动型记忆”阶段；将任务状态固化为可审计磁盘文件，彻底终结单会话遗忘隐患。',
    'https://daily.dev/marketplace': '开发者社区正转型为 Agent 插件分发生态；为智能体提供标准化工作流集市，正在成为新一代超级入口。',
    'https://specreel.dev/': '测试用例即最终营销演示；打通浏览器端 E2E 测试与动态录屏，将产品版本迭代的宣发物料产出成本降为零。',
    'https://runnersh.dev/': '桌面命令行与智能体接管界面的有机融合；让开发者随时随地感知后台 Agent 的执行心跳，保障自主可控。',
    'https://clova.email/': '单人公司必备的基础信任资产；为每一个合作方与项目自动生成隔离域名邮箱，从底层斩断信息泄露与垃圾骚扰。',
    'https://code198x.com/': '向资源受限的经典架构致敬；在显存算力泛滥的时代，掌握极致克制的内存与位图逻辑是构建轻量软件的心法。',
    'https://www.acenow.app/': '知识内化比单纯收藏重要一万倍；让每一次刷题练习都穿透回原始笔记上下文，构筑真正属于个人的认知闭环。',
    'https://approximatr.com/?src=y': '用极简的微交互唤醒对比例尺度的直觉；把硬核几何感知包装为无压力的每日五道题，是小而美产品的典范。',
    'https://rambox.app/': '多业务账号与场景隔离的终极利器；给一人公司的数十个 SaaS 客户端套上沙箱，彻底根治切换混乱与信息过载。',
    'https://www.calendar0.app': '三周连续滚动视图打破传统月历割裂感；让排期与待办在平滑的时间轴上自然流动，重塑时间管理心流。',
    'https://flowwish.app/': '打通日常开销流水与长期资产复利；在订阅制无孔不入的时代，看清每一笔微小支出的真实资金成本。',
    'https://pericentre.com/': '宇宙尺度的连续无缝交互范式；将庞大的空间天体数据以极简手感呈现，展现了现代 Web 图形渲染的工业之美。',
    'https://www.designboom.com/art/inflatable-pavilion-pneuhaus-dragonfly-compound-vision-221-camera-obscuras-compound-camera-no-3/': '用 221 枚物理针孔复现蜻蜓复眼视角；在数字屏幕过载的当下，以纯粹的光学原理唤醒人类对自然视界的情感敬畏。',
    'https://www.wallpaper.com/architecture/tag-christof-exhibition-herman-miller-palm-springs-usa': '中世纪现代主义在沙漠炽阳下的当代凝视；几何线条与干燥空气的化学反应，记录了永不褪色的设计纯粹度。',
    'https://www.designboom.com/design/art-everywhere-yinka-ilori-chairman-community-center-london-exhibition-interview/': '给废旧家具赋予色彩与社区记忆；打破冷冰冰的商业陈列，用欢快的民俗图腾将公共空间转化为温暖的对话场域。',
    'https://www.creativeboom.com/work/how-two-simple-dots-gave-pictoplasma-a-face-after-20-years-of-neutral-design/': '极简设计的克制重塑；仅凭两颗恰到好处的圆点，就在保持了 20 年理性的中性字标中注入了充满灵性的生命力。',
    'https://lovable.dev/blog/introducing-growth-tools': 'AI 编程产品正式打通全链路商业交付；从仅仅生成页面代码，进化到自带 SEO、分析与获客工具链，闭环才值钱。',
    'https://www.pkazantsev.com/writing/promise-diff/': '软件交付的信任审计利器；在正式发布前机械比对官网文案承诺与安装包实际功能的差异，从源头消灭虚假宣传。',
    'https://confidence.spotify.com/': '工业级 A/B 实验平台全面开放；摆脱单纯看指标涨跌的盲目归因，用严苛的因果推断框架护航产品重大决策。',
    'https://launchvideos.gallery/': '高质量产品发布视频的灵感弹药库；解构爆款 Demo 的镜头节奏与价值呈现，是独立开发者冷启动的绝佳教材。'
}

day_items = []

# 1. 6 ian categories × 4 items
target_6_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
for c in target_6_categories:
    picked_urls = curated_ian_picks[c]
    for idx, u in enumerate(picked_urls):
        raw_it = raw_by_url[u]
        used_set.add(u)
        day_items.append({
            'category': c,
            'title': raw_it['title'],
            'note': raw_it['judgment'],
            'so_what': so_what_overrides.get(u, '从微小变化中洞察范式转移，把外部技术演进收拢为自身确定性的产品复利。'),
            'source': raw_it['source'],
            'url': u,
            'media': raw_it['media'] or 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
            'pinned': (idx < 2)
        })

# 2. 3 vertical categories × 4 items
v_info = vertical_data['2026-10-15']
for drama in v_info['ai_drama']:
    used_set.add(drama['url'])
    day_items.append(drama)
for sp in v_info['screenplay']:
    used_set.add(sp['url'])
    day_items.append(sp)
for pm in v_info['pm']:
    used_set.add(pm['url'])
    day_items.append(pm)

if len(day_items) != 36:
    raise ValueError(f'Items count is {len(day_items)}, expected 36!')

cat_order = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 漫剧', '编剧技巧', '产品经理']
sorted_items = []
for co in cat_order:
    sorted_items.extend([it for it in day_items if it['category'] == co])

md_content = f"""---
date: '2026-10-15'
title: {json.dumps(v_info['title'], ensure_ascii=False)}
highlights: {json.dumps(v_info['highlights'], ensure_ascii=False)}
draft: false
epigraph: {json.dumps(v_info['epigraph'], ensure_ascii=False)}
lead: {json.dumps(v_info['lead'], ensure_ascii=False)}
scene: {json.dumps(v_info['scene'], ensure_ascii=False)}
cover: {v_info['cover']}
items:
"""
for it in sorted_items:
    clean_title = json.dumps(it['title'].replace('\n', ' ').strip(), ensure_ascii=False)
    clean_note = json.dumps(it['note'].replace('\n', ' ').strip(), ensure_ascii=False)
    clean_so_what = json.dumps(it['so_what'].replace('\n', ' ').strip(), ensure_ascii=False)
    clean_source = json.dumps(it['source'].strip(), ensure_ascii=False)
    clean_url = json.dumps(it['url'].strip(), ensure_ascii=False)
    clean_media = json.dumps(it['media'].strip(), ensure_ascii=False)
    pinned_val = 'true' if it.get('pinned', False) else 'false'
    md_content += f"""  - category: {json.dumps(it['category'], ensure_ascii=False)}
    title: {clean_title}
    note: {clean_note}
    so_what: {clean_so_what}
    source: {clean_source}
    url: {clean_url}
    media: {clean_media}
    pinned: {pinned_val}
"""
md_content += f"""---

## 今日主理人寄语

{v_info['closing']}
"""

out_file = 'src/content/daily/2026-10-15.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-15! Total URLs in history: {len(all_used_list)}')
