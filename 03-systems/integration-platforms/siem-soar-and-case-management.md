---
title: SIEM, SOAR, and Case Management
summary: Provenance, normalization, correlation, retention, workflow, and safe-automation boundaries for physical-security telemetry in cyber operations platforms.
page_type: system
domains: [integration, operations, cross-domain]
tags: [siem, soar, case-management, log-management, correlation, ocsf, ecs, stix, taxii]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [NIST SP 800-92, RFC 5424, OpenTelemetry Protocol 1.11, STIX 2.1, TAXII 2.1]
coverage_limit: Defensive architecture and data governance only; no production query, response playbook, credential, live containment, physical actuation, or vendor-specific connector claim.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SIEM, SOAR, and case management

Security information and event management systems collect and correlate telemetry. Security orchestration, automation, and response platforms coordinate workflows and actions. Case systems record investigation. None becomes the authoritative source of physical state merely by ingesting an event.

## Evidence flow

```text
source-native audit/event/state
 -> authenticated collection and buffering
 -> immutable raw record/reference
 -> parser and normalized record
 -> enrichment and correlation
 -> alert
 -> case and analyst decisions
 -> separately governed response request
 -> target-native outcome and audit
```

Maintain stable source identity, native event ID/sequence, raw timestamp and clock basis, collection timestamp, raw record or durable reference, parser/version, normalized fields, enrichments and their sources, rule/version, alert/case IDs, actor, and action result.

## Source types and limits

Useful sources include device authentication/administration, PACS grant/deny and door telemetry, alarm events and receiver delivery, VMS viewing/export/configuration, intercom calls, ANPR reads, gate/controller telemetry, cloud tenant administration, network/security infrastructure, and integration-adapter logs.

Availability varies. Some products expose event journals but not administrative reads; others send state changes without durable sequence or retain only short local history. Document what is absent. A connector marked healthy does not prove every event type is enabled, ordered, delivered, parsed correctly, or retained.

## Formats, transports, and schemas are different layers

The following technologies solve different problems and should not be listed as interchangeable “SIEM formats.” Pin exact versions and product profiles.

| Category | Examples | What it provides | Important limit |
|---|---|---|---|
| Source-native interface | Product audit/event API, export file, database view, proprietary stream | Closest available source semantics and identifiers | Version, completeness, ordering, retention, and support commitments vary |
| General transport/framing | Syslog, HTTPS API/webhook, file/object delivery, OTLP | Moves or frames records | Does not define physical-security event meaning or target schema |
| Vendor event representation | Common Event Format (CEF), Log Event Extended Format (LEEF) | Delimited header/extension convention for supported SIEM ecosystems | Escaping, extension keys, typing, version, and receiver limits are profile-specific |
| Normalized security schema | Open Cybersecurity Schema Framework (OCSF), Elastic Common Schema (ECS) | Shared field/class vocabulary for analytics and search | Mapping can lose native semantics; neither is a transport or proof of truth |
| Threat-intelligence exchange | STIX 2.1 with TAXII 2.1 | Structured cyber-threat knowledge and its exchange API | Not a general replacement for device telemetry, audit, alarms, or case evidence |
| Event context envelope | CloudEvents | Portable event identity/source/type/time/content context with bindings | Does not define the domain payload, delivery guarantee, or source authorization |

### Native, syslog, HTTP, and OTLP ingestion

- Preserve the original product event code, source identity, sequence, timestamps, and raw record or integrity-protected reference before normalization.
- For syslog, identify RFC 5424 versus legacy/product syntax, transport/framing, structured-data profile, maximum length, truncation, timestamp, sender authentication, and relay path. A UDP datagram is not reliable delivery evidence. [SYSLOG]
- For HTTP APIs/webhooks, define pagination/cursor, replay window, webhook authentication, request-body limits, conditional/rate behavior, and the meaning of `2xx`; acceptance is not durable indexing.
- OTLP 1.11 is an observability export protocol, not a physical-security event schema. Pin logs/data-model conventions, resource and scope attributes, transport, authentication, partial-success handling, and collector transforms. [OTLP]
- For files and object delivery, define atomic publication, manifest/integrity, compression and archive bounds, encryption, duplicate/import state, and secure retention.

### CEF and LEEF

CEF and LEEF are vendor-defined representations commonly accepted by security analytics products. They can be useful adapter targets, but a product saying “CEF” or “LEEF” is incomplete without a profile.

Document delimiter and escaping rules, encoding, header version, required fields, timestamp/timezone, typed versus textual values, extension-key dictionary, maximum event/field length, multiline/control-character handling, transport/framing, and product-specific custom fields. Test values containing delimiters, backslashes, equals signs, Unicode, newlines, and maximum lengths in the owning environment.

Do not reuse standard keys with a different meaning merely to make a dashboard populate. Namespace custom extensions and retain the source-native field/code for reverse interpretation.

### OCSF and ECS

[OCSF][OCSF] and [ECS][ECS] provide normalization vocabularies. Select a pinned schema version and mapping version; record both on every transformed record.

- Map an event only to a class/category whose semantics match.
- Preserve native severity separately from normalized severity and operational/alarm priority.
- Keep person, credential, device, source workload, target resource, site/location, and tenant identities distinct.
- Define absent/null/unknown, arrays, units, timestamps, outcome, confidence, and extension namespaces.
- Maintain round-trip mapping evidence or a loss table; not every native fact has a normalized equivalent.
- Reprocess historical data only under an explicit migration and evidential policy—the same native record can map differently after a schema update.

