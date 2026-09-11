import fs from 'fs';
import { exec } from 'child_process';

const items = JSON.parse(fs.readFileSync('scripts/raw-ian-11.json', 'utf8'));

function checkUrl(url) {
  return new Promise((resolve) => {
    const isGetOnly = url.includes('wzbj1616.com');
    const flag = isGetOnly ? '-s -o /dev/null -w "%{http_code}"' : '-s -I -L --max-time 15';
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

async function run() {
  console.log(`Filtering and checking ${items.length} items for 2026-09-11...`);
  const valid = [];
  const invalid = [];

  // Filter 36kr first
  const non36kr = [];
  for (const it of items) {
    if (it.url.includes('36kr.com')) {
      console.log(`[FILTER 36KR] ${it.title}: ${it.url}`);
      invalid.push({ it, reason: '36kr' });
    } else {
      non36kr.push(it);
    }
  }

  for (let i = 0; i < non36kr.length; i += 15) {
    const chunk = non36kr.slice(i, i + 15);
    const results = await Promise.all(chunk.map((it) => checkUrl(it.url)));
    for (let j = 0; j < chunk.length; j++) {
      const it = chunk[j];
      const res = results[j];
      if (res.ok) {
        valid.push(it);
      } else {
        console.log(`[INVALID ${res.code}] ${it.title}: ${it.url}`);
        invalid.push({ it, reason: res.code });
      }
    }
  }

  console.log(`\nValid: ${valid.length}, Invalid: ${invalid.length}`);
  fs.writeFileSync('scripts/valid-ian-11.json', JSON.stringify(valid, null, 2));
  console.log(`Saved scripts/valid-ian-11.json`);
}

run();
