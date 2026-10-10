# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-10': {
        'title': '10 月 10 日 · 行动重构认知：从虚拟推演到物理触碰，造物者的确定性回归',
        'highlights': '全网 9 大领域 36 篇高密度精选：Odyssey 3 让世界模型持续演进、Deno 与 Cloudflare 推进自托管与边缘架构、MagicAnimate 与 Seamless 拓宽漫剧视听边界、为什么商业操盘型 PM 极度稀缺、具身智能边角料生意的破局启示。',
        'epigraph': '当算法在虚拟世界里穷尽了参数的排列组合，真正的造物者已经卷起袖子，用一行行确定的代码、一抔真实的陶土、一场深入业务现场的驻场交付，在充满不确定的现实世界里打下一颗颗坚固的锚点。',
        'lead': '10 月 10 日，这个初秋周六的科技与商业图景，正在呈现出一种清晰的收敛：无论是在世界模型 Odyssey 3 中让行动直接改变生成环境，还是 Deno 加入 Cloudflare 坚决捍卫自托管与边缘主权，抑或是设计师 Coco Brun 将数字洞穴扫描转化为真实的陶瓷扩香雕塑，所有前沿的探索者都在做同一件事——穿透虚浮的 PPT 与概念狂欢，用可执行的动作在物理与数字世界的接壤处建立秩序。在漫剧与视听工业一线，MagicAnimate 和 Seamless 正在让个人创作者跨越动作与语言的重重天堑；在商业与产品落地端，只会画原型的功能 PM 加速出清，而懂得避开巨头内卷去赚“具身智能边角料”与“FDE 驻场交付”的实干家，正悄然收获着丰沛的现金流。',
        'scene': '「现在都在卷世界模型和各种 Agent，个人创作者和小团队到底还有没有机会？」「别去跟巨头拼算力底座。看看别人怎么把开源模型接进实际工作流、怎么做具身智能的传感器边角料，把一个具体场景的脏活累活做到极致，那就是谁也抢不走的身家底气。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周六，秋意渐浓。

这两天的更新里，我反复提及一个词：**确定性**。

在一个算法瞬息万变、行业焦虑蔓延的周期里，很多人总在问：下一个风口是什么？我是不是马上要被淘汰了？

但看看今天这 36 篇精选所记录的真实世界吧：
有人用一个简单的点对点房间号做出了优雅的跨设备协同；有人把虚构会议做成了一门小巧精致的生意；有人在陶瓷泥料里寻找数字艺术的物理质感；也有人在巨头不屑一顾的机器人边角料环节稳稳扎下了根。

技术从来不是为了让人陷入虚无的宏大叙事，而是为了让有想法的普通人拥有更强壮的臂膀。

趁着周末，合上电脑，去触摸真实的草木与器物，去跟真实的人聊聊他们的困惑与需求。

当你开始用行动去解决哪怕一个极其微小却真实存在的问题时，焦虑便会自然消散，属于你自己的秩序便会悄然生长。

