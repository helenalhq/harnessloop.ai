"""Bilingual Solutions page, built with the existing site components."""
from html import escape


COPY = {
    'zh': {
        'title': '我们构建的示例',
        'eyebrow': '从业务任务出发',
        'promise': '你描述业务场景，我们为你构建在本地运行的 Harness。',
        'jump': '看两个方案',
        'showcases': '同一个方法，两种业务用法',
        'industries': ('货运代理', '医学研究与情报'),
        'alts': ('集装箱与起重机组成的港口作业场景', '桌面上的研究资料与阅读笔记'),
        'diagram': ('本地工作流', '方案示意', (
            ('授权资料', '你允许访问的信息和工具'),
            ('本地 Harness', '在配置的设备上运行'),
            ('待复核结果', '简报或草稿，并附来源依据'),
        )),
        'run_kicker': '从设计到交付',
        'delivery': '你会拿到什么',
        'final': '从你每天要做的一件事开始。',
        'intro': '从每天要跟进的货运异常，到需要核对来源的医学文献。让团队先看到变化、知道证据在哪里，再决定下一步。',
        'run_title': '在本地怎么运行',
        'run_steps': (
            ('先明确任务', '带来一份不含敏感信息的流程样例。一起确定输入、可用资料、访问权限和哪些结果必须由人复核。'),
            ('在本地安装与运行', '在支持的电脑或工作站安装运行组件，配置流程与工具。只用授权来源，可手动运行；设备和环境支持时，也可按约定定时运行。'),
            ('交付结果，保留依据', '在约定的本地界面或获准渠道查看简报或草稿，以及运行记录和来源依据。不确定或失败的项目交由人工处理，对外发送按约定执行。'),
        ),
        'scope': '你会拿到配置好的本地流程、输出模板，以及运行和复核记录；我们会用约定的样例和你一起验收。',
        'cta': '讨论你的方案',
        'cards': (
            ('货代智能客服助手', '少翻系统，少漏重要跟进。把变化、需要关注的事项和原因放在一处，先看重点，再决定怎么处理。',
             ('汇总获准查看的货运动态，突出新变化和还需要跟进的事项。',
              '关键信息缺失时，标明哪里需要核实、为什么不能直接答复。',
              '根据已确认的信息整理下一步或拟好回复，由工作人员核对、修改并决定是否发出。',
              '留痕即证据：每次查找、核对与草拟都记录时间与出处。FMC 规则下，滞期费与滞箱费账单只有 30 个日历日争议窗口——记录完整，才拿得出手。'),
             '示例跟进卡（合成）',
             (('日期尚未确认', '一条货运更新没有确认日期，暂不能对外承诺时间。'),
              ('回复草稿', '我们正在核实日期，确认后会更新。'),
              ('处理状态', '仅为草稿，待人工复核，未发送。'))),
            ('医学文献及情报管理助手', '不只知道有新文献，还能看清新增证据可能改变什么、每条结论能追到哪里。同一个 Harness，换一个领域——同一套受治理的流程。',
             ('按主题跟踪获准查阅的文献、指南和研究登记来源。',
              '对照已有简报，标出哪些结论可能需要更新、哪些暂不变、哪些仍不确定；保留来源链接、发布日期和原文位置。',
              '由研究人员核对原文与证据强度，再决定是否更新简报。用于研究与情报，不提供临床建议。'),
             '示例证据提示（合成）',
             (('新线索', '跟踪主题下出现一项新的公开研究，目前只读到摘要。'),
              ('证据边界', '不能据此判断建议是否改变。'),
              ('下一步', '核对全文和研究方法后，再决定是否更新简报。'))),
        ),
        'src_label': '出处',
        'isf': {
            'title': 'ISF 申报倒计时（合成示例）',
            'rows': (('船名', 'VESSEL ZZ'), ('预计装船', '11 月 26 日'), ('申报截止', '装船前 24 小时'), ('状态', '待补文件 · 未申报')),
            'note': '合成示例：非实时运行。ISF 须经 ABI/ACE 电子申报（美国海关与边境保护局要求）；我们做草拟、核对与期限看护，不代做申报。',
            'src': '19 CFR § 113.62',
        },
    },
    'en': {
        'title': 'Examples of what we build',
        'eyebrow': 'START WITH THE WORK',
        'promise': 'Tell us how you work. We build a Harness that runs on your own computer or workstation.',
        'jump': 'Explore the solutions',
        'showcases': 'One approach, two kinds of work',
        'industries': ('FREIGHT FORWARDING', 'MEDICAL RESEARCH & INTELLIGENCE'),
        'alts': ('Container terminal with cranes and cargo containers', 'Research papers and reading notes laid out on a desk'),
        'diagram': ('Local workflow', 'Illustrated workflow', (
            ('Authorized sources', 'Information and tools you approve'),
            ('Local Harness', 'Runs on your configured device'),
            ('Output for review', 'A brief or draft with source evidence'),
        )),
        'run_kicker': 'FROM DESIGN TO DELIVERY',
        'delivery': 'What you receive',
        'final': 'Start with one task your team does every day.',
        'intro': 'From daily freight exceptions to new medical literature, give your team a clear view of what changed, where the evidence is and what needs a human decision.',
        'run_title': 'How it runs',
        'run_steps': (
            ('Agree on the task', 'Bring a workflow example without sensitive details. We agree on the inputs, sources, access and what needs human review.'),
            ('Install and run locally', 'Install the runner on a supported computer or workstation, then configure the workflow and tools. Run it manually or on an agreed schedule where supported, using only authorized sources.'),
            ('Review the output and its evidence', 'See the brief or draft, run log and source evidence in the agreed local interface or approved channel. Uncertain or failed items go to a person. External sends follow the agreed rules.'),
        ),
        'scope': 'You receive a configured local workflow, output templates, and run and review records. We verify the setup together using agreed samples.',
        'cta': 'Discuss your workflow',
        'cards': (
            ('Freight Forwarding Customer Service Assistant', 'Spend less time switching between systems and miss fewer follow-ups. See what changed, what needs attention and why.',
             ('Bring together authorized shipment updates and surface changes and open follow-ups.',
              'Show what needs checking when a key detail is missing, and why it matters before responding.',
              'Suggest a next step or draft a reply from confirmed information. Staff review it, make any edits and decide whether to send it.',
              'Keep the evidence: every lookup, check and draft keeps its timestamp and source. Under the FMC rule, a D&D bill leaves you a 30-calendar-day window to dispute — a clean record is what you bring.'),
             'Sample follow-up card (synthetic)',
             (('No confirmed date', 'A shipment update does not include a confirmed date, so there is no date to promise.'),
              ('Response draft', 'We’re checking the date and will update you once it’s confirmed.'),
              ('Status', 'Draft only. Awaiting staff review; not sent.'))),
            ('Medical Literature & Intelligence Assistant', 'Go beyond alerts about new papers. See what new evidence may change and trace each conclusion to its source. The same harness, a different domain — built on the same governed pipeline.',
             ('Track approved literature, guideline publishers and study registries by topic.',
              'Compare with previous briefs. Flag conclusions that may need updating, those that remain unchanged and questions still open. Keep the source link, publication date and relevant passage.',
              'Researchers verify the sources and the strength of the evidence before updating the brief. For research and intelligence, not clinical advice.'),
             'Sample evidence alert (synthetic)',
             (('New item', 'A new public study appeared on a tracked topic. Only the abstract has been reviewed.'),
              ('Evidence limit', 'The abstract alone does not establish a change in recommendations.'),
              ('Next step', 'Check the full text and methods before deciding whether to update the brief.'))),
        ),
        'src_label': 'Source',
        'isf': {
            'title': 'ISF countdown (synthetic example)',
            'rows': (('Vessel', 'VESSEL ZZ'), ('Est. lading', 'NOV 26'), ('Filing deadline', '24 hours before lading'), ('Status', 'Documents pending · not filed')),
            'note': 'Synthetic example: not a live run. ISF must be filed electronically via ABI/ACE (per U.S. CBP). We draft, check and watch deadlines; we do not file.',
            'src': '19 CFR § 113.62',
        },
    },
}


