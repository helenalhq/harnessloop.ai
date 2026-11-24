'use strict';
(()=>{
 const demo=document.querySelector('[data-evolution]');if(!demo)return;
 const en=document.documentElement.lang==='en';
 const stages=en?[
 ['Current harness · v0','Extract','15 days','Qualifier missing','Output awaiting evaluation','EXECUTION / v0','The first extraction loses a critical qualifier. The output is not yet ready for delivery.'],
 ['Current harness · v0','Evaluate','15 days','Source mismatch','Q-02 / Preserve the original unit','FEEDBACK / EVIDENCE','The quality check compares the result with “15 business days”. The failure is saved with its source, not silently corrected.'],
 ['Candidate harness · v1','Propose','Preserve units','Proposed rule change','Candidate isolated from the current version','CANDIDATE / NOT RELEASED','A candidate rule preserves explicit time units. Improving one answer does not yet prove the system is better.'],
 ['Candidate harness · v1','Validate','Independent tests','Regression review','Check new cases, exceptions and regressions','VALIDATION / RELEASE GATE','Test the candidate on independent examples. A failing candidate stays out of production. This demo does not report test results.'],
 ['Release gate','Promote','Approval required','Keep a rollback path','Only approved versions re-enter execution','NEXT VERSION / CONTROLLED','If validation and human approval pass, promote the version and retain the previous one. The next run starts a new feedback loop.']
 ]:[
 ['当前 Harness · v0','执行','15 天','单位限定丢失','执行输出，等待质量检查','任务执行 / v0','首次提取丢失了“工作日”限定。执行完成，不代表结果已经可以交付。'],
 ['当前 Harness · v0','评测','15 天','与原文不一致','Q-02 / 保留原始时间单位','质量反馈 / 保留证据','质量检查对照原文“15 个工作日”，记录错误及其来源，而不是只在这一次悄悄修正答案。'],
 ['候选 Harness · v1','提议','保留原始单位','提出规则变更','候选版本与当前执行版本隔离','候选变更 / 尚未发布','生成保留时间单位的候选规则。修好一个答案，还不足以证明整个系统变好了。'],
 ['候选 Harness · v1','验证','独立样本测试','检查是否退化','验证新样本、边界条件与原有任务','独立验证 / 发布闸门','用独立样本检查候选版本；没有通过的变更不进入生产。本演示不宣称真实测试结果。'],
 ['版本发布闸门','晋级','等待人工批准','保留回退路径','只有获准的版本，才能返回执行环','下一版本 / 受控进化','如果验证与人工批准通过，才晋级版本并保留旧版。下一次运行，开始新一轮有依据的改进。']];
 let index=0,paused=matchMedia('(prefers-reduced-motion: reduce)').matches,timer;
 const toggle=demo.querySelector('[data-cycle-toggle]');
 function render(){const s=stages[index];['version','state','output','output-note','evidence','story-label','story'].forEach((k,i)=>demo.querySelector('[data-'+k+']').textContent=s[i]);demo.dataset.phase=index;demo.querySelectorAll('[data-cycle-step]').forEach((b,i)=>b.setAttribute('aria-pressed',String(i===index)));}
 function playback(){clearInterval(timer);demo.classList.toggle('is-paused',paused);toggle.textContent=paused?(en?'Play animation':'播放演示'):(en?'Pause animation':'暂停演示');if(!paused&&!document.hidden)timer=setInterval(()=>{index=(index+1)%5;render()},9000);demo.querySelectorAll('svg').forEach(s=>{if(paused)s.pauseAnimations?.();else s.unpauseAnimations?.()});}
 demo.querySelectorAll('[data-cycle-step]').forEach(b=>b.addEventListener('click',()=>{paused=true;index=Number(b.dataset.cycleStep);render();playback()}));
 demo.querySelector('[data-cycle-next]').addEventListener('click',()=>{paused=true;index=(index+1)%5;render();playback()});toggle.addEventListener('click',()=>{paused=!paused;playback()});
 document.addEventListener('visibilitychange',playback);matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change',e=>{if(e.matches){paused=true;playback()}});render();playback();
})();
