#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Week 5 Assignment - File Data Interactions
"""
#Question 1 - open /etc/passwd, read-only, save full file contents to a str data type
with open("/etc/passwd","r") as FullFile:
    strFullFile = FullFile.read()
    print(len(strFullFile))
    print(f"When counting a string object, the len() function counts the number of characters.")
    print(f"This function is handy to see if a string object has any content.")

#Question 2 - open /etc/passwd, read-only, save full file contents to a list data type
with open("/etc/passwd","r") as FullFile:
    listFullFile = FullFile.readlines()
    print(len(listFullFile))
    print(f"When counting a list object, the len() function counts the number of items.")
    print(f"This function is handy to see how many lines or entries are in a file.")

#Question 3 - open /etc/passwd, read-only, save full file contents one line at a time to a variable
charcount = 0
with open("/etc/passwd","r") as FullFile:
    for line in FullFile:
        charcount += len(line)
print(charcount)
print(f"This was a devilish assignment that highlighted how you can add values into a variable and then use those values.")
