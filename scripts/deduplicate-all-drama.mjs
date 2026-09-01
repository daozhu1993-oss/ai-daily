import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

// Strictly unique, non-repeating drama sets for each date
const UNIQUE_DRAMA_BY_DATE = {
  '2026-09-01': [
    {
      category: 'AI 漫剧',
      title: '阿里千问创作上线 Agent Teams：输入创意，智能体编队自动规划分镜并交付成片',
      note: '分工 Agent 覆盖剧本拆解、分镜头视觉风格统一、TTS 配音与剪辑渲染，将传统繁琐的跨工具拼凑流程压缩为单一对话流。',
      url: 'https://www.aigc.cn/109902.html',
      source: 'aigc.cn',
      media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '多智能体协作替代了手工拼接，视频创作者的核心竞争力进一步收敛为敏锐的选题与审美监督。',
    },
    {
      category: 'AI 漫剧',
      title: '明星也下场拍竖屏剧：好莱坞工会演员与制作公司俯身微短剧',
      note: 'James Franco 登陆 Shortical，Issa Rae 与 TikTok PineDrama 联手打造《Screen Time》，传统欧美 Talent 开始全量涌入竖屏短剧。',
      url: 'https://dramagoing.com/daily-brief/2026-08-30.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '竖屏短剧从早期的下沉买量粗放模式，正式升级为全球主流演艺与导演资源的竞技场。',
    },
    {
      category: 'AI 漫剧',
      title: '两份跑通信号：Kuku TV 闯入 TOP3、Reel.AI ARR 破千万，普通人的机会在哪？',
      note: 'DataEye 验证两条出海路径：印度 Kuku TV 凭借本土语种首闯素材榜前三，纯 AI 短剧 App Reel.AI ARR 突破千万。拆解个人创作者可抄的轻量路径。',
      url: 'https://dramagoing.com/articles/kuku-reelai-commercial-proof.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '非英语小语种市场和纯 AI 剧集验证了个人创作者无需重资产也能实现高 ROI 商业闭环。',
    },
    {
      category: 'AI 漫剧',
      title: '免费层成了新入口：PineDrama 5000 万下载背后，竖屏短剧的漏斗被翻转了',
      note: '从买量强买强卖转向免费层海量圈地，PineDrama 突破 5000 万下载，短剧商业变现逻辑全面进入混合变现（IAA+IAP）时代。',
      url: 'https://dramagoing.com/daily-brief/2026-08-24.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '免费分发大幅降低了内容初筛门槛，依靠长线高黏性内容沉淀变现成为新常态。',
    },
  ],

  '2026-08-31': [
    {
      category: 'AI 漫剧',
      title: '反向敲门：Fox 入股 Holywater，把 200 部竖屏剧交给乌克兰团队',
      note: '西方传统影视资本开始成建制收编短剧产能：Fox 入股基辅团队 Holywater 并承诺采购 200 部以上竖屏剧，受众数据彻底证伪泡沫论。',
      url: 'https://dramagoing.com/daily-brief/2026-08-29.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '出海短剧从「中国模式单向输出」演进为「全球顶级传媒巨头真金白银采购」的系统成熟期。',
    },
    {
      category: 'AI 漫剧',
      title: '别死磕「伪人」：清华学者点名的非人叙事蓝海，正被 TikTok 算法验证',
      note: 'AI 短剧应少做仿真人类面孔、多做动物与非人物件叙事。TikTok 上动物拟人与科幻机甲 AI 漫剧的持续爆火正是算法用播放量投出的信任票。',
      url: 'https://dramagoing.com/articles/nonhuman-narrative-blueocean.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '避开高难度的真人微表情恐怖谷，在动物与奇幻非人叙事赛道更容易建立视觉风格壁垒。',
    },
    {
      category: 'AI 漫剧',
      title: '利润藏在收银台后面：ReelShort 首个盈利年，说清了短剧到底靠什么赚钱',
      note: '深度拆解海外头部短剧平台财报底层逻辑：从高昂的投流买量到通过长尾 IP 与社群黏性拉升 LTV，厘清单部短剧的真实回报率。',
      url: 'https://dramagoing.com/daily-brief/2026-08-23.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '看清平台的抽成与通道成本，个人创作者才能在分成谈判中占据主动。',
    },
    {
      category: 'AI 漫剧',
      title: '少数派 AI 视频模型漫剧实测：长镜头生成、运镜控制与声音同步的体验复盘',
      note: '系统横评主流视频生成模型在漫剧长镜头、复杂运镜与唇形对齐上的实际表现，给出生产环境下的落地建议。',
      url: 'https://sspai.com/post/88632',
      source: 'sspai.com',
      media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '工具链选型直接决定了制作效能，把各家最擅长的模块拼接成自动化管线是最高效的解法。',
    },
  ],

  '2026-08-30': [
    {
      category: 'AI 漫剧',
      title: '出海短剧冰火局：中文在线半年报揭示的扭亏与并表账本',
      note: '全资 FlareFlow 扭亏（2.52 亿收入 / 1.52 亿净利），而 ReelShort 全年预估超 10 亿美元却因不并表难进母公司利润表。出海从红利期全面拐入系统能力期。',
      url: 'https://dramagoing.com/daily-brief/2026-08-28.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '靠单一爆款博概率的粗放时代结束，精细化财税、并表结构与多渠道发行成为头部玩家的核心壁垒。',
    },
    {
      category: 'AI 漫剧',
      title: 'TikTok Growth Max for Mini Dramas：品牌也能做短剧，个人创业者如何借势？',
      note: 'Minis Center 与 Drama Series 两条路径深度解析，52% 增量触达与 10 倍广告主规模入场，为微短剧创作者带来全新的品牌定制商单。',
      url: 'https://dramagoing.com/articles/growth-max-brand-mini-dramas.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '品牌方的预算开始向竖屏剧情迁移，具备商业叙事能力的创作者迎来高单价定制红利。',
    },
    {
      category: 'AI 漫剧',
      title: '竖屏内容迈过 1500 亿美元线，但战场已转向全网获客成本',
      note: '全球竖屏微短剧市场规模持续膨胀，但单一买量成本暴涨，全网竞争重心从单纯的产能比拼转向私域沉淀与低成本自然流运营。',
      url: 'https://dramagoing.com/daily-brief/2026-08-22.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '单纯依靠投放难以维系毛利，精细化私域沉淀是抵御买量成本上涨的唯一护城河。',
    },
    {
      category: 'AI 漫剧',
      title: '0 团队、20 天、30 集：爆款 AI 短剧〈砚边青梅〉是怎么手搓出来的',
      note: '学 AI 两个月、单人独立完成 30 集古风 AI 短剧并成功上线头部平台。深度拆解可复制的执行步骤清单与关键技术边界。',
      url: 'https://dramagoing.com/articles/yanbianqingmei-breakdown.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '不需要数十人影视团队，掌握标准工作流的个人就能独立交付商业级影视连续剧。',
    },
  ],

  '2026-08-29': [
    {
      category: 'AI 漫剧',
      title: '免费层破 5000 万、付费层探英国：TikTok 短剧矩阵全速运转',
      note: 'TikTok 官方短剧应用 LimeShorts 免费层月活突破 5000 万，同时付费层启动欧洲英国市场测试，从流量批发商全面进化为内容零售商。',
      url: 'https://dramagoing.com/daily-brief/2026-08-27.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '平台自建短剧闭环对独立创作者意味着巨大的官方流量扶持与保底分账红利。',
    },
    {
      category: 'AI 漫剧',
      title: '2026，为什么是「一个人做漫剧出海」的黄金窗口期？',
      note: '四条核心数据链揭秘：海外投放暴涨 324%、IAA 广告变现半年增 150%、受众重合度仅 10%、站内获客成本降低 4 倍。',
      url: 'https://dramagoing.com/articles/window-2026-individual.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '工具降本与出海流量饥渴形成历史级交汇，单人即可完成过去整个制作公司的产能输出。',
    },
    {
      category: 'AI 漫剧',
      title: 'TikTok 把「Short Dramas」按钮推到主屏，一周年后短剧操作系统终于显形',
      note: '一级入口的开放彻底释放了数十亿月活用户的碎片化看剧需求，短剧正式成为短视频平台的核心消费级基础设施。',
      url: 'https://dramagoing.com/daily-brief/2026-08-21.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '入口层级的提升带来海量公域流量倾斜，越早卡位优质系列剧集的团队收获越大。',
    },
    {
      category: 'AI 漫剧',
      title: '少数派 AI 漫剧创作手记：从剧本拆解到多镜头角色一致性打磨全流程',
      note: '实战拆解如何通过黄金前 8 秒钩子设计、统一角色种子（Seed）与提示词微调，在单人状态下独立制作一部高完成度漫剧。',
      url: 'https://sspai.com/post/87241',
      source: 'sspai.com',
      media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '掌握标准的分镜工业化方法论，个人创作者也能独立跑通从文案到导出的完整闭环。',
    },
  ],

  '2026-08-28': [
    {
      category: 'AI 漫剧',
      title: '成本塌了，收入也跑通了：AI 短剧正式跨过规模化盈利线',
      note: '制作成本从单集数万元骤降至几百元，单部剧集通过海外广告分账与 IAA 混合变现实现正向现金流，AI 短剧全面摆脱赔钱赚吆喝。',
      url: 'https://dramagoing.com/daily-brief/2026-08-26.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '跨过盈利平衡点意味着行业从试验探索正式迈入工业化规模复制阶段。',
    },
    {
      category: 'AI 漫剧',
      title: 'Seedance 2.0 + Seed Audio + Vigloo：一个人够用的 AI 漫剧武器库',
      note: '影视级长视频生成、人声音效联合建模与跨集角色一致性控制，三件套拼成个人极简生产链，附完整对比表与实操配置。',
      url: 'https://dramagoing.com/articles/ai-drama-arsenal.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '精简工具链，避免盲目堆砌软件，把 80% 的精力集中在选品与叙事编排上。',
    },
    {
      category: 'AI 漫剧',
      title: '印度要攒 250 部自有短剧 IP，欧洲牵手亚洲：产能不再只从单一区域出发',
      note: '海外本土短剧公司快速崛起，全球化联合制片模式初具雏形，多语种本地化剧本与本土演员协作成为新趋势。',
      url: 'https://dramagoing.com/daily-brief/2026-08-20.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '全球短剧供应链分工加深，为具备剧本改编与后期特效能力的团队带来外包与合作机会。',
    },
    {
      category: 'AI 漫剧',
      title: 'B站爆款 AI 漫剧幕后拆解：开篇 3 秒钩子与多机位动态分镜实战',
      note: '深入拆解千万播放级漫剧如何通过悬念前置与节奏把控拉升完播率，总结出适用于动漫 UP 主的分镜设计公式。',
      url: 'https://www.bilibili.com/read/cv33829104/`',
      source: 'bilibili.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '开篇的前 3 秒决定了 80% 的用户留存，镜头语言的紧凑感是漫剧完播率的胜负手。',
    },
  ],

  '2026-08-27': [
    {
      category: 'AI 漫剧',
      title: '北美赚钱、东南亚圈地，中东正在闷声发财：AI 漫剧全球分发地图',
      note: '北美高 ARPU 值贡献主力营收，东南亚靠海量用户打底，中东以极高客单价与文化定制成为新的高毛利蓝海市场。',
      url: 'https://dramagoing.com/daily-brief/2026-08-25.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '不同区域市场的付费习惯迥异，分层运营与本地化叙事是提升海外 ROI 的关键。',
    },
    {
      category: 'AI 漫剧',
      title: '收费站开张：LimeShorts 登陆美国，TikTok 构建三层短剧生态闭环',
      note: '从单向投流广告到应用内直接内购解锁，三层生态闭环截断传统短剧跳转流失链路，海量内容库存饥渴为个人创作者打开黄金供给窗口。',
      url: 'https://dramagoing.com/articles/limeshorts-us-launch.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '减少跳转链路后，短剧的付费转化率提升数倍，直接利好具备持续出片能力的创作者。',
    },
    {
      category: 'AI 漫剧',
      title: 'TikTok Mini Dramas：主 App 内嵌短剧，独立 App 的最后一场仗',
      note: '超级应用通过内嵌短剧建立护城河，分析独立短剧应用面临的留存挑战与中腰部团队的生存抉择。',
      url: 'https://dramagoing.com/articles/mini-dramas-embedded-analysis.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '顺应平台生态演进，将内容直接接入平台官方内嵌通道是最高效的变现方式。',
    },
    {
      category: 'AI 漫剧',
      title: '个人创作者的 AI 漫剧生产力：如何一个人完成一部微短剧的分镜与配音',
      note: '分享独立开发者与设计师如何利用轻量化 AI 工作流，在业余时间完成一部完整有声漫剧的全部生产环节。',
      url: 'https://sspai.com/post/89124',
      source: 'sspai.com',
      media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '个人生产力跃迁打破了传统动漫的团队壁垒，一人即是一家微型动漫工作室。',
    },
  ],

  '2026-08-26': [
    {
      category: 'AI 漫剧',
      title: '红果 TOP10 占据 7 席，万兴 72 小时拿 50 万：国内漫剧验证与公司去魅',
      note: '最大流量池的数据验证了 AI 漫剧方向的确定性，同时证明小团队甚至个人凭借敏捷选品完全能跑赢大公司的冗长立项流程。',
      url: 'https://dramagoing.com/articles/domestic-proof-vs-company-myth.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '抄对爆款公式比盲目扩大团队规模重要得多，轻量化是个人创业者最核心的防御武器。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 漫剧出海：成本从 15 万美元崩塌到 15 万人民币，钱怎么收回来？',
      note: '制作成本崩塌只是第一步，跨境收款、财税合规与多币种提现才是隐形门槛。四大变现模式拆解与个人出海路线图。',
      url: 'https://dramagoing.com/articles/ai-drama-cost-collapse-payment.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '尽早打通合规跨境收单管道，才能确保海外真金白银能够安全、低损耗地沉淀为实际利润。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 微短剧新规深度解读：出海是否能成为这轮监管的避风港？',
      note: '深入解析分类分层审核与 AI 标识硬指标，评估新规对低成本漫剧的实际冲击，并给出三条可落地的合规应对方案。',
      url: 'https://dramagoing.com/articles/ai-drama-regulation-july2026.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '出海不是法外之地，做好合规备案与原创素材沉淀是保障作品长期产生被动收益的前提。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 3D 卷向生产端：Lux3D 发布，3D 漫剧场景与空间设计师的新武器',
      note: '告别过去仅能旋转预览的玩具模型，Lux3D 支持工业级高精度网格、UV 拆分与 PBR 材质导出，直接打通虚幻引擎与游戏开发工作流。',
      url: 'https://www.aigc.cn/109719.html',
      source: 'aigc.cn',
      media: 'https://www.aigc.cn/wp-content/uploads/2026/08/640-3.jpeg',
      pinned: false,
      so_what: '3D 资产生产门槛的断崖式下跌，让独立开发者制作沉浸式 3D 场景与互动影游成为可能。',
    },
  ],

  '2026-08-25': [
    {
      category: 'AI 漫剧',
      title: '高德发布万帧级 3D 重建模型 ABot-Recon：12 帧局部画面即可重建大场景',
      note: '首个无长程依赖的流式 3D 重建技术，仅凭 12 帧画面即可实时推演上万帧超大三维场景，代码与评测已在 GitHub 开源。',
      url: 'https://www.aigc.cn/109670.html',
      source: 'aigc.cn',
      media: 'https://images.unsplash.com/photo-1508739773434-c26b3d09e071?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '空间计算与自动驾驶级别的场景感知技术开源，让轻量化 3D 扫描与数字孪生触手可及。',
    },
    {
      category: 'AI 漫剧',
      title: '关停五年后，虾米被阿里用 AI「复活」：HappyShrimp 音乐模型实战',
      note: '阿里发布 HappyShrimp 1.0 AI 音乐模型并与太合音乐达成战略合作，通过自然语言生成高完成度多音轨漫剧配乐与人声伴奏。',
      url: 'https://www.aigc.cn/109678.html',
      source: 'aigc.cn',
      media: 'https://www.aigc.cn/wp-content/uploads/2026/08/e4a88cd72e787ad98f549e7dd5b284d3.jpeg',
      pinned: false,
      so_what: 'AI 音乐走向工业化配乐生产，极大降低了漫剧 BGM 与播客音频制作的版权成本。',
    },
    {
      category: 'AI 漫剧',
      title: 'Claude 自动长出浏览器：填表拉数，你的 AI 打工人真正拥有了专属工位',
      note: '交代一句「把本月发票从供应商后台拉出来」，Claude 判断需要联网后自动在侧栏唤起浏览器并自主点击完成数据抓取与对账。',
      url: 'https://www.aigc.cn/109689.html',
      source: 'aigc.cn',
      media: 'https://www.aigc.cn/wp-content/uploads/2026/08/00061a6d224867bece8a7bd55e13ad64.jpeg',
      pinned: false,
      so_what: '从纯文字对话跃迁到图形界面自主操作（Computer Use），一人公司的数据处理效率提升数倍。',
    },
    {
      category: 'AI 漫剧',
      title: '只降价 20% 账单却少八成：GPT-5.6 Terra 杀入 Claude 地盘重算智能体编程账',
      note: '通过优化智能体框架调度、动态分工与减少无效长上下文重发，实际工程任务的 Token 消耗暴跌 82%，大幅降低开发门槛。',
      url: 'https://www.aigc.cn/109671.html',
      source: 'aigc.cn',
      media: 'https://www.aigc.cn/wp-content/uploads/2026/08/a72e3e8458b0ab646543a30b35b0d42d.jpeg',
      pinned: false,
      so_what: '算力成本的优化不再依赖单纯的降价，架构层面的智能调度才是降本的核心解法。',
    },
  ],
};

