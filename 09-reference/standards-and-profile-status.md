---
title: "Standards and profile status"
summary: "A dated status register for the principal protocol editions, profiles, release candidates, deprecations, and legacy baselines used by this knowledge base."
page_type: register
domains:
  - cross-domain
tags:
  - standards
  - profiles
  - versions
  - deprecation
  - status-register
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "ONVIF Network Interface Specifications 26.06"
  - "SIA OSDP 2.2.2"
  - "MQTT 5.0"
  - "ANSI/ASHRAE 135-2024"
  - "OPC UA multi-part 1.05 line"
coverage_limit: "Selected global standards relevant to this repository as at 2026-08-25; licensed text, amendments, errata, regional adoption, certification listings, and exact product/firmware support must be checked at decision time."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Standards and profile status

[Home](../README.md) / [Reference](README.md) / Standards and profile status

Status snapshot: **2026-08-25**.

> This register is navigation and review evidence, not normative text or a product-support matrix. Obtain the official edition, applicable amendments/errata, certification record, and product declaration before implementation or procurement.

## Status vocabulary

| Label | Meaning in this register |
|---|---|
| Current base | Published edition used as the maintained reference on the verification date |
| Current alongside older deployment | Published and usable, but older editions remain materially deployed or interoperable |
| Release candidate | Public pre-final profile/specification; do not claim final conformance |
| Living/mutable | Publisher maintains an evolving web specification or support document; pin retrieval date |
| Legacy | Still encountered but should not be selected as a modern baseline without an explicit migration constraint |
| Deprecated | Publisher has announced withdrawal/deprecation or ended conformance submissions |
| Superseded | Replaced by a later normative edition; retain only for exact legacy compatibility |
| Edition conflict | Publisher-facing indexes disagree; obtain and identify the purchased normative copy |

The status of a standard, a profile, a certification program, a product, and a deployed feature are five different facts. See [interoperability, conformance, and profiles](../01-foundations/interoperability-conformance-and-profiles.md).

## Video and media

