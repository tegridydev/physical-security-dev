---
title: "Discovery and multicast"
summary: "A protocol-oriented guide to bounded service discovery, multicast scope, inventory binding, and safe behavior across physical-security networks."
page_type: reference
domains:
  - cross-domain
tags:
  - discovery
  - multicast
  - inventory
  - ws-discovery
  - mdns
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "OASIS WS-Discovery 1.1"
  - "RFC 6762"
  - "RFC 6763"
  - "IEEE 802.1AB-2016"
coverage_limit: "Architecture and standards-defined assignments only; routed multicast, product discovery behavior, response limits, and inventory identity require deployment-specific environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Discovery and multicast

[Home](../README.md) / [Reference](README.md) / Discovery and multicast

Discovery answers **what claims to be present**. It does not answer whether the claimant is approved, authentic, correctly located, safe to query, or authorized for control. Bind discovery to commissioned identity and inventory before using any returned endpoint.

## Discovery families

| Mechanism | Scope and role | Standards-defined orientation | Trust and operations boundary |
|---|---|---|---|
| DHCP / DHCPv6 | Supplies address and configuration through client/server and relay paths | RFC 2131 / RFC 8415 | An offered address, gateway, DNS server, or option is configuration input; protect the server/relay path |
| DNS | Resolves controlled names and service data | RFC 1034 / RFC 1035 | A record is not device authorization; govern dynamic updates, split views, TTL, and DNSSEC policy where used |
| mDNS | Link-local multicast name resolution | UDP 5353; IPv4 `224.0.0.251`; IPv6 `FF02::FB` [MDNS] | Local advertisements are untrusted and can reveal device/service metadata |
| DNS-SD | Discovers service instances using DNS records | RFC 6763; can use unicast DNS or mDNS | TXT and instance data are display/capability hints, not a trusted schema or identity |
| WS-Discovery | Probe, resolve, hello, and bye for web services | Ad hoc UDP 3702 to IPv4 `239.255.255.250` or IPv6 `FF02::C`; managed mode can use a discovery proxy [WSD] | SOAP/XML and endpoint references are untrusted; response storms and stale announcements require bounds |
| ONVIF discovery | Uses WS-Discovery to locate candidate ONVIF devices/services | ONVIF Core plus WS-Discovery | Validate scopes, types, and `XAddrs`; then establish authenticated product/service identity |
| SSDP / UPnP discovery | Search and advertisement for UPnP devices/services | UDP 1900 and scoped multicast assignments in the UPnP Device Architecture | `LOCATION` is an untrusted URL; UPnP presence does not establish physical-security product trust |
| LLDP | Adjacent-link chassis, port, and capability information | IEEE 802.1AB | Switch-neighbor evidence is valuable but is not cryptographic device identity by default |
| BACnet Who-Is / I-Am | Discovers BACnet device instances and routes | BACnet service over the configured data link; BACnet/IP often uses broadcasts | Device instance/address advertisements are untrusted until bound to PICS, project inventory, and identity |
| KNXnet/IP search | Locates KNXnet/IP endpoints | KNXnet/IP project/profile assignments | Device/project identity, supported service families, secure mode, and ETS record remain authoritative |
| OPC UA discovery | Finds server applications and endpoint descriptions | Local discovery/server mechanisms defined by OPC UA | Discovery is deliberately separate from application-certificate trust and user authorization |
| Static inventory | No active discovery; provisioned endpoint set | Site configuration and asset records | Prefer for stable high-consequence paths, but continuously reconcile drift and replacement |

See [infrastructure discovery and addressing](../02-protocols/infrastructure/discovery-and-addressing.md), [multicast, discovery, and NAT](../01-foundations/multicast-discovery-and-nat.md), and [ports, transports, and protection](ports-transports-and-protection.md).

## WS-Discovery and ONVIF handling

In WS-Discovery ad hoc mode, probes go to a multicast group and matching targets reply directly. The standard also defines managed mode through a discovery proxy and multicast suppression behavior. [WSD]

A safe consumer should:

1. send only an owner-approved, narrowly scoped probe on an intended interface/VLAN;
2. randomize and rate-limit according to the selected specification/profile;
3. cap datagram, SOAP envelope, XML depth, response count, types, scopes, endpoint-reference count, and address count;
4. correlate message identifiers and ignore unrelated, replayed, or late responses under an explicit window;
5. parse `XAddrs` as untrusted URIs and reject unexpected schemes, user-info, fragments, link-local zone confusion, and disallowed destinations;
6. prevent redirect or address substitution from crossing the approved network/tenant boundary;
7. fetch only the minimal read-only service metadata required after a separate authorization decision;
8. bind the candidate to an approved serial/product/firmware record and authenticated certificate or commissioned secret;
9. preserve the raw bounded advertisement or hash as evidence without treating it as authoritative state.

An ONVIF scope or device type is self-asserted. Conformance requires the exact registered product and firmware/profile evidence described in [ONVIF](../02-protocols/video-and-media/onvif.md).

## Multicast is delivery scope, not access control

| Concern | Design question |
|---|---|
| Scope | Is the group link-local, administratively scoped, site-scoped, or routed? Are IPv4 and IPv6 equivalent? |
| Membership | Which switch ports and receivers may join? Is IGMP/MLD snooping and querier behavior understood? |
| Routing | Which multicast routing boundary, reflector, proxy, BBMD, or relay intentionally crosses subnets? |
| Source | Is source-specific multicast used or can any reachable sender inject? |
| Capacity | What is the peak bitrate/packet rate, group count, receiver count, replication point, and storm limit? |
| Availability | What happens on querier loss, switch reboot, topology change, duplicate sender, or stale membership? |
| Confidentiality | Can an unauthorized device on an allowed segment join and observe? Is application-layer media protection required? |
| Evidence | Which group/source/interface actually carried the traffic, and how was loss/reordering measured by the owner? |

