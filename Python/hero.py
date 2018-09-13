"""
Name: Zackery Vering
Project: Lab 5B hero module
Date: 13 Sept 2018

Instructions
Create a very simple super hero class. Some attributes you will need:

Hero Name
Real Name
Power(s)
Colors
etc

Requirments
Adhere to PEP8 and utilize proper and efficient code
Utilize a __init__()
Ensure variables are correct type (class vs instance variables)
Utilize methods:
Start to format your class using getters and setters
Create an instance of your class. Populate it with data utilzing a init
and/or getters and setters

Additional:
Begin using encapsulation techniques
"""

class Hero:
    """Creates the Hero Class. The Punisher is the default."""
    def __init__(self):
        self.heroName = "The Punisher"
        self.realName = "Francis 'Frank' Castle"
        self.powers = ["Skilled in guerrilla and military tactics", 
        "Close quarters combat", "Infiltration", "Marksmanship",
        "Demolitions", "Really really angry"]
        self.colors = ["Black", "White"]

    def defualt(self):
        print("{:_^20}").format("")
        print("Hero: {}").format(self.heroName)
        print("{:_^20}").format("")
        print("Real Name: {}").format(self.realName)
        print("{:_^20}").format("")
        print("Powers:")
        for i in range(len(self.powers)):
            print(self.powers[i])
        print("{:_^20}").format("")
        print("Colors:")
        for i in range(len(self.colors)):
            print(self.colors[i])
        print("{:_^20}").format("")

    def newHero(name):
        self.heroName = name
    def newRealName(realName):
        self.heroName = realName
    def newHeroPowers(powers):
        self.powers = powers
    def newColors(colors):
        self.colors = colors