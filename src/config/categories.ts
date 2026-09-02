export interface CategoryMeta {
  key: string;
  name: string;
  slug: string;
  description: string;
  color: {
    bg: string;
    text: string;
    border: string;
    dot: string;
    darkBg: string;
    darkText: string;
    darkBorder: string;
  };
}

export const CATEGORIES: Record<string, CategoryMeta> = {
  'AI 资讯': {
    key: 'AI 资讯',
    name: 'AI 资讯',
    slug: 'ai-news',
    description: '全球前沿模型突破、重大产品发布与技术范式演进',
    color: {
      bg: 'bg-blue-50',
      text: 'text-blue-700',
      border: 'border-blue-200',
      dot: 'bg-blue-500',
      darkBg: 'dark:bg-blue-950/40',
      darkText: 'dark:text-blue-300',
      darkBorder: 'dark:border-blue-800/60',
    },
  },
  '一人公司': {
    key: '一人公司',
    name: '一人公司',
    slug: 'solopreneur',
    description: '独立开发者实战、微型 SaaS 盈利与个人商业化杠杆',
    color: {
      bg: 'bg-amber-50',
      text: 'text-amber-700',
      border: 'border-amber-200',
      dot: 'bg-amber-500',
      darkBg: 'dark:bg-amber-950/40',
      darkText: 'dark:text-amber-300',
      darkBorder: 'dark:border-amber-800/60',
    },
  },
  '产品经理': {
    key: '产品经理',
    name: '产品经理',
    slug: 'product-manager',
    description: '需求洞察、PRD 与业务架构、敏捷开发与商业闭环实战',
    color: {
      bg: 'bg-sky-50',
      text: 'text-sky-700',
      border: 'border-sky-200',
      dot: 'bg-sky-500',
      darkBg: 'dark:bg-sky-950/40',
      darkText: 'dark:text-sky-300',
      darkBorder: 'dark:border-sky-800/60',
    },
  },
  '产品设计': {
    key: '产品设计',
    name: '产品设计',
    slug: 'product-design',
    description: 'AI 时代的交互范式、微体验打磨与产品架构思辨',
    color: {
      bg: 'bg-emerald-50',
      text: 'text-emerald-700',
      border: 'border-emerald-200',
      dot: 'bg-emerald-500',
      darkBg: 'dark:bg-emerald-950/40',
      darkText: 'dark:text-emerald-300',
      darkBorder: 'dark:border-emerald-800/60',
    },
  },
  '编剧技巧': {
    key: '编剧技巧',
    name: '编剧技巧',
    slug: 'screenwriting',
    description: '故事思维、三幕剧冲突结构、情节点设计与影视叙事力量',
    color: {
      bg: 'bg-violet-50',
      text: 'text-violet-700',
      border: 'border-violet-200',
      dot: 'bg-violet-500',
      darkBg: 'dark:bg-violet-950/40',
      darkText: 'dark:text-violet-300',
      darkBorder: 'dark:border-violet-800/60',
    },
  },
  'AI 漫剧': {
    key: 'AI 漫剧',
    name: 'AI 漫剧',
    slug: 'ai-drama',
    description: 'AI 漫剧分镜、短剧叙事演进与 AIGC 影视创作前沿突破',
    color: {
      bg: 'bg-orange-50',
      text: 'text-orange-700',
      border: 'border-orange-200',
      dot: 'bg-orange-500',
      darkBg: 'dark:bg-orange-950/40',
      darkText: 'dark:text-orange-300',
      darkBorder: 'dark:border-orange-800/60',
    },
  },
  'AI 协作': {
    key: 'AI 协作',
    name: 'AI 协作',
    slug: 'ai-workflows',
    description: '人机共创心流、Agent 编排与实操效率倍增流',
    color: {
      bg: 'bg-teal-50',
      text: 'text-teal-700',
      border: 'border-teal-200',
      dot: 'bg-teal-500',
      darkBg: 'dark:bg-teal-950/40',
      darkText: 'dark:text-teal-300',
      darkBorder: 'dark:border-teal-800/60',
    },
  },
  '审美提升': {
    key: '审美提升',
    name: '审美提升',
    slug: 'aesthetics',
    description: '视觉品味、字体排版、动效细节与当代数字美学',
    color: {
      bg: 'bg-rose-50',
      text: 'text-rose-700',
      border: 'border-rose-200',
      dot: 'bg-rose-500',
      darkBg: 'dark:bg-rose-950/40',
      darkText: 'dark:text-rose-300',
      darkBorder: 'dark:border-rose-800/60',
    },
  },
  '产品营销': {
    key: '产品营销',
    name: '产品营销',
    slug: 'marketing',
    description: '冷启动分发、叙事飞轮、内容引流与增长黑客',
    color: {
      bg: 'bg-purple-50',
      text: 'text-purple-700',
      border: 'border-purple-200',
      dot: 'bg-purple-500',
      darkBg: 'dark:bg-purple-950/40',
      darkText: 'dark:text-purple-300',
      darkBorder: 'dark:border-purple-800/60',
    },
  },
};

export const CATEGORY_KEYS = Object.keys(CATEGORIES) as [string, ...string[]];

export function getCategoryByKey(key: string): CategoryMeta {
  return (
    CATEGORIES[key] || {
      key,
      name: key,
      slug: encodeURIComponent(key),
      description: '',
      color: {
        bg: 'bg-zinc-50',
        text: 'text-zinc-700',
        border: 'border-zinc-200',
        dot: 'bg-zinc-500',
        darkBg: 'dark:bg-zinc-900',
        darkText: 'dark:text-zinc-300',
        darkBorder: 'dark:border-zinc-800',
      },
    }
  );
}

export function getCategoryBySlug(slug: string): CategoryMeta | undefined {
  return Object.values(CATEGORIES).find(
    (c) => c.slug === slug || encodeURIComponent(c.key) === slug
  );
}
