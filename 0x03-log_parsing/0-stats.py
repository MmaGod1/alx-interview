#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys
import re


count_line = 0
add_file_size = 0
status_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

log_pattern = re.compile(r'^(?P<ip>[\d\.]+) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1\.1" (?P<status>\d{3}) (?P<size>\d+)$')

try:
    for line in sys.stdin:
        line = line.strip()
        match = log_pattern.match(line)
        
        if match:
            status = match.group('status')
            file_size = int(match.group('size'))

            count_line += 1
            add_file_size += file_size

            if status in status_count:
                status_count[status] += 1

            # Print metrics every 10 lines
            if count_line % 10 == 0:
                print(f"File size: {add_file_size}")
                for code in sorted(status_count.keys()):
                    if status_count[code] > 0:
                        print(f"{code}: {status_count[code]}")

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {add_file_size}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")
