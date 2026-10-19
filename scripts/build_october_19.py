# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-19': {
        'title': '10 月 19 日 · 可撤销防线与确定性交付：当智能体开始在真实系统里“留后路”',
        'highlights': '全网 9 大领域 36 篇高密度精选：DeepSeek 开放独立搜索与网页读取、Sphinx 在 Git 推送前强制代码理解审计、Shipback 为 Agent 部署保留最后撤回、ComfyUI GGUF 与 stable-fast 算力提速、40 集国风修仙短剧全本商业交割。',
        'epigraph': '最高级的自动化系统，从来不是狂妄地假设模型永不出错，而是为每一次可能发生的失控预先修筑好可撤销的退路与物理闸门。',
        'lead': '10 月 19 日，新的一周以一种更加务实、冷静的工程定调开启：AI 智能体正在告别“一次性盲目执行”，全面进入“可撤销、可审计、确定性交付”的成熟工业期。在基础能力与模型协议端，DeepSeek 罕见地将底层的结构化搜索与 Markdown 网页抽取剥离为独立计费 API，标志着“搜索即基础设施”成为公共服务；在智能体与开发协作一线，从在代码推送前强制人机问答审计的 Sphinx，到在 Agent 上传覆盖服务器文件时自动预留撤回原件的 Shipback，再到 Browser Use 详细拆解真实世界浏览器操作的边界与容错上限，工程师们正在用一道道工程闸门锁死智能体的幻觉破坏力；在一人公司与产品设计端，从把家长一周信息重构成清晰行动指引的 The Parent Inbox，到纯端侧离线混音的 Moonrain，极致的利基痛点与离线尊严依然是独立开发者的制胜底牌；在影视视听与内容工业端，ComfyUI GGUF 量化与 stable-fast 极致编译让长篇漫剧渲染彻底跑赢时间，40 集都市国风修仙短剧《月薪三千我修仙》全本商业交割，展现了 AI 赋能下类型叙事的工业化兑现。',
        'scene': '「现在的代码生成 Agent 已经能自己写完、测试并直接部署到线上服务器了，为什么还要在最后加一步手动撤销确认？」「因为现实生产环境里没有时光机。一旦 Agent 在夜里把有潜在死锁的代码推上主干，能救命的不是它有多聪明，而是那个能一秒回滚到昨天版本的红色物理按钮。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周一，新的一周开始。

今天整理这 36 篇精选时，最让我深有感触的，是 **工程师们正在教智能体学会“留后路”**。

过去一年，行业里充斥着关于“完全全自动、人类彻底离场”的宏大叙事。
但当智能体真正被接入生产环境、开始触碰服务器真实文件、调用银行账单、操作线上数据库时，现实狠狠教育了所有人：
**不可控的概率，永远不能直接凌驾于确定性的系统之上。**

所以我们看到：
Sphinx 在你推送代码前先抛出两道考题确认你真的读懂了差异；
Shipback 在覆盖服务器原件前先默默打下一份备份留好撤回通道；
3AM 把自动化修复与人工最终审批死死锁在同一条流水线上……

这绝不是技术的倒退，而是技术走向成熟与可依赖的必经之路。

对于正在操盘产品、打造独立工具的你而言：
**不要把“完全免干预”当作核心卖点，把“确定性、可控性、随时可撤销的安全感”卖给客户，才是最坚固的商业护城河。**

