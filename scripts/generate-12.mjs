import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_12 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: 'AI 漫剧出海：盘子冲到 6.5 亿，九成团队却还在亏',
    note: '行业大盘高速扩容背后的二八定律残酷显现：低水平量产抽卡导致投放买量成本高企，唯有掌握角色一致性工业管线与特定受众精准定价的团队跑出净利。',
    so_what: '规模的膨胀往往掩盖商业模型的脆弱；别做盲目卷数量的炮灰，把人效与单剧投产比（ROI）卡死在盈利线上才是生存之本。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-12.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '从烧钱买量到能赚钱：ReelShort 破 10 亿，字节搭起「短剧操作系统」',
    note: '头部出海平台商业闭环演化复盘：从单一依靠 Facebook/TikTok 买量单向推流，升级为自建平台订阅留存与多渠道长尾分发并行的成熟生态。',
    so_what: '巨头搭起基础设施后，最稀缺的是高确定性的精品供给；认清平台的生态重心转移，做平台生态里不可替代的优质内容支柱。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-03.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '出海短剧分账战报：$2100万创纪录，AI漫剧逼近真人剧',
    note: '平台官方分账历史数据剖析：AI 生成漫剧在制作周期缩短 70% 的前提下，分成收益与播放留存正全面逼近中低成本实拍真人剧。',
    so_what: '生产力代际差带来的成本优势正在被数据反复验证；尽早把影视制作管线全面转向生成式引擎，才能在存量博弈中抢得身位。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/may-payout.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '短剧出海关键动态速览：MCN考核改革、监管新规与新兴平台崛起',
    note: '梳理海外短剧生态治理规则演进：平台对低质搬运与欺诈性诱导消费加大处罚权重，精品原创与本土化自制团队迎来流量倾斜。',
    so_what: '规则越规范，正规军的优势越明显；不要在违规边缘试探短期红利，扎实做好本地化内容叙事才能获得平台长期扶持。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/weekly-june-4.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '剧本速递|《头脑特工队2》原版剧本与情绪外化技巧',
    note: '深度解构皮克斯动画的原生情绪设定法：如何把抽象的“焦虑”、“尴尬”等青春期心理具象化为性格鲜明的戏剧角色与冲突发动机。',
    so_what: '最高级的情绪共鸣是把内心的隐秘挣扎视觉化；学会将看不见的心智波澜提炼为戏剧动作，你的剧本才能拥有击穿人心的魔力。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/772',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '《F1：极速狂飙》（2025）—— 编剧视角教育解析',
    note: '高肾上腺素题材的剧作节奏把控秘籍：如何在高速竞技的视听奇观之下，细腻编织老将回归与代际传承的救赎主线。',
    so_what: '节奏感不是单纯的感官轰炸，而是张弛有度的呼吸韵律；在生死时速的节点精准插入人物前史，奇观才能真正具备重量。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/861',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '《疯狂动物城2》（2025）—— 面向教育工作者的编剧分析',
    note: '探讨架空世界观如何映射当代社会议题：如何用跨物种共处的寓言外壳，巧妙拆解多元融合、偏见消解与系统性体制冲突。',
    so_what: '优秀的架空题材绝不是空中楼阁，它本质上是对现实世界的镜像解构；用通俗的类型故事承载严肃的思辨，才能成就跨世代经典。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/862',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '第98届奥斯卡金像奖原创与改编剧本提名影片巡礼（附剧本）',
    note: '盘点全球顶尖编剧最新创作范式演进：非线性叙事、多重视角交织与不可靠叙述者在现代严肃剧情片中的开创性运用。',
    so_what: '研读行业最高峰的剧本标杆是打破思维定势的最快路径；从经典三幕式走向更自由的叙事解构，才能在内容同质化中突围。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/874',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '从投资人最看好的48个AI应用，我看到了这两个趋势',
    note: '顶级风投机构最新研报深度拆解：投资逻辑全面从“横向通用型基座套壳”转向“纵向垂直行业深度数据流”与“全自主执行 Agent”。',
    so_what: '资本的嗅觉永远最先指向退潮方向；别再做人人都能做的通用界面，扎进高壁垒的行业专有场景中，才能拿到真正的定价权。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463036.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '从封闭工具到开放平台，项目管理软件如何设计开放与集成能力',
    note: '解析现代企业级软件的演进生命周期：如何通过标准化 API、Webhook 契约与 MCP 智能体协议，从孤立应用跃迁为工作流中枢。',
    so_what: '软件的壁垒不在于功能的多少，而在于生态集成的不可替代性；做连接器与调度者，比做单点工具具有更高的商业估值。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pd/6462955.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'V4.1 Flash测速刷屏，但DeepSeek这次真正想补的是工程能力',
    note: '穿透性能跑分看底层技术突围：DeepSeek 不仅在模型结构上追求轻量，更在分布式推理通信、长文本缓存与工程部署健壮性上下足硬功夫。',
    so_what: '模型的参数只是表象，工程落地的综合成本与稳定性才是商业化的生死线；优秀的技术型产品人必须懂工程落地的全周期开销。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462122.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '“最怕AI”的小红书，是怎么搞AI的？',
    note: '深度透视真实社区生态对生成式 AI 的警惕与拥抱：如何在捍卫“真实人类经验与社交温度”护城河的同时，用 AI 赋能创作者工具链。',
    so_what: '并非所有场景都适合全面 AI 化；洞察用户对“真实人感”的心理防线，在效率与温度之间找到精妙平衡才是高级产品设计。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462983.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-12.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_12);

