---
title: "TLS certificate-chain review"
summary: "A passive review of endpoint identity, trust path, key use, expiry, and failure expectations."
page_type: lab
domains:
  - defensive-labs
tags:
  - tls
  - certificates
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "RFC 5280"
  - "RFC 8446"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# TLS certificate-chain review

[Home](../README.md) / [Defensive labs](README.md) / TLS certificate review

Lab class: **Offline certificate and policy fixtures**

## Purpose

Determine what endpoint identity is asserted, which trust anchor authorizes it, whether the client checks the intended service name, and how renewal or failure will behave.

## Procedure

1. Record the represented service name, role, protocol, product, and software/firmware context supplied with the fixture.
2. Use a synthetic chain or a sanitized, owner-supplied certificate export. Do not retrieve a chain from an endpoint as part of this lab, and never include private keys.
3. Record subject alternative names, issuer/chain, serial, validity, public-key algorithm/size, signature, key usage and extended key usage.
4. Determine whether the expected DNS/IP identity is covered and whether the documented client policy requires name and chain validation.
5. Identify trust-anchor distribution, intermediate availability and revocation/distrust behavior.
6. Determine whether mutual TLS is used and how client authorization maps the certificate identity.
7. Record expiry monitoring, renewal owner, overlap, rollback and offline time dependency.
8. Create offline fixture variants for unknown CA, wrong hostname, expired certificate, invalid usage, broken chain, and unauthorized client identity; map each to the expected policy decision.

## Reject insecure conclusions

- Encryption observed does not prove endpoint identity was validated.
- A self-signed certificate is not automatically wrong, but its fingerprint/key must be established and managed through a trustworthy out-of-band process.
- A successful browser warning bypass is not an acceptable application trust model.
- Certificate pinning without a rotation/recovery design can create an availability failure.

## Evidence checklist

- [ ] Certificate fixture provenance, digest, represented service, and software context recorded
- [ ] Subject alternative names, chain order, trust anchor, validity, usages, algorithms, and key sizes reviewed
- [ ] Name-validation and trust-policy expectations distinguished from encryption alone
- [ ] Mutual-TLS identity-to-authorization mapping documented where applicable
- [ ] Unknown-CA, wrong-name, expiry, broken-chain, invalid-usage, and unauthorized-client fixtures assessed
- [ ] Renewal, overlap, revocation/distrust, rollback, time, and monitoring dependencies recorded
- [ ] Private keys and live credentials excluded from the evidence set

## Sources

- [RFC 5280](https://www.rfc-editor.org/rfc/rfc5280), accessed 2026-08-25.
- [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), accessed 2026-08-25.

## Related pages

- [PKI, certificates, keys, and secrets](../06-security-and-assurance/pki-certificates-keys-and-secrets.md)
- [Certificate and account lifecycle](../07-operations-and-lifecycle/certificate-and-account-lifecycle.md)
