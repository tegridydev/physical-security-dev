#!/usr/bin/env python3
"""Run the offline Python examples from one small menu."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = (
    ("HTTPS JSON read", "examples/python/https_json.py"),
    ("ONVIF device information", "examples/python/onvif_device_info.py"),
    ("MQTT event validation", "examples/python/mqtt_event_contract.py"),
    ("Modbus register read", "examples/python/modbus_read.py"),
    ("RTSP and SDP inspection", "examples/python/rtsp_sdp.py"),
    ("Event trace normalisation", "examples/python/trace_events.py"),
    ("Video storage calculator", "examples/python/video_storage.py"),
    ("TLS certificate expiry check", "examples/python/tls_expiry.py"),
    ("SQLite event deduplication", "examples/python/event_store.py"),
    ("Webhook signature verification", "examples/python/webhook_hmac.py"),
)


def run_example(index: int, *, quiet: bool = False) -> bool:
    title, relative = EXAMPLES[index]
    source = ROOT / relative
    try:
        result = subprocess.run(
            [sys.executable, str(source), "--demo"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        if not quiet:
            print(f"{title}: failed: {exc}", file=sys.stderr)
        return False

    if result.returncode != 0:
        if not quiet:
            print(f"{title}: failed", file=sys.stderr)
            if result.stderr.strip():
                print(result.stderr.strip(), file=sys.stderr)
        return False

    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        if not quiet:
            print(f"{title}: demo returned invalid JSON", file=sys.stderr)
        return False

    if not isinstance(payload, dict):
        if not quiet:
            print(f"{title}: demo returned an unexpected value", file=sys.stderr)
        return False

    if quiet:
        return True

    print(f"\n{title}")
    print(json.dumps(payload, indent=2, sort_keys=True))
    return True


def run_all(*, quiet: bool = False) -> int:
    failures = []
    for index, (title, _) in enumerate(EXAMPLES):
        ok = run_example(index, quiet=quiet)
        if quiet:
            print(f"{'PASS' if ok else 'FAIL'}  {title}")
        if not ok:
            failures.append(title)
    if failures:
        print(f"\n{len(failures)} example(s) failed.", file=sys.stderr)
        return 1
    if quiet:
        print(f"\n{len(EXAMPLES)} examples passed.")
    return 0


def interactive() -> int:
    while True:
        print("\nSecurity Technician Wiki examples\n")
        for number, (title, _) in enumerate(EXAMPLES, start=1):
            print(f"{number:>2}. {title}")
        print(" A. Run all")
        print(" Q. Quit")
        try:
            choice = input("\nChoose an example: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
        if choice in {"q", "quit", "exit"}:
            return 0
        if choice in {"a", "all"}:
            return run_all()
        try:
            index = int(choice) - 1
        except ValueError:
            print("Choose a number, A or Q.")
            continue
        if not 0 <= index < len(EXAMPLES):
            print("Choose a number shown in the menu.")
            continue
        run_example(index)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--all", action="store_true", help="Run every offline Python demo.")
    group.add_argument("--test", action="store_true", help="Run every demo and validate its JSON output.")
    args = parser.parse_args(argv)
    if args.all:
        return run_all()
    if args.test:
        return run_all(quiet=True)
    return interactive()


if __name__ == "__main__":
    raise SystemExit(main())
