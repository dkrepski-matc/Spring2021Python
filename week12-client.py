#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 12 - Sockets
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 53558))

loopcount = 1
SND_DATA = "This is a connecting message."

while loopcount < 6:
    s.send(bytes(SND_DATA,"utf-8"))
    
    loopcount = loopcount + 1

    RCV_DATA = s.recv(1024)
    print(RCV_DATA.decode("utf-8"))

s.close()
