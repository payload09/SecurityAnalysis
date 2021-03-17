

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

        print("\n          usage")
        print("""\n

    -i --info                       showing how to use this tool
    -c --capturer                   specify which url you want to catch and scrap all parameters into csv file
                \n
                """)
    
    def download_images(self, url, path):

        try:
            if os.path.isdir("{}/images".format(path)) is False:
                os.makedirs("{}/images".format(path))
            #print(url)
            r = requests.session()
            get = r.get(url)
            #print(get.text)
            data = get.text
            base = BeautifulSoup(data, 'html.parser')
            image_to_find = base.find("img")
            
            img = Image.open(requests.get(image_to_find['src'], stream=True).raw)
            img.save("{}/images/imagen1.png".format(path))
            
            
            #print(image_to_find.attrs["src"])
        
            """headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                        'AppleWebKit/537.11 (KHTML, like Gecko) '
                        'Chrome/23.0.1271.64 Safari/537.11',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                        'Accept-Encoding': 'none',
                        'Accept-Language': 'en-US,en;q=0.8',
                        'Connection': 'keep-alive'}

            if os.path.isdir("{}/images".format(path)) is False:
                os.makedirs("{}/images".format(path))

            request = Request(url = url, headers = headers)

            with closing(urlopen(request).read()) as url_open:
                self.base = BeautifulSoup(url_open, "html.parser")
                
                img = self.base.findAll("img")
                #img_path = img["src"]
                #print(img_path)
                for x in img:
                    print(x["src"])
                    #image = Image.open(requests.get(img_path, stream=True).raw)
                    #image.save(str(img_path))"""
        except Exception as e:
            print(str(e))

    def showing_arguments(self, path):
        
        try:
            opts, args = getopt.getopt(self.args, "ic:", ["info", "capturer="])
            
            for o,a in opts:

                if o in ("-i","--info"):
                    self._info_arguments()
                
                if o in ("-c", "--capturer"):
                    self.download_images(a, path)
        except Exception as e:

            print("Error by: ",str(e))



if __name__ == '__main__':

    #path = input("name> ")
    path = "arturo"
    web_capturer = Web()
    web_capturer.showing_arguments(path)
    #web_capturer.download_images("wherever", path)

