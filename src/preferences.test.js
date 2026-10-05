import test from 'node:test';
import assert from 'node:assert/strict';
import { savePreferences } from './preferences.js';

const preferences = {
  provider: 'ollama',
  baseUrl: 'http://localhost:11434',
  model: 'llama3.2',
};

test('saves the selected provider, endpoint, and model', () => {
  let savedEntry;
  const storage = {
    setItem(key, value) {
      savedEntry = { key, value };
    },
  };

  assert.equal(savePreferences(preferences, storage), true);
  assert.equal(savedEntry.key, 'switchboard.preferences');
  assert.deepEqual(JSON.parse(savedEntry.value), preferences);
});

test('treats unavailable or failing storage as a non-fatal preference save', () => {
  const storage = {
    setItem() {
      throw new Error('storage unavailable');
    },
  };

  assert.equal(savePreferences(preferences, storage), false);
});
