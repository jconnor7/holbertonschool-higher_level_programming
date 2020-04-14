#!/bin/bash
#Script that takes URL and request size of body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
