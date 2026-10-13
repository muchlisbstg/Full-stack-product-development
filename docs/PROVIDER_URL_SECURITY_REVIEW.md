# Provider URL Security Review

## Status

Review and implementation plan only. This document does not claim that provider URL SSRF is fixed.

The Switchboard API currently accepts a caller-supplied `baseUrl` for both provider types. URL normalization restricts the scheme to HTTP(S) and rejects embedded credentials, but does not restrict the destination host, port, resolved IP address, or network destination. Disabling automatic redirects reduces one attack path but is not a complete SSRF defense.

## Current trust boundary

- The API binds to `127.0.0.1` by default and is intended for local development.
- Requests to `/api/chat` and `/api/models` can cause the server process to make outbound HTTP requests to the supplied provider URL.
- Chat messages are forwarded to the selected provider.
- The API does not implement user authentication; it must not be exposed to an untrusted network as-is.
- Ollama on `http://localhost:11434` is a supported local workflow and must remain supported.

## Required defense-in-depth

1. **Provider destination policy**
   - Use `https://api.openai.com` as the built-in OpenAI destination.
   - Support custom compatible providers only through an explicit operator-managed hostname allowlist.
   - For Ollama, allow the documented local loopback endpoint and require explicit operator configuration for any other destination.
   - Reject URL credentials, fragments, unexpected ports, and unsupported schemes.
2. **Connection-time network controls**
   - Enforce egress restrictions outside application URL parsing. Block cloud metadata endpoints and non-approved private, link-local, multicast, and reserved destinations for remote providers.
   - Validate every resolved A/AAAA address and prevent DNS rebinding between validation and connection. URL string checks alone cannot guarantee this.
   - Ensure redirects remain disabled and the HTTP client cannot silently follow a redirect to a different destination.
3. **Request limits**
   - Keep bounded request bodies, response deadlines, and bounded response parsing.
   - Add explicit response-size limits; a timeout alone does not cap memory consumption.
4. **Local application boundary**
   - Preserve loopback binding by default.
   - If remote access is ever introduced, require authentication, CSRF/origin protections where applicable, rate limits, and a reviewed deployment threat model.
5. **Verification**
   - Add tests for unsupported schemes, URL credentials, disallowed hostnames, IPv4/IPv6 loopback and private ranges, metadata targets, unusual ports, redirects, DNS rebinding behavior, and allowed Ollama loopback.
   - Run the repository test/build workflow and review the actual CI result before treating the change as validated.

## Safe implementation sequence

1. Agree on supported custom-provider behavior and the operator allowlist configuration.
2. Implement and test deterministic hostname/port policy in the application.
3. Add connection-time egress/DNS protections appropriate to the deployment runtime.
4. Verify Ollama local development and the built-in OpenAI endpoint still work.
5. Keep the application marked local-development-only until authentication and network exposure are separately reviewed.

## Release gate

Do not expose the API to the public internet or treat it as production-ready based on redirect blocking alone. No production deployment is authorized by this document.
