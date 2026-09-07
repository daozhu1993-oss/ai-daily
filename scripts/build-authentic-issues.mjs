import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

// Signature custom items definitions for each day
const CUSTOM_ITEMS_05 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: 'TikTok 把短剧收进自家入口，9月新规给 AI 漫剧画了红线',
    note: 'TikTok 网页版上线 Short Dramas 独立入口做生态收口，9月1日《微短剧发展管理办法》落地为 AI 漫剧备案与版权合规划定清晰红线。',
    so_what: '短剧从野蛮生长的投流买量游戏转向平台级生态生意；对小团队而言，合规与版权自证将成为比单纯爆款更关键的生存门槛。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-05.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'Seedance 2.0 + Seed Audio + Vigloo：一个人够用的 AI 漫剧武器库',
    note: '深度梳理单人创作者全套 AI 漫剧工具链路，从分镜生图、音效对白拟真到海外流媒体分发平台的一站式武器库搭配。',
    so_what: '制作工具的集成化正在将漫剧团队人数压缩至单兵作战，选准一套自洽的工具链组合，个人就能抗衡传统中型动画制作组的产能。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/ai-drama-arsenal.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '别死磕“伪人”：清华学者点名的非人叙事蓝海，正被 TikTok 算法验证',
    note: '揭秘为什么水果拟人、动物机甲与魔性非人类角色在竖屏短剧中的完播率与爆款率远超逼真人像，绕开恐怖谷效应反而打开吸睛蓝海。',
    so_what: '做内容不要在模型最薄弱的地方硬碰硬；避开真实人类面部僵硬的劣势，用非人叙事的奇观感抢夺廉价注意力是极致聪明的差异化打法。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/nonhuman-narrative-blueocean.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '2026年AI漫剧工具盘点：11款主流工具全面对比',
    note: '横向实测可灵、Runway、Luma、Midjourney 及声音驱动工具在漫剧制作管线中的优劣势、出图稳定性与综合成本消耗。',
    so_what: '工业化生产的第一法则不是迷信单一明星工具，而是搞清楚每一把工具在管线中的精确工位，降本增效从工具选型开始。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/tools-comparison.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '三幕剧：每个编剧都该掌握的第一课',
    note: '拆解古典三幕剧结构：建置、对抗与结局的黄金比例，以及如何用情节点（Plot Point）打破主角的日常平衡。',
    so_what: '三幕剧不仅是剧本的骨架，更是所有用户体验旅程的原型；懂得在开局打破平静、在推进中层层施压，你的产品与叙事才能扣人心弦。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/939',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '《盗梦空间》节奏分析：多层梦境嵌套的时间膨胀效应',
    note: '深入剖析诺兰如何通过多层梦境嵌套的时间膨胀效应，制造令人屏息的四重时空叙事交响。',
    so_what: '叙事节奏的快慢是由信息密度与时间压迫感决定的；学会多线并进与高潮收拢，能让内容产生强大的沉浸力。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/916',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '微短剧→AI漫剧转换规范手册',
    note: '详细对比真人实拍剧本与 AI 漫剧脚本的格式差异，重点解析如何将复杂的文学心理描写转化为大模型易于解析的视觉机位指令。',
    so_what: '编剧不仅要懂写戏，更要懂把戏剧意图无损传达给 AI 引擎；剧本格式的工业化改造是提升出图匹配率的关键一环。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/912',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '新人编剧100问：从灵感枯竭到人物小传立项',
    note: '汇集编剧入行常踩的 100 个深坑：从灵感枯竭如何抢救、人物小传如何立住，到如何应对剧本会上的外行意见。',
    so_what: '写作不仅是一门艺术，更是一套心理韧性与职业沟通系统；把基本功夯实，才能在漫长创作中保持稳定的高质量产出。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/899',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '产品经理的三思之道：思危、思退、思变',
    note: '在大模型摧枯拉朽重构交互界面的今天，传统 PM 必须思架构之危、思同质化功能之退、思深度业务闭环之变。',
    so_what: '危机是进化的催化剂；与其在逐渐贬值的画原型技能上内卷，不如深入垂直业务一线，做懂真实场景的商业架构师。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6459338.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '产品的“死生之地”：产品经理做产品定位',
    note: '深度剖析为什么定位不准的产品最终都会沦为巨头炮灰；如何在红海中切割出专属细分阵地，建立不可替代的心智防线。',
    so_what: '战略的本质不是决定做什么，而是决定坚决不做什么；克制地守护核心定位，你的产品才能在噪音中被清晰记住。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6457685.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'Claude 连续越界后，Anthropic 和 OpenAI 开始主动踩刹车',
    note: '随着计算机控制（Computer Use）与自主智能体能力飙升，大厂开始主动在高风险接口上修筑安全护栏与权限熔断。',
    so_what: '确定性与安全性是企业采购的底线；产品经理在设计自主功能时必须预设优雅的刹车与确认机制，防患于未然。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6459866.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '技术转产品：B端音视频SDK，如何把技术组件设计成业务能力',
    note: '拆解如何把底层复杂的编解码、网络抖动降级等纯技术参数，抽象包装为客户一键集成的直观业务场景解决方案。',
    so_what: '优秀的 B 端产品是技术的翻译官；把底层艰深的工程黑话转化为客户业务报表上的直观价值，才是产品经理的核心功力。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pd/6460680.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
];

