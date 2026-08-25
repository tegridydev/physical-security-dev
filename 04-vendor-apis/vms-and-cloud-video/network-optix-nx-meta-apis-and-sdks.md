---
title: Network Optix Nx Meta APIs and SDKs
summary: Public catalogue of Network Optix server REST, cloud, C++ plug-in SDK, developer-licence, release, and open-source client surfaces.
page_type: vendor-api
domains: [video, integration, development]
tags: [network-optix, nx-meta, nx-witness, rest-api, plugin-sdk]
scope: global with OEM/product and cloud differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Public Nx Meta developer and release documentation reviewed on 2026-08-25; OEM branding, exact server/API/SDK compatibility, credentials, licences, cloud region, build flags, and endpoint behavior require the target release contract.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Network Optix Nx Meta APIs and SDKs

[Vendor APIs](../README.md) / [VMS and cloud video](README.md) / Network Optix

Network Optix publishes several distinct developer surfaces through Nx Meta: the VMS **Server HTTP REST API**, a native **C++ Server Plugin SDK**, a **Cloud API**, and the source-available/open-source desktop client route. Nx technology is also OEMed; product branding alone is not a compatibility contract. Confirm the OEM release and enabled APIs with its supplier.

## Verified surface map

| Surface | Documented capability | Boundary |
|---|---|---|
| Server HTTP REST API | Resource/user management, live and recorded video, events/rules, PTZ and server functions | Installed server exposes its own Swagger/reference; API groups include newer, legacy and deprecated contracts |
| C++ Server Plugin SDK | Metadata, video-source and storage plug-ins | Native package must match supported server release/toolchain and licence |
| Cloud API | Cloud-account/system integration | Cloud programme, identity, tenant and region constraints apply |
| Open-source desktop client | Builds/customizes the Nx desktop client under published terms | Client source does not grant server/cloud APIs, licences, branding or support |

## Release and API version boundary

The official release page listed **Nx Meta VMS 6.1.2.42921**, published 2026-05-20, when reviewed on 2026-08-25. This dated observation is useful for source tracking only. OEM releases can lag, branch or rename components; use the build and SDK package supplied for the deployed product.

Nx documentation distinguishes new, legacy and deprecated REST API groups. Do not start new code on a legacy route because an old sample is easier to find. Retrieve the API description from the target server/build, pin the operation/schema version, and monitor deprecation/release notes for breaking changes.

## Authentication and authorization

Use the authentication mechanism documented by the exact server or Cloud API release. Protect credentials/tokens outside source and logs, require HTTPS with verified identity, and assign a dedicated least-privileged account. Separate system/user administration from camera view, playback, export, PTZ, rules and event access.

Do not expose a server’s interactive API reference outside its management boundary or enable permissive cross-origin access to simplify a browser integration. A cloud identity and a local VMS user can have different authorities and lifecycles.

## REST integration contract

- Discover the target build and supported API description at connection/commissioning time.
- Pin serialization types and treat identifiers as opaque.
- Use documented pagination/filtering; do not assume a full collection fits one response.
- Bound downloads, time ranges, media concurrency and response sizes.
- Distinguish current configuration, current operational state, and historical events.
- Reconcile resources, users, event rules and active streams after reconnect or failover.
- Treat media URLs, session tokens and exported footage as secrets/sensitive evidence.

For PTZ, I/O, rules or configuration commands, implement authorization and uncertain-outcome handling. An HTTP success does not demonstrate camera movement, recording, analytics execution or a physical output.

## C++ plug-in boundary

Server plug-ins execute close to media and VMS state. Follow the exact SDK’s ABI, compiler, platform, threading, callback, buffer ownership and lifecycle contract. Validate all metadata and media dimensions, timestamps and lengths. Bound queues and return from callbacks promptly. A crash or leak can affect recording availability, so isolate risky codecs/parsers and provide controlled disable/rollback.

Developer licences are available through the official developer process, but they are not production entitlements. Record expiry, feature limits and the production licensing path.

## Lifecycle and compatibility

Monitor release notes for REST changes, SDK package rebuild requirements and deprecated APIs. Maintain separate compatibility records for Nx Meta reference releases and every OEM distribution.

## Primary sources

- [Nx Meta developer documentation](https://meta.nxvms.com/docs/developers) — official surface catalogue.
- [Developer overview](https://meta.nxvms.com/docs/developers/knowledgebase/264-overview-kb--meta) — programme and architecture entry point.
- [Server HTTP REST API](https://meta.nxvms.com/docs/developers/knowledgebase/193-server-http-rest-api) — documented capability and API-generation boundary.
- [Nx Meta releases](https://meta.nxvms.com/download/other/releases) — dated product and SDK packages.
- [Developer licences](https://meta.nxvms.com/docs/developers/knowledgebase/208-getting-licenses-for-developers) — non-production licence route.
- [Open-source desktop client](https://meta.nxvms.com/docs/developers/knowledgebase/315-what-is-the-open-source-desktop-client) — separate client source boundary.

## Related pages

- [C++ guidance](../../05-development-and-integration/language-guides/cpp.md)
- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
- [Recording, storage, and retention](../../03-systems/video-surveillance/recording-storage-and-retention.md)
