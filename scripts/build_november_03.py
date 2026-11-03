# -*- coding: utf-8 -*-
import json
import yaml
import os

items = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "权重编程实验让大模型直接改小模型参数：神经网络权重空间可微编辑",
        "note": "跨模型元学习与参数合成的前沿探索：大语言模型不再仅输出自然语言文本，而是直接预测并微调小模型的权重矩阵切片，实现动态超参自适应。",
        "so_what": "颠覆传统海量梯度反向传播训练范式；让大模型充当“神经架构雕刻师”，在推理时按需为端侧极小模型注入针对性能力，开辟参数级可微编程新路径。",
        "source": "rikiyat.github.io",
        "url": "https://rikiyat.github.io/blog/weight-space-programming/",
        "media": "https://iandaily.xyz/digest/2026-11-03-weightspace-15d0f144ae9f.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "tinywmcraft 把小型世界模型放到手机上玩：端侧神经游戏引擎",
        "note": "端侧轻量化世界模型的突破实践：将体素游戏物理规律与渲染状态完全压缩进几兆字节的离线神经权重中，手机本地毫秒级推演交互环境。",
        "so_what": "游戏物理引擎与渲染架构的底层质变；不依赖传统图形光栅化管线，直接依靠世界模型自回归预测下一帧物理状态，为移动端具身智能提供极佳测试场。",
        "source": "maharishiva.github.io",
        "url": "https://maharishiva.github.io/tinywmcraft/",
        "media": "https://iandaily.xyz/digest/2026-11-03-tinywm-1d3952b69294.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "LiteMoE 把大模型推理拆到一千六百行：极简 Mixture of Experts 交互可视化",
        "note": "混合专家架构算法透明化的教学杰作：仅用 1600 行极简核心代码完整复现 MoE 路由分发、Top-k 门控与专家权重加权计算全流程，配备动态可视化看板。",
        "so_what": "撕开当代主流大模型神秘黑箱的极佳利器；帮助工程师与研究者抛开厚重框架的抽象包裹，直接在单步执行中直观顿悟稀疏激活计算的本质机理。",
        "source": "zhulinsen.github.io",
        "url": "https://zhulinsen.github.io/LiteMoE/visualizer/?lang=zh",
        "media": "https://iandaily.xyz/digest/2026-11-03-litemoe-b29e44ae5899.jpg",
        "pinned": False
    },
    {
        "category": "AI 资讯",
        "title": "OpenAI 用内部激活监测模型正在做什么：表征工程对齐监控前沿",
        "note": "大模型安全对齐与表征工程的核心突破：在模型隐藏层挂载轻量激活分类探针，实时检测推演过程中的越狱倾向、欺骗伪装与意图漂移。",
        "so_what": "从“黑箱盲信后置拦截”转向“神经内部态实时监控”的里程碑；为高可靠性高安全性 AI 系统的工业化落地提供了具备可解释性的白盒审计方案。",
        "source": "alignment.openai.com",
        "url": "https://alignment.openai.com/training-activation-classifiers/",
        "media": "https://iandaily.xyz/digest/2026-11-03-probes-a6c6b3b1e3c7.jpg",
        "pinned": False
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "Deedglass 比对代理说法和数据库实变：智能体执行真实因果对账",
        "note": "企业级智能体防忽悠审计中间件：自动截获 Agent 声称的“已完成修改”答复，严格与底层数据库和物理文件系统的真实 Commit 变更逐行比对。",
        "so_what": "消灭智能体“嘴上答应很完美、实际啥都没改好”的幻觉硬伤；用物理落盘证据作为唯一的验收标准，让 AI 协作在严谨工程环境中真正立得住脚。",
        "source": "deedglass.com",
        "url": "https://deedglass.com/play",
        "media": "https://iandaily.xyz/digest/2026-11-03-deedglass-825d5a75bc05.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "Intent-lens 在执行前翻译代理的工具调用：人类可读的意图透镜插件",
        "note": "多步骤智能体调用的白话翻译透镜：在危险命令执行前，将晦涩嵌套的 JSON 参数与 Shell 脚本自动翻译为人类一目了然的业务意图和潜在破坏评估。",
        "so_what": "关键生产环境人机交接的防呆安全阀；人类审阅者无需在几百行机器代码里人工找坑，一眼看懂 Agent 的动机与影响范围，大幅降低误批风险。",
        "source": "github.com",
        "url": "https://github.com/Dhananjay-JSR/claude-mods/tree/main/plugins/intent-lens",
        "media": "https://iandaily.xyz/digest/2026-11-03-intent-c2e0418ae3f9.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "ArchDocs 把设计计划和已做改动并排看：智能体架构设计与代码一致性看板",
        "note": "系统架构防腐化的结对利器：左侧展示最初制定的软件架构方案与边界约束，右侧实时并排渲染 Agent 产生的实际 PR，红色高亮偏离架构蓝图的危险改动。",
        "so_what": "捍卫系统长期可维护性的守护者；防止智能体在局部单点任务中追求短平快而破坏全局系统契约，确保每一次迭代都在顶层设计的正轨上演进。",
        "source": "archdocs.io",
        "url": "https://archdocs.io",
        "media": "https://iandaily.xyz/digest/2026-11-03-archdocs-e9e83adce14c.jpg",
        "pinned": False
    },
    {
        "category": "AI 协作",
        "title": "Smalt 让双手敲代码时也能指挥代理：语音与键盘并行结对协作",
        "note": "重塑结对编程输入通道的高效工具：开发者双手继续在 IDE 里敲核心逻辑，通过语音对后台 Agent 实时分派查错、写单测与查文档等旁路支持任务。",
        "so_what": "打破单线程工作流的认知扩容；双轨并行让脑力始终集中在最核心的创造性构思上，将零碎琐碎的机械劳动无缝异步流转出去，大幅提升编程心流质量。",
        "source": "getsmalt.com",
        "url": "https://getsmalt.com/",
        "media": "https://iandaily.xyz/digest/2026-11-03-smalt-1dab00f7b305.jpg",
        "pinned": False
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "八美元咖啡把线上感谢送进信箱：开源维护者实体明信片赞助平台",
        "note": "温情脉脉的实体赞助微型平台：赞助者在线支付 8 美元，平台负责将感谢信与定制纪念明信片物理寄送到全球开源维护者的真实信箱中，极富人情味。",
        "so_what": "微型商业中情感连接击穿数字冷漠的经典范例；在纯数字打赏日益同质化的今天，用一张跨越重洋的纸质明信片唤醒共鸣，创造极高黏性与精神归属感。",
        "source": "maintainers.coffee",
        "url": "https://maintainers.coffee/",
        "media": "https://iandaily.xyz/digest/2026-11-03-coffee-092d29abc508.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Devpush 让自己的服务器接上推送部署：极轻量单机 Git 钩子自动化",
        "note": "单兵全栈开发者的反复杂 CI/CD 利器：摒弃复杂的 Kubernetes 和云端昂贵构建集群，只需在个人 VPS 上一键配置轻量 Git 钩子，Git push 瞬间自动拉起生产部署。",
        "so_what": "回归单机极简哲学的降本典范；对于一人公司和微型项目而言，过度设计的基础设施就是负债，保持最纯粹的单机可控性才能省下大笔开销并高速迭代。",
        "source": "devpu.sh",
        "url": "https://devpu.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-03-devpush-1c07a073555f.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Gridmino 用免费日题带出小额年订阅：几何拼图微型 SaaS 变现样本",
        "note": "独立游戏与益智工具的变现闭环：每天提供一道极具巧思的免费几何多米诺拼图题形成高频打开习惯，结合小额年费解锁历史题库与解法剖析，跑通健康现金流。",
        "so_what": "以轻量级内容飞轮撬动稳定被动收入的典范；无需海量投放买量，靠极致打磨的微型智力乐趣锁死忠实核心用户群，展现单兵开发者的长长久久盈利哲学。",
        "source": "gridmino.com",
        "url": "https://gridmino.com/",
        "media": "https://iandaily.xyz/digest/2026-11-03-gridmino-36b1a95f75ea.jpg",
        "pinned": False
    },
    {
        "category": "一人公司",
        "title": "CampPowerCalc 把露营用电算到每件设备：垂直利基用电测算工具站",
        "note": "户外与离网生活垂直赛道的信息差工具：用户输入车载冰箱、探照灯、无人机等设备功率与时长，系统一键精准推导所需储能电源容量与太阳能板规格。",
        "so_what": "挖掘特定生活方式刚需痛点的利基变现教科书；在专业电商导购与佣金返利链路中充当决策枢纽，以极高转化率实现小流量大回报的个人生意。",
        "source": "camppowercalc.com",
        "url": "https://camppowercalc.com/en/calculator/battery-runtime/",
        "media": "https://iandaily.xyz/digest/2026-11-03-camppower-d8ca64ead1c1.jpg",
        "pinned": False
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Affinity 把绘图、修图和排版搬上 iPad：无订阅买断制桌面级移动套件",
        "note": "专业级桌面软件向触控平板迁移的封神答卷：拒绝功能阉割与云端订阅绑架，一次买断即可在 iPad 上获得与桌面版完全一致的高性能矢量与像素排版手感。",
        "so_what": "对抗 SaaS 订阅泛滥、坚守专业创作者主权的重磅胜利；证明移动端绝不只是信息消费玩具，只要在触控手势与界面密度上深耕，完全能承载高强度工业级交付。",
        "source": "affinity.studio",
        "url": "https://www.affinity.studio/ipad-app",
        "media": "https://iandaily.xyz/digest/2026-11-03-affinity-57efab71b002.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Cross Lyrics 让 iPad 跟着电脑唱：跨设备伴侣屏幕的纯粹微交互",
        "note": "多设备生态协同的极简点睛之作：主电脑播放流媒体音乐，闲置的 iPad 自动变身为全屏动态歌词海报伴侣屏，零配置蓝牙自愈连接，界面如黑胶封套般雅致。",
        "so_what": "用最小摩擦唤醒闲置硬件价值的微创新典范；不搞花哨的社交与推荐算法，专注打磨“静止陈列美感与即时同步”单一场景，带来极其愉悦的生活仪式感。",
        "source": "crosslyrics.com",
        "url": "https://crosslyrics.com/",
        "media": "https://iandaily.xyz/digest/2026-11-03-crosslyrics-cb9e67cbc2b8.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Sizewise 把不同品牌的尺码缝成标签：消除网购服装尺码混乱的极简设计",
        "note": "解决全球服装网购世纪痛点的轻量解决方案：将各品牌的抽象 S/M/L 尺码基于真实身材尺寸重新归一化，生成一张直观的对比刻度标签，彻底消灭试错成本。",
        "so_what": "用信息设计重塑复杂商业混沌的典型示范；通过优雅的视觉标尺化繁为简，极大降低消费者的决策摩擦与商家的退换货损耗，兼具商业与人本价值。",
        "source": "franzonlabs.se",
        "url": "https://sizewise.franzonlabs.se",
        "media": "https://iandaily.xyz/digest/2026-11-03-sizewise-01513c107b21.jpg",
        "pinned": False
    },
    {
        "category": "产品设计",
        "title": "Meeple Scan 拍一层桌游就能查评分：移动端即拍即识的桌游选品助手",
        "note": "面向线下聚会与桌游吧玩家的扫码体验革新：随手拍下桌游包装盒封面，毫秒级比对 BGG 全球数据库，直接浮现难易度、重度分与玩家真实评价榜单。",
        "so_what": "计算机视觉与垂直小众爱好圈层深度结合的精巧产品；消除了线下选游时的犹豫与踩雷焦虑，让数字情报即时赋能实体生活体验。",
        "source": "meeple-scan.com",
        "url": "https://meeple-scan.com/?ref=hn",
        "media": "https://iandaily.xyz/digest/2026-11-03-meeple-15b94f85c4f9.jpg",
        "pinned": False
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "废弃旧皮椅拆解为九件日常器物：解构主义与材料循环的手工诗学",
        "note": "工业旧物改造与先锋产品哲学的重磅实验：将一张被废弃的磨损真皮旧扶手椅彻底剖解，椅背、五金与填充物被重构为九件质朴而耐用的现代家居日常器物。",
        "so_what": "打破快消时代丢弃文化的可持续设计宣言；岁月留在皮革上的褶皱与铜绿成为独一无二的审美印记，用精湛手工艺赋予工业残骸深沉的生命尊严。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/design/discarded-leather-armchair-nine-functional-domestic-objects-jan-micha-gamer/",
        "media": "https://iandaily.xyz/digest/2026-11-03-armchair-cb8f2e328540.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Neri Oxman 让细菌在蚕丝上慢慢生长出颜色：生物色素与活体织物的先锋实验",
        "note": "跨学科材料科学与自然美学的巅峰对话：利用基因工程改造的有色微生物，在天然无染色蚕丝织物表面缓慢新陈代谢繁衍，随时间推移晕染出不可复制的生命图腾。",
        "so_what": "告别高污染化学印染的生态美学突围；让物质本身拥有呼吸与生长周期，将时间作为设计的一环，开辟了活体织物与仿生艺术的壮阔前沿。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/11/02/neri-oxman-vigils-fabric-silk-pigment/",
        "media": "https://iandaily.xyz/digest/2026-11-03-vigils-1ada14619c65.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Corkinho 用整块软木围出冥想静室：原生态多孔材料雕琢的感官庇护所",
        "note": "葡萄牙原生态软木在空间营造中的极致探索：以未经深度加工的巨幅厚实软木树皮筑起隔绝外界喧嚣的冥想小室，柔和吸收一切杂音，空气中弥漫着清新的树脂幽香。",
        "so_what": "多感官联觉在建筑空间的克制落地；不依赖繁复的装饰构件，单凭纯粹材质自带的吸音物理属性与自然肌理，便能瞬间抚平现代人躁动的神经。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/11/02/still-room-casa-no-tempo-corkinho/",
        "media": "https://iandaily.xyz/digest/2026-11-03-stillroom-9cc805629e7f.jpg",
        "pinned": False
    },
    {
        "category": "审美提升",
        "title": "瑞士邮政新定制字体：在严谨现代主义网格中注入温暖人性的字形细节",
        "note": "国家级公共形象与字体排印的精细迭代：在恪守瑞士国际主义平面风格严谨骨架的同时，在笔画交接处微调切角并融入柔和曲率，极大提升了跨媒介易读性与亲和力。",
        "so_what": "在理性工业秩序与人文温度之间达成精妙平衡；字体是公共生活最隐秘的视觉基础设施，毫厘之间的弧度微调，便能重塑整个国家公共服务的精神风貌。",
        "source": "creativeboom.com",
        "url": "https://www.creativeboom.com/work/swiss-typefaces-crafts-a-warmer-friendlier-custom-font-for-swiss-post/",
        "media": "https://iandaily.xyz/digest/2026-11-03-swisspost-a84041dff56e.jpg",
        "pinned": False
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "AtelierLab 把图纸交付和收款接成一步：垂直独立设计工作室的闭环交付 SaaS",
        "note": "攻破建筑与工业设计尾款难收顽疾的精巧方案：将高清矢量图纸与 3D 渲染成果放在受保护的网页端预览，客户完成在线结算的瞬间自动解锁源文件下载权限。",
        "so_what": "把商业因果关系硬编码进交付流程的教科书；用不可逆的技术交付契约彻底替代传统催款扯皮，捍卫独立创作者的财务安全与职业尊严。",
        "source": "atelierlab.in",
        "url": "https://www.atelierlab.in",
        "media": "https://iandaily.xyz/digest/2026-11-03-atelier-7eefa2985277.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "Trustmebro 把社区真实评价拆回具体讨论上下文：反虚假水军的社交证据罗盘",
        "note": "破解好评刷榜泛滥的独立舆情产品：自动抓取 Hacker News、Reddit 等硬核极客社区在历史真实长帖中的用户讨论切片，保留上下文争论，严禁脱水提纯与赞助操控。",
        "so_what": "真诚与真实社群背书正在成为最顶级的营销杠杆；消费者厌倦了包装完美的五星好评，展示不加滤镜的真实争辩与缺点，反而能在高端客户群体中建立强大信任。",
        "source": "trustmebro.reviews",
        "url": "https://www.trustmebro.reviews/r/hackernews",
        "media": "https://iandaily.xyz/digest/2026-11-03-trustmebro-5dc0c447107b.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "Shortener.dev 把链接追踪放进浏览器侧边栏：单兵出海敏捷投放利器",
        "note": "出海增长黑客的高频短链追踪利器：常驻浏览器侧边栏，支持一键为推特、邮件及 Discord 推广文案生成带 UTM 标签的轻量追踪短链，实时反馈点击与转化漏斗。",
        "so_what": "缩短营销动作与数据反馈回路的关键微工具；把繁琐的数据埋点嵌入日常发帖动作中，让每一次出海推广尝试都能在分钟级内得到归因验证。",
        "source": "shortener.dev",
        "url": "https://shortener.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-03-shortener-1247f2855210.jpg",
        "pinned": False
    },
    {
        "category": "产品营销",
        "title": "HackerBlogs 从分享历史反查高质量读者常看谁：极客社群自然增长发现引擎",
        "note": "基于程序员真实书签与转载链路的反向内容雷达：不靠算法推荐，纯靠高段位工程师历史分享数据的拓扑聚类，精准找到在技术圈具备超强号召力的长尾 KOL。",
        "so_what": "ToD（面向开发者）产品冷启动的精准靶向雷达；避开昂贵的泛科技媒体硬广，精准联络在小众圈层拥有绝对话语权的技术博主，实现以一当百的口碑裂变。",
        "source": "hackerblogs.app",
        "url": "https://hackerblogs.app",
        "media": "https://iandaily.xyz/digest/2026-11-03-hackerblogs-be9d6c8d22a8.jpg",
        "pinned": False
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "千亿市场之后短剧生意开始变了：从狂野买量收割走向精品内容与私域生态",
        "note": "微短剧行业从粗放暴利步入精细化洗牌的深度复盘：深入拆解单纯依赖高昂投流买量模式的全面倒挂，揭示头部制片方转战精品长效 IP 与微信小程序私域沉淀的新打法。",
        "so_what": "告别虚荣流量泡沫的生死转折点；短剧的竞争正式从“谁能抢到便宜流量”蜕变为“谁能以最低成本工业化稳定生产高水准故事并留住忠实付费观众”。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6487982.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "大厂抢夺大众时间背后谁在买单：竖屏漫剧注意力经济的商业真相与暗流",
        "note": "透视互联网巨头在用户停留时长维度的激烈内卷：剖析各大短视频与信息流平台为何不惜一切代价押注竖屏短剧，以及其在算法分发与变现收割背后的深层商业逻辑。",
        "so_what": "内容从业者理解平台扶持风向的战略地图；顺应平台对用户黏性与时长的饥渴，但绝不能沦为平台的纯买量工具人，必须在流量洪流中建立自有创作者品牌与私域底盘。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6487971.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "打开红果短剧看懂大众生活：下沉市场情感代偿与爆款漫剧的叙事底层逻辑",
        "note": "爆款下沉微短剧的社会学与大众心理剖析：从婆媳和解、小人物逆袭到草根互助，拆解为什么貌似狗血的情节能够精准击中上亿普通人内心最隐秘的情感软肋。",
        "so_what": "爆款漫剧剧作的核心底层逻辑；技术工具只是骨架，对真实普通人生活艰辛的深切共情与情绪精准代偿，才是撬动亿级完播与转化的唯一灵丹妙药。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487957.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "AI 漫剧",
        "title": "“不塌房”只是AI明星的谎言：虚拟演员人设信任与漫剧制作团队的合规防线",
        "note": "生成式视听虚拟角色商业化的冷峻反思：剖析业内以为“AI 虚拟人永不塌房”的天真幻想，指出声音侵权、模型面部越界与版权纠纷等新型风险正在给制作方带来灭顶之灾。",
        "so_what": "微短剧与漫剧工业化必须严守的法律红线；拥抱生成式技术绝不能忽视肖像权与训练数据溯源合规，筑牢防侵权合规护城河是长期资产变现的基石。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487901.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《归墟坐标》120 集硬科幻微短剧：黑洞视界边缘的时空悬疑与因果闭环构建",
        "note": "高概念硬科幻短剧的因果链编织黄金法则：探险队在接近黑洞引力视界时遭遇时间膨胀与意识孪生危机，以紧凑的 60 秒为节拍设置物理规律与时空闭环悬疑。",
        "so_what": "科幻微短剧进军高智力交锋的典范；拒绝粗劣的特效堆砌，将冷酷真实的相对论物理常识包裹进惊心动魄的人性求生博弈中，展现高级的剧作质感。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2221",
        "media": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《镜界殖民》120 集硬科幻微短剧：平行宇宙资源倾轧与双重身份对抗节拍",
        "note": "平行时空设定下的戏剧张力强化范式：主宇宙面临枯竭危机，主角潜入平行时空却发现另一个自甘堕落的自己竟掌控着核心资源密码，展开双雄智斗反转。",
        "so_what": "一人分饰两角、双重身份对抗的经典冲突升级法；在自我认同撕裂与宏大生存伦理抉择中反复推高情绪弧线，给受众带来强烈的心理冲击与哲思余味。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2222",
        "media": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《孤独星球》120 集都市情感微短剧：都市孤岛心理投射与治愈叙事弧线编排",
        "note": "现代都市题材微短剧的情绪解压技巧：失业青年与失明调音师在狭窄天台相遇，通过声音探索城市隐秘生机，以细腻克制的日常生活片段抚平大众精神内耗。",
        "so_what": "短剧跳脱狗血打脸、开辟治愈赛道的情绪密码；用接地气的微小善意与克制的生活细节对抗大都市的冰冷疏离，给身心俱疲的年轻受众提供深度情绪抚慰。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2223",
        "media": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "编剧技巧",
        "title": "《地府快递员》120 集灵异喜剧微短剧：现代职场痛点与荒诞阴阳因果反转技巧",
        "note": "反套路爆笑职场微短剧的设定魔术：平凡骑手误打误撞接下阴阳两界急件外卖业务，用应对苛刻差评、算法考核与难缠客户的现代常识整顿古代地府规矩。",
        "so_what": "将大众普遍共鸣的打工人现实痛点嫁接进荒诞奇幻外壳的解构艺术；用密集的职场自嘲与戏剧反转释放现实压力，兼具极强喜剧效果与社会讽刺力。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2224",
        "media": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "Muse 深度产品拆解：把 Agent 做成一台全权限云电脑后的系统级架构取舍",
        "note": "前沿个人智能体标杆产品的全景解构：深入剖析其放弃传统狭窄对话框、直接为 Agent 分配专属完整云端虚拟机与浏览器沙箱的架构演进得失与安全治理之道。",
        "so_what": "产品经理理解下一代 Agent 交互终局的绝佳范本；从单纯的文本中介走向真正的系统级执行中介，如何平衡算力成本、操作时延与数据安全是核心考卷。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/evaluating/6487122.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "企业级 Agent 赛道分水岭已至：从通用 Bot 玩具走向深度业务工作台的残酷淘汰",
        "note": "企业级大模型应用搭建平台的残酷洗牌复盘：同天官宣 WorkBuddy 狂飙与轻量企业 Bot 关停背后，揭示单纯聊天 Bot 正在被无情抛弃，深度嵌入审批与鉴权的系统才是未来。",
        "so_what": "B 端产品经理从虚荣狂热回归商业本质的清醒针；企业采购的从来不是会调侃的聊天机器人，而是能实打实顶替岗位繁重脏活、具备可追溯性的业务工作流中枢。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487641.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "让 Super-agent 真正成为团队同事：LobeHub 组织协同实验与权限边界设计",
        "note": "多角色智能体融入人类研发团队的组织学前沿探索：探讨如何像管理人力资源一样为不同的 Agent 分配明确的职务责任、工作权限沙箱与代码复核晋级通道。",
        "so_what": "高级产品人重构人机协作组织的架构思维；把智能体看作具备特定技能与偏见的初级员工，用严密的团队契约与流程规约加以约束，才能发挥其最大的集体智能。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487620.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "产品经理",
        "title": "企业私有化 Agent 平台选型指南：开源部署陷阱、安全沙箱与运维成本全景复盘",
        "note": "企业拥抱大模型私有化落地的全面排雷手册：深度剖析开源大模型平台在长期版本迭代断更、权限控制漏洞、多卡推理资源死锁与冷启动开销中的隐形巨额负债。",
        "so_what": "产品与技术决策者必须掌握的 TCO（全周期总拥有成本）算盘；不仅要看开源的免费代码，更要算清算力折旧、安全兜底与业务定制的隐形账单，拒绝盲目跟风踩坑。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488040.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    }
]

