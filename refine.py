"""Revision 3: a focused systems-engineering identity, bilingual by design."""
def system(en=False):
 t = ['ILLUSTRATIVE RUN / NOT LIVE','A system that learns from the work.','Source document','Delivery: 15 business days','Current harness','Candidate harness','Extract','Evaluate','Propose','Validate','Promote','Pause animation','Next step','A controlled loop. Not unchecked change.','Synthetic example · Release requires approval.'] if en else ['流程演示 / 非实时运行','让下一次执行，有据可改。','原始资料','交货时间：15 个工作日','当前 Harness','候选 Harness','执行','评测','提议','验证','晋级','暂停演示','下一步','形成改进闭环，而不是放任修改。','合成示例 · 正式发布需要批准。']
 steps=''.join(f'<button type="button" class="cycle-step" data-cycle-step="{i}" aria-pressed="{str(i==0).lower()}"><span>0{i+1}</span>{t[6+i]}</button>' for i in range(5))
 return f'''<figure class="evolution" data-evolution data-phase="0"><figcaption><span class="signal-dot"></span>{t[0]}<span class="run-code">HL—01</span></figcaption><div class="evolution-source"><span>{t[2]}</span><strong>{t[3]}</strong><i aria-hidden="true">↓</i></div><div class="engine-plane"><div class="engine-label"><span data-version>{t[4]} · v0</span><span class="engine-state" data-state>01 / {t[6]}</span></div><div class="engine-core"><svg class="orbit-path" viewBox="0 0 420 150" preserveAspectRatio="none" aria-hidden="true"><path d="M70 75 C70 15 350 15 350 75 S70 135 70 75"/><circle r="4"><animateMotion dur="5s" repeatCount="indefinite" path="M70 75 C70 15 350 15 350 75 S70 135 70 75"/></circle></svg><div class="harness-chip"><span>HARNESS</span><strong data-output>{'15 days' if en else '15 天'}</strong><small data-output-note>{'Qualifier missing' if en else '单位限定丢失'}</small></div></div><div class="engine-evidence"><span data-evidence>{'Output awaiting evaluation' if en else '执行输出，等待质量检查'}</span><span class="phase-bars" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span></div></div><div class="branch-map"><div class="branch-title">{'CANDIDATES → INDEPENDENT CHECKS → GATE' if en else '候选分支 → 独立检查 → 发布闸门'}</div><div class="branch-route"><span>{'A · Preserve units' if en else 'A · 保留单位'}</span><i>→</i><b>{'Validate' if en else '待验证'}</b><i>→</i><span>{'Approval' if en else '人工批准'}</span></div><div class="branch-route rejected"><span>{'B · Infer missing data' if en else 'B · 推测缺失值'}</span><i>→</i><b>{'Reject' if en else '拒绝'}</b><i>×</i><span>{'No evidence' if en else '无来源依据'}</span></div></div><div class="cycle-nav" aria-label="{'Demonstration steps' if en else '演示步骤'}">{steps}</div><div class="cycle-story"><small data-story-label>{'EXECUTION / v0' if en else '任务执行 / v0'}</small><p data-story>{'The first extraction loses a critical qualifier. The output is not yet ready for delivery.' if en else '首次提取丢失了“工作日”限定。执行完成，不代表结果已经可以交付。'}</p></div><div class="cycle-controls"><button type="button" data-cycle-toggle>{t[11]}</button><button type="button" data-cycle-next>{t[12]} →</button><small>{t[14]}</small></div></figure>'''
def enhance(pages, en=False):
 if '' not in pages:  # the home body is built by business.home_body; keep the home route first
  rest=dict(pages);pages.clear();pages['']=('', '');pages.update(rest)
 title,body=pages['contact']
 old='This page creates a brief in your browser. It does not send or save it. A contact channel will be added once confirmed.'
 # Remove obsolete placeholder regardless of original English wording.
 import re
 if en:
  body=re.sub(r'<p>[^<]*(?:contact channel|contact route|contact method)[^<]*</p>','<p>Generate a brief here, then copy it into your email. This form does not send or save your input.</p>',body,flags=re.I)
  block='<div class="contact-address"><span class="eyebrow">START A CONVERSATION</span><a href="mailto:contact@harnessloop.ai">contact@harnessloop.ai</a><button class="copychip" type="button" id="copy-email" data-email="contact@harnessloop.ai">Copy address</button><p>Tell us what the task is, where it breaks down and what a good result looks like. We reply within 24 hours. Please use non-sensitive examples.</p></div>'
 else:
  body=body.replace('本页仅在浏览器中生成简报，不发送、不保存。正式联系入口将在确认后接入。','先在这里整理需求，再复制到邮件中。本表单不发送、不保存输入内容。')
  block='<div class="contact-address"><span class="eyebrow">联系 HARNESSLOOP</span><a href="mailto:contact@harnessloop.ai">contact@harnessloop.ai</a><button class="copychip" type="button" id="copy-email" data-email="contact@harnessloop.ai">复制邮箱</button><p>告诉我们任务是什么、难在哪里，以及怎样才算做好。我们会在 24 小时内回复。请只使用不含敏感信息的示例。</p></div>'
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
