import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_13 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '从野路子到正规军：短剧出海的「成年礼」来了',
    note: '梳理欧美微短剧分账与流媒体平台版权合作升级：告别买量投机粗暴套路，工业化制片、本地化演员与合规发行成为主流分水岭。',
    so_what: '行业的成年礼意味着劣质搬运的红利期彻底终结；坚持内容工业化和合规运作的团队，才能在主流影视资本的洗牌期分到大蛋糕。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-09.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '9月1日，短剧出海同时撞上红线与红利',
    note: '解析海外多国数据合规监管与平台原创激励新政的同步落地：一方面面临严密审查，另一方面合规精品剧获得前所未有的阶梯分成。',
    so_what: '红线与红利是一枚硬币的两面；谁能最快将合规流程内化为日常创作习惯，谁就能独享高额合规溢价。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-02.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '两张地图之间的收入缺口，正被本地化填平',
    note: '深度拆解出海短剧在拉美与东南亚新兴市场的变现裂变：通过深度本地化配音与契合本地文化反转，跑通低客单大体量的新商业回路。',
    so_what: '本地化不是简单的文字翻译，而是文化认同与情绪共鸣的再造；做懂当地人痛点的剧本，新兴市场同样能挤出可观利润。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-08-17.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '下载涌向新兴市场，钱留在成熟市场：出海被拆成两张地图',
    note: '出海流量与收益分化全景透视：欧美市场贡献 80% 现金流，新兴市场贡献 80% 用户基数，双轮驱动打造流量与现金流闭环。',
    so_what: '明确每一部作品的战略使命；用高客单作品保利润，用下沉市场作品保用户池，矩阵式出海才能抵御单点风险。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-08-14.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: 'IMDb 排名前100的经典电影片单与剧作母题解析',
    note: '系统梳理影史百年殿堂级剧本的核心驱动力：从英雄之旅到悲剧宿命，拆解高口碑影片跨越时代的剧作母题。',
    so_what: '技术的演进改变了画面呈现，但打动人类心智的情感母题从未改变；吃透经典母题的张力模型，是一切爆款叙事的基石。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/776',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '剧本、小说等版权登记：各地著作权登记平台链接与存证维权实务',
    note: '编剧与原创作者知识产权防坑指引：国家版权局及各省官方存证通道全整理，梳理商用投稿前的电子存证与时间戳保全。',
    so_what: '创作成果是创作者最核心的数字资产；建立先存证、后商务的职业化防线，才能在 IP 授权谈判中掌握主动权。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/761',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '《白马飞飞》：儿童剧导演的创作流程与受众心智洞察',
    note: '拆解低龄受众向戏剧的分镜与注意力引导法则：如何在没有复杂台词的情况下，完全依靠鲜明形体与夸张视听锚定孩子注意力。',
    so_what: '能把最挑剔的儿童受众留住的技巧，同样适用于碎片化时代的成年人；化繁为简、用纯粹视听驱动情绪是高级视听语言。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/841',
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
    title: 'OpenAI 做了一次 Agent 测试：1200 个 AI 自己建群协同',
    note: '震撼的多智能体自发社会行为实测：当 1200 个 Agent 拥有通信协议与任务自主权后，它们自发分工、拉群建组并解决高阶复杂问题。',
    so_what: '智能体的群体涌现正在重塑组织形态；产品经理需要从“设计人机交互界面”全面进阶为“设计多智能体社会协作契约”。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462289.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '一万个Agent，88小时，OpenAI 破解数学“千禧难题”',
    note: '暴力搜索与符号推理结合的系统级胜利：通过大规模 Agent 集群并行假设验证与自省修剪，AI 正在把科研探索周期缩短万倍。',
    so_what: '复杂问题的破局点在于并行计算与自治验证；善于把复杂业务拆解为万级可并行子任务的产品架构，将具有不可思议的生产力杠杆。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462099.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '字节要用世界模型重做PICO，押注下一代内容入口',
    note: '大厂空间计算与生成式 AI 战略合流：不再依靠传统人工建模，而是通过世界模型实时生成高保真交互空间，探索次世代硬件入口。',
    so_what: '硬件的更迭本质是内容交互维度的升维；提前布局空间与具身模型的内容创作者，将拿到下一个十年的船票。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462071.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'AI Coding 的产品竟然卖了好几万，你咋搞的？',
    note: '独立开发者商业化破局手记：如何用几行核心 Prompt 和 MCP 胶水，精准切中非程序员做微型业务的刚需并实现大额营收。',
    so_what: '最值钱的技术不是最复杂的算法，而是把复杂技术降维打包给最迫切需要的人；找准高价值受众的真实阻点，小工具也能产生暴利。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6460786.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-13.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_13);

console.log(`Day 2026-09-13: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_13.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-13',
  title: '9 月 13 日 · 群体智能与生态契约：当 Agent 开始自建组织',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Anthropic CEO 论前沿模型发布节律、OpenAI 1200个智能体群聊协同实验、Vercel 发布轻量多代理框架 fx、Notion 启动移动端纯原生重构。`,
  draft: false,
  epigraph: '单个智能体是生产力的倍增器，而当智能体开始通过协议自发建群、协同分工，人类组织的协作形态正在迎来根本性的范式转移。',
  lead: '今天的技术与商业脉搏正在步入多智能体协同涌现的深水区：在技术顶层，Anthropic 首席执行官 Dario Amodei 撰文重磅呼吁建立科学严谨的前沿模型发布节律，Sam Altman 亦表态将向独立第三方机构开放深度测评权限，模型安全与治理进入规范期；而在工程与协同前沿，OpenAI 测试 1200 个 Agent 自发拉群协同、Vercel 推出轻量多代理编排框架 fx，甚至一万个 Agent 在 88 小时内联手攻克科研推理难关。从单一对话框到复杂的智能体社会生态，创造者正在经历从“执行者”到“智能体组织架构师”的全面跃迁。',
  scene: '「现在的业务系统怎么全是 Agent 在跑？」「不是一个，是一整个智能体团队。旗舰大模型当调度中枢，派发给几个轻量专业 Agent 分头做抓取、分析和代码交付，效率比过去十人团队还要高。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 1200 个智能体能够在同一个系统内自发分工建群，当万级 Agent 能够在几十小时内并肩啃下原本需要数年攻坚的复杂问题，整个软件工业的生产关系正在被重新定义。**我们不再只是单纯编写提示词的使用者，而是开始真正担任“硅基智能团队的管理者与架构师”。** 谁能用最优雅的协议编排好智能体之间的沟通边界与状态机，谁就能以单人之力撬动跨国大厂的研发效能。

与此相呼应的，是技术巨头在顶层设计上的集体自省：从 Dario Amodei 对模型节律与安全治理的呼吁，到第三方评测接口的制度化开放，AI 正在从早期的无序狂奔走向具备成熟契约的现代产业。在这个拐点上，浮躁的追涨杀跌已经无法带来超额回报，唯有那些深耕底层工作流、建立透明可验证机制的团队，才能在智能浪潮中获得长久的信任。

**不要把时间浪费在与通用能力的平庸较劲上，学会用系统思维组织智能体，做离业务本质最近的操盘手。** 愿今天的 ${finalItems.length} 篇精选资讯，能为你提供清晰的认知灯塔，在智能体生态的大爆发中抢占身位。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-13.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
