#!/usr/bin/env node

/**
 * 每日 AI 日报 · AI 起草脚本 (scripts/draft.mjs)
 * 
 * 职责：
 * 1. 拉取/读取候选条目与公开数据源。
 * 2. 调用大模型（带「岛主声音」写作指南与严格 Schema 约束）。
 * 3. 产出符合 src/content/daily/ 格式的草稿 markdown 文件（永远为 draft: true）。
 * 4. 彻底与站点前端构建解耦。
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, '..');

// 简易 .env 解析
function loadEnv() {
  const envPath = path.join(projectRoot, '.env');
  if (fs.existsSync(envPath)) {
    const content = fs.readFileSync(envPath, 'utf8');
    content.split('\n').forEach((line) => {
      const match = line.match(/^\s*([\w.-]+)\s*=\s*(.*)?\s*$/);
      if (match) {
        const key = match[1];
        let val = match[2] || '';
        val = val.replace(/^['"](.*)['"]$/, '$1').trim();
        if (!process.env[key]) {
          process.env[key] = val;
        }
      }
    });
  }
}

loadEnv();

// 参数解析
const args = process.argv.slice(2);
function getArg(name) {
  const prefix = `--${name}=`;
  const found = args.find((a) => a.startsWith(prefix));
  return found ? found.slice(prefix.length) : null;
}
const isForce = args.includes('--force');
const isMock = args.includes('--mock') || !process.env.AI_API_KEY;

// 默认日期为当天 YYYY-MM-DD
const now = new Date();
const targetDate =
  getArg('date') ||
  `${now.getFullYear()}-${String(now.getMonth() + 1).padStart(2, '0')}-${String(now.getDate()).padStart(2, '0')}`;

const targetFile = path.join(projectRoot, 'src', 'content', 'daily', `${targetDate}.md`);

console.log(`\n🤖 =================================================`);
console.log(`🚀 每日 AI 日报 · 起草助手启动`);
console.log(`📅 目标期号: ${targetDate}`);
console.log(`📁 输出文件: src/content/daily/${targetDate}.md`);
console.log(`⚙️  运行模式: ${isMock ? '离线模拟/模板模式 (Mock Mode)' : '大模型生成模式 (LLM API Mode)'}`);
console.log(`=================================================\n`);

// 检查是否已存在同名文件
if (fs.existsSync(targetFile) && !isForce) {
  console.error(`⚠️  警告: ${targetDate}.md 已存在！`);
  console.error(`👉 为防止覆盖已有的终审内容，已自动停止。如需强制覆盖，请追加 --force 参数。\n`);
  process.exit(1);
}

// 模拟数据生成器 (用于离线或无 API Key 场景)
function generateMockDraft(date) {
  return `---
date: "${date}"
title: "${date.slice(5).replace('-', ' 月 ')} 日 · 智能流与独立创造"
highlights: "AI 工作流正在从提示词工程向全自动 Agent 协同演进，小团队与一人公司迎来效率飞跃。"
draft: true
epigraph: "好的工具让你忘记工具本身，直奔创造结果。"
lead: |
  今天精选的重点聚焦在智能协作与微型商业化的结合点上。随着大模型推理速度的跃升，原本需要多部门协同的复杂内容与代码任务，现在单个创作者配合两三个垂类 Agent 即可在两小时内完成全流程闭环。
scene: |
  「这个月一个人做了 3 款微型应用？」「嗯，把重复性代码和测试全交给了 AI 结对编程助手，我只负责画架构图和写分发故事。」—— 某独立开发者的复盘笔记。
items:
  - category: "AI 资讯"
    title: "前沿多模态大模型推出视觉深度推理 API"
    note: "具备复杂图表高精度解析与界面自动操作能力，可直接用于自动化 UI 测试与设计稿还原。"
    url: "https://example.com/ai-update"
    source: "AI News"
    pinned: true
    so_what: "设计师可借此大幅减少切图与标注等低效耗时，聚焦于核心用户旅程推演。"

  - category: "一人公司"
    title: "全职创作者用 AI 自动化管道实现周更短剧分发"
    note: "将日报中的『今日一幕』脚本通过多模型管线一键生成分镜脚本与配音，全网播放量突破百万。"
    url: "https://example.com/solopreneur-case"
    source: "Product Hunt"
    pinned: false
    so_what: "将一次创作拆解为文字、图文与微短剧三套物料，是放大内容商业价值的最高杠杆。"

  - category: "产品设计"
    title: "极简暗黑模式界面的视觉对比度与层级规范"
    note: "系统剖析顶级现代生产力工具如何在 Deep Dark 调色下通过微渐变营造高级纵深感。"
    url: "https://example.com/design-system"
    source: "Design Digest"
    pinned: false
    so_what: "深色界面绝非简单的纯黑底色，合理的背景灰阶阶梯是避免视觉疲劳的关键。"

  - category: "AI 协作"
    title: "本地 Agent 编排工具工作流实战技巧"
    note: "如何通过结构化 JSON Schema 约束大模型输出，使多步骤复杂任务的执行准确率提升至 98% 以上。"
    url: "https://github.com/example/agent-workflows"
    source: "GitHub"
    pinned: false
    so_what: "写好 Schema 和防御性规则，是掌控 AI Agent 的第一核心法则。"
---

（这里是主理人编者按草稿。请在终审时根据当天的真实思考进行增删与润色。）
`;
}

// 大模型 API 调用生成器
async function generateLLMDraft(date) {
  const apiKey = process.env.AI_API_KEY;
  const apiBase = process.env.AI_API_BASE || 'https://api.openai.com/v1';
  const modelName = process.env.AI_MODEL_NAME || 'gpt-4o-mini';

  const systemPrompt = `你是一个拥有 10 年编剧与产品实战经验的中文 AI 日报主理人（产品人，擅长用故事思维驱动用户价值）。
你的任务是根据当天的 AI、产品、设计与独立开发动态，起草一份高质量的中文策展日报。

【写作指南（岛主声音）】：
1. 讲理不说教，像熟人聊天的口吻，有观点、有脾气、有判断力。
2. 拒绝 AI 腔调：不堆砌术语、不假客观、不公式化结尾。
3. 每天精选收录至少 20 条高密度图文条目，均匀覆盖全部 7 大受控分类（AI 资讯、一人公司、产品设计、审美提升、产品营销、AI 漫剧、AI 协作），每个分类至少 2~3 条。
4. 必须包含字段：
   - date: "${date}"
   - title: "M 月 D 日 · 今日主标题"
   - highlights: "一句话概括今天的主题"
   - draft: true (必须为 true)
   - epigraph: "刊头题记：一句话定调，可锐可诗"
   - lead: "今日主线/卷首语：150-250字的有观点小叙事，把今天散条目串成一条线"
   - scene: "今日一幕：30-60字的小剧场分镜或对白"
   - items: 3-5条精选，category 只能从以下受控列表选择：
     ['AI 资讯', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 协作']
     每条必须包含 title, note, url, source, pinned(boolean), so_what(对设计师/受众的价值)。

请严格按照如下 YAML frontmatter + markdown 格式直接输出，不要输出任何多余包裹标记：
---
date: "${date}"
...
---
（编者按正文）
`;

  console.log(`📡 正在调用大模型 API (${modelName})...`);

  const response = await fetch(`${apiBase.replace(/\/$/, '')}/chat/completions`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model: modelName,
      messages: [
        { role: 'system', content: systemPrompt },
        { role: 'user', content: `请为 ${date} 起草一期符合上述标准的每日 AI 日报。` },
      ],
      temperature: 0.7,
    }),
  });

  if (!response.ok) {
    throw new Error(`API 请求失败: ${response.status} ${response.statusText}`);
  }

  const result = await response.json();
  let content = result.choices?.[0]?.message?.content || '';
  
  // 清理可能包含的 markdown 代码块包裹
  content = content.replace(/^```markdown\n/, '').replace(/^```\n/, '').replace(/\n```$/, '');
  return content;
}

// 执行生成
async function run() {
  try {
    let markdownContent = '';
    if (isMock) {
      console.log('💡 使用离线模板生成草稿...');
      markdownContent = generateMockDraft(targetDate);
    } else {
      markdownContent = await generateLLMDraft(targetDate);
    }

    // 确保目标目录存在
    const dir = path.dirname(targetFile);
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }

    // 写入文件
    fs.writeFileSync(targetFile, markdownContent, 'utf8');

    console.log(`\n✅ 草稿生成成功: ${targetFile}`);
    console.log(`\n📋 【下一步人工终审流程】:`);
    console.log(`1. 在编辑器中打开 src/content/daily/${targetDate}.md`);
    console.log(`2. 审校标题、点评、删除不需要的条目、调整分类与顺序。`);
    console.log(`3. 确认无误后，将 frontmatter 中的 draft 改为 false。`);
    console.log(`4. git commit && git push 即可全自动上线！\n`);
  } catch (error) {
    console.error(`❌ 起草失败:`, error.message);
    process.exit(1);
  }
}

run();
