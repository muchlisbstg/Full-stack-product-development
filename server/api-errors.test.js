import test from 'node:test';
import assert from 'node:assert/strict';
import { once } from 'node:events';
import express from 'express';
import { apiNotFoundHandler } from './api-errors.js';

async function withApp(run) {
  const app = express();
  app.get('/api/health', (_request, response) => response.json({ ok: true }));
  app.use(apiNotFoundHandler);
  app.get('*', (_request, response) => response.type('html').send('<!doctype html><main>app</main>'));

  const server = app.listen(0, '127.0.0.1');
  await once(server, 'listening');
  const baseUrl = `http://127.0.0.1:${server.address().port}`;
  try {
    return await run(baseUrl);
  } finally {
    const closed = new Promise((resolve, reject) => {
      server.close((error) => error ? reject(error) : resolve());
    });
    server.closeAllConnections();
    await closed;
  }
}

test('returns a JSON 404 for an unknown GET API path', async () => {
  await withApp(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/missing`);
    assert.equal(response.status, 404);
    assert.equal(response.headers.get('content-type')?.split(';')[0], 'application/json');
    assert.deepEqual(await response.json(), { error: 'API endpoint not found.' });
  });
});

test('returns a JSON 404 for an unsupported method on an API path', async () => {
  await withApp(async (baseUrl) => {
    const response = await fetch(`${baseUrl}/api/chat`, { method: 'POST' });
    assert.equal(response.status, 404);
    assert.equal(response.headers.get('content-type')?.split(';')[0], 'application/json');
    assert.deepEqual(await response.json(), { error: 'API endpoint not found.' });
  });
});

test('keeps known API routes and non-API app fallback behavior unchanged', async () => {
  await withApp(async (baseUrl) => {
    const health = await fetch(`${baseUrl}/api/health`);
    assert.equal(health.status, 200);
    assert.deepEqual(await health.json(), { ok: true });

    const appShell = await fetch(`${baseUrl}/settings`);
    assert.equal(appShell.status, 200);
    assert.match(await appShell.text(), /<main>app<\/main>/);
  });
});
