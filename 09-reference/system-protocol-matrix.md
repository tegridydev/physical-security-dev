---
title: System-to-Protocol Matrix
summary: Relates physical-security system components to likely protocol boundaries without implying universal support.
page_type: reference
domains: [video, access-control, alarms, intercom, bms, ot, integration, cross-domain]
tags: [systems, protocols, architecture, matrix]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [ONVIF Profiles, GB/T 28181, OSDP, SIA DC-09, IEC 60839, SIP, Modbus, BACnet, OPC UA, IEC 60870-5, IEC 61850, Matter]
coverage_limit: Typical boundary map only; no row claims that every product supports every listed technology.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# System-to-protocol matrix

Read cells as investigation candidates, not product claims. Verify the exact device, firmware, role, license, profile, configuration, and secure mode.

| Component or boundary | Common standards/families | Common proprietary/API boundary | Primary data or function | Key risk to resolve |
|---|---|---|---|---|
| IP camera ↔ VMS | ONVIF T/S/M, RTSP/RTP/RTCP, HTTP(S), NTP | Device API/SDK, proprietary media/analytics | Live media, capabilities, events, imaging, health | Profile/role mismatch, credential sprawl, unprotected media, time drift |
| Camera/platform in applicable Chinese domain | GB/T 28181-2022, SIP/SDP/RTP, GB 35114, GB/T 43026 | Product platform extensions | Registration, catalogue, live/playback sessions, events | National-profile mismatch, domain identity, media security, abolished edition use |
| Contribution encoder ↔ receiver/cloud ingress | SRT or a declared VSF RIST profile | Vendor contribution service | Low-latency encoded media contribution | Shared secret, listener exposure, unbounded recovery, contribution mistaken for evidence export |
| Edge recorder ↔ VMS/client | ONVIF G, RTSP/RTP, HTTPS | Vendor recording/search/export SDK | Recording control, search, playback, export | Retention gaps, export integrity, time/provenance |
| Video analytics ↔ VMS/PSIM | ONVIF M, MQTT, webhook, WebSocket, API | Vendor metadata/event schema | Detections, tracks, objects, confidence | Model drift, privacy, duplicates, coordinate/time mapping |
| Intercom ↔ call platform | SIP, SDP, RTP/SRTP, HTTPS | Vendor provisioning/call-control API | Registration, call setup, audio/video, door request | Emergency priority, media security, relay authorization |
| Reader/peripheral ↔ access controller | OSDP over RS-485; legacy Wiegand/Clock-and-Data | Vendor bus | Credential presentation, keypad/biometric data, LEDs/buzzer, supervision | Weak legacy signaling, key management, bus availability, tamper |
| Access controller ↔ PACS server | HTTPS/API, TLS, time, sometimes ONVIF C/A | Vendor protocol/SDK/database contract | Configuration, decisions, events, health | Offline authority, state conflicts, actuation privilege |
| PACS/controller ↔ turnstile or security vestibule | OSDP, supervised I/O, product bus, IEC 60839-11 context | Portal controller API/SDK | Grant, direction, passage sensing, occupancy/interlock, alarms | Entrapment/egress, accessibility, tailgating inference, grant/state/passage conflation |
| PACS ↔ identity source | LDAP/SCIM/API, SAML/OIDC for operators | HR/vendor connector | People, identities, roles, lifecycle | Joiner/mover/leaver lag, authoritative fields, tenant/privacy scope |
| Operator ↔ PACS application identity | SAML 2.0 or OIDC; WebAuthn/FIDO at the identity layer | Vendor SSO/role adapter | Authentication, session, mapped administrative/operator role | Broad claims-to-role mapping, recovery downgrade, login mistaken for physical authorization |
| Mobile credential wallet ↔ cloud ↔ reader | BLE/NFC/UWB plus HTTPS/OAuth/vendor trust protocol | Issuer/vendor SDK and provisioning service | Issuance, presentation, revocation, ranging | Radio relay/downgrade, device binding, cloud outage, privacy |
| Intrusion panel ↔ receiver | SIA DC-09 and SIA/Contact ID formats | Vendor receiver protocol | Alarm, restore, test, supervision, acknowledgement | Delivery assurance, duplicate correlation, key management, failover |
| Alarm transmission system boundary | IEC 60839-5 family and applicable national profiles | Transmitter/receiver product protocol | Path performance, equipment/network supervision, alarm delivery | Wrong part/adoption, TS treated as final standard, receiver/dispatch boundary confusion |
| Warning authority ↔ public alert distributor | CAP 1.2, CAP-AU where applicable, EDXL-DE 2.0 | Jurisdiction/feed-specific API | Alert, update, cancel, area/audience, routed emergency information | Issuer/profile trust, stale lifecycle, geography, delivery mistaken for activation |
| Receiver ↔ monitoring automation | SIA DC-07 or product API | Vendor integration | Normalized event handoff and disposition | Ordering, account mapping, acknowledgement ownership |
| Detection sensor ↔ panel/controller | Dry contact/supervised circuit, serial/vendor bus | Product bus | Alarm/tamper/fault states | Electrical supervision, ambiguous semantics, sabotage, nuisance alarms |
| PSIM/integration platform ↔ domain systems | HTTPS, MQTT, WebSocket, webhook, OPC UA | Vendor SDKs and message buses | Correlation, workflow, operator context, commands | Excess privilege, semantic loss, cascading automation |
| Enterprise broker ↔ integration services | AMQP 1.0, MQTT, HTTPS | Managed broker/router contract | Commands, events, queues, settlement, dead-letter handling | Cross-tenant links, schema drift, settlement mistaken for workflow/physical completion |
| BMS ↔ field controllers | BACnet/IP/MS-TP/SC, KNX, Modbus | Vendor building protocol | Environmental state and control | Broadcast scope, weak legacy security, safety coordination |
| OT gateway ↔ PLC/device | Modbus, OPC UA, EtherNet/IP/CIP, PROFINET, DNP3 | Vendor engineering protocol | Telemetry, setpoints, control | Production/safety impact, direct-write exposure, recovery |
| Utility/power automation ↔ security integration gateway | IEC 60870-5-101/-104, IEC 61850, DNP3, OPC UA | Utility/IED/gateway profile | Power/site status, alarms, quality, time, selected telemetry | Protection/control coupling, command exposure, SCL/point-map drift, legacy security |
| Matter fabric ↔ approved building gateway | Matter 1.6 over supported IP fabrics | Ecosystem/cloud bridge | Selected sensor/device attributes and events | Fabric/ACL lifecycle, attestation overclaim, bridge trust, inappropriate PACS/fire substitution |
| Constrained device ↔ management service | CoAP/OSCORE, OMA LwM2M | Product object model/cloud | Telemetry, observation, configuration, lifecycle management | Bootstrap authority, proxy termination, ACK mistaken for outcome, resource exhaustion |
| Management plane ↔ devices | HTTPS, SSH, SNMPv3, syslog/TLS, NTP/NTS | Vendor discovery/update API | Configuration, monitoring, firmware, logs | Default/shared credentials, certificate lifecycle, supply chain |
| Cloud service ↔ on-prem connector | HTTPS/mTLS, WebSocket, MQTT | Vendor tunnel/agent | Brokered API/events/media/control | Tenant isolation, outbound trust, remote command authority, outage mode |

## Boundary questions

For every row used in a design, record:

1. source and destination roles, owners, trust zones, and authoritative system;
2. exact protocol/profile/edition, transport, port policy, discovery path, and secure mode;
3. identity, authentication, authorization, credential/key/certificate lifecycle;
4. data classification, schema, time, provenance, retention, and privacy;
5. timeouts, gaps, duplicate/retry behavior, offline mode, reconciliation, and recovery;
6. observation versus actuation and the physical consequence of error;
7. product/version/licensing evidence and owner-approved acceptance evidence.

Continue with [physical-security system architecture](../01-foundations/physical-security-system-architecture.md), [systems](../03-systems/README.md), and the [integration readiness checklist](integration-readiness-checklist.md).
