import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DATE = '2026-08-31';
const TITLE = '8 月 31 日 · 时间线助手与持久智能体：当 AI 住进你每天在刷的流';
const HIGHLIGHTS = '全网 7 大领域 65 篇高密度精选：Grok Bot 接入 X 时间线、OpenAI 持久智能体模式、Luna Graph 画布交付生产级 React 与短剧全球化。';
const EPIGRAPH = '最好的工具从不逼用户打开新的窗口，而是直接住进你每天都在看的信息流。';
const LEAD = `今天全网的产品与模型演进呈现出强烈的「流式嵌入」与「持久运行」趋势：xAI 正式将 Grok Bot 深度集成进 X 时间线与书签流，助手首次直接常驻于用户的信息消费场景；OpenAI 正在内测智能体的「持久模式」（Persistent Mode），让 Codex 等编码代理拥有跨会话长时主动干活能力；与此同时，Luna Graph 实现了设计画布直接产出生产级 React 代码，彻底抹平了设计标注与代码落地的缝隙。AI 正在从「被动问答」全面过渡为「常驻生产力」。`;
const SCENE = `「以前是代码写一半切去问 AI，现在是 Grok Bot 在时间线里看我刷推，顺便把刚聊到的 Demo 自动写完了。」`;

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

function shuffleArray(array, seed = 20260831) {
  let currentIndex = array.length, temporaryValue, randomIndex;
  let random = function() {
    let x = Math.sin(seed++) * 10000;
    return x - Math.floor(x);
  };
  while (0 !== currentIndex) {
    randomIndex = Math.floor(random() * currentIndex);
    currentIndex -= 1;
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }
  return array;
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
    category: 'AI 协作',
    title: 'OpenAI 开发「持久模式」智能体：Codex 将能够跨会话长时主动干活',
    note: '突破单次 Prompt 对话的记忆瓶颈，智能体获得跨周期的任务目标跟踪、环境自检与长程任务拆解执行能力。',
    url: 'https://www.aigc.cn/109755.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '从「即时打工人」变成「长期合伙人」，一人公司的自动化上限再次被指数级拉高。',
  },
  {
    category: 'AI 资讯',
    title: '智谱开源 GLM-5.3 模型权重：主打智能体编程与网络防御',
    note: '商汤大装置提供国产算力支撑，开源推理与微调权重，全面强化了在复杂代码仓库与系统级网络环境中的推理稳健性。',
    url: 'https://www.aigc.cn/109762.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '国产大模型在编程与安全垂直领域的全面开源，为私有化 Agent 部署提供了高性价比底座。',
  },
  {
    category: 'AI 资讯',
    title: '国家数据局：全国已建成高质量数据集超 12.6 万个，体量超 1815PB',
    note: '涵盖自动驾驶、工业制造、生物医药等数十个重点产业，多模态高质量训练语料进入规模化供给新阶段。',
    url: 'https://www.aigc.cn/109761.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '高质量数据集供给的爆发，将直接加速垂类行业模型从概念验证走向生产落地。',
  },
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

  // Add AI 漫剧 and AIGC extras
  const allItems = [...items, ...DRAMA_ITEMS, ...AIGC_EXTRAS];

  // Pinned item
  const pinnedItem = allItems.find((i) => i.pinned) || allItems[0];
  const others = allItems.filter((i) => i !== pinnedItem);

  // Shuffle others to eliminate sequential mirroring
  const shuffledOthers = shuffleArray(others, 20260831);

  const finalItems = [pinnedItem, ...shuffledOthers];

  console.log(`✅ Total items with AI 漫剧 & AIGC extras: ${finalItems.length}`);

  const frontmatter = {
    date: DATE,
    title: TITLE,
    highlights: HIGHLIGHTS,
    draft: false,
    epigraph: EPIGRAPH,
    lead: LEAD,
    scene: SCENE,
    items: finalItems,
  };

  const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 ${finalItems.length} 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  const targetFile = path.join(TARGET_DIR, `${DATE}.md`);
  fs.writeFileSync(targetFile, mdContent, 'utf8');
  console.log(`💾 Successfully generated ${targetFile}`);
}

run();
