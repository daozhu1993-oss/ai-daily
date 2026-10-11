# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-11': {
        'title': '10 月 11 日 · 意图交付与真问题沉淀：穿透功能假象，做离业务最近的解题者',
        'highlights': '全网 9 大领域 36 篇高密度精选：微软推出专门决策与打分模型、Anthropic 复盘评测中的越界行为、从注意力经济走向意图经济、即梦重塑视听短剧生态、功能是答案而问题是题目。',
        'epigraph': '当代码与功能的供给变得极其廉价且无限充沛，产品人最核心的壁垒不再是给出答案的速度，而是能否穿透客户随口说出的功能诉求，精准锚定那个最值得被解决的真实问题。',
        'lead': '10 月 11 日，初秋周日的行业脉搏正在敲响更具清醒意味的鼓点：从微软为固定选项与路由控制量身打造的 Decision-1 专门模型，到 Anthropic 严肃公开模型评测中的越界防范，底层的技术巨头正在把重心从粗放的参数暴力，转移到精准可靠的边界控制与系统契约上；在产品经理与商业模式的最前沿，一场关于“注意力经济向意图经济迁徙”的范式革命正在拉开序幕——用户不再愿意把大把时间耗费在复杂的表单与繁琐的操作中，他们只需要一个确定的结果交付；在视听与漫剧一线，随着即梦与多模态大模型的普及，曾经靠粗暴同质化收割受众的套路正遭遇 00 后的无情卸载，内容行业倒逼创作者回归扎实的人物弧光与严密因果逻辑。无论是写代码、做商业还是讲故事，停下盲目堆砌答案的惯性，想清楚那个最根本的“题目”，才是穿越周期的真正力量。',
        'scene': '「客户又提了一堆新功能需求，我们是不是得赶紧排期上线？」「别急着画原型。客户说要一把更快的锤子，往往是因为他手里的钉子根本没找对位置。先问清楚他到底要钉什么、解决什么业务卡点，这比做十个功能都管用。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周日，也是十月上旬假后第一个完整周末的最后一天。

在今天整理的 36 篇内容里，我反复看到一句话：**“功能是答案，问题是题目。”**

在过去软件匮乏的时代，谁能快速做出一套功能，谁就能占领市场；但到了大模型时代，生成一个功能、写出一段代码、配出一套流程的边际成本已经趋近于零。

当满大街都是现成的“答案”，真正稀缺的反而是那个能看懂“题目”的人。

为什么很多产品堆满了华丽的 AI 交互却无人问津？因为它们解决的是臆想出来的伪需求。
为什么优秀的独立开发者单凭一个小工具就能年入百万？因为他们切中的是真实业务流程里哪怕毫不起眼的一处痛点。

明天又是新的工作周。在开启新的代码或规划新的版本之前，不妨多花半小时问问自己：
我今天是在盲目地给出一个答案，还是在真正解决一个值得被解决的问题？

愿我们都能做那个离真实业务最近、看得最清的解题者。

