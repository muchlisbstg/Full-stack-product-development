import test from 'node:test';
import assert from 'node:assert/strict';
import { resetConversationView } from './conversation-reset.js';

function createSetters(updates) {
  return {
    setMessages: (value) => updates.push(['messages', value]),
    setDraft: (value) => updates.push(['draft', value]),
    setError: (value) => updates.push(['error', value]),
    setSidebarOpen: (value) => updates.push(['sidebarOpen', value]),
    setScrollVisible: (value) => updates.push(['scrollVisible', value]),
  };
}

test('resets conversation and hides Latest when starting a new conversation', () => {
  const updates = [];
  const didReset = resetConversationView({ busy: false, ...createSetters(updates) });

  assert.equal(didReset, true);
  assert.deepEqual(updates, [
    ['messages', []],
    ['draft', ''],
    ['error', ''],
    ['sidebarOpen', false],
    ['scrollVisible', false],
  ]);
});

test('does not reset the conversation while a response is active', () => {
  const updates = [];
  const didReset = resetConversationView({ busy: true, ...createSetters(updates) });

  assert.equal(didReset, false);
  assert.deepEqual(updates, []);
});
