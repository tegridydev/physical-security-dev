---
title: OPC Unified Architecture
summary: OPC UA information modelling, client/server and PubSub patterns, sessions, security policies, authorization, and safe integration.
page_type: protocol
domains: [ot, bms, cross-domain]
tags: [opc-ua, iec-62541, information-model, pubsub, secure-channel]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [IEC 62541, OPC 10000 multi-part 1.05 line]
coverage_limit: Companion specifications, product profiles, namespace versions, and the applicable OPC Foundation conformance units are required for a concrete integration.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# OPC Unified Architecture

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / OPC UA

OPC UA is a platform-independent architecture for typed information models, discovery, client/server services, subscriptions, methods, events, and Publish-Subscribe communication. It is a versioned multi-part family, not a monolithic “1.05.06” specification. At this review, Part 1 (Overview and Concepts), Part 2 (Security Model), and several other parts are 1.05.06, while Parts 4, 6, 8, 12, 13, 17, and 26 are 1.05.07; other parts retain still different patch levels.[^index][^part1] Record each required Part and companion specification independently.

## Model before transport

A durable client binds to namespace URI plus NodeId and validates the node class, DataType, ValueRank, engineering units, access level, modelling rule, and companion-specification version. Namespace indexes are server-session assignments and can change; never persist an index as global identity. Browse/display names are human-facing and not stable identifiers.

Every value should preserve StatusCode and source/server timestamps. Do not convert `Bad`, `Uncertain`, stale, or missing data into a normal value. For subscriptions, define sampling interval, publishing interval, queue size, discard policy, lifetime, keepalive, reconnect transfer/recreation behaviour, and how data gaps are surfaced.

Methods and writes are commands. Validate argument types and semantic preconditions, apply least privilege, use idempotency/correlation where the model supports it, and obtain completion state from the authoritative node/event rather than the transport result alone.

## Security layers

OPC UA separates SecureChannel protection, application instance identity, Session, and user identity/authorization. Select an approved endpoint, MessageSecurityMode, SecurityPolicy, application certificate, and user-token policy as a coherent set. `None` modes/policies are for explicitly isolated commissioning or diagnostics—not an acceptable production default when protected profiles are available.[^security]

- Maintain a deliberate application trust list; do not auto-trust every certificate returned by discovery.
- Validate chains, identity/application URI rules, key usage, validity, revocation policy, and algorithm strength as required by the selected profile.
- Map users/service identities to roles and authorize nodes, attributes, methods, and subscriptions; an authenticated application is not automatically an authorized operator.
- Separate discovery from trust, and expose only intended endpoints and profiles.
- Plan certificate renewal and trust-list rollover without disabling validation or sharing private keys.

## PubSub

OPC UA PubSub has its own publisher/writer and subscriber/reader configuration, transport mappings, message security, key distribution, dataset metadata, sequencing, and discovery considerations.[^pubsub] Do not apply client/server Session assumptions to PubSub. Bind publisher identity, DataSetWriterId, schema/configuration version, field types, security group, key lifetime, and stale/sequence rules explicitly.

## Safety boundary

An OPC UA server may front PLC, BMS, access-control, or energy controls. Discovery and browsing can expose a rich operational model; broad subscriptions can exhaust server resources. Use product capability statements, companion specifications, and an authorized non-production validation environment before integrating a live endpoint.

## Primary sources

[^index]: [OPC Foundation — OPC UA Online Reference](https://reference.opcfoundation.org/)
[^part1]: [OPC Foundation — OPC 10000-1 v1.05.06](https://reference.opcfoundation.org/specs/OPC-10000-1/v1.05.06)
[^security]: [OPC Foundation — OPC UA Part 2, security model](https://reference.opcfoundation.org/specs/OPC-10000-2/full)
[^pubsub]: [OPC Foundation — OPC UA Part 14, PubSub](https://reference.opcfoundation.org/specs/OPC-10000-14/v1.05.06)
- [OPC Foundation — security profiles](https://reference.opcfoundation.org/specs/OPC-10000-2/4.7)
