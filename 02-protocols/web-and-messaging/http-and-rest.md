---
title: "HTTP and REST API engineering"
summary: "Developer reference for current HTTP revisions, resource semantics, conditional requests, retries, errors, authentication, request integrity, and hardened physical-security APIs."
page_type: protocol
domains: [cross-domain, networking]
tags:
  - http
  - rest
  - tls
  - oauth
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "RFC 9110 / STD 97: HTTP Semantics"
  - "RFC 9112 / STD 99: HTTP/1.1, updated by RFC 9931"
  - "RFC 9113: HTTP/2"
  - "RFC 9114: HTTP/3"
  - "RFC 10017: OAuth 2.0 for Browser-Based Applications"
coverage_limit: "HTTP and API contract guidance only; no API, proxy, TLS endpoint, OAuth server, authorization, parser differential, performance, or high-impact request is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# HTTP and REST API engineering

[Web and messaging protocols](README.md) / HTTP and REST

HTTP supplies message semantics and versioned transports. REST is an architectural style, not a separate wire protocol, schema language, authentication method, or guarantee of good resource design. A physical-security API should document both the HTTP contract and the domain contract. [HTTP] [FIELDING]

## Current protocol bases

| Layer | Current base | Operational distinction |
|---|---|---|
| HTTP semantics | RFC 9110 / STD 97 (2022) | Methods, fields, status codes, content, representation, intermediaries |
| Caching | RFC 9111 (2022) | Cache keys, freshness, validation, invalidation, shared/private behavior |
| HTTP/1.1 framing | RFC 9112 / STD 99 (2022), updated by RFC 9931 (2026) | Text framing and strict message boundaries; parser disagreement creates smuggling risk |
| HTTP/2 | RFC 9113 (2022) | Binary framing and multiplexed streams over one connection |
| HTTP/3 | RFC 9114 (2022) | HTTP semantics over QUIC; independent streams reduce TCP head-of-line coupling |
| TLS | RFC 8446 (TLS 1.3) | Transport confidentiality, integrity, and endpoint authentication when trust is validated |

HTTP versions preserve common semantics but differ materially in framing, connection, prioritization, flow-control, and failure behavior. Gateways must translate without creating ambiguous lengths, pseudo-header errors, authority confusion, or inconsistent normalization. [HTTP1] [HTTP2] [HTTP3]

## Resource contract

A durable API defines nouns and state transitions before routes:

| Concern | Example contract question |
|---|---|
| Identity | Is a door identified by immutable system ID, controller-local number, or human name? |
| Representation | Which fields are authoritative, derived, writable, nullable, or omitted by permission? |
| Lifecycle | Can a credential be pending, active, suspended, expired, revoked, or deleted? |
| Concurrency | What prevents one client from overwriting a newer change? |
| Time | Are timestamps UTC instants, device-local readings, intervals, or uncertain observations? |
| Command | Is “unlock” a resource-state change, bounded command, queued job, or policy override? |
| Completion | Does `2xx` mean accepted, persisted, delivered to a controller, or physically observed? |

Do not model high-impact commands as harmless field updates without an explicit audit and completion model.

## Methods, safety, and idempotency

Per RFC 9110, safe methods are read-only by defined semantics; idempotent methods can be repeated with the same intended effect. Server logging or accounting does not make a safe method unsafe, but a `GET` endpoint that unlocks a door violates method semantics. [HTTP]

| Method | Intended use | Retry guidance |
|---|---|---|
| GET | Retrieve a representation | Retry only with bounds; account for cache and stale data |
| HEAD | GET metadata without response content | Same conditional/cache semantics as documented |
| POST | Submit/process/create under resource semantics | Not inherently idempotent; use a documented operation key or job ID when retries are needed |
| PUT | Replace/create the selected resource state | Idempotent semantics; still use preconditions to prevent lost updates |
| PATCH | Apply a patch format | Idempotency depends on patch and contract |
| DELETE | Remove the selected mapping/state | Idempotent semantics do not mean every response is identical |

An “idempotency key” is an application contract: define key scope, authenticated principal, target, canonical request fingerprint, retention window, concurrent duplicate behavior, response replay, and conflict result. It cannot make two semantically different requests equivalent.

## Concurrency and conditional requests

Use validators such as ETags with `If-Match` for changes and `If-None-Match` for cache validation or create-if-absent behavior. Strong versus weak validators have different comparison rules. A typical optimistic update is:

1. `GET /credentials/{id}` and record the strong ETag.
2. Validate intended transition locally.
3. `PUT` or `PATCH` with `If-Match: "recorded-tag"`.
4. Treat `412 Precondition Failed` as a concurrency conflict, refetch, and reconsider—do not overwrite blindly.

## Read-only conditional request fixture

This synthetic protocol fragment illustrates cache validation for a read. `api.example`, the credential ID, token text, and ETag are documentation values; the fragment contains no client and should not be adapted into a state-changing credential operation.

