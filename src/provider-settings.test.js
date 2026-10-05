import test from 'node:test';
import assert from 'node:assert/strict';
import { isConnectionSetupLocked, markProviderAsResponding, resetConnectionForProviderConfigChange } from './provider-settings.js';

test('locks connection settings while a chat request is active', () => {
  assert.equal(isConnectionSetupLocked(true, 'idle'), true);
});

test('locks connection settings while model availability is being checked', () => {
  assert.equal(isConnectionSetupLocked(false, 'checking'), true);
});

test('unlocks connection settings after checking settles', () => {
  for (const connection of ['idle', 'connected', 'error']) {
    assert.equal(isConnectionSetupLocked(false, connection), false);
  }
});

test('clears cached model suggestions and connection status after provider config changes', () => {
  const updates = [];
  resetConnectionForProviderConfigChange({
    setModels: (value) => updates.push(['models', value]),
    setConnection: (value) => updates.push(['connection', value]),
    setConnectionMessage: (value) => updates.push(['connectionMessage', value]),
  });

  assert.deepEqual(updates, [
    ['models', []],
    ['connection', 'idle'],
    ['connectionMessage', ''],
  ]);
});

test('replaces stale connection text after a successful chat response', () => {
  const updates = [];
  markProviderAsResponding({
    setConnection: (value) => updates.push(['connection', value]),
    setConnectionMessage: (value) => updates.push(['connectionMessage', value]),
  });

  assert.deepEqual(updates, [
    ['connection', 'connected'],
    ['connectionMessage', 'Connected and responding.'],
  ]);
});