Joining a video multicast does not authorize viewing. Network ACLs and multicast controls constrain reachability; authenticated keying/application authorization protects the stream where the selected protocol supports it. See [media streaming fundamentals](../01-foundations/media-streaming-fundamentals.md) and [RTSP, RTP, RTCP, and SDP](../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md).

## Broadcast and proxy boundaries

### BACnet/IP

BACnet/IP discovery and services can depend on broadcasts. BBMDs and Foreign Device registration intentionally extend broadcast reach. Treat Broadcast Distribution Tables, Foreign Device Tables, network numbers, and routed scopes as security-sensitive configuration; avoid circular replication and public exposure. [BACNET-IP]

BACnet/SC changes the secure data-link topology but does not authenticate an attached classic MS/TP segment or make every object write safe. See [BACnet family](../02-protocols/building-and-industrial/bacnet-family.md).

### Reflectors and relays

mDNS reflectors, SSDP relays, WS-Discovery proxies, DHCP relays, NAT traversal, and generic UDP forwarding enlarge the trust boundary. For each, record:

- exact messages and scopes forwarded;
- source-address and hop/TTL behavior;
- loop and amplification prevention;
- rate, response, and payload limits;
- tenant/site separation;
- identity binding after discovery;
- audit, health, restart, and configuration-change behavior.

Do not deploy a generic reflector merely to make discovery “work everywhere.” Prefer controlled DNS/service registries, explicit inventory, or a protocol-defined managed proxy when the operational model permits.

## Inventory promotion model

| State | Minimum evidence | Permitted use |
|---|---|---|
| Observed candidate | Interface, source address, discovery family, claimed type/name, first/last seen | Display in a quarantined candidate queue only |
| Correlated candidate | Expected switch port/site plus plausible product/serial/firmware data | Owner review and constrained metadata retrieval |
| Authenticated candidate | Validated certificate/application identity or commissioned cryptographic identity | Capability interrogation within a read-only policy |
| Approved asset | Asset owner, location, product/firmware, profiles, trust material, management path, lifecycle state | Explicitly authorized operational flows |
| Drifted/quarantined asset | Identity/address/topology/firmware conflict or expired evidence | No automatic overwrite or actuation; investigate |

Keep asset ID, protocol identifier, hardware address, IP address, DNS name, certificate identity, product serial, and physical location as separate fields. Replacements legitimately change some fields; cloning/spoofing can duplicate others.

## Defensive failure cases

- A single query elicits thousands of replies or fragments.
- A response advertises a loopback, link-local, multicast, private cross-tenant, metadata-service, or public URL.
- The same logical identity appears from two ports/addresses.
- A known address changes certificate or product identity.
- Announcements flap during boot or network loss.
- IPv6 discovery bypasses an IPv4-only policy.
- Reflectors form a loop or amplify a service across sites.
- Multicast succeeds while unicast return paths, MTU, or firewall state fail.
- A discovery parser consumes unbounded XML, TXT data, URLs, or endpoint lists.
- An integration automatically enrolls or commands every discovered device.

## Safe acceptance checklist

- [ ] Discovery family, revision, scope, interface, address family, and owner recorded
- [ ] Query and response size/rate/count bounded before parsing or allocation
- [ ] Discovered text, XML, URLs, addresses, and capabilities treated as untrusted input
- [ ] Candidate cannot trigger credential use, configuration, subscription, or actuation automatically
- [ ] Authenticated identity plus inventory/location evidence required for promotion
- [ ] Routed multicast, proxy, reflector, BBMD, and NAT boundaries documented
- [ ] IGMP/MLD/switch and IPv4/IPv6 behavior included in the environment-validation plan
- [ ] Absence from discovery not treated as proof of decommissioning
- [ ] Any environment validation has a written target allowlist, bounded query plan, and separate evidence record

## Sources

- **WSD** — [Web Services Dynamic Discovery 1.1][WSD], OASIS Standard, 1 July 2009; assignments and managed/ad hoc modes reviewed 2026-08-25.
- **MDNS** — [RFC 6762: Multicast DNS][MDNS], IETF, February 2013.
- **DNSSD** — [RFC 6763: DNS-Based Service Discovery][DNSSD], IETF, February 2013.
- **UPNP** — [UPnP Device Architecture resources][UPNP], Open Connectivity Foundation, accessed 2026-08-25.
- **LLDP** — [IEEE 802.1AB-2016: Station and Media Access Control Connectivity Discovery][LLDP], IEEE Standards Association.
- **ONVIF-CORE** — [ONVIF Network Interface Specifications][ONVIF-CORE], ONVIF, accessed 2026-08-25.
- **BACNET-IP** — [BACnet/IP reference and developer aids][BACNET-IP], ASHRAE BACnet Committee, accessed 2026-08-25.
- **OPCUA-DISCOVERY** — [OPC UA Part 4: Services, discovery service set][OPCUA-DISCOVERY], OPC Foundation, accessed 2026-08-25.

[WSD]: https://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html
[MDNS]: https://datatracker.ietf.org/doc/rfc6762/
[DNSSD]: https://datatracker.ietf.org/doc/rfc6763/
[UPNP]: https://openconnectivity.org/developer/specifications/upnp-resources/upnp/
[LLDP]: https://standards.ieee.org/standard/802_1AB-2016.html
[ONVIF-CORE]: https://www.onvif.org/profiles-specifications-new/
[BACNET-IP]: https://bacnet.org/developer-aids/
[OPCUA-DISCOVERY]: https://reference.opcfoundation.org/Core/Part4/v105/docs/5.4
