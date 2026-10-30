# -*- coding: utf-8 -*-
import json
import os
from collections import Counter

items = [
    # 1. AI 资讯 (4)
    {
        "category": "AI 资讯",
        "title": "谷歌发布 Gemini 4 Carbon：长程工程任务与网络防御前沿模型",
        "note": "谷歌前沿大模型的重要跃迁：专攻超长跨度复杂代码工程重构与高对抗网络防御场景，在深层抽象推演与多步骤漏洞修补上展现极高稳定性。",
        "so_what": "AI 从辅助写代码走向全栈软件工程自主执飞；长程工程一致性是衡量模型是否具备真正工程师水准的分水岭，模型正在重新定义高壁垒安全防御规则。",
        "source": "deepmind.google",
        "url": "https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/",
        "media": "https://iandaily.xyz/digest/2026-10-29-carbon-080f7ac32da9.jpg",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "NVIDIA 开源 Nemotron 3.5：语音转录与说话人识别统一架构",
        "note": "开源多模态音频基础模型的重大突破：单模型端到端支持 40 种语言高保真转录，将音色特征对齐、角色分离与自然语言上下文理解原生融为一体。",
        "so_what": "打破传统声学工程切片级联的繁重链路；让多方会议纪要、播客转录与具身语音交互以极低延迟完成全要素解析，极大降低企业端语音智能基座的部署门槛。",
        "source": "huggingface.co",
        "url": "https://huggingface.co/blog/nvidia/nemotron-transcribe-granary",
        "media": "https://iandaily.xyz/digest/2026-10-29-nemotron-9db430656087.jpg",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "Astra 冲击波与具身行业的 50 天：通用多模态物理世界理解复盘",
        "note": "复盘通用多模态视觉模型在机器人与空间智能领域的狂飙演进：从实时视频流多物体跟踪到毫秒级物理空间反馈，硬核记录产业生态的剧烈分化。",
        "so_what": "空间理解能力正在彻底撕开具身智能的商业破局点；单纯依靠遥控示教的传统机械臂迅速贬值，具备端到端环境因果直觉的机器人系统成为唯一赢家。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/embodied/6486357.html",
        "media": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "AI 资讯",
        "title": "中国 AI 最有权力的数据掌舵人：8 家公司与 11 位核心负责人透视",
        "note": "深度起底大模型竞争最隐秘的核动力源泉：全景扫描国内头部大模型公司高质量语料架构师、清洗标注流水线操盘手及其背后的战略数据版图。",
        "so_what": "模型参数同质化后，语料纯度成为绝对生死线；算法可以通过论文复现，但经过千万小时清洗、蒸馏并对齐行业常识的专有高质量数据集是无可替代的护城河。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6486016.html",
        "media": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 2. AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "GitHub Universe 2026：Copilot App 与多智能体端到端交付架构",
        "note": "软件开发基础设施的范式蜕变：展示从需求 issue 拆解、多代理协同编码、沙箱测试到自动化合入 PR 的统一交互平台，人类开发者全面升级为架构审阅者。",
        "so_what": "定义下一代研发组织协同的新基线；个人英雄主义的手工编码正在被多智能体装配流水线替代，团队效率的决胜点转移到规约定义与审阅吞吐能力。",
        "source": "github.blog",
        "url": "https://github.blog/news-insights/company-news/github-universe-2026-evolving-every-layer-of-the-stack/",
        "media": "https://iandaily.xyz/digest/2026-10-29-github-e8b9b146ed0a.jpg",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "OpenRouter 推出 Claude Code 按量续用方案：无缝衔接高强度工程",
        "note": "针对高强度自主编程工作流的成本与配额优化实践：当订阅额度耗尽时，无缝自动路由至底价 API 账单通道，保障大型重构任务在夜间不中断运行。",
        "so_what": "扫清无人值守代码智能体落地的最后一道计费断点；工程任务的确定性要求算力供给具备高可用弹性，精细化的多通道路由成为开发者的标配武器。",
        "source": "openrouter.ai",
        "url": "https://openrouter.ai/blog/tutorials/claude-code-usage-limit/",
        "media": "https://iandaily.xyz/digest/2026-10-29-openrouter-83c21ac5cdca.jpg",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "PostHog 推出自驾驶 CI：让智能体从真实监控数据中主动找 Bug",
        "note": "打破传统自动化测试被动等待报错的局限：智能体直连生产环境事件流与日志数据层，主动识别异常突增、归因调用堆栈并自动生成修复分支提交审阅。",
        "so_what": "软件质量保障体系从“事后被动报警”向“自主巡检修复”的质变；将数据湖变为智能体的常驻输入源，极大释放了基础架构团队的防御性精力。",
        "source": "posthog.com",
        "url": "https://posthog.com/blog/self-driving-ci",
        "media": "https://iandaily.xyz/digest/2026-10-29-posthog-6d0172448785.jpg",
        "pinned": False,
    },
    {
        "category": "AI 协作",
        "title": "Gitby 用文件认领机制消除同分支冲突：人机协同终端新体验",
        "note": "极度优雅的协同冲突防御工具：在单分支高频并发编辑场景下，通过终端热键动态认领正在修改的文件并将队友端设为临时只读，在源头消灭 merge 噩梦。",
        "so_what": "人机高速结对编程时的极简护栏；与其在代码合入时费力处理 AST 语法树冲突，不如用最小交互成本在物理层面锁定文件管辖权，保障工作流心流不中断。",
        "source": "gitby.dev",
        "url": "https://gitby.dev",
        "media": "https://iandaily.xyz/digest/2026-10-29-gitby-0362e70ffdf6.jpg",
        "pinned": False,
    },

    # 3. 一人公司 (4)
    {
        "category": "一人公司",
        "title": "WorkSnap 为按小时计费者保留完整账本：独立顾问的财务利器",
        "note": "面向高级自由职业者与独立架构师的财务工作台：将项目费率核算、预付工时消耗、精准计时与一键导出深度整合，免除一切团队协作的冗余负担。",
        "so_what": "一人企业最核心的现金流确定性保障；用极度克制的功能专注解决高价值专业交付的计费核对痛点，让单兵作战也能拥有媲美咨询公司的记账专业感。",
        "source": "worksnap.eu",
        "url": "https://worksnap.eu",
        "media": "https://iandaily.xyz/digest/2026-10-29-worksnap-3c10505de83d.jpg",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "Toolvy 把媒体处理留在浏览器本机：零服务器成本的微型 SaaS",
        "note": "基于 WebAssembly 与本地算力的实用工具矩阵：音频压缩、视频格式转码、本地离线字幕提取全部在浏览器内存执行，绝不向云端上传任何隐私素材。",
        "so_what": "独立开发者打造高毛利产品的教科书级架构；将算力成本彻底卸载给客户端芯片，不仅极大降低云服务运维开销，更用绝对隐私构筑竞争壁垒。",
        "source": "toolvy.net",
        "url": "https://toolvy.net/",
        "media": "https://iandaily.xyz/digest/2026-10-29-toolvy-3a09eee8b295.jpg",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "Ordpin 用 1% 成交抽成代替商户月租：小微餐饮轻量下单系统",
        "note": "颠覆传统外卖与点单 SaaS 高昂月费壁垒的轻量化产品：咖啡店与独立商铺即开即用，只按真实成交折后金额抽取 1% 服务费，零固定沉没成本。",
        "so_what": "一人开发撬动线下长尾商户的精准商业模式；摒弃大厂大包大揽的厚重硬件绑定，用与商户收益完全挂钩的低抽成机制打穿小微餐饮的冷启动阻力。",
        "source": "ordpin.com",
        "url": "https://ordpin.com",
        "media": "https://iandaily.xyz/digest/2026-10-29-ordpin-c9f071251230.jpg",
        "pinned": False,
    },
    {
        "category": "一人公司",
        "title": "Trvlrr 邮件解析行程与私人旅行地图：高品味个人生活数字资产",
        "note": "将零散生活碎片转化为高密度记忆资产的独立应用：转发酒店机票预订邮件即可自动提取时间线，并借助语义检索自动关联老照片，生成极简旅程海报。",
        "so_what": "单兵产品切入情感共鸣领域的极致审美范本；不与传统巨头比拼机酒交易平台，只专注于“个人生命体验的优雅数字化存档”，开辟高粘性付费空间。",
        "source": "trvlrr.app",
        "url": "https://trvlrr.app/",
        "media": "https://iandaily.xyz/digest/2026-10-29-trvlrr-a540ceecb7eb.jpg",
        "pinned": False,
    },

    # 4. 产品设计 (4)
    {
        "category": "产品设计",
        "title": "Jotcal 把日程做成远处也看得清的墙历：实体感与墨水屏交互",
        "note": "极具物理实体温度的数字日程设计：圆盘清晰标出全天安排与空档分布，针对平板与电子墨水屏深度定制高对比度模式，兼顾远距离可读性与美感。",
        "so_what": "逃离信息过载、回归环境界面（Ambient UI）的设计先锋；不抢占用户眼球，而是在空间角落静默提供清晰态势感知，展现现代软硬件设计的克制之美。",
        "source": "jotcal.app",
        "url": "https://jotcal.app/",
        "media": "https://iandaily.xyz/digest/2026-10-29-jotcal-354f424fa99d.jpg",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "SlideBySide 让观众自主进入同一份幻灯片：去中心化演示交互",
        "note": "重塑传统单向演示关系的轻量协作设计：观众通过链接进入演示房间，既可与主讲人同步翻页画线，也能暂时脱离主线自行按需前后浏览深度附录。",
        "so_what": "尊重受众注意力自主权的信息交互跃迁；打破“一人演讲、全员被动受困”的旧会议范式，让复杂商业汇报变成双向互动的沉浸式信息空间。",
        "source": "slidebyside.com",
        "url": "https://slidebyside.com/",
        "media": "https://iandaily.xyz/digest/2026-10-29-slidebyside-57e992b00a1a.jpg",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "Tucklane 为项目保存可返回的桌面：工作上下文物理态快照",
        "note": "拯救数字工作者注意力碎片化的上下文收纳器：将与特定项目关联的应用窗口、文档、网页标签与下一步便签打包归档，随时一键还原专属工作场。",
        "so_what": "将认知负荷外包给系统的极佳交互范例；多任务切换最大的损耗是找回上下文的几分钟心智预热，用物理空间记忆法让深度工作状态无缝延续。",
        "source": "enlightpixel.com",
        "url": "https://enlightpixel.com/products/tucklane",
        "media": "https://iandaily.xyz/digest/2026-10-29-tucklane-378da40e64eb.jpg",
        "pinned": False,
    },
    {
        "category": "产品设计",
        "title": "Talkhawk 松开快捷键就填入口述：语音原生输入的微交互极致",
        "note": "桌面端语音输入交互的极简形态：按住全局快捷键说话，松手瞬间大模型自动清除口误、补全标点并精准注入光标焦点，彻底杜绝悬浮窗口打扰。",
        "so_what": "AI 原生交互从“对话框”退回“无形管道”的成熟体现；最好的 AI 体验往往不需要界面，而是以肌肉记忆级的极低摩擦融入既有输入习惯。",
        "source": "talkhawk.app",
        "url": "https://talkhawk.app/",
        "media": "https://iandaily.xyz/digest/2026-10-29-talkhawk-1e915d5b91e1.jpg",
        "pinned": False,
    },

    # 5. 审美提升 (4)
    {
        "category": "审美提升",
        "title": "Studio Loutsis 打造厚木导视系统：让指示标生长进建筑表皮",
        "note": "为斯诺赫塔操刀的罗斯福总统图书馆定制视觉设计：采用温润原木与定制衬线字符，将导向标牌与墙面纹理同构，达成建筑与信息的高度一体化。",
        "so_what": "空间导向与生态美学共生的经典范式；摒弃工业塑料指示牌的突兀冷硬，用大自然的肌理与典雅排版为公共文化空间注入永恒的精神沉淀。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/architecture/studio-loutsis-timber-wayfinding-snohetta-theodore-roosevelt-library/",
        "media": "https://iandaily.xyz/digest/2026-10-29-loutsis-1aaafdf05417.jpg",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Duyi Han 织物听雨花园：上海别墅里的跨媒介通感艺术装置",
        "note": "将中国传统听雨意象转化为现代居住空间的先锋实验：水纹刺绣羊毛地毯与褶皱透光欧根纱轻拂，结合细微环境声学设计，重构居所的气氛尺度。",
        "so_what": "东方诗意与现代装置艺术的惊艳对话；证明最高级的美学体验从不止于眼球刺激，而是调动触觉、听觉与光影联觉，打造能让人心灵安顿的场域。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/art/duyi-han-rain-inspired-textile-listening-garden-shanghai-villa/",
        "media": "https://iandaily.xyz/digest/2026-10-29-duyi-92c5d196d1da.jpg",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Page\\Park 用石木天光组织校园照护：爱丁堡疗愈建筑典范",
        "note": "人本主义疗愈空间的建筑结构创新：以共享公共绿厅为核心，诊室向林地舒展延伸，抬高的木构屋架引入环绕天光，彻底驱散传统医疗封闭感。",
        "so_what": "用建筑语言传递心理关怀的极佳样板；空间几何与自然光的精心编排直接决定了使用者的情绪起伏，建筑师用温柔的材质化解了制度化的冰冷焦虑。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/10/28/pagepark-allardice-centre/",
        "media": "https://iandaily.xyz/digest/2026-10-29-pagepark-4adb4914e6c4.jpg",
        "pinned": False,
    },
    {
        "category": "审美提升",
        "title": "A2 Type 为路易斯安那现代艺术博物馆定制四套专用字体",
        "note": "顶级美术馆视觉识别系统的深厚积淀：从历史印刷档案与现代建筑肌理提炼灵感，打造涵盖经典衬线、无衬线与专用艺术字形的完整排版语言。",
        "so_what": "字体作为文化机构无形精神资产的终极呈现；一套真正优秀的美术馆字体不仅承载展陈说明，更本身就是一件跨越半个世纪时光的长效艺术品。",
        "source": "itsnicethat.com",
        "url": "https://www.itsnicethat.com/articles/a2-type-louisiana-museum-of-modern-art-graphic-design-project-281026",
        "media": "https://iandaily.xyz/digest/2026-10-29-a2type-4deb544bfbc6.jpg",
        "pinned": False,
    },

    # 6. 产品营销 (4)
    {
        "category": "产品营销",
        "title": "Convoy 用单链接聚合活动与咨询销售：私域高转化闭环",
        "note": "知识博主与独立咨询师的高转化营销中枢：将日历预约、阶梯付费、活动直播回放与后续跟进邮件集于单一短链，大幅缩短潜客决策链条。",
        "so_what": "消除多跳转化漏斗中的流失损耗；现代知识经济的变现核心是信任变现，用极简的单页体验包裹复杂的交易交付逻辑，最大化每一次公域引流的 ROI。",
        "source": "convoy.so",
        "url": "https://convoy.so",
        "media": "https://iandaily.xyz/digest/2026-10-29-convoy-ffcbde2adbb3.jpg",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "Fraud Blocker 广告虚假点击可解释拦截：保卫真实营销预算",
        "note": "AI 驱动的广告防作弊核查引擎：结合实时行为指纹与大模型异常推断，不仅精准拦截刷量机器人点击，更为每个封禁 IP 出具详尽因果证据链。",
        "so_what": "戳穿买量繁荣表象下的黑灰产泡沫；在广告投放成本高企的当下，省钱就是最直接的净利润，可解释的证据链让营销团队真正掌握对渠道的问责底气。",
        "source": "fraudblocker.com",
        "url": "https://fraudblocker.com/ai-detection",
        "media": "https://iandaily.xyz/digest/2026-10-29-fraud-e9b8d1f2abd3.jpg",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "Tulu 把自然语言问答直连业务数据：实时监控投放点击成本",
        "note": "全渠道营销数据的智能归因大脑：打通 Google/Meta 广告、网站埋点与 CRM 交易数据库，操盘手在通讯软件中发问即可获知异常成本波动的归因诊断。",
        "so_what": "终结数据看板林立却无人能看懂的决策瘫痪；将枯燥的 SQL 查询转化为随身智能顾问，帮助增长操盘手以秒级速度调整预算分配，捕捉红利窗口。",
        "source": "onetulu.com",
        "url": "https://www.onetulu.com/",
        "media": "https://iandaily.xyz/digest/2026-10-29-tulu-13bde393eb3f.jpg",
        "pinned": False,
    },
    {
        "category": "产品营销",
        "title": "从场景到记忆：体验主题化在全域转化与品牌心智中的实战指南",
        "note": "深度解析现代营销中如何跳出硬广轰炸、通过打造特定情感主题场景构筑用户记忆锚点，将短期购买行为沉淀为长期的品牌归属感。",
        "so_what": "品牌对抗流量算法不断剥削的根本解法；功能价值会被快速模仿，但带有情感温度的主题化体验却能在用户心智中构筑不可磨灭的防御壁垒。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/marketing/6485849.html",
        "media": "https://images.unsplash.com/photo-1557804506-669a67965ba0?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 7. AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "红果短剧不想成为行业公敌：全生态重兵对垒与制片方分成博弈",
        "note": "短剧巨头在分发与版权格局中的深度战略复盘：面对传统影视资本与新兴网文阵营的围剿，红果如何在免费沉浸式体验与高阶版权保护中寻找平衡。",
        "so_what": "微短剧生态从野蛮收割走向成熟博弈的缩影；平台若想长盛不衰，必须构建能让优质创作者持续获利的健康分配机制，单纯依靠买量补贴终将触及天花板。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6485847.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "红果开始给自己踩刹车了：微短剧狂飙后期的监管红线与精品化防线",
        "note": "透视微短剧赛道从低俗暴利向精品合规的主动转向：平台在内容审核、未成年人防护以及价值观导向上的系统级收紧，倒逼制作管线全面升级。",
        "so_what": "粗制滥造的短剧洗牌出局，工业化团队迎来红利；合规红线不是枷锁而是护城河，掌握高质量视听工业化管线的创作团队将在大浪淘沙后掌握定价权。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6485918.html",
        "media": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "年轻人都在找的“屏享搭子”：互动短剧与陪伴式视听新社交生态",
        "note": "微短剧在年轻群体中催生的新型社交行为洞察：结合屏幕共享、实时弹幕吐槽与分支剧情投票，将原本孤独的竖屏刷剧转变为群体情感共鸣场域。",
        "so_what": "漫剧视听产品正在从单纯内容消费向社交互动场域演变；懂得以剧集为载体设计社交玩法与互动裂变点，才能牢牢抓住 Z 世代的核心注意力。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6486187.html",
        "media": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "AI 漫剧",
        "title": "电商产品设计终极工作流：用 AI 生成可交互、可拆解的产品 3D demo",
        "note": "将微短剧镜头语言与三维电商渲染深度打通的实战管线：通过生成式大模型将单一平面货品图片转化为可 360 度旋转拆解的动态视听演示卡片。",
        "so_what": "数字资产工业化在消费级场景的全面降临；极大压缩了原本需要专业 3D 团队数周周期的建模与动效开销，让中小卖家也能以电影级质感呈现商品细节。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6486200.html",
        "media": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 8. 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "《莫比乌斯大戏院》金融反腐剧本改编：职场洗钱局中局与因果环形节拍",
        "note": "硬核现实主义商战短剧的剧作结构拆解：围绕 30 万字金融反腐小说展开，将跨国资金池暗流、账目漏洞与多方势力虚假供述编织成环形博弈节拍。",
        "so_what": "高智商行业剧对抗套路化的关键在于专业逻辑自洽；用扎实的金融审计细节与因果闭环支撑起悬疑张力，才能给习惯快餐短剧的观众带来震撼的认知冲击。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2205",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "《硅基黎明》120 集硬科幻微短剧：AI 觉醒伦理博弈与连环危机推演",
        "note": "科幻微短剧的极限戏剧压力构建法：设定在近未来人机融合临界点，通过底层代码隐蔽变异、人机信任崩塌与连续 120 个微型悬念点紧密咬合。",
        "so_what": "长篇微短剧保持完播率的黄金剧作法宝；将宏大的哲学母题分解为每集 60 秒的生死抉择与即时因果反转，既有科幻深度又有商业抓手。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2206",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "《曲率信使》120 集太空硬科幻微短剧：时间膨胀因果律与绝境选择弧光",
        "note": "硬派太空探险题材的情感核爆设计：在光速航行导致的地月时间膨胀背景下，信使在执行跨星系绝密交接中直面文明兴衰与个人孤独的终极撕裂。",
        "so_what": "用硬核物理常识为故事赋予宿命感；真正打动人心的不是花哨的特效，而是角色在不可抗拒的自然规律面前所做出的悲壮决绝与人性升华。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2207",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "编剧技巧",
        "title": "《大院老顽童》现实题材温情短剧：银发族社区喜剧与情感羁绊设计",
        "note": "精准击中全年龄层共情心智的合家欢喜剧范式：聚焦胡同大院退休老人退休后的生活狂想曲，将邻里纷争、代际沟通与老年价值重塑写得妙趣横生。",
        "so_what": "下沉银发赛道的情绪价值提纯；拒绝居高临下的说教，用生活原汁原味的笑点与暖心泪点打磨人情味，是在短剧红海中低成本突围的长青赛道。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2203",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 9. 产品经理 (4)
    {
        "category": "产品经理",
        "title": "未来 3 年，什么样的产品经理不会被淘汰？从功能交付到意图架构",
        "note": "AI 时代产品经理职能重塑的深度复盘：剖析为什么画原型、写 PRD 的传统技能正在贬值，唯有具备全局意图架构与复杂业务抽象能力的人才能立于不败。",
        "so_what": "产品人的生存认知必须全面升维；代码与界面由 Agent 生成已成定局，产品经理的真正价值在于对商业本质的准确翻译与对边缘异常的终极把控。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/class/6484360.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "详细拆解 Pi Agent：产品经理搞懂智能体状态机与行动流的最佳实践",
        "note": "深入浅出拆解顶尖交互智能体的状态机架构：从意图切分、记忆注入策略、短程规划到容错重试机制，全景还原真实生产环境中的 Agent 工程设计。",
        "so_what": "跨越理论与工程落地的必读指南；产品经理如果不懂状态机的状态流转边界与上下文损耗，设计出来的 Agent 产品在面对复杂现实任务时必然瞬间崩溃。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6486194.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "FDE 在硅谷是香饽饽，在国内可能是个坑？前瞻部署工程师岗位冷思考",
        "note": "深度起底大模型交付前线 Forward Deployed Engineer 职能异化：分析中美两地企业数字化成熟度差异对新兴复合型技术产品岗位的不同要求与职业陷阱。",
        "so_what": "盲目照搬硅谷光环往往会陷入交付泥潭；理解国内企业对非标定制与交付边界的特殊诉求，技术产品人在定位自身角色时才能避免沦为高级外包客服。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/pmd/6476320.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "产品经理",
        "title": "AI 时代产品经理竞争力迭代：从方法论执行到商业经营判断力升维",
        "note": "直击数字化产品研发本质的醒脑佳作：当生成式模型让实现任何功能的成本趋近于零时，传统教条式的敏捷迭代与原型方法论迅速贬值，商业经营判断力成为唯一稀缺资产。",
        "so_what": "警惕被“伪需求与虚荣指标”带入自嗨陷阱；不要在低效的堆砌功能上浪费生命，把 80% 的精力花在洞察真实商业因果与终身用户价值上，才是产品人的立足之本。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/pmd/6471544.html",
        "media": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
]

# Verify counts
assert len(items) == 36, f"Expected 36 items, got {len(items)}"
categories = [i["category"] for i in items]
cat_counts = Counter(categories)
print("Categories:", dict(cat_counts))
assert all(v == 4 for v in cat_counts.values()) and len(cat_counts) == 9

# Deduplicate check against all-used-urls.json
used_path = "/Users/gx/.gemini/antigravity/scratch/ai-daily/scripts/all-used-urls.json"
used_urls = set(json.load(open(used_path, "r", encoding="utf-8")))
item_urls = [i["url"] for i in items]
assert len(item_urls) == len(set(item_urls)), "Duplicate URLs within today's issue!"
dups = [u for u in item_urls if u in used_urls]
assert len(dups) == 0, f"Found duplicates in all-used-urls.json: {dups}"

# Write Markdown
target_md = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-10-29.md"

md_lines = [
    "---",
    "date: '2026-10-29'",
    'title: "10 月 29 日 · 长程工程智能体与物理环境闭环：从单点代码生成到全栈自主交付"',
    'highlights: "全网 9 大领域 36 篇高密度精选：谷歌重磅发布 Gemini 4 Carbon 长程工程模型、GitHub Universe 2026 推出多代理端到端交付、PostHog 打造自驾驶 CI 主动巡检修复、红果短剧踩刹车与行业博弈透视、未来 3 年产品经理淘汰分水岭：意图架构师的崛起。"',
    "draft: false",
    'epigraph: "当写代码的边际成本趋近于零，系统工程的架构纪律与意图理解的精准度，便成了决定一切交付成败的唯一标尺。"',
    'lead: "10 月 29 日，全球大模型产业的技术竞争全面迈入「长程复杂任务与全栈端到端交付」的深水区。谷歌重磅发布 Gemini 4 Carbon，将长程工程与安全推演推向前沿巅峰；GitHub Universe 2026 携 Copilot 多代理应用重磅登场，宣告个人英雄主义手工编码时代的落幕与多智能体协同流水线的开启；而在系统运维一线，PostHog 让 CI 具备自驾驶能力，直接从线上数据中主动追查并提交补丁。在应用与商业侧，红果短剧在狂飙之后主动踩下刹车、平衡生态与合规防线，而对于身处风暴眼中的产品经理而言，“功能是答案，问题才是题目”——当功能实现变得轻而易举，唯有穿透虚妄表象、精准定义业务真问题并架构意图流的复合型操盘手，才能在这场工业化巨变中牢牢掌握定义权。"',
    'scene: "「你们引入了这么多自主编码智能体，为什么交付速度反而变慢了？」「因为没有架构纪律的自动化就是失控的灾难。当生成代码毫无门槛时，如果没有严密的沙箱测试、意图状态机与文件锁，十个 Agent 能在十分钟内把主分支改得面目全非。」"',
    "cover: https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80",
    "items:"
]

for it in items:
    md_lines.append(f'  - category: "{it["category"]}"')
    md_lines.append(f'    title: "{it["title"]}"')
    md_lines.append(f'    note: "{it["note"]}"')
    md_lines.append(f'    so_what: "{it["so_what"]}"')
    md_lines.append(f'    source: "{it["source"]}"')
    md_lines.append(f'    url: "{it["url"]}"')
    md_lines.append(f'    media: "{it["media"]}"')
    md_lines.append(f'    pinned: {"true" if it["pinned"] else "false"}')

md_lines.append("---")
md_lines.append("")
md_lines.append("### 岛主今日寄语")
md_lines.append("")
md_lines.append("技术的每一次工业化跃迁，都在以残酷的方式重构生产力与生产关系的平衡。从 GitHub Universe 带来的多代理交付网络，到 PostHog 的自驾驶 CI 闭环，智能体不再是陪聊的玩具，而是深入复杂系统干脏活累活的执飞副驾。这也给所有从业者敲响了警钟：单点技能的熟练度正在迅速贬值，谁能跳出局部细节、拥有统揽全局的架构意图与商业洞察，谁才能在浩荡的技术浪潮中始终把握航向。")

with open(target_md, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Successfully generated {target_md}")

# Append to all-used-urls.json
all_urls = json.load(open(used_path, "r", encoding="utf-8"))
all_urls.extend(item_urls)
with open(used_path, "w", encoding="utf-8") as f:
    json.dump(all_urls, f, ensure_ascii=False, indent=2)

print(f"Updated all-used-urls.json, now contains {len(all_urls)} URLs.")
