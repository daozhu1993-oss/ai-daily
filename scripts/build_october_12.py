# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-12': {
        'title': '10 月 12 日 · 常驻算力与敏捷小矩阵：重写人机接口，从单点工具走向全栈自循环',
        'highlights': '全网 9 大领域 36 篇高密度精选：Ghost Core 把本地常驻代理装进独立硬件、Stripe 创始人预判 Agent 重写互联网入口、App 工厂成为 AI 时代最被低估的生意、红果短剧日活 1.68 亿的内容飞轮、小说作者与编剧实操手册。',
        'epigraph': '当云端庞大的模型堆叠让人产生算力眩晕，聪明的造物者已经把目光收缩回最具体的阵地——一台放在桌上常驻运行的本地电脑、一个由三个微型 SaaS 组成的小矩阵、一篇经过真人实测反复修改的 README。',
        'lead': '10 月 12 日，新一个工作周伊始的技术演进与商业战局，正在展现出强烈的“向端侧收敛、向垂直下沉”的态势：在 AI 底座与协作一线，从 Ghost Core 标价三千多美元将持续运行的个人智能体固化进桌面硬件，到 iterm-agents 和 DeadBolt 在终端侧车与 MCP 闸口处建立严格的执行控制，智能体不再漂浮在云端虚无的概念中，而是成为常驻系统底层、与本地上下文紧密咬合的数字员工；在商业化落地与产品操盘端，Stripe 创始人公开预判“AI Agent 将重写整个互联网的交互底层”，而敏锐的独立开发者与一人公司早已用行动作出了回应——不再试图做一款包罗万象的超级 App，而是搭建起敏捷高产的“App 工厂”，用小矩阵、低成本、高毛利的单兵打法抢占垂直长尾需求；在漫剧与内容创作端，从 AI 萌宠演短剧的轻量变现，到红果短剧凭借去同质化爽点供给突破 1.68 亿日活，内容工业正在淘汰纯算力包装的空洞噱头，回归严密的叙事因果与合规版权保护。',
        'scene': '「做独立开发和 AI 落地，现在非得去跟大厂卷万亿参数的超级入口吗？」「恰恰相反。大厂卷通用的管线，我们做具体到某个操作系统的端侧侧栏、做某一类特定人群的 App 小矩阵。小团队跑通从需求到现金流的闭环，比在云端空转一万次 Token 都有意义。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周一，也是十月中旬新一周的开始。

在今天整理的 36 篇精选里，有两则资讯放在一起读特别有意思：
一则是 Stripe 创始人高屋建瓴地断言：“AI Agent 将重写整个互联网”；
另一则是一个普通的独立开发者，花了 150 欧元雇了几个真人，老老实实照着自己的 README 一步步安装，把每一个被卡住的细节记下来改稿。

宏大的未来让人心潮澎湃，但真正能把未来拉进现实的，永远是后者那种卷起袖子直面具体摩擦的耐心。

无论外面的世界把“通用智能”吹得多么神乎其神，回到你的办公桌前，你依然需要面对一个个具象的客户、一行行具体的报错、一次次真实的付费决策。

不要被宏大叙事吓住，也不要被浮躁的风口牵着鼻子走。
建好你自己的工作流，守住你自己的小矩阵，哪怕今天只是把一个按钮改得更顺手、把一段说明写得更通透，你都在往属于自己的确定性迈出坚实的一步。

