export async function copyTextToClipboard(clipboard, text) {
  if (!clipboard || typeof clipboard.writeText !== 'function') return 'failed';

  try {
    await clipboard.writeText(text);
    return 'copied';
  } catch {
    return 'failed';
  }
}

export function copyStatusLabel(status) {
  if (status === 'copied') return 'Copied';
  if (status === 'failed') return 'Copy failed';
  return 'Copy';
}