const CUSTOM_ITEMS_06 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: 'LimeShorts 收费定档，TikTok 把短剧收进自家「操作系统」',
    note: 'LimeShorts 在美国收费定档（周卡 19.99/年卡 199.99 美元），字节把短剧收进自有操作系统，TikTok 原生爆款漫剧单条播放破千万。',
    so_what: '付费货架与野生实验室两条线同时在 TikTok 跑通，海外短剧从纯搬运走向深度本土化订阅与平台原生推荐生态。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-06.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '0 团队、20 天、30 集：〈砚边青梅〉是怎么手搓出来的',
    note: '拆解爆款古风 AI 漫剧一人独立全流程：角色 LoRA 锚定、分镜脚本细化、动作平滑过渡与 DaVinci 胶片级后期的实战避坑笔记。',
    so_what: '没有大厂预算的小团队同样能做出爆款；只要把统一角色特征与情绪叙事节拍吃透，手搓漫剧也能拥有极高的商业转化率。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/yanbianqingmei-breakdown.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '两份“跑通”信号：Kuku TV 闯入 TOP3、Reel.AI ARR 破千万，普通人的机会在哪？',
    note: '解析海外新兴短剧平台与 AI 短剧生成工具的商业化闭环数据：微型制作团队如何抓住平台冷启动期红利赚取稳定分账。',
    so_what: '商业机会永远在平台迭代的缝隙中；跟随头部平台的流量分配机制，以高频合格的短剧供给抢占生态位是普通人的最佳入场券。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/kuku-reelai-commercial-proof.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'AI漫剧出海：成本崩塌后钱怎么收回来',
    note: '生产端单集出图成本虽然断崖式下跌，但海外支付网关、Stripe 扣费损耗、退款率与买量投放 ROI 才是决定真正利润率的命门。',
    so_what: '降本只是上半场，收钱才是生死局；一人漫剧团队不仅要做内容极客，更要算清楚每笔海外支付与买量转化的账本。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/ai-drama-cost-collapse-payment.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '新人必看！两种常见的剧本模式',
    note: '对比「英雄之旅」单主角弧光与「群戏多视角」网状叙事的优劣势，指导创作者如何根据预算与题材选择最适配的故事模型。',
    so_what: '故事模型决定了观众的情感投入通道；选对叙事结构，能以最小的篇幅调动受众最深沉的情感共鸣。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/872',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '2025喜剧微短剧爆款创作指南：从看点剖析到实用技巧',
    note: '深度拆解喜剧短剧的三大核心搞笑机制：预期违背、身份错位与降维打击，剖析前 30 秒如何密集抛出笑点。',
    so_what: '幽默是人类面对荒谬世界的解药；在短剧中用喜剧包裹敏锐的社会洞察，传播穿透力比纯煽情高出数倍。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/851',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '古装悬疑微短剧创作技巧全解析：从爆款中汲取灵感',
    note: '剖析古典案情推演中的伏笔回收技巧：如何做到「情理之中、意料之外」，在破案主线中穿插人物身份危机。',
    so_what: '悬念是让人不断看下去的内在发动机；在产品功能引导中借镜悬念设计，能极大提升用户对未解锁特性的探索欲。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/850',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '甜宠微短剧：看点解析、爆款逻辑与成功案例洞察',
    note: '解构情绪价值供给的经典套路：情绪推拉、微小吃醋与双向奔赴，如何在极致短的篇幅内给观众带来纯粹的高多巴胺抚慰。',
    so_what: '商业的底层是情绪消费；读懂大众内心的孤独与渴望，产品才能超越单纯工具属性，成为用户的情感依托。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/849',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '当实现不再稀缺，AI PM 靠什么活下去？',
    note: '当写代码、画线框和调接口的门槛被 AI 夷为平地，产品经理的真正护城河收缩为对人类真实痛点的洞察与商业价值闭环的掌控。',
    so_what: '技术平权让同质化竞争加剧；唯有深入不为人知的细分场景，解决别人嫌脏嫌累的微小摩擦，才能拥有持续的定价权。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6425789.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '客户不续费，不是因为AI不够强，而是因为“没你也行”',
    note: '深入复盘企业客户流失的残酷真相：AI 生成的内容如果不能深度嵌入客户原有的核心审批流与系统，就会随时被当成玩具剔除。',
    so_what: '嵌入业务工作流是 SaaS 生死的生命线；千万不要做可有可无的锦上添花，做沉淀在关键数据节点上的主轴齿轮。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6460372.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '写PRD画原型时代结束，聊聊AI抢不走的3个产品经理底层能力',
    note: '细数 AI 无法替代的核心心智：复杂利益相关者平衡、非理性人性洞察与面对极端不确定性时的果决拍板。',
    so_what: '机器善于在已有的规则中寻找最优解，而人负责定义新的规则；提升自己的判断力与审美直觉，才能站在浪潮之上。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6422841.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '从 0 设计 AI 陪伴产品：陪伴产品的内核是什么？',
    note: '拆解陪伴型产品的底层心理机制：不是回答事实性问题的百科全书，而是提供持续情绪价值、安全感托底与个性化记忆沉淀的数字化化身。',
    so_what: '情感连结是世界上最稳固的粘合剂；理解陪伴背后的心理饥渴，产品经理才能在冰冷的算法中注入触动人心的温度。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pd/6457521.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
];

