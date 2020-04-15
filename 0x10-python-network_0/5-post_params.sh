#!/bin/bash
# POST request to URL and display params
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"