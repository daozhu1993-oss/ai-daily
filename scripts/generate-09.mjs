import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const CUSTOM_ITEMS_09 = [
  // AI 漫剧 (4)
  {
    category: 'AI 漫剧',
    title: '武汉团队AI漫剧保底25万/部，欧美定投模型已跑通',
    note: '跳出国内买量内卷的经典范例：通过精准对标欧美特定高客单人群的定制审美与反转剧本，达成单部漫剧 25 万元的海外发行保底。',
    so_what: '商业的终局不是拼无底线的低成本，而是拼非对称的定价权；找到海外付费意愿最高的受众池，一人漫剧团队也能跑出暴利现金流。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/wuhan-case.html',
    media: 'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: 'AI 漫剧',
    title: 'YouTube：AI短剧出海的第二战场',
    note: '深度拆解竖屏短剧在 YouTube Shorts 与长视频播放列表中的长尾变现模型：广告分成 + 会员锁章构筑的稳定复利水库。',
    so_what: '不要把鸡蛋放在同一个流量篮子里；YouTube 的长尾生命周期远超瞬时算法推流，双渠道矩阵布局是小团队抵御平台波动的安全垫。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/youtube-second-battlefield.html',
    media: 'https://images.unsplash.com/photo-1509281373149-e957c6296406?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: 'TikTok Growth Max for Mini Dramas：品牌也能做短剧，个人创业者跟不跟？',
    note: '字节最新短剧智能投放系统解析：广告预算从传统展示广告加速向定制微短剧倾斜，带来企业商单制作需求的结构性井喷。',
    so_what: 'B 端品牌的预算迁移是最大的增量红利；不仅要做 C 端买量剧，更要学会做承接企业定制商单的敏捷制作所。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/growth-max-brand-mini-dramas.html',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: 'AI 漫剧',
    title: '6月行业洗牌加速：谁活下来、凭什么？',
    note: '行业淘汰赛复盘：纯靠粗制滥造批量抽卡的投机团队成批阵亡，而坚持角色一致性、剧情工业化与合规版权的团队全面盈利。',
    so_what: '潮水退去才知道谁在裸泳；工业化与审美把关从来不是累赘，而是区分过客与常青树的生死分界线。',
    source: 'dramagoing.com',
    url: 'https://dramagoing.com/articles/h1-2026-shakeout.html',
    media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 编剧技巧 (4)
  {
    category: '编剧技巧',
    title: '涵盖所有电影类型的100个故事素材！',
    note: '全面梳理好莱坞经典 100 种戏剧原型与核心冲突库：从密室对抗到身份错位，为创作者提供取之不尽的剧本骨架。',
    so_what: '不要凭空硬憋灵感，灵感是建立在成熟母题之上的再发明；熟练掌握故事母题的排列组合，写剧本的速度就能提高十倍。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/866',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '编剧技巧',
    title: '网络视听司管理提示：微短剧要“爽”而有度',
    note: '权威监管合规深度解读：摒弃低俗擦边、反智宣泄与违背社会公序良俗的极端桥段，引导创作者转向健康有力量的爽感表达。',
    so_what: '安全合规是创作的终极底线；在政策框架内用巧妙的戏剧冲突实现高级的代入感，才能让作品具备持续长青的商业寿命。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/785',
    media: 'https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '电影剧本里的专业词汇（中英对照）',
    note: '系统整理分镜头脚本、摄影机调度、场面调度与剪辑标记的核心专业术语，助推国产剧本无缝对接海外影视制作管线。',
    so_what: '专业术语是高阶协作的通用货币；规范的分镜语言能大幅减少模型理解歧义，让 AI 引擎精准画出你脑海中的画面。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/844',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '编剧技巧',
    title: '编剧如何保护自己的剧本不被剽窃',
    note: '编剧维权全攻略：从版权登记节点、邮件抄送证据链存证到商业保密协议签署的法律实务防坑指南。',
    so_what: '知识资产是创作者最宝贵的财富；建立严密的防剽窃防侵权意识，才能在激烈的商业谈判中挺直腰杆。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/774',
    media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },

  // 产品经理 (4)
  {
    category: '产品经理',
    title: '产品经理要学会“见人下菜碟”',
    note: '与老板讲战略商业、与开发讲接口逻辑、与业务讲投入产出：拆解成熟 PM 如何用多套语言系统化解部门间的信息孤岛与博弈阻力。',
    so_what: '沟通的本质是对齐利益与心智模型；用对方听得懂的话把复杂意图推进落地，是产品经理不可替代的软实力。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6438747.html',
    media: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
    pinned: true,
  },
  {
    category: '产品经理',
    title: '内部产品经理的困局：做好了没人夸，做坏了全是锅',
    note: '剖析支撑型与后台系统 PM 的职业隐痛：如何在缺乏直接 GMV 汇报的情况下，用工时节约与业务流程加速证明团队核心价值。',
    so_what: '后台系统是企业肌肉的承重墙；学会把隐形的基础设施建设量化为管理层的显性安全资产，才能获得长久的资源倾斜。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6419202.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: 'Workbuddy继续免费，AI办公基础免费成定局，最后拼生态',
    note: '基础协同与 AI 助手全面进入零门槛时代：当套壳工具无法再收工具费，真正的竞争全面转向谁能整合客户的工作流生态与专属数据。',
    so_what: '功能免费化不可逆转，别再幻想靠简单 API 调用躺赚；把产品扎进行业生态的纵深处，做离业务最近的闭环服务。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/ai/6460555.html',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
  {
    category: '产品经理',
    title: '“系统流”短剧是很爽，但我就是怕它太爽了',
    note: '探讨短剧产品中极端多巴胺即时反馈机制对用户耐受阈值的破坏：为什么过于廉价的爽感会导致长期留存断崖式下跌。',
    so_what: '短期刺激换来短期数据，温润节制才能换来长期信赖；做产品切忌透支用户的注意力和心智，懂得留白与节制才是高级设计。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/it/6458966.html',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false,
  },
];

function balanceAndShuffle(baseItems, customItems) {
  const allItems = [...customItems, ...baseItems];
  const byCat = {};
  for (const it of allItems) {
    if (!byCat[it.category]) byCat[it.category] = [];
    byCat[it.category].push(it);
  }

  const categories = Object.keys(byCat).sort((a, b) => {
    const priority = ['AI 资讯', 'AI 漫剧', '产品经理', '编剧技巧', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 协作'];
    return priority.indexOf(a) - priority.indexOf(b);
  });

  const result = [];
  let added = true;
  while (added) {
    added = false;
    for (const cat of categories) {
      if (byCat[cat] && byCat[cat].length > 0) {
        result.push(byCat[cat].shift());
        added = true;
      }
    }
  }
  return result;
}

const rawIan = JSON.parse(fs.readFileSync('scripts/valid-ian-09.json', 'utf8'));
const finalItems = balanceAndShuffle(rawIan, CUSTOM_ITEMS_09);

console.log(`Day 2026-09-09: Total ${finalItems.length} items (Custom: ${CUSTOM_ITEMS_09.length}, Base: ${rawIan.length})`);

const frontmatter = {
  date: '2026-09-09',
  title: '9 月 9 日 · 垂类定投与生态重构：当漫剧跑通保底，工具转向内功',
  highlights: `全网 9 大领域 ${finalItems.length} 篇高密度精选：武汉团队欧美定投保底、YouTube短剧第二战场、微短剧“爽而有度”合规提示、产品经理见人下菜碟与AI办公生态重构。`,
  draft: false,
  epigraph: '当通用的工具全面转向基础免费，最值钱的不是界面的交互，而是能把真实业务数据变成现金流的垂直定投。',
  lead: '今天的技术与商业脉搏正在加速撕下浮夸的概念面具：在漫剧出海赛道，武汉团队依靠欧美定投模型跑通单部 25 万保底，AI 短剧全线开辟 YouTube 第二战场，标志着内容出海从单纯依赖投流平台，转向多渠道矩阵收益的成熟期；而在软件与产品端，Workbuddy 等通用工具相继走向基础功能免费，纯套壳工具的生存空间被极度压缩，逼迫产品经理退回真实业务场景，从内部协作摩擦、团队心智博弈与商业化闭环中挖掘坚固防线。',
  scene: '「海外的短剧分账又到账了？」「到账了。不要跟巨头抢主通道，走 YouTube 第二战场做欧美定投，一部保底 25 万，比在国内抢量稳多了。」',
  cover: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
  items: finalItems,
};

const editorial = `## 今日主理人寄语

当通用大模型与基础办公工具全面走向免费，商业世界最残酷也最清醒的法则再次显现：**没有门槛的工具终会变成零毛利的自来水，而真正能产生溢价的，永远是把特定人群、真实业务与商业闭环牢牢焊在一起的垂类解决方案。**

不论是武汉团队跳出传统国内内卷、依靠欧美精准定投模型跑通单部 25 万保底，还是产品经理在企业内部敏锐调和利益博弈、从“见人下菜碟”中提炼真需求，都在告诉我们同一个道理：**技术是浮在表面的波浪，而人性的利益与恐惧才是深不可测的海床；懂技术更懂分寸，小团队才能在狂风暴雨中稳稳立住脚跟。**

愿今天的 ${finalItems.length} 篇精选资讯，能成为你今天敲下第一行代码、写下第一个分镜剧本的灵感起点。
`;

const mdContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

${editorial}
`;

const targetPath = path.resolve('./src/content/daily/2026-09-09.md');
fs.writeFileSync(targetPath, mdContent, 'utf8');
console.log(`✅ Successfully generated ${targetPath}`);
