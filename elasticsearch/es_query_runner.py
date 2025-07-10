"""
This script connects to an Elasticsearch instance, loads a JSON-formatted search query from a file,
executes the query on a specified index, and prints the total number of matching documents.

Requirements:

install the elasticsearch client using the command "pip install elasticsearch"


Usage (example):
    python es_query_runner.py --index my_index --query query.json
    python es_query_runner.py -i query_body_1.json -i "cisco*"
    python es_query_runner.py -i query_body_1.json -i "filebeat*"

"""


import json  # Allows reading and parsing JSON data (used for the query file)
import argparse  # Helps handle command-line arguments like --index and --query
from elasticsearch import Elasticsearch  # Imports Elasticsearch client for Python

# Set up argument parser with a description
parser = argparse.ArgumentParser(description='Elasticsearch Query Options')

# Add required argument: index name to search
parser.add_argument("-i", "--index", help="index to query")

# Add required argument: path to a JSON query file
parser.add_argument("-q", "--query", help="query file")

# Parse the arguments from the command line
args = parser.parse_args()

# Get the query file path from parsed arguments
query_file = args.query

# Open and read the JSON query file
with open(query_file) as f:
    query_body = json.loads(f.read())  # Convert file content into Python dictionary

# Create a connection to Elasticsearch server
# Replace <pass> with your actual password; `verify_certs=False` disables SSL verification (not safe for production)
es_host = Elasticsearch(["https://elastic:<password>@192.168.255.5:9200/"], ca_certs=None, verify_certs=False)

# Get the index name from parsed arguments
index = args.index

# Send a search request to Elasticsearch using the index and the query body
res = es_host.search(index=index, body=query_body)

# Print the number of documents matched by the query
print(res['hits']['total']['value'])
