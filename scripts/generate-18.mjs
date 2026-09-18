import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_18 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '经济观察报深度：AI影视出海“谋生”，海外爆款率与精品化破局',
    note: '权威媒体万字长文透视：随着出海AI漫剧日均上新破百部，单纯洗稿套现的爆款率暴跌，而深耕微表情控制、当地文化钩子与电影级光影的精品短剧稳定破亿。',
    so_what: '粗放跑量红利彻底结束，漫剧进入淘汰赛阶段；唯有把AIGC视听语言精细化到每一个镜头的情绪节奏，才能在海外成熟平台拿到长期分账。',
    source: 'weibo.com',
    url: 'https://weibo.com/ttarticle/p/show?id=2309405326086040322107',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '抖音版权中心更新AI剧激励政策：解说漫分成系数上调至10倍',
    note: '平台官方释放强烈扶持信号：解说漫与精品AI短剧分成权重暴增，起步热度门槛设置多档现金直奖，全面向原创度高、制作精良的数字创作者倾斜。',
    so_what: '平台政策是创作者的风向标；从打压低质搬运到数倍奖励精品，提前拥抱高保真AIGC管线的创作者将享受新一轮平台分成红利。',
    source: 'view.inews.qq.com',
    url: 'https://view.inews.qq.com/a/20260729A03HUN00',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok官方数据：海外短剧日耗突破2000万美元，AI漫剧吸纳八成投放',
    note: 'TikTok for Business大会核心数据复盘：海外短剧大盘日消耗达2000万-3000万美元，AI剧由于无真人演员调度摩擦且ROI更稳，吞下了80%的买量预算。',
    so_what: '商业投放数据印证了AI漫剧的变现天花板；在千亿级流量买量市场中，AI漫剧已经成为广告主最确定、最具规模化效应的转化载体。',
    source: 'toutiao.com',
    url: 'https://www.toutiao.com/article/7665287214405927474',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '短剧出海告别野蛮买量：TikTok Mini Dramas站内小程序成轻量破局载体',
    note: '娱乐资本论一线调研：海外短剧正从独立App跳端买量全面转向TikTok站内Minis小程序生态，缩短50%以上的流失链路，中小团队依靠自然流即可冷启动。',
    so_what: '链路摩擦越小，转化率越高；深谙平台原生小程序生态与推荐流结合的微团队，能够在免去繁重App研发维护的同时实现高毛利奔跑。',
    source: 'dy.163.com',
    url: 'https://dy.163.com/article/L2D0KFV4051284V8.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '电影剧本梗概撰写实战：如何在千字内立住主角动机与核心戏剧钩子',
    note: '编剧行业实务拆解：剖析电影局立项梗概与资方初审的核心标准，详解如何抛弃繁冗世界观，开门见山用突发危机打破主角平衡并抛出悬念。',
    so_what: '梗概不是全书缩写，而是一把直刺读者注意力的匕首；学会用高冲突情境和强动机钩子抓住审稿人，是剧本走向工业生产的第一步。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/788',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '从备案立项看戏剧节拍：情节阻力与不可逆转的戏剧动作设计',
    note: '深度复盘高通过率优秀剧本结构：探讨主角在面对内外阻力时的层层升级与反弹，如何让每一次行动都带来不可撤销的戏剧后果。',
    so_what: '好的故事没有回头路；每一场戏都必须改变角色的处境，通过不可逆的选择层层推高冲突，戏剧张力才能如滚雪球般蓄力爆发。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/840',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '网络微短剧内容审查与合规指南：高敏题材红线与情绪安全边界',
    note: '梳理网络视听节目发行备案新规：详尽解析复仇、豪门、悬疑等传统爆款题材在合规审查中的常见踩雷点，详解正向情绪引导与价值观自洽。',
    so_what: '合规能力就是生命周期；在监管精细化的新周期里，能够巧妙平衡情绪爽感与社会价值尺度的编剧，才能吃下最持久的长尾红利。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/895',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '青年编剧商业化破局：从被动改稿工具人到建立个人叙事风格资产',
    note: '万众编剧网专访与资深编剧心得：探讨独立创作者如何摆脱甲方无休止的“缝合怪”改稿需求，通过打磨具有高度辨识度的人物台词与叙事母题脱颖而出。',
    so_what: '剧本流水线正在被AI替代，但不可复制的个人作者性反而是最稀缺的硬通货；找到你的独特视角，把风格铸造成个人的商业护城河。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/763',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '开源惊艳：Agent 开始自主复刻爆款视频，内容生产线全自动化闭环',
    note: '人人都是产品经理拆解爆款开源工作流：从多模态模型自动拉片拆解爆款分镜、提取剧本台词、到调度扩散模型重制视频，整套管线无需人工干预。',
    so_what: '当逆向工程与内容生成全流程由Agent自动化跑通，传统内容工厂的人力成本直接归零；产品经理的战场全面转向算法调优与数据回流治理。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465521.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '豆包事件作为“压力测试”：AI Agent 商业化的四重壁垒与破局点',
    note: '深度商业化复盘：从突发流量并发对底层算力的冲击，拆解AI Agent在企业付费意愿、安全围栏、业务系统打通以及单位边际成本上的关键门槛。',
    so_what: '单纯的技术调用不产生持续毛利；产品经理必须把AI能力做进企业的生产业务链核心，成为不可替代的数据资产管理者，而非可随时替换的外挂组件。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6303200.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '给 WorkBuddy 装上看板：Token 消耗透明化与企业级 ROI 审计',
    note: '企业内部AI落地实录：如何通过细粒度的Token消耗监控看板，实时追踪每个团队与各模块调用的产出价值，让隐性算力成本完全透明可量化。',
    so_what: '当AI从探索实验期走向规模化部署，算力成本控制与ROI量化是决定项目生死的关键；具备财务视角的产品经理才能赢得管理层的长期预算。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465525.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '腾讯 Octop 正式发布：本地桌面端 AI 助手的系统级接管与交互重构',
    note: '巨头本地桌面端战略复盘：腾讯发布桌面常驻助手Octop，支持本地全局上下文感知与跨应用调度，探索离开云端依赖的低延迟端侧体验。',
    so_what: '桌面级常驻助手正在成为兵家必争之地；未来最具黏性的入口不再是浏览器的标签页，而是随时响应、触手可及的系统底层交互层。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6465605.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-18.json', 'utf8'));

