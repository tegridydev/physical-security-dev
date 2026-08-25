---
title: "Secure commissioning and onboarding"
summary: "Establish unique device identity, trust, ownership, and minimum configuration without leaving bootstrap weaknesses."
page_type: security
domains:
  - cross-domain
tags:
  - commissioning
  - onboarding
  - bootstrap
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NISTIR 8259A"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Secure commissioning and onboarding

[Home](../README.md) / [Security and assurance](README.md) / Secure commissioning and onboarding

Commissioning is the transition from an untrusted or vendor-default device to an inventoried component with a verified owner, unique identity, approved software, trusted configuration, and documented recovery path.

> Commissioning procedures that touch locks, gates, alarms, elevators, fire interfaces, relays, or emergency communications require qualified personnel and an isolated, unoccupied test context. Software steps do not replace manufacturer or authority requirements.

## State machine

| State | Required properties | Exit evidence |
|---|---|---|
| Received | Model, serial, provenance, seals and expected firmware recorded | Inventory record and acceptance decision |
| Isolated | No production trust or routing; bootstrap exposure bounded | Defined commissioning network and authorized operator |
| Identified | Device identity and claimed model/firmware checked | Exact identifiers and source documentation |
| Owned | Default/shared credentials removed; local ownership established | Unique admin path and recovery custody |
| Trusted | Certificates/keys enrolled and trust anchors installed | Certificate/key identifiers and environment-validation result |
| Hardened | Unused services/accounts disabled; time, logging and update policy set | Approved configuration record |
| Integrated | Least-privilege flows and application authorization configured | Flow and permission matrix |
| Accepted | System owner approves functional, failure, and safety validation | Approved environment-validation record |

## Bootstrap hazards

- shared factory credentials or keys;
- unauthenticated discovery/configuration protocols;
- temporary HTTP or wireless setup networks left enabled;
- acceptance of self-signed certificates without an out-of-band identity check;
- permanent installation-mode keys or downgrade to legacy reader signaling;
- cloud claim codes exposed in labels, logs, screenshots, or email;
- reset workflows that re-enable insecure defaults;
- time-dependent certificates enrolled before trustworthy time exists.

## Developer requirements

- Make onboarding an explicit, auditable state machine rather than a hidden first-request shortcut.
- Bind the claimed device identity to independently obtained inventory or manufacturer evidence.
- Require intentional ownership transfer and prevent silent re-claiming.
- Make bootstrap credentials single-use or short-lived, rate-limited, and removable.
- Fail closed on identity mismatch while preserving safe local physical behavior.
- Provide idempotent enrollment and recovery from partial failure.
- Expose clear status without logging keys, tokens, credential IDs, or private topology.
- Treat factory reset and RMA as security transitions with key destruction and ownership removal.

## Acceptance record

Record exact product, hardware revision, firmware, enabled profiles, certificates/trust anchors, accounts, network flows, time source, update source, configuration export, recovery custodian, validation date, and approval owner. Keep live secret values out of design, acceptance, and inventory records.

## Sources

- **NISTIR-8259A** — [NISTIR 8259A: IoT Device Cybersecurity Capability Core Baseline][NISTIR-8259A], device identification, configuration, data protection, interface access, update and security-state awareness, accessed 2026-08-25.
- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT asset, architecture and lifecycle guidance, accessed 2026-08-25.

[NISTIR-8259A]: https://csrc.nist.gov/pubs/ir/8259/a/final
[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final

## Related pages

- [PKI, certificates, keys, and secrets](pki-certificates-keys-and-secrets.md)
- [Secure system baselines](secure-system-baselines.md)
- [Operations and lifecycle](../07-operations-and-lifecycle/README.md)
