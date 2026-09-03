import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DATE = '2026-09-03';
const TITLE = '9 月 3 日 · 极速工作马与盈利短剧：当 AI 从演示走向真正赚钱';
const HIGHLIGHTS = '全网 9 大领域 66 篇高密度精选：谷歌 Gemini 3.8 Flash 自主查错改代码、ReelShort 破 10 亿美元盈利、自进化 Agent 搭建与两种剧本推演模式。';
const EPIGRAPH = '当一款工具不仅能把代码写完，还能自己把游戏玩通并修复 Bug，它才算真正接过了键盘。';
const LEAD = `今天全网前沿呈现出极强的「闭环执行」与「商业变现」拐点：谷歌突发上线 Gemini 3.8 Flash，在极低定价下首次打通了「玩游戏 ➔ 找错 ➔ 自主改代码 ➔ 验证」的完整自闭环，Cursor 当天无缝接入；在商业内容赛道，ReelShort 全年预估突破 10 亿美元并迈过年度盈利线，字节跳动全面搭起短剧分发生态，短剧出海正式从烧钱买量拐进扎实赚钱的阶段；人人都是产品经理与万众编剧网则分别输出了自进化 Agent 搭建框架与经典剧本推演方法论。各条战线正在以惊人的速度从概念演示收敛为可算账的生产力。`;
const SCENE = `「以前是把报错扔给 AI 等它猜；现在 Gemini 3.8 Flash 自己在终端里把游戏玩了三关，顺手提了个 PR 把闪退 Bug 修了。」`;

