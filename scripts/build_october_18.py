# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-18': {
        'title': '10 月 18 日 · 端侧主权与协议竞合：当智能体开始清理上下文与生态壁垒',
        'highlights': '全网 9 大领域 36 篇高密度精选：DeepSeek Flash 缩短代理路径并兼容 Claude 规范、CtxWise 审计 MCP 上下文开销、端侧短信记账与苹果芯片功耗洞察、ComfyUI 图层与面部修复节点套件、40 集文旅微短剧与长篇星际科幻商业全本交割。',
        'epigraph': '软件生态的终局从来不是赢者通吃的孤岛围墙，而是协议互通的算力平权与用户对本地数据的绝对主权。',
        'lead': '10 月 18 日，大模型落地的一线战壕正在经历一场关于“效率与主权”的静悄悄革命。上半场大家还在为模型的千亿参数与百页提示词狂欢，下半场所有的工程师与独立造物者都开始精打细算：在底层架构端，DeepSeek 迭代 Flash 权重大幅压缩智能体任务的冗余路径，更在生态层主动拥抱兼容 Claude Code 规范，吹响了跨模型生态协议互通的号角；在人机协作与上下文审计端，从精准量化 MCP 描述到底占了多少 Token 的 CtxWise，到先行清洗邮件隐藏恶意指令的 InBox Wall，开发者正在用最锋利的微型工具给 Agent 瘦身与排毒；在一人公司与端侧架构端，从把记账逻辑死死锁在手机本地的 Fundstash，到底层读取苹果芯片真实功耗的 Siltop，离线与本地优先正在成为独立产品最坚固的信任护城河；在视听与内容工业端，ComfyUI 图层样式与 Impact Pack 高清修复套件将漫剧生产推向电影级精细合成，40 集文旅微短剧与长篇星际科幻全本交割，见证了 AI 协同下叙事产能的稳健落地。',
        'scene': '「为什么要把 MCP 工具的说明文档一字一句压缩？现在的上下文不是动辄上百万吗？」「因为上下文越长，模型不仅越贵，而且越容易在信息垃圾堆里走神。把每一个字节的调用说明都当成真金白银来省，你的 Agent 才能在几千次循环后依然神志清醒。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周日。

今天整理这 36 篇精选时，最让我触动的，是 **开发者们正在全面从“贪大求全”转向“极度克制”**。

以前大家拿到大模型，恨不得把几十个工具的全部 JSON Schema 一股脑塞进上下文，结果不仅账单暴涨，智能体还频繁产生幻觉、工具乱调。
而今天，我们看到 CtxWise 开始逐字节审计 MCP 描述，InBox Wall 在把邮件喂给模型前先扒掉隐形指令，DeepSeek 主动兼容竞品的规范……

这说明什么？
**AI 工具正在从“玩具期”正式迈入“工业期”。**
在真正的工程世界里，优雅从来不是你还能往里加什么，而是你再也无法从中减去任何多余的东西。

对于独立造物者和产品经理而言：
守住你的端侧数据主权，精简你的提示词与调用链路，把不可靠的黑盒概率，收敛进清爽、可控、低成本的微型闭环中。

