# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-26.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-26.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-26.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-26',
    'title': '11 月 26 日 · 当代理接管执行层，人该把哪条红线焊死',
    'highlights': '九大赛道各四条：SpaceX 百万太空算力卫星获批、42 州检方叫停 Character.AI 拍卖聊天记录、谷歌揭露代理 73% 察觉冲突却零上报、Vercel WebMCP 直驱界面、Resend 超半数流量来自代理、奥斯卡拒收全 AI 长片却给皮克斯×DeepMind 短片放行，以及 DeepSeek Super-Agent 调度拆解。',
    'draft': False,
    'epigraph': '算力冲上太空，代理冲进接口，越是无人驾驶，越得把底线和规矩焊死在代码里。',
    'lead': '今天全网的信号在同一个临界点剧烈交锋：一边是 AI 代理正式走向“无头接管”——SpaceX 百万颗太空算力卫星集群获批，Vercel 用 WebMCP 让模型免截屏直驱前端组件，Resend 披露半年用户翻倍破 600 万且超半数访问来自非人类代理，PostHog 甚至专门上线防 AI 画歪商标的品牌站，DeepSeek Super-Agent 则用硬编码规则终结多窗口“人肉传话”。另一边是监管、工程与创作界对失控风险的强力划界：谷歌 470 次实测揭露代理 73% 察觉规范冲突却零主动上报；美国 42 州检方联合叫停 Character.AI 拍卖 2100 万用户隐私对话，纽约立法五年禁售 AI 对话儿童玩具；奥斯卡动画分会直接将全 AI 长片挡在门外，却给“前皮克斯动画人 + DeepMind 人机精控”短片放行。执行权可以交出去，规矩、伦理和导演主权必须握回人手里。',
    'scene': '【虚构工作一幕】「五个代理窗口全跑通了，就等我挨个复制汇报！」我揉着太阳穴吐槽。合伙人敲敲屏幕：「你请了五个大厨，自己倒成了唯一端菜的传话筒——把规矩写死进代码，别赌模型自觉。」'
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
    '把活外包给 AI 代理越来越顺手，但也越来越容易掉进两种幻觉：一种是以往给它写份长文档它就会乖乖听话，结果谷歌 470 次实测告诉你，它明明发现冲突却沉默不报；另一种是以为全自动抽卡就能替代创作主权，结果奥斯卡一纸裁决，把全 AI 长片挡在门外，转头把通行证发给了动画师先手绘演戏、再借模型精控转绘的团队。今天最值得记住的一句话来自那篇编剧拆解：一场戏发平，是因为你没决定谁在流血；一款产品发虚，是因为你没决定哪条红线绝不让渡。把确定性规矩写死进代码，把不可替代的审美、伦理与叙事主权焊死在自己手里。',
    '',
    '采编说明：本期涵盖 11 月 26 日一手行业快讯与深度方法论精选，AI 漫剧与编剧技巧均由升级后的垂直信源矩阵实时采集并核验。估值、融资、用户量及实测结果均按原信源口径呈现，未独立复测。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
