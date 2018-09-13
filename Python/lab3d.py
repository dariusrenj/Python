"""
Name: Zackery Vering
Project: Lab 3D
Date: 7 Sept 2018
Instructions
Write a program that prompts a user to input an integer and calculates the factorial of that number using a while loop.
Requirments
Adhere to PEP8 (Comments, formatting, style, etc)
Utilize userinput
Utilize input validation
Utilize proper formatting
Utilize proper and clean loops and conditionals
Follow instructions above"""

#Let's user input a value and checks to see if the user's input is an int
def check_int():
    user_input = raw_input("Please input an integer.\n")
    try:
        user_input = int(user_input)
    except ValueError:
        print ("Try again.")
        user_input = check_int()
    return user_input

#Prints the title
print("{:_^20}").format("")
print("{:_^20}").format("FACTORIAL")
print("{:_^20}").format("")

#Set variables for modification
user_int = check_int()
before_mod = user_int
total = 1
#Loop to calculate factorial
while user_int > 0:
    total = total * user_int
    user_int -= 1
#Print results
print ("The factorial of {} is {}.").format(before_mod, total)


