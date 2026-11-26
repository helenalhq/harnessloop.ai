"""Production metadata and safe static-page behavior, shared by all builds."""
from html import escape
import os
ORIGIN='https://harnessloop.ai'
# Vercel context is authoritative: a Preview must never inherit a production override.
PRODUCTION=(os.environ.get('VERCEL_ENV')=='production') if 'VERCEL_ENV' in os.environ else os.environ.get('SITE_ENV')=='production'
DESCRIPTIONS={
 '':['货代与报关的本地 AI 助手：草拟回复、跟进每一票货物、盯住申报期限，发出之前先经你审批。一次性部署，无按坐席订阅。','A local AI assistant for small freight forwarders and customs brokers. It drafts replies, tracks follow-ups and watches deadlines — nothing is sent without your review.'],
 'how-it-works':['了解 HarnessLoop 的运行环与改进环：明确权限、保留证据、验证候选版本，再决定发布。','Explore execution and improvement loops: scoped permissions, traceable evidence, independent validation and controlled releases.'],
 'data-factory':['通过合成采购示例，了解资料抽取、来源定位、质量检查和候选改进如何组成数据与知识工厂。','A synthetic procurement example shows how extraction, source evidence, quality checks and candidate improvements form a data factory.'],
 'demo':['三幕交互演示：合成晨报汇总异常、跟进卡审批草稿、四元组留痕记录。只读、无后端、不收集数据。','A three-act interactive demo: a synthetic morning brief, an approval card and a four-part audit trail. Read-only, no backend, no data collection.'],
 'solutions':['货代与医学文献两类示例工作流：本地运行、保留出处、关键节点人工复核，并含 ISF 申报倒计时合成示例。','Example workflows for freight forwarding and medical literature: local operation, traceable sources and human review points, including a synthetic ISF countdown.'],
 'research':['HarnessLoop 实践笔记：双闭环设计、失败分类、独立评测与可追溯的版本改进。','HarnessLoop design notes on dual loops, failure classification, independent evaluation and traceable version improvement.'],
 'contact':['联系 HarnessLoop，讨论业务任务与验收标准。使用本地简报工具整理需求，再由你选择是否发送邮件。','Discuss your business task and acceptance criteria with HarnessLoop. Prepare a brief locally and choose whether to email it.'],
 'faq':['关于本地运行、数据边界、申报合规、收费与交付的常见问题。','Local operation, data boundaries, filing compliance, pricing and delivery: questions and answers.'],
 'privacy':['了解 HarnessLoop 网站的本地简报、语言偏好、托管访问日志与邮件联系的数据处理范围。','Learn about local briefs, language preferences, hosting access logs and email contact on the HarnessLoop website.']}
# Search-result titles, [Chinese, English]. They name the page's subject, not only its nav label.
TITLES={
 '':['货代与报关的本地 AI 助手','Local AI for Freight Forwarding & Customs'],
 'demo':['交互演示：晨报、审批与留痕','Interactive Demo: Brief, Approval, Audit Trail'],
 'solutions':['货代与医学文献 AI 助手示例','Examples: Freight & Medical AI Assistants'],
 'how-it-works':['工作原理：运行环与改进环','How It Works: Run Loop and Improvement Loop'],
 'data-factory':['数据与知识工厂：合成示例演示','Data & Knowledge Factory: Synthetic Demo'],
 'research':['实践笔记：设计方法与证据','Field Notes: Design Methods and Evidence'],
 'contact':['联系合作','Contact HarnessLoop'],
 'privacy':['隐私说明','Privacy Notice'],
 'faq':['常见问题：本地运行、收费与交付','FAQ: Local Operation, Pricing and Delivery']}
