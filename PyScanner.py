#!/usr/bin/python3


import socket
import sys
import getopt
import os
from IPy import IP



def global_variables():
    global payload
    global path
    global stack 

    payload = ''
    path = "/usr/bin/bash" # path to reverse shell
    stack = list()
# initializr this funciton to get the global variables in whole the code.
global_variables()




# this will be contain the value for use on bufferoverflow

def check_ip(ip):

    try:
        IP(ip)
        return ip
    except:
        return socket.gethostbyname(ip)




def reverse_shell(list_ports):


    pass





def show_port_opened(host, port):
    
    # list all the ports open
    host_name = check_ip(host)

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((host_name, port))
            print()
            #print("target %s  and port open %s"%(host_name,port))
        except Exception:
            return None
            #print("can't open the port")

        return port
    except:
        return None
        #print("Error in init_scanner by: ",str(e))



def init_process():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "s:", ["scanning="])

        for o,a in opts:

            if o in ('-s','--scanning'):
                for x in range(1,1000):
                    if show_port_opened(a, x) is not None:
                        stack.append(show_port_opened(a,x))

        print(stack)
    except Exception as e:
        print(str(e))





if __name__ == '__main__':

    init_process()
