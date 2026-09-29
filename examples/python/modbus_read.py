#!/usr/bin/env python3
"""Read holding or input registers from one explicitly supplied Modbus TCP endpoint."""
from __future__ import annotations
import argparse
import json
import secrets
import socket
import struct
import sys
import time

class ModbusException(ValueError):
    """The server returned a Modbus exception response."""

def request(transaction: int, unit: int, function: int, address: int, count: int) -> bytes:
    values = (transaction, unit, function, address, count)
    if any(type(v) is not int for v in values):
        raise ValueError('Request fields must be integers')
    if not 0 <= transaction <= 65535 or not 1 <= unit <= 247:
        raise ValueError('Transaction must be 0 to 65535 and unit must be 1 to 247')
    if function not in (3, 4) or not 0 <= address <= 65535 or not 1 <= count <= 125 or address + count > 65536:
        raise ValueError('Use function 3 or 4 and a valid register span of at most 125')
    return struct.pack('>HHHBBHH', transaction, 0, 6, unit, function, address, count)

def parse_response(data: bytes, transaction: int, unit: int, function: int, count: int) -> list[int]:
    if len(data) < 9 or len(data) > 260:
        raise ValueError('Invalid Modbus TCP frame size')
    tid, protocol, length, returned_unit = struct.unpack('>HHHB', data[:7])
    if tid != transaction or protocol != 0 or returned_unit != unit or length != len(data) - 6:
        raise ValueError('Response header does not match the request')
    pdu = data[7:]
    if pdu[0] == function | 0x80:
        if len(pdu) != 2:
            raise ValueError('Malformed exception response')
        raise ModbusException(f'Modbus exception code {pdu[1]}')
    if pdu[0] != function or pdu[1] != count * 2 or len(pdu) != count * 2 + 2:
        raise ValueError('Unexpected function or register byte count')
    return list(struct.unpack('>' + 'H' * count, pdu[2:]))

def receive_exact(sock: socket.socket, size: int, deadline: float) -> bytes:
    result = bytearray()
    while len(result) < size:
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise TimeoutError('Modbus response deadline exceeded')
        sock.settimeout(remaining)
        chunk = sock.recv(size - len(result))
        if not chunk:
            raise ValueError('Connection closed during response')
        result.extend(chunk)
    return bytes(result)

def read_registers(host: str, port: int, unit: int, function: int, address: int, count: int) -> list[int]:
    if not host or not 1 <= port <= 65535:
        raise ValueError('Supply a host and a valid TCP port')
    transaction = secrets.randbelow(65536)
    frame = request(transaction, unit, function, address, count)
    with socket.create_connection((host, port), timeout=5) as sock:
        sock.sendall(frame)
        deadline = time.monotonic() + 5
        header = receive_exact(sock, 7, deadline)
        length = struct.unpack('>H', header[4:6])[0]
        if not 3 <= length <= 254:
            raise ValueError('Invalid MBAP length')
        data = header + receive_exact(sock, length - 1, deadline)
    return parse_response(data, transaction, unit, function, count)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--host', help='Authorised device or loopback simulator; never a subnet')
    parser.add_argument('--port', type=int, default=502)
    parser.add_argument('--unit', type=int, default=1)
    parser.add_argument('--function', type=int, choices=(3, 4), default=3)
    parser.add_argument('--address', type=int, default=0, help='Zero based register address')
    parser.add_argument('--count', type=int, default=2)
    args = parser.parse_args()
    try:
        values = parse_response(bytes.fromhex('000100000007010304000a0014'), 1, 1, 3, 2) if args.demo else read_registers(
            args.host, args.port, args.unit, args.function, args.address, args.count)
        print(json.dumps({'registers': values}))
        return 0
    except (OSError, ValueError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
