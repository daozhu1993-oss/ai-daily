# -*- coding: utf-8 -*-
import json
import yaml
import os

items = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Meta 将专用模型送进 Muse 与 Meta AI：垂直场景小模型高效分工协作",
        "note": "Meta 正式确立‘场景专用特化模型集群’范式：不再依赖单一庞大通用模型处理所有任务，而是将意图识别、长文总结、多轮对话与视觉理解分别交由参数极度精简的特化小模型并行执行。",
        "so_what": "终结单体大模型盲目扩张的算力内卷；为企业级系统架构指明新方向——通过专业小模型的精准分工，在大幅降低推理延迟与部署成本的同时，显著提升垂直任务的交付准确率。",
        "source": "research.meta.ai",
        "url": "https://research.meta.ai/blog/specialized-models-for-muse-and-metaai",
        "media": "https://iandaily.xyz/digest/2026-11-07-metaspecial-3aede16eeb7d.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "OpenClaw 把模型目录与客户端发版拆开：动态协议驱动的热插拔模型接入架构",
        "note": "开源 AI 工具架构设计的优雅蜕变：将支持的模型目录与能力配置文件全量解耦为云端实时协议，客户端无需重新打包发版即可零延迟热插拔接入社区最新发布的基座模型。",
        "so_what": "大幅降低客户端软件适配新型大模型的维护开销；打破以往每出新模型就必须全员发版升级的笨重周期，让开发者与终端用户永远在第一时间尝鲜最新前沿权重。",
        "source": "openclaw.ai",
        "url": "https://openclaw.ai/blog/use-new-models-in-openclaw-without-an-update",
        "media": "https://iandaily.xyz/digest/2026-11-07-clawcatalog-4c411f218df5.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "OpenRouter 推出 Auto Code 专属路由：针对编程场景的动态模型分流与性价比优化",
        "note": "聚合路由平台面向开发者的杀手级演进：针对代码补全、复杂重构、单元测试与架构设计等不同颗粒度任务，动态评估各大模型实时延迟、价格与准确率，自动调度最适配模型处理。",
        "so_what": "开发者再也不用在 Claude、GPT、DeepSeek 之间纠结手工切换；用自动化路由在保证代码编写品质的同时把每月 API 账单压缩 50% 以上，实现编程算力效益最大化。",
        "source": "openrouter.ai",
        "url": "https://openrouter.ai/blog/announcements/auto-and-auto-code-routers/",
        "media": "https://iandaily.xyz/digest/2026-11-07-router-8a98429f3722.jpg",
        "pinned": False
    },
    {
        "category": "AI 资讯",
        "title": "pico-WAM 拆开动作提案与世界模型评分：具身智能体的解耦分层规划范式",
        "note": "物理世界智能体规划算法的重大突破：将机械臂或移动底盘的‘候选动作生成’与‘物理环境演化推演评分’解耦为两个独立模块，在极低计算开销下完成对复杂动力学的预判。",
        "so_what": "攻克具身智能在边缘端算力受限下实时决策的顽疾；避免了庞大世界模型全量参与动作生成的笨重拖延，让机器人动作生成兼具灵敏反应速度与长远防撞规划能力。",
        "source": "keivalya.com",
        "url": "https://www.keivalya.com/pico-wam/",
        "media": "https://iandaily.xyz/digest/2026-11-07-picowam-104adae88d63.jpg",
        "pinned": False
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "ViewFit 按网页实际渲染尺寸动态压缩图像：前端性能优化的高效自动化智能体",
        "note": "前端工程构建链路的静默加速器：自动化 Agent 模拟用户真实设备视口，检测 DOM 元素在各断点下的实际物理像素尺寸，在构建阶段精准输出无浪费的响应式图片切片。",
        "so_what": "消灭前端工程师手工切图与压缩格式的重复体力劳动；从根源上改善移动端最大内容绘制（LCP）性能指标，让网页首屏加载如丝般顺滑。",
        "source": "github.com",
        "url": "https://github.com/andrea-bonacci/viewfit",
        "media": "https://iandaily.xyz/digest/2026-11-07-viewfit-8d43e5d91245.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "ldraw-mecha 让智能体推断乐高齿轮传动再做动画：机械约束下的物理级运动生成",
        "note": "三维结构化建模与智能体协作的精彩切片：Agent 自主解析乐高机械件（LDraw）的轴承连接与齿轮齿数比，严格根据角速度与机械咬合关系自动推导出运动动画仿真。",
        "so_what": "生成式 AI 从‘视觉表面像’向‘物理结构真’的关键跃升；为机械工程教学、玩具数字化设计与复杂多构件装配验证提供了低门槛的物理可控交互工具。",
        "source": "github.com",
        "url": "https://github.com/anteloc/ldraw-mecha/tree/v0.5.0",
        "media": "https://iandaily.xyz/digest/2026-11-07-ldraw-474ce55268e0.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "EasyRunCraft 将十三种流行编辑器无缝接入智能体：跨 IDE 的统一代码补全与调度通道",
        "note": "打破现代开发者编辑环境碎片化的利器：无论是 VS Code、JetBrains、Neovim 还是 Sublime，只需一个轻量守护协议，即可将所有编辑器的当前光标上下文统一桥接给后台 Agent。",
        "so_what": "开发者无需为了享受前沿智能体能力而被迫更换习惯数十年的编辑器配置；以协议标准化的力量对抗大厂工具链垄断，守住开发者的终端环境自主权。",
        "source": "easyruncraft.com",
        "url": "https://easyruncraft.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-easyrun-e3c541fecd5a.jpg",
        "pinned": False
    },
    {
        "category": "AI 协作",
        "title": "KeepPlain 让每一行提交代码都能追溯当时的代理对话：透明化上下文追溯版本系统",
        "note": "专为 AI 辅助编程时代研发的代码审阅卫士：将 Git Commit 与当时驱动 Agent 的自然语言会话、上下文文件快照建立双向绑定，在代码行间随时呼出当时的决策推演。",
        "so_what": "化解团队面对大量 AI 生成代码时的信任危机；让代码审查者秒级理解‘为什么 AI 会这样写架构’，从根本上杜绝遗忘当初意图造成的长期维护灾难。",
        "source": "keepplain.com",
        "url": "https://keepplain.com",
        "media": "https://iandaily.xyz/digest/2026-11-07-keepplain-195ba4a8a628.jpg",
        "pinned": False
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "Word Spies 让朋友与不同 AI 模型混队猜词：多模型人格与派对猜谜的独立站变现实验",
        "note": "巧妙将派对桌游‘行动代号’与大模型拟人化融合的独立作品：支持人类玩家与具有‘傲娇’、‘过度严谨’等特化人格的 AI 组队盲盒猜词，依靠趣味性引爆朋友圈自然传播。",
        "so_what": "大模型在泛娱乐轻量社交场景下的变现典范；用极低成本的 Prompt 人格编排为经典桌游注入无限变数，通过房间内购与挑战包实现稳定的被动收入闭环。",
        "source": "wordspies.com",
        "url": "https://wordspies.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-wordspies-9eaa864bf207.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Tell the Sky 让虚拟纸灯笼沿真实地球风向漂流：浪漫慢交互与情绪寄托微产品",
        "note": "反思快节奏社交疲劳的诗意慢产品：用户在虚拟孔明灯上写下心愿与秘密，系统调用实时全球气象风场 API，让灯笼在地球三维模型上随风漫游，与其他心灵偶遇。",
        "so_what": "用情绪价值建立极高壁垒的单兵产品设计；不贩卖焦虑、不追求即时刺激，用克制而温暖的美学仪式感打动全球用户，展现了数字空间的心灵治愈力量。",
        "source": "tellthesky.com",
        "url": "https://tellthesky.com",
        "media": "https://iandaily.xyz/digest/2026-11-07-sky-28e087df6cbd.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Dub Digger 为小众电子乐打造专属虚拟听音室：垂直黑胶与数字厂牌的利基索引",
        "note": "独立黑胶发烧友打造的利基音乐发现站：自动聚合全球地下 Dub/Techno 厂牌发布的试听小样，提供极简的唱盘界面与按节奏 BPM/调性筛选的纯净试听空间。",
        "so_what": "一人公司深耕垂直利基圈层的样本；无需与 Spotify 等流媒体巨头正面竞争，靠精准满足小众死忠乐迷的找歌挑黑胶刚需，通过 Bandcamp 导购分佣实现稳健运营。",
        "source": "dubdigger.com",
        "url": "https://dubdigger.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-dubdigger-217bcdbe23bd.jpg",
        "pinned": False
    },
    {
        "category": "一人公司",
        "title": "Math Paradoxes 让经典数学与概率悖论动态仿真跑一遍：极简教育科普网站的自传播",
        "note": "用代码消灭直觉谬误的交互式科普网站：无论是蒙提霍尔三门问题还是生日悖论，用户只需点击运行，系统即刻在数万次蒙特卡洛模拟中呈现概率收敛曲线。",
        "so_what": "知识科普工具化与自裂变的经典示范；把抽象死板的数学公式做成动手即见真章的交互图表，在 Reddit、Hacker News 上自发掀起热烈讨论，沉淀大量高粘性长尾流量。",
        "source": "mathparadoxes.com",
        "url": "https://mathparadoxes.com/en/",
        "media": "https://iandaily.xyz/digest/2026-11-07-math-bbbfb4d46238.jpg",
        "pinned": False
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Infinity 让单一回答长出多条对话分支：树状分支思维与多轮推演的画布交互革新",
        "note": "颠覆传统单一线性垂直聊天流的画布式交互：针对复杂问题的多角度推演，用户可直接在任意回答节点上分叉生长出多个并行的思考脉络，形成全景知识思维树。",
        "so_what": "为研究员与复杂决策者量身打造的高阶界面范式；消除了在同一个聊天窗口里反复‘回到上一题’的上下文污染与混乱，让复杂思考在多维空间中清晰展开。",
        "source": "infinitychat.app",
        "url": "https://infinitychat.app/",
        "media": "https://iandaily.xyz/digest/2026-11-07-infinity-24a98a1b26fc.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "DrawDock 把 Android 平板变成桌面电脑的原生批注层：低延迟跨设备微交互工具",
        "note": "打破操作系统壁垒的极简手写批注方案：无需安装沉重的投屏驱动，平板通过轻量局域网协议瞬时映射为桌面主屏的压感透明画板，支持在任何窗口上即时圈点圈画。",
        "so_what": "充分利用用户现有闲置硬件的轻量设计智慧；用极小的软件体积取代昂贵的专业数位屏，为远程会议协作与在线教学提供了行云流水般的低延迟批注体验。",
        "source": "github.com",
        "url": "https://github.com/MikeCer/DrawDock",
        "media": "https://iandaily.xyz/digest/2026-11-07-drawdock-0903904a51a8.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Rindraw 让矢量笔触在反复修改后仍保持优雅路径：设计师手绘与矢量对齐的轻量工具",
        "note": "专为追求极致平滑曲线的设计师打造的矢量画板：独创自适应曲率优化算法，在人类手部微小抖动下仍能自动收拢为控制点极少的贝塞尔曲线，反复拖拽亦不形变失真。",
        "so_what": "重塑数字手绘的手感与纯粹性；消灭了传统矢量工具节点繁琐、难以修改的痛点，让概念插画与图标设计在速度与严谨度之间达成完美平衡。",
        "source": "rindraw.com",
        "url": "https://rindraw.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-rindraw-4957a75f5518.jpg",
        "pinned": False
    },
    {
        "category": "产品设计",
        "title": "Checkered Chat 让二维码本身成为离线消息信使：去中心化近场通信的极客设计",
        "note": "完全脱离蜂窝网络与蓝牙配对的面对面加密通信新尝试：将多段加密文本动态编码为不断交替变换的高密度彩色二维码阵列，对方开启摄像头即可静默扫码解码。",
        "so_what": "反脆弱极端网络环境下的通信设计思考；在音乐节断网、野外灾备或高保密面对面交接场景下，用纯光学通道完成零足迹的信息安全递送。",
        "source": "honeywired.com",
        "url": "https://honeywired.com/apps/checkered-chat/",
        "media": "https://iandaily.xyz/digest/2026-11-07-checkered-cbb4c0e5cb58.jpg",
        "pinned": False
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Ondu 3D 打印褶边与棋盘格陶瓷灯具：复古拉夫领与参数化制造的奇幻重构",
        "note": "前沿 3D 打印技术与古典装饰艺术的奇妙碰撞：设计师将伊丽莎白时代的蕾丝拉夫领褶皱与包豪斯几何黑白棋盘格融合，通过参数化陶瓷打印呈现温润层叠光影。",
        "so_what": "参数化数字制造告别冰冷机械感的新审美范本；证明现代增材制造完全可以汲取历史服饰与手工艺养分，创造出兼具雕塑张力与生活温度的当代器物美学。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/design/3d-printed-ruffled-collars-top-checkerboard-lamps-vases-and-candle-holders-in-ondu-wonderland-gliese-design/",
        "media": "https://iandaily.xyz/digest/2026-11-07-ondu-5a9b941fe80d.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Carsten Höller 在墨西哥城高楼间架起四条巨型金属滑梯：城市公共空间的体验雕塑",
        "note": "当代先锋装置艺术家在都市钢铁丛林中的激进介入：四条镜面不锈钢巨型双螺旋滑梯穿透商业综合体玻璃天顶，市民可直接穿戴毛毡护垫飞驰而下体验失重快感。",
        "so_what": "公共艺术消解城市冷漠疏离感的震撼尝试；用纯粹的身体失重与多巴胺分泌唤醒成年人的童真，证明空间美学不仅是用来远观的，更是用来用身体深切体验的。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/art/carsten-holler-people-together-four-giant-slides-mexico-city-arte-abierto-polanco-soma-sordo-madaleno-antara/",
        "media": "https://iandaily.xyz/digest/2026-11-07-slides-86f141142034.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Maison Margiela 用牙签蘸墨手绘东京旗舰店故事：极简漫画背后的解构主义美学",
        "note": "先锋时尚品牌最具反叛精神的周年志：舍弃昂贵的铜版纸高清画册，邀请漫画家仅用几根普通木质牙签蘸浓墨，在粗糙手工纸上勾勒出东京惠比寿老店的时空流转。",
        "so_what": "向奢华繁复宣战的解构主义极简美学；证明打动人心的不是器材的奢靡与像素的高低，而是用最微不足道的日常媒介传达出无可挑剔的情感纯度与审美锐度。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/art/toothpick-drawn-manga-celebrates-maison-martin-margiela-tokyo-flagship-anniversary-takehito-moriizumi-ebisu/",
        "media": "https://iandaily.xyz/digest/2026-11-07-margiela-010bd4097895.jpg",
        "pinned": False
    },
    {
        "category": "审美提升",
        "title": "Demi Nguyen 将现代金融科技系统界面与古老活字档案并置：字体排印历史的当代转译",
        "note": "跨越数百年的字体排印视觉研究：将 16 世纪铅活字印刷规范与当代彭博终端、加密货币冷峻界面的信息层级排布并列剖析，解构数字流动背后的排版秩序演进。",
        "so_what": "给数字界面设计师提供深沉的历史认知纵深；让产品人明白现代 UI 里的每一处行高、字距与基线对齐，都是人类文明在信息组织与阅读效率上的漫长求索结晶。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/readers/demi-nguyen-corporate-branding-fintech-systems-typographic-archives/",
        "media": "https://iandaily.xyz/digest/2026-11-07-demi-cd04d3f779f1.jpg",
        "pinned": False
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Per Frame 按单张快门成本精算胶卷真实花销：利基社群工具的精准心智占领",
        "note": "精准击中胶片摄影爱好者钱包痛点的微工具：输入胶卷购买价、冲扫费用与相机格式，实时计算按下一次快门的真实单张成本，并与数码拍摄做长期 TCO 账单对比。",
        "so_what": "用一个极度尖锐的‘灵魂拷问’工具在小众圈层形成病毒式自发讨论；自然承接胶卷拼购与冲扫折扣服务，展现了一人工具低成本撬动精准高净值客群的打法。",
        "source": "perframe.app",
        "url": "https://perframe.app/",
        "media": "https://iandaily.xyz/digest/2026-11-07-perframe-f4447c351a4d.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "The Map Challenge 把网站展示接上全球地图积分打卡：游戏化自裂变外链与获客网络",
        "note": "充满趣味的全球站长外链联盟游戏：各个独立产品在世界地图上点亮自己的经纬度据点，通过用户打卡探索与解密互换流量积分，把冷冰冰的友情链接做成冒险游戏。",
        "so_what": "对抗枯燥 SEO 外链建设的增长黑客典范；用强烈的成就感与探险机制刺激独立开发者自发在社交媒体晒出地图坐标，以近乎零推广预算滚起全球反向链接飞轮。",
        "source": "themapchallenge.com",
        "url": "https://themapchallenge.com/",
        "media": "https://iandaily.xyz/digest/2026-11-07-mapchallenge-04a193ef1b6e.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "utmSnap 在外链生成前锁死渠道命名规范：数据归因治理从源头消灭混乱",
        "note": "解决增长运营团队数据埋点灾难的轻量工具：为全团队统一 UTM 标签拼写模板，强制大小写规范与渠道参数联动，杜绝一人一个拼写造成的跨渠道归因数据撕裂。",
        "so_what": "守护企业营销 ROI 分析底线的基础设施；用一个几十 KB 的浏览器插件在链接生成第一秒锁死规范，让后续数十万投放下沉数据的精准度与复盘效率提升数倍。",
        "source": "utmsnap.com",
        "url": "https://utmsnap.com",
        "media": "https://iandaily.xyz/digest/2026-11-07-utmsnap-c4c6b9de8934.jpg",
        "pinned": False
    },
    {
        "category": "产品营销",
        "title": "ReachMap 把冷启动推广渠道研究变成一份分步待办：出海独立产品的 GTM 极简路线图",
        "note": "出海产品营销小白的冷启动指南：输入产品受众与品类特征，系统自动生成涵盖 Product Hunt 发布节奏、垂直 Subreddit 破冰策略与精准 KOL 触达清单的行动待办流。",
        "so_what": "击碎独立开发者面对‘产品做好了却不知卖给谁’的获客恐慌；将庞大模糊的 GTM 市场战略具象化为每天打勾即可完成的确定性任务，极大提升冷启动执行力。",
        "source": "reachmap.app",
        "url": "https://reachmap.app/",
        "media": "https://iandaily.xyz/digest/2026-11-07-reachmap-e445797eedbb.jpg",
        "pinned": False
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "两名 00 后手搓 AI 短剧获 1.4 亿播放：高概念青春校园题材与工业化制作实录",
        "note": "震撼行业的微型制片团队神话：两名毫无传统影视背景的大学生，用 Midjourney 人设垫图配合可控动态生成模型，打造出高燃超能美高短剧，在 TikTok 狂揽过亿播放与高额商单。",
        "so_what": "视听创作平民化革命的铁证；证明好莱坞与传统影视工业的高昂壁垒已被击碎，敏锐抓取全球年轻受众的高概念审美，两台电脑即可匹敌传统制片厂牌的传播爆发力。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6481139.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "《反正你也没时间活》两天播放破亿：AI 漫剧不再卷纯画质、转向人性与情绪穿透",
        "note": "全网刷屏级爆款漫剧的深度复盘：摒弃刻意炫耀 4K 高保真皮肤纹理与光影的技术执念，直面都市打工人的生存窒息与精神内耗，凭借刀刀见血的台词与犀利分镜引爆全网共情。",
        "so_what": "AI 漫剧创作者的定海神针；敲响盲目堆砌渲染算力的警钟，证明画质永远只是载体，唯有穿透现实痛感的人性剖析与深刻共鸣，才能成就真正跨圈层的现象级作品。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6454826.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "从‘拍段子’到‘扛剧集’：头部博主转型短剧的工业化流水线与生产力重构",
        "note": "短视频网红转型连续叙事剧的系统化复盘：面对段子流量见顶与粉丝审美疲劳，创作者引入 AI 分镜脚本助手与虚拟场景搭建，将原本单条视频创作升级为百集连贯短剧工业流。",
        "so_what": "自媒体内容创作者抵御算法淘汰周期的关键跳板；通过连贯的人物命运与剧集钩子锁定粉丝长期生命周期价值，借助生成式管线实现视听资产的飞跃。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/operate/6490351.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "AI 漫剧",
        "title": "复杂游戏规则一键生成动态动画：Agent 驱动的 MG 动画生成与分镜自动化实操",
        "note": "教育科普与桌游规则可视化的创新管线：输入枯燥的长篇文字规则，智能体自动抽离角色身份逻辑，将其拆解为关键帧插画并驱动生成动态 MG 动画短片。",
        "so_what": "动态信息传递成本的断崖式下跌；让复杂概念与抽象规则秒变生动有趣的视觉动态语言，为游戏开发者、企业内部培训及儿童科普打开了无限的内容产能空间。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6490339.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《寒门帝师》120 集微短剧：古装权谋、寒门学子与帝王之师的成长因果链",
        "note": "硬核历史权谋短剧的结构范本：寒门书生虽无权无势，但凭借对科举弊案、漕运税银与藩王兵制死穴的洞若观火，在朝堂倾轧中扶持傀儡皇子步步登顶。",
        "so_what": "编剧因果链条严丝合缝的示范；拒绝低级的情绪嘴炮与机械降神，将底层逆袭建立在自洽而精密的政经制度博弈中，展现智斗剧情的高阶审美爽感。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2237",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《开局一座破道观》120 集微短剧：仙侠经营、收徒兴观与轻松反套路幽默",
        "note": "反内卷仙侠经营赛道的口碑剧作：掌门面对破败山门，不打打杀杀去争夺天材地宝，而是靠科学种茶、办修仙研学班与包装网红灵兽搞活经济，趣味横生。",
        "so_what": "用现代商业经营思维解构传统仙侠类型的创新心法；在观众对苦大仇深神魔大战麻木时，用轻松治愈的反差经营律动开辟出强粘性的追剧赛道。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2238",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《神医农妃惹不起》120 集微短剧：古装女频、神医医术与甜宠逆袭的爽感节拍",
        "note": "女频大女主短剧的节奏利刃：现代外科圣手穿越冷院弃妃，一手金针断生死，一手制药经商自立门户，面对刁难瞬间以专业医理反手打脸，毫不拖泥带水。",
        "so_what": "短剧黄金 3 秒抓人与即时反馈机制的教科书；将女主专业技能的降维打击与每一次情感冲突死死扣合，让观众在密集的因果反转中获得极度顺畅的追看体验。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2239",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "编剧技巧",
        "title": "《大宋第一皇商》120 集微短剧：古装经商、信息差商战与穿越致富的因果闭环",
        "note": "聚焦宋代繁华市井与金融博弈的商战短剧：现代投资经理利用交子纸币信用机制、期货平抑粮价与海外海贸分红，在汴京掀起一场波澜壮阔的资本大博弈。",
        "so_what": "短剧商战题材‘真商战’与‘假过家家’的分水岭；通过扎实的经济学常识与历史细节支撑每一次财富翻盘，带给受众身临其境的商界智力碾压享受。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2240",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "企业 AI 转型落不了地？一张清单说清组织侧 7 步核心路径与产品边界设计",
        "note": "资深数字化操盘手总结的企业智能化避坑全景图：从高频刚需业务盘点、数据治理断点修复、试点沙箱搭建到跨部门协作利益重分配，拆解落地全生命周期。",
        "so_what": "产品经理从‘单点功能思维’跨越至‘组织变革中枢’的实战地图；帮助 PM 在面对管理层宏大愿景时保持清醒，用务实可量化的步骤守住项目交付生命线。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/pd/6490135.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "打通企业应用孤岛：多办公 App 统一互联架构与工作流智能体设计",
        "note": "破解大厂与中大型企业软件林立割裂痛点的架构实操：通过标准化统一上下文协议，将即时沟通、文档协同、项目管理与流程审批融合成一个随时响应的全局 Agent。",
        "so_what": "企业中台与协同办公产品的终极形态推演；不再逼迫员工在五六个独立软件间做人形黏合剂，让智能体成为统一的业务入口，根本性重构组织协同体验。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6490335.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "AI 时代产品经理人才面试逻辑重构：从功能画图转向系统边界与不确定性把控",
        "note": "一线大厂团队负责人的最新选拔心法：不再考核 PRD 写作与交互原型绘制速度，转而重点考察候选人对模型概率幻觉的容错架构设计、数据飞轮认知与跨学科权衡能力。",
        "so_what": "产品经理职业转型的重要警钟；单纯依靠功能堆砌与原型排版的 PM 正在快速贬值，唯有深谙系统不确定性治理与商业价值落地的复合型产品人才能立于不败之地。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/class/6490194.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "产品经理",
        "title": "把多智能体连成网状协作：跨系统 Agent 协议互联与调度产品架构实践",
        "note": "开源社区与前沿产研团队的多智能体互通实践：定义轻量级跨系统 Agent 通信标准，支持不同开发者打造的垂类代理自动发现、任务协商竞标与结果校验交接。",
        "so_what": "从‘单一巨型 Agent 孤军奋战’迈向‘智能体社会分工网络’的关键一步；产品经理必须学会设计多 Agent 之间的博弈规则与利益协同机制，掌控更大维度的系统智能。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6490031.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    }
]

