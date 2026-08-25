---
title: Discovery and addressing
summary: DHCP, DNS, mDNS/DNS-SD, WS-Discovery, LLDP, inventory binding, and safe discovery for physical-security networks.
page_type: reference
domains: [networking, cross-domain]
tags: [dhcp, dns, mdns, dns-sd, ws-discovery, lldp]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [RFC 2131, RFC 8415, RFC 1034, RFC 1035, RFC 6762, RFC 6763, OASIS WS-Discovery 1.1, IEEE 802.1AB]
coverage_limit: Protocol-level guidance; concrete DHCP/DNS schemas, vendor discovery extensions, and inventory authority are deployment-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Discovery and addressing

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Discovery and addressing

Discovery answers “what claims to be present?” Addressing answers “where can it be reached?” Neither answers “is this the approved device?” Promote a candidate into inventory only after matching an authenticated product identity, certificate or commissioned secret, expected topology, and asset-owner record.

## Protocol roles

| Protocol | Purpose | Trust warning |
|---|---|---|
| DHCP / DHCPv6 | lease addresses and configuration | unauthenticated offers/options can redirect traffic; protect server path |
| DNS | resolve scoped names to records | use controlled zones and validated update paths; a record is not device authorization |
| mDNS / DNS-SD | link-local name resolution and service advertisement | advertisements are local untrusted input and may reveal capabilities |
| WS-Discovery | SOAP-based probe/resolve and announcements, often multicast in ad hoc mode | metadata and endpoint references require validation |
| LLDP | adjacent-link device/port information | useful topology evidence, not authenticated asset identity by default |

DHCP for IPv4 is defined by RFC 2131 and DHCPv6 by RFC 8415.[^dhcp4][^dhcp6] DNS architecture and messages are defined by RFCs 1034 and 1035. mDNS and DNS-SD are RFCs 6762 and 6763. OASIS WS-Discovery 1.1 supports ad hoc multicast discovery and managed discovery through a proxy.[^wsd]

## Inventory binding

Keep separate fields for asset ID, manufacturer/product/firmware, hardware identifier, certificate/application identity, protocol device ID, DNS name, IP/MAC, switch port/LLDP neighbour, physical location, owner, first/last seen, and evidence source. Addresses and switch ports change; certificate identities can be replaced; product serials can be cloned or misreported. Reconciliation should surface conflict rather than silently overwrite.

Canonicalize names and URIs before comparison but preserve the original value for audit. Bound TXT records, SOAP/XML size/depth, endpoint list size, string length, and response count. Treat metadata as display-only unless it passes the exact protocol/schema validator. Do not interpolate discovered strings into shell commands, URLs, paths, logs, or HTML unsafely.

## Operational patterns

- Prefer an approved DHCP reservation/IPAM/DNS workflow to hard-coded spreadsheets or self-assigned defaults.
- Restrict dynamic DNS updates to authenticated principals and the intended records.
- Constrain multicast scope and discovery VLANs; do not route all discovery traffic enterprise-wide.
- Add randomized query timing and strict response/rate limits. A broad probe can create a response storm.
- Alert when an approved identity changes address unexpectedly, two identities claim one address/name, an unknown service appears, or a device moves switch port.
- Preserve last-known inventory separately from live discovery state; absence is not proof of decommissioning.

Validate discovery rate limits, DHCP/DNS conflict handling, multicast scope, LLDP trust boundaries, stale records, and recovery against an authorized target network.

## Primary sources

[^dhcp4]: [RFC Editor — RFC 2131, DHCP](https://www.rfc-editor.org/info/rfc2131/)
[^dhcp6]: [RFC Editor — RFC 8415, DHCP for IPv6](https://www.rfc-editor.org/info/rfc8415/)
[^wsd]: [OASIS — Web Services Dynamic Discovery 1.1](https://www.oasis-open.org/standard/ws-discovery/)
- [RFC Editor — RFC 1034, DNS concepts](https://www.rfc-editor.org/info/rfc1034/)
- [RFC Editor — RFC 1035, DNS implementation](https://www.rfc-editor.org/info/rfc1035/)
- [RFC Editor — RFC 6762, multicast DNS](https://www.rfc-editor.org/info/rfc6762/)
- [RFC Editor — RFC 6763, DNS-Based Service Discovery](https://www.rfc-editor.org/info/rfc6763/)
- [IEEE Standards Association — IEEE 802.1AB LLDP](https://standards.ieee.org/standard/802_1AB-2016.html)