祝你新的一周，在确定性中稳步前行。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-GGUF 量化加速套件：消费级显存跑通长篇漫剧大基座',
                'note': '漫剧本地化量产的算力破局方案：支持以 4-bit / 8-bit GGUF 格式加载 FLUX、Wan 与 Hunyuan 顶尖生成大模型，让单张 16G/24G 显卡流畅渲染高分辨率多镜头分镜。',
                'so_what': '击穿高昂云端算力租赁成本壁垒；让独立影视创作者与小型漫剧工作室依靠消费级工作站即可跑通千亿参数视听大模型。',
                'source': 'github.com',
                'url': 'https://github.com/city96/ComfyUI-GGUF',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'stable-fast 极端编译加速引擎：漫剧大批量批量渲染吞吐跃升',
                'note': '影视级渲染农场的速度倍增器：通过深度定制的 Torch-TensorRT 与算子融合编译，在保持画面精度绝对一致的前提下实现 2~3 倍推理速度飞跃。',
                'so_what': '在大规模连载交付中时间就是现金流；极致的吞吐加速直接缩短了漫剧项目的后期合成工期，显著降低单集渲染电费与折旧损耗。',
                'source': 'github.com',
                'url': 'https://github.com/chengzeyi/stable-fast',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI NestedNodeBuilder 节点封装套件：漫剧模块化子图解耦',
                'note': '漫剧大型工作流工程化治理利器：支持将面部增强、风格迁移与光影调色等几十个复杂节点封装为独立复用的子图模块，彻底根治节点画布杂乱失控。',
                'so_what': '复杂业务逻辑的模块化封装思维；把脆弱纠缠的生图节点整理为清晰的标准流水线，是漫剧团队跨岗位协同分工的关键底座。',
                'source': 'github.com',
                'url': 'https://github.com/ssitu/ComfyUI_NestedNodeBuilder',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《月薪三千我修仙》40集都市国风修仙短剧：AI 协同视听分镜与商业全本交割',
                'note': '传统修仙母题在微短剧赛道的商业变现样本：全 40 集紧凑体量，借助 AI 快速搭建御剑斗法与现代都市的反差分镜设定，人工深度打磨底层打工人的逆袭尊严与人情温度。',
                'so_what': '高概念玄幻在低成本制作中的破局路径；用 AI 快速消化繁复的法术特效设定，编剧专注把控底层共鸣与情绪递进，跑通全本商业交割。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1938',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《命运交织的二十二章》中式悬疑单元剧：塔罗隐喻、多重反转与叙事闭环',
                'note': '高结构化悬疑剧作的心法拆解：借由二十二张主阿尔卡那塔罗牌构建命运隐喻，每一章看似独立成篇却在暗线中草蛇灰线汇聚为终极命题，展示了多线索因果编织的硬功夫。',
                'so_what': '单元剧不是散装故事的拼盘；用强有力的哲学隐喻统摄不同人物的抉择，才能让短篇叙事在结尾产生排山倒海的震撼回响。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1918',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《操盘手之救赎》现实题材金融悬疑剧：股市博弈、人性贪婪与沉沦忏悔',
                'note': '严肃现实主义金融剧作复盘：深入资本市场的内幕交易与心理拉锯，生动刻画散户与庄家在红绿数字背后的狂热与绝望，以悲剧性结局敲响对欲望失控的警钟。',
                'so_what': '行业剧的根基是专业度与人性深度；拒绝悬浮的金融打怪升级，直面资本深渊对良知的噬咬，才能赋予商业剧本长久的社会批判力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1753',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《幽冥判官令》奇幻志怪微短剧：微短剧黄金节奏、因果反转与爽点机制',
                'note': '微短剧赛道头部爆款结构复盘：以善恶有报的东方因果律为动力引擎，在每集一分钟内密布“打压-反转-昭雪”的情绪闭环，精准满足大众受众对正义伸张的心理补偿。',
                'so_what': '短剧爽感的底层是对社会公平的渴望；把古老志怪文本转化为快节奏的情绪解压阀，是商业通俗短剧屡试不爽的核心抓手。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1934',
                'media': 'https://images.unsplash.com/photo-1507676184212-d03ab07a01bf?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '《古戒神豪：流浪汉横扫全城》都市奇幻短剧：小人物逆袭与底层同理心构建',
                'note': '经典都市逆袭题材的人物弧光拆解：虽然披着奇幻神豪的外衣，剧本前三集却极其扎实地铺垫了主角在底层饱受白眼的辛酸生活，为后续的情感爆发提供了扎实的认同支点。',
                'so_what': '神豪剧不能只写暴富的轻狂；唯有把下位者的无助与屈辱刻画得入木三分，后续的逆风翻盘才能产生真正击穿屏幕的情绪力量。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1755',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '让员工自费买 AI 的公司已经输了：组织智能化转型的基础设施与心智红利',
                'note': '组织拥抱 AI 进程中的认知陷阱剖析：将大模型工具采购视为边缘开销、逼迫员工自掏腰包的企业，不仅在数据安全上门户大开，更失去了自上而下沉淀业务自动化资产的战略窗口期。',
                'so_what': 'AI 不是员工的个人饰品，而是组织协同的新底层；产品经理与管理者需将 AI 采买上升为战略基建，用机制激发全员探索业务自动化。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6462090.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '这种需求怎么实现？否则单子就丢了：B端非标定制与产品通用底座的博弈艺术',
                'note': 'B端产品经理生死存亡的实战复盘：面对大客户突如其来的严苛非标定制诉求，如何在不破坏核心架构通用性的前提下，通过轻量扩展槽与业务适配层化险为夷保住订单。',
                'so_what': '通用化与定制化从不是非黑即白；优秀的产品经理懂得在架构中预留弹性接口，用标准化的构件组装出千人千面的非标解决方案。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/share/6473153.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'USP 之父罗瑟·瑞夫斯：24 条实效广告黄金法则在 AI 时代的产品重构',
                'note': '经典营销心法对现代 AI 商业化的降维打击：在生成式内容泛滥导致注意力极度稀缺的当下，重温“独特的销售主张（USP）”与单一购买理由，比制造千篇一律的 AI 噱头管用一百倍。',
                'so_what': '噪音时代，单一强主张胜过万语千言；产品经理在打磨价值主张时，必须用最朴实、不可复制的利益承诺瞬间击穿用户心智。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473650.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '科学广告奠基人斯坦利·里索的 28 个信条：拒绝自嗨，产品叙事如何穿透心智',
                'note': 'JWT 掌舵人的实证主义广告哲学复盘：广告与产品推广不是玄学创作，而是对消费者行为与真实痛点的严谨调研；拒绝空洞词藻堆砌，用可量化的事实说话。',
                'so_what': '叙事的力量建立在客观事实之上；产品经理要学会像科学家一样解剖用户痛点，用扎实的产品体验支撑每一次品牌承诺。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473980.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-19.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Select curated items for the 6 ian categories
