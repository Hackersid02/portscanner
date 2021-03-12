

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

targets  = input("[*] Ebter Targets To Scan (split then by , ): ")
ports = int (input ("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
          print("[*]Scanning Multiple Targrts ")
          for ip_addr in targets.split(','):
                   scan(ip_addr.strip(' '),ports)
else:
       scan(targets,ports)
