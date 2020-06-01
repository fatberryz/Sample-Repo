import math
import os
import sys

# requests is a 3rd party package
import requests

# print(sys.version)
print(sys.executable)
r = requests.get("https://coreyms.com")


def test(x, y):
    return x * y


print(r.status_code)
