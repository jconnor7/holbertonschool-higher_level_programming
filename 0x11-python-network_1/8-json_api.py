#!/usr/bin/python3
"""
    Takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with
    the letter as a param
"""

import requests
from sys import argv

if __name__ == "__main__":

    url = "http://b9a9168cd2ea.19.hbtn-cod.io:5000/search_user"
    letter = argv[1] if len(argv) == 2 else ""

    data = {'q': letter}
    req = requests.post(url, data)

    type_req = req.headers.get("content-type")

    if type_req != 'application/json':
        print("Not a valid JSON")
        exit()
    else:
        req_json = req.json()

    if len(req_json) == 0:
        print("No result")
    else:
        print("[{}] {}".format(req_json['id'], req_json['name']))
