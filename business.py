"""Business-first landing and contact layout. Contact controls are reused, not reimplemented."""
from html import escape
from refine import system
from solutions import COPY as SOLUTIONS

COPY = {
    'zh': {
        'tag': '私有 AI 助手 · 装在你自己的电脑上',
        'hero': '一个属于你自己的 AI 助手，按你的业务定制。',
        'lead': '用起来像 Claude Desktop、Codex 这类工具，区别是它已经按你的业务配好。装在你自己的电脑上，用你自己的模型账号，数据不出门；草拟、跟进、盯期限，发出之前永远先经你审批。',
        'cta': '讨论你的业务场景',
        'demo_cta': '看一个演示',
        'brief_cta': '下载晨报样例（PDF）',
        'pains_kicker': '以货代为例 · 每个数字都可点击核查',
        'pains_title': '漏掉一个期限，代价是确定的。',
        'pains': (
            ('ISF 申报', '错过 24 小时截止线', 'ISF 须在装船前至少 24 小时申报；逾期未申报，每次违规可被处以 $5,000（美元）定额赔偿金。', '来源：美国海关与边境保护局 · 19 CFR § 113.62', 'https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62'),
            ('滞期费与滞箱费账单', '只有 30 天争议窗口', '账单须在最后一次收费后 30 个日历日内开出，被收费方有至少 30 个日历日可以争议。往来记录就是证据。', '来源：美国联邦海事委员会 · 最终规则', 'https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/'),
            ('进口申报', '逾期按日计征滞报金', '自运输工具申报进境之日起第 15 日起按日征收，日征收金额为计税价格的 0.5‰，起征点为人民币 50 元。', '来源：海关总署令第 128 号（2024 年第 273 号令修正）', 'https://www.customs.gov.cn/customs/302249/302266/302267/356554/index.html'),
        ),
        'deliver': '从你的一项任务，到你自己的助手',
        'flow': (
            ('描述一项任务', '说清现在怎么做、哪里最费时。不需要先共享业务数据。'),
            ('我们定制，装到你的电脑', '接入你批准的资料和工具，用你自己的模型账号。'),
            ('它在业务里运行，也会变好', '每次纠正成为候选改进，经独立验证和你批准后进入下一版。'),
        ),
        'sector': '示例 · 同一个做法，两种不相干的业务',
        'examples': '方法只有一个，业务可以完全不同。',
        'examples_lead': '同一套做法，换一个行业照样成立：你描述任务，我们把助手配到你的业务里，交到你自己手上，让它接着变好。',
        'row_labels': ('痛点', '助手做什么', '你拿到什么', '怎么变好'),
        'cards': (
            ('货运代理', '客户在催一票日期未定的货，而信息散在三个系统里。', (
                '邮件、船公司网站、表格各有一半信息。跟漏一次，要么错过申报，要么一张账单过了争议期。',
                '助手汇总你授权查看的货运动态，标出缺什么、为什么现在不能答复，并起草回复。员工核对、修改后决定是否发出。',
                '装在你电脑上的客服助手、回复模板，以及每次运行的记录和出处。',
                '被退回的草稿成为候选改进；在独立样本上验证没有退化、并经人工批准后，才替换现行版本。',
            )),
            ('医学研究与情报', '每周都有新文献，没人确定哪一篇会改变简报里的结论。', (
                '靠人工追踪来源、逐条比对旧简报；一个结论要改，得回头找原文和页码。',
                '助手按主题跟踪你授权的文献和指南，对照现有简报，标出哪些结论可能要改、哪些不变、哪些还不确定，并附出处与原文位置。',
                '装在研究人员工作站上的文献助手、简报模板，以及运行和复核记录。研究员决定是否更新简报；不提供临床建议。',
                '研究员纠正过的判断成为候选改进；独立验证通过后才进入下一版。',
            )),
        ),
        'sample_title': '它给出的东西长这样（合成示例）',
        'card_link': '看完整示例',
        'tail': '你的业务不在上面？方法是同一个：',
        'tail_link': '从一项具体任务开始',
        'video_label': 'HarnessLoop 演示视频（中文，55 秒）',
        'video_note': '动画演示，含配音；使用合成数据，不含真实货物。',
        'video_link': '在 GitHub 上打开',
        'card_index': '示例',
        'video_play': '播放 55 秒视频',
        'video_failed': '视频暂时无法加载。',
        'proof': '我们的工作方法',
        'method': '先看结果，再决定要不要扩大范围。',
        'method_detail': '助手背后是一套我们叫作 Harness 的系统：上下文、工具、流程和检查，让模型按你的标准可靠地干活。先用约定样本验证输出有没有出处、未知有没有标出、复核能不能接得上，再决定要不要扩大范围。',
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
        'tag': 'YOUR OWN AI ASSISTANT · ON YOUR OWN COMPUTER',
        'hero': 'An AI assistant of your own, built around your work.',
        'lead': 'It works like tools such as Claude Desktop or Codex, except it arrives configured for your business. It runs on your own computer with your own model account, so your data never leaves your office — and nothing is sent without your review.',
        'cta': 'Discuss your workflow',
        'demo_cta': 'See a demo',
        'brief_cta': 'Get a sample morning brief',
        'pains_kicker': 'TAKE FREIGHT FORWARDING · EVERY NUMBER, CHECKABLE AT THE SOURCE',
        'pains_title': 'A missed deadline has a known price.',
        'pains': (
            ('ISF FILING', 'Miss the 24-hour deadline', 'ISF must be filed at least 24 hours before lading. Miss it, and liquidated damages of USD 5,000 apply per violation.', 'Source: U.S. CBP · 19 CFR § 113.62', 'https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62'),
            ('D&D INVOICES', 'A 30-day window to dispute', 'Carriers must bill within 30 calendar days of the last charge, and you have at least 30 days to dispute. Your records are your evidence.', 'Source: U.S. FMC · final rule on D&D billing', 'https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/'),
            ('ENTRY ERRORS', 'Up to 4× the unpaid duty', 'Gross negligence under 19 U.S.C. § 1592 means 4× the underpaid duty — or 40% of dutiable value where no revenue is lost.', 'Source: 19 U.S.C. § 1592', 'https://www.law.cornell.edu/uscode/text/19/1592'),
        ),
        'deliver': 'From one task to an assistant of your own',
        'flow': (
            ('Describe one task', 'How it is done today and where it costs the most time. No business data needed yet.'),
            ('We build it, you run it', 'On your own computer, with the sources and tools you approve and your own model account.'),
            ('It works, and it improves', 'Each correction becomes a candidate change that reaches the next version only after independent validation and your approval.'),
        ),
        'sector': 'EXAMPLES · ONE APPROACH, TWO UNRELATED JOBS',
        'examples': 'One method. Two jobs that share nothing else.',
        'examples_lead': 'The same approach holds in an industry that shares nothing with the first: describe the task, we fit an assistant to your work and hand it to you, and it keeps improving from there.',
        'row_labels': ('THE PAIN', 'THE ASSISTANT', 'WHAT YOU RECEIVE', 'HOW IT IMPROVES'),
        'cards': (
            ('Freight forwarding', 'A customer is chasing a shipment whose date is unconfirmed, and the facts sit in three systems.', (
                'Email, carrier portals and spreadsheets each hold part of the picture. One missed follow-up means a missed filing or an invoice that is past its dispute window.',
                'The assistant pulls together the shipment updates you allow, shows what is missing and why no answer can be given yet, then drafts the reply. Staff check it, edit it and decide whether to send.',
                'A customer-service assistant installed on your computer, reply templates, and a record with sources for every run.',
                'Every rejected draft becomes a candidate change. It replaces the working version only after passing independent examples and a human approval.',
            )),
            ('Medical research and intelligence', 'New papers every week, and nobody is sure which one changes the brief.', (
                'Sources are tracked by hand and old briefs compared line by line; changing one conclusion means finding the original passage again.',
                'The assistant tracks the journals and guidelines you allow by topic, compares them with the brief, and marks which conclusions may change, which hold and which stay uncertain, each with its source and place in the text.',
                'A literature assistant installed on a researcher’s workstation, brief templates, and run and review records. Researchers decide whether to update the brief; it gives no clinical advice.',
                'Judgements a researcher corrected become candidate changes, and reach the next version only after independent validation.',
            )),
        ),
        'sample_title': 'What it hands back (synthetic sample)',
        'card_link': 'See the full example',
        'tail': 'Your work is not on this list? The method is the same:',
        'tail_link': 'Start with one task',
        'video_label': 'HarnessLoop demo video (English, 55 seconds)',
        'video_note': 'Animated walkthrough with voice-over, using synthetic data (no real shipments).',
        'video_link': 'Open on GitHub',
        'card_index': 'EXAMPLE',
        'video_play': 'Play the 55-second video',
        'video_failed': 'The video could not be loaded.',
        'proof': 'HOW WE WORK',
        'method': 'Check the result before expanding the scope.',
        'method_detail': 'Behind the assistant sits what we call a harness: the context, tools, workflow and checks that make a model do reliable work to your standard. We first verify on agreed examples that outputs have sources, uncertainty is flagged and review handoffs work, then decide whether to expand.',
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
    labels = c['row_labels']
    for n, (asset, (industry, headline, rows)) in enumerate(zip(('freight', 'medical'), c['cards']), 1):
        target = prefix + 'solutions/#hl-sample-' + asset
        # The small sample repeats the one on the examples page, so the two never drift apart.
        sample = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>' for label, value in SOLUTIONS[lang]['cards'][n - 1][4])
        facts = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(text)}</dd></div>' for label, text in zip(labels, rows))
        cards.append(f'''<article class="hl-home-card">
          <div class="hl-home-card-content"><p class="hl-biz-kicker">{c['card_index']} {n:02} · {escape(industry)}</p><h3>{escape(headline)}</h3>
            <div class="hl-home-sample"><p class="hl-home-sample-title">{escape(c['sample_title'])}</p><dl>{sample}</dl></div>
            <dl class="hl-home-facts">{facts}</dl>
            <a class="hl-biz-text" href="{target}">{escape(c['card_link'])} <span aria-hidden="true">→</span></a></div>
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
        <p class="hl-home-lead">{escape(c['examples_lead'])}</p>
        <div class="hl-home-cards">{industries}</div>
        <p class="hl-home-tail">{escape(c['tail'])} <a href="{contact}">{escape(c['tail_link'])} <span aria-hidden="true">→</span></a></p>
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
