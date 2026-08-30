export interface SiteConfig {
  name: string;
  slogan: string;
  description: string;
  author: {
    name: string;
    role: string;
    bio: string;
    personalSite: string;
    featuredWorks: Array<{
      title: string;
      href: string;
    }>;
    avatar?: string;
    social: {
      x?: string;
      github?: string;
      wechat?: string;
      email?: string;
    };
  };
  url: string;
  lang: string;
  features: {
    // 邮件订阅
    newsletter: {
      enabled: boolean;
      title: string;
      description: string;
      placeholder: string;
      buttonText: string;
    };
    // 社群 CTA
    community: {
      enabled: boolean;
      title: string;
      description: string;
      buttonText: string;
      link: string;
      tag: string;
    };
    // 赞助位 (没有赞助时自动隐藏或显示招商文案)
    sponsor: {
      enabled: boolean;
      title: string;
      description: string;
      link: string;
      sponsorName?: string;
      sponsorLogo?: string;
    };
    // 付费/副刊占位路由
    premium: {
      enabled: boolean;
      title: string;
      tag: string;
      description: string;
      path: string;
    };
    // 分享功能
    sharing: {
      enabled: boolean;
    };
  };
  nav: Array<{
    label: string;
    href: string;
    badge?: string;
  }>;
}

export const siteConfig: SiteConfig = {
  name: '岛主 AI 日报',
  slogan: '用故事思维驱动用户价值，凝练每日 AI 脉搏',
  description:
    '一个由个人主理的中文策展型每日 AI 日报。关注 AI 前沿、独立产品、设计美学与人机协作。',
  author: {
    name: '岛主',
    role: '产品人',
    bio: '干过十年编剧，后来转去做产品经理，擅长用故事思维驱动各种「杂七杂八」的产品。',
    personalSite: 'https://daozhu-ai-daily.daozhu1993.workers.dev',
    featuredWorks: [],
    social: {
      x: 'https://x.com',
      github: 'https://github.com/daozhu1993-oss',
      email: 'mailto:contact@example.com',
    },
  },
  url: 'https://daozhu-ai-daily.daozhu1993.workers.dev',
  lang: 'zh-CN',
  features: {
    newsletter: {
      enabled: true,
      title: '订阅每日精选晨报',
      description: '每天清晨，把最具穿透力的 AI 洞察与产品灵感送达您的收件箱。零垃圾邮件，随时退订。',
      placeholder: '输入您的邮箱地址...',
      buttonText: '免费订阅',
    },
    community: {
      enabled: true,
      title: '关于主理人 · 岛主',
      description: '干过十年编剧，后来转去做产品经理。擅长用故事思维驱动各种「杂七杂八」的产品。',
      buttonText: '关于岛主',
      link: '/about',
      tag: '主理人',
    },
    sponsor: {
      enabled: false,
      title: '本周赞助商招募',
      description: '精准触达高质量 AI 从业者、设计师与独立开发者。',
      link: 'mailto:sponsor@example.com',
    },
    premium: {
      enabled: true,
      title: '深度副刊',
      tag: '即将推出',
      description: '故事化连载专栏：AI 时代独立创造者的人物叙事与商业实战。',
      path: '/premium',
    },
    sharing: {
      enabled: true,
    },
  },
  nav: [
    { label: '今日精选', href: '/' },
    { label: '所有归档', href: '/archive' },
    { label: '深度副刊', href: '/premium', badge: 'New' },
    { label: '关于主理人', href: '/about' },
  ],
};
