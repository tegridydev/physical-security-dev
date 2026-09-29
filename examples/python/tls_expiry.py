#!/usr/bin/env python3
"""Check the validated peer certificate on one TLS service."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
import socket
import ssl
import sys
import time

def certificate_days(cert: dict, now: float) -> int:
    if 'notAfter' not in cert or 'notBefore' not in cert:
        raise ValueError('Certificate validity dates are missing')
    start = ssl.cert_time_to_seconds(cert['notBefore'])
    end = ssl.cert_time_to_seconds(cert['notAfter'])
    if end <= start or not start <= now < end:
        raise ValueError('Certificate is not currently valid')
    return int((end - now) // 86400)

def check(host: str, port: int = 443, ca: str | None = None) -> dict:
    if not host or any(c.isspace() for c in host) or '/' in host or not 1 <= port <= 65535:
        raise ValueError('Supply a hostname without a scheme or path and a valid port')
    context = ssl.create_default_context(cafile=ca)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    with socket.create_connection((host, port), timeout=5) as plain:
        with context.wrap_socket(plain, server_hostname=host) as secure:
            cert = secure.getpeercert()
            return {'host': host, 'days_remaining': certificate_days(cert, time.time()),
                    'expires_utc': datetime.fromtimestamp(ssl.cert_time_to_seconds(cert['notAfter']), timezone.utc).isoformat(),
                    'tls_version': secure.version()}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--host')
    parser.add_argument('--port', type=int, default=443)
    parser.add_argument('--ca', help='PEM certificate authority bundle')
    parser.add_argument('--warn-days', type=int, default=30)
    args = parser.parse_args()
    if not 0 <= args.warn_days <= 3650:
        parser.error('--warn-days must be 0 to 3650')
    try:
        if args.demo:
            cert = {'notBefore': 'Jan  1 00:00:00 2026 GMT', 'notAfter': 'Oct 10 00:00:00 2026 GMT'}
            result = {'days_remaining': certificate_days(cert, datetime(2026, 9, 10, tzinfo=timezone.utc).timestamp())}
        else:
            result = check(args.host, args.port, args.ca)
        result['renewal_due'] = result['days_remaining'] <= args.warn_days
        print(json.dumps(result, sort_keys=True))
        return 2 if result['renewal_due'] and not args.demo else 0
    except (ValueError, OSError) as exc:
        print(f'Error: {type(exc).__name__}. Certificate validation or connection failed.', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
