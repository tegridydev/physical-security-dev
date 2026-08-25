---
title: Acronyms and Initialisms
summary: Expanded forms and contextual notes for abbreviations used across physical-security development and integration.
page_type: reference
domains: [cross-domain]
tags: [acronyms, abbreviations, terminology]
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: []
coverage_limit: Common expansions in this knowledge base; vendors and jurisdictions may reuse abbreviations differently.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Acronyms and initialisms

| Term | Expansion | Context note |
|---|---|---|
| AAA | Authentication, Authorization, and Accounting | Network/application access control functions |
| ACU | Access Control Unit | Access controller; product boundaries vary |
| ACS / PACS | Access Control System / Physical Access Control System | PACS avoids confusion with logical access, but also has other industry meanings |
| AHJ | Authority Having Jurisdiction | Applicable code/regulatory authority |
| AMQP | Advanced Message Queuing Protocol | AMQP 1.0 is distinct from the older 0-9-1 protocol family |
| API | Application Programming Interface | Contract may be public, partner-only, or private |
| ASDU | Application Service Data Unit | IEC telecontrol message unit; type, cause, address, quality, and time context matter |
| BLE | Bluetooth Low Energy | Radio/link foundation used by many mobile credentials |
| BMS / BAS | Building Management / Automation System | Building-control platforms and field networks |
| CA | Certification Authority | PKI issuer/trust role, not merely a certificate file |
| CAP | Common Alerting Protocol | OASIS emergency/public-warning message format; regional profiles apply |
| CCTV | Closed-Circuit Television | Historical/common term; modern video is often IP and interconnected |
| CID | Contact ID | Alarm event format associated with ANSI/SIA DC-05 |
| CORS | Cross-Origin Resource Sharing | Browser policy; not an API authorization control |
| CoAP | Constrained Application Protocol | REST-like protocol for constrained nodes and networks |
| CRC | Cyclic Redundancy Check | Error detection, not cryptographic integrity |
| CSR | Certificate Signing Request | PKI enrollment artifact |
| CTAP | Client to Authenticator Protocol | FIDO protocol between a platform/client and external or platform authenticator |
| DTMF | Dual-Tone Multi-Frequency | Used by legacy alarm/telephony signaling |
| E2EE | End-to-End Encryption | Endpoints and key ownership must be explicitly defined |
| EAP | Extensible Authentication Protocol | Framework used by 802.1X and related access methods |
| EDXL | Emergency Data Exchange Language | OASIS family including the Distribution Element envelope |
| EOL / EOS | End of Life / End of Support | Vendor definitions and dates differ |
| FOV | Field of View | Camera coverage, lens, mounting, and scene property |
| GPIO | General-Purpose Input/Output | Electrical interface; validate levels and isolation |
| GOOSE | Generic Object Oriented Substation Event | IEC 61850 fast multicast event mechanism; protection use is high impact |
| gPTP | Generalized Precision Time Protocol | IEEE 802.1AS profile of PTP for time-sensitive networks |
| HMI | Human–Machine Interface | Operator interface in OT/building environments |
| IAM | Identity and Access Management | Human/workload identity governance |
| IDS / IPS | Intrusion Detection / Prevention System | Qualify cyber/network versus physical intrusion context |
| IGMP | Internet Group Management Protocol | IPv4 multicast membership management |
| IoT | Internet of Things | Broad category, not a security or interoperability guarantee |
| JWT | JSON Web Token | A token representation; validation profile and authorization remain essential |
| KMS | Key Management System | May manage cryptographic keys but not all certificate lifecycle |
| LDAP | Lightweight Directory Access Protocol | Directory access protocol; commonly secured with TLS/SASL profiles |
| LPR / ANPR | License/Automatic Number Plate Recognition | Regional terminology for vehicle plate recognition |
| LwM2M | Lightweight Machine to Machine | OMA device-management/service-enablement profile commonly using CoAP |
| MLD | Multicast Listener Discovery | IPv6 multicast membership management |
| MMS | Manufacturing Message Specification | ISO 9506 service/protocol used by IEC 61850 client/server mappings |
| mTLS | Mutual TLS | Both peers authenticate using certificates during TLS |
| NTS | Network Time Security | Security mechanism for NTP |
| NVR | Network Video Recorder | Recording appliance/service; capabilities vary |
| OSDP | Open Supervised Device Protocol | SIA access peripheral/controller protocol |
| OSCORE | Object Security for Constrained RESTful Environments | End-to-end CoAP message protection across selected intermediaries |
| OT | Operational Technology | Systems monitoring or controlling physical processes |
| PACS | Physical Access Control System | Also used elsewhere for picture archiving; qualify context |
| PII | Personally Identifiable Information | Legal definitions differ; use local privacy terminology too |
| PIN | Personal Identification Number | A knowledge factor; storage, retries, duress, and privacy require policy |
| PKI | Public Key Infrastructure | Roles, policy, issuance, trust, revocation, renewal, custody |
| PLC | Programmable Logic Controller | Industrial controller, potentially safety/availability critical |
| PoE | Power over Ethernet | IEEE 802.3 power delivery family; budget and cabling matter |
| PSIM | Physical Security Information Management | Integration/orchestration/operator workflow platform category |
| PTP | Precision Time Protocol | IEEE 1588 time synchronization family |
| RADIUS | Remote Authentication Dial-In User Service | Common AAA protocol for network access |
| REX / RTE | Request to Exit | Input/sensor/button used in egress sequence; not proof a person exited |
| RIST | Reliable Internet Stream Transport | VSF media-contribution profile family |
| RTCP | RTP Control Protocol | Reception, timing, and participant/control information for RTP |
| RTP | Real-time Transport Protocol | Real-time media/data packet transport |
| RTSP | Real Time Streaming Protocol | Media session control, not the media transport itself |
| SDP | Session Description Protocol | Describes media sessions; does not negotiate trust by itself |
| SAML | Security Assertion Markup Language | XML-based enterprise federation; assertion validation and local role mapping are separate |
| SCIM | System for Cross-domain Identity Management | HTTP-based identity provisioning schema/protocol family |
| SCL | Substation Configuration Language | IEC 61850 engineering/configuration representation; protect as sensitive change-controlled input |
| SIEM | Security Information and Event Management | Security telemetry/correlation platform |
| SIP | Session Initiation Protocol | Multimedia session signaling, common in intercom/voice |
| SNMP | Simple Network Management Protocol | Prefer SNMPv3 security model where supported |
| SRTP | Secure Real-time Transport Protocol | Cryptographic protection for RTP media |
| SRT | Secure Reliable Transport | Project media-contribution protocol; not an IETF standard |
| SSE | Server-Sent Events | One-way HTTP event stream to a client |
| SV | Sampled Values | IEC 61850 multicast sampled-measurement mechanism |
| TLS | Transport Layer Security | Authenticated encrypted transport when validation is configured correctly |
| UWB | Ultra-Wideband | Radio/ranging technology used in some presence/mobile systems |
| VMS | Video Management System | Video device/media/user/event management platform |
| VLAN | Virtual LAN | Segmentation mechanism, not a complete trust boundary by itself |
| VPN | Virtual Private Network | Protected network path; does not replace application authorization |
| WebAuthn | Web Authentication | W3C public-key credential API used with FIDO authenticators |
| WSS | WebSocket over TLS | Common URI scheme for protected WebSocket transport |
| X.509 | Certificate framework | Common certificate format/profile used by TLS and PKI |
| XML | Extensible Markup Language | Structured format; parsers require secure configuration |

Protocol-specific abbreviations remain defined on their canonical pages where an expansion would be ambiguous.
