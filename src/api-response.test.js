import test from 'node:test';
import assert from 'node:assert/strict';
import { parseJsonResponse } from './api-response.js';

test('returns parsed JSON from a valid response', async () => {
  const payload = { text: 'Hello', usage: { totalTokens: 4 } };
  const response = { json: async () => payload };

  assert.deepEqual(await parseJsonResponse(response), payload);
});

test('replaces a raw parse error with a readable fallback and HTTP status', async () => {
  const response = {
    status: 502,
    json: async () => { throw new SyntaxError('Unexpected token <'); },
  };

  await assert.rejects(
    parseJsonResponse(response, 'The server returned an invalid model response.'),
    {
      name: 'Error',
      message: 'The server returned an invalid model response. (HTTP 502)',
    },
  );
});

test('uses the fallback without adding a status when none is available', async () => {
  const response = { json: async () => { throw new SyntaxError('Unexpected end'); } };

  await assert.rejects(
    parseJsonResponse(response, 'The server returned an invalid chat response.'),
    {
      name: 'Error',
      message: 'The server returned an invalid chat response.',
    },
  );
});
