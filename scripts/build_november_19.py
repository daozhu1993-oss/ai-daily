# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
data=ROOT/'scripts/candidates-2026-11-19.json';used_path=ROOT/'scripts/all-used-urls.json'
report=json.loads((ROOT/'scripts/verification-2026-11-19.json').read_text())
assert report['passed'] and len(report['endpoints'])==72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest()==report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest()==report['used_sha256'],'Dedup database changed: verify again before generation.'
rows=json.loads(data.read_text());out=ROOT/'src/content/daily/2026-11-19.md'
assert not out.exists(),'Issue exists; inspect before overwriting.'
meta={'date': '2026-11-19', 'title': '11 月 19 日 · 记忆有来路，能力有边界', 'highlights': '九大赛道各四条：混元开放权重、分离式推理、可追溯的代理记忆、现场小工具、营销预测与实际效果、AI短剧授权，以及剧本阅读和产品判断。', 'draft': False, 'epigraph': '能力写在介绍里，边界要落在使用的每一步。', 'lead': '今天的几条信号，都在提醒同一件事：把一项能力交到别人手里时，也要把它的来路和限制交代清楚。混元开放了权重与部署入口，许可仍需逐项看；能量式推理展示了新路线，实验范围却不能随意放大。Honcho 开始让人检查记忆结论如何形成，营销工具则需要把预测评分和真实效果分开。这样的分寸，同样关乎内容创作：一张脸进入 AI 短剧后，授权能走到哪，不能靠熟人之间一句答应。对产品人和独立开发者来说，这些细节都有很实际的价值：用户知道哪里能依赖你、哪里需要自己确认，才更容易把工具接进长期工作。做功能时，留一点位置给出处、条件和退出方式。', 'scene': '【虚构评审一幕】她指着代理保存的用户画像问：「这条结论从哪来的？」屏幕展开了三段旧对话。同事看了看，把其中一条过时的推断划掉。'}
meta['cover']=rows[0]['media'];meta['items']=rows
# JSON scalars are also valid YAML, so quotes, colons and line breaks are safe.
lines=['---']
for k,v in meta.items():
 if k!='items':lines.append(k+': '+json.dumps(v,ensure_ascii=False))
 else:
  lines.append('items:')
  for x in v:
   for j,(key,val) in enumerate(x.items()):lines.append(('  - ' if j==0 else '    ')+key+': '+json.dumps(val,ensure_ascii=False))
lines+=['---', '', '### 岛主今日寄语', '', '把工具推荐给朋友时，我们通常很会说它能做什么，却容易漏掉后半句：在什么条件下，做到什么程度。今天选进来的产品，有的把公式放在结果旁，有的让人看到记忆更新的依据，有的明确承认演示数据只是样例。这些做法不热闹，却能省掉以后许多解释。内容创作也一样，借来的故事、面孔和素材，都有各自的来路；理解它们的使用范围，本来就是制作的一部分。今天可以挑一个正在做的产品或作品，补上一处之前没说清的条件。让别人知道怎样安心地接着用，也是一种交付。', '', '采编说明：本期包含今日发现的新工具及较早发布的学习材料；性能、收入、案例和研究结论按来源口径呈现，未独立复测。TypeFighter 的玩法描述参考伊恩今日刊。编剧栏依据剧本公开简介给出阅读与练习方向，未将其作为完整剧本细读；阅读与改编权限以作者和信源说明为准。', '']
out.write_text('\n'.join(lines))
used=json.loads(used_path.read_text());new=used+[x['url'] for x in rows]
assert len(set(new))-len(set(used))==36
used_path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
print('Wrote',out,'; dedup',len(used),'->',len(new))
