---
title: "Offline RTSP and SDP inspection in Python"
summary: "Parse a synthetic RTSP DESCRIBE response and bounded SDP fields without network access."
page_type: development
domains:
  - video
  - development
tags:
  - rtsp
  - sdp
  - python
coverage_limit: "Synthetic legacy RTSP 1.0/SDP fixture; complete protocol state, authentication, transport, media negotiation, and product behavior are outside this parser."
languages:
  - Python
scope: global
content_status: maintained
technology_status: mixed
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "RFC 7826"
  - "RFC 8866"
  - "RFC 2326"
  - "RFC 4566"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2027-02-21
---

# Offline RTSP and SDP inspection in Python

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / RTSP and SDP

Target: Python 3.14.7, standard library only  
Inputs: embedded synthetic RTSP/1.0 response  
Side effects: standard output only

RFC 7826 defines RTSP 2.0 and RFC 8866 is the current SDP base. This fixture deliberately represents the still-deployed legacy RTSP 1.0/RFC 2326 and SDP/RFC 4566 combination; it is not a current-version implementation.

## Complete example

~~~python
from __future__ import annotations

MAX_MESSAGE = 16_384
MAX_LINES = 128

BODY = (
    b"v=0\r\n"
    b"o=- 1 1 IN IP4 192.0.2.10\r\n"
    b"s=Synthetic camera\r\n"
    b"t=0 0\r\n"
    b"m=video 0 RTP/AVP 96\r\n"
    b"a=rtpmap:96 H264/90000\r\n"
    b"a=control:trackID=1\r\n"
)
MESSAGE = (
    b"RTSP/1.0 200 OK\r\n"
    b"CSeq: 1\r\n"
    b"Content-Type: application/sdp\r\n"
    + b"Content-Length: " + str(len(BODY)).encode("ascii") + b"\r\n\r\n"
    + BODY
)


def inspect(message: bytes) -> list[tuple[str, str]]:
    if not message or len(message) > MAX_MESSAGE:
        raise ValueError("message size outside allowed range")
    header, separator, body = message.partition(b"\r\n\r\n")
    if not separator:
        raise ValueError("missing header delimiter")
    header_lines = header.decode("ascii").split("\r\n")
    if not header_lines or header_lines[0] != "RTSP/1.0 200 OK":
        raise ValueError("unexpected RTSP status/version")

    headers: dict[str, str] = {}
    for line in header_lines[1:]:
        name, marker, value = line.partition(":")
        if not marker:
            raise ValueError("malformed header")
        key = name.strip().lower()
        if key in headers:
            raise ValueError("duplicate header")
        headers[key] = value.strip()

    content_length = headers.get("content-length")
    if (
        content_length is None
        or not content_length.isascii()
        or not content_length.isdecimal()
        or len(content_length) > 10
    ):
        raise ValueError("invalid content length")
    declared = int(content_length)
    if declared != len(body):
        raise ValueError("content length mismatch")
    if headers.get("content-type") != "application/sdp":
        raise ValueError("unexpected content type")

    lines = body.decode("utf-8").splitlines()
    if len(lines) > MAX_LINES:
        raise ValueError("too many SDP lines")
    fields: list[tuple[str, str]] = []
    for line in lines:
        if len(line) < 2 or line[1] != "=" or len(line) > 512:
            raise ValueError("malformed SDP line")
        fields.append((line[0], line[2:]))
    return fields


for field, value in inspect(MESSAGE):
    print(field, value)
~~~

## Expected behavior

The parser accepts the synthetic response, verifies the body length and content type, and prints bounded SDP fields. It is intentionally not a complete RTSP or SDP implementation and must not be used to control a camera.

## Validation checklist

Review fixtures for truncation, duplicate headers, invalid or mismatched content length, wrong content type, overlong lines, invalid encoding, unknown payload mappings, and explicit RTSP/SDP version mismatches. Record the fixture digest, parser version, observations, and limitations separately.

## Sources

- [RFC 7826 RTSP 2.0](https://www.rfc-editor.org/rfc/rfc7826), current RTSP base, accessed 2026-08-25.
- [RFC 8866 SDP](https://www.rfc-editor.org/rfc/rfc8866), current SDP base, accessed 2026-08-25.
- [RFC 2326 RTSP 1.0](https://www.rfc-editor.org/rfc/rfc2326), accessed 2026-08-25.
- [RFC 4566 SDP](https://www.rfc-editor.org/rfc/rfc4566), obsolete legacy baseline, accessed 2026-08-25.

## Related pages

- [RTSP, RTP, RTCP, and SDP](../../02-protocols/video-and-media/rtsp-rtp-rtcp-sdp.md)
- [Python guide](../language-guides/python.md)
