#!/usr/bin/env python3
import json
import sys

# Read the JSON data from stdin
report_data = json.load(sys.stdin)

# Print the entire JSON data for inspection
print("Complete JSON Data:", report_data)

# Count the number of vulnerabilities
# vulnerability_count = len(report_data.get("VulnerabilityID", []))
 vulnerability_count = len(report_data['VulnerabilityID'])

# Print the vulnerability count
print("Vulnerability count:", vulnerability_count)
