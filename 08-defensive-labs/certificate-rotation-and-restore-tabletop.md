---
title: "Certificate rotation and restore tabletop"
summary: "Reason through trust overlap, expiry, rollback, backup restoration, and dependency ordering without changing a system."
page_type: lab
domains:
  - cross-domain
tags:
  - certificates
  - tabletop
  - recovery
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 5280"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Certificate rotation and restore tabletop

[Home](../README.md) / [Defensive labs](README.md) / Certificate rotation tabletop

Lab class: **Tabletop**

## Scenario

A management-service issuing CA will expire in 30 days. Cameras, controllers, gateways, brokers and operator clients trust it through different deployment mechanisms. A recent backup contains the old trust state, and several field devices can be updated only through a gateway.

## Discussion sequence

1. Inventory every certificate, trust anchor, service name, client and owner.
2. Identify firmware/client limitations and whether dual trust/overlap is supported.
3. Establish trustworthy time and alerting.
4. Define issuance, key generation/storage and approval for the replacement chain.
5. Sequence trust-anchor distribution before leaf replacement without creating an unintended broader trust set.
6. Define validation evidence, hold points and rollback at each cohort.
7. Determine how restored backups avoid reinstating expired or compromised trust.
8. Plan emergency revocation/distrust and temporarily disconnected assets.
9. Define safe service behavior when validation fails; reject plaintext/accept-all fallback.

## Outputs

Produce a certificate inventory, dependency graph, cohort sequence, overlap window, monitoring plan, rollback plan, backup-reconciliation rule, ownership map, and separately governed environment-validation cases.

## Review checklist

- [ ] Certificate, service-name, trust-anchor, client, owner, and expiry inventory completed
- [ ] Dual-trust, firmware/client limitations, time dependency, and cohort constraints mapped
- [ ] Key generation/storage, issuance approval, trust distribution, and leaf replacement sequenced
- [ ] Hold points, monitoring evidence, rollback, and emergency distrust/revocation decisions assigned
- [ ] Backup restoration cannot silently reinstate expired or compromised trust
- [ ] Validation failure rejects plaintext, accept-all, and unapproved bypass behavior
- [ ] Physical or operational certificate acceptance cases routed outside the tabletop

## Sources

- [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280), accessed 2026-08-25.

## Related pages

- [PKI, certificates, keys, and secrets](../06-security-and-assurance/pki-certificates-keys-and-secrets.md)
- [Resilience, backup, and recovery](../06-security-and-assurance/resilience-backup-and-recovery.md)
