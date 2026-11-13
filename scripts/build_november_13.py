# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_nov_13_candidates import candidates

date_str = "2026-11-13"
title = "11 月 13 日 · 协同生态重拳对决与单兵产出重构：Agent 组织架构化、沙箱安全隔离与漫剧全流程交付"
highlights = "全网 9 大领域 36 篇高密度精选：字节跳动豆包工作开放模型接入硬刚腾讯 WorkBuddy、BAT 新旗舰大模型回归生产阵营、前 TikTok 核心成员 2500 美元驱动 Agent 军团承包 20 人产出、SafeScript 与 Attention Queue 筑牢终端自治防线、Seedance 跑通 AI 影视剧全流程长篇交付、云风魔改智能 ABC 输入法找回心流手感。"
epigraph = "当大厂不再满足于把 AI 当作悬浮窗里的聊天玩具，而是直接杀进组织架构图、把几十个自治 Agent 编排进真实业务流时，单兵开发者凭借极低摩擦的数字小队，第一次拥有了与百人正规军正面拼交付速度的筹码。"
lead = "11 月 13 日，AI 协同生态的火药味已从底层算力战全面蔓延至企业桌面与组织调度战场。字节跳动旗下豆包工作全面开放多模型接入，正面硬刚腾讯刚刚以 REA 状态机与生产级调度构筑护城河的 WorkBuddy——协同软件的终局，正在从“谁的对话框更好用”转向“谁能接管企业的组织架构图”。在单兵创业一线，前 TikTok 核心成员展示了震撼的“极简公司范本”：月耗 2500 美元调度 Agent 军团，一人硬扛 20 人团队的交付产能；而在极客研发端，SafeScript 打造 JavaScript 安全隔离子集、Attention Queue 为 tmux 中的 Claude Code 会话拉起注意力防撞队列，筑牢放权自治的安全底线。视听与内容阵地同样迎来分水岭：Seedance 跑通全流程数字人生成与高逼真长剧交付，漫剧分镜接入 Midjourney 形成闭环，宣告纯抽卡时代终结；云风魔改三十年前智能 ABC 输入法与山姆用高反差爆款掌握流量主动权的案例，更是提醒所有产研人：在自动化洪流面前，极致克制的交互设计与穿透人性的商业反差，永远是不可被替代的灯塔。"
scene = "「字节豆包工作开放了多模型接入，腾讯 WorkBuddy 也把多 Agent 组织调度跑顺了，协同软件这把火怎么越烧越旺？」「因为以前是你给 AI 分配任务，现在是 AI 同事自己拉群、建分支、抢活干。谁先在组织架构图里把数字人和真人无缝焊死，谁就拿到了下一个十年的企业入口。」"
cover = "https://tu.aixq.cc/wp-content/uploads/2026/11/WorkBuddy-01-18ee06c008.jpg"
closing_note = "今天的 36 个切面清晰地折射出一个不可逆转的趋势：AI 正在从“辅助个人的副驾驶”，彻底蜕变为“重构生产关系的调度中枢”。从字节与腾讯在企业工作台上的短兵相接，到 2500 美元驱动 20 人产出的单兵公司实践，甚至到影视剧组里由 AI 跑通全流程长篇交付，工具的形态都在从“单点问答”蜕变为“系统协同”。对于转型期的产研人而言，焦虑没有意义，退缩更无出路。要么学会像管理外包小队一样去调度、沙箱隔离并校验你的 Agent 军团；要么像云风精修输入法手感、设计师抠细分镜光影那样，坚守人类在审美、常识与终极商业决断上的“不可替代权”。把脏活交给机器，把灵魂留给自己。"

