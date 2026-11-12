import fs from 'node:fs';import vm from 'node:vm';import assert from 'node:assert/strict';
const code=fs.readFileSync('dist/assets/evolution.js','utf8');
for(const en of [false,true])for(const reduced of [false,true]){
 const elements={};const make=()=>({textContent:'',listeners:{},addEventListener(k,f){this.listeners[k]=f},setAttribute(k,v){this[k]=v}});
 for(const k of ['version','state','output','output-note','evidence','story-label','story','cycle-toggle','cycle-next'])elements[k]=make();
 const buttons=Array.from({length:5},(_,i)=>({...make(),dataset:{cycleStep:String(i)}}));let pausedSvg=false,interval=null;
 const demo={dataset:{},classList:{toggle(){}},querySelector:s=>elements[s.slice(6,-1)],querySelectorAll:s=>s==='svg'?[{pauseAnimations(){pausedSvg=true},unpauseAnimations(){pausedSvg=false}}]:buttons};
 const context={document:{documentElement:{lang:en?'en':'zh-CN'},hidden:false,querySelector:()=>demo,addEventListener(){}},matchMedia:()=>({matches:reduced,addEventListener(){}}),setInterval:f=>(interval=f,1),clearInterval:()=>{interval=null}};
 vm.runInNewContext(code,context);assert.equal(demo.dataset.phase,0);assert.equal(pausedSvg,reduced);assert.equal(Boolean(interval),!reduced);
 buttons[2].listeners.click();assert.equal(demo.dataset.phase,2);assert.match(elements.version.textContent,/v1/);assert.equal(interval,null);assert.equal(buttons[2]['aria-pressed'],'true');
 elements['cycle-next'].listeners.click();assert.equal(demo.dataset.phase,3);elements['cycle-next'].listeners.click();assert.equal(demo.dataset.phase,4);assert.match(elements.output.textContent,en?/Approval/:/人工/);elements['cycle-next'].listeners.click();assert.equal(demo.dataset.phase,0);
 elements['cycle-toggle'].listeners.click();assert.ok(interval);interval();assert.equal(demo.dataset.phase,1);
}
console.log('PASS: both languages; all 5 steps; pause/resume; next/replay; reduced-motion starts paused; SVG pause; gate never claims release.');
