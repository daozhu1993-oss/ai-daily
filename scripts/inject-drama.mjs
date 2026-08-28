import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const TARGET_DIR = path.resolve('./src/content/daily');

const DRAMA_ITEMS = {
  '2026-08-28': [
    {
      category: 'AI 漫剧',
      title: '字节跳动发布 Seedance 2.5 与即梦 AI 漫剧工作台：突破单次 30 秒长镜头与多模态参考',
      note: '即梦 AI 深度集成 Seedance 2.5 视频大模型，单次生成时长扩展至 30 秒连贯镜头，支持多图参考与动作白模锁定，彻底打破传统漫剧镜头断层感。',
      url: 'https://jimeng.jianying.com',
      source: 'jimeng.jianying.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '长镜头连贯生成与多模态参考能力的突破，标志着 AI 漫剧真正具备了工业化承接长篇故事连载的叙事能力。',
    },
    {
      category: 'AI 漫剧',
      title: '快手可灵 AI (Kling) 升级：1080P 电影级 3D 时空物理模拟与原生运动笔刷',
      note: '采用 3D 时空联合注意力机制，支持通过运动笔刷精确指定画面局部运动轨迹，大幅动作防崩坏，被头部漫剧创作者广泛采用。',
      url: 'https://klingai.com',
      source: 'klingai.com',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '可控运镜与物理模拟精度的提升，让普通编剧也能以极低成本制作出符合电影级视听语言的动态分镜。',
    },
    {
      category: 'AI 漫剧',
      title: '生数科技 Vidu 原生多主体一致性解析：AI 漫剧多角色同框对话与复杂运镜新突破',
      note: 'Vidu 视频大模型在多主体一致性上取得重大进展，支持同一镜头内多角色稳定互动、眼神交流与视角转换，极大降低了影视漫剧的分镜制作门槛。',
      url: 'https://www.vidu.studio',
      source: 'vidu.studio',
      media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '多主体交互与镜头一致性的解决，让单人团队制作长篇多人物漫剧从理论走向规模化量产。',
    },
    {
      category: 'AI 漫剧',
      title: 'Runway Gen-3 视频生成研究：电影级摄影机运镜与光影控制深度拆解',
      note: '探索从自然语言提示词精确映射到推拉摇移、希区柯克变焦等专业电影视听语言，让单人创作者第一次拥有掌控影视级分镜画面的导筒。',
      url: 'https://runwayml.com/research',
      source: 'runwayml.com',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80" rel="noreferrer',
      pinned: false,
      so_what: '视听语言的工业化控制，正在让单人创作者拥有掌控完整电影分镜的生产力。',
    },
    {
      category: 'AI 漫剧',
      title: 'ElevenLabs 官方声音设计指南：角色情感声线合成与戏剧对白拟真',
      note: '探索如何利用音素微调与标点停顿控制合成语音中的呼吸起伏、嘲讽与迟疑，使 AI 漫剧配音跨越机械感，达到院线级戏剧表现力。',
      url: 'https://elevenlabs.io',
      source: 'elevenlabs.io',
      media: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '声音是传递戏剧潜台词的灵魂，高拟真度的语音合成彻底解决了漫剧制作的配音瓶颈。',
    },
    {
      category: 'AI 漫剧',
      title: 'Suno AI 音乐生成与声场设计：漫剧电影级背景原声带（OST）制作指南',
      note: '输入歌词、风格标签与情绪节拍，30 秒内生成包含完整配器与动态起伏的主题音乐，极大丰富了 AI 漫剧的视听叙事维度与情绪张力。',
      url: 'https://suno.com',
      source: 'suno.com',
      media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '主题旋律能快速烘托漫剧场景氛围，让视听叙事的感染力倍增。',
    },
  ],
  '2026-08-27': [
    {
      category: 'AI 漫剧',
      title: 'MiniMax 海螺 AI 视频模型升级：电影级高动态大幅度运镜与镜头张力',
      note: '海螺 AI 全新升级视频生成算法，攻克大动作画面崩塌难题，在人物武打、跑酷与强视角透视镜头中展现极高的物理稳定性。',
      url: 'https://www.minimax.io',
      source: 'minimax.io',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '大幅度肢体动作与复杂运镜的稳定，让动作类漫剧的分镜制作不再受制于抽卡概率。',
    },
    {
      category: 'AI 漫剧',
      title: 'Luma Dream Machine 影视生成：现实物理光影与长镜头摄影机控制',
      note: '深入探索 Dream Machine 的高保真物理世界模拟与直接运镜指令，生成包含真实环境反射、景深虚化与体积光的电影分镜画面。',
      url: 'https://lumalabs.ai/dream-machine',
      source: 'lumalabs.ai',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '真实光影与物理交互让漫剧视觉质感直接比肩院线动画电影。',
    },
    {
      category: 'AI 漫剧',
      title: '智谱 CogVideoX-5B 开源视频生成：支持本地离线部署与长视频生成',
      note: '智谱清言开源 50 亿参数视频大模型，支持通过 3D 因果变分自编码器（3D VAE）在消费级显卡上高效运行，成为个人创作者本地化漫剧生成的新标杆。',
      url: 'https://huggingface.co/THUDM/CogVideoX-5b',
      source: 'huggingface.co',
      media: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '开源可本地部署的视频模型降低了算力依赖，保障了创作者私有 IP 与剧本资产的安全。',
    },
    {
      category: 'AI 漫剧',
      title: 'Hedra Character 角色面部与口型驱动：实现影视级情感对话与眼神追光',
      note: '通过音频驱动人物面部微表情、头部晃动与精准口型同步，大幅减少后期修音与贴嘴型的人工工时。',
      url: 'https://www.hedra.com',
      source: 'hedra.com',
      media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '口型与微表情的自动化同步，让漫剧对话场景的制作效率提升数倍。',
    },
    {
      category: 'AI 漫剧',
      title: 'Udio 音乐生成演进：支持分轨控制与电影级配乐氛围铺底',
      note: '支持精准调整打击乐、弦乐与环境音效的分轨层次，让创作者能够像专业调音师一样为漫剧定制戏剧转折点的重音与悬疑铺垫。',
      url: 'https://www.udio.com',
      source: 'udio.com',
      media: 'https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '分轨级配乐控制让情绪渲染更加细腻精准，强化了剧情反转时的视听冲击力。',
    },
  ],
  '2026-08-26': [
    {
      category: 'AI 漫剧',
      title: 'Pika 2.0 场景融合与物理特效：为 AI 漫剧注入逼真的爆炸、融化与微观镜头',
      note: 'Pika 引入全新物理特效引擎，支持一键在画面中添加符合流体力学与重力规则的破碎、燃烧与变形动态，赋予漫剧奇幻特效。',
      url: 'https://pika.art',
      source: 'pika.art',
      media: 'https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '物理特效的轻量化生成，让单人也能在漫剧中制作出好莱坞级的魔法与战斗场面。',
    },
    {
      category: 'AI 漫剧',
      title: 'PixVerse 4K 电影质感：支持多机位切换与景深变焦控制',
      note: '支持生成超高清 4K 视频并提供导演级景深控制器（Depth of Field），使前景角色对焦与背景虚化过渡极其自然。',
      url: 'https://pixverse.ai',
      source: 'pixverse.ai',
      media: 'https://images.unsplash.com/photo-1536240478700-b869070f9279?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '景深变焦的加入增强了镜头的电影感，引导观众注意力聚焦于核心角色的微表情。',
    },
    {
      category: 'AI 漫剧',
      title: 'LivePortrait 角色肖像动态化：单张插画直接驱动精准面部微表情与眨眼',
      note: '快手开源肖像动画生成框架，只需一张二次元角色立绘和一段参考驱动视频，即可毫秒级生成逼真流畅的眨眼、微笑与转头动态。',
      url: 'https://github.com/KwaiVGI/LivePortrait',
      source: 'github.com',
      media: 'https://images.unsplash.com/photo-1581291518633-83b4ebd1d83e?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '单图驱动技术的成熟，大幅降低了 2D 漫剧角色立绘转动态视频的生产门槛。',
    },
    {
      category: 'AI 漫剧',
      title: 'F5-TTS 开源零样本语音克隆：端侧运行的高保真中英双语角色配音',
      note: '基于流匹配（Flow Matching）架构的高效语音合成系统，仅需 5 秒参考音频即可克隆出极富戏剧感染力与方言特色的角色声音。',
      url: 'https://github.com/SWivid/F5-TTS',
      source: 'github.com',
      media: 'https://images.unsplash.com/photo-1590602847861-f357a9332bbc?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '开源本地语音克隆保障了长期连载漫剧中角色声线的绝对一致性与低成本输出。',
    },
  ],
  '2026-08-25': [
    {
      category: 'AI 漫剧',
      title: 'Fish Audio 极速声音克隆：毫秒级生成多角色广播剧与角色对白',
      note: '开源语音大模型支持极低延迟实时流式合成，支持多角色音色快速切换与情绪标签注入，已广泛应用于有声漫剧与动态故事。',
      url: 'https://fish.audio',
      source: 'fish.audio',
      media: 'https://images.unsplash.com/photo-1516962215378-7fa2e137ae93?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '多角色音色库的快速构建，让单人创作者能够轻松掌控包含数十位角色的宏大漫剧世界观。',
    },
    {
      category: 'AI 漫剧',
      title: '动态漫画工业化转型：从传统纸条漫到 AI 漫剧的全流程效能提升 10 倍',
      note: '深度拆解头部动漫工作室如何借助 AI 分镜工具、角色一致性种子与自动化台词打轴，将传统需数月的漫剧制作周期压缩至数天。',
      url: 'https://jimeng.jianying.com',
      source: 'jimeng.jianying.com',
      media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
      pinned: false,
      so_what: '制作周期的数量级缩短，让创作者能够根据粉丝反馈实现周更甚至日更连载，开启高频互动叙事新时代。',
    },
  ],
};

