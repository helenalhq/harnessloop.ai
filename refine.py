"""Revision 3: a focused systems-engineering identity, bilingual by design."""
def system(en=False):
 t = ['ILLUSTRATIVE RUN / NOT LIVE','A system that learns from the work.','Source document','Delivery: 15 business days','Current harness','Candidate harness','Extract','Evaluate','Propose','Validate','Promote','Pause animation','Next step','A controlled loop. Not unchecked change.','Synthetic example · Release requires approval.'] if en else ['流程演示 / 非实时运行','让下一次执行，有据可改。','原始资料','交货时间：15 个工作日','当前 Harness','候选 Harness','执行','评测','提议','验证','晋级','暂停演示','下一步','形成改进闭环，而不是放任修改。','合成示例 · 正式发布需要批准。']
 steps=''.join(f'<button type="button" class="cycle-step" data-cycle-step="{i}" aria-pressed="{str(i==0).lower()}"><span>0{i+1}</span>{t[6+i]}</button>' for i in range(5))
 return f'''<figure class="evolution" data-evolution data-phase="0"><figcaption><span class="signal-dot"></span>{t[0]}<span class="run-code">HL—01</span></figcaption><div class="evolution-source"><span>{t[2]}</span><strong>{t[3]}</strong><i aria-hidden="true">↓</i></div><div class="engine-plane"><div class="engine-label"><span data-version>{t[4]} · v0</span><span class="engine-state" data-state>01 / {t[6]}</span></div><div class="engine-core"><svg class="orbit-path" viewBox="0 0 420 150" preserveAspectRatio="none" aria-hidden="true"><path d="M70 75 C70 15 350 15 350 75 S70 135 70 75"/><circle r="4"><animateMotion dur="5s" repeatCount="indefinite" path="M70 75 C70 15 350 15 350 75 S70 135 70 75"/></circle></svg><div class="harness-chip"><span>HARNESS</span><strong data-output>{'15 days' if en else '15 天'}</strong><small data-output-note>{'Qualifier missing' if en else '单位限定丢失'}</small></div></div><div class="engine-evidence"><span data-evidence>{'Output awaiting evaluation' if en else '执行输出，等待质量检查'}</span><span class="phase-bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span></div></div><div class="branch-map"><div class="branch-title">{'CANDIDATES → INDEPENDENT CHECKS → GATE' if en else '候选分支 → 独立检查 → 发布闸门'}</div><div class="branch-route"><span>{'A · Preserve units' if en else 'A · 保留单位'}</span><i>→</i><b>{'Validate' if en else '待验证'}</b><i>→</i><span>{'Approval' if en else '人工批准'}</span></div><div class="branch-route rejected"><span>{'B · Infer missing data' if en else 'B · 推测缺失值'}</span><i>→</i><b>{'Reject' if en else '拒绝'}</b><i>×</i><span>{'No evidence' if en else '无来源依据'}</span></div></div><div class="cycle-nav" aria-label="{'Demonstration steps' if en else '演示步骤'}">{steps}</div><div class="cycle-story"><small data-story-label>{'EXECUTION / v0' if en else '任务执行 / v0'}</small><p data-story>{'The first extraction loses a critical qualifier. The output is not yet ready for delivery.' if en else '首次提取丢失了“工作日”限定。执行完成，不代表结果已经可以交付。'}</p></div><div class="cycle-controls"><button type="button" data-cycle-toggle>{t[11]}</button><button type="button" data-cycle-next>{t[12]} →</button><small>{t[14]}</small></div></figure>'''
def dual_loop(en=False):
 """Show execution and version change as separate loops with a human release gate."""
 if en:
  copy={
   'eyebrow':'TWO LOOPS · ONE CONTROLLED SYSTEM','title':'The assistant runs one version. The next version earns approval.',
   'lead':'Doing the work and changing the system are separate activities.',
   'principle':'The running version does not rewrite itself.',
   'run':'01 · RUN LOOP','run_state':'WORKING VERSION · FIXED DURING THE RUN',
   'run_steps':('Approved input','Context & tools','Execute & check','Draft + evidence','You review'),
   'run_note':'Authorized inputs and tools only. Sources, exceptions and review handoffs stay visible; uncertain work stops for a person.',
   'improve':'02 · IMPROVEMENT LOOP','improve_state':'CANDIDATE VERSION · NOT LIVE',
   'improve_steps':('Your correction','Candidate change','Independent validation','Your approval','Next version'),
   'improve_note':'Candidates are checked on independent examples for improvement and regressions. Approval, monitoring and rollback are explicit.',
   'gate':'RELEASE GATE','decision':'Human approval','gate_note':'No automatic promotion',
  }
 else:
  copy={
   'eyebrow':'两个循环 · 一套受控系统','title':'当前版本执行任务，下一版通过验证与批准。',
   'lead':'完成工作和修改系统，是两件分开的事。',
   'principle':'运行中的版本不会改写自己。',
   'run':'01 · 运行环','run_state':'当前版本 · 本次运行中保持不变',
   'run_steps':('授权输入','上下文与工具','执行与检查','草稿与依据','你来复核'),
   'run_note':'只使用获准的资料与工具。来源、异常和复核交接保持可见；无法可靠判断时，交给人处理。',
   'improve':'02 · 改进环','improve_state':'候选版本 · 尚未生效',
   'improve_steps':('你的纠正','候选改进','独立样本验证','你批准','进入下一版'),
   'improve_note':'候选版本用独立样本检查改善与回归。批准、监测和回退都是明确的发布环节。',
   'gate':'发布闸门','decision':'人工批准','gate_note':'不会自动晋级',
  }
 def steps(names):
  return ''.join(f'<li><span>{i:02}</span><strong>{name}</strong></li>' for i,name in enumerate(names,1))
 return f'''<section class="hl-approach-loops" aria-labelledby="hl-dual-loop-title"><div class="wrap hl-approach-loop-head"><span class="eyebrow">{copy['eyebrow']}</span><h2 id="hl-dual-loop-title">{copy['title']}</h2><p class="lead">{copy['lead']}</p></div>
 <figure class="wrap hl-dual-loop"><figcaption><span>{copy['principle']}</span><span>{'FIXED RUN · CONTROLLED CHANGE' if en else '固定运行 · 受控变更'}</span></figcaption>
 <div class="hl-loop-grid"><section class="hl-loop-panel hl-loop-panel--run" aria-labelledby="hl-run-loop-{('en' if en else 'zh')}"><header><h3 id="hl-run-loop-{('en' if en else 'zh')}">{copy['run']}</h3><span>{copy['run_state']}</span></header><ol>{steps(copy['run_steps'])}</ol><p>{copy['run_note']}</p></section>
 <div class="hl-release-gate"><svg width="28" height="28" viewBox="0 0 28 28" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="5" y="12" width="18" height="13" rx="3"/><path d="M9 12V8a5 5 0 0 1 10 0v4m-5 6v3"/></svg><span>{copy['gate']}</span><strong>{copy['decision']}</strong><small>{copy['gate_note']}</small></div>
 <section class="hl-loop-panel hl-loop-panel--improve" aria-labelledby="hl-improve-loop-{('en' if en else 'zh')}"><header><h3 id="hl-improve-loop-{('en' if en else 'zh')}">{copy['improve']}</h3><span>{copy['improve_state']}</span></header><ol>{steps(copy['improve_steps'])}</ol><p>{copy['improve_note']}</p></section></div></figure></section>'''


