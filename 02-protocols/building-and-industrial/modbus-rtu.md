---
title: Modbus RTU
summary: Serial framing, timing, addressing, CRC handling, gateway behaviour, and defensive deployment guidance for Modbus RTU.
page_type: protocol
domains: [bms, ot]
tags: [modbus-rtu, serial, rs-485, crc, fieldbus]
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [Modbus over Serial Line Specification and Implementation Guide V1.02]
coverage_limit: Electrical installation values and device timing limits must be taken from the current vendor manual and applicable cabling standard.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Modbus RTU

[Home](../../README.md) / [Protocols](../README.md) / [Building and industrial](README.md) / [Modbus](modbus-family.md) / RTU

Modbus RTU places a unit address before the application PDU and a CRC-16 after it. Frame boundaries are derived from a silent interval, so baud rate, character format, receive buffering, and inter-frame timing are part of correctness—not merely serial-port settings.[^serial]

```text
address (1 octet) | function and data (PDU) | CRC low | CRC high
```

The public V1.02 guide is the baseline for new serial implementations; the specifications index labels the older 1996 serial document as legacy-only.[^hub]

## Receive state machine

1. Detect the start of a candidate frame after an idle boundary.
2. Accumulate into a fixed maximum buffer while tracking timing.
3. Determine completeness from the function-specific shape and the next idle boundary.
4. Validate address, length, and CRC before interpreting data.
5. Correlate a response with exactly one outstanding request.
6. Classify timeout, malformed frame, CRC failure, exception response, and valid response separately.

Do not resynchronise by scanning arbitrary bytes for a plausible address/function pair; that can turn line noise or a truncated frame into valid-looking telemetry. Discard the bounded candidate at a framing violation and recover at a documented idle boundary.

## Bus and gateway behaviour

RTU is normally single-request-at-a-time on a multidrop serial segment. Enforce one bus owner and bounded turnaround. A TCP-to-RTU gateway multiplexes network clients onto this serialized resource; transaction IDs on the TCP side do not make the serial bus concurrent. Configure queue limits and per-client fairness, and test what the gateway does on timeout, unit absence, broadcast, disconnect, and late replies.

Unit address `0` has broadcast semantics for supported write operations and receives no reply. Disable it unless the operational design explicitly requires it; an accidental broadcast write can affect every attached device.

## Physical-layer record

Record the actual interface standard, two-wire/four-wire mode, baud, parity, stop bits, bias, termination, isolation, shield/ground practice, connector pinout, bus topology, and unit assignments. “RS-485” alone is not a complete interface contract. Use [serial transports](../infrastructure/serial-transports.md) for electrical context.

## Defensive controls

- Put serial servers and gateways in the OT trust zone; their web/management planes are separate exposure.
- Allowlist expected unit IDs and read functions. Gate writes through explicit application authorization and site interlocks.
- Alert on CRC bursts, unexpected broadcasts, new talkers, write functions, and sustained timeout changes.
- Use isolated taps for observation. Do not attach unterminated or incorrectly biased equipment to an operating bus.

Confirm CRC byte order, timing, and maximum ADU length against the normative guide before implementation.

## Primary sources

[^serial]: [Modbus Organization — Modbus over Serial Line Specification and Implementation Guide V1.02](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
[^hub]: [Modbus Organization — specifications](https://www.modbus.org/modbus-specifications)
