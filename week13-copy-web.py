#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 13 - Website Interaction
"""
import requests

res = requests.get('https://notpurple.com')
res.raise_for_status()
notpurplepage = open('my_web_file.html', 'wb')
for file in res.iter_content(100000):
    notpurplepage.write(file)
notpurplepage.close()