新的一周即将开始，祝你保持清醒与定力，构筑属于你的高价值壁垒。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI LayerStyle 节点套件：图层样式、阴影色调与多图层合成控制',
                'note': '漫剧视觉后期的核心生产力插件：在节点流程中完整复刻 Photoshop 级别的图层混合模式、投影发光与调色滤镜，实现不同人物前景与虚拟背景的完美光影契合。',
                'so_what': '消灭 AI 生图画面脱节的塑料感；通过精细化图层节点调度，让复杂多角色分镜在同一光影基调下自然融合。',
                'source': 'github.com',
                'url': 'https://github.com/chflame163/ComfyUI_LayerStyle',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI Impact Pack 漫剧高清修复与面部细节重构：高精检测与分块重绘',
                'note': '影视级长篇漫剧分镜连续性的工业底盘：集成 Face/Hand Detailer 与 SAM 语义分割，自动锁定全景画面中的畸变小脸与手部微瑕进行逐像素增强。',
                'so_what': '彻底攻克远景镜头人物五官崩坏难题；把人工擦涂修复的体力活转化为全自动流水线，是规模化量产漫剧不可或缺的基石。',
                'source': 'github.com',
                'url': 'https://github.com/ltdrdata/ComfyUI-Impact-Pack',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI Easy-Use 模块化工作流：漫剧分镜与连续多模态提示词一键串联',
                'note': '降低漫剧工业化团队协作门槛的封装神器：把复杂的潜在空间采样、LoRA 权重栈与图生图管线打包为直观清晰的逻辑插槽，大幅提升跨团队资产共享效率。',
                'so_what': '告别混乱如毛线团的节点连线；高度标准化的封装使工作流成为易维护、可复用的数字资产，助小团队跑出大厂产能。',
                'source': 'github.com',
                'url': 'https://github.com/yolain/ComfyUI-Easy-Use',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《我，指挥官（第二季）》星际战争科幻微短剧：AI 辅助长篇科幻连载与商业全本交割',
                'note': '硬科幻连载竖屏微短剧商业交割范本：延续第一季星际远征世界观，借助 AI 辅助生成宏大轨道轰炸与战舰对决分镜设定，人工深度编织指挥官的孤立无援与战略抉择。',
                'so_what': '打破传统科幻特效的高昂成本围墙；证明在 AI 漫剧工业协同下，个人编剧亦能主导百集量级星际战争大戏的完整商业交割。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1922',
                'media': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《函谷关下活灵宝》40集文旅微短剧：传统历史 IP 与地方风貌的视听重构',
                'note': '微短剧赋能文旅融合的实战文本样本：以老子出关西行千古传奇为内核，巧妙串联现代灵宝风物与青年归乡创业冲突，在快节奏反转中弘扬道法自然哲学。',
                'so_what': '政策导向文旅短剧的破局范本；把地方特产与历史典故自然编织进戏剧冲突，摆脱枯燥宣传片说教，实现艺术性与商业价值的双向奔赴。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1937',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《钢的琴（音乐剧文学剧本）》：工业文明退场后的温情叙事与荒诞解构',
                'note': '关山经典音乐剧文学剧本深度复盘：面对重工业浪潮退去的锈蚀残局，一群小人物用钢铁铸造音乐梦想，以极具节奏感的歌词与荒诞对白反抗生活重压。',
                'so_what': '文学剧本的戏剧张力来自骨子里的倔强；在悲怆现实中注入歌舞狂欢的抒情反差，展示了经典华语音乐剧的文本分量。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1935',
                'media': 'https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《中年迷途》现实主义家庭伦理剧：多重视角下的信任危机与逆境突围',
                'note': '当代都市家庭剧的矛盾编织心法：剥离悬浮的豪门滤镜，直面中年职场裁员、婚姻倦怠与养老托育的多重现实困境，以精密因果逻辑推演角色的绝望与觉醒。',
                'so_what': '写扎实的现实主义而不是廉价狗血；唯有洞悉平凡人的隐忍与软弱，在层层冲突后给予合乎人性的救赎，才能引发主流受众的广泛情感共振。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1920',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '“剧说宝鸡”小剧场剧本征集启事：文旅深度融合下的剧作扶持与商业孵化',
                'note': '官方剧作专项扶持政策深度解读：聚焦周秦文化、青铜器之乡与民间民俗，面向全国征集适合沉浸式小剧场、实景演艺与微短剧拍摄的优质剧本，提供全链条版权孵化。',
                'so_what': '敏锐捕捉地方政府与文化基金的扶持风向；将剧本创作与特定文化场域定制绑定，是一人编剧团队稳定变现的重要渠道。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1761',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': 'DeepSeek Harness 为什么要兼容 Claude Code Mods：智能体生态标准的生态竞合',
                'note': 'AI 工具链协议之争的深度拆解：面对 Anthropic 凭借 Claude Code 建立的高黏性开发者心智，国产开源基座选择主动向下兼容其扩展协议，以生态开放换取市场份额。',
                'so_what': '在生态建立初期，兼容事实标准比自造方言更能赢得用户；产品经理在设计扩展架构时，应优先拥抱主流社区协议以降低迁移阻力。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6473810.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '大模型基座激战：Gemini 4、GPT-6 Astra 与 Claude Opus 5.5 的参数天花板',
                'note': '顶尖大模型迭代范式前瞻：从单纯卷预训练参数量，全面转向后训练强化学习（RLVR）、复杂环境长程推理与物理多模态联合对齐，大厂护城河正在重构。',
                'so_what': '看清底层技术更迭的真实代际；不要被营销公关词汇迷惑，产品经理需建立科学评测集，紧扣真实业务场景的完成率做选型。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473111.html',
                'media': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '中国大模型落地深水区：阶跃星辰与垂直产业梯队的真伪自嗨辨析',
                'note': '商业化变现与烧钱故事的冷酷拷问：在大模型通用能力平权后，垂直独角兽若不能在金融、消费或具身智能等具体产业跑通正向现金流，将迅速面临断粮危机。',
                'so_what': '业务场景的深度比通用参数更值钱；做深水区产品，必须敢于走出舒适圈深入产业毛细血管，用硬核 ROI 证明自身不可替代性。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473079.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '自我递归改进（RSI）是否真正来临？从基座演化看智能体架构范式转移',
                'note': '算法自我迭代机制的工程推演：当模型能够自主生成合成数据、构建评测反馈并持续微调自身代码时，传统瀑布式软件工程将被“模型自主飞轮”彻底颠覆。',
                'so_what': '重新定义人机分工界面；产品经理的角色正在从“功能设计者”蜕变为“算法演化环境与评价指标的裁判员”。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473500.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-18.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Select curated items for the 6 ian categories
