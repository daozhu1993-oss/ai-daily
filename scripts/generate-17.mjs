import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_17 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '短剧出海不仅是翻译配音：实测全场景 AI 换脸与数字重制工具',
    note: '人人都是产品经理深度复盘：短剧出海正从粗暴的“外挂外语字幕”进阶至全剧人物面容、文化场景与口型语调的 AI 级重映射，实现真正意义上的本土化沉浸。',
    so_what: '单纯的译制搬运红利已近枯竭；谁能掌握全场景角色资产重映射工具链，谁就能用最低边际成本让一套爆款剧本吃透全球多语言市场。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465685.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok 官方微短剧战报：单月分账破 2200 万美元，本土 AI 剧分成飙升 112%',
    note: '官方最新分账生态拆解：平台月度分成破 2200 万美元大关，本土原创 AI 剧首次成为营收第一大板块，超 12 部 AI 互动短剧斩获单部 2 万美元爆款津贴。',
    so_what: '平台真金白银的流量与现金补贴正在坚定不移地流向 AI 漫剧；依托平台扶持政策深耕垂直高保真题材，是当下确定性极高的变现通道。',
    source: 'm.thepaper.cn',
    url: 'https://m.thepaper.cn/newsDetail_forward_33677383',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '国内亏八成与出海成暴利风口对照：AI 漫剧承制生态加速洗牌',
    note: '新浪深度调研：国内承制价从 1500 元/分钟断崖跌至 600 元，而海外 TikTok 小程序与 YouTube AI 频道的流量回报率高达国内 4 倍，团队正集体加速大迁徙。',
    so_what: '内卷红海的解药是全球化；与其在国内价格战中微利挣扎，不如把成熟的工业化分镜与自动化生成能力搬到海外高 CPM 流量池中变现。',
    source: 'k.sina.com.cn',
    url: 'https://k.sina.com.cn/article_7879923018_1d5ae154a01901h3nw.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '短剧出海增长逻辑换挡：从流量粗放采买到全链路“生态经营”',
    note: '澎湃新闻权威观察：短剧出海告别野蛮买量跑量阶段，全面进入“内容供给—用户承接—站内转化—商业闭环”的深水区，轻量化站内闭环成为新增长引擎。',
    so_what: '单纯依赖投放买量的套利空间正在迅速收窄；创作者必须具备产品化思维，将短剧视为具备留存与复购属性的数字消费品来精细化运营。',
    source: 'thepaper.cn',
    url: 'https://www.thepaper.cn/newsDetail_forward_33628836',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '夏衍电影编剧周启示：破除悬浮套路，让戏剧叙事重回现实主义文学温度',
    note: '国家级编剧盛会权威总结：聚焦二十届“夏衍杯”评审导向，提倡扎根当下普通人真实生活困境的细腻观察，警惕公式化冲突与为爽而爽的工业糖精。',
    so_what: 'AI 越能批量速成情节套路，观众对真实人间烟火的渴望就越强烈；唯有深入生活肌理的情感共鸣，才能成就穿越周期的经典故事。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/800',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: 'IMDb Top 100 佳作戏剧动力学：角色内在危机与不可逆转的终极抉择',
    note: '深度拆解影史高分神作的剧作规律：外在冲突往往只是表象，真正推动剧情狂飙的是角色内心世界信念的瓦解、道德困境与必须支付沉重代价的抉择。',
    so_what: '情节的反转只能带来几秒钟的感官刺激，人物的内心挣扎才能产生持久的心灵余震；在动笔之前，先想清楚主角不可妥协的灵魂底线是什么。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/778',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '小剧场驻场演出与年轻受众对话：沉浸式叙事如何抓住新一代观众',
    note: '传统戏曲与现代戏剧实验复盘：打破第四堵墙、重构观演距离，通过紧凑的节奏互动与微表情张力，让年轻观众在沉浸共情中主动参与戏剧推进。',
    so_what: '当代受众的注意力早已习惯了高频交互；无论是舞台小剧场还是竖屏短剧，编剧都必须学会把观众从被动看客转变为叙事的“在场见证者”。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/775',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '优秀电影剧本征集评析：打破模板化脸谱，构筑高辨识度人物弧光',
    note: '省级优秀剧本征集评委实录：详尽解析初筛中被淘汰剧本的通病（动机扁平、转折突兀），详解如何通过独特的言语节奏与次要缺点塑造立体人物。',
    so_what: '完美无缺的人物往往最乏味；敢于给主角赋予合情合理的弱点与执念，才能让角色的蜕变旅程拥有撕扯感与说服力。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/790',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: 'AI 办公 Agent 集中爆发，产品经理该如何跨越“演示惊艳到落地鸡肋”的鸿沟',
    note: '人人都是产品经理深度复盘：从会议纪要到多模态文档生成，分析办公类 Agent 在真实企业落地中遇到的权限隔离、幻觉容错与工作流断层瓶颈。',
    so_what: '不要迷信天花乱坠的 Demo 演示；衡量一款 AI Agent 价值的唯一标准，是它在真实企业闭环流程中能否扛住 99% 的异常边界情况。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465594.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '当 AI 劝你下单：电商导购 Agent 入口爆火与用户真实需求的温度差',
    note: '拆解各大电商平台竞相上线的 AI 导购助手：剖析为什么用户更习惯在传统搜索筛选列表里自主比价，而非与一个拟人化的 AI 导购长篇互动。',
    so_what: '交互界面的创新不能违背用户的决策心理学；AI 导购的破局点不是做成话痨客服，而是以极简形式在关键比价节点提供高确信度的决策依据。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465690.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '字节原业务增长负责人创业复盘：把剪映式“模版+爆款飞轮”搬进 AI 视频',
    note: '一线创业实操透视：揭秘如何将剪映已被验证的“爆款模板拆解—一键同款替换—社交链裂变”增长飞轮，复刻到生成式 AI 视频创作工具当中。',
    so_what: '底层生成模型是均质化的，但应用层的增长飞轮具有极高壁垒；降低普通用户的创作门槛、提供即拿即用的爆款模板，是破圈的最强杠杆。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465523.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '从 1.6 亿下载到集体关停：AI 情感陪伴产品为何“火得快，死得更快”？',
    note: '全景复盘多款曾经现象级 AI 伴侣应用的消亡史：算力成本与长文本 Token 消耗居高不下、用户情感疲劳迅速到来、付费转化与合规审查的双重夹击。',
    so_what: '高下载量不等于健康的商业模型；没有高 LTV 支撑的纯陪伴类产品在面临算力账单时脆弱不堪，产品经理必须在一开始就算清单位经济模型（Unit Economics）。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465490.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-17.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_17);