```http
GET /v1/credentials/cred_demo_001 HTTP/1.1
Host: api.example
Authorization: Bearer replace-with-short-lived-test-token
Accept: application/json
If-None-Match: "demo-etag-7"
```

The API must authorize the read for the exact tenant/resource. A matching current validator can produce `304 Not Modified`; otherwise the server can return the authorized representation and a current validator. Even a safe method needs request, response, rate, cache, privacy, and log bounds.

## Status and error model

Use status codes consistently, then return a stable machine-readable error shape. RFC 9457 defines Problem Details for HTTP APIs. [PROBLEM]

| Status family/example | Meaning to preserve |
|---|---|
| `200`, `201`, `202`, `204` | Completed with representation; created; accepted asynchronously; completed without content |
| `304` | Conditional retrieval uses cached representation; not a generic success body |
| `400` | Syntactically/semantically invalid request when no more specific code applies |
| `401` | Authentication needed/failed and challenge semantics apply |
| `403` | Authenticated context lacks authorization or policy refuses operation |
| `404` | Resource absent or deliberately concealed by policy |
| `409` | Conflict with current domain state |
| `412` | HTTP precondition failed |
| `413`, `415`, `422`, `429` | Content too large; unsupported media type; unprocessable content; rate limited |
| `5xx` | Server/intermediary failure; not automatically safe to retry |

For asynchronous physical actions, return a job/operation resource with correlation ID, state, timestamps, result source, and expiry. Distinguish “controller acknowledged” from “door sensor confirmed.”

## Pagination, filtering, and time

- Prefer opaque cursors over mutable offset pagination for event streams.
- Bind a cursor to tenant, principal, query filters, sort order, snapshot/watermark, and expiry.
- Define inclusive/exclusive timestamp boundaries, ordering tie-breakers, late events, and clock uncertainty.
- Cap page size, query complexity, expanded relationships, date range, and export volume.
- Allowlist filter/sort fields; parameterized storage queries do not replace authorization.

## Authentication and authorization

- Use HTTPS with certificate validation. Mutual TLS can provide client/workload identity but still needs resource authorization.
- For OAuth 2.0 deployments follow RFC 9700, the current OAuth 2.0 Security Best Current Practice; use flows appropriate to public/confidential clients, sender constraint where needed, exact redirect validation, PKCE, scoped/audience-bound short-lived tokens, and refresh-token controls. [OAUTH-BCP]
- Validate token issuer, audience, signature/algorithm policy, time bounds, token type, client/subject, and required scope/claims. Do not accept a token merely because it parses.
- Authorize object and action together; prevent cross-tenant identifier substitution.
- Separate read video/events, enroll credentials, unlock/override, administer identities, export evidence, and manage devices.
- Recheck authorization for long-running exports, streams, and jobs.

Browser sessions also require CSRF, CORS, origin, cookie, SameSite, and content-security design. CORS is a browser read-control mechanism, not API authentication.

### Browser-based OAuth clients

RFC 10017 is the current IETF Best Current Practice for OAuth 2.0 browser-based applications. It evaluates architectural patterns and browser-specific threats; apply it together with RFC 9700 and the authorization server’s supported profile. [BROWSER-BCP]

- A browser application is a public client and cannot keep a distributed static client secret confidential.
- Use Authorization Code flow with PKCE and exact redirect-URI registration. Do not use the implicit grant for new applications.
- Bind `state` to the initiating browser session and intended return location; use OIDC nonce where the OIDC profile requires it.
- Prefer an architecture that keeps access/refresh tokens out of JavaScript, such as a backend-for-frontend, when consequence and deployment constraints support it.
- If tokens are exposed to browser code, keep their scope and lifetime minimal and account explicitly for XSS, malicious dependencies/extensions, storage, refresh, and multi-tab/session behavior.
- A backend-for-frontend session needs secure, HttpOnly cookies, CSRF protection, origin checks, session rotation, logout, and server-side authorization. Moving a token behind a cookie does not remove browser threats.
- Restrict third-party scripts, use an effective Content Security Policy, avoid sensitive tokens/codes in URLs and telemetry, and prevent open redirects.
- Treat refresh-token rotation or sender constraint as additional defenses under the chosen profile, not substitutes for preventing script compromise.
- Keep browser authentication/session success separate from authorization for tenant, object, operation, and high-impact physical actions.

Cross-device authorization/authentication flows have additional transaction-binding and phishing concerns; see [WebAuthn, FIDO, and passkeys](../infrastructure/webauthn-fido-and-passkeys.md).

## Message integrity and webhooks

RFC 9421 defines HTTP Message Signatures, but an application profile must still specify key discovery, algorithm policy, created/expiry time, nonce/replay behavior, and the exact covered components. Always cover authority, method, target, content digest where applicable, and security-critical fields according to the profile. A valid signature does not authorize the requested operation. [HTTP-SIG]

