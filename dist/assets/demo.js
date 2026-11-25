'use strict';
// Three-act demo interactions. Fully client-side and in-memory:
// no fetch, no storage, no data collection. Strings are set with textContent only.
(function () {
  var COPY = {
    zh: {
      src: '回复草稿 · BK-20431',
      judgeApprove: '人工 · 批准', actApprove: '发送草稿邮件（本演示未实际发送）',
      judgeEdit: '人工 · 修改', actEdit: '打开草稿编辑',
      judgeReject: '人工 · 拒绝', actReject: '草稿标记为不采用',
      noticeApprove: '已模拟批准。在生产环境中，这会把经你批准的回复交给发送通道，并把动作连同你的用户 ID 写入留痕记录。',
      noticeEdit: '已模拟编辑。在生产环境中，草稿会在你的邮件客户端中打开；修改内容与理由一起留在记录里。',
      noticeReject: '已模拟拒绝。在生产环境中，这封草稿会被标记为不采用，并要求填写原因——同样写入留痕。',
      noticeReset: '已重置。追加的演示记录已清空。'
    },
    en: {
      src: 'Reply draft · BK-20431',
      judgeApprove: 'Human · Approved', actApprove: 'Reply sent (not actually sent in this demo)',
      judgeEdit: 'Human · Edited', actEdit: 'Draft opened for editing',
      judgeReject: 'Human · Declined', actReject: 'Draft marked as declined',
      noticeApprove: 'Approval simulated. In production this hands the approved reply to the sending channel and logs the action with your user ID.',
      noticeEdit: 'Edit simulated. In production the draft opens in your email client; your changes and the reason stay in the record.',
      noticeReject: 'Rejection simulated. In production this draft is marked as declined, with a reason required — and that is logged too.',
      noticeReset: 'Reset. The appended demo rows have been cleared.'
    }
  };
  function lang() { return document.documentElement && document.documentElement.lang === 'en' ? 'en' : 'zh'; }
  function text(key) { return COPY[lang()][key]; }
  function now() { return new Date().toLocaleTimeString('en-GB'); }
  function setNotice(message) {
    var node = document.getElementById('hl-demo-notice');
    if (node) node.textContent = message;
  }
  function appendRow(judgmentKey, actionKey) {
    var tbody = document.getElementById('hl-demo-log');
    if (!tbody) return;
    var values = [now(), text('src'), text(judgmentKey), text(actionKey)];
    var row = document.createElement('tr');
    for (var i = 0; i < values.length; i++) {
      var cell = document.createElement('td');
      cell.textContent = values[i];
      row.appendChild(cell);
    }
    tbody.appendChild(row);
  }
  function act(action) {
    if (action === 'approve') { appendRow('judgeApprove', 'actApprove'); setNotice(text('noticeApprove')); }
    else if (action === 'edit') { appendRow('judgeEdit', 'actEdit'); setNotice(text('noticeEdit')); }
    else if (action === 'reject') { appendRow('judgeReject', 'actReject'); setNotice(text('noticeReject')); }
  }
  function reset() {
    var tbody = document.getElementById('hl-demo-log');
    if (!tbody) return;
    var seed = parseInt(tbody.getAttribute('data-seed') || '0', 10);
    while (tbody.rows && tbody.rows.length > seed) tbody.deleteRow(seed);
    setNotice(text('noticeReset'));
  }
  function wire() {
    var buttons = document.querySelectorAll('[data-demo-action]');
    for (var i = 0; i < buttons.length; i++) {
      (function (button) {
        button.addEventListener('click', function () {
          var action = button.getAttribute('data-demo-action');
          if (action === 'reset') reset();
          else act(action);
        });
      })(buttons[i]);
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', wire);
  else wire();
})();
