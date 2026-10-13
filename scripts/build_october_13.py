# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-13': {
        'title': '10 月 13 日 · 受控沙箱与反脆弱工作流：在概率的浪潮中构建确定的生产力底盘',
        'highlights': '全网 9 大领域 36 篇高密度精选：Meta Muse Wonder 联合训练跨会话记忆、混元与 CogVideoX 开源视听工作流、Airlock 与 Hexis 打造可控沙箱与审批快照、大厂在 C 端超级入口的防守落位、闷声赚钱的垂直 AI 产品心法。',
        'epigraph': '当大模型生成的内容在互联网泛滥成灾，真正拥有商业议价权的，绝不是那些只会按下回车键看运气的人，而是在不可预测的概率之上，建构起严格审计沙箱、确定性分支与深厚工程底盘的系统搭建者。',
        'lead': '10 月 13 日，科技前沿与商业落地的一线正在经历一场深水区的认知重塑：在 AI 模型架构与协作生态端，Meta 发布 Muse Wonder，将长周期任务调度与跨会话记忆进行端到端联合训练；与此同时，Airlock、Ramet 与 Hexis 不约而同地把焦点投向了“代理执行的可控沙箱”——让智能体先在虚拟机副本与可回滚快照中试跑，经由人工确认与权限闸口后再合入主干，标志着 Agent 协作正从粗放的玩具时代迈向严苛的企业级工程时代；在商业操盘与产品落地一线，滴滴、美团等老牌巨头正紧锣密鼓地在超级入口时代重新排兵布阵，而敏锐的垂直小团队则避开巨头火线，在那些无人问津的细分刚需中闷声斩获千万美元 ARR；在视听与漫剧工业端，腾讯 HunyuanVideo、清华 CogVideoX 与 ComfyUI ControlNet Aux 等开源工具链的全面成熟，正把高质量长镜头生成与姿态控制彻底平权给个人创作者。',
        'scene': '「现在各家模型生成效果都差不多，做 AI 产品的护城河到底靠什么？」「靠确定性。客户最怕的是模型今天听话明天抽搐。谁能在不可控的概率外面套上一层严密的测试沙箱、断点回滚和业务规则，谁才能把项目真正交付给企业并收到钱。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周二。

在今天整理的 36 篇精选里，我最想跟大家分享的一个词，叫做**“反脆弱”**。

这几个月来，行业里最普遍的焦虑是：我的模型能力是不是落后了？我的工具是不是又要被大厂的新发布覆盖了？

但看看今天那些正在闷声赚钱的团队吧：
他们没有去卷参数规模，也没有去天天盯着大模型的跑分榜单；
他们有的在做极其克制的沙箱隔离，确保智能体哪怕出错也不会删坏生产数据库；
有的在给独立开发者做极为好用的多语言应用商店截图生成器；
有的把混元与 ControlNet 的预处理器做成了一键可复用的节点工作流。

当所有人都在赌一个不可控的明天时，聪明的人在用代码把今天的工作变得坚不可摧。

不要害怕模型的频繁迭代，去构建那些能吸收迭代红利、却不受任何单一模型绑架的工作流吧。

用扎实的工程抵御概率的波动，那才是属于造物者最深厚的底气。

