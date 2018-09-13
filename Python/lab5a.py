"""
Name: Zackery Vering
Project: Lab 5A
Date: 13 Sept 2018
Instructions
Using your calculator you created from Lab4A, split up the 
functionality into modules and utilize packaging. Some things 
you could split up:

The user menu into it's own module on a higher level package
Opertions into one module, lower level
Algorithms into one module, lower level
Create a fully functional calculator using BOTH functions and lambdas.
Create a user menu as well as a "screen" where the numbers and
operations take place. The calculator needs to have the following
functionality:

Addition
Subtraction
Division
Multiplication
Power
At least two math algorithms (One can be your Fibonacci)

Requirments
Adhere to PEP8
Functionality requirments above
Utilize user input and proper validation
Utilize proper formatting
Utilize proper and clean statements and loop

Additional
More than two numbers
Continuous operations (5 + 5 + 2 - 1 / 2 for example)
Additional operations
Additonal math algorithms
"""
import time
import user_input
import operations

#define variables
user_choice = 0

#start loop
while (user_choice != 7):
    #print menu
    print("{:_^20}").format("")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Power")
    print("6. Algorithms")
    print("7. Quit")
    print("{:_^20}").format("")
    #ask user what they want to do
    user_choice = user_input.check_int()
    print("{:_^20}").format("")
    #call function based on user choice
    if (user_choice == 1):
        operations.addition()
    elif (user_choice == 2):
        operations.subtraction()
    elif (user_choice == 3):
        operations.division()
    elif (user_choice == 4):
        operations.multiplication()
    elif (user_choice == 5):
        operations.power()
    elif (user_choice == 6):
        #let user choose what algorithm they want to run
        print("You selected algorithms.")
        print("1. Fibanacci")
        print("2. Pythagoras")
        user_choice2 = user_input.check_int()
        while(True):
            if (user_choice2 == 1):
                y = int(raw_input("How many times would you like to loop?\n"))
                print("{:_^20}").format("")
                while(True):
                    for i in xrange(y):
                        print(operations.fibonacci(i))
                    break
                break
            elif (user_choice2 == 2):
                operations.pythagoras()
                break
            else:
                print("That was an invalid response. Please try again.")
                user_choice2 = user_input.check_int()
                print("{:_^20}").format("")
    elif (user_choice == 7):
        print("Have a good day!")
    else:
        print("That was an invalid response. Please try again.")
        user_choice = user_input.check_int()
        print("{:_^20}").format("")