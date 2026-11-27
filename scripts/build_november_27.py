# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-27.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-27.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-27.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-27',
    'title': '11 月 27 日 · 撕掉滤镜与黑箱，AI 产品进入硬核账本时代',
    'highlights': '九大赛道各四条：英伟达开源 Nemotron 3.5 解析套件、谷歌强制代理走 MCP 却锁死 Gmail 发信、Obsidian 官方多代理连接器、MakerGain 核验 158 个 AI 产品真实变现、Epic 虚幻引擎 6 砍掉 Blueprints、Tripo H3.5 素模盲评夺冠，以及消协近百万投诉拷问“转人工难”。',
    'draft': False,
    'epigraph': '概念滤镜退潮后，留在牌桌上的只有算得清账、兜得住底、经得起裸测的硬货。',
    'lead': '今天全网的信号都在戳破同一个泡沫：AI 正在告别靠演示视频画大饼的草莽期，全面转入算硬账、验真货的深水区。一边是底层工具彻底剥掉多余花架子——Epic 宣布虚幻引擎 6 砍掉 Blueprints 蓝图押注 AI 迁移两万脚本，Obsidian 放出官方多代理连接器同时把文件死守本机，SC26 现场 45°C 温水液冷正在悄悄淘汰传统冷水机，VAST 的 Tripo H3.5 甚至剥掉贴图在 192 组 3D 素模盲评里硬刚夺冠。另一边是全社会对“黑箱期货”与“甩锅式 AI”的硬核清算：韩国反垄断机构正式审议苹果 AI 宣传延期 18 个月，MiniMax 旗下 Talkie 因风控失守遭苹果下架，谷歌强制 Workspace 代理走 MCP 却把 Gmail 锁死在只读存草稿，全国消协近百万件投诉更是直指“不让转人工”的 KPI 畸形设计；而 MakerGain 和 BizGut 直接把 158 个 AI 产品和独立开发者的营收账本逐条标源摊在阳光下。',
    'scene': '【虚构工作一幕】「AI 客服拦截率冲上 92% 了！」运营刚报完喜，负责人把消协投诉表拍在桌上：「用户连敲十遍转人工都找不到活人，你省下的是人力账，烧光的是信任底。」'
}

meta['cover'] = rows[0]['media']
meta['items'] = rows

lines = ['---']
for k, v in meta.items():
    if k != 'items':
        lines.append(k + ': ' + json.dumps(v, ensure_ascii=False))
    else:
        lines.append('items:')
        for x in v:
            for j, (key, val) in enumerate(x.items()):
                lines.append(('  - ' if j == 0 else '    ') + key + ': ' + json.dumps(val, ensure_ascii=False))
lines += [
    '---',
    '',
    '### 岛主今日寄语',
    '',
    '今天有两条看似无关的新闻，拼在一起却最扎心：一边是转转干了十一年、关掉轻飘飘的自由市场，靠自己扛起质检和履约风险跑出 200 亿营收；另一边是大量 AI 客服把“转人工”藏进迷宫，试图用技术把售后麻烦甩回给用户。不管模型参数多大、算力多便宜，商业世界有一条铁律从来没变——谁替用户兜住最棘手的不确定性，谁就拿走利润；谁把不确定性甩回给用户，早晚被反噬。别再迷信滤镜和概念，去搭好你的 Evals 评测题库，算清你的真实账本，给用户留好那扇体面的逃生门。',
    '',
    '采编说明：本期覆盖 11 月 27 日一手技术动态、垂直漫剧与编剧方法论及商业产品复盘，所有外链与配图均经真机 GET 实测通过。营收、估值、投诉统计与评测排名均按原信源公开口径呈现，未独立复测。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
