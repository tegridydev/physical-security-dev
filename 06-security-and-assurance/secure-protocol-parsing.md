---
title: "Secure protocol parsing"
summary: "Bounded parsing, canonicalization, state validation, and failure handling for binary and structured physical-security inputs."
page_type: security
domains:
  - development
tags:
  - parser
  - input-validation
  - state-machine
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "NIST SP 800-218 Version 1.1"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
coverage_limit: "Research and static guidance only; product- and deployment-specific behavior requires controlled environment validation and authoritative product evidence."
languages:
  - Python
  - TypeScript
  - "C#"
  - Go
  - C
  - "C++"
---

# Secure protocol parsing

[Home](../README.md) / [Security and assurance](README.md) / Secure protocol parsing

Every device message, event, discovery response, media descriptor, serial frame, XML document, JSON body, topic name, SDK callback, and stored capture is untrusted input. Parse bytes into a validated model before any state transition or actuation decision.

## Parsing pipeline

1. Bound transport reads by maximum frame/document size and deadline.
2. Distinguish clean end-of-stream, timeout, truncation, protocol error, and resource exhaustion.
3. Validate framing length, checksum or integrity field before allocating from attacker-controlled sizes.
4. Decode with an explicit character set, byte order, numeric width, and overflow policy.
5. Reject unknown critical versions/types; preserve unknown optional fields only when the specification permits it.
6. Canonicalize once, then validate schema, ranges, identifiers, counts, nesting, and cross-field invariants.
7. Apply replay, sequence, timestamp, session, authorization, and state-transition checks.
8. Convert to an internal typed representation that cannot express impossible combinations.
9. Log a bounded, redacted diagnostic; never echo arbitrary binary or sensitive values blindly.

## Binary protocols

- Check minimum header length before field access.
- Perform overflow-safe arithmetic before computing end offsets or allocation sizes.
- Treat declared length as a claim, not a fact; compare it with the received buffer and protocol maximum.
- Decode fixed-width integers explicitly and avoid alignment-dependent casts.
- Validate CRC/checksum where defined, but do not treat error detection as authentication.
- Bound loops over objects, registers, TLVs, APDUs, topics, channels, or media tracks.
- Keep parser state separate per peer/session and reset it predictably after malformed input.

## XML and structured text

Disable external entity resolution and network/file retrieval unless a narrowly reviewed specification truly requires them. Bound document size, nesting, attributes, namespaces, expansion, and collection counts. Validate the post-parse semantic model; a well-formed SOAP or JSON document can still request an unauthorized or impossible operation.

## State machines

Reject messages that are valid in isolation but invalid for the negotiated version, direction, role, authentication state, or sequence. Specify behavior for duplicates, retries, out-of-order delivery, unknown extensions, reconnect, resumption, peer reboot, and partial writes.

## Language emphasis

| Language | Minimum discipline |
|---|---|
| Python | Type annotations, explicit byte slices and bounds, maximum input sizes, timeouts, narrow exception handling |
| TypeScript | Strict mode plus runtime validation; compile-time types do not validate network JSON |
| C# | Bounded spans/streams, cancellation tokens, checked numeric conversions, safe XML settings |
| Go | Reader limits, contexts/deadlines, exact binary order, explicit resource closure |
| C | Fixed-width types, checked arithmetic, no unbounded string/memory operations, single cleanup path |
| C++ | RAII ownership, spans/views with lifetime clarity, checked conversions, bounded containers |

## Defensive verification design

Validate parsers with synthetic fixtures covering empty, minimum, maximum, truncated, overlong, wrong-version, bad-integrity, duplicate, replayed, out-of-order, unknown-field, invalid-encoding, and state-invalid cases. Keep fuzzing inside an isolated offline parser harness or an explicitly owned loopback process; never direct it at operational devices.

## Sources

- **NIST-SSDF** — [NIST SP 800-218 Version 1.1][NIST-SSDF], secure development practices, accessed 2026-08-25.
- **CWE-20** — [CWE-20: Improper Input Validation][CWE-20], MITRE weakness definition and mitigations, accessed 2026-08-25.
- **CWE-611** — [CWE-611: Improper Restriction of XML External Entity Reference][CWE-611], accessed 2026-08-25.

[NIST-SSDF]: https://csrc.nist.gov/pubs/sp/800/218/final
[CWE-20]: https://cwe.mitre.org/data/definitions/20.html
[CWE-611]: https://cwe.mitre.org/data/definitions/611.html

## Related pages

- [API and event security](api-and-event-security.md)
- [Development and integration](../05-development-and-integration/README.md)
- [Defensive labs](../08-defensive-labs/README.md)
