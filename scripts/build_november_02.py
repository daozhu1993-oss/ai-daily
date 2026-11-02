# -*- coding: utf-8 -*-
import json
import yaml
import os

items = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Memdoor 公开小模型协作解题记录：轻量智能体集群决策实录",
        "note": "轻量化智能体协同推演的透明工程样本：详细公开多个小参数模型在分工拆解、交叉质疑与聚合表决中的完整推理轨迹，探索端侧集群解题极限。",
        "so_what": "打破单体超大模型垄断复杂推理的迷思；用针对性微调的轻量模型组建专家委员会，能在极低算力成本下实现媲美顶级大模型的复杂逻辑求解。",
        "source": "github.com",
        "url": "https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve",
        "media": "https://iandaily.xyz/digest/2026-11-02-memdoor-f6592e79c88f.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "RE-USE 降噪演示在浏览器本地运行：纯端侧音频智能修复",
        "note": "WebAssembly 与纯前端神经音频处理前沿：将高精度语音降噪与回声消除模型编译进浏览器本地内存，在毫秒级内完成实时环境杂音过滤。",
        "so_what": "音频智能化向端侧设备全面下沉的标志；无需将用户私密语音上传至云端服务器，在本地以零网络延迟和零隐私风险完成音频流实时纯净重构。",
        "source": "geronimo-labs.com",
        "url": "https://re-use-demo.geronimo-labs.com",
        "media": "https://iandaily.xyz/digest/2026-11-02-reuse-eae1576a30df.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "Mwmbl 开放搜索索引完整快照：去中心化去算法霸权的公共网络索引",
        "note": "非营利开源搜索引擎的里程碑发布：公开发布经过清洗的高质量全网网页结构化索引数据转储包，坚决剔除 SEO 垃圾农场与广告联盟噪声。",
        "so_what": "反抗中心化大厂算法垄断的珍贵公共基础设施；为独立开发者与学术研究者提供不受商业操纵的干净检索底座，守护开放互联网知识自由。",
        "source": "mwmbl.org",
        "url": "https://mwmbl.org/dumps",
        "media": "https://iandaily.xyz/digest/2026-11-02-mwmbl-3e2cfe75a036.jpg",
        "pinned": False
    },
    {
        "category": "AI 资讯",
        "title": "Hushkey 实验用无声口型输入文字：视觉言语识别前沿探索",
        "note": "人机交互输入维度的无声革命：通过轻量摄像头实时捕获面部肌肉与嘴唇运动轨迹，将无声默念精准解码为文本输入，解决公共场合私密输入难题。",
        "so_what": "重构公共空间人机共存边界的先锋尝试；在开放办公区或嘈杂地铁中，无需开口发声也无需敲击键盘即可完成高保密性交互，兼具包容与前瞻性。",
        "source": "github.com",
        "url": "https://github.com/amirrsyed/hushkey",
        "media": "https://images.unsplash.com/photo-1589254065878-42c9da997008?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "Bowerbird 给回答中的引语逐条验出处：严苛证据溯源代理",
        "note": "治理大模型幻觉的严密审校中间件：自动将 Agent 输出的每一句断言、引用与推导，反向回溯至知识库与网络抓取原始语段，黄色标出无支撑悬空内容。",
        "so_what": "智能体融入严肃企业级工作流的刚需插件；彻底消灭“信口开河但查无实据”的风险，把人类审阅精力从大海捞针查验缩减为聚焦红线核对。",
        "source": "github.com",
        "url": "https://github.com/jolovicdev/bowerbird",
        "media": "https://iandaily.xyz/digest/2026-11-02-bowerbird-4e7f5854ac19.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "Sweet-search 让代理先查索引再读代码：降低 Context 膨胀的检索增强",
        "note": "大型代码库结对编程的性能减负方案：智能体在动手修改前，先调用预构建 AST 语义拓扑索引定位核心切片，坚决拒绝一股脑将数万行代码灌入提示词。",
        "so_what": "降本增效与防上下文遗忘的核心技巧；精准喂入最小必要上下文，不仅大幅缩减 Token 账单开销，更能显著降低模型在长文本迷宫里的注意力漂移。",
        "source": "github.com",
        "url": "https://github.com/mrsladoje/sweet-search",
        "media": "https://iandaily.xyz/digest/2026-11-02-sweet-5bce6b0cd5a4.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "SpecGuardian 用状态规格检查 AI 实现：以形式化规约约束代码生成",
        "note": "软件工程契约在 AI 时代的进化重塑：利用 TLA+ 思想为业务流程预先定义严格的状态机转移规格，让智能体生成的实现代码必须在数学约束检验器中通过验收。",
        "so_what": "终结“代码跑通了但边界条件死锁”的隐蔽缺陷；用不可动摇的形式化规格作为机器与人类的契约护城河，让 AI 编码真正具备工业级可靠性。",
        "source": "github.com",
        "url": "https://github.com/mrasu/spec-guardian",
        "media": "https://iandaily.xyz/digest/2026-11-02-spec-6a09bcf3026d.jpg",
        "pinned": False
    },
    {
        "category": "AI 协作",
        "title": "Castov 把本地小工具接进 CLI 与 MCP：统一模型交互协议",
        "note": "极速封装个人本地脚本的桥接器：只需一行配置，即可将开发者日常积攒的 Python/Shell 运维小工具一键暴露为符合 MCP 标准的服务节点供 Agent 调用。",
        "so_what": "个人数字化资产与多智能体生态的低成本连接器；不必重构现有工具链，让沉淀多年的本地脚本瞬间化为智能体的武器库，放大个人杠杆效应。",
        "source": "castov.com",
        "url": "https://castov.com",
        "media": "https://iandaily.xyz/digest/2026-11-02-castov-b1b38866a1d4.jpg",
        "pinned": False
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "Folio 清理重复照片前先解释保留原因：有温度的本地隐私相册清理",
        "note": "克制温情的个人数据管理单兵产品：在建议删除连拍废片前，系统用简短一句解释为什么挑选出最佳的一张（构图居中、微笑清晰），全部运算在本地安全完成。",
        "so_what": "小而美工具以情感共鸣打动付费用户的教科书；冷冰冰的“一键删除”容易让用户焦虑，带理由的审慎建议不仅消除误删恐惧，更赋予产品强烈的信任溢价。",
        "source": "caddora.ie",
        "url": "https://caddora.ie/folio",
        "media": "https://iandaily.xyz/digest/2026-11-02-folio-94b34ae92c1a.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Shroom 把录屏费用交回自己的云账号：自带 S3 存储的单兵录屏 SaaS",
        "note": "对抗高昂订阅制云存储的利基工具：提供极佳的录屏剪辑与分享体验，但视频底片直接上传至用户自己的 AWS S3 或 Cloudflare R2，服务本身仅收取极低授权费。",
        "so_what": "BYOS（Bring Your Own Storage）模式在微型 SaaS 中的巨大威力；彻底摆脱沉重的视频带宽存储成本包袱，创始人利润率高达 90% 以上，轻资产稳健运转。",
        "source": "shroom.am",
        "url": "https://shroom.am",
        "media": "https://iandaily.xyz/digest/2026-11-02-shroom-59c64c97ff6d.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "PixelShrink 在浏览器本地压缩图片：纯客户端 Canvas 批量无损压缩",
        "note": "零服务端开销的工具站盈利范本：借助现代浏览器 Web Workers 与 Canvas API，纯靠客户端 CPU 快速压缩海量高清 PNG/JPEG，网站零后端服务器账单。",
        "so_what": "一人公司以零边际运维成本撬动自然流量的最佳实践；不依赖任何云端昂贵 GPU/CPU 算力，只要做好 SEO 与利基功能，小流量也能持续稳定带来被动收入。",
        "source": "compress-image.uk",
        "url": "https://compress-image.uk/",
        "media": "https://iandaily.xyz/digest/2026-11-02-pixel-8ae7f22844fc.jpg",
        "pinned": False
    },
    {
        "category": "一人公司",
        "title": "TariffPedia 从商品编码查起进口成本：跨境出海关税与合规垂直查询字典",
        "note": "跨境电商出海从业者的必备避坑指南：输入 HS 编码即可一键穿透查看欧美多国反倾销税、增值税与海关清关红线，将繁琐的官方海关文档转化为清晰图表。",
        "so_what": "挖掘垂直行业信息差的典型独立数据产品；把外贸人每天烧脑对账查规的脏活累活系统化封装，用不可替代的合规确定性赢得跨境卖家的稳定订阅。",
        "source": "tariffpedia.com",
        "url": "https://tariffpedia.com/",
        "media": "https://iandaily.xyz/digest/2026-11-02-tariff-4ef881541af2.jpg",
        "pinned": False
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "Type It Big 把屏幕变成大字手牌：即开即用零多余步骤的纯粹表达",
        "note": "反复杂化极简交互设计的巅峰之作：打开网页就是全屏超大字号输入，没有任何工具栏或设置弹窗，字号随输入字数动态自动缩放，专为远距离沟通而生。",
        "so_what": "把单一场景做到极致纯粹的减法哲学；在功能泛滥的今天，敢于砍掉一切多余花哨按钮，用户在机场接机或吵闹展会中一秒就能用上，手感无比通透。",
        "source": "typeitbig.com",
        "url": "https://typeitbig.com/",
        "media": "https://iandaily.xyz/digest/2026-11-02-typeitbig-212a337e437c.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Crosswalk 给每个终端留一行任务备注：解决并发窗口认知负荷的设计",
        "note": "程序员终端窗口管理的微小体验革新：允许在每一个活跃的分屏终端顶部悬挂一行轻量任务备注与预期目标，防止多任务并发切换时思维断流。",
        "so_what": "敏锐洞察高频心智摩擦的绝佳设计切口；微小的物理视觉锚点能大幅降低工作上下文恢复耗时，用极其克制的 UI 改动解决困扰开发者多年的盲切焦虑。",
        "source": "wareshq.com",
        "url": "https://wareshq.com/crosswalk",
        "media": "https://iandaily.xyz/digest/2026-11-02-crosswalk-3ba2516defe8.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "LanesMac 让窗口沿横向长桌展开：突破传统全屏与虚拟桌面的横向物理手感",
        "note": "桌面窗口管理范式的物理空间隐喻重构：打破叠放窗口和固定多桌面概念，将所有运行应用排布在无限延伸的横向平铺轨道上，双指横向滑动如推开实体长桌卷轴。",
        "so_what": "用空间连续性重构数字工作流的先锋探索；消除窗口层叠带来的遮挡与盲寻，赋予宽屏使用者前所未有的开阔与沉浸感，让操作回归直觉。",
        "source": "lanesmac.com",
        "url": "https://lanesmac.com",
        "media": "https://iandaily.xyz/digest/2026-11-02-lanes-07dc46914291.jpg",
        "pinned": False
    },
    {
        "category": "产品设计",
        "title": "Bobby 按依赖关系安排代码审阅：拓扑时序驱动的代码审查微体验",
        "note": "颠覆传统按文件名字母序审阅 PR 的新颖交互：自动分析代码变更的拓扑依赖因果链，先展示底层核心数据模型改动，再逐级推衍至上层业务调用。",
        "so_what": "让工具顺应人类认知规律的深刻设计；代码审阅最怕在细枝末节的修改里迷失主干，用因果拓扑序重新编排变更，审阅效率与缺陷检出率实现翻倍。",
        "source": "viraj.computer",
        "url": "https://bobby.viraj.computer/",
        "media": "https://iandaily.xyz/digest/2026-11-02-bobby-b8102f35b647.jpg",
        "pinned": False
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "澳门水边茶渣板竹塔：非遗脚手架搭接与再生农业茶渣材料的诗意融合",
        "note": "岭南非遗竹构工艺与当代可持续材料的惊艳对话：以传统手工劈篾竹搭接为坚韧支撑框架，外立面铺挂由回收废弃茶叶渣压制而成的透气纤维板，散发幽微茶香。",
        "so_what": "将生态循环哲思融入公共建筑形式的巅峰范本；让传统民间营造智慧在现代城市滨水空间重生，兼具视觉轻盈质感、嗅觉通感与深厚的人文土地联结。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/architecture/traditional-bamboo-scaffolding-tea-waste-panels-impromptu-projects-pagoda-macau/",
        "media": "https://iandaily.xyz/digest/2026-11-02-bamboo-416911e2e1be.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Buoy 把废旧船绳打印成摇摆凳：海洋渔具废弃物与机械臂 3D 打印的律动雕塑",
        "note": "海洋废弃材料与先锋计算设计的工艺突破：回收港口废弃尼龙渔网船绳并热熔造粒，由机械臂逐层打印出如海浪波纹般起伏的球底摇动凳，坐感随重心舒缓起伏。",
        "so_what": "工业废料向高雅生活雕塑的华丽蜕变；动态摇摆的物理交互呼应了材料前世经历的风浪颠簸，用考究的肌理纹路证明环保设计绝不等同于简陋与粗糙。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/11/01/buoy-stools-the-new-raw/",
        "media": "https://iandaily.xyz/digest/2026-11-02-buoy-1151dee535ab.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "伊斯坦布尔 Rami 图书馆彩色模块游园亭：现代模数游乐构件激活古建庭院",
        "note": "历史遗存保护区与先锋公共家具的激进碰撞：在数百年历史的拜占庭风貌红砖庭院中，穿插安放高饱和度几何穿孔钢板模块，为读者创造私密读书角落与穿行路径。",
        "so_what": "用克制的新旧反差为凝滞的历史空间注入新鲜血液；几何色块不仅是休憩设施，更是引导游人视线与身体流动的微型建筑装置，激活沉睡的历史公共活力。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/architecture/chromatic-pavilions-modular-play-structures-historic-istanbul-rami-library-milimetrik-architects/",
        "media": "https://iandaily.xyz/digest/2026-11-02-rami-c9cde8aef6d1.jpg",
        "pinned": False
    },
    {
        "category": "审美提升",
        "title": "Supremath 用几何规则生成至上主义构成画：数学算法与马列维奇艺术的当代回响",
        "note": "纯算法生成至上主义视觉艺术的迷人实验：基于严格的几何黄金比例、原色对比与非对称力学平衡算法，实时生成充满张力与构成感的抽象数字画作。",
        "so_what": "数学理性与纯粹美学在数字画布上的完美咬合；跨越一个世纪向至上主义致敬，展现了代码不仅能构建功能性软件，更能作为雕琢灵魂的现代画笔。",
        "source": "supremath.art",
        "url": "https://supremath.art/",
        "media": "https://iandaily.xyz/digest/2026-11-02-supremath-0d7760225ddf.jpg",
        "pinned": False
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Winch 让智能体自主接管商店 SEO：中小商户自动化转化率优化",
        "note": "面向电商独立站商户的主动型增长智能体：不仅自动分析跳出率与搜索词漏斗，更在后台自动批量重写产品描述、优化长尾元标签，以 A/B 测试数据驱动落地。",
        "so_what": "从“手动看数据报表抓瞎”走向“算法自主执行增长闭环”的技术跨越；让单兵卖家拥有大厂级精细化流量操盘能力，将每一分流量的转化潜力压榨到极致。",
        "source": "getwinch.app",
        "url": "https://getwinch.app/",
        "media": "https://iandaily.xyz/digest/2026-11-02-winch-5ae3b64de0c0.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "Overhear 把舆情监测改为按需扫描：拒绝高昂月租的单兵轻量声誉雷达",
        "note": "颠覆传统公关监测 SaaS 商业模式的轻量方案：坚决摒弃数千美金的高昂常驻月费，用户只需在产品发布或危机时刻发起单次深度全网社交舆情扫描，按次结算。",
        "so_what": "以真诚契约打破大厂软件价格垄断的利器；顺应创业团队偶发性、突发性的真实监测诉求，用极低门槛换取极高转化率，在巨头忽视的夹缝中快速立足。",
        "source": "overhear.dev",
        "url": "https://overhear.dev/",
        "media": "https://iandaily.xyz/digest/2026-11-02-overhear-572a0f5d0c1e.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "Citeon 监控品牌在 AI 回答里的引用占有率：生成式引擎时代的内容护城河",
        "note": "生成式引擎优化（GEO）前沿监测雷达：跨模型实时抓取 ChatGPT、Claude 与 Perplexity 在行业核心采购提问下的回答，精准量化自身品牌的推荐占有率与正负面评价。",
        "so_what": "搜索营销（SEO）向智能体推荐营销（GEO）转型的战略罗盘；当传统搜索框被大模型全面替代，尽早掌握自身在机器回答中的可见性权重，就是抢占未来生意命脉。",
        "source": "citeon.dev",
        "url": "https://citeon.dev",
        "media": "https://iandaily.xyz/digest/2026-11-02-citeon-91f66afa2896.jpg",
        "pinned": False
    },
    {
        "category": "产品营销",
        "title": "SiteOne 把整站 SEO 体检交成可读报告：全栈式单机开源爬虫诊断利器",
        "note": "独立站站长必备的整站健康巡检工具：单机命令行高速遍历全站数万个页面，深度检测死链、重复标题、缺少 Alt 标签及深层重定向链，输出排查清单。",
        "so_what": "做好基础技术 SEO 就是最稳固的获客基本盘；在盲目砸钱投流之前，先把自家站点的爬取障碍扫清，用扎实的页面健康度换取搜索引擎源源不断的免费权重奖励。",
        "source": "siteone.io",
        "url": "https://crawler.siteone.io/",
        "media": "https://iandaily.xyz/digest/2026-11-02-siteone-edaa65bc9bf4.jpg",
        "pinned": False
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "即梦短剧工作室实操测评：双十一每秒低至0.16元背后的视听工业化降本",
        "note": "视听生成生产力工具的工业化成本跃迁：深度实测即梦短剧工作室全流程，算力促销叠加高效分镜流转将单秒视听成本打入两毛钱大关，彻底重塑小团队预算结构。",
        "so_what": "微短剧降本增效从概念宣导走向物理账单现实；单集成本从几万断崖式跌至几千，极大降低了个体创作者试错门槛，加速短剧创作走向全民去中心化时代。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487529.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "短剧火爆出圈呼唤独立评价体系：从低质下沉到精品化评分的生态进阶",
        "note": "微短剧内容价值跃迁的行业呼声：剖析大众关于“豆瓣是否应为短剧单开评分专页”的激烈论战，探讨短剧如何摆脱粗制滥造刻板印象、走向高品质叙事认可。",
        "so_what": "行业从粗放流量狂欢走向严肃艺术批评的标志；拥有客观公正的公众评价土壤，才能引导资本从纯买量狗血套路转向精雕细琢优质剧情，沉淀长效文化资产。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6487413.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "“字节时间”到底是不是“垃圾时间”？微短剧连续刷屏背后的大众心理透视",
        "note": "透视超高黏性微短剧与信息流背后的心理奖赏机制：深入拆解大众在碎片时间里沉迷一两小时刷剧的情感代偿逻辑，以及平台在算法投喂与防沉迷合规上的博弈。",
        "so_what": "内容创作者必须洞察的大众心理刚需；用户消耗时间的本质不是追求所谓的高雅说教，而是在逼仄的生活缝隙中寻找高浓度的即时抚慰，尊重这种情绪需求才能做好爆款。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6487537.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "AI 漫剧",
        "title": "声音直播与虚拟偶像的情绪经济学：微短剧团队跨界音频赛道变现洞察",
        "note": "小团队拓展视听 IP 变现场景的新蓝海：剖析声音直播与轻量虚拟角色如何通过高频陪伴与定制互动创造惊人客单价，为漫剧创作者提供了低成本音频衍生路径。",
        "so_what": "视听资产多维变现的战略灵感；视觉制作即便再便宜也有渲染周期，而基于人设的高频语音陪伴能以极轻成本占领用户私密睡前场景，实现全天候私域复购。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6486483.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《冰封方舟》120 集末日微短剧：极致生存困境与人性救赎弧线设计",
        "note": "末日废土类型微短剧的剧作黄金法则：全球冰封极端恶劣环境下，避难所内物资匮乏与阶层倾轧步步紧逼，以紧凑的 60 秒生死抉择塑造主角从自私自保到挺身救赎的动人弧线。",
        "so_what": "极限情境是剥离虚伪、展现人性光辉的最强放大器；让主角在绝境中每一次艰难抉择都伴随巨大的道德与生存代价，能牢牢抓住观众情绪悬念，催生深度共鸣。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2217",
        "media": "https://images.unsplash.com/photo-1483921020237-2ff51e8e4b22?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《湮灭舰队》120 集太空科幻微短剧：舰队战绝境推进与悬疑危机层层加码",
        "note": "太空军旅与硬核星战题材的编剧范式：星际舰队遭遇未知降维打击深陷绝境，副官在重重猜忌与系统崩溃中层层剥茧排查内鬼，保持每集一个高潮反转。",
        "so_what": "宏大太空背景下拉紧戏剧张力的破局手段；不要沉湎于空洞的宇宙名词堆砌，把叙事视角牢牢锁定在幽闭舰桥内具体人物的心理博弈与决断上，才能让故事惊心动魄。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2218",
        "media": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《天劫代打》120 集仙侠微短剧：荒诞脑洞与渡劫反差爽感的戏剧张力编排",
        "note": "反套路爆笑仙侠微短剧的因果链重塑：底层凡人机缘巧合下掌握替各路金丹元婴大佬专业代抗天劫的绝技，利用现代电磁避雷科学解构传统修真迷信。",
        "so_what": "经典玄幻题材突破审美疲劳的奇招；用现代常识与传统仙侠规则碰撞产生的强烈错位制造密集笑点，以小博大、智斗碾压的爽感更加酣畅淋漓。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2219",
        "media": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "编剧技巧",
        "title": "《环宇公约》120 集硬科幻微短剧：文明初接触博弈与规则博弈的高潮构建",
        "note": "高概念严肃科幻短剧的交锋设计：深空科研科考船偶遇硅基文明探针，双方在没有共同语言的前提下，依托物理常数与博弈论公理在微秒级内展开生死谈判。",
        "so_what": "微短剧进军高智商严肃叙事的标杆示范；放弃低幼的狗血打杀，用严密的因果逻辑推理与宏大宇宙法则推演，满足硬核科幻受众极致的智力愉悦感。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2220",
        "media": "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "AI 办公智能体赛道深度拆解：从「能生成」到「能交付、可治理、可复用」",
        "note": "企业级办公 Agent 产品演进的必经之路：剖析腾讯 WorkBuddy 等标杆产品的架构飞跃，深入探讨多应用沙箱调度、长程审批链路集成与企业资产权限隔离的核心壁垒。",
        "so_what": "B 端产品经理从虚荣 Demo 走向严谨业务落地的指南针；企业不会为会写诗的玩具付高溢价，唯有能融入既有业务流程、交付确定性可信结果的系统才具备商业生命力。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/evaluating/6486874.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "设计师与产品经理的协作快照：状态流转、用户对象与闭环反馈设计",
        "note": "产设协同在复杂应用时代的信息流治理：深入探讨系统状态机快照如何在 PM、UI 设计师与前端之间无损流转，避免在极端边界状态下出现交互断层与需求扯皮。",
        "so_what": "打造防脆弱软件产品的底层功力；好的产品不是在常规路径上好看，而是在网络中断、并发冲突、权限降级等灰度快照下依然优雅可靠，彰显团队专业素养。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487586.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "兼具 Agent、多模态与具身经验的复合架构师：下一代产品经理的能力全景",
        "note": "全栈型 AI 产品操盘手的能力画像跃迁：深度剖析同时横跨语言模型 Agent 调度、多模态视听生成与物理世界机器人交互的实战专家，如何拆解复杂多模态系统瓶颈。",
        "so_what": "产品人跨越时代周期的成长天花板；从单纯的文本提示词工程走向具身与物理世界的真实闭环，拥有多模态全链路系统思维的 PM 正在成为行业最稀缺的战略资产。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487591.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "产品经理",
        "title": "硅谷前沿与下一代 Agent 落地实践：产品化架构演进与商业闭环深度复盘",
        "note": "对标 DeepSeek 与硅谷顶尖智能体团队的产品架构横评：解构长思考推演模型、主动记忆管理与端侧沙箱在具体企业场景下的工程取舍与商业变现模式。",
        "so_what": "给盲目跟风技术参数的产品团队注入商业清醒剂；技术优势的半衰期极其短暂，能够迅速将前沿模型能力封装为解决企业痛点的护城河产品，才是终极胜负手。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487545.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    }
]