for (const [date, dramaList] of Object.entries(DRAMA_ITEMS)) {
  const filePath = path.join(TARGET_DIR, `${date}.md`);
  if (!fs.existsSync(filePath)) continue;

  const content = fs.readFileSync(filePath, 'utf8');
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) continue;

  const frontmatter = yaml.load(match[1]);
  const existingItems = frontmatter.items || [];

  // Filter out any duplicates if already present
  const existingUrls = new Set(existingItems.map((i) => i.url));
  const newItemsToAdd = dramaList.filter((d) => !existingUrls.has(d.url));

  // Insert drama items near the top (right after the pinned item)
  if (newItemsToAdd.length > 0) {
    const pinnedIdx = existingItems.findIndex((i) => i.pinned);
    const insertPos = pinnedIdx >= 0 ? pinnedIdx + 1 : 0;
    existingItems.splice(insertPos, 0, ...newItemsToAdd);
  }

  frontmatter.items = existingItems;

  const newContent = `---
${yaml.dump(frontmatter, { lineWidth: -1 })}---

主理人编者按：今天精选的这 ${existingItems.length} 篇高密度全品类一手内容，覆盖了 AI 资讯、一人公司、产品设计、审美提升、AI 漫剧、AI 协作与产品营销，希望能为你带来最扎实的认知启发与实战工具。
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`✅ Injected ${newItemsToAdd.length} AI 漫剧 items into ${date}.md (Total items: ${existingItems.length})`);
}
