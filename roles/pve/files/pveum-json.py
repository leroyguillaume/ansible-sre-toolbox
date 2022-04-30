#!/bin/python3

import json
import subprocess
import sys

process = subprocess.Popen(
    ["pveum"] + sys.argv[1:],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
(stdout, stderr) = process.communicate()
if process.returncode != 0:
    print(stderr.decode("utf-8"), file=sys.stderr, end="")
    exit(process.returncode)
data = []
lines = stdout.decode("utf-8").splitlines()
if len(lines) > 0:
    headers = []
    header_line = lines[1]
    header_line_split = header_line.split("│")
    for header in header_line_split[1:-1]:
        headers.append(header.strip())
    for row in range(3, len(lines), 2):
        line_split = lines[row].split("│")
        row_data = {}
        for column in range(0, len(headers)):
            row_data[headers[column]] = line_split[column + 1].strip()
        data.append(row_data)
print(json.dumps(data))
