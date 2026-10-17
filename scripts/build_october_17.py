# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-17': {
        'title': '10 月 17 日 · 确定性护栏与微型闭环：当智能体开始直面物理现实与商业收敛',
        'highlights': '全网 9 大领域 36 篇高密度精选：Google 用数字孪生约束生物湿实验 Agent、ComfyUI 接入 Krea 3 伙伴节点、Anthropic 追查加密曲线历史根源、互联网保险合规风暴下的产品底牌、120 集太空战微短剧商业全本交割。',
        'epigraph': '智能体的终局绝不是任由概率在黑盒里狂奔，而是给奔腾的算法套上一层层严谨的物理孪生校验、密钥隔离防线与确定性商业收敛。',
        'lead': '10 月 17 日，周末的技术前沿正在呈现一种高度理性的“收敛姿态”：AI 的狂飙突进终于开始撞上严苛的物理规律与商业红线。在基础模型与安全攻防端，谷歌研究团队公布重磅成果，用高精度数字孪生与生化法则作为硬约束，严格规范智能体在湿实验机器人中的执行路径，标志着 Agent 正在从写诗做题迈向直面物理现实的深水区；在协作与生态工具端，ComfyUI 正式将 Krea 3 接纳为官方伙伴节点，无级生成画布与节点式调度融为一体，宣告了视听生产力工具链的大整合；在一人公司与产品营销一线，从把电子签名颠覆为“成功签完才扣费”的 SignWith，到 TechCrunch 复盘 Cal AI 依靠细分 KOC 矩阵撬动超高 ROI 的增长实操，无一不在提醒造物者：单向堆砌技术已无法带来溢价，极致克制的商业闭环与离线主权才是生存之本；在视听与戏剧创作工业端，话剧《钢的琴》与小剧场《每一件美妙的小事》深度复盘了小人物在时代浪潮下的尊严与治愈母题，而 120 集硬核太空舰队战微短剧《湮灭舰队》的全本商业交割，展现了 AI 辅助长篇科幻连载的工业化产能。',
        'scene': '「现在的 Agent 只要给够权限，什么脚本都能跑，为什么还要在外面套一层数字孪生？」「因为现实物理世界没有撤销键（Ctrl+Z）。把有毒试剂混在一起会爆炸，在没有验证的链路上跑交易会破产。算法越自主，护栏就必须越坚固。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周六。

今天整理这 36 篇精选时，最让我陷入深思的，是 **Google 尝试用数字孪生给生物实验室的智能体“立规矩”**。

在纯虚拟的文本框里，大模型产生幻觉，大不了多按一次重新生成；
但当智能体开始接管生化机械臂、操控真实的电网开关、或者代替企业签署法律合约时，**概率就是毒药**。

任何一个不符合物理化学规律的盲目试错，都可能带来不可逆的现实灾难。

这对于所有做应用层、做独立开发的产品人来说，也是最深刻的警醒：
不要把“一切全交给 AI 自由发挥”当成创新的卖点。
客户之所以愿意为专业软件付钱，恰恰是因为你的系统能在不可靠的概率外面，套上一套确定性的业务逻辑、合规审查与容灾兜底。

把天马行空的灵感收拢为可控可审计的确定性资产。
那些敢于给算法立规矩的系统搭建者，才能真正赢得商业世界的长久信任。

