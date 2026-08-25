---
title: "Observability and diagnostics"
summary: "Correlate transport, protocol, device, application, and physical outcomes using bounded telemetry, OpenTelemetry, OTLP, and W3C Trace Context without leaking sensitive data."
page_type: development
domains:
  - development
tags:
  - observability
  - diagnostics
  - telemetry
  - opentelemetry
  - otlp
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: informational
standards:
  - "OpenTelemetry Specification 1.60.0"
  - "OpenTelemetry Protocol Specification 1.11.0"
  - "W3C Trace Context"
coverage_limit: "Observability architecture and data-governance guidance; exact semantic conventions, collector topology, sampling, storage, product telemetry, and evidential requirements remain deployment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Observability and diagnostics

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Observability

An integration should answer: which source and version produced the data, which identity was used, what was requested, what was authorized, what reached the downstream system, what result was observed, and where uncertainty remains. Telemetry supports diagnosis and service management; it does not automatically become a complete security audit trail or admissible evidence.

## Current interoperability baseline

This page uses [OpenTelemetry Specification 1.60.0][OTEL] and [OTLP Specification 1.11.0][OTLP] as the dated project snapshot. OpenTelemetry evolves frequently, and its specification, protocol, API/SDK, semantic conventions, collector, and language implementations have independent versions and stability labels. Pin every component actually relied upon.

W3C Trace Context defines the interoperable `traceparent` and `tracestate` HTTP fields. It propagates correlation context, not authenticated identity, authorization, tenant membership, or data-integrity proof. [TRACE-CONTEXT]

| Layer | Useful standard concept | Deployment decision |
|---|---|---|
| Resource | Entity producing telemetry, described by resource attributes | Stable service/device/gateway identity and tenant-safe attribute policy |
| Instrumentation scope | Library/component that produced a signal | Name/version governance and collision handling |
| Trace/span | Causal and timing relationship | Sampling, parent trust, links, sensitive attributes, and status policy |
| Metric | Aggregated measurement | Instrument type, unit, temporality, aggregation, and cardinality budget |
| Log record | Timestamped structured record with optional trace correlation | Severity mapping, body/attribute schema, redaction, and retention |
| OTLP | Telemetry export protocol/data model | gRPC or HTTP transport, endpoint identity, authentication, compression, queue, and retry profile |

OpenTelemetry compatibility does not mean two products use the same semantic conventions or preserve the same fields. Document translation and loss explicitly.

## Telemetry model

### Logs

Use structured event name/version, severity, observed timestamp plus source timestamp and clock context, service/device/site identifiers, correlation/causation, operation, layer-specific outcome, error class, retry count, and configuration/build/mapping version. Redact secrets, credentials, biometric/media data, personal/location data, and sensitive topology.

Log bodies and attributes need explicit byte, depth, collection, and cardinality limits. A structured log is still untrusted input when a device, connector, or upstream service can set its fields. Prevent newline/control-character injection in text renderings and keep display strings separate from trusted identity fields.

### Metrics

Track connection/authentication success, latency, timeouts, retries, reconnects, input rejection by reason, queue count/bytes/age, dropped/coalesced items, subscription lease, event gaps/duplicates, clock drift, certificate expiry, storage/capacity, and downstream state freshness. Avoid unbounded labels such as raw device, event, credential, plate, camera, user, URL, exception, or correlation identifiers.

Define a cardinality budget per instrument and aggregation point. A backend limit that drops new series can conceal precisely the failing tenant or device fleet. Preserve a bounded diagnostic path without turning identifiers into global metric labels.

### Traces

Trace cross-service flows only when sampling and data policy protect sensitive commands, token headers, URLs, query strings, images, card values, plate data, and personal identifiers. Link to a separately protected audit record rather than duplicating full content.

Use spans to distinguish stages such as request validation, authorization decision, broker publication, adapter processing, downstream dispatch, target acknowledgement, and observed physical state. Do not collapse all stages into one `OK` status. A span ending successfully means that instrumented operation ended according to its code path; it does not prove a door, gate, alarm, camera, or notification reached the intended real-world state.

### Trace-context handling

- Parse `traceparent` strictly and reject malformed values according to the receiving profile.
- Start a new trace or link to untrusted incoming context at trust boundaries when accepting it as a parent could mislead investigation.
- Never use trace/span IDs as authentication, authorization, idempotency, or audit-event IDs.
- Bound and filter `tracestate`; downstream vendors can otherwise receive sensitive tenancy/routing context.
- Regenerate response correlation identifiers under local policy rather than reflecting arbitrary attacker-controlled strings into trusted logs.
- Preserve causation links for asynchronous work; ordinary parent/child timing does not always model queues, fan-out, retries, or replay.

## OpenTelemetry data design

### Resources and attributes

Use stable low-cardinality resource attributes for service name/namespace/instance where appropriate, deployment environment, software version, and a privacy-reviewed device/gateway classification. Do not put a raw bearer token, credential number, person name, camera URL, or precise protected location into a Resource: it is copied to many records and backends.

Semantic-convention attribute names and stability can change independently of the core specification. Pin the convention version, prefer standard attributes where semantics match, namespace custom attributes, and never reuse an existing attribute with a different physical-security meaning.

