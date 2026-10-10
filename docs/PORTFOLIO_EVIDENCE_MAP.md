# Portfolio Evidence Map

Use this page to keep public portfolio claims tied to verifiable artifacts. The repository currently contains the Switchboard AI workspace; broader full-stack capabilities should be presented as skills or planned work unless a working artifact proves the claim.

## Project: Switchboard AI workspace

| Claim area | Evidence to link | What to verify before publishing |
|---|---|---|
| React user interface | `src/App.jsx`, `src/styles.css` | Provider selection, conversation flow, responsive states |
| Local API boundary | `server/index.js` | Server binds to loopback by default; request validation and error behavior |
| Provider handling | `server/provider.js` | OpenAI/Ollama routing, upstream errors, URL restrictions |
| API key handling | `src/provider-settings.js` and server provider tests | Key is not persisted to browser storage or written to logs |
| Input and response resilience | `server/api-errors.test.js`, `server/json-body-errors.test.js`, `src/api-response.test.js` | Malformed input and provider failures produce safe outcomes |
| Accessibility interactions | `src/dialog-focus.test.js`, `src/live-regions.test.js`, keyboard tests | Keyboard-only navigation, focus restoration, screen-reader announcements |
| CI and build | `.github/workflows/ci.yml` | Required tests and production build pass on the exact commit |

## Public case-study checklist

- [ ] State the user problem and target audience.
- [ ] Separate implemented features from proposed features.
- [ ] Link the source file, test, release, or demo that supports each technical claim.
- [ ] Include architecture and important trade-offs.
- [ ] Report measurable results only when measured and reproducible.
- [ ] Redact API keys, private URLs, customer data, and internal logs.
- [ ] State current limitations, including local-only deployment or missing authentication where applicable.

## Capability labels

Use these labels consistently:
- **Implemented:** present in the default branch and supported by tests or a runnable demo.
- **In progress:** work exists on an open pull request or branch.
- **Planned:** documented intention without a merged implementation.
- **Not verified:** evidence has not yet been collected.

Do not describe the repository as an enterprise production system solely because it uses a modern stack. Production readiness depends on the specific deployment, security controls, operations, and review evidence.
