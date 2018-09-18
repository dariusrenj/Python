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
from person import Person

#create class
class Hero(Person):
    """Creates the Hero Class. The Punisher is the default."""
    #create an init
    def __init__(self):
        Person.__init__(self)
        self.heroName = "The Punisher"
        self.powers = ["Skilled in guerrilla and military tactics", 
        "Close quarters combat", "Infiltration", "Marksmanship",
        "Demolitions", "Really really angry"]
        self.colors = ["Black", "White"]

    #function to print the default
    def default(self):
        print("{:_^20}").format("")
        print("Hero: {}").format(self.heroName)
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

    #setters to create a new hero
    def newHero(self, name):
        self.heroName = name
    def newRealName(self, realName):
        self.name = realName
    def newHeroPowers(self, power):
        self.powers = power
    def newColors(self, colors):
        self.colors = colors
    def newAge(self, age):
        self.age = age
    def newHair(self, hair):
        self.hair = hair
    def newEyes(self, eyes):
        self.eyes = eyes

    #getters for hero
    def getHero(self):
        return self.heroName

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

wol = Hero()
wol.heroName = "Wolverine"
wol.name = "John Logan"
wol.hair = "Brown"
wol.colors = ["Yellow", "Black"]
wol.powers = ["Superhuman senses, agility, reflexes, and\
 animal-like attributes", "Regenerative healing factor", "Retractable\
 bone claws", "Adamantium-plated skeleton", "Skilled in hand-to-\
hand combat"]
wol.age = 130