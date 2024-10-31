#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import signal


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def handle_interrupt(signum, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        parts = line.split()
        
        if len(parts) < 9 or parts[5] != '"GET' or parts[6] != '/projects/260' or parts[7] != 'HTTP/1.1"':
            continue

        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
