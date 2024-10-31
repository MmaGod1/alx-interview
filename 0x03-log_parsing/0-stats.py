#!/usr/bin/python3
"""Read lines from standard input and compute metrics"""
import sys


status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) != 9 or parts[5] != '"GET' or parts[6] != '/projects/260' or parts[7] != 'HTTP/1.1"':
            continue
        
        # Extract the status code and file size
        status_code = parts[-2]
        try:
            file_size = int(parts[-1])
        except ValueError:
            continue
        
        # Updates metrics if status code is valid
        if status_code in status_counts:
            status_counts[status_code] += 1
        total_file_size += file_size
        line_counter += 1

        # Prints metrics every 10 lines
        if line_counter == 10:
            line_counter = 0
            print('Total file size: File size: {}'.format(total_file_size))
            for code in sorted(status_counts.keys()):
                if status_counts[code] > 0:
                    print('{}: {}'.format(code, status_counts[code]))

except KeyboardInterrupt:
    pass

finally:
    print('Total file size: File size: {}'.format(total_file_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print('{}: {}'.format(code, status_counts[code]))
