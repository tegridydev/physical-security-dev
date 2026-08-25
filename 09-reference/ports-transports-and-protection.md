---
title: "Ports, transports, and protection"
summary: "A cautious lookup for registered service ports, actual transport selection, and the protection boundary that an integration must verify."
page_type: reference
domains:
  - cross-domain
tags:
  - ports
  - transports
  - tls
  - firewall
  - network-policy
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "IANA Service Name and Transport Protocol Port Number Registry"
  - "RFC 6335"
  - "RFC 8446"
coverage_limit: "Registered and standards-defined defaults only; listener configuration, product support, negotiated protocol, firewall policy, and deployment security are not inferred from a port number."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Ports, transports, and protection

[Home](../README.md) / [Reference](README.md) / Ports, transports, and protection

> This is a planning summary, not a normative port list or firewall rule set. IANA explicitly warns that assignment does not endorse traffic and does not prove that traffic on a port is the assigned service. Confirm the exact product, firmware, listener, transport, address family, proxy path, and security mode. [IANA-PORTS]

## Keep four facts separate

| Fact | Question | Evidence |
|---|---|---|
| Service convention | Which port is registered or specified? | IANA registry and the protocol specification |
| Deployed listener | Where is this instance actually listening? | Approved configuration and owner-controlled validation |
| Transport | TCP, UDP, SCTP, QUIC, serial, or another carrier? | Negotiation/configuration and packet-level evidence |
| Protection | What authenticates, encrypts, authorizes, and limits the exchange? | TLS/security profile, credentials, ACLs, and application policy |

A port is not an identity, an authorization decision, a discovery method, or proof of encryption. TLS on a conventional secure port can still be misconfigured; a protocol on a non-default port does not become malicious or secure because of the number.

## Registered and standards-defined orientation

“Registered” below means an IANA entry exists. “Specified” means the cited protocol assigns the value. Products may use a configurable or entirely different port. Dual entries in IANA do not mean every protocol implementation supports both transports.

