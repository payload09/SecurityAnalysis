

"""
    @author Arturo Negreiros
    @version 1.0
    Happy scraping and Enjoy it!
"""
from urllib.request import Request
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import requests
from io import open
import getopt
import os
import sys
from PIL import Image
from contextlib import closing
import re


class Web:  

    def __init__(self):
        
        self.base = None
        self.args = sys.argv[1:]
    
    def _info_arguments(self):

        print("usage")
        print("""\n
        -i --info   =>       showing how to use this tool
        -c --capturer   =>   specify which url you want to catch and scrap all parameters into csv file
            \n
                """)

    def download_images(self, url, path):

        try:
            if os.path.isdir("{}/images".format(path)) is False:
                os.makedirs("{}/images".format(path))
            
            r = requests.session()
            get = r.get(url)
            
            data = get.text
            base = BeautifulSoup(data, 'html.parser')
            image_to_find = base.findAll("img")
            
            counter = 1
            for x in image_to_find:
                if "src" in x.attrs:
                    img = Image.open(requests.get(x.attrs["src"], stream = True).raw)
                    img.save("{}/images/{}.png".format(path,str(counter)))
                    counter += 1
            
        except Exception as e:
            print("Error by: ",str(e))

    def showing_arguments(self, path):
        
        try:
            opts, args = getopt.getopt(self.args, "ic:", ["info", "capturer="])
            
            for o,a in opts:

                if o in ("-i","--info"):
                    self._info_arguments()
                
                if o in ("-c", "--capturer"):
                    #self.download_images(a, path)
                    self._get_session(a)
        except Exception as e:

            print("Error by: ",str(e))

    
    def _get_session(self, url):

        request = requests.session()
        print("the cookies: %s"%request.cookies.get_dict())
        request_get = request.get(url)
        print(request_get.text)

if __name__ == '__main__':

    path = input("name> ")
    web_capturer = Web()
    web_capturer.showing_arguments(path)

