#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Functions - Celsius to Fahrenheit
"""

def celsius_to_fahrenheit(degrees_celsius):
    degrees_fahrenheit = (degrees_celsius *(9/5))+32
    return "%0.2f" % degrees_fahrenheit

def main():
    degrees_celsius = float(input("Enter a temperature in Celsius. "))
    degrees_fahrenheit = float(celsius_to_fahrenheit(degrees_celsius))
    print(f"The temperature in Fahrenheit is ", degrees_fahrenheit)

if __name__ == "__main__":
    main()
