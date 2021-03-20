
import socket
import sys
import getopt
import os
import time

class Socket_connection:

    def __init__(self, host_, port_):
        self.sock = None
        self.port = port_
        self.host = host_
        self.host_name = None
        self.connect = None
        self.address = None
        self.list_ports_openeds()

    def socket_create(self):
        """Create the connection for the sockets"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as error:
            print("Error creating socket by: ",str(error))


    def socket_bind(self):

        try:
            self.sock.bind((str(self.host), int(self.port)))
            self.sock.listen(1)
            print("[*] Connection stablished...")
        except Exception as e:
            print("Socket binding error: ", str(e))
            #self.socket_bind()
            
    def socket_accept_connection(self):

        try:
            self.connect, self.addrress = self.sock.accept()
            print("\n")
            self.host_name = self.connect.recv(1024)
        except socket.error as err:
            print("Error getting the connection: ", str(err))
    

    def list_ports_openeds(self):

        def _create_internal_connection(host, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                print("[*] Connection was done, port %s open"%port)
            except:
                return None
        try:
            print("[*] Trying to connect at %s ..."%self.host)
            print("")
            time.sleep(2)
            for x in range(1000):
                _create_internal_connection(self.host, x)
        except socket.error as error:
            print("Error by: ",str(error))

        
    


if __name__ == '__main__':
    sock = Socket_connection("192.168.100.209",21)
    sock.socket_create()
    sock.socket_bind()
    sock.socket_accept_connection()












