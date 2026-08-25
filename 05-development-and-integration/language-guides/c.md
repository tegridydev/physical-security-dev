---
title: "C protocol development"
summary: "Memory- and resource-safe C patterns for embedded, serial, and binary physical-security protocols."
page_type: development
domains:
  - development
tags:
  - c
  - embedded
languages:
  - C
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "ISO/IEC 9899:2024 (C23 current published edition)"
  - "ISO/IEC 9899:2018 (C17 baseline)"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
coverage_limit: "ISO standard text is paywalled; implementation guidance uses public secure-coding sources and a deliberate C17 compatibility baseline"
---

# C protocol development

[Home](../../README.md) / [Development](../README.md) / [Language guides](README.md) / C

C is used selectively when embedded constraints, vendor SDKs, or serial/binary protocols make it representative. ISO/IEC 9899:2024 (C23) is the current published C edition; this guide deliberately uses C17 as a broad compatibility baseline for long-lived embedded and vendor toolchains. Record the selected edition, compiler, ABI, target, library, and vendor SDK requirements for every implementation.

## Parsing baseline

- Use fixed-width integer types for wire values.
- Validate buffer length before every read and output capacity before every write.
- Check addition and multiplication for overflow before offsets or allocation.
- Decode endian values byte-wise or through reviewed helpers; do not cast unaligned wire buffers to structs.
- Bound counters, recursion, TLVs, strings, nesting and allocation.
- Use explicit state enums and reject messages invalid for the current role/session.
- Treat CRC/checksum as corruption detection, not source authentication.

## Resource and lifetime rules

Define one owner for every allocation, file descriptor, socket, timer, mutex and SDK handle. Initialize cleanup state, use one auditable cleanup path where suitable, clear sensitive buffers with a mechanism the compiler will not optimize away, and do not use unbounded string or memory operations.

## Concurrency and callbacks

Document callback thread, buffer ownership and lifetime. Avoid calling complex integration logic or blocking I/O from an ISR/vendor callback. Transfer bounded immutable work to a controlled queue and define overflow behavior.

## Environment assurance

Apply strict compiler warnings, static analysis, address/undefined-behaviour sanitizers on supported hosts, and synthetic boundary fixtures. Record the exact compiler/tool versions, target/ABI, options, fixture digest, observations, and limitations with the integration evidence.

## Sources

- **SEI-C** — [SEI CERT C Coding Standard][SEI-C], public secure-coding guidance, accessed 2026-08-25.
- **ISO-C23** — [ISO/IEC 9899:2024 catalogue entry][ISO-C23], current published C edition; paywalled standard metadata, accessed 2026-08-25.
- **ISO-C17** — [ISO/IEC 9899:2018 catalogue entry][ISO-C17], paywalled standard metadata, accessed 2026-08-25.

[SEI-C]: https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard
[ISO-C23]: https://www.iso.org/standard/82075.html
[ISO-C17]: https://www.iso.org/standard/74528.html

## Related pages

- [Binary frame and CRC](../examples/binary-frame-crc-c.md)
- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
