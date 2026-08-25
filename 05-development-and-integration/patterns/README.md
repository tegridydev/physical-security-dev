---
title: "Integration patterns"
summary: "Reusable patterns for protocol adapters, state, events, retries, backpressure, trust, and diagnostics."
page_type: index
domains:
  - development
tags:
  - patterns
  - architecture
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: "Protocol-neutral architecture patterns; exact guarantees and behavior come from selected standards, products, and deployment profiles."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Integration patterns

[Home](../../README.md) / [Development and integration](../README.md) / Patterns

| Page | Problem addressed |
|---|---|
| [Adapters, gateways, and translation](adapters-gateways-and-translation.md) | Isolate vendor/protocol variation from the domain model |
| [Polling, subscriptions, and state reconciliation](polling-subscriptions-and-state-reconciliation.md) | Combine snapshots and event streams without inventing state |
| [Retries, timeouts, and idempotency](retries-timeouts-and-idempotency.md) | Avoid duplicate or uncertain physical actions |
| [Event API contracts, normalization, and schema evolution](event-normalization-and-schema-evolution.md) | Preserve meaning, provenance and compatibility |
| [Reconnect, backpressure, and queues](reconnect-backpressure-and-queues.md) | Bound work during bursts, failure and recovery |
| [Secrets, certificates, and configuration](secrets-certificates-and-configuration.md) | Keep trust material outside code and lifecycle-safe |
| [Observability and diagnostics](observability-and-diagnostics.md) | Correlate device, protocol, integration and physical outcomes |

## Related pages

- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
