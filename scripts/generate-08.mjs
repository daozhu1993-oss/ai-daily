import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_08 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '好莱坞也来拍竖屏短剧了：从流量玩法到主流生意',
    note: 'James Franco、Issa Rae 等好莱坞明星与资本成批涌入竖屏微短剧，Omdia 估测美国市场达 15 亿美元，短剧彻底从草莽流量玩法晋升为主流内容产业。',
    so_what: '顶流创作者与传统工业资本入场意味着内容品质与叙事门槛的迅速抬高，单纯拼快抽卡的时代终结，影视级专业叙事与工业化包装成为核心胜负手。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-08.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '真人短剧Q2缩水50%，AI短剧消耗占海外投放大盘80%+',
    note: '买量消耗数据揭秘行业剧变：高昂的实拍剧组成本被 AI 漫剧直接打穿，海外大盘投放预算以压倒性优势流向高周转的生成式漫剧。',
    so_what: '生产力成本的代际差就是最残酷的商业降维打击；掌握 AI 漫剧全链路制作的人群，正在以数倍的利润率吞食传统影视外包的份额。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/ai-replacing-real.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '红果 TOP10 里 7 个是 AI 漫剧，万兴 72h 拿 50 万：国内验证 + 公司去魅',
    note: '复盘国内头部短剧平台排行榜：AI 漫剧全面统治头部榜单，小团队凭借极致垂直的脚本与高频出产击穿传统影视制作大厂的神话。',
    so_what: '不要迷信大厂的资源壁垒，在全新的内容生产范式面前，所有人都站在同一起跑线；敢于打破传统流水线的小团队才能吃到最肥沃的头啖汤。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/domestic-proof-vs-company-myth.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '邮箱入驻、AI翻译17种语言、100倍激励——个人创作者最低门槛上车指南',
    note: '拆解 TikTok 官方创作者中心（Drama Center）的个人创作者激励政策：多语种一键本地化与全球分账机制实操教程。',
    so_what: '平台在跑马圈地阶段给予的流量杠杆最为慷慨；紧贴官方政策红利，以极低的试错成本跑通第一笔海外美金分账。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/drama-center-creator-guide.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '爆款动画微短剧创作全流程技巧',
    note: '从世界观设定、人物核心动机锚定，到 90 秒快节奏分镜切分与声音情绪铺陈的实操经验指南。',
    so_what: '动画漫剧的成败在于把控受众的情绪呼吸；学会用精炼的动作指令和强烈的视觉反差推动剧情，作品才能拥有持续抓人的魔力。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/848',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '《搏击俱乐部》（1999）的编剧分析：解构双重人格与不可靠叙述者',
    note: '深入剖析大卫·芬奇经典名作的剧本诡计：如何通过巧妙的视点误导与潜意识线索，在结局引爆颠覆认知的震撼余波。',
    so_what: '不可靠叙述是高级叙事的情感放大器；在内容中善用信息不对称与反转伏笔，能让受众在顿悟的瞬间获得极大的精神震颤。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/832',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '国产悬疑类网络剧空间与叙事的关系',
    note: '探讨封闭空间、阴雨天气与老旧筒子楼等具象环境在悬疑剧作中对角色心理压迫感与命运锁死的隐喻构建。',
    so_what: '场景从来不是背景板，场景是有呼吸的隐形主角；在画面构思中赋予空间强烈的心理压迫感，剧情的戏剧张力就会不言自明。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/813',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '编剧新闻事件改编“四重雷区”深度剖析',
    note: '剖析真实事件影视化中的法律版权侵权、伦理过度消费、事实失真与戏剧扁平化四大核心深坑。',
    so_what: '真实故事是灵感的富矿，也是伦理的雷区；学会提炼人性内核而非粗暴照搬事实细节，创作才能拥有恒久的艺术尊严。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/931',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '从城乡规划到 AI 产品经理：我重新理解了“规划”这件事',
    note: '一位跨界 PM 的深度自白：做 AI 产品就像城市规划，你无法控制每个市民（用户）的每一秒行为，但你可以设计出最具导向性的骨干路网与基础设施。',
    so_what: '摆脱微观控制欲是设计现代智能系统的起点；好的产品架构是提供肥沃的土壤与通畅的动线，让用户的创造力在其中自然生长。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6451275.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '功能的守门人、时间的守卫者、机会的追逐者：产品经理的三角困局',
    note: '深入剖析 PM 日常面临的灵魂拷问：在质量底线、交付工期与业务新机会之间，如何做出不让团队崩溃的平衡决策。',
    so_what: '权衡取舍是产品经理唯一的硬核手艺；学会在混乱的输入中建立清晰的优先级标尺，才能带领团队打赢每一次关键战役。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6420088.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '开发1小时，部署5小时：PM想做OPC，应用上线经验分享',
    note: '一位产品经理尝试单兵运营一人公司（One Person Company）的心酸与蜕变：当代码生成变得容易，域名、鉴权、支付与 CI/CD 部署才是真正的沼泽。',
    so_what: '一人创业的痛点早已不在开发端而在交付运维端；尽早搭建自动化部署模板，把非核心摩擦力全部收拢，单人业务才能长久稳定。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6460579.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '腾讯阿里半年砸千亿，AI重构大厂护城河的代价是什么？',
    note: '深度透视国内互联网巨头在算力军备竞赛中的战略焦虑与财务承压：高昂的 Capex 资本开支如何倒逼业务线寻找高确定性的变现出口。',
    so_what: '大厂的巨额基建投入是小团队的杠杆红利；看清巨头的成本压力与生态走向，在巨头看不见或懒得做的纵深垂直场景里深耕，生存空间无限宽广。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6459687.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-08.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_08);