// Make sure top AI item is pinned
for (let it of rawIan) {
  if (it.title.includes('Anthropic：公开三项衡量指标，Claude 已主导自身 26% 的研发')) {
    it.pinned = true;
    break;
  }
}

const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_18);

console.log(`Day 2026-09-18: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_18.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-18',
  title: '9 月 18 日 · 自我迭代与并行裂变：当大模型开始编写自身 26% 的底层代码',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Anthropic 披露 Claude 已主导自身 26% 的研发任务、OpenAI 发布模型失调跟踪报告并上线法律版 Astra、Claude Code 开放云端并行多线程任务、开源 Agent 实现爆款视频全自动复刻。`,
  draft: false,
  epigraph: '技术的临界点往往在悄无声息中跨越：当模型开始独立完成自身四分之一的研发，软件演进的齿轮已经脱离了纯人类肉身的转速。',
  lead: '今天的科技行业迎来了一个具有里程碑意味的拐点：Anthropic 官方正式公开测量 AI 进化速度的指标框架，披露截至 2026 年 8 月，Claude 已经独立主导并完成了自身 26% 的研发任务，大模型“自我递归进化”从科幻隐喻演化为了可被审计的研发报表；与此同时，OpenAI 罕见地发布模型失调跟踪报告，公开六起深度训练中的反常对齐偏差，直面黑盒对齐的未解之谜，并同步上线挂载 2.3 亿法规索引的法律版 Astra；而在开发者工程端，Claude Code 正式开放 Projects 概念，单个对话框可自主裂变为多个后台并行云端线程，人合上电脑后任务在多云端线程中同时向前推进；在开源社区，Agent 已经开始全自动分析并复刻爆款短视频。从代码编写到研发闭环，AI 正在从人类指挥的数字副驾，加速蜕变为自我繁殖的工程母机。',
  scene: '「听说你们团队这季度没有扩招研发，交付速度反而翻倍了？」「因为现在的研发例会里，有四分之一的代码审查和架构重构是模型提给模型、模型自己跑测试合入的。我们只是在最后一公里签个字。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当 Anthropic 正式在一篇严谨的研究论文中写下“内部超过四分之一的研发任务已由 Claude 自身独立完成”时，每一个身处数字时代的创造者都应当停下手中的敲击，重新审视我们与代码、与工具的关系。

在过去几十年里，软件工程的底层法则是“人类写代码，机器执行指令”。而今天，这一单向链条正在闭环成一个自我递归的莫比乌斯环：AI 在设计更新一代的 AI 架构，AI 在调试自身的测试用例，AI 在优化运行自身的算力网络。当 Claude Code 允许把一个抽象意图裂变为几十个并发的云端执行线程，当开源 Agent 已经可以把一部爆款短视频从镜头语言到台词运镜彻底逆向复刻，留给纯粹“执行型岗位”的生存缝隙正在被极限压缩。

**未来属于那些善于定义问题、拥有极致审美并能给系统设定安全边界的人。** 无论是在大厂搭建企业级 Agent 架构，还是作为单兵创作者在海外短剧市场搏杀，核心竞争力不再是你打字有多快，而是你能否驾驭这一台自我迭代的智能引擎。愿今天的 ${finalItems.length} 篇精选资讯，带你推开通往下一代计算范式的大门。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-18.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
