---
title: BACnet Secure Connect
summary: TLS, WebSocket, hub-and-node topology, PKI lifecycle, migration, and operational controls for BACnet/SC.
page_type: protocol
domains: [bms, cross-domain]
tags: [bacnet-sc, tls, websocket, pki, secure-connect]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ANSI/ASHRAE 135-2024, Addendum bj to ANSI/ASHRAE 135-2016]
coverage_limit: Normative message, certificate, and failover requirements remain in the licensed standard; product interoperability is implementation-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# BACnet Secure Connect

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [BACnet](bacnet-family.md) / Secure Connect

BACnet Secure Connect (BACnet/SC) is a BACnet data link that uses WebSockets over TLS and supports IPv4 and IPv6. It replaces broadcast distribution at this data link with logical hub-and-node communication while preserving BACnet network and application services.[^sc] The design entered the standard through Addendum `bj` to ANSI/ASHRAE 135-2016 and is incorporated into later consolidated editions.[^bj]

## Topology

```text
SC node ── mutually authenticated TLS/WebSocket ── primary hub
   │                                                   │
   └──────── optional direct connection ───────────────┤
                                                       └── failover hub / routed BACnet networks
```

Every deployment needs explicit hub ownership, node enrolment, connection initiation rules, failover behaviour, supported direct connections, BACnet network numbering, and capacity limits. A reachable WebSocket endpoint is not automatically an approved BACnet/SC peer.

## Certificate lifecycle

- Issue unique node/hub certificates from project-controlled trust anchors; protect private keys against export.
- Bind the certificate identity to an approved BACnet device and role. Discovery, DNS, and IP address are not identity proof.
- Define validity, time-source, chain-building, revocation, renewal, emergency replacement, trust-anchor rollover, and decommissioning procedures.
- Validate the exact identity rules required by the standard and product; do not disable hostname/identity checks to “make TLS work.”
- Audit enrolment, certificate and trust-store changes, failed handshakes, unexpected issuers, reconnect storms, hub failover, and topology changes.

Use current TLS policy and protect the certificate-management plane separately. Review [TLS and PKI](../infrastructure/tls-pki-and-secure-transport.md) without replacing BACnet/SC-specific certificate rules with generic HTTPS defaults.

## Migration and residual risk

A BACnet/SC router connected to BACnet/IP or MS/TP terminates the secure data link; downstream traffic may again be unauthenticated and cleartext. Document each boundary and constrain which networks, services, objects, and writes may cross it. Avoid transparent “secure overlay” claims.

BACnet/SC provides secure transport and peer authentication. It does not by itself decide whether a peer may command a particular property, guarantee correct priority-array use, secure a device's web/SSH interface, or make bad control logic safe. Retain application authorization and safety gates from [BACnet family](bacnet-family.md).

Validate TLS policy, hub failover, certificate rotation, revocation, clock faults, and vendor interoperability in the controlled target environment.

## Primary sources

[^sc]: [BACnet International — BACnet Secure Connect](https://bacnetinternational.org/bacnetsc/)
[^bj]: [ASHRAE — published addenda to Standard 135-2016](https://www.ashrae.org/technical-resources/standards-and-guidelines/standards-addenda/standard-135-2016-bacnet-a-data-communication-protocol-for-building-automation-and-control-networks)
- [ASHRAE BACnet Committee — standard status](https://bacnet.org/updates/)
