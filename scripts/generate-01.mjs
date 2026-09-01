import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DATE = '2026-09-01';
const TITLE = '9 月 1 日 · 多智能体编排与印刷级美学：当单人创意直接调度整条流水线';
const HIGHLIGHTS = '全网 7 大领域 68 篇高密度精选：阿里千问 Agent Teams 视频编排、DeepSeek 多模态视觉开源、Mono-color 印刷美学规矩与竖屏短剧好莱坞化。';
const EPIGRAPH = '从手搓单点功能到调度智能体团队，一人公司的杠杆正在从代码层直接跃迁到编导层。';
const LEAD = `迈入九月，AI 在创作管线与工程实践中正在经历一场从「单点生成」到「团队级自主协同」的质变：阿里千问创作正式上线 Agent Teams 智能体团队功能，用户只需输入一个核心创意，剧本、分镜、原画与剪辑 Agent 便会自动组队协同交付成片；同时，DeepSeek 开源了 V4-Flash-Vision 视觉多模态模型，高并发多模态推理成本进一步下探；开源社区中 Mono-color 将传统物理印刷的套印与留白规则固化为可调用的 Skill。单人创作者第一次拥有了指挥整座虚拟工作室的底气。`;
const SCENE = `「以前一个人做视频要切五个软件，现在只要在 Agent Teams 里发一句分镜需求，剧本和原画 Agent 已经在后台吵完架把工程交出来了。」`;

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

function shuffleArray(array, seed = 20260901) {
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
    title: '阿里千问创作上线 Agent Teams：输入创意，智能体编队自动规划分镜并交付成片',
    note: '分工 Agent 覆盖剧本拆解、分镜头视觉风格统一、TTS 配音与剪辑渲染，将传统繁琐的跨工具拼凑流程压缩为单一对话流。',
    url: 'https://www.aigc.cn/109902.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '多智能体协作替代了手工拼接，视频创作者的核心竞争力进一步收敛为敏锐的选题与审美监督。',
  },
  {
    category: 'AI 资讯',
    title: 'DeepSeek-V4-Flash-Vision-Exp 开源：多模态视觉 Agent 推理成本再降数量级',
    note: '在多模态 GUI 识别、复杂图表理解与跨帧视觉追踪上表现强劲，为低成本自动化桌面操作与视频理解提供了轻量底座。',
    url: 'https://www.aigc.cn/109898.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '轻量视觉多模态模型的爆发，让端侧实时屏幕分析与低功耗视觉 Agent 普及成为可能。',
  },
  {
    category: '一人公司',
    title: 'OpenClaw 开源助手 2.0：支持全本地部署的个人 AI 副驾驶与文件助理',
    note: '支持本地多格式文档索引、离线隐私运行与多端同步，专为独立开发者和创作者打造免折腾的个人数据中枢。',
    url: 'https://www.aigc.cn/109908.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: 'Local-first 本地优先架构彻底打消敏感资产泄露顾虑，是一人公司长期沉淀知识库的稳妥选择。',
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
  const shuffledOthers = shuffleArray(others, 20260901);

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
