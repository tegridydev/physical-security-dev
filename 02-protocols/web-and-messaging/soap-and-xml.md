---
title: "SOAP, WSDL, XML Schema, and secure XML processing"
summary: "Developer reference for SOAP message structure, WSDL contracts, XML namespaces/schema, faults, bindings, and hardened parsing in physical-security services."
page_type: protocol
domains: [cross-domain, networking]
tags:
  - soap
  - xml
  - wsdl
  - xsd
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "SOAP Version 1.2, Second Edition (W3C Recommendation, 2007)"
  - "XML 1.0, Fifth Edition (W3C Recommendation, 2008)"
  - "WSDL 2.0 (W3C Recommendation, 2007)"
  - "XML Schema 1.1 (W3C Recommendation, 2012)"
coverage_limit: "SOAP/XML contract and parser-hardening guidance only; no WSDL compilation, generated binding, XML library, schema, signature profile, endpoint, or ONVIF exchange is validated."
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# SOAP, WSDL, XML Schema, and secure XML processing

[Web and messaging protocols](README.md) / SOAP and XML

SOAP defines an XML message-processing framework. WSDL describes service interfaces and bindings. XML Schema constrains document structure and data types. None of these supplies authorization, safe parser defaults, or semantic validation automatically.

## Standards snapshot

| Technology | Stable reference | Deployment note |
|---|---|---|
| SOAP 1.2 | W3C Recommendation, Second Edition, 2007 | Current W3C SOAP Recommendation; commonly uses `application/soap+xml` |
| SOAP 1.1 | W3C Note, 2000 | Still widely deployed, including contract ecosystems that predate SOAP 1.2; not interchangeable with 1.2 |
| XML 1.0 | W3C Recommendation, Fifth Edition, 2008 | Core syntax |
| XML Namespaces 1.0 | W3C Recommendation, Third Edition, 2009 | Expanded names are namespace URI plus local name; prefixes are aliases |
| WSDL 2.0 | W3C Recommendation, 2007 | Interface/operation/binding/service model |
| WSDL 1.1 | W3C Note, 2001 | Extensively deployed by SOAP toolchains and physical-security specifications |
| XML Schema 1.1 | W3C Recommendation, 2012 | Schema components and datatype constraints; support differs by library |
| WS-Addressing 1.0 | W3C Recommendation, 2006 | Endpoint references and message-addressing properties |
| WS-Security 1.1.1 | OASIS Standard, 2012 | SOAP message security building blocks; profiles and canonicalization matter |

Pin the contract family and version. A SOAP 1.1 client cannot be made SOAP 1.2 by changing only the HTTP content type. [SOAP12] [SOAP11]

## Message anatomy

```text
Envelope
├── Header (optional)
│   ├── addressing, security, correlation, routing, vendor blocks
│   └── mustUnderstand / role processing rules
└── Body (required)
    └── operation element or Fault
```

SOAP intermediaries can process header blocks targeted to roles. A receiver must apply the correct SOAP version's `mustUnderstand`, role/actor, relay, fault, and media-type rules. Silently ignoring an understood-required security header can invalidate the complete security model.

## Safe envelope fixture

**Target:** XML parser and request-construction fixture.

**Inputs:** No endpoint, credentials, device token, or production data.

**Side effects:** None.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<env:Envelope
    xmlns:env="http://www.w3.org/2003/05/soap-envelope"
    xmlns:demo="urn:example:physical-security-dev:device">
  <env:Header/>
  <env:Body>
    <demo:GetStatus>
      <demo:DeviceToken>synthetic-device-001</demo:DeviceToken>
    </demo:GetStatus>
  </env:Body>
