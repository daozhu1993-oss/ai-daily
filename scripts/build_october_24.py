# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-24': {
        'title': '10 月 24 日 · 运行时实证与逆向守门：当智能体开始学会“对自己负责”',
        'highlights': '全网 9 大领域 36 篇高密度精选：Kimi K3.1 Pro 杀进全球前四、ElevenLabs 发布端到端实时语音全套系统、Mac 本地 Agent 权限看门狗与危险 SQL 语义拦截门禁、短剧重塑传统长视频生态、双11预售定金尾款逆向履约底层资产设计全拆解。',
        'epigraph': '真正可靠的系统，从不把“可能正常”当成交付标准；在执行之前拦截危险，在执行之中留存凭据，才是智能体接管真实世界的核心底气。',
        'lead': '10 月 24 日，大模型工程落地与应用操盘正在从“浮躁的参数追逐”全面转向“运行时的确定性防御与业务硬核履约”。在这个属于程序员的节日（1024），一线开发者最关心的不再是虚幻的跑分，而是代码在真实生产环境中的稳健与安全：在基础模型端，月之暗面重磅上线 Kimi K3.1 Pro，以百万级超长上下文与极速推理能力在代码与长任务基准上杀入全球前列；ElevenLabs 则推出 Eleven Realtime，将语音识别、打断处理与双向模型调校打造成一体化端到端实时语音系统；在协作与安全防御端，开发者开始为 Agent 铸造硬核防线——从在 Mac 钥匙串和插件中布设权限看门狗，到在数据库执行之前拦截无条件危险 SQL，再到在额度消耗殆尽前设置预算熔断器，人机协作正在迅速建立“免受反噬”的安全共识；而在消费与微短剧前沿，短剧生态对传统影视平台造成降维冲击，AI 原生娱乐从单点角色聊天迈向互动叙事世界，电商双十一对定金尾款全链路履约资产的深度设计，更为所有商业产品经理敲响了“回归业务底层骨架”的沉重警钟。',
        'scene': '「为什么要在智能体执行 SQL 之前加一层 AST 语法树拦截？大模型不是已经写好了 WHERE 条件吗？」「大模型会产生幻觉，但删掉的生产数据永远不会自动长回来。让模型拥有执行权的前提，是把物理世界的安全熔断器死死掌握在确定性的代码手里。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周六，也是一年一度的 1024 程序员节。

今天整理这 36 篇精选时，最让我触动的，是 **整个行业对“确定性与责任底线”的深刻回归**。

在早期的 AI 狂欢中，人们沉迷于智能体能够“自动做很多事”的爽感；
但真正把 Agent 放到真实生产线、真实账本与真实数据库面前时，团队才发现：
**比起“会做什么”，更致命的是“它会不会在不经意间毁掉什么”。**

因此，今天我们看到了如此密集的“守门”工具：
有人在 Mac 本地严防 Agent 越权触碰钥匙串，
有人在数据库执行前用 AST 语法树死死拦住没有条件的 DELETE，
有人在额度见底之前果断拉下算力电闸……

