# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_nov_16_candidates import candidates

date_str = "2026-11-16"
title = "11 月 16 日 · 算力王座交接与事件溯源协作：Neo Cloud 黄昏、Agent 日志化、小团队 700 万美元"
highlights = "全网 9 大领域 36 篇高密度精选：黄仁勋谢幕与 Neo Cloud 黄昏重排算力版图、Anthropic 一张神图吓退研究员、Nano-Edge-TTS 把语音解码压到 175 万参数、Pizza 用不可变事件日志组织 Agent 工作、5 人零融资做到年入 700 万美元、Remindly 把提醒留进笔记、Mecanoo 拆掉十四层圆塔向公众打开央行金库、百万复刻《持械入宋》国产双图模对决、琼瑶《窗外》35 集改编的困境书写、AI 做完系统之后谁来管。"
epigraph = "算力的王座第一次出现空位，而接管它的不是更强的芯片，是一群连机房都没有的转售者和一套能把每一步都写进日志的工程纪律——这个行业终于开始为「可追溯」付钱。"
lead = "11 月 16 日，AI 版图上最值得盯的不是又发布了什么模型，而是权力结构的松动与技术纪律的回归。一手是叙事层面的地震：黄仁勋的谢幕与 Neo Cloud 的黄昏被同时摆上台面，那些靠转售算力、加杠杆租机房起家的中间层，正在被自建产能与价格战双向挤压；而 Anthropic 那张让研究员当场辞职的图，则把「能力边界」这个老问题重新钉在所有人面前——模型越强，越需要有人敢说它不能做什么。另一手是工程侧的集体转向：Pizza 用不可变 SQLite 事件日志组织 Agent 的每一轮工作，Canban 把终端任务搬进看板，Attest 把评测从「回答文本」推进到「实际动作」，MinePilot 甚至要求代码通过后还得进游戏里验收三维空间。这些产品共同说明一件事：Agent 的可靠性不来自更聪明的模型，而来自更笨但可复盘的流程。商业一线的信号同样清晰：5 个人零融资做到年入 700 万美元、一个 AI 浏览器 33 天把年收入从 100 万翻到 200 万、北大「浪漫极客」的 AI 相机月入 129 万美元——小团队正在用极窄的切口拿到极厚的现金流。而在内容与审美侧，百万预算复刻《持械入宋》逼着国产双图模正面比拼，Mecanoo 拆掉十四层圆塔把央行金库还给公众，来杯 1087 用可拆家具接近唐代古建。这一天的关键词是：把权力交出去，把纪律拿回来。"
scene = "「你们 Agent 出错的时候怎么排查？」「看日志。」「哪种日志？」「每一轮对话、每一次工具调用、每一次工作区通信，全部 append 进一张不能改的 SQLite 表——它不是给人看的漂亮界面，是给未来的自己留的证据。」"
cover = "https://image.woshipm.com/2023/04/13/d34ae8a8-d9e1-11ed-9d7a-00163e0b5ff3.jpg"
closing_note = "把今天 36 个切面摆在一起，会看到一个很朴素的规律：所有活得好的小团队，都在做「把不确定性装进容器」这件事。Pizza 把 Agent 的每一轮工作装进不可变日志，Canban 把并发任务装进看板，Attest 把评测装进真实动作，SecondGlow 把即将报废的旧 iMac 装进新工作流，简造 ERP 把亲戚小厂的手写账本装进一个只做进销存的极简系统。反过来，所有正在失速的角色——Neo Cloud 的中间商、只会转述模型的 AI 艺人、把 AI 当万能锤的产品经理——共同点是他们都在卖「不确定的承诺」，而没有交付可被检验的东西。对转型中的产品人和独立开发者来说，这一天的启示不是去追下一个模型，而是问自己一个问题：我交付的东西，别人能不能在三天后拿出来复盘？如果能，你就有了定价权；如果不能，你只是在参与一场关于运气的竞猜。把判断留给人类，把过程写成证据，把交付物做小到能被人一眼看懂——这大概就是这一轮最稳的活法。"

