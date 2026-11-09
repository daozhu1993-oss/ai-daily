# -*- coding: utf-8 -*-
import json
import os

date_str = "2026-11-09"
title = "11 月 09 日 · 从玩具到生产系统：权限沙箱、资产自建与智能体运营落地"
highlights = "全网 9 大领域 36 篇高密度精选：腾讯云企业级 Service Agent 平台从搭到管、字节 AI 业务重整与单点工具反思、《持械入宋》120亿播放主创专访、APC 本地权限规则沙箱、端到端零知识笔记与买断制个人云盘、律政短剧《正义的边界》全本拆解。"
epigraph = "把智能体放进真实业务的泥泞战壕里，决定它能不能活下来的从来不是跑分有多高，而是它有没有被锁进不可越权的权限沙箱，以及你有没有把它当成一套长期演进的运营系统。"
lead = "11 月 9 日，整个 AI 产研生态正在从“炫技式的单点 Demo”全面退潮，大步迈入“深入业务死穴的系统化运营与资产自建”深水区。在平台与架构层，腾讯云企业级 Service Agent 平台明确划出从“搭 Agent”到“管 Agent”的分水岭，治理与调度成为核心命题；字节跳动内部 AI 业务线的深刻重整更是给所有团队敲响警钟：脱离真实业务场景的单点 Agent 工具再惊艳也难逃被边缘化的命运。在协作与安全端，APC（Aleph Permission Control）将细粒度权限判定下沉到本地沙箱，彻底把控工具调用的危险越权；在独立开发与商业化层面，买断制个人云盘 DoShare、八位音乐分享 Chiptunes、纯本地端到端加密笔记 Notekpr 展现出用户对“资产所有权与隐私掌控”的强烈回归；而在短剧与漫剧赛道，非科班草根团队打造 120 亿播放《持械入宋》的实操经验，以及基于 Codex + Obsidian + Skill 的个人漫剧工业化工作台，证明在内容赛道建立高壁垒工作流比依赖外部投流更具复利价值。"
scene = "「为什么你们砍掉了那个能写诗写文案的华丽 Agent？」「因为它像个天天在办公室高谈阔论却连报销单都填不对的实习生。我们要的是能钻进系统底层跑对账单、每一步操作都有权限断言的实干家。」"
cover = "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80"
closing_note = "今天的 36 个创新切片都在讲述同一个硬道理——离开业务死穴的 AI 不过是空中楼阁，守住权限边界的系统才是真金白银。当潮水褪去，单纯的‘搭 Agent’早已不再是护城河，唯有像 FDE（前向部署工程师）一样跳进业务的泥泞战壕，将不可违背的权限沙箱、持续演进的运营链路以及创作者自主掌控的资产沉淀牢牢扎根于泥土中，你才能在这场深刻的洗牌中笑到最后。"

from verify_nov_09_candidates import candidates

# Build markdown file
md_content = f"""---
date: '{date_str}'
title: {title}
highlights: {highlights}
draft: false
epigraph: {epigraph}
lead: {lead}
scene: {scene}
cover: {cover}
items:
"""

pinned_counts = {
    "AI 资讯": 0,
    "AI 协作": 0,
    "一人公司": 0,
    "产品设计": 0,
    "审美提升": 0,
    "产品营销": 0,
    "AI 漫剧": 0,
    "编剧技巧": 0,
    "产品经理": 0
}

for item in candidates:
    cat = item["category"]
    pinned = pinned_counts[cat] < 2
    pinned_counts[cat] += 1
    
    note = item.get("note", "")
    so_what = item.get("so_what", "")
    
    md_content += f"- category: {item['category']}\n"
    md_content += f"  title: {item['title']}\n"
    md_content += f"  note: {note}\n"
    md_content += f"  so_what: {so_what}\n"
    md_content += f"  source: {item['source']}\n"
    md_content += f"  url: {item['url']}\n"
    md_content += f"  media: {item['media']}\n"
    md_content += f"  pinned: {'true' if pinned else 'false'}\n"

md_content += f"""---

### 岛主今日寄语

{closing_note}
"""

