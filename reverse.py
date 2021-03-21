import socket
import time
import threading
from  termcolor import colored
import os
import subprocess

"""
@author Arturo Negreiros (Payload)
@description Software for connect to metasploitable machine, implementing reverse shell
"""


define_host = None

def global_variables():
    global define_host
    define_host = "192.168.100.209" # defined host metasploit virtual machine

global_variables()

def main(host, port):

    try: 
        socket_connection = socket.socket() # defined socket connection object
        socket_connection.connect((str(host), int(port)))
        banner = socket_connection.recv(1024)
        port_info = colored("[*] {port} open".format(port = port), "green")
        banner = str(banner).replace("b'", "")
        print(port_info+ "\t"+banner)
        #print("[*] Connection was done")
        #print(port_info)
    

    except Exception as e:
        #print(str(e))
        pass
if __name__ == '__main__':

    for x in range (1,1000):
        
        main(define_host, x)