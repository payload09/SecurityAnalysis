#!/usr/bin/python3
"""
To establish a typical remote shell, a machine controlled by the attacker 
connects to a remote network host and requests a shell session – this is called 
a bind shell. But what if the remote host is not directly accessible, for example 
because it has no public IP or is protected by a firewall? In this situation, a 
reverse shell might be used, where the target machine initiates an outgoing connection 
to a listening network host and a shell session is established.

Reverse shells are often the only way to perform remote maintenance on hosts behind a NAT,
so they have legitimate administrative uses. However, they can also be used by cybercriminals 
to execute operating system commands on hosts protected from incoming connections by a firewall 
or other network security systems. For example, a piece of malware installed on a local
workstation via a phishing email or a malicious website might initiate an outgoing connection
to a command server and provide hackers with a reverse shell capability. Firewalls mostly filter 
incoming traffic, so an outgoing connection to a listening server will often succeed.

When attempting to compromise a server, an attacker may try to exploit a command injection vulnerability 
on the server system. The injected code will often be a reverse shell script to provide a convenient command
shell for further malicious activities.
"""

import socket
import sys
import getopt
import os
from IPy import IP

payload = ''
path = "/usr/bin/bash" # path to reverse shell
stack = list()
info = False
port = 0
host = ''
reverse = False


class Socket_connection:

    def __init__(self, host_, port_):
        self.sock = None
        self.port = port_
        self.host = host_


    def create_connection_server(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #self.sock.bind((self.host, self.port))
            self.sock.connect(("192.168.100.208", 514))
            self.sock.listen(1)
            print("[*] Connection stablished...")
        except Exception as e:
            print("Connection error: ", str(e))




def global_variables():
    global payload
    global path
    global stack
    global info
    global port
    global host
    global reverse

    
# initializr this funciton to get the global variables in whole the code.
global_variables()




# this will be contain the value for use on bufferoverflow

def check_ip(ip):

    try:
        IP(ip)
        return ip
    except:
        return socket.gethostbyname(ip)

def showing():

    print("This command line shell is for try to get reverse shell from METASPLOITABLE")
    print("""\n
    -s --scanning           is for general scanner from the ip, getting the ports currently open
    -r --reverse            if puting a host target and especific port to try to get reverse shell""")



def show_port_opened(host, name_port):
    """The purpose is get and discover which port is opened"""

    host_name = check_ip(host)

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((host_name, name_port))
            port_name = socket.getnameinfo((str(host), name_port), socket.NI_NUMERICHOST)
            print("port %s  port name %s"%(name_port, port_name))
        except Exception:
            return None

        return port
    except:
        return None


def reverse_shell(host,port):
    pass


def init_process():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "is:g:rp:h:", ["info","scanning=", "general=", 
            "reverse", "port=", "host="])
        for o,a in opts:
            
            if o in ('-s','--scanning'):
                for x in range(1,1000):
                    show_port_opened(a, x)

            elif o in ('-g','--general'):
                pass

            elif o in ('-i','--info'): showing()

            elif o in ('-r','--reverse'):reverse = True
                
            elif o in ('-p','--port'): port = int(a)

            elif o in ('-h','--host'): host = str(a)

        if reverse:

            try:
                print(host)
                print(port)
                if port is not None and host is not None:
                    sock = Socket_connection(host, port)
                    sock.create_connection_server()
                    
                else:
                    showing()
                
            except Exception as e:
                print("error: ",str(e))
            exit()

    except Exception as e:
        print("Error by: ", str(e))





if __name__ == '__main__':

    init_process()
