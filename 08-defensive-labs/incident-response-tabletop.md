---
title: "Physical-security incident-response tabletop"
summary: "Coordinate cyber containment, continuing physical function, evidence, communication, and trusted recovery."
page_type: lab
domains:
  - cross-domain
tags:
  - incident-response
  - tabletop
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "NIST SP 800-61 Rev. 3"
coverage_limit: "Offline research and planning only; product or deployment acceptance belongs to separately governed environment validation."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Physical-security incident-response tabletop

[Home](../README.md) / [Defensive labs](README.md) / Incident-response tabletop

Lab class: **Tabletop**

## Scenario

An operator reports intermittent camera loss and delayed door events. Monitoring then detects a newly used vendor-support account, a management certificate change and outbound traffic from a gateway. Some controllers retain local operation; the team cannot yet trust timestamps across systems.

## Injects

1. A critical entrance is affected during an occupied period.
2. The vendor cloud status page reports no incident.
3. A recorder contains relevant footage but is near capacity.
4. A controller's audit disagrees with the central PACS timeline.
5. The support account is shared by multiple contractors.
6. The latest configuration backup postdates the suspected compromise.
7. A proposal to reboot or factory-reset affected devices would remove volatile evidence.

## Decisions to record

- human/physical safety authority and compensating coverage;
- incident scope and authoritative communication;
- narrow identity/network containment versus loss of function;
- evidence priorities, clock uncertainty and custody;
- vendor/monitoring-centre engagement;
- trust/key/account revocation and replacement;
- known-good build/configuration selection;
- controller/server/cloud state reconciliation;
- system-owner acceptance required before return to service;
- disclosure, lessons and evergreen KB updates.

## Success criteria

The team avoids unsafe blanket shutdown, preserves evidence, revokes narrow compromised access, maintains approved physical coverage, records uncertainty, chooses a trusted recovery basis and assigns every follow-up owner/date.

## Review checklist

- [ ] Safety, security, operations, privacy, legal, vendor, and communications roles assigned
- [ ] Incident scope, timestamp uncertainty, and authoritative communication path recorded
- [ ] Containment options evaluated against continuing physical-security and life-safety needs
- [ ] Volatile, video, controller, identity, network, and configuration evidence priorities documented
- [ ] Shared support identity, certificate change, outbound traffic, and backup-trust injects resolved
- [ ] Known-good recovery basis, credential/key replacement, reconciliation, and rollback defined
- [ ] Return-to-service authority, evidence, residual risk, follow-up owners, and dates assigned

## Sources

- [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), accessed 2026-08-25.
- [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final), accessed 2026-08-25.

## Related pages

- [Incident response and evidence](../07-operations-and-lifecycle/incident-response-and-evidence.md)
- [Operational runbooks](../07-operations-and-lifecycle/runbooks.md)
