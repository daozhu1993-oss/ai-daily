import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_15 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: 'TikTok 实测 Short Dramas 一级按钮：微短剧从信息流偶遇升级为主动检索',
    note: '欧美科技博主一手实测 TikTok 主界面与 Shop、Explore 并列的 "Short Dramas" 独立入口：支持分类标签（人狼/豪门/逆袭）、按热度与上新筛选。',
    so_what: '一级入口的落地意味着微短剧获得了中心化分发货架；创作者要学会“货架思维”，针对平台筛选标签做针对性题材布局。',
    source: 'trevordecker.com',
    url: 'https://trevordecker.com/2026/08/20/tiktok-adds-a-short-dramas-button-as-its-micro-series-push-expands',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: '文汇报：AI短剧出海提速，2026年市场规模料达400亿元',
    note: '权威媒体报道 DataEye 行业预测：中国厂商贡献全球短剧出海超九成收入，AI 生成技术驱动片量增长 5 倍，制作成本压缩至传统十分之一。',
    so_what: '产业从劳动密集型全面向算法密集型跃迁；掌握工业化 AIGC 生产管线的团队，将在 400 亿蓝海大盘中获得最大利润空间。',
    source: 'wenweipo.com',
    url: 'https://www.wenweipo.com/epaper/view/newsDetail/2080711508433702912.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok短剧上半年累计分账8200万美元，AI漫剧投放占大盘八成',
    note: '深度财务结构拆解：海外短剧投放 ROI 稳定在 1.1-1.3，AI 漫剧凭借高人效与零演员调度风险，在广告采买与自然推荐中占据绝对主力。',
    so_what: '数据验证了 AI 漫剧的商业确定性；不要在真人高昂的沟通成本中空耗精力，把资源集中在数字演员与情绪钩子分镜上。',
    source: 'xueqiu.com',
    url: 'https://xueqiu.com/1138151823/402701663',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'HBO Max 与 Xfinity 部署竖屏短片系统：主流流媒体的竖屏生存战',
    note: '梳理 HBO Max 运用 AI 工具将长剧片库智能切片为高光竖屏短剧的工程管线：把流媒体庞大库存转变为钩子密集的碎片化试吃拼盘。',
    so_what: '传统长视频与竖屏短剧的界限彻底模糊；善用 AI 重新拆解长叙事为模块化微单元，是盘活海量数字资产的高阶玩法。',
    source: 'real-reel.com',
    url: 'https://www.real-reel.com/hbo-max-story-tv-xfinity-vertical-drama',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '广电60亿精品微短剧计划：个人与小团队分羹指南',
    note: '官方扶持计划深度实操拆解：如何申报“微短剧+文旅/非遗/现代科技”专项扶持基金，中小团队如何通过正规渠道获取平台阶梯保底分账。',
    so_what: '扶持基金与政策倾斜是小团队跨越冷启动资金链断裂的最稳跳板；借政策之风深耕垂直精品，远胜在纯市场买量中搏命。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/902',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '马丁·麦克唐纳剧本全集与暗黑荒诞戏剧叙事母题',
    note: '精析现代剧作大师的冲突动力学：如何在封闭空间内通过极度荒诞而符合人性的对白，制造不可逆转的命运悲喜剧。',
    so_what: '荒诞不是胡编乱造，而是对现实困境的放大投射；掌握极致的冷幽默与刺痛人心的情节转折，是高级原创编剧的试金石。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/787',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '要从根本上解决“剧本荒”：影视工业化急需底层好故事',
    note: '直面行业算力爆发但优质剧本匮乏的核心矛盾：为什么技术工具能一键生成分镜，却写不出让人热泪盈眶的剧作内核。',
    so_what: '画面产能越泛滥，真正具备叙事张力与文学温度的剧本溢价越高；做守住故事灵魂的架构师，永远处于价值链顶端。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/769',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '全国剧本创作和剧作家现状调研报告：编剧职业化与生存账本',
    note: '十年行业数据追踪大起底：编剧稿酬周期、署名权纠纷、网剧分账现状与向短剧转型路径的真实生存镜像。',
    so_what: '看清创作市场的真实分配机制；告别单一被动等稿费的雇佣模式，通过 IP 参投和分账分成绑定长期收益。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/771',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '抖音上线「兴趣卡」：流媒体内嵌可交互 AI 微小程序的全新范式',
    note: '字节跳动在短视频推荐流中测试原生可操作的「兴趣卡」：用户在刷视频时无需跳出，即可直接在卡片内完成 AI 互动与轻量工具操作。',
    so_what: '信息流交互的升维颠覆：从单向被动消费跃迁为流内即时可计算，产品经理需要重新思考如何将复杂功能微型化、原生化。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463040.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '一年25万VS每月1500美元！大厂AI算力预算彻底分裂了',
    note: '黄仁勋定调英伟达员工年均 25 万美元 Token 预算，而 Uber 等传统互联网巨头却在严格缩减额度：揭示大厂在算力 ROI 上的剧烈博弈。',
    so_what: '算力泡沫终将面临财务大考；做 AI 产品的产品经理不能只谈想象力，必须讲清楚每一枚消耗的 Token 到底带来了多少真实业务增量。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463038.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '从“黄眉大王AI播客”到小鬼旅行对谈，视频播客长出“新物种”？',
    note: '拆解多模态 AI 对传统音频播客的视听重塑：通过数字人声线拟真与上下文动态配图，将单纯的“听觉经济”升级为沉浸式视听共振。',
    so_what: '单模态内容正在加速被全模态体验包围；善于将长文本/音频转译为多维感官触达，是内容产品打破增长天花板的关键武器。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463044.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '拿下世纪难题之后，OpenAI 形式化验证“重塑”数学科研边界',
    note: 'OpenAI 下一代前沿推理模型攻克克雷研究所千禧年数学难题：揭秘符号系统与深度学习结合下的自动化假设证明新范式。',
    so_what: 'AI 正在从概率性的“胡说八道”走向具备绝对严密证明的符号闭环；高确定性推理将为金融、密码学与基础科学带来范式重构。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6463042.html',
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

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-15.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_15);

