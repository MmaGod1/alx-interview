#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
import sys


cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

def print_metrics(total_size, cache):
    """Print total file size and status code counts."""
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

try:
    for line in sys.stdin:
        if line.strip():  # Skip empty lines
            line_list = line.split()
            if len(line_list) < 9:
                continue

            # Extract status code and file size
            try:
                code = line_list[-2]
                size = int(line_list[-1])
            except (ValueError, IndexError):
                continue

            # Update metrics
            if code in cache:
                cache[code] += 1
            total_size += size
            counter += 1

            # Print metrics every 10 lines
            if counter == 10:
                print_metrics(total_size, cache)
                counter = 0

except KeyboardInterrupt:
    pass

finally:
    print_metrics(total_size, cache)
