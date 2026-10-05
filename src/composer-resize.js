const MIN_HEIGHT = 54;
const MAX_HEIGHT = 180;

export function resizeComposer(textarea) {
  if (!textarea) return;

  textarea.style.height = `${MIN_HEIGHT}px`;
  const height = Math.min(Math.max(textarea.scrollHeight, MIN_HEIGHT), MAX_HEIGHT);
  textarea.style.height = `${height}px`;
}
