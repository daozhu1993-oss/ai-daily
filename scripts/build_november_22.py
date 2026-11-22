# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-22.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-22.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-22.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-22',
    'title': '11 月 22 日 · 把底图打稳，把因果说清',
    'highlights': '九大赛道各四条：端侧量化编译器、蒙特卡洛多解搜索、单文件嵌入数据库、提词刘海屏与误发拦截、室外动态立面、隐私履约与肖像授权、爆款短剧工业化、双线叙事与评测集护城河。',
    'draft': False,
    'epigraph': '工具再快，系统的上限依然取决于最底层的因果与边界。',
    'lead': '今天的技术正在以前所未有的密度下放：从把大模型压进 5GB 内存的端侧编译器，到把完整 PostgreSQL 塞进单二进制文件的独立开发实践，单兵作战的物理阻力被迅速抹平。而在另一端，智能体协作正在探索蒙特卡洛多解搜索，短剧工业化把演员肖像、生成分镜与 3D 骨骼串成天级流水线。但随着工具越跑越快，决定系统成败的关键，反而回到了那些最质朴的锚点：智能体拿到了权限，数据库会不会被误删穿？短剧前三秒有了抓手，人物因果能不能立得住？AI 需求上线了，业务评测集能不能测出 Corner Case？对转型期的产品人与独立创作者而言，今天最有复利的动作，从来不是盲目追赶每一个新模型，而是把自己的底图打稳，把业务的因果说清。',
    'scene': '【虚构工作一幕】「换脸模型调通了，今天能批量出 50 集！」会议室里一片欢呼。主理人按灭了屏幕，指着第三集的分镜问：「这姑娘第一集被赶出家门，第三集怎么就凭空拿到祖传秘方了？因果接不上，打回重写。」'
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
    '一份成熟的交付物，最宝贵的不是“能生成什么”，而是“清楚自己不能做什么”。今天选入的项目里，有的在安装前给 Agent 扫描投毒规则，有的给回车键加了防误触阻尼，有的在代码里把指标口径严格沉淀为语义层。它们都在提醒我们：在充满概率与幻觉的生成时代，真正的专业主义，是为不确定性筑起确定的防护网。愿你在狂飙的浪潮里，始终守得住自己的因果与底线。',
    '',
    '采编说明：本期包含今日发现的新材料与经典创作解析，发布时间以各信源官方记录为准。性能指标与案例来自发布方口径，未在全硬件环境下独立复测。投资协议不等于最终交割；实验突破不等于成熟量产。剧本解析依据公开信息提供结构分析与创作练习建议，完整版权与使用权限以原创平台约定为准。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
