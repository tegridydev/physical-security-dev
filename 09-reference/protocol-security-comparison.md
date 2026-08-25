---
title: "Protocol security comparison"
summary: "A boundary-aware comparison of native and companion security mechanisms across physical-security protocols."
page_type: reference
domains:
  - cross-domain
tags:
  - protocol-security
  - comparison
  - authentication
  - encryption
  - authorization
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 8446"
  - "RFC 3711"
  - "SIA OSDP 2.2.2"
  - "BACnet Secure Connect"
  - "Modbus/TCP Security"
coverage_limit: "Protocol-family summary only; exact algorithms, editions, profiles, product implementations, certificates, keys, authorization, fallback, and end-to-end boundaries require primary specifications and deployment evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Protocol security comparison

[Home](../README.md) / [Reference](README.md) / Protocol security comparison

> This table is not a security certification or product claim. “Can provide” means a named standard/profile defines the property when correctly selected, implemented, provisioned, and validated. It does not mean a product supports or enables it.

## Comparison dimensions

| Dimension | Evidence required |
|---|---|
| Confidentiality | Exact protected bytes/hops, algorithm/profile, key ownership, termination points |
| Peer authentication | Server/client/device/user identities and validation rules |
| Integrity and freshness | Authenticated data, replay window/counter/sequence, restart/rollback handling |
| Authorization | Which identity may read, subscribe, configure, or actuate which resource |
| Downgrade resistance | Whether cleartext/legacy fallback exists and how it is prohibited/detected |
| Lifecycle | Enrollment, rotation, revocation, replacement, backup, expiry, recovery, audit |
| Residual boundary | Plain downstream bus/media, gateway cache, export, logs, physical completion |

## Family-level summary

