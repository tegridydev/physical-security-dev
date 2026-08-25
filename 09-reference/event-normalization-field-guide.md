---
title: "Event normalization field guide"
summary: "A loss-aware canonical event contract for identity, chronology, ordering, quality, evidence, privacy, and schema evolution across physical-security systems."
page_type: reference
domains:
  - integration
  - cross-domain
tags:
  - events
  - normalization
  - schemas
  - cloudevents
  - time
  - deduplication
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards:
  - "CloudEvents 1.0.2"
  - "RFC 8259"
  - "RFC 3339"
  - "RFC 9557"
  - "RFC 8785"
coverage_limit: "Vendor-neutral envelope and mapping rules only; source code tables, alarm meanings, severity policy, identity namespaces, privacy classification, delivery guarantees, and command behavior remain source- and deployment-specific."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Event normalization field guide

[Home](../README.md) / [Reference](README.md) / Event normalization field guide

Normalization should make different sources queryable without erasing their differences. Preserve source meaning, raw evidence or a protected reference, mapping version, clock quality, and uncertainty. Unknown is a valid result; invented certainty is not.

> **Safety boundary:** normalization is observation. It must never itself unlock, lock down, dispatch, silence, reset, acknowledge upstream, change a credential, move PTZ, write BMS/OT state, or drive a relay. A separately authorized command service may consume normalized evidence only through the [safety impact checklist](safety-impact-checklist.md).

## Four records, not one

| Record | Meaning | Mutability |
|---|---|---|
| Event | A source reports that something occurred or was observed | Immutable after acceptance; corrections are new records |
| State snapshot | Best-known value at a resource for an effective interval | Superseded/reconciled; retain provenance and quality |
| Command | A principal requests an intended change | Immutable request plus separate lifecycle records |
| Delivery/processing record | A broker/adapter/consumer handled an event | One event may have many attempts, deliveries, acknowledgements, and failures |

See [events, state, commands, and time](../01-foundations/events-state-commands-and-time.md) and [event normalization and schema evolution](../05-development-and-integration/patterns/event-normalization-and-schema-evolution.md).

## Minimum normalized envelope

### Event identity and provenance

| Field | Type/shape | Rule |
|---|---|---|
| `event_id` | string | Stable identity of the distinct event in the normalizer's namespace; never reuse |
| `source_event_id` | string or absent | Original event/message ID exactly as supplied; retain leading zeroes and case rules |
| `source_system` | governed string | Source family/tenant, not a mutable display name |
| `source_instance` | governed string | Exact server/controller/receiver/gateway instance identity |
| `source_session` | string or absent | Boot/session/connection epoch needed to interpret sequence reuse |
| `source_protocol` | object | Protocol/API name, exact edition/profile, transport/binding where material |
| `source_product` | object/ref | Manufacturer/product/firmware evidence reference; never inferred solely from payload text |
| `adapter_id` | string | Normalizing component and release/build identity |
| `mapping_version` | string | Immutable mapping/code-table version that produced the normalized fields |
| `ingest_route` | string/ref | Tenant/site pipeline or connector path without exposing credentials/topology unnecessarily |

If adopting CloudEvents, its required `source` plus `id` identifies a distinct event under the producer's contract. Do not overwrite the source's ID with a broker delivery ID. [CLOUDEVENTS]

### Classification and schema

| Field | Type/shape | Rule |
|---|---|---|
| `event_type` | versioned string | Stable semantic class such as `reader.connectivity.changed.v1`; not a UI sentence |
| `schema_version` | integer/string | Version of the normalized `data` contract; define compatibility policy |
| `data_schema` | URI/ref | Immutable schema reference when available; access to schema must not be required to safely bound input |
| `source_type` | string/int | Original event type/code exactly preserved |
| `source_qualifier` | string/int/absent | Original new/restore/active/inactive or protocol qualifier |
| `source_extension` | object/ref/absent | Namespaced vendor fields retained without presenting them as standard semantics |
| `category` | enum | Governed broad class: access, intrusion, video, device-health, system, audit, etc. |
| `severity_source` | string/int/absent | Original publisher severity/priority, never overwritten by incident policy |
| `priority_normalized` | enum/int/absent | Organization routing priority with documented mapping and version |
| `mapping_quality` | enum | `exact`, `partial`, `ambiguous`, `unknown`, or another governed set |

Do not map an unknown alarm code to the “closest” known emergency meaning. Preserve it as unknown, route it for review under source/site policy, and keep the raw code.

