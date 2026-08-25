---
title: "Code example index"
summary: "A safety-oriented index of every maintained code or protocol example in the knowledge base."
page_type: index
domains:
  - development
  - integration
tags:
  - code-examples
  - implementation-reference
  - safe-examples
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: "Catalogue and intended-behavior summary only; each example remains bounded to its stated synthetic or documentation target and is not product, performance, interoperability, or production assurance."
languages:
  - C
  - "C#"
  - Go
  - Python
  - TypeScript
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Code example index

[Home](../README.md) / [Reference](README.md) / Code example index

The canonical example vocabulary and handling rules are in [Reference examples](../05-development-and-integration/examples/README.md). Examples use synthetic inputs, reserved documentation names, bounded parsing, and read-only or offline behavior. Adaptations need an environment-specific review and evidence record.

## Maintained examples

| Example | Language/form | Purpose | Default boundary |
|---|---|---|---|
| [Bounded binary frame and CRC parsing](../05-development-and-integration/examples/binary-frame-crc-c.md) | C17 | Validate length, endianness, integrity, and bounds over an embedded frame | Synthetic bytes and standard output |
| [Synthetic Modbus/TCP read-response interpretation](../05-development-and-integration/examples/modbus-read-response.md) | Protocol fragment | Interpret an annotated MBAP/PDU read response | Offline data; no request or address |
| [MQTT event contract](../05-development-and-integration/examples/mqtt-event-contract.md) | JSON/topic and TypeScript fragment | Define topic, identity, payload-validation, and QoS decisions | Synthetic topic and payload |
| [Mutual-TLS health client](../05-development-and-integration/examples/mtls-client-go.md) | Go | Bound a read-only HTTPS health request using mTLS | Reserved target; read-only GET |
| [Offline trace parsing](../05-development-and-integration/examples/offline-trace-parsing-python.md) | Python | Validate bounded JSON-lines event records | Embedded synthetic records and standard output |
| [ONVIF SOAP request anatomy](../05-development-and-integration/examples/onvif-soap-request.md) | XML/SOAP fragment | Explain namespaces and request-envelope responsibilities | Synthetic envelope; no endpoint or credentials |
| [Offline RTSP and SDP inspection](../05-development-and-integration/examples/rtsp-sdp-inspection-python.md) | Python | Parse bounded RTSP response and SDP text | Embedded synthetic text and standard output |
| [Safe HTTPS JSON read](../05-development-and-integration/examples/safe-https-json-python.md) | Python | Bound a certificate-validating, read-only JSON request | Reserved target; read-only GET |
| [Timestamp normalization](../05-development-and-integration/examples/timestamp-normalization-csharp.md) | C# | Preserve source and ingestion time, offset, and sequence | Embedded synthetic timestamps and standard output |
| [WebSocket event client](../05-development-and-integration/examples/websocket-events-typescript.md) | TypeScript | Validate and bound WSS events | Reserved target; read-only synthetic subscription |

## Example forms

| Label | Meaning |
|---|---|
| Protocol fragment | Wire/schema/configuration content; intentionally not a complete program |
| Reference implementation | Complete example for the stated synthetic/documentation target, with explicit inputs, bounds, expected behavior, and side effects |
| Environment-validated | A separate evidence record identifies the exact versions, target, configuration, cases, results, limitations, and responsible integration owner |

Do not convert “no network in the default fixture” into “cannot access the network.” Review the complete source, build configuration, dependencies, environment, and local modifications before adapting an example.

## Language guides

| Language | Guide | Example coverage here |
|---|---|---|
| C | [C guide](../05-development-and-integration/language-guides/c.md) | Bounded binary frame/CRC parsing |
| C++ | [C++ guide](../05-development-and-integration/language-guides/cpp.md) | No dedicated maintained example |
| C# | [C# guide](../05-development-and-integration/language-guides/csharp.md) | Timestamp normalization |
| Go | [Go guide](../05-development-and-integration/language-guides/go.md) | Mutual-TLS health client |
| Python | [Python guide](../05-development-and-integration/language-guides/python.md) | Offline trace, RTSP/SDP inspection, HTTPS JSON read |
| TypeScript | [TypeScript guide](../05-development-and-integration/language-guides/typescript.md) | WebSocket event client; illustrative MQTT validation fragment |

Language/runtime versions on individual pages are mutable evidence. Recheck their official support status before adoption; an index row does not extend a runtime's support lifetime.

## Adaptation checklist

Before adapting an example to an environment:

- [ ] Exact page, revision, target language/runtime, dependencies, and expected behavior reviewed
- [ ] Entire source checked for network, filesystem, process, environment, credential, logging, and physical-control effects
- [ ] Reserved/synthetic identifiers remain synthetic; no production address, account, credential, media, or event substituted
- [ ] Environment is isolated, authorized, non-production, and unable to dispatch or actuate
- [ ] Read-only identity has no write/admin/door/relay/PTZ/firmware capability
- [ ] TLS trust, secrets injection, timeouts, response/message bounds, redirect/proxy, and logging policy reviewed
- [ ] Expected output and negative/boundary cases written before execution
- [ ] Stop/cleanup/rollback and evidence-capture plan exists
- [ ] Evidence records compiler/runtime versions, commands, hashes/configuration, inputs, observations, failures, limitations, owner, and date

Apply the [integration readiness checklist](integration-readiness-checklist.md) to any product-facing adaptation and the [safety impact checklist](safety-impact-checklist.md) to anything that could configure, interrupt, or actuate.

## Index maintenance

When adding an example:

1. add canonical front matter including `runtime_status` and `coverage_limit`;
2. label its status, target, inputs, side effects, expected result, and evidence boundary in the page body;
3. use synthetic/reserved data and exclude production-ready secrets/targets;
4. link its source standards and related defensive patterns;
5. add exactly one row here;
6. link a scoped environment-validation record where one supports a published claim.
