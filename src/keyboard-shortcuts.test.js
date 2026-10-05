import test from 'node:test';
import assert from 'node:assert/strict';
import { createNewConversationShortcutHandler } from './keyboard-shortcuts.js';

function makeEvent(overrides = {}) {
  let prevented = false;
  const event = {
    key: 'k',
    metaKey: false,
    ctrlKey: false,
    altKey: false,
    shiftKey: false,
    target: { tagName: 'BUTTON' },
    preventDefault() { prevented = true; },
    ...overrides,
  };
  return { event, wasPrevented: () => prevented };
}

test('starts a new conversation and prevents the browser default for Command+K', () => {
  let starts = 0;
  const handler = createNewConversationShortcutHandler(() => { starts += 1; });
  const { event, wasPrevented } = makeEvent({ metaKey: true });

  assert.equal(handler(event), true);
  assert.equal(starts, 1);
  assert.equal(wasPrevented(), true);
});

test('supports Ctrl+K on non-Mac platforms', () => {
  let starts = 0;
  const handler = createNewConversationShortcutHandler(() => { starts += 1; });
  const { event, wasPrevented } = makeEvent({ ctrlKey: true });

  assert.equal(handler(event), true);
  assert.equal(starts, 1);
  assert.equal(wasPrevented(), true);
});

test('ignores other keys and additional modifiers', () => {
  let starts = 0;
  const handler = createNewConversationShortcutHandler(() => { starts += 1; });

  for (const overrides of [
    { key: 'k' },
    { key: 'x', metaKey: true },
    { key: 'k', metaKey: true, shiftKey: true },
    { key: 'k', ctrlKey: true, altKey: true },
  ]) {
    const { event, wasPrevented } = makeEvent(overrides);
    assert.equal(handler(event), false);
    assert.equal(wasPrevented(), false);
  }
  assert.equal(starts, 0);
});

test('does not hijack shortcuts while an editable field is focused', () => {
  let starts = 0;
  const handler = createNewConversationShortcutHandler(() => { starts += 1; });
  const targets = [
    { tagName: 'INPUT' },
    { tagName: 'TEXTAREA' },
    { tagName: 'SELECT' },
    { tagName: 'DIV', isContentEditable: true },
    { tagName: 'SPAN', closest: () => ({}) },
  ];

  for (const target of targets) {
    const { event, wasPrevented } = makeEvent({ metaKey: true, target });
    assert.equal(handler(event), false);
    assert.equal(wasPrevented(), false);
  }
  assert.equal(starts, 0);
});
