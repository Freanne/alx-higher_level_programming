#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a GET request and store the response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Check if the response status code is 200
if [ "$response" -eq 200 ]; then
    # If the status code is 200, display the body of the response
    curl -s "$url"
fi
