# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-23.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-23.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-23.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-23',
    'title': '11 月 23 日 · 越是速成时代，越要讲求诚实与尺度',
    'highlights': '九大赛道各四条：跨厂困惑度基准标尺、艺术家型 PM 护城河、自托管抓包排障、纯前端 WASM 修 PDF、百年设计馆特展海报、差评潮后撤 AI 配乐、3D 资产自动管线，以及法医物证链与交互智能。',
    'draft': False,
    'epigraph': '“快”是算法的本能，“真”是创作者的信誉。',
    'lead': '当大模型能够一键生成配乐、分镜、代码乃至整套 CRM 界面，生成的速度早已不再是瓶颈，真正的考验落在了内容的真实性与使用尺度上。今天，Steam 社区对《以撒的结合》偷偷混入 AI 配乐发起集中差评抗议，直到主创道歉并重做人工音轨才告平息；而在另一端，OpenRouter 针对探针曝光的提示词留存风险紧急下架违规节点，Signal 甚至不得不针对系统级 AI 扫屏主动限制手机截屏。这些信号都在传递同一个事实：用户对“被隐瞒”、“被侵入”的容忍度正在降至冰点。工具赋能了个体一人公司的无限可能，你可以用纯 Canvas 做出即玩赛车，也可以把复杂抓包做成自托管单兵武器，但越是在速成时代，企业与创作者越需要对交付成果保持诚实。决定产品生命周期的，从来不是你用 AI 省下了多少工时，而是你是否守得住用户对你的那份底层信任。',
    'scene': '【虚构工作一幕】游戏更新发版半小时，社区论坛被一条音轨频谱截图引爆：「这转音里的生成杂音是怎么回事？」制作人连夜拉开主控台，对着满屏的差评红字叹气：「把所有生成曲目全部下掉，天亮前必须发致歉声明。」'
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
    'AI 极大地降低了制造“看起来像那么回事”的门槛，但也成倍放大了侥幸心理的代价。今天入选的项目里，有的倡议用最底层的困惑度指标替代花哨榜单，有的团队公开分享了三套标准尺寸图标的自动化管线，有的编剧坚持在刑侦剧里把每一步物证链推演到底。它们都在告诉我们：偷懒走捷径省下的力气，最后往往要在公关和返工中加倍偿还。把机器生成的杂音过滤掉，把该做的人工推敲做扎实，你的产品才会有击中人心的分量。',
    '',
    '采编说明：本期包含今日发现的新动态与精选专业解析，发布时间以各信源官方记录为准。技术指标与测试结果来自发布方口径，未在全硬件环境下独立复测。协议与倡议不等于强制行业标准；商业策略与人事变动以各企业最终官方公报为准。剧本解析依据公开信息提供结构分析与创作练习建议，完整版权与使用权限以原创平台约定为准。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
