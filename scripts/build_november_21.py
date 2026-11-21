# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
data=ROOT/'scripts/candidates-2026-11-21.json';used_path=ROOT/'scripts/all-used-urls.json'
report=json.loads((ROOT/'scripts/verification-2026-11-21.json').read_text())
assert report['passed'] and len(report['endpoints'])==72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest()==report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest()==report['used_sha256'],'Dedup database changed: verify again before generation.'
rows=json.loads(data.read_text());out=ROOT/'src/content/daily/2026-11-21.md'
assert not out.exists(),'Issue exists; inspect before overwriting.'
meta={'date': '2026-11-21', 'title': '11 月 21 日 · 写得更快以后，判断该留在哪里？', 'highlights': '九大赛道各四条：循环推理小模型、密码分析研究、处理器设计实验、浏览器代理与自动修复、可编辑文档、营销基础设施变化，以及需求判断和剧本线索。', 'draft': False, 'epigraph': '省下的操作，最后都要有人接住它的后果。', 'lead': '今天的工具正在把更多操作收进后台：浏览器代理压缩页面信息，流水线出错后自动提出修复，文档和任务文件也能直接变成界面。操作变快，判断的重量就落到了新的地方。谁确认修复可以合并，谁知道一段计算已经过期，谁能看出两份看似不同的 AI 建议其实来自同一个模板？小模型和硬件实验让个人可以尝试过去难以进入的领域，也更需要把演示、验证和可交付成果分开。对产品人来说，今天最实用的投入，是给流程留下几个清楚的位置：证据在哪里，决定由谁作出，失败后怎样退回来。创作也一样，工具可以把镜头和素材做出来，人物为什么选择、线索何时揭开，仍然决定作品能不能留住人。', 'scene': '【虚构工作一幕】修复分支生成了，屏幕上全是绿勾。她打开变更文件，问了一句：「这个异常以前为什么要留着？」会议室里，终于有人翻出了旧工单。'}
meta['cover']=rows[0]['media'];meta['items']=rows
# JSON scalars are also valid YAML, so quotes, colons and line breaks are safe.
lines=['---']
for k,v in meta.items():
 if k!='items':lines.append(k+': '+json.dumps(v,ensure_ascii=False))
 else:
  lines.append('items:')
  for x in v:
   for j,(key,val) in enumerate(x.items()):lines.append(('  - ' if j==0 else '    ')+key+': '+json.dumps(val,ensure_ascii=False))
lines+=['---', '', '### 岛主今日寄语', '', '一份方便的工具，最好能让人少做重复动作，又保留理解事情的机会。今天选入的项目里，有的把依赖关系画出来，有的让任务继续住在普通文件里，有的把修复交回审查。它们能帮我们腾出时间，但这段时间值得怎样使用，也需要自己决定。可以去看一个失败案例，听一个客户把问题说完，或者为故事里的一个选择补上代价。持续使用 AI 之后，仍然知道自己为什么这么做，是一件需要练习的事。', '', '采编说明：本期包含今日发现的新材料和较早发布的学习资源，发布时间以信源为准。性能与案例按来源口径呈现，未独立复测产品。收购协议不等于完成交割；研究与实验不等于成熟量产。编剧栏依据公开简介提供阅读和练习方向，完整阅读及使用权限以作者、信源说明为准。', '']
out.write_text('\n'.join(lines))
used=json.loads(used_path.read_text());new=used+[x['url'] for x in rows]
assert len(set(new))-len(set(used))==36
used_path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
print('Wrote',out,'; dedup',len(used),'->',len(new))
