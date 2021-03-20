#!/usr/bin/python3


import socket
import sys
import getopt
import os 
from IPy import IP


# this will be contain the value for use on bufferoverflow
payload = ''

def check_ip(ip):
    
    try:
        IP(ip)
        return ip
    except ValueError as e:
        return socket.gethostbyname(ip)


def init_scanner(host, port):
    
    host_name = check_ip(host)
    #print("[*] Initializing scanner...")
    #host_name = socket.gethostbyname(host)
    try:
        #for port in range(1,1000):
        
        #print(port) 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            sock.connect((host_name, port))
            print("connected at %s : %s ..!"%(host_name,port))
        except Exception:
            pass
            #print("can't open the port")
    except Exception as e:
        print("Error in init_scanner by: ",str(e))



def init_process():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:", ["scanning="])

        for o,a in opts:

            if o in ('-s','--scanning'):
                for x in range(1,1000):
                    init_scanner(a, x)
    except Exception as e:
        print(str(e))





if __name__ == '__main__':

    init_process()
