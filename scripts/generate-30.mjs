import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DATE = '2026-08-30';
const TITLE = '8 月 30 日 · 视频实时化与竖屏好莱坞：当生成速度首次越过播放速度';
const HIGHLIGHTS = '全网 7 大领域 63 篇高密度精选：MiniMax H3 Max 9秒极速成片、智谱 GLM-5.3 无审查版上卡、好莱坞工会明星下场拍竖屏剧与 AIGC 独家生产力。';
const EPIGRAPH = '当 AI 生成一秒视频的时间小于一秒，视频创作就从离线渲染正式跨入了实时编导时代。';
const LEAD = `今天人工智能在多模态与影视产业迎来了一个标志性转折：MiniMax 推出 H3 Max 视频模型，15 秒高动态视频生成仅需 9 秒，生成速度首次真正越过了视频的播放速度，这意味着实时的 AI 交互编导成为可能；与此同时，好莱坞明星与工会演员（如 James Franco、Issa Rae）开始成规模亲自俯身入局 TikTok 竖屏微短剧，传统巨头 Fox 更是反向入股乌克兰团队打包 200 部剧集，短剧与 AI 漫剧已从单纯的买量模式进化为全球顶级内容工业的必争之地。`;
const SCENE = `「以前给剧组做分镜，点一次生成要下楼喝杯咖啡；现在 H3 Max 9 秒就出来了，导演在旁边看着直接改词。」`;

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
    title: '两份跑通信号：Kuku TV 闯入 TOP3、Reel.AI ARR 破千万，普通人的机会在哪？',
    note: 'DataEye 验证两条出海路径：印度 Kuku TV 凭借本土语种首闯素材榜前三，纯 AI 短剧 App Reel.AI ARR 突破千万。拆解个人创作者可抄的轻量路径。',
    url: 'https://dramagoing.com/articles/kuku-reelai-commercial-proof.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '非英语小语种市场和纯 AI 剧集验证了个人创作者无需重资产也能实现高 ROI 商业闭环。',
  },
];

const AIGC_EXTRAS = [
  {
    category: '产品设计',
    title: 'AI 3D 卷向生产端：Lux3D 发布，3D 创业者与空间设计师的新武器',
    note: '告别过去仅能旋转预览的玩具模型，Lux3D 支持工业级高精度网格、UV 拆分与 PBR 材质导出，直接打通虚幻引擎与游戏开发工作流。',
    url: 'https://www.aigc.cn/109719.html',
    source: 'aigc.cn',
    media: 'https://www.aigc.cn/wp-content/uploads/2026/08/640-3.jpeg',
    pinned: false,
    so_what: '3D 资产生产门槛的断崖式下跌，让独立开发者制作沉浸式 3D 场景与互动影游成为可能。',
  },
  {
    category: 'AI 协作',
    title: 'Claude 自动长出浏览器：填表拉数，你的 AI 打工人真正拥有了专属工位',
    note: '交代一句「把本月发票从供应商后台拉出来」，Claude 判断需要联网后自动在侧栏唤起浏览器并自主点击完成数据抓取与对账。',
    url: 'https://www.aigc.cn/109689.html',
    source: 'aigc.cn',
    media: 'https://www.aigc.cn/wp-content/uploads/2026/08/00061a6d224867bece8a7bd55e13ad64.jpeg',
    pinned: false,
    so_what: '从纯文字对话跃迁到图形界面自主操作（Computer Use），一人公司的数据处理效率提升数倍。',
  },
  {
    category: 'AI 资讯',
    title: '只降价 20% 账单却少八成：GPT-5.6 Terra 杀入 Claude 地盘重算智能体编程账',
    note: '通过优化智能体框架调度、动态分工与减少无效长上下文重发，实际工程任务的 Token 消耗暴跌 82%，大幅降低开发门槛。',
    url: 'https://www.aigc.cn/109671.html',
    source: 'aigc.cn',
    media: 'https://www.aigc.cn/wp-content/uploads/2026/08/a72e3e8458b0ab646543a30b35b0d42d.jpeg',
    pinned: false,
    so_what: '算力成本的优化不再依赖单纯的降价，架构层面的智能调度才是降本的核心解法。',
  },
  {
    category: '审美提升',
    title: '关停五年后，虾米被阿里用 AI「复活」：HappyShrimp 音乐模型实战',
    note: '阿里发布 HappyShrimp 1.0 AI 音乐模型并与太合音乐达成战略合作，通过自然语言生成高完成度多音轨乐曲与人声伴奏。',
    url: 'https://www.aigc.cn/109678.html',
    source: 'aigc.cn',
    media: 'https://www.aigc.cn/wp-content/uploads/2026/08/e4a88cd72e787ad98f549e7dd5b284d3.jpeg',
    pinned: false,
    so_what: 'AI 音乐走向工业化配乐生产，极大降低了漫剧 BGM 与播客音频制作的版权成本。',
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

  // Append AIGC extras
  for (const extra of AIGC_EXTRAS) {
    if (!items.some((i) => i.title === extra.title || i.url === extra.url)) {
      items.push(extra);
    }
  }

  console.log(`✅ Total items with AI 漫剧 & AIGC extras: ${items.length}`);

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
