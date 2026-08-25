---
title: "C# protocol development"
summary: "C# guidance for enterprise VMS/PACS SDKs, services, HTTP clients, event streams, and native resource boundaries."
page_type: development
domains:
  - development
tags:
  - csharp
  - dotnet
coverage_limit: "C# and .NET integration guidance; exact patch, package, OS, vendor SDK, protocol, and product compatibility is environment-specific."
languages:
  - "C#"
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - ".NET 10 LTS"
  - "C# 14"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# C# protocol development

[Home](../../README.md) / [Development](../README.md) / [Language guides](README.md) / C#

C# is the primary reference language for enterprise VMS/PACS SDKs and Windows-hosted integrations. The reviewed baseline is .NET 10 LTS with C# 14; vendor SDK requirements may mandate another supported target [DOTNET].

## Baseline

- Enable nullable reference types, analyzer warnings and checked handling where numeric overflow matters.
- Make public protocol/domain models immutable where practical.
- Validate deserialized JSON/XML and SDK objects at runtime; annotations do not enforce wire input.
- Reuse HttpClient through an appropriate handler/factory lifecycle; do not create a new client for each request.
- Propagate CancellationToken through all I/O and waiting paths.
- Bound response bodies, streams, queues and parallel device work.

## TLS and authentication

Use platform hostname and chain validation with an explicitly managed trust store. Never publish callbacks that return true for every certificate. Separate OAuth/token acquisition, Windows/AD authentication, client certificates and vendor SDK session credentials; redact them from diagnostic context.

## Async and events

Avoid sync-over-async and unobserved fire-and-forget tasks. Unsubscribe event handlers and dispose subscriptions deterministically. Serialize state changes per device/resource when ordering matters; bound channels and define full behavior.

## Native and media SDKs

Wrap native handles in SafeHandle or vendor-recommended deterministic lifetime constructs. Control callback lifetime, thread affinity and buffer ownership. Copy or pin media buffers only under documented ownership rules, and avoid logging frame content.

## Services and plugins

Use unique service identity, least privileges and explicit shutdown. Keep plugin boundaries distrustful: version-check assemblies/packages, isolate configuration, and prevent a vendor callback from directly authorizing a physical command.

## Sources

- **DOTNET** — [.NET downloads and support status][DOTNET], .NET 10 LTS, accessed 2026-08-25.
- **CSHARP** — [C# language documentation][CSHARP], accessed 2026-08-25.

[DOTNET]: https://dotnet.microsoft.com/en-us/download/dotnet
[CSHARP]: https://learn.microsoft.com/dotnet/csharp/

## Related pages

- [Vendor APIs](../../04-vendor-apis/README.md)
- [Timestamp normalization](../examples/timestamp-normalization-csharp.md)
