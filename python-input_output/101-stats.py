#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

def parse_line(line):
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
    line = line.strip()
    print(f"Debug: Processing line: {line}")  # Debug print
    size, status = parse_line(line)
    print(f"Debug: Parsed size: {size}, status: {status}")  # Debug print
    # ... rest of the code
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)
except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_codes)
