import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { siteConfig } from '../config/site';

function escapeXml(unsafe: string): string {
  return unsafe.replace(/[<>&'"]/g, (c) => {
    switch (c) {
      case '<':
        return '&lt;';
      case '>':
        return '&gt;';
      case '&':
        return '&amp;';
      case '\'':
        return '&apos;';
      case '"':
        return '&quot;';
      default:
        return c;
    }
  });
}

export const GET: APIRoute = async ({ site }) => {
  const baseUrl = site ? site.toString().replace(/\/$/, '') : siteConfig.url;

  const allDailies = await getCollection('daily', ({ data }) => !data.draft);

  const sortedDailies = allDailies.sort(
    (a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
  );

  const rssItems = sortedDailies.map((issue) => {
    const { date, title, highlights, epigraph, lead, items } = issue.data;
    const itemUrl = `${baseUrl}/d/${date}`;
    const displayTitle = title || `${date} · 今日看点`;
    const pubDate = new Date(`${date}T08:00:00+08:00`).toUTCString();

    // Construct rich HTML content for RSS readers
    const itemsHtml = items
      .map((item) => {
        return `
        <div style="margin-bottom: 16px; padding: 12px; border: 1px solid #e5e7eb; border-radius: 8px;">
          <p style="margin: 0 0 6px 0;">
            <strong style="color: #4f46e5;">[${escapeXml(item.category)}]</strong>
            <a href="${escapeXml(item.url)}" target="_blank" rel="noopener noreferrer" style="font-weight: bold; color: #111827; text-decoration: none;">
              ${escapeXml(item.title)}
            </a>
            <span style="color: #9ca3af; font-size: 12px;">(${escapeXml(item.source)})</span>
          </p>
          <p style="margin: 0 0 6px 0; color: #374151; font-size: 14px; line-height: 1.6;">
            ${escapeXml(item.note)}
          </p>
          ${
            item.so_what
              ? `<p style="margin: 0; color: #4338ca; font-size: 12px; background: #eef2ff; padding: 6px 8px; border-radius: 4px;">
                  💡 <strong>价值沉淀：</strong>${escapeXml(item.so_what)}
                </p>`
              : ''
          }
        </div>
      `;
      })
      .join('');

    const descriptionHtml = `
      ${epigraph ? `<blockquote style="font-style: italic; border-left: 3px solid #6366f1; padding-left: 12px; margin-bottom: 16px; color: #4b5563;">「${escapeXml(epigraph)}」</blockquote>` : ''}
      ${highlights ? `<p style="font-size: 15px; font-weight: 500; color: #1f2937; margin-bottom: 16px;">${escapeXml(highlights)}</p>` : ''}
      ${lead ? `<div style="background: #f3f4f6; padding: 12px; border-radius: 8px; margin-bottom: 20px; color: #374151;"><strong>主理人主线：</strong><br/>${escapeXml(lead).replace(/\n/g, '<br/>')}</div>` : ''}
      <h4 style="margin: 20px 0 12px 0;">今日精选条目（共 ${items.length} 条）：</h4>
      ${itemsHtml}
    `;

    return `
    <item>
      <title><![CDATA[${displayTitle}]]></title>
      <link>${itemUrl}</link>
      <guid isPermaLink="true">${itemUrl}</guid>
      <pubDate>${pubDate}</pubDate>
      <description><![CDATA[${descriptionHtml}]]></description>
    </item>`;
  });

  const rssXml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title><![CDATA[${siteConfig.name}]]></title>
    <description><![CDATA[${siteConfig.description}]]></description>
    <link>${baseUrl}</link>
    <language>${siteConfig.lang}</language>
    <lastBuildDate>${new Date().toUTCString()}</lastBuildDate>
    <atom:link href="${baseUrl}/rss.xml" rel="self" type="application/rss+xml"/>
    ${rssItems.join('\n')}
  </channel>
</rss>`;

  return new Response(rssXml, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
