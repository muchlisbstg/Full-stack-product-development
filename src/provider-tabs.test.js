import test from 'node:test';
import assert from 'node:assert/strict';
import { getProviderTabIndex, handleProviderTabKey } from './provider-tabs.js';

function createTabs() {
  const state = { focused: null, selected: null };
  const tabs = {
    openai: { focus() { state.focused = 'openai'; } },
    ollama: { focus() { state.focused = 'ollama'; } },
  };
  const parentElement = {
    querySelector(selector) {
      const provider = selector.match(/data-provider="(openai|ollama)"/)?.[1];
      return provider ? tabs[provider] : null;
    },
  };
  return { state, tabs, parentElement };
}

function makeKeyEvent(key, activeProvider, parentElement) {
  return {
    key,
    currentTarget: { parentElement },
    defaultPrevented: false,
    preventDefault() { this.defaultPrevented = true; },
  };
}

test('keeps only the active provider tab in the tab sequence', () => {
  assert.equal(getProviderTabIndex('openai', 'openai'), 0);
  assert.equal(getProviderTabIndex('openai', 'ollama'), -1);
  assert.equal(getProviderTabIndex('ollama', 'openai'), -1);
  assert.equal(getProviderTabIndex('ollama', 'ollama'), 0);
});

for (const { key, active, expected } of [
  { key: 'ArrowRight', active: 'openai', expected: 'ollama' },
  { key: 'ArrowRight', active: 'ollama', expected: 'openai' },
  { key: 'ArrowLeft', active: 'openai', expected: 'ollama' },
  { key: 'ArrowLeft', active: 'ollama', expected: 'openai' },
  { key: 'Home', active: 'ollama', expected: 'openai' },
  { key: 'End', active: 'openai', expected: 'ollama' },
]) {
  test(`${key} moves focus and selects ${expected} from ${active}`, () => {
    const { state, parentElement } = createTabs();
    const event = makeKeyEvent(key, active, parentElement);

    handleProviderTabKey(event, active, (provider) => { state.selected = provider; });

    assert.equal(event.defaultPrevented, true);
    assert.equal(state.focused, expected);
    assert.equal(state.selected, expected);
  });
}

test('ignores unrelated keys and invalid active provider values', () => {
  const { state, parentElement } = createTabs();
  const unrelatedEvent = makeKeyEvent('Tab', 'openai', parentElement);
  handleProviderTabKey(unrelatedEvent, 'openai', (provider) => { state.selected = provider; });
  assert.equal(unrelatedEvent.defaultPrevented, false);

  const invalidEvent = makeKeyEvent('ArrowRight', 'other', parentElement);
  handleProviderTabKey(invalidEvent, 'other', (provider) => { state.selected = provider; });
  assert.equal(invalidEvent.defaultPrevented, false);
  assert.equal(state.selected, null);
});
