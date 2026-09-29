#!/usr/bin/env python3
"""Read ONVIF GetDeviceInformation over HTTPS or parse a built in SOAP response."""
from __future__ import annotations
import argparse
import getpass
import json
import os
import re
import ssl
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from urllib.parse import urlsplit

SOAP = 'http://www.w3.org/2003/05/soap-envelope'
DEVICE = 'http://www.onvif.org/ver10/device/wsdl'
ACTION = DEVICE + '/GetDeviceInformation'
MAX_BYTES = 65_536
REQUEST = (f'<s:Envelope xmlns:s="{SOAP}" xmlns:tds="{DEVICE}">'
           '<s:Body><tds:GetDeviceInformation/></s:Body></s:Envelope>').encode()
DEMO = (f'<s:Envelope xmlns:s="{SOAP}" xmlns:tds="{DEVICE}"><s:Body>'
        '<tds:GetDeviceInformationResponse><tds:Manufacturer>Example</tds:Manufacturer>'
        '<tds:Model>Camera Demo</tds:Model><tds:FirmwareVersion>1.0</tds:FirmwareVersion>'
        '<tds:SerialNumber>DEMO0001</tds:SerialNumber><tds:HardwareId>demo</tds:HardwareId>'
        '</tds:GetDeviceInformationResponse></s:Body></s:Envelope>').encode()

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Redirects are not accepted")

def parse_device_info(data: bytes) -> dict[str, str]:
    if len(data) > MAX_BYTES:
        raise ValueError("SOAP response exceeds 64 KiB")
    # Decode first so alternate encodings cannot hide declaration tokens.
    text = data.decode('utf-8-sig')
    if '\x00' in text or re.search(r'<!\s*(DOCTYPE|ENTITY)\b', text, re.I):
        raise ValueError("Only UTF8 XML without DTD or entity declarations is accepted")
    root = ET.fromstring(text)
    if root.tag != f'{{{SOAP}}}Envelope':
        raise ValueError("Expected a SOAP 1.2 envelope")
    bodies = root.findall(f'{{{SOAP}}}Body')
    if len(bodies) != 1 or len(bodies[0]) != 1:
        raise ValueError("Expected one SOAP body containing one response")
    response = bodies[0][0]
    if response.tag == f'{{{SOAP}}}Fault':
        raise ValueError("The device returned a SOAP fault")
    if response.tag != f'{{{DEVICE}}}GetDeviceInformationResponse':
        raise ValueError("Unexpected ONVIF response")
    result = {}
    for field in ('Manufacturer', 'Model', 'FirmwareVersion', 'SerialNumber', 'HardwareId'):
        nodes = response.findall(f'{{{DEVICE}}}{field}')
        if len(nodes) != 1 or list(nodes[0]):
            raise ValueError(f"Missing, repeated or structured field: {field}")
        value = nodes[0].text or ''
        if len(value) > 512 or any(ord(c) < 32 for c in value):
            raise ValueError("Invalid device information text")
        result[field] = value
    return result

def read_device(url: str, *, ca: str | None = None, username: str | None = None,
                password: str | None = None) -> dict[str, str]:
    target = urlsplit(url)
    if (target.scheme != 'https' or not target.hostname or target.username or target.password
            or target.fragment or any(ord(c) <= 32 or ord(c) == 127 for c in url)):
        raise ValueError("Use an exact HTTPS device service URL without embedded credentials")
    context = ssl.create_default_context(cafile=ca)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    handlers = [urllib.request.ProxyHandler({}), NoRedirect(),
                urllib.request.HTTPSHandler(context=context)]
    if username:
        manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
        manager.add_password(None, url, username, password or '')
        handlers.append(urllib.request.HTTPDigestAuthHandler(manager))
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, REQUEST, method='POST', headers={
        'Content-Type': f'application/soap+xml; charset=utf-8; action="{ACTION}"',
        'Accept': 'application/soap+xml', 'Accept-Encoding': 'identity'})
    with opener.open(req, timeout=5) as response:
        if response.status != 200:
            raise ValueError("Unexpected HTTP status")
        if response.headers.get_content_type() != 'application/soap+xml':
            raise ValueError("Expected application/soap+xml")
        if response.headers.get('Content-Encoding', 'identity').lower() != 'identity':
            raise ValueError("Compressed responses are not accepted")
        return parse_device_info(response.read(MAX_BYTES + 1))

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--demo', action='store_true')
    mode.add_argument('--url', help='Exact HTTPS device service endpoint')
    parser.add_argument('--ca', help='PEM certificate authority bundle')
    parser.add_argument('--username', help='HTTP Digest user; password is prompted or read from WIKI_ONVIF_PASSWORD')
    args = parser.parse_args()
    try:
        password = os.environ.get('WIKI_ONVIF_PASSWORD')
        if args.username and not args.demo and password is None:
            password = getpass.getpass('Device password: ')
        result = parse_device_info(DEMO) if args.demo else read_device(
            args.url, ca=args.ca, username=args.username, password=password)
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (ValueError, OSError, urllib.error.URLError, ET.ParseError, RecursionError) as exc:
        print(f"Error: {type(exc).__name__}. Check the service URL, authentication and certificate.", file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
