---
title: "WebSocket, Server-Sent Events, and webhooks"
summary: "Developer reference for bidirectional sessions, browser event streams, server callbacks, delivery semantics, authentication, replay resistance, and safe event contracts."
page_type: protocol
domains: [cross-domain, networking]
tags:
  - websocket
  - sse
  - webhooks
  - cloudevents
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 6455: WebSocket Protocol"
  - "WHATWG Server-Sent Events Living Standard"
  - "CloudEvents 1.0.2"
coverage_limit: "Transport and event-contract guidance only; no connection, browser, intermediary, callback registration, signature, delivery, retry, or endpoint behavior is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# WebSocket, Server-Sent Events, and webhooks

[Web and messaging protocols](README.md) / WebSocket, SSE, and webhooks

These mechanisms all deliver events but have different trust and delivery shapes:

| Mechanism | Direction | Connection owner | Native browser API | Typical security-system use |
|---|---|---|---|---|
| WebSocket | Bidirectional | Client opens long-lived connection | Yes | Live alarm/status UI, interactive signaling |
| Server-Sent Events (SSE) | Server to client | Client opens long-lived HTTP response | Yes, `EventSource` | Browser event/status feed |
| Webhook | Server to another server | Producer opens a new HTTP request per delivery/batch | No dedicated browser API | Alarm/access/health event integration |

Choosing a transport does not define event schema, ordering, retention, deduplication, authorization, or delivery completion.

## WebSocket protocol status

RFC 6455 is the WebSocket base. RFC 8441 defines bootstrapping WebSockets with HTTP/2 and RFC 9220 does so for HTTP/3. RFC 7692 defines compression extensions including `permessage-deflate`. These extension paths are negotiated and must not be assumed from the `ws`/`wss` URI alone. [WS] [WS-H2] [WS-H3] [WS-COMP]

### Opening handshake

For HTTP/1.1, the client sends an Upgrade request containing a fresh random key and the server replies with `101 Switching Protocols` plus the derived accept value. This detects protocol-confused intermediaries; it is not authentication. WebSocket clients must wait for the server response before sending frames. RFC 9931 reiterates why optimistic post-upgrade bytes create HTTP/1.1 parser/request-smuggling risk. [HTTP-TRANSITION]

**Target:** Documentation-only host.

**Inputs:** Placeholder key; no credentials.

**Side effects:** None.

```http
GET /v1/events HTTP/1.1
Host: events.example
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: replace-with-16-random-bytes-base64
Sec-WebSocket-Protocol: physical-security-dev.events.v1
Origin: https://console.example
```

The server must authenticate the HTTP request, validate allowed Origin values for browser clients, authorize the requested resource/subprotocol, negotiate only supported extensions, and cap pre-authentication work.

### Frame and connection behavior

- Client-to-server frames are masked; server-to-client frames are not. Masking prevents certain proxy/cache attacks and is not encryption.
- Messages can be fragmented across frames; enforce a complete-message limit across fragments.
- Control frames (close, ping, pong) have special size and fragmentation rules.
- Define text encoding/schema or binary encoding explicitly through a versioned subprotocol.
- Implement bounded send queues and backpressure; dropping, coalescing, disconnecting, or spilling must be an explicit policy.
- Define ping/pong, idle timeout, maximum connection age, drain/reconnect, and close-code behavior.
- Reauthenticate or end sessions when user entitlement, tenant membership, token, or device access changes.

Compression can amplify memory/CPU use and create cross-message confidentiality risks. Disable it for secrets or configure bounded context/window behavior after threat review.

## Server-Sent Events

SSE is defined by the WHATWG HTML Living Standard. A server responds with UTF-8 `text/event-stream`; the browser parses fields such as `event`, `data`, `id`, and `retry` and reconnects after interruption. The `Last-Event-ID` mechanism lets a client request continuation, but the service must define retention and authorization semantics. [SSE]

```text
event: door.state.changed
id: evt_demo_000042
retry: 5000
data: {"door_id":"door_demo_01","state":"closed","observed_at":"2026-08-25T00:00:00Z"}

```

The blank line dispatches the event. Multiple `data:` lines are joined with newlines. A service should:

- authenticate the initial request and authorize every event placed on that stream;
- validate `Last-Event-ID` as an opaque cursor bound to the same principal, tenant, and query;
- cap replay range, event size, connection duration, clients, and buffered bytes;
- send heartbeats/comments through intermediary idle timeouts;
- set cache and proxy buffering behavior intentionally;
- return the appropriate response when a client must stop reconnecting (the Living Standard specifies `204 No Content` for this purpose);
- avoid secrets in URLs because native `EventSource` API/header options are constrained compared with arbitrary HTTP clients.

## Webhook contract

There is no single universal webhook protocol. A complete profile defines:

- registration and callback URL validation;
- event envelope/schema/version;
- authentication and request integrity;
- delivery ID and event ID semantics;
- ordering scope;
- timeout and successful acknowledgment status;
- retry schedule, expiry, and dead-letter handling;
- duplicate, batch, partial-failure, and replay behavior;
- secret/key rotation and endpoint disablement.

Assume **at-least-once delivery** unless the producer proves a stronger end-to-end property. A consumer should durably record a scoped event/delivery ID and enqueue work before acknowledgment, then make downstream side effects idempotent. An HTTP success response usually means accepted by the consumer—not that every business effect completed.

## CloudEvents profile

CloudEvents 1.0.2 supplies a portable event envelope and HTTP binding. Pin the 1.0.2 tag: the repository's development branch can contain work-in-progress text. CloudEvents does not define transport reliability, authorization, or every domain's `data` schema. [CE] [CE-HTTP] [CE-WEBHOOK]