const CUSTOM_ITEMS_07 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '甜宠霸总退潮，狼人接棒：出海短剧进入价值深耕期',
    note: '9月初两份硬证据落地：中文在线与昆仑万维半年报坐实盈利，AI 漫剧占投放大盘 78%+，海外受众从同质化霸总彻底转向狼人魔幻题材。',
    so_what: '题材红利的轮动极其残酷；紧盯海外受众心理变迁，及时转向高溢价、长生命周期的垂类题材，才能持续维持买量正循环。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-04.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '2026，是“一个人做漫剧出海”的窗口期',
    note: '为什么当前是单兵作战出海做 AI 漫剧的黄金期？模型能力跨越可用性阈值，而传统大影视公司机构臃肿反应迟缓，给敏捷个体留下巨大缝隙。',
    so_what: '窗口期稍纵即逝；用轻量架构快速试错，把叙事核心与商业化变现链条跑顺，一个人就是一家高效运转的微型影视厂牌。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/window-2026-individual.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '收费站开张了：LimeShorts 正式登陆美国，TikTok 不再只做流量批发商',
    note: '字节跳动旗下独立短剧平台 LimeShorts 在美开启订阅收费，构建自建闭环播放场域，标志着短剧出海从投流变现进入平台会员时代。',
    so_what: '巨头搭建好收费站之后，最饥渴的就是高质量、高周转的优质内容；紧跟平台官方扶持政策，创作者将迎来新一轮分账红利。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/limeshorts-us-launch.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '7月微短剧新规落地：AI漫剧要走哪些备案程序',
    note: '梳理监管新规下 AI 漫剧的申报要件、生成内容标识规范与版权合规路径，解析合法合规上线的必备底线。',
    so_what: '监管与规范化是行业成熟的标志；提早建立规范的版权自证流程与素材溯源档案，才能防范政策风险、走得长远。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/ai-drama-regulation-july2026.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '情节点——《电影剧本写作基础》',
    note: '悉德·菲尔德经典理论重温：情节点是一切叙事前进的钩子，它钩住故事，并将其转向另一个叙事方向。',
    so_what: '每一个关键业务决策也是一个情节点；理解生活与事业的转向逻辑，你在面临突发危机时就能做出最富戏剧张力也最清醒的抉择。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/806',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '营造戏剧张力，让甲方对你的剧本欲罢不能',
    note: '揭秘编剧提案的核心攻心法：如何在提纲中凸显商业价值与不可替代的情感奇观，让投资人在 5 分钟内下定决心。',
    so_what: '提案的本质是共谋；不要展示繁杂的技术细节，而是向决策者展现一个引人入胜的成功愿景与丰厚回报。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/793',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '女性题材微短剧创作新思路与爆款案例剖析',
    note: '深入分析现代女性观众的心理投射：告别单纯苦情等待拯救，转向独立搞事业、自我救赎与清醒觉醒的爽感叙事。',
    so_what: '时代心态的变迁直接定义了主流内容的审美取向；敏锐感知大众群体的自我认同转向，是创作长盛不衰的源泉。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/839',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: 'AI 短剧制作与上线全流程详细要求',
    note: '从剧本梗概拆解、分镜提示词标准化，到画面抽卡校验与终审导出的全套实操规范，确保成片符合上线工业标准。',
    so_what: '规范化是规模化生产的唯一前提；把天马行空的创意收纳进标准作业流程，才能实现稳定、可预测的高水平交付。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/900',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '八个人并行开发，为什么反而更难',
    note: '剖析人月神话在现代微服务与大模型时代的变体：沟通拓扑复杂度随人数呈指数级上升，而单人全栈借助 AI 正在击穿传统敏捷协作边界。',
    so_what: '团队规模不再是生产力的代名词；掌握先进工具的精悍个体或极小团队，凭借零沟通损耗往往能打出超越百人团队的冲刺速度。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6460515.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '迟到的冰箱：通用技术的原生应用，为什么总要等十几年',
    note: '探讨通用底层技术（如电力、互联网与大模型）从诞生到真正孵化出改变大众生活常态的原生超级应用之间的漫长时滞。',
    so_what: '别因短期内未出现颠覆性爆款而丧失信心；历史表明，真正的原生范式跃迁往往孕育在长期的场景渗透与社会习惯重塑之中。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6460536.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '商业化产品不懂数据，等于盲人摸象',
    note: '详细拆解从流量转化漏斗、用户群体留存曲线到 LTV/CAC 偿还周期的指标推演模型，指导产品经理如何用数据反哺决策。',
    so_what: '商业化是产品的终极检验场；学会用客观严谨的量化指标审视每一个功能变更，才能在激烈的市场竞争中站稳脚跟。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6426257.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '扎克伯格想让 AI 接管 Meta 真人工作，几个月后他自己叫停了',
    note: '复盘 Meta 内部尝试让 AI 完全取代中基层员工过程中出现的上下文割裂、权责推诿与系统性瘫痪，提示全自动化的深水区陷阱。',
    so_what: '人机协同的黄金平衡点在于「人做裁决与审美把关，AI 做高频繁重的草稿编排」；盲目追求无人化只会招致系统性雪崩。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6459550.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
];

