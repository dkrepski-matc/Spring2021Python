#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
This is the Week 4 assignment script
"""
#Step 1 : create variables
varString = "Here is a nice string to slice"
varList = ["Here","is","a","nice","list","to","slice"]

#Step 2 : slicing varString
print(f"{varString[3:30:1]}")
print(f"{varString[0:3:1]}")
print(f"{varString[3:12:1]}")
print(f"{varString[0:30:2]}")
print(f"{varString[30::-1]}")

#Step 3 : slicing varList
print(varList[7::-1])
print(varList[2::-1])
print(varList[2:4:1])
print(varList[0:7:3])
print(varList[1:7:1])

#Step 4 : for loop with varString, one element per line
for stringy in varString:
    print(stringy)

#Step 5 : for loop with varList, one element per line
for listy in varList:
    print(listy)
