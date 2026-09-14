import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_14 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '竖屏短剧成了所有渠道标配：TikTok 开设一级入口，五大流媒体集体跟进',
    note: 'TikTok 把 Short Dramas 推成主界面一级按钮，Netflix/Disney+/Peacock/Prime Video/HBO Max 五大流媒体集体上线竖屏短剧入口。渠道收口正在抬高创作与货架门槛。',
    so_what: '短剧从独立 App 生意演变为全渠道的基础形态；对创作者而言，立项时想清楚不同入口的货架逻辑与分发适配，比盲目堆量更重要。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/daily-brief/2026-09-14.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok新增短剧专属入口，已有5亿+播放爆款跑出',
    note: '深度拆解 TikTok 站内短剧一级入口：通过话题聚合、排行榜与算法冷启动，让中腰部优质 AI 漫剧快速突破冷启动流量池。',
    so_what: '平台建立中心化流量货架后，流量分配更加公平透明；善用入口标签和前三秒反转钩子，中小型工作室同样能抢占头部曝光。',
    source: 'baijing.cn',
    url: 'https://www.baijing.cn/article/56526',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '马栏山东麟影视AI转型实测：制作成本降超80%，AI短漫剧年产500部',
    note: '传统影视团队全面拥抱生成式管线实录：真人实拍单部成本 15-25 万美元，转向 AI 工业化生成后降至 1-2 万美元，生产周期从按月缩短至按周。',
    so_what: '生产力工具的代际差带来绝对维度的成本碾压；尽快重构全流程 AIGC 制片标准，才能在新一轮全球影视工业革命中立于不败之地。',
    source: 'changsha.cn',
    url: 'https://news.changsha.cn/xctt/html/110187/20260727/227887.shtml',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '美国五大流媒体巨头全部“竖”起来，传统平台集体TikTok化',
    note: '深度拆解 Netflix、Disney+、Peacock、Prime Video 与 HBO Max 竖屏短剧布局：从片库 AI 剪辑到原创竖屏试水，争夺碎片化注意力。',
    so_what: '流媒体集体下场把短剧推向主流舞台；创作者需要学会为不同平台的竖屏货架定制节奏，在红海中抢占差异化身位。',
    source: 'kchuhai.com',
    url: 'https://www.kchuhai.com/report/view-67586.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '《封神2》的剧本没什么问题，问题出在哪？',
    note: '深度探讨工业化视效大片在剧作层面的节奏断层：当高密度视效轰炸掩盖了角色的内在动机与情感弧光，观众往往只剩下疲惫。',
    so_what: '视效与算力越繁荣，越凸显扎实人性情感的稀缺；切莫让炫目的技术奇观喧宾夺主，人物的内在困境才是牵引心智的真正磁石。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/770',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '长篇叙事史诗《麦芒》破15亿：以小人物命运讲好有温度的故事',
    note: '解构跨周期现实主义作品的情绪密码：如何避免空洞的说教，完全通过具体个体的生存挣扎与微小胜利，唤醒全社会的深度共情。',
    so_what: '宏大叙事必须落在具体的情感微澜上；学会把抽象的时代命题拆解为角色可感知的日常抉择，你的故事才能跨越阶层引发回响。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/930',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '国家广电总局发布微短剧管理提示：题材立项与叙事合规深度解读',
    note: '系统梳理微短剧监管政策新规：严管低俗猎奇、拜金主义与虚无历史，鼓励现实题材、正向情绪价值与工业化精品剧集。',
    so_what: '政策监管不是创作的紧箍咒，而是促进行业洗牌的正规军通道；及早对齐合规主线，才能在政策风暴中安全做大。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/830',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '全国微短剧重点规划备案公示解析：题材分化与审美进阶',
    note: '全景透视数百部最新备案剧目风向：战神与赘婿等粗糙爽剧套路锐减，现代科幻、职场反转与轻喜剧等多元高概念题材异军突起。',
    so_what: '观众的心智正在迅速审美升级；沉迷于过时套路只会加速被市场淘汰，积极探索高概念设定与复合叙事结构才能赢得下一波红利。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/810',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '一个快被遗忘的入口，突然被AI大厂抢疯了',
    note: '豆包输入法正式推出 Windows 版补齐全平台：分析大厂为何从单纯对话框转向输入法这一无处不在的底层物理入口。',
    so_what: '最无敌的用户黏性来自对日常高频动作的静默接管；与其强迫用户打开独立应用，不如将大模型能力无缝嵌入每次击键之中。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462430.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: 'GPT Image 2.5 正式上线：随手一画就能出图，交互范式再进化',
    note: 'OpenAI 悄然上线 GPT Image 2.5，生成速度与细节表现全面进化，引入即时涂鸦草图画布与多轮局部修改能力。',
    so_what: '从死板的纯文字提示词迈向“笔触草图+即时反馈画布”，下一代创作工具的核心竞争力在于人机共创的心流顺畅度。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462418.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'AI 编程助手总在“失忆”？面向 Agent 的上下文长期记忆层实践',
    note: '直面 Coding Agent 跨会话失忆与知识断层痛点：剖析面向智能体的上下文统一文件系统与长期记忆组织方案。',
    so_what: '智能体的上限不仅取决于单次推理智商，更取决于状态持久化与记忆流转效率；优秀的记忆架构是复杂多代理系统的胜负手。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462278.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '从思维链到对抗推理：OpenAI 首席科学家论异类智能与对齐边界',
    note: 'OpenAI 首席科学家 Jakub Pachocki 撰文《一种异类智能》，深度探讨深度思维链模型中的失控隐患与多层对抗对齐防线。',
    so_what: '随着模型自主推理能力的超常规演化，产品设计者必须从“设计提示词”升级为“设计不可篡改的系统状态守卫者与安全断路器”。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6462130.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // AI 协作 (1)
  {
    category: 'AI 协作',
    title: 'Simon Willison 发布 commit-rewriter 0.1：清洗 Coding Agent 提交历史',
    note: '专门用来批量清洗编程代理在 Git 提交历史中遗留的杂乱会话日志与私有 Issue 索引，提供可视化交互界面与一键回滚机制。',
    so_what: '当智能体编写了大部分代码，人类的核心职责正在转变为“代码卫生与工程边界审计”；规范的提交历史是团队可维护性的底线。',
    source: 'simonwillison.net',
    url: 'https://simonwillison.net/2026/Sep/14/commit-rewriter/',
    media: 'https://static.simonwillison.net/static/2026/commit-rewriter.webp',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-14.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_14);

