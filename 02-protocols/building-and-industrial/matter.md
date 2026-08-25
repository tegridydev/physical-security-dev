---
title: Matter
summary: Matter fabrics, commissioning, operational security, access control, device attestation, multi-admin behavior, camera support, and safe physical-security integration.
page_type: protocol
domains: [bms, video, cross-domain]
tags: [matter, csa, fabric, commissioning, device-attestation, multi-admin]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [Matter 1.6]
coverage_limit: Public Connectivity Standards Alliance material is covered; the complete normative specification package, product certification records, ecosystem behavior, and device-specific clusters remain necessary for implementation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Matter

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / Matter

Matter is an application-layer interoperability standard for connected devices. It uses IPv6 and a common data model across supported IP networks; it is **not** a radio, link layer, or replacement for Wi-Fi, Ethernet, or Thread. Bluetooth Low Energy is commonly used during discovery and commissioning, not as the ordinary operational application transport. [MATTER-SPECS]

The Connectivity Standards Alliance announced **Matter 1.6** on 17 June 2026. A product still needs an exact specification version, supported device types and clusters, certification record, ecosystem compatibility statement, and firmware baseline. A generic “Matter compatible” claim does not establish support for cameras, bridges, Joint Fabric behavior, or any particular security feature. [MATTER-16]

## Architecture and roles

```text
commissioner ---- secure onboarding ---- commissionee
     |                                      |
     +-------- fabric credentials ----------+

controller ===== CASE-secured IPv6 session ===== node
     |                                             |
 ecosystem / administrator                   endpoints + clusters

Thread node --- Thread border router --- IPv6 infrastructure
Wi-Fi/Ethernet node --------------------- IPv6 infrastructure
```

| Term | Meaning | Integration caution |
|---|---|---|
| Node | One Matter-addressable participant with a node identifier inside a fabric | A physical product can expose multiple endpoints and can belong to multiple fabrics |
| Endpoint | A logical instance within a node | Endpoint numbers are not universal device identities |
| Device type | A standardized role and required/optional cluster composition | Verify the exact revision and feature map rather than matching a display name |
| Cluster | Attributes, commands, events, data types, and behavior for a function | Cluster presence does not prove every optional command or feature is supported |
| Commissioner | Participant that onboards a commissionee into a fabric | Commissioning authority is highly privileged and should be time- and scope-bounded |
| Controller | Participant that reads, subscribes, or invokes commands after commissioning | Controller identity does not by itself grant every cluster privilege |
| Administrator | Authority able to manage fabric membership and policy | Separate ecosystem administration from ordinary automation identities |
| Bridge | Matter node representing devices that use another technology behind it | Preserve the bridged technology's identity, quality, latency, and failure boundaries |
| Fabric | Logical trust and administrative domain with shared operational credentials and scoped node identities | The same product can have different identities, policy, and state in different fabrics |

Matter discovery commonly uses DNS-SD/mDNS, while Thread devices depend on one or more border routers for IP reachability beyond the mesh. Discovery output is untrusted metadata, not authorization. Constrain multicast domains, validate advertised service data, and bind an interaction to the authenticated operational node and fabric—not merely to a hostname, product label, or discovered address.

## Data model and interaction contract

Matter represents application behavior through endpoints and clusters. Clusters can expose attributes, commands, and events; feature maps and revision metadata indicate supported subsets. An integration inventory should preserve:

- vendor/product identity and certified model/firmware record;
- fabric identifier and operational node identity without publishing sensitive credentials;
- endpoint, device type, cluster, cluster revision, feature map, and accepted command set;
- attribute/event data type, unit, range, null/unknown behavior, quality, and timestamp provenance;
- subscription limits, reporting intervals, liveness expectations, and resubscription behavior;
- bridge path and native-device identity where a bridge is involved;
- required privilege and intended physical consequence for every command;
- authoritative post-command feedback and timeout.

Do not infer physical state from successful protocol delivery. A command response can report application handling while a motor, contact, latch, camera privacy mechanism, or bridged subsystem remains delayed, obstructed, faulted, or independently overridden. Confirm important outcomes through an authoritative sensor/attribute/event and surface indeterminate state.