祝你周末充实。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI 把 Krea 3 接成可组合的伙伴节点：官方打通实时无级画布与节点工作流',
                'note': '漫剧视听工具链里程碑整合：ComfyUI 官方博客宣布与 Krea 深度打通，支持在复杂节点树中无缝嵌入 Krea 3 的实时无级画布，在节点运行间隙直接交互微调。',
                'so_what': '节点自动化与所见即所得画布不再割裂；为漫剧创作者提供了兼具大批量管线生产与单帧精细交互的混合制片体验。',
                'source': 'blog.comfy.org',
                'url': 'https://blog.comfy.org/p/krea-3-is-now-available-via-partner',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-Advanced-ControlNet 高阶控制网调度套件：多重约束分层衰减与透视锁死',
                'note': '漫剧长篇分镜透视与动作控制的基石：支持给不同 ControlNet 施加独立的步数权重衰减曲线与软遮罩，彻底杜绝多重条件叠加导致的画面烧焦与畸变。',
                'so_what': '精细化分层控制是高品质漫剧交付的关键；掌握权重滑动插值，才能在复杂光影镜头中稳定锁定角色肢体动态。',
                'source': 'github.com',
                'url': 'https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-Gemini 漫剧多模态剧本与分镜提示词生成节点：长文本直接解析结构化分镜',
                'note': '剧作文本向视听语言转化的桥梁：利用多模态推理能力，自动将编剧提交的长篇小说或微短剧剧本逐幕拆解为景别、运镜、角色表情与光影提示词。',
                'so_what': '消除人工拆分镜头的巨大体力损耗；让编剧用自然语言创作，系统自动转化为扩散模型可识别的工业级分镜指令。',
                'source': 'github.com',
                'url': 'https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《湮灭舰队》太空舰队战微短剧 全 120 集：AI 辅助创作与竖屏短剧全本商业交割',
                'note': '硬科幻太空舰队战微短剧商业交割样本：全 120 集每集 1 分钟竖屏剧本，借助 AI 快速搭建星际战舰火力参数与宏大宇宙战役世界观，人工深度打磨舰桥群像对峙。',
                'so_what': '大制作科幻题材在短剧赛道实现低成本破局；用 AI 快速消化繁复的机械设定，大幅释放了编剧的情感叙事精力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1757',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '钢的琴（话剧）：底层小人物的悲欢叙事与尊严救赎',
                'note': '中国当代现实主义话剧经典文本复盘：面对工业时代转型的残酷阵痛，下岗工人们用废钢铁为女儿纯手工打造一架真正的钢琴，用荒诞幽默守望底层尊严。',
                'so_what': '戏剧力量来自对生活真实的敬畏；不煽情、不恶俗，在灰暗现实中淬炼出最硬核的人性温情与生命尊严。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1936',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '每一件美妙的小事：小剧场互动式治愈母题解构',
                'note': '现象级单人剧作结构心法：以一个孩子为对抗母亲抑郁症而列下的快乐清单为线索，让观众直接参与戏剧演出，在生活细碎缝隙中打捞不可磨灭的光亮。',
                'so_what': '互动性是小剧场的灵魂；打破第四堵墙，将私人痛苦转化为全场共鸣的集体疗愈，是极具穿透力的高概念叙事。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1921',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '青蛇：传统志怪神话的现代性颠覆与女性意识觉醒',
                'note': '田沁鑫经典舞台文学构思拆解：彻底跳脱白蛇传传统劝善惩恶俗套，以懵懂叛逆的小青冷眼旁观人间欲望与伪善，重构关于情爱、执念与自我解放的思辨。',
                'so_what': '经典改编重在现代灵魂注入；以边缘角色的叛逆视角反思主流叙事，才能赋予传统 IP 历久弥新的思想锐度。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1754',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '舟山市影视艺术产业协会短剧/网剧原创剧本征集细则：海岛文旅与地方特色破局',
                'note': '地方影视产业定制需求解析：面向全国公开征集原创短剧与网剧剧本，带有海岛人文、海洋非遗与避暑旅游特色的题材享有优先评审与全流程拍摄扶持。',
                'so_what': '文旅短剧进入政策红利深水区；将故事类型冲突与地方风貌深度绑定，是商业剧本快速立项变现的确定性通道。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1762',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '蚂蚁保、腾讯微保、京东保、众安保险：十不得之下，谁是真王者？',
                'note': '金融科技强监管时代的产品重构推演：监管严厉叫停销售误导与捆绑诱导后，互联网保险产品从“拼流量转化漏斗”被迫转向“拼真实理赔体验与条款透明度”。',
                'so_what': '合规是检验商业模式的试金石；靠信息差赚快钱的时代终结，深筑长期信任底盘的产品才能在监管洗牌中胜出。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/share/6473878.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目：工具演进与基础设施新趋势',
                'note': '前沿开发者生态全景扫描：从本地轻量化模型调度网关，到自动化沙箱与开发者辅助插件，开源社区的聚焦点正在从通用大模型加速转移到微型执行管道。',
                'so_what': '跟着开源社区的脚印选型；不要重复造轮子，敏锐借助高星级开源底座构建垂直业务，是独立产品极速交付的秘诀。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/share/6473850.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '又一 Personal Agent 发布，帮我省下不止 200 刀：个人代理系统架构与任务闭环',
                'note': '个人自动化智能体一线操盘实操：避开臃肿的企业级中间件，用轻量 Python 脚本结合模型 API 实现跨应用数据搬运与发票整理，真实量化时间与资金 ROI。',
                'so_what': '做实用的 Agent 而非炫技的玩具；从自己每天被恶心半小时的高频机械任务切入，做出来的产品最具生命力。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473806.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '订阅了 GPT 怎么用才划算？ChatGPT 与 Codex 双引擎协同心法与 ROI 核算',
                'note': '资深产品人高阶工具流复盘：拒绝无序闲聊，明确分工让通用大模型负责方案意图推演，让代码专用模型负责结构化交付与规则校验，算清每月 20 刀的生产力产出。',
                'so_what': '工具价值取决于使用者的意图清晰度；建立严格的任务分流机制，才能让每笔微小订阅撬动数十倍业务杠杆。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473198.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-17.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Select curated items for the 6 ian categories
