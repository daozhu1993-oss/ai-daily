# -*- coding: utf-8 -*-
import json
import yaml
import os

items = [
    # AI 资讯
    {
        "category": "AI 资讯",
        "title": "Ripple 65B 开放权重与原生思维链：小算力集群的高性价比推理探索",
        "note": "开源大模型领域的高性价比突破：65B 参数量级下引入原生思维链与长程上下文自注意力机制，以中等参数规模逼近闭源巨型模型的数学推理与逻辑推演能力。",
        "so_what": "降低企业自建私有化高阶推理底座的门槛；在消费级双卡集群上即可跑满全部上下文，让严肃商业逻辑的自动化分析彻底摆脱对闭源 API 的重度依赖与成本黑洞。",
        "source": "ricursive.com",
        "url": "https://www.ricursive.com/ripple",
        "media": "https://iandaily.xyz/digest/2026-11-05-ripple-b591e5b67fee.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "Kimi K3.1 Pro 开放多模态模型权重：长上下文推理再升级",
        "note": "月之暗面将超长上下文多模态主力模型权重全面开源：支持数百万 Token 窗口下的图文混合理解、超长音视频时间轴精确定位与长程文档密集推理。",
        "so_what": "开源多模态生态的重磅利好；赋予开发者在本地解析整部影视剧分镜、数万页行业研报的底座能力，彻底打破闭源厂商对超长多模态推理的垄断。",
        "source": "huggingface.co",
        "url": "https://huggingface.co/moonshotai/Kimi-K3.1-Pro",
        "media": "https://iandaily.xyz/digest/2026-11-05-kimi-9f8b1677ba57.jpg",
        "pinned": True
    },
    {
        "category": "AI 资讯",
        "title": "Claude Code 优化后台任务状态流：降低长时间编程代理通信损耗",
        "note": "专为开发者长程自主会话打造的 CLI 架构升级：重构后台并发子任务的心跳与状态压缩机制，减少终端高频渲染刷新对上下文 Token 的无效侵蚀。",
        "so_what": "提升长流程智能体工程化编码的稳定性与续航力；让单次大型重构任务持续运行数小时而不发生上下文拥塞，让 Agent 真正像老练工程师一样沉浸开发。",
        "source": "github.com",
        "url": "https://github.com/anthropics/claude-code/releases/tag/v2.1.316",
        "media": "https://iandaily.xyz/digest/2026-11-05-claudecode-105ea9f203b2.jpg",
        "pinned": False
    },
    {
        "category": "AI 资讯",
        "title": "Phonon 浏览器端语音合成：逐词时间戳与零后端极低延迟播报",
        "note": "基于 WebAssembly 与 Web Audio API 的端侧轻量 TTS 引擎：无需向远端服务器发送音频请求，在浏览器本地毫秒级生成自然流畅语音，并精准输出每个单词的时间戳。",
        "so_what": "颠覆了交互式阅读与 AI 视听对云端配音的依赖；不仅实现了零服务器成本与零网络延迟，更让卡拉 OK 级字幕同步与端侧音画联动变得触手可及。",
        "source": "blixt.xyz",
        "url": "https://blixt.xyz/phonon/",
        "media": "https://iandaily.xyz/digest/2026-11-05-phonon-8c38648f3577.jpg",
        "pinned": False
    },

    # AI 协作
    {
        "category": "AI 协作",
        "title": "QAmcp 为 MCP 服务器提供集成测试与监控：智能体工具链稳健性保障",
        "note": "模型上下文协议（MCP）生态的工程化自愈探针：针对 MCP Tool、Resource、Prompt 协议接口，自动生成边界用例与网络容错测试，实时告警协议格式漂移。",
        "so_what": "补齐 Agent 生产部署中最薄弱的工具层可靠性短板；杜绝“模型逻辑正确但外部工具暴死”的黑天鹅灾难，让多工具协作系统具备企业级 SLA 保障。",
        "source": "qamcp.dev",
        "url": "https://qamcp.dev/?from=hackernews",
        "media": "https://iandaily.xyz/digest/2026-11-05-qamcp-c20805d53e5d.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "Atlas 给智能体一张独立的 macOS 虚拟桌面：后台运行不抢占鼠标键盘",
        "note": "解决 GUI 计算机使用智能体最大痛点的桌面虚拟化系统：为 AI Agent 分配完全独立的后台无头虚拟显示器与虚拟输入流，支持完整的图形应用交互。",
        "so_what": "人机协同体验的质的飞跃；人类开发者在主屏继续流畅敲代码写文档，AI Agent 在后台虚拟屏自动点击网页、整理表格、跑自动化用例，互不干扰、并行不悖。",
        "source": "atlas.insanearts.io",
        "url": "https://atlas.insanearts.io/",
        "media": "https://iandaily.xyz/digest/2026-11-05-atlas-1708007e9dfc.jpg",
        "pinned": True
    },
    {
        "category": "AI 协作",
        "title": "Fount 本地优先的 AI 驱动文档工作台：私密数据零泄漏的表格与笔记融合",
        "note": "将 Markdown 笔记、SQL/DuckDB 表格与本地大模型深度绑定的新型个人工作台：数据全量存储为纯文本与 SQLite 本地文件，支持复杂语义计算与数据透视。",
        "so_what": "守住数据主权的单兵生产力中枢；告别将公司敏感财报与个人生活资产托付给云端 SaaS 的被动局面，在本地享受顶级的智能文档与跨表查询体验。",
        "source": "fount.sh",
        "url": "https://www.fount.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-05-fount-e3fbd11f2925.jpg",
        "pinned": False
    },
    {
        "category": "AI 协作",
        "title": "Screenplay 智能体自动编排录制产品演示：从脚本文案到视频交付",
        "note": "专为 SaaS 团队与独立开发者打造的自动化宣发工具：智能体根据新功能发布文档自发编写分步演示脚本，操控无头浏览器进行平滑鼠标移动与高帧率录屏。",
        "so_what": "彻底消灭产品发版时手工录屏与剪辑的重复繁琐工作；代码合并上线的同时自动产出像素级精准、带光标平滑缓动的高清功能演示视频，让产品宣发效率倍增。",
        "source": "github.com",
        "url": "https://github.com/gmpetrov/agent-screenplay",
        "media": "https://iandaily.xyz/digest/2026-11-05-screenplay-7d8595f2bb0f.jpg",
        "pinned": False
    },

    # 一人公司
    {
        "category": "一人公司",
        "title": "PC Deal Check 拆解整机真实配件价值：反向推导硬件折扣与防坑利器",
        "note": "一人公司挖掘消费决策刚需的经典案例：自动抓取电商整机配置单，拆解 CPU、显卡、主板、电源散件历史低价并加权计算整机真实溢价率，直击装机信息差。",
        "so_what": "垂直导购与联盟营销的利基样本；用极其清晰的价值量化工具占领极客与普通买家的比价心智，无需庞大客服团队即可通过联盟分佣实现被动现金流。",
        "source": "pcdealcheck.com",
        "url": "https://pcdealcheck.com/",
        "media": "https://iandaily.xyz/digest/2026-11-05-pcdeal-841a0fa664c4.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Meshword 填字游戏与网格逻辑解谜合成：极简网页独立小游戏变现实验",
        "note": "巧妙结合 Wordle 词汇猜谜与数独式空间网格逻辑的纯前端轻量游戏：极简优雅的黑白设计、每日全局统一关卡与社交分享矩阵驱动病毒式传播。",
        "so_what": "独立开发者撬动长尾流量的教科书级设计；用极低的算力成本与纯静态托管创造出极高粘性的每日仪式感，为订阅会员与周边谜题书销售打下坚实漏斗。",
        "source": "meshword.org",
        "url": "https://meshword.org/",
        "media": "https://iandaily.xyz/digest/2026-11-05-meshword-252ff13037c1.jpg",
        "pinned": True
    },
    {
        "category": "一人公司",
        "title": "Pinery 将 WordPress 导出为高性能静态站点：独立开发者的极简托管方案",
        "note": "独立站点架构降本增效的极佳利器：允许创作者保留熟悉的 WordPress 富文本后台与插件生态，一键全量爬取并生成零数据库、抗 DDOS 的纯静态 HTML 站点。",
        "so_what": "消除独立站高昂服务器租金与安全运维噩梦；免费托管至 GitHub Pages、Cloudflare Pages 或边缘 CDN，网站加载速度飞升至 50ms 级别，SEO 与体验双丰收。",
        "source": "pinery.pro",
        "url": "https://www.pinery.pro/en/",
        "media": "https://iandaily.xyz/digest/2026-11-05-pinery-23dc0d4b5754.jpg",
        "pinned": False
    },
    {
        "category": "一人公司",
        "title": "Spooler 超轻量级单文件消息队列：单兵云服务异步任务处理新基石",
        "note": "拒绝 Kafka 与 RabbitMQ 的过度设计：用不到 1000 行纯 Go 代码实现带持久化 WAL、超时重试与背压保护的消息队列服务，单二进制文件开箱即用。",
        "so_what": "为微型 SaaS 与单兵架构量身定制的解耦方案；内存占用不足 10MB，却能稳定吞吐数十万异步作业，将系统复杂度与运维心智压缩至绝对极简。",
        "source": "spooler.sh",
        "url": "https://spooler.sh/",
        "media": "https://iandaily.xyz/digest/2026-11-05-spooler-e612264e6dd8.jpg",
        "pinned": False
    },

    # 产品设计
    {
        "category": "产品设计",
        "title": "OnCue 物理级倒计时任务看板：将日程安排具象化为沉浸式时间视觉流",
        "note": "反思传统日历与 Todo 表格的信息无感症：将任务持续时间与截至时刻拟物化为滑动水银柱与机械翻页卡片，让时间的流逝具备强烈的视觉压迫与实体节奏感。",
        "so_what": "生产力工具向“感官唤醒”维度的深层探索；利用空间位置与动态刻度直击拖延心理，证明优质的界面交互能通过情绪张力反哺用户的专注力。",
        "source": "oncueboard.com",
        "url": "https://www.oncueboard.com/",
        "media": "https://iandaily.xyz/digest/2026-11-05-oncue-c7dd5cd57418.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Ratio 文档内嵌动态数学与数据计算：消除文本与电子表格边界的交互革新",
        "note": "消除打字记录与切换计算器割裂感的交互范式：在任意正文段落中键入算式、单位换算或动态变量，光标所在处即刻渲染高亮求值结果并联动下游文本。",
        "so_what": "现代知识工作者的高保真草稿本；将数字与叙事逻辑融为一体，让商业计划、工程预算与生活规划的书写如行云流水般自然，极大减少上下文切换摩擦。",
        "source": "useratio.app",
        "url": "https://useratio.app/",
        "media": "https://iandaily.xyz/digest/2026-11-05-ratio-f52eebadb52d.jpg",
        "pinned": True
    },
    {
        "category": "产品设计",
        "title": "Mdview 原生轻量 Windows Markdown 查看器：毫秒级响应的纯粹阅读窗口",
        "note": "针对 Electron 臃肿巨石的反叛之作：采用原生 C++/WinUI 打造的极速 Markdown 阅读器，双击 .md 文件瞬间启动，提供排版优雅的暗色排版与目录树。",
        "so_what": "重归“小而美”的原生桌面软件美学；在内存动辄被各类套壳应用吃满的今天，用不到 5MB 的内存占用守护系统纯净度，唤醒开发者对原生流畅的渴望。",
        "source": "mdview.io",
        "url": "https://mdview.io/desktop",
        "media": "https://iandaily.xyz/digest/2026-11-05-mdview-a7aeaee63adf.jpg",
        "pinned": False
    },
    {
        "category": "产品设计",
        "title": "Md2Docx 将 Markdown 精确排版导出为 Word 文档：开发者告别格式对齐折磨",
        "note": "直击技术人员向传统企业客户交付文档的痛点：深度解析 Markdown 语法树与 LaTeX 公式，无损映射为符合企业红头与商务规范的标准 .docx 样式。",
        "so_what": "弥补现代开发者纯文本工作流与传统组织办公格式的鸿沟；让工程师保持高效纯文本书写的同时，秒级产出让甲方领导完全满意的精致 Word 报表。",
        "source": "md2docx.js.org",
        "url": "https://md2docx.js.org/",
        "media": "https://iandaily.xyz/digest/2026-11-05-md2docx-da44a5edca86.jpg",
        "pinned": False
    },

    # 审美提升
    {
        "category": "审美提升",
        "title": "Jakob Kudsk Steensen 地下水库深海光影装置：生命起源与多感官空间叙事",
        "note": "哥本哈根废弃蓄水池中的先锋生态艺术展：艺术家将显微镜下的深海浮游生物、古老水体结晶与 3D 点云扫描投影于巨大的潮湿石柱上，伴随深邃的水下低频共鸣。",
        "so_what": "空间体验与科技美学的极致交织；展示了数字生成影像如何脱离扁平屏幕的束缚，与真实空间的湿度、回声及历史痕迹产生化学反应，构筑直击心灵的沉浸仪式。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/art/this-installation-by-jakob-kudsk-steensen-considers-the-origins-and-agency-of-life/",
        "media": "https://iandaily.xyz/digest/2026-11-05-jakob-9498e548cbf7.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Atelier Manferdini 像素陶瓷与折叠铝板艺术变电站：工业基础设施的公共美学重塑",
        "note": "弗吉尼亚州大型变电站的外观革命：建筑师采用数千片不同釉面的高反射陶瓷砖与定制折叠穿孔铝板，根据一天中阳光角度折射出如同流动画卷般的像素光谱。",
        "so_what": "破解“邻避效应”的建筑美学范例；证明高危冷酷的城市电力设施无需被高墙丑陋遮蔽，通过精妙的材料质感与几何构图，工业建筑同样能成为城市的雕塑地标。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/architecture/pixelated-ceramic-tiles-folded-aluminum-electrical-substation-facade-virginia-atelier-manferdini-invisible/",
        "media": "https://iandaily.xyz/digest/2026-11-05-manferdini-1808b6091e26.jpg",
        "pinned": True
    },
    {
        "category": "审美提升",
        "title": "Abel Macias 巴黎古宅内的高饱和簇绒色彩装置：手工纺织与古典建筑的历史对话",
        "note": "巴黎历史名邸内的视觉碰撞：设计师用高饱和度的红、蓝、黄纯羊毛手工簇绒毯包覆巴洛克雕花楼梯扶手与天花板梁柱，将墨西哥民间色彩植入法式古典秩序。",
        "so_what": "审美张力往往诞生于强烈的时空错位；温润粗粝的手工织物消解了古典石材的冷峻距离感，给数字化时代的设计师提供跨文化、跨材质色彩运用的新鲜养分。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/11/04/scad-installation-design-miami-paris/",
        "media": "https://iandaily.xyz/digest/2026-11-05-scad-d35cbfbc28c0.jpg",
        "pinned": False
    },
    {
        "category": "审美提升",
        "title": "Jeju 岛原木柱承托的极简诗意餐厅空间：三根传统木构与海风光影的通透融合",
        "note": "韩国济州岛海畔的微型建筑实验：整个屋顶重量仅由三根粗壮的未加工原生杉木柱支撑，落地超白玻璃幕墙将火山岩礁石与海浪视线完全吸纳进用餐区。",
        "so_what": "东方克制哲学的现代演绎；不加雕饰的木材肌理随时间留下风霜印记，向空间设计者展示了如何以“少即是多”的结构勇气，让建筑悄然隐入大自然的磅礴背景。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/11/04/jeju-restaurant-daughters/",
        "media": "https://iandaily.xyz/digest/2026-11-05-jeju-195a14e1d03d.jpg",
        "pinned": False
    },

    # 产品营销
    {
        "category": "产品营销",
        "title": "Cloudflare 针对 AI 个人代理的流量可视化与管控：新流量生态的站长防御盾",
        "note": "边缘网络巨头对 Agent 经济的重磅基础设施重塑：推出首个精准识别、统计并可细粒度授权 Personal Agent 访问行为的管理面板，区分恶意爬虫与带单购买代理。",
        "so_what": "AI 时代站长营销与防守的新分水岭；不再盲目全盘封杀，而是通过向高意向购物 Agent 开放结构化数据通路换取精准交易转化，开启“面向智能体营销”的全新赛道。",
        "source": "blog.cloudflare.com",
        "url": "https://blog.cloudflare.com/personal-agents-visibility-control/",
        "media": "https://iandaily.xyz/digest/2026-11-05-cloudflare-1efc6b169107.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "25posts 通过 LinkedIn 曝光猜谜反推内容获客逻辑：游戏化增长与算法探秘",
        "note": "极具创意的社媒营销获客互动网页：将 25 篇爆款与扑街帖子的文案、配图及真实曝光数据制成盲盒猜题小游戏，让玩家在比拼直觉中领悟受众情绪与钩子技巧。",
        "so_what": "“边玩边学”的游戏化裂变营销范本；比干瘪的说教课程更容易在运营者圈层疯传，自然而然地将答题失败的用户转化为旗下社媒排期工具的高付费意向线索。",
        "source": "25posts.com",
        "url": "https://25posts.com/play",
        "media": "https://iandaily.xyz/digest/2026-11-05-25posts-d5eedbeae84a.jpg",
        "pinned": True
    },
    {
        "category": "产品营销",
        "title": "Slashtrends 追踪 Reddit 细分社区受众热点：出海独立产品的社群冷启动罗盘",
        "note": "直击出海团队社群营销痛点的雷达工具：实时聚类各大 Subreddit 的高频痛点词与求助提问，计算情绪热度与跟帖时机，为独立创作者标记潜在获客切入点。",
        "so_what": "摆脱盲目发帖被封禁的被动营销困境；教你在真实用户表达痛苦的时刻带着产品解决方案优雅介入，以真诚的“问题解决者”姿态完成低成本高精准的种子用户积累。",
        "source": "slashtrends.com",
        "url": "https://slashtrends.com/",
        "media": "https://iandaily.xyz/digest/2026-11-05-slashtrends-57a7d59f76b2.jpg",
        "pinned": False
    },
    {
        "category": "产品营销",
        "title": "RotateAd 独立开发者横幅与导航栏赞助互换：零预算流量互助联盟网络",
        "note": "属于独立产品圈的流量去中心化实验：各个独立站只需在页脚或导航栏嵌入一行极轻脚本，即可按照 1:1 展示比例在全联盟站点的空余广告位上轮播自家产品。",
        "so_what": "对抗 Google/Meta 昂贵广告霸权的单兵互助范式；让无数零预算的小产品抱团取暖，利用彼此的长尾受众交叉渗透，以近乎零成本的互惠交换打破流量荒原。",
        "source": "rotate.ad",
        "url": "https://rotate.ad/",
        "media": "https://iandaily.xyz/digest/2026-11-05-rotatead-8e68914f260f.jpg",
        "pinned": False
    },

    # AI 漫剧
    {
        "category": "AI 漫剧",
        "title": "跨模型生态协同：漫剧多模态视听管线的分工重组与平台壁垒打破",
        "note": "大厂与独立制作方纷纷打破单一大模型依赖：漫剧管线正演进为“Claude 编排剧本文戏 + Midjourney 锁死美术人设 + Sora/Runway 跑动态特效 + 自研语音模型配音”的混血拼装流。",
        "so_what": "标志着 AI 漫剧制片从“工具尝鲜”迈向“工业化分工成熟”；谁能构建最顺畅的跨模型上下文数据总线，谁就能在单集制作成本压至几百元的同时把视听质感拉满。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488773.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "AI 眼镜与随身第一人称视角拍摄：沉浸漫剧新机位与具身叙事探索",
        "note": "随身穿戴设备为视听创作带来全新镜头语言：利用 AI 眼镜低机位、长续航的第一人称写实视角捕捉真实生活微表情与环境光影，无缝喂入多模态漫剧生成器中重绘。",
        "so_what": "拓宽了虚实融合视听的内容边界；解决了传统纯生成漫剧动作机械、眼神空洞的假人感，用真实人类第一视角的呼吸律动与微小颤动为 AI 漫剧注入鲜活灵魂。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488630.html",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "AI 漫剧",
        "title": "大厂 AI 团队重组：视听创意工作室工业化制片流程与生产力重构",
        "note": "互联网头部视听产研架构的大洗牌：传统按照“原画、建模、特效、剪辑”切分的流水线被压缩，懂剧本逻辑与模型微调的“全栈制片人”成为独立单元核心。",
        "so_what": "个人与小团队视听工作室的历史性机遇；组织架构的扁平化让微型团队具备了抗衡传统影视工业的产能，好点子不再被漫长的项目审批与动辄数月的后期制作拖垮。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488383.html",
        "media": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "AI 漫剧",
        "title": "实测 DeepSeek“创造模式”：零门槛插件驱动漫剧分镜与动态特效生成",
        "note": "深度实操评测最新免配置创造管线：通过自然语言直接调用复杂视觉插件链，模型自主理解戏剧高潮节点并输出标准化分镜参数、运镜景别指令与关键帧提示词。",
        "so_what": "漫剧创作的“平民化核爆”；抹平了非专业创作者对 Blender、ComfyUI 复杂节点图谱的认知恐惧，让编剧一人敲字即可完成全套镜头设计与光影布光。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488371.html",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 编剧技巧
    {
        "category": "编剧技巧",
        "title": "《妖兽食堂》120 集微短剧：玄幻美食、治愈经营与反差反转的轻喜剧叙事",
        "note": "融合玄幻修真与温暖治愈的类型片创新范式：顶级大能化身小客栈掌柜，用灵草烹饪降伏狂暴上古凶兽，在轻快幽默的日常经营中穿插高燃反转。",
        "so_what": "短剧同质化严重下的“情绪反差破局法”；用治愈暖心的美食体验对冲传统短剧过度暴戾的复仇套路，既满足了观众即时解压的心理需求，又保证了长线连贯追剧动力。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2229",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《女将北征》120 集微短剧：古装女将从军与热血逆袭因果链构建",
        "note": "严谨环扣的大女主历史军旅短剧模本：摒弃低幼甜宠的宫斗桥段，聚焦边塞战场兵法交锋与家国大义，通过细密的前后伏笔将个人的成长与沙场生死死死绑定。",
        "so_what": "编剧叙事逻辑硬核度的标杆；证明即使在碎片化快节奏的短剧框架下，只要因果链条严丝合缝、军政智斗智商在线，宏大叙事与家国情怀同样能爆发出震撼的吸睛能量。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2230",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "编剧技巧",
        "title": "《不死药》120 集微短剧：都市悬疑、长生执念与人性博弈的戏剧张力",
        "note": "探讨生命伦理与财富权欲的硬核悬疑剧本：围绕一份能延寿五十年的绝密药方，三代财阀与医学底层研究员展开层层剥茧式的智斗，每次揭秘都伴随着人性的残酷拷问。",
        "so_what": "悬疑短剧剧作的高级心法；拒绝机械的为反转而反转，将戏剧冲突根植于每个人物自洽但绝不退让的核心欲望中，让每一个反转都成为命运必然，给观众持久的回味。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2231",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "编剧技巧",
        "title": "《乌合之众》120 集微短剧：都市现实、网络舆论风暴与反转真相的批判叙事",
        "note": "紧扣当代网络传播生态的尖锐现实题材短剧：一起看似无可争议的公车让座冲突被掐头去尾传上热搜，当事人经历舆论审判后绝地反击，将造谣推手与平台算法层层剖开。",
        "so_what": "抓住大众共情痛点的敏锐编剧触角；以快节奏的现实题材共振引发全网自发大讨论，展现了剧本如何借用生活中的真实焦虑完成高情绪密度的商业化表达。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2232",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },

    # 产品经理
    {
        "category": "产品经理",
        "title": "开源 3 年沉淀与数百个实战项目：AI 产品经理全景知识库与实操模型",
        "note": "资深 AI 架构师毫无保留的行业沉淀精粹：梳理涵盖模型评估标准、Token 成本精算表、智能体容错状态机及 20 个高频业务落地避坑指南的体系化方法论。",
        "so_what": "AI 产品经理告别碎片化学习与迷茫的通关地图；把从数百个真实客户项目踩坑总结的工程边界化为可复用的决策清单，极大提升复杂项目的交付确定性。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488632.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "给 AI 造上班前的仿真环境：智能体沙箱测试与产品形态演进推演",
        "note": "获千万级美金投资的前沿赛道深度拆解：如同飞行员的飞行模拟器，该系统为企业级智能体搭建具备千百种异常边缘工况的高保真沙箱，测试 Agent 的应变成熟度。",
        "so_what": "Agent 迈向严肃企业级岗位不可或缺的准考证；让智能体在真正接管企业核心生产线前完成上万次受控实操演练，为产品经理衡量 AI 上岗能力提供了严谨的量化标尺。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/chuangye/6488756.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": True
    },
    {
        "category": "产品经理",
        "title": "企业私有化 Agent 架构方案与落地推演：从研发增效到企业流程重构",
        "note": "传统企业私有化部署的系统化落地推演：从研发协同的代码辅助起步，逐步打通 ERP、CRM 等内部孤岛系统，将原本割裂的审批流演进为 Agent 自主协调的网状协作流。",
        "so_what": "洞察企业数智化转型深水区的核心路径；产品经理不再做表面功能的简单搬运工，而是借助 Agent 体系重构跨部门协同机制，真正从根本上释放组织生产力。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488290.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    },
    {
        "category": "产品经理",
        "title": "Personal Agent 的交互重塑：从 Voice 语音切入的伴随式助理新范式",
        "note": "重新思考人机交互的物理边界：以 Orilo 为代表的新一代个人助理跳出打字框逻辑，依托全双工超低延迟语音与屏幕感知，成为随时倾听、默默记录且适时提示的无形伴侣。",
        "so_what": "个人助理产品的终极形态探索；语音不是简单的命令输入工具，而是人机建立深层信任与情感共鸣的自然触手，倒逼产品人重新设计“不打扰却又无处不在”的心智模型。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6488363.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": False
    }
]

def build():
    frontmatter = {
        "date": "2026-11-05",
        "title": "11 月 05 日 · 开放权重深化与管线解耦：从全家桶霸权走向混血生态协作",
        "highlights": "全网 9 大领域 36 篇高密度精选：Ripple 65B 与 Kimi K3.1 Pro 开放多模态长文本权重、大厂打破壁垒开启跨模型漫剧管线拼装、微短剧《妖兽食堂》《女将北征》因果链拆解、给 AI 上班前建高保真模拟练习环境、PC Deal Check 拆解整机真实溢价。",
        "draft": False,
        "epigraph": "当大厂不再执着于用单一模型垄断全链条、甘愿在生产管线中各司其职时，真正的工业化分工才宣告降临；当智能体离开喧嚣的跑分展台、在模拟沙箱里接受千万次极端工况淬炼时，可信赖的数字员工才真正开始走上工作岗位。",
        "lead": "11 月 5 日，生成式技术与数字化创作正在从“单点惊艳”全面迈向“深度解耦与生态混血”。在开源模型最前沿，Ripple 65B 与 Kimi K3.1 Pro 接连开放权重，将超长上下文与深层推理的门槛打入消费级硬件区间，打破了闭源寡头对高阶智能的垄断；在漫剧视听创作端，行业彻底告别了“单一工具通吃”的幼稚期，演进为 Claude 编剧、Midjourney 人设、Sora 运镜与端侧轻量语音模型的模块化流水线；在剧作与叙事领域，微短剧通过《妖兽食堂》的反差治愈与《女将北征》的严密智斗，向粗制滥造的狗血套路宣战；而在产品落地最深处，前沿团队开始为 AI 搭建“上班前的模拟练习沙箱”，用数万次压力测试检验 Agent 的上岗资格。从单打独斗走向分工协作，从表面炫技走向可验证交付，这就是今天我们见证的务实进化。",
        "scene": "「为什么不买一套号称能搞定一切的 AI 全家桶系统？」「因为在真正严肃的商业战场上，没有哪个单一大模型能在写诗、画画、剪辑和算账上同时拿到满分。把各家最锋利的尖刀拼装成一条不卡壳的生产线，才是我们每天准时交付的秘密。」",
        "cover": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80",
        "items": items
    }

    # Verify counts
    by_cat = {}
    for it in items:
        by_cat[it["category"]] = by_cat.get(it["category"], 0) + 1
    print("Categories:", by_cat)
    assert len(by_cat) == 9
    assert all(c == 4 for c in by_cat.values())
    assert len(items) == 36

    yaml_str = yaml.dump(frontmatter, allow_unicode=True, sort_keys=False, width=1000)

    closing_text = """### 岛主今日寄语

观察今天的 36 个创新切片，最强烈的感受是“敬畏真实”。无论是为 AI 制造高仿真的上岗测试沙箱，还是微短剧拒绝狗血、用扎实的因果链构建反差与悬疑，亦或是单兵开发者做轻量消息队列和静态导出工具，大家都在从概念狂热退回到冷冰冰的现实边界中。真正的生产力提升永远来自于将各个细分模块做到极致并可靠拼装，而不是寄希望于某个无所不能的神话。沉下心去打磨你的那颗核心零件，世界自会为你预留齿轮咬合的位置。"""

    full_md = f"---\n{yaml_str}---\n\n{closing_text}\n"

    target_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-05.md"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_md)
    print(f"Successfully generated {target_path}")

    # Update all-used-urls.json
    used_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/all-used-urls.json"
    with open(used_path, "r", encoding="utf-8") as f:
        used_list = json.load(f)
    used_set = set(used_list)

    new_urls = [it["url"] for it in items]
    added = 0
    for u in new_urls:
        if u not in used_set:
            used_list.append(u)
            used_set.add(u)
            added += 1

    with open(used_path, "w", encoding="utf-8") as f:
        json.dump(used_list, f, ensure_ascii=False, indent=2)

    print(f"Added {added} new URLs to all-used-urls.json, now total: {len(used_list)}")

if __name__ == '__main__':
    build()
