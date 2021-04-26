#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 13 - Website Interaction
"""
import requests
import bs4

res = requests.get('https://notpurple.com')
res.raise_for_status()
notpurplesoup = bs4.BeautifulSoup(res.text, 'html.parser')
title=notpurplesoup.select('title')
links=notpurplesoup.select('a')
print(title)
print(links[0])
print(links[1])
