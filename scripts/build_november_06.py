# -*- coding: utf-8 -*-
import json
import yaml
import os

items = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "ERNIE 5.5 Flash Base 开放预训练权重：端云协作高吞吐轻量推理新基座",
        "note": "百度文心系列轻量化模型的关键一步：全面开源 Flash Base 预训练底座权重，聚焦高吞吐、低显存消耗场景，在单卡边缘设备上即可跑出数倍于同尺寸模型的吞吐速率。",
        "so_what": "为企业高并发批处理与端侧实时 Agent 铺平道路；打破了算力成本对大规模实时交互的束缚，让私有化离线部署具备了极具竞争力的性能价格比。",
        "source": "ernie.baidu.com",
        "url": "https://ernie.baidu.com/release/ernie-5-5-flash-base/",
        "media": "https://iandaily.xyz/digest/2026-11-06-ernie-ce8c726afc6c.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "Cursor 把内部应用从本地带到可分享网址：原型即交付的云端沙箱",
        "note": "AI 编程 IDE 交付链条的关键闭环：不仅帮开发者在本地写代码，更允许 Agent 一键将生成的轻量应用即时编译并部署到公开可访问的安全沙箱二级域名。",
        "so_what": "彻底消灭从代码生成到客户演示之间的繁琐运维断层；独立开发者与产研团队可在数秒内将脑海中的点子化为可点击、可交互的真机链接，极大推高产品验证频次。",
        "source": "cursor.com",
        "url": "https://cursor.com/changelog/build-live-apps",
        "media": "https://iandaily.xyz/digest/2026-11-06-cursor-a285c56a230c.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "OpenClaw Multiplayer 让多人共用代理现场：多开发者实时协同调试智能体",
        "note": "重构 AI 编程现场的人机协同体验：允许多名工程师同时进入智能体的运行时终端，实时围观 Agent 的推演思考、修改断点、交替注入补充上下文指令。",
        "so_what": "攻克智能体调试黑盒孤岛的关键方案；将原本单打独斗的 AI 对话升级为团队结对编程工坊，让复杂多智能体系统的调优与故障复盘具备了集体智慧。",
        "source": "openclaw.ai",
        "url": "https://openclaw.ai/blog/shattering-silos-with-openclaw-multiplayer",
        "media": "https://iandaily.xyz/digest/2026-11-06-openclaw-7ba0e04a77ef.jpg",
        "pinned": False
    },
    {
        "category": "AI 资讯",
        "title": "Gemini Omni 1.2 Flash 延长原生视频生成：长程多模态连贯视听新突破",
        "note": "Google 带来的长时序视频多模态模型升级：在保持秒级极速响应的同时，原生支持长达数十秒的物理时空连贯渲染，镜头运动与光影交织具备高保真稳定性。",
        "so_what": "击碎了 AI 视频单镜头只能维持几秒的传统瓶颈；让完整视听叙事与戏剧长镜头的自动化生成成为可能，直接降低了视频创作者拼接后期的合成成本。",
        "source": "blog.google",
        "url": "https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/",
        "media": "https://iandaily.xyz/digest/2026-11-06-gemini-6b7a905d9c11.jpg",
        "pinned": False
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "EtherPK 把看板任务交给编程代理：卡片拖拽直连 Claude Code 自动化实施",
        "note": "连接敏捷项目管理与命令行编程智能体的敏捷桥梁：在图形化看板上拖动 Markdown 任务卡片，系统自动打包需求文档、关联代码上下文并派发给后台 Claude Code。",
        "so_what": "消除非技术项目经理与终端 CLI 智能体之间的交互隔阂；无需每次打开控制台手敲提示词，用直观的任务流完成对 AI 劳动力的敏捷排期与进度追踪。",
        "source": "blog.etherpk.com",
        "url": "https://blog.etherpk.com/hand-your-markdown-tasks-to-claude-code-from-a-kanban-board",
        "media": "https://iandaily.xyz/digest/2026-11-06-etherpk-f6c86d1fa0ad.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "Lantern Lattice 让代理沿调用关系找代码：基于 AST 拓扑的有向图代码搜索",
        "note": "告别传统基于文本关键字与低准确度向量模糊匹配：解析代码抽象语法树（AST），为 Agent 构建函数与类的上下游有向依赖网络，指引智能体按图索骥。",
        "so_what": "智能体深阅读大型仓库代码的必备显微镜；大幅削减在无关联文件上的无效检索与 Token 浪费，让 Agent 能在几万行复杂工程中精准定位重构切入点。",
        "source": "github.com",
        "url": "https://github.com/julymetodiev/lantern-lattice",
        "media": "https://iandaily.xyz/digest/2026-11-06-lantern-50c2fb53f684.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "thinker 把上下文账单拆给你看：精准追踪长程智能体每个 Prompt 的 Token 损耗",
        "note": "专为 Agent 工程化落地的透明算力计费与审计工具：实时捕获并可视化每一次多轮对话、工具调用与思考链的 Token 吞吐，用多维瀑布图标记算力暗坑。",
        "so_what": "消除企业部署自主智能体的成本失控恐慌；用手术刀般的精度排查陷入死循环或冗余 System Prompt 的消耗节点，为模型选型与上下文压缩提供硬核数据支撑。",
        "source": "thinker.sh",
        "url": "https://thinker.sh/how-it-works",
        "media": "https://iandaily.xyz/digest/2026-11-06-thinker-b2c3425a1a61.jpg",
        "pinned": False
    },
    {
        "category": "AI 协作",
        "title": "Tokenome 让一行代码连回生成时的对话：智能体代码资产的可溯源版本化",
        "note": "将代码变更与当时驱动的 Prompt、上下文切片及大模型回复哈希永久绑定的版本控制插件：在代码行旁一键回溯当初人类意图与模型推演的全过程。",
        "so_what": "化解后 AI 编程时代‘代码没人敢改、不知从何而来’的技术债务恐慌；让每一行生成代码都具备可审计的上下文血缘关系，守护系统架构的可维护性。",
        "source": "tokenome.ai",
        "url": "https://tokenome.ai/",
        "media": "https://iandaily.xyz/digest/2026-11-06-tokenome-8b9207b4ab00.jpg",
        "pinned": False
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "CalmCanary 先守住检测与提醒两件事：克制而高可用的一人服务监控小站",
        "note": "一人公司对抗臃肿监控巨石 Datadog 的极简范本：摒弃眼花缭乱的指标图表，专注于服务崩溃即时发报与证书过期预警两条核心主线，配置时间不到 1 分钟。",
        "so_what": "独立开发者极简主义的典范；把精力从繁复的运维监控配置中彻底解放，以近乎零维护成本守护单兵旗下数十个微型 SaaS 的在线生命线。",
        "source": "calmcanary.co",
        "url": "https://www.calmcanary.co/",
        "media": "https://iandaily.xyz/digest/2026-11-06-calmcanary-a7cc0225ff07.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "这只虚拟鱼缸也得先养好硝化菌：极简黑白像素风网页生态模拟小游戏",
        "note": "将小众硬核生态学知识做成极简网页交互的单兵作品：玩家必须先模拟氮循环、培养硝化细菌才能维持虚拟鱼类的生命平衡，复古黑白像素风格与治愈音效极其迷人。",
        "so_what": "利基硬核爱好者的情绪催化剂；展示了一人开发者如何用真实物理与生态法则创造极高沉浸感的微型世界，靠口口相传在垂直社区构筑长效粘性壁垒。",
        "source": "fishtankatlas.com",
        "url": "https://fishtankatlas.com/play/aquarium/",
        "media": "https://iandaily.xyz/digest/2026-11-06-fishtank-96e7538d6068.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Droplis 把单次点击做成每日谜题：高留存的极简数字重力解谜独立站",
        "note": "纯前端零后端支撑的高日活小游戏：玩家每天仅有固定一次掉落规划机会，利用重力与数字消除触发连锁反应，简洁的色彩搭配与每日全球排行榜引爆自然分享。",
        "so_what": "极简游戏化增长的教科书样本；以微不足道的静态托管成本撬动成千上万每日固定打卡用户，为单兵独立站沉淀忠实的高留存私域流量池。",
        "source": "droplis.lalo.li",
        "url": "https://droplis.lalo.li/",
        "media": "https://iandaily.xyz/digest/2026-11-06-droplis-e6b3dcbbe459.jpg",
        "pinned": False
    },
    {
        "category": "一人公司",
        "title": "Spaceguesser 把猜地点搬进太阳系：行星地理知识与游戏化结合的变现样本",
        "note": "将 Geoguessr 经典玩法移植至外太空天体表面：借助 NASA 公开轨道拍摄影像，让天文爱好者通过陨石坑与地貌特征竞猜行星与卫星坐标，兼顾科普与益智。",
        "so_what": "公共开源数据二次商业化变现的绝妙切口；无需高额的数据采集费用，巧妙利用极客受众的探索欲，以轻量会员制与定制挑战包实现健康的被动收益。",
        "source": "spaceguesser.com",
        "url": "https://spaceguesser.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-spaceguesser-d598bc0e8b15.jpg",
        "pinned": False
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Detail Keeper 听一次就记住名字拼法与偏好：商务社交中的高保真细节管家",
        "note": "专为社交细节敏感人群打造的轻量人际记忆工具：告别传统笨重复杂的 CRM 字段，仅用简练文本卡片记录客户姓名读音、忌口与沟通习惯，毫秒级快速调取。",
        "so_what": "反功利化社交工具的交互创新；将产品重心从‘客户线索转化’退回到‘真诚人际尊重’，用最轻量克制的设计唤醒商务人士被信息洪流淹没的同理心。",
        "source": "detailkeeper.com",
        "url": "https://detailkeeper.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-detailkeeper-99d9957cf97d.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Climbing Guide 把动作串联做成可暂停的交互动图：空间体育的轻量可视化解析",
        "note": "攀岩发烧友倾力打造的交互动作指南：将复杂的岩壁抱石动态拆解为可任意拖动时间轴、自由旋转三维视角的矢量交互图解，每个发力支点均有清晰力学标记。",
        "so_what": "打破传统视频教学无法精准拆帧的体验壁垒；证明优秀的信息设计无需依赖重度 3D 引擎，用轻巧的前端动效就能讲透三维空间运动的核心逻辑。",
        "source": "scott1743.github.io",
        "url": "https://scott1743.github.io/climbing-guide/",
        "media": "https://iandaily.xyz/digest/2026-11-06-climbing-1ff652dc3a0b.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "aless 让不同数据文件共用一棵树：统一跨格式异构目录的极简文件浏览新范式",
        "note": "开发者本地数据探索的极简命令行工具：无缝统一 JSON、YAML、Parquet、CSV 与 SQLite 数据，以同一套树状节点交互支持层级折叠、按路径过滤与快速预览。",
        "so_what": "抹平多格式异构数据检查的认知摩擦；工程师无需在不同 GUI 工具间来回切换，在一个极度流畅的原生终端视图中透视所有结构化数据，大幅提速排障效率。",
        "source": "aless.tabnas.dev",
        "url": "https://aless.tabnas.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-06-aless-4e5470090e43.jpg",
        "pinned": False
    },
    {
        "category": "产品设计",
        "title": "qodesign 把动效组件做成单文件纯净交付：告别臃肿第三方依赖的微前端组件库",
        "note": "反思 npm 依赖地狱的前端微设计库：所有弹性按钮、流光边框与平滑浮层均打包为包含 HTML/CSS 的单个独立文件，复制粘贴即可直接在任意前端项目中运行。",
        "so_what": "极简模块化交付的极致体验；杜绝版本冲突与构建工具链锁死的噩梦，让前端开发者与智能体编码助手均能零心智负担地引入高品质视觉交互组件。",
        "source": "teodoravadani.github.io",
        "url": "https://teodoravadani.github.io/qodesign-free/",
        "media": "https://iandaily.xyz/digest/2026-11-06-qodesign-a15e7acd6640.jpg",
        "pinned": False
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Gustaf Westman 把迪士尼米奇轮廓做成厚实雕塑家具：波普解构与童趣实体化",
        "note": "瑞典先锋设计师与迪士尼的跨界力作：将经典的米奇大耳与波浪线条转化为圆润膨胀的厚实木质边几与泡泡椅，辅以高饱和奶黄与薄荷绿，打破古典家具沉闷秩序。",
        "so_what": "经典文化符号的后现代实体解构；展示了如何将平面动画的无厘头萌感与厚重的家具工艺材料完美结合，为居住空间注入反叛而治愈的幽默感与童趣张力。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/design/gustaf-westman-disney-mickey-mouse-chunky-colorful-furniture/",
        "media": "https://iandaily.xyz/digest/2026-11-06-westman-335e81e59d69.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Angelo Renna 提议让三十九棵树围出佛罗伦萨河畔浮岛：城市水域的生态漂浮森林",
        "note": "佛罗伦萨阿诺河上的先锋生态建筑构想：由 39 棵本土白杨与柳树环抱成一个浮动圆环岛屿，不仅为市民提供避暑亲水空间，其悬挂水下根系更自然净化河流微塑料。",
        "so_what": "建筑美学与生态自愈机制的诗意融合；证明城市景观不必是冰冷坚硬的混凝土堆砌，漂浮的活体植物同样可以充当抵御气候热浪与净化水质的柔性基础设施。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/architecture/angelo-renna-floating-modular-island-39-tree-ring-florence-river-firenze-little-island/",
        "media": "https://iandaily.xyz/digest/2026-11-06-renna-315cc2c996b5.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "PP-2 无唱臂光学黑胶唱机：整块阳极氧化铝与悬浮红外读取的极简仪式",
        "note": "颠覆百年机械唱针传统的东京极简音响：摒弃传统唱臂与唱针，利用超高精度非接触式激光束扫描唱片微槽，机身由整块实心铝铣削而成，唱片悬浮于透明机盖下。",
        "so_what": "工业物理极致与极简主义美学的集大成者；消除了物理摩擦对黑胶唱片的永久磨损，将音乐重放过程升华为一件宛如现代雕塑般的视觉与听觉纯粹冥想。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/technology/pp-2-turntable-reads-vinyls-without-tonearm-glass-listening-room-tokyo-waiting-for-ideas/",
        "media": "https://iandaily.xyz/digest/2026-11-06-pp2-29538c42d07d.jpg",
        "pinned": False
    },
    {
        "category": "审美提升",
        "title": "Linehouse 把杭州老工业丝绸厂区痕迹带进当代酒店：砖石锈迹与织物肌理的交融",
        "note": "杭州老运河畔工业遗址的室内蜕变：设计团队将当年丝绸印染厂的锈蚀工字钢、裸露红砖与丝绸般滑润的拉丝金属隔断并置，利用天光漫射营造出江南水乡的工业诗意。",
        "so_what": "在地历史脉络与现代奢华体验的和谐对话；向空间设计师展示了如何拒绝千篇一律的标准化流水线装潢，用场地原生的时间痕迹塑造独一无二的情感温度。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/11/05/linehouse-jen-hotel-hangzhou/",
        "media": "https://iandaily.xyz/digest/2026-11-06-linehouse-79e8ff3c782d.jpg",
        "pinned": False
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "aireel 从产品落地页直接组织一支高转化宣传短片：将静态文案自动编排为动态叙事",
        "note": "颠覆传统视频宣发制作流程的营销智能体：输入 SaaS 落地页 URL，AI 自动提取核心卖点、痛点解决因果链与用户评价，分步编排为高燃配乐与运镜演示合一的宣传短视频。",
        "so_what": "将高昂的外部视频制作外包成本缩减至零；让独立团队在产品上线当天即可分发十余条不同痛点视角的社媒宣发素材，极大缩短冷启动获客周期。",
        "source": "aireel.tv",
        "url": "https://aireel.tv/",
        "media": "https://iandaily.xyz/digest/2026-11-06-aireel-993cd87c0b09.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "PitchFlip 把创业起点画成翻页故事：告别冰冷 PPT 的情绪化互动获客新载体",
        "note": "用绘本叙事重构融资与产品发布页：将创业者解决痛点的真实心路历程绘制成支持键盘与触控翻页的插画微故事，文末顺畅植入公测预约与投资人意向沟通表单。",
        "so_what": "情绪价值驱动品牌好感度的经典打法；在大家对千篇一律的商业计划书产生审美疲劳时，用诚恳脆弱的真实故事直击用户心底，带来数倍于普通落地页的转化率。",
        "source": "pitchflip.shiptiffin.app",
        "url": "https://pitchflip.shiptiffin.app",
        "media": "https://iandaily.xyz/digest/2026-11-06-pitchflip-9904ad865da8.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "PinSharing 把地图历史留存权写进分层定价：微型工具商业闭环与增值钩子设计",
        "note": "直击出游好友协作标记地图痛点的定价范式：基础多人标注完全免费，但若想永久锁定历史足迹、生成高分辨率时间旅行热力图则触发订阅，巧妙锚定留存痛点。",
        "so_what": "微型消费级 SaaS 的变现心法；不盲目在核心功能上设卡阻碍自然口碑传播，而是利用用户对珍贵记忆‘不想丢失’的情感杠杆促成自然付费转化。",
        "source": "pinsharing.com",
        "url": "https://pinsharing.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-pinsharing-7cbdf192b1d1.jpg",
        "pinned": False
    },
    {
        "category": "产品营销",
        "title": "Trademark Screen 出海产品命名合规初筛：把高频法律避坑做成低摩擦引流利器",
        "note": "出海团队命名防暴雷的精准切入点：输入拟用产品名，秒级比对美欧及 WIPO 商标数据库同类在审商标，并给出相似度风险评分与域名社媒占用情况。",
        "so_what": "免费工具（Tool Marketing）获客的典范；把原本属于昂贵知识产权律所的初筛工作自动化，既解决了创业者命名焦虑，又顺理成章地将高意向企业导流至商标代办服务。",
        "source": "trademarkscreen.com",
        "url": "https://trademarkscreen.com/",
        "media": "https://iandaily.xyz/digest/2026-11-06-trademarkscreen-dd79237f8953.jpg",
        "pinned": False
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "农学女博士穿越宋末崖门海战：AI 短剧工业化制作实录与历史漫剧叙事探索",
        "note": "国内一线视听团队的万字深度实操复盘：用生成式大模型攻克古战场千舰云集、惊涛骇浪与复杂甲胄的一致性难题，将硬核历史痛点与现代知识穿插成高张力短剧。",
        "so_what": "AI 漫剧从概念展示步入严肃历史题材工业化创作的里程碑；证明只要剧作扎实、分镜把控精细，AI 工具完全有能力承载厚重家国情怀与大场面视听震撼。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6490063.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "腾讯微视靠短剧换种活法：大厂短剧生态转型与精品分账变阵策略",
        "note": "沉寂已久的短视频老将依托短剧重构商业逻辑：全面拥抱竖屏短剧精品化分账模式，下沉扶持头部剧本创作者与中小型 AI 制片工坊，借内容升级实现用户回流。",
        "so_what": "大厂渠道红利洗牌下的短剧新机遇；平台对粗制滥造狗血剧的打压，为兼具审美质感与快速交付能力的 AI 漫剧团队腾出了巨大的精品化分账空间。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/share/6489983.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "红果短剧接入豆包大模型：免费短剧巨头的生成式 AI 视听重组与智能互动试验",
        "note": "免费短剧霸主红果与字节豆包技术底座的重磅整合：探索在剧集播放过程中由大模型根据观众弹幕意向动态生成分支小剧场，并开启低成本漫剧批量测试。",
        "so_what": "传统影视长尾短剧分发范式的颠覆；AI 不仅重塑了制作端的成本结构，更在播放消费端开辟出‘互动伴随与即时生成’的全新商业象限。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6489655.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "AI 漫剧",
        "title": "ChatGPT 上线 Images 2.6 动图生成：漫剧关键帧与多视角动态视效进化",
        "note": "OpenAI 图像模型迎来的重大飞跃：原生支持高帧率连贯 GIF 与微动效生成，精准保持同一角色在不同景别与动作流转中的骨骼比例与面部特征一致性。",
        "so_what": "降低 AI 漫剧关键帧补间动画的合成门槛；创作者无需在不同视频放大工具间反复对齐转码，单次提示词即可产出流畅的人物微表情与转场动效。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6489533.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《仙门第一关系户》120 集微短剧：仙侠轻松、废柴逆袭与人缘流因果冲突",
        "note": "打破传统修仙苦大仇深杀戮套路的轻喜剧模本：主角毫无灵根却深谙人情世故与资源互换，在各大门派勾心斗角中靠‘借势借力’逢凶化吉，笑料百出。",
        "so_what": "短剧类型化创新的‘反英雄’人设设计心法；将现代职场社交智慧与古典仙侠架构碰撞，既消解了观众的审美疲劳，又以轻松解压的因果连环牢牢黏住追剧欲望。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2233",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《农门灵泉小富婆》120 集微短剧：古装种田、空间金手指与女频经商致富律动",
        "note": "女频治愈经商赛道的高分剧本：现代农业学家穿越破落农家，依靠一口能改善土壤的灵泉，从卖野菜起步一步步买田置地、开连锁酒楼，节奏明快舒适。",
        "so_what": "把握下沉受众‘掌控感与获得感’的情绪引擎；拒绝无谓的极品亲戚缠斗，将每一次劳作付出与财富跃升的因果闭环夯死，提供持续稳定的精神正反馈。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2234",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《天工大明》120 集微短剧：古装工匠、硬核技术造物与工部智斗逆袭",
        "note": "匠造技术流短剧的典范之作：底层小木匠凭借对卯榫力学、水利机械与火器制造的极致造诣，在皇家营造中连破权贵设下的工程死局，终成一代大国工匠。",
        "so_what": "将‘技术原理’转化为‘戏剧武器’的高级编剧手法；展现了硬核技术比拼如何在戏剧冲突中替代传统的权谋嘴炮，带给观众智力碾压的极致爽快感。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2235",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "编剧技巧",
        "title": "《寄生星图》120 集微短剧：硬科幻太空远航、未知星云与幽闭博弈悬疑",
        "note": "短剧赛道罕见的硬科幻惊悚力作：一艘探索深空的货运科考船在遭遇神秘引力透镜后，船员发现航行日志被未知意识悄然篡改，密闭空间内信任防线瞬间土崩瓦解。",
        "so_what": "空间局限下心理张力构建的教科书；证明小成本短剧只要把‘有限视角’与‘信息不对称’推到极致，仅靠三两人对话同样能营造出摄人心魄的太空惊悚史诗。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2236",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "AI 产品经理转型指南：六大细分方向、核心能力模型与进阶图谱",
        "note": "一线产研专家的系统化转型通关手册：详细剖析模型层、Agent 编排层、端侧交互层与垂类业务赋能等六大岗位的胜任力模型，为传统 PM 指明实操演进路径。",
        "so_what": "走出‘只会写 Prompt 就算 AI 产品经理’的认知泥潭；指引产品人从底层不确定性评估、工程链路容错到商业闭环构建全景式升级自身技能树。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/pmd/6490019.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "Claude Duet 主动运行后：企业 Agent 必须写入 Runtime 的四大安全边界",
        "note": "面对自主多步执行智能体，架构师总结出的金科玉律：必须在执行环境（Runtime）中强制锁死只读沙箱、单次会话预算熔断、不可逆写操作二次人机确认与全程调用审计。",
        "so_what": "消除企业管理层对智能体‘脱缰野马’恐惧的护栏规范；产品经理在设计自主 Agent 时必须把防线前置到环境层，唯有可控的自动化才具备商用可能。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6490040.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "Agent 记忆系统设计实战：一张表、一个索引与三套分层淘汰策略",
        "note": "攻克智能体长程会话失忆难题的高效工程方案：用极简 SQLite 键值表配合语义向量索引，设计出‘短期工作记忆、中期反思总结、长期事实沉淀’的分层遗忘算法。",
        "so_what": "高性价比落地智能体记忆系统的实践标杆；拒绝盲目引入重型向量数据库集群，以极轻的架构保证 Agent 在数月交互后仍能精准记住用户的个人偏好。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6489307.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "产品经理",
        "title": "政务 AI 产品落地攻坚：业务场景设计、权限隔离与责任溯源机制",
        "note": "高容错敏感体制内场景的 Agent 落地推演：如何将复杂的公文流转、市民热线工单拆分为原子化确认步骤，通过严格的权限信封与电子签名防范大模型幻觉事故。",
        "so_what": "严肃企业级场景产品经理的硬仗指南；证明在强监管高合规领域，技术炫技必须向流程严密性妥协，让 AI 充当严谨的助手而非盲目的拍板者。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/pd/6489168.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    }
]

