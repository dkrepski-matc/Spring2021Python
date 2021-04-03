#!/usr/bin/env python3
"""
Name: Daniel Krepski
email: dkrepski@madisoncollege.edu
Assignment: Week 10 - Subprocesses
"""
import subprocess
myProc = subprocess.run(['ps','-axco','command'],stdout=subprocess.PIPE)

myProcString = myProc.stdout.decode()

myProcList = myProcString.split('\n')

realProcList = myProcList[1::]

print("The number of processes running is",len(realProcList))

for line in realProcList:
    print(line)

print("Again, the number of processes running is",len(realProcList))
