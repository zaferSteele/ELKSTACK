#!/usr/bin/env python3

"""
Script: elastic_query_kibana.py
Purpose: 
    This script connects to an Elasticsearch instance and queries all indices 
    that match the pattern 'kibana*'. It performs a simple 'match_all' query,
    which retrieves all documents from those indices, and prints the total 
    number of documents found.

    It uses the official Python Elasticsearch client, which is designed as a thin 
    wrapper around Elasticsearch’s RESTful API to allow for maximum flexibility.

Usage:
    Make sure the Elasticsearch instance is accessible at the provided host.
    This script uses HTTP Basic Authentication embedded in the URL.
"""

# Import the Elasticsearch client library
from elasticsearch import Elasticsearch

# Initialize Elasticsearch client connection
# The connection string contains the username and password
es_host = Elasticsearch(
    ["https://elastic:-Rel0twWMUk8L-ZtZr=I@192.168.355.4:9200/"], # example
    ca_certs=False,        # SSL certificate file is not provided
    verify_certs=False     # Skip verification of SSL certificates 
)

# Execute a search query on all indices whose names start with "kibana"
# The 'match_all' query returns every document in the index
res = es_host.search(
    index="kibana*",                    # Index name pattern
    body={"query": {"match_all": {}}}   # Query to return all docs
)

# Output the number of documents returned by the search
# This value is nested under 'hits' → 'total' → 'value'
print("Hits Total: " + str(res['hits']['total']['value']))
