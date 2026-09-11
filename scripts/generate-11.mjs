import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_11 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '钱开始往创作者口袋流了：TikTok 分账破 8200 万，ReelShort 首度盈利',
    note: '平台商业生态跨越临界点：官方分账奖金池突破 8200 万美元，头部出海平台 ReelShort 实现季度首次规模化盈利，内容分成正向飞轮彻底成型。',
    so_what: '行业的盈利拐点是最大的信心锚；告别早期盲目烧钱补贴，内容分账进入按质量和留存公平结算的健康长跑期。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-11.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok短剧创作者平台全解析：独立创作者如何一站式出海',
    note: '全景拆解 Drama Center 官方通道：从多语种自动配音、版权合规存证到美金分账提现的一体化上车实操全指南。',
    so_what: '认准官方推荐的基础设施通道，能帮一人团队少走半年的合规弯路；踩中平台供给侧补贴窗口期，以极低试错成本积累原始资本。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/drama-center-guide.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok 官方新政解读：大陆团队合规出海通道全面打通',
    note: '梳理跨境机构与大陆本土创作者的资质审核与跨境结算绿通：政策红线明晰化为技术型团队扫清了境外开户与回款障碍。',
    so_what: '政策通道的打通消除了最大的灰色地带；合规落地让专注于技术与内容本身的敏捷团队迎来了真正的黄金出海期。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/policy-june-2026.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '漫剧出海行业简报：混合变现爆发、三大海外真实案例复盘',
    note: '拆解IAA（广告）与IAP（内购）混合变现新打法：在拉美、东南亚与欧美三大梯队市场中，不同客单价受众的分层商业化收割模型。',
    so_what: '没有放之四海而皆准的变现神话；针对不同地域的付费习惯设计梯级变现漏斗，才能将每一滴流量的剩余价值榨取到极致。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/weekly-june-5.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '《哪吒之魔童闹海》的剧本（故事）创作技巧',
    note: '剖析爆款动画电影的戏剧冲突递进法则：如何在神话母题与当代青年自我认同之间架起情感共鸣的桥梁。',
    so_what: '优秀的编剧永远在借古典的外壳讲当下的情绪困境；抓准受众未被满足的潜意识渴望，才能写出具备穿透力的台词与情节。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/760',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '小品与短剧中常用的喜剧技巧与包袱铺垫',
    note: '系统梳理错位、三翻四抖、自相矛盾等经典喜剧结构：在 30 秒短周期内通过预期违背制造高频笑点。',
    so_what: '幽默不是玄学，而是一套严密的情绪计算与预期落差机制；掌握包袱的节奏与反转公式，能让轻量级内容的完播率翻倍。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/765',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '诙谐叙事与社会洞察：近年来喜剧创作的多维成功路径',
    note: '探讨如何把尖锐的现实痛点包装进轻松诙谐的叙事外衣中：在笑声背后留出供观众咀嚼与自省的隐喻空间。',
    so_what: '真正高级的幽默来自对现实荒诞的敏锐捕捉；让观众在会心一笑后产生深度共鸣，作品才能拥有更长久的生命力。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/820',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '2026年最新微短剧制作及市场情报全景',
    note: '汇编全网题材热度走势与立项数据：战神与赘婿全面退潮，都市科幻、悬疑探案与轻喜剧成为平台采购最高溢价品类。',
    so_what: '创作必须紧跟市场供需动态；及时逃离红海过度内卷的废土题材，把筹码押注在下一轮受众审美升级的风口上。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/890',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '怎么用2-4个Agent，干一个真实项目？',
    note: '实战拆解多智能体编排落地全流程：从产品经理定义需求、架构师做接口拆解到代码与测试 Agent 自动闭环交付的敏捷架构。',
    so_what: '一个人指挥一支 Agent 团队已经从狂想变成工业日常；产品经理最核心的竞争力正在变成系统架构设计与任务拆解的精确度。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462658.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '办公AI的战火，烧到哪了？',
    note: '全景梳理办公协同领域的智能化演进：从被动的文档生成工具升级为主动监听业务流、跨系统调起企业级动作的中央调度枢纽。',
    so_what: 'AI 办公正在脱离聊天框的束缚；谁能把智能体无感缝合进既有的企业 ERP 与审批流中，谁就能拿下万亿级企业服务的护城河。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463033.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '卖的是产品，做的却还是项目：B2B软件商品化最容易忽略的一步',
    note: '剖析 SaaS 团队陷入定制外包泥潭的根源：如何在满足头部客户特殊需求的同时，抽象出高通用性的标准化产品内核。',
    so_what: '摆脱外包诅咒的关键在于强大的模块化抽象能力；学会拒绝吞噬研发资源的非标需求，才能建立高边际效益的软件资产。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pd/6462863.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '信息平权的背面：人人会用AI，少数人会沉淀出自己的骨架',
    note: '探讨大模型普及后个体认知的重新分化：工具越容易获取，依赖工具导致的思维退化越严重，唯有具备认知骨架的人能放大杠杆。',
    so_what: '别把模型的广博当成自己的底蕴；在这个人人触手可及 AI 的时代，你对业务本质的深度判断才是无法被复制的稀缺资本。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462069.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-11.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_11);

