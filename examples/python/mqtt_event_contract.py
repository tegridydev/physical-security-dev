#!/usr/bin/env python3
"""Validate a topic and JSON payload offline. This example does not connect to MQTT."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 16_384
TOKEN = re.compile(r'[A-Za-z0-9_]{1,64}\Z')
STAMP = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)\Z')
DEMO_TOPIC = 'sites/demo/devices/door01/events'
DEMO = b'{"schema_version":1,"event_id":"evt001","site_id":"demo","device_id":"door01","occurred_at":"2026-09-10T09:00:00+10:00","kind":"door_state","state":"closed"}'

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON field')
        result[key] = value
    return result

def reject_constant(value):
    raise ValueError('Nonstandard JSON number')

def validate(topic: str, data: bytes) -> dict[str, object]:
    if len(data) > MAX_BYTES:
        raise ValueError('Payload exceeds 16 KiB')
    parts = topic.split('/')
    if len(parts) != 5 or parts[0] != 'sites' or parts[2] != 'devices' or parts[4] != 'events':
        raise ValueError('Expected sites/{site}/devices/{device}/events')
    obj = json.loads(data.decode('utf-8'), object_pairs_hook=unique, parse_constant=reject_constant)
    fields = {'schema_version', 'event_id', 'site_id', 'device_id', 'occurred_at', 'kind', 'state'}
    if not isinstance(obj, dict) or set(obj) != fields:
        raise ValueError('Missing or unknown event fields')
    if type(obj['schema_version']) is not int or obj['schema_version'] != 1:
        raise ValueError('Unsupported schema version')
    for name in ('event_id', 'site_id', 'device_id'):
        if not isinstance(obj[name], str) or not TOKEN.fullmatch(obj[name]):
            raise ValueError(f'Invalid {name}')
    if obj['site_id'] != parts[1] or obj['device_id'] != parts[3]:
        raise ValueError('Topic and payload identities do not match')
    if obj['kind'] != 'door_state' or obj['state'] not in ('open', 'closed', 'unknown'):
        raise ValueError('Unknown event kind or state')
    stamp = obj['occurred_at']
    if not isinstance(stamp, str) or not STAMP.fullmatch(stamp) or stamp.endswith('-00:00'):
        raise ValueError('A timestamp with a known UTC offset is required')
    try:
        obj['occurred_at'] = datetime.fromisoformat(stamp.replace('Z', '+00:00')).astimezone(timezone.utc).isoformat().replace('+00:00', 'Z')
    except OverflowError as exc:
        raise ValueError('Timestamp is outside the supported UTC range') from exc
    return obj

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--file', type=Path, help='UTF8 JSON payload')
    parser.add_argument('--topic', help='Exact published topic, not a subscription filter')
    args = parser.parse_args()
    if not args.demo and not args.topic:
        parser.error('--topic is required with --file')
    try:
        if args.demo:
            data, topic = DEMO, DEMO_TOPIC
        else:
            with args.file.open('rb') as stream:
                data = stream.read(MAX_BYTES + 1)
            topic = args.topic
        print(json.dumps(validate(topic, data), sort_keys=True))
        return 0
    except (OSError, ValueError, RecursionError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
