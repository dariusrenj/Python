"""
Name: Zackery Vering
Project: Lab 5A
Date: 13 Sept 2018

This module contains the code for user input.
"""
def check_int():
    #ask for user input and check if it's an integer
    user_input = raw_input("What would you like to do?\n")
    try:
        user_input = int(user_input)
    except ValueError:
        print ("Try again.")
        user_input = check_int()
    return user_input

def num1():
    #ask for user input and check if it's an integer
    user_input = raw_input("What is the first number?\n")
    try:
        user_input = int(user_input)
    except ValueError:
        print ("Try again.")
        user_input = check_int()
    return user_input

def num2():
    #ask for user input and check if it's an integer
    user_input = raw_input("What is the second number?\n")
    try:
        user_input = int(user_input)
    except ValueError:
        print ("Try again.")
        user_input = check_int()
    return user_input