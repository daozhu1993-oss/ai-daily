import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-07': {
        'title': '10 月 7 日 · 节后开局与系统收敛：当人人都是 PM，核心竞争力在于意图定义',
        'highlights': '全网 9 大领域 36 篇高密度精选：Anthropic 重申人人都是产品经理、IP-Adapter 保持漫剧角色高保真、奥斯卡提名背后的剧作母题、AI 社交出海产品变现分化、Claude Code 升级模块化 Mods 能力。',
        'epigraph': '代码和画面的生成门槛降得越低，系统意图与业务边界的定义就越昂贵；当任何人都能用自然语言调度工具，真正的胜负手不在于你敲了多少行提示词，而在于你是否拥有击穿本质的产品判断力。',
        'lead': '节后首个工作日，技术演进与职场叙事迎来了一个极具戏剧性的倒挂：一年前全网还在唱衰“产品经理将被大模型淘汰”，一年后 Anthropic 核心团队却公开宣称——在自主智能体时代，“人人都必须学会当产品经理”，因为越是强大的机器执行力，越依赖精准的意图定义与边界治理；在漫剧与视听工业一线，腾讯 AI Lab 的 IP-Adapter 等技术将跨镜头的角色一致性推向实用巅峰，而海外 47 款 AI 社交产品的变现对比更给出了冰冷启示——月活差 5 倍的产品收入却完全持平，单靠流量早已失效，商业模式与垂直留存决定生死；在编剧与内容端，奥斯卡提名作品的戏剧结构再次证明，无论视效工具如何日新月异，触及人类普世情感困境与坚硬因果的主题，永远是作品长红的唯一密码。开工第一天，收敛意图，重塑核心壁垒。',
        'scene': '「节后第一天，团队都在讨论 Claude Code 升级了 Mods，我们是不是不需要招那么多初级程序员了？」「何止程序员，连初级 PM 都不够用了。现在需要的是能把业务因果想透、一眼看出模型逻辑破绽的全栈操盘手。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''节后的第一个工作日，假期里的松弛感瞬间被现实的节奏拉回。

很多朋友开工第一天就在焦虑：技术变化这么快，大厂天天发新工具，我们到底该学什么、做什么才不会被淘汰？

今天 Anthropic 的最新研判给出了最清醒的答案：**当技术执行的门槛趋近于零，思考与定义的门槛就升到了最高。**

一个优秀的造物主，在这个时代最重要的能力不是会写复杂的 Prompt，而是这三点：
1. **辨别真伪的嗅觉**：像拆解 47 个 AI 社交产品那样，一眼看穿“虚荣流量”与“真实付费”之间的鸿沟，不做无效自嗨。
2. **定义边界的定力**：给系统划定明确的输入输出约束，不让智能体在无序的上下文中裸奔。
3. **触碰人性的共鸣**：无论工具生成的多么逼真，真正能让用户或观众停留的，永远是那份有因有果、有痛有爱的人性温度。

