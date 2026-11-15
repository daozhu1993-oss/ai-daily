# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_nov_15_candidates import candidates

date_str = "2026-11-15"
title = "11 月 15 日 · 算力预算闸门与本地化反攻：DeepSeek 全家桶开源、Agent 装上花钱收据、浏览器接管全部推理"
highlights = "全网 9 大领域 36 篇高密度精选：DeepSeek 正式开放全家桶 API 让复刻 App 成为平民工程、MiniMax H3-Image 开源 10 秒出 4K、Shotoku 给 Agent 每次工具调用装上预算闸门、两人团队「卖 idea」卖出 400 万、Lampka 重做长文档暗色阅读、Daichi 森林桑拿让树干穿过平台、即梦短剧工作室 1300 元实测、《黑客帝国》中文剧本叙事节奏拆解、大模型迎来杰文斯时刻。"
epigraph = "当模型开始按 token 收钱，所有关于智能体的浪漫叙事都要重新算一遍账：真正稀缺的不再是能力，而是被授权的额度、能被审计的每一步，以及那些不愿意把数据交给云的固执。"
lead = "11 月 15 日，AI 产业的竞争重心从「谁更聪明」彻底滑向「谁更便宜、更可控、更留得住数据」。一手是 DeepSeek 正式开放全家桶 API，把曾经属于巨头的完整应用能力拆成可调用的零件，复刻一个 DeepSeek App 从团队工程变成平民周末项目；MiniMax H3-Image 用开源、10 秒出 4K、超长文本三张牌重新定义生图性价比。另一手是治理侧的集体补课：Shotoku 直接把自己插进 Agent 的执行路径，每一次工具调用都要先过预算闸门并留下收据；Coppice 为每个任务隔离工作树，先由人批准计划再分派 CLI；Cyberviber 干脆用一块 ESP32 小屏把「谁在等我」这件事变成物理信号。更有意思的是本地化反攻——Browser Whisper 把语音识别整条流水线搬进浏览器，Wipe 把 LaMa 推理迁到自定义 WebGPU，Xdoc 在本机渲染 PPTX。当推理成本与数据主权同时成为约束条件，产品设计的答案正在从「调用最强模型」转向「把最合适的模型放在离用户最近的地方」。而在商业一线，两人团队靠卖 idea 拿到 400 万、Stripe 透露前 100 家 AI 公司收入涨近 200%，提醒我们：这一轮真正的红利，属于懂得把交付物卖出去而不是把技术炫出来的人。"
scene = "「你给 Agent 加预算上限了吗？」「加了。它每调一次工具就要交一张收据，超预算直接卡住，比我管实习生还严。」「那它干活还利索吗？」「利索得像知道自己会挨罚的会计——每一分钱都花在能被审计的地方。」"
cover = "https://image.woshipm.com/2025/02/16/2f0f4a96-ec76-11ef-8495-00163e09d72f.png"
closing_note = "今天的 36 个切面共同指向一个不太浪漫但极其真实的结论：AI 的下一阶段不是更强，而是更「算得清」。DeepSeek 把能力拆成零件、Shotoku 把花费变成收据、Coppice 把执行权收回到人的批准按钮上——所有这些都是同一个动作：为失控的可能性装上限位器。对于转型中的产品人与独立开发者，这意味着两件事。第一，不要再把竞争押在「我用了哪个模型」上，那已经是公共基础设施；真正的护城河是你在成本、审计与本地化之间做出的那一组具体取舍，以及围绕这些取舍沉淀下来的工作流。第二，去找那些「不愿意上云」的场景——医疗记录、财务底稿、家族影像、政策敏感内容——那里没有流量红利，却有极高的信任溢价。把最合适的模型放在离用户最近的地方，把最脏的活交给能被审计的机器，把判断权和审美留在自己手里。这大概就是这个周期的全部答案。"

