

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
from contextlib import closing
from urllib.request import Request
import hashlib

    
url = "http://138.68.137.155:32626/"
#request = Request(url = url, headers = headers)
r = requests.session()
get = r.get(url)
data = get.text
base = BeautifulSoup(data, 'html.parser')
h3 = base.find("h3")
payload = h3.text
md5 = hashlib.md5(payload.encode()).hexdigest()
params = {"hash": md5}
response = r.post(url, data = params)
print(response.text)
    
