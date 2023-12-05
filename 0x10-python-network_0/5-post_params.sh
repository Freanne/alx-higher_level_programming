#!/bin/bash

# Check if the number of arguments is correct
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url=$1

# Define the POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with the specified parameters and display the body of the response
curl -s -X POST -d "email=$email&subject=$subject" "$url"