curated_ian_picks = {
    'AI 资讯': [
        'https://api-docs.deepseek.com/guides/search/',
        'https://bench.killswitch-lang.org/',
        'https://www.aboutamazon.com/news/devices/amazon-personal-ai-bee-frontier-bee-eclipse',
        'https://www.lennysnewsletter.com/p/a-mind-expanding-conversation-on'
    ],
    'AI 协作': [
        'https://sphinx-six-theta.vercel.app/',
        'https://github.com/aldohushi1-stack/shipback-sftp',
        'https://browser-use.com/posts/browser-agents',
        'https://3am.si/'
    ],
    '一人公司': [
        'https://atitb.com/en/bored',
        'https://milo.baby',
        'https://apps.apple.com/us/app/moonrain-sleep-sounds/id6789770084',
        'https://nanoconsole.codeberg.page/'
    ],
    '产品设计': [
        'https://die-lines.com/',
        'https://local-host.ai/connectingCaptions/',
        'https://pastekit.dev/',
        'https://csvfile.tools/viewer'
    ],
    '审美提升': [
        'https://www.designboom.com/architecture/sardinian-school-perforated-aluminum-facade-flexible-agora-leicho-architettura/',
        'https://www.wallpaper.com/architecture/36-views-of-dawsons-heights-book-review',
        'https://www.dezeen.com/2026/10/18/karimoku-new-standard-asics-furniture-crushed-trainers/',
        'https://farsidelab.com/concept/rocket-engines/'
    ],
    '产品营销': [
        'https://helptheparents.org/',
        'https://mylens.ai/',
        'https://seths.blog/2026/10/anticipating-confusion/',
        'https://popcraft.ai/mcp'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://api-docs.deepseek.com/guides/search/': '大模型搜索与网页解析能力的公共基建化；将复杂的网页清洗与结构化提取封装为独立原子接口，大幅降低了开发者自建网络爬虫与清洗管线的运维摩擦。',
    'https://bench.killswitch-lang.org/': '对抗大模型“背题库”虚假繁荣的硬核测试；用刻意陌生的人造语言逼迫模型展现真实的逻辑推理与元学习能力，为代码模型评测树立了防过拟合标杆。',
    'https://www.aboutamazon.com/news/devices/amazon-personal-ai-bee-frontier-bee-eclipse': '环境感知硬件的轻量化演进；将随身记忆整理与物理隐私开关相结合，探索在不过度打扰用户日常心流的前提下沉淀个人全景资产。',
    'https://www.lennysnewsletter.com/p/a-mind-expanding-conversation-on': '破除拟人化意识迷雾，走向严谨的可解释性研究；从底层激活模式与几何隐空间中推演模型的推理链路，为黑盒智能体的可控性审查提供了理论抓手。',
    'https://sphinx-six-theta.vercel.app/': '重构代码审查的人机信任界面；在合入主干前倒逼人类开发者回答关于 AI 改动的深层逻辑问题，消灭“闭眼通过”带来的技术债务与安全黑天鹅。',
    'https://github.com/aldohushi1-stack/shipback-sftp': '给自动化部署装上坚不可摧的倒档；在智能体覆盖生产环境文件时先行固化可回滚副本，是保障 AI 自主运维不演变为系统灾难的底线护栏。',
    'https://browser-use.com/posts/browser-agents': 'GUI 智能体从玩具走向生产环境的实战指南；承认非确定性界面的高昂探索成本，优先降级为结构化 API 协同，为浏览器代理圈定了清醒的边界。',
    'https://3am.si/': '在事故响应自动化中架设人机双重闸口；将根因推演与人工逐级确认无缝串接，为深夜高危生产运维筑起了一道清醒的防浪堤。',
    'https://atitb.com/en/bored': '反向解构屏幕时间成瘾的锋利切角；在注意力争夺白热化的红海中反其道而行之，用物理静止作为触发条件，展示了一人公司切入数字健康的小众洞察力。',
    'https://milo.baby': '从真实生活摩擦中打捞出的刚需痛点；聚焦新手父母在睡眠剥夺下的极端场景，用极简界面消灭多人重复确认的焦虑，是母婴微型工具的典范。',
    'https://apps.apple.com/us/app/moonrain-sleep-sounds/id6789770084': '把算法与音频处理死死锁在设备端侧；零账号依赖、纯离线运行的高保真环境白噪音，精准击中了注重绝对隐私的高净值睡眠障碍人群。',
    'https://nanoconsole.codeberg.page/': '向极致硬件成本发起挑战的极客浪漫；在十五美分的微控制器上榨干最后一字节内存跑通游戏机，展示了底层工程素养降维打击的生命力。',
    'https://die-lines.com/': '把枯燥复杂的工业几何标准转化为无缝交互；在浏览器端实时重构包装刀模矢量结构，将传统印前打样数天的往复沟通压缩至数秒。',
    'https://local-host.ai/connectingCaptions/': '注重隐私与演示边界的微交互设计；在本地实时转译语音字幕的同时，通过精细的屏幕捕获隔离逻辑，避免向受众泄露后台敏感窗口。',
    'https://pastekit.dev/': '把散乱文本处理收敛进单一心流工作台；自动根据格式特征动态自适应分栏树形与对照渲染，极大减轻了开发者日常多源数据对比的认知负担。',
    'https://csvfile.tools/viewer': '对现代浏览器算力与内存吞吐的极致榨取；借助虚拟列表与端侧流式解析轻松跑通百万行大表渲染，把沉重的桌面软件轻量化搬进网页。',
    'https://www.designboom.com/architecture/sardinian-school-perforated-aluminum-facade-flexible-agora-leicho-architettura/': '材料孔洞与光影律动的呼吸感；穿孔波纹铝板不仅作为遮阳外皮，更随日光迁移在校园中庭投射出流动光晕，赋予教育空间无限灵动诗意。',
    'https://www.wallpaper.com/architecture/36-views-of-dawsons-heights-book-review': '对社区公共住宅建筑肌理的深情凝视；从三十六个离散视角定格阶梯状红砖体量在都市天际线中的起伏，重新唤醒了平凡居所的人文庄严感。',
    'https://www.dezeen.com/2026/10/18/karimoku-new-standard-asics-furniture-crushed-trainers/': '运动废弃材料与日本精密木工工艺的诗意杂交；将报废跑鞋发泡鞋底粉碎重组为家具缓冲层，为循环设计提供了兼具坐感与温度的实体答案。',
    'https://farsidelab.com/concept/rocket-engines/': '硬核工程构件的结构美学数字化典藏；用交互式三维剖面层层剥离复杂管路与燃烧室循环，在工业精密咬合中展现纯粹的机械秩序之美。',
    'https://helptheparents.org/': '以收件人的真实生活节奏重塑沟通链路；告别自嗨式公文轰炸，按家庭时间表的空档编排待办指令，大幅降低了家校沟通的信息摩擦。',
    'https://mylens.ai/': '打破一刀切演示的千人千面叙事引擎；根据不同决策层受众的关切偏好动态重构原稿侧重点，揭示了生成式内容在 B2B 转化链路中的高溢价空间。',
    'https://seths.blog/2026/10/anticipating-confusion/': '顶级营销人的心智预判心法；将产品说明书与文案的重心从“炫耀功能”转向“提前化解初学者的预期混乱”，把清晰本身打造成最锋利的获客武器。',
    'https://popcraft.ai/mcp': '营销工业化流水线与智能体协议的深度绑定；通过标准 MCP 工具串接商品分镜、脚本与视觉生成，把传统广告公司的复杂制作周期压缩进一段对话。'
}

day_items = []

# 1. 6 ian categories × 4 items
target_6_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
for c in target_6_categories:
    picked_urls = curated_ian_picks[c]
    for idx, u in enumerate(picked_urls):
        raw_it = raw_by_url[u]
        used_set.add(u)
        day_items.append({
            'category': c,
            'title': raw_it['title'],
            'note': raw_it['judgment'],
            'so_what': so_what_overrides.get(u, '从微小变化中洞察范式转移，把外部技术演进收拢为自身确定性的产品复利。'),
            'source': raw_it['source'],
            'url': u,
            'media': raw_it['media'] or 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
            'pinned': (idx < 2)
        })

# 2. 3 vertical categories × 4 items
v_info = vertical_data['2026-10-19']
for drama in v_info['ai_drama']:
    used_set.add(drama['url'])
    day_items.append(drama)
for sp in v_info['screenplay']:
    used_set.add(sp['url'])
    day_items.append(sp)
for pm in v_info['pm']:
    used_set.add(pm['url'])
    day_items.append(pm)

if len(day_items) != 36:
    raise ValueError(f'Items count is {len(day_items)}, expected 36!')

cat_order = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 漫剧', '编剧技巧', '产品经理']
sorted_items = []
for co in cat_order:
    sorted_items.extend([it for it in day_items if it['category'] == co])

md_content = f"""---
date: '2026-10-19'
title: {json.dumps(v_info['title'], ensure_ascii=False)}
highlights: {json.dumps(v_info['highlights'], ensure_ascii=False)}
draft: false
epigraph: {json.dumps(v_info['epigraph'], ensure_ascii=False)}
lead: {json.dumps(v_info['lead'], ensure_ascii=False)}
scene: {json.dumps(v_info['scene'], ensure_ascii=False)}
cover: {v_info['cover']}
items:
"""
for it in sorted_items:
    clean_title = json.dumps(it['title'].replace('\n', ' ').strip(), ensure_ascii=False)
    clean_note = json.dumps(it['note'].replace('\n', ' ').strip(), ensure_ascii=False)
    clean_so_what = json.dumps(it['so_what'].replace('\n', ' ').strip(), ensure_ascii=False)
    clean_source = json.dumps(it['source'].strip(), ensure_ascii=False)
    clean_url = json.dumps(it['url'].strip(), ensure_ascii=False)
    clean_media = json.dumps(it['media'].strip(), ensure_ascii=False)
    pinned_val = 'true' if it.get('pinned', False) else 'false'
    md_content += f"""  - category: {json.dumps(it['category'], ensure_ascii=False)}
    title: {clean_title}
    note: {clean_note}
    so_what: {clean_so_what}
    source: {clean_source}
    url: {clean_url}
    media: {clean_media}
    pinned: {pinned_val}
"""
md_content += f"""---

## 今日主理人寄语

{v_info['closing']}
"""

out_file = 'src/content/daily/2026-10-19.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-19! Total URLs in history: {len(all_used_list)}')
