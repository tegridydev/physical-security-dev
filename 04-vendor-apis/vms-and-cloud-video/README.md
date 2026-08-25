---
title: VMS and Cloud Video APIs
summary: Catalogue of VMS SDKs, server and client plug-in frameworks, API gateways, cloud video APIs, media surfaces, and event integrations.
page_type: index
domains: [video, integration]
tags: [vms-sdk, cloud-video, media-api, event-api]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Vendor-owned integration surfaces and public evidence only; product editions, licences, regions, media rights, retention, and certified compatibility require project-specific confirmation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# VMS and cloud video APIs

[Vendor APIs](../README.md) / VMS and cloud video

Choose the narrowest supported integration mode. A language-neutral protocol or REST API reduces in-process coupling; an SDK component can expose richer media and object models; a client or server plug-in can deliver the deepest workflow integration but inherits the host process, release, signing, and support constraints.

## Pages

- [Milestone MIP SDK and API Gateway](milestone-mip-sdk-and-api-gateway.md)
- [Genetec Security Center SDK and Web API](genetec-security-center-sdk-and-web-api.md)
- [Network Optix Nx Meta APIs and SDKs](network-optix-nx-meta-apis-and-sdks.md)
- [Motorola Solutions and Avigilon integration surfaces](motorola-avigilon-integration-surfaces.md)
- [Eagle Eye Video API](eagle-eye-video-api.md)
- [Verkada Command APIs](verkada-command-apis.md)

## Integration-mode decision

| Mode | Strength | Coupling and risk |
|---|---|---|
| Remote REST/protocol | Process and language isolation; simpler least privilege | May expose less host UI/media functionality; auth and event recovery remain yours |
| Vendor component/library | Rich object and media access | Runtime, architecture, dependency, licence, and release coupling |
| In-process plug-in | Native UI/workflow and host services | Highest crash, privilege, signing, deployment, and upgrade impact |
| Cloud API | Vendor-managed reachability and elastic service | Tenant/region identity, rate limits, data residency, service lifecycle, and outage dependency |
| Media URL/session | Efficient browser/player delivery | Short-lived authorization, codec/container, privacy, export, and redistribution constraints |

## Non-negotiable controls

- Authorize metadata, live view, playback, export, audio, PTZ, configuration, and administration independently.
- Treat a returned media URL or session token as a secret with evidence-level sensitivity.
- Never infer durable event delivery; document cursors, acknowledgement, replay window, ordering, and reconciliation.
- Pin SDK and VMS builds and rehearse upgrades against vendor compatibility statements.
- Preserve source time, ingest time, camera/VMS identity, tenant/site, event ID, and correlation through normalization.
- Keep evidence export immutable and separate from convenience snapshots or transcodes.

See [VMS, NVR, and VSaaS architecture](../../03-systems/video-surveillance/vms-nvr-and-vsaas.md), [recording and retention](../../03-systems/video-surveillance/recording-storage-and-retention.md), [event security](../../06-security-and-assurance/api-and-event-security.md), and [adapter patterns](../../05-development-and-integration/patterns/adapters-gateways-and-translation.md).

