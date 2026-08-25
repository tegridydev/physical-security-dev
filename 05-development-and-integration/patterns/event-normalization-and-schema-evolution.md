---
title: "Event API contracts, normalization, and schema evolution"
summary: "Design transport-independent event contracts with AsyncAPI, CloudEvents context, preserved provenance, explicit physical outcomes, and safe schema evolution."
page_type: development
domains:
  - development
tags:
  - events
  - asyncapi
  - cloudevents
  - schema
  - normalization
scope: global
content_status: maintained
technology_status: not-applicable
verification: V1
runtime_status: not-applicable
safety_level: informational
standards:
  - "AsyncAPI Specification 3.1.0"
  - "CloudEvents Specification 1.0.2"
coverage_limit: "Event API and normalization design guidance; source-native schemas, transport bindings, broker guarantees, mappings, retention, and physical outcome semantics remain integration-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Event API contracts, normalization, and schema evolution

[Home](../../README.md) / [Development](../README.md) / [Patterns](README.md) / Event API contracts

An event contract should make producer intent, transport behavior, payload meaning, compatibility, and evidence boundaries reviewable. Normalization should make events comparable without erasing the native facts needed to interpret or troubleshoot them. Preserve the source record and mapping version, or a protected immutable reference to them.

## Keep four contract layers separate

| Layer | Defines | Does not prove |
|---|---|---|
| Transport/binding | MQTT, AMQP, WebSocket, HTTP webhook, broker/topic/address, security and delivery profile | Payload meaning or physical outcome |
| Operation/channel | Who sends/receives which message and under what routing contract | Broker retention, authorization, or consumer completion unless explicitly profiled |
| Event envelope | Identity, source, type, time, schema/content context and correlation | That the enclosed domain claim is true |
| Domain payload | Alarm, access, video, device, analytic, case, or command-result semantics | Transport delivery or independent sensor confirmation |

Do not make a transport acknowledgement double as a domain acknowledgement. “Webhook returned `2xx`,” “AMQP delivery accepted,” and “MQTT message arrived” do not mean an operator responded, a credential was revoked, or a door reached a requested state.

## AsyncAPI 3.1

AsyncAPI Specification 3.1.0 provides a machine-readable description for asynchronous APIs, including channels, operations, messages, servers, security schemes, correlation identifiers, traits, and protocol bindings. [ASYNCAPI]

Use an AsyncAPI document to make these decisions explicit:

- exact specification version and document identity/version;
- server/environment and protocol binding, without embedding deployable secrets;
- channel/address parameters and their validation/tenant rules;
- send/receive operation direction from the application’s perspective;
- message name, content type, schema format, schema version, examples marked synthetic, and correlation location;
- authentication scheme plus resource/channel authorization requirements;
- protocol-specific delivery, session, acknowledgement, ordering, and size profile;
- operation failure, replay, deprecation, and compatibility policy.

AsyncAPI describes a contract; it does not create a broker, enforce authorization, validate schemas at runtime, or guarantee that a product implements every binding feature. Pin the exact binding version and validate the generated/configured behavior separately. Treat channel templates and server variables as untrusted inputs: constrain them before constructing broker addresses or URLs.

## CloudEvents context

CloudEvents 1.0.2 defines a common event-context format and protocol bindings. Core attributes include `specversion`, `id`, `source`, and `type`; attributes such as `subject`, `time`, `datacontenttype`, and `dataschema` add context. [CLOUDEVENTS]

CloudEvents can improve envelope consistency across transports, but an application profile must still define:

- uniqueness scope and retention for `id`;
- URI governance and tenant binding for `source`;
- stable namespace/version rules for `type`;
- whether `time` means source occurrence, device observation, or producer publication;
- schema resolution, integrity, availability, and version compatibility;
- extension attributes, their type/cardinality, and which producer may assert them;
- binary versus structured content mode and exact transport binding;
- canonicalization/signature behavior if message-level integrity is required.

A syntactically valid CloudEvent is not an authenticated event. Validate transport identity, event source authorization, tenant/site, schema, resource bounds, and domain invariants. The CloudEvents `id` helps deduplicate within a defined source scope; it is not a globally trusted audit identity without that profile.

## Canonical envelope

Include or map the following without inventing facts:

| Concern | Recommended fields or evidence |
|---|---|
| Contract | Canonical event type, event-contract version, payload schema identity/version, content type |
| Identity | Unique event ID with scope, native event ID, producer and original device/controller/source identity |
| Scope | Tenant, organization, site, subsystem, resource namespace |
| Time | Occurrence/observation time, source timezone/offset, receive/ingest time, clock quality and uncertainty |
| Ordering | Native sequence, boot/session/epoch identity, revision, gap/reset indicator |
| Domain | Subject/object/resource, prior and new state, reason, native result/status |
| Interpretation | Severity, alarm priority, analytic confidence, data quality, each as a separate typed field |
| Lineage | Correlation, causation, original event/reference, mapping/parser version, enrichment sources |
| Governance | Sensitivity, privacy purpose, retention class, integrity/evidence reference |

Prefer explicit `unknown`, `not_observed`, or omission rules over fabricated defaults. Make source occurrence, gateway receive, broker publication, consumer ingestion, and case creation separate times.

## Mapping rules

