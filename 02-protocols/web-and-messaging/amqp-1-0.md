---
title: "AMQP 1.0 messaging"
summary: "Architecture and security guidance for AMQP 1.0 connections, sessions, links, delivery settlement, flow control, and physical-security event integration."
page_type: protocol
domains: [cross-domain, networking, integration]
tags:
  - amqp
  - messaging
  - queues
  - events
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "OASIS AMQP Version 1.0"
  - "ISO/IEC 19464:2014"
coverage_limit: "AMQP 1.0 protocol and integration guidance; broker extensions, address syntax, topology, failover, authorization, and delivery guarantees remain product- and deployment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# AMQP 1.0 messaging

[Home](../../README.md) / [Protocols](../README.md) / [Web and messaging](README.md) / AMQP 1.0

AMQP 1.0 is a standardized binary messaging protocol. It defines interoperable peers, connections, sessions, links, message sections, flow control, delivery state, settlement, transactions, and security layers. It does not prescribe a universal broker topology, address language, management API, event schema, or physical-security outcome model. [AMQP] [AMQP-OVERVIEW]

## Version boundary

Treat the version number as part of the wire contract.

| Name | Relationship to AMQP 1.0 | Integration consequence |
|---|---|---|
| AMQP 1.0 | OASIS Standard and ISO/IEC 19464:2014, confirmed current in 2025 | Use the AMQP 1.0 type system, performatives, link model, and settlement rules. [AMQP-ISO] |
| AMQP 0-9-1 and earlier | Earlier protocol family with different framing and broker concepts | Not wire-compatible with AMQP 1.0; a product supporting one does not necessarily support the other |
| Vendor messaging API | Client-library or service abstraction | May hide or constrain link credit, settlement, transactions, address syntax, or failover behavior |
| AsyncAPI `amqp` / `amqp1` binding | Interface-description binding selected by the contract | Confirm that the binding and broker actually refer to the same AMQP protocol family and product profile |

Do not infer AMQP 1.0 support from the presence of an “AMQP” checkbox, port, URI, or client-library name. Record the negotiated protocol version and the exact product profile.

## Protocol model

```text
container
  -> connection
      -> session
          -> sender link -> node
          <- receiver link <- node
```

- A **container** is an AMQP node-hosting or messaging process with a stable identity in its deployment context.
- A **connection** is the long-lived AMQP relationship carried by a transport.
- A **session** multiplexes ordered transfer work over a connection and has its own flow windows.
- A **link** is a unidirectional sender-to-receiver path. Bidirectional application exchange uses multiple links.
- A **node** is an addressable source or target, such as a queue, topic-like endpoint, or service-defined terminus.
- A **delivery** is one message transfer tracked for outcome and settlement; a large message can span multiple transfer frames.

Broker products add queues, exchanges, subscriptions, filters, dead-lettering, retention, and administration models. Those names and semantics are not automatically portable merely because the wire protocol is AMQP 1.0.

## Messages and domain contracts

An AMQP message can carry header, delivery annotations, message annotations, properties, application properties, body, and footer sections. Define which sections an application may set and which only trusted infrastructure may add.

For a physical-security event profile, define at least:

- media type and schema identifier/version;
- event identity, native source identity, tenant/site, occurrence time, receive time, and clock quality;
- correlation and causation identifiers;
- canonical and native event types without erasing source meaning;
- sensitivity, retention, ordering key, expiry, and replay treatment;
- maximum encoded and decoded size, collection counts, and nesting depth;
- behavior for unknown fields, unknown event types, invalid timestamps, and duplicate identifiers.

AMQP application properties are not a trusted identity channel by default. A publisher can often set them. Establish authenticated publisher identity at the connection/link layer and apply authorization independently of asserted tenant, site, device, role, or user fields.

## Delivery state and settlement

AMQP distinguishes transfer from delivery outcome and settlement. Common terminal outcomes include `accepted`, `rejected`, `released`, and `modified`; unsettled deliveries may require state reconciliation after interruption. [AMQP-TRANSPORT]

