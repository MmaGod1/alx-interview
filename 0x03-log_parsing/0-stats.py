#!/usr/bin/python3
"""Reads stdin line by line and computes metrics"""
import sys

count_line = 0
add_file_size = 0
status_count = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}

try:
    for line in sys.stdin:
        line = line.strip()
        line_parts = line.split(" ")
        if len(line_parts) >= 5:
            try:
                status = line_parts[-2]
                file_size = int(line_parts[-1])

                if status in status_count:
                    status_count[status] += 1
                add_file_size += file_size
                count_line += 1

                if count_line % 10 == 0:
                    print(f"File size: {add_file_size}")
                    for code in sorted(status_count.keys()):
                        if status_count[code] > 0:
                            print(f"{code}: {status_count[code]}")

            except (ValueError, IndexError):
                # Skip lines that can't be processed correctly
                continue

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {add_file_size}")
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")
