# 每日 AI 日报 · 一页纸极简运维手册

> 本文档为主理人日常运维的唯一参考指南。请将本手册加入收藏。

---

## 🚀 1. 日常发刊（两种方式）

### 方式 A：AI 辅助起草（推荐，5 分钟搞定）
1. 在终端中运行起草命令：
   ```bash
   npm run draft
   ```
   脚本将在 `src/content/daily/` 生成当天的草稿文件（如 `2026-08-28.md`）。
2. 在编辑器中打开该文件，根据当天真实思考进行终审：
   - 润色刊头题记（`epigraph`）、今日主线（`lead`）与今日一幕（`scene`）。
   - 保留 3-5 条最有价值的精选，校准点评（`note`）与价值沉淀（`so_what`）。
3. 将 frontmatter 中的 `draft: true` 改为 `draft: false`。
4. 提交并推送：
   ```bash
   git add .
   git commit -m "feat(daily): 发布 2026-08-28 日报"
   git push
   ```
   Cloudflare Pages 将在 15 秒内自动全站构建并部署上线！

---

### 方式 B：纯手动发布（零脚本依赖）
直接在 `src/content/daily/` 新建一个 `YYYY-MM-DD.md` 文件，填入标准 Frontmatter：
```markdown
---
date: "2026-08-28"
title: "8 月 28 日 · 今日主标题"
highlights: "一句话概括今天的主题看点"
draft: false
epigraph: "刊头题记：一句话定调，可锐可诗"
lead: |
  今日主线：150-250 字有观点的叙事（把散条目串成线）
scene: |
  今日一幕：30-60 字的 AI 小剧场分镜或对白
items:
  - category: "AI 资讯"       # 必须属于受控分类列表
    title: "条目标题"
    note: "一到两句原创犀利点评"
    url: "https://example.com"
    source: "X"
    pinned: false
    so_what: "这对转型中的设计师/创造者意味着什么"
---

这里可以写主理人编者按正文（可选，支持完整 Markdown 语法）。
```

---

## 🎨 2. 全站配置与变现开关 (`src/config/site.ts`)

全站所有文本、路由、商业化槽位均在 [`src/config/site.ts`](file:///Users/gx/.gemini/antigravity/scratch/ai-daily/src/config/site.ts) 集中控制，修改后保存即生效：

| 配置项 | 路径 | 说明 |
|---|---|---|
| **站名与标语** | `siteConfig.name` / `slogan` | 修改全站名称与 Logo 副标题 |
| **主理人简介** | `siteConfig.author` | 修改名字、头衔、Bio 及 X/GitHub/Email |
| **邮件订阅** | `siteConfig.features.newsletter.enabled` | 设为 `true`/`false` 控制全站订阅框显隐 |
| **社群入口** | `siteConfig.features.community.enabled` | 设为 `true`/`false`，修改社群文案与跳转链接 |
| **赞助商槽位** | `siteConfig.features.sponsor.enabled` | 设为 `true` 开启赞助位，填入赞助商名称与链接 |
| **深度副刊** | `siteConfig.features.premium.enabled` | 设为 `true`/`false` 控制导航与副刊占位页 |

---

## 🏷️ 3. 增删与修改分类 (`src/config/categories.ts`)

全站**严禁硬编码分类字符串**。增删分类只需修改 [`src/config/categories.ts`](file:///Users/gx/.gemini/antigravity/scratch/ai-daily/src/config/categories.ts)：
```typescript
export const CATEGORIES: Record<string, CategoryMeta> = {
  '新分类名': {
    key: '新分类名',
    name: '新分类名',
    slug: 'new-category-slug',
    description: '新分类的一句话描述',
    color: {
      bg: 'bg-indigo-50',
      text: 'text-indigo-700',
      border: 'border-indigo-200',
      dot: 'bg-indigo-500',
      darkBg: 'dark:bg-indigo-950/40',
      darkText: 'dark:text-indigo-300',
      darkBorder: 'dark:border-indigo-800/60',
    },
  },
  // ...
};
```
修改后，首页、单期卡片、分类页（`/tag/new-category-slug`）、归档页和 RSS 将全自动同步生效！

---

## ☁️ 4. Cloudflare Pages 部署上线指南

### 方式 1：Git 仓库自动关联（首选，推送即上线）
1. 登录 [Cloudflare Dashboard](https://dash.cloudflare.com/) → 进入 **Workers & Pages** → 点击 **Create application** → 选择 **Pages**。
2. 点击 **Connect to Git**，选中本站代码仓库。
3. 构建配置填写如下：
   - **Framework preset**: `Astro`
   - **Build command**: `npm run build`
   - **Build output directory**: `dist`
   - **Environment variables**: 添加 `NODE_VERSION = 20`
4. 点击 **Save and Deploy** 即可获得免费的全球 CDN 域名（如 `https://your-site.pages.dev`）。
5. 后续只需绑定您的自定义独立域名并开启 SSL。

### 方式 2：本地 Wrangler CLI 一键部署
```bash
# 1. 登录 Cloudflare 账号
npx wrangler login

# 2. 执行静态编译并直推部署
npm run build
npx wrangler pages deploy dist --project-name=ai-daily
```

---

## ⏪ 5. 紧急撤回与回滚操作

- **撤回某一期**：在对应的 `src/content/daily/YYYY-MM-DD.md` 中将 `draft: false` 改回 `draft: true` 并 push，该期将瞬间从全站首页、详情页、Feed 与 Sitemap 中彻底隐形。
- **Cloudflare 一键秒级回滚**：在 Cloudflare Pages 的 **Deployments** 列表中，找到上一版本，点击 **Rollback to this deployment** 即可 0 秒完成回滚。
