import test from 'node:test';
import assert from 'node:assert/strict';
import { copyStatusLabel, copyTextToClipboard } from './clipboard.js';

test('writes response text and reports success when clipboard access is available', async () => {
  let writtenText = '';
  const status = await copyTextToClipboard({
    writeText: async (text) => { writtenText = text; },
  }, 'Assistant response');

  assert.equal(status, 'copied');
  assert.equal(writtenText, 'Assistant response');
});

test('reports failure when clipboard permission is denied', async () => {
  const status = await copyTextToClipboard({
    writeText: async () => { throw new Error('Permission denied'); },
  }, 'Assistant response');

  assert.equal(status, 'failed');
});

test('reports failure when the clipboard API is unavailable', async () => {
  assert.equal(await copyTextToClipboard(undefined, 'Assistant response'), 'failed');
  assert.equal(await copyTextToClipboard({}, 'Assistant response'), 'failed');
});

test('uses visible labels for copy success and failure states', () => {
  assert.equal(copyStatusLabel('idle'), 'Copy');
  assert.equal(copyStatusLabel('copied'), 'Copied');
  assert.equal(copyStatusLabel('failed'), 'Copy failed');
});
