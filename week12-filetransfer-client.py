#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 12 - File Transfer App
"""
import socket

ONE_LOOP = (True)
filename = "filesample.txt"
sock = socket.socket()
sock.bind((socket.gethostname(),3146))
sock.listen(20)
print(f"Run the filetransfer-server.py script now...")
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    with open (filename,"rb") as file:
        data = file.read(1024)
        while data:
            conn.send(data)
            data = file.read(1024)
    print("File transfer complete.")
    conn.close()
    if(ONE_LOOP):
        break
sock.shutdown(1)
sock.close()
