const OPENAI_DEFAULT = 'https://api.openai.com/v1';
const OLLAMA_DEFAULT = 'http://localhost:11434';
const REQUEST_TIMEOUT_MS = 120_000;
const REQUEST_TIMEOUT_MESSAGE = 'The model took too long to respond. Check that the provider is running and try again.';

export class RequestError extends Error {
  constructor(message, status = 400) {
    super(message);
    this.name = 'RequestError';
    this.status = status;
  }
}

function isTimeoutError(error) {
  return error?.name === 'TimeoutError' || error?.name === 'AbortError';
}

function timeoutRequestError() {
  return new RequestError(REQUEST_TIMEOUT_MESSAGE, 504);
}

function requireObject(value) {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    throw new RequestError('Expected a JSON object.');
  }
}

function providerName(value) {
  if (value !== 'openai' && value !== 'ollama') {
    throw new RequestError('Choose either OpenAI or Ollama.');
  }
  return value;
}

export function normalizeBaseUrl(provider, value) {
  const name = providerName(provider);
  const fallback = name === 'openai' ? OPENAI_DEFAULT : OLLAMA_DEFAULT;
  const raw = String(value || fallback).trim();
  let parsed;
  try {
    parsed = new URL(raw);
  } catch {
    throw new RequestError('Enter a valid provider URL, including http:// or https://.');
  }
  if (!['http:', 'https:'].includes(parsed.protocol) || parsed.username || parsed.password) {
    throw new RequestError('Provider URLs must use HTTP or HTTPS and cannot contain credentials.');
  }
  parsed.hash = '';
  parsed.search = '';
  let base = parsed.toString().replace(/\/+$/, '');
  if (name === 'openai' && (parsed.pathname === '/' || parsed.pathname === '')) {
    base += '/v1';
  }
  return base;
}

function requireModel(value) {
  const model = typeof value === 'string' ? value.trim() : '';
  if (!model) throw new RequestError('Enter a model name.');
  if (model.length > 200) throw new RequestError('Model names must be 200 characters or less.');
  return model;
}

function requireApiKey(provider, value) {
  const apiKey = typeof value === 'string' ? value.trim() : '';
  if (provider === 'openai' && !apiKey) throw new RequestError('Add your OpenAI API key in the connection panel.');
  return apiKey;
}

function parseTemperature(value) {
  if (value === undefined || value === null || value === '') return 0.7;
  const temperature = Number(value);
  if (!Number.isFinite(temperature) || temperature < 0 || temperature > 2) {
    throw new RequestError('Temperature must be a number from 0 to 2.');
  }
  return temperature;
}

export function validateModelRequest(body) {
  requireObject(body);
  const provider = providerName(body.provider);
  return {
    provider,
    baseUrl: normalizeBaseUrl(provider, body.baseUrl),
    apiKey: requireApiKey(provider, body.apiKey),
  };
}

export function validateChatRequest(body) {
  requireObject(body);
  const provider = providerName(body.provider);
  if (!Array.isArray(body.messages) || body.messages.length === 0 || body.messages.length > 50) {
    throw new RequestError('A conversation must contain between 1 and 50 messages.');
  }
  const messages = body.messages.map((item) => {
    if (!item || !['user', 'assistant'].includes(item.role) || typeof item.content !== 'string') {
      throw new RequestError('Messages must have a user or assistant role and text content.');
    }
    if (!item.content.trim() || item.content.length > 50_000) {
      throw new RequestError('Messages must contain text and stay under 50,000 characters.');
    }
    return { role: item.role, content: item.content };
  });
  const systemPrompt = typeof body.systemPrompt === 'string' ? body.systemPrompt.trim() : '';
  if (systemPrompt.length > 10_000) throw new RequestError('System instructions must be 10,000 characters or less.');
  return {
    provider,
    baseUrl: normalizeBaseUrl(provider, body.baseUrl),
    apiKey: requireApiKey(provider, body.apiKey),
    model: requireModel(body.model),
    messages,
    systemPrompt,
    temperature: parseTemperature(body.temperature),
  };
}

function responseErrorMessage(payload, fallback) {
  if (typeof payload?.error === 'string') return payload.error;
  if (typeof payload?.error?.message === 'string') return payload.error.message;
  if (typeof payload?.message === 'string') return payload.message;
  return fallback;
}

async function fetchJson(url, options, fallbackMessage) {
  let response;
  try {
    response = await fetch(url, { ...options, signal: AbortSignal.timeout(REQUEST_TIMEOUT_MS) });
  } catch (error) {
    if (isTimeoutError(error)) throw timeoutRequestError();
    throw new RequestError(`Could not reach the provider: ${error.message}`, 502);
  }
  let payload;
  try {
    payload = await response.json();
  } catch (error) {
    if (isTimeoutError(error)) throw timeoutRequestError();
    if (response.ok) {
      throw new RequestError('The provider returned an invalid JSON response.', 502);
    }
    payload = {};
  }
  if (!response.ok) {
    throw new RequestError(responseErrorMessage(payload, fallbackMessage), 502);
  }
  return payload;
}

export async function callChatProvider(config) {
  const messages = config.systemPrompt
    ? [{ role: 'system', content: config.systemPrompt }, ...config.messages]
    : config.messages;
  if (config.provider === 'openai') {
    const payload = await fetchJson(`${config.baseUrl}/chat/completions`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        authorization: `Bearer ${config.apiKey}`,
      },
      body: JSON.stringify({ model: config.model, messages, temperature: config.temperature, stream: false }),
    }, 'OpenAI returned an error.');
    const content = payload.choices?.[0]?.message?.content;
    const text = Array.isArray(content)
      ? content.map((part) => typeof part === 'string' ? part : part?.text || '').join('')
      : content;
    if (typeof text !== 'string' || !text.trim()) throw new RequestError('The model returned an empty response.', 502);
    return { text, usage: payload.usage ? { totalTokens: payload.usage.total_tokens ?? null } : null };
  }

  const payload = await fetchJson(`${config.baseUrl}/api/chat`, {
    method: 'POST',
    headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ model: config.model, messages, stream: false, options: { temperature: config.temperature } }),
  }, 'Ollama returned an error.');
  const text = payload.message?.content;
  if (typeof text !== 'string' || !text.trim()) throw new RequestError('The model returned an empty response.', 502);
  const promptTokens = Number(payload.prompt_eval_count || 0);
  const responseTokens = Number(payload.eval_count || 0);
  const totalTokens = promptTokens + responseTokens;
  return { text, usage: totalTokens > 0 ? { totalTokens } : null };
}

function providerModelItems(payload, property, provider) {
  const items = payload?.[property];
  if (items === undefined || items === null) return [];
  if (!Array.isArray(items)) throw new RequestError(`${provider} returned an invalid model list.`, 502);
  return items;
}

export async function fetchProviderModels(config) {
  if (config.provider === 'openai') {
    const payload = await fetchJson(`${config.baseUrl}/models`, {
      headers: { authorization: `Bearer ${config.apiKey}` },
    }, 'OpenAI could not load your models.');
    return providerModelItems(payload, 'data', 'OpenAI')
      .map((item) => item?.id)
      .filter((id) => typeof id === 'string' && id.trim())
      .sort((a, b) => a.localeCompare(b));
  }
  const payload = await fetchJson(`${config.baseUrl}/api/tags`, {}, 'Ollama could not load installed models.');
  return providerModelItems(payload, 'models', 'Ollama')
    .map((item) => item?.name || item?.model)
    .filter((name) => typeof name === 'string' && name.trim())
    .sort((a, b) => a.localeCompare(b));
}
