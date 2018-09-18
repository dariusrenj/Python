"""
Name: Zackery Vering
Project: Lab 5B villian module
Date: 14 Sept 2018

Instructions
Create a very simple villian class. Some attributes you will need:

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
from person import PersonV

#create class
class Villian(PersonV):
    """Creates the Villian Class. The Punisher is the default."""
    #create an init
    def __init__(self):
        PersonV.__init__(self)
        self.villianName = "Dr. Doom"
        self.powers = ["Genius-level intellect", 
        "Skilled Sorcerer", "Armor granting the following:",
        "    Superhuman strength and near invulnerability",
        "    Energy projection and absorbtion", "    Flight via rocket boots",
        "    Force field generation",
        "    Built in arsenal of high-tech weapons and gadgets"]
        self.colors = ["Green", "Silver"]

    #function to print the default
    def default(self):
        print("{:_^20}").format("")
        print("Villian: {}").format(self.villianName)
        print("{:_^20}").format("")
        print("Real Name: {}").format(self.name)
        print("{:_^20}").format("")
        print("Powers:")
        for i in range(len(self.powers)):
            print(self.powers[i])
        print("{:_^20}").format("")
        print("Colors:")
        for i in range(len(self.colors)):
            print(self.colors[i])
        print("{:_^20}").format("")
        print("Age: {}").format(self.age)
        print("{:_^20}").format("")
        print("Hair: {}").format(self.hair)
        print("{:_^20}").format("")
        print("Eyes: {}").format(self.eyes)
        print("{:_^20}").format("")

    #setters to create a new villian
    def newVillian(self, name):
        self.villianName = name
    def newRealName(self, realName):
        self.name = realName
    def newVillianPowers(self, powers):
        self.powers = powers
    def newColors(self, colors):
        self.colors = colors
    def newAge(self, age):
        self.age = age
    def newHair(self, hair):
        self.hair = hair
    def newEyes(self, eyes):
        self.eyes = eyes

    #getters for villian
    def getVillian(self):
        return self.villianName

    def getRealName(self):
        return self.name

    def getPowers(self):
        return self.powers

    def getColors(self):
        return self.colors

    def getAge(self):
        return self.age

    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes