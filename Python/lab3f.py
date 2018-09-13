"""
Name: Zackery Vering
Project: Lab 3F FizzBuzz
Date: 10 Sept 2018
"""
#start loop that goes from 1 to 100
for i in range(1, 101):
    #if i is divisible by 3 and 5 print FizzBuzz
    if ((i % 3 == 0) and (i % 5 == 0)):
        print ("FizzBuzz")
    elif (i % 3 == 0):
        #if i is divisible by 3 but not 5 print Fizz
        print ("Fizz")
    elif (i % 5 == 0):
        #if i is divisible by 5 but not 3 print Buzz
        print ("Buzz")
    else:
        #if i is not divisible by 3 or 5 print i
        print ("{}").format(i)

#start sort of drawn out version
fizz_list = []
#make a loop and populate it
for x in range (100):
    fizz_list.append(x+1)

#start a loop for fizz_buzz
for z in range(1, len(fizz_list)):
    #set a copy variable since I'll be overwriting the list variable
    copy_var = fizz_list[z]
    # check if list variable is divisible by 3
    if (fizz_list[z] % 3 == 0):
        #if it is, change to Fizz
        fizz_list[z] = "Fizz"
        #see, needed a copy variable
        if (copy_var % 5 == 0):
            #if copy variable is divisible by 3 append Buzz
            fizz_list[z] += "Buzz"
    #if list variable isn't divisible by 3 but is by 5 change to Buzz
    elif (fizz_list[z] % 5 == 0):
        fizz_list[z] = "Buzz"
#loop through the list now and print each item in the list
for y in range(len(fizz_list)):
    print("{}").format(fizz_list[y])
        