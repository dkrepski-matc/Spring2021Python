#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Week 6 Assignment - Boolean
"""
print(f"True and True ::", bool(True == True))
print(f"False and True ::", bool(False == True))
print(f"1 == 1 and 2 == 1 ::", bool(1==1 and 2==1))
print(f"0 ::", bool(0))
print(f' "" ::', bool(""))
print(f"0.0 ::", bool(0.0))
print(f"not 0 ::", bool(not 0))
print(f'"test" == "test" ::', bool("test"=="test"))
print(f"1 == 1 or 2 != 1 ::", bool(1==1 or 2!=1))
print(f"True and 1 == 1 ::", bool(True and 1==1))
print(f"False and 0 != 0 ::", bool(False and 0!=0))
print(f"True or 1 == 1 ::", bool(True or 1==1))
print(f'"test" == "testing" ::', bool("test"=="testing"))
print(f"1 != 0 and 2 == 1 ::", bool(1==0 and 2==1))
print(f'"test" != "testing" ::', bool("test"!="testing"))
print(f'"test" == 1 ::', bool("test"==1))
print(f'1 == 1 and not ("testing" == 1 or 1 == 0) ::', bool(1==1 and not ("testing"==1 or 1==0)))
print(f'"chunky" == "bacon" and not (3 == 4 or 3 == 3) ::', bool("chunky"=="bacon" and not (3==4 or 3==3)))
print(f'3 == 3 and not ("testing" == "testing" or "Python" == "Fun") ::', bool(3==3 and not ("testing"=="testing" or "Python"=="Fun")))

