---
title: "ONVIF services, profiles, conformance, and security"
summary: "Developer reference for ONVIF discovery, SOAP services, profile status, conformance claims, events, media, access control, and secure deployment."
page_type: protocol
domains: [video, access-control]
tags:
  - onvif
  - soap
  - ws-discovery
  - profiles
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "ONVIF Network Interface Specifications 26.06 (June 2026)"
  - "ONVIF Profile V 1.0 Release Candidate (July 2026)"
  - "IEC 60839-11-31:2016"
  - "IEC 60839-11-32:2016"
  - "IEC 60839-11-33:2016"
coverage_limit: "Standards and profile architecture only; no product registration lookup, ONVIF test-tool run, live device, door, relay, PTZ, or media behavior is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# ONVIF services, profiles, conformance, and security

[Video and media protocols](README.md) / ONVIF

ONVIF standardizes interoperable interfaces for IP-based physical-security products. Its network interface specifications define services and data types; **profiles** select fixed feature sets for product interoperability; **add-ons** are optional, versioned capabilities that can evolve independently. These are different claims and must not be collapsed into “supports ONVIF.” [ONVIF-SPECS] [ONVIF-PROFILES-ADDONS]

## Verified status snapshot

Status below is verified as at **2026-08-25**. The current network-interface release is **26.06**, published in June 2026. That release includes SRTP configuration/support work, ONVIF Export File Format work, WebRTC clarifications, and security updates. [ONVIF-HISTORY] [ONVIF-2606]

| Item | Status | Integration consequence |
|---|---|---|
| Profile A | Active | Access-control configuration, credentials, schedules, and rules |
| Profile C | Active | Access control and door-control event interoperability |
| Profile D | Active | Access-control peripherals such as readers, locks, sensors, and outputs |
| Profile G | Active | Edge storage, recording search, and replay |
| Profile M | Active | Analytics metadata and events; MQTT is conditional |
| Profile S | Active but deprecating | Product-conformance submissions end **2027-03-31**; plan migration to Profile T |
| Profile T | Active | Advanced video: H.264/H.265, imaging, metadata/events, and optional bidirectional audio |
| Profile V | **Release Candidate**, released 2026-07-09 | Cloud-facing uplink including WebRTC/H.264, MQTTS events, modern authorization patterns, and conditional audio; do not label products conformant before final release and certification availability |
| Profile Q | Deprecated since 2022-04-01 | Do not use for new procurement or architecture |
| TLS Configuration Add-on 1.0 | Active but deprecating | Product submissions end **2027-03-31**; ONVIF says 2.0 is scheduled for early 2027, so treat 2.0 as planned, not published |
| Profile V Security Add-on | **Release Candidate** | Evaluate alongside Profile V; it is not a final conformance claim |

ONVIF publishes the authoritative profile list and individual profile pages. Profile S's end date and migration guidance are explicit ONVIF lifecycle announcements. [ONVIF-PROFILES] [ONVIF-S-DEP] [ONVIF-V] [ONVIF-TLS]

## Specifications, profiles, and registered products

Use this decision sequence:

1. Identify the exact product and firmware.
2. Look it up in ONVIF's conformant-products database.
3. Record the claimed profile(s) and any add-on version(s).
4. Read the profile's mandatory and conditional requirements.
5. Query runtime capabilities and service versions.
6. Run the applicable ONVIF conformance and interoperability processes where your role permits.

A product is ONVIF conformant only when it is registered by ONVIF for the claimed profile. Implementing a WSDL, responding to WS-Discovery, or passing a few client requests is not an ONVIF conformance claim. Profile features are fixed; a conditional feature becomes mandatory when the product advertises or implements the triggering capability. [ONVIF-PROFILES] [ONVIF-TEST]

## IEC 60839 access-control mapping

IEC adopted Web-services-based access-control material derived from ONVIF specifications in three parts of IEC 60839-11. The relationship is useful for procurement and architecture, but the publications and their conformity claims remain distinct. [ONVIF-IEC]