### Resource, location, and identity references

| Field | Type/shape | Rule |
|---|---|---|
| `tenant_ref` | opaque governed ref | Required for multi-tenant isolation; never trust payload-supplied tenant alone |
| `site_ref` | opaque governed ref | Stable site namespace, separately bound to source configuration |
| `zone_ref` | opaque ref/absent | Security/physical zone, not a free-text location |
| `resource.kind` | enum | Door, reader, camera, panel, receiver, input, output, point, service, etc. |
| `resource.id` | string | Stable ID in an explicit namespace; do not substitute display name/IP/MAC/token |
| `resource.source_id` | string/absent | Original protocol/product resource identifier |
| `resource.parent_ref` | ref/absent | Controller/device/system relationship under an inventory version |
| `location_text` | display string/absent | Sanitized untrusted label; never used for routing/authorization |
| `actor_ref` | privacy-preserving ref/absent | Governed identity reference only where necessary and lawful |
| `credential_ref` | privacy-preserving ref/absent | Credential record reference; never raw key, PIN, biometric, wallet token, or unnecessary number |

Keep subject ID, credential ID, facility/card number, card UID, certificate/key identity, device ID, reader ID, and door ID separate. See [credential technology comparison](credential-technology-comparison.md).

### Event semantics

| Field | Type/shape | Rule |
|---|---|---|
| `condition` | versioned enum/object | Semantic condition observed, qualified by source mapping |
| `state` | typed value/absent | State after transition only when source semantics support it |
| `previous_state` | typed value/absent | Source-supplied or reconciled value, with provenance; never guessed |
| `transition` | enum/absent | `entered`, `exited`, `changed`, `asserted`, `restored`, etc., under domain contract |
| `value` | typed value/absent | Preserve units, scale, precision, and quality; avoid locale conversion |
| `reason_code` | governed value/absent | Source or decision reason with namespace/version |
| `message` | sanitized display text/absent | Not an identifier, policy input, or command; control characters and sensitive data constrained |
| `attributes` | bounded object | Only schema-governed extension fields; unknown raw data stays namespaced/referenced |

Silence is not restore. A transport reconnect is not resource recovery. A door-contact state is not lock state. An unlock command accepted is not a door opened or safely resecured.

### Chronology and ordering

| Field | Meaning |
|---|---|
| `occurred_at` | Source claim for when the underlying occurrence happened |
| `observed_at` | Time a device/controller directly observed the condition, if distinct |
| `source_emitted_at` | Time the source says it created/transmitted the event |
| `received_at` | Time the first trusted ingestion boundary received the message |
| `normalized_at` | Time this mapping version produced the normalized record |
| `persisted_at` | Time durable event storage committed the record |
| `source_offset` | Original UTC offset, if supplied; preserve alongside normalized instant |
| `source_precision` | Seconds, milliseconds, ticks, or declared precision; do not invent digits |
| `source_clock_quality` | `within-policy`, `outside-policy`, `unknown`, `unsynchronized`, etc. with evidence |
| `source_sequence` | Original sequence/counter as string or bounded integer |
| `sequence_scope` | Device, channel, account, subscription, boot/session, or other reset scope |

Use RFC 3339 timestamps when the contract calls for Internet date/time. RFC 9557 extends the format for additional information such as time-zone annotations; consumers must explicitly support the selected profile. Preserve the original string, parsed instant, offset/annotation, precision, and parse warning where evidentiary interpretation matters. [RFC3339] [RFC9557]

Use monotonic clocks for durations, deadlines, and retry windows. Never order different systems solely by wall-clock timestamps when offset/error is unknown.

### Correlation and delivery

| Field | Rule |
|---|---|
| `correlation_id` | Groups a workflow/incident/session; does not prove causation or identity |
| `causation_id` | References the event/command that directly caused this record where known |
| `trace_context` | Propagation telemetry; untrusted inbound values must not become audit identity |
| `delivery_id` | Unique attempt/delivery identity; changes across redelivery |
| `delivery_attempt` | Bounded attempt count from the current delivery system, not source event count |
| `subscription_ref` | Consumer/subscription configuration identity and version |
| `ack_state` | Transport/broker/consumer milestone explicitly named; not operator or physical acknowledgement |
| `dedupe_key` | Versioned derived key only when source identity cannot provide one; preserve rationale and collision window |

One event can have many deliveries. Deduplicate side effects, not evidence: retain a delivery audit or counters while presenting one logical event when evidence supports equivalence.

