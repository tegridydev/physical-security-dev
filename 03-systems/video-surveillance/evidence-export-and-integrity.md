---
title: Video Evidence Export and Integrity
summary: Native/open export, provenance, signatures, transformations, chain of custody, playback, and disclosure boundaries.
page_type: system
domains: [video]
tags: [evidence, export, integrity, chain-of-custody, media-signing]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [NIST IR 8161 Rev. 1, "IEC 62676-2-11:2024", ONVIF Media Signing]
coverage_limit: Technical evidence handling only; admissibility, disclosure, search authority, retention, and chain-of-custody requirements are jurisdiction/case specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Video evidence export and integrity

Evidence quality depends on faithful retrieval, provenance, time, transformation history, protected custody, and reproducible playback. A file hash proves only that later bytes match the hashed bytes; it does not prove the camera, clock, identity, or scene was trustworthy.

## Preserve layers

1. **Native/master retrieval:** original container/segments, metadata, logs, and vendor player/codec where authorized and needed.
2. **Working copy:** controlled derivative for review, redaction, or distribution.
3. **Disclosure copy:** minimum necessary format/content with explicit transformations.

Avoid transcoding the only copy. Open formats improve access but can change compression, resolution, aspect ratio, timestamps, overlays, audio, or metadata. NIST's [Standard Practice for Data Retrieval from Digital CCTV Systems](https://www.nist.gov/document/standard-practice-data-retrieval-digital-cctv-systems) specifically notes these risks and emphasizes permission and contemporaneous audit notes.

## Export manifest

Record:

```text
case/request and legal/organizational authority
operator and authenticated account/workstation
source system/device/camera/recording identifiers and versions
requested and actual time range, timezone/offset, clock quality
native segment/track IDs, gaps, audio/metadata inclusion
export format, codec/player and exact options
file names, sizes, cryptographic hash algorithms/values
signatures/certificates and validation time/trust source
every transcode, crop, resize, overlay, redaction, trim, or rewrap
storage/copy/access/transfer/custody events
```

Store sensitive evidence only in approved evidence systems with access control, encryption, retention, audit, and legal-governance controls—not in ordinary documentation repositories.

## Interoperability and signing

[NIST IR 8161 Rev. 1](https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8161r1.pdf) recommends a CCTV digital-video export profile supporting interoperability, metadata, and chain-of-custody/integrity needs. [IEC 62676-2-11:2024](https://webstore.iec.ch/en/publication/66755) defines VMS/VSaaS interoperability levels that include export.

ONVIF's [Media Signing Specification](https://www.onvif.org/specs/stream/ONVIF-MediaSigning-Spec.pdf) describes embedding signatures and verification material in encoded media; the verifier still needs an externally trusted CA certificate. ONVIF's [26.06 specification history](https://www.onvif.org/profiles/specifications/specification-history/) added Media Signing support to its Export File Format. Verify exact device/client support and trust-chain policy—signature presence is not automatic authenticity.

## Validation

- Verify hash/signature with approved tools and trust anchors; record tool/version/result.
- Play beginning, middle, end, transitions, audio, and representative gaps using preserved and independent playback paths.
- Correlate source time with event/audit and known clock uncertainty.
- Confirm camera/source/scene and that privacy masks/overlays are source or derivative transformations as stated.
- Keep master read-only/immutable according to policy; produce new derivatives instead of overwriting.

## Privacy and release

Export authority is separate from viewing authority. Apply case/site/camera/time scope, dual review where required, watermarking/redaction policy, secure transfer, recipient validation, expiration, revocation where possible, and disclosure audit. Redaction creates a derivative and must never be represented as untouched original.

Return to [Video-surveillance systems](README.md).
