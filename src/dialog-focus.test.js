import test from 'node:test';
import assert from 'node:assert/strict';
import { focusDialogFirstControl, restoreDialogFocus, trapDialogTabKey } from './dialog-focus.js';

function createDialog(controlCount = 3) {
  const document = { activeElement: null };
  const controls = Array.from({ length: controlCount }, () => ({
    focus() { document.activeElement = this; },
  }));
  const dialog = {
    ownerDocument: document,
    querySelector: () => controls[0],
    querySelectorAll: () => controls,
    contains: (element) => controls.includes(element),
    focus() { document.activeElement = this; },
  };
  document.activeElement = controls[0] || dialog;
  return { dialog, document, controls };
}

function keyEvent(dialog, { key = 'Tab', shiftKey = false } = {}) {
  return {
    key,
    shiftKey,
    currentTarget: dialog,
    defaultPrevented: false,
    preventDefault() { this.defaultPrevented = true; },
  };
}

test('focuses the first available dialog control', () => {
  const { dialog, document, controls } = createDialog();
  document.activeElement = null;

  focusDialogFirstControl(dialog);

  assert.equal(document.activeElement, controls[0]);
});

test('restores focus to the element that opened the dialog', () => {
  let focused = false;
  restoreDialogFocus({ focus() { focused = true; } });
  assert.equal(focused, true);
  assert.doesNotThrow(() => restoreDialogFocus(null));
});

test('wraps Tab from the last control to the first', () => {
  const { dialog, document, controls } = createDialog();
  document.activeElement = controls.at(-1);
  const event = keyEvent(dialog);

  trapDialogTabKey(event);

  assert.equal(event.defaultPrevented, true);
  assert.equal(document.activeElement, controls[0]);
});

test('wraps Shift+Tab from the first control to the last', () => {
  const { dialog, document, controls } = createDialog();
  document.activeElement = controls[0];
  const event = keyEvent(dialog, { shiftKey: true });

  trapDialogTabKey(event);

  assert.equal(event.defaultPrevented, true);
  assert.equal(document.activeElement, controls.at(-1));
});

test('leaves normal Tab movement between dialog controls unchanged', () => {
  const { dialog, document, controls } = createDialog();
  document.activeElement = controls[1];
  const event = keyEvent(dialog);

  trapDialogTabKey(event);

  assert.equal(event.defaultPrevented, false);
  assert.equal(document.activeElement, controls[1]);
});

test('ignores keys other than Tab', () => {
  const { dialog, document, controls } = createDialog();
  const event = keyEvent(dialog, { key: 'Escape' });

  trapDialogTabKey(event);

  assert.equal(event.defaultPrevented, false);
  assert.equal(document.activeElement, controls[0]);
});

test('keeps focus on the dialog when it has no focusable controls', () => {
  const { dialog, document } = createDialog(0);
  document.activeElement = null;
  const event = keyEvent(dialog);

  trapDialogTabKey(event);

  assert.equal(event.defaultPrevented, true);
  assert.equal(document.activeElement, dialog);
});