details = {
    "https://www.woshipm.com/ai/6494217.html": {
        "note": "从黄仁勋卸任引发的连锁反应切入，复盘 Neo Cloud 这批「不做芯片、只转售算力」的中间层如何在自建产能扩张与价格战中被双向挤压，走向黄昏。",
        "so_what": "算力中间商的套利窗口正在关闭；依赖「租来再转卖」的 AI 基础设施创业，必须尽快向上做调度软件、向下绑场景，否则只剩毛利归零。"
    },
    "https://www.woshipm.com/ai/6494223.html": {
        "note": "一张据称让研究员当场辞职的 Anthropic 内部图流出，指向模型能力评估中那些被刻意模糊的边界与不可解释的异常表现。",
        "so_what": "模型越强，「它不能做什么」就越值钱；能给出可信边界说明的团队，会比只会演示惊艳 demo 的团队拿到更长期的企业订单。"
    },
    "https://huggingface.co/drmhse/nano-edge-tts": {
        "note": "Nano-Edge-TTS 把语音解码部分压到约 175 万参数（整模仍约三千万），目标是让 TTS 在边缘设备上跑起来；速度数据来自作者 M4 实机测试。",
        "so_what": "语音交互的端侧化门槛继续下探；硬件产品可以开始把「离线可用的自然语音」当作标配而不是卖点。"
    },
    "https://magazine.sebastianraschka.com/p/understanding-positional-embeddings": {
        "note": "Raschka 从最基础的位置嵌入一路讲到 RoPE，用示意图与公式解释「词序」究竟是如何进入注意力机制的，适合对照代码慢读。",
        "so_what": "想真正调优长上下文产品的人绕不开这一层；理解位置编码，才知道为什么长文档会「记住开头、忘记中间」。"
    },
    "https://pizza.hertzbeat.com/": {
        "note": "Pizza 把 Agent 的对话与工具调用全部写进不可变 SQLite 事件日志，工作区之间用 tell 通信，还能把远程 SSH 主机接进同一套事件流。",
        "so_what": "Agent 工程的正确抽象是「事件溯源」而非「对话历史」；一旦每一步都不可篡改，调试、审计与回滚才第一次成为可能。"
    },
    "https://canban.dev": {
        "note": "Canban 给命令行 Agent 加了一块看板，把终端任务与工作流放进统一工作台并保留卡片状态，多人或多 Agent 推进时能看见责任与进度。",
        "so_what": "当一个人同时调度多个 Agent，「谁在做什么」的可视化就是效率本身；把并发收进看板，是把混乱换成吞吐的最低成本方式。"
    },
    "https://attest-framework.github.io/": {
        "note": "Attest 把 Agent 的工具调用与实际行动纳入评测，围绕「任务到底怎么被执行」判定通过或失败，让测试走出回答文本。",
        "so_what": "评测范式的分水岭：回答正确不等于任务完成；下一代 Agent 产品的质量体系必须建立在行为轨迹而非文本比对之上。"
    },
    "https://www.bmpi.dev/dev/agent-3d-world-building/": {
        "note": "MinePilot 让 Agent 在游戏里做三维建造并接受验收，作者从漏水、碰撞与掉落三个维度复盘空间修复——代码通过之后，还得进原生游戏看结果。",
        "so_what": "「代码正确」与「效果正确」之间存在一条被长期忽略的鸿沟；涉及空间与物理的产品，验收必须回到真实渲染环境。"
    },
    "https://www.woshipm.com/ai/6262646.html": {
        "note": "5 个人、零融资、年入 700 万美元的团队复盘：如何用 AI 把每个人的战斗力放大十倍，以及在这个过程中被砍掉的岗位与流程。",
        "so_what": "极简团队的产能上限被重新定义；真正拉开差距的不是用哪个模型，而是敢不敢把组织架构按「一人一栈」重画。"
    },
    "https://www.woshipm.com/chuangye/6494211.html": {
        "note": "某 AI 浏览器 33 天内把年化收入从 100 万美元推到 200 万美元，文章拆解了它在定位、分发与付费墙上的具体动作。",
        "so_what": "AI 产品的增长窗口极短，靠的不是功能堆叠而是「一句能说清的价值」加上极窄的分发渠道；慢一步就进入同质化。"
    },
    "https://www.woshipm.com/share/6494071.html": {
        "note": "北大「浪漫极客」的 AI 相机项目月入 129 万美元：把审美判断做成产品护城河，而不是把参数做成卖点。",
        "so_what": "在模型即基础设施的时代，「品味」是少数无法被开源复制的东西；审美密集型产品的定价权远高于功能密集型。"
    },
    "https://github.com/Fawkes-hub/jianzao-erp-community": {
        "note": "简造 ERP 从亲戚小厂的进销存需求长出来，面向两三人规模的家庭小仓，社区版只开放基础 PC 进销存，生产、委外与移动端明确不在其中。",
        "so_what": "最务实的开源商业化路径是「先服务一个具体的小客户」；敢于公开不做什么，反而让边界内的产品更可信。"
    },
    "https://www.remindly.com/": {
        "note": "Remindly 把提醒功能嵌进笔记本身：快捷面板随手记下念头，保存时一起设好提醒；按 Esc 暂退也会保留未提交的草稿。",
        "so_what": "微创新的价值在于消除「工具切换」的摩擦；把提醒从日历搬回笔记，省下的正是用户最容易放弃的那一步。"
    },
    "https://dynaura.ashutoshswamy.in": {
        "note": "Dynaura 把系统通知做成灵动岛形态，零依赖组件在胶囊与展开卡片之间弹性变形，支持滑动关闭，并提供主流框架适配。",
        "so_what": "交互形态的复用是低风险高回报的设计策略；把移动端的成熟范式迁移到 Web，立刻获得「熟悉又新鲜」的体验红利。"
    },
    "https://secondglow.app/": {
        "note": "SecondGlow 让 2015–2020 年间的 Retina iMac 变成 Apple 芯片 Mac 的外接屏，先给七天试用，再决定是否买断。",
        "so_what": "「让旧硬件多活三年」是被低估的产品赛道；在消费降级与环保意识叠加的周期里，延寿类工具的商业潜力正在放大。"
    },
    "https://github.com/zhpencil/VimPDF": {
        "note": "VimPDF 用 Vim 式快捷键串起阅读与复习：高亮与批注之后可直接生成复习卡片，数据存在本地 SQLite，PDF 文件始终留在自己电脑。",
        "so_what": "「阅读—标注—复习」被割裂在三个工具里，谁先把它合成一条闭环，谁就拿到知识工作者的高频入口。"
    },
    "https://www.dezeen.com/2026/11/15/tant-a-temps-design-tang-architecture-cafe-laibei-1087-china/": {
        "note": "西安碑林旁的来杯 1087 咖啡馆保留原木梁柱，新家具全部采用悬挂或绕柱布置，让「新增的部分」随时可以整体撤回。",
        "so_what": "在历史建筑里做设计，最高级的姿态是「可逆」；把干预设计成可拆卸，比任何仿古手法都更尊重原物。"
    },
    "https://www.dezeen.com/2026/11/15/netherlands-central-bank-renovation-mecanoo/": {
        "note": "Mecanoo 改造荷兰央行时拆掉了后加的十四层圆塔，用花园与公共空间松开原本的防御边界，把金库这一封闭象征向公众打开。",
        "so_what": "机构建筑的改造本质上是权力叙事重写；敢于做减法、把「不可进入」变成「可以走进」，是空间民主化的具体动作。"
    },
    "https://www.designboom.com/design/gio-tirotto-domestic-chair-public-bench-italy-gulf-poets-vita-lenta/": {
        "note": "Gio Tirotto 把家用椅子拉长成海边公共长凳 La Lenta，取消分隔扶手，为 Gulf of Poets 多留一处能久坐的位置。",
        "so_what": "公共设计的核心指标不是造型而是「停留时长」；去掉扶手这个动作，等于主动邀请陌生人共享一段距离。"
    },
    "https://www.designboom.com/art/bird-plane-funny-weather-theo-triantafyllidis/": {
        "note": "Theo Triantafyllidis 的 Funny Weather 把曼彻斯特实时天气数据驱动成鸟群、云层与飞机的展览，换城市也换天气。",
        "so_what": "数据艺术的说服力来自「此刻此地」；绑定实时数据的装置天然具备不可复制的现场性，这是屏幕内容无法替代的价值。"
    },
    "https://www.woshipm.com/ai/6494227.html": {
        "note": "a16z 合伙人拆解 AI 应用如何获得高溢价：避开通用能力的价格战，把价值锚定在垂直工作流、专有数据与结果交付上。",
        "so_what": "定价权不来自模型能力而来自「替客户承担的后果」；越是能对结果负责的产品，越不需要参与 token 单价的内卷。"
    },
    "https://www.woshipm.com/share/6494231.html": {
        "note": "文章讨论品牌在「优雅地说谎」与「正确地讲真」之间的分寸：夸张是可被原谅的修辞，失真是不可逆的信任损耗。",
        "so_what": "AI 让内容生产变便宜的同时，也让「可信」变得更贵；愿意在关键事实上留出透明度的品牌，长期获客成本更低。"
    },
    "https://github.com/jmcbca04/declinekit": {
        "note": "DeclineKit 用开源方式回应支付信任问题：先是免费诊断，再走向订阅恢复工具，并提供 Stripe 应用，接入前可以先检查实现。",
        "so_what": "涉及钱的工具，开源可审计本身就是最强的销售话术；把「你可以先看代码」写在定价页上，比任何安全承诺都有效。"
    },
    "https://gami.fied.cc/": {
        "note": "GamiFied 是自托管的开源游戏化引擎，把业务事件换成经验值、连续记录与徽章，并做了幂等处理避免重复计数。",
        "so_what": "游戏化的失败多因「奖励与真实价值脱钩」；把事件建模做对、把幂等做稳，才有可能让成长系统真正影响留存。"
    },
    "https://www.woshipm.com/evaluating/6494225.html": {
        "note": "以「投入 100 万复刻《持械入宋》」为假设场景，横向比对两款国产新图模在角色一致性、镜头控制与成本上的实际差异。",
        "so_what": "影视级 AI 制作的选型标准已经从「单图好看」转向「跨镜头稳定」；模型的可控性比画质峰值更决定项目能不能交付。"
    },
    "https://www.woshipm.com/ai/6493996.html": {
        "note": "作者用 AI 做出 300 万播放的爆款视频，把选题、脚本、分镜、生成、剪辑与投放的完整流程逐环节拆开复盘。",
        "so_what": "爆款不是模型能力的产物而是流程设计的产物；把可复用环节固化成 SOP，才有第二次、第三次复现的可能。"
    },
    "https://www.woshipm.com/evaluating/6494221.html": {
        "note": "实测发现两个复杂任务就烧穿了 Fable 5.2 的月度套餐，文章同时肯定其规划能力的跃升与成本结构的陡峭。",
        "so_what": "强规划能力往往对应高 token 消耗；做 Agent 产品必须把「单任务预算上限」设计进产品，否则用户会在账单上被劝退。"
    },
    "https://www.woshipm.com/ai/6444818.html": {
        "note": "文章审视 AI 艺人现象背后的选择权问题：虚拟形象看起来给了用户更多选项，实际决定权仍在平台与版权方手里。",
        "so_what": "「看起来有选择」是当代产品最常见的幻觉；做内容工具时应把真实控制权交还创作者，而不是把选择做成摆设。"
    },
    "https://www.wzbj1616.com/script_info/1671": {
        "note": "琼瑶长篇小说《窗外》改编为 35 集电视剧的剧本：把一段青春成长与年代情感压缩进长篇剧集结构，处理师生关系与现实困境的尺度问题。",
        "so_what": "经典文本改编的难点不在情节而在「时代语境的翻译」；能否让今天的观众理解当年的困境，决定改编的成败。"
    },
    "https://www.wzbj1616.com/script_info/2298": {
        "note": "《黑客帝国 2》中文剧本：续作在不重复第一部设定的前提下抬高赌注，用锡安的政治线与架构师对话扩展世界观纵深。",
        "so_what": "续集写作的核心命题是「如何在不自我重复的前提下扩大格局」；把冲突从个人生存升级为系统选择，是可靠的结构解法。"
    },
    "https://www.wzbj1616.com/script_info/2323": {
        "note": "玄幻短剧《玄天归尘：玉女心经》：男频爽剧的功法体系设计与身份反转节奏，围绕修仙、仙侠与古装标签组织强钩子。",
        "so_what": "男频短剧的留存依赖「体系感 + 越阶快感」；功法层级写得越清晰，翻盘时的爽感就越有说服力。"
    },
    "https://www.wzbj1616.com/script_info/1690": {
        "note": "《反诈使命 平安中国》200 集短剧剧本：把反诈知识拆进可连载的单元结构，用侦查与社会现实线串起长周期叙事。",
        "so_what": "知识型内容的可持续性来自「单元化」；把教育目标拆成可独立成篇的故事单元，才有 200 集不断更的可能。"
    },
    "https://www.woshipm.com/pd/6494104.html": {
        "note": "文章追问「AI 能帮人做出系统，接下来谁来管」：交付之后的运维归属、责任边界与知识传承，正在成为新的组织难题。",
        "so_what": "AI 降低了「建设」的门槛，却抬高了「维护」的成本；产品设计必须把可维护性当作第一性需求，而非交付后的补丁。"
    },
    "https://www.woshipm.com/pmd/6276577.html": {
        "note": "系统梳理 GTM（市场推向策略）与 PM（产品经理）的职责差异与协同方式：一个负责把产品送进市场，一个负责把市场问题变成产品。",
        "so_what": "职责错位是产品失败的高频隐性原因；把 GTM 的验证信号接进产品决策回路，能显著降低「做出来没人买」的概率。"
    },
    "https://www.woshipm.com/share/6419345.html": {
        "note": "Anthropic 团队在 AI 让工程师产出翻八倍之后，发现新的协作难题：评审瓶颈、上下文同步与责任归属反而成为新的效率天花板。",
        "so_what": "个体产能提升不等于组织产能提升；当产出翻倍而评审不变，瓶颈会自动迁移到最慢的那个人身上。"
    },
    "https://www.woshipm.com/ai/6452804.html": {
        "note": "一个产品经理的生存报告：讲沟通、讲排雷，也讲在长期高压与频繁变更中如何与自己和解。",
        "so_what": "产品经理的长期竞争力有一半来自情绪稳定性；能管理好自己的预期，才可能在混乱的组织里持续输出判断。"
    },
}