curated_ian_picks = {
    'AI 资讯': [
        'https://api-docs.deepseek.com/news/news261017/',
        'https://github.com/SRKRZ23/vramkit',
        'https://llmspeed.dev/',
        'https://github.com/ziuus/goroute'
    ],
    'AI 协作': [
        'https://github.com/FramY2/ctxwise',
        'https://github.com/Annora998/inboxwall',
        'https://github.com/markphelps/offscreen',
        'https://github.com/bimal1023/agentfork'
    ],
    '一人公司': [
        'https://fundstash.app/',
        'https://github.com/CLoaKY233/siltop',
        'https://fourcities.app',
        'https://heytamo.com/'
    ],
    '产品设计': [
        'https://gridmark.dev/',
        'https://pomoflow.pages.dev/',
        'https://github.com/zeuros/gitgud',
        'https://caldera.social/'
    ],
    '审美提升': [
        'https://www.dezeen.com/2026/10/17/snohetta-shanghai-grand-opera-house/',
        'https://www.wallpaper.com/art/music/lighting-designers-tobias-rylander-and-michael-straun-interview',
        'https://www.designboom.com/art/laboratory-waste-art-discarded-research-prototypes-sculptural-objects-ruben-moutinho/',
        'https://www.wallpaper.com/design-interiors/interior-accessories/virginia-sin-metal-objects-ritual-collection'
    ],
    '产品营销': [
        'https://draper.chat/',
        'https://forgemesh.io/blog/pay-per-crawl-every-stack',
        'https://github.com/abhij1306/CiteLadder',
        'https://themesfor.app/'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://api-docs.deepseek.com/news/news261017/': '智能体推理路径的压缩是降低商业化调用成本的关键；模型厂商主动优化代理多轮调用的延迟与冗余词元，标志着模型迭代重心向生产环境加速靠拢。',
    'https://github.com/SRKRZ23/vramkit': '权重无损量化与 KV 缓存精简是端侧工作站的生命线；分离开权重与缓存的量化指标，让个人开发者更清晰地评估真实长文本推理损耗。',
    'https://llmspeed.dev/': '打破纯参数硬件对标的迷思；用直观可感知的打字速率取代冰冷跑分，为开发者评估本地部署的可交互性提供了敏捷参考。',
    'https://github.com/ziuus/goroute': '网关标准化是系统容灾的基石；统一多厂商 API 协议与智能故障倒换，避免了业务系统与单一云端模型强绑定。',
    'https://github.com/FramY2/ctxwise': 'MCP 工具调用的隐性成本治理开端；在向 Agent 挂载工具前审计 Schema 消耗与安全凭证，是防范上下文膨胀与越权泄露的第一道门禁。',
    'https://github.com/Annora998/inboxwall': '间接提示词注入（Indirect Prompt Injection）的实战防线；在智能体读取非受信外部邮件时清洗隐形控制符，守住自动化系统的安全底线。',
    'https://github.com/markphelps/offscreen': '给 GUI 自动化代理搭建纯净的无菌操作台；在独立沙箱虚拟机中隔离跑测试，杜绝了多代理并发抢占主屏光标与窗口焦点的噩梦。',
    'https://github.com/bimal1023/agentfork': '复杂 Agent 调试的最佳实践是分叉回溯；利用前序缓存从崩溃断点定点重放，将智能体长链路排错的算力开销降到最低。',
    'https://fundstash.app/': '极度清醒的隐私优先设计哲学；端侧解析金融短信并闭环记账，精准击中对云端泄露心存忌惮的理财人群刚需。',
    'https://github.com/CLoaKY233/siltop': '硬核极客工具的极简交付范式；零配置、无侵入式读取底层微架构状态，展示了纯粹技术沉淀转化为高价值工具的单兵爆发力。',
    'https://fourcities.app': '克制而深邃的微型独立游戏美学；无需账号、即开即玩的轻量博弈逻辑，展现了一人公司单兵打磨自足体验的从容定力。',
    'https://heytamo.com/': '将智能体交互彻底无缝融入已有社交心流；利用成熟 IM 协议接管日常琐事，降低用户下载安装新应用的决策门槛。',
    'https://gridmark.dev/': '几何秩序与生成式创意的完美咬合；在严苛网格骨架下探索标志形态，把专业设计参数的调优过程变得极其可玩与确定。',
    'https://pomoflow.pages.dev/': '反向对抗界面臃肿的极简胜利；用像素复古美学与离线无账号机制，还给专注工作者最纯粹的节奏掌控感。',
    'https://github.com/zeuros/gitgud': '高密度代码管理界面的交互范式创新；把提交脉络图与行内差异补丁无缝编排在同一视口，消灭跨页来回跳转的认知负荷。',
    'https://caldera.social/': '击碎中心化笔记平台的圈地自萌；基于本地 Markdown 原生生长的公开数字花园，展示了个人数字资产从孤岛走向联邦的可行路径。',
    'https://www.dezeen.com/2026/10/17/snohetta-shanghai-grand-opera-house/': '公共文化地标与市民日常生活的温柔缝合；连续渐进的螺旋坡道将剧场屋顶重塑为可步行的江岸观景台，消解了高雅艺术殿堂的阶级距离感。',
    'https://www.wallpaper.com/art/music/lighting-designers-tobias-rylander-and-michael-straun-interview': '巨型场馆中微观情感张力的重构心法；借助投影与白幕的虚实层叠，在万人工业体育馆中营造出如卧室般贴近耳语的私密诗意。',
    'https://www.designboom.com/art/laboratory-waste-art-discarded-research-prototypes-sculptural-objects-ruben-moutinho/': '对技术狂飙历史的物质性审视；将报废的高精尖研发零件切片重组为雕塑，在人造废弃物中凝固现代工业的残余诗性。',
    'https://www.wallpaper.com/design-interiors/interior-accessories/virginia-sin-metal-objects-ritual-collection': '传统手工陶泥语言向现代工业金属的优雅转译；用冷冽不锈钢还原温润手捏褶皱，在材质冲突中重塑了日常器皿的分量。',
    'https://draper.chat/': '在写下第一行代码前做实需求伪命题检验；用系统化的用户意向访谈代替盲目建站投放，把创业团队最宝贵的时间留给真刚需。',
    'https://forgemesh.io/blog/pay-per-crawl-every-stack': '数据资产商业化定价权的新探索；将高质量技术站点的单页爬取转变为微付费门槛，探索抗衡 AI 免费白嫖清洗的防御性基建。',
    'https://github.com/abhij1306/CiteLadder': '生成式搜索时代（GEO）品牌可见性的量化标尺；追踪大模型在解决用户购买意向时的引用权衡，为下半场品牌获客构筑情报雷达。',
    'https://themesfor.app/': '轻量化营销阵地的极速冷启动；抛弃沉重 CMS 系统，用自托管纯静态模板在数分钟内搭建高转化线索捕获站。'
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
v_info = vertical_data['2026-10-18']
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
date: '2026-10-18'
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

out_file = 'src/content/daily/2026-10-18.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-18! Total URLs in history: {len(all_used_list)}')
