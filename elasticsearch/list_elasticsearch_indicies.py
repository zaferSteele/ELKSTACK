# This script connects to an Elasticsearch server, queries for all index names starting with a given prefix (e.g., 'kibana'),
# and prints the list of matching index names. It disables HTTPS certificate verification warnings and uses basic authentication.

#!/usr/bin/env python3

# Import the requests library for making HTTP requests
import requests
# Import warning class to suppress insecure HTTPS warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Disable warning for unverified HTTPS requests (not recommended for production)
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def current_indices_list(es_host, index_prefix):
    # Initialize an empty list to store matching index names
    current_indices = []

    # Set the HTTP headers to indicate we're sending/expecting JSON
    http_header = {'content-type': 'application/json'}

    # Make a GET request to Elasticsearch's _cat API to list indices starting with prefix
    response = requests.get(es_host + "/_cat/indices/" + index_prefix + "*", headers=http_header, verify=False)

    # Split the response text by newlines to process each index line separately
    for line in response.text.split('\n'):
        if line:  # Skip empty lines
            # The 3rd word (index 2) in each line is the index name
            current_indices.append(line.split()[2])

    # Return the list of matching index names
    return current_indices

# This block runs only if the script is executed directly (not when imported)
if __name__ == "__main__":
    # Set Elasticsearch username and password
    username = ''
    password = '' #

    # Construct the full Elasticsearch URL with basic authentication
    es_host = 'https://' + username + ':' + password + '@<ip_address_and_port_number>' #eg 192.168.255.3:9200

    # Call the function to get indices starting with "kibana"
    indices_list = current_indices_list(es_host, 'kibana')

    # Print the list of matching indices
    print(indices_list)
