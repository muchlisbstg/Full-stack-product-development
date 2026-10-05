const PROVIDER_TABS = ['openai', 'ollama'];

export function getProviderTabIndex(activeProvider, tabProvider) {
  return activeProvider === tabProvider ? 0 : -1;
}

function getNextProvider(key, activeProvider) {
  const activeIndex = PROVIDER_TABS.indexOf(activeProvider);
  if (activeIndex === -1) return null;

  if (key === 'Home') return PROVIDER_TABS[0];
  if (key === 'End') return PROVIDER_TABS[PROVIDER_TABS.length - 1];
  if (key === 'ArrowRight') return PROVIDER_TABS[(activeIndex + 1) % PROVIDER_TABS.length];
  if (key === 'ArrowLeft') return PROVIDER_TABS[(activeIndex - 1 + PROVIDER_TABS.length) % PROVIDER_TABS.length];
  return null;
}

export function handleProviderTabKey(event, activeProvider, selectProvider) {
  const nextProvider = getNextProvider(event.key, activeProvider);
  if (!nextProvider) return;

  event.preventDefault();
  event.currentTarget.parentElement
    ?.querySelector(`[data-provider="${nextProvider}"]`)
    ?.focus();
  selectProvider(nextProvider);
}