| IEC publication | Interface area | Closely related ONVIF material |
|---|---|---|
| IEC 60839-11-31:2016 | Core interoperability protocol based on Web services | ONVIF core/device-service conventions on which the access-control services depend |
| IEC 60839-11-32:2016 | Access-control monitoring based on Web services | Access Control and event-monitoring service concepts associated with access-control profiles |
| IEC 60839-11-33:2016 | Access-point configuration based on Web services | Door/access-point configuration and control service concepts associated with access-control profiles |

Use the exact IEC clauses and the corresponding ONVIF specification versions to construct a requirement-level mapping; the table is an architectural crosswalk, not a clause-equivalence assertion. ONVIF's current rolling network-interface release can contain changes made after the IEC editions were published.

Keep these claims separate in requirements and product records:

- **ONVIF conformance** requires the applicable ONVIF profile implementation, testing, and registration in ONVIF's conformant-products database.
- **IEC conformity** concerns the named IEC part and edition under the applicable assessment, certification, procurement, or regulatory scheme.
- An ONVIF-registered product is not automatically certified to an IEC part, and an IEC claim is not automatically an ONVIF profile registration.
- State the product, firmware, ONVIF profile/add-on, ONVIF registration, IEC part/edition, assessment evidence, and any regional adoption independently.

Profile A, C, and D scope can overlap the access-control functions described by these IEC parts, but a profile name is not a substitute for an IEC requirements matrix. Conversely, implementing an IEC Web-service interface does not establish every mandatory or conditional feature of an ONVIF profile. [IEC-1131] [IEC-1132] [IEC-1133]

## Protocol stack and discovery

Typical device-side flow:

```text
WS-Discovery Probe/Resolve on the local discovery domain
    -> device service XAddr
GetServices / GetCapabilities
    -> service endpoints and versions
GetSystemDateAndTime / identity and security setup
    -> authenticated service calls
media, events, PTZ, recording, access, door, or I/O operations
```

ONVIF interfaces are primarily WSDL-defined SOAP/XML services over HTTP(S). WS-Discovery is useful for initial discovery but should not be treated as identity proof: discovery metadata and endpoint addresses are attacker-controlled until authenticated. Route discovered addresses through an allowlist or management-plane policy; do not let an untrusted XAddr become an unrestricted server-side request target.

## Service map

Actual availability is capability- and profile-dependent.

| Service area | Developer responsibilities |
|---|---|
| Device management | Identity, time, users, network configuration, service enumeration, reboot, certificates, and capabilities |
| Media / Media2 | Profiles/configurations, encoder/source selection, stream URI acquisition, snapshots, audio, and multicast parameters |
| Imaging | Exposure, focus, white balance, wide dynamic range, and supported option ranges |
| PTZ | Nodes/configurations, absolute/relative/continuous move, presets, status, limits, and stop behavior |
| Events | Topic discovery, subscriptions, PullPoint polling, renewal, unsubscribe, property state, and message parsing |
| Analytics | Rules/modules, supported analytics, metadata schemas, and event correlation |
| Recording, search, replay | Recording jobs/configurations, search sessions, result paging, replay URI, and time ranges |
| Device I/O | Relay outputs, digital inputs, serial ports, and audio sources/outputs where supported |
| Access rules and access control | Rules, schedules, credentials/tokens, decisions, and access events |
| Door control | Door state, lock/unlock operations, alarms, and monitored inputs/outputs |
| Uplink and WebRTC | Profile V cloud connectivity, media establishment, status, and lifecycle where supported |

Prefer `GetServices` with capability inclusion when supported, then interrogate each service's options. Never assume that because one firmware exposes an endpoint, another product with the same profile exposes every optional operation.

## Media retrieval pattern

For conventional camera integrations:

1. Enumerate media profiles/configurations.
2. Select by declared token and capabilities, not display name alone.
3. Obtain a stream URI for the intended transport and protocol.
4. Apply separate authorization and expiry policy to the returned URI.
5. Establish RTSP/RTP or the negotiated transport.
6. Monitor encoder reconfiguration, source loss, keyframe recovery, and URI expiry.

