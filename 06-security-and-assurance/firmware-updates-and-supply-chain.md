---
title: "Firmware updates and software supply chain"
summary: "Provenance, dependency, signing, update, rollback, and support-lifecycle controls for physical-security products."
page_type: security
domains:
  - development
  - operations
tags:
  - firmware
  - sbom
  - supply-chain
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-218 Version 1.1"
  - "NIST SP 800-193"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Firmware updates and software supply chain

[Home](../README.md) / [Security and assurance](README.md) / Firmware and supply chain

Physical-security deployments combine embedded firmware, operating systems, codecs, protocol libraries, SDKs, drivers, containers, mobile applications, cloud services, browser components, and integration code. The assurance boundary includes every component that can alter data, policy, identity, or physical behavior.

## Product and dependency record

For each deployed component record supplier, exact model/package, hardware revision, firmware/software build, bootloader where relevant, enabled modules, dependencies, licence, support end date, update source, signing identity, configuration compatibility, and rollback constraints. A marketing product name is not a sufficient vulnerability identifier.

## Update trust chain

An update workflow should establish:

1. provenance from an official authenticated distribution channel;
2. integrity and publisher identity using a verified signature or equivalent mechanism;
3. authorization for the exact product, hardware and target version;
4. anti-rollback policy appropriate to recovery and safety needs;
5. compatibility with configuration, profiles, integrations, certificates and evidence formats;
6. atomic or recoverable installation and bounded reboot behavior;
7. post-update version, configuration, trust and service-state evidence;
8. an environment-validated recovery route that does not reintroduce known-vulnerable trust.

Never treat a hash copied from the same unauthenticated location as independent provenance. Keep update-signing trust separate from ordinary TLS distribution trust.

## SBOM and component analysis

An SBOM helps map a disclosed component issue to products, but presence alone does not prove reachability or exploitability, and absence from an SBOM does not prove absence from a binary. Preserve supplier statements, component versions, build features, exposure, compensating controls, and the evidence supporting the triage decision.

## Physical-service constraints

Updates may interrupt recording, door decisions, alarm signaling, intercom, time, analytics, or failover. Sequence redundant components, preserve certified local functions, define maintenance state, notify operators, and avoid updates during high-risk operating windows. Firmware procedures for life-safety-connected equipment must come from the manufacturer and qualified authority.

## Developer controls

- Protect source, build workers, signing services and release credentials as production assets.
- Pin and review dependencies; record why each dependency is needed.
- Generate reproducible provenance where the build system supports it.
- Sign artifacts after controlled build and before distribution.
- Separate development, test and production signing roots.
- Verify updates in the device boot/update path, not only in the management UI.
- Make downgrade and recovery decisions explicit and auditable.
- Publish vulnerability reporting, support-period and end-of-support information.

## Sources

- **NIST-SSDF** — [NIST SP 800-218 Version 1.1][NIST-SSDF], secure development and release practices, accessed 2026-08-25.
- **NIST-800-193** — [NIST SP 800-193: Platform Firmware Resiliency Guidelines][NIST-800-193], protection, detection and recovery principles, accessed 2026-08-25.
- **NTIA-SBOM** — [NTIA Software Bill of Materials resources][NTIA-SBOM], accessed 2026-08-25.

[NIST-SSDF]: https://csrc.nist.gov/pubs/sp/800/218/final
[NIST-800-193]: https://csrc.nist.gov/pubs/sp/800/193/final
[NTIA-SBOM]: https://www.ntia.gov/page/software-bill-materials

## Related pages

- [Vulnerability management and disclosure](vulnerability-management-and-disclosure.md)
- [Secure commissioning and onboarding](secure-commissioning-and-onboarding.md)
- [Operations and lifecycle](../07-operations-and-lifecycle/README.md)
