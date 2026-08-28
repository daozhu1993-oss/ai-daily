import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { siteConfig } from '../config/site';

export const GET: APIRoute = async ({ site }) => {
  const baseUrl = site ? site.toString().replace(/\/$/, '') : siteConfig.url;

  const allDailies = await getCollection('daily', ({ data }) => !data.draft);

  const sortedDailies = allDailies.sort(
    (a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
  );

  const feedItems = sortedDailies.map((issue) => {
    const { date, title, highlights, epigraph, lead, scene, items } = issue.data;
    const itemUrl = `${baseUrl}/d/${date}`;
    const displayTitle = title || `${date} · 今日看点`;
    const datePublished = new Date(`${date}T08:00:00+08:00`).toISOString();

    const itemsHtml = items
      .map(
        (item) => `
      <div style="margin-bottom: 16px; padding: 12px; border: 1px solid #e5e7eb; border-radius: 8px;">
        <p style="margin: 0 0 6px 0;">
          <strong style="color: #4f46e5;">[${item.category}]</strong>
          <a href="${item.url}" target="_blank" rel="noopener noreferrer" style="font-weight: bold; color: #111827; text-decoration: none;">
            ${item.title}
          </a>
          <span style="color: #9ca3af; font-size: 12px;">(${item.source})</span>
        </p>
        <p style="margin: 0 0 6px 0; color: #374151; font-size: 14px; line-height: 1.6;">
          ${item.note}
        </p>
        ${
          item.so_what
            ? `<p style="margin: 0; color: #4338ca; font-size: 12px; background: #eef2ff; padding: 6px 8px; border-radius: 4px;">
                💡 <strong>价值沉淀：</strong>${item.so_what}
              </p>`
            : ''
        }
      </div>`
      )
      .join('');

    const contentHtml = `
      ${epigraph ? `<blockquote style="font-style: italic; border-left: 3px solid #6366f1; padding-left: 12px; margin-bottom: 16px; color: #4b5563;">「${epigraph}」</blockquote>` : ''}
      ${highlights ? `<p style="font-size: 15px; font-weight: 500; color: #1f2937; margin-bottom: 16px;">${highlights}</p>` : ''}
      ${lead ? `<div style="background: #f3f4f6; padding: 12px; border-radius: 8px; margin-bottom: 16px; color: #374151;"><strong>主理人主线：</strong><br/>${lead.replace(/\n/g, '<br/>')}</div>` : ''}
      ${scene ? `<div style="background: #fffbeb; border: 1px solid #fef3c7; padding: 10px 12px; border-radius: 8px; margin-bottom: 20px; color: #92400e; font-size: 13px;"><strong>🎭 今日一幕：</strong><br/><em>${scene.replace(/\n/g, '<br/>')}</em></div>` : ''}
      <h4 style="margin: 20px 0 12px 0;">今日精选条目（共 ${items.length} 条）：</h4>
      ${itemsHtml}
    `;

    return {
      id: itemUrl,
      url: itemUrl,
      title: displayTitle,
      summary: highlights || displayTitle,
      content_html: contentHtml,
      date_published: datePublished,
      tags: Array.from(new Set(items.map((i) => i.category))),
      author: {
        name: siteConfig.author.name,
      },
    };
  });

  const jsonFeed = {
    version: 'https://jsonfeed.org/version/1.1',
    title: siteConfig.name,
    home_page_url: baseUrl,
    feed_url: `${baseUrl}/feed.json`,
    description: siteConfig.description,
    user_comment: 'This is a curated AI daily newsletter JSON Feed.',
    language: siteConfig.lang,
    authors: [
      {
        name: siteConfig.author.name,
        url: baseUrl,
      },
    ],
    items: feedItems,
  };

  return new Response(JSON.stringify(jsonFeed, null, 2), {
    headers: {
      'Content-Type': 'application/feed+json; charset=utf-8',
      'Cache-Control': 'public, max-age=3600',
    },
  });
};
