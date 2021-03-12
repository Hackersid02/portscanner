

import socket
import termcolor

def scan(target,ports):
        for port in range(1,ports):
                 scan_port(target,port)

def scan_port(ipaddress,port) :


            try:
                    sock = socket.socket()
                    sock.connect((ipaddress,port))
                    print("[+]port opened" + str(port))
            except:
                    print("[_]port closed" + str(port))

targets  = 
