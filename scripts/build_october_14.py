# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-14': {
        'title': '10 月 14 日 · 确定性重构与微型资产沉淀：当大模型退居幕后，系统与意图开始接管现实',
        'highlights': '全网 9 大领域 36 篇高密度精选：Gemini 4 Argon 与端侧小模型重构安全防御、Anthropic 为代理重写版本控制、苹果 HomeView 探索家庭共享入口、微短剧全本商业出售与广电备案新动向、本体论与知识图谱救赎 RAG。',
        'epigraph': '大模型终将变成像电力一样平常的基础设施。真正决定商业生死与个人复利的，永远不是谁先通了电，而是你用这股电流驱动了怎样精准的意图系统与坚固的履约闭环。',
        'lead': '10 月 14 日，AI 行业的演进逻辑正在从“基座跑分狂欢”不可逆转地切入“真实生产力重塑”。在基础模型与系统架构端，谷歌 Gemini 4 Argon 从受限测试迈向全面开放，Liquid AI 则用 LFM2.5 将端侧推理窗口大幅延伸至 131K，端侧小模型正迅速接管代码审计与密钥防御等高频确定性任务；与此同时，Anthropic 罕见发文复盘为智能体规模化并行编程重构版本控制系统的工程实践，标志着多 Agent 协同已不再是玩具级的提示词编排，而必须直面分布式代码合流与测试断点的高维挑战；在终端与产品设计一线，苹果发布 HomeView 智能家庭中心，将交互重心从个人手持设备拓展至多用户协同的物理空间；在视听与内容工业端，广电总局最新公布 95 部重点网络动画规划备案，都市与青少题材领跑，而《女将北征》等全 120 集由 AI 辅助完成的商业短剧剧本已在版权交易市场实现全流程交割，标志着短剧与漫剧生产管线已彻底跑通商业闭环。',
        'scene': '「大模型天天发新版本，我们的产品怎么才能不被底层更新冲垮？」「把模型当成可插拔的算力引擎，把精力花在数据结构、本体知识图谱和真实物理履约上。模型越卷，你的系统底座越值钱。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周三。

今天整理这 36 篇一手资讯时，我最大的触动是：**大模型正在加速“隐形化”**。

前两年，所有人都在讨论参数规模、上下文长度、甚至每秒 Token 速度；
但到了今天，最引人注目的突破，却发生在那些极不起眼的“接口”与“底盘”上：
Anthropic 在重构代码版本控制，因为智能体写代码太快，传统的 Git 分支合并已经不堪重负；
GitHub 训练专门的 ModernBERT 小模型，只为了在开发者提交前精准识别硬编码密钥；
还有那些把 120 集竖屏微短剧用 AI 管线跑通、并直接放到交易市场交付的创作者。

当一项技术开始退居幕后、化作像水电一样的静默动力时，
它才真正开启了属于应用层与工程搭建者的黄金时代。

不要再做单纯的“提示词搬运工”，
去构建属于你自己的业务意图、数据契约与确定性工作流。

让概率的归模型，让确定的归系统。