祝你新的一周工作顺遂。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': '即梦，梦的新内容生态：字节视听基座如何重塑短剧创作者经济',
                'note': '新一代视听生产力平台深度复盘：剖析字节即梦如何打通故事线索、分镜渲染与音乐合成，让个人创作者与中小型团队实现低成本批量化漫剧试错。',
                'so_what': '工具平权带来内容爆发；在人人都能生成高清画面的时代，独特的剧情审美与情绪共鸣成为漫剧唯一的壁垒。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6476061.html',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'Claude、GPT“跨界”做视频：全模态吞噬下漫剧工具链的护城河博弈',
                'note': '视听工具链行业宏观推演：当头部通用大模型纷纷将端到端视频生成作为原生能力内置，垂直类 AI 漫剧软件如何依靠专业分镜控制与资产库深耕壁垒。',
                'so_what': '通用底座负责廉价生成，专业工具负责精确掌控；把控复杂的剧本节点与资产沉淀，是创作者抵御模型迭代的锚点。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6474292.html',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '00后“戒断”AI短剧：高频同质化反噬与叙事完播率的工业救赎',
                'note': '受众心智变迁一线洞察：粗制滥造的换脸爽剧正在遭遇年轻观众的快速审美疲劳与主动卸载，虚假的人工智能噱头再难掩盖单薄的故事骨架。',
                'so_what': '算法堆叠的爽感保质期极短；回归扎实的人物动机与不可预测的情节拐点，才能挽救漫剧的断崖式跳出率。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475822.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '真人AI混拍实战复盘：虚实结合降本增效还是过渡期的体验妥协？',
                'note': '影视制片工程一线复盘：实拍演员近景面部表情与真实肢体接触，结合背景与奇幻特效的 AI 生成，拆解当下漫剧制作中最平衡的工业化路径。',
                'so_what': '虚实混拍是当下最具性价比的落地方案；保留人性的真实微表情，把算力用在最耗费搭建成本的宏大场景上。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6475573.html',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国电影剧本备案立项公示：商业大片主线冲突与类型化故事核提炼',
                'note': '国家电影局过审剧本样本拆解：分析如何在数百字的故事梗概中，用高度凝聚的核心命题与生死抉择，瞬间确立商业类型片的剧情脊梁。',
                'so_what': '故事核是剧作的灵魂基石；好的梗概必须让观众在三句话内看到主角的不可抗拒目标与巨大危机。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/867',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '全国拍摄制作网络剧备案公示：中长剧集多线并进与叙事节奏咬合心法',
                'note': '高分网剧立项经验公开：在多阵营、长周期的叙事篇幅中，如何通过交错的情感线与悬念链，保持每一集的戏剧浓度而不出现中段塌陷。',
                'so_what': '多线叙事是一场精密的齿轮传动；让每条支线的危机都在关键节点对主线形成助推或阻力，故事才能紧凑有力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/869',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '重点微短剧规划备案公示：单集 2 分钟抓人公式与人物前置关系设计',
                'note': '官方审读案例深度复盘：剖析优秀微短剧如何在开篇 15 秒内交代人物压迫性关系，利用信息差与强烈身份反差牢牢锁住受众眼球。',
                'so_what': '开场即决战；在极短时长内省去一切无用铺垫，让冲突直接从人物既有的不可调和身份对立中引爆。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/871',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '全国微短剧重点备案审查样本：摆脱同质套路，构建合情合理的戏剧惊叹',
                'note': '过审短剧创作规律剖析：如何在合规框架下打破千篇一律的装腔打脸，将高潮建立在真实人性软弱与合情理的利益纠葛之上。',
                'so_what': '反转必须有扎实的现实逻辑作为依托；尊重生活常识的反转，才能让观众在惊讶之余产生深层的情感共鸣。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/873',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '客户说要一个功能，产品经理怎么找到真正的底层痛点？',
                'note': '资深产品人实战方法论：剖析客户提出的“功能解法”往往只是对表面症状的应激反应，PM 必须像医生一样深挖其业务系统中的真实堵点与组织利益博弈。',
                'so_what': '客户要的是结果不是功能；学会穿透表面要求做减法，用最简洁的机制解决最根本的业务摩擦。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pd/6475402.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '功能是答案，问题是题目：AI 时代产品经理唯一稀缺的资产',
                'note': '产品价值体系重构长文：当模型把实现答案的代码和功能成本降为零，能精准定义“值得被解决的真问题”的 PM 成为企业最稀缺的核心资产。',
                'so_what': '做题家时代的结束与解题者时代的开启；放下画原型的执行幻觉，锤炼对商业本质与客户隐性痛点的敏锐嗅觉。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6475555.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '把够用的智能做成一门生意：摆脱 SOTA 虚荣指标，深耕真实场景闭环',
                'note': 'AI 商业化落地实操指南：不盲目追逐千亿参数大模型的刷榜跑分，利用轻量小模型与结构化规则，把“刚好够用”的智能低成本嵌进垂直业务流。',
                'so_what': '商业比拼的是投入产出比；把算力成本控制在业务毛利之内，才能做出拥有长久生命力的赚钱产品。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475940.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': 'AI 时代，注意力经济终局，意图经济登场：从时长争夺到结果交付',
                'note': '商业底层范式转移深度解析：传统互联网围绕掠夺用户时间与信息流曝光展开，而在智能体时代，商业价值完全取决于能否一键闭环完成用户的意图委托。',
                'so_what': '告别流量贩子思维；谁能帮用户省下最多时间并给出最高质量的交付结果，谁就拥有未来商业的核心定价权。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/marketing/6475814.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-11.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

ian_by_cat = {}
for it in raw_items:
    u = it['url']
    c = it['category']
    if u not in used_set:
        ian_by_cat.setdefault(c, []).append(it)

day_items = []

# 1. AI 资讯 (3 from raw-ian-11 + 1 from Sierra Poppy)
ai_news_picked = ian_by_cat.get('AI 资讯', [])[:3]
for idx, p in enumerate(ai_news_picked):
    used_set.add(p['url'])
    day_items.append({
        'category': 'AI 资讯',
        'title': p['title'],
        'note': p['judgment'],
        'so_what': '从微小变化中洞察范式转移，把外部技术演进收拢为自身确定性的产品复利。',
        'source': p['source'],
        'url': p['url'],
        'media': p['media'] or 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
        'pinned': (idx < 2)
    })

# 4th AI 资讯 item: Sierra Poppy
sierra_item = {
    'category': 'AI 资讯',
    'title': 'Sierra 发布 Poppy 草案并新增设计伙伴',
    'note': '企业级会话体验标准草案：围绕对话意图、状态流转与品牌声调建立开放设计契约，降低智能体与外部系统的集成摩擦。',
    'so_what': '对话标准从私有黑盒走向行业共识；统一的交互草案让企业在更换底层模型时保持体验的一致连贯。',
    'source': 'sierra.ai',
    'url': 'https://sierra.ai/blog/poppy',
    'media': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
    'pinned': False
}
used_set.add(sierra_item['url'])
day_items.append(sierra_item)

# 2. Remaining 5 ian categories × 4 items
target_5_categories = ['AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
for c in target_5_categories:
    avail = ian_by_cat.get(c, [])
    picked = avail[:4]
    if len(picked) < 4:
        raise ValueError(f'Not enough items for {c}: only {len(picked)}')
    for idx, p in enumerate(picked):
        used_set.add(p['url'])
        day_items.append({
            'category': c,
            'title': p['title'],
            'note': p['judgment'],
            'so_what': '从微小变化中洞察范式转移，把外部技术演进收拢为自身确定性的产品复利。',
            'source': p['source'],
            'url': p['url'],
            'media': p['media'] or 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
            'pinned': (idx < 2)
        })

# 3. 3 vertical categories × 4 items
v_info = vertical_data['2026-10-11']
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
date: '2026-10-11'
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

out_file = 'src/content/daily/2026-10-11.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-11! Total URLs in history: {len(all_used_list)}')