| Observation | What it establishes | What it does not establish |
|---|---|---|
| Transfer frame sent | Bytes were offered on a link | Peer received or retained them |
| Delivery accepted | Receiving AMQP endpoint accepted responsibility under its link contract | Consumer processed the event, case was created, or physical state changed |
| Delivery rejected | Receiver supplied a negative AMQP outcome | Whether a separate prior attempt had an effect |
| Delivery released/modified | Delivery is available for redelivery under defined conditions | Exactly-once application processing |
| Consumer acknowledgement through a broker API | Consumer reached an API-defined point | Downstream transaction or physical outcome unless the application contract says so |

Settlement mode changes who tracks an unsettled delivery and when. “At most once,” “at least once,” or stronger application claims require an end-to-end profile covering producer persistence, broker durability, consumer transaction boundaries, deduplication, recovery, and expiry—not just a link setting.

Use a scoped immutable event or operation ID for deduplication. Bind it to authenticated producer, tenant, target, operation type, and request fingerprint; retain deduplication state for the full retry/replay window.

## Flow control and resource bounds

AMQP link credit tells a sender how many deliveries a receiver is prepared to accept. Sessions also use incoming and outgoing windows. Credit is protocol backpressure, not a complete capacity policy.

- Grant credit according to bounded queue count, bytes, processing latency, and downstream health.
- Bound frame size, message bytes before and after decompression, section counts, map/list entries, symbol/string/binary lengths, link/session count, unsettled deliveries, and idle lifetime.
- Reduce or stop credit before memory or durable storage is exhausted.
- Monitor queue age and oldest event, not only message count.
- Define expiry and dead-letter/quarantine handling; never silently discard a safety-relevant alarm because a generic time-to-live elapsed.
- Keep priority bounded and governed so one noisy publisher cannot starve restoration, health, or audit traffic.

Transport flow control cannot prevent a fast consumer from overwhelming a database, rules engine, case platform, or physical-security adapter after it accepts a delivery.

## Addressing, filters, and topology

The AMQP base specification does not provide one universal address syntax. Broker URLs, virtual hosts, dynamic nodes, durable subscriptions, shared subscriptions, selectors, wildcard rules, and dead-letter targets are commonly product-defined or supplied by extension specifications.

Document:

1. source and target address syntax, normalization, and tenant boundary;
2. who may create, delete, bind, browse, or consume from a node;
3. durable versus temporary lifetime and expiry behavior;
4. competing-consumer and ordering behavior;
5. filter language, validation, complexity limits, and unsupported-field behavior;
6. disaster-recovery topology and duplicate/loss window;
7. whether replay uses the production address or an isolated replay path.

Never place credentials, bearer tokens, personal identifiers, or sensitive site details in a URI that may enter logs or diagnostics.

## Authentication, transport security, and authorization

AMQP 1.0 defines SASL and TLS-related protocol layers, but a deployment still has to choose and enforce a security profile. [AMQP-SECURITY]

- Require a protected transport across untrusted networks; validate server identity and trust path.
- Where mutual TLS is used, map the authenticated certificate identity to a narrowly scoped messaging principal; possession of a certificate does not authorize every address.
- Allowlist SASL mechanisms appropriate to the protected transport and credential type. Reject silent downgrade to anonymous or cleartext password mechanisms.
- Separate publish, consume, browse, manage, and dynamic-node permissions by tenant/site and address.
- Reauthorize link attachment and dynamic-node creation; connection authentication alone is insufficient.
- Rotate credentials and trust anchors without requiring a fail-open window.
- Protect broker management, metrics, tracing, schema registries, and dead-letter stores as separate surfaces.

The registered ports commonly associated with AMQP are `5672/TCP` and `5671/TCP`, but a port number neither proves protocol identity nor guarantees TLS. Use an explicit URI/profile and confirm negotiation. [IANA-PORTS]

## Reconnect, failover, and replay

AMQP describes protocol state; product-specific clients often add reconnect and failover behavior. Make that behavior visible in the integration contract.

