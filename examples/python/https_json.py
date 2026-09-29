#!/usr/bin/env python3
"""Read a bounded HTTPS health response. Run with --demo before using a device."""
from __future__ import annotations
import argparse
import http.client
import json
import math
import os
import ssl
import sys
from urllib.parse import urlsplit

MAX_BYTES = 65_536

def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result

def reject_constant(value: str) -> None:
    raise ValueError(f"Invalid JSON constant: {value}")

def parse_health(data: bytes) -> dict[str, object]:
    if len(data) > MAX_BYTES:
        raise ValueError("Response exceeds 64 KiB")
    obj = json.loads(data.decode('utf-8'), object_pairs_hook=unique_object,
                     parse_constant=reject_constant)
    if not isinstance(obj, dict) or obj.get('status') not in ('healthy', 'degraded'):
        raise ValueError("Expected an object with status healthy or degraded")
    uptime = obj.get('uptime_seconds')
    if uptime is not None and (type(uptime) is not int or uptime < 0):
        raise ValueError("uptime_seconds must be a nonnegative integer")
    # Print only fields in this example's contract, never unknown device data.
    return {key: obj[key] for key in ('status', 'uptime_seconds') if key in obj}

def read_health(url: str, *, ca: str | None = None,
                token: str | None = None, timeout: float = 5.0) -> dict[str, object]:
    if not math.isfinite(timeout) or not 0 < timeout <= 30:
        raise ValueError("Timeout must be greater than zero and at most 30 seconds")
    if any(ord(c) <= 32 or ord(c) == 127 for c in url):
        raise ValueError("URL contains whitespace or control characters")
    target = urlsplit(url)
    if target.scheme != 'https' or not target.hostname or target.username or target.password or target.fragment:
        raise ValueError("Use an HTTPS URL without credentials or a fragment")
    if token and (len(token) > 4096 or any(ord(c) < 33 or ord(c) > 126 for c in token)):
        raise ValueError("Token must contain printable ASCII without whitespace")
    context = ssl.create_default_context(cafile=ca)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    headers = {'Accept': 'application/json', 'Accept-Encoding': 'identity'}
    if token:
        headers['Authorization'] = 'Bearer ' + token
    path = target.path or '/'
    if target.query:
        path += '?' + target.query
    # HTTPSConnection does not inherit proxy settings or follow redirects.
    conn = http.client.HTTPSConnection(target.hostname, target.port or 443,
                                      timeout=timeout, context=context)
    try:
        conn.request('GET', path, headers=headers)
        with conn.getresponse() as response:
            if response.status != 200:
                raise ValueError(f"Expected HTTP 200, received {response.status}")
            kind = response.getheader('Content-Type', '').split(';', 1)[0].strip().lower()
            if kind != 'application/json':
                raise ValueError("Expected application/json")
            if response.getheader('Content-Encoding', 'identity').lower() != 'identity':
                raise ValueError("Compressed responses are not accepted")
            return parse_health(response.read(MAX_BYTES + 1))
    finally:
        conn.close()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true', help='Validate a built in response without networking')
    mode.add_argument('--url', help='Exact HTTPS health endpoint; no discovery is performed')
    parser.add_argument('--ca', help='PEM trust bundle for a private certificate authority')
    parser.add_argument('--timeout', type=float, default=5, help='Socket I/O timeout in seconds, maximum 30')
    args = parser.parse_args()
    try:
        result = parse_health(b'{"status":"healthy","uptime_seconds":3600}') if args.demo else read_health(
            args.url, ca=args.ca, token=os.environ.get('WIKI_API_TOKEN'), timeout=args.timeout)
        print(json.dumps(result, sort_keys=True))
        return 0
    except (OSError, ValueError, http.client.HTTPException, RecursionError) as exc:
        print(f"Error: {type(exc).__name__}. Check the endpoint, trust bundle and response contract.", file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
