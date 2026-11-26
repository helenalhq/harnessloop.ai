"""Business-first landing and contact layout. Contact controls are reused, not reimplemented."""
from html import escape
from refine import system

COPY = {
    'zh': {
        'tag': '本地 AI · 货代与报关',
        'hero': '货代与报关的本地 AI 助手。',
        'lead': '草拟回复、跟进每一票货物、盯住每一个申报期限——发出之前，永远先经你审批。跑在你自己的电脑上，数据不出门。一次性部署，无按坐席订阅。',
        'cta': '讨论你的业务场景',
        'demo_cta': '看一个演示',
        'brief_cta': '下载晨报样例（PDF）',
        'pains_kicker': '每个数字都可点击核查',
        'pains_title': '漏掉一个期限，代价是确定的。',
        'pains': (
            ('ISF 申报', '错过 24 小时截止线', 'ISF 须在装船前至少 24 小时申报；逾期未申报，每次违规可被处以 $5,000（美元）定额赔偿金。', '来源：美国海关与边境保护局 · 19 CFR § 113.62', 'https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62'),
            ('滞期费与滞箱费账单', '只有 30 天争议窗口', '账单须在最后一次收费后 30 个日历日内开出，被收费方有至少 30 个日历日可以争议。往来记录就是证据。', '来源：美国联邦海事委员会 · 最终规则', 'https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/'),
            ('进口申报', '逾期按日计征滞报金', '自运输工具申报进境之日起第 15 日起按日征收，日征收金额为计税价格的 0.5‰，起征点为人民币 50 元。', '来源：海关总署令第 128 号（2024 年第 273 号令修正）', 'https://www.customs.gov.cn/customs/302249/302266/302267/356554/index.html'),
        ),
        'deliver': '从输入到交付',
        'flow': (
            ('从现有资料开始', '只接入你批准的来源和工具。'),
            ('把重点整理出来', '得到简报、回复草稿或带出处的记录。'),
            ('重要决定由你复核', '不确定的信息不猜测，对外操作按约定执行。'),
        ),
        'sector': '我们构建的示例',
        'examples': '同一个方法，两种业务用法。',
        'cards': (
            ('货运代理', '货代智能客服助手', '少翻系统，少漏重要跟进。一次看清变化、待确认项和可复核的回复草稿——每个动作留时间戳与出处，账单有争议时，记录就是证据。','查看示例跟进卡','港口集装箱和起重机'),
            ('医学研究与情报', '医学文献及情报管理助手', '不只知道有新文献，还看得出证据可能改变什么，并能沿出处核对。研究人员决定是否更新简报。','查看示例证据提示','桌上的研究资料与阅读笔记'),
        ),
        'video_label': 'HarnessLoop 演示视频（中文，55 秒）',
        'video_note': '动画演示，含配音；使用合成数据，不含真实货物。',
        'video_link': '在 GitHub 上打开',
        'video_play': '播放 55 秒视频',
        'video_failed': '视频暂时无法加载。',
        'proof': '我们的工作方法',
        'method': '先看结果，再决定要不要扩大范围。',
        'method_detail': '用约定样本验证输出是否有出处、未知是否被标出、复核交接是否可用。不把演示当客户成果。',
        'approach': '了解工作原理',
        'demo': '查看数据工厂演示',
        'show_demo': '展开一个合成示例',
        'next': '你想先解决哪件事？',
        'final_copy': '不需要先共享业务数据。用几句话说清任务、目前的难点，以及怎样才算做好。我们会在 24 小时内回复。',
        'contact_tag': '联系合作',
        'contact_title': '从一件具体的业务任务开始。',
        'contact_lead': '告诉我们你希望助手做什么、哪一步最费时，以及仍需由谁判断。初次联系请只用不含敏感信息的描述。',
        'engagement': '怎么开始',
        'contact_steps': (
            ('描述任务', '说清目前怎么做、问题在哪，以及希望得到什么输出。'),
            ('一起确认范围', '约定能用的资料、设备和权限，哪些步骤必须人工复核，以及如何验收。'),
            ('验证以后再扩大', '用约定样本核对输出和复核记录，再决定是否扩大范围。'),
        ),
    },
    'en': {
        'tag': 'LOCAL AI · FREIGHT & CUSTOMS',
        'hero': 'An AI assistant for small freight forwarders and customs brokers.',
        'lead': 'It drafts replies, tracks follow-ups and watches every deadline — nothing is sent without your review. Runs on your own computer. Your data never leaves your office. One-time setup, no per-seat subscription.',
        'cta': 'Discuss your workflow',
        'demo_cta': 'See a demo',
        'brief_cta': 'Get a sample morning brief',
        'pains_kicker': 'EVERY NUMBER, CHECKABLE AT THE SOURCE',
        'pains_title': 'A missed deadline has a known price.',
        'pains': (
            ('ISF FILING', 'Miss the 24-hour deadline', 'ISF must be filed at least 24 hours before lading. Miss it, and liquidated damages of USD 5,000 apply per violation.', 'Source: U.S. CBP · 19 CFR § 113.62', 'https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62'),
            ('D&D INVOICES', 'A 30-day window to dispute', 'Carriers must bill within 30 calendar days of the last charge, and you have at least 30 days to dispute. Your records are your evidence.', 'Source: U.S. FMC · final rule on D&D billing', 'https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/'),
            ('ENTRY ERRORS', 'Up to 4× the unpaid duty', 'Gross negligence under 19 U.S.C. § 1592 means 4× the underpaid duty — or 40% of dutiable value where no revenue is lost.', 'Source: 19 U.S.C. § 1592', 'https://www.law.cornell.edu/uscode/text/19/1592'),
        ),
        'deliver': 'From input to review',
        'flow': (
            ('Start with your sources', 'Use only the information and tools you approve.'),
            ('Get something your team can use', 'A brief, a response draft or a record with sources.'),
            ('Keep people in charge', 'Flag uncertainty. External actions follow agreed rules.'),
        ),
        'sector': 'EXAMPLES OF WHAT WE BUILD',
        'examples': 'One approach, two kinds of work.',
        'cards': (
            ('Freight forwarding', 'Freight Forwarding Customer Service Assistant', 'Spend less time switching between systems and miss fewer follow-ups. See what changed, what to check and what reply is ready for review — every action keeps a timestamp and its source, so when a bill is disputed, your record is your evidence.','See a sample follow-up card','Container cranes and stacks at a freight terminal'),
            ('Medical research and intelligence', 'Medical Literature & Intelligence Assistant', 'Go beyond new-paper alerts. See what evidence may change, trace it to its source, and let researchers decide whether to update the brief.','See a sample evidence alert','Research papers and reading notes on a desk'),
        ),
        'video_label': 'HarnessLoop demo video (English, 55 seconds)',
        'video_note': 'Animated walkthrough with voice-over, using synthetic data (no real shipments).',
        'video_link': 'Open on GitHub',
        'video_play': 'Play the 55-second video',
        'video_failed': 'The video could not be loaded.',
        'proof': 'HOW WE WORK',
        'method': 'Check the result before expanding the scope.',
        'method_detail': 'Use agreed examples to verify sources, uncertainty flags and review handoffs. A demonstration is not a customer result.',
        'approach': 'Explore the approach',
        'demo': 'See the data factory demo',
        'show_demo': 'Open a synthetic example',
        'next': 'What would you start with?',
        'final_copy': 'No need to share business data. Tell us what the task is, what’s difficult today and what a good result would look like. We reply within 24 hours.',
        'contact_tag': 'CONTACT',
        'contact_title': 'Start with one real task.',
        'contact_lead': 'Tell us what you need the assistant to do, what takes the most time and where a person needs to decide. Keep initial enquiries free of sensitive information.',
        'engagement': 'How to start',
        'contact_steps': (
            ('Describe the task', 'Tell us how it works today, where it breaks down and what output you need.'),
            ('Agree on scope', 'Define allowed sources, devices, permissions, review steps and acceptance criteria.'),
            ('Check it before expanding', 'Review outputs and run records against agreed samples before deciding whether to go further.'),
        ),
    },
}


