# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-21': {
        'title': '10 月 21 日 · 持久记忆与闭环履约：当智能体开始摆脱“瞬时失忆症”',
        'highlights': '全网 9 大领域 36 篇高密度精选：Mistral 推出 Voxtral 3 实时多模态语音 SDK、DeepSeek 开源 DeepInfer 推理框架、Composio Instant 为 Agent 赋予预付钱包、AI 电商落地真实痛点复盘、100 层微观人体生存电梯短剧全本商业交割。',
        'epigraph': '优秀的智能体不该在每一次新对话中退化为新生儿；把经历沉淀为结构化记忆，才是通往复杂现实履约的唯一桥梁。',
        'lead': '10 月 21 日，大模型应用开发正式迎来了从“单次问答”向“持久记忆与闭环履约”的深刻质变。如果说过去一年的智能体生态还在围绕提示词工程与简单检索做表面修补，那么今天一线工程师与产品团队则正在系统性打通现实生产的硬核链路：在端侧与语音多模态层，Mistral 重磅推出 Voxtral 3 实时语音流水线，直接将听说理解与工具调用端到端咬合，把交互延迟压缩进百毫秒量级；在推理与算力基础设施端，DeepSeek 开源的 DeepInfer 推理框架与 PyTorch 官方推出的 TorchTPU 原生后端，正在让异构硬件与国产算力真正具备无缝承接生产级流量的工程底盘；在智能体金融与闭环交付端，Composio Instant 创新性地为 Agent 赋予受控的“预付钱包”，使智能体第一次能够自主完成云资源充值、API 采买等现实世界履约动作；而在短剧与视听创作领域，从 ComfyUI 批量制片管线到 100 层微观人体生存漫剧的成熟交割，AI 视听工业化正在从概念验证全面蜕变为高频商业变现引擎。',
        'scene': '「为什么 Agent 在第一步帮我查完了机票，第二步问它要不要下单时，它却忘了我上一句说的出发日期？」「因为传统的无状态调用让模型患上了“瞬时失忆症”。真正的商业级智能体不能只靠临时的上下文拼接，它必须拥有自主调用的结构化账本与外部钱包，像真人助手一样对每一笔承诺负起全生命周期的责任。」',
        'cover': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周三。

今天整理这 36 篇精选时，最让我触动的，是 **智能体开始真正拥有“现实履约的闭环能力”**。

在过往的很多演示中，智能体看起来无所不能，但只要一涉及真金白银的外部交付——比如帮你订一张票、买一个域名、调一次付费 API——系统就会卡壳在“权限与信任”的断崖前。

而今天的技术演进正在迅速填平这条鸿沟：
从 **Composio Instant 引入的受控预付钱包机制**，到 **Voxtral 3 将工具调用端到端缝进语音流**，智能体正在从“只会夸夸其谈的参谋”，蜕变为“能签单、能买单、能对最终结果负责的执行官”。

这也给所有产品人与独立开发者指明了下半场的护城河：
**别再卷通用的问答壳子，去深扎那些需要“确权、履约、交付闭环”的重度垂直场景。**
谁能帮用户省下最后那 10 秒钟的手动付款与确认，谁就能在商业闭环中占据不可动摇的位置。

