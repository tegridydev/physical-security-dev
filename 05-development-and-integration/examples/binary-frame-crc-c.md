---
title: "Bounded binary frame and CRC parsing in C"
summary: "A synthetic C17 frame parser demonstrating length, endian, bounds, and integrity checks."
page_type: development
domains:
  - development
tags:
  - c
  - binary
  - crc
coverage_limit: "Synthetic C17 reference format; compiler, platform, sanitizer, and product-protocol behavior are environment-specific."
languages:
  - C
scope: global
content_status: maintained
technology_status: not-applicable
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "ISO/IEC 9899:2018 (C17 baseline)"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Bounded binary frame and CRC parsing in C

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / Binary frame and CRC

Target: C17, standard library only  
Inputs: synthetic reference frame, not an industry protocol  
Side effects: standard output only

## Synthetic frame

The documentation-only frame is: magic byte A5, version 01, big-endian payload length, payload, then CRC-16/CCITT-FALSE over header and payload. This invented format avoids reproducing a licensed protocol.

## Complete example

~~~c
#include <inttypes.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>

#define HEADER_SIZE 4u
#define CRC_SIZE 2u
#define MAX_PAYLOAD 256u

static uint16_t crc16_ccitt_false(const uint8_t *data, size_t length) {
    uint16_t crc = UINT16_C(0xFFFF);
    for (size_t i = 0; i < length; ++i) {
        crc ^= (uint16_t)data[i] << 8;
        for (unsigned bit = 0; bit < 8; ++bit) {
            crc = (crc & UINT16_C(0x8000))
                ? (uint16_t)((crc << 1) ^ UINT16_C(0x1021))
                : (uint16_t)(crc << 1);
        }
    }
    return crc;
}

static int parse_frame(const uint8_t *frame, size_t frame_length) {
    if (frame == NULL || frame_length < HEADER_SIZE + CRC_SIZE) return -1;
    if (frame[0] != UINT8_C(0xA5) || frame[1] != UINT8_C(0x01)) return -2;

    size_t payload_length = ((size_t)frame[2] << 8) | (size_t)frame[3];
    if (payload_length > MAX_PAYLOAD) return -3;
    if (payload_length > SIZE_MAX - HEADER_SIZE - CRC_SIZE) return -4;
    size_t expected_length = HEADER_SIZE + payload_length + CRC_SIZE;
    if (frame_length != expected_length) return -5;

    uint16_t received_crc =
        ((uint16_t)frame[expected_length - 2] << 8) |
        (uint16_t)frame[expected_length - 1];
    uint16_t calculated_crc = crc16_ccitt_false(frame, expected_length - CRC_SIZE);
    if (received_crc != calculated_crc) return -6;

    printf("validated payload length: %zu\n", payload_length);
    return 0;
}

int main(void) {
    uint8_t frame[] = {0xA5, 0x01, 0x00, 0x03, 0x10, 0x20, 0x30, 0x00, 0x00};
    uint16_t crc = crc16_ccitt_false(frame, sizeof frame - CRC_SIZE);
    frame[sizeof frame - 2] = (uint8_t)(crc >> 8);
    frame[sizeof frame - 1] = (uint8_t)crc;
    int result = parse_frame(frame, sizeof frame);
    if (result != 0) {
        fprintf(stderr, "frame rejected: %d\n", result);
        return 1;
    }
    return 0;
}
~~~

## Security properties and limits

The parser checks header length, version, payload maximum, arithmetic, exact frame length and CRC before use. CRC detects accidental corruption only; it does not authenticate the sender or prevent deliberate modification/replay.

## Environment validation checklist

- [ ] Build with the environment's strict warning profile and treat relevant warnings as failures.
- [ ] Confirm the valid synthetic frame is accepted and its bounded payload length is reported.
- [ ] Cover truncated and overlong frames, excessive declared length, wrong magic/version, CRC corruption, and empty payload.
- [ ] Apply offline address/undefined-behaviour sanitizers where the supported toolchain provides them.
- [ ] Record compiler, target/ABI, flags, sanitizer versions, fixture digest, observations, and limitations.

## Sources

- [SEI CERT C Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard), accessed 2026-08-25.

## Related pages

- [C guide](../language-guides/c.md)
- [Secure protocol parsing](../../06-security-and-assurance/secure-protocol-parsing.md)