const VALID_CATEGORIES = new Set([
  'AI 资讯',
  '一人公司',
  '产品经理',
  '产品设计',
  '编剧技巧',
  'AI 漫剧',
  'AI 协作',
  '审美提升',
  '产品营销',
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

function shuffleArray(array, seed = 20260903) {
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

// 4 strictly unique AI drama items for 2026-09-03
const DRAMA_ITEMS = [
  {
    category: 'AI 漫剧',
    title: '从烧钱买量到能赚钱：ReelShort 破 10 亿营收，字节搭起短剧操作系统',
    note: 'MPA 预测 ReelShort 年度营收破 10 亿美金并首度实现年度盈利，字节跳动加速生态整合，短剧出海从买量换增长全面拐入利润收敛期。',
    url: 'https://dramagoing.com/daily-brief/2026-09-03.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '行业从博概率走向精细化运营，具备稳定产能与分发矩阵的团队将吃下最肥沃的利润。',
  },
  {
    category: 'AI 漫剧',
    title: '万播 10 元国内卷不动了：小团队的出口在海外，但规则也变了',
    note: '国内单价跌入微利区间，海外 TikTok 渗透率不足 1% 却提供了数倍于国内的分账溢价，小团队出海必须掌握多语种本地化与合规红线。',
    url: 'https://dramagoing.com/daily-brief/2026-08-12.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '地域套利是独立创作者对抗内卷的天然杠杆，尽早建立跨国分发渠道。',
  },
  {
    category: 'AI 漫剧',
    title: '戚薇回应 AI 授权“卖脸”争议：与其被别人拿走，更愿意主动出击',
    note: '知名艺人全面拥抱数字人分身与 AIGC 授权，首创官方合规面孔授权分账模式，为短剧与虚拟剧集提供了合法合规的高辨识度明星 IP。',
    url: 'https://www.aigc.cn/110050.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '明星肖像正版化为精品 AI 短剧扫清了侵权风险，品牌联动商单空间进一步打开。',
  },
  {
    category: 'AI 漫剧',
    title: '爆款包揽的时代过去了：TikTok 短剧增长全面流向腰部长尾创作者',
    note: '白鲸数据表明端原生短剧周增量破 52 亿，TOP30 头部仅占一成多，超过八成增量被垂直题材的腰部长尾小团队稳稳吃下。',
    url: 'https://dramagoing.com/daily-brief/2026-08-13.html',
    source: 'dramagoing.com',
    media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '去中心化算法让小团队不再受制于垄断，持续深耕垂直小众受众即可获得稳定长尾收益。',
  },
];

// Screenwriting Techniques (编剧技巧) from wzbj1616
const SCREENWRITING_ITEMS = [
  {
    category: '编剧技巧',
    title: '新人必看！两种最常见的剧本模式与情节推演公式',
    note: '经典「救猫咪」英雄之旅与「动机-阻碍-危机-顿悟」逆境结构深度拆解，故事写不下去时的万能解题钥匙。',
    url: 'https://www.wzbj1616.com/script_necessary_info/872',
    source: 'wzbj1616.com',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '剧本模式就是思维模型，熟练运用模式能让你在构思产品与短剧时少走 80% 的弯路。',
  },
  {
    category: '编剧技巧',
    title: '新人编剧 100 问：从人物小传、对白潜台词到节奏卡点全梳理',
    note: '系统整理剧本创作中最容易踩坑的几十个实战盲区，告别悬浮对白与扁平人设，建立立体的人物冲突张力。',
    url: 'https://www.wzbj1616.com/script_necessary_info/899',
    source: 'wzbj1616.com',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '对白的最高境界是「言在此而意在彼」，产品文案同样需要这种润物细无声的共情力。',
  },
  {
    category: '编剧技巧',
    title: '女性题材微短剧创作新思路与爆款案例剖析',
    note: '跳出传统复仇虐恋套路，聚焦女性成长与搞钱清醒人设，情绪价值与爽点释放机制深度拆解。',
    url: 'https://www.wzbj1616.com/script_necessary_info/839',
    source: 'wzbj1616.com',
    media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '情绪内核的进化反映了受众心理变迁，敏锐捕捉当代情绪痛点是打造爆款的核心密码。',
  },
];

// Product Manager (产品经理) from woshipm
const PM_ITEMS = [
  {
    category: '产品经理',
    title: '人人都能学会的自进化 Agent 搭建指南：从需求抽象到动态记忆闭环',
    note: '抛弃传统死板的预设工作流，利用 Reflect 与 Self-Correction 机制构建能够越用越聪明、自动修正 Bug 的生产级智能体。',
    url: 'https://www.woshipm.com/ai/6458985.html',
    source: 'woshipm.com',
    media: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '产品经理必须从「画静态交互图」升级为「设计智能体的状态机与进化机制」。',
  },
  {
    category: '产品经理',
    title: 'AI 时代，产品经理的落地实操方法论：如何把大模型塞进真实业务流',
    note: '拒绝自嗨式包装，从业务 ROI 评估、容错边界设定到冷启动数据闭环，拆解真正能为企业算过账来的 AI 功能落地套路。',
    url: 'https://www.woshipm.com/class/6456202.html',
    source: 'woshipm.com',
    media: 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '技术参数无法直接产生价值，只有嵌入具体工作流并解决确定性痛点才能形成付费壁垒。',
  },
  {
    category: '产品经理',
    title: '从 40 亿到 130 亿美元！中国大模型这波真实增长，可能和你想得不一样',
    note: '深入调研 API 调用流向与企业真实开支，揭示从通用对话向深水区垂直私有化落地的资金流向与市场结构剧变。',
    url: 'https://www.woshipm.com/ai/6458981.html',
    source: 'woshipm.com',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '看清真实的产业资金流向，避免将宝贵的精力浪费在伪需求和泡沫概念上。',
  },
];

// AIGC Extras
const AIGC_EXTRAS = [
  {
    category: 'AI 资讯',
    title: '遏制智能体失控：OpenAI 正秘密开发 AI 自动终止安全防护功能',
    note: '针对长程自主 Agent 可能出现的无限循环调用或越权操作，开发系统级异常熔断机制与人工强干预接口。',
    url: 'https://www.aigc.cn/110047.html',
    source: 'aigc.cn',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: false,
    so_what: '给狂奔的智能体装上安全刹车，是企业放心将核心权限交给 Agent 的前置条件。',
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
      if (spans.length > 0) {
        const rawCat = spans[0];
        if (VALID_CATEGORIES.has(rawCat)) {
          category = rawCat;
        } else if (rawCat.includes('AI')) {
          category = 'AI 资讯';
        }
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

  // Combine items with unique AI drama, screenwriting, PM and AIGC extras
  const allItems = [...items, ...DRAMA_ITEMS, ...SCREENWRITING_ITEMS, ...PM_ITEMS, ...AIGC_EXTRAS];

  // Separate pinned item
  const pinnedItem = allItems.find((i) => i.pinned) || allItems[0];
  const others = allItems.filter((i) => i !== pinnedItem);

  // Shuffle others to eliminate sequential mirroring
  const shuffledOthers = shuffleArray(others, 20260903);

  const finalItems = [pinnedItem, ...shuffledOthers];

  console.log(`✅ Total items with 9 categories: ${finalItems.length}`);

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

主理人编者按：今天精选的这 ${finalItems.length} 篇高密度一手内容，全面覆盖了 AI 资讯、一人公司、产品经理、产品设计、编剧技巧、AI 漫剧、AI 协作、审美提升与产品营销 9 大领域，希望能为你带来最扎实的认知启发与实战工具。
`;

  const targetFile = path.join(TARGET_DIR, `${DATE}.md`);
  fs.writeFileSync(targetFile, mdContent, 'utf8');
  console.log(`💾 Successfully generated ${targetFile}`);
}

run();
