"""
Name: Zackery Vering
Project: Lab 5A
Date: 13 Sept 2018

This module contains the code for calculator operations.
"""
import user_input
from math import sqrt

def addition():
    #perform addition
    print("You selected addition.")
    add1 = user_input.num1()
    add2 = user_input.num2()
    x = add1+add2
    print ("{} + {} = {}").format(add1, add2, x)

def subtraction():
    #perform subtraction
    print("You selected subtraction.")
    sub1 = user_input.num1()
    sub2 = user_input.num2()
    x = sub1-sub2
    print ("{} - {} = {}").format(sub1, sub2, x)

def division():
    #perform division
    print("You selected division.")
    div1 = user_input.num1()
    div2 = float(user_input.num2())
    x = div1/div2
    print ("{} / {} = {}").format(div1, div2, x)

def multiplication():
    #perform multiplication
    print("You selected multiplication.")
    mul1 = user_input.num1()
    mul2 = user_input.num2()
    x = mul1*mul2
    print ("{} * {} = {}").format(mul1, mul2, x)

def power():
    #perform a power operation
    print("You selected power.")
    pow1 = user_input.num1()
    pow2 = user_input.num2()
    x = pow1**pow2
    print ("{} to the power of {} is {}").format(pow1, pow2, x)

def fibonacci(n):
    #run fibonacci
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def pythagoras():
    #perfrom pythagorian theorm
    pyt1 = user_input.num1()
    pyt2 = user_input.num2()
    print("The third side of your right triangle is {}.").format(sqrt((pyt1**2)+(pyt2**2)))