</env:Envelope>
```

Match the expanded name `{urn:example:physical-security-dev:device}GetStatus`, not the `demo` prefix text. Prefixes can legally change without changing the element's identity.

## WSDL-first implementation

A contract-first workflow:

1. Pin the WSDL, imported WSDLs/XSDs, published errata, and profile/version.
2. Resolve and vendor approved dependencies in a controlled build process; do not fetch imports dynamically in production.
3. Generate or implement types, then review generated defaults, nullable/optional semantics, numeric ranges, and collection bounds.
4. Map operations to explicit authorization and idempotency behavior.
5. Validate actual messages against both schema and application rules.
6. Test fault, version mismatch, unknown header, extension, and forward-compatibility behavior manually in the authorized environment.

WSDL describes available operations and message shapes, not which authenticated principal may invoke them or what a successful response proves physically.

## XML data model details

- An absent element, an empty element, and `xsi:nil="true"` are different states.
- Element order can be significant under a schema sequence.
- Defaulted/fixed schema values can appear in the post-schema-validation model even if absent on the wire; library behavior varies.
- Whitespace normalization is datatype-dependent.
- Decimal, integer, date/time, duration, QName, binary, and URI types require type-specific handling.
- XML timestamps can include offsets or omit a timezone; define what an absent timezone means in the application.
- Unknown extension elements need a deliberate preserve/ignore/reject policy.

## Faults and HTTP

SOAP Faults are protocol-level structured error messages; HTTP status is transport/binding state. Document both. Parse only bounded fault detail and do not expose server stacks, credentials, internal paths, policy internals, or device secrets. Preserve a correlation ID generated by the trusted service boundary.

Retry policy is operation-specific. A network failure after a mutating SOAP request does not prove the operation failed. Use an operation identifier, sequence, precondition, or read-back confirmation where the specification supports it.

## Hardened XML processing

### External resource controls

- Disable external general entities, external parameter entities, and external DTD loading for untrusted XML.
- Disable XInclude and external stylesheet/document resolution unless explicitly required and strictly allowlisted.
- Do not let schema imports, catalog resolution, or XSLT perform unrestricted network/file access.
- Use local, reviewed schemas from an immutable versioned bundle.

### Resource controls

- Cap raw body, decompressed body, element depth, node count, attribute count/length, namespace declarations, text length, base64 decoded size, list size, and processing time.
- Reject compression/entity expansion bombs before large allocation.
- Stream only when the application can maintain the same validation and authorization guarantees; streaming is not inherently safe.
- Do not deserialize arbitrary types from `xsi:type`, class names, or extension points.

### Namespace and duplicate controls

- Compare namespace URI plus local name.
- Reject duplicate singleton fields and conflicting IDs.
- Do not search the whole document for a security-relevant local name; process the exact schema path.
- Treat namespace undeclaration/rebinding and unexpected wrapper elements as parser test cases.

## XML signatures and WS-Security

TLS protects a hop. WS-Security can protect selected message parts across SOAP processing roles, but only under a precisely defined profile. For signed/encrypted SOAP:

- validate trust, algorithm, key usage, reference URI, transforms, canonicalization, signature placement, timestamp/freshness, nonce, and replay cache;
- require the signature to cover the exact body and headers the application consumes;
- bind authorization to the validated signer/token, not an unsigned identity field;
- reject duplicate IDs and wrapping structures that let validation and application code select different elements;
- never log decrypted security tokens, keys, passwords, or complete sensitive envelopes.

Schema validation alone does not stop signature wrapping, SSRF, replay, or business-logic abuse. [WSS]

## ONVIF notes

ONVIF uses WSDL-defined SOAP/XML services with multiple namespaces and service versions. Obtain service endpoints and capabilities at runtime, preserve opaque tokens, apply ONVIF profile rules, and use the exact WSDL/XSD set for the claimed network-interface release. See [ONVIF](../video-and-media/onvif.md).

## Review checklist

- [ ] SOAP 1.1 versus 1.2 and HTTP binding pinned
- [ ] WSDL/XSD/import versions pinned locally and provenance recorded
- [ ] Expanded names used; prefix text not treated as identity
- [ ] DTD, external entity, XInclude, stylesheet, schema-network, and file access disabled or tightly allowlisted
- [ ] Raw/decompressed size, depth, nodes, arrays, strings, and binary decoded size bounded
- [ ] Generated client/server code reviewed for optionality, ranges, and unsafe deserialization
- [ ] Every operation mapped to authentication, authorization, idempotency, audit, and timeout behavior
- [ ] `mustUnderstand`, Fault, extension, and version mismatch behavior defined
- [ ] XML signature validation and application element selection use the same exact nodes
- [ ] Sensitive envelopes and fault detail redacted

## Environment validation

Validate the pinned WSDL/XSD bundle, generated bindings, parser hardening, schema and application constraints, SOAP version/fault handling, endpoint authentication, authorization, timeout/retry semantics, signature selection, wrapping resistance, and interoperability against exact target versions.

## Sources

- **SOAP12** — [SOAP Version 1.2, Second Edition][SOAP12], W3C Recommendation, 27 April 2007.
- **SOAP11** — [SOAP 1.1][SOAP11], W3C Note, 8 May 2000.
- **XML** — [Extensible Markup Language (XML) 1.0, Fifth Edition][XML], W3C Recommendation, 26 November 2008.
- **XMLNS** — [Namespaces in XML 1.0, Third Edition][XMLNS], W3C Recommendation, 8 December 2009.
- **WSDL20** — [Web Services Description Language 2.0, Part 1][WSDL20], W3C Recommendation, 26 June 2007.
- **WSDL11** — [Web Services Description Language 1.1][WSDL11], W3C Note, 15 March 2001.
- **XSD11** — [W3C XML Schema Definition Language 1.1, Part 1][XSD11], W3C Recommendation, 5 April 2012.
- **WSA** — [Web Services Addressing 1.0 — Core][WSA], W3C Recommendation, 9 May 2006.
- **WSS** — [Web Services Security: SOAP Message Security 1.1.1][WSS], OASIS Standard, 18 May 2012.

[SOAP12]: https://www.w3.org/TR/soap/
[SOAP11]: https://www.w3.org/TR/2000/NOTE-SOAP-20000508/
[XML]: https://www.w3.org/TR/xml/
[XMLNS]: https://www.w3.org/TR/xml-names/
[WSDL20]: https://www.w3.org/TR/wsdl20/
[WSDL11]: https://www.w3.org/TR/2001/NOTE-wsdl-20010315
[XSD11]: https://www.w3.org/TR/xmlschema11-1/
[WSA]: https://www.w3.org/TR/ws-addr-core/
[WSS]: https://docs.oasis-open.org/wss-m/wss/v1.1.1/os/wss-SOAPMessageSecurity-v1.1.1-os.html
