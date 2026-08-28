import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DRAMA_ANALYSIS_ITEMS = {
  '2026-08-28': [
    {
      category: 'AI 漫剧',
      title: 'AI 漫剧行业大洗牌：从抽卡式量产到 IP 精品化的存活法则拆解',
      note: '深度剖析为什么 90% 粗放式抽卡漫剧面临亏损，而以自研网文 IP 闭环与工业化 Agent 分镜为核心的团队正在实现破亿播放。',
      url: 'https://36kr.com/p/2890695024765696',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: 'AI 漫剧已告别靠工具赚快钱的红利期，内容叙事掌控力与系列化 IP 才是唯一的护城河。',
    },
    {
      category: 'AI 漫剧',
      title: '单分钟成本压缩至千元：AI 微短剧与漫剧如何重构影视工业流水线',
      note: '详细测算 AI 在原画、中间帧与音画同步上的降本效应，将传统真人剧 1/7 的成本转化为高频周更甚至日更的叙事生产力。',
      url: 'https://36kr.com/p/2807386026909440',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '制作周期的数量级缩短，让创作者能够根据用户即时反馈敏捷调整剧情走向与角色命运。',
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
  '2026-08-27': [
    {
      category: 'AI 漫剧',
      title: '爆款 AI 漫剧的叙事底层逻辑：强节奏、反转爽点与自有 IP 闭环',
      note: '解析在短视频快节奏消费下，男频末世与规则怪谈漫剧为何能持续霸榜，拆解情绪价值与视觉冲击的黄金组合拳。',
      url: 'https://36kr.com/p/2847525381987588',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: 'AI 漫剧的本质是「短剧内核+动画外壳」，精准击中受众情绪爽点是低成本破圈的关键。',
    },
    {
      category: 'AI 漫剧',
      title: '微短剧与 AI 漫剧出海实录：跨语言本地化配音与海外变现 ROI 拆解',
      note: '探讨如何通过多模态 AI 工具实现海外社媒多语种配音与文化背景微调，开拓海外高单价内容变现的第二曲线。',
      url: 'https://36kr.com/p/2916172605178625',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '出海不仅是语言翻译，更是利用 AI 低成本本地化能力重构海外受众的视听消费体验。',
    },
    {
      category: 'AI 漫剧',
      title: 'B站爆款 AI 漫剧幕后拆解：开篇 3 秒钩子与多机位动态分镜实战',
      note: '深入拆解千万播放级漫剧如何通过悬念前置与节奏把控拉升完播率，总结出适用于动漫 UP 主的分镜设计公式。',
      url: 'https://www.bilibili.com/read/cv33829104/',
      source: 'bilibili.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '开篇的前 3 秒决定了 80% 的用户留存，镜头语言的紧凑感是漫剧完播率的胜负手。',
    },
  ],
  '2026-08-26': [
    {
      category: 'AI 漫剧',
      title: '从抽卡拼凑到系列化剧 N 代：AI 漫剧如何破解「千人一面」的审美疲劳',
      note: '探讨为什么单一提示词生成的模板脸正在被观众抛弃，头部团队如何通过资产沉淀与长线世界观绑定打造长青剧集。',
      url: 'https://36kr.com/p/2908865886675718',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '克服模板化脸谱是建立高黏性粉丝心智的必经之路，角色资产化运营正在成为行业新共识。',
    },
    {
      category: 'AI 漫剧',
      title: '2026 暑期档 AI 漫剧崛起观察：低成本高周转，AI 短剧消耗量如何反超真人实拍',
      note: '深度解读为什么平台政策与分账系数正在向精品 AI 漫剧倾斜，解析真人短剧高亏损背景下漫剧的结构性红利。',
      url: 'https://36kr.com/p/2923594951111425',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '抓住平台流量倾斜窗口期，以极低制作成本快速跑通商业闭环是当前最确定的机会。',
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
  '2026-08-25': [
    {
      category: 'AI 漫剧',
      title: '从短剧出道到品牌代言：AI 漫剧角色「艺人化」运营与长尾商业价值',
      note: '解析 AI 虚拟角色如何通过持续更新的漫剧作品积累真实粉丝，打通广告代言、私域定制与衍生周边的长线变现链路。',
      url: 'https://36kr.com/p/2873194012741376',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: 'AI 漫剧的终局不仅是赚分账流量费，更是低成本孵化高辨识度虚拟 IP 资产。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 漫剧商业化 ROI 闭环实战：万播收益、小说推文 CPS 与付费转化模式',
      note: '拆解短视频平台流量激励、小说推文分佣与付费短剧解锁三种核心盈利模式，为独立创作者厘清财务模型。',
      url: 'https://36kr.com/p/2865910482939904',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '清晰的商业模式倒推选题与节奏设计，才能避免「叫好不叫座」的无效自嗨。',
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
};

for (const [date, dramaList] of Object.entries(DRAMA_ANALYSIS_ITEMS)) {
  const filePath = path.join(TARGET_DIR, `${date}.md`);
  if (!fs.existsSync(filePath)) continue;

  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) continue;

  const frontmatter = yaml.load(match[1]);
  let existingItems = frontmatter.items || [];

  // Remove any old drama items that were tool homepages
  existingItems = existingItems.filter((i) => i.category !== 'AI 漫剧');

  // Insert real analysis drama items at position 1 (right after pinned item)
  const pinnedIdx = existingItems.findIndex((i) => i.pinned);
  const insertPos = pinnedIdx >= 0 ? pinnedIdx + 1 : 0;
  existingItems.splice(insertPos, 0, ...dramaList);

  frontmatter.items = existingItems;

  const newContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 ${existingItems.length} 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`✅ Injected ${dramaList.length} deep AI 漫剧 analysis articles into ${date}.md (Total items: ${existingItems.length})`);
}
