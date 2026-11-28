# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib, json

ROOT = Path(__file__).resolve().parents[1]
data = ROOT / 'scripts/candidates-2026-11-28.json'
used_path = ROOT / 'scripts/all-used-urls.json'
report = json.loads((ROOT / 'scripts/verification-2026-11-28.json').read_text())

assert report['passed'] and len(report['endpoints']) == 72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest() == report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest() == report['used_sha256'], 'Dedup database changed: verify again before generation.'

rows = json.loads(data.read_text())
out = ROOT / 'src/content/daily/2026-11-28.md'
assert not out.exists(), 'Issue exists; inspect before overwriting.'

meta = {
    'date': '2026-11-28',
    'title': '11 月 28 日 · 跳过旧商店与旧流程，AI 新分发管道正式合龙',
    'highlights': '九大赛道各四条：小红书素人笔记挂 Vibe Coding 轻应用玩出 18.2 万人次、支付宝 SkillPay 打通 Agent 技能挂牌变现、OpenAI 反诉苹果施压供应链、iOS 27.3 云端 Siri 设每日 20 次配额、豆包独家接入剪映双轨剪辑、红果短剧日活 1.68 亿抢攻客厅大屏，以及纽约时报封禁 Photoshop 2027。',
    'draft': False,
    'epigraph': '当一篇笔记能直接挂出 18 万人玩的轻应用，当一个技能包能按 1% 费率挂牌收钱，旧分发高墙正在集体松动。',
    'lead': '今天全网的信号都在指向同一场大迁徙：绕开臃肿旧商店与繁琐旧软件的新分发管道，正在以肉眼可见的速度合龙。一边是新通路全面跑通——小红书创作者用 Vibe Coding 把“折星星”交互页面直接挂在笔记底部，不到三千粉就撬动 18.2 万人次体验；支付宝 SkillPay 上线让 Agent 技能正式挂牌收钱，买断交本地、订阅走云端沙盒护明文源码；豆包独家接入剪映，把“一句话粗剪”和“多轨草稿精修”接成闭环；日活飙到 1.68 亿反超“爱优腾芒”总和的红果短剧，则顺势向客厅电视大屏挥师。另一边，旧秩序的摩擦与成本警钟同步拉响：OpenAI 反诉苹果窃密并指控施压供应链，iOS 27.3 拟给云端 Siri 设日限 20 枚配额开始算力收租，纽约时报干脆对自由摄影师禁用 Photoshop 2027 以防隐藏 AI 误打 C2PA 标签，就连机械硬盘也彻底告别六年百元每 TB 的旧时代。',
    'scene': '【虚构工作一幕】「不到三千粉的小号，把 AI 写的折星星页面挂在笔记底下，一夜玩了十几万人！」增长经理瞪大眼。老板合上应用商店驳回邮件：「别死磕旧入口了，明天全员改做内容流里的轻应用。」'
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
    '很长一段时间里，独立开发者和内容创作者都被卡在两道老门槛前：想做软件，得熬过打包、上架审核和买量冷启动；想卖技能和工作流，只能写成免费文档赚几声吆喝。今天看到的两个切口彻底改写了游戏规则——在小红书评论区里，普通人已经靠挂在笔记底部的 Vibe Coding 轻应用直接跑出十几万真实游玩；在支付宝 SkillPay 里，一个打包好的 Agent 技能也能像正规商品一样明码标价、云端护源码、按 1% 费率结算。别再守着上一代应用商店和按席位月付的老黄历打转，去离用户注意力最近、离代理调用链路最短的地方搭你的新货架。',
    '',
    '采编说明：本期覆盖 11 月 28 日一手科技动态、垂直 AI 漫剧与编剧技巧及产品商业深度拆解，全部 36 篇外链与 36 张配图均通过真机 GET 实测。日活、游玩人次、价差测算与费率均按原信源公开口径呈现，未独立复测。',
    ''
]

out.write_text('\n'.join(lines))
used = json.loads(used_path.read_text())
new = used + [x['url'] for x in rows]
assert len(set(new)) - len(set(used)) == 36
used_path.write_text(json.dumps(new, ensure_ascii=False, indent=2) + '\n')
print('Wrote', out, '; dedup', len(used), '->', len(new))
