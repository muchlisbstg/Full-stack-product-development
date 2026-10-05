import test from 'node:test';
import assert from 'node:assert/strict';
import { shouldSubmitMessageOnEnter } from './composer-keyboard.js';

test('submits on Enter when not composing', () => {
  assert.equal(shouldSubmitMessageOnEnter({ key: 'Enter', shiftKey: false }), true);
});

test('keeps Shift+Enter available for a newline', () => {
  assert.equal(shouldSubmitMessageOnEnter({ key: 'Enter', shiftKey: true }), false);
});

test('does not submit Enter while an IME composition is active', () => {
  assert.equal(shouldSubmitMessageOnEnter({ key: 'Enter', shiftKey: false, isComposing: true }), false);
  assert.equal(shouldSubmitMessageOnEnter({ key: 'Enter', shiftKey: false, nativeEvent: { isComposing: true } }), false);
});

test('does not submit for the legacy IME composition key code', () => {
  assert.equal(shouldSubmitMessageOnEnter({ key: 'Enter', shiftKey: false, keyCode: 229 }), false);
  assert.equal(shouldSubmitMessageOnEnter({ key: 'Enter', shiftKey: false, nativeEvent: { keyCode: 229 } }), false);
});

test('ignores keys other than Enter', () => {
  assert.equal(shouldSubmitMessageOnEnter({ key: 'k', shiftKey: false }), false);
});
