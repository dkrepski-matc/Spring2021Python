#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu 
Assignment: Functions - Fahrenheit to Celsius
"""
def fahrenheit_to_celsius(degrees_fahrenheit):
    degrees_celsius = (degrees_fahrenheit - 32)*(5/9)
    return "%0.2f" % degrees_celsius

def main():
    degrees_fahrenheit = float(input("Enter a temperature in Fahrenheit. "))
    degrees_celsius = float(fahrenheit_to_celsius(degrees_fahrenheit))
    print(f"The temperature in Celsius is ",degrees_celsius)

if __name__ == "__main__":
    main()
