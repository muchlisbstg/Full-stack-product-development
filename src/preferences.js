const PREFERENCES_KEY = 'switchboard.preferences';

export function savePreferences({ provider, baseUrl, model }, storage) {
  try {
    const target = storage ?? globalThis.localStorage;
    target.setItem(PREFERENCES_KEY, JSON.stringify({ provider, baseUrl, model }));
    return true;
  } catch {
    return false;
  }
}
