#!/usr/bin/env python3
"""Inspect a saved RTSP DESCRIBE response containing SDP. No network requests."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 65_536
SDP = b'v=0\r\no=- 1 1 IN IP4 192.0.2.10\r\ns=Demo\r\nt=0 0\r\nm=video 0 RTP/AVP 96\r\na=rtpmap:96 H264/90000\r\na=control:track1\r\n'
DEMO = b'RTSP/1.0 200 OK\r\nCSeq: 1\r\nContent-Type: application/sdp\r\nContent-Length: ' + str(len(SDP)).encode() + b'\r\n\r\n' + SDP

def inspect(data: bytes) -> dict[str, object]:
    if len(data) > MAX_BYTES:
        raise ValueError('Saved response exceeds 64 KiB')
    header, separator, body = data.partition(b'\r\n\r\n')
    if not separator or len(header) > 16_384:
        raise ValueError('Missing or oversized RTSP header')
    lines = header.decode('ascii').split('\r\n')
    if not re.fullmatch(r'RTSP/(?:1\.0|2\.0) 200 [\x20-\x7e]*', lines[0]):
        raise ValueError('Expected a successful RTSP response')
    fields = {}
    for line in lines[1:]:
        name, colon, value = line.partition(':')
        name = name.lower()
        if not colon or not re.fullmatch(r'[a-z0-9-]+', name) or name in fields:
            raise ValueError('Malformed or duplicate RTSP header')
        fields[name] = value.strip()
    if fields.get('content-type', '').split(';')[0].lower() != 'application/sdp':
        raise ValueError('Expected SDP content')
    length = fields.get('content-length', '')
    if not length.isascii() or not length.isdecimal() or int(length) != len(body):
        raise ValueError('Content length does not match the saved body')
    if not re.fullmatch(r'\d{1,10}', fields.get('cseq', '')):
        raise ValueError('Missing or invalid CSeq')
    text = body.decode('utf-8')
    media: list[dict[str, object]] = []
    if not text.startswith('v=0\r\n'):
        raise ValueError('Expected SDP version 0 with CRLF line endings')
    for line in text.split('\r\n'):
        if len(line) > 4096 or any(ord(c) < 32 for c in line):
            raise ValueError('Invalid SDP line')
        if line.startswith('m='):
            values = line[2:].split()
            if len(values) < 4 or len(media) >= 32:
                raise ValueError('Invalid media description')
            media.append({'type': values[0], 'port': values[1], 'transport': values[2], 'formats': values[3:], 'rtpmap': []})
        elif line.startswith('a=rtpmap:') and media:
            media[-1]['rtpmap'].append(line.removeprefix('a=rtpmap:'))
    if not media:
        raise ValueError('No media descriptions found')
    return {'cseq': int(fields['cseq']), 'media': media}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--file', type=Path, help='One raw RTSP response with CRLF bytes preserved')
    args = parser.parse_args()
    try:
        data = DEMO
        if args.file:
            with args.file.open('rb') as source:
                data = source.read(MAX_BYTES + 1)
        print(json.dumps(inspect(data), indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