def _icon(name):
    paths = {
        'sources': '<path d="M4 5h11l4 4v10H4z M15 5v4h4 M7 12h9 M7 15h7"/>',
        'device': '<rect x="3.5" y="4.5" width="17" height="12" rx="2"/><path d="M12 17v3m-4 0h8M8 11l2 2 4-4"/>',
        'review': '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 12l3 3 5-6"/>',
        'arr': '<path d="M4 12h15m-6-6 6 6-6 6"/>',
    }
    return f'<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">{paths[name]}</svg>'


def add_solutions(pages, lang):
    data = COPY[lang]
    contact = '/en/contact/' if lang == 'en' else '/contact/'
    diagram_title, diagram_label, diagram_steps = data['diagram']
    diagram = ''.join(
        f'<li class="hl-workflow-step"><span class="hl-workflow-icon">{_icon(icon)}</span>'
        f'<span><strong>{escape(label)}</strong><small>{escape(detail)}</small></span></li>'
        for icon, (label, detail) in zip(('sources', 'device', 'review'), diagram_steps)
    )
    isf = data['isf']
    isf_rows = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>' for label, value in isf['rows'])
    isf_html = f'''<section class="hl-sample hl-sample--isf" aria-labelledby="hl-sample-isf">
            <div class="hl-sample-title"><span class="hl-sample-icon">{_icon('device')}</span><h4 id="hl-sample-isf">{escape(isf['title'])}</h4></div>
            <dl>{isf_rows}</dl>
            <p class="hl-sample-note">{escape(isf['note'])} {escape(data['src_label'])}：<a href="https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62" target="_blank" rel="noopener noreferrer">{escape(isf['src'])}</a>{'。' if lang == 'zh' else '.'}</p>
          </section>'''
    showcases = []
    for i, (title, summary, steps, sample, rows) in enumerate(data['cards']):
        asset = ('freight', 'medical')[i]
        items = ''.join(f'<li>{escape(step)}</li>' for step in steps)
        notes = ''.join(f'<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>' for label, value in rows)
        alt = escape(data['alts'][i])
        extra = isf_html if i == 0 else ''
        showcases.append(f'''<article class="hl-showcase hl-showcase--{asset}">
          <div class="hl-showcase-pair">
            <div class="hl-showcase-copy">
              <p class="hl-kicker"><span>{i + 1:02}</span>{escape(data['industries'][i])}</p>
              <h3>{escape(title)}</h3><p class="hl-showcase-summary">{escape(summary)}</p>
              <ul class="hl-feature-list">{items}</ul>
            </div>
            <div class="hl-showcase-image">
              <img src="/assets/hl-{asset}-v3.webp" width="1260" height="840" loading="lazy" alt="{alt}">
            </div>
          </div>
          <section class="hl-sample" aria-labelledby="hl-sample-{asset}">
            <div class="hl-sample-title"><span class="hl-sample-icon">{_icon('sources')}</span><h4 id="hl-sample-{asset}">{escape(sample)}</h4></div>
            <dl>{notes}</dl>
          </section>
          {extra}
        </article>''')
    steps = ''.join(
        f'<li><span class="hl-run-number">{i:02}</span><h3>{escape(heading)}</h3><p>{escape(detail)}</p></li>'
        for i, (heading, detail) in enumerate(data['run_steps'], start=1)
    )
    title = data['title']
    arrow = _icon('arr')
    showcase_html = ''.join(showcases)
    body = f'''<div class="hl-solutions">
      <section class="hl-solutions-hero" aria-labelledby="hl-solutions-title">
        <div class="wrap hl-hero-grid">
          <div class="hl-hero-copy">
            <p class="hl-kicker hl-hero-kicker">{escape(data['eyebrow'])}</p>
            <h1 id="hl-solutions-title">{escape(title)}</h1>
            <p class="hl-promise">{escape(data['promise'])}</p>
            <p class="hl-intro">{escape(data['intro'])}</p>
            <div class="hl-actions">
              <a class="hl-action hl-action--primary" href="{contact}">{escape(data['cta'])}{arrow}</a>
              <a class="hl-action hl-action--secondary" href="#hl-showcases">{escape(data['jump'])}<span aria-hidden="true">↓</span></a>
            </div>
          </div>
          <figure class="hl-workflow" id="hl-workflow-diagram" aria-labelledby="hl-workflow-title">
            <figcaption><strong id="hl-workflow-title">{escape(diagram_title)}</strong><span>{escape(diagram_label)}</span></figcaption>
            <ol>{diagram}</ol>
          </figure>
        </div>
      </section>
      <section class="wrap hl-showcases" id="hl-showcases" aria-labelledby="hl-showcases-title">
        <h2 id="hl-showcases-title">{escape(data['showcases'])}</h2>
        {showcase_html}
      </section>
      <section class="hl-run" id="hl-local-run" aria-labelledby="hl-run-title">
        <div class="wrap">
          <p class="hl-kicker">{escape(data['run_kicker'])}</p>
          <h2 id="hl-run-title">{escape(data['run_title'])}</h2>
          <ol class="hl-run-steps">{steps}</ol>
          <div class="hl-deliverables"><h3>{escape(data['delivery'])}</h3><p>{escape(data['scope'])}</p></div>
        </div>
      </section>
      <section class="hl-final" aria-labelledby="hl-final-title">
        <div class="wrap hl-final-grid"><h2 id="hl-final-title">{escape(data['final'])}</h2>
          <a class="hl-action hl-action--primary" href="{contact}">{escape(data['cta'])}{arrow}</a>
        </div>
      </section>
    </div>'''
    pages['solutions'] = (title, body)
