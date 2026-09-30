import fs from 'fs';
import path from 'path';

const date = '2026-09-30';
const filePath = path.resolve(`src/content/daily/${date}.md`);
const usedUrlsPath = path.resolve('scripts/all-used-urls.json');

const items = [
  // 1. AI 资讯 (4 items)
  {
    category: 'AI 资讯',
    title: 'OpenAI：DevDay 2026 正式开幕，模型代理全面进驻深度工作间',
    note: '最新开发者大会现场实况：新一代轻量模型、常驻系统级代理与跨平台插件扩展同时登场，ChatGPT 正式从单一聊天窗口进化为深嵌工作系统的全自主协作环境。',
    so_what: '单点 AI 对话框的时代已进入尾声；未来的竞争关键在于能否将智能体无缝植入真实工作间，使其拥有连续上下文与跨工具自主执行权。',
    source: 'openai.com',
    url: 'https://openai.com/index/devday-2026-recap',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: 'AI 资讯',
    title: 'LMSYS Arena 深度裁决：模型裁判对自身生成的答案存在明显自恋偏好',
    note: '在 12 个前沿大模型裁决的 3.4 万次对战数据中，AI 裁判与人类真实投票的一致率仅为 56.9%，且几乎所有模型都在暗中偏袒自身或同源家族的代码与文风。',
    so_what: '不要迷信“用模型评测模型”的廉价方案；自动化基准测试若缺乏高标准人类专家的监督闭环，极易陷入模型自圆其说的认知盲区。',
    source: 'x.com',
    url: 'https://x.com/arena/status/2104965778613452895',
    media: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: 'AI 资讯',
    title: 'NVIDIA 携手 Kumo：发布 Kumo Tabular，单次推理穿透复杂表格决策',
    note: '开源专为企业结构化关系数据定制的模型架构，无需繁琐的特征工程与手工清洗，即可在一轮前向推理中完成多表连接分析与高精度数值预测。',
    so_what: '大模型解决通用知识，专用架构攻坚业务腹地；攻克非结构化文本之后，结构化企业核心数据的推理落地正在开启万亿级商业机会。',
    source: 'huggingface.co',
    url: 'https://huggingface.co/blog/nvidia/kumo-tabular',
    media: 'https://images.unsplash.com/photo-1504868584819-f8e8b4b6d7e3?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: 'AI 资讯',
    title: '重资产投资倒逼商业化：AI 行业需在 2031 年前实现 6 万亿美元年收入支撑基建',
    note: '最新行业宏观报告透视全球数据中心扩张狂潮：当前全球 GPU 与电力算力资本开支呈指数级爆发，唯有端到端商业化飞轮高速转动才能承受重资产折旧周期。',
    so_what: '算力军备竞赛已无退路，纯技术叙事的估值泡沫正被加速挤出；无论是巨头还是创业者，最终都必须回到扎实的现金流与客户 ROI 上。',
    source: 'thenationalnews.com',
    url: 'https://thenationalnews.com/future/technology/2026/09/29/ai-industry-needs-to-earn-6-trillion-by-2031-to-justify-data-centres/',
    media: 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 2. AI 协作 (4 items)
  {
    category: 'AI 协作',
    title: 'Shopify 绝密工程披露：利用 AI 协作管线在 12 周内全盘重写原生移动应用',
    note: '工程团队详尽拆解如何借助大型语言模型和自动化测试闭环，以极精简的人力架构将数百万行庞大且老旧的移动端基础设施彻底推倒重构。',
    so_what: 'AI 协作不仅能补全代码，更能重塑重构节奏；敢于利用智能体做系统级大工程的团队，其迭代效率将彻底拉开与传统开发流程的差距。',
    source: 'newsletter.pragmaticengineer.com',
    url: 'https://newsletter.pragmaticengineer.com/p/shopify-native-mobile',
    media: 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: 'AI 协作',
    title: 'Cursor：在对话界面直接实时生成交互式图表与架构思维导图',
    note: '新版编辑器将纯文本代码生成的边界进一步扩展：在侧边栏对话中即可将复杂的架构逻辑、数据流动与状态机直接渲染为可视化拓扑视图。',
    so_what: '视觉理解是降低认知负荷的最佳武器；架构思维的可视化反馈，让开发者在处理大型代码库时能够瞬间抓住全局意图。',
    source: 'cursor.com',
    url: 'https://cursor.com/',
    media: 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: 'AI 协作',
    title: 'dbx：以编辑器选区作为绝对边界的开源精简 AI 上下文引擎',
    note: '彻底摒弃漫无边际的全仓库文件投喂模式，严格将当前选中的代码块与精确定位的符号表作为提示词边界，显著减少模型幻觉并提升单次响应准确率。',
    so_what: '上下文不是越多越好，精准与克制才是解题核心；给智能体设定明确的执行边界，才能产出高度可靠的工程交付。',
    source: 'github.com',
    url: 'https://github.com/t8y2/dbx',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: 'AI 协作',
    title: 'Emil Kowalski：将访谈散记做成会主动追问逻辑漏洞的智能判断工具',
    note: '知名交互工程师演示全新用户调研工作流：输入碎片化的访谈笔记后，Agent 不仅能自动提炼需求，还会像产品老兵一样反向质询论点中缺乏数据支撑的弱项。',
    so_what: '优秀的 AI 协作伙伴不应只做谄媚的答题机器人，更要做敢于挑刺的思考陪练，逼迫你在早期就堵上产品逻辑的破绽。',
    source: 'x.com',
    url: 'https://x.com/emilkowalski/status/2105006505284235662',
    media: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 3. 一人公司 (4 items)
  {
    category: '一人公司',
    title: 'Tiny Fishing：网页小游戏利用离线金币构建极具黏性的用户回访正循环',
    note: '极简钓鱼小游戏自动记录离线进度，隔天重访即可一键领取丰厚金币，再引导玩家投入更深海域的鱼线与鱼钩，单靠纯网页端实现了惊人的自然留存与广告转化。',
    so_what: '小微产品无需复杂的系统功能；抓住一个极具确定性的人性正反馈闭环，单兵作战也能跑出高额且稳定的长尾收益。',
    source: 'tinyfishing.app',
    url: 'https://tinyfishing.app/',
    media: 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '一人公司',
    title: 'Danny Postma：多产品矩阵交叉互通是单兵团队抵抗巨头碾压的剩余护城河',
    note: '多款独立出海产品操盘手深度复盘：单点爆款生命周期极易被大厂模仿终结，只有将多个细分工具串联成互为流量与信任背书的资产矩阵，才能稳固立足。',
    so_what: '不要在一棵树上吊死，也不要分散孤立打法；用小产品打头阵，用多产品矩阵接住沉淀下来的真实用户关系，才是独立开发的终局。',
    source: 'x.com',
    url: 'https://x.com/dannypostma/status/2104786807594610778',
    media: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '一人公司',
    title: '微型设计套件启示录：靠 7.9 万高黏性订阅用户实现极高利润率的商业闭环',
    note: '专注微小痛点的系列设计插件团队公开财务切片：不盲目追求外部融资与团队扩张，仅凭精益代码库与高度聚焦的社群口碑，做出了超 80% 的净利表现。',
    so_what: '做产品不是做规模竞赛，而是做利润质量；把一小群人的痛点解决到极致，一人公司也能拥有无惧周期的生存韧性。',
    source: 'x.com',
    url: 'https://x.com/agazdecki/status/2104990758373835109',
    media: 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: '一人公司',
    title: 'Cloudflare 发布 EmDash 1.0：利用分布式插件注册表彻底重构边缘 CMS',
    note: '官方推出新一代无服务器内容管理系统架构，将轻量数据库、边缘计算与安全沙箱插件深度融合，让独立开发者几分钟内即可搭建起全球极速分发的内容站点。',
    so_what: '现代边缘基建已将全栈部署门槛降至冰点；选择与边缘计算紧密协同的现代技术栈，独立开发者可以把绝大部分精力放回业务与内容本身。',
    source: 'blog.cloudflare.com',
    url: 'https://blog.cloudflare.com/emdash-cms-plugin-registry/',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 4. 产品设计 (4 items)
  {
    category: '产品设计',
    title: 'Paper.design：为数字化纸张滤镜细腻还原真实折痕、纤维与光影皱褶',
    note: '创意设计工具重构拟物化交互表达：不再使用粗暴的静态贴图，而是通过动态物理着色器将纸张纤维的受光角度与受压折痕精确还原，带来温润的触觉质感。',
    so_what: '在千篇一律的扁平化界面审美疲劳之后，对物理材质细节的极致打磨正在成为产品脱颖而出、建立情感连接的高级手段。',
    source: 'paper.design',
    url: 'https://paper.design/',
    media: 'https://images.unsplash.com/photo-1586075010923-2dd4570fb338?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '产品设计',
    title: 'Supertake：将碎片化投资灵感与推演逻辑重塑为可追踪的结构化实体',
    note: '投资分析工具彻底重构笔记产品形态：把原本散落在对话记录与随手记里的看盘假设，直接封装为带时效、具备关联标的与校验指标的可操作交互卡片。',
    so_what: '设计的本质是厘清信息关系；当界面能够将抽象的认知过程结构化，用户就能从混沌的信息茧房中获得掌控感。',
    source: 'supertake.com',
    url: 'https://supertake.com/',
    media: 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '产品设计',
    title: '少数派评测：Apple Watch 12 如何将零碎健康提醒织成无感的连续反馈网',
    note: '深度交互体验剖析：不再采用生硬弹窗惊扰用户，而是借助传感器融合与动态微振动，在睡眠、心率突变与压力阈值之间建立渐进式、不具压迫感的健康闭环。',
    so_what: '最高级的设计是“感知不到它的存在却已被它守护”；减少打扰频率，提升反馈精准度，是软硬件协同体验的核心准则。',
    source: 'sspai.com',
    url: 'https://sspai.com/post/115061',
    media: 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: '产品设计',
    title: 'HeyPCB：将多人实时协作光标与版本推演引入精密电路设计画布',
    note: '硬件 CAD 工具迎来 Figma 时刻：电子工程师与结构设计师可以在同一块高精度电路板原理图上实时查看彼此的光标轨迹、走线冲突提示与电气规则检验。',
    so_what: '实时协作的范式正在从通用文档向垂直硬核工业领域强力渗透；打破传统本地单机工具的孤岛，是所有专业软件重生的必由之路。',
    source: 'heypcb.ai',
    url: 'https://heypcb.ai/multiplayer',
    media: 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 5. 审美提升 (4 items)
  {
    category: '审美提升',
    title: 'LANG 旗舰店：将香港历史建筑的市井碎片巧妙嵌进洛杉矶旧工业仓库',
    note: '著名建筑事务所操刀空间实验：不采用粗暴的仿古复制，而是提取霓虹招牌、马赛克地砖与老旧铁网等文化碎片，在粗犷的工业水泥骨架中激荡出跨洋的记忆张力。',
    so_what: '审美的力量来自文明记忆的解构与重组；拒绝流于表面的符号拼接，用空间叙事建立文化坐标，才能让实体空间拥有直抵人心的灵魂。',
    source: 'designboom.com',
    url: 'https://www.designboom.com/architecture/lang-los-angeles-flagship-fragments-hong-kong-former-warehouse-studio-paul-chan/',
    media: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '审美提升',
    title: 'Displaay 发布 Cassette：以三种字宽轴精准致敬模拟时代的磁带工业美学',
    note: '独立字体工作室带来全新可变字体作品：通过比例、半等宽与等宽三种骨架系统，将磁带外壳上的机械刻度与墨陷特征化入现代排版网格，兼具机械感与可读性。',
    so_what: '优秀的字体设计从历史媒介中汲取秩序；在数字屏幕上复活模拟时代的温度与工业骨架，是视觉高级感的绝佳来源。',
    source: 'displaay.net',
    url: 'https://displaay.net/typeface/cassette',
    media: 'https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '审美提升',
    title: 'Es Devlin：用两千本实体旧书打造直径八米的震撼可旋转巨型图书馆',
    note: '伦敦设计博物馆重量级特展：舞台设计大师将两千本承载不同年代阅读痕迹的古籍置入可旋转机械球体，让观众在环形视线交错中感受人类知识与时间流转的宏大诗意。',
    so_what: '物体本身的岁月痕迹就是最顶级的材料；将时间的重量与机械动势结合，能够创造出纯粹文字无法企及的震撼场域。',
    source: 'designboom.com',
    url: 'https://www.designboom.com/design/es-devlin-rotating-library-2000-books-london-design-museum-other-worlds/',
    media: 'https://images.unsplash.com/photo-1507842229451-7f01be7ac128?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: '审美提升',
    title: 'Dior 2027 巴黎大秀：以极简白色几何跑道切开朦胧水雾的自然园林景观',
    note: 'Bureau Betak 精心编排的时装舞台：保留花园中天然的水面、垂柳与升腾水雾作为舞台背景，纯净的硬边白色跑道如一道几何光线穿透自然，构筑出极强的超现实对立。',
    so_what: '最高级的前卫不是掩盖自然，而是以极致克制的现代几何介入自然，在冲突中形成震撼的呼吸感。',
    source: 'designboom.com',
    url: 'https://www.designboom.com/design/bureau-betak-geometric-white-runway-mist-filled-landscape-dior-summer-2027-show-paris-fashion-week-jonathan-anderson/',
    media: 'https://images.unsplash.com/photo-1509631179647-0177331693ae?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 6. 产品营销 (4 items)
  {
    category: '产品营销',
    title: 'a16z Speedrun：以 25 万美元启动金与云算力额度定制年轻黑客冷启动入口',
    note: '顶级风投将投资协议、算力配额与严苛截止日打包成确定性产品化方案，极大降低学生极客与年轻工程师迈入创业赛道的门槛，实现早期案源批量捕获。',
    so_what: '营销的最高境界是将招募机制做成透明的产品；用清晰的承诺与确定性赋能消除早期犹豫，才能在激烈的生源竞争中锁定最敏锐的头脑。',
    source: 'a16z.com',
    url: 'https://a16z.com/speedrun/',
    media: 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '产品营销',
    title: 'Lenny Rachitsky：将一次性线下峰会完整拆解为持续长尾分发的全量知识库',
    note: '知名商业主播示范高密度内容复用范本：把 Lenny & Friends 峰会的主舞台对话与实战干货，按主题、人群痛点切片并配齐讲义上线，让现场体验转化为持久的获客磁石。',
    so_what: '不要做一次性消耗的营销活动；把每一场活动都当成可复用的数字资产来打造，才能让前期的每一份投入都在时间复利中持续回报。',
    source: 'lennysnewsletter.com',
    url: 'https://www.lennysnewsletter.com/p/all-of-the-lenny-and-friends-summit',
    media: 'https://images.unsplash.com/photo-1515187029135-18ee286d815b?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '产品营销',
    title: 'Tibo：用 200 位真实创始人的闭门互助现场直接向外界展示高浓度社群价值',
    note: '独立造物主摒弃空洞的社群宣传口号，直接将创始人互相推演商业模式、引荐渠道资源与避免翻车的实战过程做成公开案例，极具说服力地兑现了入会价值。',
    so_what: '最好的文案不是吹嘘氛围有多好，而是展示用户在里面拿到了什么具体结果；透明与真实是高溢价社群的最强说服力。',
    source: 'x.com',
    url: 'https://x.com/tibo_maker/status/2104917020416336115',
    media: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: '产品营销',
    title: 'Caffè Fortuna：将百年阿尔法·罗密欧的四叶草传奇重构为沉浸式咖啡空间',
    note: '台北全新品牌联名空间落成：暗绿釉面瓷砖、温润深木饰面与赛车速度线完美契合，未摆放任何夸张广告牌，却让每一位进店者自然浸润在百年意式速度美学之中。',
    so_what: '品牌跨界不是贴牌卖货，而是生活方式的情感迁移；将经典的文化图腾自然融入日常消费场景，往往能激发出意料之外的品牌认同。',
    source: 'designboom.com',
    url: 'https://www.designboom.com/design/dark-wood-deep-green-alfa-romeo-iconic-design-caffe-fortuna-taipei-rlww-studio/',
    media: 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 7. AI 漫剧 (4 items)
  {
    category: 'AI 漫剧',
    title: '云雀工坊（Lark Studio）：将字幕、翻译、配音与合成管线完全收拢在本地',
    note: '高星开源漫剧工作站重磅升级：支持单机调用本地模型完成多语种字幕时间轴切分、角色音色克隆与画面自动对齐，彻底斩断对云端第三方收费接口的依赖。',
    so_what: '内容创作者最大的资产是私域数据与稳定流转的管线；将关键音画合成留在本地，既守住了资产安全，又极大地压低了规模化试错成本。',
    source: 'github.com',
    url: 'https://github.com/ixugo/lark-studio',
    media: 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: 'AI 漫剧',
    title: '双屏设备铰链交互与微动漫画叙事：从硬件角度探寻漫画翻页的体感革新',
    note: '交互设计师针对双屏折叠设备的新一代动态漫剧开发指南：通过获取精确到 5 度的铰链旋转角度 API，实现类似真实手翻书的立体透视变化与剧情分镜悬念展开。',
    so_what: '形式与内容向来相辅相成；当硬件物理形态发生进化，敏锐的漫剧创作者应当第一时间借由硬件新特性设计出前所未有的沉浸阅读体感。',
    source: 'youtube.com',
    url: 'https://www.youtube.com/watch?v=y227RF0smAg',
    media: 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: 'AI 漫剧',
    title: '秦兆阳文学编辑手记：现实主义叙事力量如何为通俗漫画注入坚实精神骨架',
    note: '文艺编剧网深度刊载名家手记：解析文学编辑如何帮助创作者在荒诞或类型化题材中扎下生活的根须，避免短剧与漫剧走向轻浮空洞的套路重复。',
    so_what: '视觉技术能制造瞬间的多巴胺，但唯有真实的现实主义情感内核才能让观众产生深层共鸣；AI 漫剧在堆砌画质之外，最缺的正是这种文学厚度。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/945',
    media: 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: 'AI 漫剧',
    title: 'OpenAI 发布 GPT Image 2.5：精准攻克多人物主体与分镜光影一致性短板',
    note: '全新视觉生成架构实现重大突破：在保持动漫角色面部五官高度一致的前提下，支持在复杂场景切换中保持空间主光源、阴影投射与服饰纹理的连续统一。',
    so_what: '一致性难题一旦被底层模型攻破，AI 漫剧的产能将迎来十倍级爆发；创作者的重心将从“如何抽卡调教画面”全面转向“如何讲好一个抓人的故事”。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6462019.html',
    media: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 8. 编剧技巧 (4 items)
  {
    category: '编剧技巧',
    title: '万众编剧网：“戏剧小说”全球华语征集启事与跨媒介戏剧化改编指南',
    note: '权威编剧平台发布重磅征集细则：重点扶持具备强动作性、明确人物困境与高冲突因果关系的原创小说，为影视、舞台剧及网络漫剧打通源头文本孵化通道。',
    so_what: '跨媒介改编的核心在于“戏剧动作”的提炼；写作者如果能在小说阶段就预设舞台或银幕的视听张力，就能在 IP 产业链条中抢占最高溢价。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/921',
    media: 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '编剧技巧',
    title: '关于“比稿”乱象与行业生态：编剧如何在非标竞争中守住知识产权与创意边界',
    note: '资深制片人与编剧深度对谈：剖析项目前期无序比稿、创意盗用与非标立项的行业痼疾，系统梳理了故事梗概保护、立项备案协议与阶段交付确权的标准范本。',
    so_what: '好点子不值钱，受法律保护且可落地的文学资产才值钱；创作者必须建立完备的自我保护防线，避免在早期沟通中无偿透支核心资产。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/922',
    media: 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '编剧技巧',
    title: '剧本为骨，温情为魂：解码爆款音乐剧《0528》长红出圈的情感弧光构建',
    note: '舞台剧创作复盘精粹：分析创作者如何将琐碎的生活困境升华为跌宕起伏的母题冲撞，在 90 分钟内通过七次情节递进精准击中当代都市观众的情绪防线。',
    so_what: '长红作品的秘密从来不是刻意煽情，而是严格遵从因果规律的戏剧骨架；先把人物的欲望与阻碍立牢，情感的爆发才能水到渠成。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/924',
    media: 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: '编剧技巧',
    title: '《微短剧发展管理办法》正式落地：行业告别野蛮生长，合规与精品化审读要点',
    note: '行业主管部门新规细则解读：对题材立项、价值导向与内容分级做出更严谨的规范指引，依靠低俗反转与劣质爽点博眼球的短剧模式正被加速淘汰出局。',
    so_what: '监管的收紧是优质创作者的红利；当粗制滥造的流量投机者退场，深耕人物成长、拥有扎实戏剧结构的正规军将迎来真正的黄金期。',
    source: 'wzbj1616.com',
    url: 'https://www.wzbj1616.com/script_necessary_info/933',
    media: 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },

  // 9. 产品经理 (4 items)
  {
    category: '产品经理',
    title: '中年人的 100 种花式创业与亏钱陷阱：穿透伪需求，重识商业世界的基本常识',
    note: '人人都是产品经理深度万字长文：复盘数十位资深大厂骨干离职创业的真实惨痛案例，剖析把“自我感动式需求”误判为“真实市场痛点”的典型思维误区。',
    so_what: '任何不以真实付费转化为前提的产品构想，都是致命的幻觉；产品经理最大的自律，是克制住做复杂功能的冲动，直面冰冷的交易本质。',
    source: 'woshipm.com',
    url: 'https://www.woshipm.com/pmd/6460700.html',
    media: 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '产品经理',
    title: 'Arvid Kahl：先稳住业务核心数据与确定性 API，再迎接智能体接入浪潮',
    note: '资深创业导师警示产品负责人：不要盲目在产品外层包裹华而不实的 AI 聊天气泡，而应先清洗并开放最干净的数据接口，为机器世界的程序化调用铺好路。',
    so_what: '未来的主流产品使用者很可能不再是人类眼球，而是自动化 Agent；把底层的 API 设计得确定、健壮且优雅，才是面向未来的产品架构。',
    source: 'x.com',
    url: 'https://x.com/arvidkahl/status/2104972253620580767',
    media: 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
    pinned: true
  },
  {
    category: '产品经理',
    title: 'Yongfook：破除单产品执念，独立操盘手如何靠多产品组合抵御市场黑天鹅',
    note: 'Bannerbear 创始人复盘十年创业经验：单款 SaaS 随时可能面临平台政策调整或巨头抄袭风险，用轻量代码构建互不干扰的独立产品组合，能大幅增强抗风险能力。',
    so_what: '不要做脆弱的单点赌徒；把可复用的营销、支付与用户资产抽象出来，让多产品成为抗击周期波动的分布式安全气囊。',
    source: 'x.com',
    url: 'https://x.com/yongfook/status/2104740383708397920',
    media: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
    pinned: false
  },
  {
    category: '产品经理',
    title: 'HumanBench：用微小真实边界题暴露大模型的典型认知盲区与设计反思',
    note: '全新开源评估基准上线：通过大量看似简单却暗藏陷阱的人类日常常识题，直观揭示出大模型在因果推理与空间想象上的脆弱性，为 AI 产品设计提供警示。',
    so_what: '了解工具的上限很重要，看清工具的下限更关键；设计 AI 产品时永远要为模型的“反常识崩溃”预留人工兜底机制。',
    source: 'humanbench.ybuild.ai',
    url: 'https://humanbench.ybuild.ai/',
    media: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=800&auto=format&fit=crop&q=80',
    pinned: false
  }
];

const frontmatter = `---
date: '${date}'
title: 9 月 30 日 · 代理进驻工作间与多模态叙事：在重资产竞赛中构筑个人护城河
highlights: 全网 9 大领域 36 篇高密度精选：OpenAI DevDay 将常驻代理推入工作间、Shopify 用 AI 在 12 周内重构原生应用、Lenny 拆解峰会可沉淀内容库、云雀工坊本地化音画合成管线、微短剧管理新规落地与戏剧小说叙事规范。
draft: false
epigraph: 模型的能力越是下沉到操作系统与日常工作流，靠单点信息差维系的工具就越脆弱；当 AI 成为人人可调用的默认底座，决定产品胜负与个人护城河的，从来不是多快跑完一个 Demo，而是能否沉淀出不可被替代的资产闭环与情感共鸣。
lead: 9 月底的科技与商业演进，正清晰地指向两个相辅相成的分水岭：在技术底座与工程协作端，OpenAI DevDay 全面将常驻代理与工作空间深度绑定，Shopify 凭 AI 工具链在短短 12 周内完成原生移动端重构，NVIDIA 与 Kumo Tabular 攻坚复杂工业表格推理，而数据中心 6 万亿美元的营收预期也在倒逼整个行业从算力狂热转向严肃的 ROI 审视；在小微产品与内容生产一线，单兵创业者正在打破“只守一个产品”的执念，转向通过跨端资产与私域社群构筑护城河，云雀工坊将漫剧音视频合成管线完全收拢至本地，而编剧行业新规的施行与戏剧小说征集，则再度验证了无论工具如何迭代，扎实的戏剧因果与人物弧光永远是内容破圈的压舱石。无论你在写代码、做产品还是讲故事，唯有看清底层意图并敢于沉淀确定性资产，才能在激荡的变局中稳步前行。
scene: 「你们还在为每个小需求专门写 Agent 吗？」「早就过了那个阶段了。现在我们直接把常驻代理收进工作间管线，代码和音画合成全走本地与确定性沙箱，核心资产握在手里，跑得比谁都踏实。」
cover: https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80
items:
${items.map(it => `  - category: ${it.category}
    title: ${it.title}
    note: ${it.note}
    so_what: ${it.so_what}
    source: ${it.source}
    url: ${it.url}
    media: ${it.media}
    pinned: ${it.pinned}`).join('\n')}
---

## 今日主理人寄语

今天是 9 月的最后一天。回看整整一个月的技术演进与行业洗牌，有一个趋势已经清晰得不容置疑：

**AI 正在从“聊天窗口里的玩具”，加速蜕变为“常驻在工作系统深处的生产力引擎”。**

OpenAI DevDay 展现的代理工作间、Shopify 在 12 周内用 AI 完成全盘重构的工程奇迹，都在证明一件事：那些还在惊叹于模型写出几句漂亮文案的人，正在被那些把 AI 接入生产管线、直接交付系统结果的实干家迅速拉开距离。

然而，工具的狂飙也带来了空前的资产焦虑。随着数据中心数万亿美元的巨额资本开支逼近商业化大考，单靠“概念炒作”和“功能套壳”的产品将以最快速度被挤出牌桌。

在这样激荡的大变局下，小团队和单兵造物主真正的破局点在哪里？

**第一，做减法，守住底线。** 像 dbx 那样把选区作为严格边界，像云雀工坊那样把合成管线收拢在本地，不要什么都交给云端黑盒，确定性与私域控制权才是安全感的来源。

**第二，做组合，打破孤岛。** 听一听 Danny Postma 和 Yongfook 的操盘经验，别把全部身家赌在一个孤立的爆款上，打造多产品协同的互助矩阵，让流量和信任相互滋养。

**第三，做深耕，重塑骨架。** 无论是做产品还是写故事，去看看音乐剧《0528》的情感弧光，去研究微短剧新规对因果逻辑的严苛要求。多巴胺来得快去得也快，只有扎根于人类真实困境与情感共鸣的作品，才能穿越周期的狂风暴雨。

金秋十月即将启幕。愿这 36 篇精心雕琢的资讯，能陪你在纷繁的噪音中理清头绪，积攒力量，坚定地筑牢属于你自己的护城河。
`;

fs.writeFileSync(filePath, frontmatter, 'utf8');
console.log(`Successfully written: ${filePath}`);

// Update all-used-urls.json
const allUsed = JSON.parse(fs.readFileSync(usedUrlsPath, 'utf8'));
const usedSet = new Set(allUsed);
let added = 0;
for (const it of items) {
  if (!usedSet.has(it.url)) {
    allUsed.push(it.url);
    usedSet.add(it.url);
    added++;
  }
}
fs.writeFileSync(usedUrlsPath, JSON.stringify(allUsed, null, 2), 'utf8');
console.log(`Updated all-used-urls.json: added ${added} new URLs, total count: ${allUsed.length}`);
