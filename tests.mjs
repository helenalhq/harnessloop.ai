import {readFileSync,existsSync} from 'node:fs';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const routes=['','how-it-works','data-factory','research','contact','privacy','faq','solutions','demo'];
for(const lang of ['zh','en'])for(const route of routes){const prefix=lang==='en'?'en/':(route?'':'zh/');const html=readFileSync(`dist/${prefix}${route?route+'/':''}index.html`,'utf8');assert.match(html,new RegExp(`lang="${lang==='zh'?'zh-CN':'en'}"`));assert.match(html,/name="viewport"/);assert.match(html,/name="robots" content="(?:noindex,nofollow|index,follow)"/);assert.match(html,/data-language=/);for(const m of html.matchAll(/(?:href|src)="(\/[^"#]*)"/g)){const p=m[1];assert.ok(existsSync(`dist${p}${p.endsWith('/')?'index.html':''}`),`Broken link: ${p}`);} if(lang==='en'){const body=html.replace(/<a class="language".*?<\/a>/,'');assert.ok(!/[\u4e00-\u9fff]/.test(body),`Chinese in English ${route}`);}}
for (const [homePath, solutionPath, otherPath, contactPath, heading, freight, medical] of [
  ['/zh/', '/solutions/', '/en/solutions/', '/contact/', '我们构建的示例', '货代智能客服助手', '医学文献及情报管理助手'],
  ['/en/', '/en/solutions/', '/solutions/', '/en/contact/', 'Examples of what we build', 'Freight Forwarding Customer Service Assistant', 'Medical Literature &amp; Intelligence Assistant'],
]) {
  const local = path => readFileSync(`dist${path}index.html`, 'utf8');
  const home = local(homePath);
  assert.ok(home.includes(`href="${solutionPath}"`), `Missing Solutions navigation from ${homePath}`);
  const html = local(solutionPath);
  assert.ok(html.includes(homePath === '/en/' ? 'Tell us how you work. We build a Harness that runs on your own computer or workstation.' : '你描述业务场景，我们为你构建在本地运行的 Harness。'));
  assert.ok(html.includes(`<h1 id="hl-solutions-title">${heading}</h1>`));
  assert.ok(html.includes(`<h3>${freight}</h3>`));
  assert.ok(html.includes(`<h3>${medical}</h3>`));
  assert.ok(html.includes(`class="language" href="${otherPath}"`));
  assert.equal([...html.matchAll(new RegExp(`class="hl-action hl-action--primary" href="${contactPath}"`, "g"))].length, 2, "Hero and final CTAs must use the contact page in the same language");
  assert.equal((html.match(/<article class="hl-showcase/g) || []).length, 2);
  assert.ok(html.includes('id="hl-workflow-diagram"'));
  assert.ok(html.includes('href="#hl-showcases"') && html.includes('id="hl-showcases"'));
  assert.ok(html.includes('id="hl-local-run"'));
  let imageCount = 0;
  for (const image of html.matchAll(/<img src="(\/assets\/hl-(?:freight|medical)-v3\.webp)" width="(\d+)" height="(\d+)" loading="lazy" alt="([^"]+)"/g)) {
    const file = readFileSync('dist' + image[1]);
    assert.equal(file.subarray(8, 12).toString(), 'WEBP');
    assert.ok(file.length < 250_000, 'Illustrations must be optimized WebP images');
    assert.ok(Number(image[2]) >= 640 && Number(image[3]) >= 400, 'Intrinsic image dimensions prevent layout shifts');
    imageCount++;
  }
  assert.equal(imageCount, 2);
  assert.doesNotMatch(html, /<form|https?:\/\/[^"]+\.invalid/);
  const examples = [...html.matchAll(/<article class="hl-showcase[^"]*">(.*?)<\/article>/gs)].map(match => match[1]);
  for (const example of examples) {
    assert.doesNotMatch(example.replace(/https?:\/\/[^"\s]+/g, ''), /\b\d{2}:\d{2}\b|\b[A-Z]{2,}-\d{2,}\b|\b20\d{2}-\d{2}-\d{2}\b|\bworkdays?\b|\bbusiness days?\b|工作日|截点/i,
      'Public examples must not include precise times, dates, record identifiers or operational cutoffs');
  }
  const expected = homePath === '/en/' ? ['No confirmed date', 'Response draft', 'does not establish a change in recommendations']
    : ['日期尚未确认', '回复草稿', '不能据此判断建议是否改变'];
  for (const item of expected) assert.ok(html.includes(item), `Missing public sample safeguard: ${item}`);
  const delivery = homePath === '/en/' ? ['How it runs', 'Install and run locally', 'where supported', 'configured local workflow', 'review records']
    : ['在本地怎么运行', '在本地安装与运行', '设备和环境支持', '配置好的本地流程', '复核记录'];
  for (const item of delivery) assert.ok(html.includes(item), `Missing delivery detail: ${item}`);


}
for (const [base, homePath, homePromise, contactPromise] of [
  ['/', '/zh/', '一个属于你自己的 AI 助手，按你的业务定制。', '从一件具体的业务任务开始。'],
  ['/en/', '/en/', 'An AI assistant of your own, built around your work.', 'Start with one real task.'],
]) {
  const home=readFileSync('dist'+homePath+'index.html','utf8');
  assert.ok(home.includes(homePromise), 'Home should lead with a customer outcome');
  assert.doesNotMatch(home, /Bring us a real task|从一个真实业务问题开始/, 'Remove the duplicate legacy Home CTA only');
  assert.ok(home.indexOf('id="hl-home-solutions"') > 0);
  assert.ok(home.indexOf('id="hl-home-solutions"') < home.indexOf('id="hl-home-method"'), 'Industry examples precede technical proof');
  // Each example answers the same four questions in the same order, and shows a labelled sample.
  const sections=home.split('class="hl-home-card"').slice(1);
  assert.equal(sections.length,2,'Two examples on the home page');
  const labels=base==='/en/'?['THE PAIN','THE ASSISTANT','WHAT YOU RECEIVE','HOW IT IMPROVES']:['痛点','助手做什么','你拿到什么','怎么变好'];
  for (const [name, id] of [['freight','freight'],['medical','medical']]) {
    const card=sections.shift().split('</article>')[0];
    assert.deepEqual([...card.matchAll(/<dt>([^<]+)<\/dt>/g)].map((m) => m[1]).slice(-4),labels,name+' example: pain, harness, delivery, improvement');
    assert.ok(/合成示例|synthetic sample/.test(card),'The home sample must say it is synthetic');
    assert.ok(/独立(?:验证|样本)|independent (?:validation|examples)/.test(card),'Say how the next version is earned: '+name);
    assert.ok(/装在|installed on/.test(card),'Say where the deliverable runs: '+name);
    assert.ok(card.includes('href="'+base+'solutions/#hl-sample-'+id+'"'));
  }
  assert.ok(home.includes('data-evolution'), 'Optional legacy demonstration remains available');
  // The walkthrough video streams from GitHub only on play; its poster is ours.
  const video=home.match(/<video ([^>]*)><source src="([^"]+)" type="video\/mp4">/);
  assert.ok(video,'Home page needs the walkthrough video');
  assert.equal(video[2],'https://github.com/helenalhq/media/releases/download/v1.0/demo-55s-'+(base==='/en/'?'en':'zh')+'.mp4');
  for(const attr of ['controls','playsinline','preload="none"']) assert.ok(video[1].includes(attr),'Video must stay user-initiated: '+attr);
  assert.doesNotMatch(video[1],/autoplay|muted/,'The video has a voice-over and starts only on request');
  const poster=video[1].match(/poster="(\/[^"]+)"/);assert.ok(existsSync('dist'+poster[1]),'Video poster must ship with the site');
  assert.ok(home.includes('href="https://github.com/helenalhq/media/releases/tag/v1.0" target="_blank" rel="noopener noreferrer"'),'Offer the GitHub copy as fallback');
  assert.ok(/合成数据|synthetic data/.test(home),'The video uses synthetic data and must say so');
  // The player sits in the hero with our play button and a fallback when GitHub does not answer.
  const hero=home.split('class="hl-biz-hero"')[1].split('</section>')[0];
  assert.match(hero,/class="hl-hero-media">\s*<div class="hl-video-frame"><video [^>]*data-play="/,'The video opens the page, inside the hero');
  assert.match(hero,/<p class="hl-video-failed hidden">[^<]+<a href="https:\/\/github.com\/helenalhq\/media\/releases\/tag\/v1.0"/);
  assert.doesNotMatch(home,/class="hl-home-video"/);
  assert.match(home,/<section class="wrap hl-home-flow" aria-labelledby="hl-home-flow-title"><p class="hl-biz-kicker" id="hl-home-flow-title">[^<]+<\/p><ol>(<li><span aria-hidden="true">\d\d<\/span><div><strong>[^<]+<\/strong><p>[^<]+<\/p><\/div><\/li>){3}<\/ol><\/section>/);
  assert.ok(home.includes('class="hl-nav-contact" href="'+base+'contact/"'));
  const contact=readFileSync('dist'+base+'contact/index.html','utf8');
  assert.ok(contact.includes(contactPromise));
  assert.equal((contact.match(/<li class="hl-engagement-step">/g)||[]).length,3);
  assert.doesNotMatch(contact, /<form|type="submit"/);
  for (const id of ['copy-email','brief-form','generate-brief','brief-panel','copy-brief','email-brief','copy-status']) {
    assert.ok(contact.includes('id="'+id+'"'),'Required local draft control not preserved: '+id);
  }
}
const app=readFileSync('dist/assets/app.js','utf8');assert.ok(!/fetch\(|XMLHttpRequest|sendBeacon/.test(app));assert.match(app,/textContent=/);
// Progressively added behaviour: both scripts stay silent until needed and store nothing.
for(const file of ['video.js','motion.js']){
  const code=readFileSync('dist/assets/'+file,'utf8');
  assert.ok(!/fetch\(|XMLHttpRequest|sendBeacon|localStorage|sessionIndex|indexedDB|document\.cookie/.test(code),file+' must not track or fetch');
}
const motion=readFileSync('dist/assets/motion.js','utf8');
assert.match(motion,/prefers-reduced-motion/);assert.match(motion,/IntersectionObserver/);assert.match(motion,/is-in/);
const player=readFileSync('dist/assets/video.js','utf8');
assert.match(player,/video\.controls\s*=\s*true/);assert.match(player,/video\.play\(\)/);assert.match(player,/'error'/);
const css=readFileSync('dist/assets/business.css','utf8');
assert.match(css,/\.hl-reveal-on :is\([^)]*\):not\(\.is-in\) \{opacity:0/,'Only motion.js decides what is hidden, and only before it is in view');
assert.match(css,/@media print \{\.hl-reveal-on/);
for(const lang of ['zh-CN','en']){
 const els=new Map(), buttons=[0,1,2].map(i=>({dataset:{stage:String(i)},setAttribute(k,v){this[k]=v},addEventListener(){},focus(){}}));
 for(const key of ['.menu','#navigation','#demo-output','#brief-form','#generate-brief','#brief','#brief-panel','#copy-status','#copy-brief','#email-brief','[data-language]'])els.set(key,{dataset:{language:'en'},handlers:{},addEventListener(k,f){this.handlers[k]=f},classList:{toggle(){},remove(){}},getAttribute(){return 'false'},setAttribute(k,v){this[k]=v}});
 els.get('#brief-form').querySelectorAll=()=>['task','pain','criteria','name'].map(name=>({name,value:({task:'<script>alert(1)</script>',pain:'formats',criteria:'sources',name:'ACME Freight'})[name],reportValidity(){return true}}));
 const ctx={document:{addEventListener(){},documentElement:{lang},querySelector:k=>els.get(k),querySelectorAll:()=>buttons},FormData:class {get(k){return {task:'<script>alert(1)</script>',pain:'formats',criteria:'sources'}[k]}},navigator:{clipboard:{writeText:async()=>{}}},localStorage:{setItem(){}}};
 vm.createContext(ctx);vm.runInContext(app,ctx);vm.runInContext('showStage(2)',ctx);assert.match(els.get('#demo-output').innerHTML,lang==='en'?/15 business days/:/15 个工作日/);assert.equal(buttons[2]['aria-selected'],'true');els.get('#generate-brief').handlers.click();assert.match(els.get('#brief').textContent,/<script>alert/);assert.match(els.get('#brief').textContent,lang==='en'?/Not sent/:/未发送/);assert.match(els.get('#brief').textContent,lang==='en'?/From: ACME Freight/:/联系人：ACME Freight/,'The optional name belongs in the brief');assert.doesNotMatch(decodeURIComponent(els.get('#email-brief').href),/Not sent|未发送/,'The email draft must not carry the on-screen status line');assert.match(els.get('#email-brief').href,/^mailto:contact@harnessloop\.ai\?subject=/);const before=els.get('#brief').textContent;els.get('#brief-form').querySelectorAll=()=>[{name:'task',value:'',reportValidity(){return false}}];els.get('#generate-brief').handlers.click();assert.equal(els.get('#brief').textContent,before);
}
const language=readFileSync('dist/assets/language.js','utf8');for(const [path,saved,locale,expect] of [['/',null,'zh-CN',false],['/',null,'en-US',false],['/','zh','en-US',false],['/','en','zh-CN',false],['/en/contact/',null,'zh-CN',false]]){let redirected=false;vm.runInNewContext(language,{location:{pathname:path,search:'',hash:'',replace(){redirected=true}},navigator:{language:locale},localStorage:{getItem(){return saved}}});assert.equal(redirected,expect);}
console.log('PASS: 18 routes, links, localization, preview boundary; bilingual demo + safe local briefs; stable language URLs.');

// Revision 3 regression: contact route and footer on all locales; client-side email draft.
for(const lang of ['', 'en/']) {
 for(const route of routes) {const html=readFileSync(`dist/${lang}${route?route+'/':''}index.html`,'utf8');assert.match(html,/href="mailto:contact@harnessloop.ai"/);}
 const contact=readFileSync(`dist/${lang}contact/index.html`,'utf8');assert.match(contact,/id="email-brief"/);assert.ok(contact.indexOf('id="email-brief"')<contact.indexOf('id="copy-brief"'),'Opening the email draft comes before copying');assert.ok(!/will be added once confirmed|正式联系入口将在确认后接入/.test(contact));
 const demo=readFileSync(`dist/${lang}data-factory/index.html`,'utf8');assert.match(demo,/role="tabpanel"/);assert.equal([...demo.matchAll(/aria-controls="demo-output"/g)].length,3);
}
assert.match(app,/encodeURIComponent/);assert.ok(!app.includes("state:'good'"));console.log('PASS: bilingual mailto, local email draft, tab relationships, no unverified success status.');

const config=JSON.parse(readFileSync('vercel.json','utf8'));assert.ok(config.redirects.some(r=>r.source==='/'&&r.destination==='/en/'));
assert.match(config.headers[0].headers.find(h=>h.key==='Content-Security-Policy').value,/media-src https:\/\/github\.com /,'Only GitHub media is allowed through the CSP');
assert.match(readFileSync('dist/zh/index.html','utf8'),/canonical" href="https:\/\/harnessloop.ai\/zh\/"/);
assert.match(readFileSync('dist/en/contact/index.html','utf8'),/Review it there, then click Send\./);
assert.match(readFileSync('dist/contact/index.html','utf8'),/本站不会提交表单或自动发邮件/);

// Three-act interactive demo: synthetic banner, three acts, approval buttons, audit trail, client-side-only script.
for (const [path, banner, heading, approve, headers, contactPath] of [
  ['/demo/', '合成数据 · 交互演示 · 非真实货物', '三幕，看它怎么工作。', '批准发送', ['时间','来源','判断','动作'], '/contact/'],
  ['/en/demo/', 'Synthetic data · Interactive demo · No real shipments', 'Three acts. Watch how it works.', 'Approve', ['Time','Source','Judgment','Action'], '/en/contact/'],
]) {
  const html = readFileSync(`dist${path}index.html`, 'utf8');
  assert.ok(html.includes('class="hl-demo-banner"'), 'Demo page needs the fixed synthetic-data banner');
  assert.ok(html.includes(banner));
  assert.ok(html.includes(`<h1 id="hl-demo-title">${heading}</h1>`));
  assert.ok(html.includes('<button type="button" class="hl-demo-btn hl-demo-btn--approve" data-demo-action="approve">' + approve + '</button>'));
  assert.ok(html.includes('<button type="button" class="hl-demo-btn hl-demo-btn--reset" data-demo-action="reset">'));
  assert.ok(html.includes('id="hl-demo-notice" role="status" aria-live="polite"'));
  assert.ok(html.includes('id="hl-demo-log"'));
  assert.ok(html.includes('<table class="hl-demo-log"'));
  for (const h of headers) assert.ok(html.includes(`<th scope="col">${h}</th>`), `Missing audit column: ${h}`);
  for (const act of [1, 2, 3]) assert.ok(html.includes(`id="hl-demo-act-${act}"`));
  assert.ok(html.includes(`href="${contactPath}"`), 'Every act must offer the contact exit in the same language');
  assert.ok(html.includes('/assets/demo.css') && html.includes('/assets/demo.js'), 'Demo assets must be wired in');
  assert.doesNotMatch(html, /<form|type="submit"/);
  assert.ok(html.includes('19 CFR § 113.62') && html.includes('shipper@example.com'), 'Synthetic brief and draft must be present');
  // The brief's headline counts must match the rows a visitor can count: 3 anomalies, 1 draft awaiting approval.
  assert.match(html, /<div class="hl-demo-stats"><div><b>6/, 'The brief summarizes six items');
  assert.equal((html.match(/<span class="dot dot--(alert|warn)"/g) || []).length, 3, 'Exactly three rows may carry an anomaly dot: the stats say 3');
  assert.equal((html.match(/<span class="dot dot--ok"/g) || []).length, 3, 'The remaining three rows are normal');
  assert.equal((html.match(/<strong>BK-\d+<\/strong><p>[^<]*(草稿|draft)/g) || []).length, 1, 'Only one row offers a draft: the stats say 1');
}
const demoJs=readFileSync('dist/assets/demo.js','utf8');
assert.ok(!/fetch\(|XMLHttpRequest|sendBeacon|localStorage|sessionStorage/.test(demoJs),'Demo must stay client-side with no storage');
for(const lang of ['zh-CN','en']){
  const notice={set textContent(v){this.value=v}},log={rows:{length:2},_n:2,getAttribute:k=>'2',appendChild(){this._n++;this.rows.length++},deleteRow(){this._n--;this.rows.length--}};
  const buttons=[['approve'],['edit'],['reject'],['reset']].map(([action])=>({handlers:{},addEventListener(k,f){this.handlers[k]=f},getAttribute:()=>action}));
  const ctx={document:{readyState:'complete',documentElement:{lang},getElementById:id=>id==='hl-demo-log'?log:notice,querySelectorAll:()=>buttons,createElement:()=>({textContent:'',appendChild(){}})},Date:class{toLocaleTimeString(){return '08:04:11'}}};
  vm.createContext(ctx);vm.runInContext(demoJs,ctx);
  buttons[0].handlers.click();
  assert.equal(log.rows.length,3,'Approve must append one audit row');
  assert.match(notice.value,lang==='en'?/Approval simulated/:/已模拟批准/);
  buttons[3].handlers.click();
  assert.equal(log.rows.length,2,'Reset must restore the seeded rows');
  assert.match(notice.value,lang==='en'?/Reset/:/已重置/);
}
console.log('PASS: three-act demo page, synthetic labelling, client-side audit trail, language parity.');
