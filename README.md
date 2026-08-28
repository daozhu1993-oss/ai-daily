# 每日 AI 日报 · AI Daily Digest

> 一个由个人主理、高审美、高信息密度的中文策展型每日 AI 日报静态网站。

---

## 🌟 项目亮点

- ⚡ **极致性能与零成本**：基于 **Astro 5 + Tailwind CSS + Markdown + Cloudflare Pages** 构建，纯静态生成、全球 CDN 分发、零维护费用。
- 🎯 **岛主视角与故事思维（核心护城河）**：
  - **刊头题记 (`epigraph`)**：一句话定调，可锐可诗。
  - **主理人主线 (`lead`)**：150-250 字有观点的叙事，把散乱的条目串联成深度洞察。
  - **今日一幕 (`scene`)**：30-60 字的 AI 小剧场微剧本与分镜场景。
  - **价值沉淀 (`so_what`)**：剖析每条技术资讯对设计师与独立创造者的深层商业价值。
- 🌓 **全站无闪烁暗/亮主题**：现代中文字阶排版优化，`<head>` 提前执行防 FOUC 脚本，本地状态持久记忆。
- 📡 **全渠道分发与订阅**：内置标准 **RSS 2.0 (`/rss.xml`)**、**JSON Feed 1.1 (`/feed.json`)**、动态 Sitemap 与 OG 社交分享底图。
- 💼 **第一天内建变现结构**：邮件订阅、社群 CTA、赞助位、深度副刊占位，全部由 `src/config/site.ts` 集中开关。
- 🤖 **彻底解耦的 AI 起草管线**：独立 Node 脚本 `npm run draft`，草稿永远带 `draft: true`，绝不绕过人工终审。

---

## 📂 项目结构

```text
├── functions/               # Cloudflare Pages 边缘函数 (API)
│   └── api/subscribe.ts     # 邮件订阅接口
├── public/                  # 静态公共资源 (Favicon, OG 底图, Robots.txt)
├── scripts/                 # 独立内容生产与起草脚本 (与前端解耦)
│   ├── draft.mjs            # AI 起草脚本 (支持 Mock 与 LLM 模式)
│   ├── sources.json         # 公开监控与抓取数据源清单
│   └── README.md            # 起草与人工终审工作流
├── src/
│   ├── components/          # 原创卡片与交互组件
│   │   ├── DailyItemCard.astro    # 单条资讯卡片
│   │   ├── DailyIssueCard.astro   # 往期精简卡片
│   │   ├── NewsletterForm.astro   # 邮件订阅组件
│   │   ├── CommunityCTA.astro     # 社群引流组件
│   │   ├── SponsorSlot.astro      # 赞助商槽位
│   │   ├── ShareButtons.astro     # 社交分享组件
│   │   └── ThemeToggle.astro      # 暗亮主题切换
│   ├── config/
│   │   ├── site.ts          # 全站元数据与功能开关
│   │   └── categories.ts    # 6 大受控分类集中定义
│   ├── content/
│   │   └── daily/           # 每期 Markdown 文件 (YYYY-MM-DD.md)
│   ├── layouts/
│   │   └── BaseLayout.astro # 基础 HTML5 布局
│   ├── pages/               # 路由与静态端点
│   │   ├── index.astro      # 首页 (最新完整流 + 往期倒序列表)
│   │   ├── archive.astro    # 时间线归档页
│   │   ├── about.astro      # 关于主理人与本站
│   │   ├── premium.astro    # 深度副刊占位页
│   │   ├── 404.astro        # 404 页面
│   │   ├── d/[date].astro   # 单期独立详情页
│   │   ├── tag/[category].astro # 分类跨日期聚合页
│   │   ├── rss.xml.ts       # 标准 RSS 2.0
│   │   ├── feed.json.ts     # 标准 JSON Feed 1.1
│   │   └── sitemap.xml.ts   # 动态 XML Sitemap
│   └── styles/
│       └── global.css       # 中文排版与主题变量
├── OPERATIONS.md            # 一页纸极简运维手册
└── wrangler.toml            # Cloudflare Pages 部署配置
```

---

## 🛠️ 快速开始

```bash
# 1. 安装依赖
npm install

# 2. 启动本地开发服务
npm run dev

# 3. 类型与 Schema 检查
npm run check

# 4. 生产打包
npm run build

# 5. 起草新一期日报
npm run draft
```

---

## 📖 详细运维手册

请查阅 [一页纸极简运维手册 (OPERATIONS.md)](file:///Users/gx/.gemini/antigravity/scratch/ai-daily/OPERATIONS.md) 了解如何发刊、增删分类、开关变现模块及部署上线。
