import {readFileSync,existsSync} from 'node:fs';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const routes=['','how-it-works','data-factory','research','contact','privacy'];
for(const lang of ['zh','en'])for(const route of routes){const prefix=lang==='en'?'en/':'';const html=readFileSync(`dist/${prefix}${route?route+'/':''}index.html`,'utf8');assert.match(html,new RegExp(`lang="${lang==='zh'?'zh-CN':'en'}"`));assert.match(html,/name="viewport"/);assert.match(html,/noindex,nofollow/);assert.match(html,/data-language=/);for(const m of html.matchAll(/(?:href|src)="(\/[^"#]*)"/g)){const p=m[1];assert.ok(existsSync(`dist${p}${p.endsWith('/')?'index.html':''}`),`Broken link: ${p}`);} if(lang==='en'){const body=html.replace(/<a class="language".*?<\/a>/,'');assert.ok(!/[\u4e00-\u9fff]/.test(body),`Chinese in English ${route}`);}}
const app=readFileSync('dist/assets/app.js','utf8');assert.ok(!/fetch\(|XMLHttpRequest|sendBeacon/.test(app));assert.match(app,/textContent=/);
for(const lang of ['zh-CN','en']){
 const els=new Map(), buttons=[0,1,2].map(i=>({dataset:{stage:String(i)},setAttribute(k,v){this[k]=v},addEventListener(){},focus(){}}));
 for(const key of ['.menu','#navigation','#demo-output','#brief-form','#brief','#brief-panel','#copy-status','#copy-brief','#email-brief','[data-language]'])els.set(key,{dataset:{language:'en'},handlers:{},addEventListener(k,f){this.handlers[k]=f},classList:{toggle(){},remove(){}},getAttribute(){return 'false'},setAttribute(k,v){this[k]=v}});
 const ctx={document:{documentElement:{lang},querySelector:k=>els.get(k),querySelectorAll:()=>buttons},FormData:class {get(k){return {task:'<script>alert(1)</script>',pain:'formats',criteria:'sources'}[k]}},navigator:{clipboard:{writeText:async()=>{}}},localStorage:{setItem(){}}};
 vm.createContext(ctx);vm.runInContext(app,ctx);vm.runInContext('showStage(2)',ctx);assert.match(els.get('#demo-output').innerHTML,lang==='en'?/15 business days/:/15 个工作日/);assert.equal(buttons[2]['aria-selected'],'true');els.get('#brief-form').handlers.submit({preventDefault(){},currentTarget:{}});assert.match(els.get('#brief').textContent,/<script>alert/);assert.match(els.get('#brief').textContent,lang==='en'?/Not sent/:/未发送/);
}
const language=readFileSync('dist/assets/language.js','utf8');for(const [path,saved,locale,expect] of [['/',null,'zh-CN',false],['/',null,'en-US',true],['/','zh','en-US',false],['/','en','zh-CN',true],['/en/contact/',null,'zh-CN',false]]){let redirected=false;vm.runInNewContext(language,{location:{pathname:path,search:'',hash:'',replace(){redirected=true}},navigator:{language:locale},localStorage:{getItem(){return saved}}});assert.equal(redirected,expect);}
console.log('PASS: 12 routes, links, localization, preview boundary; bilingual demo + safe local briefs; language default and saved choice.');

// Revision 3 regression: contact route and footer on all locales; client-side email draft.
for(const lang of ['', 'en/']) {
 for(const route of routes) {const html=readFileSync(`dist/${lang}${route?route+'/':''}index.html`,'utf8');assert.match(html,/href="mailto:contact@harnessloop.ai"/);}
 const contact=readFileSync(`dist/${lang}contact/index.html`,'utf8');assert.match(contact,/id="email-brief"/);assert.ok(!/will be added once confirmed|正式联系入口将在确认后接入/.test(contact));
 const demo=readFileSync(`dist/${lang}data-factory/index.html`,'utf8');assert.match(demo,/role="tabpanel"/);assert.equal([...demo.matchAll(/aria-controls="demo-output"/g)].length,3);
}
assert.match(app,/encodeURIComponent/);assert.ok(!app.includes("state:'good'"));console.log('PASS: bilingual mailto, local email draft, tab relationships, no unverified success status.');