console.log(`Day 2026-09-11: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_11.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-11',
  title: '9 月 11 日 · 端侧轻量与生态筑堤：当基座沉入水底，应用浮出水面',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：DeepSeek 发布更小 Flash 模型、ElevenLabs 签约环球音乐正版化、多智能体团队编排实战、办公 AI 从对话框迈入系统级调度。`,
  draft: false,
  epigraph: '算力的极致终归是平民化，当巨头把基座做成随取随用的自来水，决定胜负的永远是谁在水面之上搭建了不可撼动的生态堤坝。',
  lead: '今天的技术与商业脉搏正在经历一场关键的相变：DeepSeek 再次亮剑，发布体积更小、吞吐更快的新一代 Flash 模型，宣告模型推理成本进一步击穿底线；ElevenLabs 联手环球音乐开启多年版权合作，标志着音频生成全面踏入商业出版的正规通道；而在应用与工程端，从 OpenAI 开放 Agents 编排 API、GitHub 推出代码扫描接口，到产品经理用 2-4 个 Agent 闭环交付真实业务，AI 正在彻底告别孤岛式的单机实验，全面嵌入企业级系统的骨架与工作流中。',
  scene: '「现在的端侧模型速度怎么样？」「极快。DeepSeek 的新 Flash 几乎感觉不到延迟，而且 ElevenLabs 已经跟环球音乐签了正版合作，以后做产品再也不用担心版权和算力账单了。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 DeepSeek 把模型体积与调用成本再次大幅压缩，当 ElevenLabs 与环球音乐完成正版签约，整个 AI 产业正在以前所未有的速度撕下技术神话的滤镜，回归商业基础设施的本质：**模型本身正在变成无处不在的“水电煤”，而真正的红利与溢价，正在向拥有行业真实数据、能够驾驭复杂智能体流、并且守住合规底线的应用端疯狂倾斜。**

对于产品人与独立创造者而言，这既是最好的时代，也是要求最高的时代。信息平权的背面，是“人人都会调用模型，但极少数人能沉淀出系统骨架”。如果你只是在通用界面上套壳，你的价值随时会被更廉价的基础设施轻易稀释；但如果你能像今天优秀的从业者一样，用 2 到 4 个 Agent 编排出一套自动化跑通特定业务的闭环，你一个人就是一家高利润的软件公司。

**不要去追赶每一朵瞬息万变的浪花，把精力投入到底层工作流的重构与真实用户的长期留存上。** 愿今天的 ${finalItems.length} 篇精选资讯，能成为你今天搭建下一代智能产品与商业闭环的坚固砖石。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-11.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