祝你周末愉快。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'Meta Muse 深度解析：多模态创意伙伴如何重构漫剧故事板与视觉原型生成',
                'note': '深度拆解 Meta 最新创意多模态助手：将剧本分镜、风格锁定与角色姿态编排融为一体，支持创作者以低认知负荷完成复杂概念视觉化。',
                'so_what': '视听创意的摩擦力进一步降低；一人编导借助 Muse 即可在数小时内完成过去需团队协作数周的动态分镜原型。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/evaluating/6472859.html',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '多模态大模型落地实测：从单帧高质量渲染到连续漫剧分镜的一致性博弈',
                'note': '一线工业级工作流实测复盘：评测主流多模态基座在复杂光影、运镜轨迹与多角色互动下的表现，揭示一致性与动作幅度之间的工程权衡。',
                'so_what': '不再被单一好看的宣发样片迷惑；只有在长时序、强运镜下保持主体与空间连贯性，才能成为真正可商业化交付的生产力工具。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473384.html',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'MagicAnimate 开源时序一致性动画框架：驱动静态漫剧角色完成高动态复杂动作',
                'note': '北大与字节开源的时间序列扩散框架：通过时间注意力机制在保持角色身份与服装细节完整的前提下，精准根据驱动骨骼渲染连贯流畅的动态画面。',
                'so_what': '2D 漫画立绘到 3D 动作漫剧的鸿沟被彻底填平；原画师沉淀的经典 IP 资产可以极低成本转化为动态剧集。',
                'source': 'github.com',
                'url': 'https://github.com/PKU-YuanGroup/MagicAnimate',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': 'Seamless Communication 多语言同传与口型合成：让 AI 漫剧一键出海跨国传播',
                'note': 'Meta 开源前沿音画多语言系统：不仅保留说话人的音色情绪与语调起伏，更支持端到端跨语种语音翻译与逼真音视频对齐，赋能漫剧全球化出海。',
                'so_what': '文化出海不再受限于漫长的高昂配音译制周期；原生多语言视听资产将直接参与全球内容市场的存量争夺。',
                'source': 'github.com',
                'url': 'https://github.com/camenduru/seamless_communication',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国电影剧本备案立项公示：类型片剧情主线设计与戏剧两难困境构建',
                'note': '电影局过审剧本样本拆解：分析在商业类型片开局中，如何通过设计不可调和的伦理困境与价值取舍，迅速将主角推入生死存亡的抉择漩涡。',
                'so_what': '没有真正的两难，就没有真正的人物觉醒；让主角在对错之间抉择是平庸的，逼其在两种崇高或两种痛苦之间抉择才见功力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/853',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '剧本人物救赎弧光打造指南：从心理创伤防线到底层价值观裂变的编剧心法',
                'note': '深度剖析经典叙事中的人物成长曲线：主角如何带着内在缺陷出发，在一次次危机事件中经历信念崩塌与精神重塑，最终完成由内而外的蜕变。',
                'so_what': '事件是人物的试金石；与其不断堆砌外部惊险，不如让每一次外在危机精准击中主角心灵最脆弱的防线。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/858',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '全国重点微短剧规划备案公示：剧情反转合规与紧凑因果链条审读指南',
                'note': '官方重点微短剧过审范本解读：如何在 2 分钟单集限制内，摆脱粗暴逻辑断裂，依靠严密信息差与人物性格动机推演出合情合理的反转。',
                'so_what': '反转不是为了吓观众一跳，而是为了揭示更深层的真实；严密的因果铺垫才能让反转产生余音绕梁的情感震撼。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/859',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '商业类型片反派人物弧光与戏剧对抗力量：让对手的信念成为主角成长的磨刀石',
                'note': '高阶编剧理论分享：平庸的故事制造坏人，伟大的故事塑造对手；只有当反派拥有无可辩驳的哲学动机与行动逻辑时，主角的胜利才有沉甸甸的分量。',
                'so_what': '强劲的对手定义了主角的高度；花在丰满反派身上的笔墨，最终都会转化为整个故事坚如磐石的戏剧张力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/863',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '为什么好产品经理在这个时代极度稀缺？从需求执行者到商业操盘手的代际跃迁',
                'note': '互联网产品行业深度复盘：工具与代码生成门槛大幅下降后，只会写文档、跟进度的“传话筒型 PM”加速被淘汰；真正稀缺的是拥有商业闭环判断力与深度同理心的操盘手。',
                'so_what': '技能的贬值正在倒逼认知的升维；放下对功能列表的执念，学会为真实的客户 ROI 和组织现金流负责。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6473224.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'Personal Agent 重写互联网入口：从人机交互演进看超级应用与个人代理的终局',
                'note': '人工智能与交互界面未来形态深度推演：当模型能够自主理解意图、拆解多步动作并跨系统调用工具，传统搜索框与 App 格子铺正不可逆地退化为底层数据服务商。',
                'so_what': '入口权杖正在发生历史性转移；做产品的核心不再是争夺用户的眼球时长，而是争取成为个人 Agent 首选调用的可信能力节点。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473085.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'AI 陪练场景商业化落地实战：从虚拟互动噱头到高客单复购服务的产品闭环',
                'note': '垂直赛道真实创业案例复盘：详细剖析 AI 陪练如何在职业技能实训与语言学习中跑通商业模式，将单次尝鲜转化为高粘性续费的教研闭环。',
                'so_what': '离开交付结果的陪伴无法形成长久商业价值；把 Agent 的能力锚定在明确可衡量的技能提升上，才能筑起坚实的付费壁垒。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/chuangye/6471435.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '具身智能的“边角料生意”：避开本体造车式内卷，深耕工业自动化与场景数据服务',
                'note': '硬件与大模型结合赛道冷思考：当大厂与资本疯狂涌入人形机器人本体研发时，敏锐的创业者正通过传感器标定、清洗合成数据与夹爪执行工具切入确定性丰厚的细分市场。',
                'so_what': '卖水者的利润往往比淘金者更稳固；在狂热概念的边缘寻找供应链与落地链条中的真实堵点，是一人公司与小团队的最优解。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/embodied/6473110.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

target_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
raw_path = 'scripts/raw-ian-10.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

ian_by_cat = {}
for it in raw_items:
    u = it['url']
    c = it['category']
    if u not in used_set and c in target_categories:
        ian_by_cat.setdefault(c, []).append(it)

day_items = []

# 1. 6 ian categories × 4 items
for c in target_categories:
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

# 2. 3 vertical categories × 4 items
v_info = vertical_data['2026-10-10']
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
date: '2026-10-10'
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

out_file = 'src/content/daily/2026-10-10.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-10! Total URLs in history: {len(all_used_list)}')
