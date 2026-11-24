#!/usr/bin/env python3
# coding: utf-8
"""
Upgrade AI 漫剧 & 编剧技巧 across the latest 10 issues (2026-11-15 to 2026-11-24)
using freshly verified high-quality vertical sources.
Verifies all 160 endpoints (80 URLs + 80 images) via real GET HTTP 200 before writing.
"""
import concurrent.futures
import json
import subprocess
import sys
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

pool = json.loads(Path("/tmp/vertical_nov15_24_pool.json").read_text(encoding="utf-8"))
aibase = json.loads(Path("/tmp/aibase_verified.json").read_text(encoding="utf-8"))

D = pool["AI 漫剧"]
S = pool["编剧技巧"]
aibase_by_url = {x["url"]: x for x in aibase}

def item(src_obj, category, title, note, so_what, pinned=False):
    url = src_obj["url"].split("?utm_source=")[0]
    return {
        "category": category,
        "title": title,
        "note": note,
        "url": url,
        "media": src_obj["media"],
        "so_what": so_what,
        "pinned": pinned,
        "source": src_obj["source"],
    }

# 10 days: 2026-11-24 down to 2026-11-15 (newest sources matched to newest dates)
PLAN = {
    "2026-11-24": {
        "AI 漫剧": [
            item(aibase_by_url["https://news.aibase.com/zh/news/32479"], "AI 漫剧",
                 "90 分钟全 AI 电影长片《奇妙连接》登陆三家卫视，零实景拍摄",
                 "深圳团队出品的首部全流程 AIGC 故事长片正式上星播出，全程未动用一台实景摄像机，验证生成式影视已打通广电级播出审片链路。",
                 "全 AI 长片上星标志着画质与连贯性越过及格线，接下来决定生死的不再是“能不能生成”，而是剧本与节奏。", True),
            item(D[12], "AI 漫剧",
                 "Maxon Plus 把可选式 AI 能力正式引入 Cinema 4D 与 ZBrush",
                 "老牌三维与雕刻软件巨头推出 opt-in 模式 AI 辅助模块，让动画与漫剧美术在不破坏既有三维资产管线的前提下加速纹理与造型迭代。",
                 "工业级制作不会抛弃可控三维软件，把 AI 作为可选插件嵌进成熟资产流才是最稳妥的提效路线。", False),
            item(D[29], "AI 漫剧",
                 "转描动画救场：《Cherry and Virgin》导演谈多视觉风格切换",
                 "导演川尻将由拆解如何用转描技术把实拍表演转化为多变的手绘质感，在有限预算下同时撑住情绪真实度与强烈视觉风格化。",
                 "预算有限的漫剧团队可以借鉴“实拍参考+风格化转译”路线，比纯抽卡更容易锁死人物表演神态。", False),
            item(D[46], "AI 漫剧",
                 "befores & afters 拆解蜘蛛侠动作场面的视效与动态调度",
                 "深入剖析超级英雄高速摆荡镜头的动态预演、摄影机速度曲线与肢体张力控制，还原好莱坞级动作动画如何把速度感做实。",
                 "AI 漫剧做高燃打戏最怕动作发飘，先抄透成熟动作片的摄影机速度曲线与停顿帧设计。", False),
        ],
        "编剧技巧": [
            item(S[44], "编剧技巧",
                 "StudioBinder 实操指南：6 步写出高完播微短剧剧本",
                 "系统拆解超短体量剧集的开篇钩子、单场强冲突、信息极简压缩与集尾卡点，把传统三幕剧浓缩进一两分钟的竖屏情绪爆发里。",
                 "微短剧不是长剧砍成碎片，必须把每一分钟当成独立微型高潮来写，前三秒不给悬念就流失观众。", True),
            item(S[25], "编剧技巧",
                 "黑名单新锐交易剧本《Tell Me Everything》高概念卖点拆解",
                 "Go Into The Story 复盘最新成交的原创 Spec 剧本，解析其如何仅靠一句清晰且自带情绪张力的核心前提迅速打动好莱坞制片方。",
                 "好前提自带冲突引擎，写大纲前先测试一句话能不能让听众立刻脑补出两场必然爆发的对手戏。", False),
            item(S[70], "编剧技巧",
                 "John August：如何把“嫉妒”等七宗罪写成高级人物内驱力",
                 "好莱坞一线编剧拆解负面欲望在剧作中的能量，指出让主角拥有难以启齿却人人共鸣的小嫉妒，比强行塑造完美圣人更有戏剧生命力。",
                 "人物立不住往往是因为太“正确”；给主角留一块见不得光的心结，冲突就会自己长出来。", False),
            item(S[47], "编剧技巧",
                 "Industrial Scripts：如何用剧本第一页死死锁住读者注意力",
                 "逐行拆解经典电影与高分剧本的开篇第一页，总结通过动作画面、反常细节与潜台词迅速建立世界观和基调的实操法则。",
                 "审稿人和观众都只给第一页三十秒耐心，别在开头堆背景说明，直接从人物正在做的一件反常小事切入。", False),
        ],
    },
    "2026-11-23": {
        "AI 漫剧": [
            item(D[78], "AI 漫剧",
                 "爱范儿锐评：AI 降本增笑，为什么粗制滥造正引发审美反噬？",
                 "复盘近期多起 AI 广告与视频短片翻车案例，指出缺乏导演审美把关的批量生成正在透支观众耐心，低质“塑料感”已成最大劝退项。",
                 "AI 漫剧的第一波流量红利已过，接下来谁能在构图、光影与表演克制上摆脱“AI 塑料味”，谁才能留住付费观众。", True),
            item(D[13], "AI 漫剧",
                 "第 99 届奥斯卡 38 部动画长片入围初选，数量创历史新高",
                 "AWN 统计显示全球独立与跨国合拍动画爆发式增长，多元画风与轻量化制片管线正打破传统好莱坞大厂对长片动画的垄断。",
                 "动画产能门槛正在全球范围内下移，小团队靠鲜明美术风格和精准题材切口完全有机会突围大厂包围。", False),
            item(D[47], "AI 漫剧",
                 "《Digger》微缩实景模型与数字合成的视觉幕后之旅",
                 "befores & afters 呈现剧组如何将实体微缩置景与现代数字视效融合，用真实物理光影为虚拟镜头注入难以替代的厚重质感。",
                 "纯数字生成容易显得轻飘，用真实材质贴图或实拍光影参考作底图，能立刻拉高漫剧画面的电影感。", False),
            item(D[34], "AI 漫剧",
                 "热门漫画《Fireborn》敲定动画剧集化，由 Titmouse 操刀",
                 "《机械之声》制作方 Titmouse 接手漫画 IP 改编，展示欧美成人向漫改剧集从条漫分镜向动态番剧转化的成熟工业路径。",
                 "静态漫画验证过的人物关系与世界观，是动画与漫剧立项最稳的风险过滤器。", False),
        ],
        "编剧技巧": [
            item(S[10], "编剧技巧",
                 "布考斯基为何说大多数创作者写的东西都很无聊？",
                 "No Film School 引述作家布考斯基的写作忠告，点破过度追求安全套路与华丽辞藻如何杀死文字活力，呼吁回归尖锐真实的生活观察。",
                 "去 AI 味和去无聊感的核心是一致的：删掉正确的废话，把你自己真正感到刺痛或荒诞的细节写进去。", True),
            item(S[26], "编剧技巧",
                 "2026 黑名单长片编剧工坊学员实战复盘：好故事是怎么磨出来的",
                 "多位入选 2026 Black List Feature Lab 的编剧分享从初稿卡壳到推翻重写的真实心路，揭秘顶级导师如何帮剧本找到真正的情感主轴。",
                 "初稿从来不是用来炫技的，而是用来暴露结构病灶的；敢于砍掉最得意但偏离主线的桥段，剧本才会起飞。", False),
            item(S[71], "编剧技巧",
                 "John August：被遗忘的配角艺术，如何用三句台词立住龙套",
                 "剖析好莱坞经典影片里的惊艳小角色，说明哪怕只出场两分钟的配角也必须有自己的小算盘与当下诉求，绝不能只当推进剧情的工具人。",
                 "把剧里的服务员、保安和路人都当成有自己烦恼的活人来写，整场戏的真实感会瞬间翻倍。", False),
            item(S[48], "编剧技巧",
                 "Industrial Scripts：如何定位并彻底重写剧本里最拉垮的一场戏",
                 "给出一套可落地的单场戏诊断清单：当某场戏读起来发闷时，检查是否缺少价值正负转折、进场太早或人物目标冲突不够直接。",
                 "改稿别急着润色台词，先问这场戏结束时人物处境有没有反转；没有转折的纯过场戏直接合并或删掉。", False),
        ],
    },
    "2026-11-22": {
        "AI 漫剧": [
            item(D[41], "AI 漫剧",
                 "动画短片《The Piano》获官方“纯人工制作认证”，行业分化加剧",
                 "Animation Magazine 报道独立动画短片正式贴上 Human Made Mark 标签，折射出在 AI 生成席卷影视后，创作者开始主动区分手艺边界。",
                 "透明标注制作方式将成为行业常态：走工业效率流就拼更新速度与爽点密度，走艺术收藏流就拼稀缺手艺。", True),
            item(D[48], "AI 漫剧",
                 "拆解《足球教练》第四季里那些观众根本看不出来的“隐形视效”",
                 "befores & afters 揭秘剧集如何用大量无缝环境扩展、人群合成与天气替换服务文戏表演，把视效彻底藏在故事背后。",
                 "最好的技术应用不是炫技炸屏，而是用低成本数字补景解决实拍或漫剧场景一致性难题。", False),
            item(D[35], "AI 漫剧",
                 "冲奥动画短片《Beyond Measure》全网上线，极简叙事样本解析",
                 "具备奥斯卡竞逐资格的独立短片开放线上免费观看，展示在几分钟极短篇幅内如何靠纯视觉节奏讲完一个完整情绪弧光。",
                 "做 2 分钟一集的漫剧非常值得多拉冲奥动画短片，学习它们如何省去废话、纯靠镜头对比传递情绪。", False),
            item(D[23], "AI 漫剧",
                 "AI 影视工作室 Utopai Studios 在比弗利山庄设立新据点扩张",
                 "AWN 报道主打生成式影视管线的 Utopai Studios 进驻好莱坞核心圈，加速对接主流制片方与商业项目落地。",
                 "AI 影视团队正在从“技术极客小作坊”向“对接传统制片资源的正规军”演进，制片统筹能力正变得稀缺。", False),
        ],
        "编剧技巧": [
            item(S[28], "编剧技巧",
                 "Screenwriting 101：爱情喜剧大师南希·迈耶斯的剧作心法",
                 "黑名单博客梳理南希·迈耶斯如何把角色性格写进居住空间、道具细节与日常争执，让轻松喜剧同时具备极高的生活质感与共情力。",
                 "场景不只是台词的背景板；让角色住什么房子、桌面摆什么物件直接开口交代性格，能省掉大段自我介绍。", True),
            item(S[15], "编剧技巧",
                 "No Film School：你的下一个爆款剧集创意，可能就坐在餐桌对面",
                 "拆解如何把家庭聚会或职场饭局里的尴尬瞬间升级为高概念影视前提，用“如果把这件小事推到极端会怎样”的思维练出好题材。",
                 "别在真空里憋宏大世界观，最容易引发观众共鸣的戏剧冲突，往往藏在亲密关系里那句没说出口的怨言中。", False),
            item(S[50], "编剧技巧",
                 "Industrial Scripts：如何写出高级潜台词，让对白言外有意",
                 "深度解析“说出口的面具”与“没说出口的诉求”之间的张力，用大量正反例示范如何改掉直白喊口号的 On-the-nose 烂台词。",
                 "人物越想隐藏什么，对白就越绕着什么打转；把直白的情绪宣泄改成借题发挥，台词立刻长出钩子。", False),
            item(S[72], "编剧技巧",
                 "John August：超越一句话梗概，回答清楚你的故事究竟在讲什么",
                 "剖析 Logline（卖点梗概）与 Theme（主题立意）的区别，提醒编剧在向制片人提案前必须先想透故事真正探讨的人性命题。",
                 "卖点决定别人愿不愿意点开第一集，而内核主题决定观众看完后会不会主动帮你转发安利。", False),
        ],
    },
    "2026-11-21": {
        "AI 漫剧": [
            item(D[20], "AI 漫剧",
                 "AI 驱动动画厂牌 Animaj 新作《Ozzy Fox》定档登陆 Disney+",
                 "曾以 AI 辅助动画管线引发关注的 Animaj 拿下全球顶级流媒体发行档期，验证“AI 提效 + 成熟儿童/家庭 IP 运营”的商业闭环。",
                 "技术本身不是终点，用 AI 把传统动画的制作周期压缩一半后，迅速抢占流媒体稳定频道才是大生意。", True),
            item(D[49], "AI 漫剧",
                 "重温视效经典：二十年后回看，咕噜这个数字角色为何依然封神？",
                 "befores & afters 深度复盘数字生物表演捕捉、眼神光微表情与演员灵魂注入的结合，解释为什么好技术永远服务于好演技。",
                 "AI 生成角色常陷入“恐怖谷”，核心缺的不是皮肤分辨率，而是符合心理动机的微表情停顿与眼神焦点。", False),
            item(D[36], "AI 漫剧",
                 "冲奥动画短片《Paradaïz》导演访谈：把个人记忆转译成视觉隐喻",
                 "导演 Matea Radic 拆解如何从私人生活经历中提炼出极具辨识度的色彩体系与角色造型，让小成本短片在国际影展脱颖而出。",
                 "同质化提示词产出的画风千篇一律，注入创作者私人的视觉记忆与色彩偏好，才是漫剧的辨识度护城河。", False),
            item(D[22], "AI 漫剧",
                 "海外动画厂牌 Animotion 携新作《Question Club》正式登陆 B 站",
                 "AWN 关注海外中短视频动画加速进入中国二次元核心社区，跨境动画发行正从长剧向轻量化、强互动系列片倾斜。",
                 "国内 B 站与短视频平台对轻体量系列动画胃口极大，具备清晰人设和单元剧结构的漫剧最易跑出长尾。", False),
        ],
        "编剧技巧": [
            item(S[51], "编剧技巧",
                 "Industrial Scripts：动作与打戏剧本怎么写才能让画面燃起来？",
                 "拆解高分动作片剧本如何用短句节奏、精准动词与空间位移写出窒息感，避免把打戏写成枯燥的武术招式说明书。",
                 "写漫剧打戏分镜前先记住：打斗本质是人物关系和情绪的延续，每一招都要写出“为什么要打”和“打完局势怎么变”。", True),
            item(S[79], "编剧技巧",
                 "IndieWire 专访《头脑特工队 2》编剧：揭秘皮克斯智囊团改稿机制",
                 "编剧 Meg LeFauve 还原皮克斯 Brain Trust 如何做“只诊断病灶、不开处方”的残酷审稿，以及如何把抽象焦虑具象化为可爱角色。",
                 "顶级团队审剧本从不替编剧改具体台词，而是逼着创作者直面“为什么这段我没共情”的底层逻辑漏洞。", False),
            item(S[29], "编剧技巧",
                 "黑名单编剧深度访谈（终篇）：Katla Sólnes 谈剧本定稿与人物弧光",
                 "聚焦剧本后期精修阶段如何把松散的中段收紧，让主角在结局的选择与开篇缺陷形成精准遥相呼应。",
                 "中段一塌全剧皆散；定稿前单独把主角每一场戏的抉择列成清单，检查代价是不是一场比一场沉重。", False),
            item(S[73], "编剧技巧",
                 "John August：奥斯汀电影节“前三页剧本挑战”逐页实战点评",
                 "现场解剖投稿剧本的前三页，直指新手最常犯的过度描写视觉废话、人物出场缺乏辨识度与入戏太慢三大通病。",
                 "不管写电影还是漫剧，把前 3 页的静态环境描写砍掉一半，让主角在第一页就陷入一个小麻烦。", False),
        ],
    },
    "2026-11-20": {
        "AI 漫剧": [
            item(D[66], "AI 漫剧",
                 "Instagram 上线内容防盗保护：自动监测搬运并测试 AI 语音比对",
                 "CineD 报道平台推出跨账号搬运自动拦截与 AI 口播声纹匹配测试，帮助原创短视频与漫剧团队守住流量归属与署名权。",
                 "漫剧爆款最怕上线两小时就被全网切片搬运，善用平台原声与画面指纹保护机制是保住 ROI 的必修课。", True),
            item(D[50], "AI 漫剧",
                 "CoSA 团队拆解现象级怪谈《Backrooms（后室）》视效制作流程",
                 "befores & afters 揭秘工作室如何把风靡全网的阈限空间都市传说做成高质感影视画面，拆解低光噪点、复古画幅与空间畸变技巧。",
                 "规则怪谈与阈限空间极度契合 AI 漫剧的低成本优势——靠氛围压迫与声音设计取胜，无需昂贵大场面特效。", False),
            item(D[51], "AI 漫剧",
                 "定格动画的魅力：抽帧质感与手工材质如何击中数字时代观众",
                 "剖析定格动画刻意保留的帧率顿挫与手作肌理为何在超清流媒体时代反而极具吸引力，为风格化短片提供反向参考。",
                 "AI 漫剧未必非要追求丝滑 60 帧，刻意控制抽帧节奏与黏土/剪纸材质感，反而能做出过目不忘的视觉标签。", False),
            item(D[19], "AI 漫剧",
                 "奥斯卡学院软件基金会迎来新掌门，推动影视开源资产标准演进",
                 "AWN 报道 Andrew Pearce 出任 ASWF 执行总监，持续推进 OpenUSD、OpenEXR 等开源标准，打通影视与实时引擎资产互通。",
                 "OpenUSD 等开放格式正在成为跨工具流转的通用语言，漫剧团队沉淀场景与角色资产时尽量拥抱开放标准。", False),
        ],
        "编剧技巧": [
            item(S[52], "编剧技巧",
                 "Industrial Scripts：如何写出极具追更粘性的剧集单集剧本",
                 "系统拆解剧集 A/B/C 多线穿插配比、冷开场（Teaser）钩子设计与幕间悬念卡点，教你用结构留住下一集点击率。",
                 "剧集与电影最大的不同在于“不能一次解决所有矛盾”——每集结尾留一个撕开新伤口的小反转，观众才会追更。", True),
            item(S[30], "编剧技巧",
                 "黑名单交易剧本《Fairytale in New York》：高概念都市喜剧怎么立",
                 "Go Into The Story 拆解最新成交的纽约背景原创剧本，分析特定城市空间如何与倒计时事件绑定，催生高密度喜剧误会。",
                 "好故事离不开具体的物理空间约束：把角色关在特定时间与地点的“高压锅”里，戏自然就沸腾了。", False),
            item(S[19], "编剧技巧",
                 "No Film School：007 詹姆斯·邦德必须遵守的四条系列人物铁律",
                 "复盘延续六十余年的顶级动作 IP 角色圣经，解析创作者如何在时代变迁中既刷新剧情又不破坏核心观众对人设的底线期待。",
                 "做系列漫剧或长篇 IP，先写清主角“绝对会做”和“绝对不做”的四条铁律，换编剧也不会写崩人设。", False),
            item(S[75], "编剧技巧",
                 "John August 分享《人物塑造工具箱》：避免写出一堆同质化工具人",
                 "提供一套从日常习惯、口头禅、回避话题到道德底线的多维人物校验法，帮助编剧在动笔写对白前先把角色声线彻底拉开。",
                 "检验人物成不成功就用“遮名测试”：把剧本里角色名字全遮住，看读者还能不能一眼认出这句话是谁说的。", False),
        ],
    },
    "2026-11-19": {
        "AI 漫剧": [
            item(D[70], "AI 漫剧",
                 "电影拉片与分镜神库 ShotDeck 大改版：支持自然语言检索动态片段",
                 "CineD 报道专业影视参考库升级自然语言搜镜头与影视动态片段功能，并开放公开参考板，极大加速导演与分镜师前期找参考效率。",
                 "AI 生图生视频最怕“空想提示词”，用 ShotDeck 先按情绪和光影找到电影实拍参考帧，画质和构图瞬间稳两个档次。", True),
            item(D[73], "AI 漫剧",
                 "Aiarty Video Enhancer 实测：纯离线端侧 AI 视频去噪与 4K 超分",
                 "面向视频创作者的本地化画质增强工具，针对低光照噪点、压缩伪影与分辨率不足做专项修复，免去大素材上传云端的耗时。",
                 "AI 视频模型直出素材常带闪烁和糊边，在后期环节接一套稳定的离线超分去噪管线，成片质感立竿见影。", False),
            item(D[72], "AI 漫剧",
                 "rushes Rentals 上线：90% 分成的独立影视自建站直售新工具",
                 "定位 Vimeo On Demand 的轻量替代品，允许创作者直接在自己官网开启付费点播租赁并拿走 90% 净收入，降低对大平台抽成依赖。",
                 "精品独立漫剧与动画短片除了靠平台流量分成，完全可以搭配自建站做高毛利核心粉丝直售。", False),
            item(D[26], "AI 漫剧",
                 "《生命之书》导演 Jorge R. Gutiérrez 领衔新厂牌 HEEBOO 创作片单",
                 "AWN 报道知名风格化动画导演主导创作者驱动型新片单，押注高辨识度拉美视觉美学与跨媒介原创 IP 孵化。",
                 "强视觉作者风格是最难被竞品复制的护城河，小厂牌与其模仿迪士尼，不如死磕一种极致独特的地域或民俗画风。", False),
        ],
        "编剧技巧": [
            item(S[46], "编剧技巧",
                 "StudioBinder 终极指南：如何写好一部抓人的正剧（Drama）剧本",
                 "从核心道德困境、渐进式危机升级到角色内在缺陷外化，用经典名片图解正剧如何不靠狗血反转也能让观众屏息看完。",
                 "高级戏剧张力不是靠坏人降智使坏，而是让两个都有苦衷的好人在无法妥协的利益面前迎头相撞。", True),
            item(S[49], "编剧技巧",
                 "Industrial Scripts：混合类型片（Genre-Blending）的叙事平衡艺术",
                 "拆解如何把悬疑+喜剧、科幻+家庭伦理等跨类型元素有机缝合，指出必须先定好一个主类型兑现观众核心预期，再用副类型制造新鲜感。",
                 "微短剧和漫剧最容易出爆款的是“熟类型+新皮囊”，但切忌两头不靠，主线的情感爽感一定要给足。", False),
            item(S[76], "编剧技巧",
                 "John August 拆解经典人物原型（Archetypes）的现代反套路用法",
                 "深入讨论导师、骗徒、阴影对手等经典叙事原型如何避免沦为脸谱化刻板印象，通过给原型注入反常识弱点重新激活戏剧新鲜感。",
                 "套路之所以管用是因为符合人类深层心理，用原型搭骨架、用反差细节填血肉，既省理解成本又不显老套。", False),
            item(S[31], "编剧技巧",
                 "黑名单编剧访谈（第三篇）：如何靠场景压力逼出人物真实选择",
                 "Katla Sólnes 分享自己在写第二幕中段时，如何不断撤掉主角的后路，逼迫角色在公开场合做出无法挽回的决定。",
                 "第二幕发水最常见的原因是主角还能轻松逃避；把退路堵死，角色才会被迫行动起来。", False),
        ],
    },
    "2026-11-18": {
        "AI 漫剧": [
            item(D[53], "AI 漫剧",
                 "雪山实拍遇上数字资产：《Tenzing》幕后视效拆解卷曝光",
                 "befores & afters 放出登山传记片视效对比卷，展示如何将真实外景与程序化暴风雪、山脊数字绘景无缝融合，兼顾安全与宏大尺度。",
                 "宏大奇观场景不必全靠盲生成，把前景人物表演做稳、中远景用可控数字绘景延伸，最省算力也最稳。", True),
            item(D[42], "AI 漫剧",
                 "Pluto TV 免费频道一口气引入六部 Adult Swim 热门成人动画",
                 "Animation Magazine 报道免费广告流媒体（FAST）大举加码成人向动画内容，印证轻体量、强风格成人动画拥有极高的复看留存。",
                 "成人向短平快动画的商业生命周期极长，把单集控制在 5-15 分钟且梗密度拉满，非常适合跨平台长尾分发。", False),
            item(D[28], "AI 漫剧",
                 "波丽佳音官宣原创动画新企划《KUKU-LOOP》，定档 2027 亮相",
                 "AWN 追踪日本老牌厂牌继续押注“时间循环”母题原创番剧，展示日漫委员会制下提前两年锁定核心视觉与宣发节点的节奏。",
                 "“循环”母题在漫剧与动画里经久不衰，因为场景资产可以高频复用，极省预算又能靠信息差不断制造反转。", False),
            item(D[21], "AI 漫剧",
                 "Maga Animation 操刀游戏续作《The Wardrobe 2》2D 预告动画",
                 "独立游戏与专业 2D 动画工作室跨界联动，用极高帧数的夸张手绘喜剧表现力在预告片阶段迅速引爆玩家社区讨论。",
                 "独立游戏宣发 PV 正在成为精品 AI/2D 动画团队的高客单价 B 端业务入口，短而炸的 60 秒成片最吃香。", False),
        ],
        "编剧技巧": [
            item(S[39], "编剧技巧",
                 "StudioBinder 实操：如何专业拆解剧本并制作统筹拆解表",
                 "手把手示范如何用色彩标记从文字剧本中提取角色、道具、服化、特效与场景清单，打通编剧案头到实际制片预算的关键一跃。",
                 "无论实拍还是 AI 漫剧，动工前先做完剧本三清单（角色/场景/道具资产锁），能减少后期 80% 的穿帮与返工。", True),
            item(S[59], "编剧技巧",
                 "Industrial Scripts：如何构建步步紧逼、绝不泄气的强戏剧冲突",
                 "区分外部障碍、人际对抗与内心撕裂三层冲突，示范如何让对手的动机和主角同样充分，避免反派沦为纯功能性的降智沙包。",
                 "反派有多强，主角的高光就有多亮；给反派一套站得住脚的价值观，整部戏的格局会瞬间拉高。", False),
            item(S[77], "编剧技巧",
                 "John August：文字里的“隐形导演术”，不写运镜词如何控镜头",
                 "教编剧如何通过段落换行、信息揭示顺序与感官动词引导读者脑海里的景别切换，而无需在剧本里堆满生硬的“特写/推镜”指令。",
                 "好剧本不用写“镜头推进”，只需另起一行写“茶杯里的水纹颤了一下”，所有读者和导演都会自动切到特写。", False),
            item(S[0], "编剧技巧",
                 "No Film School：秋天意象在影像叙事中如何承担隐形情绪转场",
                 "分析经典影片如何利用季节枯荣、色调冷暖与落叶环境音外化人物内心的告别与转折，用视觉隐喻替代多余的旁白独白。",
                 "能用环境天气和色彩变化演出来的情绪，就别让角色张嘴念出来；克制的意象比煽情台词更耐人回味。", False),
        ],
    },
    "2026-11-17": {
        "AI 漫剧": [
            item(D[54], "AI 漫剧",
                 "揭秘《Obsession》面部微表情数字精修管线与无痕合成工艺",
                 "befores & afters 深度拆解制作团队如何在不破坏演员原生表演肌理的前提下，用精细数字工具完成微妙面部修饰与光影匹配。",
                 "AI 漫剧换脸或微调最怕磨皮成假人，保留皮肤纹理与真实眼神光反射，才能过得了观众这一关。", True),
            item(D[55], "AI 漫剧",
                 "真假难辨：拆解灾难片《The Lost Bus》里实拍与 CG 的无缝边界",
                 "对比片场原始素材与最终成片，还原剧组如何把烟火实拍元素叠加进全 CG 危机环境，用物理交互细节欺骗人眼。",
                 "漫剧与短片做大场面不必迷信纯端到端生成，用真实烟雾、火光素材做前景叠加合成，质感立刻逼近院线。", False),
            item(D[38], "AI 漫剧",
                 "莱卡工作室开启定格新片《Wildwood》试映，坚守高难度手工奇观",
                 "Animation Magazine 报道顶级定格厂牌 LAIKA 的最新动向，在全行业狂卷 AI 提速的当下继续用极致工艺建立不可替代的品牌溢价。",
                 "越是效率工具普及，顶级手作工艺就越变成奢侈品；找准自己团队在“效率”与“工艺”光谱上的生态位。", False),
            item(D[69], "AI 漫剧",
                 "Cinelab 推出便携远程片场样片套件，打通跨洲实时审片流程",
                 "CineD 报道专业影视后期方案商如何把沉重的数据回传与校色样片压缩进便携箱，实现全球外景地与后期机房的当日协同。",
                 "远程分布式协作已成为影视与漫剧团队常态，把版本命名、样片批注与资产回传规范化，能大幅降低沟通成本。", False),
        ],
        "编剧技巧": [
            item(S[40], "编剧技巧",
                 "StudioBinder 镜表指南：把文字剧本精准翻译成导演镜头清单",
                 "完整解析 Shot List 里的景别、机位角度、运镜方式与声音提示字段，帮助创作者在开机或生图前把每一场戏的视听语言定死。",
                 "AI 漫剧提示词写不稳，往往是缺了这张镜头清单——先把景别、角度、主体动作拆成表格，出片率能翻一倍。", True),
            item(S[60], "编剧技巧",
                 "Industrial Scripts：如何塑造让观众真正共情、念念不忘的角色",
                 "拆解观众爱上一个角色的四个关键触发器：具体的小善意、不完美的脆弱感、主动采取行动的决心，以及面临两难时的真实代价。",
                 "被动挨打、只靠金手指翻盘的主角很难留住人；让角色在逆境里主动迈出哪怕微小的一步，共情就建立了。", False),
            item(S[32], "编剧技巧",
                 "黑名单编剧访谈（第二篇）：如何把模糊灵感孵化成扎实分场大纲",
                 "Katla Sólnes 分享从笔记碎片走到完整故事骨架的实操步骤，重点讨论如何在动笔写对话前先验证所有情节点是否成立。",
                 "别一有灵感就急着写第一场对白；先用索引卡把开端、中点、灵魂暗夜和结局四个锚点钉牢，能少废三稿。", False),
            item(S[4], "编剧技巧",
                 "No Film School 拉片：1993 年《亚当斯一家 2》为何封神喜剧名场面",
                 "逐镜拆解克里斯蒂娜·里奇主演的经典感恩节舞台剧桥段，剖析如何用极度一本正经的反讽表演颠覆传统合家欢套路。",
                 "高级讽刺喜剧从不挤眉弄眼讨好观众——让角色用最严肃的态度干最离谱的事，笑点才足够锋利。", False),
        ],
    },
    "2026-11-16": {
        "AI 漫剧": [
            item(D[30], "AI 漫剧",
                 "变形金刚推出全新擎天柱动画短片，借 YouTube 特别活动唤醒老 IP",
                 "Animation Magazine 报道孩之宝用高密度短片搭配经典动画重映做 YouTube 节点营销，验证“大 IP 轻短片化”在流媒体时代的新活力。",
                 "老 IP 激活不必动辄押注上亿长片，用 3-5 分钟高燃高还原度的短片试水社区反馈，性价比极高。", True),
            item(D[39], "AI 漫剧",
                 "动画先驱唐·布鲁斯纪录片导演访谈：重温手绘黄金时代的叙事胆识",
                 "回溯《鼠谭秘奇》《美国鼠谭》背后的独立突围史，探讨老一辈动画人如何在大厂压力下坚持用黑暗与真实的童话打动观众。",
                 "别低估观众的审美与情感承受力，哪怕是动画和漫剧，敢触碰真实的失去与勇气才能成为长青作品。", False),
            item(D[27], "AI 漫剧",
                 "畅销两亿册绘本《Little Critter》正式启动系列动画剧集开发",
                 "AWN 报道经典儿童绘本历经数十年沉淀后进军系列动画，展示出版物静态插画转化为动态连续剧集的角色重塑与节奏改编。",
                 "绘本与图文故事天然自带现成的分镜和美术设定，是 AI 动画与低幼漫剧最富矿的改编来源之一。", False),
            item(D[81], "AI 漫剧",
                 "鸿蒙版醒图升级 AI 修图管线：局部精修与效率协同体验实测",
                 "爱范儿实测移动端图像处理工具如何把复杂 AI 消除、光影重绘塞进直观手势里，降低创作者做封面图与海报的后期门槛。",
                 "漫剧宣发点击率一半靠封面，把端侧轻量 AI 修图纳入日常宣发工作流，能快速跑通多版 AB 封面测试。", False),
        ],
        "编剧技巧": [
            item(S[43], "编剧技巧",
                 "StudioBinder 评测：主流故事板（Storyboard）工具与分镜模板精选",
                 "横向对比影视与动画行业常用的故事板绘制工具与标准版式模板，帮助独立导演和漫剧团队选出最顺手的可视化预演方案。",
                 "文字分镜与成片之间隔着一道巨大的理解鸿沟，先出干净的四格/六格故事板定构图，能省下大量算力抽卡费。", True),
            item(S[61], "编剧技巧",
                 "Industrial Scripts：五幕剧结构深度拆解，掌控长片与剧集节奏",
                 "跳出机械的三幕套路，详细拆解莎士比亚式五幕结构如何更精细地切分“触发、上升、中点转折、坠落与决战”五个情绪坡度。",
                 "当你发现故事第二幕太长容易塌腰时，换成五幕视角把中段一分为二，节奏锚点立刻清晰得多。", False),
            item(S[78], "编剧技巧",
                 "John August 对谈艾伦·索金：顶级快节奏对白背后的音乐性与冲突",
                 "两位好莱坞金牌编剧罕见同台，索金揭秘自己如何用“立场寸步不让+语言节拍押韵”写出令人欲罢不能的高密度争执戏。",
                 "好对白不是模仿生活里的结巴废话，而是提纯后的交锋——让每个人说话都带着想赢下对方的明确意图。", False),
            item(S[35], "编剧技巧",
                 "黑名单交易剧本《Non-Refundable》：一个书名就能讲清的高概念悬疑",
                 "Go Into The Story 拆解最新售出的悬疑惊悚 Spec 剧本，解析片名本身如何自带倒计时紧迫感与不可逆的交易赌注。",
                 "起片名也是剧作的一部分：好片名本身就包含冲突或悬念，能让观众在刷到封面的半秒内产生点击冲动。", False),
        ],
    },
    "2026-11-15": {
        "AI 漫剧": [
            item(D[32], "AI 漫剧",
                 "2026 葡萄牙 Cinanima 国际动画节揭晓大奖：独立短片美学风向标",
                 "Animation Magazine 盘点老牌国际动画节获奖名单，展现全球独立动画在手绘实验、黑色幽默与社会隐喻上的最新探索。",
                 "常看欧洲与独立动画节获奖短片能有效防审美固化，把先锋视觉隐喻降维用到商业漫剧里往往出奇制胜。", True),
            item(D[37], "AI 漫剧",
                 "TMS 在 Anime Frontier 庆贺《名侦探柯南》：长青动漫 IP 的剧场版运作",
                 "解析日本头部动画公司如何借海外漫展试映与公开配音招募维系跨代际粉丝粘性，让老牌推理番持续刷新年度票房纪录。",
                 "单元剧框架叠加每年一次的大事件剧场版，是动漫 IP 跨越十年周期仍能持续吸金的最稳结构。", False),
            item(D[11], "AI 漫剧",
                 "AWN 本周全球动画预告精选：《无敌少侠》与《平屋慢生活》同台亮相",
                 "一站式梳理欧美硬核超级英雄漫改与日本治愈系日常漫改的最新预告动态，对比两种截然不同的动画节奏与情绪抓手。",
                 "漫剧赛道不只适合爽文打脸，高反差的日常治愈系只要人物够立体，同样能切下极高粘性的细分人群。", False),
            item(D[44], "AI 漫剧",
                 "短剧化音乐动画《Ozzy Fox》登陆流媒体：3 分钟强节奏叙事模板",
                 "Animation Magazine 聚焦短片化音乐动画系列的发行策略，拆解如何用抓耳旋律与明快色彩在三分钟内完成一集完整情绪闭环。",
                 "声音和节奏记忆点在短视频场景下比画面更洗脑，给漫剧设计专属 BGM 钩子能大幅提升二创传播率。", False),
        ],
        "编剧技巧": [
            item(S[64], "编剧技巧",
                 "Industrial Scripts：情节（Plot）与故事（Story）的本质区别是什么？",
                 "一针见血点破许多剧本“发生了一堆事却没故事”的病灶：情节是外部发生的事件链，而故事是这些事件如何迫使主角内在发生蜕变。",
                 "写完大纲先自查：如果把主角换成另一个性格的人，剧情走向会不会完全改变？如果不变，那你只写了事件没写故事。", True),
            item(S[53], "编剧技巧",
                 "Industrial Scripts：如何写出能直接打动投资人的故事大纲（Treatment）",
                 "拆解专业剧本大纲的篇幅控制、现在时态画面感与情绪推进写法，教你用十页以内的流畅叙事卖出整部电影或剧集。",
                 "投资人和制片人很少有耐心直接读完百页剧本；能把故事的爽点、泪点和商业卖点浓缩进一份精彩大纲，项目就成了一半。", False),
            item(S[36], "编剧技巧",
                 "Go Into The Story：AI 与 IP 垄断时代，原创 Spec 剧本为何依然珍贵",
                 "黑名单主理人 Scott Myers 复盘多部逆袭卖出的原创剧本案例，证明市场上最稀缺的永远是带着作者独特生命体验与鲜活声音的新鲜故事。",
                 "模型能轻松拼接出一万个旧套路，但拼不出你真实经历过的人性褶皱；原创故事的不可替代性反而在升值。", False),
            item(S[66], "编剧技巧",
                 "Industrial Scripts：如何写好故事结局与余韵（Denouement），避免虎头蛇尾",
                 "剖析高潮决战之后收尾段落的剧作功能：不靠冗长说教总结主题，而是用一个呼应开篇的微小生活动作让观众回味无穷。",
                 "好结局就像乐曲的最后一个休止符——高潮解决外部危机后，留一分钟静场交代人物新常态，余韵立刻翻倍。", False),
        ],
    },
}

