#!/bin/bash
#a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

response_size=$(curl -s "$1" | wc -c)

if [ $? -ne 0 ]; then
	echo "ERROR: Failed to retrieve the URL or invalid URL."
	exit 1
fi

echo "Size of the response body: $response_size bytes"