- Map only when semantics match; use vendor/native subtype for non-equivalent concepts.
- Keep alarm priority, analytic confidence, device severity and operational urgency distinct.
- Do not turn missing, unsupported or stale values into false or zero.
- Preserve units, coordinate systems, credential format, timezone and identifier namespace.
- Avoid deriving person identity from a raw credential number unless explicitly authorized and necessary.
- Treat restoration/clear/acknowledgement as separate events or transitions according to source semantics.
- Preserve contradictory observations rather than overwriting them with one “current truth.”
- Make each enrichment attributable and expiring; a lookup result is not part of the original observation.
- Never translate `access granted` into `person entered`, `door contact open` into `forced entry`, or receiver acknowledgement into operator response without the additional required evidence.

## Delivery, ordering, and deduplication

- Assume duplicate and delayed delivery unless the complete end-to-end profile proves otherwise.
- Define ordering scope: producer, device, controller, resource, partition, or tenant. Global order is rarely available.
- Carry a boot/session/epoch marker when counters reset after restart or failover.
- Detect gaps without treating every gap as malicious; record the recovery and evidence impact.
- Scope deduplication by authenticated source and tenant plus event ID; define its retention window.
- Keep replay/test/import traffic in an explicit namespace and prevent it from triggering production automation.
- Bound event age and future-clock tolerance, but quarantine stale safety-relevant events instead of silently dropping them.

## Evolution strategy

- Add optional fields compatibly and define consumer behavior for unknown fields.
- Version breaking semantic changes, not every additive field.
- Keep stable identifiers stable; never recycle meanings under an old type.
- Validate at runtime even when a language has static types.
- Store the decoder/mapping version so historical events remain interpretable.
- Provide dual-read or dual-publish migration only for a bounded window with observability.
- Reserve removed enum values/field identifiers where the schema technology supports it.
- Do not narrow numeric/time ranges, change units, change requiredness, or reinterpret `null` silently.
- Test producer-old/consumer-new and producer-new/consumer-old combinations with synthetic fixtures.
- Publish deprecation date, migration owner, usage evidence, and rollback criteria.

Maintain a compatibility table:

| Change | Usually compatible only when | Common breakage |
|---|---|---|
| Add optional field | Consumers ignore unknown optional fields | Strict deserializers reject it |
| Add enum value | Consumers preserve/handle unknown values | Exhaustive switches fail or map to a false default |
| Widen identifier/time range | Every runtime and store preserves it | JavaScript integer precision, database truncation |
| Change topic/channel | Dual route and deduplication are bounded | Duplicate processing or missing consumers |
| Split/merge event type | Meaning and correlation are versioned | Counts, alarms, and restoration logic change |

## Consumer contract

Consumers must tolerate duplicate and delayed delivery, reject unsupported critical versions, bound input, enforce tenant/resource authorization, and define how unknown events are quarantined. Apply limits to encoded and decoded bytes, decompression ratio, depth, collection size, strings, numbers, schema resolution, concurrent validation, queue count/bytes/age, and processing time.

A consumer must not actuate physical equipment solely from an untrusted or low-confidence normalized event. Route any approved automation through a separate command contract with fresh authorization, prerequisites, idempotency, bounded lifetime, audit, and target-native outcome confirmation.

## Contract assurance

- Lint AsyncAPI and schema documents under pinned tool versions as part of the owning project’s review process.
- Review protocol bindings against the actual broker/client profile rather than relying on generated defaults.
- Use synthetic positive, boundary, malformed, duplicate, delayed, reordered, unknown-version, and cross-tenant fixtures.
- Compare normalized output with protected native input and mapping version.
- Exercise rollback and mixed-version migration in an isolated environment owned by the system operator.
- Capture evidence for schema/binding versions, validation results, mapping approval, and known coverage limits.

## Review checklist

- [ ] Transport/binding, operation/channel, envelope, and domain payload documented separately
- [ ] AsyncAPI version, binding version, security, address variables, messages, and correlation profile pinned
- [ ] CloudEvents attribute semantics, source/ID scope, schema, content mode, and extensions profiled where used
- [ ] Native record/reference, source identity, mapping version, clocks, sequence, and uncertainty preserved
- [ ] Duplicate, delay, reorder, gap, replay, poison-message, and backpressure behavior defined
- [ ] Compatibility matrix covers unknown fields/enums, ranges, null/absence, channels, and mixed versions
- [ ] Tenant/resource authorization and encoded/decoded resource limits enforced
- [ ] Transport acceptance, workflow processing, and physical outcome kept separate
- [ ] Test/replay traffic cannot reach production automation
- [ ] Sensitive identity, access, alarm, video, and location data minimized in messages, logs, and fixtures

## Related pages

- [API and event security](../../06-security-and-assurance/api-and-event-security.md)
- [Logging, time, and evidence integrity](../../06-security-and-assurance/logging-time-and-evidence-integrity.md)
- [Reconnect, backpressure, and queues](reconnect-backpressure-and-queues.md)
- [Observability and diagnostics](observability-and-diagnostics.md)

## Sources

- **ASYNCAPI** — [AsyncAPI Specification 3.1.0][ASYNCAPI], AsyncAPI Initiative.
- **CLOUDEVENTS** — [CloudEvents Specification 1.0.2][CLOUDEVENTS], Cloud Native Computing Foundation.

[ASYNCAPI]: https://www.asyncapi.com/docs/reference/specification/v3.1.0
[CLOUDEVENTS]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
