---
title: "Secure system baselines"
summary: "Minimum security outcomes for cameras, recorders, access-control components, alarm systems, gateways, and management services."
page_type: security
domains:
  - cross-domain
tags:
  - baseline
  - hardening
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-82 Rev. 3"
  - "NISTIR 8259A"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Secure system baselines

[Home](../README.md) / [Security and assurance](README.md) / Secure system baselines

These are minimum engineering outcomes, not universal vendor configuration commands. Apply exact manufacturer guidance, model/firmware capabilities, operational risk, and local safety requirements. Record every unsupported control and compensating measure.

## Universal baseline

- Inventory exact hardware, firmware/software, enabled protocols, interfaces, licences and support status.
- Remove or change default/shared credentials; issue unique device/workload identity.
- Enable the strongest supported authenticated encrypted mode and validate peer identity.
- Disable unused services, discovery after commissioning where feasible, legacy fallback, unused accounts and unmanaged cloud access.
- Enforce role- and object-scoped authorization for viewing, administration, export, credential management and actuation.
- Segment device, management, integration, operator, monitoring and support paths.
- Configure trustworthy time, centralized health/security logging, bounded storage and alerting.
- Verify signed update provenance and maintain a recovery/rollback path.
- Back up configuration and trust dependencies under separate protection.
- Document safe degraded behavior, physical tamper controls, privacy/retention and decommissioning.

## Component additions

| Component | Additional minimum outcomes |
|---|---|
| Camera/encoder | Separate media view from configuration; protect RTSP/media credentials; constrain multicast; disable anonymous snapshots; mask sensitive areas; monitor stream/config/tamper/time changes |
| NVR/VMS/VSaaS | Separate operator/admin/export roles; protect recording and signing keys; constrain device onboarding; audit search/export/delete; capacity and retention alarms; secure failover |
| Reader/controller/PACS | Prefer authenticated supervised reader links; remove installation/default keys; protect credential lifecycle; authorize outputs separately; preserve certified egress/fire dependencies |
| Alarm/intercom | Protect receiver accounts and event origin; use dual-path supervision appropriately; secure audio/video and call control; never allow integrations to suppress certified behavior |
| Gateway/broker | Unique workload identities; per-direction/topic/API policy; schema and size limits; bounded queues/retries; no transparent insecure transit; full command/event correlation |
| Management server | Harden host/database; separate service accounts; protect admin interface, backups and API secrets; control plugins/SDKs; monitor privilege and policy changes |
| Operator workstation | Managed endpoint, strong login, least privilege, controlled export/removable media, screen/privacy protection, no direct device administration by default |
| Cloud connector | Explicit tenancy and data flow; mTLS/workload identity; constrained outbound destinations; token/key rotation; offline behavior; vendor-support and deletion/export boundaries |

## Legacy exception record

When a device cannot meet the baseline, record the missing property, exact affected interface, exploit/precondition, business and physical impact, isolation, upstream control, monitoring, replacement target, accountable risk owner, and expiry/review date. Avoid vague entries such as accepted because legacy.

## Environment validation record

Validate the resulting configuration in a representative non-production environment against the applicable manufacturer documentation. Capture the exact version, commands/settings, expected and observed result, rollback path, accountable reviewer, and limitations in the environment-validation record.

## Sources

- **NIST-800-82** — [NIST SP 800-82 Rev. 3][NIST-800-82], OT security controls and architecture, accessed 2026-08-25.
- **NISTIR-8259A** — [NISTIR 8259A IoT Device Cybersecurity Capability Core Baseline][NISTIR-8259A], accessed 2026-08-25.
- **CISA-SBD** — [CISA Secure by Design][CISA-SBD], manufacturer principles and guidance, accessed 2026-08-25.

[NIST-800-82]: https://csrc.nist.gov/pubs/sp/800/82/r3/final
[NISTIR-8259A]: https://csrc.nist.gov/pubs/ir/8259/a/final
[CISA-SBD]: https://www.cisa.gov/securebydesign

## Related pages

- [Secure commissioning and onboarding](secure-commissioning-and-onboarding.md)
- [Segmentation and conduits](segmentation-and-conduits.md)
- [System architectures](../03-systems/README.md)
