# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-22': {
        'title': '10 月 22 日 · 权限沙箱与物理闭环：当智能体开始踏入“真实物理世界”',
        'highlights': '全网 9 大领域 36 篇高密度精选：vLLM 联合蚂蚁开源通用量化内核 Humming、LiteLLM 供应链失窃事件紧急复盘、个人 Agent 战火烧向物理硬件与端侧设备、ComfyUI 生产级节点套件与 AI 视频工业化阵痛、《三国演义》AI 漫剧商业全案与校园悬疑短剧全本交割。',
        'epigraph': '智能体的真正分水岭，不在于它在虚拟对话框里多会聊天，而在于它能否在严格的权限沙箱保护下，稳妥地接管物理世界的真实交付。',
        'lead': '10 月 22 日，大模型前沿技术正加速从“云端推理虚拟自嗨”走向“端侧物理硬件与供应链安全防御”的深水战场。如果说过去的智能体开发还在聚焦于提示词编排与上下文拼装，那么今天整个技术生态正在遭遇最严峻的工程与安全考验：在基础设施与供应链安全端，LiteLLM 恶意版本被投毒导致敏感凭据外泄事件引爆全球开发者社区，迫使整个行业从粗放接入转向严格的沙箱隔离与依赖锁定；在算力优化端，蚂蚁集团与 vLLM 联合开源统一量化推理内核 Humming，将异构硬件部署门槛进一步压低；而在终端交互层面，各大巨头与独立开发者正全力把个人 Agent 推向智能眼镜、手机端侧与实体硬件，让小模型直接接管屏幕视觉与物理控制；在视听漫剧创作前线，行业在经历了一年的 AI 视频生成狂欢后，正从粗暴拼量转向精细化镜头语法与工业化资产沉淀，ComfyUI 生产级路由套件与《三国演义》AI 漫剧分镜全本交割，为微短剧工业化交付提供了坚实样本。',
        'scene': '「为什么要在本地开发环境里给 Agent 加上重重权限弹窗？让它自动执行不是更爽吗？」「前天那起依赖投毒事件还不够敲响警钟吗？当智能体拥有了调用终端与支付的权力，每一行外部依赖都可能成为隐蔽的窃听器。没有沙箱与确定性门禁的智能体，无异于在裸奔的炸药堆上跳舞。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周四。

今天整理这 36 篇精选时，最让我警醒也最振奋的，是 **智能体技术生态正在迅速告别“玩具期”与“裸奔期”**。

一方面，**安全防线被推到了台前**：
LiteLLM 供应链事件给所有人上了一堂沉重的安全课——大模型时代的“中间件”，往往掌握着企业最高等级的 API 密钥与用户数据。
未来的顶尖架构师，核心竞争力不再只是比拼谁的模型 Prompt 写得花哨，而是谁能在复杂的 Agent 工具链中构建严密、不可逾越的权限沙箱。

另一方面，**应用落地正在走出虚拟对话框，扎进端侧硬件与现实业务深水区**：
无论是端侧 2B 模型的手机屏幕自动化控制，还是老工坊将 25 年隐性经验转化为自造血产品，
都在昭示着同一个规律：
**能带来真实生产力增量、能为物理世界结果买单的技术，才拥有跨越周期的硬通货价值。**

