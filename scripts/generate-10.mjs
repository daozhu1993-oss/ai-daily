import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_10 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '监管立规矩，好莱坞也下场：短剧出海走到"能算账"的拐点',
    note: '9月双重风向标：国内微短剧新规AI强制打标叫停诱导刷剧，同时好莱坞明星凯文·哈特携20部原创短剧下场，短剧正式迈入工业化与能算账的成熟阶段。',
    so_what: '行业野蛮生长期彻底终结，监管筑牢底线、大工业抬高天花板；草莽团队必须转向精细化合规与成熟管线制作。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-10.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'Seedance 2.0 + Seed Audio + Vigloo：一个人够用的 AI 漫剧武器库',
    note: '盘点个人创作者高人效闭环管线：从画面运镜生成、多语种拟真配音到海外发行分账，一套轻量级工具栈即可撑起完整工作室。',
    so_what: '工具链的深度整合释放了超级个体的能量；把不同模型串联成高复用自动化流水线，一人也能拥有媲美小型影视公司的工业产能。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/ai-drama-arsenal.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok Mini Dramas：主App内嵌短剧，独立App的最后一场仗',
    note: '巨头生态闭环正在蚕食独立短剧平台生存空间：TikTok 直接在主站内嵌短剧流并打通支付，第三方平台面临流量断供危机。',
    so_what: '平台规则永远在变，不要押注单一独立 App 渠道；紧跟超级 App 的内嵌生态红利，做原生供给者才能免受挤压。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/mini-dramas-embedded-analysis.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '6月分账战报：$2800万再创历史新高，AI漫剧占比突破40%',
    note: '拆解出海短剧平台官方分账报告：AI 漫剧因极高投入产出比与快速回本周期，占据了头部平台近半收益份额。',
    so_what: '数据是最有力的商业自证；AI 漫剧不再是边缘实验，而是真正能产生大额现金流的支柱型内容品类。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/june-payout.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '《哪吒之魔童闹海》在剧本创作上的成功之处',
    note: '剖析现象级国漫续作的剧作精髓：如何在继承前作人物弧光的基础上升级核心矛盾，用更高烈度的伦理与命运冲突抓住全年龄层。',
    so_what: '爆款续集绝非简单的要素堆砌，必须在人物信念与世界观边界上做极限施压；故事的张力来自不可调和的深层价值对抗。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/768',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '犯罪、悬疑、刑侦类影视剧涉及的法医鉴定编剧素材',
    note: '刑侦与悬疑微短剧必备硬核知识库：从死亡时间推断、伤痕形态到物证比对链条，避免逻辑硬伤导致观众瞬间出戏。',
    so_what: '细节的真实感是悬疑剧的第一生命线；硬核专业设定的准确性能够极大提升作品的质感与厚重度。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/766',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '行业视角下爆款探案题材剧的创作逻辑与破局之道',
    note: '解析近年来高口碑破圈探案剧的核心范式：如何平衡社会派现实隐喻与本格派推理爽感，建立高黏性双主角羁绊。',
    so_what: '案件只是剖析人性的手术刀；真正让观众念念不忘的不是诡计本身，而是案情背后折射出的社会时代痛点。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/814',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '2026平台微短剧、漫剧官方内容审核规则一览',
    note: '权威归纳主流平台最新内容红线与过审指引：涉及价值观引导、暴力尺度与违规导流的重点避坑全指南。',
    so_what: '懂审核规则才能保护创作心血；把合规意识前置到大纲与分镜阶段，是职业创作者的基本素养。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/910',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '苹果迟到6年的折叠屏，打了所有“创新焦虑者”的脸',
    note: '深度探讨技术成熟度与商业落地节奏的权衡：为什么苹果总在供应链与用户心智彻底成熟时才切入，从后发制人看产品节奏感。',
    so_what: '盲目抢跑容易沦为市场先烈，精准切入才能定义品类标准；成熟产品经理懂得克制创新的冲动，等待系统级优势成型。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6462554.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '用 AI 做项目，怎么避免“屎上雕花”？',
    note: '直击团队用 AI 赋能的典型误区：业务核心逻辑千疮百孔却试图靠大模型包装遮羞，分析如何把 AI 真正用到业务承重点上。',
    so_what: 'AI 只能放大现有业务的价值，无法拯救失效的商业底层；先理顺真实的业务流，再去谈技术智能化。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462106.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '换皮肤、上直播、养桌宠，AI办公开始卷情绪价值？',
    note: '观察协同工具在功能同质化后的突围尝试：在严肃生产力场景中引入情感陪伴与游戏化机制，是伪需求还是新抓手？',
    so_what: '工具不仅要解决效率问题，还要解决人的心理疲劳；在高压的数字化办公环境中，情绪体验正成为关键的产品差异化要素。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462342.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'AI标识、版权存证、跨境互操作：AI痕迹追踪催生哪些新生意？',
    note: '解读全球监管落地催生的基础设施机会：当生成式内容必须全链路打标，水印追踪、溯源存证与合规验证成为高成长性赛道。',
    so_what: '政策与合规的收紧往往伴随着万亿级的企业服务蓝海；提前布局合规底座的团队，将成为新周期的卖水人。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6460015.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-10.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_10);

