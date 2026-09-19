import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const ALL_ITEMS_19 = [
  // 1. AI 资讯 (4)
  {
    category: 'AI 资讯',
    title: 'Anthropic 与 Accenture 达成 20 亿美元安全战略合作：设立“嵌入式评估员”团队',
    note: '双方承诺未来五年各自至少投资 10 亿美元，建立常驻嵌入式红队评估员机制，攻坚企业级大模型安全合规与对齐审计。',
    so_what: '安全不再是写在白皮书里的道德口号，而是真金白银的数十亿商业基建；拥有严密安全合规认证的大模型才能敲开万亿企业核心生产系统的大门。',
    source: 'anthropic.com',
    url: 'https://www.anthropic.com/news/accenture-partnership',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 资讯',
    title: 'OpenAI 呼吁建立国家级强制安全规范，公开支持加州 AI 安全法案',
    note: '主动支持针对前沿模型的独立第三方评估、算力集群监控与防范生物风险法规，表明对齐合规已成为行业前置门槛。',
    so_what: '监管闸门正在加速落下；对 AI 开发者而言，合规成本将迅速固化为头部壁垒，初创项目必须尽早将安全防线前置至架构底层。',
    source: 'openai.com',
    url: 'https://openai.com/index/our-perspective-on-california-ai-safety-bills/',
    media: 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 资讯',
    title: 'DeepMind 联合创始人 Shane Legg 展望 AGI：重申 2028 年达到“最小可用 AGI”有 50% 概率',
    note: '警告行业切勿盲目且轻率地宣布 AGI 到来，指出目前系统在自主推演、长程可靠性与跨物理世界感知上依然存在基础性理论断层。',
    so_what: '避免在短期亢奋中高估应用落地速度，但在长期技术演进上保持敬畏；做扎根当下确定性业务的产品，远胜在虚幻的 AGI 口号中空转。',
    source: 'deepmind.google',
    url: 'https://deepmind.google/discover/blog/introducing-the-deepmind-institute/',
    media: 'https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 资讯',
    title: 'Google 重组 AI 责任部门：将 90 人安全团队独立于 DeepMind',
    note: '破除研究团队“既主导前沿研发又自我审查合规”的双重角色冲突，构建集团级跨产品线的中立安全评估流程。',
    so_what: '组织架构决定产品走向；当顶尖实验室把安全治理做成独立实体，意味着 AI 风险管控已经具备了类似财务审计的一票否决权。',
    source: 'blog.google',
    url: 'https://blog.google/technology/ai/advancing-responsible-ai-governance/',
    media: 'https://images.unsplash.com/photo-1573164713988-8665fc963095?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 2. AI 协作 (4)
  {
    category: 'AI 协作',
    title: 'Cursor 正式发布“Projects”架构：协调智能体调度上千子代理',
    note: '开发者维护长期庞大工程的新范式：Coordinator 智能体在云端自动拆解重构任务并并发分派给上千个子代理，全自动同步规范与测试用例。',
    so_what: '编程范式正式从“逐行敲代码”跃迁为“调度数字工程军团”；工程师的核心竞争力正在从底层语法熟悉度转向高阶系统拆解与意图编排能力。',
    source: 'cursor.com',
    url: 'https://cursor.com/changelog',
    media: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 协作',
    title: 'Linear 发布 9 月更新：推出 Priority Inbox 与自动撰写简报 Agent',
    note: '优先级收件箱智能过滤噪音、提炼阻断型关键卡点，内置 Agent 无需提示词即可根据项目上下文自动生成进度简报。',
    so_what: '好的 AI 不是一个突兀的聊天框，而是无缝融入现有产品心流的隐形润滑剂；把决策信息密度做到极致，是生产力工具永恒的护城河。',
    source: 'linear.app',
    url: 'https://linear.app/changelog/2026-09-16-priority-inbox',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 协作',
    title: 'Mastra：基于 TypeScript 的开源轻量级 Agent 编排框架爆火',
    note: '专为全栈与前端开发者打造的 Agent 开发体系，原生支持工作流状态机、MCP 协议集成与本地全流程可视化调试。',
    so_what: 'Python 不再垄断 AI 开发生态；TS 生态的高速补齐让数百万 Web 全栈开发者能够以极低门槛无缝切入多智能体协同系统的研发。',
    source: 'mastra.ai',
    url: 'https://mastra.ai/docs',
    media: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 协作',
    title: 'Simon Willison 详解本地端侧小模型的受限解码与结构化 JSON 保证',
    note: '深入分析端侧 LLM 在调用外部工具时的结构化输出优化方案：通过语法树约束确保 100% 输出合法字段，消除一半报错中断。',
    so_what: 'Agent 执行链条中最脆弱的就是工具调用的解析失误；底层受限解码的成熟，让边缘端小模型在无网络环境下也能胜任高可靠性任务。',
    source: 'simonwillison.net',
    url: 'https://simonwillison.net/2026/Sep/18/structured-outputs/',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 3. 产品经理 (4)
  {
    category: '产品经理',
    title: '谷歌 Gemini 桌面客户端实测复盘：全局热键常驻与本地屏幕感知的得与失',
    note: '深度评测系统级常驻桌面助手的真实表现：虽具备毫秒级全局屏幕唤醒与意图感知，但在多屏幕切换与复杂应用拦截上依然存在认知断点。',
    so_what: '桌面级常驻入口是巨头的必争之地，但也面临最严苛的用户打扰容忍度；产品经理需要克制设计唤醒频次，让系统只在用户真正卡点时出现。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465532.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '你动嘴，AI干活：产品经理必学的 Vibe Coding 与自然语言编程实操',
    note: '探讨如何通过自然语言对话驱动前端组件与后端数据库的实时联调，用运行中的真实交互原型取代传统数十页死板的 PRD 文档。',
    so_what: '沟通介质的升维直接缩短了产品迭代半衰期；能够用代码级原型直接表达产品构想的产品经理，将对传统仅负责画线框图的同行形成代际压制。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6430061.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '让 AI 做研究很容易，难的是让它承认自己错了：论 Agent 反思机制与自我纠错',
    note: '剖析大模型在自主长程推理中的“证实偏见”——倾向于为最初的错误假设寻找合理借口；详解如何引入红蓝对抗机制设计高容错业务系统。',
    so_what: '不具备批判性质检能力的自动化是危险的放任；产品经理的核心职责是为 Agent 的推演链条设立防呆防偏的硬性审计断点。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465492.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'AI 推荐了你，却用不上你：这家公司靠诊断“AI 搜索引擎截流”斩获 400 万美元融资',
    note: '生成式引擎优化（GEO）商业实战：分析为什么大模型在回答里引用了你的品牌却未能促成跳转，以及如何重新优化结构化数据夺回精准客流。',
    so_what: '传统搜索引擎依靠关键词排名，而 AI 时代依靠“权威语境权重”；尽早布局能被大模型深度理解并主动导流的结构化内容阵地。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6464197.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 4. AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '卡在悬崖边的角色变成了对话框：短剧出海正在裂变出全新互动形态',
    note: '漫剧出海行业观察：短剧正在从单一“上下滑竖屏视频”裂变出互动剧、好莱坞直接拍进 TikTok 的原生 PGC、以及反向孵化长视频的超级 IP。',
    so_what: '渠道抢入口、买量红利退潮后，竞争的杠杆彻底转向形态与题材的差异化；谁能让用户在看完一集后产生互动留存，谁就能守住高 LTV 盘子。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-19.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'Character.ai 上线自制微短剧：悬念处一键拉起角色对话，用户月均停留破 950 分钟',
    note: '颠覆传统流媒体播放逻辑：观众在剧情悬崖处直接与剧中角色实时对谈、追问真相甚至推演平行支线，被动看剧变身为高参与度角色扮演。',
    so_what: '留存时长的终极抓手是用户的“在场感”；把冰冷的单向视听转译为可交互的情感陪伴，是微团队对抗大厂海量买量预算的最强差异化利刃。',
    source: 'cherrybowl.io',
    url: 'https://cherrybowl.io/intelligence/the-cliffhanger-gets-a-chat-window-microdrama-s-five-new-fronts-20260908',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '好莱坞不另建独立 App 了：Mansa 把三档原生黑人短剧直接拍进 TikTok Minis',
    note: '顶尖好莱坞明星 David Oyelowo 旗下影视工作室入局短剧：放弃跳转下载独立 App，直接长在 TikTok 平台原生小程序里做闭环追更与分发。',
    so_what: '平台原生化是短剧分发的确定性终局；借力平台既有的社交分发网络与账号体系，能够把漏斗流失率压缩到极限。',
    source: 'deadline.com',
    url: 'https://deadline.com/2026/09/david-oyelowo-nate-parker-tiktok-microdramas-mansa-studios-1237065179',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'ShortMax 稳居美区娱乐畅销榜第 17 位：2026 海外短剧产业价值预估翻倍至 60-90 亿美元',
    note: '国际发行商在海外应用商店成为常驻居民，全球短剧 App 突破 237 款；市场规模从少数巨头垄断向跨区域混战扩散，增量全面依赖本地化与形态创新。',
    so_what: '蛋糕在迅速做大，但座次在剧烈重排；紧跟本地化题材与广告变现（IAA）混合模型的团队，将在下一轮洗牌中占据主导。',
    source: 'keeppay.net',
    url: 'https://www.keeppay.net/en/blog/short-drama-overseas-2026',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 5. 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '电视剧备案立项风向：从宏大叙事下沉到微观人性的现实主义温度',
    note: '影视主管部门立项导向深度解读：严控悬浮伪现实，鼓励深入市井生活与微观个体情感，用扎实的人物弧光承载时代风貌。',
    so_what: '剧作的穿透力来自对真实人性的慈悲与观察；切口越微小具体，故事的文学厚度与共情力量就越坚韧。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/782',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '重大题材戏剧张力构建：如何在真实历史框架下设计动人的戏剧弧光',
    note: '剖析历史重大题材的戏剧转译之道：如何在既定的历史结局之下，挖掘人物在关键历史转折点上的心理拉扯与道德抉择。',
    so_what: '真实历史是剧作的锚，但角色的内在危机是故事的帆；让宏大叙事回归到“人”的困境，才能打破说教感。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/870',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '电影剧本情节动力学：如何精准设置中点危机（Midpoint）重燃叙事引擎',
    note: '经典戏剧结构核心法则：中点决不是情节停滞的喘息，而是将主角推向不可逆转境地的重大反转，假胜利在此转化为真正的生死考验。',
    so_what: '很多剧本在中段疲软无力，正是因为缺乏有分量的中点危机；在剧作中段果断斩断角色的退路，剧情才能获得第二宇宙速度。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/920',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '行业剧与专业剧本实战：怎样让枯燥的专业知识成为推动人物冲突的利刃',
    note: '专业行业题材剧本实操指南：避免把台词变成说明书，将专业规则的死板与人性的温度对立起来，把技术博弈化作戏剧生死。',
    so_what: '行业细节不是用来炫技的贴纸，而是角色的生存武器；吃透行业的潜规则与道德灰色地带，你的职场剧才能拥有摄人心魄的职业质感。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/925',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 6. 一人公司 (3)
  {
    category: '一人公司',
    title: 'Nomads.com 接入 Flighty：一键导入个人飞行里程与全球旅居足迹',
    note: '数字游民平台巧妙打通成熟飞行记录应用接口，用户上传 CSV 即可瞬间生成精美的常驻国家热力图与个人旅居档案。',
    so_what: '单人开发者不要在通用功能上重新造轮子；善于利用外部现成的数据资产，把精力集中在增强自身社区的独家体验上。',
    source: 'nomads.com',
    url: 'https://nomads.com/destinations',
    media: 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '一人公司',
    title: '37signals 的开源人才飞轮：独立开发者公开修 bug，直接免试获聘入职',
    note: '独立开发者通过为开源项目贡献高质量 PR 与优化动效，在无常规招聘流程的情况下被团队全职录用。',
    so_what: '公开构建与开源贡献是当代创造者最具说服力的通用信用；解决真实世界难题的确定性代码，胜过千言万语的简历包装。',
    source: '37signals.com',
    url: 'https://37signals.com/podcast/',
    media: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '一人公司',
    title: 'Axiom 登顶 Product Hunt：单人团队打造极简数据清洗应用',
    note: '独立开发者打造的表单数据快速清洗工具上线首日登顶前三，主打 3 分钟极速嵌入、0 冗余配置的微型 SaaS 变现闭环。',
    so_what: '小即是美；在巨头争相堆砌大而全功能的时代，专注把一个单点微任务做到丝滑无感，是独立小团队最高效的生存法则。',
    source: 'producthunt.com',
    url: 'https://www.producthunt.com/',
    media: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 7. 产品设计 (3)
  {
    category: '产品设计',
    title: 'Figma 进化为全链路产品决策平台：跳出单纯画图软件工具定位',
    note: '全面整合开发交付、多状态可交互原型与 AI 自动化验收测试，设计稿正在从静态像素交付物升级为活的业务决策树。',
    so_what: '设计工具正在吞噬传统产品经理与前端的边界；未来的设计师不仅负责界面审美，更负责在同一块画布上推演完整的业务状态机。',
    source: 'figma.com',
    url: 'https://www.figma.com/blog/design-systems-ai-era/',
    media: 'https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品设计',
    title: 'Basecamp 5 看板卡片模版上线：Card Table 支持列结构与高频流一键复用',
    note: '引入看板卡片全量模板机制，高频复用的研发迭代、内容排期与审批列表可直接一键打包另存为母版。',
    so_what: '减少每一次启动新项目的认知摩擦；把可复用的业务流沉淀为模板资产，是保持小团队高人效运转的底层设计智慧。',
    source: 'basecamp.com',
    url: 'https://basecamp.com/updates',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品设计',
    title: 'Unicorn Studio 实装泛光色散参数：让光感随距离色移',
    note: '动效工具加入物理色散滑块，光晕边缘从中心白向边缘蓝红非线性自然过渡，实时渲染出具有呼吸感的现代数字胶片质感。',
    so_what: '审美的高级感往往藏在微妙的物理细节里；告别生硬的纯线性渐变，用符合人眼光学直觉的色彩插值赋予界面鲜活的生命力。',
    source: 'unicorn.studio',
    url: 'https://www.unicorn.studio/showcase',
    media: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 8. 审美提升 (3)
  {
    category: '审美提升',
    title: 'RHAD Architects 新斯科舍海景长屋：碳化烧杉板融入玄武岩海岸',
    note: '极简沿海独栋建筑设计典范：整面炭黑烧杉板与玄武岩海岸斜坡浑然一体，巨幅落地悬窗将自然海湾直接框成随天光流转的挂画。',
    so_what: '真正的奢华是对自然的谦卑退让；在数字产品设计中亦是如此，克制的设计体量与恰到好处的留白，更能衬托核心内容的光芒。',
    source: 'dezeen.com',
    url: 'https://www.dezeen.com/',
    media: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '审美提升',
    title: 'Typewolf 2026 秋季排版风向：高对比度衬线体与微型点阵字体的复古回潮',
    note: '观察当代先锋数字产品在排版上的集体审美转向：打破千篇一律的无衬线工业感，借助古典衬线体与复古像素点阵的碰撞表达极客态度。',
    so_what: '字体是品牌的声调与体温；在算法同质化的今天，精心挑选具有独特文学质感的字体排版，是品牌脱离平庸最直接的审美名片。',
    source: 'typewolf.com',
    url: 'https://www.typewolf.com/recommendations',
    media: 'https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '审美提升',
    title: 'Studio Iron 伦敦设计节金工刺青展：将硬质金属与手作皮革纹理重构为空间装置',
    note: '传统手工锁子甲与手工刺青皮革跨界融合，将粗粝的工业重工技艺与人体触觉记忆转化为兼具力量与温度的当代空间艺术。',
    so_what: '审美突破往往发生在不同介质的交界处；善于借用实体工业的质感与手工触觉，能为虚拟数字界面带来震撼的情感重量。',
    source: 'londondesignfestival.com',
    url: 'https://www.londondesignfestival.com/events/studio-iron',
    media: 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 9. 产品营销 (3)
  {
    category: '产品营销',
    title: 'PostHog 开源核心看板控件库：把核心数据分析工具做成最高效的获客诱饵',
    note: '将自用高交互度图表与热图独立开源发布，不设商业防线，直接吸引数以万计的开发者在自有业务中嵌入其分析底座。',
    so_what: '最好的营销不是打广告，而是提供让目标用户爱不释手的生产力武器；开源是开发者生态中最无可争议的信任杠杆。',
    source: 'posthog.com',
    url: 'https://posthog.com/blog/open-source-charts-announcement',
    media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品营销',
    title: 'Build in Public 的情绪价值变现：去“AI味”文案的本质是保留人类不完美的毛边',
    note: '独立开发者文案传播心得：大模型生成的辞藻往往因过于周密工整而显得机械冷漠，保留情绪波澜、真实的挫败与口语思考反而能赢得忠实拥趸。',
    so_what: '完美是冷冰冰的机器属性，而脆弱是真正的人性连接；敢于在公众面前袒露真实的开发波折，是个人 IP 最具感染力的吸铁石。',
    source: 'x.com',
    url: 'https://x.com/',
    media: 'https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品营销',
    title: 'GEO 时代的内容战略：不要写给大模型看不懂的套话，做独家一手行业数据源',
    note: '深度解构生成式引擎时代的内容分发规律：泛泛而谈的陈词滥调会被大模型无情压缩过滤，唯有一手详实的实操数据与独家复盘能被模型作为权威信源引用。',
    so_what: '内容分发的评价标准从点击量转向了“信息熵与引用度”；把每一个案例复盘做成不可替代的行业标杆，才能在大模型时代获得持续长尾流量。',
    source: 'growth.design',
    url: 'https://growth.design/case-studies/duolingo-onboarding',
    media: 'https://images.unsplash.com/photo-1533750516457-a7f992034fec?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
];

function balanceAndShuffle(items) {
  const byCat = {};
  for (const it of items) {
    if (!byCat[it.category]) byCat[it.category] = [];
    byCat[it.category].push(it);
  }

  const categories = Object.keys(byCat).sort((a, b) => {
    const priority = ['AI 资讯', 'AI 漫剧', '产品经理', '编剧技巧', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 协作'];
    return priority.indexOf(a) - priority.indexOf(b);
  });

  const result = [];
  let added = true;
  while (added) {
    added = false;
    for (const cat of categories) {
      if (byCat[cat] && byCat[cat].length > 0) {
        result.push(byCat[cat].shift());
        added = true;
      }
    }
  }
  return result;
}

const finalItems = balanceAndShuffle(ALL_ITEMS_19);

console.log(`Day 2026-09-19: Total ${finalItems.length} items curated.`);

const frontmatter = {
  date: '2026-09-19',
  title: '9 月 19 日 · 互动裂变与安全围栏：当短剧拥有对话框，大模型走向二十亿安全联盟',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Anthropic 与 Accenture 组建 20 亿美元安全战略联盟、Character.ai 开启短剧高潮互动对话框、Cursor Projects 调度上千子代理、Linear 发布 Priority Inbox、短剧出海迎来原生好莱坞 PGC 与 IP 反哺长视频。`,
  draft: false,
  epigraph: '当短剧的悬崖边长出了一个对话框，当企业安全团队把评估员直接嵌入模型核心，AI 与内容的边界正在双向溶解：观众不再是被动的看客，模型也不再是脱缰的黑盒。',
  lead: '今天的科技与数字内容生态正在经历一场深刻的“双向奔赴”：在底层技术与商业基建侧，Anthropic 正式携手 Accenture 达成总额超 20 亿美元的 AI 安全战略合作，首次向外部咨询巨头派驻“嵌入式评估员”设立安全红队，标志着大模型从单纯追求性能参数狂飙，进入了严苛的企业级信任与安全合规周期；而在应用层，Cursor Projects 允许单个协调 Agent 在云端并发调度上千个子代理，完成过去需要数十人研发团队数周才能跑完的大型代码重构；在内容与文娱消费端，短剧出海正在彻底打破“上下滑竖屏视频”的传统定义：Character.ai 把短剧停在剧情反转悬崖处的角色直接变成可即时互动的对话框，用户月均停留超过 950 分钟；好莱坞一线团队放弃独立 App 开发，将原生 PGC 直接拍进 TikTok Minis，同时海外竖屏爆款反向孵化长视频真人秀。从模型底层安全围栏的加固，到内容消费终端的多维互动裂变，人机共创的新物种正在加速繁衍。',
  scene: '「听说你们现在看短剧都不上下划了？」「看完一集卡在男主跳崖处，屏幕直接弹出一个实时对话框，你可以逼问他真相，甚至用文字拉扯出一条全新的隐藏支线。追剧变成了玩互动式剧本杀。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 Anthropic 拿出二十亿美元筑牢前沿模型的安全堤坝，当 Character.ai 把卡在剧情悬念处的主角变成了可以深夜长谈的对话框，一个耐人寻味的信号正在浮出水面：**技术正在从野蛮生长的狂飙期，全面进入与真实人类社会结构“深度咬合”的精细期。**

在过去，我们谈论 AI，往往停留在基座模型又刷了哪个榜单、算力又翻了几倍。但对身处产业一线的创造者而言，真正带来商业回报的从来不是抽象的参数，而是模型如何安全地嵌入企业的业务流程，以及如何为普通用户创造前所未有的情感共鸣。

短剧出海不再只是买量套利的粗放机器，好莱坞 PGC 的入场与互动支线的演进，说明好内容永远在向着更能占据受众注意力的形态进化；软件工程也不再只是敲代码的敲门砖，Cursor 上千子代理的并发协作，让单兵开发者拥有了过去跨国工程兵团的算力杠杆。

**不要在旧范式的废墟里打转，去寻找那些正在生长出新交互形态的裂缝。** 愿今天的 ${finalItems.length} 篇精选资讯，能为你提供最前沿的洞察航标。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-19.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
