#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sI 0.0.0.0:5000/route_4 | grep 'Allow' | awk '{print  $2,$3,$4}'