### Quality, validation, and evidence

| Field | Rule |
|---|---|
| `validation.syntax` | Parser/schema outcome and version |
| `validation.integrity` | CRC/MAC/signature/TLS evidence stated precisely; CRC is not authenticity |
| `validation.peer_identity` | Authenticated source identity and trust-policy reference, not secret material |
| `validation.authorization` | Whether the source was allowed to publish for tenant/site/resource/type |
| `quality` | Stale, uncertain, substituted, test, incomplete, gap, clock, sequence, and mapping flags |
| `confidence` | Only when the source/model defines scale, calibration, threshold, and version; never generic “percent true” |
| `parse_warnings` | Bounded codes, not raw attacker-controlled text |
| `raw_ref` | Protected immutable/bounded source-record reference, where retention policy allows |
| `raw_digest` | Algorithm plus digest over explicitly defined original bytes; never recompute over a lossy parse |
| `evidence_policy` | Retention/access/redaction/classification rule and version |

A TLS connection authenticates a peer/hop under a trust policy; it does not prove every payload field true. A valid signature does not authorize an event type for a tenant/site/resource. Record these decisions separately.

## Missing, null, unknown, and false

| Representation | Meaning |
|---|---|
| Field absent | Source/mapping did not supply it or schema makes it optional |
| `null` | Explicit no-value only if the schema defines that meaning |
| `unknown` enum/value | Source supplied an unsupported/ambiguous value or state cannot be established |
| `false` / zero / empty string | Actual values; never use as generic missing defaults |
| Mapping warning | Transformation lost precision, namespace, code, or certainty |

Preserve unrecognized enum/code values in a source field and mark normalized mapping unknown. Forward-compatible parsers must not crash, silently coerce, or grant a more privileged meaning.

## Deduplication and ordering

Preferred identity evidence, strongest first:

1. source-defined immutable event ID within a stable authenticated source namespace;
2. source session/boot epoch plus sequence/counter whose reset and wrap rules are known;
3. protocol transaction/message identity plus source/account/resource/type under a documented retry window;
4. a versioned derived fingerprint over defined stable source fields/raw bytes, with collision/false-merge analysis;
5. heuristic time/value matching only for display correlation—not destructive deduplication.

Never deduplicate solely on timestamp, event text, card number, door name, or normalized type. A restore and a new alarm can share fields; multiple legitimate events can occur within one timestamp precision.

For ordering:

- order within the strongest known sequence scope;
- detect gap, duplicate, wrap, reset, rollback, and concurrent sources explicitly;
- preserve arrival order separately from occurrence order;
- use watermarks/bounded lateness only under a documented source/consumer contract;
- reconcile current state from an authoritative query after reconnect when safe and supported;
- never discard a late emergency/alarm event merely because its source time is old.

## Schema evolution

- Use stable versioned event types or an explicit schema version; document which changes are additive or breaking.
- Add optional fields with defined absence semantics; do not change units/type/meaning in place.
- Never reuse removed enum numbers, bit meanings, protocol codes, or schema field numbers.
- Consumers must preserve or safely ignore unknown additive fields and reject unsupported breaking versions deterministically.
- Version code tables and severity mappings independently when they change on a different lifecycle.
- Dual-publish/migrate only for a bounded window; correlate old/new records without causing duplicate side effects.
- Reprocessing raw records with a new mapping produces a new derived version/provenance, not silent mutation of old evidence.

## Safe synthetic CloudEvents-shaped fixture

The fixture below is a synthetic protocol illustration. Its people, credentials, endpoints, commands, and identifiers are deliberately non-operational.

```json
{
  "specversion": "1.0",
  "id": "evt-synthetic-0007",
  "source": "urn:example:lab:access-controller:ac-01",
  "type": "org.example.reader.connectivity.changed.v1",
  "subject": "reader/rdr-014",
  "time": "2026-08-25T03:14:15.120Z",
  "datacontenttype": "application/json",
  "dataschema": "https://schemas.example/events/reader-connectivity/v1",
  "data": {
    "schema_version": 1,
    "source_type": "SYNTHETIC_LINK_STATE",
    "mapping_version": "access-map-1.0.0",
    "tenant_ref": "tenant-synthetic",
    "site_ref": "site-synthetic-a",
    "resource": {
      "kind": "reader",
      "id": "rdr-014"
    },
    "previous_state": "online",
    "state": "offline",
    "transition": "changed",
    "observed_at": "2026-08-25T03:14:14.900Z",
    "received_at": "2026-08-25T03:14:15.120Z",
    "source_sequence": "88421",
    "sequence_scope": "controller-boot-session-synthetic-3",
    "mapping_quality": "exact",
    "quality": ["synthetic", "source-clock-within-policy"],
    "raw_ref": "urn:example:evidence:trace:0007"
  }
}
```

