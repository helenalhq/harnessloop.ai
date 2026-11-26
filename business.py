"""Business-first landing and contact layout. Contact controls are reused, not reimplemented."""
from html import escape
from refine import system

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
        'sector': '两个例子 · 同一种定制方法',
        'examples': '业务不同，助手也该不同。',
        'examples_lead': '你把任务讲清楚，我们按你的资料、流程和审批方式定制。',
        'node_labels': ('授权资料', '你的助手', '你来审批'),
        'delivery_label': '你拿到什么',
        'improve_label': '它怎么变好',
        'improve_steps': ('你的纠正', '独立验证', '你批准', '下一版'),
        'cards': (
            ('货代 · 客户跟进', '客户在催，船期还没确认。',
             '邮件、船司门户、表格，各有一段答案。',
             ('邮件 / 门户 / 表格', '汇总 / 核对 / 草拟', '回复草稿'),
             '日期未确认 · 草稿未发送',
             '你的电脑：客服助手 + 回复模板 + 运行记录'),
            ('医学研究 · 情报简报', '新文献来了，结论要不要改？',
             '人工追来源、对简报、找原文，费时又难追溯。',
             ('文献 / 指南 / 旧简报', '对照 / 标注 / 溯源', '证据提示'),
             '仅读到摘要 · 需核对全文',
             '研究员工作站：文献助手 + 简报模板 + 复核记录'),
        ),
        'synthetic': '合成示例',
        'card_link': '看完整示例与输出',
        'tail': '你的业务不在上面？',
        'tail_link': '从一项具体任务开始',
        'video_label': 'HarnessLoop 演示视频（中文，55 秒）',
        'video_note': '动画演示，含配音；使用合成数据，不含真实货物。',
        'video_link': '在 GitHub 上打开',
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
        'sector': 'TWO BUSINESSES · ONE TAILORED APPROACH',
        'examples': 'Different business. A different assistant.',
        'examples_lead': 'You describe the task. We tailor the assistant to your sources, workflow and approvals.',
        'node_labels': ('APPROVED SOURCES', 'YOUR ASSISTANT', 'YOU APPROVE'),
        'delivery_label': 'WHAT YOU RECEIVE',
        'improve_label': 'HOW IT IMPROVES',
        'improve_steps': ('Your correction', 'Independent validation', 'Your approval', 'Next version'),
        'cards': (
            ('Freight · Customer follow-up', 'The customer wants a date. You don’t have one yet.',
             'The answer is split across email, carrier portals and spreadsheets.',
             ('Email / portals / sheets', 'Gather / check / draft', 'Reply draft'),
             'Date unconfirmed · Not sent',
             'On your computer: assistant + reply templates + run records'),
            ('Medical research · Intelligence briefs', 'A new paper is out. Does the brief change?',
             'Tracking sources, comparing briefs and finding passages by hand.',
             ('Papers / guidance / briefs', 'Compare / flag / cite', 'Evidence alert'),
             'Abstract only · Review full text',
             'On the workstation: assistant + brief templates + review records'),
        ),
        'synthetic': 'SYNTHETIC',
        'card_link': 'See the full example and output',
        'tail': 'Your work is not on this list?',
        'tail_link': 'Start with one task',
        'video_label': 'HarnessLoop demo video (English, 55 seconds)',
        'video_note': 'Animated walkthrough with voice-over, using synthetic data (no real shipments).',
        'video_link': 'Open on GitHub',
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


def _example_icon(name):
    paths = {
        'freight': '<path d="M3 15h18l-2 4H6z M6 15V8h12v7 M9 8V5h6v3 M9 11h.01 M12 11h.01 M15 11h.01"/>',
        'medical': '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H11v16H6.5A2.5 2.5 0 0 0 4 21.5z M20 5.5A2.5 2.5 0 0 0 17.5 3H13v16h4.5a2.5 2.5 0 0 1 2.5 2.5z"/>',
        'sources': '<path d="M8 3h8l4 4v10H8z M16 3v5h4 M8 21H4V7h4 M11 12h6 M11 15h5"/>',
        'assistant': '<path d="m12 3 1.7 5.3L19 10l-5.3 1.7L12 17l-1.7-5.3L5 10l5.3-1.7z M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
        'output': '<path d="M6 3h8l4 4v14H6z M14 3v5h4 M9 15l2 2 4-5"/>',
        'device': '<rect x="4" y="4" width="16" height="12" rx="2"/><path d="M2 20h20 M9 20l1-4h4l1 4"/>',
        'loop': '<path d="M20 7h-5V2 M4 17h5v5 M5.1 9a8 8 0 0 1 13.2-3L20 7 M4 17l1.7 1A8 8 0 0 0 18.9 15"/>',
        'arrow': '<path d="M4 12h16m-6-6 6 6-6 6"/>',
    }
    return f'<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{paths[name]}</svg>'


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
    for asset, (industry, headline, pain, nodes, sample, delivery) in zip(('freight', 'medical'), c['cards']):
        target = prefix + 'solutions/#hl-sample-' + asset
        steps = []
        for i, (label, value) in enumerate(zip(c['node_labels'], nodes)):
            icon = ('sources', 'assistant', 'output')[i]
            arrow = '' if i == 0 else f'<span class="hl-example-arrow" aria-hidden="true">{_example_icon("arrow")}</span>'
            result = '' if i < 2 else f'<span class="hl-example-sample"><b>{escape(c["synthetic"])}</b>{escape(sample)}</span>'
            steps.append(f'''<li class="hl-example-node hl-example-node--{i}">{arrow}<span class="hl-example-node-icon">{_example_icon(icon)}</span>
              <small>{escape(label)}</small><strong>{escape(value)}</strong>{result}</li>''')
        cards.append(f'''<article class="hl-home-card hl-home-card--{asset}" aria-labelledby="hl-home-example-{lang}-{asset}">
          <div class="hl-home-card-content">
            <div class="hl-home-card-heading"><span class="hl-home-card-icon">{_example_icon(asset)}</span><p class="hl-biz-kicker">{escape(industry)}</p></div>
            <h3 id="hl-home-example-{lang}-{asset}">{escape(headline)}</h3><p class="hl-home-card-pain">{escape(pain)}</p>
            <ol class="hl-example-flow">{''.join(steps)}</ol>
            <p class="hl-home-delivery">{_example_icon('device')}<span><small>{escape(c['delivery_label'])}</small><strong>{escape(delivery)}</strong></span></p>
            <a class="hl-biz-text" href="{target}">{escape(c['card_link'])} <span aria-hidden="true">→</span></a>
          </div>
        </article>''')
    industries = ''.join(cards)
    improvements = ''.join(f'<li>{escape(step)}</li>' for step in c['improve_steps'])
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
        <div class="hl-home-improve"><span class="hl-home-improve-icon">{_example_icon('loop')}</span><div><p>{escape(c['improve_label'])}</p><ol>{improvements}</ol></div></div>
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
