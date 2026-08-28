import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const PAGES = [
  { url: 'https://iandaily.xyz/', date: '2026-08-28', title: '8 月 28 日 · 伊恩日刊精选' },
  { url: 'https://iandaily.xyz/d/2026-08-27', date: '2026-08-27', title: '8 月 27 日 · 伊恩日刊精选' },
  { url: 'https://iandaily.xyz/d/2026-08-26', date: '2026-08-26', title: '8 月 26 日 · 伊恩日刊精选' },
  { url: 'https://iandaily.xyz/d/2026-08-25', date: '2026-08-25', title: '8 月 25 日 · 伊恩日刊精选' },
];

const VALID_CATEGORIES = new Set([
  'AI 资讯',
  '一人公司',
  '产品设计',
  '审美提升',
  '产品营销',
  'AI 漫剧',
  'AI 协作',
]);

function decodeEntities(str) {
  if (!str) return '';
  return str
    .replace(/&#x27;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&nbsp;/g, ' ')
    .trim();
}

async function scrapePage({ url, date, title }) {
  console.log(`📡 Fetching ${url} for date ${date}...`);
  const res = await fetch(url, {
    headers: {
      'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    },
  });
  if (!res.ok) {
    console.error(`Failed to fetch ${url}: status ${res.status}`);
    return;
  }

  const html = await res.text();
  const cardRegex = /<a[^>]*class="plaza-card[^"]*"[^>]*href="([^"]+)"[^>]*>([\s\S]*?)<\/a>/g;
  const items = [];
  let match;

  while ((match = cardRegex.exec(html)) !== null) {
    const href = match[1];
    const cardContent = match[2];

    const imgMatch = cardContent.match(/<img[^>]*src="([^"]+)"/);
    let media = imgMatch ? imgMatch[1] : '';
    if (media.startsWith('/')) {
      media = 'https://iandaily.xyz' + media;
    }

    const kickerMatch = cardContent.match(/<div class="plaza-kicker">([\s\S]*?)<\/div>/);
    let category = 'AI 资讯';
    let source = '';
    if (kickerMatch) {
      const spans = [...kickerMatch[1].matchAll(/<span>([^<]+)<\/span>/g)].map((m) =>
        decodeEntities(m[1])
      );
      if (spans.length > 0 && VALID_CATEGORIES.has(spans[0])) {
        category = spans[0];
      }
      if (spans.length > 1) {
        source = spans[spans.length - 1];
      }
    }

    const titleMatch = cardContent.match(/<h3 class="plaza-title">([\s\S]*?)<\/h3>/);
    const itemTitle = titleMatch ? decodeEntities(titleMatch[1]) : '';

    const noteMatch = cardContent.match(/<p class="plaza-judgment">([\s\S]*?)<\/p>/);
    const itemNote = noteMatch ? decodeEntities(noteMatch[1]) : '';

    if (itemTitle && href) {
      if (!source) {
        try {
          source = new URL(href).hostname.replace(/^www\./, '');
        } catch {
          source = 'web';
        }
      }

      items.push({
        category,
        title: itemTitle,
        note: itemNote,
        url: href,
        source,
        media: media || 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
        pinned: items.length === 0,
        so_what: itemNote,
      });
    }
  }

  console.log(`✅ Extracted ${items.length} items for ${date}`);

  const frontmatter = {
    date,
    title,
    highlights: `全网 7 大领域 ${items.length} 篇精选：100% 同步伊恩日刊一手资讯。`,
    draft: false,
    epigraph: '设计、AI 与一人公司的每日真实切片。',
    lead: `今日共精选 ${items.length} 篇前沿动态，覆盖模型底座、一人公司轻量级实战、产品设计与现代美学。`,
    scene: '「今天又有哪些新工具和新思路跑通了？」',
    items,
  };

  const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

伊恩日刊每日精选，同步前沿一手真实动态与产品解构。
`;

  const targetFile = path.join(TARGET_DIR, `${date}.md`);
  fs.writeFileSync(targetFile, mdContent, 'utf8');
  console.log(`💾 Saved to ${targetFile}`);
}

async function run() {
  for (const page of PAGES) {
    await scrapePage(page);
  }
  console.log('🎉 All pages scraped and saved successfully!');
}

run();
