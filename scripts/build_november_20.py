# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
data=ROOT/'scripts/candidates-2026-11-20.json';used_path=ROOT/'scripts/all-used-urls.json'
report=json.loads((ROOT/'scripts/verification-2026-11-20.json').read_text())
assert report['passed'] and len(report['endpoints'])==72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest()==report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest()==report['used_sha256'],'Dedup database changed: verify again before generation.'
rows=json.loads(data.read_text());out=ROOT/'src/content/daily/2026-11-20.md'
assert not out.exists(),'Issue exists; inspect before overwriting.'
meta={'date': '2026-11-20', 'title': '11 月 20 日 · 模型谈估值，创作者谈交付', 'highlights': '九大赛道各四条：Gemini 4 Neon、Anthropic IPO 公告、数据中心外部成本、Vercel 多代理留言板、小团队工具、AI科幻长片与内容生意，以及业务规则和剧本结构。', 'draft': False, 'epigraph': '一次漂亮的生成，离一门能养活人的生意，还隔着很多小事。', 'lead': '一边是 Anthropic 的 IPO 公告和 Google 新模型，一边是双语报价单、抠图服务和独自完成的科幻长片。钱在向模型聚集，普通创作者也得回答自己的问题：客户到底为什么付费？今天这些材料给出的线索很具体。有人把笔记直接变成网站，有人替用户省掉漫长下载，有人把资产命名从口头传递做成规则。大能力落到小环节，才开始进入实际工作。与此同时，MIT 提醒我们看见算力之外的环境代价，独立音乐人的经历也让降本有了另一面。对产品人来说，今天值得重新算的账，既有生成和订阅，也有返工、交接与人的投入。先把一件承诺过的事稳稳做完，再判断下一项能力要不要加。', 'scene': '【虚构工作一幕】样片播完，客户点了点头，又问：「人物换个表情，其他地方能别动吗？」他关掉演示窗口，重新打开了分镜、图层和预算表。'}
meta['cover']=rows[24]['media'];meta['items']=rows
# JSON scalars are also valid YAML, so quotes, colons and line breaks are safe.
lines=['---']
for k,v in meta.items():
 if k!='items':lines.append(k+': '+json.dumps(v,ensure_ascii=False))
 else:
  lines.append('items:')
  for x in v:
   for j,(key,val) in enumerate(x.items()):lines.append(('  - ' if j==0 else '    ')+key+': '+json.dumps(val,ensure_ascii=False))
lines+=['---', '', '### 岛主今日寄语', '', '一个小工具把报价单排清楚，一次抠图省下反复描边，一份规则让同事不用再来问第三遍，这些事看起来都不大，却有具体的人愿意继续使用。今天的大新闻值得关注，手头的小交付也值得认真。模型、资金和平台还会快速变化，留在自己手里的，可以是一套用得顺的流程、一批反复回来的人，以及一部终于剪完的作品。做内容也好，做产品也好，都需要给那些不容易展示的工作留出时间：核对、修改、协商，还有把最后一点收拾干净。收费的底气，常常就是从这些地方慢慢攒出来的。', '', '采编说明：本期收录今日发现的新材料及较早发布的学习资源，具体发布时间以信源为准。模型测试、案例、价格及研究结论按来源口径呈现，未独立复测产品功能。IPO 信息依据公司公告，拟定安排不等于后续结果。编剧栏依据公开简介给出阅读与练习方向，完整阅读和改编权限以作者、信源说明为准。', '']
out.write_text('\n'.join(lines))
used=json.loads(used_path.read_text());new=used+[x['url'] for x in rows]
assert len(set(new))-len(set(used))==36
used_path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
print('Wrote',out,'; dedup',len(used),'->',len(new))
