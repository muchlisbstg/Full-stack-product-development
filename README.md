# Full-stack Product Development — Switchboard Case Study

This repository is part of a full-stack product development portfolio. Its current concrete project is **Switchboard**, a local-first AI workspace described below. The repository name represents the portfolio area; it does not imply that every web, mobile, backend, QA, or DevOps capability is already implemented here.

## Switchboard — AI workspace

A local-first AI agent workspace where you can switch between the OpenAI API and an Ollama model in the same app. The React chat UI talks to a small Node/Express API, which keeps provider requests server-side and avoids exposing your OpenAI key to the browser's network requests.

## Features

- Switch providers in one workspace: OpenAI or a locally running Ollama server.
- Load available models from the selected provider, or type a model name manually.
- Keep the conversation context, set a system instruction, and tune temperature.
- Render Markdown and GitHub-flavored Markdown in assistant replies.
- Keep the API key in app memory only; it is not written to local storage, environment files, or server logs.
- Bind the app server to `127.0.0.1` by default for local use.

## Requirements

- Node.js 20 or newer
- npm
- For OpenAI: an API key with API access
- For Ollama: [Ollama](https://ollama.com/) running locally, plus at least one downloaded model

## Start the app

```bash
npm install
cp .env.example .env
npm run dev
```

Open [http://localhost:5173](http://localhost:5173). The Vite client proxies `/api` calls to the local Express server at `http://127.0.0.1:8787`.

For Ollama, make sure the Ollama service is running and download a model if needed, for example:

```bash
ollama pull llama3.2
```

Then select **Ollama**, leave the server URL as `http://localhost:11434`, choose `llama3.2`, and use **Test connection** to load installed models. For OpenAI, select **OpenAI**, enter your API key, and load models or type a model ID. Your key is held in memory for the current page session only and must be entered again after a refresh.

## Factory trawler dashboard preview

A standalone, responsive UI concept for factory-trawler fleet operations is available at `/factory-trawler-preview.html` while the Vite development server is running. The dashboard uses illustrative sample data and demo-only interactions; it does not connect to vessel systems or control equipment.

## Production build

```bash
npm run build
npm start
```

The production server serves the built client and API from `http://127.0.0.1:8787` by default. The standalone dashboard preview is also available at `/factory-trawler-preview.html`. Set `PORT` in `.env` to change the API port.

## Scripts

| Command | Purpose |
| --- | --- |
| `npm run dev` | Start the Vite client and local API together |
| `npm run build` | Create the production client bundle in `dist/` |
| `npm start` | Serve the production build and API |
| `npm test` | Run provider validation and URL normalization tests |

## Security notes

- The OpenAI API key is sent from the browser to the local API only when needed; it is not persisted or logged by this app.
- The app is intended for local development. The API binds to loopback (`127.0.0.1`) and does not include user authentication.
- A custom provider URL is sent the same chat content as the selected provider. Only use endpoints you trust.
- Provider origins are restricted: OpenAI defaults to `https://api.openai.com`, and Ollama defaults to loopback port `11434`. Custom provider origins must be explicitly configured by the operator in `PROVIDER_URL_ALLOWLIST` as comma-separated exact origins (scheme + hostname + port, with no path), for example `https://api.example.com,http://localhost:1234`.
- URL origin allowlisting is not a complete SSRF defense: DNS rebinding and unsafe network routes still require connection-time validation and outbound network/egress controls. Keep this app bound to loopback and do not expose it to untrusted networks.
- Ollama must be reachable from the computer running this app's API server.
