---
title: Video-System Health and Service Monitoring
summary: Layered health, useful-image checks, recording continuity, dependency monitoring, alerts, and service evidence.
page_type: system
domains: [video]
tags: [health, monitoring, uptime, recording-gaps, service]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: safety-relevant
standards: ["IEC 62676-4:2025", NIST IR 8259A]
coverage_limit: Monitoring model only; thresholds, service levels, and useful-image criteria must come from the site's operational requirement and acceptance criteria.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Video-system health and service monitoring

“Online” is not a useful video-service state. Health must show the highest layer currently evidenced and the age/quality of that evidence.

## Layered model

| Layer | Examples | Does not prove |
|---|---|---|
| Power/environment | PoE draw, PSU/UPS, temperature | Network or useful image |
| Link/network | port/link, IP, packet loss, DNS/routing | Authenticated service |
| Device/service | HTTPS/ONVIF/RTSP response, certificate | Fresh media or recording |
| Stream | packets, decode, changing frames, codec/profile | Correct scene/quality |
| Image/audio | brightness, blur, occlusion, view, audio level | Recording continuity |
| Recording/index | segments, index lag, playback sample | Retention/export/evidence |
| Analytics/events | input and inference/event rate | Accurate detection |
| Operator outcome | alert received/owned/resolved | Permanent remediation |

Represent each separately. Unknown or stale cannot become healthy.

## Signals

- device reboot/uptime, firmware/configuration hash/version, certificate/credential expiry;
- PoE/power, temperature, storage/card wear, fan/disk/array/object errors;
- bitrate, frame/keyframe rate, resolution/codec, packet loss/jitter/reconnect;
- last decodable/changing frame and source timestamp/clock offset;
- view/tamper/blur/dark/bright/obstruction and privacy-mask drift;
- central/edge recording gap, late segment, index lag, retention/deletion failure;
- event/metadata subscription sequence gaps, silence, rate anomaly, rule/model state;
- recorder/VMS database, license, queue, storage, identity, DNS/time, WAN/cloud dependencies.

## Alert design

Define threshold, duration, priority, site/time context, suppression/maintenance, owner, escalation, and recovery evidence. Correlate common-cause failures—switch, WAN, power, certificate CA, time, cloud—without collapsing affected cameras into one invisible aggregate.

Avoid automated restart as first response. Bound retries/reboots, protect recording catch-up, and escalate repeated recovery. Preserve pre-restart diagnostics.

## Service workflow

```text
detect -> qualify/correlate -> notify -> acknowledge/own
 -> diagnose -> restore -> independently verify -> close -> trend/prevent
```

An alert acknowledgement does not restore service. Closure should state actual root cause or uncertainty, changes made, validation evidence, gaps/impact, and follow-up.

## Security and privacy

Monitoring agents/accounts should be read-only where possible and separately scoped from viewing/actuation. Do not send thumbnails, live URLs, credentials, or personal metadata into general monitoring without need. Protect diagnostics and packet captures as sensitive.

NIST [IR 8259A](https://csrc.nist.gov/pubs/ir/8259/a/final) identifies six core IoT device cybersecurity capabilities useful for acquisition and monitoring: device identification, device configuration, data protection, logical access to interfaces, software update, and cybersecurity-state awareness. [IEC 62676-4:2025](https://webstore.iec.ch/en/publication/110108) includes maintenance in its VSS application-guideline scope.

## Acceptance

Inject approved non-destructive faults in an isolated or maintenance context—loss of stream, recording destination, time, certificate renewal, storage pressure, WAN, and view degradation—and verify alert, impact, restoration, and gap visibility.

Return to [Video-surveillance systems](README.md).
