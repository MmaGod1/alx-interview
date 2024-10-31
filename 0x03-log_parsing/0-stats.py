#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys
import signal
import re


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
pattern = re.compile(
    r'^\d{1,3}(\.\d{1,3}){3} - \S+ \S+ "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'
)

def print_stats():
    """Prints the accumulated file size and status code counts."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_interrupt(signum, frame):
    """Handles keyboard interrupt and prints final stats."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        match = pattern.match(line)
        if not match:
            continue

        status_code = int(match.group(2))
        file_size = int(match.group(3))

        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