def privacy(en):
 if en:return '''<div class="wrap subhero"><span class="eyebrow">PRIVACY</span><h1>Your information, in context.</h1><p class="micro">Updated 15 November 2026</p><h2>What this website does</h2><p class="lead">HarnessLoop is an informational website with synthetic demonstrations. It has no user accounts, payment processing or file uploads. Service scope and data handling for a client project are agreed separately before any project data is provided.</p><h2>A brief stays in your browser</h2><p>The brief tool generates text in the current page. It does not submit your input to a server, save it in cookies or local storage, or retain it after refresh or a language switch. Copying uses your browser clipboard. The email link opens your mail application with a draft; you decide whether to send it.</p><h2>Local storage and hosting</h2><p>This website stores nothing in your browser: no cookies and no local storage. Chinese and English pages have stable URLs; use the language link in the header to switch, and in-site links keep your language. This website does not include analytics trackers, advertising scripts, third-party fonts or an external form service. Hosting providers may process network and request information to serve and secure the website. For Vercel’s practices, see <a href="https://vercel.com/legal/privacy-policy" rel="noopener noreferrer" target="_blank">Vercel’s privacy notice</a>.</p><h2>The demo video</h2><p>The walkthrough video on the home page is hosted on GitHub (github.com), not on this website. The still image and player appear first; the video itself is requested from GitHub only when you press play, and GitHub then receives your IP address for that request. A link under the video opens the same file on GitHub.</p><h2>When you email</h2><p>Messages you choose to send to contact@harnessloop.ai pass through email providers and are available to the recipient to review and respond to your enquiry. Email is separate from the local brief tool. Please do not send medical records, personal sensitive information, credentials or confidential client data. Agree a suitable data-sharing process before supplying project materials.</p><h2>Questions and requests</h2><p>For questions about this website or information you have sent, contact <a href="mailto:contact@harnessloop.ai">contact@harnessloop.ai</a>. Include only the information needed to identify your enquiry.</p></div>'''
 return '''<div class="wrap subhero"><span class="eyebrow">隐私说明</span><h1>清楚说明，<br>信息在哪里处理。</h1><p class="micro">更新于 2026 年 11 月 15 日</p><h2>本站的范围</h2><p class="lead">HarnessLoop 是业务介绍与合成演示网站，不提供用户账号、支付或文件上传。客户项目的服务范围与数据处理方式，应在提供项目数据前另行约定。</p><h2>简报只在浏览器中生成</h2><p>简报工具在当前页面中生成文字，不向服务器提交输入，不写入 Cookie 或本地存储，刷新或切换语言后不保留。复制功能使用浏览器剪贴板。邮件链接会在邮件客户端中打开草稿，是否发送由你决定。</p><h2>本地存储与托管</h2><p>本站不在你的浏览器中保存任何数据：没有 Cookie，也没有本地存储。中英文页面各有固定网址，通过页首语言链接切换，站内链接会保持你的语言。本站没有接入分析追踪、广告脚本、第三方字体或外部表单服务。托管服务商可能为提供网站和保障安全处理网络及访问请求信息。Vercel 的处理方式见其<a href="https://vercel.com/legal/privacy-policy" rel="noopener noreferrer" target="_blank">隐私说明</a>。</p><h2>关于演示视频</h2><p>首页的演示视频托管在 GitHub（github.com），不在本站服务器上。页面先显示封面图和播放器，只有在你点击播放时才会向 GitHub 请求视频，届时 GitHub 会收到你的 IP 地址。视频下方的链接可在 GitHub 上打开同一文件。</p><h2>当你主动发送邮件</h2><p>主动发送到 contact@harnessloop.ai 的邮件会经过邮件服务商处理，收件方可阅读并用于了解和回复你的咨询。这与本地简报工具是不同的处理过程。请勿发送病历、个人敏感信息、密码或客户机密；提供项目资料前，请先约定适当的数据交换方式。</p><h2>问题与请求</h2><p>如对本站或已发送的信息有疑问，请联系 <a href="mailto:contact@harnessloop.ai">contact@harnessloop.ai</a>，仅提供定位咨询所需的信息。</p></div>'''