| Protocol/family | Base or legacy posture | Protected option or required security | Principal residual risk | Canonical page |
|---|---|---|---|---|
| HTTP/REST | HTTP alone is cleartext; application auth varies | HTTPS with validated TLS; OAuth/mTLS/message signatures as profiled | TLS does not make methods safe, authorize objects, or stop SSRF/parser faults | [HTTP and REST](../02-protocols/web-and-messaging/http-and-rest.md) |
| SOAP/XML | SOAP/XML has no inherent channel protection | HTTPS; WS-Security/XML Signature only under a tightly specified profile | XML parser/entity/signature-wrapping risk; intermediaries and signed-part ambiguity | [SOAP and XML](../02-protocols/web-and-messaging/soap-and-xml.md) |
| WebSocket | `ws` is cleartext and upgrade inherits HTTP auth context | `wss` with TLS plus origin/session/resource authorization | Long-lived revocation, reauthentication, message bounds, and connection hijack | [WebSocket, SSE, and webhooks](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) |
| SSE / webhooks | Inherits HTTP; callback authenticity is application-defined | HTTPS plus scoped auth; signed webhooks with replay policy where specified | Callback SSRF, secret rotation, retries/duplicates, receiver durability | [WebSocket, SSE, and webhooks](../02-protocols/web-and-messaging/websocket-sse-and-webhooks.md) |
| MQTT | Protocol can run without protected transport; broker auth/ACLs are deployment choices | TLS/mTLS and per-client topic/action authorization | Wildcards, retained/Will state, shared identities, bridges, queue exhaustion | [MQTT](../02-protocols/web-and-messaging/mqtt.md) |
| AMQP 1.0 | SASL/TLS and authorization are selected by the deployment; settlement is not security | TLS/mTLS, appropriate SASL mechanism, virtual-host/node/link permissions | Anonymous/weak SASL, cross-tenant link authorization, settlement mistaken for physical completion | [AMQP 1.0](../02-protocols/web-and-messaging/amqp-1-0.md) |
| CoAP / LwM2M | Plain CoAP has no universal application security; bootstrap/profile choices vary | DTLS/TLS or OSCORE, including Group OSCORE only under an explicit group-security design | Proxy termination, replay/context loss, unsafe bootstrap, observation amplification, ACK mistaken for outcome | [CoAP, OSCORE, and LwM2M](../02-protocols/web-and-messaging/coap-oscore-and-lwm2m.md) |
| CAP / EDXL | XML formats do not authenticate an alert issuer by themselves | Authenticated transport and/or an explicitly profiled XML signature plus issuer/feed authorization | Signature wrapping/canonicalization, stale update/cancel chains, wrong geography/audience, delivery mistaken for activation | [CAP and EDXL](../02-protocols/web-and-messaging/cap-and-edxl-emergency-messaging.md) |
| gRPC | Security comes from its HTTP/2/transport and application profile | TLS/mTLS plus per-RPC/resource authorization and bounded metadata | Reflection/admin exposure, retrying mutations, streaming revocation, schema/resource exhaustion | [gRPC and serialization](../02-protocols/web-and-messaging/grpc-and-serialization.md) |
| ONVIF | Services span HTTP/SOAP, WS-Discovery, events, RTSP/RTP; deployments vary | TLS/device/user security capabilities, protected service endpoints, SRTP where profiled/supported | Discovery is unauthenticated; profile registration does not prove site configuration; media may remain plain | [ONVIF](../02-protocols/video-and-media/onvif.md) |
| GB/T 28181 | Base SIP/XML/RTP deployments require an explicit security profile and national requirement mapping | Applicable GB 35114 mechanisms plus authenticated signalling/transport and platform authorization | Domain/account impersonation, catalogue leakage, weak media protection, security-standard edition mismatch | [GB/T 28181](../02-protocols/video-and-media/gbt-28181.md) |
| RTSP / RTP / RTCP | Plain control/media lacks modern confidentiality; RTP sequence is not anti-replay security | RTSP over TLS where supported; SRTP/SRTCP with authenticated key management | SDP/address injection, weak URL credentials, multicast joinability, key-management mismatch | [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md) |
| SIP | Hop-by-hop signaling commonly appears in legacy/plain forms | SIP over TLS/SIPS routing; current Digest/identity profiles; SRTP for media | TLS signaling does not protect media; DTMF/door actions need separate authorization | [SIP and SRTP](../02-protocols/video-and-media/sip-and-srtp.md) |
| WebRTC | Security architecture requires protected media/keying in conforming WebRTC | DTLS-SRTP/SRTP, ICE credentials, HTTPS/WSS signaling under application control | Signaling service can misauthorize; TURN/SFU may observe metadata/media by design | [WebRTC](../02-protocols/video-and-media/webrtc.md) |
| SRT / RIST | Contribution recovery profiles do not supply application/user authorization or evidence policy | SRT encryption/passphrase handling or RIST security profile as explicitly supported, plus endpoint/network identity | Shared/static secrets, unauthenticated endpoint selection, resource exhaustion, confusing contribution protection with content entitlement | [SRT and RIST](../02-protocols/video-and-media/srt-and-rist.md) |
| OSDP | CRC/checksum mode is not cryptographic protection | OSDP Secure Channel with unique managed keys | Install-mode/default-key misuse, cleartext fallback, insecure credential before/after link | [OSDP](../02-protocols/access-control/osdp.md) |
| Wiegand / Clock-and-Data | No native confidentiality, mutual authentication, or replay protection | Replacement by protected reader-controller transport; compensating physical controls during migration | Static identifiers, easy observation/injection, no supervision, converters preserve weak hop | [Legacy reader interfaces](../02-protocols/access-control/legacy-reader-interfaces.md) |
| Contactless/smart card | UID or public memory is not authentication; security is application/profile-specific | Challenge-response, secure messaging, shared-key or public-key applications | Default/shared keys, relay, downgrade to UID, reader-controller loss of assurance | [Contactless and smart-card standards](../02-protocols/access-control/contactless-and-smart-card-standards.md) |
| BACnet/IP classic | Does not provide modern per-message peer authentication/confidentiality for every exchange | BACnet/SC uses WebSocket/TLS and PKI for a secure data link | Object/property/priority authorization; legacy MS/TP remains plain behind a router | [BACnet/SC](../02-protocols/building-and-industrial/bacnet-secure-connect.md) |
| Modbus RTU/TCP classic | CRC/MBAP transaction ID are not security; no native authorization/confidentiality | Modbus Security uses mutual TLS, X.509 identities, and certificate role information | Product-specific authorization, unsafe register writes, cleartext gateway downstream | [Modbus Security](../02-protocols/building-and-industrial/modbus-security.md) |
| OPC UA | Security modes/policies are explicitly selectable, including insecure choices | SecureChannel, application certificates, Sessions, user tokens, roles/access controls | Auto-trust, `None`, obsolete policy, namespace/semantic mistakes, method/write consequence | [OPC UA](../02-protocols/building-and-industrial/opc-ua.md) |
| IEC 60870-5-101/-104 | Base telecontrol profiles were not designed with modern end-to-end identity/confidentiality | Applicable IEC 62351-5 mechanisms, protected conduits, strict station/ASDU allowlists, and operational authorization | Legacy endpoint support, gateway security termination, replay/time/quality ambiguity, high-impact commands | [IEC 60870-5-101 and -104](../02-protocols/building-and-industrial/iec-60870-5-101-and-104.md) |
| IEC 61850 | MMS, GOOSE, SV, and engineering workflows have different threat and timing models | Applicable IEC 62351 parts, certificates/roles, message security, and protected engineering lifecycle | Protection latency/availability trade-offs, SCL tampering, multicast trust, control/protection coupling | [IEC 61850](../02-protocols/building-and-industrial/iec-61850.md) |
| Matter | Commissioning, fabrics, operational certificates, and ACLs provide ecosystem security primitives | Device attestation during commissioning, fabric operational credentials, ACLs, secure sessions, lifecycle removal | Attestation is not authorization; stale fabrics/controllers, bridge trust, cloud/ecosystem account compromise | [Matter](../02-protocols/building-and-industrial/matter.md) |
| KNX classic | Plain telegrams do not provide modern cryptographic protection | KNX IP Secure for IP paths; KNX Data Secure for selected group/object data | Mixed secure/plain configuration, keyring exposure, gateway termination, sequence recovery | [KNX Secure](../02-protocols/building-and-industrial/knx-secure.md) |
| SNMP | v1/v2c community model is weak and generally unencrypted | SNMPv3 USM `authPriv`, or applicable secure transport model | Shared engine state/keys, overly broad views, SET permission, trap authenticity | [Monitoring and administration](../02-protocols/infrastructure/monitoring-and-secure-administration.md) |
| Syslog | UDP/TCP forms may be unauthenticated and cleartext | Syslog over TLS with validated identities | Hop protection is not durable storage integrity; loss/framing/backpressure remains | [Monitoring and administration](../02-protocols/infrastructure/monitoring-and-secure-administration.md) |
| NTP | Plain NTP can be spoofed/manipulated on reachable paths | Network Time Security (NTS) for supported NTP deployments | Authenticated source may still be wrong; endpoint clock/holdover/step policy matters | [Time synchronisation](../02-protocols/infrastructure/time-synchronisation.md) |
| Alarm formats DC-03/DC-05/DC-07 | Historical formats do not provide a complete modern cryptographic security model | Protected conduit/gateway and strict source/account binding; use a modern supported reporting profile | A syntactically valid event is not dispatch authorization; downstream routes are high-impact | [Alarm monitoring](../02-protocols/alarm-monitoring/README.md) |
| SIA DC-09 | Edition/configuration dependent; older deployments may use weak/long-lived material | Exact edition's encryption/authentication/key-management options; 2026 adds key-rotation capability | Account authorization, duplicate/replay handling, monitoring policy, product interoperability | [SIA DC-09](../02-protocols/alarm-monitoring/sia-dc-09.md) |
| SAML / OIDC | Assertions/tokens are bearer-like security objects whose validation profile is application-specific | Signed assertions/tokens over HTTPS; strict issuer, audience, recipient/redirect, nonce/state/PKCE, key lifecycle | XML signature wrapping, token substitution, confused deputy, broad role mapping, stale sessions | [Enterprise federation](../02-protocols/infrastructure/enterprise-federation-saml-and-oidc.md) |
| SCIM | HTTPS API protection and OAuth scope are deployment choices | TLS plus narrowly scoped client identity, resource/attribute authorization, reconciliation, and audit | Overbroad provisioning, tenant crossing, mutable identifiers, async acceptance mistaken for downstream completion | [SCIM provisioning](../02-protocols/infrastructure/scim-identity-provisioning.md) |
| WebAuthn / FIDO | Public-key authentication is scoped to the relying-party origin and credential policy | WebAuthn ceremony validation, authenticator policy, secure origin, challenge/freshness, recovery controls | Account recovery downgrade, sync/account boundary, attestation overclaim, login mistaken for PACS authorization | [WebAuthn, FIDO, and passkeys](../02-protocols/infrastructure/webauthn-fido-and-passkeys.md) |