### Events and links

Span events are useful for bounded milestones; span links model causal relationships that are not a single parent/child chain. Neither replaces a durable domain event. Keep source-native event ID, schema/mapping version, and evidence reference in the domain record, and propagate only minimal correlation into telemetry.

### Status and errors

Record machine-readable error class plus the layer that failed: DNS/connect, TLS/trust, authentication, authorization, protocol, schema, unsupported capability, stale/uncertain state, rate/capacity, downstream rejection, timeout, or internal fault. Avoid high-cardinality exception messages as metric attributes. Scrub stack traces and attach them only to access-controlled diagnostic storage.

## OTLP export and collector boundaries

OTLP defines telemetry request/response and partial-success concepts over its supported transports. A successful export establishes collector acceptance under that contract, not durable storage, alert evaluation, case creation, or evidence retention.

- Validate exporter and collector endpoint identity; use workload authentication and least privilege.
- Separate tenants/environments before a shared collector can mix or route records incorrectly.
- Bound request and decompressed bytes, record/attribute counts, string lengths, concurrent exports, queue count/bytes/age, and retry lifetime.
- Treat partial success, rejection counts, timeouts, and uncertain exports as visible outcomes.
- Apply backoff, jitter, retry budgets, and bounded disk queues; never let telemetry exhaust resources needed for the controlled system.
- Encrypt local queues when they contain sensitive operations or identity/location information, and define secure expiry.
- Govern collector processors as code/configuration: redaction, sampling, enrichment, filtering, routing, and attribute transformation can change evidence meaning.
- Do not expose unauthenticated collector receivers or diagnostic interfaces to device networks.

Use separate pipelines or independently retained records when audit/evidence requirements exceed ordinary observability sampling and retention.

## Sampling and loss

Head and tail sampling affect what can be reconstructed. Tail sampling requires buffering and can concentrate sensitive data. Define which security/audit events must never depend solely on trace sampling.

Telemetry can be lost through SDK limits, exporter queues, collector rejection, network interruption, backend ingestion limits, sampling, retention, or clock disorder. Monitor the monitoring path with independent health signals and synthetic canaries that contain no sensitive production data.

Record configuration revision and counters for dropped spans/logs/metric points, rejected OTLP items, queue overflow, sampling decisions, and backend throttling. “No alert” is not evidence that no event occurred when pipeline completeness is unknown.

## Error taxonomy

Keep transport, trust/authentication, authorization, protocol/version, validation, unsupported capability, stale state, downstream rejection, timeout/uncertain outcome, resource exhaustion and internal fault distinct. Operators need a safe next action; developers need structured context.

Map errors to stable classes while retaining a protected source-native code/reference. Do not retry based on a human-readable message substring. A timeout after a mutating request is an uncertain outcome, not proof of failure.

## Support bundles

Generate from an allowlist, redact before packaging, encrypt for the intended recipient, expire access, and log collection/export. Include versions, effective redacted configuration, health and relevant bounded logs; exclude private keys, reusable tokens, raw credentials and unrelated surveillance data.

Support bundles should state collection window, source clock quality, collector/tool version, redaction policy/version, missing sources, truncation, and integrity manifest. Review every new diagnostic artifact before adding it to the allowlist.

## Review checklist

- [ ] OpenTelemetry, OTLP, semantic-convention, collector, and language-component versions pinned
- [ ] Resources, scopes, logs, metrics, traces, domain events, audit records, and evidence have distinct purposes
- [ ] Encoded/decoded size, attribute, cardinality, queue, concurrency, retry, and retention limits enforced
- [ ] Trace context treated as untrusted correlation, never identity, authorization, idempotency, or audit proof
- [ ] Sensitive commands, tokens, credentials, people, location, video, biometrics, and topology redacted/minimized
- [ ] OTLP authentication, tenant isolation, partial success, uncertain export, and backpressure handled
- [ ] Sampling and every telemetry-loss point documented and independently monitored
- [ ] Transport, authorization, downstream acknowledgement, and observed physical outcome remain separate
- [ ] Audit/evidence records remain available when ordinary telemetry is sampled or transformed
- [ ] Support bundles are allowlisted, bounded, redacted, encrypted, expiring, and audited

## Related pages

- [Logging, time, and evidence integrity](../../06-security-and-assurance/logging-time-and-evidence-integrity.md)
- [Reconnect, backpressure, and queues](reconnect-backpressure-and-queues.md)
- [Monitoring and health](../../07-operations-and-lifecycle/monitoring-and-health.md)
- [Event API contracts, normalization, and schema evolution](event-normalization-and-schema-evolution.md)

## Sources

- **OTEL** — [OpenTelemetry Specification 1.60.0][OTEL], OpenTelemetry project.
- **OTLP** — [OpenTelemetry Protocol Specification 1.11.0][OTLP], OpenTelemetry project.
- **TRACE-CONTEXT** — [W3C Trace Context][TRACE-CONTEXT], W3C Recommendation.

[OTEL]: https://opentelemetry.io/docs/specs/otel/
[OTLP]: https://opentelemetry.io/docs/specs/otlp/
[TRACE-CONTEXT]: https://www.w3.org/TR/trace-context/