def build():
    frontmatter = {
        "date": "2026-11-02",
        "title": "11 月 02 日 · 智能体集群自决与交付契约重构：从黑箱对话狂欢到可治理工程闭环",
        "highlights": "全网 9 大领域 36 篇高密度精选：Memdoor 记录小模型团队协作解题实录、Bowerbird 严苛溯源回答证据链、即梦短剧每秒成本压至 0.16 元引爆工业化、AI 办公智能体从「能生成」到「能交付可复用」、Type It Big 纯粹无废话的大字全屏手牌。",
        "draft": False,
        "epigraph": "软件工程走过半个世纪沉淀下来的契约与拓扑，不该在大模型的模糊概率里被彻底冲垮；真正成熟的智能体不是在聊天框里滔滔不绝，而是带着确定性证据把代码送进沙箱跑通测试。",
        "lead": "11 月 2 日，数字化前沿的探索正在经历一场从“概率黑箱”到“确定性工程”的集体觉醒。在智能体协作前线，工程师们不再迷信单个庞然大物，而是用 Memdoor 与 Sweet-search 探索小参数集群分工，用 Bowerbird 和 SpecGuardian 将每一步推演钉死在事实证据与形式化规格之上；在视听创作战场，即梦短剧把生成成本压降到每秒 0.16 元，以惊人的工业化效率彻底重写制作预算；而在商业软件落地的最深处，企业不再为“能生成几千字漂亮废话”买单，WorkBuddy 的走红标志着办公 Agent 正式跨入“能交付、可治理、可复用”的严肃生产阶段。喧嚣散去，给技术套上严丝合缝的规约与缰绳，才是让生产力真正爆发的终极密码。",
        "scene": "「这个 Agent 昨天一口气改了我 40 个文件，看着特智能，今天一跑测试全崩了，我找谁说理去？」「所以千万别给它无限自由。把规格先立好，让它每改一行都提供引用证据和依赖拓扑，能过沙箱编译的才叫代码，通不过的叫数字垃圾。」",
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

站在十一月初的节点上，我们看到 AI 领域正在完成一次关键的成人礼——从惊叹于“它居然能像人一样说话”，走向严谨追问“它交付的东西到底能不能对业务负责”。无论是一人公司把录屏与订阅做成零隐私风险的微型 SaaS，还是建筑师把茶渣与废弃船绳编进公共空间，其核心都在于对真实世界物理边界与人性尊严的敬畏。不要被浮夸的技术演示迷了双眼，守住你的工程标准，沉入业务细节，把确定性交付做到极致。"""

    full_md = f"---\n{yaml_str}---\n\n{closing_text}\n"

    target_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-02.md"
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
