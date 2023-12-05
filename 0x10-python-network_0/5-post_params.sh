#!/bin/bash
# Get the URL from the command line argument
url=$1

# Define the POST parameters
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request with the specified parameters and display the body of the response
curl -X POST "$url"-s -d "email=$email&subject=$subject"