def enhance(pages, en=False):
 title,body=pages['how-it-works']
 pages['how-it-works']=(title,body.replace('<div data-dual-loop></div>',dual_loop(en)))
 if '' not in pages:  # the home body is built by business.home_body; keep the home route first
  rest=dict(pages);pages.clear();pages['']=('', '');pages.update(rest)
 title,body=pages['contact']
 old='This page creates a brief in your browser. It does not send or save it. A contact channel will be added once confirmed.'
 # Remove obsolete placeholder regardless of original English wording.
 import re
 if en:
  body=re.sub(r'<p>[^<]*(?:contact channel|contact route|contact method)[^<]*</p>','<p>Generate a brief here, then copy it into your email. This form does not send or save your input.</p>',body,flags=re.I)
  block='<div class="contact-address"><span class="eyebrow">START A CONVERSATION</span><a class="hl-email-address" href="mailto:contact@harnessloop.ai">contact@harnessloop.ai</a><a class="hl-direct-email" href="mailto:contact@harnessloop.ai">Open an email draft →</a><button class="copychip" type="button" id="copy-email" data-email="contact@harnessloop.ai">Copy address</button><p>Tell us what the task is, where it breaks down and what a good result looks like. We reply within 24 hours. Please use non-sensitive examples.</p></div>'
 else:
  body=body.replace('本页仅在浏览器中生成简报，不发送、不保存。正式联系入口将在确认后接入。','先在这里整理需求，再复制到邮件中。本表单不发送、不保存输入内容。')
  block='<div class="contact-address"><span class="eyebrow">联系 HARNESSLOOP</span><a class="hl-email-address" href="mailto:contact@harnessloop.ai">contact@harnessloop.ai</a><a class="hl-direct-email" href="mailto:contact@harnessloop.ai">打开邮件草稿 →</a><button class="copychip" type="button" id="copy-email" data-email="contact@harnessloop.ai">复制邮箱</button><p>告诉我们任务是什么、难在哪里，以及怎样才算做好。我们会在 24 小时内回复。请只使用不含敏感信息的示例。</p></div>'
 body=body.replace('<section class="wrap two"', '<div class="wrap">'+block+'</div><section class="wrap two"',1)
 # The email draft is the primary next step; copying is the fallback for machines without a mail app.
 note='You review and send the email yourself. Opening your email app does not send it. No mail app? Copy the brief into your webmail.' if en else '由你检查并发送邮件。打开邮件客户端不会自动发送。没有配置邮件客户端时，可复制简报到网页邮箱。'
 actions='<div class="hl-brief-actions"><a class="btn brief-email" id="email-brief" href="mailto:contact@harnessloop.ai">'+('Open the email draft' if en else '打开邮件草稿')+'</a><button class="btn secondary" id="copy-brief" type="button">'
 assert body.count('<button class="btn secondary" id="copy-brief" type="button">')==1 and body.count('<p id="copy-status"')==1
 body=body.replace('<button class="btn secondary" id="copy-brief" type="button">',actions,1).replace('<p id="copy-status"','</div><p class="micro">'+note+'</p><p id="copy-status"',1)
 pages['contact']=(title,body)
 title,body=pages['data-factory']
 body=body.replace('id="demo-output" aria-live="polite"','id="demo-output" role="tabpanel" aria-labelledby="stage-0" aria-live="polite" tabindex="0"')
 for i in range(3):
  body=body.replace(f'data-stage="{i}"', f'data-stage="{i}" id="stage-{i}" aria-controls="demo-output" tabindex="{0 if i==0 else -1}"')
 pages['data-factory']=(title,body)
