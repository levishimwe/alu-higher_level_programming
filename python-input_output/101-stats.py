#!/usr/bin/python3
"""
This module reads stdin line by line and computes metrics.

It calculates the total file size and counts occurrences of
HTTP status codes. Stats are printed every 10 lines and when
interrupted by CTRL+C.
"""

import sys

def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
    """Parse a line of input and extract size and status code."""
    try:
        parts = line.split()
        size = int(parts[-1])
        status = int(parts[-2])
        return size, status
    except (ValueError, IndexError):
        return None, None

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        size, status = parse_line(line.strip())
        if size is not None:
            total_size += size
        if status in status_codes:
            status_codes[status] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)
