#!/bin/bash
# This script sends a request to a URL and displays only the status code of the response
curl -o /dev/null -s -w "%{http_code}" "$1"