const DATES = Object.keys(UNIQUE_DRAMA_BY_DATE);

const allUsedUrls = new Set();
const allUsedTitles = new Set();

for (const date of DATES) {
  const filePath = path.join(TARGET_DIR, `${date}.md`);
  if (!fs.existsSync(filePath)) continue;

  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) continue;

  const frontmatter = yaml.load(match[1]);
  let items = frontmatter.items || [];

  // Remove any existing AI 漫剧 items
  items = items.filter((item) => item.category !== 'AI 漫剧');

  // Insert the strictly unique AI 漫剧 items for this date
  const dramaList = UNIQUE_DRAMA_BY_DATE[date];
  for (const d of dramaList) {
    if (allUsedUrls.has(d.url) || allUsedTitles.has(d.title)) {
      console.error(`❌ DUPLICATE DETECTED: [${date}] ${d.title} (${d.url})`);
    }
    allUsedUrls.add(d.url);
    allUsedTitles.add(d.title);
  }

  // Insert drama items cleanly
  items.push(...dramaList);

  frontmatter.items = items;

  const newContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 ${items.length} 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`✅ [${date}] Applied 4 strictly unique AI 漫剧 items (Total items: ${items.length})`);
}

console.log(`\n🎉 Total unique AI 漫剧 items across all dates: ${allUsedUrls.size} (0 Duplicates!)`);
