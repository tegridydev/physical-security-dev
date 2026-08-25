---
title: "MQTT event contract"
summary: "A synthetic MQTT event and validation contract for bounded, authenticated broker integrations."
page_type: development
domains:
  - integration
tags:
  - mqtt
  - events
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "MQTT Version 5.0"
coverage_limit: "Synthetic MQTT 5 event contract; broker topology, authorization, client behavior, extensions, and product limits require an environment profile."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# MQTT event contract

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / MQTT event contract

Input: synthetic JSON and documentation-only topic  
Side effects: none

## Topic and payload

Topic:

~~~text
security.example/site-a/camera/12/health
~~~

Payload:

~~~json
{
  "schema": "camera.health/1",
  "eventId": "evt-001",
  "source": "camera-12",
  "occurredAt": "2026-08-25T02:15:00Z",
  "sequence": 42,
  "state": "degraded"
}
~~~

## Contract decisions

- Broker authenticates a unique publisher identity and authorizes only the exact site/device topic hierarchy.
- Tenant/site/device scope is derived or cross-checked server-side, not trusted from payload alone.
- Payload is bounded, UTF-8 JSON and runtime-schema validated.
- Event identity, sequence and source time support duplicate/gap analysis but do not prove physical truth.
- QoS is chosen from the end-to-end processing need; QoS acknowledgement does not prove an operator or downstream system acted.
- Retained-message use is explicit because retained security state becomes broker-stored sensitive data.
- Session, expiry, will, replay, dead-letter and offline queue behavior are documented.
- TLS peer validation and client authorization remain enabled; no plaintext fallback exists.

## Payload validation profile

Before constructing a typed camera-health event, require an exact object shape; bounded strings; the supported schema identifier; a valid offset-bearing timestamp; a non-negative safe-integer sequence; and an allowlisted state. Reject duplicate JSON member names at the parser boundary. Cross-check the authenticated publisher and authorized topic against payload site/source fields, then apply duplicate/replay and sequence-gap policy. Static TypeScript types alone do not enforce any of these checks.

## Sources

- [OASIS MQTT Version 5.0](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html), accessed 2026-08-25.

## Related pages

- [MQTT](../../02-protocols/web-and-messaging/mqtt.md)
- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
