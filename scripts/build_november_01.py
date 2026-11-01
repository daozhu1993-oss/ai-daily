# -*- coding: utf-8 -*-
import json
import os
from collections import Counter

items = [
    # 1. AI 资讯 (4)
    {
        "category": "AI 资讯",
        "title": "BootGPT 把极小语言模型塞进可启动扇区：裸机计算极端约束实验",
        "note": "计算机体系结构与大模型的极客跨界实验：在毫无操作系统和驱动支持的裸机 BIOS/UEFI 引导扇区内，塞入极简语言模型推理内核，探索算力极简边界。",
        "so_what": "打破当代 AI 必须依赖厚重操作系统和庞大运行时的思维定势；证明只要具备最基础的指令流转，模型就能作为底层固件运行，为极端环境计算提供灵感。",
        "source": "github.com",
        "url": "https://github.com/kerlenton/bootgpt",
        "media": "https://iandaily.xyz/digest/2026-11-01-bootgpt-c816d1d067f3.jpg",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "Tadpole 逐步记录小模型代理怎样长成：40 亿参数工程演进全景",
        "note": "小参数量智能体微调训练的透明化范本：从基础工具调用循环、轨迹回放测试到强化学习后训练，完整记录 4B 参数模型在特定垂类任务中能力跃迁的度量数据。",
        "so_what": "端侧轻量化智能体落地的务实指南；参数规模不是万能钥匙，系统级的数据配比与针对性训练，完全能让小模型在垂直场景展现媲美百亿巨模型的执行力。",
        "source": "github.com",
        "url": "https://github.com/shakewingo/Tadpole",
        "media": "https://iandaily.xyz/digest/2026-11-01-tadpole-a1db258d99f2.jpg",
        "pinned": True,
    },
    {
        "category": "AI 资讯",
        "title": "KuralHub 披露全球多语种情绪语音数据缺口：非对称语料生态现状",
        "note": "语音大模型前沿研究的冷峻透视：全面普查全球 70 种主要语言，发现 25 种语言在自然细腻的情绪语音标注上完全空白，语料贫瘠正在加剧模型文化的单极化。",
        "so_what": "多模态语音交互全球化落地的核心暗礁；没有高质量、具备丰富情感张力的一手原生语料，再高深的算法也无法跨越跨文化多语种交互的语境鸿沟。",
        "source": "aaivu.github.io",
        "url": "https://aaivu.github.io/KuralHub/datasets.html",
        "media": "https://iandaily.xyz/digest/2026-11-01-kuralhub-22707b0e68bb.jpg",
        "pinned": False,
    },
    {
        "category": "AI 资讯",
        "title": "Wiz 深度汇总 9 个 AI 开发平台安全事件：黑十月凭据泄露警示录",
        "note": "云原生安全权威机构的重磅报告：复盘近期主流 AI 平台在多租户环境、提示词反向注入、凭据侧漏与跨项目执行沙箱逃逸中的典型漏洞攻击路径。",
        "so_what": "给盲目接入各种 AI 工具的企业敲响安全警钟；追求开发效率绝不能以牺牲隔离防线为代价，建立基于最小权限和动态凭据网关的风控体系迫在眉睫。",
        "source": "wiz.io",
        "url": "https://www.wiz.io/blog/black-october-for-ai-developer-platforms",
        "media": "https://iandaily.xyz/digest/2026-11-01-wiz-120482e4bbe3.jpg",
        "pinned": False,
    },

    # 2. AI 协作 (4)
    {
        "category": "AI 协作",
        "title": "Clawdline 跨电脑聚合分散编码会话：全平台智能体状态看板",
        "note": "解决多设备高频结对编程痛点的统一收纳器：跨机器追踪 Claude Code 与 Codex 终端进程，将运行中、等待人工输入与已完成任务归拢至单一仪表盘。",
        "so_what": "大幅消除在多台工位机与云端开发机之间来回切换的认知摩擦；让工程师对并发执行的多个长程重构任务保持全局态势感知，从容掌控异步产出节奏。",
        "source": "clawdline.com",
        "url": "https://clawdline.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-clawdline-c877a45fdf4f.jpg",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "Enclyra 用本地小模型操作 Mac 桌面：端侧离线高隐私自动化",
        "note": "无惧云端网络抖动与数据外泄的桌面 Agent 方案：完全依托本机神经算力解析屏幕截图与文档上下文，自动执行跨应用繁琐报表填报与文件归档。",
        "so_what": "高敏感行业（金融、法务、医疗）拥抱智能体自动化的破局点；在不上传哪怕一个像素的前提下实现桌面自主巡航，兼顾极致数据主权与自动化生产力。",
        "source": "enclyralabs.com",
        "url": "https://www.enclyralabs.com",
        "media": "https://iandaily.xyz/digest/2026-11-01-enclyra-1dfdb2dd1d66.jpg",
        "pinned": True,
    },
    {
        "category": "AI 协作",
        "title": "Fastbrowse 为网页操作留下可核对结果：带证据链的自主浏览",
        "note": "高可靠性网络爬取与表单填报执行流：智能体在完成跨页面数据提取与操作后，自动截取目标段落原始文字与操作时间戳作为防幻觉证据附在结论末尾。",
        "so_what": "终结自动化执行中的“黑箱盲信”隐患；让人类审阅者在几秒内对照证据链完成真伪核验，大幅提升多步复杂流程在严肃业务环境下的采信度。",
        "source": "fastbrowse.ai",
        "url": "https://www.fastbrowse.ai/",
        "media": "https://iandaily.xyz/digest/2026-11-01-fastbrowse-af2c3920dd7f.jpg",
        "pinned": False,
    },
    {
        "category": "AI 协作",
        "title": "Archwhere 把智能体改动放回架构地图：可视化防止系统架构退化",
        "note": "大型遗留代码库协同重构利器：将 Agent 提交的每一个 Pull Request 与任务切片，动态映射到全系统微服务依赖拓扑图上，红色标出对核心公共库的潜在侵蚀。",
        "so_what": "智能体时代架构师捍卫系统整洁度的坚固盾牌；防止 AI 盲目局部最优而破坏全局架构契约，让代码修改与系统边界定义在物理拓扑上协同演进。",
        "source": "github.com",
        "url": "https://github.com/tapaskar/archwhere",
        "media": "https://iandaily.xyz/digest/2026-11-01-archwhere-9ef998db5da9.jpg",
        "pinned": False,
    },

    # 3. 一人公司 (4)
    {
        "category": "一人公司",
        "title": "Subfaro 不连银行也能管理全网订阅：零隐私焦虑的财务小管家",
        "note": "克制而高雅的个人订阅跟踪工具：坚决不向任何第三方金融机构索取银行接口权限，靠极简录入与智能账期推算，清晰呈现年化固定支出与暴涨预警。",
        "so_what": "小而美工具赢得尊重的典范；在人人试图过度抓取用户敏感数据的时代，主动划清边界、把控制权完全留给用户，反而能在付费市场赢得稳固信赖。",
        "source": "subfaro.com",
        "url": "https://subfaro.com/en/",
        "media": "https://iandaily.xyz/digest/2026-11-01-subfaro-0d24c2cc3bc8.jpg",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "ClassicalBot 为古典乐演出开放结构化接口：长尾文化数据的独立变现",
        "note": "深耕高雅艺术小众赛道的独立数据工程：自动化聚合全球主流音乐厅、交响乐团与演奏大师的演出日程，清洗为对开发者极度友好的标准化 JSON API。",
        "so_what": "单兵开发者挖掘非标垂直数据金矿的绝佳样本；大厂不屑于做脏活累活的长尾领域，往往蕴藏着极高黏性与高净值受众，足以支撑健康的个人商业循环。",
        "source": "classicalbot.com",
        "url": "https://classicalbot.com/api/docs",
        "media": "https://iandaily.xyz/digest/2026-11-01-classicalbot-c37bd4363fb0.jpg",
        "pinned": True,
    },
    {
        "category": "一人公司",
        "title": "UPC 标签工具盯住精准打印尺寸：物理一比一输出的极致工具",
        "note": "解决跨境电商卖家真实痛点的微型 SaaS：摒弃任何花哨功能，严格按照 PostScript 物理点数排版条码，完美适配 Avery 标签纸与亚马逊 FBA 严苛标准。",
        "so_what": "把单一功能做到极致零误差的商业力量；跨境卖家痛恨因打印轻微偏移导致的退货惩罚，用极高确定性解决痛点，哪怕单一页面也能稳定收割全球订单。",
        "source": "upclabelmaker.com",
        "url": "https://upclabelmaker.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-upclabelmaker-d3bf6402d6ad.jpg",
        "pinned": False,
    },
    {
        "category": "一人公司",
        "title": "Joshternet 用纯文本声明串起独立网站：去中心化重温早期互联网温情",
        "note": "独立博客圈的文艺复兴协议：只需在自己域名根目录下放置一份简单的文本清单，就能自动加入志同道合的独立站长互联网络，重温没有算法绑架的冲浪时代。",
        "so_what": "在被封闭社交平台垄断的今天守护独立意志；不依赖中心化大厂平台推荐，靠协议自发编织个人数字领地，展现一人公司创作者对开放互联网的精神坚守。",
        "source": "joshternet.org",
        "url": "https://joshternet.org/",
        "media": "https://iandaily.xyz/digest/2026-11-01-joshternet-92dd1ba974df.jpg",
        "pinned": False,
    },

    # 4. 产品设计 (4)
    {
        "category": "产品设计",
        "title": "BBRouter 在三维面包板上搭建电脑：可交互硬件电路仿真艺术",
        "note": "硬核计算机教育交互界面的封神之作：将经典 8 位计算机的每一枚芯片、跳线、时钟与指示灯放入可 360 度自由旋转的三维空间，支持逐脉冲单步单调执行。",
        "so_what": "把抽象晦涩的底层逻辑转化为物理级可感体验的极致示范；好的产品设计能让使用者在指尖拖动连线中瞬间顿悟计算的真谛，兼具学术价值与极客美学。",
        "source": "bbrouter.com",
        "url": "https://bbrouter.com/bbrouter/ben-eater-sap-1",
        "media": "https://iandaily.xyz/digest/2026-11-01-bbrouter-a924ae9aa97c.jpg",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "CiteLLM 让问答结果直接回到 PDF 原句：消除幻觉的锚点交互",
        "note": "学术与严肃文档阅读交互的精准重构：大模型回答中的每一个数据与论断均携带精准可点击锚点，点击瞬间右侧 PDF 自动平滑滚动并黄色高亮对应段落原句。",
        "so_what": "重建人机信任的关键微体验设计；告别“大模型一本正经胡说八道却无从查证”的焦虑，用原汁原味的上下文溯源，将 AI 真正驯化为经得起推敲的科研助手。",
        "source": "citellm.com",
        "url": "https://citellm.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-citellm-6d257774f78b.jpg",
        "pinned": True,
    },
    {
        "category": "产品设计",
        "title": "Jointter 把猜词变成点线网络拼图：多感官几何文字益智游戏",
        "note": "极具新意的新型文字游戏交互机制：字母分散隐藏在弹性连接线构成的拓扑节点中，用户通过拖拽重组点位、感知连线张力来推导隐藏单词，兼具触觉与智力乐趣。",
        "so_what": "用几何直觉重构传统枯燥文字玩法的绝妙思路；跳出 Wordle 矩阵填色的既有窠臼，将图论拓扑与词汇联想融为一体，带来令人耳目一新的沉浸手感。",
        "source": "jointter.com",
        "url": "https://www.jointter.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-jointter-d116fb8df3db.jpg",
        "pinned": False,
    },
    {
        "category": "产品设计",
        "title": "Woodshed 给乐器练习录音打上进度熟练度：专注音乐心流的极简工作流",
        "note": "专为器乐演奏者打磨的录音复盘工具：一键随手录下断断续续的练习，按曲目动机智能拆解并支持五档熟练度标记，随时与上周甚至上个月的版本并排回听。",
        "so_what": "真正懂垂直专业人群心智模型的工具典范；不搞花哨的调音器和社区社交，把全部交互克制在“录下、标记、比对成长”的微小闭环中，带来极强心理奖赏。",
        "source": "getwoodshed.com",
        "url": "https://getwoodshed.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-woodshed-58902daeae10.jpg",
        "pinned": False,
    },

    # 5. 审美提升 (4)
    {
        "category": "审美提升",
        "title": "WOLOLOW 2.0 把太空屋缩成床头灯：1960 年代太空未来主义的当代凝视",
        "note": "工业设计致敬经典建筑的惊艳之作：精准借用 1968 年芬兰经典 Futuro 椭圆飞碟屋建筑轮廓，通过高光镜面金属表皮与环形舷窗漫反射，将时代先锋感凝固在床头。",
        "so_what": "跨越半个世纪的复古未来主义美学唤醒；经典设计之所以永恒，在于其蕴含的对未知宇宙的纯粹好奇与浪漫，用考究的比例与材质让日常器物拥有建筑般的尊严。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/design/wololow-2-0-1960s-space-age-architecture-elliptical-bedside-light-arthur-koshatahyan-kostya-trunov/",
        "media": "https://iandaily.xyz/digest/2026-11-01-wololow-e48bc7eac0dc.jpg",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Peiyang Li 编织竹椅铺满发光钩织花：刚韧与柔软的暗夜诗意对话",
        "note": "当代先锋手工艺与材料实验力作：以传统中国手工劈篾竹编构成刚硬骨架，上方繁密缝缀由紫外线反应特殊纱线钩织的花卉簇群，在黑夜中绽放出梦幻幽光。",
        "so_what": "打破传统家具功能主义单一维度的艺术跃迁；材料刚与柔的激烈冲突、白昼自然温润与暗夜荧光异化的戏剧张力，赋予静止物体强烈的生命体仪式感。",
        "source": "designboom.com",
        "url": "https://www.designboom.com/design/woven-bamboo-armchair-uv-reactive-crocheted-blooms-dark-peiyang-camille-li/",
        "media": "https://iandaily.xyz/digest/2026-11-01-blooms-abd6cc86a797.jpg",
        "pinned": True,
    },
    {
        "category": "审美提升",
        "title": "Em-Estudio 墨西哥城地下酒吧：以二手旧书店为封面雕琢沉浸街景",
        "note": "藏匿在繁华街区背后的空间叙事魔术：入口伪装成破旧温暖的二手旧书店，推开隐蔽书架转角步入地下空间，质朴原木书墙与昏暗聚光交织出如梦似幻的淘书节奏。",
        "so_what": "商业空间体验主题化与情绪代入的顶级范本；物理边界的转换就是心理状态的解压阀，通过书香与醇酒的意象通感，在喧嚣都市中打造能安顿精神的地下庇护所。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/10/31/libreria-valladolid-mexico-city-bar-em-estudio/",
        "media": "https://iandaily.xyz/digest/2026-11-01-libreria-8fd25dfee3cf.jpg",
        "pinned": False,
    },
    {
        "category": "审美提升",
        "title": "O’Sullivan Skoufoglou 伦敦花园工作室：用低矮红砖基座托起通透木构画框",
        "note": "英国私家花园庭院微建筑的典雅实践：以沉稳质朴的低矮红砖基托起全景实木大开窗框架，室内工作台完全向绿意盎然的庭院尽头敞开，消解建筑与自然隔阂。",
        "so_what": "用克制的几何尺度重塑生活与创造空间的连接；不需要宏伟的大体量，几道考究的木线条与窗外摇曳的树影，便能让每天的伏案创作成为一种融入自然的享受。",
        "source": "dezeen.com",
        "url": "https://www.dezeen.com/2026/10/31/osullivan-skoufoglou-architects-garden-studio/",
        "media": "https://iandaily.xyz/digest/2026-11-01-gardenstudio-1cabba1de736.jpg",
        "pinned": False,
    },

    # 6. 产品营销 (4)
    {
        "category": "产品营销",
        "title": "Publishub 预测分析短视频观众流失秒数：让每一刀剪辑都有数据归因",
        "note": "短视频工业化内容诊断前沿产品：创作者在发布前上传初剪样片，系统通过视觉节拍与语义注意力模型，精确指出前 3 秒或反转处可能导致滑走的具体秒数。",
        "so_what": "从“玄学凭感觉剪辑”走向“确定性数据把关”的生产力跃迁；在算法平台极度挑剔的完播率考核下，发布前排查掉哪怕一个流失断点，就能撬动指数级的自然流量推荐。",
        "source": "getpublishub.com",
        "url": "https://www.getpublishub.com",
        "media": "https://iandaily.xyz/digest/2026-11-01-publishub-905e89ac3757.jpg",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "Yoga Write Code 从官网业务推导高转化选题：业务导向的精准内容增长",
        "note": "反常识的内容营销生成工具：坚决拒绝堆砌没有商业价值的泛流量热词，先深度逆向解析企业官网的核心商业模式，再生成紧密挂钩成单意向的深度专业文章大纲。",
        "so_what": "戳穿“自嗨式虚荣阅读量”的营销照妖镜；带来 10 万个无关路人，不如吸引 10 个真正有采购决策权的企业关键人，以业务转化闭环为唯一尺标打磨内容。",
        "source": "yogawritecode.com",
        "url": "https://yogawritecode.com",
        "media": "https://iandaily.xyz/digest/2026-11-01-yogawritecode-169453a13b32.jpg",
        "pinned": True,
    },
    {
        "category": "产品营销",
        "title": "No moat 把微型软件发现做成细分目录：不吹泡沫的透明化分发公约",
        "note": "独立软件出海领域的清流分发平台：严格按照真实使用场景、受众规模与收费模式建立细分归类，将创始人公开验证过的 ARR 与真实运行年限作为核心衡量维度。",
        "so_what": "对抗投机套壳软件泡沫的良心阵地；让真正脚踏实地解决痛点的单兵工具摆脱刷榜黑客的碾压，依靠透明口碑获得稳定的长尾精准自然流量。",
        "source": "nomoat.app",
        "url": "https://nomoat.app/",
        "media": "https://iandaily.xyz/digest/2026-11-01-nomoat-c298528678e8.jpg",
        "pinned": False,
    },
    {
        "category": "产品营销",
        "title": "Galleris 让画廊标签直连艺术家原声：极简扫码重构高客单艺术品询盘",
        "note": "艺术展览与藏家沟通链路的高效重构：观众在展签旁扫码即可收听艺术家创作时的亲口自述与高清细节解读，有意向者一键拉起即时通讯，极大缩短联络链路。",
        "so_what": "高客单非标商品信任转化的精巧设计；消除传统画廊高高在上的冰冷距离感，用创作者最真挚的声音打破心智防线，让每一次驻足凝视都有机会沉淀为私域高净值客户。",
        "source": "gallerismuseum.com",
        "url": "https://www.gallerismuseum.com/",
        "media": "https://iandaily.xyz/digest/2026-11-01-galleris-598c4c2450a6.jpg",
        "pinned": False,
    },

    # 7. AI 漫剧 (4)
    {
        "category": "AI 漫剧",
        "title": "60 亿播放漫剧赚不到 100 万：微短剧 ROI 倒挂与商业变现困局深度复盘",
        "note": "揭开微短剧虚假繁荣背后的残酷财务真相：抽丝剥茧拆解天量播放量背后高达 85% 以上的买量投流成本、平台通道费剥削与创作者微薄分账的真实泥潭。",
        "so_what": "盲目狂热入局者的当头棒喝；单纯追求播放量数字的虚荣游戏已经破产，唯有跑通高复购私域沉淀、衍生品变现与极致视听生成降本，短剧团队才能拥有真利润。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487447.html",
        "media": "https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "短剧重回小程序：绿泡泡社交打法改写了谁的赚钱公式？",
        "note": "微短剧分发生态重归私域阵地的重大转向：面对独立 App 买量成本居高不下的现实，各大制片方重返微信小程序生态，依托朋友圈裂变与公众号社群降低获客摩擦。",
        "so_what": "流量红利见底后的渠道战术理性回归；搞懂熟人社交圈层的病毒式自发裂变与即开即看的轻量体验，是中小微制作团队在巨头夹缝中守住利润率的关键命门。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/operate/6487378.html",
        "media": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "AI 漫剧",
        "title": "一刷起来至少两小时：全网戒不掉的红果短剧为什么反倒害怕“被捧杀”",
        "note": "透视微短剧巨头在用户沉迷与监管红线之间的走钢丝博弈：剖析高密度多巴胺刺激机制如何引发公众对大众精神健康的担忧，以及平台主动限流合规的深层考量。",
        "so_what": "内容产品的长期主义生死防线；极致的情绪操控虽然能换来短期惊人的用户时长，但若缺乏社会价值与文化厚度，随时可能在监管铁拳与大众反噬下一夕倾覆。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/it/6486814.html",
        "media": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "AI 漫剧",
        "title": "消耗中国算力一半？马斯克、范德彪 AI 二创爆火背后的视听裂变密码",
        "note": "现象级全民生成式视听狂欢的深度文化解剖：从搞笑对白音色替换、跨文化身份拼贴到草根模因病毒传播，解析生成式视听工具如何引爆大众创作者的表达欲。",
        "so_what": "视听消费从“精英单向投喂”向“大众参与式狂欢”的质变；幽默、解构与强烈情绪共鸣是穿透算法流量的最强武器，为漫剧创作者提供了取之不尽的网感养料。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6486531.html",
        "media": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 8. 编剧技巧 (4)
    {
        "category": "编剧技巧",
        "title": "《修仙逆天改命》120 集微短剧：废柴逆袭与升级流戏剧节拍深度拆解",
        "note": "经典男频玄幻仙侠短剧的节奏控制黄金准则：从宗门受辱、偶得金手指机缘到宗门大比连环打脸，严格以每集 60 秒为单位设置微型危机反转，步步为营。",
        "so_what": "升级流类型片经久不衰的底层逻辑；受众追求的从不是虚幻的仙侠世界，而是每一次艰苦付出都能得到即时、明确、无可争议的能力暴涨与社会地位承认的快感。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2212",
        "media": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "《闪婚娇妻有点甜》120 集甜宠短剧：先婚后爱与多重马甲反转节拍编排",
        "note": "下沉女频爆款情感短剧的心理投射技巧：被迫协议结婚的底层平凡灰姑娘，在日常相处中逐步展露神医、顶级黑客等惊人马甲，让冷酷霸总彻底沦陷折服。",
        "so_what": "紧扣女性观众隐秘自尊补偿的剧作法宝；多重马甲不仅是情节反转的推进器，更是打破门第悬殊阶层壁垒、实现势均力敌爱情幻想的最强戏剧支撑。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2213",
        "media": "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "编剧技巧",
        "title": "《鉴宝捡漏天王》120 集都市鉴宝短剧：知识博弈与反向打脸爽感设计",
        "note": "都市鉴宝类型短剧的专业性塑造：利用古玩市场潘家园的暗语规矩、真假瓷器断代与微观开片细节，将骗局设局与反向收割编织成步步惊心的智力交锋。",
        "so_what": "行业题材规避低智狗血的有效手段；让打脸建立在扎实可信的专业文物常识与历史典故之上，既满足了观众猎奇心理，又极大提升了全剧的质感档次。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2215",
        "media": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "编剧技巧",
        "title": "《星舰农民》120 集星际种田短剧：硬核太空开荒与生存因果链构建",
        "note": "微短剧少见的硬科幻与种田奇妙融合：退役星舰老兵在贫瘠的外星荒原殖民地开垦农田，运用封闭生态循环、水质提纯与水培生化科技，抵御宇宙风暴与星际海盗。",
        "so_what": "将宏大冰冷的科幻题材拉回土地生活烟火气的剧作典范；用最朴素的粮食种植抵抗星际虚无，给习惯了打打杀杀的观众带来无与伦比的安全感与治愈力。",
        "source": "wzbj1616.com",
        "url": "https://www.wzbj1616.com/script_info/2216",
        "media": "https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },

    # 9. 产品经理 (4)
    {
        "category": "产品经理",
        "title": "实测灵光 2.0：对标 Muse 背后，中美 Personal Agent 底层逻辑的本质分歧",
        "note": "顶尖个人智能体产品的深度横评思考：深入剖析美国产品聚焦单点深度专业交付与 API 组合拳，而国内产品更侧重全流程保姆级陪伴与微信生态连接的战略差异。",
        "so_what": "产品经理对抗盲目崇拜海外竞品的清醒标尺；软件不仅是代码逻辑，更是特定文化土壤下用户生活方式的投射，尊重本土工作流习惯才能做出国民级应用。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/evaluating/6487428.html",
        "media": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "详解 Super Agent 交互设计：不仅要会主动干活，更要懂得何时闭嘴",
        "note": "新一代主动型智能体的交互克制哲学：探讨主动推送代办任务、后台静默执行与打扰人类阈值的动态平衡算法，告别啰嗦无聊的对话框刷屏灾难。",
        "so_what": "高级产品经理对人机交互边界的深刻理解；真正优秀的私人管家从不大呼小叫邀功，而是在关键节点默默铺平道路，不过度消耗用户有限的注意力带宽。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487459.html",
        "media": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80",
        "pinned": True,
    },
    {
        "category": "产品经理",
        "title": "从 Agent 开发平台到 AI 团队工作台：扣子的三次战略转向与结构性约束",
        "note": "头部大模型应用搭建平台的系统级演进复盘：深度拆解其从人人可用的轻量 Bot 玩具，转型为支持多角色协作、权限审批与企业系统对接的工作台历程。",
        "so_what": "工具型平台拓展商业天花板的必经之役；当 C 端尝鲜热潮退去，唯有沉入企业真实复杂的协作链条中做重做深，才能将短暂的流量转化为稳固的订阅营收。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/evaluating/6486885.html",
        "media": "https://images.unsplash.com/photo-1556761175-5973dc0f32e7?w=800&auto=format&fit=crop&q=80",
        "pinned": False,
    },
    {
        "category": "产品经理",
        "title": "当 AI 开始替用户搜索与推荐决策：企业获客与产品呈现逻辑的历史级剧变",
        "note": "人机中介时代的商业获客范式转移：探讨当最终消费者不再逐条浏览搜索结果列表、而是完全听从个人智能体的提炼推荐时，产品经理应如何重新设计产品信息架构。",
        "so_what": "未来三年每一个数字化产品操盘手面临的终极命题；不仅要面向人类眼球设计界面，更要面向机器解析引擎（Agent API）结构化输出产品核心价值与可信凭证。",
        "source": "woshipm.com",
        "url": "https://www.woshipm.com/ai/6487433.html",
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
target_md = "/Users/gx/.gemini/antigravity/scratch/ai-daily/src/content/daily/2026-11-01.md"

md_lines = [
    "---",
    "date: '2026-11-01'",
    'title: "11 月 01 日 · 裸机极简自举与人机交互克制：从虚荣数据狂欢到商业本质回归"',
    'highlights: "全网 9 大领域 36 篇高密度精选：BootGPT 把语言模型塞进可启动引导扇区、Clawdline 跨电脑聚合多编码会话、实测灵光 2.0 剖析中美个人代理底层分歧、60 亿播放漫剧赚不到百万：短剧 ROI 倒挂大解剖、Super Agent 交互设计：不仅会干活更懂何时闭嘴。"',
    "draft: false",
    'epigraph: "最高级的智能不是无休止的啰嗦打扰，而是在关键节点默默铺平道路；最好的商业不是天量播放的自嗨，而是扣除一切投流成本后稳稳落袋的真金白银。"',
    'lead: "11 月 1 日，十一月的开篇见证了全球人工智能与数字化创作生态对“本质”的深情回望。在最底层的极客世界，开发者们尝试将极小语言模型直接写入裸机启动扇区，用极度严苛的约束重新审视算力的纯粹；在开发者协同前沿，Clawdline 与 Fastbrowse 致力于将分散各处的智能体会话收拢至统一证据链中，解决异步执行的黑箱盲信；在视听与漫剧战场，行业终于撕下了天量播放量的遮羞布——60 亿播放赚不到 100 万的残酷现实，倒逼团队全面转战私域裂变与低成本工业化管线；而在智能体交互与产品落地的最高维度，优秀的产品经理正在学会让 AI“懂得何时闭嘴”，在中美不同工作流土壤中寻找差异化生长的确定性。泡沫正在被刺破，务实的创造者正在接过时代的接力棒。"',
    'scene: "「你们的智能体每天主动给我推送三千条工作进展，我光点已读就快疯了，这叫解放生产力？」「真正的秘书从来不会把所有草稿都端给你看。它应该在后台把脏活干完，只在需要你签字画押时递上一杯温咖啡和两行结论。」"',
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
md_lines.append("十一月的第一天，整个行业都在用最真实的教训教会我们克制。无论是把模型写进引导扇区的极客探索，还是对微短剧天量播放却陷入亏损的深刻反思，亦或是智能体设计中对人类注意力边界的敬畏，无一不在印证那个朴素的商业铁律——脱离了真实客户价值与健康财务模型的繁荣，终究只是一场脆弱的数字幻影。克制你的表达欲，打磨你的核心护城河，少看虚荣的指标，多做真正能为用户省下时间、创造利润的实事。")

with open(target_md, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Successfully generated {target_md}")

# Append to all-used-urls.json
all_urls = json.load(open(used_path, "r", encoding="utf-8"))
all_urls.extend(item_urls)
with open(used_path, "w", encoding="utf-8") as f:
    json.dump(all_urls, f, ensure_ascii=False, indent=2)

print(f"Updated all-used-urls.json, now contains {len(all_urls)} URLs.")
