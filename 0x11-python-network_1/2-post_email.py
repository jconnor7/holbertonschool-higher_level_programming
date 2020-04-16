#!/usr/bin/python3
"""
    Takes in a URL and an email, sends a POST request
    to the passed URL with the email as a parameter,
     and displays the body of the response
"""

import urllib.parse
import urllib.request
from sys import argv

url = argv[1]
values = {'email': argv[2]}

data = urllib.parse.urlencode(values).encode('utf-8')

req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    body_resp = response.read().decode('utf-8')
    print(body_resp)
