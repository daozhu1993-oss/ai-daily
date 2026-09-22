import fs from "fs";
import path from "path";
import yaml from "js-yaml";

const ALL_ITEMS_22 = [
  // 1. AI 资讯 (4)
  {
    category: "AI 资讯",
    title: "小米：正式开源 MiMo-V2.6 全模态基座大模型权重",
    note: "打破全模态前沿大模型被少数海外巨头闭源垄断的局面，以完全开放许可释放端到端多模态权重，大幅降低端侧设备与自建算力集群的视觉-文本融合部署门槛。",
    so_what: "端侧全模态开源正在重塑硬件生态；当主流厂商在移动设备上把视觉交互做到底层芯片级对齐，第三方开发者才能真正做出脱离云端延迟的实时感知产品。",
    source: "mimo.xiaomi.com",
    url: "https://mimo.xiaomi.com/mimo-v2-6",
    media: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 资讯",
    title: "Tomer Tunguz：专用决策器将业务 if 语句成本降低百倍",
    note: "深度解构软件工程底层质变：传统代码中冗长脆弱的硬编码条件判断，正被毫秒级、极低推理成本的专用决策模型取代，重构系统架构弹性。",
    so_what: "未来的业务架构不是写满穷举规则的规则引擎，而是由极小模型组成的意图路由器；将分支决策交给微模型，能让复杂系统的维护成本断崖式下跌。",
    source: "tomtunguz.com",
    url: "https://tomtunguz.com/ai-comes-for-the-if-statement",
    media: "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 资讯",
    title: "通义千问：Qwen-Image 实现文生图与局部编辑端到端统一",
    note: "告别传统工作流中生图模型与修图重绘模型割裂拼接的痛点，通过统一架构在单次前向传播中兼顾高精生成与像素级精准局部修改。",
    so_what: "单一模型整合全链路正在成为视觉大模型的新常态；减少中间环节的格式转换与特征损失，意味着工业级分镜与海报出图的稳定性产生质的飞跃。",
    source: "qwen.ai",
    url: "https://qwen.ai/blog?id=qwen-image-2.1",
    media: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "AI 资讯",
    title: "Artificial Analysis：Grok 4.7 独立基准实测与长文档推理跃升",
    note: "脱离厂商宣传自说自话，通过多维度独立权威评测揭示 Grok 4.7 在长文档上下文对齐、办公逻辑推演与多轮对话一致性上跻身全球知识第一梯队。",
    so_what: "技术选型必须建立在第三方真实测算基准之上；随着推理成本持续压缩，企业级 Agent 在面对超长代码仓与复杂合规文档时有了更具性价比的选择。",
    source: "artificialanalysis.ai",
    url: "https://artificialanalysis.ai/articles/benchmarking-grok-4-7",
    media: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 2. AI 协作 (4)
  {
    category: "AI 协作",
    title: "Linear：重构 CI 应对 AI 编码爆炸引发的单测阻塞瓶颈",
    note: "复盘 AI Agent 编写代码导致提交量与 PR 爆发后的基础设施危机：通过细粒度增量缓存与测试并行拆解，将阻塞流水线的平均等待时间压缩至极限。",
    so_what: "当生产代码的速度被 AI 提升十倍，测试与部署管道就成了新的阿喀琉斯之踵；研发团队必须重构 CI/CD，才能消化智能体带来的海量产出。",
    source: "linear.app",
    url: "https://linear.app/now/ci-bottleneck-reworked",
    media: "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 协作",
    title: "trycua/cua：开源跨操作系统系统级操控引擎",
    note: "针对各类桌面智能体面临的底层系统碎片化痛点，统一了跨 macOS、Windows 和 Linux 的外设输入、屏幕捕获与动作调度抽象接口。",
    so_what: "让 Agent 自主操控电脑的前提是拥有可靠的“手和脚”；系统级跨平台标准抽象层的成熟，使开发者无需为每一个操作系统重新编写底座驱动。",
    source: "github.com",
    url: "https://github.com/trycua/cua",
    media: "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 协作",
    title: "ai-memory：跨编码终端的长期记忆库与上下文持久化",
    note: "提供轻量且独立的记忆存储协议，把跨不同终端、不同 IDE 与智能体对话沉淀的项目架构背景结构化保存，彻底终结换模型重新解释的繁琐。",
    so_what: "记忆层是解决大模型“失忆症”的终极解法；将项目规约沉淀为外挂的确定性向量记忆，才能让不同 Agent 共享同一个长远工程目标。",
    source: "github.com",
    url: "https://github.com/akitaonrails/ai-memory",
    media: "https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "AI 协作",
    title: "MVT：开源移动设备高阶渗透数字取证分析工具包",
    note: "面向移动端高隐蔽安全威胁的自动化取证分析流水线，将复杂的系统镜像备份解析、恶意痕迹比对与时间线还原全流程标准化与全量开源。",
    so_what: "随着端侧智能体被赋予越来越多的系统操作权限，透明且可追溯的数字取证不再只是极客玩具，而是保障终端资产安全不可或缺的防线。",
    source: "github.com",
    url: "https://github.com/mvt-project/mvt",
    media: "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 3. 一人公司 (4)
  {
    category: "一人公司",
    title: "Mycel：独立工作室交付物自动草拟系统",
    note: "专为单兵设计咨询团队打造：基于历史方案沉淀知识飞轮，使个人创作者能像大型跨国事务所般瞬间生成严谨规范的验收文档与报价清单。",
    so_what: "一人公司的规模不在于 headcount，而在于专业交付的厚重感；用自动化系统将繁复沉闷的商务文档流程化，才能腾出精力专注核心创造。",
    source: "mycelai.dev",
    url: "https://mycelai.dev/",
    media: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "一人公司",
    title: "Embedful：数分钟快速内嵌白标企业级客户数据看板",
    note: "无需编写复杂的权限隔离和数据透视前端，只需简单连接底层视图，即可为 SaaS 客户提供高质感、交互流畅的可内嵌白标分析面板。",
    so_what: "企业客户愿意为高可信的数据看板付出数倍溢价；通过预制组件交付大厂级看板，让单人团队也能从容承接高客单价 B 端企业单。",
    source: "embedful.io",
    url: "https://embedful.io/",
    media: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "一人公司",
    title: "Project NOMAD：纯离线个人数字知识方舟",
    note: "在家庭私有硬件上完整封装海量人类经典典籍、开源维基百科与轻量离线推理模型，构筑即便遭遇极端断网也能自洽运转的数字防灾基站。",
    so_what: "数字资产的最高主权是‘物理离线可用’；在云服务订阅与黑盒下架频发的时代，为核心个人知识库打造物理安全舱是真正的抗脆弱投资。",
    source: "github.com",
    url: "https://github.com/Crosstalk-Solutions/project-nomad",
    media: "https://images.unsplash.com/photo-1507842229451-7f01be6370d2?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "一人公司",
    title: "Minicart：创作者免折腾极简数字资产一页店铺",
    note: "彻底摒弃传统电商系统的繁杂插件与层级后台，用单页极简画布快速完成虚拟商品陈列、多币种结算与自动分发，零运维成本。",
    so_what: "每一道多余的结算点击都会流失 20% 的付款用户；对于售卖数字资源的独立创作者，去中心化的即时一页闭环才是转化率的定海神针。",
    source: "minicart.app",
    url: "https://minicart.app/",
    media: "https://images.unsplash.com/photo-1556742049-0a67c5574f73?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 4. 产品设计 (4)
  {
    category: "产品设计",
    title: "NotchOwl：刘海屏悬停效率微空间",
    note: "把屏幕刘海这一被动避让的物理缺陷重塑为轻量手势悬停微空间，以不占主视觉焦点的优雅微交互，聚合瞬时灵感速记与番茄钟。",
    so_what: "顶级交互总能在被忽视的系统边缘创造意外惊喜；把‘妥协的死角’转化为‘随叫随到的效率岛’，是用心做设计的最佳体现。",
    source: "notchowl.com",
    url: "https://notchowl.com/",
    media: "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品设计",
    title: "OmniDICOM：极速三维医学影像交互工具",
    note: "将以往笨重迟缓的放射学三维体渲染与横切面分析，通过现代化 WebAssembly 重构为毫无卡顿的毫秒级即时响应原生应用。",
    so_what: "专业工具的生产力取决于响应延迟；把繁重算力搬进轻量级现代架构中，能让医生和研究人员在流畅的交互中更快捕捉关键病灶。",
    source: "omnidicom.com",
    url: "https://omnidicom.com/",
    media: "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品设计",
    title: "Supercut：原生极速图像抠图修饰工具",
    note: "专为高频图层合成与发丝级精细抠图设计，剔除掉云端修图软件冗长的加载与非必要功能，带来无延迟、纯本地的原生交互回馈。",
    so_what: "工具软件的返璞归真胜过盲目做加法；在用户最痛的单一场景上把速度做到极致，往往能直接击溃大而全的平庸竞品。",
    source: "supercut.dev",
    url: "https://supercut.dev/",
    media: "https://images.unsplash.com/photo-1542744094-3a31f272c490?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品设计",
    title: "Harbor：全离线明码标价个人知识库",
    note: "拒绝云端算法绑架与永无止境的订阅制套路，坚持本地优先架构与一次性买断定价，为深度思考者提供不被打扰的数字思想庇护所。",
    so_what: "当所有软件都在逼用户联网上云，‘离线与买断’反而成了最强差异化；尊重用户的隐私与所有权，是赢得硬核用户忠诚的终极商业契约。",
    source: "harbor.my",
    url: "https://harbor.my/",
    media: "https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 5. 审美提升 (4)
  {
    category: "审美提升",
    title: "MOS：纽约 Art Omi 编织感铝制通透展亭",
    note: "以工业波纹铝板与交错穿孔构件编织出呼吸感十足的篮状曲面，让粗犷的现代金属材质在自然日光漫射下投射出如蕾丝般轻柔的诗意光影。",
    so_what: "材料的灵魂在于结构赋予的张力；用工业量产的廉价金属演绎大自然的通透与轻盈，展现了高超的形式转化美学功力。",
    source: "dezeen.com",
    url: "https://www.dezeen.com/2026/09/21/mos-art-omi-aluminium-pavilion/",
    media: "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "审美提升",
    title: "Motspråk：解构胶合板油彩画作重组为立体单椅",
    note: "先在平面胶合板上挥洒完整的大幅抽象油彩，再经精准计算锯切拆解并以纯榫卯重组为座椅，让观者在入座时穿梭于二维笔触与三维雕塑之间。",
    so_what: "打破媒介界限的设计才具备永恒趣味；让功能性家具承载纯艺术画作的破损与拼接，唤醒人们对物品多重生命形态的凝视。",
    source: "designboom.com",
    url: "https://www.designboom.com/design/motsprak-plywood-painting-chair-peytil-eitil-arbenz-thoren/",
    media: "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "审美提升",
    title: "Daylight：柔和排版与温润医疗交互美学",
    note: "以温润的人文主义衬线字体替换医疗科技惯用的冷酷无衬线，配以舒展松弛的行距留白与大地色阶，从视觉底层舒缓病患求医时的心理重压。",
    so_what: "排版与字重本身就具备心理疗愈功能；在情绪敏感的健康场景中，克制而富有体温的文字间距，能无声地传递出深沉的关怀感。",
    source: "typewolf.com",
    url: "https://www.typewolf.com/site-of-the-day/daylight-health",
    media: "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "审美提升",
    title: "Bebeau：18 块纯天然板岩雕琢的矿物吉他",
    note: "颠覆几百年来乐器必用木材的物理教条，耗时数月用坚硬冰冷的天然地质板岩打磨成轻薄琴体，激发出清脆、悠长且反常识的空灵共鸣。",
    so_what: "美感常常诞生在对传统的颠覆与重构中；敢于将常识中‘沉重不可发声’的石头做成悠扬琴器，是探索材料极限的浪漫壮举。",
    source: "designboom.com",
    url: "https://www.designboom.com/design/guitar-sound-stone-bebeau-builds-slate-rock/",
    media: "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 6. 产品营销 (4)
  {
    category: "产品营销",
    title: "AppGrowthKit：AI 驱动的移动商店高转化截屏生成范式",
    note: "汇聚全球应用商店顶级畅销应用的排版叙事范式，基于输入的应用卖点自动推导符合当地受众审美的截屏布局与文案钩子，极大加速出海 A/B 测试。",
    so_what: "商店详情页是流量漏斗里成本最高的关卡；用经过数据验证的成熟视觉结构替代设计师的自我表达，才能把买量每一分钱压榨出最大转化率。",
    source: "appgrowthkit.com",
    url: "https://appgrowthkit.com/",
    media: "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品营销",
    title: "PostSider：人机协作社媒全矩阵敏捷分发中心",
    note: "打通个人创作者与多 Agent 之间的排期与润色断层，在保持创作者个人语调的前提下，将一段思考自动转化为符合 X、领英与长文规范的多端矩阵发布。",
    so_what: "分发决定了优质内容的生命力；与其在各平台反复排版消耗意志，不如将跨渠道适配交给标准化流水线，把精力留给最有价值的第一手洞察。",
    source: "postsider.com",
    url: "https://postsider.com/",
    media: "https://images.unsplash.com/photo-1511578314322-379afb476865?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品营销",
    title: "少数派：一台主机多重角色的场景化软文范式复盘",
    note: "拆解爆款硬件营销软文的深层心理路径：跳脱出参数与跑分的无效堆砌，从极客家庭服务器到客厅娱乐主机具体推演生活切片，激发读者代入感。",
    so_what: "用户买的从来不是硬件参数，而是‘换上这台设备后更体面的生活方式’；用具体的场景细节击中渴望，远比列满 CPU 核心数更有说服力。",
    source: "sspai.com",
    url: "https://sspai.com/post/114829",
    media: "https://images.unsplash.com/photo-1544816155-12df9643f363?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品营销",
    title: "Lappka：将原始 UI 界面瞬时转化为高级感出海宣发卡片",
    note: "把繁琐的多设备边框裁切与光影渲染封装为拖拽式画布，数分钟内生成具有北欧留白与质感高光的产品出海图谱，显著提升海外社交媒体点击率。",
    so_what: "包装就是产品的第一印象；海外受众对视觉质感有着极强的隐性挑剔，体面的视觉呈现能让中小团队免于被打上‘廉价草台班子’的刻板标签。",
    source: "lappka.store",
    url: "https://www.lappka.store/",
    media: "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 7. AI 漫剧 (4)
  {
    category: "AI 漫剧",
    title: "漫剧出海：免费看广告，付费解锁——短剧出海的混合变现时代来了",
    note: "深度解构短剧出海深层演化：全球下载狂飙背后，纯付费模式在新兴市场遭遇天花板，以 FreeReels 为代表的‘免费广告（IAA）+ 付费解锁（IAP）’混合变现席卷行业。",
    so_what: "单纯靠买量拉动付费的时代已然终结；用免费看广告把东南亚和拉美流量盘活，再用北美高客单单集付费收割利润，是当下最健康的跨区域双池水泵模型。",
    source: "dramagoing.com",
    url: "https://dramagoing.com/daily-brief/2026-09-22.html",
    media: "https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 漫剧",
    title: "Mintegral H1 报告：全球短剧 App 下载暴涨 95.5% 达 14.5 亿次",
    note: "权威广告网络数据显示：短剧创意素材密度冲至 1887 领跑全品类，东南亚（5.18 亿次）与拉美（3.55 亿次）包揽八成流量，但北美依然贡献近半数海外真金白银。",
    so_what: "流量的大头和利润的大头在地理上彻底撕裂；短剧公司必须根据区域特征实施差异化产品定价与分发策略，切忌用一套买量打法跑通全球。",
    source: "marketingdive.com",
    url: "https://www.marketingdive.com/news/microdrama-advertising-surges-as-downloads-soar-report/828416/",
    media: "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "AI 漫剧",
    title: "AutoClip：长视频高光智能二创与自动切片工具",
    note: "专为短剧与视频剪辑师设计：通过声学特征与情绪曲线分析长视频对白，自动定位高戏剧张力爆点并完成竖屏居中构图与字幕烧录，将剪辑效率提升五倍。",
    so_what: "短剧宣发的胜负手在于前 3 秒黄金抓手；用算法自动嗅探最抓人的对立与反转瞬间，能以极低成本源源不断为信息流广告提供投流素材。",
    source: "github.com",
    url: "https://github.com/zhouxiaoka/autoclip",
    media: "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "AI 漫剧",
    title: "Streaming Meme：短剧混合变现占比达 57.6%，激励视频 eCPM 破 18.5 美元",
    note: "拆解短剧广告变现价值结构：短剧单次会话达 22 分钟（长视频移动端的 3 倍），激励视频 eCPM 达到 18.50 美元（休闲游戏的 2.3 倍），成移动广告单价新王者。",
    so_what: "‘用时间换剧情’在心理机制上完美契合了沉没成本心理；把广告位设计成解锁高潮剧集的正向奖励，用户不仅不反感，反而会自发看完广告。",
    source: "streamingmeme.com",
    url: "https://www.streamingmeme.com/articles/short-drama-app-downloads-hit-1-45-billion-as-hybrid-monetization-dominates",
    media: "https://images.unsplash.com/photo-1518173946687-a4c8a383392e?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 8. 编剧技巧 (4)
  {
    category: "编剧技巧",
    title: "万众编剧：编剧实用手册——如何从生活毛边提炼高概念故事？",
    note: "系统拆解故事核心构架：如何从碎片化的生活见闻中提炼出强对抗、高辨识度的‘如果……将会怎样’的核心假说，并在第一幕迅速建立观众同理心。",
    so_what: "好的故事不是词藻的堆砌，而是情境的极致挤压；把人物置入不得不做出痛苦抉择的极端困境中，角色的灵魂与戏剧张力才会自然喷薄而出。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/716",
    media: "https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "编剧技巧",
    title: "万众编剧：怎样设计具有驱动力的剧本事件？",
    note: "剖析剧本因果链条设计：打破平铺直叙的流水账纪录，通过‘危机触发—动机升级—代价加码’的三级跳机制，让每一个情节点都成为不可逆的命运转折。",
    so_what: "平庸的剧本只描述发生了什么，卓越的剧本展示每次选择带来的不可承受之重；让主角为每一个决定付出代价，观众的心率才会跟着剧情起伏。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/718",
    media: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "编剧技巧",
    title: "万众编剧：剧本创作必需的五大类角色功能网络",
    note: "解析角色配置的动力学模型：主角、对手、盟友、导师与信使并不是孤立的个体，而是围绕核心矛盾相互投射、互为镜像的心理功能能量场。",
    so_what: "配角存在的唯一意义是映照主角的内在缺陷并推动其质变；角色间如果缺少价值观的本质对抗，剧情必然陷入空洞虚假的喧嚣。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/721",
    media: "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "编剧技巧",
    title: "万众编剧：剧本写作中反转技巧的运用——误导与情理之中",
    note: "解密悬疑与短剧抓人反转的设计心法：如何巧妙利用‘铺垫与障眼法（Red Herring）’制造预期违背，同时在细节深处埋下符合逻辑的铁证，实现‘意料之外，情理之中’。",
    so_what: "拙劣的反转是把观众当傻子任意愚弄，高明的反转是让观众回看时恍然大悟并心服口服；伏笔埋得越深越自然，揭晓一刻的震撼力就越持久。",
    source: "wzbj1616.com",
    url: "https://www.wzbj1616.com/script_necessary_info/727",
    media: "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },

  // 9. 产品经理 (4)
  {
    category: "产品经理",
    title: "Lenny 深度复盘：Warp 如何靠 AI 工厂流水线每月合并 2,000 个 PR",
    note: "解构现代顶尖软件工程的组织跃迁：摒弃传统敏捷晨会与人力排期，建立起由智能体自主认领 issue、自主编写单测、自动跑通 CI 并提交合并的‘AI 软件装配流水线’。",
    so_what: "产品经理的角色正在从‘功能需求规划者’转型为‘智能体装配流水线的架构师’；懂得如何为 Agent 设立精准意图约束并设计验收机制，是下个世代 PM 的核心生存力。",
    source: "lennysnewsletter.com",
    url: "https://www.lennysnewsletter.com/p/how-warp-ships-2000-prs-a-month-with",
    media: "https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品经理",
    title: "BuilderIO：开源 agent-native 原生智能体应用框架",
    note: "定义下一代应用形态：不把 AI 当作聊天外挂补丁，而是将软件的状态流、交互意图与数据插槽作为系统的一等公民，让智能体与用户共享同一套操作上下文。",
    so_what: "当软件架构进入 agent-native 时代，传统静态界面的设计范式将被彻底瓦解；产品经理必须学会设计具备高度容错与自主探索能力的自适应交互界面。",
    source: "github.com",
    url: "https://github.com/BuilderIO/agent-native",
    media: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80",
    pinned: true,
  },
  {
    category: "产品经理",
    title: "Foremerge：多智能体并发意图冲突检测与架构治理",
    note: "解决多 Agent 协同研发的核心痛点：不仅能检测物理行级代码冲突，更能在业务意图层提早捕捉两个智能体在系统抽象设计与数据契约上的潜在逻辑分歧。",
    so_what: "管理多个自主 Agent 与管理多名工程师一样，最大的风险永远在‘意图理解的偏差’；把冲突检测提升到业务语义与架构契约层，才能防止代码库沦为无法维护的技术垃圾场。",
    source: "github.com",
    url: "https://github.com/naw103/foremerge",
    media: "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
  {
    category: "产品经理",
    title: "bmpi：Jev 边界与被动收入工程系统的长期思考",
    note: "深入探讨智能体接管基础决策原语后的商业护城河：当编写代码与自动化调用的边际成本逼近于零，如何构建具有非对称优势、抗周期波动的被动收入产品系统。",
    so_what: "单纯卖调用量或简单界面的产品将被通用 Agent 迅速夷平；唯有掌控稀缺的私有数据通道、深度行业信任与不可替代的分发节点，才能建立穿越周期的护城河。",
    source: "bmpi.dev",
    url: "https://www.bmpi.dev/dev/jev-boundary/",
    media: "https://images.unsplash.com/photo-1507679799987-c73779587ccf?w=800&auto=format&fit=crop&q=80",
    pinned: false,
  },
];

const frontmatter = {
  date: "2026-09-22",
  title: "9 月 22 日 · 智能装配与混合变现：当 Warp 用 Agent 重塑工厂，短剧在广告与付费间算清分账",
  highlights: "全网 9 大领域 36 篇高密度精选：Lenny 深度拆解 Warp 如何靠 AI 工厂每月合并 2000 个 PR、小米开源 MiMo-V2.6 全模态基座大模型、Mintegral 披露短剧出海 14.5 亿下载背后的混合变现浪潮、Tomer Tunguz 解密 AI 决策器重构 if 语句、万众编剧解构高概念故事与反转技巧。",
  draft: false,
  epigraph: "当工程研发从“写代码”升级为管理智能体装配流水线，当短剧出海从单纯砸钱买量转向“看广告换免费、掏真金买爽点”的精细分账——谁能把系统的每个环节算得足够细，谁才能在AI浪潮的退潮期里站稳脚跟。",
  lead: "今天的科技创新与数字商业一线正在经历一场深刻的系统级重构：在组织与研发效能赛道，Lenny's Newsletter 披露了终端工具 Warp 如何建立起由 Agent 自主认领任务、自写测试、自动跑通 CI 并每月合并 2,000 个 PR 的“AI 软件装配流水线”，完美印证了 Tomer Tunguz 所指出的“业务 if 条件分支正被毫秒级决策模型全面重构”；小米则向开源社区释出 MiMo-V2.6 全模态基座模型权重，打破闭源巨头的端侧视觉垄断；与此同时，在内容与数字文娱一线，Mintegral 最新 H1 2026 报告揭开短剧出海的残酷分化——全球短剧 App 下载同比暴涨 95.5% 突破 14.5 亿次，东南亚与拉美占尽八成流量却难赚钱，真正的利润依然死死锚定在北美，推动 57.6% 的短剧 App 转向“免费看广告（IAA）与付费解锁（IAP）”并行的混合变现时代，激励视频 eCPM 冲上 18.5 美元；从流水线式的智能体代码治理，到精细切割的跨国双池变现，每一个人都在重新审视生产力与商业价值的硬核闭环。",
  scene: "「你们团队现在一个月提几千个 PR，代码审查难道不崩溃吗？」「我们早就不用人工一行行 review 业务代码了。人和 Agent 各管各的：人只定义意图插槽与冲突边界，Agent 工厂自己领 issue、自写单测、自跑 CI。就像现在短剧出海一样，谁还在东南亚死磕付费？免费广告换留存，高客单放北美，两套齿轮各自咬死运转。」",
  cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80",
  items: ALL_ITEMS_22,
};

const closingNote = `
## 今日主理人寄语

当软件开发不再依靠人脑一行行码出堆叠的业务逻辑，而是由 Agent 军团在装配线上自动认领任务、自写单测、每月合并两千个 PR；当短剧出海不再盲目押注单一高价付费，而是用免费广告接住新兴市场，用精细化单集分账锁定北美利润——**狂躁的造梦时代已经彻底谢幕，精细的系统工程正在全面接管赛场。**

无论是写代码、做产品，还是拍短剧、卖数字资产，所有能跑赢周期的商业体都在做同一件事：

**把脆弱的经验转化为自动化的装配线，把单一的盈利通道重构为高弹性的混合变现网。**

别把精力浪费在与不可逆的趋势较劲上；去设计你的意图插槽，去算清每一个区域的留存与分账。

愿今天的 36 篇精选资讯，能为你提供看清下半场牌局的坚定航标。
`;

function run() {
  const yamlContent = yaml.dump(frontmatter, { lineWidth: -1, noRefs: true });
  const fullContent = `---\n${yamlContent}---\n${closingNote}\n`;
  
  const targetPath = path.resolve("src/content/daily/2026-09-22.md");
  fs.writeFileSync(targetPath, fullContent, "utf8");
  console.log("Successfully written:", targetPath);

  // Update all-used-urls.json
  const usedUrlsPath = path.resolve("scripts/all-used-urls.json");
  const usedUrls = JSON.parse(fs.readFileSync(usedUrlsPath, "utf8"));
  const usedSet = new Set(usedUrls);

  let added = 0;
  for (const item of ALL_ITEMS_22) {
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
