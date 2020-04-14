#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep 'Allow' | awk '{print  $2,$3,$4}'
