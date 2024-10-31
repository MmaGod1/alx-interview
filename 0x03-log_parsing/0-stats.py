#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''

import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split()
        
        # Validate line format before processing
        if len(line_list) < 9 or line_list[5] != '"GET' or line_list[6] != '/projects/260' or line_list[7] != 'HTTP/1.1"':
            continue
        
        # Process status code and file size if format is valid
        code = line_list[-2]
        try:
            size = int(line_list[-1])
        except ValueError:
            continue
        
        if code in cache:
            cache[code] += 1
        total_size += size
        counter += 1

        # Print statistics every 10 lines
        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass

finally:
    # Final output of statistics
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
