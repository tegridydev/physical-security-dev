---
title: "API and event security"
summary: "Secure command APIs, event streams, webhooks, brokers, and cross-system state synchronization."
page_type: security
domains:
  - integration
tags:
  - api-security
  - eventing
  - mqtt
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "OAuth 2.0 Security Best Current Practice, RFC 9700"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# API and event security

[Home](../README.md) / [Security and assurance](README.md) / API and event security

Physical-security integrations commonly mix commands, snapshots, configuration, telemetry, alarms, audit events, and identity data on one platform. Treat each as a separate capability with independent authorization, sensitivity, integrity, ordering, retention, and side-effect rules.

## Command contract

A state-changing API should define:

- authenticated subject and workload identity;
- explicit action and resource scope;
- preconditions and current state/version;
- request identifier and idempotency behavior;
- authorization decision and policy version;
- bounded timeout, retry rules, and uncertain-outcome handling;
- physical side effect and safe failure state;
- immutable audit correlation from request through device outcome;
- denial and partial-failure semantics.

Never retry a high-impact command blindly after timeout: the first request may have succeeded even if its response was lost. Query authoritative state or use a protocol-supported idempotency key before deciding.

## Event contract

An event envelope should carry stable type/version, source identity, event identity, occurrence time, observation/ingestion time, sequence where meaningful, site/tenant scope, subject/object identifiers, data classification, integrity context, and correlation/causation identifiers.

Consumers must define behavior for duplicate, delayed, missing, reordered, malformed, unauthorized, unknown-version, and replayed events. Delivery acknowledgement means the broker or receiver accepted a message; it does not prove the physical event occurred or that an operator acted on it.

## Broker and topic security

- Authenticate clients uniquely and authorize publish and subscribe separately.
- Keep tenant/site/device identifiers server-derived when possible.
- Prevent wildcard subscriptions from escaping the caller's authorized hierarchy.
- Review retained messages, durable sessions, shared subscriptions, dead-letter queues, and replay stores as data repositories.
- Bound payload size, inflight messages, session lifetime, queue depth, retry rate, and reconnect behavior.
- Encrypt the connection, validate peer identity, and avoid plaintext fallback.

## Webhooks and callbacks

Authenticate the sender with mTLS or a well-designed signature/token mechanism; validate timestamp/freshness and replay identifier; acknowledge only after durable acceptance; separate delivery retries from business processing; and do not follow arbitrary callback redirects. Apply outbound allowlists to prevent server-side request forgery.

## Data minimization

Avoid placing full card numbers, biometric data, faces, tokens, passwords, internal URLs, or unnecessary location context in events and logs. Use opaque stable identifiers with separately controlled lookup when the integration does not require raw sensitive data.

## Sources

- **RFC-9700** — [RFC 9700: Best Current Practice for OAuth 2.0 Security][RFC-9700], accessed 2026-08-25.
- **OWASP-API** — [OWASP API Security Top 10 2023][OWASP-API], implementation risk reference, accessed 2026-08-25.
- **NIST-800-92** — [NIST SP 800-92: Guide to Computer Security Log Management][NIST-800-92], accessed 2026-08-25.

[RFC-9700]: https://www.rfc-editor.org/rfc/rfc9700
[OWASP-API]: https://owasp.org/API-Security/editions/2023/en/0x11-t10/
[NIST-800-92]: https://csrc.nist.gov/pubs/sp/800/92/final

## Related pages

- [Identity, authentication, and authorization](identity-authentication-and-authorization.md)
- [Secure protocol parsing](secure-protocol-parsing.md)
- [Web and messaging protocols](../02-protocols/web-and-messaging/README.md)
