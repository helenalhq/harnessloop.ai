"""Visible, bilingual answers and matching machine-readable entities."""
import json
from html import escape
ORIGIN='https://harnessloop.ai'
FAQ={
'zh':[
('什么是 AI Agent Harness？','AI Agent Harness 是围绕模型的执行系统，组织任务上下文、授权工具、执行步骤、质量检查和人工审批。模型生成或推理，Harness 决定如何把这些能力用于具体业务任务。'),
('自进化 Harness 会自行修改生产系统吗？','这里的自进化指受控迭代：记录失败与人工修正，提出候选修改，用独立样本与基线比较，经约定的发布闸门后采用。它不等于无限自主改写生产系统，也不必涉及模型权重训练。'),
('Harness 与提示词、RAG 有什么区别？','提示词规定模型的任务与输出要求；RAG 为模型检索相关资料。Harness 可以把二者与工具、权限、流程状态、验证和人工复核连接起来。是否需要这些组件，取决于业务任务。'),
('数据与知识工厂如何使用 Harness？','将文档抽取、来源定位、字段规则检查和人工复核连接为工作流。错误与修正可用于设计下一版候选，并通过独立评测检查是否改善。本站的采购资料示例是合成演示，不是客户成果。'),
('如何判断一次迭代真的变好了？','先约定任务和验收标准，再用独立样本比较候选与基线，同时检查回归、成本和需要人工处理的情况。不能仅凭一个演示或优化时使用的样本声称质量提升。'),
('如何开始合作，需要提交业务数据吗？','先通过 contact@harnessloop.ai 说明任务、当前问题和验收标准。本站简报工具仅在浏览器本地生成文字。初次联系请勿发送病历、敏感个人信息、凭据或客户机密；数据接入和交付范围需另行约定。')],
'en':[
('What is an AI agent harness?','An AI agent harness is the execution system around a model. It organizes task context, authorized tools, execution steps, quality checks and human approval. The model generates or reasons; the harness determines how those capabilities are used for a business task.'),
('Does a self-improving harness change production on its own?','Here, self-improvement means controlled iteration: record failures and human corrections, propose a candidate, compare it with a baseline on independent samples, and apply agreed release gates. It does not mean unrestricted production changes or necessarily training model weights.'),
('How does a harness differ from prompts and RAG?','Prompts specify a model’s task and output requirements. Retrieval-augmented generation (RAG) retrieves relevant material. A harness can connect both with tools, permissions, workflow state, validation and human review. The task determines which components are needed.'),
('How does a data and knowledge factory use a harness?','It connects document extraction, source evidence, field validation and human review in a workflow. Errors and corrections inform the next candidate, which is checked with independent evaluation. The procurement example on this website is synthetic, not a customer outcome.'),
('How do you know an iteration is better?','Agree the task and acceptance criteria first. Compare a candidate with a baseline on independent samples, while checking regressions, cost and cases requiring human review. A demonstration or the samples used for optimization alone cannot establish a quality improvement.'),
('How can we start, and should we send business data?','Email contact@harnessloop.ai with your task, current difficulties and acceptance criteria. The website’s brief tool generates text locally in your browser. Do not send medical records, sensitive personal information, credentials or client secrets in an initial enquiry. Data access and delivery scope are agreed separately.')]
}
def extend(pages,lang):
 en=lang=='en'
 title='AI Agent Harness: Questions & Answers' if en else 'AI Agent Harness 与自进化工作流常见问题'
 body='<div class="wrap subhero"><span class="eyebrow">'+('GUIDE' if en else '概念与合作指南')+'</span><h1>'+title+'</h1><p class="lead">'+('A practical guide to business-specific execution systems, evaluation and controlled improvement.' if en else '理解业务专属执行系统、独立评测与受控迭代的边界。')+'</p></div><section class="wrap">'
 for q,a in FAQ[lang]:body+='<article class="box" style="margin-bottom:24px"><h2>'+escape(q)+'</h2><p>'+escape(a)+'</p></article>'
 base='/en/' if en else '/'
 body+='<p><a href="'+base+'how-it-works/">'+('Explore our approach' if en else '了解工作原理')+'</a> · <a href="'+base+'data-factory/">'+('See the synthetic data-factory demonstration' if en else '查看数据工厂合成演示')+'</a></p></section>'
 pages['faq']=(title,body)
 title,body=pages[''];pages['']=(('Custom AI Agent Harnesses & Controlled Improvement' if en else '业务定制 AI Agent Harness 与受控自进化'),body)
 title,body=pages['how-it-works'];pages['how-it-works']=(('How an AI Agent Harness Works' if en else 'AI Agent Harness 工作原理与双闭环'),body)

def structured(lang,slug,title,desc):
 base='/en/' if lang=='en' else '/';url=ORIGIN+('/zh/' if lang=='zh' and not slug else base+(slug+'/' if slug else ''))
 org={'@type':'Organization','@id':ORIGIN+'/#organization','name':'HarnessLoop','url':ORIGIN,'email':'contact@harnessloop.ai'}
 web={'@type':'WebSite','@id':ORIGIN+'/#website','url':ORIGIN,'name':'HarnessLoop','publisher':{'@id':org['@id']},'inLanguage':['zh-CN','en']}
 page={'@type':'FAQPage' if slug=='faq' else 'WebPage','@id':url+'#webpage','url':url,'name':title+' | HarnessLoop','description':desc,'inLanguage':'en' if lang=='en' else 'zh-CN','isPartOf':{'@id':web['@id']},'about':{'@id':org['@id']}}
 if slug=='faq':page['mainEntity']=[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in FAQ[lang]]
 return '<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':[org,web,page]},ensure_ascii=False).replace('<','\\u003c')+'</script>'
