---
title: "MQTT 5.0, MQTT 3.1.1, and Sparkplug 3.0"
summary: "Developer reference for MQTT connections, sessions, topics, QoS, retained messages, wills, Sparkplug state, broker authorization, and reliable security-event processing."
page_type: protocol
domains: [cross-domain, networking]
tags:
  - mqtt
  - broker
  - pubsub
  - mqtls
  - sparkplug
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "MQTT Version 5.0, OASIS Standard, 7 March 2019"
  - "MQTT Version 3.1.1, OASIS Standard, 29 October 2014 / ISO/IEC 20922:2016"
  - "Eclipse Sparkplug Specification 3.0"
coverage_limit: "MQTT protocol, Sparkplug 3.0 application-profile semantics, and defensive broker/application design only; product interoperability, broker/client behavior, security controls, commands, persistence, and failover require separate evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# MQTT 5.0, MQTT 3.1.1, and Sparkplug 3.0

[Web and messaging protocols](README.md) / MQTT

MQTT is a lightweight brokered publish/subscribe protocol. Version 5.0 is the current OASIS Standard and supersedes MQTT 3.1.1, but both remain deployed. A client and broker must agree the protocol level; v5 properties and reason codes cannot simply be sent to a 3.1.1 endpoint. [MQTT5] [MQTT311]

## Architecture

```text
publisher ---- PUBLISH ----> broker ---- PUBLISH ----> subscriber
                         topic matching
                         session state
                         retained messages
                         access control
                         inflight QoS state
```

The broker is a high-value trust boundary: it authenticates clients, authorizes topic actions, stores transient/persistent state, routes events, and may retain sensitive payloads.

## Version comparison

| Capability | MQTT 3.1.1 | MQTT 5.0 |
|---|---|---|
| Connection result detail | Limited CONNACK codes | Rich reason codes and reason strings |
| Session lifecycle | Clean Session flag | Clean Start plus Session Expiry Interval |
| Message expiry | No base property | Message Expiry Interval |
| Metadata | Topic/payload plus fixed fields | User Properties, Content Type, Payload Format Indicator, Response Topic, Correlation Data |
| Server guidance | Limited | Server Reference, Receive Maximum, Maximum Packet Size, Topic Alias limits |
| Enhanced authentication | Not in base | AUTH exchange and authentication method/data |
| Subscription features | Basic filters/QoS | Subscription identifiers, no-local, retain handling/as-published |

Do not expose v5 Reason String or User Property content from an untrusted peer directly in logs/UI without length and content controls.

## Connection lifecycle

1. Establish the approved transport, normally TLS for remote or shared networks.
2. Client sends `CONNECT` with protocol version, client ID, session settings, authentication, keepalive, and optional Will.
3. Broker authenticates, authorizes connection parameters, resolves existing session state, and sends `CONNACK`.
4. Client subscribes and/or publishes within ACLs and negotiated limits.
5. Keepalive and network I/O prove connection liveness, not application health.
6. Clean `DISCONNECT` or ungraceful loss ends the network connection; session and Will behavior follows negotiated state.

Use unique, stable client IDs when resuming sessions. Two devices using the same client ID can displace one another and confuse inflight/deduplication state.

## QoS semantics

| QoS | Protocol delivery objective | Application consequence |
|---|---|---|
| 0 | At most once | No acknowledgment; loss possible |
| 1 | At least once | Retransmission can deliver duplicates |
| 2 | Exactly once between one MQTT sender and one receiver through the QoS handshake | Does not make database, webhook, relay, or other downstream side effects exactly once |

QoS is negotiated per delivery path. A publisher's QoS and a subscription's granted QoS determine the outgoing delivery QoS. Session loss, bridge behavior, application restart, and writes outside the MQTT state machine can still duplicate or lose business effects.

Consumers should use a domain event ID, transaction, and idempotent state transition. MQTT Packet Identifier is scoped protocol state and is not a permanent domain-event identifier.

## Sessions and inflight state

- In v5, separate Clean Start from Session Expiry; document both client and broker limits.
- Persist subscription and inflight QoS state only as long as required.
- Bound queued messages per client, inflight count, expiry, and bytes; use a defined overflow policy.
- Reconcile after session loss rather than assuming a durable session existed.
- Test reconnect backoff and staggered startup to avoid a fleet reconnect storm.

## Retained messages

A retained PUBLISH is the broker's last retained value for a topic, delivered to later matching subscriptions according to retain rules. It is not an event log and can outlive the producing connection.

- Use retained state only for explicit current-state topics.
- Include observation time, source, quality, and schema version.
- Define how retained state is cleared and who may clear it.
- Protect retained payloads at rest and through topic ACLs.
- Do not retain transient alarms or commands unless the domain model explicitly requires it.
- A stale retained “unlocked” or “online” value must not be interpreted as a current physical observation.

## Will messages

