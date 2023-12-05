#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Use curl to send an OPTIONS request and display the Allow header from the response
curl -sI -X OPTIONS "$url" | grep -i "Allow" | awk '{print $2}'
