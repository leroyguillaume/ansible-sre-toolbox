#!/bin/python3

import json
import re
import subprocess
import sys

header_regex = re.compile(r"^([a-z]+)(\(([a-z]{2})\))?")
process = subprocess.Popen(
    ["qm"] + sys.argv[1:],
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
    header_line = lines[0]
    header_line_split = re.split(r"\s+", header_line)
    for header in header_line_split[1:-1]:
        matcher = header_regex.match(header.lower())
        if matcher.group(2) is None:
            header = matcher.group(1)
        else:
            header = matcher.group(1) + "_" + matcher.group(3)
        headers.append(header)
    for row in range(1, len(lines)):
        line_split = re.split(r"\s+", lines[row])
        row_data = {}
        for column in range(0, len(headers)):
            row_data[headers[column]] = line_split[column + 1].strip()
        data.append(row_data)
print(json.dumps(data))
