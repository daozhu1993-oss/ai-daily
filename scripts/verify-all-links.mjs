import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';
import { exec } from 'child_process';

const DATES = ['2026-09-05', '2026-09-06', '2026-09-07', '2026-09-08', '2026-09-09', '2026-09-10'];

function checkUrlOnce(url, maxTime = 15) {
  return new Promise((resolve) => {
    const isGetOnly = url.includes('wzbj1616.com');
    const flag = isGetOnly ? '-s -o /dev/null -w "%{http_code}"' : `-s -I -L --max-time ${maxTime}`;
    const cmd = `curl ${flag} -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)" "${url}"`;

    exec(cmd, (err, stdout) => {
      if (err) return resolve({ ok: false, code: 'TIMEOUT/ERR', url });
      if (isGetOnly) {
        const code = parseInt(stdout.trim(), 10);
        return resolve({ ok: code >= 200 && code < 400, code, url });
      }
      const matches = [...stdout.matchAll(/HTTP\/[12](?:\.[01])?\s+(\d{3})/g)];
      if (!matches || matches.length === 0) {
        return resolve({ ok: false, code: 'NO_RESPONSE', url });
      }
      const lastCode = parseInt(matches[matches.length - 1][1], 10);
      resolve({ ok: lastCode >= 200 && lastCode < 400, code: lastCode, url });
    });
  });
}

async function checkUrl(url) {
  let res = await checkUrlOnce(url, 15);
  if (!res.ok) {
    // Retry once with 20s
    res = await checkUrlOnce(url, 20);
  }
  return res;
}

async function verifyAll() {
  let totalTested = 0;
  let totalPassed = 0;
  let failedItems = [];

  for (const date of DATES) {
    const filePath = path.resolve(`./src/content/daily/${date}.md`);
    const content = fs.readFileSync(filePath, 'utf8');
    const fm = content.split('---')[1];
    const data = yaml.load(fm);

    console.log(`\n================ Testing ${date} (${data.items.length} items) ================`);

    // Chunk requests by 15 for fast parallel execution
    for (let i = 0; i < data.items.length; i += 15) {
      const chunk = data.items.slice(i, i + 15);
      const results = await Promise.all(chunk.map((item) => checkUrl(item.url)));

      for (let j = 0; j < chunk.length; j++) {
        totalTested++;
        const res = results[j];
        const item = chunk[j];
        if (res.ok) {
          totalPassed++;
        } else {
          console.error(`❌ [${res.code}] [${item.category}] "${item.title}" -> ${item.url}`);
          failedItems.push({ date, ...item, error: res.code });
        }
      }
    }
  }

  console.log(`\n================ SUMMARY ================`);
  console.log(`Total URLs Tested: ${totalTested}`);
  console.log(`Total Passed (HTTP 200/30x): ${totalPassed}`);
  console.log(`Total Failed: ${failedItems.length}`);

  if (failedItems.length > 0) {
    console.error(`\nFAILED ITEMS LIST:`, failedItems);
    process.exit(1);
  } else {
    console.log(`\n🎉 100% OF ALL URLS ARE VERIFIED AND WORKING!`);
  }
}

verifyAll();