The Will can publish when a connection ends without a normal disconnect under the protocol rules. It indicates broker/client-connection failure context, not necessarily device power loss or physical tampering. Use a delayed Will in v5 where appropriate to avoid false offline events during brief reconnects, and reconcile with a fresh birth/online state.

## Sparkplug 3.0 application profile

Eclipse Sparkplug 3.0 is an **application profile built on MQTT**, not another MQTT protocol version. It adds a topic namespace, state-management conventions, a Protocol Buffers payload, metric types/aliases, and roles for edge nodes, devices, and host applications. An implementation must pin both the Sparkplug specification and the MQTT protocol level supported by every product; “Sparkplug 3.0” does not mean “MQTT 3.0.” [SPARKPLUG] [SPARKPLUG30]

The Sparkplug topic structure has this conceptual shape:

```text
namespace / group_id / message_type / edge_node_id / optional_device_id
```

The namespace used by the current specification can contain `spBv1.0`; that namespace label is part of the Sparkplug wire convention and is not the edition number of the Sparkplug specification or the negotiated MQTT protocol level. Preserve identifiers exactly and validate each segment for allowed length and characters. Treat group, edge-node, and device identifiers as routing claims until they are bound to the authenticated MQTT client by broker policy.

Sparkplug host `STATE` coordination uses its own specification-defined topic form. Do not force that control-plane state into the ordinary edge-node/device grammar or grant it through an overly broad wildcard.

### Birth, data, command, and death messages

Sparkplug message types distinguish edge-node and device lifecycle and traffic, including:

| Message family | Intended meaning | Boundary to preserve |
|---|---|---|
| `NBIRTH` / `DBIRTH` | Establishes the edge-node/device metric set and session context | A birth certificate is application-session state, not proof of physical installation or health |
| `NDATA` / `DDATA` | Reports metric values after birth | Each metric still needs timestamp, quality, range, source, and stale-state policy |
| `NCMD` / `DCMD` | Carries command intent to an edge node/device | Broker delivery or payload acceptance is not authorization or physical completion |
| `NDEATH` / `DDEATH` | Signals loss/end of the applicable Sparkplug session under defined behavior | Death does not by itself prove power loss, tamper, equipment failure, or physical state |

An edge node's death certificate is normally connected to MQTT Will behavior so the broker can publish it after an ungraceful session loss. Network partition, broker failover, client takeover, queueing, reconnect timing, and stale retained state can all affect what an application observes. Reconcile a new birth, sequence/session state, complete metric definition, and authoritative device observations before declaring recovery.

Metric aliases and sequence values are scoped by the Sparkplug session rules. Do not persist an alias as a permanent fleet identifier or deduplicate domain events solely with an 8-bit/session-scoped sequence. A consumer that misses a birth or detects a sequence gap should surface incomplete context and follow the specified rebirth/recovery behavior rather than guessing the metric definition.

### Sparkplug state is not physical state

Sparkplug birth/death and host-state conventions coordinate MQTT application availability. They do not establish that:

- a contact, lock, gate, camera, sensor, PLC, or bridged device is physically healthy;
- a metric is current, calibrated, unsuppressed, and sourced from the claimed point;
- a command passed domain authorization or reached an actuator;
- a recorder committed media or an alarm reached an operator;
- an MQTT session is the only valid path controlling the equipment.

Model at least connection/session state, edge-node application state, device communication state, metric quality/freshness, command workflow state, and authoritative physical state separately. A fresh `NBIRTH` can coexist with stale downstream devices; an `NDEATH` can coexist with equipment continuing local autonomous operation.

### Sparkplug security and tenancy

Sparkplug does not replace MQTT transport security or broker authorization. Apply TLS and client identity, then bind each authenticated client to the exact Sparkplug group, edge-node/device IDs, and permitted message types. In particular:

- only the owning edge identity may publish its birth, data, and death topics;
- host/application identities receive only authorized groups and issue commands only to allowed nodes/devices;
- retained-message permissions and Will registration must prevent fabrication of another node's lifecycle state;
- primary/host-state behavior, failover, and split-brain handling must be explicit for the selected implementation;
- protobuf payload size, metric count, property nesting, strings/bytes, dataset dimensions, and decompression/allocation work must be bounded;
- credentials and personal/operational data must not be embedded in topic identifiers or metric names.

## Topic design

The following synthetic topic convention illustrates versioned, tenant-scoped names without using a real endpoint or identifier:

```text
physical-security-dev/v1/tenants/tenant_demo/sites/site_demo_01/doors/door_demo_01/state
physical-security-dev/v1/tenants/tenant_demo/sites/site_demo_01/controllers/controller_demo_01/health
```

Recommended rules:

- put version and stable resource IDs in the topic; human names belong in payload/metadata;
- keep secrets, personal data, credential numbers, tokens, and access decisions out of topic names because brokers log/index topics widely;
- distinguish event, current-state, command, command-result, and health namespaces;
- document case sensitivity, Unicode normalization policy, maximum levels/length, and allowed characters;
- authorize exact publish and subscribe filters separately;
- treat `+` and `#` wildcard subscriptions as privileged and constrain `$`/broker-management namespaces;
- review shared subscriptions (`$share/{group}/{filter}`) as competing-consumer semantics, not broadcast.

