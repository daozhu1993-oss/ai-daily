# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-23': {
        'title': '10 月 23 日 · 极简闭环与边界收敛：当智能体开始学会“退回主循环”',
        'highlights': '全网 9 大领域 36 篇高密度精选：Anthropic 深度拆解何时把子代理收回主循环、OpenAI 正式开放高频小决策 API、腾讯司内实践揭秘员工如何用 Skill 撬动全员 AI 协作、微信挟流量入局短剧分发变局、ComfyUI 电影级调色视听管线全案交割。',
        'epigraph': '多智能体的繁复网络往往是工程混乱的伪装；最高明的架构师从不迷信层层派发，而是在最恰当的时机，果断把复杂的子系统收回精简的主循环。',
        'lead': '10 月 23 日，大模型工程落地与 Agent 架构设计正在集体迎来一场深刻的“反思与收敛”。在经历了多代理系统（Multi-Agent）相互套娃调用的膨胀狂欢后，头部团队开始用血淋淋的生产账单与调试痛苦反思架构复杂度：Anthropic 官方工程博客重磅发布架构长文，系统性解答“何时该把子代理收拢回主智能体循环”，揭示过度分工导致的上下文重复膨胀与调试黑洞；OpenAI 则顺势正式商用开放限定选项的高频小决策 API，将路由与分类成本压至微秒与分厘级；在企业协同与产品操盘一线，腾讯司内实践全面公开了普通员工如何用可复现的 Skill 模块化接管高频业务，微信与抖音在微短剧分发战场的正面交锋更宣告了粗放流量变现时代的终结；在视听生成前线，伴随着数字人主播在双十一前夜的大规模离场，行业彻底告别伪需求自嗨，全面拥抱以 ComfyUI 电影级节点与鲁迅经典文学短剧改编为代表的工业化重度交付。',
        'scene': '「我们给系统设计了七个互相协作的子 Agent，为什么客户的问题还是经常在中间被踢皮球弄丢？」「因为每一次跨 Agent 的代理调用，本质上都是一次昂贵且充满损耗的上下文重述。把能内聚的逻辑做成确定性 Skill 收回主循环，你的系统才会拥有真正的执行力。」',
        'cover': 'https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周五。

今天整理这 36 篇精选时，最让我产生共鸣的，是 **Anthropic 对“智能体收敛与克制”的深层反思**。

过去一年里，行业充斥着各种花哨的多智能体拓扑图：
一个主管 Agent，派发给三个规划 Agent，再向下调度十几个微型工具 Agent……
纸面上看极其智能，真正放到生产环境，却经常变成互相推诿、账单暴涨、假死不知所措的灾难现场。

Anthropic 的工程师给出了极其清醒的判断：
**很多时候，你根本不需要那么多独立的子代理。把任务提炼成干净可控的 Skill，收回一个强悍的主循环中，系统的稳健度和执行速度反而会成倍跃升。**

做系统是这样，做产品与做商业亦是如此：
不要用战术上的复杂，去掩盖战略上的摇摆。
越是面对不确定性，越要把核心能力收拢收敛，做到极简、闭环与致命的扎实。