## Commissioning and operational sessions

Commissioning establishes a product in a fabric. The process includes discovery, proof of possession, device attestation, provisioning of operational credentials, network configuration where applicable, and installation of fabric policy. Matter distinguishes commissioning security from routine operational sessions:

- **PASE** establishes a password-authenticated commissioning session from setup information;
- **CASE** establishes certificate-authenticated operational sessions between fabric members;
- operational certificates and fabric-scoped keys identify nodes after commissioning;
- group communication has different key, replay, membership, and feedback properties from unicast interaction.

Setup codes and QR payloads are onboarding secrets. Keep them out of screenshots, issue trackers, telemetry, public asset records, and long-lived application logs. Commission only during an authorized window, identify the intended physical product independently, reject unexpected fabrics, and close the commissioning window after use.

Decommissioning must remove fabric membership, revoke or age out credentials as the applicable ecosystem permits, clear sensitive local state, and reconcile any bridge or cloud record. A factory reset changes trust state and may disrupt every ecosystem attached to the node; it is not a routine troubleshooting step.

## Device attestation is not authorization

Matter device attestation uses a Device Attestation Certificate chain and associated certification declarations to support product-origin and certification checks during commissioning. Its decision inputs and trusted Product Attestation Authority roots require lifecycle management.

Attestation can help answer whether a commissionee presents an acceptable certified product identity. It does **not** establish:

- that the person commissioning it is authorized for the site;
- that the product is physically installed at the claimed location;
- that its current firmware is vulnerability-free;
- that a controller should receive access to a door, camera, relay, or occupancy signal;
- that a later command produced the intended physical outcome.

Record attestation result, policy version, certificate identifiers, certification declaration result, exception approval, and firmware/product baseline separately from application authorization.

## Fabric access control

Matter access-control entries are fabric-scoped and express privilege, authenticated subject, and target constraints. Exact fields and behavior are version-dependent, but the engineering rules are stable:

- grant the minimum privilege needed for the required endpoints and clusters;
- use distinct identities for administrators, automation controllers, bridges, and observability collectors;
- avoid broad node, group, or CASE Authenticated Tag grants without a documented membership lifecycle;
- protect access-control and operational-credential management as administrative functions;
- reconcile policy after node replacement, ecosystem removal, bridge migration, or fabric changes;
- treat group commands as potentially wide actuation with limited per-recipient confirmation;
- log policy changes and denied high-impact commands without disclosing keys or setup payloads.

Matter policy is one layer. A security platform still needs tenant/site/resource authorization, operator role, purpose, schedule, emergency override, separation of duties, and local safety interlocks. Do not translate a broad ecosystem role directly into unrestricted physical-security control.

## Multi-admin and Joint Fabric boundaries

Traditional multi-admin behavior allows a product to participate in more than one fabric, giving each ecosystem its own credentials, node identity, access-control state, subscriptions, and lifecycle. Matter 1.6 also introduces **Joint Fabric** capabilities intended to improve multi-ecosystem sharing. Treat Joint Fabric as an explicit capability with ecosystem- and product-specific support, not as a property of every Matter 1.6 deployment. [MATTER-16]

For either model, define:

- which administrator owns initial onboarding, removal, update policy, and recovery;
- whether identities and policy are independent, synchronized, or jointly administered;
- how duplicate automations, events, and commands are prevented;
- what one ecosystem can learn about another ecosystem or its users;
- what happens when one administrator removes the node or becomes unavailable;
- how audit records correlate fabric-scoped identities without creating an unnecessary global identifier.

Shared control increases the need for deterministic precedence. Two valid ecosystems can issue conflicting commands without either being malicious.

## Cameras and physical-security boundaries

Matter 1.5 introduced camera support; Matter 1.5.1 refined camera performance and device flexibility. Matter 1.6 is the current published family baseline on the verification date. A camera integration must therefore pin the exact product and cluster revision rather than infer a uniform “Matter camera” capability. [MATTER-15] [MATTER-151] [MATTER-16]

Matter camera support does not automatically provide:

