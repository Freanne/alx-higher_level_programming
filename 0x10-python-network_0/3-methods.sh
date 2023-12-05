#!/bin/bash
# Check if the number of arguments is correct
curl -sI "$1" | grep Allow | awk '{split($0, methods, ": "); print methods[2]}'