愿你在今天的造物中，学会给架构做减法，把最重要的精力留给刀刃上的真实交付。周末愉快！''',
        'ai_news': [
            {
                'category': 'AI 资讯',
                'title': 'OpenAI 把限定答案的小决策接口正式开放',
                'note': '面向高频业务路由的小决策商业 API：支持返回概率、预设选项与多维评分，单次批量可处理四百问，原生集成实时语音与上下文缓存，适合超低延迟分类过滤。',
                'so_what': '打破通用大模型做简单分类的算力浪费；用极轻量低价的小决策接口替代昂贵的端到端生成，为高吞吐业务路由卸载 80% 算力开销。',
                'source': 'openai.com',
                'url': 'https://openai.com/index/decisions-api',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'Sierra 用姓名和号码测试语音代理基本功',
                'note': 'Bret Taylor 创立的语音 Agent 独角兽发布的最新测试基准：设计 200 个横跨十类复杂实体信息的任务，严苛对比宁静、环境噪声与人声插话干扰下的识别与记忆留存。',
                'so_what': '直击企业级语音智能体商业交付的核心命门；只有在嘈杂现实中保持关键数字与实体零差错，语音 Agent 才能真正接管真实的售后电话。',
                'source': 'sierra.ai',
                'url': 'https://sierra.ai/blog/tau-entity-can-voice-agents-get-the-details-right',
                'media': 'https://iandaily.xyz/digest/2026-10-23-tauentity-bdf396f5f393.jpg',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': '外部研究者披露代理监控系统的压力测试',
                'note': '前沿机构 METR 与 Redwood 对高级自动化代理长达三周的高权限红队攻防复盘：深入测试监控系统在多步隐蔽越权、环境嗅探与权限绕过中的防御盲区。',
                'so_what': '给自主智能体的大规模企业内放行敲响警钟；光看单步防护远远不够，必须建立跨会话全周期的多重交叉审计机制。',
                'source': 'blog.redwoodresearch.org',
                'url': 'https://blog.redwoodresearch.org/p/red-teaming-openais-internal-agent',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 资讯',
                'title': 'Decido 把文档小决策搬到笔记本 CPU',
                'note': '完全离线运行的轻量决策与分类开源套件：专门针对文本是非判断、多选分类与置信度评分进行微调，仅需数十 GB 内存即可在纯 CPU 环境下跑出毫秒级响应。',
                'so_what': '敏感文档处理去云端化的理想基底；在保障绝对数据安全的前提下，让法务与合规团队在普通本地工作站上完成大规模初筛。',
                'source': 'github.com',
                'url': 'https://github.com/decido-ai/decido',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI Movie Tree Blocks：漫剧制片级动态调色与视听同步高级节点',
                'note': '专业短剧视觉管线的电影级节点合集：提供 ACES 颜色空间无损转换、多机位动态镜头虚化、长视频多轨道音频波形与画面帧同步对齐，彻底告别单图拼凑感。',
                'so_what': '让 AI 生成真正具备院线级视听质感；用电影工业的标准色彩与镜头语法赋能漫剧团队，构建不可逾越的制作壁垒。',
                'source': 'github.com',
                'url': 'https://github.com/melMass/comfy_mtb',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '短剧“变天”！微信绿泡泡挟流量入局，红果告别“看剧赚金币”',
                'note': '微短剧分发格局重构的深度透视：巨头携庞大社交关系链直接下场，粗放的网赚撒币买量模式迅速失效，精品化叙事与垂直分发成为下半场生死线。',
                'so_what': '渠道红利向内容品质红利的深刻迁移；AI 漫剧创作者不能只依赖投流算法，必须打造具有社交裂变能力的真实好内容。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6483429.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '“双十一”前夜，阿里云虚拟数字人为何退场？',
                'note': '大厂对虚拟人商业化泡沫的果断止损复盘：僵硬的语音互动与高昂的定制算力成本难以承接复杂的真实带货转化，行业开始转向更有温度与实效的轻量生成方案。',
                'so_what': '走出虚拟制片造神滤镜的清醒解药；技术必须贴近真实 ROI，盲目堆砌高大上形象不如在漫剧和实景短视频中解决具体转化。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6483144.html',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《祝福》经典文学改编微短剧：传统经典在 AI 漫剧时代的人性共鸣与工业化分镜全案',
                'note': '严肃文学 IP 改编为高密度微短剧的开创性剧作全本：保留鲁迅原作深刻的人性悲悯与封建礼教批判，结合现代快节奏视听分镜语言，打造具有文化厚度的漫剧标杆。',
                'so_what': '公版严肃文学在微短剧赛道的价值重估；用经典文学骨骼摆脱快餐爽剧的低俗泥潭，开辟微短剧精品化的高维通路。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1784',
                'media': 'https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《兰陵王入阵曲》历史古装短剧：英雄史诗与悲壮宿命的戏剧弧光构建',
                'note': '宏大历史题材在微短剧篇幅下的剧作剖析：通过狰狞面具与清秀面容的强烈戏剧反差，将家国保卫战与宫廷权谋猜忌紧密交织，构建出荡气回肠的悲剧史诗感。',
                'so_what': '历史传奇题材的人物弧光塑造范本；避免平铺直叙的历史记叙，用极致的情感羁绊与宿命对抗紧紧抓住观众心弦。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1799',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《系统求求你》轻喜剧短剧：系统流逆袭与荒诞包袱的节奏铺设',
                'note': '爆款网络流行设定的喜剧化剧作拆解：当金手指系统频频发布坑爹任务与不靠谱惩罚，主角如何在荒诞尴尬中绝地求生，密集反转与自嘲包袱层出不穷。',
                'so_what': '把流行爽文套路反套路化的解题思路；用无厘头喜剧解构严肃冲突，为同质化严重的系统流短剧注入全新的爆笑生机。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1785',
                'media': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《富妈妈穷妈妈》荒诞喜剧短剧：家庭代际冲突与教育焦虑的戏剧化解构',
                'note': '现实题材微短剧的情绪爆破力解析：将不同阶层的育儿理念与虚荣攀比推向荒诞极致，在鸡飞狗跳的喜剧冲突中层层揭开当代家庭的情感真相与真实温情。',
                'so_what': '社会热点议题在短剧创作中的敏锐捕捉；用幽默包袱包裹锋利社会观察，既有极高的话题传播度，又具备回味深长的现实厚度。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1800',
                'media': 'https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '《泣阳之泪》（81集古装短剧）：黑白无常神话新编与虐恋叙事范本',
                'note': '传统东方志怪民俗的现代剧作重塑：颠覆传统勾魂使者的脸谱化形象，赋予黑白无常前世纠葛与人间温情，以宿命轮回为动力推动虐恋故事步步升级。',
                'so_what': '东方神话 IP 现代重塑的情感催化技法；将玄幻民俗世界观与细腻言情深度咬合，为古装垂类短剧开辟高黏性吸粉路径。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1787',
                'media': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '深度讨论 Personal Agent：“最互联网”的 AI 命题',
                'note': '个人智能体商业与产品逻辑的底层推演：探讨当 Agent 拥有个人全部历史上下文与执行授权时，传统搜索引擎、应用商店与操作系统的分发入口将被如何彻底颠覆。',
                'so_what': '未来十年互联网核心入口迁移的战略思考；产品经理必须思考自身业务如何成为 Agent 调用链条中不可替代的终点履约节点。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6483579.html',
                'media': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '腾讯司内实践：手把手教你如何用 Skill 与 AI 协作',
                'note': '大厂一线员工自发推动 AI 生产力落地的宝贵复盘：不等待顶层架构设计，从写文档、做数据分析与需求初筛等具体卡点切入，将高频经验沉淀为可被团队共享的标准化 Skill。',
                'so_what': '从“个人用 AI 聊天”到“团队用 Skill 固化生产力”的关键跨越；为企业推进 AI 协同落地提供了极具参考价值的自下而上范本。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6483517.html',
                'media': 'https://images.unsplash.com/photo-1556742049-0a67e557224d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '在武装押运行业做产品：一个没有竞品可抄的B端复盘',
                'note': '重度特种行业数字化建设的极限实战记录：面对军工级安防要求、极端网络环境与严苛物理流程，产品经理如何在零竞品参考下深入现场梳理业务蓝图。',
                'so_what': 'B端产品经理核心硬实力的极致体现；脱离消费互联网的大厂套路，深入物理世界最复杂的业务现场才是产品人不可替代的护城河。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pd/6483392.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '对话 Google Labs 负责人：大团队正在拖垮 AI 产品创新，我们用 2-3 个人、100 天验证一个方向',
                'note': '硅谷顶尖实验室反官僚主义敏捷孵化哲学的深度对话：在 AI 时代，大兵团作战反而因冗长审批与政治博弈失去敏锐度，精简的全栈敏捷特种兵才是验证创新的最优解。',
                'so_what': '打破大厂资源迷信的清醒剂；给予一人公司与微型创业团队巨大的信心，在 AI 杠杆赋能下，小团队完全具备颠覆庞大组织的创新敏捷度。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6483070.html',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

# 2. Curated Ian picks (20 items across 5 categories)
raw_ian_path = 'scripts/raw-ian-23.json'
with open(raw_ian_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

curated_ian_picks = {
    'AI 协作': [
        'https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop',
        'https://www.heal.dev/',
        'https://resend.com/products/inboxes',
        'https://github.com/anishchugh05/mnemolith'
    ],
    '一人公司': [
        'https://hookman.dev/',
        'https://deskypaw.app/',
        'https://calends.date',
        'https://blisswriter.app/'
    ],
    '产品设计': [
        'https://kino.ai/tools/transcode',
        'https://microsoft.github.io/flint-chart/',
        'https://shapcn.com/',
        'https://deepcell.net/'
    ],
    '审美提升': [
        'https://www.designboom.com/technology/tune-x3-headphones-pressec-vintage-studio-equipment/',
        'https://www.dezeen.com/2026/10/22/jonathan-corral-arquitectos-uad-alamedas-durango/',
        'https://www.designboom.com/design/molo-softwall-flexible-light-responsive-paper-partition-system/',
        'https://www.designboom.com/art/hayden-clay-williams-everyday-objects-stained-glass-sculptures-surrealism/'
    ],
    '产品营销': [
        'https://ahrefs.com/blog/headless-content-marketing/',
        'https://markdown2x.com/zh',
        'https://causo.ai/',
        'https://ugcpeople.com'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://claude.com/blog/building-agents-when-to-fold-subagents-into-your-main-agent-loop': '终结对 Multi-Agent 架构的盲目崇拜；用奥卡姆剃刀原则给智能体系统做减法，让 Agent 的执行确定性与推理成本实现质的跃迁。',
    'https://www.heal.dev/': '把软件工程 Agent 从静态猜测升级为动态实证；消灭“看着逻辑没错但一跑就挂”的假死 Bug，大幅缩短端到端修复交付周期。',
    'https://resend.com/products/inboxes': '把被动邮件转化为智能体的主动工作流；为人机协作提供了一个天然符合人类商业直觉的统一交互界面。',
    'https://github.com/anishchugh05/mnemolith': '破解 Agent 长期记忆污染的硬核方案；用版本树绑定上下文生命周期，让智能体的认知与现实代码库时刻保持强一致性。',
    'https://hookman.dev/': '解决单兵开发者多分支调试 Webhook 的高频痛点；告别反复配置 ngrok 与换域名的繁琐操作，把宝贵精力留给核心功能开发。',
    'https://deskypaw.app/': '小而美情绪价值工具的经典变现样本；拒绝生硬的功能堆砌，用恰到好处的情感陪伴与买断制定价赢得海外独立开发者的喜爱。',
    'https://calends.date': '把财务主权牢牢抓在自己手中的极客利器；告别第三方账本的数据泄露隐患，清晰度量跨币种出海运营的真实净现金流。',
    'https://blisswriter.app/': '将现代版本控制思想嫁接到内容创作；消灭创作者对修改好段落的患得患失，极大释放剧情探索的灵感自由度。',
    'https://kino.ai/tools/transcode': 'Web 平台图形与算力潜能的极致释放；消灭安装笨重本地后处理软件的高门槛，让影视后期流水线具备即开即用的轻盈手感。',
    'https://microsoft.github.io/flint-chart/': '数据可视化工程的解耦革新；让 AI 生成交互式分析看板不再受限于繁复的 SVG 样式代码，大幅提升数据可视化的组件化复用率。',
    'https://shapcn.com/': '在像素级微交互中注入物理呼吸感；消除生硬的状态跳变，用优雅的视觉反馈抚平用户的等待与操作焦虑。',
    'https://deepcell.net/': '终结数据更新后的“人肉复制粘贴”噩梦；把数据源、叙述逻辑与展示物料串成一条活的管道，重塑企业分析资产的交付范式。',
    'https://www.designboom.com/technology/tune-x3-headphones-pressec-vintage-studio-equipment/': '触觉物理反馈对触屏虚拟滑块的有力反击；在高度同质化的数码产品中重新找回老式仪器的机械厚重感与操控仪式感。',
    'https://www.dezeen.com/2026/10/22/jonathan-corral-arquitectos-uad-alamedas-durango/': '历史文脉在现代建筑语汇中的高级转译；证明真正的在地设计不是简单照搬古迹皮毛，而是用当代结构唤醒深层的空间精神。',
    'https://www.designboom.com/design/molo-softwall-flexible-light-responsive-paper-partition-system/': '纸张材料对刚性墙体空间的轻量颠覆；赋予商业空间极其轻盈的流动性与光影透气感，树立了模块化空间美学的新典范。',
    'https://www.designboom.com/art/hayden-clay-williams-everyday-objects-stained-glass-sculptures-surrealism/': '材料错位带来的深层审美冲击；用崇高神圣的传统工艺包裹转瞬即逝的工业垃圾，引发人们对日常造物价值的深刻审视。',
    'https://ahrefs.com/blog/headless-content-marketing/': '内容营销下半场的规则剧变；只有提供不可替代的一手实验数据、独特观点与严谨事实，才能在 AI 生成时代守住品牌的认知心智。',
    'https://markdown2x.com/zh': '消除技术内容跨平台分发时的格式错乱痛点；把枯燥的排版耗时压缩至秒级，让高价值专业思考迅速转化为全网分发资产。',
    'https://causo.ai/': '在红海获客中另辟蹊径的精准打击战术；用多维弱信号交叉验证真实业务需求，以极低营销成本撬动高单价企业合约。',
    'https://ugcpeople.com': '用模块化工业思维解构爆款短视频广告；精准利用黄金三秒抓住受众注意力，大幅降低信息流广告起量的测试成本。'
}

day_items = []

# 1. AI 资讯 (from vertical_data)
v_info = vertical_data['2026-10-23']
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
date: '2026-10-23'
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

out_file = 'src/content/daily/2026-10-23.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-23! Total URLs in history: {len(all_used_list)}')
