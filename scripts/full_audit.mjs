import fs from "fs";
import path from "path";
import { exec } from "child_process";
import { promisify } from "util";
const execAsync = promisify(exec);

const dir = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily";
const targetDates = [
  "2026-10-27",
  "2026-10-26",
  "2026-10-25",
  "2026-10-24",
  "2026-10-23",
  "2026-10-22",
  "2026-10-21",
  "2026-10-20",
  "2026-10-19"
];

const allItems = [];
for (const date of targetDates) {
  const file = `${date}.md`;
  const filePath = path.join(dir, file);
  if (!fs.existsSync(filePath)) continue;
  const content = fs.readFileSync(filePath, "utf-8");
  const regex = /category:\s*"([^"]+)"\s*\n\s*title:\s*"([^"]+)"[\s\S]*?url:\s*"([^"]+)"/g;
  let match;
  while ((match = regex.exec(content)) !== null) {
    allItems.push({
      file,
      category: match[1],
      title: match[2],
      url: match[3]
    });
  }
}

console.log(`Auditing ${allItems.length} items across ${targetDates.length} days...`);

async function checkItem(item) {
  // Use curl with follow redirects and 6s timeout
  const escapedUrl = item.url.replace(/"/g, '\\"');
  const cmd = `curl -s -L --max-time 6 -o - -w "\n<<<SPLIT>>>%{http_code}\n%{url_effective}" -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36" "${escapedUrl}"`;
  try {
    const { stdout } = await execAsync(cmd, { maxBuffer: 5 * 1024 * 1024 });
    const parts = stdout.split("\n<<<SPLIT>>>");
    const html = parts[0] || "";
    const metaLines = (parts[1] || "").trim().split("\n");
    const code = metaLines[0] || "000";
    const finalUrl = metaLines[1] || item.url;
    
    const titleMatch = html.match(/<title[^>]*>([^<]+)<\/title>/i);
    const pageTitle = titleMatch ? titleMatch[1].replace(/\s+/g, " ").trim() : "(No <title>)";
    
    let isError = false;
    let reason = "OK";
    
    if (code === "404" || pageTitle.includes("404") || pageTitle.includes("页面未找到") || pageTitle.includes("Not Found")) {
      isError = true;
      reason = "404 Not Found";
    } else if (code === "500" || code === "502" || code === "503" || code === "504") {
      isError = true;
      reason = `HTTP ${code} Server Error`;
    } else if (code === "000") {
      isError = true;
      reason = "Connection Timeout / Refused";
    } else if (code === "403") {
      // Could be WAF or forbidden
      reason = "HTTP 403 Forbidden / Anti-bot";
      isError = true;
    }
    
    return {
      file: item.file,
      category: item.category,
      itemTitle: item.title,
      url: item.url,
      finalUrl,
      code,
      pageTitle,
      reason,
      isError
    };
  } catch (err) {
    return {
      file: item.file,
      category: item.category,
      itemTitle: item.title,
      url: item.url,
      finalUrl: item.url,
      code: "000",
      pageTitle: "(Error)",
      reason: err.message,
      isError: true
    };
  }
}

async function runPool(items, limit) {
  const results = [];
  let idx = 0;
  async function worker() {
    while (idx < items.length) {
      const cur = idx++;
      results[cur] = await checkItem(items[cur]);
      const r = results[cur];
      const status = r.isError ? `[FAIL: ${r.reason}]` : "[OK]";
      console.log(`[${cur + 1}/${items.length}] ${status} ${r.file} [${r.category}] ${r.itemTitle.slice(0, 25)} -> ${r.url}`);
    }
  }
  await Promise.all(Array.from({ length: limit }, () => worker()));
  return results;
}

const results = await runPool(allItems, 12);
const failures = results.filter(r => r.isError);
console.log(`\n==========================================`);
console.log(`AUDIT COMPLETE: Total ${results.length}, Failures: ${failures.length}`);
console.log(`==========================================`);

fs.writeFileSync("/tmp/audit_all_results.json", JSON.stringify(results, null, 2));
fs.writeFileSync("/tmp/audit_all_failures.json", JSON.stringify(failures, null, 2));
