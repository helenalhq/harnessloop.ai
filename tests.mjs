import {readFileSync,existsSync} from 'node:fs';
import assert from 'node:assert/strict';
const routes=['','how-it-works','data-factory','research','contact','privacy'];
for(const route of routes){const html=readFileSync(`dist/${route?route+'/':''}index.html`,'utf8');assert.match(html,/lang="zh-CN"/);assert.match(html,/name="viewport"/);assert.match(html,/noindex,nofollow/);for(const m of html.matchAll(/(?:href|src)="(\/[^"#]*)"/g)){const p=m[1];assert.ok(existsSync(`dist${p}${p.endsWith('/')?'index.html':''}`),`Broken link: ${p}`);} }
const app=readFileSync('dist/assets/app.js','utf8');assert.ok(!/fetch\(|localStorage|sessionStorage/.test(app));assert.match(app,/textContent=/);console.log('PASS: 6 routes, local assets/links, preview indexing boundary, no network or storage in interaction code');