lines = []
lines.append("---")
lines.append(f'title: "{title}"')
lines.append(f'date: "{date_str}"')
lines.append(f'highlights: "{highlights}"')
lines.append(f'epigraph: "{epigraph}"')
lines.append(f'lead: "{lead}"')
lines.append(f'scene: "{scene}"')
lines.append(f'cover: "{cover}"')
lines.append("items:")

missing = []
for item in candidates:
    url = item["url"]
    cat = item["category"]
    pinned = item.get("pinned", False)
    d = details.get(url)
    if not d:
        missing.append(url)
        d = {"note": item["title"], "so_what": "对转型中的产品人具有明确借鉴价值。"}
    lines.append(f"- category: {cat}")
    lines.append(f"  title: {item['title']}")
    lines.append(f"  note: {d['note']}")
    lines.append(f"  so_what: {d['so_what']}")
    lines.append(f"  source: {item['source']}")
    lines.append(f"  url: {url}")
    lines.append(f"  media: {item['media']}")
    lines.append(f"  pinned: {'true' if pinned else 'false'}")

lines.append("---")
lines.append("")
lines.append("### 岛主今日寄语")
lines.append("")
lines.append(closing_note)
lines.append("")

if missing:
    print("WARNING missing details:", missing)

out_path = f"/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/{date_str}.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Wrote {out_path} ({os.path.getsize(out_path)} bytes)")

all_used_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/all-used-urls.json"
used_list = json.load(open(all_used_path))
used_set = set(used_list)
old_len = len(used_list)
added = 0
for item in candidates:
    if item["url"] not in used_set:
        used_list.append(item["url"])
        used_set.add(item["url"])
        added += 1
json.dump(used_list, open(all_used_path, "w"), ensure_ascii=False, indent=2)
print(f"Updated used urls: +{added} ({old_len} -> {len(used_list)})")
