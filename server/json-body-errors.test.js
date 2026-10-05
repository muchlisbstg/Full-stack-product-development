import test from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import express from 'express';
import { JSON_BODY_LIMIT, jsonBodyErrorHandler } from './json-body-errors.js';

async function withApi(run) {
  const app = express();
  app.use(express.json({ limit: JSON_BODY_LIMIT }));
  app.use(jsonBodyErrorHandler);
  app.post('/api/chat', (request, response) => response.json({ received: request.body }));

  const server = app.listen(0, '127.0.0.1');
  await once(server, 'listening');
  const url = `http://127.0.0.1:${server.address().port}/api/chat`;
  try {
    return await run(url);
  } finally {
    const closed = new Promise((resolve, reject) => {
      server.close((error) => error ? reject(error) : resolve());
    });
    server.closeAllConnections();
    await closed;
  }
}

async function postJson(url, body) {
  return fetch(url, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body,
  });
}

test('returns a JSON 400 for malformed JSON request bodies', async () => {
  await withApi(async (url) => {
    const response = await postJson(url, '{"provider":');
    assert.equal(response.status, 400);
    assert.equal(response.headers.get('content-type')?.split(';')[0], 'application/json');
    assert.deepEqual(await response.json(), { error: 'Request body must be valid JSON.' });
  });
});

test('returns a JSON 413 when the request body exceeds the configured limit', async () => {
  await withApi(async (url) => {
    const response = await postJson(url, JSON.stringify({ content: 'x'.repeat(JSON_BODY_LIMIT) }));
    assert.equal(response.status, 413);
    assert.equal(response.headers.get('content-type')?.split(';')[0], 'application/json');
    assert.deepEqual(await response.json(), { error: 'Request body exceeds the 1 MiB limit.' });
  });
});

test('passes valid JSON bodies through to the API route', async () => {
  await withApi(async (url) => {
    const response = await postJson(url, JSON.stringify({ provider: 'ollama' }));
    assert.equal(response.status, 200);
    assert.deepEqual(await response.json(), { received: { provider: 'ollama' } });
  });
});
