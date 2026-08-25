---
title: SIA AV-01 audio verification and two-way voice commands
summary: Developer reference for the DTMF monitoring-operator command set used with premises audio-verification systems.
page_type: protocol
domains: [alarms, intercom]
tags: [sia, av-01, audio-verification, dtmf, privacy]
scope: global
content_status: maintained
technology_status: legacy
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [SIA AV-01-2014]
coverage_limit: Public SIA scope was reviewed; exact command assignments and timing require the purchased normative standard and product documentation.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# SIA AV-01 audio verification and two-way voice commands

[Home](../../README.md) / [Protocols](../README.md) / [Alarm monitoring](README.md) / AV-01

SIA AV-01-2014 describes minimum DTMF command sets by which a monitoring-service operator controls a premises audio-verification/two-way-voice system. SIA's public scope includes basic two-way voice, microphone or microphone-zone control, relay or relay-zone control, and optional integrated-home functions.[^sia-av01]

## Boundary and roles

```text
monitoring operator
   │ presses authorized DTMF command
   ▼
telephone / receiver audio path
   ▼
premises audio-verification system
   ├─ listen / talk mode
   ├─ microphone or zone selection
   └─ relay or integrated function, if implemented
```

AV-01 is a control vocabulary over an established call/audio path. It is not a modern media-signalling, encryption, identity, consent, or recording-retention standard. SIP, RTP, WebRTC, cellular, or VoIP equipment may carry the call, but does not change AV-01's application semantics.

## Integration model

Represent commands as constrained actions, not arbitrary digits:

- operator identity and authenticated session;
- target account and active alarm/verification session;
- requested mode, microphone zone, relay zone, or function;
- product capability and whether the function is permitted for that account;
- command issue, tone-delivery, device acknowledgement, and observed-result times;
- timeout, ambiguous outcome, and any fallback to manual procedure;
- recording/retention and access-control context.

The operator console must not expose commands unsupported by the exact premises device. Avoid automatic retry of relay or mode commands after an uncertain result; the first command may have taken effect even when its acknowledgement was lost.

## Security, privacy, and safety

- Authenticate the operator and bind each call to the expected account and receiver session before enabling commands.
- Apply least privilege separately to listen, talk, microphone-zone, and relay functions.
- Prevent DTMF from unrelated call legs, announcements, recordings, or injected audio from reaching the command decoder.
- Rate-limit invalid sequences and terminate or escalate on repeated authentication or command errors.
- Make active listening/talk state unambiguous to the operator; respect applicable notice, consent, minimization, and retention law.
- Treat microphones and recordings as sensitive surveillance data.
- Treat any relay command as physical actuation. Document the connected load and prohibit use for egress, fire, life safety, or another unsafe function unless the complete certified system explicitly supports it.

DTMF recognition is not cryptographic authentication, and a successful tone decode does not prove that a microphone, loudspeaker, or relay reached its intended physical state.

## Compatibility record

Record AV-01 edition, device model/firmware, supported command groups, microphone/relay zone mapping, call transport and codecs, DTMF transport mode, timeouts, acknowledgements, operator permissions, recording policy, and safe behaviour on call loss. Exact assignments must come from the licensed standard and product manual.

## Safety boundary

Do not call, listen to, speak through, or actuate a production premises system for exploratory validation. Validate media negotiation, consent indications, timeout, teardown, audit, and failure handling only in a fully isolated, consented setup with no dispatch and no connected physical load.

## Primary source

[^sia-av01]: Security Industry Association, [SIA AV-01-2014 — Protocol for Audio Verification and Two-Way Voice](https://www.securityindustry.org/industry-standards/sia-av-01-2014/), reviewed 2026-08-25.
