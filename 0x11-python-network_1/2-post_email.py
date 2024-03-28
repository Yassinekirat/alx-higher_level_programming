#!/usr/bin/python3
'''script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
'''

from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]
    data = {'email': argv[2]}
    req = Request(url, urlencode(data).encode())
    with urlopen(req) as response:
        res = response.read().decode("utf-8")
        print(res)
