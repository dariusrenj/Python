"""
Name: Zackery Vering
Project: Lab 5C person module
Date: 14 Sept 2018

Instructions
Update your hero class lab with the following additions:

Create a generic Person class
Create a Hero class that inherits from Person
Refactor code where needed
Utilize proper Encapsulation
Include user input
Use getters and setters

Requirments
Adhere to PEP8 and utilize proper and efficient code
Input validation
Utilize a __init__()
Ensure variables are correct type (class vs instance variables)
Utilize methods for getters and setters
Create an few instances of your class. Populate it with data utilzing a init and/or getters and setters
Split your classes into seperate files and import them properly

Additional:
Expand this program into a game or larger program. Some possible ideas:
Hero vs Villan
Battle Royal
Guess that Hero
etc
"""

#create class
class Person:
    """Creates the Person Class. Frank Castle is the default."""
    #create an init
    def __init__(self):
        self.name = "Francis 'Frank' Castle"
        self.age = 44
        self.hair = "Brown"
        self.eyes = "Blue"

    #function to print the default
    def defualt(self):
        print("{:_^20}").format("")
        print("Person: {}").format(self.name)
        print("{:_^20}").format("")
        print("Age: {}").format(int(self.age))
        print("{:_^20}").format("")
        print("Hair: {}").format(self.hair)
        print("{:_^20}").format("")
        print("Eyes: {}").format(self.eyes)
        print("{:_^20}").format("")

    #setters to create a new person
    def newPerson(name):
        self.name = name
    def newAge(age):
        self.age = age
    def newHair(hair):
        self.hair = hair
    def newEyes(eyes):
        self.eyes = eyes

    #getters for person
    def getPerson(self):
        return self.name

    def getAge(self):
        return self.age

    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes

#create class
class PersonV:
    """Creates the PersonV Class. Frank Castle is the default."""
    #create an init
    def __init__(self):
        self.name = "Victor Von Doom"
        self.age = 45
        self.hair = "Brown"
        self.eyes = "Brown"

    #function to print the default
    def defualt(self):
        print("{:_^20}").format("")
        print("Person: {}").format(self.name)
        print("{:_^20}").format("")
        print("Age: {}").format(int(self.age))
        print("{:_^20}").format("")
        print("Hair: {}").format(self.hair)
        print("{:_^20}").format("")
        print("Eyes: {}").format(self.eyes)
        print("{:_^20}").format("")

    #setters to create a new person
    def newPersonV(name):
        self.name = name
    def newAgeV(age):
        self.age = age
    def newHairV(hair):
        self.hair = hair
    def newEyesV(eyes):
        self.eyes = eyes

    #getters for person
    def getPersonV(self):
        return self.name

    def getAgeV(self):
        return self.age

    def getHairV(self):
        return self.hair

    def getEyesV(self):
        return self.eyes