details = {
    # AI 资讯
    "https://www.woshipm.com/ai/6493081.html": {
        "note": "字节跳动重磅升级豆包工作协同平台，不仅打破自研模型壁垒开放第三方大模型自由接入，更直指腾讯 WorkBuddy 的核心腹地，拉开巨头协同工作台正面对决序幕。",
        "so_what": "协同软件竞争重心正式从“自带哪个闭门模型”转向“多模型混合调度与工作流编排生态”；拥有更开放集成能力的桌面工作台将快速吸纳企业既有资产。"
    },
    "https://www.woshipm.com/it/6493196.html": {
        "note": "复盘国内 BAT 新一代旗舰模型密集发布后的格局嬗变：不再盲目比拼榜单虚高评分，而是全面下沉至各家公有云、办公套件与工业场景拼生产级落地 ROI。",
        "so_what": "大模型进入“唯有生产环境真交付才算数”的务实期；企业与个人采购时必须按真实调用延迟、长文本退化率和并发单价核算综合账目。"
    },
    "https://www.woshipm.com/ai/6492556.html": {
        "note": "深度原理 Hydrogen-1.0 评测报告：针对科研推理、复杂数学证明与长篇学术文献跨领域交叉检索专门优化，在严谨学术问答体感上超越常规通用大模型。",
        "so_what": "印证垂直领域推理模型对通用大模型的错位竞争优势；在容错率极低的科研与硬核工程场景，强逻辑约束的模型比通才聊天助手更有黏性。"
    },
    "https://huggingface.co/papers/2611.12304": {
        "note": "面向大规模自主智能体长上下文推理的高性能服务架构论文：提出 Agent-Adaptive 动态资源感知调度，针对智能体多轮自省与工具调用的突发并发做算力伸缩。",
        "so_what": "为下一代企业级 Agent 集群部署提供关键基建参考；告别传统固定配额部署，用动态自适应服务层把智能体吞吐成本降低数倍。"
    },
    # AI 协作
    "https://github.com/SafeScript/safescript": {
        "note": "专门针对大模型生成代码执行安全设计的 JavaScript 极简安全子集：在语言规范层面彻底斩断不可信网络访问与环境污染漏洞，提供天然沙箱隔离。",
        "so_what": "当让 Agent 在本地跑代码成为标配，传统的外部容器隔离太重；从执行引擎和语言子集底层设防，才是轻量嵌入式协同工具的终极安全防线。"
    },
    "https://github.com/nodo-labs-uk/attention-queue": {
        "note": "为在 tmux 中多窗口运行 Claude Code 的极客量身打造的注意力队列 TUI 工具：支持对并发代理的每一步关键操作进行排队审查、单步放行或随手微调。",
        "so_what": "解决开发者一人统筹多只代码小队时的“注意力过载与审查漏网”痛点；将混乱的终端切换梳理成井井有条的审批流，大幅降低代码翻车概率。"
    },
    "https://www.woshipm.com/ai/6481849.html": {
        "note": "深入拆解腾讯 WorkBuddy 的技术底层实现：详解其如何利用 REA（Reasoning-Execution-Audit）状态机与多 Agent 组织调度图，把模糊指令转化为稳定生产成果。",
        "so_what": "生产级 Agent 产品设计的标杆级工业拆解；证明没有严格的状态机约束与审计流，任何 Agent 系统进入真实企业业务时都会被不可控的长尾异常拖垮。"
    },
    "https://www.woshipm.com/ai/6492769.html": {
        "note": "梳理 Grok Bot 协同大版本的关键进化：不再局限于单一聊天窗口问答，而是支持像真人同事一样驻留群聊、主动捕捉未决事项并跨系统协同推进脏活累活。",
        "so_what": "协作形态正在从“召之即来挥之即去”的被动助手，进化为“常驻团队敏锐补位”的自治伙伴；对协同工具的人机角色边界提出了全新定义。"
    },
    # 一人公司
    "https://www.woshipm.com/chuangye/6492482.html": {
        "note": "前 TikTok 核心骨干创办 AI 原生单兵公司的真实财务复盘：全职仅创始人一人，通过月度花费 2500 美元调用各种 Agent 自动完成市场调研、文案生成与代码测试。",
        "so_what": "超级个体的教科书级落地实操；证明在大模型时代，单兵无需组建庞大管理层，只要把工作流切分得足够结构化，一人就能扛起百万元级 ARR 营收。"
    },
    "https://www.woshipm.com/chuangye/6493011.html": {
        "note": "剖析新一代社交与效率产品的逆向设计哲学：打破依靠算法让人持续沉迷刷屏的传统套路，反其道而行之帮助用户在极短时间内完成目标并立刻离开。",
        "so_what": "在数字过载与注意力剥削愈演愈烈的环境下，“尊重时间、用完即走”正在从道德口号转化为极具商业溢价的差异化产品卖点。"
    },
    "https://termsheetplease.com/": {
        "note": "独立开发者打造的像素风趣味互动小游戏：戏仿经典游戏《请出示文件》，让玩家扮演疲于奔命的投资经理对各种离谱的创业项目与 Term Sheet 进行尽职调查。",
        "so_what": "极佳的情绪共鸣与病毒式传播案例；深挖创投圈行业黑话与荒诞痛点，以极低开发成本击穿高净值极客与投资人群圈层。"
    },
    "https://litek8s.dev/": {
        "note": "用纯 Rust 语言手搓的轻量级单二进制 Kubernetes API 实现：空载待机仅占 23MB 内存，极大降低了在边缘节点和本地开发机跑 K8s 生态工具的门槛。",
        "so_what": "一人公司向基础系统工程深度突围的优秀样板；把笨重复杂的企业级标准重构成极度灵巧的单兵武器，精准收割极简主义运维开发者。"
    },
    # 产品设计
    "https://blog.codingnow.com/2026/11/abc_mod.html": {
        "note": "著名程序员云风（CodingNow）分享动手魔改三十年前智能 ABC 输入法的心路历程：剔除现代输入法臃肿的云端词库与弹窗杂音，追求毫秒级零延迟与无干扰心流输入。",
        "so_what": "对当下泛滥的“花哨臃肿功能堆砌”最深刻的技术反思；产品经理当知：最极致的用户体验往往不是增加了什么，而是把干扰心流的杂质彻底剔除。"
    },
    "https://spirolo.com/": {
        "note": "用 Rust 编写的前端测试套件隐患静态分析工具：不仅分析性能卓越，其官网与分析报告排版更融入极具高级感的三维透视与微质感图表设计。",
        "so_what": "开发者工具“审美消费级化”的典范；把枯燥死板的代码扫描终端输出，升华为富有视觉享受的交互报表，直接拉开与其他开源 CLI 的心智差距。"
    },
    "https://github.com/humanethq/airgap-check": {
        "note": "专门审计 AI 开源仓库在断网（--network none）极端环境下能否稳定运行的开源工具：快速捕捉那些隐蔽依赖外部网络下载权重或上报埋点的潜在崩溃点。",
        "so_what": "在金融、涉密军工与高合规行业，离线可用是硬红线；一款贴心的小工具能大幅简化企业合规采购团队的本地化可用性排查流程。"
    },
    "https://av.github.io/safe-sand/": {
        "note": "基于 WebGL2 的超逼真流体物理沙粒交互模拟站：指尖在屏幕划过即可带起物理碰撞、重力堆叠与色彩流转，展现惊人的浏览器图形学计算力。",
        "so_what": "微交互与数字联觉的终极展示；即使没有任何文字说明，纯粹的物理触感与流体响应就能在瞬间捕获用户的感官愉悦，适合汲取进前沿触觉反馈设计。"
    },
    # 审美提升
    "https://www.dezeen.com/2026/11/12/minimal-pedal-4-delivery-vehicle/": {
        "note": "Minimal 设计团队打造的 Pedal 4 微出行货运载具：将小型电动货车的防护舱体与货运自行车的轻灵骨架结合，线条极其流畅洗练，重构物流末端市容。",
        "so_what": "工业设计对城市公共环境美学的重要塑造；让工具车脱离“破旧粗糙”的刻板印象，赋予城市基础设施体面而有温度的现代科技雕塑感。"
    },
    "https://www.dezeen.com/2026/11/09/sony-walkman-headphones-mdr-3r/": {
        "note": "Sony 让 1979 年伴随初代 Walkman 问世的经典橙色海绵头戴耳机以现代技术 MDR-3R 重生：极致纤细的金属头梁与高饱和橙色碰撞出跨越时代的先锋气息。",
        "so_what": "情怀符号与现代工艺结合的高阶美学样本；真正经典的设计语言拥有超越周期的抗衰老能力，在数码产品千篇一律的今天散发独树一帜的辨识度。"
    },
    "https://www.dezeen.com/2026/11/06/dado-furniture-allen-kaufmann/": {
        "note": "设计师 Allen Kaufmann 推出的 Dado 家具系列：整套实木桌椅无需任何螺丝或金属连接件，全凭一道经过精密测算的单一机械卡榫结构完美自锁。",
        "so_what": "“结构即装饰”极简哲学在家具领域的巅峰演练；摒弃一切冗余涂抹，让连接处的物理咬合本身成为最耐人寻味的审美焦点。"
    },
    "https://www.dezeen.com/2026/11/10/gustaf-westman-full-disney-collection-donald-duck-bookstand/": {
        "note": "瑞典设计新星 Gustaf Westman 联名迪士尼推出全套雕塑感家居：将唐老鸭经典翘臀、米奇大耳朵与标志性波浪曲面融为一体，充满童趣而不失高级冷感。",
        "so_what": "大众流行文化 IP 向当代先锋设计语言转译的高分作业；用克制的高级调色与雕塑线条提炼经典动画符号，成功跳脱出廉价儿童周边范畴。"
    },
    # 产品营销
    "https://www.woshipm.com/operate/6493004.html": {
        "note": "深度解构山姆会员店的爆款操盘逻辑：为什么左手卖 20 元的巨无霸泡面桶引发全网疯抢，右手卖 399 元高质感羽绒服迅速售罄，背后的心智锚定策略何在？",
        "so_what": "掌握反差定价与社交货币供给的营销高段位；用极端吸睛的平价符号撬动自发传播，再借会员严选背书把高客单长尾品类顺滑带走。"
    },
    "https://www.woshipm.com/it/6493087.html": {
        "note": "餐饮行业把外卖平台满减补贴当做“抖加信息流”投流的新打法剖析：通过精密计算起送门槛与阶梯优惠，用极低补贴成本换取外卖首页与全城列表霸榜。",
        "so_what": "把既有平台的流量分发算法摸透之后的跨维度套利；证明商业操盘手永远不要只看工具的字面定义，将其改造成获客漏斗才能赚取超额回报。"
    },
    "https://www.woshipm.com/marketing/6492890.html": {
        "note": "线下实体门店价格战与扩张惨痛复盘：许多品牌在疯狂补贴中虽然短期抢下了账面市场份额，却因服务质量崩塌把真正高价值的老客户彻底驱离。",
        "so_what": "深刻的商业增长警钟；没有留存与单位正向经济模型的规模扩张无异于饮鸩止渴，产品营销的终极目的是筛选高黏性资产而非收割流动羊毛。"
    },
    "https://www.woshipm.com/ai/6332345.html": {
        "note": "详述 Agent Skills 规范如何让资深从业者的实战经验变成可结构化分发、按次调用的标准化数字资产，引发一场知识资本化与个人 IP 变现的全新浪潮。",
        "so_what": "内容创作者与专家顾问的盈利模型重构；未来的顾问咨询不再按小时卖嘴皮子，而是把多年踩坑经验打包成开箱即用的 Agent Skill 躺着收税。"
    },
    # AI 漫剧
    "https://www.woshipm.com/it/6492533.html": {
        "note": "实测 Seedance 全流程数字人影视剧生成管线：打通从分镜脚本、高拟真演员一致性控制到长篇剧情全流程渲染交付，实现短剧低成本工业化量产。",
        "so_what": "标志着 AI 漫剧正式迈过“只能拍几秒片段拼剪”的粗糙阶段，全面进驻长剧集工业化生产流；影视制作的产能门槛被永久性击穿。"
    },
    "https://www.woshipm.com/ai/6492976.html": {
        "note": "拆解专业美术设计师使用 AI 生成短剧分镜时的核心技法鸿沟：为什么普通人总生成千篇一律的网感大头照，而高手凭借三维空间透视与光线落点提示词稳出大片？",
        "so_what": "AI 工具越普及，基础美学素养与导演思维的溢价就越高；掌握景别过渡、视线顺畅引导与色彩心理学，是漫剧创作者拉开阶梯差距的真正内功。"
    },
    "https://www.woshipm.com/ai/6492564.html": {
        "note": "MiniMax 与 Seedream 两大主流商用生图模型在短剧制作场景的硬核横评：对比两者在复杂肢体交互、连续角色微表情及大纵深场景渲染上的优劣路线。",
        "so_what": "为 AI 漫剧团队技术选型提供详实基准；在制作管线中切忌死守单一模型，前台角色特写与背景大景别分流调用才是平衡质量与算力成本的正解。"
    },
    "https://www.woshipm.com/ai/6276556.html": {
        "note": "Lovart 全面接入 Midjourney 生态的全家桶实战指南：通过结构化提示词模板与运镜轨迹约束，让生图天花板 MJ 直接无缝服务于漫剧分镜的一键产出。",
        "so_what": "解决独立创作者在多个平台反复来回折腾画幅与垫图的低效困境；将顶级画质引擎打包进工业化工作流，大幅提速漫剧前期的脚本视听化速度。"
    },
    # 编剧技巧
    "https://www.wzbj1616.com/script_info/2261": {
        "note": "120 集女频爆款微短剧剧本范本《穿成虐文炮灰千金，我不演了》：主角穿书开局即掀桌，拒绝沦为原著男主虐恋道具，以理智打脸与独立商业崛起为主线。",
        "so_what": "精准切中现代女性观众对“传统苦情自残叙事”的彻底厌弃；将爽点重心从“求得男主施舍”转移为“自我价值与权力的重新夺取”，情绪代入极强。"
    },
    "https://www.wzbj1616.com/script_info/2256": {
        "note": "百集甜宠萌宝剧本《替嫁萌宝》全集拆解：运用替嫁与萌宝双重高概念钩子，把契约夫妻之间的冰冷试探通过软萌助攻转化为高频情感升温推进器。",
        "so_what": "短剧下沉市场永不过时的情感母题结构；萌宝既是天然的剧情润滑剂也是解构严肃矛盾的喜剧工具，能以极低情绪门槛牢牢锁定全家型观众。"
    },
    "https://www.wzbj1616.com/script_info/2264": {
        "note": "现实主义都市情感短剧《她说没事》剧本精读：聚焦职场与人际交往中普遍存在的“讨好型人格”，通过细微的情绪压抑与突如其来的临界爆发推动戏剧反转。",
        "so_what": "示范小成本都市剧如何用扎实的情感观察打动人心；不靠夸张狗血的互扇耳光，靠真实可感的职场心理共鸣同样能实现高完播与深度二创裂变。"
    },
    "https://www.wzbj1616.com/script_info/2265": {
        "note": "奇幻微悬疑喜剧《月迷津渡》创作技法剖析：在民俗微恐与迷雾小镇的肃杀基调中，巧妙穿插欢喜冤家的轻喜剧笑点，形成张弛有度的视听波浪。",
        "so_what": "类型片混搭的高级手法；微恐制造悬疑危机抓住注意力，轻喜缓解心理疲惫释放多巴胺，两者交替共振使观众不知不觉连刷数十集而不觉疲劳。"
    },
    # 产品经理
    "https://www.woshipm.com/pmd/6487883.html": {
        "note": "深度探讨女性产品经理在复杂软件系统操盘中的进阶之道：如何将天然敏锐的用户共情能力，与技术博弈和商业收益中的冷酷决断力无缝融合。",
        "so_what": "高级产品人必备的双轨思维：只有共情容易陷入细节溺爱，只有决断容易偏离真实人性；能在两者之间游刃有余调配重心者方可执掌大型业务底盘。"
    },
    "https://www.woshipm.com/pmd/6472679.html": {
        "note": "重新标定产品经理不可被替代的 5 大核心基石职责：需求定义、价值排序、跨职能对齐、商业闭环落地与生命周期度量，击碎所谓“AI 淘汰产品经理”的恐慌。",
        "so_what": "给技术变革期迷茫从业者的定心丸；大模型可以替你画高保真原型和写需求文档，但决定“做不做、为谁做、谁买单”的商业常识永远在人脑之中。"
    },
    "https://www.woshipm.com/ai/6404370.html": {
        "note": "犀利剖析过度迷信 AI 自动化带来的产品灾难：当团队习惯于让大模型自动产出 PRD 与竞品报告时，往往会在脱离真实业务一线的同时陷入平庸功能死循环。",
        "so_what": "敲响产品思考外包的警钟；没有亲临一线访谈用户和拆解底层财务数据的所谓“智能生成文档”，只会制造更多无人问津的数字垃圾。"
    },
    "https://www.woshipm.com/share/6319547.html": {
        "note": "资深数据产品经理踩坑实录：深入剖析同比、环比在不同商业季节性与业务突发变动下的失真陷阱，给出构建多维度动态基准指标的科学方法。",
        "so_what": "做数字化与智能决策产品不可或缺的基础功底；脱离业务实质的机械指标对比不仅毫无指导意义，反而会误导核心管理层做出灾难性预算决策。"
    },
}

