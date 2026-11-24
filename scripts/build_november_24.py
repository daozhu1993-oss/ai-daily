# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-24.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-24.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-24.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-24',
    'title': '11 月 24 日 · 当买家变成代理，人靠什么留住信任？',
    'highlights': '九大赛道各四条：循环架构 GLM-5.4、AISI 安全评测漏洞、Claude Ship 自动审修 PR、本地纯文本 CRM、代码派生设计规范、a16z 万次代理购物 B2A 法则、Sora 退场复盘，以及说书人复仇局与产品颠覆诊断。',
    'draft': False,
    'epigraph': '代理接管筛选之后，花哨包装失效，真实参数与手艺反而更值钱。',
    'lead': '今天的几条信号拼出了同一张商业切面：a16z 跑完一万多次代理购物实测，宣告面向 AI 买家的 B2A 经济正式成型；Claude Ship 开始自动审查、修补并按策略审批 PR；而英国 AISI 的研究冷水浇头——换一种攻击策略，原本漏报率只有 0.2% 的安全监视器直接飙升到 22.7%。当代理开始替人挑商品、审代码、管日程，两条看似矛盾的规律正在同时生效：面向机器的那一面，产品必须极其结构化、可校验，就像把设计规范写进构建契约、把客户资料存成本地纯文本；而面向人类的那一面，大牌节日广告集体回归手工动画，甚至连疑似 AI 补帧都要被观众拿着放大镜审视。对转型中的产品人和创作者而言，今天最值钱的清醒是分清边界：把繁琐流转交给代码契约，把真实手艺与信任留给人。',
    'scene': '【虚构工作一幕】「推广页改完三版，为什么代理比价器全把我们过滤掉了？」运营盯着报表发懵。产品经理翻开页面源码叹了口气：「你把真实价格藏在三层弹窗和营销海报图里，AI 买家根本懒得猜。」'
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
    '效率工具越发达，糊弄人的成本越低，被识破的速度也越快。今天入选的案例里，有的用纯文本把一人公司数据牢牢握在本地，有的用代码构建期强校验取代注定过期的文档，有的则因大厂收紧路线或广告细节穿帮付出代价。不管你的下一个客户是坐在屏幕前的人，还是替他下单的 AI 代理，靠信息差和花架子讨巧的窗口都在迅速关闭。把结构做透明，把手艺做扎实，才是穿越周期的硬通货。',
    '',
    '采编说明：本期包含今日发现的一手动态与精选行业复盘，发布时间以各信源官方记录为准。模型表现、融资估值与测试数据均按来源口径呈现，未独立复测。剧本解析依据公开简介提供结构拆解与创作练习参考，完整阅读及版权合作请以原平台规则为准。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
