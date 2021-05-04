#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 14 - JSON
"""
import argparse
import requests
import json

parser = argparse.ArgumentParser(description="Script to pass in an IP address")
parser.add_argument('-ip', '--IP address', dest='varIP', metavar='[an IP address]', default='address',
    type=str, required=True, help='Enter an IP address')
#print(parser.print_help())
IPaddress = parser.parse_args().varIP
#print(IPaddress)

URL = ("http://ipinfo.io/"+IPaddress+"/json")
#print(URL)

json_raw = requests.get(URL)
#print(json_raw.text)
#print(str(json.loads(myDict.text)))
myDict = json.loads(json_raw.text)
#print(myDict.keys())

for key in myDict:
    print(f"{key} : {myDict[key]}")
