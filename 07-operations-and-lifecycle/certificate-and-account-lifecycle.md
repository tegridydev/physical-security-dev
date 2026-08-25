---
title: "Certificate and account lifecycle"
summary: "Operate human, service, device and vendor access without expiry, orphaning, or shared-account drift."
page_type: operations
domains:
  - operations
tags:
  - certificates
  - accounts
  - access-review
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards:
  - "NIST SP 800-63-4"
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Certificate and account lifecycle

[Home](../README.md) / [Operations and lifecycle](README.md) / Certificate and account lifecycle

Treat device certificates, workload identities, API credentials, operator accounts, physical credentials, vendor access and break-glass access as separate inventories with linked owners and review triggers.

## Lifecycle events

| Event | Required actions |
|---|---|
| Join/install | Verify identity, issue unique least-privilege access, set expiry/review, record recovery owner |
| Move/change | Recalculate roles, sites, door/device scope, tenant and support access; remove inherited permissions |
| Certificate renewal | Validate name/key use, stage trust overlap, confirm time, deploy, verify, retire old trust |
| Suspected compromise | Revoke/disable, contain sessions, rotate related material, inspect use, restore trusted identity |
| Leave/remove | Disable promptly, revoke tokens/certificates/credentials, transfer ownership, preserve audit |
| Vendor engagement end | Remove accounts, tunnels, API keys, certificates, cloud delegation and local exceptions |
| Decommission | Destroy private keys/secrets and remove the asset from trust, directory, broker, cloud and recovery systems |

## Account rules

- Use named human accounts and unique service identities; prohibit shared daily administration.
- Separate operator, administrator, installer, audit, export and high-impact control roles.
- Set service credentials to non-interactive use and restrict origin/resource/action.
- Review dormant, orphaned, default, local fallback, vendor and break-glass identities.
- Rotate without embedding secrets in integration source or documentation.
- Monitor denied authentication, role changes, token issuance, certificate errors and use outside expected context.

## Certificate register

Record subject/service identity, issuer, serial/fingerprint, key usage, endpoints, trust anchors, issue/expiry, renewal method, owner, revocation mechanism, algorithm/profile, deployment status and dependent protocol. Alert early enough for change approval and staged rollout.

## Sources

- **NIST-800-63** — [NIST SP 800-63-4 Digital Identity Guidelines][NIST-800-63], accessed 2026-08-25.
- **NIST-800-57** — [NIST SP 800-57 Part 1 Rev. 5: Key Management][NIST-800-57], accessed 2026-08-25.

[NIST-800-63]: https://csrc.nist.gov/pubs/sp/800/63/4/final
[NIST-800-57]: https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final

## Related pages

- [PKI, certificates, keys, and secrets](../06-security-and-assurance/pki-certificates-keys-and-secrets.md)
- [Identity, authentication, and authorization](../06-security-and-assurance/identity-authentication-and-authorization.md)
- [Decommissioning and disposal](decommissioning-and-disposal.md)
