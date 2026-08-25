---
title: Credential Lifecycle Systems
summary: Identity binding, issuance, activation, use, suspension, replacement, revocation, key management, and audit across physical credentials.
page_type: system
domains: [access-control, identity]
tags: [credentials, issuance, revocation, card-management, lifecycle]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [ISO/IEC 14443 series, ISO/IEC 7816 series, ONVIF Profile A]
coverage_limit: Governance/system model only; no live credential values, keys, cloning, encoding, bypass, or product-specific issuance procedure.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Credential lifecycle systems

A credential is a managed security object bound to an identity/account and access policy. The number printed or emitted by a card is only one identifier, often low assurance. Lifecycle failure—overlong validity, duplicate issue, delayed revocation, unsafe recovery—can defeat strong cryptography.

## Lifecycle

```text
request/sponsorship -> identity proof/binding -> approval -> manufacture/provision
 -> activate -> present/use -> renew/update -> suspend/revoke/expire
 -> replace/recover -> return/destroy -> retain minimal audit
```

Separate requester, approver, issuer/encoder/provisioning service, subject, PACS policy owner, key custodian, help desk/recovery, and auditor. High-risk issuance/key operations may require two-person control.

## Credential record

Store non-secret metadata:

- internal opaque credential ID and type/application/version;
- subject/account and sponsor with effective dates;
- physical/mobile token inventory ID/status;
- issuer, approval, assurance, issuance/activation/expiry/revocation times;
- permitted sites/access policy references, not uncontrolled copied rights;
- lost/stolen/replaced/returned linkage and reason;
- key/diversification version identifiers without secret material;
- last reconciliation and audit provenance.

Facility code/card number, chip UID, application account, mobile token, certificate, and PACS credential IDs are different namespaces. Preserve bit length/leading zeros and never infer format from a decimal display.

## System boundaries

ONVIF [Profile A](https://www.onvif.org/profiles/onvif-profile-a/) includes granting/revoking credentials plus schedules/access rules at the PACS interface. ISO/IEC 14443 and 7816 catalogue entries describe contactless/contact smart-card families, not the application/key scheme. Exact card technology and personalization specifications may be paid/licensed.

An HR disable should trigger controlled access reassessment, but employment status is not itself a complete physical-access policy. Use effective-dated changes, idempotent provisioning, acknowledgements, controller download/reconciliation, and exception handling.

## Recovery and replacement

Verify claimant and sponsor; mark old credential suspended/revoked before or atomically with replacement where operations allow; identify overlap exceptions; reconcile controllers and offline devices; and alert on later old-token use. Do not use easily discovered personal data as recovery proof.

Temporary/visitor credentials need sponsor, scope, start/end, collection/automatic expiry, reuse rules, and badge accountability. Shared credentials destroy attribution and should be avoided or explicitly governed.

## Security/privacy

- Protect issuance workstations, printers/encoders, mobile provisioning, HSM/key systems, stock, rejected cards, and exports.
- Never log keys, PINs, activation secrets, full credential numbers, biometric templates, or mobile tokens.
- Separate credential administration from door control and audit review.
- Monitor bulk issue/export, privilege changes, after-hours issuance, duplicate identifiers, stale active credentials, failed revocation, and controller divergence.
- Retain only lifecycle evidence needed for policy/legal purpose; access histories are not a general people-tracking dataset.

See [credentials and identity media](../../01-foundations/credentials-and-identity-media.md).

Return to [Access-control systems](README.md).