# Let's populate the detailed note & so_what for all items
details = {
    # AI 资讯
    "https://git-aarvin.github.io/mei/": {
        "note": "将大模型的吞吐性能、上下文延迟与实际 API 计费成本直观并排对比的极简评估仪表盘，助工程师告别凭感觉选型。",
        "so_what": "砍掉企业技术选型中的虚幻溢价；让产品经理与架构师能够以明确的单位 Token 产出比核算架构方案，把算力账单锁死在健康区间。"
    },
    "https://amsach.github.io/maple/": {
        "note": "针对混合专家（MoE）模型的定向权重修剪与稀疏化框架：在保留核心推理通路的前提下，将数十 GB 的庞大模型精简至可在消费级硬件上流畅离线运行。",
        "so_what": "本地化与端侧私有部署的普惠利器；极大压低了垂直场景专精模型的部署门槛，让无外网孤岛环境也能拥有高水准推理大脑。"
    },
    "https://modelrefs.com/": {
        "note": "颠覆传统刷榜基准（Leaderboard）的新型模型雷达：每一项模型能力的评分都强关联至公开可复现的代码示例与生产失败案例回放。",
        "so_what": "终结大模型厂商的公关宣传跑分泡沫；让开发团队根据实际业务中遇到的生僻语法、长程推理与边界报错挑选真正靠谱的基座。"
    },
    "https://offlinevault.dev": {
        "note": "开箱即用的完全离线知识管理与问答方案：将文档索引、向量嵌入与端侧轻量小模型封装为单个独立可执行包，无需安装任何复杂依赖。",
        "so_what": "高度合规敏感行业（法务、军工、医疗）知识资产数字化的黄金解法；实现物理级网络阻断下的智能问答，绝无数据外泄之虞。"
    },
    # AI 协作
    "https://playground.alephapc.com/": {
        "note": "赋予开发者在本地零成本模拟与调试 Agent 行为准则的权限控制游乐场：利用声明式策略文件拦截危险命令、校验参数合法性并设置条件审批。",
        "so_what": "解决企业不敢把写权限交给自主智能体的根本障碍；让安全合规团队在 Agent 上线前像编写防火墙规则一样精细打磨安全防线。"
    },
    "https://plannotator.ai/inbox/": {
        "note": "专为人类与自主 Agent 协作设计的异步收件箱：当智能体在长程推演中遭遇高风险操作或模糊意图时，自动生成结构化卡片静候人类批准。",
        "so_what": "彻底打通人机协作的‘半自动’黄金分割点；避免开发者被迫全程盯盘，把低认知负荷的流水线交由机器，人类只在高杠杆决策点一键批复。"
    },
    "https://psicode.ai/": {
        "note": "超轻量级的便携式编码 Agent 微内核：无需常驻后台重型服务，直接以跨平台单个小二进制运行，支持与各种 IDE 及终端无缝咬合。",
        "so_what": "极客与数字游民的极速开发外脑；在资源受限的轻薄本甚至树莓派上也能瞬间唤醒，提供精准的代码重构与测试辅助。"
    },
    "https://codend.dev": {
        "note": "从需求描述直接演进为云端预览分支与 GitHub PR 的全自动交付流水线：Agent 自主拉取分支、编写代码、运行自动化测试并生成即时预览链接。",
        "so_what": "重新定义初级研发工作流的交付标准；团队负责人无需再在本地编译审查，直接在浏览器中体验功能分支并一键合入生产。"
    },
    # 一人公司
    "https://chiptunes.studio/": {
        "note": "单页原生 WebAudio 实现的 8-bit 芯片音乐创作器：无需注册、即开即弹，并将全曲音符编码压缩至单个 URL Hash 中便于一键传播。",
        "so_what": "零后端成本、纯前端计算的单兵软件典范；巧妙利用 URL 状态持久化消除数据库开销，在怀旧极客圈迅速引爆自然病毒式传播。"
    },
    "https://getcloud.doshare.me/": {
        "note": "针对订阅制疲劳群体的个人私有云盘商业创新：用户单次付费购买软件授权，配合自有 S3 兼容对象存储，彻底告别按月割韭菜。",
        "so_what": "一人公司对抗 SaaS 订阅大厂的差异化杀手锏；切中用户对数据主权与成本可控的深层诉求，靠一次性清晰买断建立稳健现金流。"
    },
    "https://fuelpriceatlas.com/": {
        "note": "专注全球各国实时官方燃油价格的垂直数据地图：通过爬虫自动化清洗多国能源部公开接口，为跨国物流、自驾游与跨境车队提供透明价格基准。",
        "so_what": "典型的小而美自动化信息差变现产品；微小切口、持续更新，通过高质量 SEO 与垂直行业定向广告实现常年被动收入。"
    },
    "https://kindleclippings.pages.dev/": {
        "note": "极致纯粹的浏览器端静态工具：直接解析用户导出的 My Clippings.txt 原始文档，在本地 IndexedDB 中进行去重、标签分类与 Markdown 格式转换。",
        "so_what": "践行隐私第一与零服务器运维成本的极简哲学；给千万重度电子书读者提供了安心可靠的永久笔记整理利器。"
    },
    # 产品设计
    "https://github.com/Shann5/tab-league": {
        "note": "极其体贴的浏览器标签页管理微创新：在用户误关标签页的黄金 5 秒内，以非侵入式的悬浮徽标提供无缝撤销与情境快照恢复通道。",
        "so_what": "典范级的防御性设计（Defensive Design）；将用户不慎犯错的挫败感转化为令人惊喜的掌控感，细节见真章。"
    },
    "https://notekpr.md": {
        "note": "将极简 Markdown 写作与客户端密码学无缝熔铸的笔记应用：所有文字在离开设备前完成对称加密，服务器仅充当不可视的盲中继。",
        "so_what": "现代协作软件对隐私底线的主动捍卫；证明极致安全并不必然牺牲轻快流畅的编辑体验，为私密知识库立下新标杆。"
    },
    "https://justapause.com": {
        "note": "巧妙结合前置摄像头视线追踪的轻量桌面工具：一旦检测到使用者头部偏离屏幕，瞬间将敏感窗口施加磨砂毛玻璃遮罩，回正时平滑恢复。",
        "so_what": "公共场所（咖啡厅、高铁、开放工位）办公者的安全感倍增器；用自然的行为感知替代繁琐的手动锁屏快捷键，优雅且克制。"
    },
    "https://fuzzyfoundry.com/emcee": {
        "note": "打破传统操作系统窗口层叠混乱的原生管理工具：允许用户像移动物理卡片一样把关联的应用窗口编组、命名并在多屏幕间无缝甩动。",
        "so_what": "深度工作者认知负荷的有效减压阀；将杂乱的多任务上下文收敛为逻辑清晰的专注工作区，重塑桌面交互直觉。"
    },
    # 审美提升
    "https://www.designboom.com/architecture/raw-concrete-steel-stripped-back-1960s-apartment-zagreb-simple-architecture/": {
        "note": "克罗地亚老旧公寓改造的极致空间样本：剥离廉价石膏吊顶与墙皮，裸露出六十年代坚实质朴的原生混凝土梁柱，搭配定制暖色橡木家具。",
        "so_what": "粗粝与温润的张力对话；启发数字产品在极简质感设计中善用留白与底色肌理，营造耐人寻味的恒久质感。"
    },
    "https://www.designboom.com/architecture/sweeping-concrete-zao-art-center-rizhao-china/": {
        "note": "山东日照山坡上的大地艺术建筑：巨型平缓混凝土曲面从山体蜿蜒伸出，精密计算的几何天窗将海天光影引入幽深展厅。",
        "so_what": "建筑与自然环境共生的东方诗意；为界面设计提供了宏大与精微并存的体量节奏参考，用结构本身说话。"
    },
    "https://www.designboom.com/art/scaffolding-safety-mesh-observation-platforms-lugano-demolition-sites-sit-for-a-while-sknypl/": {
        "note": "瑞士卢加诺拆迁工地的临时空间干预：利用脚手架与亮色安全网搭建公共观景台，邀请市民停下脚步凝视城市代谢与建筑解构全过程。",
        "so_what": "将‘建设中的瑕疵’转化为‘美学参与’的先锋视角；启示产品人正视系统迭代中的过渡态，让用户参与产品的生命演化。"
    },
    "https://www.wallpaper.com/design-interiors/lighting/angelo-lelii-guide-arredoluce-lighting-design": {
        "note": "战后意大利传奇照明品牌 Arredoluce 创始人设计生涯回顾：将精密的黄铜关节、配重平衡臂与色彩明快的小巧遮罩结合得天衣无缝。",
        "so_what": "机械功能性与形式优雅感的完美平衡；在纯粹工程结构中注入诗意，为复杂交互系统的精简表达提供无尽灵感。"
    },
    # 产品营销
    "https://recap.studio/": {
        "note": "专为 SaaS 独立开发者打造的视频营销神器：智能分析鼠标光标与关键交互区域，自动平滑缩放画面并添加高质感动态阴影背景。",
        "so_what": "极大压低专业级产品宣发视频制作门槛；让技术人员无需苦学 Final Cut，几分钟内即可输出硅谷大厂水准的高转化演示视频。"
    },
    "https://aircheck.dev": {
        "note": "针对自主运营 Agent 的多渠道内容质检门禁系统：在帖子投放到 X、LinkedIn 与社交群组前，自动拦截重复词、违禁词及格式断行畸变。",
        "so_what": "规避 AI 自主发帖引发品牌灾难的最后一道护城河；在规模化内容矩阵营销中兼顾分发效率与专业审美品控。"
    },
    "https://github.com/tryaida/aida": {
        "note": "通过监测用户在界面上的真实操作步骤，自动生成带有交互高亮截图、步骤拆解与排错建议的在线帮助文档生成工具。",
        "so_what": "砍掉繁重的手工文档撰写负担；显著降低新用户入门踩坑率与客诉成本，用顺滑的上手体验换取扎实的用户留存。"
    },
    "https://shutdownwatch.com/": {
        "note": "追踪各类数字服务、API 与云产品下线停运公告的公共信息平台：提前向订阅者发出数据导出倒计时与平替迁移指南。",
        "so_what": "反向做‘停服预警’获得高净值技术受众的聪明定位；既是开发者选型的避雷指南，也是竞品吸纳流失用户的最佳流量抓手。"
    },
    # AI 漫剧
    "https://www.woshipm.com/ai/6490565.html": {
        "note": "深度解剖今年现象级历史题材微短剧的工业化内核：拒绝高昂信息流投流买量，全靠硬核考据道具、高密度戏剧冲突与克制制作打透下沉与一二线市场。",
        "so_what": "给陷入投流内卷的短剧行业指明生路；证明视听赛道的内容品质与扎实叙事本身才是最强复利，好内容能靠口碑击穿算法牢笼。"
    },
    "https://www.woshipm.com/ai/6490593.html": {
        "note": "将大语言模型实时流式推理与视频分镜渲染融合的前沿交互实验：观众不再是被动旁观者，可随时开口打断并与剧中角色实时对话改变剧情走向。",
        "so_what": "视听内容从线性播放迈向生成式游戏化交互的历史拐点；为漫剧创作者打开了角色沉浸感与用户付费点设计的全新想象空间。"
    },
    "https://www.woshipm.com/it/6490886.html": {
        "note": "揭开国内短剧团队在东南亚掘金的真实渠道地貌：面对海外银行卡渗透率低、线上支付繁琐的痛点，通过运营商短代扣费与线下地推重构支付飞轮。",
        "so_what": "出海内容创业必须尊重本地基建现实；技术与画质优势只有配合极度本土化的结算通道与接地气的人性洞察，才能转化为真金白银。"
    },
    "https://www.woshipm.com/ai/6490727.html": {
        "note": "个人创作者结合本地知识库与编码智能体的闭环生产力实践：将故事大纲拆解、角色设定卡管理与提示词自动化组装打造成高复用流水线。",
        "so_what": "单兵内容极客的工业化作战指南；消灭每次从零手搓提示词的巨大心智消耗，把个人创作者的产能拉升至小型工作室水准。"
    },
    # 编剧技巧
    "https://www.wzbj1616.com/script_info/2245": {
        "note": "探讨程序正义与实体正义两难困境的硬核律政短剧：年轻辩护律师在为涉嫌杀人的昔日恩师辩护过程中，发现案件背后牵扯出跨国药企二十年的草菅人命罪恶。",
        "so_what": "律政类型短剧在法律专业度与戏剧反转间的精巧平衡；利用法律条文盲区作为悬念钩子，将道德拷问推向极致，剧作结构极其扎实严谨。"
    },
    "https://www.wzbj1616.com/script_info/2246": {
        "note": "唤醒古典武侠热血与镖局信义的群像剧作：一家濒临破产的偏远镖局接到一桩凶险万分的神秘暗镖，几个性格迥异的底层小伙计在生死护送中淬炼出侠义脊梁。",
        "so_what": "群像成长戏在短篇幅中的节奏分配典范；每个人物都有鲜明的动机软肋与高光时刻，用平民视角重构荡气回肠的中国式侠道精神。"
    },
    "https://www.wzbj1616.com/script_info/2247": {
        "note": "极具哲思深度的悬疑心理博弈剧本：天才棋手在人生绝境中与神秘黑衣人展开一场以生命为赌注的七日残局对弈，每下一步都对应着揭开一段尘封的愧疚记忆。",
        "so_what": "将智力对抗转化为内心救赎的高维剧作解法；摆脱了粗浅的打脸爽感，以古典命运悲剧感与精密伏笔给观众带来直击灵魂的心灵震颤。"
    },
    "https://www.wzbj1616.com/script_info/2248": {
        "note": "儒道流东方玄幻在微短剧形态下的成功示范：寒门书生以笔墨为剑、以诗词引动天地浩然正气，打破世家大族对修行资源的垄断壁垒。",
        "so_what": "传统文化金句与现代爽感节奏的完美缝合；每三分钟一次诗词引动的视觉奇观与阶层反击，给下沉网文改编短剧树立了极具商业竞争力的标杆。"
    },
    # 产品经理
    "https://www.woshipm.com/evaluating/6490871.html": {
        "note": "深度剖析腾讯云企业级智能体管理平台架构演进：企业在拥有成百上千个 Agent 后，治理、调用链监控、权限熔断与 SLA 质检成为决定生死的首要诉求。",
        "so_what": "产品经理构建平台级产品能力的关键分水岭；告别仅仅给业务方提供玩具级低代码画布，转向建立支撑企业严肃业务运转的‘智能体操作系统’。"
    },
    "https://www.woshipm.com/ai/6490861.html": {
        "note": "字节跳动扣子（Coze）与 Trae 组织架构大调整背后的业务复盘：单点工具型产品用户增长迅猛却缺乏深层商业黏性，唯有深深嵌入主营电商与信息流才能立足。",
        "so_what": "警醒所有 AI 创业者与大厂 PM：孤立的技术闪光点无法构成商业闭环，必须紧紧咬合进核心业务的交易与收益流程中，才能免遭大浪淘沙。"
    },
    "https://www.woshipm.com/ai/6447479.html": {
        "note": "彻底推翻‘智能体等于 ChatBot’的肤浅偏见：真正能产生生产力价值的 Agent 是由数据感知、定时巡检、确定性流程约束与人工干预兜底构成的有机系统。",
        "so_what": "产品经理岗位能力的底层重构指南；从‘写对话提示词’转变为‘系统动力学设计’，掌控复杂系统在长周期运行中的稳健演进。"
    },
    "https://www.woshipm.com/pmd/6471893.html": {
        "note": "硅谷 Palantir 核心工程师角色在 AI 时代的大规模普及：产品经理走出象牙塔、驻扎在大型政企客户现场，用代码和架构能力把不确定的大模型按进客户真实泥泞系统。",
        "so_what": "破解 AI 落地‘最后一公里’的最佳职业路径；拒绝做空中画饼的 PPT 经理，成为既懂算法边界又能在一线解决脏活累活的稀缺复合型人才。"
    }
}

# Rebuild md_content with precise notes and so_whats
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
    "items:"
]

pinned_map = {}
for item in candidates:
    cat = item["category"]
    count = pinned_map.get(cat, 0)
    pinned = count < 2
    pinned_map[cat] = count + 1
    
    u = item["url"]
    d = details.get(u, {})
    note = d.get("note", item.get("note", ""))
    so_what = d.get("so_what", item.get("so_what", ""))
    
    lines.append(f"- category: {cat}")
    lines.append(f"  title: {item['title']}")
    lines.append(f"  note: {note}")
    lines.append(f"  so_what: {so_what}")
    lines.append(f"  source: {item['source']}")
    lines.append(f"  url: {item['url']}")
    lines.append(f"  media: {item['media']}")
    lines.append(f"  pinned: {'true' if pinned else 'false'}")

lines.append("---")
lines.append("")
lines.append("### 岛主今日寄语")
lines.append("")
lines.append(closing_note)
lines.append("")

out_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-09.md"
with open(out_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Successfully wrote {out_path} ({os.path.getsize(out_path)} bytes)")

# Update scripts/all-used-urls.json
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
