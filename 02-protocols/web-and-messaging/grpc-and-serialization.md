---
title: "gRPC and serialization contracts"
summary: "Developer reference for gRPC methods/streams, HTTP/2 framing, deadlines, retries, metadata, Protocol Buffers evolution, and safe JSON/CBOR/XML handling."
page_type: protocol
domains: [cross-domain, networking]
tags:
  - grpc
  - protobuf
  - json
  - cbor
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "gRPC over HTTP/2 protocol"
  - "Protocol Buffers proto3 / Editions 2023 and 2024"
  - "RFC 8259: JSON"
  - "RFC 8949 / STD 94: CBOR"
coverage_limit: "RPC and serialization contract guidance only; no schema compilation, generated client/server, serializer, parser, TLS, HTTP/2, retry, stream, or interoperability behavior is validated."
languages: [Protocol Buffers]
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# gRPC and serialization contracts

[Web and messaging protocols](README.md) / gRPC and serialization

gRPC defines typed remote calls and streaming over HTTP/2 in its core wire protocol. Protocol Buffers are its default interface and message definition technology, but gRPC security, lifecycle, deadlines, and domain semantics remain application responsibilities. [GRPC-INTRO] [GRPC-H2]

## RPC shapes

| Shape | Request/response flow | Physical-security fit |
|---|---|---|
| Unary | One request, one response | Read configuration/state; bounded command submission |
| Server streaming | One request, response stream | Event/health feed or search results |
| Client streaming | Request stream, one response | Batched telemetry/upload with explicit commit semantics |
| Bidirectional streaming | Independent streams in both directions | Gateway synchronization; complex backpressure and authorization |

HTTP/2 stream success is not domain completion. gRPC conveys final status in trailers; clients must consume the final status rather than treating receipt of messages or HTTP status `200` alone as success. [GRPC-H2]

## Wire-level essentials

- The canonical gRPC media type begins with `application/grpc`.
- Each message is length-prefixed and can be compressed according to negotiated message encoding.
- HTTP/2 headers carry method path, timeout, content type, accepted encodings, and metadata.
- Response trailers carry `grpc-status` and optional `grpc-message`/status details.
- Binary metadata names use the `-bin` suffix and have specific encoding rules.
- HTTP/2 flow control is necessary but not a complete application backpressure policy.

Cap compressed and decompressed message sizes, metadata, concurrent streams, per-stream buffered messages, stream lifetime, and total work. Do not allocate the declared message length before checking it.

## Service contract example

**Target:** Read-only synthetic door-state API definition.

**Inputs:** No production identifiers or endpoint.

**Side effects:** The example exposes only a read operation.

```proto
syntax = "proto3";

package physical_security_dev.access.v1;

import "google/protobuf/timestamp.proto";

service DoorStateService {
  rpc GetDoorState(GetDoorStateRequest) returns (DoorState);
}

message GetDoorStateRequest {
  string door_id = 1;
}

message DoorState {
  string door_id = 1;
  Position position = 2;
  google.protobuf.Timestamp observed_at = 3;
  uint64 revision = 4;

  enum Position {
    POSITION_UNSPECIFIED = 0;
    POSITION_OPEN = 1;
    POSITION_CLOSED = 2;
    POSITION_UNKNOWN = 3;
  }
}
```

Use an explicit unknown/unspecified enum value. Validate `door_id` by authenticated tenant and authorization; generated types do not enforce object-level access control.

## Deadlines, cancellation, and completion

- Every call should have a deadline derived from user/system budget; avoid infinite streams without renewal.
- Propagate a shorter downstream budget rather than resetting the full timeout at every hop.
- Observe cancellation and stop downstream work; client cancellation does not prove a physical command was not already committed.
- For high-impact mutations, return an operation/command ID and separately report accepted, dispatched, controller-acknowledged, and sensor-confirmed states.
- Bound stream idle time and maximum age, and reauthorize on renewal/reconnect.

## Retry and idempotency

