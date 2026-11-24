import {readFileSync,existsSync} from 'node:fs';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const routes=['','how-it-works','data-factory','research','contact','privacy','faq','solutions'];
for(const lang of ['zh','en'])for(const route of routes){const prefix=lang==='en'?'en/':(route?'':'zh/');const html=readFileSync(`dist/${prefix}${route?route+'/':''}index.html`,'utf8');assert.match(html,new RegExp(`lang="${lang==='zh'?'zh-CN':'en'}"`));assert.match(html,/name="viewport"/);assert.match(html,/name="robots" content="(?:noindex,nofollow|index,follow)"/);assert.match(html,/data-language=/);for(const m of html.matchAll(/(?:href|src)="(\/[^"#]*)"/g)){const p=m[1];assert.ok(existsSync(`dist${p}${p.endsWith('/')?'index.html':''}`),`Broken link: ${p}`);} if(lang==='en'){const body=html.replace(/<a class="language".*?<\/a>/,'');assert.ok(!/[\u4e00-\u9fff]/.test(body),`Chinese in English ${route}`);}}
for (const [homePath, solutionPath, otherPath, contactPath, heading, freight, medical] of [
  ['/zh/', '/solutions/', '/en/solutions/', '/contact/', '解决方案', '货代智能客服助手', '医学文献及情报管理助手'],
  ['/en/', '/en/solutions/', '/solutions/', '/en/contact/', 'Solutions', 'Freight Forwarding Customer Service Assistant', 'Medical Literature &amp; Intelligence Assistant'],
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
    assert.doesNotMatch(example, /\b\d{2}:\d{2}\b|\b[A-Z]{2,}-\d{2,}\b|\b20\d{2}-\d{2}-\d{2}\b|\bworkdays?\b|\bbusiness days?\b|工作日|截点/i,
      'Public examples must not include precise times, dates, record identifiers or operational cutoffs');
  }
  const expected = homePath === '/en/' ? ['No confirmed date', 'Response draft', 'does not establish a change in recommendations']
    : ['日期尚未确认', '回复草稿', '不能据此判断建议是否改变'];
  for (const item of expected) assert.ok(html.includes(item), `Missing public sample safeguard: ${item}`);
  const delivery = homePath === '/en/' ? ['How it runs', 'Install and run locally', 'where supported', 'configured local workflow', 'review records']
    : ['在本地怎么运行', '在本地安装与运行', '设备和环境支持', '配置好的本地流程', '复核记录'];
  for (const item of delivery) assert.ok(html.includes(item), `Missing delivery detail: ${item}`);


}
const app=readFileSync('dist/assets/app.js','utf8');assert.ok(!/fetch\(|XMLHttpRequest|sendBeacon/.test(app));assert.match(app,/textContent=/);
for(const lang of ['zh-CN','en']){
 const els=new Map(), buttons=[0,1,2].map(i=>({dataset:{stage:String(i)},setAttribute(k,v){this[k]=v},addEventListener(){},focus(){}}));
 for(const key of ['.menu','#navigation','#demo-output','#brief-form','#generate-brief','#brief','#brief-panel','#copy-status','#copy-brief','#email-brief','[data-language]'])els.set(key,{dataset:{language:'en'},handlers:{},addEventListener(k,f){this.handlers[k]=f},classList:{toggle(){},remove(){}},getAttribute(){return 'false'},setAttribute(k,v){this[k]=v}});
 els.get('#brief-form').querySelectorAll=()=>['task','pain','criteria'].map(name=>({name,value:({task:'<script>alert(1)</script>',pain:'formats',criteria:'sources'})[name],reportValidity(){return true}}));
 const ctx={document:{addEventListener(){},documentElement:{lang},querySelector:k=>els.get(k),querySelectorAll:()=>buttons},FormData:class {get(k){return {task:'<script>alert(1)</script>',pain:'formats',criteria:'sources'}[k]}},navigator:{clipboard:{writeText:async()=>{}}},localStorage:{setItem(){}}};
 vm.createContext(ctx);vm.runInContext(app,ctx);vm.runInContext('showStage(2)',ctx);assert.match(els.get('#demo-output').innerHTML,lang==='en'?/15 business days/:/15 个工作日/);assert.equal(buttons[2]['aria-selected'],'true');els.get('#generate-brief').handlers.click();assert.match(els.get('#brief').textContent,/<script>alert/);assert.match(els.get('#brief').textContent,lang==='en'?/Not sent/:/未发送/);const before=els.get('#brief').textContent;els.get('#brief-form').querySelectorAll=()=>[{name:'task',value:'',reportValidity(){return false}}];els.get('#generate-brief').handlers.click();assert.equal(els.get('#brief').textContent,before);
}
const language=readFileSync('dist/assets/language.js','utf8');for(const [path,saved,locale,expect] of [['/',null,'zh-CN',false],['/',null,'en-US',false],['/','zh','en-US',false],['/','en','zh-CN',false],['/en/contact/',null,'zh-CN',false]]){let redirected=false;vm.runInNewContext(language,{location:{pathname:path,search:'',hash:'',replace(){redirected=true}},navigator:{language:locale},localStorage:{getItem(){return saved}}});assert.equal(redirected,expect);}
console.log('PASS: 16 routes, links, localization, preview boundary; bilingual demo + safe local briefs; stable language URLs.');

// Revision 3 regression: contact route and footer on all locales; client-side email draft.
for(const lang of ['', 'en/']) {
 for(const route of routes) {const html=readFileSync(`dist/${lang}${route?route+'/':''}index.html`,'utf8');assert.match(html,/href="mailto:contact@harnessloop.ai"/);}
 const contact=readFileSync(`dist/${lang}contact/index.html`,'utf8');assert.match(contact,/id="email-brief"/);assert.ok(!/will be added once confirmed|正式联系入口将在确认后接入/.test(contact));
 const demo=readFileSync(`dist/${lang}data-factory/index.html`,'utf8');assert.match(demo,/role="tabpanel"/);assert.equal([...demo.matchAll(/aria-controls="demo-output"/g)].length,3);
}
assert.match(app,/encodeURIComponent/);assert.ok(!app.includes("state:'good'"));console.log('PASS: bilingual mailto, local email draft, tab relationships, no unverified success status.');

const config=JSON.parse(readFileSync('vercel.json','utf8'));assert.ok(config.redirects.some(r=>r.source==='/'&&r.destination==='/en/'));
assert.match(readFileSync('dist/zh/index.html','utf8'),/canonical" href="https:\/\/harnessloop.ai\/zh\/"/);
assert.match(readFileSync('dist/en/contact/index.html','utf8'),/click Send there/);
assert.match(readFileSync('dist/contact/index.html','utf8'),/本站不会提交表单或自动发邮件/);