# The walkthrough videos are public release assets of the HarnessLoop media repository.
VIDEO_RELEASE = 'https://github.com/helenalhq/media/releases/tag/v1.0'
VIDEO = {lang: f'https://github.com/helenalhq/media/releases/download/v1.0/demo-55s-{lang}.mp4' for lang in ('zh', 'en')}


def home_body(lang):
    c = COPY[lang]
    prefix = '/en/' if lang == 'en' else '/'
    contact = prefix + 'contact/'
    demo = prefix + 'demo/'
    brief = '/assets/sample-brief-zh.pdf' if lang == 'zh' else '/assets/sample-brief.pdf'
    flow = ''.join(
        f'<li><span aria-hidden="true">{n:02}</span><div><strong>{escape(label)}</strong><p>{escape(description)}</p></div></li>'
        for n, (label, description) in enumerate(c['flow'], 1)
    )
    pains = ''.join(
        f'''<article class="hl-pain-card"><p class="hl-pain-index">{n:02} · {escape(domain)}</p><h3>{escape(pain)}</h3><p>{escape(detail)}</p><a class="hl-pain-source" href="{url}" target="_blank" rel="noopener noreferrer">{escape(source)} <span aria-hidden="true">→</span></a></article>'''
        for n, (domain, pain, detail, source, url) in enumerate(c['pains'], 1)
    )
    cards = []
    for asset, (industry, title, detail, link, alt) in zip(('freight', 'medical'), c['cards']):
        target = prefix + 'solutions/#hl-sample-' + asset
        cards.append(f'''<article class="hl-home-card">
          <a href="{target}" class="hl-home-card-photo" aria-label="{escape(title)}">
            <img src="/assets/hl-{asset}-v3.webp" width="1260" height="840" alt="{escape(alt)}" decoding="async">
          </a>
          <div class="hl-home-card-content"><p class="hl-biz-kicker">{escape(industry)}</p><h3>{escape(title)}</h3>
            <p>{escape(detail)}</p><a class="hl-biz-text" href="{target}">{escape(link)} <span aria-hidden="true">→</span></a></div>
        </article>''')
    industries = ''.join(cards)
    demonstration = system(lang == 'en')
    # Nothing is downloaded from GitHub until the visitor presses play.
    github_link = f'''<a href="{VIDEO_RELEASE}" target="_blank" rel="noopener noreferrer">{escape(c['video_link'])} <span aria-hidden="true">→</span></a>'''
    player = f'''<div class="hl-hero-media">
          <div class="hl-video-frame"><video controls playsinline preload="none" width="1920" height="1080" poster="/assets/demo-poster-{lang}.webp" aria-label="{escape(c['video_label'])}" data-play="{escape(c['video_play'])}"><source src="{VIDEO[lang]}" type="video/mp4">{escape(c['video_link'])}</video></div>
          <p class="hl-video-failed hidden">{escape(c['video_failed'])} {github_link}</p>
          <p class="hl-video-note">{escape(c['video_note'])} {github_link}</p>
        </div>
'''
    return f'''<div class="hl-business hl-home">
      <section class="hl-biz-hero" aria-labelledby="hl-home-title">
        <div class="wrap hl-biz-hero-grid"><div>
          <p class="hl-biz-kicker">{escape(c['tag'])}</p><h1 id="hl-home-title">{escape(c['hero'])}</h1>
          <p class="hl-biz-lead">{escape(c['lead'])}</p><div class="hl-biz-actions">
            <a class="hl-biz-button" href="{demo}">{escape(c['demo_cta'])} <span aria-hidden="true">→</span></a>
            <a class="hl-biz-secondary" href="{contact}">{escape(c['cta'])} <span aria-hidden="true">→</span></a>
          </div></div>{player}</div>
      </section>
      <section class="wrap hl-home-flow" aria-labelledby="hl-home-flow-title"><p class="hl-biz-kicker" id="hl-home-flow-title">{escape(c['deliver'])}</p><ol>{flow}</ol></section>
      <section class="wrap hl-home-pains" aria-labelledby="hl-home-pains-title">
        <p class="hl-biz-kicker">{escape(c['pains_kicker'])}</p><h2 id="hl-home-pains-title">{escape(c['pains_title'])}</h2>
        <div class="hl-pain-cards">{pains}</div>
      </section>
      <section class="wrap hl-home-solutions" id="hl-home-solutions" aria-labelledby="hl-home-examples-title">
        <p class="hl-biz-kicker">{escape(c['sector'])}</p><h2 id="hl-home-examples-title">{escape(c['examples'])}</h2>
        <div class="hl-home-cards">{industries}</div>
      </section>
      <section class="hl-home-method" id="hl-home-method" aria-labelledby="hl-home-method-title">
        <div class="wrap"><p class="hl-biz-kicker">{escape(c['proof'])}</p><h2 id="hl-home-method-title">{escape(c['method'])}</h2>
          <p>{escape(c['method_detail'])}</p>
          <div class="hl-biz-actions"><a class="hl-biz-text" href="{prefix}how-it-works/">{escape(c['approach'])} <span aria-hidden="true">→</span></a>
          <a class="hl-biz-text" href="{prefix}data-factory/">{escape(c['demo'])} <span aria-hidden="true">→</span></a>
          <a class="hl-biz-text" href="{brief}">{escape(c['brief_cta'])} <span aria-hidden="true">↓</span></a></div>
          <details class="hl-home-proof"><summary>{escape(c['show_demo'])}</summary>{demonstration}</details>
        </div>
      </section>
      <section class="hl-biz-final"><div class="wrap hl-biz-final-grid"><div><h2>{escape(c['next'])}</h2><p>{escape(c['final_copy'])}</p></div><a class="hl-biz-button" href="{contact}">{escape(c['cta'])} <span aria-hidden="true">→</span></a></div></section>
    </div>'''


