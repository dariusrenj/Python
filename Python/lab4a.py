"""
Name: Zackery Vering
Project: Lab 4A
Date: 10 Sept 2018
Instructions
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
import Tkinter
import tkMessageBox
from math import sqrt
from PIL import JpegPresets

top = Tkinter.Tk()
top.title("Calculator")
top.grid(baseWidth=10, widthInc=10, baseHeight=10, heightInc=10)
#define variables
user_choice = 0
result = 0
label4 = Tkinter.Label()
#define functions
def addition():
    global result
    result = int(first_num.get()) + int(second_num.get())
    label4 = Tkinter.Label(top, text="{}".format(result))
    label4.grid(column=1, row=6)

def subtraction():

    global result
    result = int(first_num.get()) - int(second_num.get())
    label4 = Tkinter.Label(top, text="{}".format(result))
    label4.grid(column=1, row=6)

def division():
    global result
    result = float(first_num.get()) / float(second_num.get())
    label4 = Tkinter.Label(top, text="{}".format(result))
    label4.grid(column=1, row=6)

def multiplication():
    global result
    result = int(first_num.get()) * int(second_num.get())
    label4 = Tkinter.Label(top, text="{}".format(result))
    label4.grid(column=1, row=6)

def power():
    global result
    result = int(first_num.get()) ** int(second_num.get())
    label4 = Tkinter.Label(top, text="{}".format(result))
    label4.grid(column=1, row=6)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def fib():
    global result
    result= str('')
    for i in range(int(first_num.get())):
        if (result == ''):
            result = str(fibonacci(i))
        else:
            result = result + ',' + str(fibonacci(i))
        label4 = Tkinter.Label(top, text="{}".format(result))
        label4.grid(column=1, row=6)

def pythagoras():
    global result
    result = sqrt((int(first_num.get())**2) + (int(second_num.get()**2)))
    label4 = Tkinter.Label(top, text="{}".format(result))
    label4.grid(column=1, row=6)

def surprise():
    picture = Tkinter.Tk()
    picture.title("Surprise!")
    top.grid(baseWidth=10, widthInc=10, baseHeight=10, heightInc=10)
    #photo = Tkinter.PhotoImage(file="CerberusRE2.jpg")
    #doge = Tkinter.Button(picture, image=photo, command=quit)
    #doge.grid(column=1, row=0)
    doge_label = Tkinter.Label(picture, text="This is temp text. Still working on this.")
    doge_label.grid(column=1, row=1)
    picture.mainloop()

label1 = Tkinter.Label(top, text="First Number")
label1.grid(column=0, row=0)
first_num = Tkinter.Entry(top)
first_num.grid(column=1, row=0)
label2 = Tkinter.Label(top, text="Second Number")
label2.grid(column=0, row=1)
second_num = Tkinter.Entry(top)
second_num.grid(column=1, row=1)
add = Tkinter.Button(top, text="Addition", width=12, command=addition)
sub = Tkinter.Button(top, text="Subtraction", width=12, command=subtraction)
div = Tkinter.Button(top, text="Division", width=12, command=division)
mul = Tkinter.Button(top, text="Multiplication", width=12, command=multiplication)
pwr = Tkinter.Button(top, text="Power", width=12, command=power)
pyt = Tkinter.Button(top, text="Pythagoras", width=12, command=pythagoras)
fib = Tkinter.Button(top, text="Fibonacci", width=12, command=fib)
sur = Tkinter.Button(top, text="Something Else", width=12, command=surprise)
qit = Tkinter.Button(top, text="Quit", width=12, command=quit)
add.grid(column=0, row=2)
sub.grid(column=1, row=2)
div.grid(column=2, row=2)
mul.grid(column=0, row=3)
pwr.grid(column=1, row=3)
pyt.grid(column=2, row=3)
fib.grid(column=0, row=4)
sur.grid(column=1, row=4)
qit.grid(column=1, row=5)
label3 = Tkinter.Label(top, text="Result")
label3.grid(column=0, row=6)
label4 = Tkinter.Label(top, text="{}".format(result))
label4.grid(column=1, row=6)
top.mainloop()