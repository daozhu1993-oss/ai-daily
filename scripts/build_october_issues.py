import json
import os
import re

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

# Define supplemental vertical items for all 6 days (AI 漫剧, 编剧技巧, 产品经理, and 1 extra for AI 资讯 on Day 05)
vertical_data = {
    '2026-10-01': {
        'title': '10 月 1 日 · 破除伪需求与全栈自治：长假归航，重塑商业与创作基石',
        'highlights': '全网 9 大领域 36 篇高密度精选：快手开源可图文字渲染大模型、LivePortrait 驱动高保真角色表情、AI 微短剧分类分层标准解读、三幕剧心跳因果设计、从业务倒推用户行为指标。',
        'epigraph': '模型的能力越是廉价，能被一眼看穿的伪需求就死得越快；当技术的喧嚣退去，唯有扎实的数据转化、严密的因果戏剧骨架与端侧自治的确定性，才是穿越周期的真正基石。',
        'lead': '进入金秋十月，技术演进正在加速告别概念炒作，大步迈入业务深水区与垂直工业化。在 AI 漫剧与内容生产一线，快手开源可图（Kolors）大模型攻坚中英文字渲染与角色一致性，LivePortrait 彻底打破数字角色面部微表情僵硬的僵局，而行业对 22 万部 AI 短剧的深度复盘则敲响了警钟——播放量破亿的不到千分之五，单纯依靠猎奇题材已无法支撑商业闭环；在剧作技巧与戏剧理论端，三幕剧结构被重新定义为故事的心跳与因果约束，倒逼创作者走出流水账迷局；在产品与商业化战场，老练的操盘手开始从最终业务结果倒推指标，坚决斩断虚荣流量的诱惑。无论身处哪个赛道，唯有戒骄戒躁、重塑底层骨架的人，才能在重构的秩序中稳步扎根。',
        'scene': '「国庆大家都在聊大模型的新 Demo，你们怎么在改底层业务流水线？」「因为 Demo 换不来真金白银。我们把指标直接挂在留存和履约上，剧本因果不扎实的直接打回，先把内功练扎实比什么都强。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''十月的第一天，整个世界都在放缓节奏。

但在科技与造物的一线，深度的沉淀与反思才刚刚开始。过去几个月，我们见证了太多喧闹的发布会和漫天飞舞的估值神话，但当潮水稍稍退去，留在沙滩上的究竟还剩什么？

**第一，警惕一切不能自洽的“自我感动”。** 无论是做产品还是写故事，最致命的陷阱就是把自己的臆想当成用户的痛点。去看看那些真正盈利的一人公司，没有华丽的说辞，只有冰冷而真实的复购与离线回访。

**第二，尊重因果，打牢脊柱。** 剧本第二幕为什么总会塌？因为没有遵循生活和戏剧的必然因果。写代码、架架构也是如此，缺乏防御性隔离与确定性沙箱的系统，跑得越快，崩溃时越惨烈。

**第三，把能力收归私有与端侧。** 不要过度依赖远端不可控的黑盒，能留在本地的资产就留在本地，能沉淀为自身选题库与工作流的经验就牢牢抓住。

新的一月，愿我们都能在宁静中找回前行的从容。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': '快手开源 Kolors（可图）：攻坚中英文字渲染与漫剧人物面部高度一致性',
                'note': '官方重磅开源自研扩散基座：在海量图文对齐与高保真汉字排版上取得突破，有效化解传统文生图模型文字乱码与动漫人物多视角面部崩坏的顽疾。',
                'so_what': '文字与角色一致性是漫剧工业化的两大命门；开源基座的升级让小团队无需高昂成本即可单机产出连贯分镜。',
                'source': 'github.com',
                'url': 'https://github.com/Kwai-Kolors/Kolors',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'LivePortrait 肖像微表情驱动开源：漫剧角色即时口型与丰富情绪对齐',
                'note': '前沿视觉驱动管线落地：仅需单张静态角色原画与一段参考视频，即可无缝迁移精准的眼神顾盼、唇齿微动与呼吸感微表情，兼顾拟真度与极速推理。',
                'so_what': '让静态立绘“活起来”的技术门槛被彻底抹平；漫剧创作者的制作重心可以真正转向分镜张力与情绪张力的雕琢。',
                'source': 'github.com',
                'url': 'https://github.com/chaojie/LivePortrait',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '行业深度复盘：22 万部 AI 短剧狂奔之后，破亿爆款不足千分之五的残酷真相',
                'note': '行业万字全景透视：海量低门槛工具引发严重的题材同质化与劣币驱逐良币，单纯依靠猎奇吸睛的流水线短剧正在被主流平台与付费受众无情抛弃。',
                'so_what': '技术的普及消除了产能门槛，却将审美与故事的门槛推向了前所未有的高度；唯有深耕真实情感共鸣才能穿越周期。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473856.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '万众编剧网：AI 微短剧分类分层标准发布，视听工业化与合规备案评测指引',
                'note': '主管部门与行业协会联合规范细则：明确将 AI 辅助生成与全流程自动化短剧纳入分级管理，重点考核原创剧本梗概、视听艺术水准与核心价值观导向。',
                'so_what': '野蛮生长结束，合规化时代降临；掌握标准规范并具备扎实原创剧作能力的团队将迎来合规红利。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/917',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '为什么你的故事像流水账？故事的本质是冲突、变化与不可逆的价值对立',
                'note': '名家剧作基础精析：深入剖析新手编剧高频误区——把事件罗列当作戏剧冲突；详述如何通过给主角设定两难困境与不可逆选择，激活戏剧张力。',
                'so_what': '故事的推力不是时间的流逝，而是主角被迫作出的沉重选择；没有代价的选择，引不起观众哪怕一秒的情绪波澜。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/948',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '第二幕为什么总塌？三幕剧不是八股套路公式，而是人类认知的心跳节拍器',
                'note': '戏剧骨架构建指南：拆解第二幕中段容易出现的剧情注水、动机模糊与目标漂移，系统传授如何通过“中间点危机”与“至暗时刻”维系故事主线。',
                'so_what': '第二幕是编剧功力的试金石；用严密的因果链条串联危机，才能牢牢锁住读者的好奇心与注意力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/949',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '开篇为什么无聊？前 10 分钟抓不住人背后的激励事件与日常世界失衡',
                'note': '剧作开篇黄金法则：如何在最短篇幅内确立主角的日常世界与内在缺陷，并通过外在激励事件的猛烈撞击，彻底打碎现状逼迫其踏上冒险征途。',
                'so_what': '开篇的任务不是交代背景，而是制造失衡；越快打破主角的平静，故事的吸睛效率就越高。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/951',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '“剧美中国”全国剧本征集评析：跨媒介改编如何在小说中预设舞台视听动作',
                'note': '专业剧作征集指南：详述评委会如何审查文学底稿的视听转化潜力，指导写作者在纯文字叙述中多用富有外部动作与空间关系的语言。',
                'so_what': '优秀的文本在笔尖落下时就已经具备了分镜意识；为影视和漫剧留足改编空间，是文本溢价的关键。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/901',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '产品指标怎么定？从最终业务交付结果倒推用户核心行为指标树',
                'note': '资深产品总监深度拆解：拒绝流于表面的 PV/UV 虚荣考核，建立从企业商业闭环、交易履约到关键摩擦节点层层下钻的确定性指标治理体系。',
                'so_what': '指标不是越多越好看，而是能否指导行动；用冰冷的业务交付倒逼产品设计，才能避免沦为功能堆砌的“表哥表姐”。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/operate/6473988.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '离业务越近，越觉得流量没那么重要：穿透虚荣曝光的实战经营哲学',
                'note': '一线操盘手万字反思：分析为何数千万的公域泛曝光换不来几个高净值客户，详解如何靠垂直高信任度内容与精准履约建立抗周期的私域护城河。',
                'so_what': '流量泡沫终会破裂，真实的交易信任才是压舱石；把精力用在提高单客全生命周期价值上，小团队也能安身立命。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/operate/6473854.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'AI 办公刚刚来到 1972 年：人机交互范式与工作流重构的深度思考',
                'note': '从施乐帕洛阿尔托研究中心（PARC）图形界面历史透视当下生成式 AI：现在的聊天框正如早期的命令行终端，真正的空间化、意图化交互界面尚未成型。',
                'so_what': '不要把视野局限在对话气泡里；下一代颠覆性的 AI 产品必然发生在操作系统的交互重构中。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473826.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '把爆款内容拆解为可复用选题库：内容型产品的信息架构与资产化沉淀',
                'note': '知名内容增长黑客方法论：将偶发性的爆款灵感抽象为人格设定、情绪诱饵、痛点反转与行动指令四维矩阵，打造可持续自循环的内容生产流水线。',
                'so_what': '灵感不可靠，结构才可靠；把一次性的成功经验产品化为资产，是单兵造物主持续规模化输出的关键。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6462760.html',
                'media': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    },

    '2026-10-02': {
        'title': '10 月 2 日 · 端侧感知与微型飞轮：在巨头阴影下构筑小而美自循环',
        'highlights': '全网 9 大领域 36 篇高密度精选：混元 DiT 视觉大模型开源、Fish Speech 零样本拟真语音对齐、Stripe 揭示 AI 混合定价新信号、万字拆解 DeepSeek Harness 桌面版架构、电视剧主角改编实录。',
        'epigraph': '不要试图在巨头搭建好的主干道上与重型装甲车比拼马力；在他们视线之外的微型垂直场景里，用极佳的端侧触感与自循环飞轮扎下根须，才是独立造物的生存之道。',
        'lead': '10 月 2 日的科技与商业格局，正愈发清晰地展现出分层竞争的残酷真相：在底层模型与基建侧，巨头们正在大举开源诸如混元 DiT、Fish Speech 这样原本被严密雪藏的重量级音画模型，逼迫整个行业重新评估私有算法的保密壁垒；在商业模式与定价博弈一线，Stripe 最新发布的行业支付洞察揭示了令人警惕的信号——Token 盗用与滥用激增，传统纯按席位或纯按 API 调用的商业模式正在崩溃，混合动态定价与严苛防刷策略成为企业生存刚需；在剧作与垂直内容端，《主角》从严肃文学到影视剧本的改编历程再度印证，越是宏大的时代叙事，越需要将针尖扎在微小个体的执念与挣扎之中。认清生态位置，不盲目崇拜庞然大物，在小而美中构建确定性现金流。',
        'scene': '「很多团队还在把开源大模型直接套壳卖月费，这模式还能撑多久？」「Stripe 的数据早就给出了答案，不解决垂直闭环和防刷治理，光算力账单就能把公司拖垮。现在必须做深嵌业务的混合定价。」',
        'cover': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1600&auto=format&fit=crop&q=80',
        'closing': '''长假的第二天，喧嚣的外部世界渐渐安静下来。

每当我们看到科技巨头又公布了动辄千亿参数的模型或者数以万计的算力集群，心中难免会升起一种渺小感。但历史一次又一次证明：**参天大树之下，永远生长着最繁茂的灌木与苔藓。**

像 TypingMind、Tiny Fishing 这样的独立产品，没有去拼大模型的训练算力，他们只是守住了用户每天打开电脑时那几秒钟的真实习惯，就稳稳地拿到了属于自己的丰厚回报。

做产品也是如此。不要妄想一上来就拯救世界或者颠覆大厂，去找到那个被大厂看不上、却让某一群人痛苦不堪的具体摩擦点；用极致克制的代码和优雅体面的交互去抚平它。

哪怕只有几千个愿意为你付费的忠实用户，你的一人公司就已经战胜了绝大多数虚浮的独角兽。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': '腾讯开源混元 DiT 视觉大模型：支持多轮局部重绘与复杂分镜连贯生成',
                'note': '企业级 Diffusion Transformer 架构开放权重：基于高质量多模态对齐训练，支持高精度中英文指令遵循与局部微调，极大降低漫剧连续画格的破损率。',
                'so_what': '大厂核心图像基座的开源，让独立动画与漫剧创作者拥有了对齐工业标准的本地画布渲染能力。',
                'source': 'github.com',
                'url': 'https://github.com/Tencent/HunyuanDiT',
                'media': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'Fish Speech 开源零样本多语种语音合成：漫剧多角色音色克隆与自然语气演绎',
                'note': '高性能自回归语音大模型突破：仅需十余秒干净音频即可克隆任意角色声线，且支持低延迟流式推理与跨语种语调迁移，完美契合多角色漫剧广播剧。',
                'so_what': '配音外包周期被压缩至以秒计算；创作者一人即可分饰多角，赋予不同角色鲜明的声线辨识度。',
                'source': 'github.com',
                'url': 'https://github.com/fishaudio/fish-speech',
                'media': 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '品牌争相涌入 AI 漫剧：大促节点下的内容营销新战场与长效留存博弈',
                'note': '前沿消费与品牌营销深度调研：传统硬广转化断崖式下滑，定制化剧情漫剧通过将产品卖点自然编织进悬疑或反转故事中，实现了数倍于图文的互动完播率。',
                'so_what': '营销正在全面短剧化与漫剧化；掌握漫剧分镜与剧情抓手的产品人，正在掌握新一代注意力分配权。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473516.html',
                'media': 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '上海推进人工智能赋能微短剧高质量发展措施：资金扶持与算力集群落地',
                'note': '地方产业政策重磅出炉：设立专项扶持基金，对采用国产自研视听大模型、具备高水准剧作立意并在海外实现文化出海的优质短剧团队给予重点补贴。',
                'so_what': '微短剧与漫剧正在从草莽游击队走向国家战略性数字内容产业，合规且技术过硬的团队享有巨大的政策先机。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/903',
                'media': 'https://images.unsplash.com/photo-1509631179647-0177331693ae?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '各地方与平台短剧扶持观察：预算、门槛与年轻创作者的真实破局机会',
                'note': '万众编剧网深度产业调研：全盘盘点各大主流长短视频平台与各地文旅基金的最新签约细则，剖析保底分成、阶梯分账与版权独占条款中的潜在陷阱。',
                'so_what': '签约不仅要看眼前的启动资金，更要看后续长尾衍生权的归属；理清合同边界是独立创作者安身立命的前提。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/944',
                'media': 'https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '电视剧《主角》改编实录：从茅盾文学奖小说到剧本的结构重组与人物提纯',
                'note': '殿堂级名作改编手记剖析：解析编剧团队如何将长篇纯文学小说中的庞杂叙事线索提炼为高度戏剧化的舞台与荧幕动作，将主角的命运起伏作为绝对脊柱。',
                'so_what': '文学性是灵肉，戏剧性是骨架；改编的最高境界不是照搬字句，而是重塑原著中最核心的生命驱动力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/896',
                'media': 'https://images.unsplash.com/photo-1507842229451-7f01be7ac128?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '2026 年 9 月全国一类微短剧规划备案公示：重点现实题材审读导向与合规指南',
                'note': '广电立项动态梳理：通过对最新一批备案微短剧题目的类型学分析，归纳出当下审查对聚焦职场奋斗、家庭代际理解与非遗传承等现实主义题材的明确偏好。',
                'so_what': '立项是作品面世的第一道门槛；顺应合规与时代语境，在规范的框架内发挥极致戏剧才华，是职业编剧的必修课。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/954',
                'media': 'https://images.unsplash.com/photo-1513694203232-719a280e022f?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '《八仙！》主创私藏书单公开：神话志怪母题与现代戏剧结构的无缝融合法则',
                'note': '新锐爆款舞台剧主创心法：揭示如何将传统民俗神话中的天马行空想象，收敛在现代戏剧严密的危机倒计时与人物成长弧光之中，让古老故事重新打动现代人。',
                'so_what': '传统文化是取之不尽的宝库，但必须用现代观众的情感密码来解锁；古为今用，关键在找准普世共情点。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/937',
                'media': 'https://images.unsplash.com/photo-1541701494587-cb58502866ab?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': 'Token 盗用激增与混合定价兴起：Stripe 深度揭示 AI 经济背后的支付与安全新变局',
                'note': '全球支付巨头披露独家数据：AI 产品的非正常凭证调用与逆向爬取正在激增，传统的按量或按月单一计费已被淘汰，必须采用基准功能订阅加弹性消耗配额的复合架构。',
                'so_what': '商业模式必须与工程安全紧密咬合；设计 AI 产品时，如果不把防刷与阶梯定价做进第一版架构，用户增长只会加速破产。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473642.html',
                'media': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '万字拆解 DeepSeek Harness 桌面版：系统架构、多端协同与能力边界全景评测',
                'note': '资深产品架构师硬核拆解：详尽分析如何将本地轻量化模型与云端超级智能体调度结合，既守住个人隐私与响应低延迟，又能按需调度云端算力完成复杂任务。',
                'so_what': '端云协同是未来 AI 桌面端产品的终极形态；把离线小模型当门卫、云端大模型当智囊，是平衡成本与体验的最佳解法。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/evaluating/6473256.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'a16z 投资哲学洞察：押注 AI 头部赢家，让真实业务增长速度跑赢估值泡沫',
                'note': '顶级风投内部研判纪要：面对当前市场上泛滥的包装型 AI 初创企业，资本正在极速收拢到那些具备真实高黏性用户行为、健康的毛利率与持续技术复利的企业。',
                'so_what': '讲故事拿钱的时代已经结束，考卷上只剩下真实商业留存；产品经理最大的竞争力是帮助公司在细分赛道跑出正向现金流。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473814.html',
                'media': 'https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '让员工自费买 AI 的公司已经输了：组织演进与生产力工具解放的深度反思',
                'note': '企业数字化转型犀利批评：揭示许多传统企业口头高喊拥抱 AI，实际却将前沿生产力工具视为成本负担，导致真正具备敏锐度的高效员工不得不自费购买个人工具。',
                'so_what': '先进工具的阻碍从来不是预算，而是陈旧的组织心智；优秀的团队会主动拆除审批藩篱，将最锋利的武器交到一线作战人员手中。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6462090.html',
                'media': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    },

    '2026-10-03': {
        'title': '10 月 3 日 · 意图画布与物理触感：界面设计告别扁平虚无的具象觉醒',
        'highlights': '全网 9 大领域 36 篇高密度精选：Open-Sora 视频生成开源落地、StoryMaker 保持角色高度连贯、Databricks CEO 谈前沿训练放缓与实用主义、微短剧管理规范征求意见、伯恩巴克 40 条说服铁律。',
        'epigraph': '当屏幕上的扁平色块和千篇一律的卡片让人产生审美厌倦，设计的本质正在重新向物理世界与具象意图回归；有呼吸感的材质、确定性的因果与克制的高级留白，才是打动人心的稀缺品。',
        'lead': '10 月 3 日的审美与工程浪潮，共同奏响了一曲“去虚向实”的交响乐。在设计与交互一线，越来越多的先锋造物主开始反思数字世界的悬浮感——无论是纸张纤维滤镜中逼真的物理受光与折痕，还是把繁杂的投资推演整理为带时效的可触摸实体，产品设计正在挣脱扁平风格的虚无枷锁；在开源视频与多模态制片端，Open-Sora 与 StoryMaker 连番突破，不仅将高品质电影级视频镜头带入个人工作站，更彻底攻克了漫剧连贯分镜换脸走样的难题；在商业理念与广告哲学层面，广告传奇伯恩巴克的 40 条黄金法则历久弥新——广告不是冰冷的算法统计，而是触及人性的说服艺术。在技术狂奔的时代，保持对艺术直觉与生活物理质感的敬畏，才能创造出耐看、耐用的作品。',
        'scene': '「现在做界面还在用那种千篇一律的卡片堆叠吗？」「早就没人看了！用户需要的是直观可控的物理反馈。你看这个材质着色器，光线角度随着鼠标微调，手感有了，留存自然就上来了。」',
        'cover': 'https://images.unsplash.com/photo-1507842229451-7f01be7ac128?w=1600&auto=format&fit=crop&q=80',
        'closing': '''长假过半，很多平时的焦虑开始在这几天里被重新审视。

我们是不是在太多的数字化工具里迷失了自己？那些数不清的看板、无限滚动的消息流，以及由算法生成的塑料感图片，究竟给我们的生活留下了什么？

**好作品的第一特质，是“真实感”。**

像 Open-Sora 这样开源的视频管线，或者 StoryMaker 对角色一笔一划的连贯勾勒，他们的意义从来不是为了生产更多的数字垃圾，而是为了让有故事想讲的人，能更自由、更具象地把心里的世界呈现出来。

去看看现实生活里的石头、旧书和木头吧。正是那些看似不完美的划痕、磨损与重量，构成了人类文明中最打动人心的美学。

做产品亦然。少一点浮躁的假大空，多一点沉下心打磨细节的工匠定力。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'Open-Sora 开源高质量长镜头视频生成：为短剧与漫剧创作者解锁电影级运镜',
                'note': '开源视频大模型前沿迭代：支持高动态范围下的电影级推拉摇移运镜控制，并针对复杂光影交互做了专门优化，大幅压缩生成单段高质量漫剧过场的耗时。',
                'so_what': '过去只有好莱坞或大型特效棚才玩得起的复杂运镜，现在单台高配工作站即可跑通，极大释放了个体视觉创作者的表达力。',
                'source': 'github.com',
                'url': 'https://github.com/hpcaitech/Open-Sora',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'StoryMaker：开源个性化连贯角色生成，彻底终结漫剧换脸与特征漂移',
                'note': '学术界与工业界联合重磅开源：无需针对单个角色进行数小时微调，即可在任意姿态、服饰与光影场景中严格锁定角色的五官面部与发型特征。',
                'so_what': '多镜头分镜一致性是漫剧制作的核心卡点；StoryMaker 让创作者告别繁琐的后期换脸修图，真正实现“一镜到底”的连贯故事表达。',
                'source': 'github.com',
                'url': 'https://github.com/storymaker/StoryMaker',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '2026 年前三季度微短剧（AI 短剧）市场情报：从粗暴买量反噬走向内容精品化',
                'note': '行业权威季度分析报告：流量采买成本上涨超 40%，依靠粗糙反转切片买量跑马圈地的老路已经走通无望，拥有强黏性 IP 与稳定分发渠道的精品漫剧成为资本新宠。',
                'so_what': '买量红利期宣告结束，内容红利期正式拉开序幕；打磨好故事本身的吸引力，才能在存量博弈中活下来。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/952',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '全国微短剧与 AI 短剧剧本征集汇总：聚焦悬疑反转与现实科幻交叉新题材',
                'note': '编剧平台前沿风向透视：重点平台加大对具备科幻设定但根植于现实人伦纠葛剧本的扶持力度，要求投稿文本必须附带清晰的角色关系拓扑图与分镜大纲。',
                'so_what': '剧本是工业化生产的施工图；懂得用标准化分镜语言交付文本的编剧，在剧组与漫剧团队中享有最高话语权。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/904',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《微短剧发展管理办法》公开征求意见：备案审查规范化与精品导向解析',
                'note': '政策专家逐条解读新规草案：强化对微短剧全流程内容审读把控，明确要求建立违规题材动态黑名单，严打同质化洗稿与低俗擦边。',
                'so_what': '粗制滥造的投机者将被制度化清理，为潜心打磨好剧本的专业创作者腾出了健康的生存空间。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/914',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '电影剧本（梗概）备案立项公示：类型片剧情“钩子”与前置危机设计法则',
                'note': '权威立项案例复盘：深入剖析通过国家电影局备案的数十部悬疑与爱情类型片梗概，展示如何在 500 字内布置出令评审过目不忘的致命危机与戏剧困局。',
                'so_what': '梗概不是全剧的缩写，而是戏剧钩子的陈列；抓住主要矛盾，一剑封喉，才是专业提案的基本功。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/943',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《给阿嬷的情书》剧本赏析：东方温情叙事中的因果闭环与情感沉淀法门',
                'note': '优秀剧作文学性拆解：展示如何利用日常器物、书信线索与跨越半个世纪的细节呼应，在没有剧烈打斗与大起大落的情形下激荡出催人泪下的深沉情感。',
                'so_what': '平静的水面下往往蕴藏着最澎湃的波涛；懂得利用情感的余味与克制，往往比刻意大喊大叫更有力量。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/897',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '校园戏剧剧本有奖征集启事：青春母题与成长困境的戏剧化提炼',
                'note': '面向青年创作者的全国征集令：重点扶持突破陈词滥调、真实反映青年一代在学业压力、社会融入与人际孤立中寻找自我价值的原创新作。',
                'so_what': '年轻人的困惑是最鲜活的时代镜子；拒绝说教，平视青春的迷茫，才能写出引发万人空巷共鸣的佳作。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/886',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '对谈 Databricks CEO：真正的 RSI 根本没有发生，前沿模型训练正在放缓与务实',
                'note': '大数据与 AI 领军人物深度洞察：所谓的模型自我递归进化（RSI）在工程现实中面临巨大的数据枯竭与收益递减，当务之急是将现有模型能力真正吃透并服务实体企业。',
                'so_what': '不要过度焦虑未到来的超级奇点；把现有的能力用好、把业务闭环做扎实，足以在这个时代构建坚不可摧的壁垒。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473635.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'GitHub 开源定律：今天有个闭源产品刷屏，明天就有个 Openxxx 登上热榜',
                'note': '软件生态演进规律深度复盘：任何缺乏数据与网络效应护城河的纯前端或单点 AI 功能，都会在 48 小时内被全球开源社区复刻，单点功能套壳没有未来。',
                'so_what': '不要再做容易被克隆的功能外壳；唯有独家私域资产、极深的工作流粘性与真实社群信任，才是开源浪潮冲不垮的堡垒。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473633.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '最火 AI 岗位 FDE 深度剖析：前线部署工程师如何连接模型与客户真实业务',
                'note': '新兴岗位全面解构：Forward Deployed Engineer 成为企业争抢的香饽饽，核心能力并非纯学术算法调优，而是深入客户业务现场、清洗脏数据并将模型稳健落地的实战力。',
                'so_what': '技术落地的最后一公里最值钱；产品经理转型 FDE 思维，懂技术更懂业务现场痛点，身价倍增。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/zhichang/6473816.html',
                'media': 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '创意宗师伯恩巴克：广告不是冷冰冰的科学，而是击穿人心的说服艺术（40 条）',
                'note': '现代广告奠基人传世心法精粹：严厉驳斥纯数据唯上的机械增长论，强调真正能够改变用户心智并创造长效商业价值的，永远是对人性弱点与情感渴望的深刻洞察。',
                'so_what': '数据只能告诉你过去发生了什么，洞察才能告诉你未来该去向何方；做增长不要迷信转化漏斗的数字游戏，先问问自己的产品有没有打动人心。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/marketing/6473824.html',
                'media': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    },

    '2026-10-04': {
        'title': '10 月 4 日 · 剧作骨架与漫剧工业：当生成技术填平画功，唯有因果冲突能破局',
        'highlights': '全网 9 大领域 36 篇高密度精选：Audiobox 可控拟音模型开源、Animate Anyone 骨骼动作迁移落地、微短剧市场情报全景、重点短剧规划备案审读要点、抖音上线交互式「兴趣卡」。',
        'epigraph': '当生成模型让任何人都能一秒画出华丽的画面，单纯拼画功的时代就已经死了；留在牌桌上的，只剩下谁能在更短的分秒里编织出更残酷的戏剧冲突与更不可逆的人物命运。',
        'lead': '10 月 4 日的内容消费与技术生态，正在经历一场深刻的价值重估。在视觉与声音的工业管线端，开源技术的拼图正以惊人的速度补齐——Audiobox 带来了前所未有的环境音场与可控拟音能力，Animate Anyone 则让任意静态人物原画能够自如跟随骨骼动作生动起舞，从画画、配音到角色动作的制作全链路被彻底打通；但在内容消费的前线，市场却呈现出极具讽刺意味的冷酷分化——粗制滥造的短剧陷入严重的滞销，而剧本因果扎实、人物动机饱满的精品内容却赢得了超额溢价；在产品交互层面，抖音上线的交互式「兴趣卡」再度表明，未来的内容交互绝非单向被动灌输，而是用户与内容节点之间的实时探索与共鸣交锋。技术填平了鸿沟，剧作能力重新登顶。',
        'scene': '「现在做漫剧动画只要把人物画出来，动效和配音都能一键生成了，那以后漫剧岂不是泛滥成灾？」「泛滥的是垃圾，值钱的是好故事。画面再炫，第三集交代不清人物动机，观众立刻划走。编剧的地位反而空前拔高了。」',
        'cover': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=1600&auto=format&fit=crop&q=80',
        'closing': '''到了假期的中段，各种喧嚣的聚会逐渐散去。

坐在书桌前，我们常常会问自己：当 AI 已经能够模仿人类写出流畅的文案、画出漂亮的插画、甚至合成完美的配音——**人类创作者真正的尊严与不可替代性到底在哪里？**

今天的 36 篇资讯给出了一个无比明确的回答：**在因果里，在痛感里，在那些不可逆转的选择里。**

大模型理解“然后呢”，但它理解不了“凭什么”。它知道一个情节之后可以接一万种可能，但它体会不到一个有血有肉的人在面对命运十字路口时，那种撕心裂肺的犹豫与决绝。

这种痛感，这种对生命真相的体会，是任何冰冷的矩阵乘法永远计算不出来的。

无论你在构思一个剧本、设计一个产品，还是打磨一段代码，请把你的生命体验与真实情感注入其中。那才是你的作品唯一不被算法吞噬的灵魂。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'Audiobox 开源可控拟音与环境音场生成：漫剧音效与空间对白端到端制作',
                'note': '多模态音频生成重大突破：不仅能根据文字提示生成逼真的雨声、脚步声与开门声，还能直接指定发声物体的材质与空间混响距离，打造沉浸式音画一体。',
                'so_what': '漫剧制作中耗时漫长的音效剪辑与对齐工作被一键自动化，单人即可完成好莱坞级别的空间音效混音。',
                'source': 'github.com',
                'url': 'https://github.com/AIGC-Audio/Audiobox',
                'media': 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'Animate Anyone 角色动作迁移开源落地：静态角色立绘瞬间化为生动漫剧动态',
                'note': '骨骼驱动图像生成代表作全面工程化：在保持角色服饰细节与面部特征零失真的前提下，精准跟随任意舞蹈或剧情打斗姿态序列，实现极高帧率流畅渲染。',
                'so_what': '原画资产得以最大化复用；动漫与短剧团队可以用极低的代价实现复杂打斗与大动作分镜表现。',
                'source': 'github.com',
                'url': 'https://github.com/alibaba/animate-anyone',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '微短剧市场情报深度解析：告别粗放流量红利，短剧全链路走向精品化工业化',
                'note': '行业最新投融资与完播数据复盘：投流回报率（ROI）持续收窄，促使制作方将大比例预算从买量转移到前期剧本孵化与高质量音画制作上。',
                'so_what': '市场正在从“谁会投流谁称王”进化到“谁有内容谁长青”；掌握精良制作管线的团队迎来真正的上升通道。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/927',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '全国文旅微短剧征集活动汇总：实景空间结合 AI 虚拟生成开拓视听新业态',
                'note': '文旅部与广电总局联合倡议：鼓励创作者深入传统古镇、名山大川取景，并结合 AI 生成的奇幻志怪特效，打造带动地方文旅消费的现象级短剧。',
                'so_what': '跨界融合带来了全新的资金与商业化出口；跳出传统的纯线上流量博弈，与实体经济结合天地宽广。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/928',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国重点微短剧规划备案公示：剧情反转设计与正向价值观平衡审读要点',
                'note': '主管部门审查案例通报剖析：明确指出单纯为了反转而反转、缺乏生活逻辑与道德基底的剧目将难以过审，倡导在戏剧张力中展现人性温度与真善美。',
                'so_what': '戏剧反转必须有扎实的情感依据，而不是机械的为了爽而爽；遵循因果律的巧妙反转才是经得起推敲的高级技巧。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/942',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '重大题材电视剧《莫道君行早》立项公示：历史因果与人物群像交织编织法',
                'note': '国家级大戏筹备经验剖析：如何在大跨度的历史洪流中精准捕捉多位历史人物的内心波澜，通过微观生活细节与宏观历史事件的同频共振构建史诗感。',
                'so_what': '群像戏最忌面面俱到沦为流水账；找准一个核心精神主线，让每个人物都成为该主线不同侧面的投影，方能立住。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/936',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '电影剧本（梗概）备案立项要诀：如何在有限篇幅内交代清悬疑主线与反派压迫感',
                'note': '优秀报审剧本样本拆解：反派的强大程度决定了主角胜利的含金量；传授如何在梗概中迅速树立势均力敌、甚至占据绝对优势的对立力量。',
                'so_what': '没有强大的阻碍，就没有英雄的诞生；把对手写扎实、写深刻，主角的光芒才能真正绽放。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/898',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '番茄小说院线电影征集计划：网络文学爆款走向大银幕的剧作改编标准',
                'note': '头部网文平台影游联动细则：网络小说往往篇幅冗长、爽点密集，改编为电影必须进行大刀阔斧的“剧情截流与主线浓缩”，严格遵循标准三幕剧时长。',
                'so_what': '媒介形态不同，叙事节奏天差地别；从无限流到 120 分钟闭环，学会忍痛割爱是编剧最重要的专业自律。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/911',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '抖音上线「兴趣卡」：全新交互式 AI 互动卡片重构信息流消费与搜索闭环',
                'note': '短视频超级平台重磅交互实验：不再满足于视频下方的简单评论区，引入具备独立状态与微型应用能力的“兴趣卡”，支持用户在看播过程中原位探索。',
                'so_what': '信息流消费正在从被动观看跃迁为主动交互；在内容消费的原位提供轻量可操作微组件，是下一代超级 App 的共同方向。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6463040.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '具身智能千亿融资背后：「异标的闭环」如何撑起估值泡沫与商业化大考',
                'note': '硬科技赛道万字透视：资本市场疯狂给机器人与实体 AI 注入重金，但缺乏稳定通用场景的致命缺陷导致商业化落地困难重重，亟需找到确定性的封闭场景验证闭环。',
                'so_what': '技术越是前沿，商业化陷阱就越隐蔽；不要被宏大叙事冲昏头脑，评估技术产品必须严格考察其落地的真实生产力回报。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6463440.html',
                'media': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '国庆出游用 AI 被坑惨了：自动化旅行规划工具的边界与容错冗余设计',
                'note': '用户体验真实翻车案例复盘：大模型在处理非标准现实地理信息、景区动态限流与临时道路封闭时频繁出现幻觉，导致完全依赖 AI 规划的用户在现场陷入绝境。',
                'so_what': '现实世界充满了非结构化的突发变量；设计 AI 应用永远不能做“全自动封闭假设”，必须给用户保留便捷的人工核验与备选兜底入口。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6473648.html',
                'media': 'https://images.unsplash.com/photo-1507842229451-7f01be7ac128?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': 'AI 产品经理方法论框架：从模型选型、评测集构建到业务交付的端到端闭环',
                'note': '业界首份系统化方法论手册精粹：打破传统软件产品经理只画线框图的旧习惯，详细拆解如何构建精准的业务金标评测集、设计 Prompt 防护网并权衡推理成本。',
                'so_what': 'AI 产品经理的核心竞争力不再是 PRD 写得多厚，而是对模型能力边界的精准把控与确定性评测集的构建能力。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/class/6468281.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    },

    '2026-10-05': {
        'title': '10 月 5 日 · 治理围栏与确定性沙箱：Agent 走向真实业务的生产防线',
        'highlights': '全网 9 大领域 36 篇高密度精选：Google Research 谈暴力堆卡见顶与下一代架构、Amphion 开源全套音频音乐工作站、Bark 拟真情感语音对齐、电视剧网络剧备案重点审查、网约车 AI 落地 ROI 测算。',
        'epigraph': '模型在沙箱里的每一次自由发挥，都可能是生产环境里的一场灾难；当智能体从玩具走向基础设施，真正的成熟标志不是它能写出多么惊艳的代码，而是能否在严格的权限围栏中驯服其不确定性。',
        'lead': '10 月 5 日的科技前沿，正在迎来一场深刻的思想交锋。在底层技术研究的最高象牙塔，Google Research 负责人公开表态——暴力堆叠算力卡的预训练红利正在见顶，下一代架构突破绝不在简单扩大参数规模，而在推理逻辑结构与物理现实感知的交互革新；在智能体部署一线，行业共识迅速凝聚在系统安全与确定性沙箱上，任何越过白名单权限的自主调用都被严厉禁止；在音频与漫剧创作端，Amphion 与 Bark 开源套件提供了从背景旋律配乐到拟真对白笑声的一揽子生成方案，大幅消除了音频外包门槛；在实体经济与产品经理前线，网约车与制造巨头的落地复盘则无情刺破了炒作泡沫：技术必须算得清单位经济账，否则只是虚假的估值安慰剂。保持清醒，筑牢防线。',
        'scene': '「听说有大厂让 Agent 自主处理数据库迁移，结果把测试库当成生产库清空了？」「所以我们现在的系统，Agent 只给建议，最终执行权严格锁死在确定性沙箱和人工物理确认键上，谁也不敢逾越。」',
        'cover': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1600&auto=format&fit=crop&q=80',
        'closing': '''假期的尾声越来越近，收心的时刻悄然来临。

回看这一周的思考，有一个词始终在脑海中挥之不去：**确定性。**

大模型天生是概率机器，它擅长在混沌中寻找关联，但商业世界和软件工程需要的是百分之百的确定性——钱不能付错，数据不能丢，剧本的人物因果不能荒谬，生产系统的权限不能失控。

一个优秀的造物主，绝不是盲目崇拜概率黑盒的人，而是懂得用确定性的围栏、形式化的测试与严密的逻辑，将黑盒的力量收束在安全管道里的驯兽师。

**克制，永远是高级的代名词。**

当你能够管住技术膨胀的野心，把精力集中在为用户提供确定性的价值交付上，你的产品就拥有了最坚固的护城河。准备好迎接假期的最后一天，整装待发！''',
        'ai_news_supp': {
            'category': 'AI 资讯',
            'title': '对话 Google Research 负责人：暴力堆卡已到尽头，下一代架构突破不在预训练',
            'note': '顶尖科学家对模型狂热的深刻反思：单靠增加数据量与卡数获得的提升越来越平缓，未来的技术奇点将发生在更深层的推演符号推理、状态自洽检验与具身物理交互之中。',
            'so_what': '不要盲信算力通吃的粗放逻辑；深耕细分领域精细化推演与业务知识对齐的创业者，将迎来弯道超车的历史契机。',
            'source': 'woshipm.com',
            'url': 'https://www.woshipm.com/ai/6473822.html',
            'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
            'pinned': True
        },
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'Amphion 开源音频、音乐与语音生成工具包：高水准漫剧配乐配音一揽子解决',
                'note': '高星开源视听研究平台：涵盖文本转语音、歌声合成、音乐生成与声学转换四大支柱能力，支持精细化控制音调起伏与情绪渲染，彻底满足漫剧团队对私有化部署的需求。',
                'so_what': '视听工具链的全面收拢，让独立制作人摆脱了对云端碎片化收费服务的依赖，在本地构建起全流程可控的音频工业化生产线。',
                'source': 'github.com',
                'url': 'https://github.com/open-mmlab/Amphion',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'Bark 开源拟真文本转语音模型：支持语气词、叹息、笑声与高度自然对白演绎',
                'note': '深度自回归音频模型经典之作：突破传统 TTS 机械呆板的发音缺陷，能够通过标记自然插入情绪停顿、背景呢喃与拟声词，极大赋予漫剧角色逼真的灵魂。',
                'so_what': '角色不再像是在读课文，而是在真实对话；情绪维度的丰满直接将受众的完播与共鸣程度提升了数个量级。',
                'source': 'github.com',
                'url': 'https://github.com/suno-ai/bark',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '全国微短剧与 AI 短剧剧本征集：高冲突悬疑剧本成热点，强调分镜节奏掌控',
                'note': '主流影视剧本交易平台数据追踪：悬疑推理题材征集量激增，资方普遍要求单集时长在 90 秒内必须包含至少两个情绪反转点与一个悬念钩子。',
                'so_what': '快节奏并不等于胡编乱造，越是在极短时间内推进剧情，越考验编剧对每一句台词与分镜画面的信息密度掌控。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/926',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《开膛手杰克》驻演启幕：小剧场沉浸式戏剧如何用高密度分镜感吸粉无数',
                'note': '先锋线下戏剧主创经验交流：抛弃传统大舞台的疏离感，采用类似电影近景特写的视听布置，让观众在几步之遥感受戏剧动作的压迫感与悬疑张力。',
                'so_what': '打破第四堵墙的交互体感，给线上短剧与漫剧设计提供了极其宝贵的灵感参照——让受众成为故事现场的一分子。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/929',
                'media': 'https://images.unsplash.com/photo-1507842229451-7f01be7ac128?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国拍摄制作电视剧（网络剧）备案公示：现实题材立项审读要点与红线警示',
                'note': '官方审读意见深度拆解：强调对涉及公共安全、金融秩序与重大历史节点的题材必须严谨求证，严禁架空乱造，注重展现普通劳动者的奋斗与温情。',
                'so_what': '在合规红线内寻找最大的戏剧自由度；把故事扎进真实社会土壤，不仅能顺利过审，更能引起主流圈层的强烈共鸣。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/953',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '微短剧规划备案深度解析：同质化套路被加速淘汰，细分类型化创作迎来爆发期',
                'note': '行业剧本孵化研讨纪要：传统的霸总赘婿题材过审率大幅下滑，职场悬疑、银发族情感、科幻漫改等垂直细分赛道正在成为平台争夺的重点高地。',
                'so_what': '逃离拥挤的红海，去尚未被充分开发的垂直人群里寻找故事题材，小成本剧本也能跑出意料之外的投资回报率。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/934',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '网络剧备案公示：强情节叙事与视听语言节奏把控的心法与实操禁忌',
                'note': '资深网剧监制对谈录：分析网剧观众在前三集的流失规律，详述如何通过“主线危机挂帅、副线情感纠葛、单集结尾必留扣子”的标准工程化方法锁死弃剧率。',
                'so_what': '好编剧必须具备产品经理的漏斗思维；把每一分钟的观看都视作用户对时间的投资，用高密度的戏剧回报留住观众。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/891',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '微短剧与长剧剧本征集细则一览：平台扶持政策比对与合同风险防范实务',
                'note': '编剧权益保护指南：详尽解析多份平台标准格式合同中的排他性条款、署名权让渡与尾款支付节点陷阱，指导新手创作者如何在法理上护住自己的心血。',
                'so_what': '懂得保护自己才能在创作的长跑中存活；合同条款里的一字之差，可能决定了未来数年的创作命运。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/889',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': 'AI 打车不应成为网约车平台估值安慰剂：技术落地必须算清单位经济账（UE）',
                'note': '商业深度评论：自动驾驶与智能调度在出行领域的包装估值正在遭遇冷水，高昂的传感器折旧、云端算力调度与安全冗余成本，倒逼企业重新审视单车利润模型。',
                'so_what': '离开单位经济模型的谈技术落地都是耍流氓；产品负责人必须穿透技术炒作光环，算清每一笔商业投入的真实回报。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473522.html',
                'media': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '汽车业 WorkBuddy 协同实战：制造型巨头如何将协同 Agent 嵌入研发流程',
                'note': '传统实体制造数字化标杆案例：拆解车企如何将大模型 Agent 安全接入保密的整车工程数据库，在不发生核心图纸外泄的前提下将零部件选型周期压缩 60%。',
                'so_what': '重资产传统行业才是 AI 提效的主战场；解决好权限隔离与私有化落地，产品在 B 端市场的客单价将极为可观。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473637.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '让不会用 App 的人自己办业务：语音与视觉 Agent 穿透数字鸿沟的商业价值',
                'note': '包容性设计（Inclusive Design）前沿案例：海外初创利用基于语音和屏幕视觉交互的轻量 Agent，帮助低认知门槛人群自如完成转账与缴费，成功完成巨额融资。',
                'so_what': '设计的终极目的不是迎合少数科技精英，而是服务最广泛的普通人；消除交互摩擦本身就是极其强大的商业护城河。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6464200.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '商业流量沉浮录：商业操盘手如何看待公域平台流量分配与品牌私域沉淀',
                'note': '资深电商与流量增长操盘手全盘复盘：平台算法机制永远在动态调整，任何将全部命脉托付给单一平台推荐流的商业模式都是脆弱的，必须将公域流量转化为私域资产。',
                'so_what': '租来的房子再华丽也不是自己的；借公域的风起飞，但一定要把用户沉淀在能直接触达的独立根据地里。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6473520.html',
                'media': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    },

    '2026-10-06': {
        'title': '10 月 6 日 · 开源权重与混合经济：算力退潮期，如何锁定不可替代的资产',
        'highlights': '全网 9 大领域 36 篇高密度精选：Beam 开源大模型公布核心参数、PaddleSpeech 工业语音合成套件落地、金茶花文创微短剧大赛指引、支付宝设立智能体涌现奖、弹性计算异构调度架构抉择。',
        'epigraph': '长假终章，算力基建的狂热在现实的引力面前逐渐收敛；在这个混合经济与开源权重并存的新周期，单纯依赖外部接口的套壳工具正在快速贬值，唯有深植于业务流程、拥有私有数据闭环与扎实情感叙事的资产，才能真正抵御风浪。',
        'lead': '今天是 10 月 6 日，金秋长假的最后一天。整个科技与商业界正在以极度务实的姿态迎接假后的全新战役。在模型基建与开源阵营，Beam 正式公布了 501B 总参数与 23B 激活参数的顶尖架构，本地化推理与端侧计算正在飞速追平云端性能；在软件协作与工业落地端，PaddleSpeech 等工业级语音工具链将字幕与多角色对齐彻底打磨至生产级水准，支付宝更是重磅设立“智能体涌现奖”，以数千万生态资金倒逼 Agent 从空谈走向真实生活服务闭环；而在内容与编剧一线，全国青年剧作评选与重点立项公示再度敲响警钟——技术越是唾手可得，作品的思想深度、时代立意与对普通人真实命运的悲悯，越是不可被算法替代的最高溢价。收心归位，锁定属于你自己的不可替代资产。',
        'scene': '「长假最后一天了，明天开工，你们团队第四季度的核心目标是什么？」「砍掉所有华而不实的 AI 概念功能，把核心业务的单位经济模型算清楚，把客户最痛的流程用本地工具做成闭环。稳扎稳打，活得比谁都久。」',
        'cover': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1600&auto=format&fit=crop&q=80',
        'closing': '''长假的最后一天，也是我们重新整装出发的起点。

过去这几天，当许多人还在沉醉于节日的闲适时，我们为你完整补齐了落下的每一期高密度日刊。回看这 6 天、216 篇精挑细选的深度资讯，从模型基座的演进，到一人公司的生存手感，再到剧作因果的严密骨架——**所有的线索都汇聚成了同一个方向：**

**不要做随波逐流的投机者，去做拥有确定性护城河的长期主义造物主。**

明天，第四季度的冲刺号角就要吹响。无论外面的世界如何吵闹，守住你的代码质量，守住你的商业利润，守住你讲好一个真实故事的初心。

这 36 篇最新的前沿思考，就是送给你的开工弹药。愿你在这个秋天，结出最丰硕的果实！''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'PaddleSpeech 开源工业级语音套件：端到端漫剧字幕语音对齐与合成流水线',
                'note': '百度飞桨核心语音全栈能力升级：提供从语音识别、跨语种语音合成到工业级精准音画时间轴对齐的一站式工具链，全面兼容主流漫剧后期制作工程。',
                'so_what': '工业级的稳定性和超低显存占用，让小型工作室也能像现代化装配车间一样，高标准、零误差地流水线化交付漫剧。',
                'source': 'github.com',
                'url': 'https://github.com/PaddlePaddle/PaddleSpeech',
                'media': 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '网络剧备案公示：古装与科幻漫剧 IP 改编风向及视听工业化评估细则',
                'note': '广电最新重点网剧立项报告：强调漫改真人剧或动画剧必须保留原著中最核心的人物精神特质，同时在特效镜头运用上注重真实物理视听规律。',
                'so_what': '漫改作品是当前最大的文化资产增量之一；尊重原作灵魂与遵循视听工业规律相结合，是漫剧破圈的关键钥匙。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/932',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '金茶花国际文创微短剧大赛启幕：数字漫剧与非遗文创跨界共创新路径',
                'note': '国际文创赛事权威指南：设立专项扶持赛道，鼓励数字漫剧团队深入非遗技艺、地域民族神话，用年轻一代喜闻乐见的高清漫剧形态重塑传统文化。',
                'so_what': '非遗与地域文化自带强大的审美势能与官方扶持背书；把 AI 漫剧技术用于赋能传统文明，兼具商业与社会价值。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/918',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '全国电视剧网络剧备案公示：严肃现实题材的情感抓手与戏剧爆发力',
                'note': '行业资深评委谈审读体会：面对大量同质化悬疑剧情，能够沉下心来描摹普通工人、教师或科研人员命运沉浮的作品，反而往往能在一分钟内打动评审。',
                'so_what': '生活本身就是最震撼的剧本；AI 漫剧不能只沉迷于仙侠打斗，多关注真实人间的悲欢离合，才能触及更广阔的大众市场。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/919',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '全国拍摄制作电视剧备案公示：重大社会议题戏剧化破题的心法与范式',
                'note': '国家级重点题材立项手记：如何将乡村振兴、老龄化社会与科技自强等宏大命题，拆解为家庭成员之间具体的理念冲突与利益纠葛，让政策语言化为生动对白。',
                'so_what': '宏大题材最忌概念化口号；用最微小的人物悲喜去映照时代的大江大河，戏剧才具有直击心灵的感染力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/888',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '2025 全国青年剧作计划评选揭晓：青年编剧在人物困境与时代命题中的探索',
                'note': '编剧行业年度奖项深度复盘：表彰那些不盲从流水线套路、敢于直面青年群体真实生存阵痛与精神求索的原创作品，剖析获奖剧作在情节结构上的过人之处。',
                'so_what': '行业永远渴望新鲜、真诚的声音；坚守自己独特的观察视角，不被短期的市场泡沫带偏，青年编剧才能迎来真正立得住的代表作。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/892',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '电影剧本（梗概）备案立项公示：故事骨架与立项审读要诀的深度剖析',
                'note': '资深审读专家亲授秘诀：如何用三句话精炼交代人物的核心欲望、不可调和的外部对抗力量以及故事最终升华的价值哲学，大幅提升报审立项通过率。',
                'so_what': '清晰是信心的外化；如果编剧自己都没法在短时间内讲透故事脊梁，就不能指望观众在影院里坐满两个小时。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/906',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '全国重点微短剧规划备案公示：剧情快节奏与反套路人物设计的实战范本',
                'note': '优秀微短剧备案梗概深度剖析：展示如何打破“千篇一律的完美主角”刻板印象，给主角设定鲜明而合乎人情的性格瑕疵，在剧情高速推进中制造意料之外的反转。',
                'so_what': '有缺陷的人物才可爱，有破绽的英雄才真实；反套路不是为了离经叛道，而是为了回归人性的复杂。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_necessary_info/909',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '弹性计算与异构算力调度：大模型基础设施架构师在成本风暴中的关键抉择',
                'note': '硬核算力架构实战复盘：深入剖析如何在昂贵的 H100 集群与性价比端侧 GPU 之间搭建动态感知路由，在保证服务 SLA 的同时将大促期间的推理总成本拉低 45%。',
                'so_what': '成本控制是企业长期生存的硬实力；懂调度、懂算力性价比的产品架构师，能在经济下行周期中为公司省下数千万真金白银。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473631.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '年轻人消费心智大变局：从单纯功能买单到情绪价值买单的产品定义新法则',
                'note': '新消费与互联网产品前沿洞察：单纯比拼功能参数的传统产品正在遭遇冷落，能够在物理交互、视觉美学与社群共鸣中提供治愈与自我认同的产品呈现爆发式增长。',
                'so_what': '功能是底线，情绪是上限；产品经理必须从冷冰冰的逻辑推演中走出来，深刻理解当代人在屏幕背后那颗渴望被抚慰的心。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6473828.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'DevEco Studio 插件集成实战：鸿蒙生态伙伴 SDK 接入的架构解耦与设计规范',
                'note': '移动端开发架构实战复盘：在全新生态环境下，如何通过模块化架构设计避免第三方 SDK 对核心代码库造成强耦合，保证系统的长期可维护性。',
                'so_what': '跨端与生态迁移考验的是系统解耦能力；前瞻性的模块化设计，能让产品在新机遇降临时以最轻盈的姿态快速接入。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6462980.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '支付宝设立“智能体涌现奖”与无人机航线开通：技术奇点下的实体生活服务融合',
                'note': '蚂蚁集团与美团最新落地动作：设立专项生态基金重奖能够切实解决医疗挂号、养老照护与本地低空配送痛点的端到端智能体，推动 AI 全面深入烟火人间。',
                'so_what': 'AI 的终局不在赛博空间，在柴米油盐；将智能体真正接入实体世界的物理履约，将激发出无法估量的巨大社会与经济价值。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pmd/6463225.html',
                'media': 'https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

# Process each day sequentially
days_order = ['2026-10-01', '2026-10-02', '2026-10-03', '2026-10-04', '2026-10-05', '2026-10-06']
target_categories = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']

for d in days_order:
    dd = d.split('-')[-1]
    raw_path = f'scripts/raw-ian-{dd}.json'
    with open(raw_path, 'r', encoding='utf-8') as f:
        raw_items = json.load(f)
    
    # Filter fresh items from ian by category
    ian_by_cat = {}
    for it in raw_items:
        u = it['url']
        c = it['category']
        if u not in used_set and c in target_categories:
            ian_by_cat.setdefault(c, []).append(it)
    
    day_items = []
    
    # 1. Take 4 items for each of the 6 ian categories
    for c in target_categories:
        avail = ian_by_cat.get(c, [])
        if c == 'AI 资讯' and d == '2026-10-05':
            # Day 05 has 3 from ian + 1 supplemental
            picked = avail[:3]
            for p in picked:
                used_set.add(p['url'])
                day_items.append({
                    'category': c,
                    'title': p['title'],
                    'note': p['judgment'],
                    'so_what': '保持对前沿技术的敏锐度，聚焦具有确定性工程价值的技术进展。',
                    'source': p['source'],
                    'url': p['url'],
                    'media': p['media'] or 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                    'pinned': len(day_items) % 4 < 2
                })
            # Add supplement
            supp = vertical_data[d]['ai_news_supp']
            used_set.add(supp['url'])
            day_items.append(supp)
        else:
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

    # 2. Add the 3 vertical categories (4 items each)
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

    # Ensure categories are grouped logically
    cat_order = ['AI 资讯', 'AI 协作', '一人公司', '产品设计', '审美提升', '产品营销', 'AI 漫剧', '编剧技巧', '产品经理']
    sorted_items = []
    for co in cat_order:
        sorted_items.extend([it for it in day_items if it['category'] == co])
        
    # Build markdown
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

# Save updated all-used-urls.json
all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating all 6 days! Total URLs in history: {len(all_used_list)}')