这正是技术走向成熟的标志：
**真正的成熟，不是无所顾忌地狂奔，而是学会在关键边界处刹车。**
在这个属于造物者的节日里，愿你的代码永远清晰稳健，愿你的智能体在确定性的护栏中，为你创造持久的确定性复利。程序员节快乐！''',
        'ai_news': [
            {
                'category': 'AI 资讯',
                'title': 'Kimi K3.1 Pro 上线长上下文与高速版本',
                'note': '月之暗面重磅发布的生产级长任务模型：支持百万级超长上下文窗口与极速端到端生成，针对复杂长程编码与高频智能体工具调用深度调优，API 已全量开放。',
                'so_what': '国产前沿长上下文代码基座的重大跨越；为全天候大型代码库重构与自主 Agent 闭环提供了低延迟、高可用的算力底座。',
                'source': 'kimi.com',
                'url': 'https://www.kimi.com/blog/kimi-k3-1-pro',
                'media': 'https://iandaily.xyz/digest/2026-10-24-kimik31-4fa68e544b39.jpg',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'Eleven Realtime 把语音轮转接成一套系统',
                'note': '语音交互独角兽推出的端到端实时语音对话栈：提供 Mini 自然闲聊与 Max 复杂任务双模形态，将语音识别、语义理解、拟真声音与用户打断处理整合成极低延迟流水线。',
                'so_what': '终结传统语音链路拼装的卡顿痛点；端到端打断与情绪响应让智能体具备真正符合人类听觉直觉的自然交互体验。',
                'source': 'elevenlabs.io',
                'url': 'https://elevenlabs.io/realtime',
                'media': 'https://iandaily.xyz/digest/2026-10-24-elevenrealtime-cc555b864a41.jpg',
                'pinned': True
            },
            {
                'category': 'AI 资讯',
                'title': 'fal 发布面向快速迭代的 FLUX 3 Max',
                'note': '基于 FLUX 3 深度后训练的极速视频生成管线：原生支持文本与单图一键扩展为高帧率动态视频，在保持画质与运动一致性的同时将单镜推理耗时大幅压缩。',
                'so_what': '视听漫剧快速试错的生产力杠杆；让分镜师在几分钟内批量验证动态运镜与景别构图，极大缩短前期资产探索周期。',
                'source': 'fal.ai',
                'url': 'https://fal.ai/flux-3-max',
                'media': 'https://iandaily.xyz/digest/2026-10-24-flux3max-f6934a57a6f2.jpg',
                'pinned': False
            },
            {
                'category': 'AI 资讯',
                'title': 'Clairic 给抽取字段同时返回位置与置信度',
                'note': 'Cloudflare 官方开源的高效非结构化信息抽取模型：在提取实体信息的同时精确定位原文行段与置信度打分，支持空值兜底与强类型输出，专为复杂长文档自动化设计。',
                'so_what': '把模型信息抽取从“不可测黑盒”升级为“可审计凭据”；为后续数据库写入与业务履约提供了极具确定性的防御门禁。',
                'source': 'blog.cloudflare.com',
                'url': 'https://blog.cloudflare.com/clairic-extraction-model/',
                'media': 'https://iandaily.xyz/digest/2026-10-24-clairic-9b02adb4b3cf.jpg',
                'pinned': False
            }
        ],
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI WAS Node Suite：专业影视后期图像混叠、多层批处理与音视频处理套件',
                'note': 'AI 漫剧制片工业化的顶级节点军火库：提供 200+ 生产级节点，覆盖图层通道混合、蒙版动态羽化、色彩校准与音视频波形帧对齐，满足长篇漫剧的高精渲染需求。',
                'so_what': '把零散出图升维为专业数字影视后期流水线；用标准化的节点消除批处理瑕疵，为长篇漫剧的高频稳定交付筑牢地基。',
                'source': 'github.com',
                'url': 'https://github.com/WASasquatch/was-node-suite-comfyui',
                'media': 'https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '从角色聊天到互动叙事世界：AI原生娱乐的下一站',
                'note': '生成式 AI 在视听与互动娱乐领域演进的深度研判：分析行业如何从单薄的“拟人伴侣聊天”跨越至拥有连贯剧情、多角色博弈与玩家选择反馈的动态互动叙事大世界。',
                'so_what': 'AI 漫剧与互动影游的融合终局；揭示未来爆款娱乐内容不仅要有电影级视听，更要依托世界观状态机实现真正的沉浸式代入。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6483642.html',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': '被嘲笑土鳖的短剧，正在让优爱腾芒“去死”？传统影视工业的颠覆与重构',
                'note': '长短视频行业格局剧变的重磅复盘：揭示微短剧如何以极致的生产效率、高频情绪爽点与敏捷成本结构，全面蚕食传统长视频平台的开机时长与广告大盘。',
                'so_what': '影视工业制造逻辑的不可逆颠覆；传统影视人必须放下傲慢，学习微短剧的黄金 3 秒抓手与情绪价值供给，完成敏捷自我迭代。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/it/6483634.html',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《教授的杀意》科幻微短剧：AI 伦理失控与硬核悬疑推理商业全案',
                'note': '高概念科技悬疑微短剧剧作范本：围绕顶尖高校人工智能实验室的一桩离奇密室死亡案展开，将前沿大模型安全对抗、学术剽窃与心理博弈严密嵌套，反转迭起。',
                'so_what': '科技前沿热点与密室推理的深度结合；精准契合当代年轻极客群体的审美趣味，为 AI 漫剧制作团队提供了兼具思想深度与戏剧爆点的优质资产。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1808',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '《停尸间的嘴替》都市职业悬疑短剧：法医视角下的冷酷推理与黑色幽默',
                'note': '职业类型短剧的破圈写法拆解：以一位性格孤僻但业务极强的毒舌青年法医为主角，用死者伤痕倒推真相，将硬核病理学知识与职场黑色幽默巧妙缝合。',
                'so_what': '冷门职业剧快速建立观众信任的方法论；用绝对扎实的专业细节打造降维打击爽感，展现差异化人设在悬疑短剧中的强大吸睛力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1806',
                'media': 'https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《榜一猎人》都市现实题材短剧：网络直播生态反诈与猎手博弈的悬疑节奏',
                'note': '贴地飞行的下沉市场现实主义力作：聚焦秀场直播打赏与杀猪盘黑产，以伪装成神秘“榜一大哥”的反诈猎手为主线，层层撕开直播间的情绪操控骗局。',
                'so_what': '现实主义题材在网络短剧中的情绪引爆点；紧扣大众身边的真实痛点与人性的贪婪软肋，兼具强悬疑观赏性与巨大社会警示价值。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1810',
                'media': 'https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '《道情密语：1942青凉寺》年代谍战短剧：跨时空悬疑解密与多线暗号编织',
                'note': '高难度谍战微短剧的情节密度掌控：围绕抗战时期一座千年古刹中隐藏的加密电台，通过道情戏曲声腔、香火气味与经卷夹层设计多重暗号，悬念环环相扣。',
                'so_what': '传统民俗非遗元素与硬核谍战的戏剧化融合；证明短剧即使在小成本限制下，依靠精密的因果网与暗号编排同样能写出院线级窒息紧迫感。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1813',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '《风吹八零，绒花似锦》年代女性创业短剧：非遗传承与时代浪潮中的爽感落地',
                'note': '非遗文旅与大女主搞钱题材的精妙结合：主角重回改革开放初期，凭借祖传非遗绒花手艺力抗家族破产危机，一步步将传统老手艺推向广交会与国际舞台。',
                'so_what': '大女主逆袭题材如何跳出情爱撕逼泥潭；把女性自我价值实现与真实商业实干深度绑定，赢得更具消费力受众的长线共鸣。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/1812',
                'media': 'https://images.unsplash.com/photo-1461360370896-922624d12aa1?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': '双11预售开始了：定金、尾款与逆向履约退款的底层产品资产设计',
                'note': '电商大促交易中枢核心资产架构全景复盘：抽丝剥茧拆解复杂预售场景下的定金膨胀、跨店凑单、限时尾款支付以及售后逆向拦截等数十个边界状态机。',
                'so_what': '高阶交易产品经理的基本功底线；只有把订单状态机与资金流、货品流严丝合缝闭环，系统才能扛住数亿级并发与极端薅羊毛风控。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/pd/6483649.html',
                'media': 'https://images.unsplash.com/photo-1556742049-0a67e557224d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '闲鱼用户交易痛点分析与改进思路：C2C 信任机制与逆向纠纷闭环',
                'note': 'C2C 非标二手交易平台的深度产品体检：直击“货不对板、到手刀、恶意退款”等核心顽疾，系统推演信用分级质押、验货宝流程前置与小法庭机制优化。',
                'so_what': '平台型产品经理的博弈机制设计修养；治理非标交易的本质是设计合理的利益制衡机制，用制度约束消除平台交易摩擦。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/evaluating/6483248.html',
                'media': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '花 499元给猫买个 AI 项圈：宠物硬件 Agent 的拟人化交互与场景创新',
                'note': '软硬件结合宠物消费赛道的爆款产品复盘：通过项圈传感器采集宠物运动与叫声，结合多模态大模型自动生成幽默诙谐的“猫咪第一人称日记”推送到手机。',
                'so_what': '情感代偿与硬件 Agent 的黄金切角；证明大模型在消费电子领域的最大机会往往不在于高大上的生产力工具，而在于提供无可替代的情绪价值。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/chuangye/6483396.html',
                'media': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': '别再争谁是“中国版Muse”了：卖铲子的 ICT 厂商先赚到了钱与基础设施账本',
                'note': '大模型应用狂热背后的冷静商业账本透视：当消费级 AI 应用还在为了留存与高昂算力补贴苦苦挣扎时，底层光模块、液冷算力与高速交换网络厂商早已赚得盆满钵满。',
                'so_what': '穿越技术炒作周期的商业理性思考；看清产业链价值分配格局，要么做离真实交付最近的垂直闭环，要么做不可或缺的基础设施卖铲人。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6483646.html',
                'media': 'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

# 2. Curated Ian picks (20 items across 5 categories)
raw_ian_path = 'scripts/raw-ian-24.json'
with open(raw_ian_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

curated_ian_picks = {
    'AI 协作': [
        'https://installplango.com/',
        'https://vericto.com/',
        'https://peras.vertias.eu/',
        'https://corgi.computer/'
    ],
    '一人公司': [
        'https://headsup.benvenutisoftware.com/',
        'https://taveo.app/en',
        'https://www.cryptex-vault.com/',
        'https://github.com/alisheryeginbay/amgi'
    ],
    '产品设计': [
        'https://withbeckon.app/',
        'https://useinstantsearch.com/',
        'https://gotemail.net/',
        'https://www.impossiblemachines.xyz'
    ],
    '审美提升': [
        'https://www.wallpaper.com/tech/fender-x-paul-smith-telecaster',
        'https://www.designboom.com/architecture/jean-prouve-1944-demountable-house-japanese-tea-pavilion-design-miami-paris-2026-galerie-patrick-seguin/',
        'https://www.designboom.com/architecture/snohetta-barth-spaces-le-rosey-boarding-school/',
        'https://www.designboom.com/architecture/oma-potato-head-good-times-general-store-bali-indonesia/'
    ],
    '产品营销': [
        'https://monid.ai/rankings',
        'https://www.producthunt.com/posts/product-hunt-visual-launch-editor',
        'https://dub.co/startups',
        'https://marketmee.app'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://installplango.com/': '防范 AI 供应链投毒与越权操作的系统级护栏；给拥有终端操作权的本地 Agent 戴上安全金箍，防止开发机敏感资产外泄。',
    'https://vericto.com/': '智能体接管真实生产数据库的刚性门禁；把模型写 SQL 产生的灾难性失误消灭在网络传输阶段，守住企业数据资产底线。',
    'https://peras.vertias.eu/': '勒住自主智能体死循环调用的算力缰绳；防止 Agent 在深夜静默陷入调试死循环导致团队月末遭遇数千美元天价账单。',
    'https://corgi.computer/': '终结多终端切屏的上下文迷航；让人类架构师在并发调度多个 Agent 时保持清晰全局视界，从容处理关键决策。',
    'https://headsup.benvenutisoftware.com/': '单兵开发微产品的经典设计哲学；直击远程工作者“沉迷编码错过开会”的强痛点，以极简交付与买断制赢得稳定现金流。',
    'https://taveo.app/en': '把产品使用门槛削到绝对极致的典范；消除社交场景下的下载与账号摩擦，靠极致易用性实现口碑自发裂变。',
    'https://www.cryptex-vault.com/': '在云端服务频繁暴雷时代重塑数据主权；把核心资产留给本地加密算法，让独立开发者彻底告别中心化账密泄漏风险。',
    'https://github.com/alisheryeginbay/amgi': '拒绝封闭专有数据库的格式主权觉醒；让个人的终身学习记忆资产随纯文本永久流传，消除对特定工具的依赖绑定。',
    'https://withbeckon.app/': '对既有桌面窗口切换定式的优雅升维；利用人类肌肉记忆的放射手势，把每日数百次的切换摩擦降至零感知。',
    'https://useinstantsearch.com/': '终结“文件名想不起来就找不到文件”的抓狂体验；用现代轻量向量检索技术重塑本地文件系统，极大释放知识工作者生产力。',
    'https://gotemail.net/': '化硬件槽点为交互焦点的神来之笔；在不打扰深度工作心流的前提下，把边缘通知做成精致优雅的环境微交互。',
    'https://www.impossiblemachines.xyz': '声明式编程范式向实体物理世界的伟大跨界；让非专业工程师也能凭借纯粹的目标直觉，完成复杂机构设计。',
    'https://www.wallpaper.com/tech/fender-x-paul-smith-telecaster': '跨界联名审美的高级示范；不是粗暴贴牌印刷，而是让时装色彩节奏与乐器木质肌理产生深刻的工业美学共鸣。',
    'https://www.designboom.com/architecture/jean-prouve-1944-demountable-house-japanese-tea-pavilion-design-miami-paris-2026-galerie-patrick-seguin/': '工业实用主义与东方精神空间的绝妙平衡；证明优秀的结构设计具有超越时代的容器属性，能自如包容截然不同的文化意境。',
    'https://www.designboom.com/architecture/snohetta-barth-spaces-le-rosey-boarding-school/': '空间形态对教育关系的深层重塑；用流动的物理动线替代冰冷的纪律规训，让空间本身成为启迪心智的隐形导师。',
    'https://www.designboom.com/architecture/oma-potato-head-good-times-general-store-bali-indonesia/': '可持续商业理念在零售空间的具象化呈现；将幕后的材料循环转化为前台的核心审美焦点，赋予商业消费深厚的可持续尊严。',
    'https://monid.ai/rankings': '穿透喧嚣看清真实需求的商业试金石；帮助出海独立开发者看准到底哪些垂直 Agent 正在被真实用户高频买单。',
    'https://www.producthunt.com/posts/product-hunt-visual-launch-editor': '消除产品发布者的临场认知摩擦；所见即所得的极简交互大幅提升上线信心，让产品首发如呼吸般顺畅。',
    'https://dub.co/startups': '早期 SaaS 启动全民分销的低成本快车道；用成熟的佣金基础设施撬动忠实用户的裂变传播，低风险撬动冷启动增长。',
    'https://marketmee.app': '终结独立开发者“会写代码不会营销”的长期阵痛；让每一次构建发布都自动转化为高转化的多渠道公关事件。'
}

day_items = []

# 1. AI 资讯 (from vertical_data)
v_info = vertical_data['2026-10-24']
for news in v_info['ai_news']:
    used_set.add(news['url'])
    day_items.append(news)

# 2. 5 ian categories × 4 items
target_5_categories = ['AI 协作', '一人公司', '产品设计', '审美提升', '产品营销']
for c in target_5_categories:
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

# 3. 3 vertical categories × 4 items
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
date: '2026-10-24'
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

out_file = 'src/content/daily/2026-10-24.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-24! Total URLs in history: {len(all_used_list)}')