console.log(`Day 2026-09-14: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_14.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-14',
  title: '9 月 14 日 · 触达重构与隐性渗透：当大模型退居幕后',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：ChatGPT 电话接入实时语音接口、豆包输入法攻占全平台底层入口、TikTok 上线 Short Dramas 一级按钮五大流媒体跟进、Simon Willison 发布 Agent 提交历史清洗工具。`,
  draft: false,
  epigraph: '最深远的技术渗透，从来不是让用户专门打开一个新窗口，而是让旧入口拥有新心智。',
  lead: '今天的技术与商业脉搏正在发生一场深刻的“阵地转移”：过去两年，全行业都在卷网页端和大模型专属 App 的独立流量，但今天的标志性事件表明，巨头们开始全面回防无处不在的“底层物理入口”——OpenAI 通过 GPT-Live SIP 正式将实时语音能力接入传统电话线路，让 AI 摆脱 App 限制渗透进最底层的通话通道；字节跳动旗下的豆包输入法完成全平台补齐，把大模型隐匿在每一次击键与文本输入中；而在内容消费端，TikTok 更是直接在主界面并排上线 Short Dramas 一级按钮，引来北美五大流媒体全面跟进竖屏入口。无论是系统输入、电信网络还是顶级流量分发货架，AI 正在从喧嚣的“前台表演者”演变为“不可或缺的底层水电”。',
  scene: '「你们为什么要把大模型做进输入法和电话线里？」「因为普通用户不会天天想着换一个新的 AI 客户端，但他们每天都要打字、都要接电话。把智能藏在他们已经形成肌肉记忆的入口里，才是真正的无声颠覆。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

过去很长一段时间，大家都在比拼谁家的 AI 独立客户端日活更高，谁能在对话框里回答更多刁钻的问题。但今天这几条看似平淡却极具杀伤力的动态提醒我们：**AI 的下半场，是一场关于“隐形化与渠道收口”的阵地战。**

无论是电话拨号盘上跑起的 GPT-Live SIP，还是桌面与移动端键盘背后默默辅助的输入法智能体，它们不再试图把用户拽进一个孤立的黑盒窗口，而是悄无声息地嵌在用户的必经之路上。在内容端，短剧出海同样经历着从“到处买量试水”到“各平台开设一级货架”的收口过程。当分发被标准化、基础设施被巨头接管，留给独立开发者和产品人的破局点，唯有极具确定性的精准场景与深度的本地化叙事。

**与其做一个功能繁琐、需要用户建立新认知的“庞然大物”，不如做一把锋利的微型手术刀，嵌在最顺手的缝隙里。** 愿今天的 ${finalItems.length} 篇精选资讯，能为你厘清真实的生态流向，在底层范式迁移中看清未来的立足点。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-14.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