console.log(`Day 2026-09-08: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_08.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-08',
  title: '9 月 8 日 · 资本进场与分镜提权：当好莱坞拍起微短剧，小团队深耕重资产',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：好莱坞竖屏短剧爆发、AI漫剧海外消耗超80%、产品经理三角困局破解、动画短剧创作SOP与一人公司OPC实战。`,
  draft: false,
  epigraph: '喧嚣属于流量的追逐者，而红利永远属于把剧情逻辑、商业交付与交付底座跑成一体的笃行者。',
  lead: '今天的信号展现出鲜明的“重工业下场”特征：在影视端，好莱坞一线主创与资本集体入局竖屏短剧，红果与海外投放大盘中 AI 漫剧占比突破 80%，标志着短剧彻底告别野蛮生长的草莽期，跨进专业工业化比拼的新周期；而在软件工程与产品端，大厂砸千亿重构生态，单兵开发者用 OPC（一人公司）架构打通部署，功能的守门人正在转型为商业闭环的架构师。不论是拍片还是写代码，最硬核的壁垒重新回到了对人性的理解与对确定性交付的较真。',
  scene: '「好莱坞大导也要来抢竖屏饭碗了？」「他们带来了千万预算，但我们有日产十集的分镜流水线和二十套逆境转折脚本。战场不在画幅大小，在谁懂前五秒的人性。」',
  cover: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当好莱坞名导与传统大资本成批涌入竖屏短剧赛道，很多人以为小团队的生存空间被压缩了；但真相恰恰相反——大船进场把整个水池搅热了，而真正能够快速转身、以极致敏捷抢占细分生态位的，永远是那些打通了 AI 工具链的微型车间。

不论是红果榜单上 AI 漫剧对真人短剧的快速替代，还是单兵产品经理借助自动化流水线完成从 PRD 到商业化收单的完整闭环，都在印证同一个逻辑：**资本可以买来昂贵的演员和豪华的机房，但买不来对用户微小情绪波动的敏锐嗅觉；把故事讲透、把产品做实，这些深扎地面的笨功夫，就是我们最坚固的防波堤。**

愿今天的 ${finalItems.length} 篇精选资讯，能成为你今天敲下第一行代码、写下第一个分镜剧本的灵感起点。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-08.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
