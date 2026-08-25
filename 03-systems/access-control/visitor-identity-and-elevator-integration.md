---
title: Visitor, Identity, and Elevator Integration
summary: Identity-source boundaries, visitor sponsorship, provisioning/reconciliation, temporary access, and safe lift-destination integration.
page_type: system
domains: [access-control, identity]
tags: [visitors, hr, identity, scim, elevators]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [RFC 7643, RFC 7644, PSIA PLAI]
coverage_limit: Integration model only; no lift safety/control sequence, destination-dispatch command, access policy, identity-proofing level, or local visitor/legal requirement.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Visitor, identity, and elevator integration

HR, identity governance, visitor management, PACS, and lift systems each own different facts. Integration should propagate the minimum approved intent, not make any one source omnipotent.

## Authority map

| System | Authoritative for | Must not imply automatically |
|---|---|---|
| HR/workforce | Employment/contract relationship attributes | Door/floor authorization |
| Identity governance | Account lifecycle, group/approval workflow | Physical presence or passage |
| Visitor management | Visit, sponsor, expected time, check-in status | Unsupervised access rights |
| PACS | Physical credentials, access rules, decisions, door audit | Employee/visitor master identity |
| Lift destination/control | Approved car/floor operation and safety logic | Identity lifecycle or building occupancy truth |

## Provisioning pipeline

```text
source change -> validate/map -> approval/policy -> PACS identity/credential/rules
 -> controller download/ack -> effective state reconciliation -> expiry/revocation
```

Use immutable source IDs and mapping versions; do not join people by display name/email alone. Effective start/end times, timezone, sponsor, site, role, credential status, and policy reason need explicit semantics. A successful API response is not proof all controllers are current.

[RFC 7643](https://www.rfc-editor.org/info/rfc7643) and [RFC 7644](https://www.rfc-editor.org/info/rfc7644) define SCIM user/group schema and HTTP provisioning protocol for cross-domain identity management. SCIM does not define PACS doors/access rules or complete authentication policy. PSIA's [PLAI overview](https://psialliance.org/all-about-plai/) specifically addresses dynamic physical/logical identity and privilege transfer to disparate PACS, based on its own specification scope.

## Visitor lifecycle

Require sponsor and purpose; verify the visitor under local policy; scope site/areas/schedule/escort; issue a visibly temporary, unique credential; activate at check-in rather than invitation where appropriate; expire/revoke automatically; record return/loss; and handle no-show/cancel/overstay. Do not expose host calendars, attendee lists, ID documents, photos, health/vehicle details, or movement beyond need.

Pre-registration links and QR credentials must be signed/scoped/fresh, protected against forwarding/reuse, and revocable. Reception overrides require reason and audit.

## Lift/elevator boundary

PACS may provide an approved floor set or destination request; the certified lift system retains motion, door, load, emergency, fire-service, and safety authority. Use the exact manufacturer-approved interface and local lift/fire standards. Never write controller registers or simulate safety inputs from a generic integration.

Distinguish credential permitted floors, submitted destination, accepted destination, assigned car, passenger entry, car movement, and arrival. A destination acknowledgement is not passage or safe transport.

## Failure and privacy

Define IdP/HR/visitor/PACS/lift/network/time outage, duplicate identity, delayed termination, expired visit, controller offline, visitor credential loss, destination rejection, emergency mode, and recovery. Emergency/accessible egress/operation must not depend on enterprise provisioning availability.

Reconcile active people/credentials/visits regularly; alert orphaned accounts, overlong validity, failed revocation, duplicate source links, and controller divergence. Keep movement/access histories purpose-limited and restricted.

Return to [Access-control systems](README.md).