新的一周，愿你步履笃定，产出丰沛。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'AI猫狗演短剧，谁在背后数钱？萌宠数字分身低成本变现链路拆解',
                'note': '轻量化短剧变现一线实操：剖析团队如何利用高拟真动物口型合成与换脸技术，在极低演员成本下批量生产高情绪共鸣的宠物情景剧。',
                'so_what': '垂直品类往往拥有最高的投入产出比；避开宏大古装特效内卷，深耕高粘性垂直情感赛道是小团队的最优解。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475535.html',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '5集播放量破1.5亿，国产AI韩剧热度能否持续？爆款题材红利与续航困境',
                'note': '跨国题材漫剧现象级复盘：分析国产团队借用韩剧强冲突狗血母题结合 AI 快速渲染在海外引爆流量的机制，以及后续付费断崖的深层痛点。',
                'so_what': '流量高峰不是商业终局；没有扎实的长线人设支撑与情绪递进，单靠新奇画风引爆的漫剧很难产生长效付费复购。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475292.html',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '吃了不烧心：红果短剧日活1.68亿背后的内容排布与爽点供给机制',
                'note': '免费短剧平台工业化打法透视：红果如何摆脱传统暴利付费短剧的粗制滥造，通过高频微反转与温和爽点排布，构建稳固的平台留存飞轮。',
                'so_what': '商业模式决定内容形态；从单次收割转向广告长效变现，倒逼漫剧内容供给走向稳定、耐看与工业化标准。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6475190.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '大厂卷 Jarvis，Samantha却在恋爱影游里冒了头？情感分支剧情设计',
                'note': '互动影游与角色伴侣交叉赛道复盘：分析将多模态大模型赋予动态角色后，如何在非线性短剧中设计情感分支，让观众产生真切的互动代入感。',
                'so_what': '从单向观看走向双向互动；漫剧与影游的边界正在消融，把剧情选择权交还给受众是重塑沉浸感的新风口。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473731.html',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': 'AI时代小说作者与编剧实操手册：从网文IP提炼到分镜脚本转化与版权防坑',
                'note': '资深编剧机构实务指南：网文作者与编剧如何合规使用大模型辅助创作、如何防止原创核心梗概泄露，以及遭遇侵权后的全套法律取证链路。',
                'so_what': '技术是工具，产权是底线；在人机协同成为常态的当下，保护好自己的核心母题与原创版权是创作者安身立命的前提。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/art_info/959',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '2026年9月全国一类微短剧规划备案公示：剧情反转合规与审查底线指引',
                'note': '官方重点过审样本深度审读：分析优秀一类微短剧如何在严格合规红线下，摒弃三俗打脸套路，依靠精巧的人性博弈与社会痛点产生戏剧张力。',
                'so_what': '合规是创作的第一生产力；在规则边界内找到高级的戏剧表达，是商业编剧从野蛮生长迈向成熟工业化的标志。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/art_info/954',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '2026年9月全国拍摄制作网络剧备案公示：大时代题材与因果冲突咬合心法',
                'note': '广电立项数据全景复盘：296 部过审剧目中网络剧占比超八成，剖析中剧与短剧集如何在时代变迁的大背景下精密咬合人物命运与主线危机。',
                'so_what': '时代感是故事最坚韧的容器；让个人的困境折射时代的脉搏，作品才能在快餐娱乐中脱颖而出，获得穿越周期的生命力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/art_info/953',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '2026年前三季度微短剧与AI短剧市场情报及发展预测：剧情精品化转型',
                'note': '影视产业宏观调研长文：前三季度短剧市场正式告别流量野蛮收割期，精品化、IP 化与剧本工业化成为制作方赢得生存空间的核心战略。',
                'so_what': '粗放流量红利见顶，内容审美红利开启；好编剧永远是视听产业最硬的通货，故事的厚度决定了商业天花板的高度。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/art_info/952',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': 'Stripe创始人：AI Agent 将重写整个互联网，重塑软件核心交互与支付',
                'note': '全球科技领袖前瞻对谈：当个人智能体取代人类在各个网站之间点击表单和完成支付，传统 Web 的 SEO、广告与用户入口将迎来底层重构。',
                'so_what': '为人设计转向为 Agent 设计；未来的优秀产品必须具备机器可解析的 API 与明确的行动接口，才能接入下一代智能体生态。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475925.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'App 工厂才是 AI 时代最被低估的生意：小团队敏捷矩阵的产品全栈打法',
                'note': '独立开发商业模式深度拆解：一人团队不把身家性命押注在单一爆款上，而是围绕特定受众需求流水线式研发 10~20 款微型 SaaS，构建抗风险矩阵。',
                'so_what': '矩阵化分摊试错成本；借用 AI 的高产出能力做矩阵式产品布局，是一人公司在巨头阴影下稳定盈利的最优解。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475790.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '从市场机会到商业变现：华为流程体系背后的产品端到端统一逻辑',
                'note': '经典硬件与科技制造方法论剖析：拆解华为 IPD（集成产品开发）与 DSTE 战略规划体系，看千亿级企业如何把虚无的市场线索转译为确定性交付。',
                'so_what': '组织流程保障商业闭环；大企业的流程智慧在于消除个人认知盲区，把产品创新的偶然性转化为工程交付的必然性。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pd/6475256.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '为什么 AI 产品更需要体验评测？穿透幻觉率与响应时延的产品度量衡',
                'note': 'AI 产品经理度量衡体系构建：不能仅依赖学术基准评测，必须建立贴合用户真实业务场景的人机交互评测体系，将时延、容错与心理预期精细量化。',
                'so_what': '体验评测是产品迭代的罗盘；建立场景化评测标准，才能在不可预测的模型概率中为用户提供可预测的确定性服务。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475495.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-12.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

target_6_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
ian_by_cat = {}
for it in raw_items:
    u = it['url']
    c = it['category']
    if u not in used_set and c in target_6_categories:
        ian_by_cat.setdefault(c, []).append(it)

day_items = []

# 1. 6 ian categories × 4 items
for c in target_6_categories:
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
v_info = vertical_data['2026-10-12']
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
date: '2026-10-12'
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

out_file = 'src/content/daily/2026-10-12.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-12! Total URLs in history: {len(all_used_list)}')