console.log(`Day 2026-09-15: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_15.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-15',
  title: '9 月 15 日 · 系统级共生与多模态流：当 Agent 接管操作系统视界',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：Apple 重磅推 Siri AI 接管全局屏幕视界、ElevenLabs 统一多媒体 MCP 接口、抖音测试信息流交互「兴趣卡」、DeepMind 发布天气大模型 WeatherNext 3、Linear 推出自动化 Loops 引擎。`,
  draft: false,
  epigraph: '从“唤醒一个对话框”到“让 AI 随时看懂你正在注视的屏幕”，人机协作正完成从问答工具到数字共生体的惊险一跃。',
  lead: '今天的科技行业迎来了操作系统级 AI 的里程碑时刻：苹果正式公布新一代 Siri AI，不再满足于语音指令的被动应答，而是赋予其全局屏幕感知、跨应用邮件与照片图谱检索、以及深入系统底层的跨 App 自主操作能力，AI 终于拥有了“人类视线与数字手脚”；而在内容与分发生态，抖音全面灰度测试革命性的流内可交互「兴趣卡」，打破短视频单向播放的死水，让轻量 AI 微程序成为信息流原生内容；同一时间，ElevenLabs 将语音、音乐、图像与视频统一打包进标准化 MCP 协议，Suno 允许 AI 直接在多轨时间线上编曲。从底层操作系统的系统级接管，到流媒体内容的原生可编程化，大模型正在彻底粉碎旧时代的孤立软件形态。',
  scene: '「现在的系统助手和以前有什么区别？」「以前是你把文字粘贴给它求答案；现在是你停在任何界面，它已经看懂了你在看什么，并默默替你把接下来的三个跨应用操作全部排好了。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当苹果把 Siri AI 打造为一个能够“理解屏幕上下文、跨 App 调动系统权限”的真正个人智能体，当抖音开始在信息流里内嵌可实时交互的“AI 兴趣卡”，我们必须意识到：**传统意义上割裂的独立软件（App）时代正在不可逆地走向黄昏。**

过去十几年，移动互联网的核心逻辑是“造一个应用，圈一片领地，让用户留在里面”。但随着系统级多模态感知与 Agent 协议的成熟，用户的交互习惯正在被原子化瓦解——用户不再关心自己是在哪一个具体的 App 里，他们只关心“当前眼前的事情能否被最高效地达成”。无论是企业内部通过 Linear Loops 实现的无感流转，还是内容消费端抖音把应用直接做成可互动的卡片，界面的边界正在彻底消融。

**面对系统级智能体的横扫，单点功能的微小工具生存空间正在被快速挤压。** 真正能在这个新周期建立护城河的，唯有深度的专有业务状态流、极具情感穿透力的原创 IP 叙事，以及对特定垂类人群工作流的极致端到端封装。愿今天的 ${finalItems.length} 篇精选资讯，能陪伴你在这场界面大洗牌中看清本质，精准卡位。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-15.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
