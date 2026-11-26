'use strict';
/* Poster with one play button. Without JavaScript, or before it runs, the browser's own
   controls stay on the element, so the video is never left unplayable. */
document.querySelectorAll('.hl-video-frame > video[data-play]').forEach((video) => {
  const frame = video.parentElement;
  const button = document.createElement('button');
  button.type = 'button';
  button.className = 'hl-video-play';
  const icon = document.createElement('span');
  icon.setAttribute('aria-hidden', 'true');
  icon.className = 'hl-video-play-icon';
  icon.innerHTML = '<svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor"><path d="M7 4.5v15l13-7.5z"/></svg>';
  const label = document.createElement('span');
  label.textContent = video.dataset.play;
  button.append(icon, label);
  button.addEventListener('click', () => {
    video.controls = true;
    frame.classList.add('is-playing');
    video.play();
  });
  video.addEventListener('play', () => frame.classList.add('is-playing'));
  video.addEventListener('loadeddata', () => frame.classList.remove('is-failed'));
  /* With <source> children the browser reports a failed download on the source, not the video. */
  for (const target of [video, ...video.querySelectorAll('source')]) {
    target.addEventListener('error', () => frame.classList.add('is-failed'));
  }
  frame.append(button);
  video.removeAttribute('controls');
});