祝你今天产出满满。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': '广电总局 2026 年 9 月重点网络动画片备案公示：题材结构与精品漫剧合规风向',
                'note': '官方权威公示数据全景洞察：9 月全国共 95 部重点网络动画片完成规划备案，青少与科幻题材合计占比近四成，平台对精品化、合规化短剧漫剧的审核门槛进一步提升。',
                'so_what': '合规是漫剧规模化变现的前提；摸清官方题材配比与价值观红线，才能确保作品顺利拿号、安全上线。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/art_info/961',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '《女将北征》全 120 集 AI 辅助竖屏微短剧：工业化流水线实战与全本商业交付',
                'note': '行业首部明确标明 AI 辅助创作的全本商业交付案例：现代女军官魂穿军户的逆袭爽剧，每集 1 分钟竖屏完稿，全面验证了 AI 在长线连载微短剧中的工业化产能。',
                'so_what': '微短剧全流程 AI 化已走出实验室；学会用智能体拆解分镜、打磨对白并实现全本交割，是创作者降本增效的核心路径。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1763',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'PKU Open-Sora-Plan 开源视频生成管线：高质量长视频与动画生成工程底座',
                'note': '北大团队开源通用视频扩散框架：支持高质量高分辨率视频生成，优化时空注意力机制，为长镜头叙事与复杂运动分镜提供开箱即用的工业级底盘。',
                'so_what': '视频扩散模型进入开源普惠期；独立工作室无需自研大底座，即可基于开源权重训练专属角色的动态运镜。',
                'source': 'github.com',
                'url': 'https://github.com/PKU-YuanGroup/Open-Sora-Plan',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-AnimateDiff-Evolved 进阶动画工作流：支持长篇漫剧与运动模块深度控制',
                'note': '漫剧生成不可或缺的运动中枢：全面增强 AnimateDiff 在 ComfyUI 下的调度能力，支持运动模块热插拔与提示词分段插值，消除镜头突变与角色漂移。',
                'so_what': '运动连贯性是漫剧质感的分水岭；掌握模块化时空采样工作流，才能稳定产出符合分镜脚本的流畅镜头。',
                'source': 'github.com',
                'url': 'https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '为什么你的反派只是个“绊脚石”？——对手越强，故事越好看',
                'note': '剧作人物对抗核心技巧：反派不是毫无逻辑的恶意工具人，真正让观众窒息的压迫感，来自反派坚不可摧的底层信念与主角不可调和的根本冲突。',
                'so_what': '好戏看反派；给对手赋予完整自洽的价值观与压倒性优势，主角的绝境突围才具备扣人心弦的戏剧张力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/957',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '为什么主角从头到尾像同一个人？——人物弧光：欲望 vs 需求',
                'note': '角色成长心路进阶指南：区分“主角想要什么（欲望）”与“主角真正需要什么（内在需求）”，人物弧光的本质是在残酷现实中打破执念完成心智升维。',
                'so_what': '剧情推动情节，弧光触动人心；把主角逼入欲望与需求的决裂十字路口，角色才能从扁平立绘变成活生生的人。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/956',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '为什么你的剧情推不动？——人物没目标，剧情就推不动',
                'note': '剧作动力机制深度剖析：如果主角缺乏具体、迫切且不可逆转的核心目标，所有的事件堆砌都只是被动流水账；目标越清晰，行动阻力才会越具象。',
                'so_what': '动力源于执念；在剧本前五分钟赋予主角不可妥协的行动动机，是解决情节拖沓与节奏涣散的唯一解药。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/955',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '第二届陕西微短剧剧本创作大赛通知：立足西部文化底蕴打造精品微短剧',
                'note': '官方微短剧赛事导向解析：鼓励创作者依托深厚历史文化底蕴，探索“文学创作—影视制作—文旅融合”的发展桥梁，助力精品微短剧品牌出圈。',
                'so_what': '文旅融合是短剧获得官方扶持与商业定制的黄金风口；把微反转短剧框架嫁接到特定地域风土中，具有极高的立项胜率。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1764',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '向量库是 RAG 的伪命题，知识图谱是答案，本体论是灵魂',
                'note': '知识检索与企业级 Agent 架构深度洞见：简单的向量语义切片无法解决多跳推理与因果约束，只有结合实体本体论与确定性图谱拓扑，企业级问答才具有可信度。',
                'so_what': '概率召回无法支撑严谨业务；从单纯拼向量检索转向本体知识建模，是严肃企业级 AI 产品的核心护城河。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473808.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'BI 真正的生意才刚开始：当 AI 从对话框走向企业核心指标与决策闭环',
                'note': '数据商业智能产品操盘复盘：自然语言生成 SQL 只是皮毛，真正值钱的是将指标口径治理、异常因果归因与自动化业务行动做成无缝闭环。',
                'so_what': '客户要的不是聊天窗口，而是利润归因；跳出“Text-to-SQL”玩具功能，做懂行业口径的智能决策副驾。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473848.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'Agent 和 RPA，八竿子打不着的俩物种，为啥非要往一起扯？',
                'note': '自动化技术演进与产品落地思辨：Agent 负责模糊意图规划与动态容错，RPA 负责刚性流程执行与审计隔离，两者融合才是企业端降本的终极形态。',
                'so_what': '别陷入二元对立；把大模型的“脑”套上传统自动化确定的“手脚”，才是企业能买单、能落地的工程解。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6471455.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '产品经理 35 岁就没出路了吗？转型意图架构与商业操盘的破局路径',
                'note': '行业转型阵痛期个人职业复盘：画原型、写 PRD 的传统执行岗加速贬值，真正具备不可替代性的是对复杂业务意图的解构力与多智能体商业闭环的操盘力。',
                'so_what': '技术迭代逼迫能力重组；从功能画图匠蜕变为理解系统架构与现金流周转的一号位，是产品人的唯一进阶通路。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/share/6473987.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-14.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Select curated items for the 6 ian categories
