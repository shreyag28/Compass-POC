#!/usr/bin/env python3
import json
import sys

# Read the JSON data from stdin
report_data = json.load(sys.stdin)

# Print the entire JSON data for inspection
#print("Complete JSON Data:", report_data)

# Count the number of vulnerabilities
# vulnerability_count = len(report_data.get("VulnerabilityID", []))
# vulnerability_count = len(report_data['VulnerabilityID'])

if 'VulnerabilityID' in report_data:
    # Extract the list of vulnerabilities
    vulnerabilities = report_data['VulnerabilityID']

    # Count the occurrences of 'VulnerabilityID' in the list
    vulnerability_count = sum(1 for vulnerability in vulnerabilities if 'VulnerabilityID' in vulnerability)
    # Print the vulnerability count
    print("Vulnerability count:", vulnerability_count)




