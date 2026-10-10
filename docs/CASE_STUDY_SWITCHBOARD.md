# Case Study: Switchboard

**Project type:** AI-assisted workspace  
**Evidence status:** repository-based technical summary; product behavior and outcomes must be verified before public claims.

## Problem framing

Users may want one workspace for interacting with hosted and locally running language models without embedding provider credentials in a browser client. Switchboard explores a small application boundary between a React client and a Node.js API.

## Proposed user journey

1. User opens the workspace.
2. User selects/configures a supported provider.
3. Client submits a request to the application API.
4. Server adapter calls the configured provider.
5. Client renders the response and reports failures clearly.

This journey is a product description, not a claim that every step has been acceptance-tested in production.

## Architecture

- **Client:** React and Vite.
- **API:** Node.js and Express.
- **Model providers:** OpenAI API and a local Ollama endpoint.
- **Response UI:** Markdown rendering.
- **Quality:** repository includes Node test support and Vite build scripts; latest CI result should be linked from GitHub Actions.

## Key engineering decisions

### Keep provider secrets server-side

Provider credentials must not be bundled into client assets. Configuration should be read by the server from environment variables or a secret manager.

### Isolate provider-specific behavior

Keep provider request/response differences behind a small adapter boundary. Normalize errors before returning them to the client; never forward credentials or raw secret-bearing provider payloads.

### Make failures visible

The UI should distinguish invalid configuration, provider timeout, unavailable local service, rate limiting, and unexpected server errors without exposing stack traces.

## Risks to validate

- Authentication and authorization if deployed beyond a trusted local environment.
- Request size and rate limits.
- CORS and server network binding.
- Provider timeout and cancellation behavior.
- Markdown rendering safety for untrusted model output.
- Logging and retention of prompts and responses.
- Dependency and secret scanning.
- Accessibility and responsive layout.

## Verification checklist

- [ ] Clean install succeeds using the documented Node version.
- [ ] Unit tests pass from a clean checkout.
- [ ] Production build succeeds.
- [ ] OpenAI path tested with a non-production key.
- [ ] Ollama path tested against a local instance.
- [ ] Invalid credentials and provider timeouts have safe user-facing errors.
- [ ] No secrets appear in browser bundles, logs, or committed files.
- [ ] Screenshots and a short demo are captured.
- [ ] Measured results are added only after measurement.

## Results

Do not claim customer adoption, uptime, cost savings, production readiness, or security certification without evidence. Add screenshots, run links, and measurements here as they become available.
