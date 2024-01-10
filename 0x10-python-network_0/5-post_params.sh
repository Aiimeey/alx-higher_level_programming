#!/bin/bash
# Script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
# Variables email and subject must be sent with specified values
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
