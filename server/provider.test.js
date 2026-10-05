import test from 'node:test';
import assert from 'node:assert/strict';
import { normalizeBaseUrl, validateChatRequest, validateModelRequest } from './provider.js';

const validChat = {
  provider: 'ollama',
  baseUrl: 'http://localhost:11434/',
  model: 'llama3.2',
  messages: [{ role: 'user', content: 'Hello' }],
};

test('adds /v1 to a root OpenAI API URL', () => {
  assert.equal(normalizeBaseUrl('openai', 'https://api.openai.com'), 'https://api.openai.com/v1');
});

test('preserves a configured OpenAI API path', () => {
  assert.equal(normalizeBaseUrl('openai', 'http://localhost:1234/v1/'), 'http://localhost:1234/v1');
});

test('normalizes an Ollama root URL without adding a route', () => {
  assert.equal(normalizeBaseUrl('ollama', 'http://localhost:11434/'), 'http://localhost:11434');
});

test('rejects non-http provider URLs and embedded credentials', () => {
  assert.throws(() => normalizeBaseUrl('ollama', 'file:///tmp/ollama'), /HTTP or HTTPS/);
  assert.throws(() => normalizeBaseUrl('openai', 'https://user:pass@example.com/v1'), /cannot contain credentials/);
});

test('validates Ollama chat settings and applies safe defaults', () => {
  const config = validateChatRequest(validChat);
  assert.equal(config.baseUrl, 'http://localhost:11434');
  assert.equal(config.temperature, 0.7);
  assert.equal(config.systemPrompt, '');
});

test('rejects a missing OpenAI API key', () => {
  assert.throws(() => validateModelRequest({ provider: 'openai', baseUrl: 'https://api.openai.com/v1' }), /API key/);
});

test('rejects invalid messages and out-of-range temperature', () => {
  assert.throws(() => validateChatRequest({ ...validChat, messages: [{ role: 'system', content: 'no' }] }), /user or assistant/);
  assert.throws(() => validateChatRequest({ ...validChat, temperature: 3 }), /from 0 to 2/);
});
