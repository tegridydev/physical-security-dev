---
title: "Diagram index"
summary: "A curated navigation index for the knowledge base's text-native architectures, flows, state models, boundaries, and data-layout figures."
page_type: index
domains:
  - cross-domain
tags:
  - diagrams
  - architecture
  - data-flow
  - navigation
  - text-figures
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: "Curated page-level navigation; figures are explanatory and never normative topology, product support, electrical design, or site evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Diagram index

[Home](../README.md) / [Reference](README.md) / Diagram index

The knowledge base uses fenced plain-text figures so architecture remains readable in ordinary Markdown without a site generator. Figures explain roles and boundaries; they do not prescribe a product topology, pinout, electrical design, firewall rule, safety circuit, or command procedure.

## Reading conventions

| Mark | Meaning unless the page says otherwise |
|---|---|
| `→` or `──>` | Direction of request, data, event, trust promotion, or intended flow—not necessarily a persistent connection |
| `↔` | Bidirectional exchange; does not imply equal authority or symmetric security |
| `↓` | Encapsulation, processing stage, dependency, or transition |
| `[component]` / named box | Logical role, not necessarily a separate host/product |
| Dashed/logical boundary | Trust, responsibility, or processing boundary; consult surrounding prose |
| Branch/state arrow | Possible transition, not proof that every product supports it |

Always read the text immediately before and after a figure. The canonical standard, product evidence, configuration, and environment-validation record outrank a teaching diagram.

## Orientation and foundations

| Page | Figure focus | Use it for |
|---|---|---|
| [Physical-security protocol landscape](../physical-security-protocol-landscape.md) | Layered integration path and cross-domain map | Locating protocols between physical interfaces, transport, application, system, and operations |
| [Scope and boundaries](../00-start-here/scope-and-boundaries.md) | Physical-effect boundary | Distinguishing research/observation from a real-world control path |
| [Architecture and layering](../01-foundations/architecture-and-layering.md) | Layer stack, encapsulation, profile/product chain | Classifying a claim at the correct layer |
| [Physical-security system architecture](../01-foundations/physical-security-system-architecture.md) | Reference topology and shared services | Identifying edge devices, controllers, management, integrations, and trust boundaries |
| [Networking fundamentals](../01-foundations/networking-fundamentals.md) | End-to-end layered network path | Separating link, IP, transport, TLS, and application failures |
| [Trust boundaries and segmentation](../01-foundations/trust-boundaries-and-segmentation.md) | Zones and conduits | Recording where identity, authority, and consequence cross a boundary |
| [Architecture and layering](../01-foundations/architecture-and-layering.md) | Encapsulation versus semantic equivalence | Avoiding the assumption that a gateway preserves every property |
| [Credentials and identity media](../01-foundations/credentials-and-identity-media.md) | Subject-to-credential-to-reader-to-controller chain | Finding where proof can be reduced to an identifier |
| [Identity, authentication, and authorization](../01-foundations/identity-authentication-and-authorization.md) | Identity decision and physical-access chains | Separating identity, authentication, policy, command, and observed result |
| [Events, state, commands, and time](../01-foundations/events-state-commands-and-time.md) | State reconstruction and command lifecycle | Preserving distinct occurrence, delivery, acceptance, and physical milestones |
| [Encoding and serialization](../01-foundations/encoding-and-serialization.md) | Bytes-to-validated-domain-object pipeline | Placing bounds, decoding, schema, and semantic validation |
| [Interoperability, conformance, and profiles](../01-foundations/interoperability-conformance-and-profiles.md) | Capability record and conformance chain | Turning broad support claims into testable product/role evidence |
| [Media streaming fundamentals](../01-foundations/media-streaming-fundamentals.md) | Capture, encode, signal, transport, decode path | Locating media/control/security/capacity responsibilities |
| [Multicast, discovery, and NAT](../01-foundations/multicast-discovery-and-nat.md) | Secure enrollment path | Keeping discovery separate from trusted inventory and authorization |
| [Observability and evidence](../01-foundations/observability-and-evidence.md) | Layered health model | Diagnosing service without collapsing link, protocol, data, and physical health |
| [Ethernet, PoE, and power budgets](../01-foundations/ethernet-poe-and-power-budgets.md) | End-to-end power chain | Accounting for PSE, channel loss, PD, accessories, and degraded supply |
| [Serial and field interfaces](../01-foundations/serial-and-field-interfaces.md) | Multidrop bus record | Separating electrical, wiring, UART, framing, and application layers |
| [Dry contacts and supervised circuits](../01-foundations/dry-contacts-and-supervised-circuits.md) | Relay command versus physical feedback | Avoiding “relay energized equals physical result” |
| [TLS, PKI, and certificates](../01-foundations/tls-pki-and-certificates.md) | Certificate/trust lifecycle | Planning enrollment, validation, rotation, revocation, and recovery |

