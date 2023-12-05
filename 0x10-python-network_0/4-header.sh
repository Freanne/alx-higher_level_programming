#!/bin/bash
# Get the URL from the command line argument
url=$1

# Use curl to send a GET request with the specified header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$url"
