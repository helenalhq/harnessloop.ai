"""Three-act interactive demo page: synthetic morning brief, approval card, audit trail.

All content is synthetic and clearly labelled. The page is read-only client-side:
no backend, no form, no data collection. The only script is demo.js, which appends
audit rows in memory and writes status text via textContent.
"""


def _ships(en):
    ecfr = 'https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62'
    fmc = 'https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/'
    if en:
        return (
            ('alert', 'VESSEL ZZ · PO-11892', 'ISF filing — 4 hr 20 min left; 2 items missing: consignee tax ID, port-of-lading code', '19 CFR § 113.62', ecfr),
            ('warn', 'BK-20415 · Invoice #D-1104', 'D&amp;D dispute window — 12 days left; 5 records archived', 'FMC final rule', fmc),
            ('warn', 'BK-20431', 'Customer asks for the ETD — date unconfirmed; a reply draft waits for your review', 'Unknown flagged, not guessed', None),
            ('ok', 'BK-20388', 'Document check — 14 fields aligned to their source lines; no anomalies', 'Checked', None),
            ('ok', 'BK-20375', 'Duty pre-classification — suggestion reviewed and archived; nothing to do', 'Archived', None),
            ('ok', 'BK-20361', 'Booking confirmation — space confirmed; documents complete', 'Confirmed', None),
        )
    return (
        ('alert', 'VESSEL ZZ · PO-11892', 'ISF 申报 — 距截止 4 小时 20 分，缺 2 项：收货人税号、装货港代码', '19 CFR § 113.62', ecfr),
        ('warn', 'BK-20415 · 账单 #D-1104', '滞期费与滞箱费争议窗口 — 还剩 12 天，已归档 5 份往来记录', 'FMC 最终规则', fmc),
        ('warn', 'BK-20431', '客户催问预计开船时间 — 日期未确认，回复草稿已生成，等你审批', '不猜测 · 标出未知', None),
        ('ok', 'BK-20388', '单据核对 — 14 个字段已对齐来源行，无异常', '已核对', None),
        ('ok', 'BK-20375', '关税预归类 — 建议已复核并归档，无需跟进', '已归档', None),
        ('ok', 'BK-20361', '订舱确认 — 舱位已确认，资料齐全', '已确认', None),
    )


