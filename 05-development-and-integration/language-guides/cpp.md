---
title: "C++ protocol development"
summary: "RAII, ownership, spans, native media, and safe device-SDK integration in C++."
page_type: development
domains:
  - development
tags:
  - cpp
  - native-sdk
languages:
  - "C++"
scope: global
content_status: maintained
technology_status: current
verification: V1
runtime_status: not-applicable
safety_level: safety-relevant
standards:
  - "ISO/IEC 14882:2024 (C++23)"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
coverage_limit: "ISO standard text is paywalled; guidance uses public Core Guidelines and vendor requirements"
---

# C++ protocol development

[Home](../../README.md) / [Development](../README.md) / [Language guides](README.md) / C++

C++ is used for native media pipelines, device SDKs and performance-sensitive protocol work. C++23 is the current published ISO C++ standard; use an older language mode only when a vendor SDK/toolchain requires it and record the deviation [ISOCPP].

## Ownership model

- Use RAII wrappers for sockets, files, SDK handles, locks and media buffers.
- Prefer value types and unique ownership; make shared ownership an explicit concurrency decision.
- Use spans/views only while the referenced storage lifetime is guaranteed.
- Express optional/error results without sentinel pointer or magic numeric ambiguity.
- Keep callback registrations in an object that unregisters before dependent state is destroyed.

## Parsing and memory safety

Validate lengths and checked arithmetic before constructing spans, iterating TLVs or allocating. Avoid reinterpret-casting untrusted bytes into structs. Decode explicit widths/endian, bound containers, and keep text encoding explicit. Use string_view only when lifetime is stable.

## Media and SDK boundaries

Record who owns a frame, whether callbacks are synchronous, thread affinity, alignment, pixel/codec format, timestamp domain and how long the memory remains valid. Copy only when necessary, but never retain borrowed SDK memory past its contract. Keep proprietary SDK objects behind an adapter.

## Error and shutdown

Choose a consistent exception/error boundary. Never allow exceptions through C callbacks. Stop new work, cancel/wake blocking I/O, unsubscribe callbacks, join workers, then release downstream handles in a documented order.

## Environment assurance

Apply strict compiler warnings, static analysis, sanitizers, fuzzing against offline parsers, and synthetic lifetime/concurrency cases. Record compiler and standard-library versions, ABI, options, fixture corpus, observations, and limitations with the integration evidence.

## Sources

- **ISOCPP** — [Standard C++: The Standard][ISOCPP], current C++23 status and ISO/IEC 14882:2024 identification, accessed 2026-08-25.
- **CPP-GUIDELINES** — [C++ Core Guidelines][CPP-GUIDELINES], public community guidance, accessed 2026-08-25.

[ISOCPP]: https://isocpp.org/std/the-standard
[CPP-GUIDELINES]: https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines

## Related pages

- [Binary frame and CRC](../examples/binary-frame-crc-c.md)
- [Vendor APIs](../../04-vendor-apis/README.md)
