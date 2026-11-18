# coding: utf-8
"""Generate only from the verified candidate snapshot; then append dedup URLs."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
data=ROOT/'scripts/candidates-2026-11-18.json';used_path=ROOT/'scripts/all-used-urls.json'
report=json.loads((ROOT/'scripts/verification-2026-11-18.json').read_text())
assert report['passed'] and len(report['endpoints'])==72 and all(x['ok'] for x in report['endpoints'])
assert hashlib.sha256(data.read_bytes()).hexdigest()==report['candidate_sha256']
assert hashlib.sha256(used_path.read_bytes()).hexdigest()==report['used_sha256'],'Dedup database changed: verify again before generation.'
rows=json.loads(data.read_text());out=ROOT/'src/content/daily/2026-11-18.md'
assert not out.exists(),'Issue exists; inspect before overwriting.'
meta={'date': '2026-11-18', 'title': '11 月 18 日 · 成功提示亮了，事情真的办完了吗？', 'highlights': '九大赛道各四条：Gemini 代办任务、Replit Missions 的预算边界、编码会话交接、表单假成功测试、互动视频叙事，以及场景写作与产品验收。', 'draft': False, 'epigraph': '最需要验收的，往往是那些看起来已经成功的地方。', 'lead': '今天最让我停下来的，是一项联系表单测试：页面显示发送成功，背后却没有携带输入内容的请求。这个小问题，正好照见 AI 产品正在跨过的门槛。Gemini 开始预约、付账和购物，Replit 用目标与预算组织代理执行；能力越接近真实生活，一次假成功就越难被原谅。协作工具也在补功课：截图带着位置进入修复，决定和纠正留给下一场会话。内容生产同样如此，观众在互动视频里做了选择，下一幕就应该有所回应。对产品人来说，今天值得做的事很具体：打开一个自己已经交付的功能，顺着用户的动作走到最后，看看钱、消息、文件或剧情，究竟有没有抵达该到的地方。', 'scene': '【虚构工作一幕】她点完提交，绿色提示亮起。十分钟后，收件箱还是空的。「刚才到底发给谁了？」同事打开请求记录，两个人都没再说话。'}
meta['cover']=rows[3]['media'];meta['items']=rows
# JSON scalars are also valid YAML, so quotes, colons and line breaks are safe.
lines=['---']
for k,v in meta.items():
 if k!='items':lines.append(k+': '+json.dumps(v,ensure_ascii=False))
 else:
  lines.append('items:')
  for x in v:
   for j,(key,val) in enumerate(x.items()):lines.append(('  - ' if j==0 else '    ')+key+': '+json.dumps(val,ensure_ascii=False))
lines+=['---', '', '### 岛主今日寄语', '', '做产品的人很容易爱上那些一眼就能展示的进步：页面更漂亮了，回答更流畅了，生成的视频也更像那么回事。可用户过日子，靠的是后面那些不显眼的环节。消息有没有送到，预约有没有落定，改掉一个细节会不会弄坏别处，故事里的选择有没有留下后果。今天这些工具和文章，适合拿来检查自己的交付习惯。别急着加下一项能力，先把一条已经承诺过的路径走通；遇到不确定的地方，就留下回执、确认和接手的位置。让用户少猜一次发生了什么，你的产品就多一分被继续使用的理由。', '', '采编说明：本期收录今日发现的新工具与较早发布的学习材料，文中保留厂商自述和第三方研究的适用范围。未独立复测产品功能或研究结论。两篇无文章配图的编剧教程使用信源品牌图；两篇剧本推荐依据公开介绍，完整阅读以信源提供的入口为准。', '']
out.write_text('\n'.join(lines))
used=json.loads(used_path.read_text());new=used+[x['url'] for x in rows]
assert len(set(new))-len(set(used))==36
used_path.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n')
print('Wrote',out,'; dedup',len(used),'->',len(new))