gRPC retry behavior can be controlled by service config and client libraries. A transparent or configured retry can duplicate an application invocation. [GRPC-RETRY]

- Mark/document which methods are safe to retry.
- Use a scoped operation ID and request fingerprint for mutating calls.
- Store deduplication state durably for at least the maximum retry/replay window.
- Apply backoff, jitter, attempt count, retry budget, and deadline.
- Never retry every `UNAVAILABLE` blindly: the server may have performed the action before losing the response.
- Do not use `UNKNOWN` or `INTERNAL` as a generic retry signal.

## Authentication and authorization

- Use TLS with server validation; use mutual TLS for workload/device identity where appropriate.
- Treat metadata as untrusted until the transport/auth interceptor validates it.
- Validate token issuer, audience, signature policy, time, and scope; strip client attempts to set internal identity headers.
- Authorize the exact RPC plus tenant/site/resource/action.
- Reauthorize streams and each high-impact message where entitlement can change.
- Protect reflection, health, channelz, debugging, and admin services; they can expose schema/topology/operational data.
- Keep credentials and personal/access data out of status messages, metadata logs, and traces.

## Protocol Buffers evolution

The official Protocol Buffers documentation covers proto2, proto3, and Editions; Editions 2023 and 2024 are documented in the current support matrix. Pin the compiler/runtime compatibility window and the language edition/syntax in source control. [PROTO3] [PROTO-SUPPORT]

### Safe changes

- Add a new field using a never-used positive field number.
- Make receivers tolerate and preserve unknown fields where the runtime/round-trip path supports it.
- Add enum values only when consumers handle unknown numeric values.
- Add new RPCs without changing existing path semantics.

### Dangerous changes

- Never reuse a deleted field number; reserve deleted numbers and names.
- Do not change a field between semantically incompatible wire/application types merely because some encodings are wire-compatible.
- Avoid changing repeated/singular, oneof membership, signedness, or interpretation without the official compatibility rules and migration.
- Do not assume old clients preserve unknown fields after converting through ProtoJSON or another representation.
- Do not sign/hash ordinary protobuf serialization as though it were canonical: Protocol Buffers explicitly states serialization is not canonical. “Deterministic” output is not a cross-language, cross-version canonical format guarantee. [PROTO-NONCANON]

### Resource and type controls

Bound total bytes, recursion depth, repeated/map entries, string/bytes length, unknown-field volume, `Any` type resolution, and decompressed input. The Protocol Buffers implementation limits document hard and practical limits, but application limits should be much lower. [PROTO-LIMITS]

## JSON

RFC 8259 defines JSON. A safe API profile additionally defines number range/precision, duplicate-member policy, Unicode handling, top-level shape, null/absent semantics, date/time format, canonicalization if signatures need it, and maximum depth/size. [JSON]

- Reject duplicate object names or define one consistent rejection behavior across every component.
- Do not evaluate JSON as code.
- Treat large/exponential numbers carefully; JavaScript and integer runtimes have different exact ranges.
- Normalize identifiers under domain rules, not by silently normalizing signed payload bytes.
- ProtoJSON is a mapping with its own compatibility rules; it is not identical to protobuf binary and does not carry unknown fields in the same way.

## CBOR

RFC 8949 / STD 94 defines CBOR. It supports compact typed values and streaming-friendly encodings, but a deployment must choose a deterministic encoding profile when byte-for-byte signing or hashing is required. Validate preferred/allowed tags, map-key types, duplicate keys, indefinite-length items, nesting, lengths, numeric range, and floating-point edge cases. Valid CBOR is not necessarily deterministic CBOR. [CBOR]

## XML

SOAP and XML Schema are covered separately in [SOAP and XML](soap-and-xml.md). When translating XML, JSON, CBOR, and protobuf, write a loss table for absent/null/empty, number precision, byte strings, map keys, ordering, timestamps, enum unknowns, extensions, and signatures. A generic transcoder can silently change security-relevant meaning.

## Status model

Use canonical gRPC codes consistently:

