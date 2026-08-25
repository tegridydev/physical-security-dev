---
title: VMS, NVR, and VSaaS Platforms
summary: Roles, deployment models, authority, tenancy, media/event paths, availability, and migration for video-management platforms.
page_type: system
domains: [video]
tags: [vms, nvr, vsaas, cloud-video, video-management]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: ["IEC 62676-2-11:2024", ONVIF Profiles T G M, ONVIF Profile V Release Candidate]
coverage_limit: Platform-neutral architecture; licensed features, API behavior, residency, and service commitments require exact vendor/contract verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# VMS, NVR, and VSaaS platforms

A video management system (VMS) coordinates devices, live viewing, recording, search, events, users, audit, and integrations. A network video recorder (NVR) packages some or all roles in an appliance. Video Surveillance as a Service (VSaaS) moves management and often storage/processing to cloud services, but does not remove edge or network dependencies.

## Role decomposition

| Role | Authority/data |
|---|---|
| Device registry | Logical camera/source IDs, capabilities, credentials, configuration intent |
| Media ingress | Sessions, stream selection, receive health, transcoding/relay |
| Recording service | Recording policy, segment/index creation, retention/deletion |
| Event service | Subscriptions, normalization, rules, bookmarks/incidents |
| Client/access service | User/workload auth, site/tenant/resource permissions |
| Federation/cloud control | Site registry, remote access, tenancy, regional services |
| Export/evidence | Search selection, native/open export, provenance, audit |

Products combine these roles; design redundancy and privilege around the roles, not one product name.

## Deployment patterns

- **Central VMS:** cameras stream to site/datacentre recorders and management servers.
- **Distributed/federated:** sites retain local recording/control; a central service searches/views via federation.
- **Edge recording:** camera/local device records and VMS retrieves/reconciles gaps, often using ONVIF Profile G or native APIs.
- **Hybrid cloud:** on-site gateway/recording plus cloud management/remote access/analytics.
- **Cloud-first VSaaS:** device or gateway initiates authenticated uplink; recording may use local buffer and cloud object storage.

[IEC 62676-2-11:2024](https://webstore.iec.ch/en/publication/66755) defines public-scope interoperability profiles for VMS/cloud VSaaS interfaces, including levels from export to exclusive video control. It is not a blanket authorization to share video.

ONVIF Profile V is still a **Release Candidate** on 2026-08-25. The [official FAQ](https://www.onvif.org/profiles/profile-v/faq/) says products cannot claim conformance until finalization and testing. Treat current Profile V designs as changeable.

## Data and control boundaries

Separate live view, playback/export, event/metadata, device management, PTZ/I/O, platform administration, and support access. A cloud viewer should not inherit camera firmware or relay rights. Federation must preserve site/tenant identity and distinguish local authority from cached central state.

## Availability

Define behavior under camera, recorder, storage, database, message bus, identity provider, DNS/time, WAN, cloud region, license, and certificate outage. Record recovery point/objective, buffer capacity, gap reconciliation, split-brain/fencing, client failover, and whether local operators retain required functions.

Do not assume high availability because multiple nodes exist. Validate shared dependencies, storage quorum, licenses, virtual infrastructure, switches/PoE, and recovery procedures.

## Cloud and tenancy

- Establish customer/vendor controller/processor roles, region, subprocessors, support access, retention/deletion, legal hold, export, and tenant exit.
- Use distinct device/workload/user identities and resource/site/tenant authorization; test cross-tenant denials.
- Limit device egress to named services and verify certificate/token bootstrap and rotation.
- Understand who can decrypt live, recorded, analytic, and exported data and where keys reside.
- Plan service termination: credential revocation, local ownership, bulk evidence/config export, deletion confirmation, and replacement path.

## Migration/acceptance

Build a capability intersection for exact device/client profiles, codecs, events, analytics, PTZ, recording, audio, I/O, certificates, and APIs. Test migration with representative retention, bookmarks, users/roles, audit, time, edge gaps, exports, and rollback. Never equate an imported camera list with a complete evidential migration.

Return to [Video-surveillance systems](README.md).
