#!/usr/bin/python3
'''Script to read lines from standard input and compute metrics'''

import sys

# Dictionary to store counts of different HTTP status codes
status_tracker = {'200': 0, '301': 0, '400': 0, '401': 0,
                  '403': 0, '404': 0, '405': 0, '500': 0}
size_total = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_parts = line.split()
        
        # Validate line structure based on expected length and pattern
        if len(line_parts) > 4:
            status_code = line_parts[-2]
            try:
                file_size = int(line_parts[-1])
            except ValueError:
                continue
            
            # Update counts if status code is tracked
            if status_code in status_tracker:
                status_tracker[status_code] += 1
            size_total += file_size
            line_counter += 1

        # Output metrics every 10 lines
        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(size_total))
            for code, count in sorted(status_tracker.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    pass

finally:
    # Final metrics printout
    print('File size: {}'.format(size_total))
    for code, count in sorted(status_tracker.items()):
        if count != 0:
            print('{}: {}'.format(code, count))
