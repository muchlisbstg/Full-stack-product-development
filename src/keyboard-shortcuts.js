const EDITABLE_ELEMENTS = new Set(['INPUT', 'TEXTAREA', 'SELECT']);

function isEditableTarget(target) {
  const tagName = typeof target?.tagName === 'string' ? target.tagName.toUpperCase() : '';
  return EDITABLE_ELEMENTS.has(tagName)
    || target?.isContentEditable === true
    || Boolean(target?.closest?.('[contenteditable]:not([contenteditable="false"])'));
}

export function createNewConversationShortcutHandler(onNewConversation) {
  return (event) => {
    const key = typeof event?.key === 'string' ? event.key.toLowerCase() : '';
    if (
      key !== 'k'
      || (!event.metaKey && !event.ctrlKey)
      || event.altKey
      || event.shiftKey
      || isEditableTarget(event.target)
    ) {
      return false;
    }

    event.preventDefault();
    onNewConversation();
    return true;
  };
}

export function createEscapeShortcutHandler(onEscape) {
  return (event) => {
    if (event?.key !== 'Escape') return false;

    event.preventDefault();
    onEscape();
    return true;
  };
}
