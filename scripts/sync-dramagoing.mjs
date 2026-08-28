import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DRAMAGOING_ITEMS = {
  '2026-08-28': [
    {
      category: 'AI 漫剧',
      title: '出海短剧冰火局：中文在线半年报揭示的扭亏与并表账本',
      note: '全资 FlareFlow 扭亏（2.52 亿收入 / 1.52 亿净利），而 ReelShort 全年预估超 10 亿美元却因不并表难进母公司利润表。出海从红利期全面拐入系统能力期。',
      url: 'https://dramagoing.com/daily-brief/2026-08-28.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '靠单一爆款博概率的粗放时代结束，精细化财税、并表结构与多渠道发行成为头部玩家的核心壁垒。',
    },
    {
      category: 'AI 漫剧',
      title: '两份跑通信号：Kuku TV 闯入 TOP3、Reel.AI ARR 破千万，普通人的机会在哪？',
      note: 'DataEye 验证两条出海路径：印度 Kuku TV 凭借本土语种首闯素材榜前三，纯 AI 短剧 App Reel.AI ARR 突破千万。拆解个人创作者可抄的轻量路径。',
      url: 'https://dramagoing.com/articles/kuku-reelai-commercial-proof.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '非英语小语种市场和纯 AI 剧集验证了个人创作者无需重资产也能实现高 ROI 商业闭环。',
    },
    {
      category: 'AI 漫剧',
      title: '别死磕「伪人」：清华学者点名的非人叙事蓝海，正被 TikTok 算法验证',
      note: 'AI 短剧应少做仿真人类面孔、多做动物与非人物件叙事。TikTok 上动物拟人与科幻机甲 AI 漫剧的持续爆火正是算法用播放量投出的信任票。',
      url: 'https://dramagoing.com/articles/nonhuman-narrative-blueocean.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '避开高难度的真人微表情恐怖谷，在动物与奇幻非人叙事赛道更容易建立视觉风格壁垒。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 漫剧行业大洗牌：从抽卡式量产到 IP 精品化的存活法则拆解',
      note: '深度剖析为什么 90% 粗放式抽卡漫剧面临亏损，而以自研网文 IP 闭环与工业化 Agent 分镜为核心的团队正在实现破亿播放。',
      url: 'https://36kr.com/p/2890695024765696',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: 'AI 漫剧已告别靠工具赚快钱的红利期，内容叙事掌控力与系列化 IP 才是唯一的护城河。',
    },
  ],
  '2026-08-27': [
    {
      category: 'AI 漫剧',
      title: '免费层破 5000 万、付费层探英国：TikTok 短剧矩阵全速运转',
      note: 'TikTok 官方短剧应用 LimeShorts 免费层月活突破 5000 万，同时付费层启动欧洲英国市场测试，从流量批发商全面进化为内容零售商。',
      url: 'https://dramagoing.com/daily-brief/2026-08-27.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '平台自建短剧闭环对独立创作者意味着巨大的官方流量扶持与保底分账红利。',
    },
    {
      category: 'AI 漫剧',
      title: '收费站开张：LimeShorts 登陆美国，TikTok 构建三层短剧生态闭环',
      note: '从单向投流广告到应用内直接内购解锁，三层生态闭环截断传统短剧跳转流失链路，海量内容库存饥渴为个人创作者打开黄金供给窗口。',
      url: 'https://dramagoing.com/articles/limeshorts-us-launch.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '减少跳转链路后，短剧的付费转化率提升数倍，直接利好具备持续出片能力的创作者。',
    },
    {
      category: 'AI 漫剧',
      title: '2026，为什么是「一个人做漫剧出海」的黄金窗口期？',
      note: '四条核心数据链揭秘：海外投放暴涨 324%、IAA 广告变现半年增 150%、受众重合度仅 10%、站内获客成本降低 4 倍。',
      url: 'https://dramagoing.com/articles/window-2026-individual.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551836022-d5d88e9218df?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '工具降本与出海流量饥渴形成历史级交汇，单人即可完成过去整个制作公司的产能输出。',
    },
    {
      category: 'AI 漫剧',
      title: '爆款 AI 漫剧的叙事底层逻辑：强节奏、反转爽点与自有 IP 闭环',
      note: '解析在短视频快节奏消费下，男频末世与规则怪谈漫剧为何能持续霸榜，拆解情绪价值与视觉冲击的黄金组合拳。',
      url: 'https://36kr.com/p/2847525381987588',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: 'AI 漫剧的本质是「短剧内核+动画外壳」，精准击中受众情绪爽点是低成本破圈的关键。',
    },
  ],
  '2026-08-26': [
    {
      category: 'AI 漫剧',
      title: '成本塌了，收入也跑通了：AI 短剧正式跨过规模化盈利线',
      note: '制作成本从单集数万元骤降至几百元，单部剧集通过海外广告分账与 IAA 混合变现实现正向现金流，AI 短剧全面摆脱赔钱赚吆喝。',
      url: 'https://dramagoing.com/daily-brief/2026-08-26.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '跨过盈利平衡点意味着行业从试验探索正式迈入工业化规模复制阶段。',
    },
    {
      category: 'AI 漫剧',
      title: '0 团队、20 天、30 集：爆款 AI 短剧〈砚边青梅〉是怎么手搓出来的',
      note: '学 AI 两个月、单人独立完成 30 集古风 AI 短剧并成功上线头部平台。深度拆解可复制的执行步骤清单与关键技术边界。',
      url: 'https://dramagoing.com/articles/yanbianqingmei-breakdown.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '不需要数十人影视团队，掌握标准工作流的个人就能独立交付商业级影视连续剧。',
    },
    {
      category: 'AI 漫剧',
      title: 'Seedance 2.0 + Seed Audio + Vigloo：一个人够用的 AI 漫剧武器库',
      note: '影视级长视频生成、人声音效联合建模与跨集角色一致性控制，三件套拼成个人极简生产链，附完整对比表与实操配置。',
      url: 'https://dramagoing.com/articles/ai-drama-arsenal.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '精简工具链，避免盲目堆砌软件，把 80% 的精力集中在选品与叙事编排上。',
    },
    {
      category: 'AI 漫剧',
      title: '从抽卡拼凑到系列化剧 N 代：AI 漫剧如何破解「千人一面」的审美疲劳',
      note: '探讨为什么单一提示词生成的模板脸正在被观众抛弃，头部团队如何通过资产沉淀与长线世界观绑定打造长青剧集。',
      url: 'https://36kr.com/p/2908865886675718',
      source: '36kr.com',
      media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '克服模板化脸谱是建立高黏性粉丝心智的必经之路，角色资产化运营正在成为行业新共识。',
    },
  ],
  '2026-08-25': [
    {
      category: 'AI 漫剧',
      title: '北美赚钱、东南亚圈地，中东正在闷声发财：AI 漫剧全球分发地图',
      note: '北美高 ARPU 值贡献主力营收，东南亚靠海量用户打底，中东以极高客单价与文化定制成为新的高毛利蓝海市场。',
      url: 'https://dramagoing.com/daily-brief/2026-08-25.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '不同区域市场的付费习惯迥异，分层运营与本地化叙事是提升海外 ROI 的关键。',
    },
    {
      category: 'AI 漫剧',
      title: '红果 TOP10 占据 7 席，万兴 72 小时拿 50 万：国内漫剧验证与公司去魅',
      note: '最大流量池的数据验证了 AI 漫剧方向的确定性，同时证明小团队甚至个人凭借敏捷选品完全能跑赢大公司的冗长立项流程。',
      url: 'https://dramagoing.com/articles/domestic-proof-vs-company-myth.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '抄对爆款公式比盲目扩大团队规模重要得多，轻量化是个人创业者最核心的防御武器。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 漫剧出海：成本从 15 万美元崩塌到 15 万人民币，钱怎么收回来？',
      note: '制作成本崩塌只是第一步，跨境收款、财税合规与多币种提现才是隐形门槛。四大变现模式拆解与个人出海路线图。',
      url: 'https://dramagoing.com/articles/ai-drama-cost-collapse-payment.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1551434678-e076c223a692?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '尽早打通合规跨境收单管道，才能确保海外真金白银能够安全、低损耗地沉淀为实际利润。',
    },
    {
      category: 'AI 漫剧',
      title: 'AI 微短剧新规深度解读：出海是否能成为这轮监管的避风港？',
      note: '深入解析分类分层审核与 AI 标识硬指标，评估新规对低成本漫剧的实际冲击，并给出三条可落地的合规应对方案。',
      url: 'https://dramagoing.com/articles/ai-drama-regulation-july2026.html',
      source: 'dramagoing.com',
      media: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '出海不是法外之地，做好合规备案与原创素材沉淀是保障作品长期产生被动收益的前提。',
    },
  ],
};

for (const [date, dramaList] of Object.entries(DRAMAGOING_ITEMS)) {
  const filePath = path.join(TARGET_DIR, `${date}.md`);
  if (!fs.existsSync(filePath)) continue;

  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) continue;

  const frontmatter = yaml.load(match[1]);
  let existingItems = frontmatter.items || [];

  // Remove existing drama items
  existingItems = existingItems.filter((i) => i.category !== 'AI 漫剧');

  // Insert verified dramagoing items at position 1 (right after pinned item)
  const pinnedIdx = existingItems.findIndex((i) => i.pinned);
  const insertPos = pinnedIdx >= 0 ? pinnedIdx + 1 : 0;
  existingItems.splice(insertPos, 0, ...dramaList);

  frontmatter.items = existingItems;

  const newContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 ${existingItems.length} 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`✅ Injected ${dramaList.length} dramagoing AI 漫剧 articles into ${date}.md (Total items: ${existingItems.length})`);
}
