# -*- coding: utf-8 -*-
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verify_nov_12_candidates import candidates

date_str = "2026-11-12"
title = "11 月 12 日 · B2A 经济敲门与产能暗战：多模态校准决策、代理防篡改隔离及短剧算力虹吸"
highlights = "全网 9 大领域 36 篇高密度精选：Google 发布 Gemini Decisions API 单次千级多模态决策、Gemini 4 Carbon 与 Qwen 4 Max 实测落差、Claude Bulkhead 与 Attentry 筑牢并发 Agent 防线、a16z 预言 B2A 经济新客户、可灵估值飙上 180 亿美元背后的 AI 视频模型横评与短剧 55% 算力虹吸。"
epigraph = "当你的产品下一位真正下单的客户不再是坐在屏幕前的人类，而是毫秒级比价、调用 API、且随时可能并发把你本地开发服务器 kill 掉的自主 Agent，你的架构边界、商业定价和工作流隔离就已经不能沿用旧世界的假设。"
lead = "11 月 12 日，AI 应用的坐标轴正在从“陪人聊天”加速滑向“替人决策与自治执行”。在底座层，Google 推出 Gemini Decisions API，把千级多模态判断压缩进单次校准调用，而 Gemini 4 Carbon 全面开放与 Qwen 4 Max Preview 的密集实测也撕开了参数榜单之外的体感温差——工程与 3D 跃升很快，前端审美与稳定交互仍在漫长爬坡。在研发一线，多 Agent 并行跑通后暴露出更锋利的秩序隐患：Claude Bulkhead 专治并发代理互相 pkill 端口与抢占 Git 暂存区的“手脚打架”，Attentry 本地拦截每次文件篡改，Jane Street 则开源苏格拉底式技能树防止程序员把大脑彻底外包。商业与视听战场同样火药味十足：a16z 合伙人提醒创业者盯紧紧随 B2B/B2C 之后的“B2A（面向智能体）”经济；可灵估值冲上 180 亿美元的同时，研究显示 AI 短剧与视频生成已吞下国内 55% 的 Token 消耗，95% 新短剧被 AI 改写生产流，唯有像《咪的妙脆角》那样守住角色跨集一致性的团队才能赚到长红溢价。"
scene = "「并发开三个编程 Agent 的时候，它们真像三个各干各的实习生。」「比实习生更刺激——一个刚把测试跑起来，另一个顺手 pkill 了隔壁的端口，顺带把半截代码 git add 进了同一个提交。以后管 Agent 的第一步不是写更好的 Prompt，是给每个代理划一道焊死的隔离舱壁。」"
cover = "https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini__decisions__blog-header_2784x1566.width-1300.png"
closing_note = "把今天跨度看似极大的 36 条信息放在同一张桌面上，会浮现出同一条清晰的主线：AI 正在告别“惊艳一瞥的演示玩具”，被无情推入高并发、强隔离、重一致性与算力成本核算的真实工业现场。不管是防编程代理互相撞车的隔离舱、跨集不能换脸的猫咪 IP、把硬件创始人扔进零下二十度的硬核出圈评测，还是面试官眼里筛选 AI 产品经理的四项底层硬功夫，本质上都在回答同一件事——在自动化把平庸产能的价格压到趋近于零之后，真正稀缺且值钱的，永远是“边界的清晰感”、“审美的校准权”与“稳定交付的确定性”。"