- ONVIF profile conformance or ONVIF service behavior;
- VMS recording, retention, evidence export, chain of custody, or legal hold;
- universal browser, codec, WebRTC gateway, or NAT traversal compatibility;
- a complete event taxonomy, analytics model, or alarm-monitoring contract;
- authorization suitable for privacy zones, microphone use, PTZ, or recording access.

Maintain separate media-session authorization, codec/transport limits, privacy and recording policy, event provenance, and evidence controls. A Matter bridge or controller should not become an unreviewed path around the camera/VMS security model.

## Bridging and cross-domain automation

A bridge translates identity, state, command, timing, and failure semantics between Matter and another protocol. It cannot manufacture guarantees absent on the native side. Record native identifiers and quality, distinguish cached from observed state, cap translation queues, expose partial failure, and avoid silently mapping unknown values to a safe-looking default.

Keep fire/life-safety control, access decisions, lock release, lift control, and other certified behavior outside ordinary consumer automation unless the complete approved system design explicitly includes that path. Matter scenes, routines, occupancy, and presence are convenient automation inputs; they are not authoritative access decisions or emergency-system states.

## Failure and recovery cases

- commissioner loses connectivity after operational credentials are installed but before the UI reports completion;
- node belongs to a fabric but network provisioning, DNS-SD, or border routing is unavailable;
- Thread border-router failover changes path or reachability;
- operational certificate, trust root, group key, or ecosystem account is rotated or removed;
- subscriptions lapse and cached attributes appear current;
- bridge is reachable while one or more bridged devices are stale or absent;
- two fabrics issue conflicting commands or maintain inconsistent policy;
- firmware update changes endpoint composition, feature maps, or behavior;
- factory reset leaves stale inventory, cloud, automation, or evidence records.

Recovery should reconcile fabric membership, endpoint/cluster inventory, policy, subscriptions, bridge mappings, and authoritative physical state. Avoid blind replay of commands after an indeterminate disconnect.

## Design and evidence checklist

- [ ] Matter specification, product firmware, certification record, device types, clusters, revisions, and feature maps pinned
- [ ] Operational network/bearer and Thread border-router dependencies documented
- [ ] Commissioner, administrator, controller, bridge, and observability identities separated
- [ ] Setup payloads, attestation roots, operational certificates, group keys, and rotation/removal lifecycle protected
- [ ] Attestation policy kept distinct from user authorization and site acceptance
- [ ] Fabric ACLs mapped to tenant/site/resource policy with least privilege
- [ ] Multi-admin or Joint Fabric ownership, synchronization, privacy, conflict, and removal behavior defined
- [ ] Attribute freshness, subscription gaps, bridge quality, and unknown state preserved
- [ ] Commands have idempotency/replay policy and authoritative post-condition feedback
- [ ] Camera media, privacy, recording, event, evidence, and ONVIF boundaries documented separately
- [ ] Fire/life-safety, lock, gate, lift, relay, and other high-impact paths require approved system-level controls
- [ ] Commissioning, policy changes, fabric membership, firmware, and administrative actions produce reviewable audit evidence

## Sources

- **MATTER-SPECS** — [Matter specification downloads][MATTER-SPECS], Connectivity Standards Alliance, accessed 2026-08-25. Complete specification packages may require an access request or licence acceptance.
- **MATTER-16** — [Matter 1.6 enables more intuitive setup, multi-ecosystem experiences, and context-driven control][MATTER-16], Connectivity Standards Alliance, 17 June 2026.
- **MATTER-151** — [Matter 1.5.1: enhancing camera performance and expanding device flexibility][MATTER-151], Connectivity Standards Alliance, 31 March 2026.
- **MATTER-15** — [Matter 1.5 introduces cameras, closures, and enhanced energy-management capabilities][MATTER-15], Connectivity Standards Alliance, 20 November 2025.

[MATTER-SPECS]: https://csa-iot.org/developer-resource/specifications-download-request/
[MATTER-16]: https://csa-iot.org/newsroom/matter-1-6-enables-more-intuitive-setup-multi-ecosystem-experiences-and-context-driven-control/
[MATTER-151]: https://csa-iot.org/newsroom/matter-1-5-1-enhancing-camera-performance-and-expanding-device-flexibility/
[MATTER-15]: https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/