def check_endpoint(task):
    date_str, cat, idx, kind, url = task
    cmd = ["curl", "-sSL", "--max-time", "25", "--retry", "1", "-A", UA, "-o", "/dev/null", "-w", "%{http_code}\t%{content_type}", url]
    if any(h in url for h in ["aibase.com", "qbitai.com", "ifanr.com", "woshipm.com", "wzbj1616.com"]):
        cmd[1:1] = ["--noproxy", "*"]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=40)
        parts = r.stdout.split("\t", 1)
        code = parts[0]
        ctype = parts[1] if len(parts) > 1 else ""
        ok = r.returncode == 0 and code == "200" and (kind != "MEDIA" or ctype.startswith("image/"))
        return dict(date=date_str, category=cat, idx=idx, kind=kind, url=url, status=code, content_type=ctype, ok=ok)
    except Exception as e:
        return dict(date=date_str, category=cat, idx=idx, kind=kind, url=url, status="ERR", content_type=str(e), ok=False)

def main():
    used_path = ROOT / "scripts/all-used-urls.json"
    used = json.loads(used_path.read_text(encoding="utf-8"))
    norm = lambda u: u.strip().rstrip("/").replace("http://", "https://")
    used_set = {norm(u) for u in used}

    # 1. Structural & uniqueness assertions across all 80 items
    all_new_urls = []
    tasks = []
    for d, cats in sorted(PLAN.items()):
        for cat in ["AI 漫剧", "编剧技巧"]:
            lst = cats[cat]
            assert len(lst) == 4, (d, cat, len(lst))
            assert sum(1 for x in lst if x["pinned"]) == 1, (d, cat)
            for idx, x in enumerate(lst):
                nu = norm(x["url"])
                assert nu not in used_set, f"DUPLICATE against used DB: {x['url']}"
                assert nu not in all_new_urls, f"DUPLICATE within batch: {x['url']}"
                all_new_urls.append(nu)
                tasks.append((d, cat, idx, "URL", x["url"]))
                tasks.append((d, cat, idx, "MEDIA", x["media"]))

    assert len(all_new_urls) == 80
    print(f"PASS: 0 duplicates across all 80 replacement items & global used DB ({len(used)} URLs).", flush=True)

    # 2. Strict GET HTTP 200 verification on all 160 endpoints
    print(f"Verifying {len(tasks)} endpoints via live GET...", flush=True)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
        for res in pool.map(check_endpoint, tasks):
            results.append(res)
            if not res["ok"]:
                print("FAIL:", res, flush=True)

    failed = [r for r in results if not r["ok"]]
    (ROOT / "scripts/verification-backfill-nov15-24.json").write_text(
        json.dumps({"total": len(results), "passed": len(failed) == 0, "failed": failed, "endpoints": results}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )
    if failed:
        print(f"ABORTING: {len(failed)} endpoints failed verification!", flush=True)
        sys.exit(1)

    print("SUCCESS: ALL 160 endpoints (80 URLs + 80 media) returned HTTP 200/OK!", flush=True)

    # 3. Rewrite the 10 daily markdown files cleanly, preserving all other 7 categories and body
    for d, cats in sorted(PLAN.items()):
        md_path = ROOT / f"src/content/daily/{d}.md"
        raw = md_path.read_text(encoding="utf-8")
        assert raw.startswith("---\n"), f"Unexpected frontmatter in {md_path}"
        _, fm_str, body = raw.split("---", 2)
        meta = yaml.safe_load(fm_str)
        old_items = meta["items"]
        assert len(old_items) == 36, (d, len(old_items))

        # Preserve exact category ordering slots: replace AI 漫剧 block and 编剧技巧 block in-place
        new_items = []
        inserted_drama = False
        inserted_sw = False
        for it in old_items:
            if it["category"] == "AI 漫剧":
                if not inserted_drama:
                    new_items.extend(cats["AI 漫剧"])
                    inserted_drama = True
            elif it["category"] == "编剧技巧":
                if not inserted_sw:
                    new_items.extend(cats["编剧技巧"])
                    inserted_sw = True
            else:
                new_items.append(it)

        assert inserted_drama and inserted_sw and len(new_items) == 36, (d, len(new_items))
        # Verify 9 categories x 4 items, 1 pinned per category
        c_counts = {}
        p_counts = {}
        for x in new_items:
            c_counts[x["category"]] = c_counts.get(x["category"], 0) + 1
            if x.get("pinned"):
                p_counts[x["category"]] = p_counts.get(x["category"], 0) + 1
        assert len(c_counts) == 9 and set(c_counts.values()) == {4}, (d, c_counts)
        assert len(p_counts) == 9 and set(p_counts.values()) == {1}, (d, p_counts)

        meta["items"] = new_items
        # Update highlights on 2026-11-24 to reflect the upgraded vertical items
        if d == "2026-11-24":
            meta["highlights"] = "九大赛道各四条：循环架构 GLM-5.4、AISI 安全评测漏洞、Claude Ship 自动审修 PR、本地纯文本 CRM、代码派生设计规范、a16z 万次代理购物 B2A 法则、全 AI 长片上星与微短剧六步剧本法。"

        # Serialize frontmatter cleanly with JSON scalars (valid YAML, immune to quote/colon issues)
        lines = ["---"]
        for k, v in meta.items():
            if k != "items":
                # Keep date as YYYY-MM-DD string if yaml parsed it as datetime.date
                if hasattr(v, "isoformat"):
                    v = v.isoformat()
                lines.append(k + ": " + json.dumps(v, ensure_ascii=False))
            else:
                lines.append("items:")
                for x in v:
                    ordered_keys = ["category", "title", "note", "url", "media", "so_what", "pinned", "source"]
                    keys = [kk for kk in ordered_keys if kk in x] + [kk for kk in x if kk not in ordered_keys]
                    for j, key in enumerate(keys):
                        lines.append(("  - " if j == 0 else "    ") + key + ": " + json.dumps(x[key], ensure_ascii=False))
        lines.append("---")
        md_path.write_text("\n".join(lines) + body, encoding="utf-8")

        # Also sync candidates-2026-11-XX.json if it exists
        cand_path = ROOT / f"scripts/candidates-{d}.json"
        if cand_path.exists():
            cand_path.write_text(json.dumps(new_items, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        print(f"Updated {md_path.name} (and synced candidates if present).", flush=True)

    # 4. Append all 80 new URLs to scripts/all-used-urls.json
    new_used = used + [x["url"] for d in sorted(PLAN) for cat in ["AI 漫剧", "编剧技巧"] for x in PLAN[d][cat]]
    assert len(set(norm(u) for u in new_used)) - len(used_set) == 80
    used_path.write_text(json.dumps(new_used, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Updated all-used-urls.json: {len(used)} -> {len(new_used)}", flush=True)

    # 5. Update 2026-11-24-精选总览.md in dialogue folder
    dialogue_dir = Path("/Users/gx/Library/Application Support/Cindy/owners/7f95b3f0c479b22b4be9/dialogues/2026-11-14/f9d8a669-d7a1-4b3f-ac57-d553e940a6c6")
    rows24 = json.loads((ROOT / "scripts/candidates-2026-11-24.json").read_text(encoding="utf-8"))
    ov_lines = ["# 2026-11-24 精选总览（已升级新垂直信源）", "", "| 赛道 | 标题与信源 | 核心洞察 |", "|---|---|---|"]
    for r in rows24:
        ov_lines.append(f"| {r['category']} | [{r['title']}]({r['url']}) · {r['source']} | {r['so_what']} |")
    (dialogue_dir / "2026-11-24-精选总览.md").write_text("\n".join(ov_lines) + "\n", encoding="utf-8")
    print("Updated 2026-11-24-精选总览.md!")

if __name__ == "__main__":
    main()
