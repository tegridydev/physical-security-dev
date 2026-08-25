---
title: "Change, firmware, and patching"
summary: "Plan versioned changes around protocol compatibility, physical availability, evidence, and recovery."
page_type: operations
domains:
  - operations
tags:
  - change-management
  - patching
  - firmware
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-40 Rev. 4"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Change, firmware, and patching

[Home](../README.md) / [Operations and lifecycle](README.md) / Change, firmware, and patching

An update can change authentication, certificates, protocol profiles, codecs, schemas, SDK behavior, database formats, device drivers, discovery, firewall flows, storage use and safety-related integration timing. Read release notes and security advisories for every intermediate and target version.

## Change record

- purpose, risk and urgency;
- exact source and target versions;
- affected assets, protocols, profiles, dependencies and integrations;
- vendor support and artifact/signature evidence;
- configuration/data format and downgrade compatibility;
- expected service and physical impact;
- prerequisite backups and recovery credentials;
- staged sequence, hold points and stop conditions;
- environment acceptance cases and evidence;
- rollback/rebuild plan and decision authority;
- inventory, baseline and documentation updates.

## Staging strategy

Use representative non-production equipment where available, then a bounded pilot that does not compromise required coverage or safety. Validate authentication, secure transport, discovery, streams, events, control authorization, time, logging, storage, offline/failover, backup/restore, and integrations. Record expected and observed results, approval, limitations, and stop conditions before expanding the pilot.

## Emergency mitigation

When a fix cannot be deployed immediately, record affected versions and exposure, disable the vulnerable interface/feature where safe, restrict network and identity paths, increase monitoring, preserve evidence, and set a dated replacement or remediation decision. A compensating control must not create an undocumented life-safety or availability failure.

## Rollback cautions

Downgrade may be blocked, unsupported, erase configuration, invalidate signatures, require database rollback, re-enable vulnerable defaults, or break certificate/key formats. Prefer a documented recovery image and configuration restore over assuming a version downgrade is reversible.

## Sources

- **NIST-800-40** — [NIST SP 800-40 Rev. 4: Guide to Enterprise Patch Management Planning][NIST-800-40], accessed 2026-08-25.
- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT change and patch considerations, accessed 2026-08-25.

[NIST-800-40]: https://csrc.nist.gov/pubs/sp/800/40/r4/final
[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## Related pages

- [Firmware and supply chain](../06-security-and-assurance/firmware-updates-and-supply-chain.md)
- [Asset and configuration inventory](asset-and-configuration-inventory.md)
- [Commissioning and acceptance](commissioning-and-acceptance.md)
