#!/bin/bash
#This displays thestaus code of the response 
curl -s -o /dev/null -w "%{http_code}" "$1"
