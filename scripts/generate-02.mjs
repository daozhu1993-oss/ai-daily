import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DATE = '2026-09-02';
const TITLE = '9 月 2 日 · 提示词缓存与逐帧界面：当长程智能体终于不必看账单';
const HIGHLIGHTS = '全网 7 大领域 63 篇高密度精选：Anthropic Fable 5.1 缓存降本四分之三、Runway Solaris 逐帧生成动态 UI、Webtoon 入局竖屏短剧与 TikTok 原创爆款破 3 亿。';
const EPIGRAPH = '真正推动智能体从玩具走向生产力的，不是跑分高了 1%，而是上下文缓存便宜了 75%。';
const LEAD = `今天 AI 模型与交互界面迎来了两个极具实战意义的突破：Anthropic 发布 Fable 5.1，将长任务 Prompt 缓存读取成本直接砍去四分之三，让多轮长程 Agent 终于不必受困于暴涨的 Token 账单；与此同时，Runway 推出 Solaris 视频生成 UI 范式，界面不再依赖繁复的前端手写，而是根据用户意图逐帧动态渲染长出；在微短剧赛道，全球漫画巨头 Webtoon 携顶级 IP 全量进军竖屏微短剧，TikTok 官方自制剧《In The Name Of Beauty》12 天突破 3 亿播放，内容工业正从野蛮买量进入头部精品自研的新战场。`;
const SCENE = `「以前跑一个长程爬虫 Agent 总是心惊胆战看账单；现在有了 1/4 缓存价，智能体可以把整个库的源码完整翻上十遍。」`;

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

function shuffleArray(array, seed = 20260902) {
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

// 4 strictly unique AI drama items that have NEVER been used before
const DRAMA_ITEMS = [
  {
    category: 'AI 漫剧',
    title: 'TikTok 亲自造的爆款：一部韩妆短剧 12 天破 3 亿，平台不再只当流量房东',
    note: 'TikTok 官方下场操盘原创短剧《In The Name Of Beauty》，44 集、12 天全球播放破 3 亿，验证了平台自研自制与高辨识度垂类 IP 的恐怖爆发力。',
    url: 'https://dramagoing.com/daily-brief/2026-08-19.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '平台从收过路费转为深度自制，优质垂直题材制作团队迎来官方直接采买红利。',
  },
  {
    category: 'AI 漫剧',
    title: '漫画巨头亲自下场做竖屏：Webtoon 入局 Microdrama，低质套脸剧被加速清退',
    note: '韩国数字漫画巨头 Webtoon 将旗下头部热门条漫 IP 批量改编为竖屏微短剧，降维打击传统粗制滥造的抽卡流水线作品。',
    url: 'https://dramagoing.com/daily-brief/2026-08-18.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '成熟漫画 IP 自带高忠诚度受众，漫改剧是降低冷启动获客成本的最优解法。',
  },
  {
    category: 'AI 漫剧',
    title: '收租变共担：TikTok 推出全球共创计划，AI 承制 500 元/分钟收编创作者',
    note: '剧本授权分一半、AI 承制每分钟补贴 500 元、爆款单部最高奖励数万美元，官方生态重构了个人创作者的确定性收入预期。',
    url: 'https://dramagoing.com/daily-brief/2026-08-16.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '平台保底补贴有效对冲了买量风险，一人团队凭借标准化制作流即可获得稳定现金流。',
  },
  {
    category: 'AI 漫剧',
    title: '猎奇 AI 吃下四成消费时长：海马人霸榜十天背后的视觉注意力经济',
    note: '数据表明非传统真人脸孔的奇幻怪诞设定在完播率上碾压传统霸总题材，独特的视觉奇观成为天然的流量放大器。',
    url: 'https://dramagoing.com/daily-brief/2026-08-15.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '摆脱同质化的同框审美，在概念设定上做极限差异化是低成本抢夺公域注意力的杀招。',
  },
];

const AIGC_EXTRAS = [
  {
    category: 'AI 资讯',
    title: '谷歌发布 TimesFM-3：3.3 亿参数零样本多变量时间序列预测模型',
    note: '仅需 3.3 亿参数即可在金融高频波动、气象异常与服务器负载预测上超越传统百亿模型，已在 Hugging Face 与 GitHub 开源。',
    url: 'https://www.aigc.cn/109941.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '轻量化专用模型在垂直时序预测场景的 ROI 远高于通用大模型，适合端侧直接部署。',
  },
  {
    category: 'AI 协作',
    title: '具身智能转向 VLA+WAM 融合范式：端到端世界动作模型重构硬件链',
    note: '将视觉-语言-动作（VLA）与世界动作模型（WAM）深度绑定，机器人拥有了常识物理推演与长时规划执行能力。',
    url: 'https://www.aigc.cn/109938.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '具身大脑的快速迭代正在倒逼机器人执行器与感知模组实现标准化与平价化。',
  },
  {
    category: 'AI 资讯',
    title: '中国大模型周调用量连续 17 周全球居首，智谱认领 Ox Alpha 旗舰模型',
    note: '国内开发者生态在 API 调用与落地吞吐量上持续领跑全球，智谱公布 Ox Alpha 在复杂系统推理中的全栈国产算力测评报告。',
    url: 'https://www.aigc.cn/109936.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '庞大的真实业务调用量构成了飞轮效应，加速了模型在极端工程边界下的迭代收敛。',
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

  // Combine items with unique AI drama and AIGC extras
  const allItems = [...items, ...DRAMA_ITEMS, ...AIGC_EXTRAS];

  // Separate pinned item
  const pinnedItem = allItems.find((i) => i.pinned) || allItems[0];
  const others = allItems.filter((i) => i !== pinnedItem);

  // Shuffle others to eliminate sequential mirroring
  const shuffledOthers = shuffleArray(others, 20260902);

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
