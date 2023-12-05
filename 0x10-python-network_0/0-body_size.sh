#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send a request and store the response in a variable
response=$(curl -sI "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}' | tr -d '\r')

# Display the content length in bytes
echo "$content_length"