## Security terminators are architectural components

A gateway, reverse proxy, recorder, broker, hub, router, or cloud service that decrypts and re-emits data creates a new boundary. Record:

- identity and trust before and after termination;
- plaintext exposure in memory, disk, queues, logs, backups, and diagnostics;
- authorization translation and any loss of source identity;
- schema/semantic translation and unknown-field handling;
- key and certificate custody;
- outage, failover, replay, retry, and duplicate behavior;
- whether a secure upstream link becomes a legacy cleartext field link.

End-to-end should name endpoints and bytes. “Encrypted in transit” without that boundary is not actionable evidence.

## Common false equivalences

| Claim | Why it is unsafe |
|---|---|
| “It is on 443, therefore secure.” | Port 443 does not prove TLS validation, expected application, or authorization |
| “The VLAN is trusted.” | Segmentation limits reachability; it does not authenticate endpoints or constrain authorized insiders |
| “The CRC passed.” | CRC detects accidental corruption, not deliberate forgery |
| “The certificate is valid.” | A valid chain may still identify the wrong endpoint, role, site, or compromised key |
| “The user logged in.” | Authentication does not grant every resource/action or prove current session intent |
| “The command returned success.” | Transport/application acceptance is not physical completion |
| “The profile is certified.” | Certification must match exact product/firmware/role and does not verify deployment configuration |
| “Media is encrypted.” | Signaling, metadata, recording, exports, or an SFU/gateway may remain exposed |