def add_demo(pages, lang):
    en = lang == 'en'
    prefix = '/en/' if en else '/'
    contact = prefix + 'contact/'
    if en:
        banner = 'Synthetic data · Interactive demo · No real shipments'
        kicker = 'INTERACTIVE DEMO · ABOUT 3 MINUTES'
        title = 'Three acts. Watch how it works.'
        lead = 'Act one: a morning brief lays out six items and their anomalies at a glance. Act two: a reply draft with an unconfirmed date — approve, edit or reject, it is your click. Act three: the four-part record every action leaves behind. Read-only, no backend, no data collection.'
        acts = (('01', 'Brief'), ('02', 'Follow-up'), ('03', 'Audit trail'))
        a1 = ('ACT ONE · THE MORNING BRIEF', 'Every morning, the anomalies surface.',
              'The daily brief lays out status, anomalies and sources at a glance. The red and amber rows are the three anomalies; only BK-20431 has a draft waiting for you.')
        a2 = ('ACT TWO · THE FOLLOW-UP CARD', 'Ready to send? You decide.',
              'The customer asks for an estimated departure and the date is not confirmed. The assistant drafts the reply — and does not send it. Approve, edit or reject: your click.')
        review = ('THE REVIEW BOUNDARY', 'A draft is not an action.', (
            ('Source', 'The carrier has not confirmed a departure date.'),
            ('Assistant', 'Drafts a cautious holding reply; never invents an ETD.'),
            ('You', 'Nothing is sent until you approve it in your mail client.'),
        ))
        a3 = ('ACT THREE · THE AUDIT TRAIL', 'Every action leaves a four-part record.',
              'Time, source, judgment, action — who did what, based on what, when. When a bill is disputed, this is your evidence. Clicking the buttons in act two appends a demo row to this table.')
        brief_mast = ('Morning brief · Synthetic example', 'NO. 004')
        brief_meta = ('Wednesday, 25 November 2026', 'Runs locally; data never leaves your device')
        stats = (('6', 'items summarized'), ('3', 'anomalies flagged'), ('1', 'draft awaiting approval'))
        a1_note = 'The green rows keep their sources too. Here they are static rows; in a live brief, every row opens to show its source and the original passage.'
        a2_head = ('Follow-up card · BK-20431', 'Date unconfirmed')
        draft_label = 'Draft email · Not sent'
        draft_rows = (('From', 'You (not sent)'), ('To', 'shipper@example.com'), ('Subject', 'Re: BK-20431 estimated departure'))
        draft_body = 'Hello, regarding the estimated departure of BK-20431, we are checking with the carrier and will update you as soon as it is confirmed.'
        buttons = (('approve', 'Approve'), ('edit', 'Edit'), ('reject', 'Reject'), ('reset', 'Reset demo'))
        notice_default = 'Click any button above and watch what happens.'
        log_headers = ('Time', 'Source', 'Judgment', 'Action')
        seed = (
            ('08:00:12', 'System · Brief v004', 'Automatic', 'Aggregated 6 items; flagged 3 anomalies'),
            ('08:00:14', 'System · Brief v004', 'Automatic', 'Drafted reply: BK-20431 ETD (date unconfirmed)'),
        )
        a3_note = 'Synthetic demo records, held only in this page. Refresh clears them.'
        final_h = 'That is the whole demo.'
        final_p = 'No backend, no login, no data collection — every number and row above is synthetic. In a real deployment, the same three acts run on your data, your SOP and your approvals.'
        exit_text = 'Discuss your workflow'
        cta = 'Discuss your workflow'
    else:
        banner = '合成数据 · 交互演示 · 非真实货物'
        kicker = '交互演示 · 约 3 分钟'
        title = '三幕，看它怎么工作。'
        lead = '第一幕：晨报把 6 项状态和异常一次性摆出来。第二幕：一封日期未确认的回复草稿，批准、编辑或拒绝由你点。第三幕：每个动作留下的四元组记录。全程只读、无后端、不收集数据。'
        acts = (('01', '晨报'), ('02', '跟进卡'), ('03', '留痕'))
        a1 = ('第一幕 · 晨报', '一早，异常自己浮出来。',
              '每天生成的晨报把状态、异常和来源一次性摆出来。红色与黄色的三行就是那 3 处异常；只有 BK-20431 有一封草稿等你审批。')
        a2 = ('第二幕 · 跟进卡', '要发出去吗？你说了算。',
              '客户催问预计开船时间，而日期还没确认。助手写好草稿，但不发送——批准、编辑还是拒绝，由你点。')
        review = ('复核边界', '草稿不等于已执行。', (
            ('来源', '船公司尚未确认开船日期。'),
            ('助手', '只起草谨慎的跟进回复，不编造预计开船时间。'),
            ('你', '在你的邮件客户端里批准之前，不会发出任何内容。'),
        ))
        a3 = ('第三幕 · 留痕', '每个动作，留下四元组记录。',
              '时间、来源、判断、动作——谁在什么时候基于什么做了什么。账单有争议时，这就是你的证据。点击第二幕的按钮，会给这张表追加一条演示记录。')
        brief_mast = ('晨报 · 合成示例', 'NO. 004')
        brief_meta = ('2026 年 11 月 25 日 · 星期三', '本地运行，数据未离开你的设备')
        stats = (('6 项', '状态汇总'), ('3 处', '异常标记'), ('1 封', '草稿待审批'))
        a1_note = '绿色行同样保留出处。演示里它们是静态行；真实晨报中，每一行都可以点开，看到出处与原文位置。'
        a2_head = ('跟进卡 · BK-20431', '日期未确认')
        draft_label = '草稿邮件 · 未发送'
        draft_rows = (('发件人', '你（未发送）'), ('收件人', 'shipper@example.com'), ('主题', 'Re: BK-20431 预计开船时间'))
        draft_body = '您好，关于 BK-20431 的预计开船时间，我们正在与船公司确认，一旦确定会第一时间回复您。'
        buttons = (('approve', '批准发送'), ('edit', '编辑'), ('reject', '拒绝'), ('reset', '重置演示'))
        notice_default = '点击上面任意一个按钮，看看会发生什么。'
        log_headers = ('时间', '来源', '判断', '动作')
        seed = (
            ('08:00:12', '系统 · 晨报 v004', '自动', '汇总 6 项状态，标记 3 处异常'),
            ('08:00:14', '系统 · 晨报 v004', '自动', '生成回复草稿：BK-20431 预计开船时间（日期未确认）'),
        )
        a3_note = '以上为合成演示记录，只存在于当前页面，刷新即清空。'
        final_h = '演示到此为止。'
        final_p = '没有后端、没有登录、没有数据收集——上面的每一个数字、每一行记录都是合成的。真实部署里，同样的三幕跑的是你的业务数据、你的 SOP 和你的审批。'
        exit_text = '讨论你的业务场景'
        cta = '讨论你的业务场景'

    # The three flagged rows are exactly the three anomalies and the single draft in the
    # stats above; keep the counts, the dots and the seed audit rows in step.
    ships = ''.join(
        f'''<div class="hl-demo-ship"><span class="dot dot--{status}" aria-hidden="true"></span><div><strong>{label}</strong><p>{detail}</p></div>{f'<a class="hl-demo-chip" href="{url}" target="_blank" rel="noopener noreferrer">{chip} <span aria-hidden="true">→</span></a>' if url else f'<span class="hl-demo-chip">{chip}</span>'}</div>'''
        for status, label, detail, chip, url in _ships(en)
    )
    stats_html = ''.join(f'<div><b>{number}</b><span>{name}</span></div>' for number, name in stats)
    acts_html = ''.join(f'<a href="#hl-demo-act-{i}"><span aria-hidden="true">{number}</span>{name}</a>' for i, (number, name) in enumerate(acts, 1))
    buttons_html = ''.join(f'<button type="button" class="hl-demo-btn hl-demo-btn--{action}" data-demo-action="{action}">{label}</button>' for action, label in buttons)
    review_html = ''.join(f'<li><strong>{label}</strong><span>{detail}</span></li>' for label, detail in review[2])
    draft_fields = ''.join(f'<div><dt>{key}</dt><dd>{value}</dd></div>' for key, value in draft_rows)
    seed_html = ''.join(f'<tr><td>{time}</td><td>{source}</td><td>{judgment}</td><td>{action}</td></tr>' for time, source, judgment, action in seed)
    headers_html = ''.join(f'<th scope="col">{header}</th>' for header in log_headers)
    a1_note_para = f'<p class="hl-demo-note">{a1_note}</p>'
    a3_note_para = f'<p class="hl-demo-note">{a3_note}</p>'
    body = f'''<div class="hl-business hl-demo">
      <div class="hl-demo-banner">{banner}</div>
      <section class="hl-demo-hero" aria-labelledby="hl-demo-title"><div class="wrap">
        <p class="hl-biz-kicker">{kicker}</p>
        <h1 id="hl-demo-title">{title}</h1>
        <p class="hl-demo-lead">{lead}</p>
        <nav class="hl-demo-acts" aria-label="{('Demo acts' if en else '演示三幕')}">{acts_html}</nav>
      </div></section>
      <section class="wrap hl-demo-act" id="hl-demo-act-1" aria-labelledby="hl-demo-a1-title">
        <p class="hl-biz-kicker">{a1[0]}</p><h2 id="hl-demo-a1-title">{a1[1]}</h2><p class="hl-demo-lead">{a1[2]}</p>
        <div class="hl-demo-brief">
          <div class="hl-demo-brief-head"><strong>{brief_mast[0]}</strong><span class="tag">{brief_mast[1]}</span></div>
          <div class="hl-demo-brief-meta"><span>{brief_meta[0]}</span><span>{brief_meta[1]}</span></div>
          <div class="hl-demo-stats">{stats_html}</div>
          <div class="hl-demo-ships">{ships}</div>
        </div>
        {a1_note_para}
      </section>
      <section class="wrap hl-demo-act" id="hl-demo-act-2" aria-labelledby="hl-demo-a2-title">
        <p class="hl-biz-kicker">{a2[0]}</p><h2 id="hl-demo-a2-title">{a2[1]}</h2><p class="hl-demo-lead">{a2[2]}</p>
        <div class="hl-demo-act2-grid">
          <div class="hl-demo-follow">
            <div class="hl-demo-follow-head"><strong>{a2_head[0]}</strong><span class="tag">{a2_head[1]}</span></div>
            <div class="hl-demo-draft">
              <div class="hl-demo-draft-head"><span>{draft_label}</span><span>{('Visible only in your email client' if en else '只在你的邮件客户端里可见')}</span></div>
              <dl class="hl-demo-draft-fields">{draft_fields}</dl>
              <p>{draft_body}</p>
            </div>
            <div class="hl-demo-actions">{buttons_html}</div>
            <p class="hl-demo-notice" id="hl-demo-notice" role="status" aria-live="polite">{notice_default}</p>
          </div>
          <aside class="hl-demo-review" aria-label="{review[0]}">
            <p>{review[0]}</p><h3>{review[1]}</h3><ol>{review_html}</ol>
          </aside>
        </div>
        <div class="hl-demo-exit"><a class="hl-biz-text" href="{contact}">{exit_text} <span aria-hidden="true">→</span></a></div>
      </section>
      <section class="wrap hl-demo-act" id="hl-demo-act-3" aria-labelledby="hl-demo-a3-title">
        <p class="hl-biz-kicker">{a3[0]}</p><h2 id="hl-demo-a3-title">{a3[1]}</h2><p class="hl-demo-lead">{a3[2]}</p>
        <div class="hl-demo-log-wrap" role="region" aria-label="{('Synthetic audit trail' if en else '合成留痕记录')}">
          <table class="hl-demo-log" aria-label="{('Synthetic audit trail' if en else '合成留痕记录')}">
            <thead><tr>{headers_html}</tr></thead>
            <tbody id="hl-demo-log" data-seed="2">{seed_html}</tbody>
          </table>
        </div>
        {a3_note_para}
      </section>
      <section class="hl-demo-final"><div class="wrap hl-demo-final-grid"><div>
        <h2>{final_h}</h2><p>{final_p}</p>
      </div><a class="hl-biz-button" href="{contact}">{cta} <span aria-hidden="true">→</span></a></div></section>
    </div>'''
    pages['demo'] = ('演示' if not en else 'Demo', body)