console.log(`Day 2026-09-10: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_10.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-10',
  title: '9 月 10 日 · 秩序重构与心智沉淀：当合规筑牢底盘，产品回归克制',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：短剧监管立规矩与好莱坞进场、苹果折叠屏的产品克制哲学、微短剧平台审核红线、AI办公的情绪价值突围。`,
  draft: false,
  epigraph: '粗放狂奔的红利终会见底，当规则与巨头同时筑牢底盘，最值钱的不是抢跑的姿态，而是耐得住寂寞的商业克制。',
  lead: '今天的技术与商业脉搏正在步入深水区的秩序重构：在微短剧赛道，《微短剧发展管理办法》正式落地推行 AI 内容强制打标，叫停粗暴的算法诱导，而好莱坞顶级班底则携原创短剧加速下场，标志着内容出海正式告别“野路子”，进入“能算账、拼工业”的成熟拐点；在硬件与产品端，苹果迟到六年的折叠屏以极度克制的供应链成熟度打破“创新焦虑”，印证了商业竞争从不奖励盲目抢跑，真正能穿越周期的，始终是在业务承重点上做深做透的系统性壁垒。',
  scene: '「监管打标一收紧，很多小团队都慌了？」「慌的是搞擦边抽卡的。规则立住了，好莱坞明星和海外主流预算才敢大笔进场，能算清账的团队好日子才刚开始。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

任何一个新兴产业的演进，都会经历从野蛮生长到规则重塑的惊险一跃。今天我们看到的，正是这样一场集体清醒：国内微短剧新规对 AI 内容强制打标并叫停诱导算法，好莱坞主流班底与资本全面进场；硬件端苹果折叠屏的克制后发，软件端协同工具对“屎上雕花”的反思与情绪价值的探索——无一不在释放同一个信号：**单纯依靠信息差与投机抢跑的红利已经枯竭，商业竞争正在全面退守到真实交付力、合规壁垒与用户深层心智的阵地上。**

对于产品人与独立创业者而言，合规与工业化从来不是创新的紧箍咒，而是洗牌期里最好的护城河。当盲目加杠杆的投机者被挤出牌桌，懂得在规则框架内深耕特定受众、把每一个分镜与每一行代码都紧贴业务现金流的务实团队，才拥有了不可替代的定价权。**不要在浮躁的焦虑中盲目狂奔，克制、精准、守住承重墙，才是小团队跑赢大周期的唯一解法。**

愿今天的 ${finalItems.length} 篇精选资讯，能为你厘清喧嚣背后的底层脉络，在秩序重构的时代从容落子。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-10.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
