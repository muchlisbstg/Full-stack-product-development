import test from 'node:test';
import assert from 'node:assert/strict';
import { resizeComposer } from './composer-resize.js';

function makeTextarea(scrollHeight) {
  return { scrollHeight, style: { height: '' } };
}

test('keeps short drafts at the 54px minimum height', () => {
  const textarea = makeTextarea(42);

  resizeComposer(textarea);

  assert.equal(textarea.style.height, '54px');
});

test('grows to fit the draft when within the height limit', () => {
  const textarea = makeTextarea(116);

  resizeComposer(textarea);

  assert.equal(textarea.style.height, '116px');
});

test('caps long drafts at the 180px maximum height', () => {
  const textarea = makeTextarea(260);

  resizeComposer(textarea);

  assert.equal(textarea.style.height, '180px');
});

test('does nothing when the textarea is not mounted', () => {
  assert.doesNotThrow(() => resizeComposer(null));
});