curated_ian_picks = {
    'AI 资讯': [
        'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/',
        'https://github.blog/ai-and-ml/githubs-model-for-secret-detection-finding-more-secrets-with-less-noise/',
        'https://www.liquid.ai/blog/lfm2-5-24b-a2b',
        'https://blog.character.ai/an-update-on-character-ai/'
    ],
    'AI 协作': [
        'https://www.anthropic.com/engineering/redesigning-source-control',
        'https://climanager.solhun.com/',
        'https://www.langchain.com/blog/agent-traces-ai-search-langsmith',
        'https://github.com/imhuhe/gongwen-kit'
    ],
    '一人公司': [
        'https://keepword.net/',
        'https://opensidian.org/',
        'https://guitoro.com/',
        'https://www.livecoloringbook.com/'
    ],
    '产品设计': [
        'https://openwhispr.com/',
        'https://www.apple.com/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home/',
        'https://getret.app/',
        'https://hidatalinker.onesolo.app/'
    ],
    '审美提升': [
        'https://www.designboom.com/architecture/fifty-oak-trees-stone-paved-clearing-contemporary-italian-piazza-ghisellini-architetti/',
        'https://www.wallpaper.com/design-interiors/noe-kuremoto-pad-2026-collectible-design',
        'https://www.wallpaper.com/design-interiors/interior-design/a-captivating-new-book-offers-a-look-inside-the-astonishing-chicago-headquarters-of-ebony-and-jet-magazines',
        'https://www.designboom.com/architecture/four-pitched-roof-volumes-timber-clad-coastal-house-of-cards-belgium/'
    ],
    '产品营销': [
        'https://agentcraft.ai/',
        'https://www.mentionbird.ai/',
        'https://getappniche.com/tools/app-store-keyword-tool',
        'https://postnitro.ai/agents'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/': '大模型基座从闭门评测走向真实业务攻防；网络防御与受控接口是企业级落地的试金石。',
    'https://github.blog/ai-and-ml/githubs-model-for-secret-detection-finding-more-secrets-with-less-noise/': '大模型擅长推理，小模型长于特定特征匹配；合理搭配能把代码安全防线前置到极低成本。',
    'https://www.liquid.ai/blog/lfm2-5-24b-a2b': '端侧长上下文模型进入可用阶段；离线处理敏感长文档与代码工程的算力门槛大幅降低。',
    'https://blog.character.ai/an-update-on-character-ai/': '纯聊天娱乐产品的商业故事面临清算；缺乏严肃履约与高黏性工作流的 AI 应用难以抵御高昂算力成本。',
    'https://www.anthropic.com/engineering/redesigning-source-control': '智能体并行编码正彻底摧毁传统 Git 工作流；为 Agent 规模化设计全新的版本合流协议是当下最硬核的基建。',
    'https://climanager.solhun.com/': '给终端加上可控的“眼睛与手脚”；让开发者随时无缝接管智能体执行，是建立人机信任的绝佳设计。',
    'https://www.langchain.com/blog/agent-traces-ai-search-langsmith': '别在海量调用日志里大海捞针；用语义描述直接定位 Agent 翻车现场，是可观测性系统的进化方向。',
    'https://github.com/imhuhe/gongwen-kit': '不要替用户做不可逆的决定；以“修订与批注”保留人工最终裁决权，是高专业度工具不可逾越的底线。',
    'https://keepword.net/': '数字痕迹的真实性正在贬值；为网页修改提供去中心化存证见证，精准击中信息问责的刚需。',
    'https://opensidian.org/': '纯本地 Markdown 是终极的数字抗风险资产；避开云端锁死，保护个人知识资产的主权。',
    'https://guitoro.com/': '用极低门槛的键盘映射还原真实乐器手感；把硬核技能拆解为游戏化微反馈，是极佳的教育产品思路。',
    'https://www.livecoloringbook.com/': '物理创作与数字互动的无缝串联；让孩子的纸面手绘活在共享小世界里，提供了极佳的情感附加值。',
    'https://openwhispr.com/': '跨终端离线语音输入生态闭环；让开源听写工具覆盖手机与桌面，端侧隐私保护是其核心武器。',
    'https://www.apple.com/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home/': '智能设备正从个人独占走向家庭共享空间；设计兼顾多用户权限与情境感知的界面是下一个风口。',
    'https://getret.app/': '把线性对话框打散成空间画布；多会话并行与收件箱机制大幅释放了开发者管理多个 Agent 的并发生产力。',
    'https://hidatalinker.onesolo.app/': '克制是轻量工具的美德；在笨重的官方客户端与过载的多合一软件之间，为日常高频查库找到最轻快的切角。',
    'https://www.designboom.com/architecture/fifty-oak-trees-stone-paved-clearing-contemporary-italian-piazza-ghisellini-architetti/': '用自然生态缝合城市公共空间；树阵不仅提供物理阴凉，更以透水蓄水系统重构了现代人居的可持续质感。',
    'https://www.wallpaper.com/design-interiors/noe-kuremoto-pad-2026-collectible-design': '手工与原始图腾的现代觉醒；在数字复制泛滥的时代，带有泥土与火焰温度的非标手作更显珍贵。',
    'https://www.wallpaper.com/design-interiors/interior-design/a-captivating-new-book-offers-a-look-inside-the-astonishing-chicago-headquarters-of-ebony-and-jet-magazines': '空间是时代精神最诚实的标本；黑人出版先驱的历史办公空间，用浓烈的色彩与材质记录了不可磨灭的文化骄傲。',
    'https://www.designboom.com/architecture/four-pitched-roof-volumes-timber-clad-coastal-house-of-cards-belgium/': '用极简的木屋顶解构传统坡屋顶；预制木板构成的无柱空间，展现了当代建筑材料与结构力学的从容融合。',
    'https://agentcraft.ai/': '最真实的营销素材来自日常生产现场；把内部微知识点自动编排为多平台内容，将内容获客成本降到极限。',
    'https://www.mentionbird.ai/': 'GEO（生成式引擎优化）正在取代传统 SEO；监控品牌在 AI 对话中的引用率，是新一代增长团队的必修课。',
    'https://getappniche.com/tools/app-store-keyword-tool': '选品胜过努力；在动工开发前通过应用商店高频关键词挖掘真实搜索需求，能把冷启动风险降到最低。',
    'https://postnitro.ai/agents': '内容生产不仅要有文字，更要有精美的视觉排版排期；为 Agent 补上全渠道设计输出能力，完成了营销自动化的最后一公里。'
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
v_info = vertical_data['2026-10-14']
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
date: '2026-10-14'
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

out_file = 'src/content/daily/2026-10-14.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-14! Total URLs in history: {len(all_used_list)}')
