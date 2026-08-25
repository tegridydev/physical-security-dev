---
title: "Development and integration"
summary: "Secure implementation patterns, language guidance, and reference examples for physical-security protocols."
page_type: index
domains:
  - development
  - integration
tags:
  - development
  - integration
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "NIST SP 800-218 Version 1.1"
coverage_limit: "Language baselines and reference examples are implementation guidance; product, SDK, deployment, and interoperability behavior depends on the selected environment."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Development and integration

[Home](../README.md) / Development and integration

This section is the bridge between protocol specifications and maintainable integration software. It emphasizes explicit state, versioning, secure identity, bounded resources, deterministic failure, observability, and safe physical consequences.

Reference examples use synthetic inputs and documentation domains, and exclude physical actuation. Evaluate them only in an isolated, authorized environment with pinned versions, bounded resources, and recorded evidence.

## Contents

- [Integration patterns](patterns/README.md)
- [Language guides](language-guides/README.md)
- [Reference examples](examples/README.md)
- [Security and assurance](../06-security-and-assurance/README.md)
- [Defensive labs](../08-defensive-labs/README.md)

## Design priorities

1. Model roles, identity, authorization and state transitions before endpoints or libraries.
2. Treat every byte, field, callback and SDK object as untrusted until validated.
3. Make timeouts, retries, idempotency, ordering, replay and reconciliation explicit.
4. Bound memory, queues, connections, payloads, parsing work and log output.
5. Separate observation, configuration, administration and physical actuation capabilities.
6. Preserve correlation from external request through normalized event and device outcome.
7. Keep product/version quirks in adapters; keep the domain model vendor-neutral.

## Language selection

| Language | Primary reference use | Reviewed baseline on 2026-08-25 |
|---|---|---|
| Python | Offline fixtures, protocol exploration, parsers and small clients | Python 3.14.7 |
| TypeScript | Browser/Node HTTP, WebSocket, MQTT and WebRTC integrations | TypeScript 7; Node.js 24 LTS |
| C# | Enterprise VMS/PACS SDKs and Windows services | .NET 10 LTS; C# 14 |
| Go | Concurrent gateways, collectors and network services | Go 1.27 |
| C | Embedded, serial and constrained binary framing | C17 baseline unless SDK requires another edition |
| C++ | Native media/device SDKs and RAII-based integrations | C++23 baseline unless SDK requires another edition |

Pin the exact patch and dependency versions in each integration project; the table is a documentation review baseline, not a compatibility guarantee. Official release sources are maintained in each language page.

## Sources

- **NIST-SSDF** — [NIST SP 800-218 Version 1.1][NIST-SSDF], accessed 2026-08-25.

[NIST-SSDF]: https://csrc.nist.gov/pubs/sp/800/218/final

## Related pages

- [Protocol catalogue](../02-protocols/README.md)
- [System architectures](../03-systems/README.md)
- [Code-example index](../09-reference/code-example-index.md)