## Protocol figures — access control and credentials

| Page | Figure focus | Boundary highlighted |
|---|---|---|
| [Access-control protocol map](../02-protocols/access-control/README.md) | Credential, reader, controller, PACS, and opening | Medium, proof, link, decision, and physical effect are separate |
| [OSDP](../02-protocols/access-control/osdp.md) | Bus topology, frame/exchange, Secure Channel provisioning, ACU state | RS-485, protocol state, cryptographic state, and high-impact output |
| [Legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md) | Wiegand 26-bit layout and offline decode shape | Bit format does not add link authentication or supervision |
| [Contactless and smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md) | ISO layer map and APDU command/response shapes | RF/contact transport is separate from credential application security |
| [NFC, BLE, and UWB](../02-protocols/access-control/nfc-ble-and-uwb.md) | Multi-radio layers and conceptual access state machine | Discovery/range is not identity; reader/controller proof remains required |
| [Credential formats and mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md) | Assurance chain and static bit-layout anatomy | Namespace and cryptographic proof can be lost by output conversion |

## Protocol figures — video, media, web, and messaging

| Page | Figure focus | Boundary highlighted |
|---|---|---|
| [Protocol families](../02-protocols/README.md) | Protocol reference reading stack | Physical/electrical, framing, transport, application, profile, product |
| [ONVIF](../02-protocols/video-and-media/onvif.md) | ONVIF service/discovery/media stack | WS-Discovery, SOAP services, media control, stream, and product profile |
| [GB/T 28181](../02-protocols/video-and-media/gbt-28181.md) | SIP-domain registration, catalogue, signalling, events, and media path | National application profile, platform/device role, media, and security requirements remain separate |
| [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) | On-demand session sequence | Control negotiation, SDP description, RTP media, RTCP telemetry |
| [WebRTC](../02-protocols/video-and-media/webrtc.md) | Signaling, ICE/STUN/TURN, DTLS-SRTP path | Application signaling authority versus protected peer/relay media |
| [SIP and SRTP](../02-protocols/video-and-media/sip-and-srtp.md) | Intercom call flow | SIP signaling, SDP offer/answer, RTP/SRTP, and separately authorized door control |
| [SRT and RIST](../02-protocols/video-and-media/srt-and-rist.md) | Contribution sender/network/receiver boundary | Recovery and transport security do not add entitlement, application authorization, or evidential provenance |
| [MQTT](../02-protocols/web-and-messaging/mqtt.md) | Broker architecture and topic hierarchy | Producer/broker/consumer identities, sessions, retained state, and ACLs |
| [AMQP 1.0](../02-protocols/web-and-messaging/amqp-1-0.md) | Container/session/link flow and settlement boundary | Credit and delivery settlement remain distinct from downstream workflow and physical outcome |
| [CoAP, OSCORE, and LwM2M](../02-protocols/web-and-messaging/coap-oscore-and-lwm2m.md) | Constrained exchange, proxy, object-security, and management roles | Transport ACK, object security, device management, and physical result are separate |
| [CAP and EDXL emergency messaging](../02-protocols/web-and-messaging/cap-and-edxl-emergency-messaging.md) | Alert/update/cancel chain and EDXL distribution envelope | Issuer, profile, geography, delivery, presentation, and activation remain separate evidence |
| [SOAP and XML](../02-protocols/web-and-messaging/soap-and-xml.md) | Envelope anatomy | Transport, XML namespace/schema, SOAP headers/body, action and fault processing |
| [WebSocket, SSE, and webhooks](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) | SSE event-stream wire shape | Long-lived stream framing and event contract; not delivery durability |

