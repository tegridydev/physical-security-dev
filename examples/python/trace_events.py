#!/usr/bin/env python3
"""Normalise a bounded JSONL event trace to UTC without connecting to equipment."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import re
import sys
from typing import BinaryIO, Iterator

MAX_LINE = 16_384
MAX_TOTAL = 8 * 1024 * 1024
MAX_ROWS = 10_000
STAMP = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)\Z')
DEMO = b'{"event_id":"evt001","device_id":"door01","occurred_at":"2026-09-10T09:00:00+10:00","state":"closed"}\n'

def utc(value: object) -> str:
    if not isinstance(value, str) or not STAMP.fullmatch(value) or value.endswith('-00:00'):
        raise ValueError('Timestamp requires a known numeric offset or Z')
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(timezone.utc).isoformat().replace('+00:00', 'Z')
    except OverflowError as exc:
        raise ValueError('Timestamp is outside the supported UTC range') from exc

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result

def reject_constant(value):
    raise ValueError('Nonstandard JSON constant')

def normalise(stream: BinaryIO) -> Iterator[dict[str, str]]:
    total = 0
    for row in range(1, MAX_ROWS + 2):
        line = stream.readline(MAX_LINE + 1)
        if not line:
            return
        total += len(line)
        if len(line) > MAX_LINE or total > MAX_TOTAL or row > MAX_ROWS:
            raise ValueError(f'Input limit exceeded at line {row}')
        if not line.strip():
            raise ValueError(f'Blank line at {row}')
        obj = json.loads(line.decode('utf-8'), object_pairs_hook=unique, parse_constant=reject_constant)
        fields = {'event_id', 'device_id', 'occurred_at', 'state'}
        if not isinstance(obj, dict) or set(obj) != fields:
            raise ValueError(f'Invalid event fields at line {row}')
        for key in ('event_id', 'device_id'):
            if not isinstance(obj[key], str) or not re.fullmatch(r'[A-Za-z0-9_]{1,64}', obj[key]):
                raise ValueError(f'Invalid {key} at line {row}')
        if obj['state'] not in ('open', 'closed', 'unknown'):
            raise ValueError(f'Unknown state at line {row}')
        obj['occurred_at'] = utc(obj['occurred_at'])
        yield obj

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--file', type=Path)
    args = parser.parse_args()
    try:
        with (io.BytesIO(DEMO) if args.demo else args.file.open('rb')) as stream:
            # Validate the bounded input completely before writing any output.
            rows = list(normalise(stream))
        for row in rows:
            print(json.dumps(row, sort_keys=True))
        return 0
    except (OSError, ValueError, RecursionError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
