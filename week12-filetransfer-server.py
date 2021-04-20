#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 12 - File Transfer App
"""
import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 3146))
sock.send(b"Hello from client")
with open("newsample.txt","wb") as file:
    print(f"Receiving data...")
    while True:
        data = sock.recv(1024)
        if not data:
            break
        file.write(data)
filename = "newsample.txt"
print(f"File transferred. Check it out, it's filename is {filename}")
sock.close()
