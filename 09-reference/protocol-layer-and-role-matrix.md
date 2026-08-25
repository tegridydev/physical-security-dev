---
title: Protocol Layer and Role Matrix
summary: Maps important protocol families to communication layers, typical roles, data direction, and companion technologies.
page_type: reference
domains: [video, access-control, alarms, intercom, bms, ot, networking, cross-domain]
tags: [protocols, layers, roles, matrix]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [ONVIF Profiles, GB/T 28181-2022, OSDP, MQTT 5.0, AMQP 1.0, Modbus, BACnet, OPC UA, IEC 60870-5, IEC 61850, Matter 1.6]
coverage_limit: Architectural mapping only; editions, options, security modes, transports, and product roles require exact verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Protocol layer and role matrix

A single solution typically uses several rows. “Over IP” is not a complete protocol description, and technologies at different layers are not alternatives.

| Family | Primary layer/model | Typical roles | Direction/model | Common companions | Canonical page |
|---|---|---|---|---|---|
| ONVIF | Application profiles and web services | Device, client, media service, recording/search, access roles | Request/response plus events/media | HTTP(S), SOAP/XML, WS-Discovery, RTSP/RTP, MQTT conditionally | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| GB/T 28181 | Video-surveillance application/domain protocol | SIP domain, device, platform, catalogue/event/media roles | Registration, catalogue/events, SIP session control, RTP media | SIP, SDP, RTP/RTCP, XML, GB 35114 security | [GB/T 28181](../02-protocols/video-and-media/gbt-28181.md) |
| RTSP | Media-session control | Client and media server | Stateful request/response | SDP, RTP/RTCP, authentication, TLS in supported profiles | [RTSP/RTP/SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| RTP/RTCP | Real-time media/data transport and control | Sender, receiver, mixer/translator | Usually datagram flows plus reports | SDP, RTSP/SIP/WebRTC, SRTP | [RTSP/RTP/SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| WebRTC | Secure real-time communications suite | Browser/native peers and signaling/relay services | Peer media/data with application-defined signaling | ICE, STUN, TURN, DTLS-SRTP, SDP | [WebRTC](../02-protocols/video-and-media/webrtc.md) |
| SIP | Session signaling | User agents, proxies, registrars, B2BUAs | Request/response and dialogs | SDP, RTP/SRTP, TLS, digest or deployment identity | [SIP and SRTP](../02-protocols/video-and-media/sip-and-srtp.md) |
| SRT / RIST | Media contribution transport families | Sender/caller/listener or RIST sender/receiver roles | Long-lived contribution media flow with retransmission/recovery profile | Encoded media, encryption/profile, network QoS, application authorization | [SRT and RIST](../02-protocols/video-and-media/srt-and-rist.md) |
| OSDP | Access peripheral application protocol | Control panel and peripheral device | Addressed bidirectional bus; poll/reply model | Commonly RS-485; Secure Channel | [OSDP](../02-protocols/access-control/osdp.md) |
| Wiegand interface | Legacy electrical/data interface | Reader to controller | Primarily one-way pulses | Credential formats and vendor wiring | [Legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md) |
| SIA DC-09 | Alarm transport/application framing | Premises transmitter and central-station receiver | Supervised event delivery and acknowledgement | IP transport; underlying SIA/contact formats as applicable | [DC-09](../02-protocols/alarm-monitoring/sia-dc-09.md) |
| SIA DC-03 / DC-05 | Alarm message formats | Alarm panel/transmitter and receiver | Event records | DC-09, dial/receiver product transport | [Alarm protocols](../02-protocols/alarm-monitoring/README.md) |
| IEC 60839-5 | Alarm-transmission system/equipment/network family | Supervised premises, transmission-network, receiving-centre roles | Requirements split across independently versioned parts | National adoption, product profile, monitoring procedure | [IEC 60839 alarm transmission](../02-protocols/alarm-monitoring/iec-60839-alarm-transmission.md) |
| HTTP/REST-style APIs | Web transport/application convention | Client and server/resource service | Request/response | TLS, OAuth/OIDC, mTLS, JSON/XML, webhook | [HTTP and REST](../02-protocols/web-and-messaging/http-and-rest.md) |
| SOAP/XML | Contracted web services/serialization | Service client and server | Request/response and extension frameworks | HTTP(S), WSDL, WS-* | [SOAP and XML](../02-protocols/web-and-messaging/soap-and-xml.md) |
| MQTT | Brokered application messaging | Publisher, subscriber, broker | Publish/subscribe with session/QoS semantics | TCP, TLS, client identity, topic ACL, payload schema | [MQTT](../02-protocols/web-and-messaging/mqtt.md) |
| AMQP 1.0 | Message-oriented application protocol | Container, connection/session/link endpoints; sender and receiver | Credit-based links and settlement | TCP, TLS, SASL, broker/router policy, application schema | [AMQP 1.0](../02-protocols/web-and-messaging/amqp-1-0.md) |
| CoAP / OSCORE / LwM2M | Constrained REST-like exchange, object security, and management profile | Client/server; origin/proxy; LwM2M client/server/bootstrap roles | Request/response, observe, block-wise, managed objects | UDP/TCP/WebSocket, DTLS/TLS, OSCORE, object model | [CoAP, OSCORE, and LwM2M](../02-protocols/web-and-messaging/coap-oscore-and-lwm2m.md) |
| CAP / EDXL-DE | Emergency message and distribution-envelope formats | Alert issuer, aggregator, distributor, consumer | Alert/update/cancel lifecycle and routed XML messages | HTTPS/message transport, regional profile, XML signatures under explicit profile | [CAP and EDXL](../02-protocols/web-and-messaging/cap-and-edxl-emergency-messaging.md) |
| WebSocket | Full-duplex application channel | Client and server | Long-lived bidirectional messages | HTTP upgrade, TLS, application authentication/schema | [WebSocket/SSE/webhook](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) |
| Modbus RTU | Industrial application protocol over serial framing | Client/master and server/slave devices | Request/reply | Serial line, vendor register map | [Modbus RTU](../02-protocols/building-and-industrial/modbus-rtu.md) |
| Modbus/TCP | Industrial application protocol over TCP | Client and server | Request/reply with transaction identifiers | TCP/IP, segmentation; Modbus Security where supported | [Modbus/TCP](../02-protocols/building-and-industrial/modbus-tcp.md) |
| BACnet | Building-automation objects/services | BACnet devices and clients; routers; management systems | Request/reply, notifications, discovery | BACnet/IP, MS/TP, or BACnet/SC data links | [BACnet family](../02-protocols/building-and-industrial/bacnet-family.md) |
| BACnet/SC | Secure BACnet data link | Nodes and hubs | TLS-protected WebSocket connections | BACnet application/network layers, PKI | [BACnet/SC](../02-protocols/building-and-industrial/bacnet-secure-connect.md) |
| KNX | Building-control application/system family | Sensors, actuators, controllers, management tools | Group communication and configuration | TP/RF/IP/IPv6 media; Data/IP Secure where applicable | [KNX](../02-protocols/building-and-industrial/knx.md) |
| OPC UA | Information modeling and service framework | Clients, servers, publishers/subscribers | Services and PubSub models | UA Secure Conversation, application certs, user identity | [OPC UA](../02-protocols/building-and-industrial/opc-ua.md) |
| IEC 60870-5-101/-104 | Telecontrol application companion profiles | Controlling station, controlled station, gateway | ASDUs over serial or TCP profile | IEC 62351 security, time/quality/address model | [IEC 60870-5-101 and -104](../02-protocols/building-and-industrial/iec-60870-5-101-and-104.md) |
| IEC 61850 | Utility information model and communication mappings | IEDs, clients/servers, publishers/subscribers, engineering tools | MMS services plus GOOSE/SV multicast and SCL engineering | Ethernet, time, IEC 62351, conformance/profile | [IEC 61850](../02-protocols/building-and-industrial/iec-61850.md) |
| Matter | Fabric-based IP application protocol | Commissioner, controller, administrator, node, bridge | Commissioning, cluster commands/attributes/events | IPv6, Thread/Wi-Fi/Ethernet, certificates, attestation, ACLs | [Matter](../02-protocols/building-and-industrial/matter.md) |
| SAML / OIDC | Enterprise federation protocols | Identity provider/openid provider, service/relying party, client | Assertions or authorization-code/token/user-info flows | HTTPS, metadata/JWKs, OAuth security profile, local role mapping | [Enterprise federation](../02-protocols/infrastructure/enterprise-federation-saml-and-oidc.md) |
| SCIM | Identity provisioning protocol/schema | Provisioning client and service provider | Resource CRUD, bulk/filter, cursor and event-assisted reconciliation | HTTPS, OAuth/mTLS profile, authoritative identity lifecycle | [SCIM](../02-protocols/infrastructure/scim-identity-provisioning.md) |
| WebAuthn / CTAP | Web authentication and authenticator protocol | Relying party, client/browser, authenticator | Challenge/response registration and authentication ceremonies | HTTPS origin, FIDO credentials, CTAP transports, recovery policy | [WebAuthn and FIDO](../02-protocols/infrastructure/webauthn-fido-and-passkeys.md) |
| SNMP | Network/device management | Manager and agent | Polling plus notifications | UDP/TCP profiles; SNMPv3 security | [Monitoring/admin](../02-protocols/infrastructure/monitoring-and-secure-administration.md) |
| Syslog | Event/log transport and message format family | Originator, relay, collector | Push/event stream | UDP/TCP/TLS profiles, time and integrity pipeline | [Monitoring/admin](../02-protocols/infrastructure/monitoring-and-secure-administration.md) |
| NTP/NTS/PTP | Time distribution | Clients/servers or clock hierarchy | Request/response or precision time messages | DNS, PKI/keys, network timing design | [Time](../02-protocols/infrastructure/time-synchronisation.md) |
| TLS | Secure transport/session | Client and server peers | Authenticated protected channel | TCP/application protocol, X.509/PKI, sometimes PSK | [TLS](../02-protocols/infrastructure/tls-pki-and-secure-transport.md) |

## Questions the matrix cannot answer

- Which product role and optional features are actually supported?
- Is the secure mode enabled with an acceptable key lifecycle?
- What semantics and safety consequence does a field or command carry?
- Can an event be replayed, duplicated, reordered, or lost?
- Which component remains authoritative during partitions?
- Is a product licensed and conformant for the exact firmware version?

Resolve those questions in the linked family page, applicable system page, product documentation, and an approved environment-validation record.