curated_ian_picks = {
    'AI 资讯': [
        'https://ollama.com/blog/reflection-beam',
        'https://www.anthropic.com/research/ecdsa-curve-origins',
        'https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/',
        'https://github.com/ValerioDolci/capy-flash'
    ],
    'AI 协作': [
        'https://www.conifer.build/parallax/',
        'https://usebeeline.app',
        'https://gbrain.io/tools',
        'https://github.com/paveo-dev/paveo'
    ],
    '一人公司': [
        'https://downcheck.dev/',
        'https://apps.apple.com/us/app/ptrace-run-tracker/id6785292238',
        'https://github.com/devYRPauli/putaway',
        'https://caseblossom.com/'
    ],
    '产品设计': [
        'https://www.trytaim.com/',
        'https://github.com/elmsec/eqmini',
        'https://wayseer.app/',
        'https://toolbit.app/'
    ],
    '审美提升': [
        'https://www.designboom.com/architecture/saint-of-athens-peace-chaos-boutique-monochromatic-high-contrast-zones-thessaloniki/',
        'https://www.dezeen.com/2026/10/16/spaces-by-manah-soil-sea-community-centre-india/',
        'https://demo-disc.pixelnest.io/',
        'https://www.designboom.com/architecture/nightswimming-giovanna-silva-discotheques-light-nightlife-guest-essay/'
    ],
    '产品营销': [
        'https://lobby.domains/',
        'https://signwith.co/',
        'https://techcrunch.com/2026/10/15/when-it-came-to-cal-ais-viral-success-a-small-army-of-influencers-paid-off/',
        'https://ahrefs.com/blog/automated-content-creation/'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://ollama.com/blog/reflection-beam': '本地部署模型反思推理机制平民化；在本地离线环境下跑通自我反思与多路径搜寻，是隐私敏感场景的核心方案。',
    'https://www.anthropic.com/research/ecdsa-curve-origins': '安全底层的黑天鹅往往隐藏在历史参数中；用大模型逆向审计经典密码学算法源头，展示了 AI 在形式化安全领域的深厚潜力。',
    'https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/': '智能体落地物理世界必须受自然规律硬约束；将生化数字孪生作为虚拟沙箱，彻底根治物理实操中的灾难性试错。',
    'https://github.com/ValerioDolci/capy-flash': '普通游戏显卡分布式推理门槛被击穿；利用闲置双卡协同分摊显存压力，为个人开发者跑大参数模型打开了窗口。',
    'https://www.conifer.build/parallax/': '智能体监督不能靠事后看日志；建立全天候的“船长”监视层对执行偏差进行实时矫正，是保障多任务长周期收敛的前提。',
    'https://usebeeline.app': '打破人和 Agent 的隔离墙；让人类工程师与多个编码智能体平起平坐地同室结对，极大缩短了指令确认延迟。',
    'https://gbrain.io/tools': '给智能体设定严格的信任边界；将敏感第三方密钥隐藏在安全执行隔离区，避免 Prompt 注入攻击导致的越权泄露。',
    'https://github.com/paveo-dev/paveo': '把终端执行从无政府状态收拢为受控系统；通过静态规则审计拦截越权命令，为自动化代理筑起最后一道防火墙。',
    'https://downcheck.dev/': '极简监控工具的克制之美；不依赖复杂云服务，用轻量静态页面聚合全部关键依赖状态，直观降低运维心智负担。',
    'https://apps.apple.com/us/app/ptrace-run-tracker/id6785292238': '个人健康数据资产的私有化主权；将运动轨迹以结构化方式开放给私有 Agent，探索属于单兵用户的个性化训练闭环。',
    'https://github.com/devYRPauli/putaway': '自动化整理的最佳实践不是靠玄学分类；用直观易懂的文件夹规则重构杂乱下载目录，把清爽感还给桌面。',
    'https://caseblossom.com/': '极其锐利的一人公司切角；避开红海配件市场，专攻小众墨水屏阅读器个性化定制外壳，展示了精准捕捉利基溢价的商业嗅觉。',
    'https://www.trytaim.com/': '自然语言到生产力数据的丝滑流转；随口一句语音直接拆分为条理分明的日历排期与知识便签，消灭手动录入摩擦。',
    'https://github.com/elmsec/eqmini': '极度克制的系统级微工具；为不同应用独立设定专属均衡曲线，把声学控制权重新交回音乐极客手中。',
    'https://wayseer.app/': '空间化重塑庞杂架构感知；将枯燥的微服务拓扑转化为可游走穿行的数字空间，极大提升了分布式系统的可观测性直觉。',
    'https://toolbit.app/': '把数据与执行全部留在本地；离线极速运行的日常小工具箱，消灭繁琐在线转换工具带来的隐私泄露风险。',
    'https://www.designboom.com/architecture/saint-of-athens-peace-chaos-boutique-monochromatic-high-contrast-zones-thessaloniki/': '空间双重叙事的戏剧张力；用纯粹黑白单色与高饱和色彩的决绝割裂，在单体零售空间内制造出令人窒息的冲突情绪。',
    'https://www.dezeen.com/2026/10/16/spaces-by-manah-soil-sea-community-centre-india/': '传统手作材料对沿海人居的温柔庇护；泥砖拱券与自然通风对流，在现代化浪潮中守护了本土建筑的生态尊严。',
    'https://demo-disc.pixelnest.io/': '千禧年黄金时代的游戏美学回潮；用低多边形与复古光盘界面包裹现代独立游戏，证明情怀交互能赋予产品强大的仪式感。',
    'https://www.designboom.com/architecture/nightswimming-giovanna-silva-discotheques-light-nightlife-guest-essay/': '空间光影记忆的人文标本；用冷静克制的镜头凝固夜店空间在白昼中的空旷与孤寂，记录人类亚文化社交场域的消长。',
    'https://lobby.domains/': '缩短品牌诞生到落地的链路；在敲定创意的瞬间即刻比对全球域名池状态，将品牌冷启动的前期阻力降到极低。',
    'https://signwith.co/': '颠覆巨头垄断的商业计费重构；拒绝强制席位月费绑架，按真实完成签署量按次扣费，精准击中中小企业的长尾刚需。',
    'https://techcrunch.com/2026/10/15/when-it-came-to-cal-ais-viral-success-a-small-army-of-influencers-paid-off/': '大体量投放不如小圈层高密渗透；借助垂直 KOC 军团撬动爆发式自传播，揭示了当下消费级 AI 应用最低成本的获客解法。',
    'https://ahrefs.com/blog/automated-content-creation/': '严肃内容工程化与低质 AI 垃圾的区别；将内容生产拆分为调研、审查与分发各环节的可控流水线，守护品牌信誉底线。'
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
v_info = vertical_data['2026-10-17']
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
date: '2026-10-17'
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

out_file = 'src/content/daily/2026-10-17.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-17! Total URLs in history: {len(all_used_list)}')
