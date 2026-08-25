---
title: "Remote access"
summary: "Controlled remote administration and vendor support for physical-security and OT environments."
page_type: security
domains:
  - infrastructure
tags:
  - remote-access
  - support
  - bastion
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-46 Rev. 2"
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Remote access

[Home](../README.md) / [Security and assurance](README.md) / Remote access

Remote support often crosses the strongest physical-security boundary and can expose high-impact administrative or actuation functions. Treat it as an exceptional, observable workflow rather than permanent background connectivity.

## Preferred pattern

1. A named operator, support engineer, or vendor representative requests access for a defined purpose, system, and time window.
2. An accountable site authority approves the scope.
3. Strongly authenticated identity enters through a managed access service or bastion.
4. Policy permits only named destinations, protocols, and role capabilities.
5. The session and administrative actions are logged; sensitive screen/traffic recording follows applicable privacy rules.
6. Access expires automatically, credentials/tokens are invalidated, and temporary rules are removed.
7. Changes and resulting system state are reviewed.

## Requirements

- No direct inbound exposure of device or management interfaces to the public Internet.
- Separate vendor identities; never share the local administrator account.
- Phishing-resistant multifactor authentication where practical, plus managed endpoint posture.
- Just-in-time authorization, short session lifetime, and explicit elevation.
- Destination allowlists and prevention of arbitrary lateral movement.
- File-transfer controls, malware handling, and provenance for tools/firmware.
- Out-of-band revocation and a local method to disable the path.
- Safe behavior if the remote session drops during a configuration change.
- Monitoring for access outside approved windows, unusual targets, repeated denial, and new tunnels.

## Vendor cloud and outbound tunnels

Inventory every device-originated cloud connection, destination, identity, purpose, data category, update behavior, and disablement path. Outbound TLS is not automatically trustworthy: validate destination identity, constrain DNS/routing, monitor changes, and understand whether the tunnel permits reverse administration.

## Prohibited shortcuts

- persistent shared remote-desktop credentials;
- consumer remote-access tools installed outside asset/change management;
- port forwarding directly to cameras, controllers, recorders, or panels;
- disabling certificate checks to reach an appliance;
- unmanaged support laptops bridging trusted and untrusted networks;
- leaving commissioning VPNs or firewall exceptions permanently enabled.

## Sources

- **NIST-800-46** — [NIST SP 800-46 Rev. 2: Guide to Enterprise Telework, Remote Access, and BYOD Security][NIST-800-46], accessed 2026-08-25.
- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT remote-access and architecture guidance, accessed 2026-08-25.
- **NIST-1800-45** — [NIST SP 1800-45: Operational Technology Remote Access][NIST-1800-45], final June 2026, accessed 2026-08-25.

[NIST-800-46]: https://csrc.nist.gov/pubs/sp/800/46/r2/final
[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[NIST-1800-45]: https://www.nccoe.nist.gov/projects/cybersecurity-water-and-wastewater-sector/ot-remote-access

## Related pages

- [Segmentation and conduits](segmentation-and-conduits.md)
- [Identity, authentication, and authorization](identity-authentication-and-authorization.md)
- [Operations and lifecycle](../07-operations-and-lifecycle/README.md)