- `INVALID_ARGUMENT`: request invalid independent of current system state.
- `FAILED_PRECONDITION`: operation cannot run in current state.
- `NOT_FOUND`: resource absent/concealed by policy.
- `ALREADY_EXISTS`: creation conflicts with an existing resource.
- `UNAUTHENTICATED`: valid authentication credentials missing/invalid.
- `PERMISSION_DENIED`: authenticated caller lacks permission.
- `ABORTED`: concurrency/transaction conflict that the application may retry after reread.
- `RESOURCE_EXHAUSTED`: quota/limit reached.
- `UNAVAILABLE`: transient service reachability; mutation outcome may be unknown.
- `DEADLINE_EXCEEDED`: deadline expired; work may still have completed unless cancellation/commit semantics say otherwise.

Return structured, bounded details and a trusted correlation ID; do not reveal stacks or policy internals.

## Review checklist

- [ ] RPC shape, method path, schema syntax/edition, compiler/runtime window pinned
- [ ] TLS/auth metadata and per-resource authorization defined
- [ ] Deadlines, cancellation, stream idle/max age, and downstream budget propagation implemented
- [ ] Retryable methods and operation deduplication explicitly documented
- [ ] Message/metadata/decompression/depth/stream/concurrency limits enforced
- [ ] Field numbers never reused; deletions reserved; enum unknowns handled
- [ ] No ordinary protobuf encoding treated as canonical for signatures/hashes
- [ ] JSON/CBOR duplicate, numeric, depth, tag, and deterministic-encoding rules defined
- [ ] Reflection/health/debug/admin surfaces protected
- [ ] Domain completion distinguished from gRPC transport status

## Environment validation

Pin a supported compiler/runtime matrix and validate generated client/server compatibility, HTTP/2 limits, TLS identity, deadline and cancellation propagation, retry/deduplication, streaming backpressure, malformed serialization, schema evolution, and cross-language interoperability.

## Sources

- **GRPC-INTRO** — [Introduction to gRPC][GRPC-INTRO], gRPC project documentation, accessed 2026-08-25.
- **GRPC-H2** — [gRPC over HTTP/2 Protocol][GRPC-H2], gRPC project protocol specification, accessed 2026-08-25.
- **GRPC-RETRY** — [Retry][GRPC-RETRY], gRPC project documentation, accessed 2026-08-25.
- **GRPC-AUTH** — [Authentication][GRPC-AUTH], gRPC project documentation, accessed 2026-08-25.
- **PROTO3** — [Language Guide (proto 3)][PROTO3], Protocol Buffers documentation, accessed 2026-08-25.
- **PROTO-SUPPORT** — [Version Support][PROTO-SUPPORT], Protocol Buffers documentation, accessed 2026-08-25.
- **PROTO-NONCANON** — [Proto Serialization Is Not Canonical][PROTO-NONCANON], Protocol Buffers documentation, accessed 2026-08-25.
- **PROTO-LIMITS** — [Proto Limits][PROTO-LIMITS], Protocol Buffers documentation, accessed 2026-08-25.
- **JSON** — [RFC 8259: The JavaScript Object Notation Data Interchange Format][JSON], IETF, December 2017.
- **CBOR** — [RFC 8949 / STD 94: Concise Binary Object Representation][CBOR], IETF, December 2020.

[GRPC-INTRO]: https://grpc.io/docs/what-is-grpc/introduction/
[GRPC-H2]: https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md
[GRPC-RETRY]: https://grpc.io/docs/guides/retry/
[GRPC-AUTH]: https://grpc.io/docs/guides/auth/
[PROTO3]: https://protobuf.dev/programming-guides/proto3/
[PROTO-SUPPORT]: https://protobuf.dev/support/version-support/
[PROTO-NONCANON]: https://protobuf.dev/programming-guides/serialization-not-canonical/
[PROTO-LIMITS]: https://protobuf.dev/programming-guides/proto-limits/
[JSON]: https://datatracker.ietf.org/doc/rfc8259/
[CBOR]: https://datatracker.ietf.org/doc/rfc8949/
