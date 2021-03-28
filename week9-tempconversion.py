#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Week 9 - Functions - Temperature Converter
"""

temperature = float(input("Enter a temperature. "))
measure = input("Is that in degrees Fahrenheit (F) or Celsius (C)? ")

if measure == "f" or measure == "F":
    import f2c
    degrees_fahrenheit = temperature
    result = f2c.fahrenheit_to_celsius(temperature)
    print(f"It is",result, "degrees Celsius.") 

elif measure == "c" or measure == "C":
    import c2f
    degrees_celsius = temperature
    result = c2f.celsius_to_fahrenheit(temperature)
    print(f"It is",result, "degrees Fahrenheit.")

else:
    print("You must make a valid choice.")
