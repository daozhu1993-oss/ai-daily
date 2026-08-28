import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import { CATEGORY_KEYS } from './config/categories';

const dailyCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/daily' }),
  schema: z.object({
    // 必填日期，也是 URL 路由与排序主键 (格式: YYYY-MM-DD)
    date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/, {
      message: '日期格式必须为 YYYY-MM-DD，例如 2026-08-28',
    }),
    // 可选标题，不填则由模板格式化为「X 月 X 日 · 今日看点」
    title: z.string().optional(),
    // 列表卡片与 OG 分享图核心摘要
    highlights: z.string().optional(),
    // 自定义封面图 (留空则自动生成)
    cover: z.string().optional(),
    // 草稿开关: true 时不发布、不进列表、不进 RSS
    draft: z.boolean().default(false),

    // ==================== 附录 B：岛主特色字段 ====================
    // 刊头题记: 一句话定调，可锐可诗
    epigraph: z.string().optional(),
    // 今日主线/卷首语: 150-250 字有观点的叙事（把散条目串成线）
    lead: z.string().optional(),
    // 今日一幕: 30-60 字的 AI 小剧场（对白或分镜，极高辨识度）
    scene: z.string().optional(),

    // ==================== 条目列表 ====================
    items: z.array(
      z.object({
        // 受控分类
        category: z.enum(CATEGORY_KEYS as [string, ...string[]], {
          errorMap: () => ({
            message: `分类必须属于受控列表: ${CATEGORY_KEYS.join(' | ')}`,
          }),
        }),
        // 条目标题
        title: z.string().min(1, '标题不能为空'),
        // 原创深度点评（一到两句：为什么值得看 / 核心判断）
        note: z.string().min(1, '点评不能为空'),
        // 外链来源 (必须为合法 URL)
        url: z.string().url('必须为合法的外链 URL'),
        // 来源平台名称 (X, GitHub, Product Hunt, Blog, YouTube 等)
        source: z.string().min(1, '来源平台不能为空'),
        // 可选媒体附件 (图片或视频相对/绝对路径)
        media: z.string().optional(),
        // 是否置顶到当期最前
        pinned: z.boolean().default(false),
        // 附录 B：价值反思（这对转型中的设计师/创造者意味着什么）
        so_what: z.string().optional(),
      })
    ),
  }),
});

export const collections = {
  daily: dailyCollection,
};
