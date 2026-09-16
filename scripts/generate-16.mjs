import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_16 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '下载破亿、非洲剧跑出 6000 万播放：短剧出海的下一站是新兴市场',
    note: '字节旗下免费短剧 App PineDrama 下载破亿，非洲背景剧集《10亿奈拉新娘》播放超 6000 万。中国工业化爽剧配方加速在拉美与非洲下沉市场跑通。',
    so_what: '短剧出海重心正从单一欧美付费市场向高留存新兴市场分化；欧美收利润、新兴市场做大用户池的双轮驱动已成主流。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-16.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'PineDrama 下载量突破 1 亿：免费模式在海外短剧市场撕开大缺口',
    note: '腾讯新闻权威报道：字节旗下 PineDrama 日活破 700 万，凭借前期全免策略打破传统 IAP 买量垄断，广告支持模式（IAA）时长占比飙升至 83%。',
    so_what: '免费模式正在吞噬传统高买量微短剧的生存空间；创作者必须拥抱广告变现与高频复访机制，降低用户尝鲜摩擦力。',
    source: 'news.qq.com',
    url: 'https://news.qq.com/rain/a/20260914A0BU1A00',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '界面新闻：海外微短剧上半年下载破 14 亿次，IAA 免费广告模式增速达 150%',
    note: '行业大盘全景透视：全球月活冲破 2.58 亿，内购达 12.7 亿美元。印度、印尼与巴西贡献超七成下载，免费广告变现增速远超内购。',
    so_what: '宏观数据印证了区域分化的结构性机会；根据不同国家购买力精准匹配“内购付费”或“广告激励”，是精细化运营的关键。',
    source: 'jiemian.com',
    url: 'https://www.jiemian.com/article/15076957.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok Minis 闭环成型：短剧“即点即看”，上半年站内分账达 8200 万美元',
    note: '拆解站内小程序免跳端生态：用户在短视频推荐流中一键直达完整剧集，已接入十余家头部机构，AI 互动短剧分账季度环比暴增 280%。',
    so_what: '跳端损耗是短剧最大的转化杀手；拥抱平台原生小程序生态，能将流失率降到最低，充分享受算法推荐红利。',
    source: 'tkfff.cn',
    url: 'https://tkfff.cn/news/373.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '奥斯卡最佳剧本奖深度拆解：高口碑影片的剧作张力与文学底色',
    note: '深度剖析全球顶尖电影剧本的戏剧张力构建：从打破日常平衡的突发危机，到层层递进的情感抉择与人物救赎。',
    so_what: '视听工业再发达，剧本依然是一剧之本；吃透经典好莱坞与欧洲艺术片的情感节拍器，才能构建直击人心的故事弧光。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/781',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '夏衍杯优秀电影剧本征集启示：时代母题与现实主义文学温度',
    note: '梳理国家级剧作大奖的评审导向：鼓励深入时代肌理的真实生活观察，杜绝悬浮狗血套路，扶持兼具商业性与思想深度的原创力量。',
    so_what: '故事的生命力来自对真实人性的体察；把微观个体的真实悲欢与时代脉搏缝合在一起，是所有高分叙事的共通底色。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/805',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '国际电影节剧作风向透视：从奇观崇拜回归角色内在驱动',
    note: '评析近期国际获奖佳作的共同叙事转向：不再沉溺于纯视效轰炸，而是将镜头重新对准角色的道德困境与复杂心理交锋。',
    so_what: '当 AI 能以极低成本批量生成视效奇观，最不可替代的资产变成了深邃的人物心理刻画；做扎根人性深处的耐嚼故事。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/875',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '从严肃文学到戏剧剧本：著名作家谈叙事介质转译实战',
    note: '深度专访小说家跨界戏剧编剧的心得：如何把长篇小说的繁复内心独白，精简提炼为演员可演、镜头可拍的外部戏剧动作。',
    so_what: '戏剧是行动的艺术；学会把看不见的情绪波澜外化为尖锐的戏剧动作与台词交锋，你的剧本才能拥有真正的戏剧性。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/780',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '广告投放这件事，正在变成一条AI流水线',
    note: '广告投放全生命周期 AI 化深度复盘：从受众意图挖掘、动态素材批量生成、到竞价自动出价与归因分析，人工干预被压缩到策略底层。',
    so_what: '流量投放的胜负手从人工操盘技巧转向了“流水线算法模型与数据飞轮”；产品经理必须理解如何搭建端到端自闭环的增长工程系统。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463289.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '你的 10 万播放，为什么换不来 1 个付费客户？',
    note: '直面虚荣指标与商业转化的断层痛点：拆解高播放低转化的症结，剖析公域流量向私域精准付费转化的信任梯度模型。',
    so_what: '流量不等于用户，停留不等于信任；不要沉迷于表层的数字泡沫，以终为始设计清晰的交付路径与购买钩子才是商业闭环本质。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463300.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '“用户行为分析”的标准答案：核心指标与留存漏斗实操',
    note: '系统梳理现代产品用户行为分析框架：从首日关键路径（Aha时刻）、用户流失预警到队列留存分析，提供可直接套用的评估模板。',
    so_what: '数据分析的价值不在于事后画报表，而在于指引下一步的迭代动作；建立敏锐的行为分析看板，才能在纷繁复杂的反馈中抓准主线。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463285.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '当AI文字泛滥成灾，好内容还有救吗？',
    note: '探讨生成式 AI 带来的文字通胀困境：当互联网充斥着平庸的信息垃圾，读者反而对有真实体验、深度见解与鲜明态度的声音产生极高溢价。',
    so_what: '通用内容的贬值正是独家认知升值的催化剂；坚守第一人称的真实实战经验与独到故事叙事，就是对抗算法同质化的最强壁垒。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463282.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
];

