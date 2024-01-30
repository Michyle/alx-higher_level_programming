#!/bin/bash
# This sends a JSON POST request to a url that passed as the first argument and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
