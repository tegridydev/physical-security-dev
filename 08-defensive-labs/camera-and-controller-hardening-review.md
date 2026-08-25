---
title: "Camera and controller hardening review"
summary: "An offline, version-scoped review of official product guidance and sanitized configuration artefacts against the security baseline."
page_type: lab
domains:
  - video
  - access-control
tags:
  - hardening
  - camera
  - controller
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: []
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Camera and controller hardening review

[Home](../README.md) / [Defensive labs](README.md) / Hardening review

Lab class: **Offline documentation and sanitized configuration fixture**

## Evidence-first procedure

1. Select a product scenario and record the represented model, hardware revision, firmware, enabled licences/profiles, and official hardening/security documentation.
2. Use a synthetic configuration or a sanitized, owner-supplied offline export. Do not obtain an export by contacting a device as part of this lab.
3. Compare with the [secure system baseline](../06-security-and-assurance/secure-system-baselines.md): identity, accounts, protocols, TLS, certificates, discovery, network flows, time, logs, update, storage, remote/cloud access and physical tamper.
4. For a controller, additionally review reader-link secure mode/key lifecycle, offline authorization, outputs/interlocks and server/cloud reconciliation.
5. For a camera, additionally review media/snapshot authorization, multicast, edge recording, privacy masks, analytics/events and signing/export support.
6. Record unsupported controls, unknown fields, evidence gaps, and candidate compensating measures without changing any product configuration.
7. Route change, rollback, and physical acceptance planning to the owner-approved [environment validation checklist](../10-sources-and-maintenance/manual-qa-checklist.md).

## Stop conditions

Stop if the artefact's provenance or version is uncertain, it exposes live credentials, media, personal data, or cryptographic material, or the review would require product, device, service, or network contact. Sanitize the artefact or move the work to the separately governed environment-validation process.

## Evidence checklist

- [ ] Represented model, hardware revision, firmware, licences, and profiles recorded
- [ ] Official hardening guide and security-advisory sources pinned to versions and dates
- [ ] Configuration fixture provenance, sanitization, digest, and handling classification recorded
- [ ] Accounts, protocols, TLS, time, logging, update, storage, remote access, and tamper controls reviewed
- [ ] Camera- or controller-specific controls and unknown fields recorded separately
- [ ] Gaps, compensating-control proposals, and evidence limits documented
- [ ] Any configuration change or physical acceptance work routed outside the lab section

## Related pages

- [Secure commissioning](../06-security-and-assurance/secure-commissioning-and-onboarding.md)
- [Vendor APIs](../04-vendor-apis/README.md)
