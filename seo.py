"""Visible, bilingual answers and matching machine-readable entities."""
import json
from html import escape
ORIGIN='https://harnessloop.ai'
FAQ={
'zh':[
('这个助手装在哪里运行？','安装在你自己选定的电脑或工作站上，数据不出你的设备与内网。需要我方远程支持时，先经你临时授权，操作记录保留。'),
('AI 会不会自己发邮件、自己改单？','不会。对外动作默认只生成草稿，经你审批后才执行。不确定的信息会被标出，不会被猜成答案。'),
('用哪个模型？账号由谁提供？','我们与主流桌面 Agent 运行时配合使用，模型账号由你自备，用量与费用你自己可见、可控。'),
('ISF 与报关由你们代申报吗？','不代申报。ISF 与报关须经持牌报关行和 ABI/ACE 通道（美国海关与边境保护局要求）。我们做草拟、核对与期限看护。'),
('需要什么设备？','一台普通办公电脑或工作站即可，不需要服务器机房。具体配置在评估任务后确认。'),
('怎么收费？','一次性部署 + 年度维保，无按坐席订阅，试点开放中。具体报价在了解任务和验收标准后给出。'),
('出错了怎么办？','每台部署保留运行日志与复核记录，问题优先修复；支持方式与响应约定在合作时写入范围。'),
('和 SaaS 工具有什么不同？','数据不出门、无订阅费用、流程按你的 SOP 定制；接受远程支持时也只需临时授权。'),
('多长时间能上线？','约定样本验证通过后，部署通常两周内完成（不含影子运行期）。具体时间以任务评估为准。'),
('你们是谁？','HarnessLoop 以单人公司（OPC）的方式运作，你直接与运营它的人沟通。我们建议从一个具体任务开始合作：contact@harnessloop.ai。')],
'en':[
('Where does the assistant run?','On a computer or workstation you choose. Your data stays on your device and network. Remote support, if needed, happens only with your temporary authorization and is logged.'),
('Will the AI send emails or change documents on its own?','No. External actions start as drafts and only go out after your approval. Missing or uncertain information is flagged, never guessed.'),
('Which model do you use, and whose account?','We work with mainstream desktop agent runtimes. You bring your own model account, so usage and cost stay visible and under your control.'),
('Do you file ISF or customs entries for us?','No. ISF and entry filing must go through licensed customs brokers and ABI/ACE (per U.S. CBP). We draft, check and watch deadlines.'),
('What hardware do we need?','An ordinary office computer or workstation. No server room required. Exact requirements follow the task assessment.'),
('How does pricing work?','One-time setup plus annual maintenance. No per-seat subscription. Pilot engagements are available; we quote after understanding the task and its acceptance criteria.'),
('What happens when something goes wrong?','Every deployment keeps run logs and review records, and issues are fixed as a priority. Support terms are agreed in scope.'),
('How is this different from SaaS tools?','Your data stays local, there is no subscription, and the workflow is shaped around your SOP.'),
('How long does it take to go live?','After agreed sample verification, deployment typically takes about two weeks, excluding a shadow-running period. Final timing depends on the task assessment.'),
('Who are you?','HarnessLoop is run as a one-person company (OPC), so you work directly with the person who runs it. We suggest starting with one concrete task: contact@harnessloop.ai.')]
}
def extend(pages,lang):
 en=lang=='en'
 title='Questions & answers' if en else '常见问题'
 body='<div class="wrap subhero"><span class="eyebrow">'+('GUIDE' if en else '概念与合作指南')+'</span><h1>'+title+'</h1><p class="lead">'+('Local operation, data boundaries, filing compliance, pricing and delivery: how an engagement works.' if en else '本地运行、数据边界、申报合规、收费与交付：关于合作方式的常见问题。')+'</p></div><section class="wrap">'
 for q,a in FAQ[lang]:body+='<article class="box" style="margin-bottom:24px"><h2>'+escape(q)+'</h2><p>'+escape(a)+'</p></article>'
 base='/en/' if en else '/'
 body+='<p><a href="'+base+'how-it-works/">'+('Explore our approach' if en else '了解工作原理')+'</a> · <a href="'+base+'data-factory/">'+('See the synthetic data-factory demonstration' if en else '查看数据工厂合成演示')+'</a></p></section>'
 pages['faq']=(title,body)
 title,body=pages[''];pages['']=(('Local AI for Freight Forwarding & Customs' if en else '货代与报关的本地 AI 助手'),body)
 title,body=pages['how-it-works'];pages['how-it-works']=(('How an AI Agent Harness Works' if en else 'AI Agent Harness 工作原理与双闭环'),body)

def structured(lang,slug,title,desc):
 base='/en/' if lang=='en' else '/';url=ORIGIN+('/zh/' if lang=='zh' and not slug else base+(slug+'/' if slug else ''))
 org={'@type':'Organization','@id':ORIGIN+'/#organization','name':'HarnessLoop','url':ORIGIN,'email':'contact@harnessloop.ai'}
 web={'@type':'WebSite','@id':ORIGIN+'/#website','url':ORIGIN,'name':'HarnessLoop','publisher':{'@id':org['@id']},'inLanguage':['zh-CN','en']}
 page={'@type':'FAQPage' if slug=='faq' else 'WebPage','@id':url+'#webpage','url':url,'name':title+' | HarnessLoop','description':desc,'inLanguage':'en' if lang=='en' else 'zh-CN','isPartOf':{'@id':web['@id']},'about':{'@id':org['@id']}}
 if slug=='faq':page['mainEntity']=[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ[lang]]
 return '<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':[org,web,page]},ensure_ascii=False).replace('<','\\u003c')+'</script>'
