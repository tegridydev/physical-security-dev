---
title: Device and Edge Video APIs
summary: Catalogue of native device APIs, camera and intercom SDKs, and on-device application frameworks.
page_type: index
domains: [video, intercom, integration]
tags: [device-api, edge-applications, camera-sdk, intercom-api]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Vendor-native surfaces only at evidence-bounded capability level; model support, firmware compatibility, licences, and standard-protocol conformance require exact product verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Device and edge video APIs

[Vendor APIs](../README.md) / Device and edge video

Device APIs sit close to sensors, relays, microphones, credentials, firmware, and evidence. Treat discovery or video read access separately from configuration, account administration, PTZ, audio, door release, output control, application installation, and firmware operations.

## Pages

- [Axis VAPIX and ACAP](axis-vapix-and-acap.md)
- [Hikvision ISAPI and HEOP](hikvision-isapi-and-heop.md)
- [Dahua CGI and NetSDK](dahua-cgi-and-netsdk.md)
- [Hanwha SUNAPI and Open Platform](hanwha-sunapi-and-open-platform.md)
- [Bosch video and device integration](bosch-video-and-device-integration.md)
- [2N HTTP and platform APIs](2n-http-and-platform-apis.md)
- [Zenitel APIs and SDKs](zenitel-apis-and-sdks.md)

## Architecture choice

| Need | Prefer when supported | Main review question |
|---|---|---|
| Fleet-neutral discovery/media | Declared ONVIF or other standard profile | Does the exact model have a valid conformance declaration and required conditional features? |
| Vendor-specific configuration or events | Native HTTPS API | Can the integration discover API/version capabilities rather than infer them from model name? |
| High-throughput native media/client integration | Vendor SDK | Which package version, runtime, architecture, codec licence, and product builds are supported? |
| Analytics or business logic on device | Supported edge application framework | What are signing, sandboxing, resources, upgrade, permission, and rollback contracts? |
| Intercom/access actuation | Narrow native service with least privilege | What independent authorization and physical safety controls protect the command? |

## Minimum device record

Record vendor, model, hardware revision, firmware/OS, enabled API family and version, advertised capabilities, TLS and identity state, time source, roles, licences, installed edge apps, app signatures, resource limits, and rollback path. Do not enable legacy HTTP or broad administrator access merely because an old integration sample uses it.

Related foundations: [media streaming](../../01-foundations/media-streaming-fundamentals.md), [TLS and PKI](../../01-foundations/tls-pki-and-certificates.md), [multicast and discovery](../../01-foundations/multicast-discovery-and-nat.md), and [secure commissioning](../../06-security-and-assurance/secure-commissioning-and-onboarding.md).