details = {
    # AI 资讯
    "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/": {
        "note": "Google 推出的多模态校准决策接口：支持开发者在单次请求中批量评估高达 1,000 个跨图文决策问题，输出带有置信校准的轻量结构化判断。",
        "so_what": "把大模型从“昂贵的话痨生成器”拆分成“高速低延迟的批量裁判员”；适合风控审核、推荐过滤与自动化路由等高频判别场景直接替换脆弱规则引擎。"
    },
    "https://www.woshipm.com/ai/6492919.html": {
        "note": "针对 Google 全面放开的旗舰多模态模型 Gemini 4 Carbon 展开一线开发实测：对比此前的 Claude Fable 5.2 前端跑通成本与真实代码产出体感落差。",
        "so_what": "提醒一线选型者警惕“跑分神坛与真实工程手感的剪刀差”；复杂交互页面依然极其考验指令遵循稳定性与细微品味，不要盲目用单一榜单替业务做决定。"
    },
    "https://www.woshipm.com/ai/6492783.html": {
        "note": "揭秘此前匿名模型 Qoduck 即为 Qwen 4 Max Preview：实测发现其在复杂代码重构与 3D 场景搭建上跃升显著，但在前端视觉排版审美上与 Fable 5.2 仍有代差。",
        "so_what": "国产旗舰大模型正快速补齐长链条工程与三维空间推理短板；现阶段“算法/后端交给 Qwen 4 Max，审美与 UI 精修叠加高品位模型混编”更具性价比。"
    },
    "https://www.woshipm.com/ai/6492755.html": {
        "note": "微信视觉团队开源的轻量多面手 WeVisOne-VL：把以往分散的找人定格、商品计数、包装 OCR 识字与精细主体抠图打包进统一视觉模型里一站执行。",
        "so_what": "工业图像处理很少需要天马行空的创作，90% 耗时耗在细碎标注与机械抠图上；垂直统一视觉模型直接消除了电商与运营流水线的工具链拼装成本。"
    },
    # AI 协作
    "https://github.com/dooly6276/claude-bulkhead": {
        "note": "针对开发者同时开启多个 Claude Code 终端时的灾难现场打造的沙盒防撞工具：阻止代理误杀其他窗口正在跑的开发服务、抢占监听端口或混提交他人改一半的 Git 分支。",
        "so_what": "当人手调度三到五个并发编程代理变成日常，“进程级、端口级与工作区级的舱壁隔离”将成为下一代 AI IDE 与 CLI 的标配底层能力。"
    },
    "https://github.com/Aarv-1o/Attentry": {
        "note": "专盯代码代理“私下动手脚”的本地文件变更审计盾牌：实时捕获代理发起的每一次读写修改轨迹，把隐蔽的跨目录误改高亮拦截在人为确认前。",
        "so_what": "给予自主 Agent 写权限的最大心理障碍不是速度慢，而是“不知道它顺手改坏了哪个角落”；细粒度本地审计正在成为工程团队放行自治代理的通行证。"
    },
    "https://smarchone.github.io/docs/": {
        "note": "面向文档协作流设计的自动化修订服务端：允许协作者直接在正文中写下批注意见，由文档服务器调度上下文自动重构对应段落并生成规范改动。",
        "so_what": "重构人与 AI 改稿的交互重心：不再来回复制整篇文本丢进聊天框，而是让行内批注像代码 Review 的 PR Comment 一样自动合入正本。"
    },
    "https://github.com/janestreet/agent_skills": {
        "note": "华尔街顶级量化机构 Jane Street 开源的一组 Agent Skills 实战技能包，其中 Socratic Tutor 模块刻意限制 AI 直接吐答案，改为通过苏格拉底式反问引导人类自己推导。",
        "so_what": "金融顶级工程团队对“过度依赖 AI 导致工程师退化”给出的解药：把教育心理学写进 Skill 约束，让智能体既当副驾驶也当严厉教练。"
    },
    # 一人公司
    "https://www.woshipm.com/ai/6492839.html": {
        "note": "梳理 a16z 合伙人 Olivia Moore 提出的 B2A（Business-to-Agent）经济范式：随着软件代理开始自主挑选工具与采购数据，产品的核心买单方正悄然从人类转向 Agent。",
        "so_what": "给独立开发者指明下一波红利风口：与其花重金买人类注意力广告，不如先把文档写得对 LLM 极度友好、暴露清晰鉴权与按次计费的 MCP/API 接口。"
    },
    "https://mflare.yuy1n.io/": {
        "note": "极简的 macOS 菜单栏状态常驻小工具：实时拉取 Cloudflare Workers 的用量配额、请求峰值与自动构建状态，异常接近限额立刻桌面弹窗预警。",
        "so_what": "高度精准的微痛点独立产品样板：紧紧寄生在高频重度使用的云服务边缘部署流旁，无需复杂后台就能稳稳吃下边缘计算开发者的工具预算。"
    },
    "https://floodroute.com": {
        "note": "支持沿时间轴拖拽回放的城市内涝与洪峰淹水街区地图：将零散气象降雨、积水深度与社区受灾记录直观投影到真实街道坐标之上。",
        "so_what": "公共开源数据+极致专注地图交互的低成本变现模板：对买房避坑、城市通勤避险与保险精算人群极具传播力与信息差溢价。"
    },
    "https://deedbell.com/today": {
        "note": "每天清晨只安静推送一条微小、立刻能落地的善意行动提示，例如给老友发一句问候或帮邻座扶一把门，没有社交广场也不卷打卡排名。",
        "so_what": "证明在算法焦虑溢出、通知栏噪音爆炸的时代，极度克制、单一意图且自带情绪疗愈属性的单页微应用反而容易依靠口耳相传长出忠实留存。"
    },
    # 产品设计
    "https://www.watched.earth": {
        "note": "输入地球上任意一个经纬度地点，即可回溯本周所有飞越你头顶的人造卫星轨迹，并调取对应轨道传回的实拍高空地球影像。",
        "so_what": "把原本冰冷抽象的航天轨道星历数据，翻译成充满浪漫与惊奇感的“此刻谁在看着我头顶”个人体验；信息可视化最打动人的永远是与“我”发生连接。"
    },
    "https://getnegs.com/try/": {
        "note": "直接在浏览器里运行的高精度物理胶片模拟实验室：按真实银盐感光层与光谱响应曲线计算曝光冲扫效果，告别千篇一律的生硬色彩滤镜。",
        "so_what": "硬核图形学与发烧友审美结合的典范；当基础调色被套壳软件卷滥时，回到物理底层做“真拟真”，才能让专业摄影用户心甘情愿停下来试用并付费。"
    },
    "https://rat-race.heyitsjam.es/": {
        "note": "开发者用 TypeScript 逐像素复活了 1994 年 Macintosh 系统上极具记忆点的 68k 经典迷宫老鼠屏保，还原当年的像素抖动与寻路趣味。",
        "so_what": "怀旧情感与工程致敬的绝佳小切口：轻量化浏览器交互同样承载文化质感，也是在单调现代 SaaS 界面里找回“软件曾让人会心一笑”灵气的标本。"
    },
    "https://faceanalysis.app/": {
        "note": "全程依托浏览器本地算力完成人脸三庭五眼、对称度与轮廓几何比例测算的工具站，所有照片图像完全留在用户自己内存里处理，零云端上传。",
        "so_what": "对于高度敏感的人脸与隐私测评类需求，“纯前端 Local-first 零上传”本身就是打消用户疑虑、直接拉高页面完成率的核心产品卖点。"
    },
    # 审美提升
    "https://www.dezeen.com/2026/11/12/steven-holl-cauny-watch-tribute-alvaro-siza/": {
        "note": "美国建筑大师 Steven Holl 携手腕表品牌 Cauny 打造“雕塑感腕表”，设计灵感直接源于与普利兹克奖得主 Álvaro Siza 的对谈，将建筑光影切面与明快原色戴在腕间。",
        "so_what": "顶格跨界工业设计的教科书：不被传统表盘指针对称性束缚，用建筑体块与留白比例重建微小日常物品的精神张力。"
    },
    "https://www.dezeen.com/2026/11/12/licht-kunst-licht-cologne-cathedral/": {
        "note": "照明设计团队 Licht Kunst Licht 为科隆大教堂更换 700 余盏表面隐蔽安装的新式 LED 灯具，让这座世界最高双塔哥特建筑在夜幕中呈现近乎“石雕自发光”的通透质感。",
        "so_what": "高端照明设计最忌喧宾夺主看到灯头本身；硬件隐身、只让空间结构和材质肌理自己说话，也是极佳产品视觉设计的底层法则。"
    },
    "https://www.dezeen.com/2026/11/09/freetown-memorial-sierra-leone-carrier-corps-tosin-oshinowo/": {
        "note": "建筑师 Tosin Oshinówò 在弗里敦用轻盈透亮的玻璃棱镜冠冕重塑历史搬运兵团纪念碑，借阳光折射跨越沉重伤痛记忆，赋予公共纪念建筑呼吸感。",
        "so_what": "打破“纪念建筑必沉重灰暗”的刻板美学惯性；材质透明感与自然光路径设计，能让庄重叙事获得截然不同的现代感染力。"
    },
    "https://www.dezeen.com/2026/11/09/studio-aslak-curifylabs-pharmaprinter-aurum-empower-pharmacists/": {
        "note": "芬兰设计工作室 Studio Aslak 为 CurifyLabs 重新设计 Aurum 3D 定制制药打印机，用温润优雅的家电级曲面外壳替代冷冰冰的实验室钢架。",
        "so_what": "B 端专业仪器与医疗硬件升级的巨大设计蓝海：降低操作者的心理压迫感与威慑力，本身就是极其有力量的生产力设计。"
    },
    # 产品营销
    "https://www.woshipm.com/operate/6359632.html": {
        "note": "复盘开源项目 OpenClaw 凭“人人皆可养虾”情绪爆火并拿下 80+ 热搜后的传播曲线，拆解为何多数靠焦虑与猎奇冲上热搜的产品很快销声匿迹。",
        "so_what": "情绪焦虑可以低成本换来第一波爆发式声量，但无法留住次日习惯；营销必须提前在峰值前铺好真实高频刚需承接动作，否则热搜即终点。"
    },
    "https://www.woshipm.com/operate/6484706.html": {
        "note": "复盘中国硬件科技团队一条 23 分钟全英文海外爆款评测：创始人亲自用英文口播，把设备放进零下 20 度折腾上千次后硬核拆解铰链微米折痕，震撼海外极客圈。",
        "so_what": "中国团队出海最锋利的武器往往不是精致包装，而是毫无水分的工程实测诚意与创始人第一人称硬核专业背书，透明实验自带跨文化信任穿透力。"
    },
    "https://www.woshipm.com/it/6492829.html": {
        "note": "结合花旗研报拆解今年双 11 电商变局：当传统电商成交增速趋稳，淘宝闪购、美团闪购与京东秒送三强把战火烧到了半小时即时履约主战场。",
        "so_what": "流量见顶之后，“交付时间颗粒度”成为新的营销钩子；谁能把消费者心里“网购等于等三天”的预期改写成“像点外卖一样买万物”，谁就能切走增量盘。"
    },
    "https://simonwillison.net/2026/Nov/9/details-summary/": {
        "note": "著名开发者 Simon Willison 分享了一项看似微小却影响深远的协作礼仪：别再把 Claude Code 生成的大段啰嗦解释直接贴进 PR，请用 HTML details/summary 标签折叠起来。",
        "so_what": "内容分发与工程沟通进入“AI 噪音超载期”后的关键修养：尊重人类评审者的有限注意力，主动做好信噪比分层，远比一股脑全量倾倒更容易赢得合作支持。"
    },
    # AI 漫剧
    "https://www.woshipm.com/evaluating/6492915.html": {
        "note": "结合快手可灵 AI 增资交割后估值突破 180 亿美元（超母公司港股市值）的资本热潮，面向实际创作者对当前主流视频生成大模型做全维度分镜落地横评。",
        "so_what": "AI 视频赛道已从资本讲故事正式步入重资产商用决胜期；创作者选型时不能只看宣传大片，必须拿运镜稳定度、口型同步和重抽抽卡废片率算真账。"
    },
    "https://www.woshipm.com/ai/6492578.html": {
        "note": "披露一组震撼行业的数据：国内全部大模型 Token 消耗中 AI 短剧与视频已占走 55%，最新上线短剧更是有 95% 深度融入了 AI 生产管线，旧拍摄生态寒冬已至。",
        "so_what": "印证 AI 漫剧绝非小众边缘玩具而是当前算力最大买主之一；传统剧组如果不向“AI 编导+人类审美把关”的轻量精兵模式转型，利润率将被急速挤压清零。"
    },
    "https://www.woshipm.com/ai/6492777.html": {
        "note": "深度剖析抖音爆款账号“咪的妙脆角”单条点赞破 163 万、转发 71 万的流量密码：让同一只顶着“妙脆角”的小猫跨越修水泵、吃火锅等剧情始终长成同一个角色。",
        "so_what": "在 AI 一键生成廉价杂耍短视频铺天盖地的当下，“跨剧集角色形象、性格与世界观一致性的长线资产沉淀”才是漫剧号逃离一次性的核心护城河。"
    },
    "https://www.woshipm.com/ai/6492854.html": {
        "note": "手把手拆解用 Codex 驱动 Blender 自动构建并导出可自由奔跑、开船、钓鱼、挖矿的三维沙盒小世界，且直接能够在本地浏览器中打开漫游交互。",
        "so_what": "提示 AI 漫剧创作者打破纯二维生图抽卡的局限：一旦用代码先行搭出可反复机位取景的固定 3D 舞台，角色走位与空间连贯性难题将迎刃而解。"
    },
    # 编剧技巧
    "https://www.wzbj1616.com/script_info/2266": {
        "note": "原创海外 AI 奇幻短剧剧本样本《领主大人：请指教》：讲述遭兄长背叛驱逐的狼族王女化名侍女潜伏吸血鬼古堡、裙下藏刀与高冷领主极限拉扯的强强复仇线。",
        "so_what": "极度适配海外 AI 漫剧视觉奇观的黄金配方：狼族与吸血鬼高辨识度人设自带视听冲击力，加上身份隐藏与双强博弈钩子，天然拉高前十秒完播转化。"
    },
    "https://www.wzbj1616.com/script_info/2267": {
        "note": "现代职场科技悬疑本《芯片泄密那天，全公司都说是我》：工程师遭门禁、指纹与监控“全套伪证”栽赃开除，全凭一张晚于拔盘四小时才生成的底层日志反杀。",
        "so_what": "演示高智商现代悬疑如何用“真实技术细节时间差”当核心戏剧引擎；摆脱无脑嘶吼扯头花，扎实严谨的硬核证据链反转更能抓住下沉与精英双层观众。"
    },
    "https://www.wzbj1616.com/script_info/2260": {
        "note": "120 集高能末世重生微短剧全本模型《重生回末世前，我囤空了全城》：开局遭背叛惨死，重生回到灾难爆发前三个月倾尽家财造堡垒、狂囤物资直到丧尸围城拔枪反击。",
        "so_what": "拆解男频/女频通用的“末世倒计时资源收集”上瘾心流：观众在明确时间压迫下看着主角一点点把安全屋塞满，每一步消费采购都在释放极度解压的掌控爽感。"
    },
    "https://www.wzbj1616.com/script_info/2259": {
        "note": "反差感拉满的 120 集玄学直播剧《我在殡仪馆夜班算命》：新手入行当殡仪馆夜班入殓化妆师，凭看见亡者心愿开启深夜直播代偿，却顺藤摸瓜撞破人体标本暗黑产业链。",
        "so_what": "绝佳的“高压猎奇职业场景+直播弹幕即时互动”复合结构：单集用小鬼心愿满足情感共鸣，长线用黑市阴谋牢牢锁住全季追更欲望。"
    },
    # 产品经理
    "https://www.woshipm.com/pmd/6282137.html": {
        "note": "一线招聘负责人面试上百位“AI PM”候选人后给出的残酷过滤清单：剔除只会套词库和画假大空流程图的简历党，直指决定最终拿 Offer 的四项硬核底层思考能力。",
        "so_what": "提醒转型中的产品经理迅速戒掉“Prompt 调参幻觉”；面试官真正高薪求贤的是评测集设计能力、幻觉兜底机制规划与真实的商业单元经济账算得清。"
    },
    "https://www.woshipm.com/pmd/6058206.html": {
        "note": "清晰切分当前市场上的三类核心 AI 产品经理画像（业务深耕型、模型评测优化型、工程平台基建型），并给出各自的能力补齐路径与职业晋升避坑地图。",
        "so_what": "帮助迷茫中的 PM 精准对号入座：千万不要企图用单一“全栈”口号通吃，找准自己过往经验嫁接基座能力的最短杠杆才是高胜率突围法则。"
    },
    "https://www.woshipm.com/operate/6484321.html": {
        "note": "深入探讨传统体验研究中常用的“满意度/NPS”在非确定性生成式 AI 产品上为何频频失灵，并回到“预期—感知落差”理论重建智能体验评测坐标系。",
        "so_what": "AI 产品常常让用户在“期待它全能结果答非所问”时产生强烈挫败；优秀 PM 要懂得在交互文案和加载态里主动管理心理预期，而非一味追求满分幻想。"
    },
    "https://www.woshipm.com/ai/6321654.html": {
        "note": "面向非算法出身产品经理的技术边界通识课：把大语言模型与多模态模型底层的注意力窗口、概率分布本质与工程落地硬限制翻译成能直接指导画原型的产品语言。",
        "so_what": "做 AI 产品最怕用传统决定论软件思维写 PRD；彻底摸透模型的“天性擅长与天然盲区”，才能少走九成反人性的死胡同需求。"
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
