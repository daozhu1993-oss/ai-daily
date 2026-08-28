import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { CATEGORIES } from '../config/categories';
import { siteConfig } from '../config/site';

export const GET: APIRoute = async ({ site }) => {
  const baseUrl = site ? site.toString().replace(/\/$/, '') : siteConfig.url;

  const allDailies = await getCollection('daily', ({ data }) => !data.draft);

  const urls: Array<{ loc: string; lastmod?: string; changefreq: string; priority: string }> = [];

  // 1. Home
  urls.push({
    loc: `${baseUrl}/`,
    lastmod: allDailies[0]?.data.date,
    changefreq: 'daily',
    priority: '1.0',
  });

  // 2. Archive
  urls.push({
    loc: `${baseUrl}/archive`,
    changefreq: 'daily',
    priority: '0.8',
  });

  // 3. About & Premium
  urls.push({
    loc: `${baseUrl}/about`,
    changefreq: 'monthly',
    priority: '0.5',
  });
  urls.push({
    loc: `${baseUrl}/premium`,
    changefreq: 'weekly',
    priority: '0.6',
  });

  // 4. Categories
  Object.values(CATEGORIES).forEach((cat) => {
    urls.push({
      loc: `${baseUrl}/tag/${cat.slug}`,
      changefreq: 'daily',
      priority: '0.7',
    });
  });

  // 5. Daily Issues
  allDailies.forEach((issue) => {
    urls.push({
      loc: `${baseUrl}/d/${issue.data.date}`,
      lastmod: issue.data.date,
      changefreq: 'never',
      priority: '0.9',
    });
  });

  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${urls
  .map(
    (u) => `  <url>
    <loc>${u.loc}</loc>
    ${u.lastmod ? `<lastmod>${u.lastmod}</lastmod>` : ''}
    <changefreq>${u.changefreq}</changefreq>
    <priority>${u.priority}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(sitemapXml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=86400',
    },
  });
};
