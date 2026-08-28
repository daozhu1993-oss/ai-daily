import fs from 'node:fs';
import path from 'node:path';

const dailyDir = path.resolve('src/content/daily');
const files = fs.readdirSync(dailyDir).filter(f => f.endsWith('.md'));

async function checkUrl(url) {
  try {
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 7000);
    
    // Some sites block HEAD or need User-Agent
    const res = await fetch(url, {
      method: 'GET',
      headers: {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
      },
      signal: controller.signal
    });
    clearTimeout(timeout);
    return { status: res.status, ok: res.status >= 200 && res.status < 400 };
  } catch (err) {
    return { status: 0, error: err.message, ok: false };
  }
}

async function run() {
  console.log('🔍 开始全面核对 180 条资讯外链有效性...\n');
  const results = [];
  
  for (const file of files) {
    const content = fs.readFileSync(path.join(dailyDir, file), 'utf-8');
    const lines = content.split('\n');
    let currentTitle = '';
    
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      if (line.trim().startsWith('title:')) {
        currentTitle = line.replace('title:', '').trim().replace(/^["']|["']$/g, '');
      }
      if (line.trim().startsWith('url:')) {
        const url = line.replace('url:', '').trim().replace(/^["']|["']$/g, '');
        results.push({ file, title: currentTitle, line: i + 1, url });
      }
    }
  }

  console.log(`共提取到 ${results.length} 个待检测链接，正在并发核对真实响应状态...\n`);

  const badLinks = [];
  const validLinks = [];

  // Batch requests to prevent rate limit
  const batchSize = 10;
  for (let i = 0; i < results.length; i += batchSize) {
    const batch = results.slice(i, i + batchSize);
    await Promise.all(batch.map(async (item) => {
      const res = await checkUrl(item.url);
      if (res.ok) {
        validLinks.push({ ...item, status: res.status });
        process.stdout.write('✓');
      } else {
        badLinks.push({ ...item, status: res.status, error: res.error });
        process.stdout.write('✗');
      }
    }));
  }

  console.log('\n\n================ 检测结果报告 ================');
  console.log(`✅ 正常链接: ${validLinks.length}`);
  console.log(`❌ 异常/404链接: ${badLinks.length}\n`);

  if (badLinks.length > 0) {
    console.log('异常链接明细:');
    badLinks.forEach((b, idx) => {
      console.log(`[${idx + 1}] [${b.file}:${b.line}] ${b.title}`);
      console.log(`    URL: ${b.url}`);
      console.log(`    Status: ${b.status} ${b.error || ''}`);
    });
  }

  fs.writeFileSync('scripts/link-check-report.json', JSON.stringify({ valid: validLinks, bad: badLinks }, null, 2));
}

run();
