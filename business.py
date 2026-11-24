"""Business-first landing and contact layout. Contact controls are reused, not reimplemented."""
from html import escape
from refine import system

COPY = {
    'zh': {
        'tag': '为你的业务定制',
        'hero': '把每天重复的工作，做成在你本地运行的助手。',
        'lead': '把要跟进的变化、查过的资料和待复核的结果放在一起。我们先和你选一件值得做好的事，再按你的工具、权限和验收要求配置。',
        'cta': '讨论你的业务场景',
        'jump': '查看解决方案',
        'deliver': '从输入到交付',
        'flow': (
            ('从现有资料开始', '只接入你批准的来源和工具。'),
            ('把重点整理出来', '得到简报、回复草稿或带出处的记录。'),
            ('重要决定由你复核', '不确定的信息不猜测，对外操作按约定执行。'),
        ),
        'sector': '业务解决方案',
        'examples': '先做出团队每天用得上的东西。',
        'cards': (
            ('货运代理', '货代智能客服助手', '少翻系统，少漏重要跟进。一次看清变化、待确认项和可以交给同事复核的回复草稿。','查看示例跟进卡','港口集装箱和起重机'),
            ('医学研究与情报', '医学文献及情报管理助手', '不只知道有新文献，还看得出证据可能改变什么，并能沿出处核对。研究人员决定是否更新简报。','查看示例证据提示','桌上的研究资料与阅读笔记'),
        ),
        'proof': '我们的工作方法',
        'method': '先看结果，再决定要不要扩大范围。',
        'method_detail': '用约定样本验证输出是否有出处、未知是否被标出、复核交接是否可用。不把演示当客户成果。',
        'approach': '了解工作原理',
        'demo': '查看数据工厂演示',
        'show_demo': '展开一个合成示例',
        'next': '你想先解决哪件事？',
        'final_copy': '不需要先共享业务数据。用几句话说清任务、目前的难点，以及怎样才算做好。',
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
        'tag': 'BUILT AROUND YOUR WORK',
        'hero': 'Turn recurring work into an assistant that runs on your own computer.',
        'lead': 'See what changed, what the sources say and what needs a person’s review. Start with one task, then shape the workflow around your tools, permissions and acceptance criteria.',
        'cta': 'Discuss your workflow',
        'jump': 'Explore the solutions',
        'deliver': 'From input to review',
        'flow': (
            ('Start with your sources', 'Use only the information and tools you approve.'),
            ('Get something your team can use', 'A brief, a response draft or a record with sources.'),
            ('Keep people in charge', 'Flag uncertainty. External actions follow agreed rules.'),
        ),
        'sector': 'BUSINESS SOLUTIONS',
        'examples': 'Start with something your team can use.',
        'cards': (
            ('Freight forwarding', 'Freight Forwarding Customer Service Assistant', 'Spend less time switching between systems and miss fewer follow-ups. See what changed, what to check and what reply is ready for review.','See a sample follow-up card','Container cranes and stacks at a freight terminal'),
            ('Medical research and intelligence', 'Medical Literature & Intelligence Assistant', 'Go beyond new-paper alerts. See what evidence may change, trace it to its source, and let researchers decide whether to update the brief.','See a sample evidence alert','Research papers and reading notes on a desk'),
        ),
        'proof': 'HOW WE WORK',
        'method': 'Check the result before expanding the scope.',
        'method_detail': 'Use agreed examples to verify sources, uncertainty flags and review handoffs. A demonstration is not a customer result.',
        'approach': 'Explore the approach',
        'demo': 'See the data factory demo',
        'show_demo': 'Open a synthetic example',
        'next': 'What would you start with?',
        'final_copy': 'No need to share business data. Tell us what the task is, what’s difficult today and what a good result would look like.',
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


def home_body(lang):
    c = COPY[lang]
    prefix = '/en/' if lang == 'en' else '/'
    contact = prefix + 'contact/'
    flow = ''.join(
        f'<li><span aria-hidden="true">{n:02}</span><div><strong>{escape(label)}</strong><p>{escape(description)}</p></div></li>'
        for n, (label, description) in enumerate(c['flow'], 1)
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
    return f'''<div class="hl-business hl-home">
      <section class="hl-biz-hero" aria-labelledby="hl-home-title">
        <div class="wrap hl-biz-hero-grid"><div>
          <p class="hl-biz-kicker">{escape(c['tag'])}</p><h1 id="hl-home-title">{escape(c['hero'])}</h1>
          <p class="hl-biz-lead">{escape(c['lead'])}</p><div class="hl-biz-actions">
            <a class="hl-biz-button" href="{contact}">{escape(c['cta'])} <span aria-hidden="true">→</span></a>
            <a class="hl-biz-secondary" href="#hl-home-solutions">{escape(c['jump'])} <span aria-hidden="true">↓</span></a>
          </div></div><aside class="hl-home-flow"><h2>{escape(c['deliver'])}</h2><ol>{flow}</ol></aside>
        </div>
      </section>
      <section class="wrap hl-home-solutions" id="hl-home-solutions" aria-labelledby="hl-home-examples-title">
        <p class="hl-biz-kicker">{escape(c['sector'])}</p><h2 id="hl-home-examples-title">{escape(c['examples'])}</h2>
        <div class="hl-home-cards">{industries}</div>
      </section>
      <section class="hl-home-method" id="hl-home-method" aria-labelledby="hl-home-method-title">
        <div class="wrap"><p class="hl-biz-kicker">{escape(c['proof'])}</p><h2 id="hl-home-method-title">{escape(c['method'])}</h2>
          <p>{escape(c['method_detail'])}</p>
          <div class="hl-biz-actions"><a class="hl-biz-text" href="{prefix}how-it-works/">{escape(c['approach'])} <span aria-hidden="true">→</span></a>
          <a class="hl-biz-text" href="{prefix}data-factory/">{escape(c['demo'])} <span aria-hidden="true">→</span></a></div>
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