def prepare(body,slug,en):
 if slug=='privacy':return privacy(en)
 body=body.replace('在每次反馈中进化。','以验证驱动持续进化。')
 if slug=='contact':
  # Three short numbered steps read faster than one run-on paragraph; the limits stay visible below them.
  steps_en=['Fill in the fields and generate a local brief.','Open the email draft in your email app.','Review it there, then click Send.']
  steps_zh=['填写内容，生成本地简报。','在邮件客户端打开邮件草稿。','检查无误后，在邮件客户端点击发送。']
  steps=''.join('<li>'+step+'</li>' for step in (steps_en if en else steps_zh))
  limit=('This website does not submit or send messages. If no email app is configured, copy the brief into your webmail and send it to contact@harnessloop.ai.' if en else '本站不会提交表单或自动发邮件。如未配置邮件客户端，请复制简报到网页邮箱，发送至 contact@harnessloop.ai。')
  explanation=f'<strong>{"Three steps" if en else "如何联系"}</strong><ol>{steps}</ol><span class="notice-note">{limit}</span>'
  body=body.replace('<div class="box"><h3>', '<div class="box"><div class="notice notice-steps">'+explanation+'</div><h3>',1)
  body=body.replace('<form class="form" id="brief-form">','<div class="form" id="brief-form" role="group" aria-label="'+('Local brief tool' if en else '本地简报工具')+'">').replace('</form>','</div>')
  body=body.replace('type="submit"','type="button" id="generate-brief"')
  body=body.replace('name="task"','name="task" autocomplete="off"').replace('name="pain"','name="pain" autocomplete="off"').replace('name="criteria"','name="criteria" autocomplete="off"')
  body+='<noscript><p class="wrap notice">'+('JavaScript is unavailable. The brief tool is disabled; use the email address above to contact us. Nothing entered here is submitted.' if en else 'JavaScript 不可用，简报工具无法运行。请使用上方邮箱联系；这里填写的内容不会提交。')+'</p></noscript>'
 if slug=='data-factory':
  body+='<noscript><p class="wrap notice">'+('Static example: the source says “15 business days”, but the baseline extracts “15 days”. A candidate keeps the original unit; independent validation is still required.' if en else '静态示例：原文为“15 个工作日”，基线误提取为“15 天”。候选版本保留原始单位，但仍需独立验证。')+'</p></noscript>'
 return body

def metadata(lang,slug,title):
 path='/zh/' if lang=='zh' and not slug else ('/en/' if lang=='en' else '/')+(slug+'/' if slug else '')
 zh=ORIGIN+'/'+(slug+'/' if slug else 'zh/');en=ORIGIN+'/en/'+(slug+'/' if slug else '')
 desc=DESCRIPTIONS[slug][lang=='en'];url=ORIGIN+path
 share=ORIGIN+('/assets/social-zh.png' if lang=='zh' else '/assets/social.png');alt='HarnessLoop：货代与报关的本地 AI 助手' if lang=='zh' else 'HarnessLoop: Local AI for freight forwarding and customs'
 from seo import structured
 return desc, structured(lang,slug,title,desc)+f'''<link rel="canonical" href="{url}"><link rel="alternate" hreflang="zh-CN" href="{zh}"><link rel="alternate" hreflang="en" href="{en}"><link rel="alternate" hreflang="x-default" href="{en}"><meta property="og:type" content="website"><meta property="og:site_name" content="HarnessLoop"><meta property="og:title" content="{escape(title)} | HarnessLoop"><meta property="og:description" content="{escape(desc)}"><meta property="og:url" content="{url}"><meta property="og:locale" content="{'en_US' if lang=='en' else 'zh_CN'}"><meta property="og:image" content="{share}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{alt}"><meta name="twitter:image" content="{share}"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{escape(title)} | HarnessLoop"><meta name="twitter:description" content="{escape(desc)}">'''
