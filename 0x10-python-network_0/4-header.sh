#!/bin/bash
#this send a GET request to the ur and displays the body of the response
curl -sH "X-School-User-Id: 98" "$1"
