#!/usr/bin/env python3
import json
import sys

# Read the JSON data from stdin
report_data = json.load(sys.stdin)

# Count the number of vulnerabilities
vulnerability_count = len(report_data["Vulnerabilities"])

# Print the vulnerability count
print(vulnerability_count)
