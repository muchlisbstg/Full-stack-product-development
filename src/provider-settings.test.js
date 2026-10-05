import test from 'node:test';
import assert from 'node:assert/strict';
import { isConnectionSetupLocked } from './provider-settings.js';

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
