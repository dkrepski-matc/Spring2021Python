#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 7 Dictionaries
"""
#Question 1: Make a dictionary containing FQDN to IP address mappings
addresses = {"server1.testlab.com":"192.168.1.10", "server2.testlab.com":"192.168.1.11",
    "server3.testlab.com":"192.168.1.12", "server4.testlab.com":"192.168.1.13",
    "server5.testlab.com":"192.168.1.14", "server6.testlab.com":"192.168.1.15"}
print("This is the dictionary 'addresses' as provided by Question 1")
print(addresses)
print("-"*40)
#Question 2: List all of the FQDNs in the dictionary
print(f"The FQDNs in this dictionary are: ", addresses.keys())
print("-"*40)
#Question 3: List all of the IP Addresses in the dictionary
print(f"The IP Addresses in this dictionary are: ", addresses.values())
print("-"*40)
#Question 4: List all of the full records (key/value pairs)
print(f"The list of the full records: ", addresses.items())
print("-"*40)
#Question 5: Add more names to the address mappings
print("Here we add two more items using dict['x'] ='y'")
addresses["server7.testlab.com"] = "192.168.1.16"
addresses["server8.testlab.com"] = "192.168.1.17"
print("-"*40)
#Question 6: Test if server2.testlab.com is contained in your dictionary
print("Is server2.testlab.com in this dictionary?")
if "server2.testlab.com" in addresses:
    print("Yes it is!")
else:
    print("No it is not.")
print("-"*40)
#Question 7: Test if server10.testlab.com is contained in your dictionary
print("Is server10.testlab.com in this dictionary?")
if "server10.testlab.com" in addresses:
    print("Yes it is!")
else:
    print("No it is not.")