- Use backoff, jitter, a retry budget, and a total recovery deadline.
- Distinguish DNS/connect/TLS/SASL/open/session/link/attach failures in telemetry.
- Treat an interrupted unsettled delivery as uncertain until state is reconciled or safely deduplicated.
- Do not reset sequence or deduplication state merely because the TCP connection changed.
- Define whether alternate endpoints share durable state or are independent brokers.
- Bound offline spooling by count, bytes, age, sensitivity, and encryption-at-rest requirements.
- Quarantine incompatible schema versions instead of repeatedly redelivering them into a hot loop.

## Transactions and physical actions

AMQP transactions can coordinate AMQP resource operations within the supported transaction model. They do not create an atomic transaction with a PACS controller, door contact, video recorder, dispatch process, or emergency communication system.

For high-impact requests, keep separate states such as:

```text
created -> authorized -> published -> AMQP accepted
        -> adapter accepted -> downstream dispatched
        -> target acknowledged -> observed outcome | failed | uncertain
```

Require fresh authorization and an operation-specific policy at the adapter. Do not let a generic event consumer translate arbitrary message fields into unlock, lockdown, relay, alarm-reset, camera-control, or notification actions.

## Observability and evidence

Record the AMQP endpoint identity, authenticated principal, connection/session/link identifiers where useful, source/target address, delivery tag in bounded form, settlement outcome, redelivery indicator, schema/mapping version, retry count, queue age, correlation ID, and downstream outcome. Avoid logging bodies or application properties wholesale.

Useful measures include connection and authentication failures, link attach denials, credit exhaustion, unsettled count, accepted/rejected/released deliveries, redelivery, expired/quarantined messages, queue bytes/age, parser failures, tenant-policy denials, and end-to-end freshness.

## Review checklist

- [ ] AMQP 1.0 distinguished from AMQP 0-9-1 and vendor APIs
- [ ] Exact broker/client versions, URI profile, SASL mechanisms, TLS policy, and endpoint identity documented
- [ ] Address syntax, node lifetime, topology, ordering, filtering, and failover behavior pinned
- [ ] Publish/consume/manage authorization isolated by tenant, site, and address
- [ ] Frame, message, decompression, collection, link, session, queue, and spool limits enforced
- [ ] Link credit connected to bounded downstream capacity
- [ ] Settlement and recovery semantics mapped to application deduplication and transactions
- [ ] Schema evolution, provenance, invalid-event quarantine, expiry, and replay defined
- [ ] AMQP acceptance kept distinct from consumer, workflow, and physical outcomes
- [ ] High-impact subscribers use a separate authorization and safety boundary

## Sources

- **AMQP** — [AMQP Version 1.0 OASIS Standard][AMQP], OASIS, October 2012.
- **AMQP-ISO** — [ISO/IEC 19464:2014: Advanced Message Queuing Protocol (AMQP) v1.0 specification][AMQP-ISO], ISO/IEC; last reviewed and confirmed in 2025.
- **AMQP-OVERVIEW** — [AMQP Version 1.0, Part 0: Overview][AMQP-OVERVIEW], OASIS.
- **AMQP-TRANSPORT** — [AMQP Version 1.0, Part 2: Transport][AMQP-TRANSPORT], OASIS.
- **AMQP-MESSAGING** — [AMQP Version 1.0, Part 3: Messaging][AMQP-MESSAGING], OASIS.
- **AMQP-SECURITY** — [AMQP Version 1.0, Part 5: Security][AMQP-SECURITY], OASIS.
- **IANA-PORTS** — [Service Name and Transport Protocol Port Number Registry][IANA-PORTS], IANA, `amqp` and `amqps` entries, accessed 2026-08-25.

[AMQP]: https://www.oasis-open.org/standard/amqp/
[AMQP-ISO]: https://www.iso.org/standard/64955.html
[AMQP-OVERVIEW]: https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-overview-v1.0-os.html
[AMQP-TRANSPORT]: https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-transport-v1.0-os.html
[AMQP-MESSAGING]: https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-messaging-v1.0-os.html
[AMQP-SECURITY]: https://docs.oasis-open.org/amqp/core/v1.0/os/amqp-core-security-v1.0-os.html
[IANA-PORTS]: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