OCSF and ECS can coexist in one estate when different destinations require them. Avoid a chain of lossy mappings such as native → CEF → ECS → OCSF when a direct mapping from protected native input is possible.

### STIX/TAXII and CloudEvents

STIX 2.1 represents cyber-threat intelligence objects/relationships; TAXII 2.1 defines an application-layer protocol for exchanging that content. [STIX] [TAXII] Use them for threat knowledge, indicators, observed-data context, and sharing workflows—not as a generic envelope for every access, alarm, camera, or door-state event.

CloudEvents can wrap event context across supported bindings, but its `source`, `id`, and `type` must be profiled and authorized. A valid CloudEvent carrying STIX or a normalized event still needs domain validation, privacy policy, resource limits, and mapping provenance. [CLOUDEVENTS]

## Normalization

Use a common envelope without destroying native meaning:

- source system, device/controller/site/tenant, event class and native code;
- subject/credential/object only where authorized and necessary;
- target resource/location, source and receive time, sequence, severity, quality;
- outcome at the layer observed: requested, accepted, denied, failed, restored, or unknown;
- privacy/sensitivity class and retention class;
- raw record reference, mapping/parser version, and confidence for derived data.

Do not translate `door contact open` into `forced entry` without the required controller context, or `receiver acknowledged` into `operator responded`. Preserve alarm, restore, acknowledgement, case closure, and physical outcome separately.

Keep a machine-readable mapping record with source product/schema/version, parser version, destination schema/version, rule-set hash/version, field-level transformations, dropped/derived fields, test-fixture version, approval, and effective date. Parser success is not semantic correctness.

## Correlation and cases

Rules should state purpose, sources, time window and clock tolerance, missing-data behavior, suppressions, threshold, owner, version, test evidence, and review date. Keep contributing and contradictory records so an analyst can explain an alert.

A case is a working record, not a rewrite of source evidence. Record allegations/observations separately from findings; preserve analyst actions, evidence access/export, decision rationale, handovers, retention holds, and closure/reopen events. Restrict sensitive video, biometrics, plate, access, and employee/visitor data by case purpose and role.

## SOAR boundary

Cyber actions such as disabling an account or isolating a host can still cause operational harm. Physical actions—unlocking, locking down, gate cycling, lift control, alarm bypass/reset, camera movement, relay control, or emergency notification—are high-impact and must not be driven by a generic playbook.

Where an action is approved, use a semantic, tightly scoped target request with fresh authorization, prerequisites, reason, confirmation, idempotency, timeout, human approval where appropriate, rollback/recovery, and target-native outcome. Command dispatch is not physical completion.

Prefer recommended actions and evidence collection when authority or safety is uncertain. A failed or partially completed playbook must stop visibly and preserve which steps did or did not occur.

## Log protection and operations

- Authenticate sources/collectors and protect transport where the system supports it.
- Buffer deliberately; monitor queue age, drops, parser errors, schema drift, and source silence.
- Apply least privilege to collection, search, bulk export, rule change, case access, and response.
- Protect integrity through access control, append-oriented handling, replication/backups, and independently retained administration/audit evidence.
- Synchronize time while retaining source and receive clocks and known uncertainty.
- Define retention by operational, security, privacy, legal, and evidential need; do not retain everything indefinitely.
- Test restoration and the ability to reconstruct mapping, rule, case, and audit context.
- Monitor source silence, expected-versus-received counts where available, sequence gaps, truncation, parser rejection, unmapped values, mapping drift, collector partial success, and destination indexing delay.

## Source baseline and status limitation

NIST [SP 800-92](https://csrc.nist.gov/pubs/sp/800/92/final) remains the final published *Guide to Computer Security Log Management*. NIST has also published [SP 800-92 Rev. 1 as an Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd); as of 2026-08-25 it is not treated here as a final standard. Recheck that status at the scheduled review.

See [Integration platforms](README.md) and [PSIM and command platforms](psim-and-command-platforms.md).

## Primary format and protocol sources

- **SYSLOG** — [RFC 5424: The Syslog Protocol][SYSLOG], IETF.
- **OTLP** — [OpenTelemetry Protocol Specification 1.11][OTLP], OpenTelemetry project.
- **OCSF** — [Open Cybersecurity Schema Framework schema browser][OCSF], OCSF project.
- **ECS** — [Elastic Common Schema reference][ECS], Elastic.
- **STIX** — [STIX Version 2.1 OASIS Standard][STIX], OASIS.
- **TAXII** — [TAXII Version 2.1 OASIS Standard][TAXII], OASIS.
- **CLOUDEVENTS** — [CloudEvents Specification 1.0.2][CLOUDEVENTS], Cloud Native Computing Foundation.

[SYSLOG]: https://www.rfc-editor.org/info/rfc5424/
[OTLP]: https://opentelemetry.io/docs/specs/otlp/
[OCSF]: https://schema.ocsf.io/
[ECS]: https://www.elastic.co/guide/en/ecs/current/index.html
[STIX]: https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html
[TAXII]: https://docs.oasis-open.org/cti/taxii/v2.1/os/taxii-v2.1-os.html
[CLOUDEVENTS]: https://github.com/cloudevents/spec/blob/v1.0.2/cloudevents/spec.md