function balanceAndShuffle(baseItems, customItems) {
  const allItems = [...customItems, ...baseItems];
  const byCat = {};
  for (const it of allItems) {
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-16.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_16);

console.log(`Day 2026-09-16: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_16.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-16',
  title: '9 月 16 日 · 毫秒级原生流与多智能体链：当工具全面演化为全自动流水线',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Google DeepMind 发布 Gemini 3.8 Live 原生音频实时打断模型、Notion 开放链式子代理协作、OpenRouter 平台 OpenAI 算力消耗量两年半首超对手、字节 PineDrama 破亿下沉市场爆发、达芬奇剪辑 Agent JackAICut 开源。`,
  draft: false,
  epigraph: '当大模型跨越了等待生成的时间缝隙，真正的颠覆不是回答变快了，而是人机交互彻底告别了“等待命令”，进入了全时并行的流水线时代。',
  lead: '今天的技术与商业脉搏正在经历一场关于“延迟与自动化链条”的集中突破：在技术顶层，Google DeepMind 重磅发布 Gemini 3.8 Live 原生音频模型，彻底抹平了传统音频转文字再转语音的中间损耗，实现极低延迟的原生打断与语调感知，对话终于拥有了真正的人类心流；而在开发者与工程侧，Notion 正式开放 Custom Agents 链式调用子代理能力，单体 Agent 正在被“分工明确的数字团队”取代；同时，独立开发者开源了直接生成达芬奇剪辑工程的 JackAICut，把长视频初剪彻底变成了无需人工值守的后端流水线；在内容与流量端，字节旗下 PineDrama 下载量正式破亿，验证了中国工业化爽剧配方在新兴市场势如破竹的降维打击。从毫秒级低延迟推演，到多智能体链式协同，软件工业的底层生产关系正在加速固化。',
  scene: '「现在的剪辑和写代码，为什么感觉程序员和剪辑师都闲下来了？」「因为前台只负责下发目标，后台的子代理链条会自动把素材切片、对齐时间线、跑测试用例并合并代码。人不再是流水线上的工人，而是变成了整条产线的质检员。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 Google 把音频对话做到近乎零延迟的毫秒级原生打断，当 Notion 把工作区 Agent 升级为可彼此派发任务的链式子代理，当国人开发者用开源 Agent 把好莱坞级别的达芬奇剪辑做成自动化管道，一个清晰的信号已经摆在所有人面前：**人机交互正在告别“提问—等待—复制粘贴”的原始手工业阶段，全面进入“流水线系统工程”时代。**

在手工业时代，你比拼的是提示词写得多工整、单次调用有多惊艳；但在流水线时代，决定胜负的是你能不能把复杂的业务目标拆解为可自动纠错、可链式衔接的状态机。字节用 PineDrama 在海外新兴市场狂揽上亿下载也是同样的逻辑——它输出的不是单部剧的灵光一闪，而是中国跑通的工业化叙事配方与分发飞轮。

**不要再把 AI 当成一个需要你伺候的聊天伙伴，把它当成产线上的传输带和机械臂。** 思考你的业务里哪一段可以彻底“无人值守”，把精力留给最不可替代的顶层审美与商业判断。愿今天的 ${finalItems.length} 篇精选资讯，能为你提供最前沿的工业化生产力参考。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-16.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
