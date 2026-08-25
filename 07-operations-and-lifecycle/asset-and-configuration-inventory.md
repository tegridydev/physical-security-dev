---
title: "Asset and configuration inventory"
summary: "Version-specific inventory for devices, software, protocols, identities, trust, topology, and data."
page_type: operations
domains:
  - operations
tags:
  - inventory
  - configuration
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-82 Rev. 3"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Asset and configuration inventory

[Home](../README.md) / [Operations and lifecycle](README.md) / Asset and configuration inventory

An inventory must support vulnerability triage, flow control, certificate renewal, interoperability, recovery, privacy review and decommissioning. IP address and product name alone do not identify a physical-security asset adequately.

## Minimum asset record

| Category | Fields |
|---|---|
| Identity | Stable asset ID, site/zone, role, manufacturer, model, serial, hardware revision |
| Software | Firmware, OS, application, driver/SDK/plugin and dependency versions |
| Interfaces | Physical ports, MAC/IP, serial address, radio identities, cloud tenant/device ID |
| Protocols | Exact versions/profiles, secure mode, role, ports, discovery and enabled options |
| Trust | Certificate fingerprints/serials, issuer, expiry, key purpose, shared-key identifier, enrollment owner |
| Access | Admin/operator/service/vendor identities and role/policy mapping |
| Data | Media/events/credentials/biometrics stored or transmitted, retention and destinations |
| Lifecycle | Install, warranty/support end, update source, backup, replacement and disposal status |
| Safety | Actuators/interlocks/egress/fire/elevator dependencies and responsible authority |
| Evidence | Last configuration review, environment validation, deviations, approvals, and source documents |

Do not store passwords, private keys, bearer tokens, biometric templates or full credentials in the inventory. Store references to an approved secret or evidence system.

## Configuration baseline

Capture enabled services, users/roles, network and discovery settings, TLS/certificate policy, protocol/profile options, time, logging, storage/retention, event subscriptions, broker topics/ACLs, integration mappings, update channel, failover/offline behavior and disabled legacy interfaces. Prefer structured exports where supported, but protect them as sensitive configuration.

## Reconciliation

Reconcile authoritative management inventory with network observation, vendor cloud, controller/server databases, certificate register and physical survey. Discovery can find unexpected assets but must not be treated as the sole inventory because offline, segmented and serial devices may be absent.

## Change triggers

Update inventory after installation, replacement, firmware/software change, role or certificate change, topology/flow change, protocol/profile enablement, cloud ownership transfer, incident, backup restoration and decommissioning. Preserve history sufficient to interpret old events and evidence.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], asset management and OT architecture guidance, accessed 2026-08-25.
- **CISA-ASSET** — [CISA Foundations for OT Cybersecurity: Asset Inventory Guidance][CISA-ASSET], accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[CISA-ASSET]: https://www.cisa.gov/resources-tools/resources/foundations-ot-cybersecurity-asset-inventory-guidance-owners-and-operators

## Related pages

- [Change, firmware, and patching](change-firmware-and-patching.md)
- [Certificate and account lifecycle](certificate-and-account-lifecycle.md)
- [Vulnerability management](../06-security-and-assurance/vulnerability-management-and-disclosure.md)