def build():
    frontmatter = {
        "date": "2026-11-07",
        "title": "11 月 07 日 · 垂直特化与意图分流：从单体全能神话走向精细协作矩阵",
        "highlights": "全网 9 大领域 36 篇高密度精选：Meta 将专用模型送进场景矩阵、OpenRouter 推出 Auto Code 专属路由、两名 00 后手搓 AI 短剧获 1.4 亿播放、企业 AI 转型组织侧 7 步路线图、《反正你也没时间活》从卷画质转向卷人性。",
        "draft": False,
        "epigraph": "当所有人都在期待一个通晓万物的超级单体大模型时，工业界最前沿却在全力把大模型切成无数颗垂直小齿轮；当内容消费对千篇一律的精致画质脱敏时，刺痛现实的情绪核弹才刚刚在微短剧里引爆。",
        "lead": "11 月 7 日，大模型应用正迎来一次深刻的“分工大转向”。在算力与模型底座端，Meta 正式将场景特化专用小模型引入 Muse 与核心产品线，OpenRouter 更是单独设立了针对编程场景的 Auto Code 自动分流路由，这标志着靠单个庞大模型通吃所有意图的旧时代彻底终结，专业的事由专业小模型协同分包成为行业共识；在视听与内容生产端，两名 00 后凭借手搓 AI 短剧斩获 1.4 亿播放，爆款短剧《反正你也没时间活》在两天内播放破亿，行业赫然发现纯粹比拼画质精细度的军备竞赛已经见顶，能够穿透现代人脆弱防御的人性洞察与情绪共振才是决胜盘；在一人公司与产品设计端，独立创作者们将注意力收缩至极致利基——从乐高物理齿轮传动推演、多模型混战猜词到按单张快门成本精算胶卷，用极轻的产品构型抢占用户心智。不再追求假大空的宏大叙事，把每一个针尖大小的真实痛点扎透，这就是今天创新的硬核底色。",
        "scene": "「为什么要把用户的一个请求在后台拆给三个不同的小模型来回答？」「因为在真实的产线里，全能的通才往往样样通样样松，而三个各怀绝技的特种兵配合，不仅速度快十倍、成本低一个数量级，最重要的是，他们永远不会在自己专业的领域犯低级错误。」",
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

今天的 36 个切片为我们揭示了一个朴素却极为有力的事实——‘特化带来效率，共鸣带来溢价’。无论 Meta 把大模型切碎成小模型跑分工，还是 00 后不再卷 4K 炫目贴图、转而在短剧里直击都市生存的窒息痛点，大家都在放弃空洞的技术狂欢，回归人性的真实温度与工程的效率本质。不必妄图成为无所不知的巨无霸，在你的细分领域里做一把锋利不可替代的手术刀，你就拥有了穿越周期的最大确定性。"""

    full_md = f"---\n{yaml_str}---\n\n{closing_text}\n"

    target_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-07.md"
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
