---
title: IP Addressing, Routing, and Ports
summary: Address planning, routing, service naming, firewall flow records, and safe use of port-number references.
page_type: foundation
domains: [cross-domain]
tags: [ip, routing, ports, firewall, dns]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 1918, RFC 4193, RFC 5737, RFC 6335]
coverage_limit: Does not prescribe a site addressing plan or claim product defaults.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# IP addressing, routing, and ports

An address locates an interface in a routing context; it is not a durable device identity or an authorization claim. A port identifies a transport endpoint convention; it does not prove which protocol, version, or peer is present.

## Address categories

- IPv4 private-use space is defined by [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918); it is not inherently trusted or globally unique.
- IPv6 unique-local addresses are defined by [RFC 4193](https://www.rfc-editor.org/rfc/rfc4193); link-local addresses have interface scope and often need a zone identifier in software.
- Documentation must use [RFC 5737](https://www.rfc-editor.org/rfc/rfc5737) IPv4 ranges and [RFC 3849](https://www.rfc-editor.org/rfc/rfc3849) IPv6 space, not plausible customer networks.
- Loopback is appropriate only when the entire example is local and no device connectivity is implied.

Inventory address assignment source—static, DHCP reservation, dynamic DHCP, SLAAC, vendor discovery, or cloud enrollment—and the recovery procedure when it changes.

## Routing and zones

Route only the flows the architecture requires. A typical flow record contains:

```yaml
source_zone: video-edge
source_role: camera
destination_service: vms-ingest.example
address_family: dual-stack
transport: tcp
destination_port: product-documented
initiator: camera
protection: tls-with-server-auth
purpose: event-and-health-uplink
availability: locally-buffered-for-30-minutes
owner: video-platform-team
```

Prefer service identity and named policy objects where tooling supports them, while retaining resolved-address observability. Avoid broad “camera VLAN to server VLAN” permissions that silently expose management and control interfaces.

## Ports

IANA maintains the [Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/). Registered numbers are references, not universal product facts. Products may use configurable or dynamic ports; protocols such as RTP can negotiate media ports; TLS may protect a service on either a conventional or product-specific port.

For each port, record direction and initiation. A firewall rule written as “allow 443” is incomplete without source/destination, TCP/UDP, IP version, purpose, TLS identity, and whether return traffic is stateful.

## NAT and port forwarding

Network Address Translation changes addressing and often blocks inbound initiation; it does not authenticate, authorize, or encrypt. Avoid exposing device management or media interfaces by generic port forwarding. Prefer authenticated outbound device connections, a managed application proxy, or an approved remote-access boundary with strong identity and logging.

Protocols embedding addresses or opening negotiated secondary connections need NAT-aware design. Discovery multicast usually does not cross routers/NAT without an explicit proxy or gateway, and extending it can widen spoofing/exposure.

## DNS and certificates

Separate device hostname, service discovery name, certificate identity, and display name. If TLS uses DNS identity, certificate names and DNS lifecycle must be coordinated. Define behaviour for stale cache, split-horizon views, multiple addresses, failover, DNSSEC where used, and resolver outage.

## Do not infer

- An open port is not proof of a service.
- A closed port is not proof a feature is absent; it may be disabled or outbound-only.
- Same subnet is not authorization.
- Private address is not confidentiality.
- Reachability is not health, and health is not safe physical operation.

