#!/usr/bin/python3
import sys
"""Reads stdin line by line and computes metrics"""


count_line = 0
add_file_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0,
                403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        line = line.strip()
        line_str = line.split()
        
        if len(line_str) > 7:
            status = int(line_str[6])
            file_size = int(line_str[7])

            count_line += 1
            add_file_size += file_size

            if status in status_count:
                status_count[status] += 1

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
