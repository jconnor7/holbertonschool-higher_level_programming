#!/usr/bin/python3
"""
    Python script that takes in a URL, sends a request
    to the URL and displays the value of the X-Request-Id
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        dict_info = response.info()
        print(dict_info['X-Request-Id'])
