---
title: Cameras and Video Encoders
summary: Capture-chain, stream, identity, configuration, privacy, security, and failure models for network cameras and encoders.
page_type: system
domains: [video]
tags: [cameras, encoders, image-capture, onvif]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: ["IEC 62676-2-31:2019", ONVIF Profile T]
coverage_limit: System architecture only; optical design, placement, scene legality, and exact device capabilities require site/product verification.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Cameras and video encoders

A network camera combines optical sensor, image signal processing, codecs, event/analytics logic, network services, storage, identity, and sometimes physical I/O. An encoder adds network streams to analogue/specialist sources. Model those functions separately even when one enclosure provides them.

## Capture chain

```text
scene/illumination -> lens/focus/iris -> image sensor -> image processing
 -> privacy mask/overlay -> encoder profile -> media transport/recording
 -> decoder/display/export
```

Image usefulness depends on scene purpose: detection, observation, recognition, identification, overview, evidence, or analytics. Resolution alone is insufficient; field of view, target pixel density, focus, shutter/motion blur, dynamic range, illumination/IR, compression, frame rate, weather, vibration, occlusion, and display/export transformations all matter.

## Canonical entities

Keep stable IDs for device, physical sensor/video source, encoder configuration, media profile, stream URI/session, metadata source, recording track, I/O, and location. An IP address or stream URL is mutable routing data, not camera identity.

Multiple streams may serve different purposes:

- evidential recording at higher quality;
- lower-bandwidth live/remote viewing;
- analytics with crop/scale/frame constraints;
- mobile thumbnails or event clips.

Record exact source/profile so an event can be correlated to the right media. Configuration changes can invalidate pixel-density, analytics, or retention assumptions.

## Interfaces

[IEC 62676-2-31:2019](https://webstore.iec.ch/en/publication/61227) publicly scopes web-service interfaces for media/imaging configuration, real-time audio/video, PTZ, and analytics. ONVIF [Profile T](https://www.onvif.org/profiles/profile-t/) covers advanced streaming and related conditional capabilities; exact product/profile conformance must be checked in ONVIF's database. Native vendor APIs commonly remain necessary for advanced imaging, analytics, firmware, or hardware-specific features.

See [ONVIF](../../02-protocols/video-and-media/onvif.md) and [RTSP/RTP/RTCP/SDP](../../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md).

## Security and privacy

- Enroll each device with unique credentials/certificate and least-privilege viewing, recording, analytics, and management roles.
- Protect every relevant path—management HTTPS does not imply encrypted RTSP/media, events, or vendor SDK traffic.
- Disable unused discovery, legacy protocols, anonymous snapshots, cloud/P2P services, audio, I/O, and default accounts.
- Treat privacy masks as configuration requiring privilege and audit. Verify whether masks apply before encoding/export/analytics rather than only in one client display.
- Restrict firmware/update sources and preserve supported recovery; inventory hardware, firmware, plugins/apps, certificates, and end-of-support.
- Minimize audio and analytics metadata; they can be more privacy-sensitive than the image.

## Failure and health

Distinguish power/link loss, authenticated-service failure, stalled/frozen stream, excessive packet loss, wrong codec/profile, lens obstruction/defocus, moved view, image washout/darkness, storage failure, clock error, analytics failure, and configuration drift. A heartbeat proves only application reachability.

Use a known scene/reference and time-varying content checks where appropriate; hash comparison of frames can detect freezing but can also false alarm on static scenes. Do not automate a PoE restart loop without bounds, escalation, and recording-impact awareness.

## Acceptance evidence

- exact model/hardware/firmware and profile declaration;
- each media profile, codec/level/resolution/rate/bitrate/keyframe and purpose;
- source-to-display/export quality under representative conditions;
- time synchronization and media-to-event correlation;
- authentication/authorization and certificate rotation;
- restart, network loss, recorder failover, configuration backup/restore;
- privacy mask/audio/metadata behavior in live, recorded, analytic, and exported paths;
- physical view/tamper and useful-image monitoring.

Runtime acceptance belongs to the user; this page makes no device claim.

Return to [Video-surveillance systems](README.md).