愿你在今天的造物中，锚定真实交付，筑牢属于自己的确定性壁垒。''',
        'ai_news': [
            {
                'category': 'AI 资讯',
                'title': 'Voxtral 3 把听说与工具调用接成语音流水线',
                'note': 'Mistral 重磅发布的端到端多模态语音 SDK：打通了高拟真语音识别、复杂意图推理与外部工具调用，将对话往返延迟压缩至百毫秒极值，提供完全私有化部署选项。',
                'so_what': '打破传统 ASR-LLM-TTS 串联流水线的延迟黑洞；端到端原生语音意图解析，为下一代实时车载助理与高频人机协作智能体树立了标杆。',
                'source': 'mistral.ai',
                'url': 'https://mistral.ai/news/voxtral-3/',
                'media': 'https://images.unsplash.com/photo-1589254065878-42c9da997008?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'DeepSeek 开源推理框架 DeepInfer',
                'note': 'DeepSeek 官方开源的下一代高并发推理加速框架：针对 MoE 架构深度定制显存调度算法与内核算子，在超长上下文高并发吞吐场景下将首字延迟降低超 40%。',
                'so_what': 'MoE 架构工业级落地的推理基石；自研算子与通信掩盖策略彻底释放了异构硬件潜能，为低成本高并发 AI 服务筑牢底座。',
                'source': 'github.com',
                'url': 'https://github.com/deepseek-ai/DeepInfer',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'llm-d 1.0 把推理服务重点移向持续运营',
                'note': 'IBM 联合开源社区发布的生产级大模型推理管理平台：原生集成动态配额、多级缓存击穿防护与分布式灰度发布，把模型服务的关注点从单点性能扩展至全生命周期 SLA 保障。',
                'so_what': '大模型工程从玩具迈向工业级基础设施的标志；提供完备的遥测指标与金丝雀发布机制，让企业级大模型服务具备传统微服务级别的稳健度。',
                'source': 'research.ibm.com',
                'url': 'https://research.ibm.com/blog/llmd-1-0-is-ready-for-production-inference-serving',
                'media': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 资讯',
                'title': 'TorchTPU 让 PyTorch 原生连接 TPU 后端',
                'note': 'PyTorch 官方正式推出的原生 TPU 加速后端：无需通过繁琐的外部转换层即可直接将标准 PyTorch 算子编译为 XLA 图并调度至云端 TPU 集群，极大降低迁移开销。',
                'so_what': '打破专用硬件软件生态壁垒；统一的顶层 API 让算法团队可以在 GPU 与 TPU 算力池间灵活横跳，规避单一供应链风险。',
                'source': 'pytorch.org',
                'url': 'https://pytorch.org/blog/introducing-torchtpu/',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI Tooling Nodes 批处理套件：复杂漫剧多镜头节点树规范与批量排队渲染',
                'note': '漫剧制片团队的核心管线增强插件：提供镜头元数据透传、分辨率自动适配与多镜头批量任务队列调度，避免单图生成中断影响整集出片节奏。',
                'so_what': '作坊式出图走向工业化流水线的关键跨越；用标准化的节点接口降低资产交接损耗，让长篇漫剧的批量稳定出片成为现实。',
                'source': 'github.com',
                'url': 'https://github.com/Acly/comfyui-tooling-nodes',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'AI 短剧“杀不死”游戏：互动影游与生成式视听的深度竞合与边界思考',
                'note': '行业从狂热降温后的清醒复盘：探讨 AI 视频生成如何与互动游戏机制结合，分析高频生成内容在沉浸交互、分支剧情与叙事代入感中的优势与先天局限。',
                'so_what': '技术狂欢过后的商业冷水；厘清 AI 视听是强化玩法而非取代机制，为探索“AI 生成+互动叙事”的从业者指明了现实定位。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6480940.html',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '《人体100层生存电梯》微观世界求生漫剧商业全本：细胞群像与异化危机视听分镜交割',
                'note': '脑洞大开的高概念生存科幻漫剧全案：将人体微观循环系统具象化为百层封闭垂直电梯，各器官细胞化身不同阶层求生者，以快节奏高能反转展现免疫系统对抗病变危机的宏大史诗。',
                'so_what': '将科普硬核知识与爆款无限流题材深度融合；严密的分镜设计与戏剧张力为 AI 漫剧视觉团队提供了开箱即用的工业化生产蓝本。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1745',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《天下清官——张伯行》历史正剧文学剧本全案：廉吏风骨与官场权谋交织的影视化重塑',
                'note': '宏大传统历史正剧文学全本：以清代廉吏张伯行力抗江南科场舞弊案为主线，兼顾严肃历史考据与激烈戏剧博弈，为文旅宣发与历史漫剧创制提供了坚实的文学底盘。',
                'so_what': '传统文化 IP 的高维视听再现；厚重的文学骨骼让微短剧跳出无脑爽点泥潭，证明严肃题材在分众精品市场依然具备强劲穿透力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1747',
                'media': 'https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《肠道紧急会议》荒诞讽刺短剧：拟人化器官博弈与当代打工人健康焦虑的喜剧化解构',
                'note': '爆笑微短剧编剧范式解析：将暴饮暴食与熬夜加班具象为消化道内部的紧急罢工与弹劾听证会，用荒诞解构的职场黑话映射打工人生活真相，节奏明快、包袱密集。',
                'so_what': '把日常痛点转化为戏剧冲突的极佳切口；以小见大的隐喻手法既能瞬间击中受众共鸣，又巧妙规避了严肃说教的沉重感。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1744',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《宿主发烧那一夜》群像灾难守城短剧：微观免疫战线与宏观末世灾难叙事结构的镜像映射',
                'note': '微观拟人题材如何写出院线级灾难史诗感的高级范本：将一场常见的流感高热，重构为类似中世纪围城战的悲壮守卫战，白细胞前赴后继的战友情谊构建出强大的情感弧光。',
                'so_what': '以灾难片叙事语法赋能微观题材；精巧的情节阶梯与悲壮宿命感，展现了编剧在设定限制下挖掘极致戏剧张力的深厚功力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1743',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《妈妈的反杀，28天追回20万》现实反诈短剧：强情节悬疑与母职心理对抗的社会派剧作',
                'note': '贴地飞行的现实题材微短剧创作全案：取材自真实境外电诈与养老投资陷阱案例，不走金手指爽剧路线，全凭平凡母亲的隐忍布局、蛛丝马迹取证与心理攻防战步步为营。',
                'so_what': '现实主义短剧在下沉市场的超强爆破力；用扎实的逻辑推演与母性本能的情绪张力唤醒全民反诈警觉，社会价值与商业点播双赢。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1741',
                'media': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '《星界撤离：零号玩家》搜打撤赛博短剧：游戏机制向视听叙事转化的节奏把控与爽点铺设',
                'note': '针对年轻电竞与科幻核心受众的高概念剧作：精准提炼“搜刮、交火、限时撤离”的核心游戏快感，结合赛博义体改装与阵营背叛暗线，打造每一集都有生死倒计时的极致紧迫感。',
                'so_what': '跨媒介叙事在短剧领域的成功嫁接；把游戏玩家天然熟悉的负重机制与安全区博弈化为剧作动力，开辟了年轻态垂类短剧的新蓝海。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1915',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '一线从业者的真实声音：AI 电商应用的痛点和卡点复盘',
                'note': '大厂与新创电商团队在 AI 落地一线的实战血泪史：深度剖析智能客服答非所问、商品生图质感失真退货率攀升、营销文案同质化严重等现实卡点，探讨如何建立品控闭环。',
                'so_what': '走出大模型造神滤镜的清醒审视；只有深入供应链履约与售后纠纷一线，才能找到技术与商业真实场景严丝合缝的结合点。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6480943.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '双11再交手，抖音京东在争什么？存量博弈下的产品与履约较量',
                'note': '电商存量博弈下平台核心能力演进的深度研判：内容流量池与货架确定性履约的正面碰撞，分析平台如何在极致低价策略下平衡商家毛利空间与用户端心智留存。',
                'so_what': '电商产品战略从流量驱动向供应链深水区切换；理解履约确定性与价格力心智的平衡点，是中高级产品经理洞悉平台胜负手的关键视界。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6481278.html',
                'media': 'https://images.unsplash.com/photo-1556742049-0a67e557224d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '京东采销朋友圈引诉讼背后：藏在比价里的“毛保”账本与供应链底牌',
                'note': '供应链商业模式与平台规则博弈的透视：抽丝剥茧拆解采销“毛利保证”协议背后的财务逻辑，揭示多平台比价机制对品牌全渠道价格体系的冲击与重构。',
                'so_what': '看穿平台规则背后的利益再分配机理；真正的商业洞察不仅是产品功能的推演，更在于读懂上下游各方的利益底牌与博弈杠杆。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6481142.html',
                'media': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '联盟广告商业化模式演进：从粗放分发到全域精准归因',
                'note': '广告商业化产品核心逻辑的跃迁脉络：回顾移动互联网时代 CPS、CPA 模式的兴衰，深入探讨后隐私时代通过自研多触点归因与增量实验实现高价值获客的技术演进。',
                'so_what': '商业化产品经理的底层方法论修养；在流量红利消退的当下，唯有依靠精准归因与全链路度量，才能帮广告主挤干泡沫榨取真实增量。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/operate/6480959.html',
                'media': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

# 2. Curated Ian picks (20 items across 5 categories)
raw_ian_path = 'scripts/raw-ian-21.json'
with open(raw_ian_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

curated_ian_picks = {
    'AI 协作': [
        'https://forgeturl.github.io/md2chat',
        'https://github.com/alibaba/qz-browser-agent',
        'https://github.com/reticlehq/reticle',
        'https://composio.dev/instant'
    ],
    '一人公司': [
        'https://resourcedeck.app/',
        'https://apps.apple.com/us/app/taprev-saas-revenue-tracker/id6758924195',
        'https://purepdfhq.com',
        'https://deathplanswitch.com/'
    ],
    '产品设计': [
        'https://pdfkind.com/edit-pdf',
        'https://spacebar.greg.technology/',
        'https://misfitdev.github.io/daisy/',
        'https://inflight.co/'
    ],
    '审美提升': [
        'https://www.designboom.com/architecture/vincent-darre-le-magnifique-hotel-paris-theatrical-interiors/',
        'https://www.dezeen.com/2026/10/20/box-9-brick-soho-restaurant-kid/',
        'https://www.designboom.com/art/sandbag-castle-sustainable-concrete-alternatives-floating-installation-eindhoven-yvonne-mak/',
        'https://www.dezeen.com/2026/10/20/wildlife-pavilion-desai-chia-architecture-new-york/'
    ],
    '产品营销': [
        'https://reception.sh/',
        'https://launchloop.dev',
        'https://www.creativeboom.com/news/oslos-grumpiest-resident-returns-new-halfdan-winter-campaign-generates-5m-views/',
        'https://pug.sh/'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://forgeturl.github.io/md2chat': '人机协作排版体验的微创新；告别全屏截图导致的文字无法复制与低清模糊，让技术笔记在即时通讯中既养眼又实用。',
    'https://github.com/alibaba/qz-browser-agent': '“人机共驾”才是落地网页 Agent 的务实解；在完全无人值守与纯手动操作之间取得平衡，让复杂长流程网页自动化真正可靠可用。',
    'https://github.com/reticlehq/reticle': '软件工程 Agent 闭环的最后一块拼图；不仅写代码，更在真实运行环境中收集执行凭据，把代码交付从“盲盒提交”升级为“证据驱动”。',
    'https://composio.dev/instant': '让智能体跨过“经济行为自主”的质变奇点；受控钱包机制解开了传统自动化在资金层面的死结，为全自主商业闭环扫清了障碍。',
    'https://resourcedeck.app/': '数据主权与无压响应的极简美学；告别繁重协同工具的账号权限与月费泥潭，一个离线文件即可维系高效生产节奏。',
    'https://apps.apple.com/us/app/taprev-saas-revenue-tracker/id6758924195': '消除多平台对账的心智损耗；清晰明了的资金仪表盘让单兵创业者随时掌握现金流生命线，专注于核心产品迭代。',
    'https://purepdfhq.com': '工具型出海微产品的经典解法；用现代浏览器端侧算力消灭服务器带宽与存储开销，极低边际成本成就高粘性口碑。',
    'https://deathplanswitch.com/': '一人公司的终极契约精神；把单点故障（SPOF）的伦理防线做成透明自动化协议，赋予微型企业跨越周期的商业信任。',
    'https://pdfkind.com/edit-pdf': '对既有文档工作流的非侵入式升维；消除格式转换过程中的版面错乱痛点，把复杂操作收敛为一个光标点击。',
    'https://spacebar.greg.technology/': '系统级微交互的生产力倍增器；无需启动沉重的大型 IDE 或数据分析软件，随时随地在文件树中完成数据巡检。',
    'https://misfitdev.github.io/daisy/': '多机办公极客的桌面减法；打破硬件物理边界，用原生手势直觉消除机械切换开关的繁琐操作。',
    'https://inflight.co/': '终结设计与研发间的“踢皮球”沟通成本；视觉批注直接闭环为代码提交，让细微设计改动的交付周期缩短至分钟级。',
    'https://www.designboom.com/architecture/vincent-darre-le-magnifique-hotel-paris-theatrical-interiors/': '历史文脉与空间情绪的深邃交融；拒绝千篇一律的现代极简，用强烈的戏剧仪式感赋予商业空间不可替代的叙事灵魂。',
    'https://www.dezeen.com/2026/10/20/box-9-brick-soho-restaurant-kid/': '可持续建筑材料与在地街区文脉的温柔对齐；用循环材料的肌理讲述岁月故事，展现低调而高级的审美底蕴。',
    'https://www.designboom.com/art/sandbag-castle-sustainable-concrete-alternatives-floating-installation-eindhoven-yvonne-mak/': '公共艺术对生态危机的幽默回应；将沉重的工程材料转化为轻盈漂浮的视觉奇观，拓展了低碳材料的艺术边界。',
    'https://www.dezeen.com/2026/10/20/wildlife-pavilion-desai-chia-architecture-new-york/': '消融于自然背景中的克制设计；建筑不宣兵夺主，以纯粹的几何形体化身为自然观察与精神冥想的澄澈容器。',
    'https://reception.sh/': '在痛点最敏锐的“黄金时刻”完成价值交付；将售后支持窗口重塑为最高效的追加销售与续费转化阵地。',
    'https://launchloop.dev': '消除技术人员“会写代码不会宣传”的心智负担；让每一次代码提交都成为触达潜在用户的有效公关素材。',
    'https://www.creativeboom.com/news/oslos-grumpiest-resident-returns-new-halfdan-winter-campaign-generates-5m-views/': '反常识反套路的真实人设击穿用户防御；放弃浮夸宏大的说教式宣传，用自嘲与黑色幽默赢得年轻受众的情感共鸣。',
    'https://pug.sh/': '找回被浏览器隐私保护切碎的营销因果链路；为独立站提供了零依赖、低成本的长周期漏斗分析利器。'
}

day_items = []

# 1. AI 资讯 (from vertical_data)
v_info = vertical_data['2026-10-21']
for news in v_info['ai_news']:
    used_set.add(news['url'])
    day_items.append(news)

# 2. 5 ian categories × 4 items
target_5_categories = ['AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
for c in target_5_categories:
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

# 3. 3 vertical categories × 4 items
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
date: '2026-10-21'
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

out_file = 'src/content/daily/2026-10-21.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-21! Total URLs in history: {len(all_used_list)}')
