#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 12 - File Transfer App
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50007))

while True:
    s.listen()
    
    clientsocket, address = s.accept()
    print(f"We are connected by {address}")
    while True:
        data = s.recv(1024)
        print(data)
        if not data:
            break
        with open("newsample.txt","wb") as file:
            file.write(data)
            print(f"Done")
    s.close()