| Family | Registered or specified endpoint | Intended orientation | Important qualification |
|---|---:|---|---|
| DNS | 53/TCP and 53/UDP | Name resolution | Transport choice depends on message and resolver policy; DNS identity is not application authorization |
| DHCPv4 | 67/UDP server, 68/UDP client | Address/configuration assignment | Broadcast/relay behavior and server trust require network controls |
| NTP | 123/UDP | Time synchronization | Plain NTP is not NTS; record source authentication and clock quality separately |
| mDNS | 5353/UDP | Link-local multicast naming | Advertisements are untrusted discovery input and expose service metadata |
| WS-Discovery | 3702/UDP in ad hoc multicast mode | Probe, resolve, hello, and bye | Managed mode can use HTTP; advertised endpoint references still need validation |
| HTTP | 80/TCP | Cleartext HTTP convention | HTTP versions, upgrades, proxies, and redirects require explicit handling |
| HTTPS | 443/TCP; HTTP/3 commonly uses QUIC over 443/UDP | HTTP protected by TLS, or HTTP/3 over QUIC | Validate ALPN, certificate identity, origin, proxy, and application authorization |
| WebSocket / SSE / webhooks | Usually the parent HTTP(S) listener | Streaming or callback application patterns | No dedicated port proves WebSocket, SSE, webhook authenticity, or callback safety |
| gRPC | No dedicated universal service port | RPC commonly over HTTP/2 | Product/API documentation owns the listener and TLS policy |
| LDAP / LDAPS convention | 389/TCP or UDP; 636/TCP for LDAP over TLS | Directory access | Prefer an explicitly protected profile; StartTLS and implicit TLS are distinct configurations |
| SSH | 22/TCP | Secure administration and subsystems such as SFTP | Host-key validation and user authorization remain mandatory |
| SNMP | 161/UDP requests, 162/UDP notifications are common registrations | Monitoring and management | SNMP version/security model matters; v1/v2c community strings are not modern authentication |
| Syslog | 514/UDP or TCP registrations; 6514/TCP for syslog over TLS | Event transport | Framing, reliability, TLS identity, durability, and loss accounting remain separate |
| RTSP | 554/TCP and UDP registrations | Media-session control | RTSP 1.0/2.0 support, TLS, authentication, and RTP transport are separate capabilities |
| RTP / RTCP / SRTP | Session-negotiated dynamic ports in many deployments | Media and control reports | SDP/ICE or product configuration selects flows; do not open an unrestricted range |
| SIP | 5060/TCP, UDP, or SCTP registrations | Session signaling | A 5060 listener is not protected merely because authentication exists |
| SIP over TLS convention | 5061/TCP or SCTP registration | TLS-protected SIP hop | SIPS routing and media protection are separate; require SRTP where appropriate |
| STUN / TURN | 3478/TCP or UDP; 5349/TCP or UDP for TLS/DTLS forms | NAT traversal and relay | WebRTC can also use other configured TURN endpoints and transports |
| MQTT | 1883/TCP; `secure-mqtt` 8883/TCP | Brokered messaging | The MQTT standard does not make 8883 a complete security profile; verify TLS and topic ACLs |
| AMQP | 5672/TCP; 5671/TCP for AMQP over TLS | Brokered messaging | Protocol version, SASL, virtual host, TLS identity, and authorization must match |
| CoAP / CoAPS | 5683/TCP or UDP; 5684/TCP or UDP for protected forms | Constrained request/response and observation | Transport and security profile differ; OSCORE protects messages independently of the transport port |
| RADIUS / accounting | 1812 and 1813 registrations over TCP/UDP; deployed products commonly use UDP | Network AAA and accounting | Pin RFC/profile and server identity; classic RADIUS security limitations remain regardless of port |
| RADIUS over TLS / RADIUS 1.1 | `radsec` 2083/TCP registration | Experimental TLS-protected RADIUS family | RFC 6614 and RFC 9765 are distinct Experimental protocols; explicit bilateral support is required |
| BACnet/IP | 47808/UDP is the common BACnet/IP value (`0xBAC0`) | BACnet BVLL over IP | Project configuration may differ; classic BACnet/IP is not BACnet/SC |
| KNXnet/IP | 3671/UDP convention | KNX IP routing, tunneling, and discovery | KNX IP Secure is an explicit profile, not a consequence of the port |
| Modbus/TCP | 502/TCP | Classic Modbus application protocol over TCP | No native modern peer authentication or confidentiality |
| Modbus Security | 802/TCP | Modbus/TCP protected with mutual TLS and certificates | Product authorization remains product-specific; a TLS gateway may expose cleartext downstream |
| OPC UA | 4840/TCP is a registered convention for OPC UA TCP | UA client/server endpoint | Endpoint URL, transport/profile, SecurityPolicy, mode, application certificate, and user token form one decision |
| DNP3 | 20000/TCP and UDP registrations | DNP3 over IP convention | Exact master/outstation profile, transport, Secure Authentication, and command authority remain separate |
| IEC 60870-5-104 | 2404/TCP registration | Telecontrol over TCP companion profile | Address/cause/type/time/quality semantics and IEC 62351 protection require explicit profiles |
| IEC 61850 MMS | 102/TCP convention inherited from ISO-TSAP/COTP services | Client/server MMS mapping | GOOSE and Sampled Values use data-link multicast rather than this TCP port; never invent an IP port for them |
| Matter | 5540/TCP and UDP registration | Operational discovery and communication | Fabric identity, secure session, ACL, commissioning, and transport support remain product-specific |
| ONVIF services | No single ONVIF application port | SOAP/HTTP(S), RTSP, events, and optional transports | Use device-advertised, validated service endpoints and registered product/profile evidence |
| OSDP | No IP service port in the base reader-controller link | Serial multidrop access-control link | Record RS-485 profile, address, Secure Channel, and any gateway boundary |
| Wiegand / Clock-and-Data | No IP service port | Electrical reader signaling | A network converter adds a separate vendor transport; it does not upgrade the legacy link |
| GB/T 28181 | Deployment/profile-selected SIP and media endpoints | Platform/device signalling and media | Record the exact national profile and configured endpoints; do not infer a universal listener from SIP conventions |
| SRT / RIST | No universal port for the protocol families | Media contribution | Endpoint/port, caller/listener/profile, firewall, encryption, and authorization are deployment contracts |
| CAP / EDXL | No dedicated universal port | Emergency XML commonly carried by a profiled HTTPS or messaging service | Transport delivery and alert activation are separate; the issuing authority/feed contract owns the endpoint |

Primary port evidence is the live IANA registry, reviewed 2026-08-25. Protocol-specific pages remain canonical for semantics: [video and media](../02-protocols/video-and-media/README.md), [web and messaging](../02-protocols/web-and-messaging/README.md), [access control](../02-protocols/access-control/README.md), [building and industrial](../02-protocols/building-and-industrial/README.md), and [infrastructure](../02-protocols/infrastructure/README.md).

## Protection map

