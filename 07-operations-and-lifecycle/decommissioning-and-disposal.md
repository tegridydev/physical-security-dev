---
title: "Decommissioning and disposal"
summary: "Remove data, identity, trust, network access, cloud ownership, licences, and recovery artifacts safely."
page_type: operations
domains:
  - operations
tags:
  - decommissioning
  - disposal
  - sanitization
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-88 Rev. 2"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Decommissioning and disposal

[Home](../README.md) / [Operations and lifecycle](README.md) / Decommissioning and disposal

Removing hardware does not remove its identities, data, credentials, certificates, cloud claim, API access, licences, backups or references from other systems. Decommissioning is a coordinated trust and data transition.

## Preconditions

- Confirm replacement coverage and safe physical behavior.
- Identify authoritative configuration, evidence, retention and legal-hold needs.
- Export only required records through an auditable process.
- Map device/workload certificates, shared keys, tokens, accounts, mobile credentials, broker ACLs, firewall rules, DNS/DHCP, monitoring, backups, vendor cloud and support contracts.
- Obtain manufacturer guidance for reset, ownership release, storage removal and licensed/certified functions.

## Removal sequence

1. Stop new assignments and integrations; announce the maintenance boundary.
2. Preserve required evidence, configuration and support records.
3. Revoke or remove accounts, certificates, tokens, shared keys and cloud ownership.
4. Remove routes, firewall policy, discovery, DNS/DHCP, broker/API permissions and monitoring exceptions.
5. Remove credentials and mappings from controller, VMS/PACS/PSIM, mobile and identity systems.
6. Sanitize storage using media- and sensitivity-appropriate methods; physically destroy when required.
7. Remove recovery copies and backups when retention permits.
8. Update inventories, diagrams, licences, risk records and certificate/source registers.
9. Complete a system-owner review confirming that no orphaned access, event noise, physical gap, or unsafe dependency remains.

## Transfer and resale

Factory reset is not proof that all storage, secure elements, cloud bindings, logs, edge recordings, certificates or recoverable data were removed. Record the exact sanitization method and verification limitation. Transfer must include explicit release from vendor/cloud tenancy and destruction or revocation of prior trust.

## Sources

- **NIST-800-88** — [NIST SP 800-88 Rev. 2: Guidelines for Media Sanitization][NIST-800-88], final September 2025, accessed 2026-08-25.
- **NISTIR-8259A** — [NISTIR 8259A IoT Device Cybersecurity Capability Core Baseline][NISTIR-8259A], device lifecycle capabilities, accessed 2026-08-25.

[NIST-800-88]: https://csrc.nist.gov/pubs/sp/800/88/r2/final
[NISTIR-8259A]: https://csrc.nist.gov/pubs/ir/8259/a/final

## Related pages

- [Certificate and account lifecycle](certificate-and-account-lifecycle.md)
- [Privacy and sensitive data](../06-security-and-assurance/privacy-and-sensitive-data.md)
- [Asset and configuration inventory](asset-and-configuration-inventory.md)