## Protocol figures — alarm monitoring

| Page | Figure focus | Boundary highlighted |
|---|---|---|
| [Alarm-monitoring protocols](../02-protocols/alarm-monitoring/README.md) | Premises-to-receiver-to-automation path | Transport/report acceptance, automation ingest, operator response, and dispatch |
| [Contact ID / SIA DC-05](../02-protocols/alarm-monitoring/contact-id-sia-dc-05.md) | DTMF communicator/receiver sequence | Handshake/message/kissoff versus automation/operator handling |
| [SIA AV-01](../02-protocols/alarm-monitoring/sia-av-01.md) | Operator audio-verification path | Voice/DTMF, premises session, privacy, relay actuation |
| [SIA DC-03](../02-protocols/alarm-monitoring/sia-dc-03.md) | Communicator-to-receiver framing path | Message blocks, parser, acknowledgement, and security wrapper |
| [SIA DC-07](../02-protocols/alarm-monitoring/sia-dc-07.md) | Receiver-to-automation feed | Durable acceptance/backpressure and downstream routing |
| [SIA DC-09](../02-protocols/alarm-monitoring/sia-dc-09.md) | IP alarm reporting path | Sender/account identity, receiver ACK, encryption, retry, and dispatch boundary |
| [IEC 60839 alarm transmission](../02-protocols/alarm-monitoring/iec-60839-alarm-transmission.md) | Premises, transmission-network, receiving-centre, and response boundaries | Independently versioned IEC parts and national/product profiles must not be collapsed |

## Protocol figures — building, industrial, and legacy interoperability

| Page | Figure focus | Boundary highlighted |
|---|---|---|
| [BACnet Secure Connect](../02-protocols/building-and-industrial/bacnet-secure-connect.md) | Node/hub/failover topology | TLS/PKI secure link versus BACnet object/write semantics and legacy segments |
| [Modbus family](../02-protocols/building-and-industrial/modbus-family.md) | Application PDU mapped to serial/TCP/security carriers | Shared function/register semantics do not equal identical transport/security |
| [Modbus RTU](../02-protocols/building-and-industrial/modbus-rtu.md) | RTU frame and receive state | Inter-character timing, address/function/data/CRC, bus/gateway behavior |
| [Modbus TCP](../02-protocols/building-and-industrial/modbus-tcp.md) | MBAP/PDU over TCP stream | TCP chunks are not message boundaries; transaction and unit IDs remain distinct |
| [Matter](../02-protocols/building-and-industrial/matter.md) | Commissioner, fabric, controller, bridge, and node trust model | Attestation, operational identity, ACL authorization, application state, and physical outcome differ |
| [IEC 60870-5-101 and -104](../02-protocols/building-and-industrial/iec-60870-5-101-and-104.md) | Telecontrol station/ASDU/gateway paths | Serial/TCP carriers, addresses, cause, quality, time, security, and command authority remain explicit |
| [IEC 61850](../02-protocols/building-and-industrial/iec-61850.md) | Logical model, SCL engineering, MMS, GOOSE, and SV paths | Engineering configuration, client/server, multicast, security, and protection/control coupling differ |
| [Enterprise federation with SAML and OIDC](../02-protocols/infrastructure/enterprise-federation-saml-and-oidc.md) | Identity-provider, application, claims, and local-role boundary | Federation authentication never substitutes for local high-impact authorization |
| [SCIM identity provisioning](../02-protocols/infrastructure/scim-identity-provisioning.md) | Authoritative identity, provisioning client/service, PACS adapter, and reconciliation | API acceptance, source lifecycle, downstream state, and physical access rights differ |
| [WebAuthn, FIDO, and passkeys](../02-protocols/infrastructure/webauthn-fido-and-passkeys.md) | Relying party, browser/client, authenticator, and recovery boundary | Web authentication is distinct from PACS credential presentation and physical authorization |
| [Pelco-D and Pelco-P](../02-protocols/interoperability-and-legacy/pelco-d-and-p.md) | Legacy serial PTZ path | Non-normative legacy orientation and physical movement consequence |
| [PSIA PLAI](../02-protocols/interoperability-and-legacy/psia-plai.md) | Logical-area synchronization path | Identity/access semantics, synchronization authority, and extension mapping |

