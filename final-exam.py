#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Final Exam! Where did the semester go?
"""
import argparse
import requests
import bs4
import json
import socket

parser = argparse.ArgumentParser(description="Final exam script!")
parser.add_argument('-ip', '--IP address', dest='varIP', metavar='[an IP address]', default='address',
    type=str, required=True, help='Enter an IP address')
parser.add_argument('-f', '--function', dest='varInt', metavar='[the function number]', default=10,
    type=int, required=True, help='Enter the number function you want.')
#print(parser.print_help())

IPaddress = parser.parse_args().varIP
FunNum = parser.parse_args().varInt
#print(IPaddress)
#print(FunNum)
URL = ("http://"+IPaddress+"/q"+str(FunNum))
print("Name: Daniel Krepski")
print(URL)

def get_response():
    response = requests.get(URL)
    print(response.text)

def parse_string():
    response = requests.get(URL)
    response.raise_for_status()
    responseSoup = bs4.BeautifulSoup(response.text, 'html.parser')
    example = responseSoup.h3.string
    print(f"ANSWER: {example[2::3]}")

def parse_header():
    response = requests.get(URL)
    for key,value in response.headers.items():
        if key == "MATC-HEADER":
            print(f"ANSWER: {value}")

def parse_json():
    response = requests.get(URL)
    myDict = json.loads(response.text)
#    print(myDict)
    for key in myDict:
#        print(myDict[key])
        for key2 in myDict[key]:
#            print(key2)
            if key2["title"] == "1984":
                print(f"ANSWER: {key2['author']}")

def socket_client():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    RPORTS = range(5000,6000)
    for RPORT in RPORTS:
        try:
            sock.connect((IPaddress, RPORT))
            sock.send(bytes("secret","utf-8"))
            RCV_DATA = sock.recv(1024)
            Answer = RCV_DATA.decode("utf-8")
            print(f"ANSWER: {Answer}")
            sock.close()
        except:
#            print(f"{RPORT} failed")
            pass

if FunNum == 1:
    get_response()
elif FunNum == 2:
    parse_string()
elif FunNum == 3:
    parse_header()
elif FunNum == 4:
    parse_json()
elif FunNum == 5:
    socket_client()