祝你今天产出满满。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'Tencent HunyuanVideo 开源视频大模型：电影级漫剧运镜生成与本地管线部署',
                'note': '腾讯开源新一代工业级视频基座：原生高分辨率支持，提供可控运镜与主体特征深度锁定，创作者可在本地工作站搭建完整的电影级漫剧渲染管线。',
                'so_what': '高质量视频生成底座全面开源下沉；个人创作者无需依赖高昂云端 API，在本地算力即可跑通大片级漫剧分镜生成。',
                'source': 'github.com',
                'url': 'https://github.com/Tencent/HunyuanVideo',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'CogVideoX 开源视听生成框架：支持文本与图生漫剧高动态长镜头连贯渲染',
                'note': '清华智谱前沿视频扩散模型：针对角色高动态运动与复杂光影过渡进行专门优化，大幅缓解传统视频生成中的抽搐形变与背景漂移。',
                'so_what': '长时序动态稳定性是漫剧生产力的分水岭；CogVideoX 为故事片长镜头连续推拉摇移提供了可靠的开源工程解法。',
                'source': 'github.com',
                'url': 'https://github.com/THUDM/CogVideo',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-ControlNet-Aux 预处理器套件：漫剧角色姿态与深度线稿高精度控制',
                'note': '漫剧工业化不可或缺的控制中枢：集成 OpenPose、LineArt、Depth 等数十种特征提取器，实现剧本角色打斗分镜与镜头透视的绝对受控。',
                'so_what': '精准控制力是商业化交付的基石；用预处理器牢牢锁死角色骨骼与空间结构，彻底摆脱“靠天吃饭抽卡”的生成困境。',
                'source': 'github.com',
                'url': 'https://github.com/Fannovel16/comfyui_controlnet_aux',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '“中国Muse”过不了豆包：多模态视听基座实测对比与漫剧落地博弈',
                'note': '视听工具链一线深度评测：对比主流多模态音乐与视听生成工具在复杂情感情境下的表现，揭示单点功能惊艳与全流程交付闭环之间的鸿沟。',
                'so_what': '单点 Demo 容易，端到端交付极难；漫剧创作者选型时应重点考察工具对现有工作流的兼容度与持续稳定性。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475905.html',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国剧本征集信息汇总：类型片题材偏好与文旅微短剧立项趋势剖析',
                'note': '万众编剧网行业信息全景梳理：详细拆解全国一季度剧本征集热点，文旅融合、烟火市井与强悬疑微短剧成为出品方高频采购的核心品类。',
                'so_what': '瞄准真实买方需求；编剧在动笔前摸清资方题材偏好与落地场景，才能避免陷入闭门造车无人问津的窘境。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/882',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '国家广电总局 2026 国际微短剧大赛通知：精品化叙事与跨国出海破局',
                'note': '官方权威赛事创作导向解析：鼓励创作者打破低俗噱头，立足全球传播视角，用具有人类普遍情感共鸣的故事范式推动中国微短剧扬帆出海。',
                'so_what': '出海需要普世的人性语言；将东方文化底蕴包裹在严密的好莱坞三幕式冲突框架中，是短剧叩开国际市场的利器。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1736',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '神兽类短剧红果赛道剧本定制需求：知名 IP 衍生与下沉市场爆款法则',
                'note': '头部平台定制剧本一线诉求拆解：如何将既有的动漫神兽 IP 转化为适合免费短剧受众的快节奏情景喜剧，突出视觉符号与情绪反差。',
                'so_what': 'IP 衍生是确定性最高的商业通路；懂得围绕既有资产设计强情绪微反转，是商业编剧不可替代的核心交付力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1737',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '剧本作品《多余者》深度拆解：人物心理缺陷与阶层困境中的戏剧冲突',
                'note': '高质量原创剧本样本评析：主角如何在被家庭与社会边缘化的重重困境中，经历内心深处自尊与软弱的拉扯，最终在极限压迫下完成精神救赎。',
                'so_what': '真正的人物弧光来自不可调和的内在矛盾；让主角直面自己最隐秘的耻辱，故事才会迸发出摧枯拉朽的感染力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1741',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': 'AI 超级入口时代，滴滴、美团在 C 端 App 的防守落位与产品重构',
                'note': '本地生活与出行巨头防守战略推演：当系统级 Agent 意图一键直达，依赖复杂货架与多级点击的传统超级 App 如何依靠闭环履约网络筑起不可逾越的高墙。',
                'so_what': '线下履约是线上算法的最终锚点；纯软件入口容易被重塑，而深扎物理世界供应链与调度系统的产品拥有最坚固的壁垒。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475405.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '千万美元起步，那些鲜少听说、闷声赚钱的垂直 AI 产品操盘心法',
                'note': '海外高估值小团队商业复盘：避开大厂重兵把守的通用大模型赛道，深耕法律、医疗文档与外包客服等极其肮脏繁琐的垂直闭环，实现惊人毛利。',
                'so_what': '闷声发大财的核心是避开聚光灯；寻找那些巨头嫌脏、外行不懂的垂直业务堵点，是独立团队最高胜率的商业选择。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475751.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '当所有人都用 AI 写内容，产品人与独立开发者的个人 IP 靠什么胜出？',
                'note': '个人品牌与产品增长深度复盘：生成式文本导致互联网信息垃圾过剩，真正被认可并沉淀为商业资产的，是带着体温的真实决策复盘与血泪踩坑经验。',
                'so_what': '真实是算法时代最稀缺的奢侈品；拒绝毫无个性的 AI 腔调，用带有个人偏见与真情实感的洞见建立不可替代的情感链接。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/operate/6475586.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '做重大业务决策前，先让 AI 唱反调：用反向思维提升产品战略胜率',
                'note': '资深产品人高阶决策心法：让大模型扮演挑刺的竞争对手或尖刻的投资人，系统性审查产品方案中的逻辑漏洞与乐观偏见，建立防错机制。',
                'so_what': '最好的参谋是敢于反驳你的人；借助 AI 构建红蓝军对抗推演，把致命错误扼杀在方案评审阶段。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6475557.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-13.json'
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
v_info = vertical_data['2026-10-13']
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
date: '2026-10-13'
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

out_file = 'src/content/daily/2026-10-13.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-13! Total URLs in history: {len(all_used_list)}')
