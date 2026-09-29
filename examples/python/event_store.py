#!/usr/bin/env python3
"""Store one event once in SQLite, with a composite device and event identity."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import sys

MAX_BYTES = 16_384
DEMO = b'{"device_id":"door01","event_id":"evt001","state":"closed"}'

def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('Duplicate JSON key')
        result[key] = value
    return result

def reject_constant(value):
    raise ValueError('Nonstandard JSON number')

def connect(path: str = ':memory:') -> sqlite3.Connection:
    conn = sqlite3.connect(path, timeout=5)
    conn.execute('PRAGMA trusted_schema=OFF')
    conn.execute("""CREATE TABLE IF NOT EXISTS events (
        device_id TEXT NOT NULL, event_id TEXT NOT NULL,
        payload TEXT NOT NULL, digest TEXT NOT NULL,
        PRIMARY KEY (device_id, event_id))""")
    conn.commit()
    return conn

def store(conn: sqlite3.Connection, data: bytes) -> bool:
    if len(data) > MAX_BYTES:
        raise ValueError('Event exceeds 16 KiB')
    obj = json.loads(data.decode('utf-8'), object_pairs_hook=unique, parse_constant=reject_constant)
    if not isinstance(obj, dict) or set(obj) != {'device_id', 'event_id', 'state'}:
        raise ValueError('Expected device_id, event_id and state')
    for key in ('device_id', 'event_id'):
        if not isinstance(obj[key], str) or not re.fullmatch(r'[A-Za-z0-9_]{1,64}', obj[key]):
            raise ValueError(f'Invalid {key}')
    if obj['state'] not in ('open', 'closed', 'unknown'):
        raise ValueError('Unknown state')
    payload = json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True)
    digest = hashlib.sha256(payload.encode('utf-8')).hexdigest()
    # The insert and collision check share one transaction. This does not make
    # a later network call or physical action part of that transaction.
    with conn:
        cursor = conn.execute('INSERT INTO events VALUES (?, ?, ?, ?) ON CONFLICT(device_id, event_id) DO NOTHING',
                              (obj['device_id'], obj['event_id'], payload, digest))
        if cursor.rowcount == 1:
            return True
        stored = conn.execute('SELECT digest FROM events WHERE device_id=? AND event_id=?',
                              (obj['device_id'], obj['event_id'])).fetchone()
        if stored is None or stored[0] != digest:
            raise ValueError('Event identity was reused with a different payload')
        return False

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--file', type=Path)
    parser.add_argument('--database', type=Path, help='Local SQLite database; created when missing')
    args = parser.parse_args()
    if not args.demo and not args.database:
        parser.error('--database is required with --file')
    conn = None
    try:
        conn = connect(':memory:' if args.demo else str(args.database))
        if args.demo:
            print(json.dumps({'first_insert': store(conn, DEMO), 'duplicate_insert': store(conn, DEMO)}))
        else:
            with args.file.open('rb') as source:
                data = source.read(MAX_BYTES + 1)
            print(json.dumps({'inserted': store(conn, data)}))
        return 0
    except (ValueError, OSError, sqlite3.Error, RecursionError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    raise SystemExit(main())