def build():
    frontmatter = {
        "date": "2026-11-06",
        "title": "11 月 06 日 · 现场可观测性与单兵边界重塑：从黑盒幻觉走向可验证交互现场",
        "highlights": "全网 9 大领域 36 篇高密度精选：ERNIE 5.5 Flash Base 与 Gemini Omni 1.2 开放长视频轻量底座、Claude Code 看板编排与 Token 细颗粒度账单追踪、农学博士穿越崖门海战的 AI 短剧工业化实录、一人公司极简网页游戏与生态模拟、企业级 Agent 四大 Runtime 安全边界。",
        "draft": False,
        "epigraph": "当代码生成不再停留在无序的黑盒自嗨、开始顺着 AST 调用拓扑溯源时，真正的工程可控性才开始浮现；当智能体不再试图全知全能、学会在预设的 Runtime 沙箱边界内稳健交接时，企业级生产力才宣告真正落地。",
        "lead": "11 月 6 日，人工智能应用正在从狂热的概念炒作迅速下沉为“现场级可观测性与精准边界控制”。在底层基础设施端，ERNIE 5.5 Flash Base 开放轻量高吞吐预训练权重，Gemini Omni 1.2 Flash 突破长视频原生多模态生成，让端侧与低成本推理具备了坚实基石；在智能体协作最前线，开发者不再满足于黑盒 prompt 碰运气，Lantern Lattice 用有向调用图引导 Agent 精准定位源码，thinker 将每次交互的 Token 损耗透明化拆解，企业更直接将四大不可逾越的安全红线硬编码进 Runtime 环境；在视听与内容阵地，团队用工业化 AI 短剧全流程复刻宋末崖门海战的历史悲壮，证明视听生成已迈过技术 demo 阶段，全面进入高密度叙事实战；一人公司开发者们则用极简的硝化菌生态鱼缸、天体解谜和高留存单页工具，演示着如何在巨头夹缝中靠极低算力成本收割长尾现金流。看清边界，守住确定性，这是所有实干派当下最坚硬的护甲。",
        "scene": "「为什么要把智能体调用每个函数的 Token 账单和代码调用链都实时画在看板上？」「因为在严肃系统里，无法解释的黑盒就是随时爆炸的定时炸弹。只有把 Agent 的每一步心跳和花销都晒在阳光下，我们才敢把它推进生产集群。」",
        "cover": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80",
        "items": items
    }

    # Verify counts
    by_cat = {}
    for it in items:
        by_cat[it["category"]] = by_cat.get(it["category"], 0) + 1
    print("Categories:", by_cat)
    assert len(by_cat) == 9
    assert all(c == 4 for c in by_cat.values())
    assert len(items) == 36

    yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False, width=1000)

    closing_text = """### 岛主今日寄语

今天的 36 个创新切片都在指向同一个底层命题——“可控的边界就是生产力本身”。无论是在代码库里用 AST 约束智能体的搜索路径、给 Agent 的 Runtime 锁死沙箱权限，还是把长程任务的 Token 消耗拆成明明白白的账单，实干家们都在主动为狂奔的技术套上缰绳。没有缰绳的烈马只会踏翻农田，而套上缰绳的骏马才能拉动重工业的马车。找到属于你业务的那个确定性边界，然后把它死死焊进系统里。"""

    full_md = f"---\n{yaml_str}---\n\n{closing_text}\n"

    target_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-06.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"Successfully generated {target_path}")

    # Update all-used-urls.json
    used_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/all-used-urls.json"
    with open(used_path, "r", encoding="utf-8") as f:
        used_list = json.load(f)
    used_set = set(used_list)

    new_urls = [it["url"] for it in items]
    added = 0
    for u in new_urls:
        if u not in used_set:
            used_list.append(u)
            used_set.add(u)
            added += 1

    with open(used_path, "w", encoding="utf-8") as f:
        json.dump(used_list, f, ensure_ascii=False, indent=2)

    print(f"Added {added} new URLs to all-used-urls.json, now total: {len(used_list)}")

if __name__ == '__main__':
    build()
