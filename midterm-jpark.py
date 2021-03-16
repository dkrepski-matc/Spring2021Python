#!/usr/bin/env python3
"""
Name: Daniel Krepski
Email: dkrepski@madisoncollege.edu
Assignment: Midterm Activity 2: A Python In Jurassic Park
"""
print("Name: Daniel Krepski")
password_database = {"Username":"dnedry", "Password":"please"}
command_database = {"reboot":"OK. I will reboot all park systems.",
 "shutdown":"OK. I will shut down all park systems.", "done":"I hate all this hacker stuff."}
white_rabbit_object = 0
#This is used to break out of the while loop

counter = 0
#This is used to count the number of failed authentication attempts

while white_rabbit_object == 0 and counter < 3:
    input_user = input("Username:")
    input_password = input("Password:")

    if input_user in password_database["Username"] and input_password in password_database["Password"]:
        white_rabbit_object = 1
        print("Hi Dennis. You're still the best hacker in Jurassic Park.")
        command = input(f"Please enter a command [{command_database.keys()}]: ")
        if command == "reboot":
            print(command_database["reboot"])
        elif command == "shutdown":
            print(command_database["shutdown"])
        elif command == "done":
            print(command_database["done"])
        else:
            print("The Lysine Contingency has been put into effect.")
    else:
        counter = counter + 1
        if counter == 3:
            for line in range(25):
                print ("You didn't say the magic word!")
        else:
            print(f"You didn't say the magic word. {counter}")
