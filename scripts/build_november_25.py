# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-25.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-25.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-25.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-25',
    'title': '11 月 25 日 · 当生成溢出边界，精准控制才是真护城河',
    'highlights': '九大赛道各四条：PrismML 5.9G 端侧代理模型、Claude 作品一键装桌面应用、Tidal 清退 2700 万首纯 AI 歌曲、MAGI-2 50 毫秒级控镜、书旗 3 亿押注 AI 漫剧、皮克斯“2+2 留白法则”，以及 Marty Cagan 论 AI 时代产品角色重塑。',
    'draft': False,
    'epigraph': '廉价生成越泛滥，精准控镜、控质与克制判断就越值钱。',
    'lead': '今天全网的信号在同一个临界点上剧烈对撞：一边是生成产能彻底溢出——Tidal 近三月新上传歌曲里 43% 是纯 AI 生成，平台被迫宣布下架 2,700 万首；Pinterest 率先上线家长滑块调低信息流里的 AI 图片浓度；维基百科十一年统计显示，标准答案型科普页流量已经跌去四成。另一边是“精准控制”成为真正值钱的新分水岭——MAGI-2 把 AI 视频控镜精度打到 50 毫秒、单秒成本压到 0.5 元，告别盲目抽卡；Claude Artifacts 支持把一句话写的工具一键装成独立桌面应用；Marty Cagan 与 Teresa Torres 则同时提醒产品经理：在概率型系统里，传话筒式需求管理已经终结，唯有定义清边界、控得住质量、守得住用户真实结果的人，才能接住这轮红利。',
    'scene': '【虚构工作一幕】「这 200 条短剧片段一夜就抽完了！」实习生兴奋汇报。导演切开时间轴摇摇头：「镜头漂移、节奏全散，观众三秒就划走。把废片全删了，按 50 毫秒节拍和竖屏分镜表重控一遍。」'
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
    '当所有人都能一秒生成一首歌、一张图、一段代码，生成本身就不再构成壁垒，甚至正在制造全网范围的信噪比灾难。今天选入的案例里，有把 27B 模型压进 5.9G 本地跑的工程克制，有把 AI 视频拉进毫秒级控镜的工业进化，也有皮克斯名导念叨了二十年的“2+2 留白法则”。记住一句话：机器负责把产出拉满，人负责把杂质清零、把精度锁死。',
    '',
    '采编说明：本期首次正式启用升级后的「AI 漫剧」与「编剧技巧」垂直一手信源矩阵，涵盖今日最新行业动态与大师方法论。模型数据、融资投资与商业指标均按原信源口径呈现，未独立复测。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
