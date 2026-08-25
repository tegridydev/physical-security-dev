---
title: Foundations
summary: Shared architectural, networking, data, security, media, field-interface, and reliability concepts for physical-security development.
page_type: index
domains: [cross-domain]
tags: [foundations, architecture, networking, security]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Conceptual and implementation foundations; protocol-specific wire detail belongs in 02-protocols.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Foundations

These pages supply the stable concepts used throughout the protocol, system, development, security, and operations sections. Read them as a connected model: layers describe **where** behaviour occurs; actors and trust boundaries describe **who** controls it; data and state models describe **what** it means; failure semantics describe **what happens when certainty is lost**.

## Architecture and meaning

- [Architecture and layering](architecture-and-layering.md)
- [Physical-security system architecture](physical-security-system-architecture.md)
- [Interoperability, conformance, and profiles](interoperability-conformance-and-profiles.md)
- [Data models and semantics](data-models-and-semantics.md)
- [Events, state, commands, and time](events-state-commands-and-time.md)
- [Encoding and serialization](encoding-and-serialization.md)

## Networks, trust, and identity

- [Networking fundamentals](networking-fundamentals.md)
- [IP addressing, routing, and ports](ip-addressing-routing-and-ports.md)
- [Multicast, discovery, and NAT](multicast-discovery-and-nat.md)
- [Trust boundaries and segmentation](trust-boundaries-and-segmentation.md)
- [TLS, PKI, and certificates](tls-pki-and-certificates.md)
- [Identity, authentication, and authorization](identity-authentication-and-authorization.md)
- [Time synchronization](time-synchronization.md)

## Media, field, power, and credentials

- [Media streaming fundamentals](media-streaming-fundamentals.md)
- [Serial and field interfaces](serial-and-field-interfaces.md)
- [Dry contacts and supervised circuits](dry-contacts-and-supervised-circuits.md)
- [Ethernet, PoE, and power budgets](ethernet-poe-and-power-budgets.md)
- [Wireless and radio fundamentals](wireless-and-radio-fundamentals.md)
- [Credentials and identity media](credentials-and-identity-media.md)

## Building dependable integrations

- [Reliability and failure semantics](reliability-and-failure-semantics.md)
- [Observability and evidence](observability-and-evidence.md)
- [Secure integration lifecycle](secure-integration-lifecycle.md)

## Foundational rule

Never infer an end-to-end property from one layer. TLS can protect a connection while the endpoint is over-privileged; a valid credential can be presented by the wrong person; a delivered event can carry an incorrect source time; and a successful command acknowledgement can precede a failed physical action.

Return to [Start here](../00-start-here/README.md) or the [root index](../README.md).

