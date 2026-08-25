---
title: Milestone MIP SDK and API Gateway
summary: Publicly documented Milestone XProtect integration modes across MIP SDK protocols, .NET components, plug-ins, and API Gateway REST services.
page_type: vendor-api
domains: [video, integration, development]
tags: [milestone, xprotect, mip-sdk, api-gateway, vms-sdk]
scope: global with XProtect product and licence differences
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: Public MIP SDK documentation and release notes reviewed on 2026-08-25; exact XProtect edition/build, API availability, licences, runtime, authentication configuration, media entitlement, and backward compatibility are not asserted.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Milestone MIP SDK and API Gateway

[Vendor APIs](../README.md) / [VMS and cloud video](README.md) / Milestone

The Milestone Integration Platform (MIP) is not one SDK call surface. It defines three major integration modes: remote **protocol integrations**, reusable **.NET components**, and in-process **plug-ins** hosted by XProtect applications. The **API Gateway** provides a current front door for selected REST/protocol services. Select the least coupled mode that supplies the required function.

## Verified surface map

| Surface | Execution boundary | Documented capability | Coupling |
|---|---|---|---|
| MIP protocol APIs | Remote process, potentially any OS/language | Configuration, events/alarms, messaging/control, video/audio/metadata, authentication, status and other service families | Lowest host coupling; each protocol has its own contract |
| MIP .NET components | External .NET application | Higher-level access to XProtect services and object models | Coupled to supported .NET/package/product versions |
| MIP plug-ins | Inside Smart Client, Management Client or Event Server | Native UI, configuration and server workflow extensions | Highest privilege, process and upgrade coupling |
| API Gateway | XProtect gateway/front end | REST entry points and selected services, with centralized identity integration | Product/build/configuration and API availability apply |

The public MIP documentation explicitly describes protocol integrations as usable across operating systems and languages, while components and plug-ins are .NET-centered. Because this page contains no code, `languages: []` records example coverage, not SDK language support.

## Capability families

The official API overview groups integration needs including configuration, events and alarms, messaging and control, video/audio/metadata, authentication, access control, licensing and system status. Availability is not uniform. Build a capability manifest against the installed XProtect product rather than selecting a library simply because a similarly named API appears in the documentation tree.

For media, record the selected service/protocol, stream profile, codec, transport, timestamp basis, playback/live distinction and authorization lifetime. For events, record initial subscription position, filters, renewals, ordering, duplicate/gap behavior and replay/reconciliation support. For control, document target state, preconditions, timeout outcome and audit correlation.

## Authentication and authorization

Milestone documents Basic, Windows and OAuth-related authentication paths in its environment/login guidance; the available method depends on integration mode and system configuration. The API Gateway uses the XProtect identity-provider/OAuth/OIDC architecture for supported services.

- Prefer a non-human workload identity where the supported flow allows.
- Use HTTPS and validate the server identity; do not disable `secureOnly` or certificate checks to make an example connect.
- Scope privileges by site/device and capability: configuration, live, playback, export, audio, PTZ and administration are different rights.
- Keep client secrets and refresh/access tokens outside source, plug-in packages and logs.
- Re-authorize and reconcile after token expiry, management-server failover or service restart.

Never infer that authentication to one MIP service grants access to every API behind the gateway.

## Choosing an integration mode

Use a remote protocol/API when service isolation, language choice and independent deployment matter. Use a component when the supported .NET abstraction removes meaningful protocol complexity. Use a plug-in only when the workflow must be native to an XProtect client/server and the operational owner accepts host-process risk.

For plug-ins:

- verify signing/distribution and supported host locations;
- avoid blocking host UI or Event Server threads;
- bound memory, media and event queues;
- use the host’s supported configuration and credential services;
- handle disable/uninstall and partial upgrade;
- test compatibility for every XProtect release the deployment supports.

## Release and licence contract

The public documentation tree showed **MIP SDK 2026 R1** as a current documentation/release line on 2026-08-25, alongside earlier release trees. This is a dated documentation observation, not a claim that all customers should or can deploy it. The target XProtect edition, installed product build, device licence, integration licence and enabled gateway services determine availability.

Do not assume forward or backward binary compatibility. Read the exact MIP and XProtect release notes, breaking changes, runtime requirements and known limitations. Maintain an upgrade matrix and rollback plan.

## Primary sources

- [MIP VMS API documentation](https://doc.developer.milestonesys.com/mipvmsapi/) — current public documentation root.
- [MIP SDK architecture](https://doc.developer.milestonesys.com/mipsdk/content_4.html) and [integration modes](https://doc.developer.milestonesys.com/mipvmsapi/content/integration-modes/) — protocol/component/plug-in boundaries.
- [MIP API overview](https://doc.developer.milestonesys.com/mipvmsapi/api-overview/) — capability families.
- [Protocol APIs and API Gateway](https://doc.developer.milestonesys.com/mipsdk/reference/protocols/index.html) — official protocol catalogue.
- [Environment login and authentication](https://doc.developer.milestonesys.com/mipsdk/gettingstarted/intro_environments_login.html) — identity modes and secure connection guidance.
- [MIP SDK 2026 R1 introduction](https://doc.developer.milestonesys.com/mipsdk/gettingstarted/mip2026R1_intro.html) and [release tree](https://doc.developer.milestonesys.com/mipsdk/tree_home.html) — dated lifecycle evidence.

## Related pages

- [VMS, NVR, and VSaaS](../../03-systems/video-surveillance/vms-nvr-and-vsaas.md)
- [C# integration guidance](../../05-development-and-integration/language-guides/csharp.md)
- [Secrets, certificates, and configuration](../../05-development-and-integration/patterns/secrets-certificates-and-configuration.md)
