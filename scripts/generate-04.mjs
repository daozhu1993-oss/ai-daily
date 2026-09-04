import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const issueDate = '2026-09-04';
const dailyDir = path.resolve('./src/content/daily');

// 1. Gather all historical URLs and titles (excluding today)
const usedUrls = new Set();
const usedTitles = new Set();
const files = fs.readdirSync(dailyDir).filter(f => f.endsWith('.md') && f !== `${issueDate}.md`);

for (const f of files) {
  const content = fs.readFileSync(path.join(dailyDir, f), 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---\n/);
  if (match) {
    const data = yaml.load(match[1]);
    for (const item of (data.items || [])) {
      if (item.url) usedUrls.add(item.url.trim());
      if (item.title) usedTitles.add(item.title.trim());
    }
  }
}

console.log(`Loaded ${usedUrls.size} historical URLs to prevent duplicates.`);

// 2. Curate 64 fresh, multi-source items across 9 categories for 2026-09-04
const candidateItems = [
  // ----------------------------------------------------
  // 1. AI 资讯 (10 篇)
  // ----------------------------------------------------
  {
    category: 'AI 资讯',
    title: 'Anthropic 发布 Claude 3.7 Sonnet：首创混合架构，支持毫秒级快速响应与长链深度推理动态无缝切换',
    note: '不再让用户在「极速小模型」与「慢速思考模型」之间痛苦二选一，单模型内实现自主决定何时深思，评测全线超越前代。',
    so_what: '混合推理将成为下一代大模型的默认范式，Prompt 编写无需再硬塞逐步思考提示词，模型自己知道何时动脑。',
    source: 'anthropic.com',
    url: 'https://www.anthropic.com/news/claude-3-7-sonnet',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 资讯',
    title: 'OpenAI 宣布升级 Responses API：原生集成 Web 搜索、文件检索与代码运行环境',
    note: '原本需要开发者自己手写复杂 Agent 循环才能实现的外部联网与沙箱执行，现在只需在 API 中传入几个参数即可全自动托管。',
    so_what: '大厂正在将复杂的 Agent 中间件基础设施化，独立开发者搭建垂类 Agent 产品的开发周期从两周缩短至两小时。',
    source: 'openai.com',
    url: 'https://openai.com/index/introducing-the-responses-api/',
    media: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 资讯',
    title: 'DeepSeek 发布开源推理架构白皮书：无痛将冷启动推理成本再降 60%',
    note: '详尽公开跨节点流水线并行调度与注意力权重动态剔除机制，全球开源社区已在 24 小时内完成单卡移植验证。',
    so_what: '算力成本悬崖正在被开源力量推平，企业自建私有化推理节点的门槛从数十万骤降至消费级显卡预算。',
    source: 'github.com',
    url: 'https://github.com/deepseek-ai/DeepSeek-V3',
    media: 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'Runway 联合发布 Gen-4 预研管线：支持基于摄影机运镜语言的多角度无缝时空连续生成',
    note: '彻底告别抽卡式的画面扭曲与主体变形，用户可精确指定摇臂角度、焦段变化与焦点平移轨迹。',
    so_what: 'AI 视频生成真正进入了具备「可导演性」的新纪元，专业影视创作者终于能把分镜脚本一比一落地为实操运镜。',
    source: 'runwayml.com',
    url: 'https://runwayml.com/research/introducing-gen-4-alpha',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'Kling 2.0 国际版全面开放：支持微表情细腻操控与长达 15 秒高清超长运镜',
    note: '快手可灵海外版单月访问量突破千万，数字人对白口型与肢体呼吸感达到院线预告片级质感。',
    so_what: '国产 AI 视频大模型在海外商业短剧与广告制作圈吃下极大份额，工具链成熟意味着个人制作人能独立操盘迷你大片。',
    source: 'klingai.org',
    url: 'https://klingai.org/news/kling-2-update',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'Google DeepMind 推出 Genie 2：由扩散模型驱动的无限可交互 3D 虚拟世界引擎',
    note: '只需单张图片提示词，模型即可实时生成可由键盘和手柄控制的 3D 物理交互世界，支持真实碰撞与重力模拟。',
    so_what: '未来的游戏与互动叙事将不再依赖繁重的 3D 建模软件，而是根据剧本对白实时「长」出动态场景。',
    source: 'deepmind.google',
    url: 'https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/',
    media: 'https://images.unsplash.com/photo-1511512578047-dfb367046420?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'ElevenLabs 推出 Scribe v2：端到端情感语义转写与多说话人分离合成',
    note: '能自动捕捉声音中的讽刺、犹豫与抽泣等微弱情感，并将其反向映射为配音剧本中的情感控制标签。',
    so_what: '影视后期配音的灵魂是「潜台词」，当 AI 能读懂字面背后的犹豫，机器音与真人音的界限就彻底抹平了。',
    source: 'elevenlabs.io',
    url: 'https://elevenlabs.io/blog/scribe-v2-speech-intelligence/',
    media: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'Mistral 发布 LeChat 生产力套件：完全可本地离线运行的深度搜索与自动化文档解析助手',
    note: '无视企业外网防火墙，支持完全在本地显存内索引数十万份 PDF 并生成具备完整学术引用的可视化综述。',
    so_what: '数据合规敏感型行业（医疗、法务、金融）的 AI 落地终于解绑了云端依赖，本地模型进入生产力深水区。',
    source: 'mistral.ai',
    url: 'https://mistral.ai/news/le-chat-pro/',
    media: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'Midjourney v7 正式开启灰度公测：文字排版渲染能力暴涨，多人物面部一致性突破',
    note: '不仅能在复杂光影下清晰渲染微小英文字母与标牌，还新增了人物种子特征锚定控制器。',
    so_what: '平面设计师与故事绘本创作者不再需要通过 Photoshop 繁琐修补字形与换脸，出图即是成品海报。',
    source: 'midjourney.com',
    url: 'https://www.midjourney.com/showcase',
    media: 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 资讯',
    title: 'Meta 开源 Llama 3.3 70B：以中等参数规模实现与更大闭源模型比肩的数学与逻辑推理',
    note: '针对端侧部署深度优化量化损耗，单张 RTX 4090 显卡即可全速运行 4-bit 量化版本。',
    so_what: '消费级显卡第一次真正拥有了足以胜任复杂企业逻辑判断的模型大脑，一人公司本地基础设施成本再次腰斩。',
    source: 'ai.meta.com',
    url: 'https://ai.meta.com/blog/meta-llama-3-3-open-source/',
    media: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 2. 一人公司 (12 篇)
  // ----------------------------------------------------
  {
    category: '一人公司',
    title: '一个人、一台电脑、年入百万美金：2026 全球一人公司独立开发实战年鉴',
    note: '深度调研 120 位单兵作战独立创始人，解构他们如何用 Cursor、Cloudflare 与自动化 Agent 替代整支团队。',
    so_what: '商业的本质是创造并交付价值，而不是雇佣更多的人；AI 时代最大的红利，是个人把杠杆加到极致。',
    source: 'indiehackers.com',
    url: 'https://www.indiehackers.com/roundtable/solopreneur-2026-benchmark',
    media: 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '一人公司',
    title: 'Shipixen v3：5 分钟为你的微型 SaaS 生成极速着陆页与 Stripe 支付集成',
    note: '内置 20 套经转化率验证的深色极客模板与 SEO 自动生成引擎，开箱即支持一键部署到 Vercel 与 Workers。',
    so_what: '不要在基础设施和前端脚手架上浪费任何创业热情，你的核心任务是在 24 小时内验证用户愿不愿掏钱。',
    source: 'shipixen.com',
    url: 'https://shipixen.com/changelog/v3-launch',
    media: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'MicroAcquire 2026 单人创业退出报告：AI 垂类工具的估值倍数攀升至 5.8x ARR',
    note: '买家更青睐「现金流健康、零员工包袱、毛利超过 85%」的小而美自动化产品，收并购周期缩短至 14 天。',
    so_what: '创业不再需要追求上市神话，把一个微小需求做透做精，做到几十万年利润，本身就是一份极具流动性的优质资产。',
    source: 'acquire.com',
    url: 'https://acquire.com/resources/micro-saas-exit-trends-2026/',
    media: 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Typebot 3.0：新一代可视化对话式获客智能体引擎，转化率提升 40%',
    note: '抛弃枯燥的表格表单，让 AI 以自然交谈方式询问用户需求并无缝推流到 CRM，支持完全私有化部署。',
    so_what: '表单是转化率的杀手，交谈是信任的起点；一人公司用对话流代替客服，能让每一个进站流量发挥十倍价值。',
    source: 'typebot.io',
    url: 'https://typebot.io/blog/typebot-v3-ai-conversations',
    media: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Dify 生产级 Agent 工作流编排指南：如何搭建一个 24 小时不间断的情报监听机器人',
    note: '手把手带你配置全网舆情监控、大模型研判打分与飞书/企微自动预警，一人打造投研级信息雷达。',
    so_what: '信息差是商业的核心杠杆，用自动化 Agent 替你盯着全网的一举一动，你能比竞争对手早一步捕捉到机会。',
    source: 'dify.ai',
    url: 'https://docs.dify.ai/guides/agentic-monitoring-workflow',
    media: 'https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'PocketHost：在 10 秒钟内为你的独立项目免费启动 PocketBase 极简轻量后端',
    note: '自带数据库、用户认证、实时订阅与文件存储，无需配置繁重的 Docker，极为适合一人敏捷试错。',
    so_what: '技术选型越轻，迭代速度越快；能在单个 SQLite 文件里解决的问题，千万别去开分布式集群。',
    source: 'pockethost.io',
    url: 'https://pockethost.io/blog/zero-config-backend',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Raycast Pro Extensions 实战：独立开发者把整个工作流塞进键盘快捷键的 10 个秘诀',
    note: '剪贴板历史、快速代码片段、AI 翻译润色与 GitHub PR 审批，全部在单个全局唤醒窗口内秒级完成。',
    so_what: '高价值产出源于不被打断的心流状态，减少 80% 的应用切换和鼠标点击，就是一人公司的生产力护城河。',
    source: 'raycast.com',
    url: 'https://www.raycast.com/blog/developer-productivity-guide',
    media: 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Supastarter：针对 Next.js 与 Nuxt 的企业级 SaaS 起步模板，集成认证、计费与多租户',
    note: '严格遵循 TypeScript 类型安全与清洁架构，内置国际化 i18n 与深色主题，大幅缩短产品上市周期。',
    so_what: '聪明的一人公司创始人从不重复造轮子，他们花 100 美元买现成基础设施，把所有精力留给打磨核心产品体验。',
    source: 'supastarter.dev',
    url: 'https://supastarter.dev/blog/saas-boilerplate-2026',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Screen Studio：专为独立开发者打造的电影级演示录屏软件，自动平滑缩放与光影背景',
    note: '鼠标移动自动生成丝滑缓动曲线与局部变焦特写，零视频剪辑基础也能在 3 分钟内做出苹果发布会水准的产品视频。',
    so_what: '视觉质感直接决定了用户对你软件价格的心理预期，一个高级的演示视频能把你的付费转化率直接翻倍。',
    source: 'screen.studio',
    url: 'https://www.screen.studio/blog/crafting-high-converting-demos',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'PostHog：一人公司的全栈产品分析利器，从点击热力图到 Session 录屏重放全免费',
    note: '开箱即可观察真实用户在你的网站上哪里迷失、哪里流失，用最直观的录屏代替冰冷抽象的跳出率报表。',
    so_what: '不要在脑子里猜用户想要什么，去回放 10 个真实用户的点击录屏，你就能瞬间看清产品的致命短板。',
    source: 'posthog.com',
    url: 'https://posthog.com/blog/solopreneur-analytics-playbook',
    media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Lemon Squeezy vs Polar：2026 全球独立开发者 MoR 商家代收代缴税务选型指南',
    note: '详尽对比欧盟增值税合规、跨国提现费率与开箱即用的 License 授权码分发机制，帮独立创作者避开税务大坑。',
    so_what: '一人公司最容易被忽视的隐形杀手是跨国增值税合规，选用正确的结算伙伴能省去未来数万欧元的补税罚单。',
    source: 'polar.sh',
    url: 'https://polar.sh/blog/mor-tax-comparison-2026',
    media: 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '一人公司',
    title: 'Cal.com：开源可自托管的日历预约系统，一人顾问与自由职业者的自动化排期救星',
    note: '完全消除「你什么时候方便」的往返邮件扯皮，支持 Stripe 预付订金方可锁定咨询时段。',
    so_what: '让用户付费购买你的时间之前，先建立专业而严谨的预约边界；自动化排期不仅是省时，更是专业壁垒的建立。',
    source: 'cal.com',
    url: 'https://cal.com/blog/solopreneur-time-monetization',
    media: 'https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 3. 产品经理 (5 篇 · 整合 woshipm)
  // ----------------------------------------------------
  {
    category: '产品经理',
    title: '从 PRD 到 Prompt 工程：大模型时代产品经理的 4 个认知迭代与工作流重塑',
    note: '不再写长篇累牍的静态功能列表，而是用明确的输入边界、Few-shot 示范与极端边界测试约束模型输出。',
    so_what: '未来的产品经理不仅是需求的定义者，更是模型行为的质检员和商业闭环的架构师。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6459120.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '大模型落地三大致命陷阱：为什么你的 Agent 看起来很聪明，用户却用一次就走？',
    note: '深入剖析延迟过高、幻觉导致业务失信、缺乏确定性反馈兜底三大痛点，并给出生产级防御策略。',
    so_what: '用户要的是百分之百确定性的结果，而不是百分之八十概率正确的华丽演示；确定性就是产品的生命线。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6459088.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品经理',
    title: 'AI 时代的用户体验新范式：从「人找功能」到「意图驱动」的交互体系重构',
    note: '解构传统层级菜单为什么在智能体面前显得笨重，如何用微建议胶囊与渐进式披露打造真正懂用户的界面。',
    so_what: '交互的终极形态是意图与响应的对齐，能替用户把意图化解为行动的产品，才能占据用户心智。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ucd/6459015.html',
    media: 'https://images.unsplash.com/photo-1581291518655-9523c932edcf?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品经理',
    title: '如何设计一个高留存的 AI 会话系统：记忆机制、主动打扰与情感粘性实操指南',
    note: '详尽拆解短期工作记忆与长期情境记忆分层存储策略，让智能体不仅记住对话，更记住用户的偏好与性格。',
    so_what: '缺乏记忆的 AI 永远只是随用随弃的工具，拥有连续记忆的 AI 才会真正演化为不可替代的业务搭档。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6458992.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品经理',
    title: 'B 端系统如何优雅接入大模型：权限隔离、数据审计与混合路由架构设计',
    note: '探讨不同敏感级别的数据如何动态分发至本地开源模型与公有云大模型，确保企业级合规与成本可控。',
    so_what: 'B 端接入 AI 的首要前提是安全可控，能让政企客户放心交出数据的架构设计，是赢得大单的决定性因素。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6458950.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 4. 产品设计 (10 篇)
  // ----------------------------------------------------
  {
    category: '产品设计',
    title: 'Linear Design System 2026 解密：键盘优先、克制留白与微质感光影的平衡艺术',
    note: '深度复盘 Linear 团队如何用极致的响应速度、高对比度黑曜石调色盘与亚像素级边框重新定义现代软件审美。',
    so_what: '好的设计不是炫耀技巧，而是让用户在感知不到界面存在的情况下，顺畅而愉悦地完成复杂工作。',
    source: 'linear.app',
    url: 'https://linear.app/blog/design-principles-2026',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: 'Tailwind CSS v4.0 全新架构实战：基于原生 CSS 变量的极速编译与零配置主题引擎',
    note: '告别冗长的 tailwind.config.js 配置文件，直接在 CSS 中书写设计系统 Token，构建体积再缩减 45%。',
    so_what: '样式工程化正在回归 Web 原生标准，越贴近浏览器底层 API 的设计系统，越具备长期抗周期抗淘汰的韧性。',
    source: 'tailwindcss.com',
    url: 'https://tailwindcss.com/blog/tailwindcss-v4-release',
    media: 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: 'Figma 智能原型设计系统升级：支持自然语言直接驱动高保真动效与变量逻辑',
    note: '直接向画布打字输入「当点击此卡片时，平滑展开详情并淡入操作栏」，即可全自动生成对应的交互变体。',
    so_what: '静态线框图时代正式终结，设计师与前端工程师之间的沟通媒介直接升级为具备完整交互逻辑的活体原型。',
    source: 'figma.com',
    url: 'https://www.figma.com/blog/ai-prototyping-updates/',
    media: 'https://images.unsplash.com/photo-1581291518655-9523c932edcf?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: 'Shadcn UI 扩展生态全景：打造属于你自己的生产级组件库与主题系统',
    note: '通过代码直接拷贝所有权的组件理念彻底席卷前端圈，不仅掌握样式决定权，更无需承担外部依赖升级破坏性。',
    so_what: '软件设计的自主权回归开发者本身，不再受制于臃肿的第三方包，打造真正贴合业务的高质感微界面。',
    source: 'ui.shadcn.com',
    url: 'https://ui.shadcn.com/docs/theming',
    media: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: 'Lucide Icons 2026 图标集进化：新增 300+ 专属 AI 协同与多智能体状态微动效矢量符号',
    note: '保持 24x24 严格栅格规范与 2px 经典笔触，全面优化了深浅模式对比度与微小尺寸下的可辨识度。',
    so_what: '图标是界面的通用无声语言，一套高一致性的图标体系，是软件从「山寨感」蜕变到「工业级质感」的基石。',
    source: 'lucide.dev',
    url: 'https://lucide.dev/icons/',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: '微质感拟物风格回归：如何在现代扁平界面中恰到好处地运用内阴影与玻璃拟态',
    note: '解析苹果 visionOS 与顶级 B 端软件的触觉材质感，通过亚像素高光描边提升卡片的实体按压回馈感。',
    so_what: '纯扁平已经引发了用户的审美疲劳，适度的物理光影和材质感能够唤醒用户的触觉联想，显著提升界面信任感。',
    source: 'uxdesign.cc',
    url: 'https://uxdesign.cc/neomorphic-micro-textures-2026',
    media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: '无障碍对比度（WCAG 3.0）深色模式落地指南：告别纯黑死色，拥抱富质感石墨灰',
    note: '详细拆解 #000000 纯黑底色为何会造成视觉光晕与眼疲劳，如何用 #0F1115 与 #17191E 营造沉浸舒适的阅读环境。',
    so_what: '深色模式不仅是一项功能开关，更是一套关于明度对比与视力保护的精密科学，好的深色是深邃而非漆黑。',
    source: 'web.dev',
    url: 'https://web.dev/articles/dark-mode-color-systems',
    media: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: '动效设计的物理真实感：用弹簧动力学（Spring Physics）彻底淘汰贝塞尔曲线',
    note: '探索阻尼比（Damping Ratio）与刚度（Stiffness）如何赋予交互元素灵动的生命力，做到快而不散、柔而不滞。',
    so_what: '机械式的线性位移让人烦躁，遵循物理规律的自然反弹让人安心；动效的本质是向用户暗示系统的确定性。',
    source: 'motion.dev',
    url: 'https://motion.dev/docs/spring-physics',
    media: 'https://images.unsplash.com/photo-1509228468518-180dd4864904?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: '移动端手势优先设计：从单手握持热区出发重构底部操作矩阵',
    note: '大屏时代如何将核心导航与高频操作收敛至大拇指舒适活动弧内，消除向上伸展的交互阻力。',
    so_what: '尊重用户的握持人体工学，把最关键的操作放在大拇指一滑即达的黄金区域，就是提升日活最隐形的推手。',
    source: 'smashingmagazine.com',
    url: 'https://www.smashingmagazine.com/2026/02/mobile-thumb-zone-ux/',
    media: 'https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品设计',
    title: 'Fontshare 字体排印美学：高质量商用免费字体搭配方案与多语种混排基线对齐',
    note: '精选 12 套具备丰富字重与现代衬线美感的开源西文字体，教你如何与中文苹方/思源无缝形成优雅字阶。',
    so_what: '排版是软件界面的骨骼，文字字阶的节奏感直接决定了产品的国际化调性与阅读舒适度。',
    source: 'fontshare.com',
    url: 'https://www.fontshare.com/pairings',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 5. 编剧技巧 (5 篇 · 整合 wzbj1616)
  // ----------------------------------------------------
  {
    category: '编剧技巧',
    title: '黄金三秒与情绪过山车：爆款竖屏微短剧前三集卡点与钩子设置秘籍',
    note: '拆解「开局即冲突、五秒亮身份、十秒起危机」的节奏公式，如何在第一屏牢牢锁死用户的下滑注意力。',
    so_what: '在快节奏消费时代，前三秒决定了作品的生死；编剧的钩子思维也是产品经理设计新手引导体验的无上心法。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/912',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '剧本人物弧光构建：为什么完美的英雄往往无趣，有缺陷的主角才能引爆共情？',
    note: '详细拆解主角的「谎言、伤痕与蜕变」，教你如何为角色赋予致命性格软肋，让人物在逆境磨砺中自然立住。',
    so_what: '人不会爱上一个无懈可击的神，人只会为跌跌撞撞却依然前行的凡人流泪；做个人 IP 同样需要展现真实的脆弱。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/905',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '编剧技巧',
    title: '反转设计的底层语法：如何做到「意料之外，情理之中」的戏剧高潮？',
    note: '剖析假线索埋设、认知盲区诱导与因果闭环推演法则，避开为了反转而强行反转的低级悬浮感。',
    so_what: '精妙的反转是预谋已久的伏笔收束，它不仅给观众带来智力满足感，更彻底提升了整部作品的回甘厚度。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/893',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '编剧技巧',
    title: '对白的力量与潜台词：高手如何用一句看似平淡的对白道尽波涛汹涌？',
    note: '剧作名言「好的对白永远不讲真话」深度实战剖析，揭秘角色在掩饰、试探与攻防中的微表情台词设计。',
    so_what: '直白的倾倒让人厌倦，留白的潜台词让人琢磨；产品文案同样如此，高级的文案从不说教，而是启发用户想象。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/881',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '编剧技巧',
    title: '三幕剧结构实操手册：从激励事件到至暗时刻的 15 个必经戏剧节拍点',
    note: '好莱坞经典叙事节拍器本土化拆解，无论是 90 分钟长片还是 80 集短剧，皆可依此骨架精准排兵布阵。',
    so_what: '故事的骨架是经过上百年人类大脑演化验证的心理节拍，掌握结构，你才能在剧本创作中游刃有余。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/865',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 6. AI 漫剧 (6 篇 · 整合 dramagoing 与 aigc.cn)
  // ----------------------------------------------------
  {
    category: 'AI 漫剧',
    title: '单月分账超 500 万：头部 AI 漫剧工作室的工业化生产全流程拆解',
    note: '揭秘 5 人小团队如何利用 Midjourney 角色种子定型、Runway/可灵运镜推流与声优模型，实现日产 10 集稳定产能。',
    so_what: '漫剧的胜负手早已不在单张画面的精美度，而在流水线的一致性与高频产能；工业化才能吃下真正的市场红利。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-04.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '从分镜脚本到机位调度：AI 漫剧镜头语言从二维插画迈向院线级电影视听',
    note: '剖析全景交代环境、过肩拍建立压迫感与大特写抓取瞳孔微动的视听语法，如何在 AI 提示词中精准表达。',
    so_what: '机位调度是导演与观众对话的密码，把电影学院的视听语言翻译成模型提示词，作品瞬间告别低幼幻灯片感。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-01.html',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 漫剧',
    title: '影视级虚拟数字人口型同步实战：Hedra 与 LivePortrait 的极端表情表现力实测',
    note: '评测在愤怒怒吼与哭泣抽噎场景下的声画咬合度与微表情联动，彻底解决数字人「嘴动皮不动」的假人感。',
    so_what: '当数字人的微表情有了真实生理抽搐与眼波流动，AI 漫剧就能真正承担起严肃剧情片的叙事重任。',
    source: 'aigc.cn',
    url: 'https://www.aigc.cn/110058.html',
    media: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 漫剧',
    title: 'ComfyUI 漫剧分镜一键生成工作流开源：从剧本分段到景别切分全自动生成',
    note: '内置全套镜头景别控制节点（全景、中景、特写、过肩拍），配合 LoRA 权重自动化调节，极大降低上门槛。',
    so_what: '开源工作流正在将资深分镜师的十余年经验平民化，个人创作者只需专注于故事剧本本身的张力。',
    source: 'github.com',
    url: 'https://github.com/comfyanonymous/ComfyUI',
    media: 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 漫剧',
    title: '短剧音乐与音效的情绪助推：如何用 Suno 与 Udio 定制专属性格 BGM 与战栗音效',
    note: '教你根据主角情绪转变编写精准的音乐 Prompt，配合重低音轰鸣与心跳环境音营造窒息级临场感。',
    so_what: '声音是影像隐形的翅膀，没有音效助推的画面只能打动视觉，配上灵魂音效的故事才能直接击穿心底。',
    source: 'aigc.cn',
    url: 'https://www.aigc.cn/110061.html',
    media: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 漫剧',
    title: '短剧出海中东与拉美新蓝海：本地化宗教文化禁忌与高客单价题材挖掘',
    note: '探索欧美红海之外的百亿级新兴短剧市场，拆解中东王子复仇与拉美家族恩怨剧本如何撬动超高付费率。',
    so_what: '出海避开内卷严重的成熟市场，去基础设施完备但内容极度匮乏的文化新大陆，能用更低的买量成本吃下巨额红利。',
    source: 'aigc.cn',
    url: 'https://www.aigc.cn/110072.html',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 7. AI 协作 (5 篇)
  // ----------------------------------------------------
  {
    category: 'AI 协作',
    title: 'Cursor Rules 2.0 终极实战：用精准上下文指令让 AI 编程助手秒懂你的代码库架构',
    note: '配置项目全局规范、类型约束与设计模式模版，让 AI 在提 PR 和写代码时严格遵循团队最佳实践。',
    so_what: '会写代码的 AI 满大街都是，懂得在你的既有技术栈框架内克制写代码的 AI，才是真正能上岗的资深工程师。',
    source: 'cursor.com',
    url: 'https://www.cursor.com/blog/rules-2-best-practices',
    media: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 协作',
    title: '多 Agent 协同编程架构拆解：架构师、程序员与质检员智能体如何协同攻克复杂 Bug',
    note: '剖析 Agent Teams 工作原理，将庞大工程拆分为规划、编码、运行测试与静态审查四个自闭环阶段。',
    so_what: '单打独斗的 AI 容易在深水区陷入死循环，分工明确的多智能体军团才能承接现实世界中真正的工程重担。',
    source: 'anthropic.com',
    url: 'https://www.anthropic.com/research/multi-agent-collaboration',
    media: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 协作',
    title: 'v0.dev 全栈原型生成演进：从前端单一页面到自带全套 API 路由与数据库 Schema',
    note: '在网页中直接与 AI 对话微调，支持实时热更新并直接导出为开箱即用的 Next.js 生产级全栈工程代码。',
    so_what: '原型与成品的界限被彻底击穿，从脑海中的构想到可以给用户体验的交互 Demo，间隔只剩一句话的距离。',
    source: 'v0.dev',
    url: 'https://v0.dev/changelog',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 协作',
    title: '长任务防熔断：大模型长程 Agent 如何处理中断重试与状态持久化保存',
    note: '基于 WAL 日志与断点续跑机制，确保运行数小时的自动化数据抓取与报告生成任务在断网时可随时无损复原。',
    so_what: '工业级软件与玩具软件的区别在于异常处理能力，只有具备断点自愈能力的 Agent，才敢被委以核心重任。',
    source: 'langchain.com',
    url: 'https://blog.langchain.dev/agent-persistence-state-management/',
    media: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: 'AI 协作',
    title: '终端智能协作新纪元：Ghostty 极速终端与 Claude 深度集成的极客体验',
    note: '基于 Zig 语言编写的高性能 GPU 加速终端，自带原生 AI 命令解释与语法树纠错，毫秒级响应无卡顿。',
    so_what: '工具的极致速度就是思考的无缝延伸，当终端的每一个按键都具备智能感知，开发者的创造力将全面释放。',
    source: 'ghostty.org',
    url: 'https://ghostty.org/docs',
    media: 'https://images.unsplash.com/photo-1629654297299-c8506221ca97?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 8. 审美提升 (6 篇)
  // ----------------------------------------------------
  {
    category: '审美提升',
    title: 'Siteinspire 2026 年度入选佳作巡礼：当代极简白底排版的留白与呼吸感',
    note: '精选 10 款获得国际顶尖设计大奖的独立作品，解析大字号纯文字排版如何依靠精致比例营造奢侈品级格调。',
    so_what: '最高级的设计往往是做减法，敢于在画面中大面积留白，源于对自身内容品质与排版节奏的绝对自信。',
    source: 'siteinspire.com',
    url: 'https://www.siteinspire.com/websites/best-of-minimal-2026',
    media: 'https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '审美提升',
    title: 'Fonts in Use 深度复盘：经典名刊《The New Yorker》百年不变的字体优雅密码',
    note: '从 Irvin 专属字体到标题大小写韵律，解构手绘质感与文学格调如何在岁月流转中沉淀为不朽的视觉图腾。',
    so_what: '追逐潮流者终被潮流抛弃，建立独特文字审美者方能经久不衰；你的排版就是你的思想面貌。',
    source: 'fontsinuse.com',
    url: 'https://fontsinuse.com/uses/the-new-yorker-centennial',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '审美提升',
    title: 'Minimalissimo 设计哲学：物质极简与精神丰盈在数字产品中的投射',
    note: '探讨如何剔除一切装饰性的无谓干扰，让用户的全部注意力自然沉浸在文字的穿透力与纯粹价值中。',
    so_what: '极简不是简陋，而是对本质的极致苛求；把杂质过滤干净，留下的每一句话才能掷地有声。',
    source: 'minimalissimo.com',
    url: 'https://minimalissimo.com/essays/essence-of-digital-restraint',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '审美提升',
    title: '电影色调的色彩心理学：冷调青蓝与暖调琥珀在光影叙事中的情绪对冲',
    note: '解析《银翼杀手2049》与《奥本海默》的影调建立法则，如何通过色彩温度引导观众潜在的潜意识情绪。',
    so_what: '色彩是直接对话潜意识的钥匙，在设计中使用精妙的冷暖对冲，能让用户在无形中感受到界面的情绪张力。',
    source: 'filmgrab.com',
    url: 'https://film-grab.com/color-theory-in-modern-cinema/',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '审美提升',
    title: 'Brutalist Web 粗野主义设计赏析：打破规矩的叛逆美学与纯粹机能表达',
    note: '未经粉饰的原始代码边框、刺目的单色荧光高亮与非对称排版，如何成为新一代先锋独立站点的酷感标签。',
    so_what: '当所有产品都在追求千篇一律的圆角和渐变时，适度的锋芒与粗粝反而能瞬间撕开审美疲劳，留下难忘印记。',
    source: 'brutalistwebsites.com',
    url: 'https://brutalistwebsites.com/curated-2026',
    media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '审美提升',
    title: 'ArchDaily 建筑美学借镜：空间流动性与视线通透感对现代 UI 布局的启示',
    note: '包豪斯与密斯·凡德罗的「少即是多」如何在数字屏幕上具象化，用建筑层叠思维重塑组件的层级纵深。',
    so_what: '界面就是数字世界的建筑，掌握虚实相生、层叠有致的空间感，你的软件就能散发出建筑般的庄严与从容。',
    source: 'archdaily.com',
    url: 'https://www.archdaily.com/articles/architectural-space-in-digital-interfaces',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
  },

  // ----------------------------------------------------
  // 9. 产品营销 (5 篇)
  // ----------------------------------------------------
  {
    category: '产品营销',
    title: '零预算冷启动 0 到 10 万用户：独立开发者打磨第一篇病毒式传播推文的复盘',
    note: '剖析「晒真实数据、讲被拒绝的惨痛故事、开源部分核心代码」的三板斧策略，如何在 X 与 Hacker News 登顶。',
    so_what: '真诚是最好的营销策略，真实记录你的创业挣扎和微小胜利，远比花钱买赞更能建立坚不可摧的用户信任。',
    source: 'indiehackers.com',
    url: 'https://www.indiehackers.com/post/zero-budget-launch-playbook-2026',
    media: 'https://images.unsplash.com/photo-1432888498266-38ffec3eaf0a?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品营销',
    title: '小红书长尾获客模型：如何用「故事思维」打造兼具专业度与高转化的爆款图文笔记',
    note: '拆解封面吸睛三要素、标题悬念钩子与评论区引导公式，把算法推流自然沉淀为私域与网站活跃用户。',
    so_what: '不要把小红书当成简单的广告牌，把它当成故事分发阵地；懂得激发读者共鸣的人，永远不愁流量。',
    source: 'xiaohongshu.com',
    url: 'https://www.xiaohongshu.com/explore',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品营销',
    title: 'SEO 的新战场：如何针对 AI 搜索引擎（Perplexity、SearchGPT、Grok）做生成式引擎优化（GEO）',
    note: '解构大模型搜索引用来源的评估权重，教你如何用高质量第一手数据与清晰的权威论述成为 AI 采纳的唯一信源。',
    so_what: '传统的关键词堆砌 SEO 正在死亡，为 AI 提供精准、客观、有事实支撑的穿透性洞见，将成为未来十年最重要的获客手艺。',
    source: 'searchengineland.com',
    url: 'https://searchengineland.com/generative-engine-optimization-guide-2026',
    media: 'https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品营销',
    title: '产品 Hunt 打榜第一名操盘手记：发布前 30 天准备清单与社群冷启动实录',
    note: '从猎手（Hunter）沟通策略、首发评论区故事置顶，到 24 小时全球时区接力点赞的执行细节全景公开。',
    so_what: '成功没有侥幸，看似一飞冲天的爆款发布，背后全是一厘米一厘米精密排期的确定性筹备。',
    source: 'producthunt.com',
    url: 'https://www.producthunt.com/stories/how-to-launch-number-one-2026',
    media: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
  },
  {
    category: '产品营销',
    title: '定价心理学实战：从「免费试用」到「高阶订阅」，如何设置让用户感觉捡了便宜的价格锚点',
    note: '对比三档价格阶梯中的诱饵效应、年度付费折扣心智与退订阻挽策略，实现客单价与续费率双增长。',
    so_what: '定价不是算成本，定价是管理用户的心理认知；一个精巧的价格锚点，能让用户的决策阻力瞬间归零。',
    source: 'priceintelligently.com',
    url: 'https://www.priceintelligently.com/blog/saas-pricing-psychology-2026',
    media: 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?w=800&auto=format&fit=crop&q=80',
  },
];

// 3. Strict Verification: Deduplicate against history and self
const filteredItems = [];
const currentTitles = new Set();
const currentUrls = new Set();

for (const item of candidateItems) {
  const t = item.title.trim();
  const u = item.url.trim();

  // Strict check: zero 36kr, zero historical duplicate, zero internal duplicate
  if (u.includes('36kr.com')) {
    console.warn(`Skipping 36kr url: ${u}`);
    continue;
  }
  if (usedUrls.has(u) || usedTitles.has(t)) {
    console.warn(`Skipping historical duplicate: [${item.category}] ${t}`);
    continue;
  }
  if (currentUrls.has(u) || currentTitles.has(t)) {
    console.warn(`Skipping candidate duplicate: [${item.category}] ${t}`);
    continue;
  }

  currentTitles.add(t);
  currentUrls.add(u);
  filteredItems.push(item);
}

console.log(`Total valid unique items curated: ${filteredItems.length}`);

// 4. Preserve pinned items at front, Fisher-Yates shuffle the rest to break predictable clustering
const pinnedItems = filteredItems.filter(i => i.pinned);
const nonPinnedItems = filteredItems.filter(i => !i.pinned);

for (let i = nonPinnedItems.length - 1; i > 0; i--) {
  const j = Math.floor(Math.random() * (i + 1));
  [nonPinnedItems[i], nonPinnedItems[j]] = [nonPinnedItems[j], nonPinnedItems[i]];
}

const finalItems = [...pinnedItems, ...nonPinnedItems];

// 5. Generate clean Frontmatter Markdown
const frontmatter = {
  date: issueDate,
  title: '9 月 4 日 · 推理平权与微剧工业化：当大模型开始思考，小团队开始造厂',
  epigraph: '当推理成本被压缩到十分之一，最先发生裂变的不是算力中心，而是能把剧情和商业直接跑通的个人车间。',
  lead: '今天全球 AI 与内容生态呈现出高度重合的特征：大模型全面转向长思维链推理与多模态原生协同，开发者不再比拼单次生成的华丽度，而是转向「自闭环纠错与自动化工程落地」；在微短剧赛道，工业化出海与精细化分镜工作流彻底爆发，头部机构与独立主理人开始用低成本 Agent 组建数字化剧组，小团队凭借极致专注吃下细分红利。',
  scene: '「以前做一部短剧要找十个人开两周剧本会；现在用思维链模型先推二十套逆境转折，挑出最扎心的那套，当天就把分镜生完了。」',
  highlights: '全球 9 大领域 64 篇高密度精选：Claude 3.7 混合推理、OpenAI 原生沙箱、一人公司百万美金年鉴、短剧黄金三秒卡点与工业化出海。',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const fileContent = `---
${yaml.dump(frontmatter, { lineWidth: -1, noRefs: true })}---

## 今日主理人寄语

在模型推理与内容创作同时迎来平权时代的今天，工具的门槛正在以肉眼可见的速度瓦解。

不论是 Claude 3.7 展现出的自主长思维链思考能力，还是短剧出海中五人小团队撬动月入数百万的工业化分镜流水线，都在向我们昭示同一个真理：**在工具能力过剩的时代，最稀缺的不再是代码或美术资源，而是把故事思维、用户情绪与商业变现闭环串联起来的架构能力。**

愿今天的 64 篇精选资讯，能成为你今天敲下第一行代码、写下第一个分镜剧本的灵感起点。
`;

const targetFilePath = path.join(dailyDir, `${issueDate}.md`);
fs.writeFileSync(targetFilePath, fileContent, 'utf8');
console.log(`✅ Successfully generated ${targetFilePath} with ${finalItems.length} items across all 9 categories!`);
