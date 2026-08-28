# 🤖 AI Agent 维护与日常采编指南 (AGENTS.md / Codex 指南)

欢迎使用 Codex 或任何 AI Agent 维护 **岛主 AI 日报 (ai-daily)**！本项目采用了极度模块化、强类型校验的静态站点架构。

---

## 🛠 一、 技术栈与核心架构

- **框架**：[Astro 5 (Content Layer)](https://astro.build/) + TypeScript
- **样式**：Tailwind CSS + 暗色/亮色自适应主题
- **内容存储**：`src/content/daily/YYYY-MM-DD.md`（强类型 Markdown Content Collection）
- **部署平台**：Cloudflare Workers / Pages（关联 GitHub `main` 分支自动 CI/CD 构建）

---

## 📝 二、 日常新增一期日报流程（以 YYYY-MM-DD 为例）

### 1. 文件创建路径
新建文件：`src/content/daily/YYYY-MM-DD.md`

### 2. 标准 Frontmatter Schema 格式

```yaml
---
date: "2026-08-29"
title: "8 月 29 日 · [岛主专属主线标题：犀利/诗意/产品人视角]"
highlights: "全网 7 大领域 60 篇高密度精选：[重点突出今日核心突破与商业案例]。"
draft: false
epigraph: "[刊头题记：一句话定调]"
lead: |
  [今日主线叙事：150-250 字有观点的产品人解读，把散点串成时代趋势线]
scene: |
  [今日一幕：30-60 字的 AI 小剧场或行业真实对白分镜]
items:
  - category: "AI 漫剧" # 必须属于受控分类之一
    title: "文章标题"
    note: "主理人一到两句到位、带判断的犀利点评。"
    url: "https://example.com/article" # 真实有效且具备阅读深度的文章/研报链接
    source: "example.com"
    media: "https://images.unsplash.com/..." # 高清封面预览图
    pinned: false
    so_what: "这对转型中的产品人/独立开发者意味着什么。"
---

主理人编者按：今天精选的这 60 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
```

---

## 🏷️ 三、 7 大受控分类列表 (严格对齐)

1. `AI 资讯`：全球前沿模型突破、重大发布、学术论文与算力基建
2. `一人公司`：独立开发者实战、微型 SaaS 盈利与个人商业化杠杆
3. `产品设计`：交互范式、微体验打磨、意图画布与设计系统
4. `审美提升`：视觉品味、字体排版、动效细节与当代数字美学
5. `产品营销`：公开构建（Build in Public）、增长黑客与 SEO 优化
6. `AI 漫剧`：漫剧分镜设计、视频生成连贯镜头、行业爆款复盘与商业变现
7. `AI 协作`：人机共创心流、MCP 协议、Agent 编排与自动化流

---

## 🔍 四、 质量核验与自动化命令

每次修改或新增内容后，请依次运行以下命令：

```bash
# 1. 验证 TypeScript 类型与 Astro 内容约束（必须 0 errors）
npm run check

# 2. 本地静态构建测试
npm run build

# 3. 提交并推送到 GitHub（Cloudflare 会自动在全球边缘节点上线）
git add .
git commit -m "feat: publish daily issue YYYY-MM-DD"
git push
```

---

## ⚡ 五、 自动化脚本清单

- `node scripts/sync-iandaily.mjs`：从参考源自动抓取并生成标准化日报文件
- `node scripts/inject-drama.mjs`：为指定日期批量注入 AI 漫剧深度分析
- `node scripts/verify-links.mjs`：并发测试全站所有外链的真实连通性与 HTTP 状态码
