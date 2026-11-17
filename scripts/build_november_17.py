"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
data=ROOT/'scripts/candidates-2026-11-17.json';used_path=ROOT/'scripts/all-used-urls.json'
report=json.loads((ROOT/'scripts/verification-2026-11-17.json').read_text())
assert report['passed'] and len(report['endpoints'])==72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest()==report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest()==report['used_sha256'],'Dedup database changed: verify again before generation.'
rows=json.loads(data.read_text());out=ROOT/'src/content/daily/2026-11-17.md'
assert not out.exists(),'Issue exists; inspect before overwriting.'
meta=dict(date='2026-11-17',title='11 月 17 日 · 把 AI 的账算到任务上，把故事的账算到人物身上',highlights='9 大赛道各 4 条：TokenEconomizer 与企业 AI 成本、可接管的代理协作、小产品的窄切口、萌系动画与视频生产流程，以及故事结构和产品需求取舍。',draft=False,epigraph='一张便宜的账单，未必买得到一次完整的交付。',lead='今天这批信号，值得连起来看。微软把编码代理的节流办法放回历史任务里找，Databricks 把模型价格放到完成任务的账本上算；协作工具则忙着补进度、权限和接管入口。大家终于开始问：这件事到底做完没有，出了问题谁能接住？同样的问题也出现在内容生产里。萌系动画有了更快的生成流程，角色能不能撑到第二十集，却仍然要靠欲望、关系和冲突。小团队的机会，就藏在这些具体的缺口里：替用户省掉一段来回折腾，让作品可以修改，让任务可以恢复，让故事值得继续。今天不妨少开一个工具，多挑一件手头的事，把耗时、返工和实际结果记下来。',scene='【工作台上的虚构一幕】屏幕上四个代理都亮了绿灯。她没有点发布，而是打开交付文件：「灯亮了，东西呢？」桌边那杯咖啡已经凉了。',cover=rows[2]['media'],items=rows)
# JSON scalars are also valid YAML, so quotes, colons and line breaks are safe.
lines=['---']
for k,v in meta.items():
 if k!='items':lines.append(k+': '+json.dumps(v,ensure_ascii=False))
 else:
  lines.append('items:')
  for x in v:
   for j,(key,val) in enumerate(x.items()):lines.append(('  - ' if j==0 else '    ')+key+': '+json.dumps(val,ensure_ascii=False))
lines+=['---','','### 岛主今日寄语','','做产品和写故事，经常在同一个地方犯懒：以为事情发生了，价值就出现了。模型调用成功，不等于客户的问题解决了；镜头生成得漂亮，也不等于人物值得被记住。今天收录的工具与教程，可以拿来做一次很小的练习：选一个正在反复返工的任务，写清楚它给谁用、什么时候算完成，以及谁来判断。再选一个自己写不下去的人物，问他究竟想要什么，又愿意付出什么。工具能替我们省很多动作，取舍还得亲自做。','','采编说明：本期包含今日发现的工具与较早发布的学习材料；第三方案例数据保留来源归属。部分动态产品页的功能描述参考伊恩 11 月 17 日刊，未独立复测产品。编剧教程使用信源品牌图。','']
out.write_text('\n'.join(lines))
used=json.loads(used_path.read_text());new=used+[x['url'] for x in rows]
assert len(set(new))-len(set(used))==36
used_path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
print('Wrote',out,'; dedup',len(used),'->',len(new))
