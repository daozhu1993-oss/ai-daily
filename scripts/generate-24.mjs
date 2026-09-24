import fs from "fs";
import path from "path";
import yaml from "js-yaml";

const ALL_ITEMS_24 = [
  // 1. AI 资讯 (4)
  {
    category: "AI 资讯",
    title: "Anthropic：结合前沿模型发现新型类基因编辑酶系统",
    note: "研发团队借助 Claude 在海量宏基因组暗物质中精准识别出未被标记的 CRISPR 相关酶系，在生命科学未知序列注释上取得实验验证成果。",
    so_what: "大模型正在跳出代码和文本生成的存量博弈，进入物理与生物科学的一线发现链路；对于垂直场景从业者而言，将领域先验知识结构化为高质量特征才是壁垒所在。",
    source: "anthropic.com",
    url: "https://www.anthropic.com/news/claude-discovers-novel-enzyme-system",
    media: "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 资讯",
    title: "DeepMind：推出新一代多音色语音模型 Gemini 3.8 TTS",
    note: "全面升级端到端语音合成架构，支持在单次推理中平滑切换多角色语调、呼吸停顿与情绪强度，大幅降低长篇有声书与多轮对话的机器生硬感。",
    so_what: "语音交互正在告别拼凑词句的罐头音质；当拟真度和呼吸感达到真人级别，下一代语音 Agent 在客服、教育与互动叙事中的渗透速度将成倍提升。",
    source: "deepmind.google",
    url: "https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech",
    media: "https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 资讯",
    title: "Modal：揭秘支撑万亿级编程智能体的高吞吐推理架构",
    note: "深入复盘万亿 Token 与海量参数下高并发代码补全与 Agent 执行集群的底层调度，利用容器毫秒级冷启动与显存热池化把推理成本压缩至极低水位。",
    so_what: "工程落地的真正差距在基础设施的边缘毫秒控制；盲目堆砌算力无法解决延迟毛刺，精细化调度与内存复用才是交付生产级服务的基础功底。",
    source: "modal.com",
    url: "https://modal.com/blog/trillion-tokens-trillion-parameters",
    media: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "AI 资讯",
    title: "Simon Willison：开源双声线互动演练工具 TTS Playground",
    note: "开源极简 Web 端双角色语音对话调试看板，允许开发者直接在浏览器端实时调整 Gemini 语音模型的 Prompt 与语气参数，零成本直观验证音频表现。",
    so_what: "好的开发者工具能把调试反馈周期从几分钟压缩到几毫秒；在构建新型多模态产品前，先搭建一套直观的可视化手感操纵台能少走大量弯路。",
    source: "simonwillison.net",
    url: "https://simonwillison.net/2026/Sep/23/gemini-tts-playground/",
    media: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 2. AI 协作 (4)
  {
    category: "AI 协作",
    title: "pbakaus：开源提升智能体设计审美的语言 Impeccable",
    note: "通过结构化视觉约束规则与负面样式白名单，让编码智能体在生成前端界面时主动遵循层级对比、边距比例与现代色彩体系，杜绝粗糙的 AI 风模板套用。",
    so_what: "智能体写代码已经不再是瓶颈，瓶颈在于它缺乏对人类审美的直觉感知；用设计系统的确定性规范去约束 Agent，是交付高水准界面的标准做法。",
    source: "github.com",
    url: "https://github.com/pbakaus/impeccable",
    media: "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 协作",
    title: "Google：开源轻量智能体编排运行时框架 ax",
    note: "采用极简微内核架构设计，将模型路由、外部工具调用与长期记忆状态机完全解耦，为开发者提供高可测、可回溯且无厂商锁定的执行运行时。",
    so_what: "不要把业务逻辑死锁在臃肿的大一统框架中；轻量透明的状态机与标准调用接口，才能让团队随心所欲地替换底层模型而不必重构系统。",
    source: "github.com",
    url: "https://github.com/google/ax",
    media: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 协作",
    title: "DeusData：推出毫秒级代码知识图谱协议服务 codebase-memory-mcp",
    note: "实现 Model Context Protocol 标准协议，在本地增量解析项目抽象语法树与调用拓扑，让 Cursor 与 Claude 等工具秒级掌握百万行代码全局血缘。",
    so_what: "长上下文不能代替精确的图谱索引；让 Agent 在动手改代码前先看清函数引用链与依赖影响面，是彻底杜绝破坏性重构的核心武器。",
    source: "github.com",
    url: "https://github.com/DeusData/codebase-memory-mcp",
    media: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "AI 协作",
    title: "Strands：推出生产级智能体测试约束框架 Strands Harness",
    note: "专门针对长流程自主 Agent 打造的端到端自动化测试脚手架，支持模拟不可靠网络、伪造工具响应与回放真实日志，确保复杂工作流的回归稳定性。",
    so_what: "没有自动化评估防护网的 Agent 无法真正跑在生产环境；通过确定性的 Mock 与边界测试把随机性关进笼子里，软件工程的基本原则依然适用。",
    source: "strandsagents.com",
    url: "https://strandsagents.com/blog/introducing-strands-harness/",
    media: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 3. 一人公司 (4)
  {
    category: "一人公司",
    title: "DrivingBench：开源评测自动驾驶大模型的真实博弈决策",
    note: "独立研究团队构建覆盖上万种长尾博弈工况的轻量化评测体系，直接检验多模态大模型在遭遇突发路况时的因果推断与路径合规能力。",
    so_what: "单兵团队不需要造体量巨大的通用基础模型；只要在最关键的高价值垂直评测或数据基准上做深做透，同样能成为行业必须引用的权威标尺。",
    source: "drivingbench.com",
    url: "https://drivingbench.com/",
    media: "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "一人公司",
    title: "cyyself：用极简嵌入式硬件实现童年音乐梦想",
    note: "单人硬核实操手记：利用廉价微控制器与纯手工焊接电路，自主逆向古董音频合成芯片协议，把少年时代的纯粹爱好变为高度自洽的软硬件作品。",
    so_what: "做独立产品最强大的源动力不是追逐虚浮风口，而是解决内心最深切的情感渴望；当热爱与工程技艺融合，作品本身就会散发不可替代的温度。",
    source: "blog.cyyself.name",
    url: "https://blog.cyyself.name/my-musical-dream/",
    media: "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "一人公司",
    title: "Hoston：掌上手机随身运维微型控制面板",
    note: "专为一人团队打造的移动端轻量服务器监控面板，无需在手机上敲打冗长的 SSH 命令，点击即可查看服务负载、重启 Docker 容器与接收宕机警报。",
    so_what: "一人公司的关键是维持极轻的心理心智负担；把繁琐的后勤运维压缩进手机屏幕的简单按键里，才能将宝贵注意力完全留在业务迭代上。",
    source: "hoston.work",
    url: "https://hoston.work",
    media: "https://images.unsplash.com/photo-1526470608268-f674ce90ebd4?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "一人公司",
    title: "ShiftBar：自主掌控全局菜单栏状态的轻巧实用工具",
    note: "极简轻量级 macOS 状态栏管理利器，完全杜绝臃肿后台常驻与不必要的数据上报，让个人桌面在多屏幕与密集应用协作中保持干净清爽。",
    so_what: "用户对软件的信任正在回归本地自持与克制设计；不搞复杂花哨的概念包装，只把一个微小却高频的日常痛点解决彻底，就是微型产品的生存之道。",
    source: "shiftbar.0x01.build",
    url: "https://shiftbar.0x01.build",
    media: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 4. 产品设计 (4)
  {
    category: "产品设计",
    title: "PicSqueeze：纯浏览器端批量无损图片压缩利器",
    note: "基于 WebAssembly 与本地浏览器图形管线实现，零服务端上传开销，几毫秒内完成数百张高分辨率配图的极限无损减重并保留元数据。",
    so_what: "隐私安全与即时响应正在成为客户端体验的核心竞争力；将重算力直接卸载到用户浏览器本地，既节约服务器带宽成本，又让用户用得安心。",
    source: "tliens.github.io",
    url: "https://tliens.github.io/picsqueeze/?lang=zh",
    media: "https://images.unsplash.com/photo-1542744094-3a31f272c490?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品设计",
    title: "Here Wallpaper：把真实城市足迹编织成艺术壁纸",
    note: "巧妙抓取地理空间足迹数据，通过程序化几何连线与优雅色彩渐变，将单调的跑步路线和旅行轨迹转化为充满呼吸感与私人叙事的手机壁纸。",
    so_what: "好设计的本质是把冰冷枯燥的数据转译为用户内心的情感认同；善于发掘用户生活日常中沉睡的数字资产，往往能孕育出小而美的爆款体验。",
    source: "sspai.com",
    url: "https://sspai.com/post/114904",
    media: "https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品设计",
    title: "Lyrics2Song：聚焦文字韵律与分段节奏的 AI 编曲站",
    note: "摒弃传统复杂的乐理参数配置界面，直接将用户输入的诗词与歌词文本映射为带有情绪呼吸与起承转合的完整音频旋律，极大降低即兴创作门槛。",
    so_what: "降低创作门槛不是无脑交给黑盒一键生成，而是为用户保留核心表达主导权；把复杂的音频编排转化为直观的词句韵律调校，就是最懂人性的交互设计。",
    source: "lyricstosongai.org",
    url: "https://lyricstosongai.org/zh",
    media: "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品设计",
    title: "Naise AI：微型团队的内容营销与品牌传播托管智能体",
    note: "专为资源受限的单兵与小团队设计，通过学习企业产品文档与品牌基调，自动拆解生成匹配各渠道分发格式的内容脚本与排版物料。",
    so_what: "产品体验不再局限于 App 界面内部，而是延展到外部传播的每一个触点；用自动化流水线保持品牌对外发声的一致性，能为团队节省大量琐碎沟通成本。",
    source: "naise.ai",
    url: "https://naise.ai",
    media: "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 5. 审美提升 (4)
  {
    category: "审美提升",
    title: "MET：把小提琴家身躯化作共感觉光影乐谱",
    note: "大都会艺术博物馆突破传统静态展陈模式，通过高速运动捕捉与实时生成式光影投影，将演奏者的肌肉张力与音符振动转译为具象的流体视觉雕塑。",
    so_what: "当数字技术与现场艺术深度共振，观众感受到的不再是冰冷屏幕，而是全感官的情绪包裹；探索跨媒介的联觉设计，是拓展数字审美边界的必修课。",
    source: "designboom.com",
    url: "https://www.designboom.com/art/synesthesia-light-audrey-wright-musical-body-metropolitan-museum-geoff-robertson-stephanie-ann-boyd/",
    media: "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "审美提升",
    title: "Typewolf：Muse Paris 极致法式排版与留白视觉",
    note: "精选巴黎设计机构的极简数字作品，运用大面积从容留白、克制的衬线标题排版与精细的微阴影过渡，展现高端时尚品牌所独有的疏离高级感。",
    so_what: "高级感往往来自于对元素的敢于舍弃而非无度堆砌；学会用大间距与优雅字体建立清晰的视觉层级，页面不需要花哨装饰也能充满力量。",
    source: "typewolf.com",
    url: "https://www.typewolf.com/site-of-the-day/muse-paris",
    media: "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "审美提升",
    title: "Typewolf：Board 模块化几何构图与动态网格设计",
    note: "将严格的瑞士国际主义网格系统与现代 Web 交互相融合，通过高对比度的粗衬线字体与精准计算的几何间隙，打造出严谨又富有韵律的版面节奏。",
    so_what: "数学之美是界面的底层骨骼；掌握严格的比例尺与模块化网格，即使处理海量杂乱信息也能保持界面的整齐秩序与视觉从容。",
    source: "typewolf.com",
    url: "https://www.typewolf.com/site-of-the-day/board",
    media: "https://images.unsplash.com/photo-1513542789411-b6a5d4f31634?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "审美提升",
    title: "Typewolf：Elena Scott 极简人文肖像与多列版面编排",
    note: "通过温暖柔和的人文自然采光摄影，结合非对称多列排版与低饱和灰度底色，营造出沉静内敛且富有人情味的现代个人作品集范例。",
    so_what: "视觉风格是创作者内心情绪的外化表达；善于运用真实的自然光线质感与呼吸感留白，能让冰冷的数字载体具备穿透人心的真实温度。",
    source: "typewolf.com",
    url: "https://www.typewolf.com/site-of-the-day/elena-scott",
    media: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 6. 产品营销 (4)
  {
    category: "产品营销",
    title: "Koto：重构 Rakbank 现代金融品牌视觉体系",
    note: "顶级设计机构主导的老牌银行全面重塑：彻底抛弃过去沉闷刻板的传统金融符号，用大胆明快的色彩组合与鲜活现代的动态图形，重塑年轻客群认同。",
    so_what: "品牌视觉升级绝不仅是换个图标，而是重构与用户之间的心理契约；在用户注意力碎片化的今天，敢于打破行业旧有刻板印象才能抢占心智高地。",
    source: "underconsideration.com",
    url: "https://underconsideration.com/brandnew/archives/new_logo_and_identity_for_rakbank_by_koto.php",
    media: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品营销",
    title: "Unlisted：2026 年 9 月幽灵招聘报告，近三成企业长期悬挂虚假在招岗位",
    note: "基于对全球数千家科技企业公开职位的长期追踪，揭露近 30% 的在线招聘实为向资本市场展示扩张假象或收集简历的虚假挂牌，引发求职市场信任危机。",
    so_what: "看懂行业真实供需关系是职场与创业的第一步；在充满噪音与虚假繁荣的市场环境中，务必穿透表面公关数据，聚焦真实的业务交付与现金流。",
    source: "unlisted.careers",
    url: "https://unlisted.careers/ghost-jobs/report/2026-09",
    media: "https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品营销",
    title: "人人都是产品经理：Clay 内部复盘，零广告预算实现高速增长的 5 个内容动作",
    note: "高估值数据工具增长团队全盘公开实战打法：不花一分钱买量广告，通过可复用的公开模板生态、精细化实操指南与创始团队高质量专业分享驱动自传播。",
    so_what: "昂贵的信息流买量会掩盖产品的真实留存缺陷；做出真正解决问题的内容工具并把模板开放给社区，依靠高价值知识沉淀带来的自然增长最为长久。",
    source: "woshipm.com",
    url: "https://www.woshipm.com/operate/6469215.html",
    media: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品营销",
    title: "人人都是产品经理：种草被清算，品牌投向社交平台的营销预算如何测算真实 ROI？",
    note: "深度拆解当前消费品营销的虚火困局：揭露无节制投流种草背后的数据自嗨与高退货率现实，提倡建立端到端穿透到真实首购与复购周期的量化考核模型。",
    so_what: "潮水退去后，所有无法带来真实正向现金流的营销泡沫都将被无情刺破；衡量传播有效性的唯一标准，是它是否真正帮业务筑牢了转化与留存闭环。",
    source: "woshipm.com",
    url: "https://www.woshipm.com/operate/6463686.html",
    media: "https://images.unsplash.com/photo-1556742049-0a67c5574f73?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 7. AI 漫剧 (4)
  {
    category: "AI 漫剧",
    title: "红果短剧：免费模式掀翻买量行业桌子，重塑短剧商业与分成生态",
    note: "字节系红果短剧凭借“全剧免费+广告与电商变现”强势崛起，月活逼近一亿大关，彻底打破传统依赖充值付费与高达 80% 买量投流成本的旧有恶性内卷。",
    so_what: "短剧的竞争格局正在发生本质剧变；当分发管道被大厂免费模式重写，短剧创作者唯有靠更极致的故事黏性与工业化生产效率，才能在广告分成生态中稳固立足。",
    source: "woshipm.com",
    url: "https://www.woshipm.com/it/6469273.html",
    media: "https://images.unsplash.com/photo-1579208575657-c595a05383b7?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 漫剧",
    title: "万众编剧网：微短剧新规落地大盘观察，单日 3309 部 22 万集短剧获批备案",
    note: "微短剧备案新规正式实施首日，全国多省市主管部门与平台协同发力，3309 部微短剧在分类分层审核体系下平稳过审获批，行业合规正规化大幕全面拉开。",
    so_what: "合规准入不是阻碍发展的门槛，而是良币驱逐劣币的保护墙；熟悉政策导向、建立规范的剧本立项与审查流程，是团队从野蛮生长迈向长期经营的基石。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/708",
    media: "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 漫剧",
    title: "万众编剧网：各地微短剧产业扶持政策盘点与基地算力补贴",
    note: "系统梳理杭州、西安、成都、郑州等地最新推出的微短剧专项扶持举措，涵盖剧本创作资金资助、AI 影视制作渲染算力补贴及拍摄场地租金减免等全链条扶持。",
    so_what: "影视创作要善于借助政策杠杆降低前期的制作重资产成本；积极拥抱各地的产业补贴与场地资源，能帮助独立工作室快速完成首期作品的生产闭环。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/715",
    media: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "AI 漫剧",
    title: "字幕工作室：浏览器端开箱即用的短视频与微剧字幕极速压制利器",
    note: "轻量级免安装纯前端短视频字幕处理工具，支持导入本地音视频自动对齐时间轴、样式微调与一键硬字幕压制，大幅缩短短剧分集切片与分发交付周期。",
    so_what: "短视频与微短剧制作的最后一步往往被琐碎的字幕与压制消耗大量时间；用轻量级浏览器工具打通最后一公里流水线，能将日常剪辑效率提升数倍。",
    source: "video-transcript.zishu.me",
    url: "https://video-transcript.zishu.me",
    media: "https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 8. 编剧技巧 (4)
  {
    category: "编剧技巧",
    title: "万众编剧网：电影《西虹市首富》剧情为何不构成“抄袭”？戏剧构思与表达的司法边界",
    note: "通过知名喜剧侵权案终审判决深度解析：“一个月花光十个亿”属于不受著作权法保护的思想与公有创意概念，只有具体的人物性格、人物关系与情节编排才构成受保护的独创性表达。",
    so_what: "区分“思想”与“表达”是编剧保护自己与规避风险的基本常识；创意虽然珍贵，但真正让剧本成立并受到法律保护的，永远是精密扎实的情节设计与台词塑造。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/720",
    media: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "编剧技巧",
    title: "万众编剧网：故事提纲与故事结构在认定剽窃中的法定作用",
    note: "详尽梳理司法审判中对大纲与结构相似性的判定标准：若故事提纲仅包含常见人物模板与套路化冲突走向，不享有著作权排他保护；唯有高度精细且不可替代的因果链条才构成保护依据。",
    so_what: "写大纲不要只停留在“前女友回国复仇”这类烂大街标签上；为剧本注入不可替代的细节伏笔、反转动因与情感转折，才是让作品具备独创价值的核心所在。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/722",
    media: "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "编剧技巧",
    title: "万众编剧网：经典类型片研究——西部片的情感张力与冲突法则",
    note: "拆解经典西部电影的永恒叙事内核：文明律法与荒野自由的撕裂冲突、独行英雄的道德困境与宿命救赎，如何迁移并赋能现代都市短剧与末日科幻创作。",
    so_what: "类型片是经过几百年市场检验的情绪母题；无论外在视觉包装如何随 AI 变幻，掌握类型片对人性恐惧与渴望的调动法则，作品才拥有长久打动人心的力量。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/723",
    media: "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "编剧技巧",
    title: "万众编剧网：编剧与剧本纠纷常见类型及司法判例裁判规则",
    note: "结合数十起真实诉讼判例，深度盘点署名权被剥夺、拖欠稿酬、委托创作版权归属不清等行业重灾区，为创作者提供可落地的合同防坑与证据留存规范指南。",
    so_what: "创作的第一道防线不是写出好故事，而是用严密的合同保护劳动成果；在动笔之前理清权属条款与验收节点，才能免遭不法资方的无情剥削。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/732",
    media: "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 9. 产品经理 (4)
  {
    category: "产品经理",
    title: "Pragmatic Engineer：专访 Maggie Appleton，设计工程与人机交互界面的未来演进",
    note: "资深交互研究员深入剖析：大模型让界面从“静态控件表单”向“动态延展画布与意图认知界面”迁移，产品人必须重新定义人与机器共同思考的交互契约。",
    so_what: "不要把 AI 时代的交互设计窄化为聊天输入框；构建能让用户直观观察模型状态、随时介入调整并保持控制感的意图界面，是新一代产品经理的最高门槛。",
    source: "newsletter.pragmaticengineer.com",
    url: "https://newsletter.pragmaticengineer.com/p/design-engineering-with-maggie-appleton",
    media: "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品经理",
    title: "人人都是产品经理：Dreamforce 观察，当 UI 不再是软件主体，SaaS 的核心资产是什么？",
    note: "当 Agent 能够自主跨越界面读取数据并执行指令，传统以“页面功能多少”计价的 SaaS 面临被架空的危机，真正的护城河沉淀为底层私有工作流与高可信状态库。",
    so_what: "如果你的产品只是一套薄薄的 CRUD 表单界面，它随时可能被通用智能体碾平；深扎客户复杂的业务协同关系链与不可替代的领域上下文，才能在 Agent 时代保持不可替代。",
    source: "woshipm.com",
    url: "https://www.woshipm.com/it/6469004.html",
    media: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品经理",
    title: "人人都是产品经理：深度剖析，为什么产品经理守住“产品边界”会如此艰难？",
    note: "从老板战略摇摆、大客户定制施压到团队自我感动，系统性拆解导致产品功能臃肿失焦的六大诱因，提出以核心价值单元为尺度的功能否决机制与裁剪准则。",
    so_what: "决定产品成败的往往不是你加了什么功能，而是你勇敢拒绝了什么需求；守不住产品边界的产品经理，终究会把团队拖入无休止定制却无法规模化的泥潭。",
    source: "woshipm.com",
    url: "https://www.woshipm.com/pmd/6461254.html",
    media: "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品经理",
    title: "人人都是产品经理：VibeCoding 浪潮席卷而来，产品经理最值钱的核心能力发生了怎样的位移？",
    note: "当 AI 辅助编程让写代码变得越来越廉价，产品经理的价值不再是写冗长的 PRD 文档与画高保真原型，而是转变为问题定义的精准度、系统解构能力与商业转化闭环。",
    so_what: "生产力的爆发在迅速拉平技术实现的壁垒；未来优秀的产品经理必须同时具备架构师的严密逻辑与商业嗅觉，把模糊的客户痛点翻译成确定性的业务解决方案。",
    source: "woshipm.com",
    url: "https://www.woshipm.com/pmd/6387711.html",
    media: "https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
];

const frontmatter = {
  date: "2026-09-24",
  title: "9 月 24 日 · 破壁免费与意图重塑：当短剧掀翻买量旧牌桌，界面从表单走向认知画布",
  highlights: "全网 9 大领域 36 篇高密度精选：红果短剧免费模式月活破亿掀翻买量行业牌桌、新规首日 3309 部微短剧备案获批、Anthropic 借助模型发现新型类基因编辑酶、DeepMind 发布多音色 Gemini 3.8 TTS、Maggie Appleton 拆解意图界面与设计工程新范式。",
  draft: false,
  epigraph: "当一种商业模式需要靠 80% 的买量费用来维持呼吸，它就已经是一具行尸走肉；撕开买量遮羞布的从来不是更会投流的操盘手，而是把免费与效率做到极致的破局者。",
  lead: "今天的内容生态与软件架构正在经历两场几乎同步的“底牌翻转”：在文娱与短剧一线，红果短剧凭借“全剧免费+广告变现”的模式强力突围，月活迅速逼近一亿，把过去全靠高额投流买量、充值分成被层层抽干的旧有草莽生态彻底掀翻；与此同时，微短剧分类分层备案新规落地首日即有 3309 部 22 万集短剧平稳获批，各地政策正密集出台算力与场地补贴，行业正式告别野蛮内卷，迈向规模化的内容工业化正规军时代。而在产品与技术底层，交互范式正从“死板的输入框与表单按钮”加速向“动态意图画布”演进——Pragmatic Engineer 对 Maggie Appleton 的长文专访清晰揭示，当 AI 的代码生产成本无限降低，软件的核心资产不再是前端页面画得多繁琐，而是底层工作流知识沉淀与确定性的系统约束；从 Anthropic 在未知生物序列中发现类基因编辑酶，到 DeepMind 与开源社区搭建毫秒级语音与代码记忆协议，所有聪明的创造者都在做同一件事：不当买量与概念的二道贩子，回到真实场景中把产品边界守死、把交付做硬。",
  scene: "「你们还在找投流团队算首日 ROI 和买量回本周期吗？」「早不指望了。红果免费模式一出来，纯靠买量的短剧基本在给平台打白工。我们现在要么拿各地微短剧基地的算力补贴直接跑精细化自制剧，要么老老实实做长尾剧情留存，靠广告长线分成。不把牌桌掀了，永远赚不到辛苦钱。」",
  cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80",
  items: ALL_ITEMS_24,
};

const closingNote = `
## 今日主理人寄语

当短剧行业靠 80% 买量投流构筑的虚假繁荣被“全免费+广告生态”一枪掀翻，当成千上万的微短剧在合规备案新规下告别粗制滥造；当软件研发从纠结表单控件的堆砌，转向深入探讨意图画布与状态图谱——**商业和技术的风向标正在用毫不留情的方式惩罚投机者，奖赏那些扎根真实场景的耐心建造者。**

在这个时代做产品、写代码、搞创作，最危险的幻觉就是把“暂时的流量通道”当成了“长久的业务壁垒”。

**通道是别人的，随时可以提价或者关闭；唯有你沉淀在系统里的私有工作流、独创的故事逻辑，以及对真实用户痛点的深刻洞察，才是谁也拿不走的真资产。**

守住你的产品边界，敢于拒绝无效的噪音；用确定性的工程手段去驾驭不确定的大模型，把每一个微小的高频痛点打磨到极致。

愿今天的 36 篇精选资讯，能为你扫清迷雾，照亮前路。
`;

function run() {
  const yamlContent = yaml.dump(frontmatter, { lineWidth: -1, noRefs: true });
  const fullContent = `---\n${yamlContent}---\n${closingNote}\n`;
  
  const targetPath = path.resolve("src/content/daily/2026-09-24.md");
  fs.writeFileSync(targetPath, fullContent, "utf8");
  console.log("Successfully written:", targetPath);

  // Update all-used-urls.json
  const usedUrlsPath = path.resolve("scripts/all-used-urls.json");
  const usedUrls = JSON.parse(fs.readFileSync(usedUrlsPath, "utf8"));
  const usedSet = new Set(usedUrls);

  let added = 0;
  for (const item of ALL_ITEMS_24) {
    if (!usedSet.has(item.url)) {
      usedUrls.push(item.url);
      usedSet.add(item.url);
      added++;
    }
  }

  fs.writeFileSync(usedUrlsPath, JSON.stringify(usedUrls, null, 2), "utf8");
  console.log(`Updated all-used-urls.json: added ${added} new URLs, total count: ${usedUrls.length}`);
}

run();
