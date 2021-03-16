#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Midterm exam - Flow Control
"""
print("Name: Daniel Krepski")
#Total is the counter for the line number total
Total = 0
#Entry is list that will be filled with the output from the file
Entry = []
with open ("Midterm-if.txt","r") as FullFile:
    for line in FullFile:
        Entry = line.split(",")
        Entry[5] = Entry[5].strip()
        if "gmeach18@ed.gov" in Entry:
            Total += int(Entry[0])
#           print(Entry)                       <-- These print lines were for my own testing
        elif "248.253.63.149" in Entry:
            Total += int(Entry[0])
#           print(Entry)                       <-- to make sure I had the right lines for adding
        elif "Whiteland" in Entry:
            Total += int(Entry[0])
#           print(Entry)                       <-- and to help me troubleshoot my problem of removing '\n' from the line
        elif "80.222.19.190" in Entry:
            Total += int(Entry[0])
#           print(Entry)
        elif "Kayley" in Entry:
            Total += int(Entry[0])
#           print(Entry)
        elif "dcassyqw@microsoft.com" in Entry:
            Total += int(Entry[0])
#           print(Entry)
print(f"The total is: {Total}")