def build():
    frontmatter = {
        "date": "2026-11-03",
        "title": "11 月 03 日 · 真实物理因果对账与企业级退潮清算：从通用神话破灭到垂直业务深潜",
        "highlights": "全网 9 大领域 36 篇高密度精选：权重编程让大模型直接修改小模型参数、Deedglass 严密比对 Agent 说法与数据库真实落盘、短剧迈过千亿规模后的狂野退潮与私域变现、Muse 把智能体做成云电脑后的架构得失、Affinity 桌面套件无订阅搬上 iPad。",
        "draft": False,
        "epigraph": "商业不会因为你接入了最酷的模型就对你网开一面；真正能活下来的企业级应用，靠的从来不是天花乱坠的 Demo，而是在千头万绪的真实脏业务里，能一笔一笔核对清楚每一行数据库落盘与每一分账单流水。",
        "lead": "11 月 3 日，随着行业从狂热的概念炒作中步入冷静期，一场关于“真实因果与确定性”的深刻清算正在全链路展开。在学术与算力前沿，极客们开始尝试用权重编程直接操控模型参数，并用激活监控探针实时窥视大模型的内部意图；在智能体落地战场，Deedglass 和 ArchDocs 正在逼迫 Agent 交代真实数据库变更，企业级工作台的分水岭已至——通用聊天 Bot 批量退场，能融入深层业务审批、承担系统风险的垂直产品接管主场；在视听领域，短剧破千亿后的买量暴利幻象正在破灭，团队全面转入私域高复购与低成本视听工业化；而在单兵工具与现代设计前线，买断制、自带存储（BYOS）与纯端侧轻量工具以清醒的姿态持续收割长尾口碑。泡沫退去，泥泞中唯有脚踏实地的深潜者才能铸就不可动摇的商业壁垒。",
        "scene": "「领导天天追问我接入了 AI 之后，业务到底提效了多少百分比，我拿什么向他证明？」「别再拿‘生成了多少篇文案’糊弄人了。去拿 Deedglass 对账单，告诉他数据库里哪几条关键因果是智能体搞定的、哪几个报错被沙箱拦下了，拿出能 audited 的硬数据，他才不敢质疑你。」",
        "cover": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80",
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

走过 11 月的头几天，我们更加清晰地感知到行业重心的位移——技术自嗨的泡沫被挤压殆尽，对真实世界物理账单与因果关系的尊重全面回归。无论是一人公司把录屏与露营算电做成零服务器成本的小而美生意，还是设计师在 iPad 上坚持买断制对抗泛滥的 SaaS 订阅，都证明了真诚、克制与硬核落地永远是商业社会最稀缺的硬通货。别在虚无的估值神话里打转，沉下心去，把每一个具体用户的真实痛点做到无可挑剔。"""

    full_md = f"---\n{yaml_str}---\n\n{closing_text}\n"

    target_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-03.md"
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