Profile tokens are opaque identifiers. Persisting a token can be useful, but integrations must recover when a factory reset, firmware change, or configuration replacement invalidates it.

## Event consumption

PullPoint is commonly easier to operate through firewalls than callbacks. A robust consumer:

- obtains the topic set and validates expected namespaces;
- creates a subscription with a bounded lifetime;
- polls with bounded timeout and message count;
- renews before expiry and recreates on lost subscription;
- parses `Topic`, source, key, data, UTC time, and property-operation semantics;
- deduplicates using application context because transport retries and reconnects can repeat state;
- treats `Initialized`, `Changed`, and `Deleted` property operations distinctly;
- records device clock quality and never assumes clocks are synchronized.

Profile M metadata/events and its conditional MQTT support do not make every Profile M product an MQTT publisher. Query the advertised capability and authenticate broker connections independently. [ONVIF-M]

## Safe SOAP shape

**Target:** Offline request construction for an ONVIF device-service operation.

**Inputs:** Synthetic endpoint and no credentials.

**Side effects:** Offline construction only; any transport adapter must enforce authorization, target allowlisting, and operation-specific policy.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<s:Envelope
    xmlns:s="http://www.w3.org/2003/05/soap-envelope"
    xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
  <s:Header/>
  <s:Body>
    <tds:GetServices>
      <tds:IncludeCapability>true</tds:IncludeCapability>
    </tds:GetServices>
  </s:Body>