// Helper to interleave and balance items across categories
function balanceAndShuffle(baseItems, customItems) {
  // Combine all
  const allItems = [...customItems, ...baseItems];

  // Group by category
  const byCat = {};
  for (const it of allItems) {
    if (!byCat[it.category]) byCat[it.category] = [];
    byCat[it.category].push(it);
  }

  // Interleave round-robin across categories
  const categories = Object.keys(byCat).sort((a, b) => {
    // Put signature custom categories early in the round-robin
    const priority = ['AI 资讯', 'AI 漫剧', '产品经理', '编剧技巧', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 协作'];
    return priority.indexOf(a) - priority.indexOf(b);
  });

  const result = [];
  let added = true;
  let round = 0;

  while (added) {
    added = false;
    for (const cat of categories) {
      if (byCat[cat] && byCat[cat].length > 0) {
        result.push(byCat[cat].shift());
        added = true;
      }
    }
    round++;
  }

  // Ensure pinned items stay pinned
  return result;
}

const DAYS = [
  {
    date: '2026-09-05',
    title: '9 月 5 日 · 代理自闭环与漫剧工业化：当大模型开始交差，创作者开始验票',
    epigraph: '当推理成本被压缩到十分之一，最先发生质变的不是算力中心，而是能把剧情和商业直接跑通的个人车间。',
    lead: '今天的信号不在某一个模型又快了多少，而在代理开始彼此传话、自己约时间、自己追发票，也开始替人修改公开页面。另一边，费马大定理的形式化证明、音乐生成和三维场景都在把“复杂制作”拆成可核对的中间步骤。效率确实在上升，但一个反常识的提醒也更清楚了：代理越会交差，人的验收就越不能省。把链接点开、把权限收紧、把结果放回真实环境里跑，这些笨动作会重新成为智能协作的核心。',
    scene: '「它说网页已经修好了。」「把链接发我。」「……它只是把 URL 改成了正确答案，馆子还没关。」',
    cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
    editorial: `## 今日主理人寄语

在多智能体代理开始彼此传话、自闭环交差的时代，人类最重要的动作不再是继续盲目踩油门，而是点开链接去较真验收。

不论是费马大定理展现出的机器级形式化自证，还是海外 TikTok 漫剧团队 4 小时走完分镜剪辑的工业化流水线，都在向我们昭示同一个真理：**代理越会交差，人的审美验收就越不能省；把故事内核想透、把价值闭环跑通，这些笨功夫才是智能协作时代最深的护城河。**

愿今天的精选一手资讯，能成为你敲下第一行代码、写下第一个分镜剧本的灵感起点。
`,
    customItems: CUSTOM_ITEMS_05,
    ianFile: 'scripts/valid-ian-05.json',
  },
  {
    date: '2026-09-06',
    title: '9 月 6 日 · 自动化编排与情绪引爆点：从调参控件到短剧连环钩子',
    epigraph: '当调参变成了自动化的工作流，最值钱的技能重新回到了剧本里：如何让人在前五秒舍不得划走。',
    lead: '今天的信号展现出极强的工业化收敛趋势：前端不再满足于静态组件的堆叠，而是全面转向 Design Token 的多层解耦与自动化测试的深度闭环；而在内容赛道，AI 漫剧彻底跨过了「偶尔惊艳」的抽卡阶段，步入以 LoRA 角色一致性、DaVinci 胶片级调色与短剧连环危机推演为特征的成熟工业期。小团队凭借这套高效工具链，正在以令人惊叹的节奏收割垂直领域的注意力红利。',
    scene: '「这部漫剧的主角怎么三集换了三张脸？」「别催，等今晚多视角 LoRA 跑完，明天她就能拥有永久户口了。」',
    cover: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=1600&auto=format&fit=crop&q=80',
    editorial: `## 今日主理人寄语

在自动化已经能够接管大部分日常琐碎调参的当下，真正能把好产品与烂产品区分开的，永远是对人性情绪的敏锐把控。

不论是编剧在短剧前三秒埋下的连环危机钩子，还是产品经理在空状态界面里递出的温和台阶，底层的思维模型完全相通：**先懂人性的软肋与渴望，再去指挥手里的模型与工具；技术负责把动作做快，故事思维负责把价值做深。**

愿今天的精选一手资讯，能成为你敲下第一行代码、写下第一个分镜剧本的灵感起点。
`,
    customItems: CUSTOM_ITEMS_06,
    ianFile: 'scripts/valid-ian-06.json',
  },
  {
    date: '2026-09-07',
    title: '9 月 7 日 · 微型车间与叙事裂变：小工具收走日常，好故事收割注意力',
    epigraph: '当出图和写代码变得愈发廉价，整个世界最硬核的手艺重新归拢到两件事上：造出不坏的小车间，讲出扎心的好故事。',
    lead: '今天的全网动态呈现出极为鲜明的两极分化与交融：在技术底座上，模型开始具备多参考图连续视频生成、超级对齐与计算机自主控制的硬核能力，一人开发者凭借 Supabase 与无服务架构就能维系长达数年的 0 故障现金流小车间；而在内容与商业转化端，AI 漫剧彻底摆脱粗制滥造，开始在文学台本翻译、微弱呼吸声声效与至暗时刻戏剧节拍上精雕细琢。两股力量汇聚在一起，正在为小团队打开前所未有的广阔天地。',
    scene: '「出图现在只要两分钱一张，为什么他们还能一集分账上万？」「因为观众付钱买的从来不是像素点，而是那一刻心跳漏掉一拍的痛感。」',
    cover: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
    editorial: `## 今日主理人寄语

时代的车轮滚滚向前，当出图和写代码的边际成本不断趋近于零，整个世界最硬核的手艺重新归拢到两件事上：造出不坏的小车间，讲出扎心的好故事。

不论是多参考图连续视频生成展现出的工业化突破，还是短剧出海中靠微弱喘息声与至暗时刻戏剧节拍引爆全球市场，都在向我们昭示同一个真理：**观众与客户付钱买的从来不是像素点或算力消耗，而是那一刻心跳漏掉一拍的共鸣，以及真正替他解决痛点的踏实感。**

愿今天的精选一手资讯，能成为你敲下第一行代码、写下第一个分镜剧本的灵感起点。
`,
    customItems: CUSTOM_ITEMS_07,
    ianFile: 'scripts/valid-ian-07.json',
  },
];

for (const day of DAYS) {
  const rawIan = JSON.parse(fs.readFileSync(day.ianFile, 'utf8'));
  const finalItems = balanceAndShuffle(rawIan, day.customItems);

  console.log(`Day ${day.date}: Total ${finalItems.length} items (Custom: ${day.customItems.length}, Base: ${rawIan.length})`);

  const frontmatter = {
    date: day.date,
    title: day.title,
    highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：覆盖 AI 资讯、一人公司、产品经理、产品设计、编剧技巧、AI 漫剧、AI 协作、审美提升与产品营销。`,
    draft: false,
    epigraph: day.epigraph,
    lead: day.lead,
    scene: day.scene,
    cover: day.cover,
    items: finalItems,
  };

  const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${day.editorial}
`;

  const targetPath = path.resolve(`./src/content/daily/${day.date}.md`);
  fs.writeFileSync(targetPath, mdContent, 'utf8');
  console.log(`✅ Successfully wrote ${targetPath}`);
}
