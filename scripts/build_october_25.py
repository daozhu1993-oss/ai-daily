# -*- coding: utf-8 -*-
import json
import os

items = [
    # 1. AI 资讯 (4)
    {
        "category": "AI 资讯",
        "title": "Dream-1 用统一接口尝试控制陌生机器人",
        "note": "Dreamlabs 官方展示双臂机器人跨场景执行现实任务，并开放按小时计费 API；泛化表现突破传统特定工位限制，支持物理世界多样化操作。",
        "so_what": "具身智能从实验室专用控制步入通用 API 时代的重要里程碑；为后续软硬件协同操盘与物理空间自动化交付开辟了标准化接口通道。",
        "source": "dreamlabs.ai",
        "url": "https://dreamlabs.ai/research/dream-1/",
        "media": "https://iandaily.xyz/digest/2026-10-25-dream1-a83b27c1f8d9.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "GPU unlock 尝试释放部分显卡的半精度吞吐",
        "note": "Linux 开源内核模块在显卡驱动接管前动态调整底层指令发射速率；根据用户实测在部分消费级与计算卡上大幅改善 FP16/BF16 推理吞吐。",
        "so_what": "独立开发者与微型算力团队的硬核算力榨取利器；以极低工程成本释放沉睡硬件性能，压低单机本地部署大模型的延迟开销。",
        "source": "github.com",
        "url": "https://github.com/Zagitta/gpu-unlock",
        "media": "https://iandaily.xyz/digest/2026-10-25-gpuunlock-b12a8740c3ef.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "Mantid 让本机训练先和简单猜测比一轮",
        "note": "导入表格或业务文档后提出预测任务，自动对比简单启发式基线与模型表现；若未显著胜出或数据不足则即时报警中断昂贵训练。",
        "so_what": "治愈大模型落地“拿大炮打蚊子”虚荣病的清醒剂；在消耗算力前严格量化业务增益，帮团队守住 ROI 底线。",
        "source": "mantid.dev",
        "url": "https://mantid.dev",
        "media": "https://iandaily.xyz/digest/2026-10-25-mantid-091a45ce31aa.jpg?v=2026-10-25",
        "pinned": False,
    },
    {
        "category": "AI 资讯",
        "title": "Xet Server 给模型文件建立可离线的分发层",
        "note": "完全兼容 Hugging Face 客户端协议的内容寻址去重分发网关；通过分块指纹在局域网内缓存权重，断网或网络波动时仍可高速拉取交付。",
        "so_what": "终结团队内部多节点重复下载数十 GB 模型的带宽黑洞；以极简自托管方案打造离线韧性分发基础设施。",
        "source": "github.com",
        "url": "https://github.com/guilt/xet-server",
        "media": "https://iandaily.xyz/digest/2026-10-25-xetserver-fa23bc01e65d.jpg?v=2026-10-25",
        "pinned": False,
    },

    # 2. AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "1Password 让代理登录时拿权限而非密码",
        "note": "老牌密码管理巨头推出的个人 Agent 授权方案：用户在加密保管库中审批特定任务权限，代理获取受限临时令牌完成操作，明文密码永不暴露。",
        "so_what": "Agent 接管真实互联网生态的刚性安全底座；将智能体从“裸奔高危操作”推进至“细粒度受控委托”，为跨应用深水自动化扫清阻碍。",
        "source": "1password.com",
        "url": "https://1password.com/personal-ai-agent-integrations",
        "media": "https://iandaily.xyz/digest/2026-10-25-1password-62a938cde101.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "GenAIcode 给多种编程命令行统一接口",
        "note": "解耦多模型 CLI 调度与反馈的统一事件驱动层；无论底层切换 Claude 还是本地模型，均保持一致的执行流，并根据自动化测试结果决定重试策略。",
        "so_what": "对抗单一大模型供应商绑定的架构解药；让代码生成流水线具备无缝热插拔能力，以确定性的测试结果掌控代码质量。",
        "source": "github.com",
        "url": "https://github.com/gtanczyk/genaicode",
        "media": "https://iandaily.xyz/digest/2026-10-25-genaicode-443bca2e01df.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "Multipeer 把团队与代理放在同一画布",
        "note": "打破传统聊天框交互的多维空间协同画布：终端命令行、设计稿蓝图与实时运行预览同屏并排讨论，人类架构师与多个 Agent 按角色共享操作权。",
        "so_what": "人机协同从单向线性问答升级为多维空间操盘；消除跨窗口切换的认知断层，大幅提升复杂项目架构推演效率。",
        "source": "multipeer.sh",
        "url": "https://multipeer.sh",
        "media": "https://iandaily.xyz/digest/2026-10-25-multipeer-91fbc34d5671.jpg?v=2026-10-25",
        "pinned": False,
    },
    {
        "category": "AI 协作",
        "title": "AgentValley 把 Claude 代理状态塞进刘海",
        "note": "开源 Mac 顶部刘海扩展：每一个后台并发运行的 Agent 会话与子任务各占一行轻量状态条，实时呈现执行阶段与等待人类输入的确认动作。",
        "so_what": "优雅的环境微交互典范；不侵占核心工作视窗的同时让多 Agent 并发状态一览无余，彻底消除后台异步任务的遗忘焦虑。",
        "source": "agentvalley.app",
        "url": "https://agentvalley.app/",
        "media": "https://iandaily.xyz/digest/2026-10-25-agentvalley-112dfc45ea09.jpg?v=2026-10-25",
        "pinned": False,
    },

    # 3. 一人公司 (4)
    {
        "category": "一人公司",
        "title": "TranscriptClip 从公开视频提取带时间的字幕",
        "note": "直击创作者高频痛点的单兵微工具：粘贴公开视频链接即刻解析并导出带毫秒级时间轴的 TXT、SRT 与 VTT，初始试用无需注册。",
        "so_what": "单兵独立开发的极简切口模板；消除用户注册门槛，用极致轻快的确定性交付在出海创作者生态中构建稳健付费闭环。",
        "source": "transcriptclip.com",
        "url": "https://transcriptclip.com/",
        "media": "https://iandaily.xyz/digest/2026-10-25-transcriptclip-36790aebcf01.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "Shotstash 让小团队用现有硬盘共享素材",
        "note": "视频制作优先的自托管片库系统：基于本地闲置硬盘构建团队素材中枢，原生支持大文件断点续传、元数据标签与内部分享，完全开源免费。",
        "so_what": "向高昂云存储与 SaaS 订阅账单说不；让小型影视漫剧工作室用最低成本盘活已有物理资产，守住独立现金流底线。",
        "source": "github.com",
        "url": "https://github.com/Aldyernesto/shotstash",
        "media": "https://iandaily.xyz/digest/2026-10-25-shotstash-7019fce0d86e.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "Chord 用一个本地文件接起账本与净资产",
        "note": "纯本地离线单文件记账软件：支持一键导入主流银行 QFX 账单，无需绑定任何第三方账户，全键盘流极速穿透分类与多账户净资产推演。",
        "so_what": "财务数据隐私与格式主权的硬核捍卫；不依赖云端服务随时可能下线的风险，让个人与一人公司的核心账目永久安全留在本机。",
        "source": "chordfi.aquaflamingolabs.com",
        "url": "https://chordfi.aquaflamingolabs.com",
        "media": "https://iandaily.xyz/digest/2026-10-25-chord-48203c9d110f.jpg?v=2026-10-25",
        "pinned": False,
    },
    {
        "category": "一人公司",
        "title": "Shedi 把开发工具留下的大文件逐项说清",
        "note": "独立开发者打造的 macOS 清理工具：逐项透明剖析 Xcode、Docker 与 Node 依赖包缓存的磁盘占用，采用一次性买断授权，删除前先入废纸篓安全可控。",
        "so_what": "买断制实用微工具的经典商业范式；直击开发者小容量 Mac 硬盘频频告急的刚需，凭借高确定性与安全感收获极佳口碑。",
        "source": "shedi.app",
        "url": "https://shedi.app/",
        "media": "https://iandaily.xyz/digest/2026-10-25-shedi-29dcb0f19634.jpg?v=2026-10-25",
        "pinned": False,
    },

    # 4. 产品设计 (4)
    {
        "category": "产品设计",
        "title": "How It Went 让路线成为旅行短片的主角",
        "note": "将倾斜三维时空地图与连续轨迹合为一体：把零散的照片与视频片段精准锚定在地理路线节点上，按行走动线自动串联生成叙事短片。",
        "so_what": "突破相册瀑布流定式的时空交互创新；把冰冷的地点标记升华为富有情感流动的旅程故事，展现时空一体化设计的独特魅力。",
        "source": "howitwent.app",
        "url": "https://howitwent.app/",
        "media": "https://iandaily.xyz/digest/2026-10-25-howitwent-5d7ba619e078.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "Orisuji 把折叠手机变成纸迷宫的一步",
        "note": "深度结合折叠屏物理特性的创新游戏机制：屏幕两页物理合拢时通路奇妙重叠，展开时又将角色引向全新分支，将硬件动作转变为核心解谜玩法。",
        "so_what": "从“适配折叠屏”到“以折叠屏为灵魂”的交互升维；充分尊重设备物理特性的原生设计，往往能创造出无法被替代的惊喜感。",
        "source": "apps.apple.com",
        "url": "https://apps.apple.com/us/app/orisuji/id6817092898",
        "media": "https://iandaily.xyz/digest/2026-10-25-orisuji-803ca198ed61.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "一份数字礼物可以装进信纸和短旋律",
        "note": "无需注册的轻量情绪交互礼盒网页：在白描信笺上自由手绘微动贴纸、排版文字并搭配治愈短旋律，一键生成私密链接直接送达收件人。",
        "so_what": "高饱和度情绪价值与零摩擦体验的完美融合；证明优秀的设计不在于复杂功能的堆砌，而在于用最克制的载体唤醒人与人之间的细腻共鸣。",
        "source": "alittleloveforyou.app",
        "url": "https://alittleloveforyou.app/",
        "media": "https://iandaily.xyz/digest/2026-10-25-alittlelove-609de241cb23.jpg?v=2026-10-25",
        "pinned": False,
    },
    {
        "category": "产品设计",
        "title": "OpenZPL 把标签打印指令先转成预览",
        "note": "工业级标签指令的现代 Web 转译器：将晦涩的 Zebra ZPL 硬件打印代码直接在浏览器中渲染为高保真 PNG 与矢量 PDF，批量出单前先完成像素级校对。",
        "so_what": "消灭仓储与物流硬件交互的试错成本；用纯软件层的友好交互包裹粗糙的工业协议，把枯燥的后勤配置打磨成优雅的现代体验。",
        "source": "openzpl.com",
        "url": "https://openzpl.com/",
        "media": "https://iandaily.xyz/digest/2026-10-25-openzpl-1721df904321.jpg?v=2026-10-25",
        "pinned": False,
    },

    # 5. 审美提升 (4)
    {
        "category": "审美提升",
        "title": "爱马仕橱窗把房间缝成柔软的被子",
        "note": "Space Popular 为爱马仕伦敦旗舰店打造的诗意装置：用细腻绗缝织物构筑出柔软壁炉、虚实窗棂与轻柔织物浮云，将奢华皮具轻柔包裹在温暖梦境中。",
        "so_what": "空间叙事对商业陈列的降维赋能；摆脱商品单调罗列，用材质的触觉通感与建筑语言构建引人入胜的品牌精神引力场。",
        "source": "wallpaper.com",
        "url": "https://www.wallpaper.com/architecture/hermes-quilt-windows-space-popular-london",
        "media": "https://iandaily.xyz/digest/2026-10-25-hermes-d81a97bc1032.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Avocado House 从三个圆切出沙漠庭院",
        "note": "加州荒漠中由三个纯粹几何圆相切而成的隐秘住所：弧形夯土墙围合出内省庭院，开口精准定格远山与巨石，泳池与天地融为一体。",
        "so_what": "极简几何形体与自然荒野的张力对话；用最纯粹的几何秩序为残酷干旱的物理环境注入宁静深远的建筑庇护感。",
        "source": "wallpaper.com",
        "url": "https://www.wallpaper.com/architecture/residential/avocado-house-desert-home-california-usa",
        "media": "https://iandaily.xyz/digest/2026-10-25-avocadohouse-39d2c67f08e1.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "细线立柱随着人的靠近改变影子",
        "note": "坂本洋太郎将传统竹帘通透感转译为动力机械交互艺术：悬垂细线在微型电机驱动下旋转，光影投影随驻足观众的距离与步频实时变幻。",
        "so_what": "东方留白美学与现代动态机械的优雅缝合；证明最震撼的科技艺术不需要刺眼的屏幕，而是对自然光影与人体存在的细腻捕捉。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/art/youtaro-sakamoto-kinetic-thread-column-human-presence-shifting-shadows-schattenrequisit/",
        "media": "https://iandaily.xyz/digest/2026-10-25-threadcolumn-821f00b991da.jpg?v=2026-10-25",
        "pinned": False,
    },
    {
        "category": "审美提升",
        "title": "Gasfree 把模块合成器的接线搬进网页",
        "note": "纯 Web Audio 打造的模块化 Eurorack 合成器网页：面板支持完全翻转，支持真实的虚拟跳线接驳、控制电压调制与滤波器旋钮阻尼调节。",
        "so_what": "数字拟物化美学的硬核复兴；将昂贵的专业物理声学设备降维为每个人触手可及的浏览器交互，让音色探索充满仪式感。",
        "source": "gasfree.app",
        "url": "https://gasfree.app/",
        "media": "https://iandaily.xyz/digest/2026-10-25-gasfree-5561a3ec8401.jpg?v=2026-10-25",
        "pinned": False,
    },

    # 6. 产品营销 (4)
    {
        "category": "产品营销",
        "title": "外链工作台把提交进度从记忆变成记录",
        "note": "出海产品冷启动的结构化看板：系统梳理全球 500+ 高质量产品目录与提交入口，支持按项目进度打标、追踪收录状态与历史回链。",
        "so_what": "把零散低效的冷启动推广沉淀为标准化作业流程（SOP）；消除海外分发时的执行混乱，确保每一分推广精力都落地生根。",
        "source": "ffee.me",
        "url": "https://ffee.me/product-submission/",
        "media": "https://iandaily.xyz/digest/2026-10-25-ffeeproduct-02b9da54a8cf.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "AI Cite Who 把推荐证据拆成网站修改任务",
        "note": "生成式搜索时代（GEO）的内容审计平台：核对主流大模型在推荐具体行业解决方案时的引用信源与缺失事实，生成立即可执行的页面事实修改清单。",
        "so_what": "从争夺传统点击量转向争夺“AI 权威引用实体”；让品牌在机器对话中抢占被信赖的权威证据位，赢得下一代流量分配权。",
        "source": "aicitewho.com",
        "url": "https://aicitewho.com/",
        "media": "https://iandaily.xyz/digest/2026-10-25-aicitewho-7918cae10b42.jpg?v=2026-10-25",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "LinkIntel 把自己的发帖结果交回写作助手",
        "note": "社交媒体增长闭环工具：自动抓取多平台历史推文的数据表现与互动指标，经 MCP 协议无缝喂回本地编写 Agent，基于实测反馈动态校准文案网感。",
        "so_what": "用真实转化数据反哺内容生产的主动智能体回路；彻底告别拍脑袋自嗨，让每一次发帖都成为算法进化的强化学习样本。",
        "source": "getlinkintel.com",
        "url": "https://www.getlinkintel.com/",
        "media": "https://iandaily.xyz/digest/2026-10-25-linkintel-4710bde551cb.jpg?v=2026-10-25",
        "pinned": False,
    },
    {
        "category": "产品营销",
        "title": "ConferenceFindr 从行业与预算筛线下活动",
        "note": "精准 B2B 线下获客雷达：支持按垂直行业、举办城市与门票预算快速收窄全球展会范围，提供 MCP 接口供营销智能体自主检索匹配参展机会。",
        "so_what": "实体高客单获客场景的智能化检索基础设施；打破线上买量红海，帮助出海企业在精准的物理面对面场景中高效签单。",
        "source": "conferencefindr.com",
        "url": "https://www.conferencefindr.com",
        "media": "https://iandaily.xyz/digest/2026-10-25-conferencefindr-9310a0df32ea.jpg?v=2026-10-25",
        "pinned": False,
    },

    # 7. AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "全民“戒断”红果，可能吗？短剧下沉生态与免费模式的成瘾机制解剖",
        "note": "微短剧下沉市场免费模式的深度商业剖析：抽丝剥茧拆解红果等平台如何以“看剧赚金币 + 算法强爽点”重构中老年与下沉群体的心智，形成高频消费黏性。",
        "so_what": "视听产品必须深刻理解的用户心理学账本；免费不是慈善而是更高维的注意力收割，漫剧创作必须把黄金 3 秒抓手与情绪补偿作为第一原则。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6483664.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "拉美短剧：流量按吨卖，收入按克算——出海本土化与低成本制作实录",
        "note": "出海短剧开拓拉美新兴市场的实战账本透视：深入剖析买量成本、语言文化隔阂以及海外支付履约挑战，还原低成本本土化团队如何依靠极致周转跑出微利。",
        "so_what": "出海内容操盘手的冷静生存手册；别被虚假的高播放量迷惑，只有把制作成本、投放漏斗与海外本地结汇死死算透，业务才具备活下去的底气。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6482999.html",
        "media": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "“你被AI取代了”：短剧人的2026与虚拟制片实操",
        "note": "一线影视与短剧制作团队的转型纪实：详述传统打光师、道具师与副导演如何告别沉重现场器材，全面拥抱 ComfyUI、3D 空间资产与虚拟制片工作流。",
        "so_what": "影视生产力格局的不可逆迁徙；技术淘汰的不是创作者，而是抱残守缺的旧生产关系，掌握 AI 管线的全能单兵将全面统治新视听时代。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6482977.html",
        "media": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "AI 漫剧",
        "title": "AI短剧公司几乎不要基础岗：影视后期工业化革命与劳动力结构重构",
        "note": "生成式 AI 制片公司运营模式的深度行业观察：随着画风一致性、分镜扩写与口型对齐全流程节点化，传统初级原画、抠像与套剪岗位被大幅精简。",
        "so_what": "工业化后期流水线的终局预演；一人操盘全链路不再是口号，产品型制片人必须建立从剧本策划到管线交付的全栈掌控力。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6483874.html",
        "media": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 8. 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "《盼归》家庭古装短剧：家国恩怨与代际和解的情感戏因果网",
        "note": "古装情感类型短剧的因果冲突范本：自幼厌战的少年被卷入父亲通敌叛国的弥天大罪，在逃亡与调查中将父子反目与生死羁绊严密嵌套。",
        "so_what": "类型短剧如何在快节奏中构建扎实情感弧光；用外部生死危机强力催化内部代际和解，让观众在紧凑情节中获得深层共情体验。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/1786",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "《离婚后，我成为前夫的白月光》都市虐恋短剧：情绪价值错位与逆袭打脸节拍",
        "note": "都市下沉情感短剧的爆款密码拆解：前期极致隐忍奉献与误解牺牲，后期华丽蜕变后对前夫的降维惩戒，节拍紧凑且每一集都设有情绪抓手钩子。",
        "so_what": "情感补偿类剧本的经典商业写法；精准捕捉目标受众在现实中被压抑的情绪委屈，用工整的打脸因果律交付极致代偿爽感。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/1789",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "《返乡后，我凭手艺赢麻了》乡村轻喜剧短剧：女性成长与手艺逆袭的爽点落地",
        "note": "新农村搞钱题材的精妙结构示范：摒弃传统恶俗婆媳撕逼，以女主祖传非遗手艺与现代乡村电商结合为主线，用踏实的商业进阶包裹接地气的温情笑料。",
        "so_what": "大女主独立成长题材的破局之道；将爽感扎根在真实的手艺壁垒与商业智慧上，既符合政策导向又具备广阔的商业变现势能。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/1795",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "编剧技巧",
        "title": "《魔鬼的心》哲学悬疑短剧：灵魂拷问与命运博弈的高概念设定",
        "note": "高概念思辨短剧的结构编织技巧：以一场关乎灵魂交易的神秘契约为引爆点，主角在逆天改命与道德深渊间层层涉险，反转不断且结局发人深省。",
        "so_what": "悬疑短剧跳出低质同质化的升阶指南；用坚实的高概念哲学命题托底冲突，证明短剧同样能承载严肃的精神思考与剧作分量。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/1796",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 9. 产品经理 (4)
    {
        "category": "产品经理",
        "title": "业财产品实战：对账中心 0-1 产品设计与复杂边界状态机",
        "note": "交易中枢底层架构复盘：深入拆解三方支付、银联渠道、预付账户与财务总账之间复杂的多渠道对账流水设计，系统推演长链路平账与差错逆向冲销机制。",
        "so_what": "高阶交易与金融产品经理的基本功标尺；只有把资金流、业务流与会计凭证的边界状态机严丝合缝闭环，平台才能在海量并发下安全运转。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/operate/6483720.html",
        "media": "https://images.unsplash.com/photo-1556742049-0a67e557224d?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "一条视频 1160万播放，为什么几乎没人下载 App？191个创业者的增长复盘",
        "note": "穿透虚荣流量迷雾的冷血增长复盘：深度剖析爆款短视频引来的泛娱乐点赞与核心目标受众之间的巨大断层，警示创业团队切莫将曝光误判为产品核心价值。",
        "so_what": "刺破流量泡沫的产品人清醒剂；流量不等于转化，曝光不等于留存，必须围绕核心用户的付费交付链条打磨产品，而非沉迷算法虚热。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/chuangye/6483400.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "逐渐被淘汰的 AI 产品设计与交互：从“聊天框套壳”到“意图动作流”",
        "note": "AI 原生交互范式的深水演进复盘：全面剖析为什么传统的空白对话框难以承载严肃复杂的生产力任务，探讨基于上下文画板、原位修改与主动动作的未来系统形态。",
        "so_what": "AI 时代产品经理的设计范式迁徙；停止让用户在对话框中猜谜，用确定性的系统结构赋能大模型，把意图转译为稳定可靠的业务动作。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6483815.html",
        "media": "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "产品经理",
        "title": "好的商业模式三句话就能讲清楚：从真伪需求判断到护城河构建的实战指南",
        "note": "资深创业操盘手的底层商业思考方法论：剔除所有花哨的技术概念，直面目标客户痛点有多痛、交付边际成本有多低以及对手为什么抄不走这三大终极拷问。",
        "so_what": "一人公司与初创团队的生死护身符；在资源极度有限的前提下，唯有建立清晰明了的商业常识，才能在长跑中建立牢不可破的竞争壁垒。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/chuangye/6476870.html",
        "media": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
]