console.log(`Day 2026-09-12: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_12.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-12',
  title: '9 月 12 日 · 落地重围与心流守门：当狂热退去，拼的是交付全景',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Vercel 沙箱全球 20 区域落地、Claude 团队展示 SRE 告警自动化修复流、DeepSeek 工程架构底层拆解、从封闭工具到开放平台的产品跃迁。`,
  draft: false,
  epigraph: '炒作能带来最初的围观，但唯有严丝合缝的工程确定性与真实交付，才能在浪潮退去后留在牌桌之上。',
  lead: '今天的技术与商业世界正在经历一场极其健康的去泡沫化洗礼：在云原生与智能体基础设施端，Vercel 将代码沙箱无缝扩展至全球二十个数据中心，Google Cloud 携手官方文档推出即插即用 MCP 插件，Claude 团队更首次公开了智能体自主响应生产环境告警、比对指标并生成合并建议的全自动化 SRE 流水线；在产业与商业应用端，风投资本全面抛弃“横向套壳”，转向对高确定性垂类工作流与自主 Agent 的重注。技术不再是悬空的奇迹，它已经成为每一条真实业务流水线上，守护质量、降低摩擦与构筑护城河的核心齿轮。',
  scene: '「生产环境半夜报了个指标异常？」「不用叫醒开发，Claude 代理已经去查日志、比对前三次发布记录，并在 Slack 里提了带详细证据链的合并修复建议，工程师点个确定就行。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 Vercel 把执行沙箱铺满全球二十个区域，当 Claude 团队把智能体正式引入核心运维告警闭环，我们清晰地看到：**AI 正在以前所未有的确定性，接管软件工程中那些机械、繁琐却不容有失的承重节点。** 智能体不再是一个只能在输入框里陪你聊天的助手，而是一个拥有沙箱环境、能够跨工具调用、会自己翻查指标并给出严密证据链的数字工友。

对于产品经理与一人开发者而言，这意味着你的角色正在经历根本性的蜕变：从过去亲力亲为的原型绘制者和需求传声筒，转变为高阶系统的架构师与质检员。风投机构不再青睐浮于表面的横向套壳应用，真正的护城河永远属于那些能够把真实行业数据、严密验证机制与多 Agent 协作工作流深度咬合在一起的垂直产品。

**不要被瞬息万变的概念所绑架，回归工程落地的全周期开销，守住业务最核心的承重点。** 愿今天的 ${finalItems.length} 篇精选资讯，能为你提供充足的弹药与视野，在智能时代的深水区从容前行。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-12.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
