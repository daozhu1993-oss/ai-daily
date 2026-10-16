# -*- coding: utf-8 -*-
import json
import os

used_urls_path = 'scripts/all-used-urls.json'
with open(used_urls_path, 'r', encoding='utf-8') as f:
    used_urls = json.load(f)

used_set = set(used_urls)

vertical_data = {
    '2026-10-16': {
        'title': '10 月 16 日 · 分布式协同与前进部署：当 AI 从单点生成走向企业深水区',
        'highlights': '全网 9 大领域 36 篇高密度精选：Meta 开源 Muse Spark 视听权重、Claude Code Review 全面开放、苹果 MLX 实现四台 Mac Studio 分布式推理、Anthropic 投入一亿美元培训一万名 FDE 前进部署工程师、Cloudflare 与 OpenAI 探索智能体网页发现协议。',
        'epigraph': '软件行业从来不缺写 Demo 的天才，真正稀缺的，是那些愿意穿上工服扎进企业一线、把不可预测的模型改造成坚不可摧生产底座的前进部署者。',
        'lead': '10 月 16 日，AI 产业的一线战事正在发生一次里程碑式的战略迁徙：单点模型的“炫技时代”宣告终结，重构企业协同与分布式基础设施的“深水区时代”全面降临。在底层模型与硬件架构端，Meta 罕见开源 Muse Spark Open 视听大模型权重，苹果 MLX 框架则正式验证了仅靠 4 台消费级 Mac Studio 即可跑通高吞吐分布式推理，算力去中心化正成为现实；在智能体与开发协同端，Claude Code Review 向全量团队组织开放，Polylane 与 withHuman 不约而同地把重心放在“生产环境影响面审计与人工权限审批”，Agent 的失控风险被牢牢框入沙箱；在商业操盘与落地一线，Anthropic 投下重磅炸弹——宣布投入 1 亿美元为行业培养 1 万名 FDE（Forward Deployed Engineer，前进部署工程师），这不仅是向传统软件交付模式的致敬，更宣告了 AI 落地已彻底摆脱“卖 API 躺赚”的幻想，必须深扎客户业务现场定制闭环；在视听与内容工业端，ComfyUI FizzNodes 带来关键帧与运镜权重的高精插值调度，120 集 AI 辅助科幻微短剧《冰封方舟》全本交付，展现了算法与人工打磨协同下的内容产能跃升。',
        'scene': '「模型越来越强，为什么大厂反而开始重金招募驻场交付工程师了？」「因为客户的核心系统不是游乐场。哪怕大模型写代码快十倍，谁去帮客户梳理三十年遗留的脏数据？谁去在断网环境下搭建高可用容灾？最后能收到尾款的，永远是敢在现场解决最后一个 BUG 的人。」',
        'cover': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=1600&auto=format&fit=crop&q=80',
        'closing': '''今天是周五。

今天读完这 36 篇精选，我感触最深的一个行业信号，就是 **Anthropic 豪掷 1 亿美元培养 1 万名 FDE（前进部署工程师）**。

这个动作极具风向标意义。
在过去两年里，硅谷的大模型叙事一直充斥着“超级智能一键取代所有软件与人力”的狂妄；
但走到今天，哪怕是拥有最强模型的 Anthropic，也不得不承认一个朴素的商业现实：
**客户的业务不是由完美的 API 构成的，而是由无数脏数据、历史遗留系统、部门利益博弈与严苛的合规条款交织而成的泥潭。**

光靠隔空卖 Token，救不了陷入停滞的企业交付；
真正能把 AI 转化为生产力利润的，是那些既懂大模型架构、又懂业务系统、愿意走到现场去啃硬骨头的工程操盘手。

给所有正在转型中的产品人与开发者的建议：
不要再沉迷于做一个只会在群里转发新产品发布会的“AI 观察家”。
走入具体的行业，去搞清楚一家外贸工厂怎么排期、一家医疗机构怎么对账、一个漫剧团队怎么锁定角色分镜。

在泥泞中构建出确定性的交付系统，那才是你在这个时代不可被算法替代的最高壁垒。

祝你周末愉快。''',
        'ai_drama': [
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI FizzNodes 关键帧调度套件：精准控制漫剧镜头运镜与动态权重插值',
                'note': '漫剧动态镜头调度的核心枢纽：支持用数学公式与贝塞尔曲线对提示词权重、运动模块与相机运镜进行精细插值，彻底解决长镜头视角跳变与动作僵硬。',
                'so_what': '告别靠运气抽卡的动态生成；掌握关键帧权重数学调度，才能在 ComfyUI 里重塑电影级推拉摇移运镜控制。',
                'source': 'github.com',
                'url': 'https://github.com/FizzleDorf/ComfyUI_FizzNodes',
                'media': 'https://images.unsplash.com/photo-1578632767115-351597cf2477?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'ComfyUI-Manager 扩展生态中枢：漫剧工业化流水线节点依赖管理与模型自动化部署',
                'note': '漫剧制作团队工程化标准底盘：一键管理成百上千个复杂自定义节点、显存优化补丁与模型权重版本同步，消除团队协作中的环境配置黑洞。',
                'so_what': '工业化交付的前提是工作流跨工作站一致；标准化的节点包管理器是漫剧工作室规模化分工的基石。',
                'source': 'github.com',
                'url': 'https://github.com/ltdrdata/ComfyUI-Manager',
                'media': 'https://images.unsplash.com/photo-1534447677768-be436bb09401?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': 'AI 漫剧',
                'title': 'Krea 3 生成式视听生产工作台：将局部重绘、动态扩图与镜头运动统一在无级画布中',
                'note': '新一代视听生产力画布：打破单帧出图与后期视频软件的割裂，创作者可在同一空间内直接框选画面局部进行微动态注入、角色修面与运镜推移。',
                'so_what': '交互画布正在取代线性时间轴；在无级空间内完成从概念分镜到成片动态修正，极大压缩了漫剧迭代周期。',
                'source': 'krea.ai',
                'url': 'https://www.krea.ai/krea-3',
                'media': 'https://images.unsplash.com/photo-1485846234645-a62644f84728?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': 'AI 漫剧',
                'title': '《冰封方舟》末日科幻微短剧 全 120 集：AI 辅助创作与竖屏短剧全本商业交割',
                'note': '末世求生高概念短剧商业交割样本：全 120 集竖屏短剧剧本，借助 AI 快速搭建极寒方舟科技设定与孤寂人设，人工深度润色情感拉扯与生死抉择。',
                'so_what': 'AI 辅助长线叙事全面跑通；从设定生成到分集冲突打磨，人机协同已成为微短剧低成本高产出的标准模式。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1756',
                'media': 'https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'screenplay': [
            {
                'category': '编剧技巧',
                'title': '蚀光纪元（20 分钟 40 集末世微短剧）：多线索权谋叙事与末日人性抉择',
                'note': '硬核废土题材剧本创作范式拆解：借鉴经典史诗的多方阵营制衡架构，在生存资源极限压迫下，把个人复仇升华为人道主义信仰的坚守。',
                'so_what': '格局决定故事上限；即使在快节奏的微短剧中，引入多阵营博弈与价值观撕裂，也能赋予作品震撼的厚重感。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/2169',
                'media': 'https://images.unsplash.com/photo-1455390582262-044cdead277a?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '那一夜，我们说相声：赖声川传统曲艺母题解构与消逝岁月的戏剧回响',
                'note': '华语戏剧里程碑经典剧作结构复盘：以说相声这一濒临消亡的民间艺术形式为外壳，层层剥开台北、重庆直至北平的文化记忆断层，笑中带泪。',
                'so_what': '最高级的喜剧内核是悲剧；用荒诞的形式包裹对文明与时间消逝的痛惜，故事才能穿越时代产生永恒共振。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/2174',
                'media': 'https://images.unsplash.com/photo-1457369804613-52c61a468e7d?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '编剧技巧',
                'title': '她死于 1988（刑侦犯罪悬疑剧）：双时空积案穿透与至亲谎言下的情感救赎',
                'note': '社会派刑侦剧本构思心法：一盘旧磁带串起十三年两代人的谎言与秘密，真正的悬念不仅在于抓到真凶，更在于撕开至亲之间以爱为名的残忍遮蔽。',
                'so_what': '悬疑剧的终点是伦理审视；让凶案成为照妖镜，映照出家庭中隐秘的自私与妥协，悬疑才能直抵人心。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/script_info/2170',
                'media': 'https://images.unsplash.com/photo-1450133064473-71024230f91b?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '编剧技巧',
                'title': '原创 60 集都市喜剧小品《银发强国歌》：老龄化社区风貌与接地气烟火微冲突',
                'note': '银发赛道喜剧剧本创作实操：取材真实社区老年人日常，拒绝刻板说教，用生活化微误会与幽默拌嘴传递积极豁达的老年心境。',
                'so_what': '精准踩中人口结构红利；关注被主流商业短剧忽视的银发族精神世界，具有极高的社会效益与下沉市场潜力。',
                'source': 'wzbj1616.com',
                'url': 'https://www.wzbj1616.com/sign_script_info/1765',
                'media': 'https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ],
        'pm': [
            {
                'category': '产品经理',
                'title': 'Anthropic 开班：投入 1 亿美金培训 1 万名 FDE 前进部署工程师',
                'note': '大模型大厂商业战略重大转折：隔空调用 API 无法攻克大客户最后一公里，亲自重金培训深入企业内网搞定制、洗数据、搭流水线的驻场特战队。',
                'so_what': '纯软件神话破灭；懂模型又懂客户业务泥泞的“前进部署工程师”正在成为 AI 商业落地阶段最核心的操盘手。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473804.html',
                'media': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': '腾讯悄悄做了个免费 AI 接待员：上传文档就能替你回复访客',
                'note': '巨头入局垂直轻量客服工具：将复杂的 RAG 知识库配置极简化为“上传 PDF 即可上线”，直击中小微企业低成本获客与咨询的痛点。',
                'so_what': '大厂正在把低阶 AI 包装功能打成免费基建；做中间层工具的团队必须迅速向深度业务履约和工作流整合撤退。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473812.html',
                'media': 'https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=800&auto=format&fit=crop&q=80',
                'pinned': True
            },
            {
                'category': '产品经理',
                'title': 'DeepSeek 拟人形象大战：AI 产品的角色 IP 化与社区情感护城河',
                'note': '大模型技术产品化与人格化深度复盘：当模型技术能力差距不断缩小时，具有鲜明性格主张、视觉符号与社区二创土壤的拟人形象，正在成为独特的心智资产。',
                'so_what': '参数无情，情绪无价；在冷冰冰的技术之上赋予产品独特的拟人温度，能激发难以被技术追赶替代的社区归属感。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473818.html',
                'media': 'https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            },
            {
                'category': '产品经理',
                'title': 'AI 老和我抢网页，我给它配了个专用浏览器：人机环境隔离与专属执行沙箱设计',
                'note': '自动化智能体桌面端实操痛点与架构解决：将 Agent 的无头自动化操作与人类主机的日常工作区进行严格的浏览器沙箱隔离，消除 Cookie 冲突与窗口争抢。',
                'so_what': '优秀的产品经理善于从日常微小别扭中提炼架构；物理与环境隔离是构建长效人机协同系统的基础卫生标准。',
                'source': 'woshipm.com',
                'url': 'https://www.woshipm.com/ai/6473802.html',
                'media': 'https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80',
                'pinned': False
            }
        ]
    }
}

raw_path = 'scripts/raw-ian-16.json'
with open(raw_path, 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Select curated items for the 6 ian categories
curated_ian_picks = {
    'AI 资讯': [
        'https://pytorch.org/blog/muse-spark-open/',
        'https://claude.com/blog/code-review-is-now-generally-available',
        'https://bfl.ai/blog/flux-3-image-klein',
        'https://machinelearning.apple.com/research/mlx-distributed-inference'
    ],
    'AI 协作': [
        'https://polylane.com/use-cases/impact-analysis/',
        'https://github.com/cshum/imagor-mcp',
        'https://withhuman.ai/',
        'https://navige.ai/'
    ],
    '一人公司': [
        'https://unfenced.land/',
        'https://belownew.com/',
        'https://tryearshot.net/index.html',
        'https://routeeditor.com/'
    ],
    '产品设计': [
        'https://sygal.app',
        'https://apps.apple.com/us/app/diagrammar-mermaid-diagram/id6799964195',
        'https://theorem.fundaments.work/',
        'https://reelbird.app/'
    ],
    '审美提升': [
        'https://www.designboom.com/readers/moyo-shirt-jacket-korean-hanbok-silhouette-east-african-kitenge-textile-jerrybag-hyunah-kim-ili-studio/',
        'https://www.itsnicethat.com/articles/nicer-tuesdays-london-september-foam-magazine-151026',
        'https://www.designboom.com/architecture/mycelium-hypha-lume-pavilion-human-movement-light/',
        'https://www.dezeen.com/2026/10/15/schemata-architects-linden-house/'
    ],
    '产品营销': [
        'https://blog.cloudflare.com/cloudflare-openai-discovery-agentic-web/',
        'https://github.com/zachbrown29/lintel-marketing-playbooks',
        'https://forwarder.cc',
        'https://chatway.app/'
    ]
}

# Lookup dictionary for raw items
raw_by_url = {it['url']: it for it in raw_items}

# Custom so_what mapping for curated ian items to ensure top editorial depth
so_what_overrides = {
    'https://pytorch.org/blog/muse-spark-open/': '多模态视听基座全面拥抱开源；掌握原生多模态联合生成框架，打破音画孤岛。',
    'https://claude.com/blog/code-review-is-now-generally-available': '代码评审进入智能体自治时代；将大模型审查前置到 Git 工作流中，将低级缺陷扼杀在合入主干之前。',
    'https://bfl.ai/blog/flux-3-image-klein': '图像扩散模型迎来跨参考图高保真编辑突破；多图参考风格与主体特征对齐，奠定商业设计交付底座。',
    'https://machinelearning.apple.com/research/mlx-distributed-inference': '消费级工作站分布式算力迎来质变；无需昂贵数据中心，四台 Mac 组网即可低成本跑通千亿大模型。',
    'https://polylane.com/use-cases/impact-analysis/': '把代码合并的盲盒风险彻底透明化；在仿真生产环境中预先推演 PR 影响面，是系统高可用的防浪堤。',
    'https://github.com/cshum/imagor-mcp': '图片处理协议全面标准化；将复杂的裁剪、排版与滤镜封装为单个 MCP 网址，极大减轻了智能体调用负担。',
    'https://withhuman.ai/': '在失控与全自动之间架设安全刹车阀；敏感操作强制人工批准，是智能体被企业严肃采购的底线前提。',
    'https://navige.ai/': '防止递归死循环刷爆账单；在 Agent 执行层设置精准的成本预算与调用熔断，是精细化运营的必修课。',
    'https://unfenced.land/': '极其锋利的垂直利基切角；专为特定土地买家解决无边界地块痛点，展示了一人公司选品的绝佳嗅觉。',
    'https://belownew.com/': '绿色循环经济时代的价值比对工具；把全新、官翻与二手行情并排呈现，帮理性消费者算清全生命周期成本。',
    'https://tryearshot.net/index.html': '旧硬件资产的灵性再利用；闲置手机化身低成本环境声音哨兵，不依赖云端即可守护家庭安全。',
    'https://routeeditor.com/': '户外小众爱好者的硬核刚需；在极简交互下完成 GPX 轨迹修剪与断点接合，展示了工具软件克制之美。',
    'https://sygal.app': '回归文档最质朴的本质；将臃肿格式转化为纯净纯文本，把数据控制权与终极轻快还给专业用户。',
    'https://apps.apple.com/us/app/diagrammar-mermaid-diagram/id6799964195': '离线设备端原生图形绘制体验；用文本思维快速具象化复杂架构与业务泳道，消灭繁琐拖拽。',
    'https://theorem.fundaments.work/': '让数字阅读划线真正沉淀为个人资产；无缝直通本地 Markdown 库，击破封闭笔记应用的围墙花园。',
    'https://reelbird.app/': '把隐私与算力牢牢锁在本地设备；无需担心敏感业务录屏泄露到云端，重塑专业视频工具的安全感。',
    'https://www.designboom.com/readers/moyo-shirt-jacket-korean-hanbok-silhouette-east-african-kitenge-textile-jerrybag-hyunah-kim-ili-studio/': '跨大洲传统文化的重构实验；把东方儒雅轮廓注入东非浓烈蜡染，展现了跨媒介与跨地域美学的无限活力。',
    'https://www.itsnicethat.com/articles/nicer-tuesdays-london-september-foam-magazine-151026': '纸质刊物在数字时代的从容定力；二十五年排版与印刷材料的迭代，见证了实体阅读无可替代的质感。',
    'https://www.designboom.com/architecture/mycelium-hypha-lume-pavilion-human-movement-light/': '有机生物材料与空间感知的对话；菌丝体模块随着人流动态呼吸发光，模糊了建筑结构与生命体的边界。',
    'https://www.dezeen.com/2026/10/15/schemata-architects-linden-house/': '新旧建筑肌理的温和共生；轻盈的锯齿天窗将两座百年石屋缝合，让空间在历史沉淀中涌入充沛自然光。',
    'https://blog.cloudflare.com/cloudflare-openai-discovery-agentic-web/': '智能体互联网时代的 SEO 重构；在边缘网络建立 AI 友好型发现协议，提前卡位 Agent 时代的流量分配权。',
    'https://github.com/zachbrown29/lintel-marketing-playbooks': '将模糊的营销增长拆解为标准化开源策略；按企业真实发展阶段对症下药，拒绝盲目套用大厂模版。',
    'https://forwarder.cc': '极简架构解决核心堵点；让无后端静态站一键获得可靠的线索捕获能力，是独立出海开发者降本利器。',
    'https://chatway.app/': '全渠道客服中枢的无缝集成；将离散的访客对话与 Agent 代理无缝对接，大幅提升线索转化留存率。'
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
v_info = vertical_data['2026-10-16']
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
date: '2026-10-16'
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

out_file = 'src/content/daily/2026-10-16.md'
with open(out_file, 'w', encoding='utf-8') as out:
    out.write(md_content)
print(f'Successfully generated: {out_file} (36 items)')

all_used_list = list(used_urls)
for u in used_set:
    if u not in used_urls:
        all_used_list.append(u)

with open(used_urls_path, 'w', encoding='utf-8') as f:
    json.dump(all_used_list, f, ensure_ascii=False, indent=2)

print(f'\nFinished generating 2026-10-16! Total URLs in history: {len(all_used_list)}')
