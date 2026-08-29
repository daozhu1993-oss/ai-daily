import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DATE = '2026-08-29';
const TITLE = '8 月 29 日 · 算力稀疏化与开发者索引：当智能体拥有专属知识库';
const HIGHLIGHTS = '全网 7 大领域 60 篇高密度精选：腾讯混元 Hy4 770B 权重开源、Firecrawl 七千万开发者索引、短剧出海并表账本与一人公司微工具。';
const EPIGRAPH = '开源不仅是公开代码，更是把大模型的思考权重完整交还给开发者社群。';
const LEAD = `今天全网的技术脉搏呈现出极具突破性的务实演进：腾讯正式开源 770B 参数混元 Hy4 Preview 模型，仅激活 49B 参数便实现 1M 原生超长上下文，让企业级长文本推理成本进入平民化区间；与此同时，Firecrawl 推出专供编码 Agent 使用的 7000 万份开发者索引库，智能体终于不再依赖通用搜索的模糊匹配。从模型算力稀疏化到专业开发者基础设施，AI 正在从「玩具」全面进化为「生产力底座」。`;
const SCENE = `「你们的 Agent 为什么能秒级定位十几年前的底层库变更？」「因为我们给它挂了 Firecrawl 的专属开发者索引，比人工去翻文档快 100 倍。」`;

const VALID_CATEGORIES = new Set([
  'AI 资讯',
  '一人公司',
  '产品设计',
  '审美提升',
  '产品营销',
  'AI 漫剧',
  'AI 协作',
]);

function decodeEntities(str) {
  if (!str) return '';
  return str
    .replace(/&#x27;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&nbsp;/g, ' ')
    .trim();
}

const DRAMA_ITEMS = [
  {
    category: 'AI 漫剧',
    title: '出海短剧冰火局：中文在线半年报揭示的扭亏与并表账本',
    note: '全资 FlareFlow 扭亏（2.52 亿收入 / 1.52 亿净利），而 ReelShort 全年预估超 10 亿美元却因不并表难进母公司利润表。出海从红利期全面拐入系统能力期。',
    url: 'https://dramagoing.com/daily-brief/2026-08-28.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '靠单一爆款博概率的粗放时代结束，精细化财税、并表结构与多渠道发行成为头部玩家的核心壁垒。',
  },
  {
    category: 'AI 漫剧',
    title: '两份跑通信号：Kuku TV 闯入 TOP3、Reel.AI ARR 破千万，普通人的机会在哪？',
    note: 'DataEye 验证两条出海路径：印度 Kuku TV 凭借本土语种首闯素材榜前三，纯 AI 短剧 App Reel.AI ARR 突破千万。拆解个人创作者可抄的轻量路径。',
    url: 'https://dramagoing.com/articles/kuku-reelai-commercial-proof.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '非英语小语种市场和纯 AI 剧集验证了个人创作者无需重资产也能实现高 ROI 商业闭环。',
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
    title: 'AI 漫剧行业大洗牌：从抽卡式量产到 IP 精品化的存活法则拆解',
    note: '深度剖析为什么 90% 粗放式抽卡漫剧面临亏损，而以自研网文 IP 闭环与工业化 Agent 分镜为核心的团队正在实现破亿播放。',
    url: 'https://36kr.com/p/2890695024765696',
    source: '36kr.com',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: 'AI 漫剧已告别靠工具赚快钱的红利期，内容叙事掌控力与系列化 IP 才是唯一的护城河。',
  },
  {
    category: 'AI 漫剧',
    title: '单分钟成本压缩至千元：AI 微短剧与漫剧如何重构影视工业流水线',
    note: '详细测算 AI 在原画、中间帧与音画同步上的降本效应，将传统真人剧 1/7 的成本转化为高频周更甚至日更的叙事生产力。',
    url: 'https://36kr.com/p/2807386026909440',
    source: '36kr.com',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '制作周期的数量级缩短，让创作者能够根据用户即时反馈敏捷调整剧情走向与角色命运。',
  },
];

async function run() {
  console.log(`📡 Fetching https://iandaily.xyz/ for ${DATE}...`);
  const res = await fetch('https://iandaily.xyz/', {
    headers: {
      'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    },
  });

  const html = await res.text();
  const cardRegex = /<a[^>]*class="plaza-card[^"]*"[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g;
  const items = [];
  let match;

  while ((match = cardRegex.exec(html)) !== null) {
    const href = match[1];
    const cardContent = match[2];

    const imgMatch = cardContent.match(/<img[^>]*src="([^"]+)"/);
    let media = imgMatch ? imgMatch[1] : '';
    if (media.startsWith('/')) {
      media = 'https://iandaily.xyz' + media;
    }

    const kickerMatch = cardContent.match(/<div class="plaza-kicker">([\s\S]*?)<\/div>/);
    let category = 'AI 资讯';
    let source = '';
    if (kickerMatch) {
      const spans = [...kickerMatch[1].matchAll(/<span>([^<]+)<\/span>/g)].map((m) =>
        decodeEntities(m[1])
      );
      if (spans.length > 0 && VALID_CATEGORIES.has(spans[0])) {
        category = spans[0];
      }
      if (spans.length > 1) {
        source = spans[spans.length - 1];
      }
    }

    const titleMatch = cardContent.match(/<h3 class="plaza-title">([\s\S]*?)<\/h3>/);
    const itemTitle = titleMatch ? decodeEntities(titleMatch[1]) : '';

    const noteMatch = cardContent.match(/<p class="plaza-judgment">([\s\S]*?)<\/p>/);
    const itemNote = noteMatch ? decodeEntities(noteMatch[1]) : '';

    if (itemTitle && href) {
      if (!source) {
        try {
          source = new URL(href).hostname.replace(/^www\./, '');
        } catch {
          source = 'web';
        }
      }

      items.push({
        category,
        title: itemTitle,
        note: itemNote,
        url: href,
        source,
        media: media || 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
        pinned: items.length === 0,
        so_what: itemNote,
      });
    }
  }

  console.log(`✅ Extracted ${items.length} items from iandaily`);

  // Insert AI 漫剧 items right after pinned item
  items.splice(1, 0, ...DRAMA_ITEMS);
  console.log(`✅ Total items with AI 漫剧: ${items.length}`);

  const frontmatter = {
    date: DATE,
    title: TITLE,
    highlights: HIGHLIGHTS,
    draft: false,
    epigraph: EPIGRAPH,
    lead: LEAD,
    scene: SCENE,
    items,
  };

  const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 ${items.length} 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  const targetFile = path.join(TARGET_DIR, `${DATE}.md`);
  fs.writeFileSync(targetFile, mdContent, 'utf8');
  console.log(`💾 Successfully generated ${targetFile}`);
}

run();