console.log(`Day 2026-09-17: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_17.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-17',
  title: '9 月 17 日 · 长程自主与全景画布：当 Agent 离线值守并重构工作记忆',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Anthropic 将离线长程任务 Cowork 合并进主入口、Claude 实装全屏文档幻灯片画布、Demis Hassabis 宣布成立 DeepMind 研究院、ChatGPT 探索对话式赞助商助手、短剧出海迎来全场景 AI 数字重制。`,
  draft: false,
  epigraph: '真正的生产力跃迁不是你在屏幕前看着 AI 快速打字，而是当你合上电脑入睡时，Agent 已经在云端替你跑完了跨部门协同并排好了明日待审决策。',
  lead: '今天的科技演进正在清晰地跨越“人机协同”的临界点：在产品架构顶层，Anthropic 正式将支持长程离线值守的 Cowork 深度合并进 Claude 主入口，用户不再需要守着网页等回答，AI 可以在断网关机状态下在云端自主阅读几十份文档并产出完备报告；与此同时，Claude 原生实装了可在线全屏演示、多人协同批注的文档与幻灯片交互画布（Artifacts 升级版），彻底把对话框升级为全功能生产力工作台；而在商业变现端，ChatGPT 正式测试具备双向问答能力的对话式品牌助手，颠覆传统展示广告；在影视内容端，短剧出海跨过简单的译制搬运，进入全场景角色资产 AI 重映射时代。从离线长任务执行到全屏协作画布，软件正在从被动响应的工具，演化为全时段并行的生产伙伴。',
  scene: '「你昨天下班前丢给系统的那个跨部门数据审计跑完了吗？」「昨晚合上电脑我就没管它，今早一打开，Claude 已经在全景画布里把异常账目标记好，连汇报用的幻灯片和执行摘要都全自动排版好了。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 Anthropic 把支持离线长程运行的 Cowork 正式合并进 Claude 主界面，并端出可全屏演示协同的文档与幻灯片交互画布，整个行业正在经历一次静水深流的质变：**AI 正在从“一个需要你紧盯屏幕等待回复的对话气泡”，蜕变为“一个自带工作记忆、离线执行、并拥有完整生产工作台的数字合伙人”。**

过去两年，我们被困在对话框的方寸之间，被动地输入提示词、等待流式打字、复制粘贴代码。但真实世界的高价值工作从来不是一问一答的快问快答，而是需要数小时研读复杂上下文、多轮自我校验、最终产出结构化决策方案的长程工程。这也是为什么短剧出海领域正在发生颠覆——简单的翻译字幕没人看了，真正的玩家正在用 AI 重构全场景的角色面孔与文化语境；这也是为什么产品经理们不再为虚幻的 AI 伴侣买单，而是将目光锁定在能跑通企业真实异常边界的垂直 Agent。

**工具正在隐形，但你的业务护城河必须愈发清晰。** 当算力与生成能力成为平价水电，唯有对用户痛点的深刻洞察与不可替代的审美品味，才能穿越技术的狂暴迭代。愿今天的 ${finalItems.length} 篇前沿资讯，为你锚定下一阶段的思考坐标。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-17.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