def contact_body(prepared, lang):
    c = COPY[lang]
    _, marker, rest = prepared.partition('<div class="contact-address">')
    if not marker:
        raise ValueError('Expected the existing contact address panel')
    email, _, rest = rest.partition('</div>')
    _, marker, rest = rest.partition('<div class="box">')
    if not marker:
        raise ValueError('Expected the existing local brief panel')
    tool, suffix = rest.rsplit('</div></section>', 1)
    if 'id="brief-form"' not in tool or 'id="copy-email"' not in email or '<noscript>' not in suffix:
        raise ValueError('Expected intact local brief, email and no-JavaScript fallback')
    steps = ''.join(
        f'<li class="hl-engagement-step"><span aria-hidden="true">{n:02}</span><div><h3>{escape(heading)}</h3><p>{escape(detail)}</p></div></li>'
        for n, (heading, detail) in enumerate(c['contact_steps'], start=1)
    )
    return f'''<div class="hl-business hl-contact">
      <section class="hl-biz-hero" aria-labelledby="hl-contact-title"><div class="wrap hl-contact-hero">
        <p class="hl-biz-kicker">{escape(c['contact_tag'])}</p>
        <h1 id="hl-contact-title">{escape(c['contact_title'])}</h1><p class="hl-biz-lead">{escape(c['contact_lead'])}</p>
      </div></section>
      <section class="wrap hl-contact-grid" aria-label="{escape(c['engagement'])}">
        <div class="hl-engagement">
          <h2>{escape(c['engagement'])}</h2><ol>{steps}</ol>
          <div class="contact-address">{email}</div>
        </div>
        <div class="box hl-contact-brief">{tool}</div>
      </section>{suffix}
    </div>'''