## Payload contract

MQTT transports bytes. Define media type/encoding, schema/version, event ID, source, subject, occurrence/observation times, sequence scope, tenant, quality, and compatibility. In v5, Content Type and Payload Format Indicator can assist but are untrusted claims.

Cap MQTT packet and decoded payload size, nesting, collection length, compression ratio, string length, and processing time. Validate before authorization-dependent routing or side effects.

## Security profile

### Transport and identity

- Prefer MQTT over TLS with server certificate validation; use mutual TLS or a modern scoped credential scheme when suitable.
- Ports 1883 (MQTT) and 8883 (secure MQTT) are IANA-registered conventions, not proof that TLS or plaintext is actually present. [IANA-PORTS]
- Give each device/application a unique credential and client identity; rotate/revoke independently.
- Disable anonymous access and sample/default accounts.
- Constrain source networks and broker listeners; isolate management APIs and cluster traffic.

### Authorization

- Enforce least-privilege ACLs for connect, publish, subscribe, retained write/clear, and management separately.
- Bind tenant/site/device identity from authenticated context, not a client-chosen topic segment alone.
- Prevent a device from publishing another device's health/state or subscribing to unrelated tenant events.
- Make command topics especially narrow; include command ID, expiry, intended target, issuer, and result topic under a signed/authorized application contract.
- Never treat broker receipt of an unlock command as physical completion.

### Broker resilience

- Enforce maximum packet, receive maximum, connections, subscriptions, wildcard breadth, queued bytes, retained count/size, inflight state, message rate, and auth attempts.
- Apply per-client/tenant quotas before shared resource exhaustion.
- Protect persistence, backups, cluster links, bridge credentials, plugins, and administrative interfaces.
- Validate extension/plugin behavior against v3.1.1 and v5 parser differences.

## ONVIF context

ONVIF Profile M includes MQTT event delivery as a conditional capability. ONVIF Profile V was a release candidate on the verification date and describes MQTTS JSON event uplink. Neither claim means any arbitrary MQTT topic/schema is ONVIF interoperable; follow the applicable ONVIF service/profile definitions and device capability advertisement. [ONVIF-M] [ONVIF-V]

## Review checklist

- [ ] Protocol version and transport/TLS listener explicit
- [ ] Unique client identity and credential lifecycle defined
- [ ] Session expiry, clean start, inflight, queue, and reconnect behavior documented
- [ ] QoS mapped honestly to application duplicate/loss behavior
- [ ] Topic hierarchy/version and wildcard/shared-subscription rules reviewed
- [ ] Sparkplug edition, MQTT protocol level, namespace, roles, topic ownership, and payload limits pinned where used
- [ ] Sparkplug birth/death, sequence, aliases, rebirth, host failover, and stale-state behavior cannot masquerade as physical state
- [ ] Publish/subscribe/retained/management ACLs bound to authenticated identity
- [ ] Retained and Will semantics cannot masquerade as fresh physical state
- [ ] Packet, payload, rate, subscription, queue, and persistence limits set
- [ ] Event IDs and side effects idempotent
- [ ] Broker, bridge, plugin, persistence, backup, and admin-plane security included

## Sources

- **MQTT5** — [MQTT Version 5.0][MQTT5], OASIS Standard, 7 March 2019.
- **MQTT311** — [MQTT Version 3.1.1][MQTT311], OASIS Standard, 29 October 2014; also published as ISO/IEC 20922:2016.
- **IANA-PORTS** — [Service Name and Transport Protocol Port Number Registry][IANA-PORTS], IANA, entries for `mqtt` and `secure-mqtt`, accessed 2026-08-25.
- **TLS13** — [RFC 8446: TLS 1.3][TLS13], IETF, August 2018.
- **SPARKPLUG** — [Eclipse Sparkplug specification][SPARKPLUG], Eclipse Foundation, accessed 2026-08-25.
- **SPARKPLUG30** — [Eclipse Sparkplug Specification 3.0][SPARKPLUG30], Eclipse Foundation, accessed 2026-08-25.
- **ONVIF-M** — [Profile M][ONVIF-M], ONVIF, accessed 2026-08-25.
- **ONVIF-V** — [Profile V][ONVIF-V], ONVIF, release candidate dated 2026-07-09.

[MQTT5]: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
[MQTT311]: https://docs.oasis-open.org/mqtt/mqtt/v3.1.1/mqtt-v3.1.1.html
[IANA-PORTS]: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
[TLS13]: https://datatracker.ietf.org/doc/rfc8446/
[SPARKPLUG]: https://sparkplug.eclipse.org/specification/
[SPARKPLUG30]: https://sparkplug.eclipse.org/specification/version/3.0/
[ONVIF-M]: https://www.onvif.org/profiles/profile-m/
[ONVIF-V]: https://www.onvif.org/profiles/profile-v/
