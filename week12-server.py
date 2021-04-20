#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 12 - Sockets
"""

import socket

RCV_DATA = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 53558))

while(1):
    s.listen(5)
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    while 1:
        RCV_DATA = clientsocket.recv(1024)
        if not RCV_DATA: break
        print(f"The server received this data:{RCV_DATA}")
        clientsocket.sendall(RCV_DATA)
    clientsocket.close()
