---
title: Axis VAPIX and ACAP
summary: Publicly documented Axis device APIs, model-driven configuration services, API discovery, and the supported on-device ACAP application framework.
page_type: vendor-api
domains: [video, integration, development]
tags: [axis, vapix, acap, edge-applications, device-api]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Public Axis developer documentation reviewed on 2026-08-25; exact VAPIX category, API maturity, device model, AXIS OS, ACAP SDK, architecture, licence, and resource compatibility are not asserted.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Axis VAPIX and ACAP

[Vendor APIs](../README.md) / [Device and edge video](README.md) / Axis

Axis exposes two related but distinct integration planes. **VAPIX** is the device-facing API family; **ACAP** is the supported framework for applications that execute on compatible Axis devices. A third distinction matters inside VAPIX: long-established category APIs and newer model-driven Device Configuration APIs do not share one universal version or maturity level.

## Verified scope and access

| Surface | Purpose | Public evidence | Access and compatibility boundary |
|---|---|---|---|
| VAPIX | Open device API family organized by video, audio, analytics, events, I/O, security, system and configuration categories | Public reference | Each API publishes its own product/AXIS OS properties; presence must be discovered or checked |
| API Discovery Service | Enumerates public APIs and versions exposed by a device | Public reference; introduced with AXIS OS 8.50 | Older products/OS can differ; discovery itself does not grant authorization |
| Device Configuration APIs | Model-driven JSON/OpenAPI configuration services | Public reference; framework released in AXIS OS 12.3 | Individual APIs have independent alpha, beta, or released maturity and OS support |
| VAPIX Application API | Uploads, controls and manages ACAP applications and licences | Public reference | Administrative privilege and device/OS capability apply |
| ACAP | SDK and toolchain for supported on-device applications | Public portal and compatibility guide | Target device, architecture, AXIS OS/ACAP SDK, signing, resources and API support must align |

Core documentation is publicly readable without a developer-portal login. Device ownership, accounts, certificates, application packages, licences, and operational permissions remain separate.

## Version and capability contract

Do not use a model name alone as capability detection. Record:

- exact device model and hardware revision;
- installed AXIS OS and its support track;
- API Discovery Service output where available;
- VAPIX API name and reported version;
- property/capability gates named by the individual API;
- ACAP SDK version, target architecture and supported API set;
- edge-application package/signature and any application licence.

Axis states that, from AXIS OS 12, the ACAP version aligns with AXIS OS: AXIS OS 12.x and the 2026 LTS line use ACAP 12, while AXIS OS 11.x and the 2024 LTS line use ACAP 4. This is a compatibility naming rule, not permission to assume an application built for one target runs on every device in that line.

The supported-APIs reference is the boundary for ACAP. APIs inherited from the underlying operating system but not documented as supported can change without notice. Axis also says beta APIs are not for production. Treat alpha/beta configuration APIs as evaluation-only and pin their maturity in the design record.

## Authentication and authorization

Prefer HTTPS, validate the device certificate against the deployment trust policy, and provision a unique least-privileged integration identity. Do not normalize old examples using cleartext HTTP or broad administrator accounts into a current design.

The Application API contains administrative operations and requires an Administrator role for the documented management functions. Some Application API operations can return HTTP success while expressing an application-level error in the body; therefore, HTTP status alone is not a completion decision. Parse the documented result contract and then reconcile application state.

For an ACAP application calling local VAPIX services, Axis documents a virtual-host credential service from AXIS OS 11.6, reaching general availability in 11.9. Its credentials are held in memory and removed at reboot; the documented service has a finite account limit. Use only the supported D-Bus interface and design renewal after restart. Never scrape device files or rely on undocumented local credentials.

## Data, events, media, and commands

VAPIX is a family, not one schema. Media, event, analytics, I/O and configuration services can use different request, response and delivery models. For every selected API, capture:

- media profile, codec, transport and authorization lifetime;
- event namespace/schema, subscription renewal, source time and reconnect behavior;
- configuration read/write preconditions and post-write state verification;
- PTZ, audio, relay, door/intercom or application-management side effects;
- documented payload, connection and concurrency limits.

Do not assume a successful configuration response means a downstream sensor, application, stream consumer, or relay reached the intended physical state. Query authoritative state and preserve device-originated evidence.

## ACAP security and operations

Treat an edge application as privileged supply-chain software:

- minimize requested device APIs and filesystem/network access;
- pin SDK and base environment digests supplied by the supported toolchain;
- verify package origin and signing requirements;
- bound CPU, memory, storage, sockets, queue depth and log volume;
- handle camera reboot, application restart, time correction and network partition;
- keep secrets outside package source and logs;
- stage upgrade and rollback against the exact device/OS matrix.

Container tooling used to build or distribute ACAP environments does not itself create an isolation guarantee on the device. Use only the security and sandbox contract published for the target ACAP release.

## Lifecycle and compatibility

The Device Configuration framework was described as released at AXIS OS 12.3, but each member API retains its own maturity. ACAP 12 was the current documentation line observed on 2026-08-25. Re-check the supported API table and AXIS OS lifecycle before every release.

## Primary sources

- [VAPIX Library](https://developer.axis.com/vapix/) — public API catalogue, accessed 2026-08-25.
- [API Discovery Service](https://developer.axis.com/vapix/network-video/api-discovery-service/) — discovery and version boundary.
- [Device Configuration APIs](https://developer.axis.com/vapix/device-configuration/) and [framework overview](https://developer.axis.com/vapix/device-configuration/device-configuration-apis/) — maturity and AXIS OS boundary.
- [VAPIX Application API](https://developer.axis.com/vapix/applications/application-api/) — ACAP application management contract.
- [ACAP documentation](https://developer.axis.com/acap/) and [supported APIs](https://developer.axis.com/acap/reference/supported-apis/) — current framework and compatibility policy.
- [VAPIX access for ACAP applications](https://developer.axis.com/acap/3/develop-applications/vapix-access-for-acap-applications/) — supported local credential mechanism.

## Related pages

- [ONVIF](../../02-protocols/video-and-media/onvif.md)
- [Secure commissioning](../../06-security-and-assurance/secure-commissioning-and-onboarding.md)
- [Firmware and supply chain](../../06-security-and-assurance/firmware-updates-and-supply-chain.md)
