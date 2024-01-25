#!/bin/bash
#This is a DELETE request to the url passed as the first argument and displays the body of the response
curl -sX DELETE "$1"