lines = [
    "---",
    f"date: '{date_str}'",
    f"title: {title}",
    f"highlights: {highlights}",
    "draft: false",
    f"epigraph: {epigraph}",
    f"lead: {lead}",
    f"scene: {scene}",
    f"cover: {cover}",
    "items:",
]

for item in candidates:
    url = item["url"]
    cat = item["category"]
    pinned = item.get("pinned", False)
    d = details.get(url, {})
    note = d["note"]
    so_what = d["so_what"]

    lines.append(f"- category: {cat}")
    lines.append(f"  title: {item['title']}")
    lines.append(f"  note: {note}")
    lines.append(f"  so_what: {so_what}")
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

print(f"Successfully wrote {out_path} ({os.path.getsize(out_path)} bytes)")

all_used_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/all-used-urls.json"
with open(all_used_path, "r", encoding="utf-8") as f:
    used_list = json.load(f)

old_len = len(used_list)
used_set = set(used_list)
new_added = 0
for item in candidates:
    if item["url"] not in used_set:
        used_list.append(item["url"])
        used_set.add(item["url"])
        new_added += 1

with open(all_used_path, "w", encoding="utf-8") as f:
    json.dump(used_list, f, ensure_ascii=False, indent=2)

print(f"Updated {all_used_path}: added {new_added} URLs (total {old_len} -> {len(used_list)})")