details = {
    "https://www.woshipm.com/ai/6493974.html": {
        "note": "DeepSeek 正式开放全家桶 API，把对话、推理、代码等能力全部拆成可独立调用的接口，开发者第一次能完整复刻一个 DeepSeek App 的全部行为。",
        "so_what": "能力层的护城河彻底塌了；产品人的差异化只剩交互设计、场景选择与工作流编排，模型本身不再是卖点。"
    },
    "https://www.woshipm.com/ai/6493967.html": {
        "note": "MiniMax H3-Image 实测复盘：开源权重、10 秒出 4K、超长文本理解三张牌，落到电商主图、长图文、分镜草图与版式延展四类真实玩法。",
        "so_what": "生图进入「性能过剩、成本见底」阶段；图像团队的竞争力从出图质量转向选题、批量一致性与后期工作流的工程化。"
    },
    "https://www.woshipm.com/ai/6493998.html": {
        "note": "「史上最严」湿实验预测基准发布，结果扎心：即使推理预算拉满、算力翻五倍，模型在真实生物实验预测上依然无法越过可靠性红线。",
        "so_what": "给所有「加算力就能解决」的乐观预期降温；在容错极低的科研与医疗场景，模型必须被当作假设生成器而非结论输出器。"
    },
    "https://whisper.tanpreet.xyz/demo/": {
        "note": "Browser Whisper 把语音识别整条流水线搬进浏览器：模型先下载到本地，再以 WebGPU 转写，全程不需要服务端密钥，音频不出设备。",
        "so_what": "隐私敏感型语音产品（会议、诊疗、法务）终于有了合规的技术底座；「本地推理 + 无密钥」正在成为 To B 的准入条件。"
    },
    "https://www.shotoku.dev/": {
        "note": "Shotoku 直接插进 Agent 的执行路径，在每次工具调用前返回批准、拒绝或待审三种状态，并为每一步留下可核对的收据与预算消耗记录。",
        "so_what": "Agent 治理从「事后看日志」走向「事前设闸门」；没接入执行路径的规则都只是装饰，预算控制必须变成架构而不是文档。"
    },
    "https://github.com/fertile-org/coppice": {
        "note": "Coppice 为每个 Agent 任务隔离独立工作树，先由人批准计划，再分派 CLI 执行，完成后的差异仍需人工验收，绝不自动合并。",
        "so_what": "多 Agent 并行的正确姿势不是放任自由，而是用工作树隔离 + 计划审批 + 人工验收三步，把并行度换成可控的返工成本。"
    },
    "https://cyberviber.de/": {
        "note": "Cyberviber 用一块 ESP32 桌面小屏，按紧急程度排列所有 Claude 会话，点按即可聚焦对应终端，把「谁在等我」变成可瞥一眼的物理信号。",
        "so_what": "当一个人同时跑五六个 Agent，「注意力调度」成为新的效率瓶颈；把数字状态外化到物理界面，是被低估的产品机会。"
    },
    "https://github.com/noambrand/ai-time-estimator": {
        "note": "时间估算器用操作量与本机会话速率算出 P10/P50/P90 概率区间，再用真实耗时反校，且明确不计人工等待时间。",
        "so_what": "给「AI 到底快了多少」这个模糊问题提供可验证的度量框架；概率区间比单点估时更诚实，也更适合用于排期谈判。"
    },
    "https://www.woshipm.com/share/6493912.html": {
        "note": "国内两人团队靠「卖 idea」做到 400 万收入：不卖软件不卖服务，只卖被验证过的问题定义与解决方案草图，交付物极轻但决策价值极高。",
        "so_what": "一人公司的定价锚点可以是「替客户省掉的试错成本」，而非工时；把想法打磨成可评估的资产，是知识变现的最高形态。"
    },
    "https://www.woshipm.com/chuangye/6493062.html": {
        "note": "离开 Meta 后她做了一条能分析情绪的 AI 项链，拿下 3300 万美元融资：把可穿戴从数据采集升级为情绪反馈，切进被忽视的心理健康场景。",
        "so_what": "硬件创业的机会不在参数而在场景错位；情绪与健康是最愿意为「被理解」付费的赛道，但需直面隐私与伦理的硬约束。"
    },
    "https://www.woshipm.com/chuangye/6493970.html": {
        "note": "Stripe AI 首席营收官透露，前 100 家 AI 公司收入涨了近 200%，其中一半来自海外市场。",
        "so_what": "AI 商业化的真实增量在跨境而非本土存量；从第一天就把定价、支付与合规设计成多市场可用，是这个周期的基本盘。"
    },
    "https://mopup.online/developers": {
        "note": "Mopup 专治开发环境的空间泄漏：聚焦构建缓存、Agent 工作树与开发服务器残留，扫描后由人核对再清理，避免误删未提交文件。",
        "so_what": "Agent 时代的运维新痛点正在浮现——工作树与缓存会以指数级增长；配套的清理与治理工具将成为开发者的刚需基础设施。"
    },
    "https://lampka.app/": {
        "note": "Lampka 重做长文档暗色阅读：只让文字页面变暗，图表与图片保留原色，另加悬停引文预览、分屏与离线朗读。",
        "so_what": "「局部暗色」比全屏反色更尊重阅读真实性；这类看似微小的取舍，恰恰是专业阅读工具区别于通用阅读器的分水岭。"
    },
    "https://structurify.io/en/playground/": {
        "note": "Xdoc 在浏览器里预览并导出 PPTX：整条渲染链留在本机，无需安装 Office，代价是排版会受支持特性与可用字体限制。",
        "so_what": "文档工具的去云化有明显的合规溢价；但同时必须诚实地把能力边界写在明面上，否则一次排版崩坏就会摧毁信任。"
    },
    "https://wipe.photos/": {
        "note": "Wipe 把 LaMa 推理迁移到自定义 WebGPU 实现，照片消除全程在浏览器内完成，并主动标注加速数字为作者自测。",
        "so_what": "把重推理搬到端侧已具备工程可行性；「本地处理 + 诚实标注」是获取专业用户信任的低成本高回报策略。"
    },
    "https://www.woshipm.com/pd/6493466.html": {
        "note": "智能硬件产品绕不开的 4 个真问题与 4 条应对原则：供应链、固件迭代、售后成本与合规认证，每一条都能把软件思维击穿。",
        "so_what": "软件产品经理转硬件的最大风险是低估物理世界的摩擦成本；先把售后与固件升级路径设计好，再谈功能创新。"
    },
    "https://www.dezeen.com/2026/11/14/daichi-inc-silent-river-tree-sauna/": {
        "note": "Daichi 设计的日本森林桑拿：纤薄木平台为既有树木留孔让树干穿过，玻璃桑拿房尽量减少视线阻隔，让林木成为空间本身的一部分。",
        "so_what": "最高级的空间设计是「退让」而非「添加」；为既有元素让位的克制，比任何造型语言都更能建立人与环境的关系。"
    },
    "https://www.dezeen.com/2026/11/14/arudeko-bianni-waste-wool-paper-material/": {
        "note": "Arudeko 把染色废羊毛与再生纸条交织成透光纸材 Bianni，可弯成灯罩，同时保留织物纹理与柔和透光性。",
        "so_what": "材料创新正在成为可持续设计的真实抓手；废料的重构比回收口号更能创造商业价值与视觉识别度。"
    },
    "https://www.dezeen.com/2026/11/14/parque-del-jaguar-colectivo-c733-tulum-mexico-ecological-park/": {
        "note": "C733 用干砌石墙组织墨西哥图卢姆 Jaguar 公园边界：石缝容许动物通行，游客设施集中收进已经被扰动的区域。",
        "so_what": "生态设计的关键不是造景而是划界；用低技术手段（干砌石）实现高复杂度目标，是可持续项目最经济的解法。"
    },
    "https://www.designboom.com/art/rune-bosse-living-lung-trees-life-support-ecological-collapse/": {
        "note": "Rune Bosse 把活树接上人工肺：透明膜随呼吸机鼓起收缩，让树木以医疗器械的方式「呼吸」，构成生态崩溃的视觉预演。",
        "so_what": "最有力的环保表达不是数据而是体感；把抽象危机翻译成可被身体感知的装置，是当代艺术介入公共议题的有效路径。"
    },
    "https://www.woshipm.com/ai/6474232.html": {
        "note": "a16z 最新消费洞察：AI 的付费机会并不在流量入口，而在流量之外的场景深处——那些原本没人愿意做、也做不完的琐碎工作。",
        "so_what": "别再挤 AI 超级 App 的独木桥；真正的付费意愿藏在低频、高痛、非标准化的工作里，那里没有流量却有预算。"
    },
    "https://pricemend.com/retailers": {
        "note": "Pricemend 整理 595 家门店的退货与保价政策，逐条保留原句与核查日期，未读条目明确标记待核，而不是用摘要糊过去。",
        "so_what": "在 AI 生成内容泛滥的时代，「可溯源 + 承认未知」本身就是产品力；诚实的数据结构比漂亮的总结更能建立长期信任。"
    },
    "https://www.woshipm.com/share/6493903.html": {
        "note": "小红书爆款卖货观察第一期：拆解平台内容与成交链路，指出爆款的三件前置功课——人群、场景与可复述的卖点。",
        "so_what": "种草不是文案技巧而是需求翻译；把产品放进具体生活场景并给出可复述的一句话，比任何投放模型都更有效。"
    },
    "https://www.woshipm.com/share/6477142.html": {
        "note": "重新定义「承诺」：不卖牛排，卖烧烤时的滋滋声——用户购买的不是参数，而是使用瞬间的感官预期与身份想象。",
        "so_what": "所有 To C 文案的底层动作都是「把功能翻译成体感」；谁能让用户先在脑子里听见声音，谁就先拿到成交。"
    },
    "https://www.woshipm.com/ai/6493844.html": {
        "note": "充了 1300 元实测即梦短剧工作室：逐项拆解钱花在哪里、哪些环节顺畅、哪些环节仍然卡手，给出真实的成本与产出对照。",
        "so_what": "AI 影视工具的真实门槛是「单位成片成本」而非单次生成效果；预算有限时，先跑通一条最短闭环再谈规模化。"
    },
    "https://www.woshipm.com/ai/6493976.html": {
        "note": "劝爸妈别刷 AI 短剧的真实困境：内容分级缺位、平台推荐无差别投放，让中老年用户暴露在高度套路化的情绪内容里。",
        "so_what": "AI 内容爆发正在制造新的数字鸿沟；面向银发群体的「内容健康度」设计，是被严重低估的产品与社会议题。"
    },
    "https://www.woshipm.com/ai/6367455.html": {
        "note": "凌晨 3 点上班的 AI 漫剧公司：为避开算力高峰期的高价，把渲染任务整体搬到深夜，形成被成本逼出来的「错峰生产」作息。",
        "so_what": "算力价格已经成为内容生产的排班变量；能调度好时间与算力曲线的团队，等于凭空多出三成毛利。"
    },
    "https://www.woshipm.com/operate/6373912.html": {
        "note": "猫猫互扇耳光的 AI 短剧全球疯传：几乎无对白、动作与情绪直给，绕开语言与文化的翻译损耗，实现极低成本的跨市场传播。",
        "so_what": "出海内容的最低成本路径是「去语言化」；用动作、情绪与节奏讲清楚一件事，比精致台词更容易突破文化边界。"
    },
    "https://www.wzbj1616.com/script_info/2299": {
        "note": "《黑客帝国》中文剧本拆解：世界观在动作场景中前置释放，关键信息分段投喂，红蓝药丸一场戏用极简选择完成人物与主题的双重确立。",
        "so_what": "高概念设定的正确打开方式是「边打边讲」；把世界观藏进动作与选择里，观众才不会在开场三分钟被设定压垮。"
    },
    "https://www.wzbj1616.com/script_info/2284": {
        "note": "《僵尸肖恩》中文版剧本：把类型恐怖与英式日常幽默焊在一起，用生活琐事的迟钝反应制造反差，让恐怖与喜剧共享同一套节拍。",
        "so_what": "类型混搭的关键是共享节奏而非拼接场景；当幽默与惊悚踩在同一拍子上，观众才会同时笑出声又被吓到。"
    },
    "https://www.wzbj1616.com/script_info/1670": {
        "note": "院线电影《智能木马》剧本：用犯罪悬疑的强钩子外壳，包裹技术伦理与社会现实议题，让类型快感承担议题表达。",
        "so_what": "严肃议题想被看见，必须先被「好看」；用类型片结构承载社会观察，是当下最有效的公共表达策略。"
    },
    "https://www.wzbj1616.com/script_info/2324": {
        "note": "男频玄幻短剧《元婴落地，我不许你们跪着活》：开局三分钟完成受辱、隐忍与越阶翻盘，爽点节拍密集且每集末尾必留反杀悬念。",
        "so_what": "短剧的留存公式是「羞辱—压抑—爆发」的高频循环；节奏密度比世界观深度更决定付费转化。"
    },
    "https://www.woshipm.com/ai/6429828.html": {
        "note": "AI 大厂集体转向的「杰文斯时刻」：单位推理成本下降并未带来支出下降，反而因为调用量暴涨导致总花费持续攀升。",
        "so_what": "别用「以后会更便宜」做产品假设；成本优化必须做进架构（缓存、路由、小模型分流），否则规模越大越亏。"
    },
    "https://www.woshipm.com/ai/6489955.html": {
        "note": "Agent 运作像开厨房：把点单、备料、出菜、退单对应到任务拆解、上下文准备、结果交付与异常回滚，用可管理的工序替代玄学调优。",
        "so_what": "Agent 产品的可用性来自流程设计而非提示词魔法；把不确定性收进有边界的工序，用户才敢把真实业务交出去。"
    },
    "https://www.woshipm.com/pmd/6190033.html": {
        "note": "高阶产品经理必懂的产品生命周期：从探索、增长、成熟到衰退，每个阶段的核心指标、组织形态与决策清单都截然不同。",
        "so_what": "最常见的能力错配是用增长期打法运营成熟期产品；先判断阶段，再决定要不要投入、投入多少、投在哪里。"
    },
    "https://www.woshipm.com/share/6339734.html": {
        "note": "未来设计的「双核大脑」：设计思维负责共情、定义与取舍，计算思维负责建模、验证与规模化，两者必须交替而非二选一。",
        "so_what": "AI 时代设计者的真正门槛是双核切换；只会共情无法规模化，只会计算做不出人愿意用的东西。"
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

for item in candidates:
    url = item["url"]
    cat = item["category"]
    pinned = item.get("pinned", False)
    d = details.get(url)
    if not d:
        print("MISSING DETAIL:", url)
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

out_path = f"/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/{date_str}.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Wrote {out_path} ({os.path.getsize(out_path)} bytes)")

all_used_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/all-used-urls.json"
used_list = json.load(open(all_used_path))
used_set = set(used_list)
old_len = len(used_list)
new_added = 0
for item in candidates:
    if item["url"] not in used_set:
        used_list.append(item["url"])
        used_set.add(item["url"])
        new_added += 1
json.dump(used_list, open(all_used_path, "w"), ensure_ascii=False, indent=2)
print(f"Updated used urls: +{new_added} ({old_len} -> {len(used_list)})")
