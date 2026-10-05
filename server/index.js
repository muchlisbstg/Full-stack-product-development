import 'dotenv/config';
import express from 'express';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { callChatProvider, fetchProviderModels, validateChatRequest, validateModelRequest } from './provider.js';

const app = express();
const port = Number(process.env.PORT || 8787);
const host = '127.0.0.1';
const here = path.dirname(fileURLToPath(import.meta.url));

app.disable('x-powered-by');
app.use(express.json({ limit: '1mb' }));

app.get('/api/health', (_req, res) => {
  res.json({ ok: true, app: 'switchboard' });
});

app.post('/api/models', async (req, res) => {
  try {
    const config = validateModelRequest(req.body);
    const models = await fetchProviderModels(config);
    res.json({ models });
  } catch (error) {
    res.status(error.status || 502).json({ error: error.message || 'Unable to load models.' });
  }
});

app.post('/api/chat', async (req, res) => {
  try {
    const config = validateChatRequest(req.body);
    const result = await callChatProvider(config);
    res.json(result);
  } catch (error) {
    res.status(error.status || 502).json({ error: error.message || 'The model request failed.' });
  }
});

const dist = path.resolve(here, '../dist');
app.use(express.static(dist));
app.get('*', (_req, res, next) => {
  res.sendFile(path.join(dist, 'index.html'), (error) => {
    if (error) next();
  });
});

app.listen(port, host, () => {
  console.log(`Switchboard API listening on http://${host}:${port}`);
});
