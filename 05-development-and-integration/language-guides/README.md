---
title: "Language guides"
summary: "Language-specific secure implementation guidance without duplicating every protocol example."
page_type: index
domains:
  - development
tags:
  - languages
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: "Language guidance establishes secure implementation baselines; exact patch, library, SDK, product, and platform compatibility is environment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Language guides

[Home](../../README.md) / [Development and integration](../README.md) / Language guides

Each protocol example uses the language whose ecosystem or safety model teaches something useful. The same request is not translated into six languages merely for parity.

| Guide | Best fit |
|---|---|
| [Python](python.md) | Offline fixtures, exploration, parsers and compact clients |
| [TypeScript](typescript.md) | Browser/Node APIs, WebSocket, MQTT and WebRTC |
| [C#](csharp.md) | Enterprise VMS/PACS SDKs and Windows services |
| [Go](go.md) | Concurrent gateways, collectors and network services |
| [C](c.md) | Embedded, serial and bounded binary protocol implementations |
| [C++](cpp.md) | Native media/device SDKs and ownership-safe integrations |

## Shared rules

- Declare exact runtime/compiler, dependencies, protocol/API and product/firmware scope.
- Validate peer certificates and hostnames; never publish trust-all examples.
- Set deadlines, cancellation, input and resource bounds.
- Validate runtime data even in statically typed languages.
- Redact secrets and sensitive physical/security data.
- Default examples to offline, read-only or mock behavior.
- Classify material as conceptual, protocol fragment, or reference implementation; attach runtime-validation status only when reproducible environment evidence exists.

## Related pages

- [Reference examples](../examples/README.md)
- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