| Family | Snapshot status | Engineering consequence | Canonical page |
|---|---|---|---|
| ONVIF Network Interface Specifications | **26.06**, June 2026 release, current snapshot | Record every service namespace/version and test-specification release; “ONVIF” alone is incomplete | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| ONVIF Profiles A, C, D, G, M, S, T | Published profiles listed by ONVIF; individual lifecycle differs | Match exact product/firmware/role and conditional features in the registered-products database | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| ONVIF Profile S | Published but **deprecation in progress**; ONVIF says new product-conformance submissions end 2027-03-31 | Plan Profile T migration; existing conformant products do not become non-conformant merely from the submission cutoff | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| ONVIF Profile Q | **Deprecated 2022-04-01** | Do not use as a new procurement/security baseline | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| ONVIF Profile V and Profile V Security Add-on | **Release candidate**, Profile V page dated 2026-07-09 | Track final text and test tools; never represent RC implementation as final conformance | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| ONVIF TLS Configuration Add-on | 1.0 published with transition toward 2.0; ONVIF lists 1.0 submission end 2027-03-31 and plans 2.0 in early 2027 | Pin add-on version and transition dates; confirm final 2.0 status later | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| RTSP 2.0 | RFC 7826, current standards-track reference | Treat RTSP 2.0 as a separate capability from 1.0 | [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| RTSP 1.0 | RFC 2326 is obsoleted by RFC 7826 but remains materially deployed | Preserve for declared legacy/product interoperability only; do not mix version state machines | [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| RTP / RTCP | RFC 3550 / STD 64 with updates and profiles | Pin payload, feedback, security, multiplexing, and clock rules, not just “RTP” | [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| SDP | RFC 8866 is the current base and obsoletes RFC 4566 | Preserve offered version/profile; validate all address and format fields | [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| WebRTC browser API | W3C Recommendation dated 2025-03-13; browser behavior remains versioned/mutable | Pin target browsers and IETF media/security suite; owner compatibility testing remains required | [WebRTC](../02-protocols/video-and-media/webrtc.md) |
| SIP / SRTP | SIP RFC 3261 and SRTP RFC 3711 remain bases with many updates/extensions | Declare extension, identity, Digest, offer/answer, key-management, and SRTP profile set | [SIP and SRTP](../02-protocols/video-and-media/sip-and-srtp.md) |
| HLS | RFC 8216 is published; second-edition work was an Internet-Draft on the snapshot date | Label draft behavior as work in progress and pin player/server expectations | [Codecs and streaming](../02-protocols/video-and-media/codecs-and-streaming.md) |
| MPEG-DASH | ISO/IEC 23009-1:2026 Edition 6 is the current reviewed base | Pin profiles, codecs, manifests, segment addressing, DRM/entitlement, origin/cache, and player support | [Codecs and streaming](../02-protocols/video-and-media/codecs-and-streaming.md) |
| GB/T 28181 | **GB/T 28181-2022** current; 2016 edition abolished; related GB 35114-2017 and GB/T 43026-2023 have separate roles | Pin national/regional requirement, domain/role, security edition, and test evidence | [GB/T 28181](../02-protocols/video-and-media/gbt-28181.md) |
| SRT | Active project protocol; reviewed library release 1.5.6; the IETF Internet-Draft expired and is not an IETF standard | Pin implementation/library/interop profile; track security advisories and never call SRT an RFC | [SRT and RIST](../02-protocols/video-and-media/srt-and-rist.md) |
| RIST | VSF Simple Profile 2020; Main and Advanced Profile publications reviewed at 2024 status | Pin exact VSF Technical Recommendation/profile and implementation subset | [SRT and RIST](../02-protocols/video-and-media/srt-and-rist.md) |

## Web, messaging, and serialization

| Family | Snapshot status | Engineering consequence | Canonical page |
|---|---|---|---|
| HTTP semantics/cache/1.1/2/3 | RFCs 9110–9114 are the current coordinated base set; RFC 9931 (March 2026) updates HTTP/1.1 transition security | Pin supported HTTP versions and intermediaries; apply current update/errata state | [HTTP and REST](../02-protocols/web-and-messaging/http-and-rest.md) |
| REST | Architectural style, not a versioned wire standard or conformance label | Specify the API's media types, resources, errors, auth, versioning, and semantics | [HTTP and REST](../02-protocols/web-and-messaging/http-and-rest.md) |
| SOAP | SOAP 1.2 Second Edition is a W3C Recommendation; SOAP 1.1 persists in deployed profiles | Pin envelope/binding/WSDL/profile; do not treat 1.1 and 1.2 as interchangeable | [SOAP and XML](../02-protocols/web-and-messaging/soap-and-xml.md) |
| WebSocket | RFC 6455 base remains current with extension/subprotocol registries and updates | Pin HTTP opening context, extensions, subprotocol, auth renewal, and bounds | [WebSocket, SSE, and webhooks](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) |
| Server-Sent Events | WHATWG HTML Living Standard feature | Pin browser/client behavior and event contract retrieval date | [WebSocket, SSE, and webhooks](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) |
| Webhooks | No single universal webhook standard | Treat each vendor/API contract, signature, replay, retry, and callback-registration profile separately | [WebSocket, SSE, and webhooks](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) |
| MQTT 5.0 | OASIS Standard, 2019, current published major version | Declare protocol version and feature subset; v3.1.1 behavior differs | [MQTT](../02-protocols/web-and-messaging/mqtt.md) |
| MQTT 3.1.1 | OASIS Standard 2014 / ISO/IEC 20922:2016; still current for compatibility but older than v5 | Do not send v5 properties or assume v5 reason/session semantics | [MQTT](../02-protocols/web-and-messaging/mqtt.md) |
| gRPC | Project protocol/docs are maintained and implementation support windows are mutable | Pin protocol mapping, runtime, generated-code/compiler window, and transport profile | [gRPC and serialization](../02-protocols/web-and-messaging/grpc-and-serialization.md) |
| Protocol Buffers | Edition/language/runtime support is versioned; ordinary serialization is explicitly non-canonical | Pin schema syntax/edition and runtime support window; never reuse field numbers | [gRPC and serialization](../02-protocols/web-and-messaging/grpc-and-serialization.md) |
| JSON / CBOR | RFC 8259 and RFC 8949 / STD 94 are current bases | Add explicit duplicate, numeric, depth, tag, deterministic/canonical rules when needed | [gRPC and serialization](../02-protocols/web-and-messaging/grpc-and-serialization.md) |
| AMQP 1.0 | OASIS Standard, distinct from AMQP 0-9-1 | Pin role, link, settlement, SASL/TLS, transaction, and product extension support | [AMQP 1.0](../02-protocols/web-and-messaging/amqp-1-0.md) |
| CoAP / OSCORE | RFC 7252, RFC 8323, RFC 8613, and RFC 9175 are published IETF bases with distinct transports/security scopes | Pin UDP/TCP/WebSocket, OSCORE/group profile, observation, proxy, and application semantics | [CoAP, OSCORE, and LwM2M](../02-protocols/web-and-messaging/coap-oscore-and-lwm2m.md) |
| OMA LwM2M | **1.2.2** is the reviewed published release | Pin Core/Transport/Device Management documents, object model, bootstrap, and implementation support | [CoAP, OSCORE, and LwM2M](../02-protocols/web-and-messaging/coap-oscore-and-lwm2m.md) |
| CAP / EDXL-DE | CAP 1.2 is an OASIS Standard and ITU-T X.1303bis basis; EDXL-DE 2.0 is Committee Specification 02 | Pin regional profile and issuer/feed contract; delivery is not activation | [CAP and EDXL](../02-protocols/web-and-messaging/cap-and-edxl-emergency-messaging.md) |

## Access control and credentials

| Family | Snapshot status | Engineering consequence | Canonical page |
|---|---|---|---|
| SIA OSDP | **2.2.2**, released October 2024, current SIA baseline | Buy/use normative edition and exact conformance profile; verify Secure Channel and roles | [OSDP](../02-protocols/access-control/osdp.md) |
| IEC OSDP adoption | IEC 60839-11-5:2020, edition 1.0 | Record whether project/procurement cites SIA or IEC edition and applicable regional adoption | [OSDP](../02-protocols/access-control/osdp.md) |
| SIA 26-bit Wiegand | SIA AC-01-1996.10; legacy interface/format baseline | Do not select as a modern secure reader link; retain only for migration evidence | [Legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md) |
| ISO/IEC 14443 | Parts have independent edition/amendment status; Parts 1/3/4 are 2018 bases and Part 2 is 2020 in this snapshot | Pin every required part and amendment; RF/interface conformance does not define credential security | [Contactless and smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md) |
| ISO/IEC 15693 | Parts 1:2018, 2:2019, and **3:2026** in this snapshot | Do not cite the family without individual parts/editions | [Contactless and smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md) |
| ISO/IEC 7816 | Multi-part series with different editions; Part 4:2020 confirmed 2025 | Pin command/application/profile parts; ISO 7816 compatibility is not a credential assurance claim | [Contactless and smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md) |
| NFC Forum | Release 15 published June 2025; CR15/TR15.0 launched October 2025; Certification Release 15 **authorized May 2026** | Pin technical set, test release, authorized certification release, and product feature record separately | [NFC, BLE, and UWB](../02-protocols/access-control/nfc-ble-and-uwb.md) |
| Bluetooth Core | **6.3 adopted May 2026** | Pin controller/host/profile/features; adoption does not imply product supports every feature | [NFC, BLE, and UWB](../02-protocols/access-control/nfc-ble-and-uwb.md) |
| IEEE UWB base | IEEE 802.15.4-2024 active; 802.15.4z-2020 superseded; P802.15.4ab active project on snapshot date | Treat 4ab as draft/project work; product FiRa/ranging claims require exact feature/certification evidence | [NFC, BLE, and UWB](../02-protocols/access-control/nfc-ble-and-uwb.md) |
| FiRa | Core 4.0 specifications/certification announced December 2025 | Pin exact device role and certified feature set; “UWB” alone is insufficient | [NFC, BLE, and UWB](../02-protocols/access-control/nfc-ble-and-uwb.md) |
| Aliro | **1.0 introduced 2026-02-26** | New current baseline; require exact product/role/certification evidence and track early revisions | [Credential formats and mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md) |
| PKOC | Core/NFC/BLE **2.0.1 dated 2026-08-13**; PKOC over OSDP 1.63 approved 2024-03-22 | Record each component/binding version; do not infer product support | [Credential formats and mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md) |
| PIV | FIPS 201-3 current base; SP 800-73-5 Part 1 final 2024 | Select exact authentication mechanism and facility-access risk profile | [Credential formats and mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md) |
| SAML / OpenID Connect | SAML 2.0 and OpenID Connect Core 1.0 remain published enterprise-federation bases; OAuth security guidance continues through RFC updates | Pin metadata/issuer/audience/recipient, flow, token, client, and logout/session profile | [Enterprise federation](../02-protocols/infrastructure/enterprise-federation-saml-and-oidc.md) |
| SCIM | RFC 7643/7644 bases plus RFC 9865, RFC 9944, and RFC 9967 extensions reviewed | Pin schema/resource types, extension support, cursor model, async signalling, and reconciliation rules | [SCIM provisioning](../02-protocols/infrastructure/scim-identity-provisioning.md) |
| WebAuthn / CTAP | WebAuthn Level 2 final; Level 3 Candidate Recommendation; CTAP 2.3 Proposed Standard; CTAP 2.3.1 Working Draft | Do not present candidate/draft features as final; pin browser, platform, authenticator, and extension support | [WebAuthn, FIDO, and passkeys](../02-protocols/infrastructure/webauthn-fido-and-passkeys.md) |

## Alarm monitoring

| Family | Snapshot status | Engineering consequence | Canonical page |
|---|---|---|---|
| SIA DC-09 | **DC-09-2026**, current public listing; 2026 revision adds normative key-rotation capability | Purchase/use exact edition and verify both endpoint security/key-rotation modes | [SIA DC-09](../02-protocols/alarm-monitoring/sia-dc-09.md) |
| SIA DC-03 | Public listing **DC-03-2017** | Exact licensed timing/framing/code behavior required; treat as legacy security posture | [SIA DC-03](../02-protocols/alarm-monitoring/sia-dc-03.md) |
| Contact ID / SIA DC-05 | Public listing **DC-05-2016**; legacy DTMF format | No modern cryptographic security; validate carrier/gateway/receiver path | [Contact ID](../02-protocols/alarm-monitoring/contact-id-sia-dc-05.md) |
| SIA DC-07 | Public page says 2001.04 while store exposes a 2012 label: **edition conflict** | Identify the purchased normative copy; never guess frame/code rules | [SIA DC-07](../02-protocols/alarm-monitoring/sia-dc-07.md) |
| SIA AV-01 | Public listing **AV-01-2014** | Treat audio/DTMF/relay capabilities as privacy- and safety-sensitive | [SIA AV-01](../02-protocols/alarm-monitoring/sia-av-01.md) |
| IEC 60839-5 family | IEC 60839-5-1:2014, -5-2:2016, and -5-3:2016 are separate published parts; IEC TS 60839-7-8:2019 remains a Technical Specification | Obtain licensed parts and national adoption; do not treat the TS as a final International Standard | [IEC 60839 alarm transmission](../02-protocols/alarm-monitoring/iec-60839-alarm-transmission.md) |

## Building, industrial, and infrastructure

| Family | Snapshot status | Engineering consequence | Canonical page |
|---|---|---|---|
| BACnet | ANSI/ASHRAE **135-2024** current base used by committee updates; addenda/errata remain separately maintained | Obtain standard plus applicable addenda/errata and product PICS/certification | [BACnet family](../02-protocols/building-and-industrial/bacnet-family.md) |
| BACnet/SC | Current BACnet secure data-link option within maintained BACnet work | Verify node/hub/failover and certificate lifecycle; legacy links remain separate | [BACnet/SC](../02-protocols/building-and-industrial/bacnet-secure-connect.md) |
| Modbus application protocol | V1.1b3 remains the current publisher-listed application specification | Treat semantic/address model and transport mapping separately | [Modbus family](../02-protocols/building-and-industrial/modbus-family.md) |
| Modbus serial | Serial Line Protocol and Implementation Guide V1.02 is publisher-recommended for new serial implementations; an older 1996 document is labeled legacy-only | Record exact serial guide, electrical profile, and product limits | [Modbus RTU](../02-protocols/building-and-industrial/modbus-rtu.md) |
| Modbus Security | Publisher lists MB-TCP-Security v36, dated 2021-07-30 | Pin certificate/role profile and product support; port 802 alone proves nothing | [Modbus Security](../02-protocols/building-and-industrial/modbus-security.md) |
| OPC UA | Multi-part 1.05 line: Parts 1/2 and several others are 1.05.06; Parts 4/6/8/12/13/17/26 are 1.05.07 at this snapshot; other Parts differ | Pin every required Part/companion specification, profile, namespace/model version, and product certification | [OPC UA](../02-protocols/building-and-industrial/opc-ua.md) |
| KNX | Public **V3** set dated February 2025; member/certification **3.0.4** released 2025-08-22 and used for certification from end-August | Identify whether evidence is the public set, member document, or certification record; pin media/profile/secure feature and ETS project | [KNX](../02-protocols/building-and-industrial/knx.md) |
| DNP3 | IEEE 1815-2012 remains last published but is administratively inactive; superseding P1815 is an Active PAR/draft | Do not present P1815 as published; pin installed subset/profile and secure-authentication support | [DNP3](../02-protocols/building-and-industrial/dnp3.md) |
| IEC 60870-5-101/-104 | Published telecontrol companion profiles; IEC TS 60870-5-7:2025 and IEC 62351-5:2023 provide separate security context | Pin every base/companion/security part and national/product profile | [IEC 60870-5-101 and -104](../02-protocols/building-and-industrial/iec-60870-5-101-and-104.md) |
| IEC 61850 | Maintained multi-part utility-automation family with independently versioned SCL, communication mappings, conformance, and IEC 62351 security parts | Pin every required part, edition/amendment, logical model, SCL profile, and product conformance evidence | [IEC 61850](../02-protocols/building-and-industrial/iec-61850.md) |
| Matter | **Matter 1.6** is the current reviewed CSA release; camera support began in 1.5 and was refined in 1.5.1 | Pin device type, cluster, fabric/controller, certification, and ecosystem support; never infer PACS/ONVIF/fire capability | [Matter](../02-protocols/building-and-industrial/matter.md) |
| RADIUS over TLS / RADIUS 1.1 | RFC 6614 and RFC 9765 are both Experimental; RFC 9765 requires TLS 1.3 and removes legacy MD5 packet mechanisms | Require explicit bilateral support and certificate/identity policy; do not treat RFC status as deployment approval | [AAA and network access](../02-protocols/infrastructure/aaa-and-network-access.md) |
| TLS | TLS 1.3 RFC 8446 current base; TLS 1.2 remains deployed under current policy constraints | Use current algorithm/profile policy and product capability; never silently downgrade | [TLS, PKI, and secure transport](../02-protocols/infrastructure/tls-pki-and-secure-transport.md) |
| NTP / NTS | NTPv4 RFC 5905; NTS RFC 8915 | NTS support must be explicit; security and clock accuracy are separate evidence | [Time synchronisation](../02-protocols/infrastructure/time-synchronisation.md) |
| SNMP | SNMPv3 architecture/USM current standards family; v1/v2c remain legacy deployments | Prefer authenticated privacy mode where supported; pin MIB revisions | [Monitoring and administration](../02-protocols/infrastructure/monitoring-and-secure-administration.md) |

## How to use this register

For a design or compatibility record, copy none of the rows blindly. Instead record:

1. publisher and exact title;
2. edition/version/date and amendments/errata;
3. normative role, profile, options, and required/conditional features;
4. certification/conformance program and exact product/firmware listing;
5. product-declared capability plus configuration evidence;
6. owner-controlled interoperability, negative, failure, and recovery results;
7. migration trigger, withdrawal date, and next review.

Update this page when a listed publisher changes a revision, lifecycle date, test program, or release-candidate state. Do not update `last_verified` merely because prose was edited.

## Sources

- **ONVIF-HISTORY** — [ONVIF Specification History][ONVIF-HISTORY], including June 2026 release, accessed 2026-08-25.
- **ONVIF-PROFILES** — [ONVIF Profiles, Add-ons and Specifications][ONVIF-PROFILES], lifecycle status accessed 2026-08-25.
- **IETF-RFC** — [IETF Datatracker RFC index][IETF-RFC], individual RFC status pages accessed 2026-08-25.
- **W3C-WEBRTC** — [WebRTC: Real-Time Communication in Browsers][W3C-WEBRTC], W3C Recommendation, 13 March 2025.
- **MQTT5** — [MQTT Version 5.0][MQTT5], OASIS Standard, 7 March 2019.
- **SIA-OSDP** — [Open Supervised Device Protocol][SIA-OSDP], Security Industry Association, accessed 2026-08-25.
- **SIA-INDEX** — [At-a-Glance Guide to SIA Standards][SIA-INDEX], Security Industry Association, accessed 2026-08-25.
- **NFC-SPECS** — [NFC Forum Specifications][NFC-SPECS], accessed 2026-08-25.
- **BT63** — [Bluetooth Core Specification 6.3][BT63], Bluetooth SIG, adopted May 2026.
- **IEEE154** — [IEEE 802.15.4-2024][IEEE154], IEEE Standards Association.
- **FIRA4** — [FiRa Core 4.0 specifications and certification announcement][FIRA4], FiRa Consortium, 3 December 2025.
- **ALIRO** — [Introducing Aliro 1.0][ALIRO], Connectivity Standards Alliance, 26 February 2026.
- **PKOC** — [Secure Credential Interoperability and PKOC][PKOC], PSIA, status dated 13 August 2026.
- **BACNET-UPDATES** — [BACnet standard and addenda status][BACNET-UPDATES], ASHRAE BACnet Committee, accessed 2026-08-25.
- **MODBUS** — [Modbus specifications and implementation guides][MODBUS], Modbus Organization, accessed 2026-08-25.
- **OPCUA** — [OPC UA Part 1 v1.05.06][OPCUA], OPC Foundation, published 22 October 2025.
- **KNX304** — [KNX Standard Version 3.0.4][KNX304], KNX Association, 22 August 2025.

[ONVIF-HISTORY]: https://www.onvif.org/profiles/specifications/specification-history/
[ONVIF-PROFILES]: https://www.onvif.org/profiles-add-ons-specifications/
[IETF-RFC]: https://datatracker.ietf.org/doc/
[W3C-WEBRTC]: https://www.w3.org/TR/webrtc/
[MQTT5]: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
[SIA-OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[SIA-INDEX]: https://www.securityindustry.org/industry-standards/at-a-glance-guide-to-sia-standards/
[NFC-SPECS]: https://nfc-forum.org/build/specifications
[BT63]: https://www.bluetooth.com/specifications/specs/core-specification-6-3/
[IEEE154]: https://standards.ieee.org/ieee/802.15.4/11041/
[FIRA4]: https://firaconsortium.org/news/press-releases/2025/12/fira-consortium-unveils-fira-core-4-0-specifications-and-certification
[ALIRO]: https://csa-iot.org/newsroom/introducing-aliro-1-0-a-unified-standard-to-transform-the-access-control-ecosystem/
[PKOC]: https://psialliance.org/securecredentials/
[BACNET-UPDATES]: https://bacnet.org/updates/
[MODBUS]: https://www.modbus.org/modbus-specifications
[OPCUA]: https://reference.opcfoundation.org/specs/OPC-10000-1/v1.05.06
[KNX304]: https://www.knx.org/news/knx-launches-knx-standard-version-304
