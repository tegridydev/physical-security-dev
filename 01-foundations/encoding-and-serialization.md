---
title: Encoding and Serialization
summary: Safe handling of binary frames, text, JSON, XML, schema evolution, and untrusted device data.
page_type: foundation
domains: [cross-domain]
tags: [encoding, serialization, binary, json, xml, parsing]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: informational
standards: [RFC 8259, RFC 8949, XML 1.0]
coverage_limit: Language-neutral principles; implementation guidance must follow the chosen parser/library version.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Encoding and serialization

Treat every byte from a device, broker, SDK, file, webhook, or discovery response as untrusted—even on a private network. Physical-security devices are long-lived, heterogeneous, and frequently expose legacy parsers.

## Processing pipeline

```text
bounded read -> frame detection -> integrity check -> structural parse
             -> schema validation -> semantic validation -> authorization
             -> state change or storage
```

Set limits before allocation: total message size, nesting depth, collection count, field/string length, decompressed size, number of XML entities, attachment count, and processing time. Reject trailing or concatenated data unless the framing explicitly permits it.

## Binary protocols

Document byte order, bit numbering, signedness, length unit, escape rules, checksum coverage, alignment, and counter wrap. Before reading a field:

1. prove the minimum remaining length;
2. validate declared lengths against frame and configured maximum;
3. use checked arithmetic for offsets and lengths;
4. reject impossible enum/reserved combinations as specified;
5. distinguish incomplete stream data from malformed frames.

A checksum detects some transmission errors; it is not cryptographic integrity or peer authentication.

## JSON

[RFC 8259](https://www.rfc-editor.org/rfc/rfc8259) defines JSON syntax and interoperability considerations. Applications must still decide:

- duplicate member names;
- integer/float precision and range;
- unknown fields and enum values;
- Unicode normalization and display safety;
- absent versus `null`;
- canonicalization if signing or hashing;
- schema/version negotiation.

Reject non-finite numbers unless explicitly defined by another encoding. Avoid round-tripping large credential identifiers through a number type that loses precision.

## XML and SOAP

Use namespace-aware parsing, a local schema set for the applicable edition, and hardened parser defaults. Disable external entity resolution and network retrieval unless a narrowly controlled use case requires it. Cap entity expansion and document size. Do not select elements by local name alone when namespaces distinguish semantics.

The authoritative XML specifications are maintained by the [W3C](https://www.w3.org/TR/xml/). Protocols such as ONVIF also publish their own schemas and Web Services Description Language (WSDL); validate against the version actually negotiated or documented.

## Compact and schema-driven encodings

CBOR ([RFC 8949](https://www.rfc-editor.org/rfc/rfc8949)), Protocol Buffers, and vendor binary SDKs can reduce size but still require bounds, schema versioning, unknown-field policy, and canonicalization rules. “Generated parser” does not remove semantic validation.

## Logging and evidence

Never log credentials, authorization headers, cookies, private keys, biometric templates, card secrets, full access tokens, or unnecessary personal data. Store a bounded sanitized excerpt, message type, sizes, parse outcome, source identity, trace ID, and integrity hash/reference when raw evidence belongs in a separately controlled store.

## Schema evolution

Prefer additive compatible change. Producers should not reuse a field with new meaning; consumers should define unknown-field and unknown-enum behaviour; both should expose schema/protocol version. A mapper version belongs in provenance so historical data can be interpreted after corrections.

