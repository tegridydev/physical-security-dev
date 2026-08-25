---
title: Integration Platforms
summary: Architecture and navigation for PSIM, BMS/SCADA, SIEM/SOAR, identity/HR/visitor, cloud/mobile, and multi-tenant platforms.
page_type: index
domains: [cross-domain, bms, ot, identity]
tags: [integration-platforms, psim, siem, identity, cloud]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST SP 800-82 Rev. 3, NIST SP 800-207, RFC 7643, RFC 7644]
coverage_limit: Platform-neutral architecture; vendor feature/API scope and organizational response authority require separate verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Integration platforms

An integration platform aggregates authority and sensitive data. Its value is correlation and workflow; its danger is silently turning observation paths into broad cross-domain control.

## Pages

- [PSIM and command platforms](psim-and-command-platforms.md)
- [BMS and SCADA integration](bms-and-scada-integration.md)
- [SIEM, SOAR, and case management](siem-soar-and-case-management.md)
- [HR, identity, and visitor integration](hr-identity-and-visitor-integration.md)
- [Cloud, mobile, and multi-tenant platforms](cloud-mobile-and-multi-tenant-platforms.md)

## Boundary pattern

```text
source-specific adapter -> canonical event/state -> policy/rules/workflow
 -> operator decision or separately authorized automation -> target adapter
```

Preserve original event IDs and provenance. Separate adapters and credentials by site, tenant, domain, and operation. A rule engine must not infer physical completion from command dispatch.

NIST [SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) includes physical access and building automation in OT and emphasizes safety/reliability. NIST [SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) rejects implicit trust based only on network location. Use those principles at every cross-domain boundary.

Return to [Systems](../README.md).