## Selection checklist

- [ ] Exact protocol edition, security add-on/profile, and product role pinned
- [ ] Plain/legacy fallback prohibited or explicitly isolated and monitored
- [ ] Server, client/device, service, user, and credential identities modeled separately
- [ ] Least privilege defined for observe, subscribe, configure, and actuate actions
- [ ] Key/certificate bootstrap, rotation, revocation, replacement, backup, and recovery owned
- [ ] Replay/sequence/counter behavior across reboot and restore documented
- [ ] Every security termination and cleartext downstream segment diagrammed
- [ ] Parser, connection, rate, queue, and decompression limits included
- [ ] Successful request never substituted for authoritative physical-state confirmation
- [ ] Product claims and configuration require exact owner-approved evidence rather than inference from this comparison

## Sources

- **TLS13** — [RFC 8446: TLS 1.3][TLS13], IETF, August 2018.
- **SRTP** — [RFC 3711: Secure Real-time Transport Protocol][SRTP], IETF, March 2004.
- **WEBRTC-SEC** — [RFC 8827: WebRTC Security Architecture][WEBRTC-SEC], IETF, January 2021.
- **OSDP** — [Open Supervised Device Protocol][OSDP], Security Industry Association, OSDP 2.2.2 status reviewed 2026-08-25.
- **BACNET-SC** — [BACnet Secure Connect resources][BACNET-SC], ASHRAE BACnet Committee, accessed 2026-08-25.
- **MODBUS-SEC** — [Modbus Security specifications][MODBUS-SEC], Modbus Organization, accessed 2026-08-25.
- **OPCUA-SEC** — [OPC UA Part 2: Security Model][OPCUA-SEC], OPC Foundation, accessed 2026-08-25.
- **KNX-SEC** — [KNX Security overview][KNX-SEC], KNX Association, accessed 2026-08-25.
- **SNMP-USM** — [RFC 3414: User-based Security Model for SNMPv3][SNMP-USM], IETF, December 2002.
- **NTS** — [RFC 8915: Network Time Security for NTP][NTS], IETF, September 2020.

[TLS13]: https://datatracker.ietf.org/doc/rfc8446/
[SRTP]: https://datatracker.ietf.org/doc/rfc3711/
[WEBRTC-SEC]: https://datatracker.ietf.org/doc/rfc8827/
[OSDP]: https://www.securityindustry.org/industry-standards/open-supervised-device-protocol/
[BACNET-SC]: https://bacnet.org/sc/
[MODBUS-SEC]: https://www.modbus.org/modbus-specifications
[OPCUA-SEC]: https://reference.opcfoundation.org/specs/OPC-10000-2/full
[KNX-SEC]: https://support.knx.org/hc/en-us/articles/360012630199-KNX-Security-overview
[SNMP-USM]: https://datatracker.ietf.org/doc/rfc3414/
[NTS]: https://datatracker.ietf.org/doc/rfc8915/