第四季度已经正式拉开大幕。收拾好心情，扎扎实实打好属于你自己的战役！''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'IP-Adapter 开源跨镜头与风格保持技术：漫剧分镜角色零微调特征高度统一',
                'note': '腾讯 AI Lab 重磅图像提示适配器：解耦交叉注意力机制，无需对角色进行繁琐的 LoRA 微调，仅凭单张参考图即可在多变光影和复杂分镜中保持面部五官与服饰细节不走样。',
                'so_what': '解决了漫剧连贯生产的最大痛点；跨镜头特征一致性的大幅提升，使多格动漫与条漫的制作效率实现数十倍跃升。',
                'source': 'github.com',
                'url': 'https://github.com/tencent-ailab/IP-Adapter',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'AnimateDiff 文本驱动动画开源管线：低成本生成高质量漫剧连续动态与微表情',
                'note': '个性化动画扩散模型领跑者：在既有文本转图像模型基础上无缝插入运动建模模块，使原本静态的漫剧分镜能够自然呼吸、眨眼并完成细腻的戏剧动作过渡。',
                'so_what': '打破了静态漫画与动态漫之间的技术鸿沟；小型团队甚至个人创作者也能单机跑出番剧级的动态过场。',
                'source': 'github.com',
                'url': 'https://github.com/guoyww/AnimateDiff',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '悬在 Muse 头上的剑：数字人与 AI 漫剧生成版权博弈、素材清洗与合规防线',
                'note': '前沿内容法理深度探讨：拆解爆款生成工具在训练集版权、肖像授权以及生成产物归属上的潜在法律暗礁，梳理制作方在商业化前夕必须完成的合规尽调要点。',
                'so_what': '合规是漫剧商业化的生命线；在早期就建立干净的原创授权素材库，才能避免在作品爆火后遭遇灾难性的版权诉讼。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473510.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': 'TripoSR 超快单图 3D 重建：漫剧道具、建筑与场景资产秒级生成与空间摆放',
                'note': '前沿 3D 快速生成管线开源：单张物品照片在半秒内即可重构成高精度的 3D 网格模型，方便漫剧主创将其直接拖入三维场景中自由调整机位透视与分镜构图。',
                'so_what': '空间透视难题迎刃而解；借助快速 3D 资产辅助搭建场景，漫剧分镜的景深感与运镜自由度获得了质的飞跃。',
                'source': 'github.com',
                'url': 'https://github.com/VAST-AI-Research/TripoSR',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '第 98 届奥斯卡提名作品揭晓：类型片母题演进与剧作冲突深层解构',
                'note': '全球殿堂级影视剧作复盘：深度对照入围最佳原创与改编剧本的顶尖范本，解析名家如何在经典三幕剧框架中通过反常规的人物弧光打破套路，激发全球受众共鸣。',
                'so_what': '类型片不是八股文，而是共情公约数；在熟悉的类型安全感中注入意料之外的人物抉择，是最高级的编剧艺术。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/868',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '重大题材电视剧《古田之路》立项公示：历史转折点的人物抉择与信仰弧光编织',
                'note': '权威立项案例剖析：展示如何在重大历史决策的缝隙中发掘真实人性的困惑与争论，通过思想交锋而非空洞口号生动展现历史发展的必然规律。',
                'so_what': '写重大题材最怕人物扁平化；把英雄还原为有血有肉、有痛苦有坚持的普通人，故事才具备震撼人心的力量。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/857',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '广电重点微短剧规划备案公示：剧情反转合规与主流价值导向审读细则解析',
                'note': '立项审读要点最新梳理：严控恶意制造阶层对立、拜金主义与虚无主义的情节反转，大力倡导在戏剧张力中融入普通人通过双手拼搏改变命运的温情底色。',
                'so_what': '反转只是手段，立意才是灵魂；紧扣合规导向设计巧妙的因果闭环，既能确保立项无忧，也能打出有口碑的长线爆款。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/864',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '电影剧本（梗概）备案立项公示：类型片剧情钩子与核心悬念布局技巧实操',
                'note': '备案过审优秀梗概精析：如何在开篇 300 字内交代清主角无法逃避的生死困境，并通过层层加码的对抗力量让悬念一直紧绷到最终决战时刻。',
                'so_what': '好的故事钩子就像倒计时的炸弹；把导火索点燃在观众眼前，他们才愿意一路跟随你屏息凝神到最后一秒。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/856',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '一年前说 PM 会被淘汰，现在 Anthropic 却说：人人都得学会当产品经理',
                'note': 'AI 巨头组织哲学重磅逆转：随着工程师利用 AI 编写代码的速度提升数倍，技术执行门槛骤降，理解业务上下文、定义问题本质与权衡取舍的“PM 思维”成为全员最紧缺的底层能力。',
                'so_what': '岗位名称可能会变，但产品思维永不贬值；谁能想透真实世界的需求边界与价值交付，谁就是智能时代的主导者。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6473402.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '盘点 47 个 AI 社交出海产品：月活差近 5 倍收入却持平，穿透伪增长的商业本质',
                'note': '海外商业化万字深度复盘：对比分析数十款 AI 角色与陪伴产品，揭示高月活并不等于高收入，那些能够针对高净值垂直群体打造深层情感黏性与高客单订阅的产品拥有惊人的暴利。',
                'so_what': '停止盲目追求虚荣的 DAU 规模；做深垂直黏性、拉高客单价与 LTV，一人小团队也能在海外闷声发大财。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473416.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'Claude Code 最新版更新 Mods 模块化能力：致敬开源架构与自动化调度演进',
                'note': '顶级开发助手重构扩展机制：引入高度灵活的插件化 Mods 机制，支持开发者为本地终端 Agent 自定义安装调试工具、环境监视器与审查规则，实现极强的可组装性。',
                'so_what': '模块化与解耦是复杂系统抗击熵增的唯一法则；把大模型装进可拔插的工程管道，才能打造出经久耐用的工具流。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473496.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': 'MiniMax M3.1 深度实测：国产前沿基座敢跟顶配 Opus 掰手腕的工程底气',
                'note': '硬核评测全景展现：全面测试国产大模型在复杂多轮代码生成、长文本因果推演与工业 API 调度中的实战表现，展现了在大算力限制下极高的数据质量调优水准。',
                'so_what': '追赶的步伐超乎想象；学会敏锐评估不同基座模型的性价比与任务强项，按需混合调度是当下最明智的架构策略。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/evaluating/6473382.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    },

    '2026-10-08': {
        'title': '10 月 8 日 · 模块化调度与真实调研：用严谨边界穿透信息茧房',
        'highlights': '全网 9 大领域 36 篇高密度精选：从小红书竞品到行业调研实测、腾讯元宝加入个人 Agent 战场、TripoSR 场景 3D 重建、电视剧中国 1927 立项、ChatGPT Dot 评测与端侧轻量视觉骨干网络。',
        'epigraph': '工具的进化没有消灭思考，而是严酷地惩罚了懒惰的思维；当你把调研交给 AI 时，得到的可能只是一份看似完美的幻觉，唯有带上挑剔的判断力深入业务泥潭，才能捞出带血的商业真相。',
        'lead': '10 月 8 日的行业视野，正聚焦于如何用严谨的工具与清醒的调研穿透数据迷雾。在产品研究一线，一线从业者完整披露了借助大模型进行竞品拆解与行业调研的实战得失——如果缺乏对一手业务逻辑的挑剔质询，模型输出的报告只会把团队引入充满逻辑破绽的信息茧房；在多智能体生态端，腾讯元宝等国民级入口全面杀入个人常驻 Agent 战局，而 Claude Code 与 Cursor 对插件式 Mods 与后台协同的探索，正加速将个人开发者的单机环境打造成全自主软件车间；在影视剧本与漫剧工业端，重大革命题材《中国 1927》等重磅立项公示，再度展现了大历史格局下群像人物编织的高超戏剧功力。不被生成的虚荣结论蒙蔽，用严密的边界与一手事实做判断，是每一个造物主的必修课。',
        'scene': '「你们用 AI 写的行业竞品分析，投资人怎么一眼就看出了漏洞？」「因为模型只会整理网上公开的二手废话，根本不知道线下真实的履约成本和退换货损耗。现在我们调研必须加上一线实地暗访。」',
        'cover': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80',
        'closing': '''长假后的第二个工作日，大家都已经完全进入了工作状态。

在这个人人都在谈论效率、谈论一键生成的时代，今天这一期日刊想送给大家一个关键词：**挑剔。**

AI 很容易给我们一种错觉：只要问一句，几秒钟后就能得到一份洋洋洒洒几千字的调研报告、几幅漂亮的画、或者一段跑得通的代码。很多人便因此放下了戒心，把思考的控制权全盘交给了机器。

但真实的商业世界是残酷的。那些能在残酷的市场竞争中杀出来的强者，从来不会轻信任何二手的漂亮报告。他们会亲自下场去摸供应链的每一个零件，去跟每一个愤怒的用户面对面沟通，去逐行审视每一段可能崩溃的代码。

**机器负责加速推演，而人类负责死守真相。**

带着对真实的敬畏去构建你的产品、打磨你的故事吧。无论环境如何变化，真诚与严谨永远是这个时代最昂贵的光芒。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'Muse 狂飙与虚拟分镜退潮：AI 漫剧工具从概念炒作走向工业流水线整合',
                'note': '视听工具生态深度观察：单点概念型生图工具日活断崖式下跌，能够与专业剪辑软件、三维分镜引擎无缝咬合的系统级工作流平台正在垄断头部影视动漫工作室。',
                'so_what': '单点工具的寿命极其短暂；把漫剧制作全流程整合为稳定流转的工业级管线，是漫剧团队筑牢护城河的核心资产。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473303.html',
                'media': 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'FastViT 实时视觉骨干网络开源：端侧设备超高帧率漫剧分镜与特效即时预览',
                'note': '苹果开源轻量化视觉神经网络：在 iPhone 与 Mac 芯片上实现极低延迟的高清图像特征提取与滤镜渲染，为移动端漫剧制作提供毫秒级交互反馈。',
                'so_what': '本地端侧算力正在释放巨大的即时生产力；创作者在平板或手机上即可完成高保真分镜实时推演，创作手感大增。',
                'source': 'github.com',
                'url': 'https://github.com/apple/ml-fastvit',
                'media': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'MobileAgent 跨应用视觉交互智能体：自主测试漫剧阅读器跨屏交互体验',
                'note': '端侧自主 Agent 前沿实验：基于纯视觉屏幕理解，模拟真实读者在折叠屏与手机上连续翻页、双击缩放与弹幕互动，全自动揪出分镜排版破损与渲染卡顿。',
                'so_what': '交互测试自动化消除了繁重的真机测试成本；智能体替你先当读者，确保交付给用户的每一话漫剧都拥有丝滑触感。',
                'source': 'github.com',
                'url': 'https://github.com/X-PLUG/MobileAgent',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': 'Mamba 线性长序列建模应用：长篇剧本与连续多集漫剧分镜时序自洽推演',
                'note': '状态空间模型（SSM）颠覆长上下文推理：在处理数万字长剧本与数十集连续分镜时显存占用恒定，彻底避免传统 Transformer 架构跨集遗忘伏笔与设定冲突。',
                'so_what': '跨越超长周期的叙事连续性有了技术解法；宏大世界观与复杂人物关系网的漫剧创作门槛大幅降低。',
                'source': 'github.com',
                'url': 'https://github.com/state-spaces/mamba',
                'media': 'https://images.unsplash.com/photo-1507842229451-7f01be7ac128?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '重大革命题材电视剧《中国 1927》立项公示：大历史叙事中的命运抉择与群像刻画',
                'note': '国家广电总局同意摄制重点剧目深度拆解：解析主创如何在波澜壮阔的时代风暴中聚焦具体历史人物的内心波澜，通过微观日常抉择串联起宏大的历史车轮。',
                'so_what': '大历史需要大格局，更需要微切口；把历史的必然性收敛在具体人物的执念与牺牲中，剧本才具有沉甸甸的史诗分量。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/883',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '重大题材电视剧《星火征途》摄制公示：戏剧主线与信念弧光的坚实锚定法门',
                'note': '经典剧作申报指南复盘：展现如何在长跨度叙事中确立单一且不可动摇的超级主线，让每一场战役、每一次转战都成为主角信念蜕变的催化剂。',
                'so_what': '没有超级主线的故事就是一盘散沙；让所有支线冲突都服务于主角的核心蜕变，整部大戏才能一气呵成。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/884',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '2026 年 8 月全国拍摄制作网络剧备案公示：强情节类型剧与年轻受众心理契合',
                'note': '网络视听立项数据前瞻：青春冒险与硬核悬疑网络剧呈现爆发式增长，平台评审重点考察单集叙事节奏是否紧凑、核心人物是否具备当代青年的心理投射。',
                'so_what': '尊重年轻受众的信息消化速度；摒弃拖沓铺垫，把最尖锐的矛盾在开场迅速引爆，才能在首播期锁定高留存。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/938',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '电视剧备案公示：悬疑推理与都市现实题材审读导向及情节密度把控要诀',
                'note': '资深编剧审读意见公开：剖析在悬疑推理中如何合理安排伏笔与误导信息（红鲱鱼），既保证解谜快感，又严谨维护法理与社会公序良俗底线。',
                'so_what': '智力较量必须遵从严格的生活常识与逻辑自洽；经得起反复推敲的严密推理，才是硬核悬疑剧的安身立命之本。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/941',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '从小红书竞品到行业报告：我用大模型做了一次产品调研的教训与真知',
                'note': '资深 PM 真实避坑复盘：剖析大模型在提炼宏观趋势时的强大优势，以及在面对垂直线下履约痛点、灰度数据与用户微表情时的致命盲区，提出“AI 提纲+实地肉身质询”的双轨调研法。',
                'so_what': '大模型是效率杠杆，不是思考拐杖；唯有把脚踩进真实业务的泥土里，拿到的调研结论才敢作为战略决策依据。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473400.html',
                'media': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '腾讯元宝杀入个人智能体大战：国民级入口争夺背后的生态护城河演进',
                'note': '巨头战略打法深度透视：腾讯将个人 Agent 全面接入微信与 QQ 生态关系链，不再单纯拼模型刷榜，而是以极高的社交即时触达与长尾生活服务闭环构筑超级防御墙。',
                'so_what': '技术终会被抹平，场景与关系链才是永久护城河；做产品一定要扎进用户最离不开的高频物理场景中。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473518.html',
                'media': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '实测 ChatGPT Dot：交互界面微创新与桌面个人助理的产品演进路径',
                'note': '先锋交互深度测评：剖析以悬浮小圆点形态常驻屏幕边缘的微交互设计，如何通过按需唤醒、上下文感知与极低屏幕遮挡率，彻底改变人类与 AI 助理的相处模式。',
                'so_what': '最好的交互是非侵入式的；减少对用户心流的粗暴打断，让智能体像空气一样随叫随到，是桌面端交互设计的黄金准则。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/evaluating/6473388.html',
                'media': 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '海外消费群体赴华扫货观察：供应链极致性价比如何重塑全球消费心智',
                'note': '跨境与新消费深度剖析：从单纯网购跨境包裹到外国消费者直接深入义乌与华强北现场采购，中国制造业无与伦比的敏捷交付与全产业链配套正在形成不可撼动的全球引力。',
                'so_what': '实体供应链的深度整合是最坚硬的压舱石；把数字化工具与强大的制造土壤紧密结合，才能做出无惧脱钩的超级产品。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6473420.html',
                'media': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

days_order = ['2026-10-07', '2026-10-08']
target_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']

for d in days_order:
    dd = d.split('-')[-1]
    raw_path = f'scripts/raw-ian-{dd}.json'
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_items = json.load(f)
    
    ian_by_cat = {}
    for it in raw_items:
        u = it['url']
        c = it['category']
        if u not in used_set and c in target_categories:
            ian_by_cat.setdefault(c, []).append(it)
            
    day_items = []
    
    # 1. 6 ian categories × 4 items
    for c in target_categories:
        avail = ian_by_cat.get(c, [])
        picked = avail[:4]
        if len(picked) < 4:
            raise ValueError(f'Not enough items for {d} {c}: only {len(picked)}')
        for idx, p in enumerate(picked):
            used_set.add(p['url'])
            day_items.append({
                'category': c,
                'title': p['title'],
                'note': p['judgment'],
                'so_what': '从微小变化中洞察范式转移，把外部技术演进收拢为自身确定性的产品复利。',
                'source': p['source'],
                'url': p['url'],
                'media': p['media'] or 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': (idx < 2)
            })
            
    # 2. 3 vertical categories × 4 items
    v_info = vertical_data[d]
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
        raise ValueError(f'Day {d} items count is {len(day_items)}, expected 36!')
        
    cat_order = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 漫剧', '编剧技巧', '产品经理']
    sorted_items = []
    for co in cat_order:
        sorted_items.extend([it for it in day_items if it['category'] == co])
        
    md_content = f"""---
date: '{d}'
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

    out_file = f'src/content/daily/{d}.md'
    with open(out_file, 'w', encoding='utf-8') as out:
        out.write(md_content)
    print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating both days! Total URLs in history: {len(all_used_list)}')