| Carrier or wrapper | What it can provide | What it does not establish by itself | Canonical guidance |
|---|---|---|---|
| TLS | Confidentiality and integrity for a connection; authenticated server and optionally client when validation is correct | Business authorization, safe command semantics, downstream protection, durable delivery | [TLS, PKI, and secure transport](../02-protocols/infrastructure/tls-pki-and-secure-transport.md) |
| DTLS | TLS-like protection for datagrams | Reliable delivery, application authorization, or protection beyond the terminating peer | [WebRTC](../02-protocols/video-and-media/webrtc.md) |
| QUIC | Encrypted authenticated transport incorporating TLS 1.3 | Safe HTTP/API semantics or authorization | [HTTP and REST](../02-protocols/web-and-messaging/http-and-rest.md) |
| SRTP / SRTCP | Media confidentiality, integrity/authentication profiles, and replay handling | Signaling identity, call authorization, recording policy | [SIP and SRTP](../02-protocols/video-and-media/sip-and-srtp.md) |
| OSDP Secure Channel | Protected messaging between OSDP control panel and peripheral | Protection of a credential before the reader or beyond a terminating gateway | [OSDP](../02-protocols/access-control/osdp.md) |
| BACnet/SC | TLS/WebSocket-based secure BACnet data link | Object/property write safety or encryption on attached MS/TP segments | [BACnet/SC](../02-protocols/building-and-industrial/bacnet-secure-connect.md) |
| Modbus Security | Mutual-TLS protection and certificate-carried role information for Modbus/TCP | Correct register model, safe write, or protected RTU segment | [Modbus Security](../02-protocols/building-and-industrial/modbus-security.md) |
| KNX IP Secure / Data Secure | Protected IP communication / protected selected application telegrams | Protection of unrelated management APIs or unselected/plain group objects | [KNX Secure](../02-protocols/building-and-industrial/knx-secure.md) |
| Network tunnel or VPN | Protected conduit between tunnel endpoints | Native endpoint identity, least-privilege application authorization, or protection past the tunnel | [Trust boundaries and segmentation](../01-foundations/trust-boundaries-and-segmentation.md) |

See [protocol security comparison](protocol-security-comparison.md) for a family-level view.

## Firewall and conduit record

For every allowed flow, record:

| Field | Required detail |
|---|---|
| Purpose and owner | Named integration, operational owner, data/controller owner |
| Direction | Initiator, responder, return path, address family, and whether callbacks reverse the expected direction |
| Endpoint identity | Asset IDs, approved names/addresses, certificate/application identity, expected service |
| Service | Actual configured local/remote port and transport—not only a registry value |
| Discovery dependency | Broadcast/multicast/proxy requirement and how discovery becomes trusted inventory |
| Protection | TLS/DTLS/security profile, mutual authentication, trust anchors, credential rotation |
| Authorization | Resource, action, tenant/site, topic, object/property, or stream scope |
| Reliability | Timeout, retry, keepalive, session renewal, failover, duplicate/unknown-outcome policy |
| Capacity | Connection, packet, message, bandwidth, rate, and queue limits |
| Evidence | Configuration reference, standard revision, product documentation, approval, environment-validation date |
| Revocation | Expiry/review date and removal/rollback owner |

Avoid “any-to-device on standard ports.” Resolve bounded source and destination sets, preserve IPv4/IPv6 parity, deny management services from operational clients, and monitor both accepted and denied flows without logging secrets.

## Verification checklist

- [ ] IANA/standard value treated as orientation, not product evidence
- [ ] Actual listener and transport obtained from approved configuration
- [ ] Redirect, proxy, gateway, NAT, multicast, and callback paths included
- [ ] TLS/security profile and both endpoint identities verified separately
- [ ] Application authorization and physical consequence recorded
- [ ] Dynamic RTP/ICE ranges bounded by negotiated/product policy
- [ ] Serial and radio protocols not forced into an invented IP-port model
- [ ] Firewall rule has owner, evidence, expiry, monitoring, and rollback
- [ ] Listener evidence comes from approved configuration or a separately authorized environment-validation record, not an inferred default

## Sources

- **IANA-PORTS** — [Service Name and Transport Protocol Port Number Registry][IANA-PORTS], IANA, last-updated status reviewed 2026-08-25.
- **PORT-GUIDANCE** — [RFC 6335: Internet Assigned Numbers Authority Procedures for the Management of the Service Name and Transport Protocol Port Number Registry][PORT-GUIDANCE], IETF, August 2011.
- **HTTP3** — [RFC 9114: HTTP/3][HTTP3], IETF, June 2022.
- **WSD** — [WS-Discovery 1.1][WSD], OASIS Standard, 1 July 2009.
- **MDNS** — [RFC 6762: Multicast DNS][MDNS], IETF, February 2013.
- **MODBUS-SEC** — [Modbus specifications and implementation guides][MODBUS-SEC], Modbus Organization, status reviewed 2026-08-25.
- **TLS13** — [RFC 8446: TLS 1.3][TLS13], IETF, August 2018.

[IANA-PORTS]: https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
[PORT-GUIDANCE]: https://datatracker.ietf.org/doc/rfc6335/
[HTTP3]: https://datatracker.ietf.org/doc/rfc9114/
[WSD]: https://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html
[MDNS]: https://datatracker.ietf.org/doc/rfc6762/
[MODBUS-SEC]: https://www.modbus.org/modbus-specifications
[TLS13]: https://datatracker.ietf.org/doc/rfc8446/