# Verify counts
assert len(items) == 36, f"Expected 36 items, got {len(items)}"
categories = [i["category"] for i in items]
from collections import Counter
cat_counts = Counter(categories)
print("Categories:", dict(cat_counts))
assert all(v == 4 for v in cat_counts.values()) and len(cat_counts) == 9

# Deduplicate check against all-used-urls.json
used_path = "scripts/all-used-urls.json"
used_urls = set(json.load(open(used_path, "r", encoding="utf-8")))
item_urls = [i["url"] for i in items]
assert len(item_urls) == len(set(item_urls)), "Duplicate URLs within today's issue!"
dups = [u for u in item_urls if u in used_urls]
assert len(dups) == 0, f"Found duplicates in all-used-urls.json: {dups}"

# Generate Markdown
date_str = "2026-10-25"
title_str = "10 月 25 日 · 具身动作与主权收拢：当智能体开始告别“对话框虚荣”"
highlights_str = "全网 9 大领域 36 篇高密度精选：1Password 推出个人 Agent 权限委派接管登录、Dream-1 统一双臂机器人跨场景物理接口、微短剧拉美出海账本与免费模式下沉成瘾机制全剖析、AI 漫剧虚拟制片重构传统影视后期、业财底层对账中心 0-1 边界状态机设计复盘。"
epigraph_str = "在对话框里扮演全知全能的智能体正在迅速失宠；能跨越应用拿到受限权限、能替人类真实操作现实机械与账本的动作流，才是大模型落地真正的硬通货。"
lead_str = "10 月 25 日，大模型应用生态正经历一场直击灵魂的“范式大迁徙”。随着千亿级大模型在参数竞赛上的边际效应递减，整个行业开始集体清算过去的浮躁自嗨：单薄的问答聊天框正在被主流用户加速抛弃，取而代之的是深度融入工作流的意图画布与后台动作系统；1Password 官方推出个人 Agent 权限委派机制，让智能体跨应用接管任务时告别“明文密码裸奔”的巨大隐患；Dreamlabs 发布统一接口让双臂机器人跨场景接管现实世界的物理搬运；在视听与内容出海战场，微短剧在拉美和三四线市场的极致免费模式与买量账本被彻底摊开，AI 漫剧制片公司更是全面重构传统影视后期岗位，一人操盘全流程虚拟制片正在从预言变为现实；而在商业与交易中枢一线，点赞千万却零转化的冷血复盘与业财底层对账状态机的精细设计，都在向所有产品人传递同一个朴素真理——穿越技术泡沫的唯一底牌，是用扎实落地的产品资产解决真实世界的真问题。"
scene_str = "「我们做一个能陪用户随时聊天的悬浮助手，体验不是挺好的吗？」「用户打开工具不是来跟你促膝长谈的。别让用户在对话框里猜提示词，把能直接执行的按钮、画布与对账动作摆到他面前，才是真正的产品交付。」"

