import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const ISSUE_METAS = {
  '2026-08-28': {
    title: '8 月 28 日 · 驱动标准化与全链路自动化：当 Agent 开始接管现实设备',
    highlights: '全网 7 大领域 60 篇高密度精选：Anthropic MHS 硬件协议、OpenClaw 开源生态、Qwen 架构开源与一人公司实战。',
    epigraph: '协议决定边界：当 Agent 开始插上现实硬件的插头，软件的垄断神话正在被一个个轻量智能体瓦解。',
    lead: '今天全网的技术脉搏呈现出极强的一致性：单向对话式大模型的参数军备竞赛正在降温，真正的战场全面转移到「如何让 AI 丝滑连接现实世界的工具链与硬件设备」。从 MHS 驱动层标准到个人助手 OpenClaw 的爆发，AI 正在从封闭的聊天框走向无处不在的后台微执行层。对产品人而言，与其在应用层重复造大而全的轮子，不如用故事思维把特定人群的微任务串联成自动化流。',
    scene: '「你的新产品怎么两周就打通了 20 多个企业服务？」「我没写一行定制对接代码，全挂了开源驱动协议，给 Agent 塞了份规则守则它自己就跑通了。」',
  },
  '2026-08-27': {
    title: '8 月 27 日 · 极致性价比与模型轻量化：开源基座的算力重构',
    highlights: '全网 7 大领域 60 篇高密度精选：GLM-5.3-Flash 降本十倍、多模态智能体演进、微型产品变现与设计系统。',
    epigraph: '代码负责把产品做出来，而叙事决定它能走多远、能卖多贵。',
    lead: '昨天跟一位做了 8 年传统 SaaS 的老兵交流，他最大的困惑是：为什么现在年轻人用两周搓出来的 AI 包装产品，能在 Product Hunt 上拿第一，而自己性能强十倍的系统却无人问津？答案很简单：在模型平权时代，功能不再稀缺，注意力与信任才是真正的硬通货。',
    scene: '「这个产品的核心壁垒是什么？」「没有壁垒，但我给它讲了一个让 10 万人热血沸腾的转型故事。」—— 某 AI 独立产品创始人在播客中的坦白。',
  },
  '2026-08-26': {
    title: '8 月 26 日 · 意图交互与工具规范的博弈：规范是分裂还是优化',
    highlights: '全网 7 大领域 60 篇高密度精选：AGENTS.md 规范争议、端到端自动化流、极速排版与独立开发实战。',
    epigraph: '最高级的交互是无感的：你专注于意图，系统默默完成编排。',
    lead: '提示词工程（Prompt Engineering）大概是过去两年最反人类的过渡期产物。让普通用户在输入框里手写几十行格式规范，就像要求 90 年代的电脑用户必须在终端里敲汇编指令一样荒谬。未来的赢家必定属于那些将自然语言隐藏在直观动作背后的产品。',
    scene: '「用户要的从来不是 Prompt 模板，他们要的是点击一下，把一坨乱七八糟的会议录音变成可以直接发给客户的汇报 PDF。」',
  },
  '2026-08-25': {
    title: '8 月 25 日 · 智能体与物理世界的连接点：从界面生成到具身感知',
    highlights: '全网 7 大领域 60 篇高密度精选：多模态感知、无服务器边缘架构、独立出海产品与视觉排版美学。',
    epigraph: '工具的进化史，就是把复杂的认知负荷逐渐交由底层吞吐的历史。',
    lead: '从屏幕像素到物理传感器，智能体正在以前所未有的速度侵入现实世界的每一个角落。无论是独立开发者依靠边缘计算搭建的高毛利微型服务，还是影视创作者依靠多镜头分镜构建的数字剧场，创造者的杠杆从未如此巨大。',
    scene: '「一个人真的能维护全套跨国服务吗？」「当 CI/CD、客服问答和账单全交由 Agent 守护时，单人就是一家完整的跨国软件公司。」',
  },
};

for (const [date, meta] of Object.entries(ISSUE_METAS)) {
  const filePath = path.join(TARGET_DIR, `${date}.md`);
  if (!fs.existsSync(filePath)) continue;

  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) continue;

  const frontmatter = yaml.load(match[1]);
  frontmatter.title = meta.title;
  frontmatter.highlights = meta.highlights;
  frontmatter.epigraph = meta.epigraph;
  frontmatter.lead = meta.lead;
  frontmatter.scene = meta.scene;

  const newContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 60 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`✅ Updated editorial branding for ${date}`);
}