## Parser and intermediary safety

- Reject ambiguous HTTP/1.1 framing and conflicting length/transfer metadata; keep proxy/backend parsing aligned.
- Normalize a path once under a documented URI policy; avoid decoding or case rules that differ across authorization and routing layers.
- Validate `Host`/authority against the selected tenant and endpoint.
- Bound header fields, trailers, body, decompressed body, multipart parts, streams, concurrent requests, and HPACK/QPACK state.
- Do not send untrusted post-transition protocol bytes optimistically on HTTP/1.1. RFC 9931, published March 2026, adds requirements to prevent request-smuggling/parser risks during rejected `Upgrade` or `CONNECT` transitions. [HTTP-TRANSITION]
- Treat redirects as new authorization/egress decisions; never forward credentials across origin by default.

## Caching and sensitive data

Explicitly set cache policy. Credential records, live images, access events, configuration, and exports usually require private/no-store semantics tailored to the application. Ensure shared-cache keys include all representation-varying dimensions and never depend on `Authorization` behavior implicitly. Signed or expiring URLs need cache lifetimes no longer than authorization.

## Client reliability contract

- Set connect, TLS, header, body-idle, and total deadlines.
- Cancel abandoned requests and bound response reads.
- Retry only documented transient failures, with exponential backoff, jitter, retry budget, and `Retry-After` handling.
- Never retry a mutating request solely because no response arrived; its effect may have occurred.
- Use circuit breaking/load shedding without converting an access outage into an unsafe fail-open.
- Preserve a correlation ID but do not let clients choose trusted audit identity fields.

## Review checklist

- [ ] Exact HTTP versions, TLS policy, ALPN, proxy chain, and timeout behavior documented
- [ ] Resource identities, lifecycle states, command completion, and error model defined
- [ ] Safe/idempotent method semantics respected
- [ ] ETag/precondition and duplicate-request behavior specified
- [ ] Authentication plus per-object/per-action authorization enforced
- [ ] OAuth/token validation profile and credential rotation documented where used
- [ ] Browser clients follow RFC 10017 architecture, PKCE, redirect, cookie/session, CSRF, XSS, and token-storage guidance
- [ ] Parser, body, decompression, pagination, export, and concurrency limits enforced
- [ ] Request-smuggling differentials tested manually by the system owner or qualified assessor
- [ ] Sensitive caching, logs, traces, URLs, and error fields reviewed

## Sources

- **HTTP** — [RFC 9110 / STD 97: HTTP Semantics][HTTP], IETF, June 2022.
- **HTTP-CACHE** — [RFC 9111: HTTP Caching][HTTP-CACHE], IETF, June 2022.
- **HTTP1** — [RFC 9112 / STD 99: HTTP/1.1][HTTP1], IETF, June 2022, updated by RFC 9931.
- **HTTP2** — [RFC 9113: HTTP/2][HTTP2], IETF, June 2022.
- **HTTP3** — [RFC 9114: HTTP/3][HTTP3], IETF, June 2022.
- **HTTP-TRANSITION** — [RFC 9931: Security Considerations for Optimistic Protocol Transitions in HTTP/1.1][HTTP-TRANSITION], IETF, March 2026.
- **TLS13** — [RFC 8446: TLS 1.3][TLS13], IETF, August 2018.
- **OAUTH-BCP** — [RFC 9700 / BCP 240: Best Current Practice for OAuth 2.0 Security][OAUTH-BCP], IETF, January 2025.
- **BROWSER-BCP** — [RFC 10017: OAuth 2.0 for Browser-Based Applications][BROWSER-BCP], IETF.
- **HTTP-SIG** — [RFC 9421: HTTP Message Signatures][HTTP-SIG], IETF, February 2024.
- **PROBLEM** — [RFC 9457: Problem Details for HTTP APIs][PROBLEM], IETF, July 2023.
- **FIELDING** — [Architectural Styles and the Design of Network-based Software Architectures, Chapter 5][FIELDING], Roy Fielding, 2000.

[HTTP]: https://datatracker.ietf.org/doc/rfc9110/
[HTTP-CACHE]: https://datatracker.ietf.org/doc/rfc9111/
[HTTP1]: https://datatracker.ietf.org/doc/rfc9112/
[HTTP2]: https://datatracker.ietf.org/doc/rfc9113/
[HTTP3]: https://datatracker.ietf.org/doc/rfc9114/
[HTTP-TRANSITION]: https://datatracker.ietf.org/doc/rfc9931/
[TLS13]: https://datatracker.ietf.org/doc/rfc8446/
[OAUTH-BCP]: https://datatracker.ietf.org/doc/rfc9700/
[BROWSER-BCP]: https://www.rfc-editor.org/info/rfc10017/
[HTTP-SIG]: https://datatracker.ietf.org/doc/rfc9421/
[PROBLEM]: https://datatracker.ietf.org/doc/rfc9457/
[FIELDING]: https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