## System figures — access control

| Page | Figure focus |
|---|---|
| [Access-control systems](../03-systems/access-control/README.md) | End-to-end access decision chain |
| [PACS architecture](../03-systems/access-control/pacs-architecture.md) | PACS services, controllers, readers, identity sources, operations |
| [Panels, readers, and door I/O](../03-systems/access-control/panels-readers-and-door-io.md) | Controller/reader/input/output/lock feedback chain |
| [Credential lifecycle](../03-systems/access-control/credential-lifecycle.md) | Proofing, issuance, activation, use, suspension/revocation, retirement |
| [Mobile access](../03-systems/access-control/mobile-access.md) | Issuer/cloud/mobile/reader/controller path |
| [Pedestrian portals, turnstiles, and interlocked doors](../03-systems/access-control/pedestrian-portals-turnstiles-and-interlocked-doors.md) | Access grant, actuator, barrier/door state, occupancy, and passage chain |
| [Offline operation and anti-passback](../03-systems/access-control/offline-operation-and-anti-passback.md) | Online/offline authority, cache, reconciliation, anti-passback state |
| [Biometrics](../03-systems/access-control/biometrics.md) | Capture/template/matcher/decision and privacy boundary |
| [Locks, egress, and life safety](../03-systems/access-control/locks-egress-and-life-safety.md) | Access command versus egress/fire/local hardware authority |
| [Visitor, identity, and elevator integration](../03-systems/access-control/visitor-identity-and-elevator-integration.md) | Identity/visitor/PACS/lift integration and authority boundaries |

## System figures — integration platforms

| Page | Figure focus |
|---|---|
| [Integration platforms](../03-systems/integration-platforms/README.md) | Cross-domain adapter/broker/platform boundary |
| [PSIM and command platforms](../03-systems/integration-platforms/psim-and-command-platforms.md) | Event correlation, operator workflow, commands, and system-of-record boundary |
| [SIEM, SOAR, and case management](../03-systems/integration-platforms/siem-soar-and-case-management.md) | Security event/case/automation path and actuation separation |
| [BMS and SCADA integration](../03-systems/integration-platforms/bms-and-scada-integration.md) | Physical security to building/OT gateway and write authority |
| [HR, identity, and visitor integration](../03-systems/integration-platforms/hr-identity-and-visitor-integration.md) | Joiner/mover/leaver and identity synchronization boundaries |
| [Cloud, mobile, and multi-tenant platforms](../03-systems/integration-platforms/cloud-mobile-and-multi-tenant-platforms.md) | Tenant, regional cloud, mobile, edge, and dependency boundaries |

## System figures — intercom, intrusion, and perimeter

| Page | Figure focus |
|---|---|
| [Intercom system architecture](../03-systems/intercom-and-emergency-communications/intercom-system-architecture.md) | Endpoint/call server/media/door/recording topology |
| [Call routing, media, and door control](../03-systems/intercom-and-emergency-communications/call-routing-media-and-door-control.md) | Signaling/media route and separate physical-control authorization |
| [Emergency phones, mass notification, and PA](../03-systems/intercom-and-emergency-communications/emergency-phones-mass-notification-and-pa.md) | Emergency call/message sources, distribution, acknowledgement, and certified boundaries |
| [Intrusion-monitoring systems](../03-systems/intrusion-monitoring/README.md) | Sensor-to-panel-to-receiver-to-operator event lifecycle |
| [Panels, zones, and sensors](../03-systems/intrusion-monitoring/panels-zones-and-sensors.md) | Detection/electrical zone/panel/event semantics |
| [Communicators, receivers, and monitoring](../03-systems/intrusion-monitoring/communicators-receivers-and-monitoring.md) | Supervised reporting, ACK, automation, and operator path |
| [Duress, panic, and fire boundaries](../03-systems/intrusion-monitoring/duress-panic-and-fire-boundaries.md) | High-impact alarm categories and dispatch/life-safety separation |
| [Perimeter security architecture](../03-systems/perimeter-and-detection/perimeter-security-architecture.md) | Sensors/zones/analytics/command-center/response boundary |
| [ANPR/LPR systems](../03-systems/perimeter-and-detection/anpr-lpr-systems.md) | Capture/OCR/match/event/retention pipeline |
| [Gates, barriers, and vehicle access](../03-systems/perimeter-and-detection/gates-barriers-and-vehicle-access.md) | Credential/detection/controller/safety-device/movement/feedback chain |

