---
title: "Requirements and procurement"
summary: "Turn protocol support claims into versioned, secure, testable and maintainable acceptance requirements."
page_type: operations
domains:
  - operations
tags:
  - requirements
  - procurement
  - conformance
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-161 Rev. 1 Update 1"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Requirements and procurement

[Home](../README.md) / [Operations and lifecycle](README.md) / Requirements and procurement

A claim such as supports ONVIF, OSDP, MQTT, HTTPS, BACnet, REST, or encryption is not an acceptance requirement. Specify the exact profile/version, mandatory and optional features, secure mode, identity model, failure behavior, scale, evidence, and supported product/firmware combination.

## Requirement anatomy

Write each requirement with:

- actor and operational purpose;
- exact standard/profile/API and edition;
- required roles, services, operations and optional features;
- transport, secure mode, authentication and authorization;
- topology, network direction, discovery and port behavior;
- capacity, latency, retry, failover and offline expectations;
- malformed/unauthorized input behavior;
- logs, metrics, timestamps and audit correlation;
- compatibility and migration constraints;
- acceptance method and evidence;
- lifecycle, security advisory, support and update obligation.

## Conformance versus interoperability

Standards conformance is version- and implementation-specific. Require an official conformance listing where a programme exists, tied to exact model and firmware/software, then validate the deployment's selected feature combination. A vendor statement that a product supports a standard is not equivalent to certification or successful system interoperability.

## Security questions

- Are unique device identities and credentials supported at scale?
- Can plaintext and legacy fallback be disabled?
- How are certificates/keys enrolled, renewed, revoked, backed up and destroyed?
- Which roles can view media, export evidence, administer users, update firmware or actuate outputs?
- Which outbound cloud/support connections exist and can they be disabled or constrained?
- Are update artifacts signed, and what is the supported rollback/recovery path?
- What are the disclosure channel, support period and end-of-support notice?
- Is an SBOM or equivalent component disclosure available and versioned?
- How are logs exported securely, and which events identify security degradation?

## Acceptance evidence

Require architecture and data-flow diagrams, port/flow matrix, protocol/API references, conformance listing, hardening guide, security advisories, update/recovery documentation, role matrix, certificate workflow, event schema, capacity assumptions, backup/restore procedure, known limitations and exact test environment. Environment-specific acceptance remains necessary; documentation review cannot establish runtime behavior.

## Sources

- **NIST-800-161** — [NIST SP 800-161 Rev. 1 Update 1: Cybersecurity Supply Chain Risk Management Practices][NIST-800-161], final update dated 2024-11-01, accessed 2026-08-25.
- **NIST-SSDF** — [NIST SP 800-218, Secure Software Development Framework (SSDF) Version 1.1][NIST-SSDF], final supplier and secure-development vocabulary; SP 800-218 Rev. 1 / SSDF Version 1.2 remains an Initial Public Draft, accessed 2026-08-25.

[NIST-800-161]: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final
[NIST-SSDF]: https://csrc.nist.gov/pubs/sp/800/218/final

## Related pages

- [Interoperability, conformance, and profiles](../01-foundations/interoperability-conformance-and-profiles.md)
- [Vendor APIs](../04-vendor-apis/README.md)
- [Commissioning and acceptance](commissioning-and-acceptance.md)