</s:Envelope>
```

The actual HTTP binding, SOAP action, authentication headers, TLS trust, timeouts, and XML limits must follow the device's advertised WSDL and the relevant ONVIF release. See [SOAP and XML](../web-and-messaging/soap-and-xml.md).

## Security architecture

### Transport and device identity

- Prefer HTTPS with certificate validation and managed trust anchors. Do not silently fall back to HTTP after a TLS failure.
- Provision unique device identities and credentials; reject shared factory credentials.
- Pinning can reduce trust scope but needs an explicit renewal/replacement path.
- Segment device, recorder, client, and cloud planes. Limit discovery multicast to intended segments.
- Normalize and validate service endpoint addresses before following them.

### Authentication and authorization

- Use the strongest mechanism both parties explicitly support; never place passwords in stream URLs or logs.
- Give discovery, read-only monitoring, video retrieval, PTZ, door control, firmware/configuration, and user administration separate roles.
- Treat door unlock, relay activation, configuration reset, user changes, and certificate changes as high-impact operations requiring explicit policy and audit.
- Reauthorize long-lived subscriptions and media sessions after account, role, or credential changes.

### XML and message handling

- Disable external entities and external DTD resolution.
- Bound envelope, element depth, attribute count, text length, arrays, metadata frames, and decompressed size.
- Match namespace URI plus local name; do not match a security-relevant element by local name alone.
- Reject ambiguous duplicates and unexpected signature placement if a security profile uses signed XML.
- Treat schema validation as syntax checking, not authorization.

### Media and events

RTP is not encrypted by default. Use SRTP or another explicitly negotiated protected media path when required; release 26.06 adding SRTP-related configuration work does not imply every device or profile supports SRTP. Protect event data as sensitive operational telemetry: it can reveal occupancy, door state, camera health, location, and alarm posture.

## Failure and interoperability checklist

- [ ] Exact firmware and registered profile/add-on claims recorded
- [ ] Network-interface release and each service namespace/version recorded
- [ ] Required versus conditional profile features mapped
- [ ] TLS trust, hostname/address rules, clock requirements, and credential rotation validated against target versions
- [ ] HTTP/SOAP timeout and retry policy is operation-specific
- [ ] Mutating operations are not blindly retried
- [ ] Event renewal, replay/deduplication, and clock discontinuity handled
- [ ] Media tokens, URIs, encoder changes, and restart recovery handled
- [ ] XML, metadata, image, and event sizes bounded
- [ ] PTZ, relay, door, and configuration operations explicitly authorized and audited
- [ ] Profile S and TLS Add-on 1.0 migration dates tracked
- [ ] Release-candidate features never represented as final conformance

## Environment validation

Treat the cited standards status as a snapshot, not a statement about any product. Record ONVIF Device/Client Test Tool results, product-database entries, exact firmware, advertised capabilities, service namespaces, TLS behavior, event and media recovery, and cross-vendor interoperability evidence for the deployed versions.

## Sources

- **ONVIF-SPECS** — [Network Interface Specifications][ONVIF-SPECS], ONVIF, accessed 2026-08-25.
- **ONVIF-HISTORY** — [Specification History][ONVIF-HISTORY], ONVIF, accessed 2026-08-25.
- **ONVIF-2606** — [June 2026 (26.06) specification release][ONVIF-2606], ONVIF, June 2026, accessed 2026-08-25.
- **ONVIF-PROFILES** — [Profiles][ONVIF-PROFILES], ONVIF, status accessed 2026-08-25.
- **ONVIF-PROFILES-ADDONS** — [Profiles, Add-ons and Specifications][ONVIF-PROFILES-ADDONS], ONVIF, accessed 2026-08-25.
- **ONVIF-TEST** — [Device Test Specifications 26.06][ONVIF-TEST], ONVIF, June 2026, accessed 2026-08-25.
- **ONVIF-S-DEP** — [Profile S Deprecation Q&A][ONVIF-S-DEP], ONVIF, accessed 2026-08-25.
- **ONVIF-V** — [Profile V][ONVIF-V], ONVIF, release candidate dated 2026-07-09, accessed 2026-08-25.
- **ONVIF-V-SEC** — [Profile V Security Add-on][ONVIF-V-SEC], ONVIF, release candidate, accessed 2026-08-25.
- **ONVIF-M** — [Profile M][ONVIF-M], ONVIF, accessed 2026-08-25.
- **ONVIF-TLS** — [TLS Configuration Add-on][ONVIF-TLS], ONVIF, lifecycle status accessed 2026-08-25.
- **ONVIF-IEC** — [IEC adopts ONVIF specification for access-control standard][ONVIF-IEC], ONVIF, accessed 2026-08-25.
- **IEC-1131** — [IEC 60839-11-31:2016][IEC-1131], IEC, core interoperability protocol based on Web services.
- **IEC-1132** — [IEC 60839-11-32:2016][IEC-1132], IEC, access-control monitoring based on Web services.
- **IEC-1133** — [IEC 60839-11-33:2016][IEC-1133], IEC, access-point configuration based on Web services.

[ONVIF-SPECS]: https://www.onvif.org/profiles-specifications-new/
[ONVIF-HISTORY]: https://www.onvif.org/profiles/specifications/specification-history/
[ONVIF-2606]: https://www.onvif.org/profiles/specifications/specification-history/june-2026/
[ONVIF-PROFILES]: https://www.onvif.org/profiles/
[ONVIF-PROFILES-ADDONS]: https://www.onvif.org/profiles-add-ons-specifications/
[ONVIF-TEST]: https://www.onvif.org/profiles/conformance/device-test-2/
[ONVIF-S-DEP]: https://www.onvif.org/profiles/profile-s/profile-s-deprecation-qna/
[ONVIF-V]: https://www.onvif.org/profiles/profile-v/
[ONVIF-V-SEC]: https://www.onvif.org/add-on/profile-v-security-add-on/
[ONVIF-M]: https://www.onvif.org/profiles/profile-m/
[ONVIF-TLS]: https://www.onvif.org/profiles/add-on/tls-configuration-add-on/
[ONVIF-IEC]: https://www.onvif.org/pressrelease/global-standards-group-iec-adopts-onvif-specification-for-new-access-control-standard/
[IEC-1131]: https://webstore.iec.ch/en/publication/32774
[IEC-1132]: https://webstore.iec.ch/en/publication/31982
[IEC-1133]: https://webstore.iec.ch/en/publication/32750
