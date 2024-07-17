#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def parse_line(line):
    try:
        parts = line.split()
        size = int(parts[-1])
        status = parts[-2]
        return size, status
    except:
        return None, None

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        size, status = parse_line(line.strip())
        if size is not None and status is not None:
            total_size += size
            if int(status) in status_codes:
                status_codes[int(status)] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)

print_stats(total_size, status_codes)