lines = [
    "---",
    f"date: '{date_str}'",
    f'title: "{title_str}"',
    f'highlights: "{highlights_str}"',
    "draft: false",
    f'epigraph: "{epigraph_str}"',
    f'lead: "{lead_str}"',
    f'scene: "{scene_str}"',
    "cover: https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80",
    "items:",
]

for it in items:
    lines.append(f'  - category: "{it["category"]}"')
    lines.append(f'    title: "{it["title"]}"')
    # Escape quotes in note and so_what
    safe_note = it["note"].replace('"', '\\"')
    safe_sowhat = it["so_what"].replace('"', '\\"')
    lines.append(f'    note: "{safe_note}"')
    lines.append(f'    so_what: "{safe_sowhat}"')
    lines.append(f'    source: "{it["source"]}"')
    lines.append(f'    url: "{it["url"]}"')
    lines.append(f'    media: "{it["media"]}"')
    lines.append(f'    pinned: {"true" if it["pinned"] else "false"}')

lines.append("---")
lines.append("")
lines.append("## 今日主理人寄语")
lines.append("")
lines.append("今天是周日。")
lines.append("")
lines.append("梳理今天这 36 篇来自全球前沿的硬核动态时，我最强烈的感受是：")
lines.append("**AI 行业终于开始集体告别“在对话框里陪聊”的虚荣期，大步迈入“在真实世界里拿结果”的动作交付期。**")
lines.append("")
lines.append("曾几何时，无数产品试图把所有场景塞进一个聊天输入框；")
lines.append("但实践证明，用户没有那么多闲情逸致去揣摩 Prompt，更不愿意对着冰冷的加载光标等待一段正确的废话。")
lines.append("")
lines.append("今天，真正的突破正在发生在那些充满摩擦的深水区：")
lines.append("1Password 开始让 Agent 拿到受控的会话权限去真实接管网页操作；")
lines.append("Dreamlabs 正在用标准 API 把动作指令灌入双臂机器人的机械关节；")
lines.append("影视漫剧团队用 ComfyUI 和虚拟制片彻底洗牌后期流水线；")
lines.append("而交易与业财产品经理，则在对账状态机里为每一分钱的流转筑牢防线……")
lines.append("")
lines.append("技术从来不讲虚荣的情面，它只奖赏那些直面物理规律与商业现实的躬身入局者。")
lines.append("愿你在新的一周里，少一些对话框里的浮想联翩，多一些在真实系统与动作流中的笃定深耕。")

md_content = "\n".join(lines) + "\n"

target_md = f"src/content/daily/{date_str}.md"
with open(target_md, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"Generated {target_md} with {len(items)} items!")

# Update all-used-urls.json
all_updated = list(used_urls) + item_urls
with open(used_path, "w", encoding="utf-8") as f:
    json.dump(all_updated, f, indent=2, ensure_ascii=False)
print(f"Updated {used_path}: from {len(used_urls)} to {len(all_updated)} URLs.")
