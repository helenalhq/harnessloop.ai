'use strict';
/* One restrained entrance for groups of cards. Content is only ever hidden when this script
   runs, supports the observer and the visitor has not asked for reduced motion. */
(() => {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduced || !('IntersectionObserver' in window)) return;
  const selector = '.hl-pain-card,.hl-home-card,.hl-faq-item,.hl-engagement-step,.hl-showcase,.hl-run-steps>li,.hl-deliverables>li';
  const items = [...document.querySelectorAll(selector)];
  if (!items.length) return;
  document.documentElement.classList.add('hl-reveal-on');
  const io = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-in');
      io.unobserve(entry.target);
    }
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  for (const el of items) {
    const box = el.getBoundingClientRect();
    /* Already on screen at load: show at once, so nothing pops in on first paint. */
    if (box.top < window.innerHeight * 0.92 && box.bottom > 0) el.classList.add('is-in');
    else io.observe(el);
  }
})();