愿你在今天的造物中，既保持对边界与安全的敬畏，又具备敢于穿透物理交付的笃定。''',
        'ai_news': [
            {
                'category': 'AI 资讯',
                'title': 'Humming 开源量化推理的通用内核库',
                'note': '蚂蚁集团与 vLLM 社区联合开源的高性能通用推理内核：将 AWQ、GPTQ 与 SmoothQuant 等多种前沿量化格式收拢进统一切分与调度实现，显著提升长文本高并发吞吐。',
                'so_what': '打破碎片化量化格式的硬件适配鸿沟；为企业级私有化模型服务提供了跨 GPU 架构的统一性能基石。',
                'source': 'vllm.ai',
                'url': 'https://vllm.ai/blog/2026-10-21-humming',
                'media': 'https://iandaily.xyz/digest/2026-10-22-humming-13ca92900715.jpg',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'Recursive 发布可在笔记本运行的 Flint',
                'note': '四百亿总参数的混合专家（MoE）编码模型：通过极致激活参数稀疏化与端侧算子优化，让开发者能够在主流笔记本上获得逼近大型商业模型的本地代码补全与调试体验。',
                'so_what': '端侧代码自闭环的又一飞跃；在保护企业敏感源码资产的前提下，把顶尖编程 Agent 的算力开销降至零边际成本。',
                'source': 'recursive.com',
                'url': 'https://recursive.com/updates/introducing-recursive-flint',
                'media': 'https://iandaily.xyz/digest/2026-10-22-recursiveflint-5128fe36c111.jpg',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'Opposable 让小模型在 Android 本机操作',
                'note': '端侧 UI 自动化的极轻量实践：仅需二十亿参数的小模型即可实时解析手机屏幕截图并执行精准点击滑动，对高频标准操作优先走本地确定性脚本路由。',
                'so_what': '移动端个人助理的全新破局点；摆脱云端多模态高昂延迟与隐私顾虑，为端侧硬件智能体铺平了工程落地道路。',
                'source': 'getopposable.com',
                'url': 'https://getopposable.com/blog/computer-use-on-the-phone',
                'media': 'https://iandaily.xyz/digest/2026-10-22-opposable-4ede24a9acc4.jpg',
                'pinned': False
            },
            {
                'category': 'AI 资讯',
                'title': 'LiteLLM 恶意版本把模型网关变成失窃入口',
                'note': 'AI 基础设施供应链安全的重大险情复盘：知名模型路由网关 PyPI 镜像遭遇供应链投毒，恶意代码静默窃取团队环境变量与 API 密钥，给全行业敲响合规警钟。',
                'so_what': '大模型中间件的安全门禁不可轻忽；将模型访问收拢为网关的同时，必须建立严格的哈希校验与外发网络监控沙箱。',
                'source': 'wiz.io',
                'url': 'https://www.wiz.io/blog/litellm-compromised-steals-credentials',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI rgthree 生产级节点套件：复杂多镜头工作流静音/旁路与上下文快速路由',
                'note': '专业漫剧制片团队的核心工作流支柱：提供多路开关静音/旁路、全局书签快速定位与极速连线路由，极大减轻数百个节点的大型长视频生成管线的排障负荷。',
                'so_what': '把生图作坊提升为影视工业化流水线的关键基建；通过规范化节点编排杜绝无效重绘，大幅缩短漫剧整集的出片周期。',
                'source': 'github.com',
                'url': 'https://github.com/rgthree/rgthree-comfy',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'AI 视频爆发一年：一代人的生产红利和视听工业化阵痛',
                'note': '生成式视频技术爆发一周年的深度行业全景复盘：技术门槛拉平后，视听创作者迅速从参数狂欢跌入同质化泥潭，唯有深耕镜头调度、情绪连贯与戏剧审美才能穿越周期。',
                'so_what': '走出唯算力论的清醒审视；生成工具的平权终将把竞争导向叙事核心，证明好故事与经典电影语言依然是视听内容不可替代的灵魂。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6482660.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '单日 5606 本新书：AI 正在重塑网文供给与微短剧漫改流水线',
                'note': '网文供给端工业化海啸的微观透视：AI 生成网文数量呈指数级爆发，倒逼行业迅速重构从海量文本初筛、自动提取戏剧梗概到快速转化为 AI 漫剧分镜的端到端孵化链条。',
                'so_what': '上下游生态重组中的重大产品机会；谁能用 AI 把巨量粗糙网文精准提纯为高转化漫剧剧本与分镜资产，谁就能截留产业链最丰厚的利润。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6482745.html',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《三国演义》第一季 1-12集AI漫剧商业全本：历史权谋与视听分镜交割',
                'note': '传统经典名著的 AI 漫剧工业化改编标杆：将东汉末年群雄逐鹿的宏大历史场景拆解为适合 AI 视频模型生成的标准化角色三视图、分镜台本与动态运镜提示词，全流程商业交割。',
                'so_what': '公版经典 IP 依托 AI 漫剧焕发新生机；通过标准化视听资产库极大降低宏大历史题材的制作成本，为传统文化出海提供了可复制的工业化范本。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1803',
                'media': 'https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《十七岁的审判》（60集悬疑短剧）：校园悬疑与陈年旧案人性审判的因果网编织',
                'note': '强情节悬疑微短剧的剧作全案剖析：围绕一桩尘封十年的校园坠亡案，采用多重视角罗生门叙事与高频反转，将青少年心理阴影与家庭伦理压力编织成密不透风的悬疑戏剧网。',
                'so_what': '悬疑短剧长线钩子的设计典范；用严密的逻辑闭环与复杂人性的深度挖掘代替无脑暴力噱头，展现精品悬疑短剧的破圈穿透力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1798',
                'media': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《昼夜之间》社区悬疑短剧：昼夜双线博弈与代际联手探案的节奏掌控',
                'note': '贴地飞行的都市现实悬疑创作范本：以老刑警与短视频探案博主的代际观念冲突为切口，将现代数字取证与传统痕迹勘验有机结合，节奏张弛有度，烟火气与压迫感兼具。',
                'so_what': '现实主义短剧在代际情感与类型元素间的精妙平衡；用扎实的生活细节增强真实感，为悬疑剧作注入厚重的情感底色。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1790',
                'media': 'https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《12次的人生复活试炼》奇幻无限流短剧：宿命轮回与人性的极致拷问',
                'note': '高概念无限流设定下的剧作解构：每一次生命重启不仅没有带来金手指爽感，反而暴露出更残酷的道德困境，精巧的因果阶梯推动主角完成从利己到救赎的精神蜕变。',
                'so_what': '把游戏化重置机制转化为剧作驱动力的上乘之作；在严谨的时空规则约束下挖掘情感张力，为高概念微短剧创作提供了优秀的类型解法。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1791',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '《宛城大捷》古代战争微短剧：极限绝境下的谋略博弈与群像破局',
                'note': '微型篇幅展现宏大战争场面的编剧技法：放弃耗费巨大的全景式铺陈，聚焦于城墙隘口十数位不同阵营将士的生死抉择与声东击西战术博弈，以小见大、惊心动魄。',
                'so_what': '低预算下拍摄史诗战争题材的聪明打法；把剧作重心放在心理攻防与智谋碰撞上，用紧凑的分镜与高压节奏征服观众。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1788',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '从找场景到做 Skill：AI 赋能落地的工程拆解方法',
                'note': '大模型业务落地方法论的体系化重构：深度拆解如何从真实业务摩擦中提炼核心 Prompt、定义结构化输入输出，并将其封装为具备容错机制的生产级 Skill。',
                'so_what': 'AI 产品经理从概念布道迈向工程闭环的必经之路；掌握工具化封装与边界防御能力，才是保障 AI 方案落地见效的真实内功。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6482891.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '双11走向分化：天猫押旗舰店+AI，抖音扩流量池，京东放大供应链',
                'note': '电商存量竞争白热化下各大平台战略分歧的深度研判：分析平台如何在价格力见底的背景下，分别依托自研 AI 工具提效、内容私域深耕与确定性物流构建差异化壁垒。',
                'so_what': '看透平台规则更迭背后的底层驱动力；高级产品经理必须洞悉流量、供应链与技术创新的三元博弈，方能找准自身的战略生态位。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6482557.html',
                'media': 'https://images.unsplash.com/photo-1556742049-0a67e557224d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'Personal Agent 战火正在烧向硬件：端侧物理交互与场景闭环',
                'note': '个人智能体从纯软件服务向物理载体渗透的趋势研判：智能眼镜、可穿戴徽章与车载座舱成为争夺第一视角的先锋战场，分析硬件功耗、端侧算力与交互摩擦的现实卡点。',
                'so_what': '下一代人机交互终端的范式转移；软件产品人必须尽早建立软硬结合的产品视界，把握端侧物理感知所释放的全新场景红利。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6482556.html',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '别去公域当炮灰：一家25年老工坊如何靠“经验产品化”跑通自造血？',
                'note': '传统手艺团队数字化转型的扎实复盘：拒绝盲目烧钱买量，将数十年的非标手艺提炼为标准知识库与产品化服务包，以极高复购与口碑在私域实现稳定盈利。',
                'so_what': '独立创业者在流量内卷时代的破局灵药；将独特的隐性专业资产结构化产品化，才是抵御外部平台流量剥削的最硬底牌。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/operate/6482645.html',
                'media': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

# 2. Curated Ian picks (20 items across 5 categories)
raw_ian_path = 'scripts/raw-ian-22.json'
with open(raw_ian_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

curated_ian_picks = {
    'AI 协作': [
        'https://www.band.ai/use-cases/band-desktop',
        'https://www.trylasso.online',
        'https://github.com/unionai-oss/hlock',
        'https://squidbrake.com/benchmark'
    ],
    '一人公司': [
        'https://mood-tracker.org/',
        'https://github.com/freshNfunky/Timeminator-Community',
        'https://qovilio.com/',
        'https://makevideosmaller.com/'
    ],
    '产品设计': [
        'https://riffcalendar.com',
        'https://useit.im/',
        'https://apps.apple.com/cn/app/id6761676075',
        'https://vitalsmac.com/'
    ],
    '审美提升': [
        'https://www.wallpaper.com/art/music/apple-musics-new-visual-identity-turns-sound-into-liquid-with-help-from-fred-again',
        'https://www.designboom.com/design/steel-spheres-curved-glass-leonardo-garza-sensory-installation-byredo-matter-memory/',
        'https://www.designboom.com/design/boss-design-the-loop-lucy-chair-circular-initiative/',
        'https://www.dezeen.com/2026/10/21/dosorozco-casa-sima/'
    ],
    '产品营销': [
        'https://www.flagsmith.com/feature/experimentation-platform',
        'https://www.nativeship.io/',
        'https://github.com/SupercmoHQ/superCMO-skills',
        'https://www.flyweel.co/'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://www.band.ai/use-cases/band-desktop': '从单点编码助手向智能体项目团队的范式跃迁；用透明看板消灭多 Agent 协同中的重复试错与上下文断层。',
    'https://www.trylasso.online': '终结截图打字描述界面的低效沟通；把人类的空间视觉直觉无缝转化为 Agent 能够直接消费的精准结构化坐标。',
    'https://github.com/unionai-oss/hlock': 'Agent 工程走向标准化交付的基石；用类似 package-lock 的确定性机制终结“在我的机器上能跑”的协作混沌。',
    'https://squidbrake.com/benchmark': '给敢于全自动交付的团队一把安全标尺；在 Agent 上线前用实战级陷阱测试防御纵深，防患于未然。',
    'https://mood-tracker.org/': '单兵产品的极简优雅法则；用纯端侧静态架构消灭服务器运维成本，靠极度克制与隐私安全赢得口碑留存。',
    'https://github.com/freshNfunky/Timeminator-Community': '个体数字游民的商业护城河；把计费与交付证据死死掌握在自己手中，告别抽成高昂且随时被封号的中心化平台。',
    'https://qovilio.com/': '直击数字游民“静默扣费”的慢性失血痛点；用清晰的财务日历帮助独立开发者守住来之不易的正向现金流。',
    'https://makevideosmaller.com/': '出海实用微工具的教科书范式；把重度转码算力完全卸载给用户端设备，以接近零的服务器边际成本赚取长尾流量。',
    'https://riffcalendar.com': '对既有百年时间空间界面的深度重构；用流畅的连续手感消除认知跳跃，为效率工具树立了触觉交互新高度。',
    'https://useit.im/': '数字设计交付向物理实体生产的端到端穿透；消除打样过程中的繁琐返工，把实体产品的打样周期从数周压缩至数小时。',
    'https://apps.apple.com/cn/app/id6761676075': '利用环境微交互唤醒沉睡数字资产的优秀范例；不打扰用户注意力，在不经意的物理抬腕间创造温暖的情感共振。',
    'https://vitalsmac.com/': '重塑系统级监控信息的易读性；把冰冷的底层 PID 抽象为用户熟知的业务应用，让 Mac 极客随时洞察系统瓶颈。',
    'https://www.wallpaper.com/art/music/apple-musics-new-visual-identity-turns-sound-into-liquid-with-help-from-fred-again': '数字工业化时代对物理偶然性美学的返璞归真；拒绝纯算法渲染的塑料感，用真实物理介质构建出不可复制的高级艺术通感。',
    'https://www.designboom.com/design/steel-spheres-curved-glass-leonardo-garza-sensory-installation-byredo-matter-memory/': '五感联觉与品牌空间情绪叙事的典范；证明高维审美体验必须打破单一视听通道，通过多感官共鸣激发深层情感记忆。',
    'https://www.designboom.com/design/boss-design-the-loop-lucy-chair-circular-initiative/': '设计不仅关乎造型，更关乎产品全生命周期的物质伦理；把易维修性升华为核心美学特征，树立了工业设计的可持续标杆。',
    'https://www.dezeen.com/2026/10/21/dosorozco-casa-sima/': '人造物融入自然肌理的克制哲学；建筑不以高傲的几何体宣告征服，而是化作山林幽静对话中一个沉思的阴影。',
    'https://www.flagsmith.com/feature/experimentation-platform': '消除产品经理与开发团队在 A/B 测试上的沟通摩擦；把上线发布从“盲人摸象的开关切换”升级为“数据驱动的确定性迭代”。',
    'https://www.nativeship.io/': '中小软件借船出海的高 ROI 营销飞轮；借助主流自动化工具的庞大用户生态，让自家 API 成为万千开发者流水线里的标配积木。',
    'https://github.com/SupercmoHQ/superCMO-skills': '将千万级广告代理公司的策划方法论沉淀为可复用的代码技能；大幅降低独立开发团队与初创企业的冷启动内容营销门槛。',
    'https://www.flyweel.co/': '穿透虚荣曝光指标的底层财务清醒；帮操盘手在追逐高 ROI 增长的同时勒紧资金链缰绳，守住企业安全运营生命线。'
}

day_items = []

# 1. AI 资讯 (from vertical_data)
v_info = vertical_data['2026-10-22']
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
date: '2026-10-22'
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

out_file = 'src/content/daily/2026-10-22.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-22! Total URLs in history: {len(all_used_list)}')
