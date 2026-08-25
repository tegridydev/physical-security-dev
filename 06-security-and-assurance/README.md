---
title: "Security and assurance"
summary: "Threat-led security guidance for physical-security protocols, devices, services, and integrations."
page_type: index
domains:
  - cross-domain
tags:
  - security
  - assurance
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-82 Rev. 3"
  - "NIST SP 800-218 Version 1.1"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Security and assurance

[Home](../README.md) / Security and assurance

This section turns protocol capabilities into defensible system properties. Encryption support alone does not make a deployment secure: identity, authorization, commissioning, key lifecycle, failure behavior, monitoring, recovery, and physical consequences all matter.

NIST includes physical access control, building automation, physical-environment monitoring, and other cyber-physical systems within operational technology, whose security must preserve performance, reliability, and safety [NIST-800-82]. At the **2026-08-25** baseline, Rev. 3 remains the final guide. NIST's Rev. 4 item is an **Initial Preliminary Draft / pre-draft call for comments**, published 2026-01-22; it is revision work, not a replacement final publication [NIST-800-82-R4].

## Start here

| Page | Purpose | Verification |
|---|---|---|
| [Threat modelling and trust boundaries](threat-modeling-and-trust-boundaries.md) | Model assets, actors, flows, abuse cases, and physical effects | V2 |
| [Segmentation and conduits](segmentation-and-conduits.md) | Isolate device, management, integration, and user planes | V2 |
| [Identity and authorization controls](identity-authentication-and-authorization.md) | Apply identity and permission controls to people, devices, services, and commands | V2 |
| [PKI, certificates, keys, and secrets](pki-certificates-keys-and-secrets.md) | Operate trust material through its full lifecycle | V2 |
| [Secure commissioning and onboarding](secure-commissioning-and-onboarding.md) | Establish device identity without permanent bootstrap weaknesses | V2 |
| [Secure protocol parsing](secure-protocol-parsing.md) | Build bounded, fail-closed parsers and state machines | V2 |
| [API and event security](api-and-event-security.md) | Protect commands, events, webhooks, and message brokers | V2 |
| [Remote access](remote-access.md) | Constrain support and administrative paths | V2 |
| [Firmware and software supply chain](firmware-updates-and-supply-chain.md) | Protect build, update, dependency, and provenance flows | V2 |
| [Vulnerability management](vulnerability-management-and-disclosure.md) | Triage advisories and coordinate remediation | V2 |
| [Logging, time, and evidence integrity](logging-time-and-evidence-integrity.md) | Preserve trustworthy audit and evidential context | V2 |
| [Privacy and sensitive data](privacy-and-sensitive-data.md) | Minimize exposure of surveillance, identity, and credential data | V2 |
| [Resilience, backup, and recovery](resilience-backup-and-recovery.md) | Design predictable degraded modes and recoverability | V2 |
| [Secure system baselines](secure-system-baselines.md) | Apply minimum controls by component role | V2 |

## Core invariants

- Treat observe, configure, administer, and actuate as different permission classes.
- Authenticate both endpoints where feasible; authorize every operation independently of transport security.
- Treat discovery, commissioning, time, update, and recovery paths as part of the attack surface.
- Prefer deny-by-default network and application policy, with named and reviewable exceptions.
- Preserve safe physical behavior when networks, identity providers, clouds, certificates, or clocks fail.
- Record exact model, firmware, protocol profile, secure-mode configuration, and trust anchors before asserting security or interoperability.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3: Guide to Operational Technology Security][NIST-800-82], final September 2023, accessed 2026-08-25.
- **NIST-800-82-R4** — [NIST SP 800-82 Rev. 4 Initial Preliminary Draft][NIST-800-82-R4], pre-draft call published 2026-01-22, accessed 2026-08-25.
- **NIST-SSDF** — [NIST SP 800-218: Secure Software Development Framework Version 1.1][NIST-SSDF], final February 2022, accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[NIST-800-82-R4]: https://csrc.nist.gov/pubs/sp/800/82/r4/iprd
[NIST-SSDF]: https://csrc.nist.gov/pubs/sp/800/218/final

## Related pages

- [Development and integration](../05-development-and-integration/README.md)
- [Operations and lifecycle](../07-operations-and-lifecycle/README.md)
- [Defensive labs](../08-defensive-labs/README.md)
