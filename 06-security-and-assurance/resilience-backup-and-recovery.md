---
title: "Resilience, backup, and recovery"
summary: "Predictable degraded modes, protected backups, restoration dependencies, and cyber-physical recovery."
page_type: security
domains:
  - operations
tags:
  - resilience
  - backup
  - recovery
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-82 Rev. 3"
  - "NIST SP 1339"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Resilience, backup, and recovery

[Home](../README.md) / [Security and assurance](README.md) / Resilience, backup, and recovery

Availability is not a single uptime percentage. A physical-security system must define what each edge device, controller, server, integration and operator can safely do when dependencies fail, and how authoritative state is reconciled after recovery.

## Dependency failure matrix

Evaluate loss of power, network path, DNS, DHCP, time, directory/IdP, CA/revocation, broker, database, storage, management server, controller, cloud, cellular path, primary site and operator workstation. For each dependency record:

- locally retained capability and duration;
- default physical behavior and safety authority;
- queue/storage capacity and overflow behavior;
- operator indication and monitoring evidence;
- retry/backoff and failover sequence;
- split-brain or duplicate-command risk;
- recovery ordering and state reconciliation;
- conditions requiring qualified/manual intervention.

## Backup scope

Back up more than application databases: device/controller configuration, system topology, identities and roles, schedules and rules, certificates and trust anchors, encryption/signing-key custody information, licence/entitlement data, integration mappings, broker configuration, evidence indexes, firmware/software installers, documentation, and recovery credentials.

Keep keys and secrets under appropriate separate protection; a configuration backup that cannot be decrypted or a backup that exposes every private key is not a workable recovery design.

## Backup properties

- defined source and consistency point;
- authenticated and encrypted transfer;
- immutable or separately administered copy;
- retention and deletion aligned with sensitive-data policy;
- inventory of dependencies needed to restore;
- integrity verification and anomaly monitoring;
- protected recovery credentials and break-glass access;
- controlled restoration exercise with exact versions, accountable owner, and observed result.

## Recovery sequence

1. Establish safety and preserve relevant evidence.
2. Contain compromised trust, accounts, network paths and update sources.
3. Choose a known-good hardware, firmware, software and configuration baseline.
4. Restore identity, trust, time and core infrastructure in a documented order.
5. Restore management and integrations without immediately reconnecting untrusted devices.
6. Re-enrol or rekey endpoints where trust may be compromised.
7. Reconcile queued events, commands, credentials, schedules, recordings and controller state.
8. Complete and approve functional, failure, audit, and safety validation before returning to normal service.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], contingency and OT resilience guidance, accessed 2026-08-25.
- **NIST-1339** — [NIST SP 1339: Operational Technology Backup Quick Start Guide][NIST-1339], final June 2026, accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[NIST-1339]: https://csrc.nist.gov/pubs/sp/1339/final

## Related pages

- [Firmware updates and software supply chain](firmware-updates-and-supply-chain.md)
- [Logging, time, and evidence integrity](logging-time-and-evidence-integrity.md)
- [Operations and lifecycle](../07-operations-and-lifecycle/README.md)
