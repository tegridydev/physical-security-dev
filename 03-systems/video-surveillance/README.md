---
title: Video-Surveillance Systems
summary: Architecture and navigation for image capture, video management, recording, analytics, PTZ, evidence, and operational health.
page_type: index
domains: [video]
tags: [video-surveillance, vms, cameras, recording]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: [IEC 62676 series, ONVIF Profiles T G M V]
coverage_limit: Technology-neutral system guidance; camera placement, legal surveillance purpose, and exact product capabilities remain site/product specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Video-surveillance systems

Video is a chain of capture, encoding, transport, recording, indexing, viewing, analytics, export, and evidence handling. A green camera status does not prove useful images or continuous recording.

## Pages

- [Cameras and encoders](cameras-and-encoders.md)
- [VMS, NVR, and VSaaS](vms-nvr-and-vsaas.md)
- [Recording, storage, and retention](recording-storage-and-retention.md)
- [Analytics and metadata](analytics-and-metadata.md)
- [PTZ and device I/O](ptz-and-device-io.md)
- [Evidence export and integrity](evidence-export-and-integrity.md)
- [Health and service monitoring](health-and-service-monitoring.md)

## Data/control paths

```text
scene -> sensor/lens -> encoder -> live media -> viewer/analytics
                        |             |
                        +-> edge/central/cloud recording -> search/export
camera events/metadata -> event service/broker -> VMS/PSIM/SIEM
management client -> configuration/PTZ/I-O/firmware -> device
```

Keep capture time, media clock, receive time, recording index, and export time separate. Preserve camera/stream/recording IDs and transformation history.

## Source baseline

[IEC 62676-4:2025](https://webstore.iec.ch/en/publication/110108) publicly scopes planning, design, installation, testing, commissioning, and maintenance for video-surveillance systems. ONVIF's [profiles overview](https://www.onvif.org/profiles/) maps Profile T to advanced streaming, G to edge storage/retrieval, and M to analytics metadata/events. Profile V remains Release Candidate at this baseline and cannot yet support conformance claims.

Return to [Systems](../README.md).
