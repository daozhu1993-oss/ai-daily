# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-09': {
        'title': '10 月 9 日 · 驻场交付与物理手感：穿透虚拟泡沫，重识造物本质',
        'highlights': '全网 9 大领域 36 篇高密度精选：Google 开源端侧 GPU 推理底座、Anthropic 公开定时 Agent 续跑规则、大厂派 FDE 驻场交付成为新常态、为什么好产品经理极度稀缺、WanVideo 与混元开源视听工作流。',
        'epigraph': '当大模型生成的 PPT 和华丽 Demo 再也换不来客户的支票，大厂开始把工程师和 PM 派往真实的客户现场；穿透数字泡沫的唯一方法，是用带着体温的双手去触碰真实的物理世界与真实的业务泥土。',
        'lead': '10 月 9 日的技术演进与商业战局，正在迎来一场深刻的“返璞归真”：在企业级 AI 落地最前线，腾讯、字节、Kimi 几乎同时做出了同一个动作——不再满足于纯线上 API 交付，而是组建重兵派工程师和产品经理亲赴客户现场（FDE 驻场交付），因为他们终于看清，最难的从来不是调用模型，而是如何把算法严丝合缝地嵌进客户脏乱差的已有业务系统；在产品设计与审美一线，从现代汽车坚决在智能大屏旁保留物理旋钮，到设计师用 USM 模块拼出极简酒吧，界面的设计正在从空洞的扁平色块走向温润的物理触感；在视听工业与漫剧创作端，开源视听模型的参数和渲染管线全面下沉至个人工作站，世界模型的仿真突破更是让虚拟光影与真实物理世界融为一体。无论身处哪一个行业，离开虚妄的概念，去解决一个真实的问题，才能在重构的秩序中拥有坚固的护城河。',
        'scene': '「现在大模型落地，客户还要看纯线上 API 评测吗？」「根本不看那些跑分。现在竞标直接比谁能派 FDE 驻场三天，在客户内网把脏数据洗干净、把审批流跑通。能解决实际业务摩擦的才是真本事。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周五，也是节后第一个完整工作周的尾声。

回看这一周各家大厂的动作与行业变迁，最让我感慨的，就是那句看似朴素却极具力量的常识：**商业的终局永远在真实的泥土里。**

前两年，行业里充斥着“只要调通 API 就能颠覆一切”的傲慢；但到了今天，哪怕是估值百亿的头部模型公司，也必须老老实实组建 FDE 驻场团队，去客户的工厂、仓库和办公室里，处理那些最琐碎、最繁重的边界问题。

做产品、写代码、讲故事，莫不如此。

为什么好的产品经理在这个时代反而极度稀缺？因为只会画原型和堆功能的人太多，而真正拥有商业直觉、愿意下场帮业务算清每一分钱的人太少。

为什么粗制滥造的 AI 短剧播放量破不了亿？因为没有经过生活历练的算力拼凑，打动不了一个有血有肉的普通人。