CloudEvents defines interoperable context attributes and bindings; it does not define this physical-security `data` schema, processing model, security policy, or event meaning. Stable CloudEvents release 1.0.2 was the published baseline on 2026-08-25; the repository main branch showed 1.0.3 work in progress, so production profiles should pin the released tag. [CLOUDEVENTS]

## JSON and canonicalization rules

- Accept only the contract's character encoding/media type; JSON interoperability is UTF-8 under RFC 8259 network use.
- Bound encoded bytes, decompressed bytes, nesting, object members, arrays, strings, numbers, and total events before allocation.
- Reject duplicate object member names or define a single strict policy across all producers/consumers; do not let parsers disagree.
- Validate integers/ranges without floating-point loss, especially identifiers, sequences, counters, and epoch values.
- Do not sign/hash “ordinary protobuf/JSON serialization” as though it were inherently canonical.
- If JSON canonicalization is required, implement and name RFC 8785 JCS exactly, including its input constraints; preserve the original bytes separately when evidentiary identity depends on them. [JCS]
- Authenticate before expensive schema resolution/normalization where possible, but retain a bounded rejection audit.

## Severity and alarm lifecycle

Keep at least three values separate:

1. source severity/priority/code;
2. normalized domain condition under a versioned mapping;
3. local incident/routing priority under site policy.

Likewise, `new`, `active`, `acknowledged`, `silenced`, `restored`, `closed`, and `dispatched` are not interchangeable. A receiver ACK, broker ACK, application persistence, operator acknowledgement, and physical restoration are different milestones. See [alarm monitoring protocols](../02-protocols/alarm-monitoring/README.md).

## Review checklist

- [ ] Event, state, command, and delivery records separate
- [ ] Source plus event ID, delivery ID, correlation, and causation have distinct semantics
- [ ] Source code/qualifier/extensions preserved with namespace and edition
- [ ] Tenant/site/resource/actor/credential references use governed separate namespaces
- [ ] Occurred/observed/emitted/received/normalized/persisted times and clock quality preserved
- [ ] Sequence scope, reboot/reset/wrap/gap/duplicate/late behavior defined
- [ ] Null/missing/unknown/false and enum-forward-compatibility rules explicit
- [ ] Mapping and code-table versions immutable and auditable
- [ ] Raw evidence reference/digest boundary and privacy/retention policy defined
- [ ] Parser/message/decompression/resource limits and duplicate JSON member policy defined
- [ ] Authentication, source authorization, integrity, quality, and semantic truth not collapsed
- [ ] Normalized event cannot directly actuate or acknowledge a high-impact system
- [ ] Fixture uses only synthetic, non-operational identifiers; source/product behavior is evidenced through separate environment validation

## Sources

- **CLOUDEVENTS** — [CloudEvents specification repository and released documents][CLOUDEVENTS], CNCF, stable release 1.0.2 and work-in-progress state reviewed 2026-08-25.
- **CLOUDEVENTS-102** — [CloudEvents 1.0.2 core specification][CLOUDEVENTS-102], CNCF, released baseline.
- **JSON** — [RFC 8259: The JavaScript Object Notation Data Interchange Format][JSON], IETF, December 2017.
- **RFC3339** — [RFC 3339: Date and Time on the Internet: Timestamps][RFC3339], IETF, July 2002.
- **RFC9557** — [RFC 9557: Date and Time on the Internet: Timestamps with Additional Information][RFC9557], IETF, April 2024; updates RFC 3339.
- **JCS** — [RFC 8785: JSON Canonicalization Scheme][JCS], IETF, June 2020.

[CLOUDEVENTS]: https://github.com/cloudevents/spec
[CLOUDEVENTS-102]: https://github.com/cloudevents/spec/blob/ce%40v1.0.2/cloudevents/spec.md
[JSON]: https://datatracker.ietf.org/doc/rfc8259/
[RFC3339]: https://datatracker.ietf.org/doc/rfc3339/
[RFC9557]: https://datatracker.ietf.org/doc/rfc9557/
[JCS]: https://datatracker.ietf.org/doc/rfc8785/
