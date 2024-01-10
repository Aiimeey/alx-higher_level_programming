#!/bin/bash
# Script that takes in a URL as an argument,sends GET request,displays response
curl -sX GET -H "X-School-User-Id: 98" "$1"