```json
{
  "specversion": "1.0",
  "id": "evt_demo_000042",
  "source": "https://events.example/sites/site_demo_01",
  "type": "com.example.access.door.state.v1",
  "subject": "doors/door_demo_01",
  "time": "2026-08-25T00:00:00Z",
  "datacontenttype": "application/json",
  "data": {
    "state": "closed",
    "quality": "observed"
  }
}
```

Treat `source`, `subject`, `type`, `time`, and `id` as untrusted claims until the authenticated producer profile validates them. Use a composite deduplication key when IDs are unique only within producer/source scope.

## Webhook request protection

Options include mutual TLS, OAuth sender credentials, and signed HTTP messages. RFC 9421 can carry HTTP Message Signatures, but the webhook profile must mandate:

- accepted algorithms and key identifiers;
- key-distribution/trust rules and rotation overlap;
- covered method, target authority/path/query, timestamp, content digest, and relevant headers;
- maximum clock skew, signature expiry, and nonce/delivery-ID replay cache;
- exact raw bytes or canonical representation used for content verification;
- behavior when proxies rewrite covered components.

Verify the signature over the received bytes before parsing a large body when the profile permits, but always apply a small transport size limit first. A valid signature proves key use under the profile; authorization still depends on producer, tenant, event type, and target subscription. [HTTP-SIG]

## Callback registration and SSRF

Webhook registration turns your producer into an HTTP client to user-influenced destinations. Defend against SSRF:

- require HTTPS and validate the complete URL;
- allowlist domains/tenants where feasible;
- resolve and connect under egress policy, checking every address family and redirect;
- block loopback, link-local, private/control-plane, metadata, multicast, and prohibited ports unless explicitly intended;
- revalidate on DNS changes and each redirect; prevent DNS rebinding gaps;
- do not attach producer-internal credentials to callback requests;
- use per-subscription secrets and network isolation;
- send a challenge/verification request that creates no state at the target.

## Common event semantics

- `event_id`: stable identity of the domain event.
- `delivery_id`: identity of this delivery attempt/batch.
- `occurred_at`: when the source says it happened.
- `observed_at`: when an ingest boundary observed it.
- `sequence`: meaningful only with a documented producer/partition scope.
- `schema_version`: compatibility contract independent of transport version.
- `quality`: observed, inferred, corrected, deleted, or unknown as appropriate.

Do not derive a door's current state by blindly applying events after gaps. Support snapshot/resynchronization and declare how corrections and out-of-order events are represented.

## Review checklist

- [ ] Direction and connection ownership match the use case
- [ ] Exact WebSocket subprotocol/SSE event/Webhook envelope version pinned
- [ ] Authentication at connection/delivery and authorization per stream/event enforced
- [ ] Origin/CORS/cookie/CSRF behavior reviewed for browser clients
- [ ] Message/event/body, fragment, buffer, queue, and connection limits set
- [ ] Ordering, gap, duplicate, replay, retry, and resynchronization behavior documented
- [ ] Callback SSRF and redirect/DNS controls enforced
- [ ] Signature/mTLS/OAuth key lifecycle and replay window documented
- [ ] Backpressure, slow consumer, reconnect storm, and dead-letter behavior designed
- [ ] Sensitive event fields minimized and logs redacted

## Environment validation

Validate WebSocket/SSE browser and intermediary behaviour, Origin and cookie policy, buffering and backpressure, reconnect storms, entitlement changes, webhook registration SSRF controls, signature/key rotation, retry/expiry, duplicate delivery, dead-letter handling, and resynchronization in the target environment.

## Sources

- **WS** — [RFC 6455: The WebSocket Protocol][WS], IETF, December 2011.
- **WS-H2** — [RFC 8441: Bootstrapping WebSockets with HTTP/2][WS-H2], IETF, September 2018.
- **WS-H3** — [RFC 9220: Bootstrapping WebSockets with HTTP/3][WS-H3], IETF, June 2022.
- **WS-COMP** — [RFC 7692: Compression Extensions for WebSocket][WS-COMP], IETF, September 2015.
- **HTTP-TRANSITION** — [RFC 9931: Security Considerations for Optimistic Protocol Transitions in HTTP/1.1][HTTP-TRANSITION], IETF, March 2026.
- **SSE** — [Server-sent events][SSE], WHATWG HTML Living Standard, accessed 2026-08-25.
- **CE** — [CloudEvents Specification 1.0.2][CE], CNCF CloudEvents, tagged release.
- **CE-HTTP** — [CloudEvents HTTP Protocol Binding 1.0.2][CE-HTTP], CNCF CloudEvents, tagged release.
- **CE-WEBHOOK** — [CloudEvents HTTP Webhook 1.0.2][CE-WEBHOOK], CNCF CloudEvents, tagged release.
- **HTTP-SIG** — [RFC 9421: HTTP Message Signatures][HTTP-SIG], IETF, February 2024.

[WS]: https://datatracker.ietf.org/doc/rfc6455/
[WS-H2]: https://datatracker.ietf.org/doc/rfc8441/
[WS-H3]: https://datatracker.ietf.org/doc/rfc9220/
[WS-COMP]: https://datatracker.ietf.org/doc/rfc7692/
[HTTP-TRANSITION]: https://datatracker.ietf.org/doc/rfc9931/
[SSE]: https://html.spec.whatwg.org/multipage/server-sent-events.html
[CE]: https://github.com/cloudevents/spec/tree/ce%40v1.0.2
[CE-HTTP]: https://github.com/cloudevents/spec/blob/ce%40v1.0.2/cloudevents/bindings/http-protocol-binding.md
[CE-WEBHOOK]: https://github.com/cloudevents/spec/blob/ce%40v1.0.2/cloudevents/http-webhook.md
[HTTP-SIG]: https://datatracker.ietf.org/doc/rfc9421/
