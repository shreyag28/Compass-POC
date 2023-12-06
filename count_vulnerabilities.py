#!/usr/bin/env python3
import json
import sys

try:
    # Read the JSON data from stdin
    report_data = json.load(sys.stdin)

    # Initialize a counter for 'VulnerabilityID' occurrences
    vulnerability_id_count = 0

    # Function to recursively count occurrences of 'VulnerabilityID'
    def count_vulnerability_id(obj):
        global vulnerability_id_count
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'VulnerabilityID':
                    vulnerability_id_count += 1
                else:
                    count_vulnerability_id(value)
        elif isinstance(obj, list):
            for item in obj:
                count_vulnerability_id(item)

    # Call the function to count occurrences
    count_vulnerability_id(report_data)

    # Print the total count of 'VulnerabilityID' occurrences
    print(vulnerability_id_count)

except Exception as e:
    # Print an error message if there's an exception during script execution
    print("Error:", str(e))
