#!/usr/bin/env python3
"""Verify a raw webhook body against the example signing contract. Offline only."""
from __future__ import annotations
import argparse
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import sys
import time

MAX_BYTES = 65_536
WINDOW = 300

def verify(body: bytes, timestamp: str, signature: str, key: bytes, now: int) -> bool:
    if len(body) > MAX_BYTES or not 32 <= len(key) <= 1024:
        raise ValueError('Body must be at most 64 KiB; key must be 32 to 1024 bytes')
    if not re.fullmatch(r'[1-9][0-9]{8,11}', timestamp):
        raise ValueError('Timestamp must be canonical decimal Unix seconds')
    if abs(now - int(timestamp)) > WINDOW:
        return False
    if not re.fullmatch(r'sha256=[0-9a-f]{64}', signature):
        return False
    # Sign exactly the timestamp, a full stop, and the unchanged body bytes.
    expected = hmac.new(key, timestamp.encode('ascii') + b'.' + body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature[7:], expected)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--file', type=Path, help='Raw request body; do not parse and reserialise it first')
    parser.add_argument('--timestamp')
    parser.add_argument('--signature')
    args = parser.parse_args()
    if not args.demo and (not args.timestamp or not args.signature):
        parser.error('--timestamp and --signature are required with --file')
    try:
        if args.demo:
            # Public fixture key for the demo only. Never use it on a service.
            key = b'demo_key_for_offline_example_only'
            body, stamp, now = b'{"event_id":"evt001"}', '1788994800', 1788994800
            signature = 'sha256=' + hmac.new(key, stamp.encode() + b'.' + body, hashlib.sha256).hexdigest()
        else:
            key_hex = os.environ.get('WIKI_WEBHOOK_KEY_HEX', '')
            if not re.fullmatch(r'[0-9A-Fa-f]{64,2048}', key_hex) or len(key_hex) % 2:
                raise ValueError('Set WIKI_WEBHOOK_KEY_HEX to a secret key of at least 32 random bytes')
            key = bytes.fromhex(key_hex)
            with args.file.open('rb') as source:
                body = source.read(MAX_BYTES + 1)
            stamp, signature, now = args.timestamp, args.signature, int(time.time())
        valid = verify(body, stamp, signature, key, now)
        print(json.dumps({'signature_valid': valid}))
        return 0 if valid else 2
    except (ValueError, OSError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
