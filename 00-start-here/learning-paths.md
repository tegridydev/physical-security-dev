---
title: Learning Paths
summary: Role- and goal-based routes through the physical-security knowledge base.
page_type: guide
domains: [cross-domain]
tags: [learning, roadmap, onboarding]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Suggested sequencing, not a competency or certification framework.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Learning paths

Do not try to memorize the protocol catalogue. Learn the shared models first, then one end-to-end workflow at a time.

## New physical-security developer

1. [Architecture and layering](../01-foundations/architecture-and-layering.md)
2. [Physical-security system architecture](../01-foundations/physical-security-system-architecture.md)
3. [Networking fundamentals](../01-foundations/networking-fundamentals.md)
4. [Events, state, commands, and time](../01-foundations/events-state-commands-and-time.md)
5. [Identity, authentication, and authorization](../01-foundations/identity-authentication-and-authorization.md)
6. [Protocol landscape](../physical-security-protocol-landscape.md)

Outcome: explain a flow from field device to client, name every layer, and distinguish observation from command.

## Video and VMS integration

Start with [media fundamentals](../01-foundations/media-streaming-fundamentals.md), [multicast and discovery](../01-foundations/multicast-discovery-and-nat.md), and [time synchronization](../01-foundations/time-synchronization.md). Then study [ONVIF](../02-protocols/video-and-media/onvif.md), [RTSP/RTP/RTCP/SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md), [WebRTC](../02-protocols/video-and-media/webrtc.md), [HTTP](../02-protocols/web-and-messaging/http-and-rest.md), and the [relevant vendor API](../04-vendor-apis/README.md). Add [GB/T 28181](../02-protocols/video-and-media/gbt-28181.md) for applicable Chinese deployments and [SRT/RIST](../02-protocols/video-and-media/srt-and-rist.md) only for contribution-network requirements. Finish with [event normalization](../05-development-and-integration/patterns/event-normalization-and-schema-evolution.md), reconnect, bounded buffering, certificate validation, and evidence integrity.

Outcome: trace control, media, metadata, events, and authentication as separate but correlated flows.

## Access-control integration

Read [credentials and identity media](../01-foundations/credentials-and-identity-media.md), [serial and field interfaces](../01-foundations/serial-and-field-interfaces.md), [dry contacts and supervised circuits](../01-foundations/dry-contacts-and-supervised-circuits.md), and [failure semantics](../01-foundations/reliability-and-failure-semantics.md). Then study [OSDP](../02-protocols/access-control/osdp.md), [legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md), [contactless/smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md), [mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md), [pedestrian portals](../03-systems/access-control/pedestrian-portals-turnstiles-and-interlocked-doors.md), and [PACS APIs](../04-vendor-apis/access-and-identity/README.md). Use [federation](../02-protocols/infrastructure/enterprise-federation-saml-and-oidc.md), [SCIM](../02-protocols/infrastructure/scim-identity-provisioning.md), and [WebAuthn/FIDO](../02-protocols/infrastructure/webauthn-fido-and-passkeys.md) where enterprise identity crosses into PACS administration.

Outcome: distinguish credential identifier, authentication factor, access decision, door state, and audit event—and identify which component is authoritative for each.

## Alarm and monitoring integration

Read [events, state, commands, and time](../01-foundations/events-state-commands-and-time.md), [data modelling](../01-foundations/data-models-and-semantics.md), and [reliability and failure semantics](../01-foundations/reliability-and-failure-semantics.md). Then use the [alarm-protocol index](../02-protocols/alarm-monitoring/README.md) for the SIA families and [IEC 60839 alarm transmission](../02-protocols/alarm-monitoring/iec-60839-alarm-transmission.md), followed by [intrusion-monitoring systems](../03-systems/intrusion-monitoring/README.md) for receivers, verification, and redundant path supervision. Use [CAP and EDXL](../02-protocols/web-and-messaging/cap-and-edxl-emergency-messaging.md) for public-warning message exchange, not as a panel-to-receiver substitute.

Outcome: model alarm, restore, cancel, test, communication fault, and acknowledgement without assuming ordered or exactly-once delivery.

## Building and OT convergence

Read [trust boundaries and segmentation](../01-foundations/trust-boundaries-and-segmentation.md), [serial and field interfaces](../01-foundations/serial-and-field-interfaces.md), [TLS and PKI](../01-foundations/tls-pki-and-certificates.md), and [secure integration lifecycle](../01-foundations/secure-integration-lifecycle.md). Then use the [building and industrial index](../02-protocols/building-and-industrial/README.md) for Modbus, BACnet/BACnet/SC, KNX Secure, OPC UA, IEC 60870-5, IEC 61850, Matter, and only the protocols actually present at the site.

Outcome: broker the minimum required information across zones without turning an analytics or enterprise integration into an uncontrolled actuation path.

## Defensive reviewer

Follow [verification and safety](verification-and-safety.md), [trust boundaries](../01-foundations/trust-boundaries-and-segmentation.md), [identity and authorization](../01-foundations/identity-authentication-and-authorization.md), [TLS and PKI](../01-foundations/tls-pki-and-certificates.md), [reliability](../01-foundations/reliability-and-failure-semantics.md), and [observability and evidence](../01-foundations/observability-and-evidence.md). Apply [security and assurance](../06-security-and-assurance/README.md) and only the [defensive-lab class](../08-defensive-labs/README.md) authorized for the environment.

Outcome: produce a finding that states evidence, affected version/path, preconditions, physical consequence, uncertainty, and a proportionate mitigation.

## Suggested depth

Use three passes:

- **Map:** actors, layers, data/control paths, lifecycle, and trust boundaries.
- **Mechanics:** framing, state, timing, errors, identity, and secure modes.
- **Assurance:** negative cases, degradation, recovery, logging, version drift, and source verification.
