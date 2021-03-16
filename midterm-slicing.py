#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Midterm activity 3: slicing
"""
print("Name: Daniel Krepski")

with open("slicing-file.txt","r") as File:
    lines = File.readlines()
    
    line1 = lines[-3:-2:]
    line2 = lines[2:5:]
    line3 = lines[-10:12:-2]
    line4 = lines[10:13:]
    line5 = lines[-19:-22:-1]

line1 = " ".join(line1)
line2 = "".join(line2)
line3 = "".join(line3)
line4 = "".join(line4)
line5 = "".join(line5)

quote = str(line1) + str(line2) + str(line3) + str(line4) + str(line5)


print(quote.replace("\n"," "))
