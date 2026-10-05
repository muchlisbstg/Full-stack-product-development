export function resetConversationView({
  busy,
  setMessages,
  setDraft,
  setError,
  setSidebarOpen,
  setScrollVisible,
}) {
  if (busy) return false;

  setMessages([]);
  setDraft('');
  setError('');
  setSidebarOpen(false);
  setScrollVisible(false);
  return true;
}
