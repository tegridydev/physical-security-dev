---
title: "Web and messaging protocols"
summary: "Index for web APIs, XML services, event delivery, message brokers, RPC, and serialization in physical-security integrations."
page_type: index
domains: [cross-domain, networking]
tags:
  - http
  - rest
  - soap
  - websocket
  - mqtt
  - grpc
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: "Navigation and interaction-shape guidance only; no API, broker, parser, endpoint, or delivery behavior is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Web and messaging protocols

[Knowledge base](../../README.md) / Web and messaging protocols

This section covers the general-purpose transports and encodings used to connect access-control systems, video platforms, intercoms, intrusion systems, cloud services, and automation consumers. It focuses on developer-visible contracts and defensive integration behavior.

## Reading map

| Module | Use it for |
|---|---|
| [HTTP and REST](http-and-rest.md) | HTTP/1.1, HTTP/2, HTTP/3, resource modeling, retries, caching, authorization, and safe client behavior |
| [SOAP and XML](soap-and-xml.md) | SOAP envelopes, WSDL contracts, XML Schema, namespaces, faults, and hardened XML processing |
| [WebSocket, SSE, and webhooks](websocket-sse-and-webhooks.md) | Bidirectional sessions, server-to-browser streams, and server-to-server event callbacks |
| [MQTT](mqtt.md) | Brokered telemetry/events, sessions, QoS, retained state, topic design, and ACLs |
| [AMQP 1.0](amqp-1-0.md) | Brokered or peer messaging with links, credit, settlement, transactions, TLS, and SASL |
| [CoAP, OSCORE, and LwM2M](coap-oscore-and-lwm2m.md) | Constrained request/response, object security, observation, and device-management profiles |
| [CAP and EDXL emergency messaging](cap-and-edxl-emergency-messaging.md) | Public warning and emergency-information envelopes, lifecycle, profiles, and delivery boundaries |
| [gRPC and serialization](grpc-and-serialization.md) | Typed RPC, streaming, Protocol Buffers, JSON, and CBOR evolution and parser safety |

## Choose by interaction shape

| Need | Typical fit | Important caveat |
|---|---|---|
| Request/response resource API | HTTP with a documented REST-style contract | REST is an architectural style, not a wire standard or automatic security property |
| Contract-first XML operations | SOAP/WSDL | Harden every XML parser; schema validity is not authorization |
| Long-lived bidirectional messages | WebSocket | Define an application subprotocol, flow control, liveness, and reauthentication |
| One-way browser event stream | SSE | It is server-to-client only and reconnects automatically |
| Server-to-server event push | Webhook | Assume retries and duplicates; authenticate the message and constrain callback destinations |
| Many producers/consumers through a broker | MQTT | QoS does not make business side effects exactly once |
| Brokered queues, routing, and link settlement | AMQP 1.0 | Settlement is a messaging outcome, not proof of downstream physical handling |
| Constrained device request/observe | CoAP with an explicit security/profile design | A CoAP ACK is not proof of application or physical outcome |
| Typed internal RPC and streaming | gRPC | Deadlines, compatibility rules, and message-size bounds are part of the API contract |

## Cross-cutting contract

For every integration, document:

- protocol/version and transport security profile;
- endpoint and trust-boundary ownership;
- client/service identity, authentication, and per-operation authorization;
- schema version and compatibility rules;
- timeout, retry, idempotency, ordering, duplicate, and backpressure behavior;
- maximum request/message/field/depth/stream duration;
- timestamp, clock-skew, replay, correlation, and event-ID semantics;
- redaction, retention, audit, privacy, and incident behavior;
- degraded operation and recovery after network partition, credential rotation, or restart.

## Example and verification policy

Examples use synthetic identifiers, documentation domains, and RFC documentation addresses. Do not paste production credentials, tokens, certificates, device identifiers, or callback URLs into them. `V1` on this index denotes navigation review; child pages use `V2` for standards-based technical claims, while deployment evidence remains separately scoped.

## Related sections

- [Video and media protocols](../video-and-media/README.md)
- [Access-control protocols](../access-control/README.md)
