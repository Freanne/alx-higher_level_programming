#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request with the specified header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$url"
