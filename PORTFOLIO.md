# Muchlis Bstg — Full-Stack Product Development Portfolio

> Engineering portfolio for demonstrating product thinking, application architecture, implementation quality, and delivery discipline.

## Profile

Full-stack developer focused on business applications, API integration, workflow automation, and AI-assisted engineering. The goal is to build software that is useful, testable, secure by default, and maintainable.

## Featured project in this repository: Switchboard

**Status:** Existing application scaffold; verify current behavior locally before presenting it as production-ready.

Switchboard is a local-first AI workspace with a React/Vite client and a Node/Express API. It is designed to let users work with OpenAI or a locally running Ollama model through one interface.

### What the codebase demonstrates

- React UI composition and client-side state.
- Node.js and Express API boundary.
- Provider configuration for remote and local model backends.
- Markdown response rendering.
- Small, testable utility modules with Node test coverage.
- Vite-based development and production build scripts.
- Local-first intent and server-side handling of provider requests.

### Architecture at a glance

```text
React + Vite UI
      |
      | HTTP API
      v
Node.js + Express
      |
      +---- OpenAI API
      |
      +---- Local Ollama endpoint
```

Provider credentials should remain server-side. Before deployment, review authentication, request limits, secret handling, error redaction, CORS, and network binding for the intended environment.

## Engineering capabilities

| Area | Evidence to add as the portfolio matures |
|---|---|
| Discovery | Problem statement, target users, requirements, and acceptance criteria |
| Design | Screenshots, interaction notes, responsive and accessibility checks |
| Frontend | Component structure, loading/error states, keyboard behavior |
| Backend | API contract, validation, safe error responses, provider adapters |
| Data | Data flow and retention decisions; avoid storing secrets or sensitive prompts by default |
| Quality | Test results, reproducible build steps, and known limitations |
| Delivery | CI status, deployment notes, versioned releases, and rollback approach |

## Case-study format

For each project, document:

1. **Problem** — who experiences the problem and why it matters.
2. **Constraints** — technical, business, security, and operational boundaries.
3. **Solution** — the implemented behavior, not planned behavior.
4. **Architecture** — major components and trust boundaries.
5. **Validation** — commands run, tests passed, and unresolved failures.
6. **Evidence** — screenshots, demo, release, or issue/PR links.
7. **Outcome** — measurable result only when it has been measured.

## Roadmap

- [ ] Verify install, test, and build commands on a clean environment.
- [ ] Add current UI screenshots and a short demo walkthrough.
- [ ] Document API routes, request validation, and failure modes.
- [ ] Add automated CI for tests and production build.
- [ ] Record accessibility, security, and performance findings.
- [ ] Publish a deployment guide only after a target environment is selected.

## Related work

- [Business Automation System](https://github.com/muchlisbstg/business-automation-system) — workflow contracts, backend orchestration, and CI validation.
- [Enterprise Export Platform USA](https://github.com/muchlisbstg/enterprise-export-platform-usa) — modular enterprise platform planning and export-oriented workflow design.

## Integrity note

This portfolio distinguishes implemented features from proposals. Do not infer customer adoption, production uptime, security certification, regulatory compliance, or business results unless independently verified.