## System figures — video surveillance

| Page | Figure focus |
|---|---|
| [Video-surveillance systems](../03-systems/video-surveillance/README.md) | Capture, recording, viewing, event, and management paths |
| [Cameras and encoders](../03-systems/video-surveillance/cameras-and-encoders.md) | Optical capture through encoder, stream, metadata, and device services |
| [Recording, storage, and retention](../03-systems/video-surveillance/recording-storage-and-retention.md) | Recording lifecycle and capacity relationship |
| [Analytics and metadata](../03-systems/video-surveillance/analytics-and-metadata.md) | Frames-to-model-to-metadata/event pipeline |
| [PTZ and device I/O](../03-systems/video-surveillance/ptz-and-device-io.md) | Command arbitration, motor/output actuation, and feedback |
| [Health and service monitoring](../03-systems/video-surveillance/health-and-service-monitoring.md) | Layered health and service-response workflow |
| [Evidence export and integrity](../03-systems/video-surveillance/evidence-export-and-integrity.md) | Export manifest, custody, validation, and release boundary |

## Data layouts, formulas, and record fixtures

These fenced figures are useful references but are not architecture diagrams.

| Page | Fixture |
|---|---|
| [Legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md) | Synthetic 26-bit Wiegand layout and offline decoder shape |
| [Contactless and smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md) | ISO 7816 APDU command/response field shapes and synthetic fixture |
| [Credential formats and mobile credentials](../02-protocols/access-control/credential-formats-and-mobile-credentials.md) | Static credential bit-layout and safe record shape |
| [SOAP and XML](../02-protocols/web-and-messaging/soap-and-xml.md) | SOAP envelope fixture |
| [MQTT event contract example](../05-development-and-integration/examples/mqtt-event-contract.md) | Synthetic topic and event payload |
| [Modbus read-response example](../05-development-and-integration/examples/modbus-read-response.md) | Synthetic byte sequence and field interpretation |
| [Video bandwidth/storage lab](../08-defensive-labs/video-bandwidth-and-storage-calculation.md) | Capacity formula and synthetic scenario worksheet |
| [Media bandwidth and storage reference](media-bandwidth-and-storage.md) | Unit-safe formulas and synthetic calculation |
| [Cabling, power, and distance caveats](cabling-power-and-distance-caveats.md) | Voltage-drop formulas and PoE budget chain |
| [Integration readiness checklist](integration-readiness-checklist.md) | Readiness evidence record template |
| [Safety impact checklist](safety-impact-checklist.md) | High-impact review record template |

Code/protocol fixtures are also indexed by [code example index](code-example-index.md).

## What is intentionally not indexed as a diagram

- YAML front-matter examples in the metadata policy;
- citation-format examples;
- ordinary JSON/XML/SDP/HTTP/SIP message examples unless they materially illustrate a layout;
- source code listings, which belong in the code example index;
- tables that already serve as the clearer comparison form.

## Maintenance checklist

- [ ] Add a page here only when a figure materially explains architecture, sequence, state, boundary, or data layout
- [ ] Use a page-level link so heading renames do not create fragile anchors
- [ ] Describe the decision/boundary, not merely repeat the page title
- [ ] Keep figures text-native and legible without rendering or color
- [ ] Add a legend locally when arrows/boxes differ from the conventions above
- [ ] Mark conceptual, synthetic, non-normative, or release-candidate content in surrounding prose
- [ ] Never use a diagram as product-support, conformance, electrical, safety, or deployment evidence
- [ ] Reconcile this index during repository review after adding or removing a figure
