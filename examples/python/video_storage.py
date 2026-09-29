#!/usr/bin/env python3
"""Estimate continuous video storage from measured average bitrate."""
from __future__ import annotations
import argparse
from decimal import Decimal, InvalidOperation
import json
import sys

def estimate(cameras: int, mbps: Decimal, days: Decimal,
             overhead: Decimal = Decimal('0'), reserve: Decimal = Decimal('0')) -> dict[str, str]:
    if type(cameras) is not int or not 1 <= cameras <= 100_000:
        raise ValueError('Camera count must be 1 to 100000')
    if any(not x.is_finite() for x in (mbps, days, overhead, reserve)):
        raise ValueError('Inputs must be finite')
    if not 0 < mbps <= 10_000 or not 0 < days <= 3650:
        raise ValueError('Use positive bitrate up to 10000 Mbps and retention up to 3650 days')
    if not 0 <= overhead <= 100 or not 0 <= reserve < 100:
        raise ValueError('Overhead must be 0 to 100 percent; reserve must be less than 100 percent')
    bits_per_second = Decimal(cameras) * mbps * 1_000_000
    recording = bits_per_second * 86400 * days / 8
    stored = recording * (1 + overhead / 100)
    usable = stored / (1 - reserve / 100)
    return {'aggregate_mbps': str(Decimal(cameras) * mbps),
            'recording_tb': format(recording / 10**12, '.3f'),
            'required_usable_tb': format(usable / 10**12, '.3f'),
            'required_usable_tib': format(usable / 2**40, '.3f')}

def decimal_input(value: str) -> Decimal:
    try:
        result = Decimal(value)
        if not result.is_finite():
            raise InvalidOperation
        return result
    except InvalidOperation as exc:
        raise argparse.ArgumentTypeError('Use a finite decimal number') from exc

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--cameras', type=int)
    parser.add_argument('--mbps', type=decimal_input, help='Measured average megabits per second for each camera')
    parser.add_argument('--days', type=decimal_input)
    parser.add_argument('--overhead', type=decimal_input, default=Decimal('0'), help='Additional stored data as a percentage')
    parser.add_argument('--reserve', type=decimal_input, default=Decimal('0'), help='Percentage of usable capacity kept free')
    args = parser.parse_args()
    if not args.demo and None in (args.cameras, args.mbps, args.days):
        parser.error('Supply --cameras, --mbps and --days, or use --demo')
    try:
        result = estimate(8, Decimal('4'), Decimal('30'), Decimal('10'), Decimal('20')) if args.demo else estimate(
            args.cameras, args.mbps, args.days, args.overhead, args.reserve)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, InvalidOperation) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