周末将至。走出屏幕，去看看街头的烟火人间，去感受真实物体的重量与温度吧。最顶级的灵感与最坚硬的壁垒，永远藏在生活的真实细节之中。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-WanVideoWrapper 开源工作流：轻量化显存跑通电影级漫剧长镜头渲染',
                'note': '新一代视频扩散架构工程化适配：针对个人创作者显存受限痛点，通过分块显存管理与高效注意力算子，单张消费级显卡即可流畅渲染高清漫剧分镜与动态过渡。',
                'so_what': '高端漫剧渲染算力门槛进一步下移；个人创作者在工作站上即可实现高质量长镜头推拉摇移自主生成。',
                'source': 'github.com',
                'url': 'https://github.com/kijai/ComfyUI-WanVideoWrapper',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-HunyuanVideoWrapper：混元视频工作流打通漫剧分镜一键渲染与本地编排',
                'note': '开源视频基座专属扩展：全面支持多分辨率、可控运镜与主体特征锁定，支持创作者在节点画布中直观串联分镜脚本与音视频合成流水线。',
                'so_what': '节点化视听管线极大提升了协作效率；把漫剧生产流程资产化为可复用的本地工作流，是工作室的核心竞争力。',
                'source': 'github.com',
                'url': 'https://github.com/kijai/ComfyUI-HunyuanVideoWrapper',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '世界模型与物理仿真漫剧：当视觉生成拥有真实物理法则，虚拟制片迎来真实光影',
                'note': '前沿视觉生成架构解析：深入剖析下一代世界模型如何将重力加速度、刚体碰撞与光学折射等物理规律融入生成潜空间，彻底告别反常识的“画面抽搐与漂移”。',
                'so_what': '真实感是顶级视听的基石；符合物理常识的漫剧动画，才能给观众带来毫无违和感的沉浸观影体验。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473081.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '具身多模态模型落地启示：从虚拟角色动画到真实世界动作迁移的商业化路径',
                'note': '机器人与视听动画交叉探索：分析如何将仿真世界中训练完成的高难度肢体打斗与舞蹈动作，无缝迁移至数字漫剧角色模型中，打造拳拳到肉的高燃打斗分镜。',
                'so_what': '跨学科技术迁移正在成为破局捷径；借用具身智能的动作控制算法，漫剧动作表现力直逼一线院线动画大作。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473189.html',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国电影剧本（梗概）备案立项公示：类型片剧情主线与人物命运前置危机设计',
                'note': '国家电影局过审剧本样本拆解：展示资深编剧如何在 500 字的故事梗概中，用极具张力的前置危机打破主角平静生活，逼迫其做出无法挽回的重大伦理抉择。',
                'so_what': '危机越尖锐，选择越沉重，人物的灵魂就越耀眼；开场即决战，是商业类型片抓住眼球的不二法则。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/852',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '全国重点微短剧规划备案公示：剧情反转合规与紧凑因果链条审读指南',
                'note': '官方审读案例深度复盘：剖析优秀过审短剧如何摆脱低俗狗血套路，将反转建立在合乎人情世故的误会与利益博弈上，实现悬念紧绷与正向立意的完美统一。',
                'so_what': '反转不是魔术戏法，而是因果的收束；尊重现实逻辑的反转，才能让受众在拍案叫绝的同时产生深切共鸣。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/854',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '全国拍摄制作网络剧备案公示：大情节与多线交织叙事的情绪密度把控心法',
                'note': '高分网剧立项经验公开：阐述在多主角、多阵营的大框架下，如何通过交错的危机节点与信息不对称，精准控制每一集的情绪起伏，避免多线并进导致的故事散焦。',
                'so_what': '多线叙事是一场精密的齿轮咬合；让每条支线的危机都在最高潮与主线碰撞，才能引爆成倍的戏剧能量。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/855',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '校园戏剧剧本有奖征集启事：青年群体的精神困境与时代命题提炼指南',
                'note': '面向青年主创的权威创作指引：鼓励创作者告别悬浮的象牙塔幻想，深入观察当下青年在求职压力、亲情疏离与自我身份认同中的真实困惑，用真诚的戏剧语言打动时代。',
                'so_what': '真诚是通向一切心灵的捷径；敢于直面自己这一代人的痛处，才能创作出被时代铭记的作品。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/894',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '为什么好产品经理极度稀缺？穿透功能堆叠，寻找拥有商业直觉的造物主',
                'note': '互联网产品反思长文：指出只会写 PRD、画原型图的“功能型 PM”正在被大模型无情替代，而真正稀缺的是能看清商业全局闭环、敢于做减法并对用户体验拥有偏执敬畏的“造物型 PM”。',
                'so_what': '告别流水线式的技能平庸；培养自己独立算出商业账目与穿透需求真伪的直觉，是产品人唯一的保值资产。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pd/6473240.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '腾讯、字节、Kimi 都开始往客户现场派人：FDE 驻场交付成为大模型落地的必由之路',
                'note': 'AI 商业化一线重磅转向：大厂不再高高在上兜售纯 API 接口，而是组织精锐 FDE 团队深入客户机房与办公区，直面肮脏非标的数据源与复杂的业务流程阻力。',
                'so_what': '技术的高傲被现实狠狠打脸；离开客户业务现场的 AI 都是空中楼阁，弯下腰解决具体业务摩擦的人才能赢得市场。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473100.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'a16z 最新市场洞察：AI 拿走美国 VC 86% 资金，toB 算清 ROI，toC Agent 入口博弈加速',
                'note': '全球创投宏观透视：资本进一步极化，缺乏明确客户回报的包装项目迅速出清；企业端重点考核每一笔 Token 消耗带来的生产力节省，消费端则围绕常驻个人入口展开白刃战。',
                'so_what': '算账时代正式降临；无论是做 B 端提效还是 C 端助理，不能证明正向投资回报率的产品都无法在下半场存活。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473404.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '字节「小豆」呼之欲出，腾讯三路推进：个人 Agent 已成巨头组织能力与生态之战',
                'note': '超级大厂个人智能体终局之战前瞻：不再局限于通用对话助手，而是全面打通搜索、内容生态、社交关系与本地系统级控制权限，争夺下一代智能设备的操作系统级超级入口。',
                'so_what': '单打独斗的独立小助手将面临平台级碾压；一人公司必须避开巨头的生态主干道，深耕那些巨头看不上的垂直脏活累活。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473164.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

target_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
raw_path = 'scripts/raw-ian-09.json'
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
v_info = vertical_data['2026-10-09']
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
date: '2026-10-09'
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

out_file = 'src/content/daily/2026-10-09.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-09! Total URLs in history: {len(all_used_list)}')
