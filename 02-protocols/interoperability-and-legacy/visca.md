---
title: Sony VISCA and VISCA over IP
summary: VISCA serial and IP framing, command/inquiry state, sequence and retransmission handling, model scoping, and safe PTZ control.
page_type: protocol
domains: [video]
tags: [visca, visca-over-ip, sony, ptz, udp, rs-422]
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-applicable
safety_level: high-impact
standards: [Sony VISCA, Sony VISCA over IP]
coverage_limit: Based on official Sony BRC/SRG command lists; commands, payload types, transports, limits, and timing vary by exact camera model and software version.
languages: []
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Sony VISCA and VISCA over IP

[Home](../../README.md) / [Protocols](../README.md) / [Interoperability and legacy](README.md) / VISCA

VISCA is Sony's camera-control protocol. Official command lists define serial VISCA and VISCA over IP for specific BRC/SRG models; third-party products may implement different subsets or variants. Bind every adapter to an exact model, software version, manual revision, transport, and capability matrix.[^sony]

## Serial VISCA

For the reviewed Sony models, serial VISCA uses RS-422, 9600 or 38400 bit/s, 8 data bits, one stop bit, no parity, no XON/XOFF or RTS/CTS, and a daisy-chain addressing model with one controller and up to seven peripherals.[^sony]

A VISCA packet is 3–16 bytes: an address header, 1–14 message bytes, and `FF` terminator. Controllers send commands or inquiries. Commands normally receive an ACK identifying a camera command socket, followed by Completion or Error; inquiries return data/Completion without an ACK. The reviewed devices have a small bounded command-buffer/socket model, so correlation and backpressure are mandatory.

Do not send the next command merely because ACK arrived: ACK means accepted into a buffer, while Completion means execution ended. Completion order can differ when multiple commands are outstanding. Keep socket number, operation, send time, ACK, completion/error, cancel state, and subsequent observed camera state.

## VISCA over IP

The reviewed Sony command list specifies IPv4/UDP port **52381**, an 8-byte message header, a 1–16-byte payload, payload type/length, and a sequence number.[^sony] VISCA address fields are fixed for controller/camera roles rather than carrying the IP endpoint identity; serial broadcast/address-setting behaviour is restricted.

UDP does not guarantee delivery. Sony requires application delivery confirmation and retransmission behaviour and describes retransmitting with the same sequence number to infer whether a command or response was lost. Implement the exact model manual's table—blindly allocating a new sequence and repeating a movement/preset command can duplicate an action. Bound retries, use monotonic time, reject responses from unexpected endpoints, handle wrap/reset, and stop on sequence error rather than guessing.

## Parser and capability rules

- Validate IP header payload type, declared 1–16-byte length, total datagram length, sequence, VISCA terminator, response class, socket, and model-specific parameter ranges before dispatch.
- Reject unsupported categories/commands and preserve distinct syntax, buffer-full, cancelled, no-socket, and not-executable errors.
- Serialize commands where the manual requires; inquiries may have different correlation rules.
- Clamp pan/tilt/zoom speeds and positions to model limits. Use a dead-man stop for continuous motion and query/observe final state.
- Treat preset recall/store, power, focus/iris, tally, menu, tracking, and device-setting commands as separately authorized capabilities.

## Security and safety

The reviewed VISCA transports do not provide modern cryptographic peer authentication or confidentiality. Restrict UDP and serial paths to approved controllers, isolate camera management, prevent public reachability, and use an authenticated gateway if remote control is required. Source IP is still not operator identity; the gateway must enforce authorization and audit.

PTZ motion affects privacy and security coverage. Provide priority/ownership arbitration with the VMS/operator, mechanical clearance, stop/recovery, rate limits, preset governance, and policy zones. Validate movement, retransmission, limit, stop, and controller-conflict behaviour only with an authorized camera in a controlled setting.

## Primary sources

[^sony]: [Sony — VISCA Command List, BRC-X400/X401 and SRG-X series, software 2.10](https://pro.sony/support/res/manuals/E042/3230148ee903c204b912cca5c2c3f5aa/E0421001M.pdf)
- [Sony — newer SRG-X40UH/H40UH VISCA command list](https://pro.sony/support/res/manuals/5046/91d09d554cfc9e06372abbe82a55c18e/50462901M.pdf)
