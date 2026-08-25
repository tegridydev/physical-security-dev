---
title: Serial transports
summary: UART, TIA-232, TIA-422, TIA-485, framing, wiring, gateways, isolation, and safe serial integration.
page_type: reference
domains: [ot, bms, cross-domain]
tags: [uart, rs-232, rs-422, rs-485, serial, gateway]
scope: global
content_status: maintained
technology_status: mixed
verification: V1
runtime_status: not-applicable
safety_level: high-impact
standards: [TIA-232, TIA-422, TIA-485]
coverage_limit: TIA electrical standards are licensed; exact pinout, voltage, topology, termination, timing, and protocol are product- and site-specific.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Serial transports

[Home](../../README.md) / [Protocols](../README.md) / [Infrastructure](README.md) / Serial transports

“Serial” describes a transmission style, not a complete protocol. UART framing, TIA-232/422/485 electrical interfaces, connector/pinout, duplex/topology, and the application protocol are independent choices. A DB-9, RJ-style connector, terminal block, or USB adapter does not identify the signal standard.

## Layer record

| Layer | Record |
|---|---|
| Electrical | standard/variant, signal levels, single-ended/differential, isolation, common-mode/ground, surge protection |
| Wiring | connector and pinout, cable, shield/drain, topology, pair allocation, termination, bias, length |
| UART/framing | baud, data bits, parity, stop bits, bit order, idle polarity, flow control, break handling |
| Link/application | address, frame boundary, length, escaping, checksum/CRC, direction, acknowledgement, timing |

TIA-232 is typically point-to-point and single-ended. TIA-422 commonly uses differential drivers for point-to-point/multidrop receiver arrangements. TIA-485 supports differential multipoint buses and is frequently half-duplex, but none of those statements supplies a universal connector or application protocol. Obtain the applicable TIA standard and both product manuals before connecting.[^tia]

## Receiver and state machine

Use a fixed maximum frame size, incremental parser, explicit idle/inter-character timeout, validated length, checksum/CRC before semantic decode, and a bounded outstanding-request state. Separate framing error, parity/overrun, checksum failure, application negative response, timeout, late response, and disconnect.

Do not treat a CRC as security; it detects accidental corruption, not deliberate modification. Do not resynchronise on arbitrary “plausible” bytes without a protocol-defined boundary. Use monotonic time for frame and response timers.

## Multidrop and direction control

For two-wire half-duplex buses, only the intended transmitter may drive at a time. Define driver-enable timing, turnaround, collision recovery, addressing, broadcast, bias and termination. USB-to-serial adapters, terminal servers, and IP gateways add buffering, latency, packetisation, reconnect, modem-signal, and configuration behaviour that can violate device timing.

Record gateway serial profile, TCP client/server mode, connection sharing, queue limit, idle close, keepalive, packet-boundary algorithm, TLS/management support, firmware, and failure semantics. TCP transport does not preserve serial frame boundaries automatically.

## Safe connection procedure

Before attachment, obtain a pinout, measure/confirm signal levels with appropriate equipment, isolate grounds, identify whether the port supplies power, and confirm termination/bias ownership. Use galvanic isolation and surge protection appropriate to the environment. Prefer a listen-only isolated tap for observation and an isolated bench for active work.

Connecting a mismatched transceiver can damage equipment, disturb a live bus, release a gate, stop telemetry, or create ground current. Confirm electrical compatibility, isolation, termination, bias, idle state, and recovery on an approved bench before any site connection.

## Primary sources

[^tia]: [Telecommunications Industry Association — obtain TIA standards](https://tiaonline.org/products-and-services/buy-standards/)
- [Modbus Organization — serial-line implementation guide as an application example](https://www.modbus.org/docs/Modbus_over_serial_line_V1_02.pdf)
