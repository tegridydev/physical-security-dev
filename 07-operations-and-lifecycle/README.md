---
title: "Operations and lifecycle"
summary: "Protocol-aware practices from requirements and commissioning through monitoring, response, recovery, and disposal."
page_type: index
domains:
  - operations
tags:
  - lifecycle
  - operations
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Operations and lifecycle

[Home](../README.md) / Operations and lifecycle

Secure protocol engineering continues after integration code ships. Versions, certificates, time, storage, vendor services, permissions, network paths, physical dependencies, and support status change throughout the deployment.

> Procedures involving doors, gates, alarms, elevators, fire interfaces, emergency communications, relays, or occupied sites require product-specific instructions, qualified personnel, system-owner approval, and the applicable local authority.

## Lifecycle pages

| Page | Outcome |
|---|---|
| [Requirements and procurement](requirements-and-procurement.md) | Testable protocol, security, support, and evidence requirements |
| [Site survey and design records](site-survey-and-design-records.md) | Complete topology, dependency, capacity, and boundary inputs |
| [Commissioning and acceptance](commissioning-and-acceptance.md) | Controlled transition from delivery to service |
| [Asset and configuration inventory](asset-and-configuration-inventory.md) | Version-specific source of operational truth |
| [Change, firmware, and patching](change-firmware-and-patching.md) | Risk-aware change and recovery workflow |
| [Certificate and account lifecycle](certificate-and-account-lifecycle.md) | Prevent expiry, orphaning, and shared access |
| [Monitoring and health](monitoring-and-health.md) | Detect loss of security function and degraded evidence |
| [Incident response and evidence](incident-response-and-evidence.md) | Contain cyber risk without creating unsafe physical effects |
| [Decommissioning and disposal](decommissioning-and-disposal.md) | Remove trust, data, access, and vendor ownership |
| [Operational runbooks](runbooks.md) | Decision trees for common failures |

## Operating record

Every system should have named sources of truth for inventory, topology, approved flows, configuration baseline, account/role model, certificates and trust anchors, protocol/profile versions, vendor support, backup/recovery, monitoring, and unresolved risks. Those records must use exact model and version identifiers.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], operational technology lifecycle guidance, accessed 2026-08-25.
- **NIST-CSF** — [NIST Cybersecurity Framework 2.0][NIST-CSF], accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[NIST-CSF]: https://www.nist.gov/cyberframework

## Related pages

- [Security and assurance](../06-security-and-assurance/README.md)
- [Defensive labs](../08-defensive-labs/README.md)
- [Reference](../09-reference/README.md)
