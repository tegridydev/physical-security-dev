---
title: "Reference examples"
summary: "Safe implementation references using synthetic data, bounded behavior, and documentation-only targets."
page_type: index
domains:
  - development
tags:
  - examples
  - code
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: []
coverage_limit: "Reference examples use synthetic inputs and documentation domains; integration owners must profile versions, dependencies, limits, endpoints, and authorization for their environment."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Reference examples

[Home](../../README.md) / [Development and integration](../README.md) / Examples

Use these examples with synthetic data, loopback, or an isolated authorized environment. Their read-only and offline boundaries are part of the examples and must not be widened to physical actuation.

## Status vocabulary

| Status | Meaning |
|---|---|
| Conceptual | Pseudocode or incomplete explanatory fragment |
| Protocol-fragment | Wire/schema/configuration fragment, not a complete program |
| Reference implementation | Complete example with stated inputs, side effects, bounds, and expected behavior |
| `partially-runtime-validated` | Recorded evidence covers selected cases in an identified environment |
| `runtime-validated` | Recorded evidence covers the declared cases, versions, environment, observations, and limitations |

## Examples

| Page | Language | Purpose | Status |
|---|---|---|---|
| [Offline trace parsing](offline-trace-parsing-python.md) | Python | Validate a synthetic JSON-lines event trace | Reference implementation |
| [Safe HTTPS JSON read](safe-https-json-python.md) | Python | Bounded TLS-validated read-only request | Reference implementation |
| [Offline RTSP/SDP inspection](rtsp-sdp-inspection-python.md) | Python | Parse synthetic RTSP and SDP text | Reference implementation |
| [mTLS health client](mtls-client-go.md) | Go | Read-only mutual-TLS health request | Reference implementation |
| [WebSocket event client](websocket-events-typescript.md) | TypeScript | Validate and bound synthetic WSS events | Reference implementation |
| [Timestamp normalization](timestamp-normalization-csharp.md) | C# | Preserve occurrence and ingestion time | Reference implementation |
| [Binary frame and CRC](binary-frame-crc-c.md) | C | Bounded synthetic frame parsing | Reference implementation |
| [ONVIF SOAP request anatomy](onvif-soap-request.md) | XML | Explain namespaces and request envelope | Protocol-fragment |
| [MQTT event contract](mqtt-event-contract.md) | JSON/TypeScript | Topic, identity, validation and QoS decisions | Protocol-fragment |
| [Modbus read response](modbus-read-response.md) | Hex | Safely interpret a synthetic read response | Protocol-fragment |

## Universal requirements

- Documentation domains and synthetic identifiers only.
- No real credentials, media, card values or customer data.
- No certificate bypass or plaintext fallback.
- Bounded time, bytes, retries, queues and logs.
- Read-only or offline behavior; physical actuation is excluded.
- Environment-validation evidence identifies exact versions, cases, observations, limitations, and the responsible integration owner.

## Related pages

- [Language guides](../language-guides/README.md)
- [Defensive labs](../../08-defensive-labs/README.md)
