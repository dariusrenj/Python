"""
Name: Zackery Vering
Project: Lab 5B
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
import hero
import villian

a=hero.Hero()
b=villian.Villian()
c=hero.wol
user_hero = hero.Hero()
user_villian = villian.Villian()
user_created1 = 0
user_created2 = 0
print("Default Hero")
hero.Hero.default(a)
print("Defualt Villian")
villian.Villian.default(b)
c.default()
print("Would you like to create a new hero?")
user_input = raw_input("(Y/N)\n").lower()
create_new = 0
while(create_new == 0):
    if (user_input == "y"):
        user_created1 = 1
        print("User wants to create a new Hero.")
        user_hero.newHero(raw_input("What is your hero's name?\n"))
        user_hero.newRealName(raw_input("What is your hero's real name?\n"))
        user_hero.newHair(raw_input("What color is your hero's hair?\n"))
        user_hero.newEyes(raw_input("What color are your hero's eyes?\n"))
        user_hero.newAge(int(raw_input("How old is your hero?\n")))
        power_input = 0
        user_hero.powers = [""]
        user_hero.colors = [""]
        powers = [""]
        while (power_input == 0):
            if (powers == [""]):
                powers = [raw_input("What is your hero's power?\n")]
            else:
                powers.append(raw_input("What is your hero's power?\n"))
            print("Would you like to add another power?\n")
            user_power = raw_input("(Y/N)\n").lower()
            if (user_power != 'y'):
                if (user_power == 'n'):
                    user_hero.newHeroPowers(powers)
                    power_input = 1
                else:
                    print("That was an invalid response. So, your response has defaulted to 'no'.")
                    user_hero.newHeroPowers(powers)
                    power_input = 1
        color_input = 0
        colors = [""]
        while (color_input == 0):
            if (colors == [""]):
                colors = [raw_input("What is your hero's color?\n")]
            else:
                colors.append(raw_input("What is your hero's color?\n"))
            print("Would you like to add another color?\n")
            user_colors = raw_input("(Y/N)\n").lower()
            if (user_colors != 'y'):
                if (user_colors == 'n'):
                    user_hero.newColors(colors)
                    color_input = 1
                else:
                    print("That was an invalid response. So, your response has defaulted to 'no'.")
                    user_hero.newColors(colors)
                    color_input = 1
        create_new = 1
    elif (user_input == "n"):
        print("Would you like to create a new villian?\n")
        user_input2 = raw_input("(Y/N)\n").lower()
        create_new2 = 0
        while(create_new2 == 0):
            if (user_input2 == "y"):
                print("User wants to create a new Villian.")
                user_villian.newVillian(raw_input("What is your villian's name?\n"))
                user_villian.newRealName(raw_input("What is your villian's real name?\n"))
                user_villian.newHair(raw_input("What color is your villian's hair?\n"))
                user_villian.newEyes(raw_input("What color are your villian's eyes?\n"))
                user_villian.newAge(int(raw_input("How old is your villian?\n")))
                power_input = 0
                user_villian.powers = [""]
                user_villian.colors = [""]
                powers = [""]
                while (power_input == 0):
                    if (powers == [""]):
                        powers = [raw_input("What is your villian's power?\n")]
                    else:
                        powers.append(raw_input("What is your villian's power?\n"))
                    print("Would you like to add another power?\n")
                    user_power = raw_input("(Y/N)\n").lower()
                    if (user_power != 'y'):
                        if (user_power == 'n'):
                            user_villian.newVillianPowers(powers)
                            power_input = 1
                        else:
                            print("That was an invalid response. So, your response has defaulted to 'no'.")
                            user_villian.newVillianPowers(powers)
                            power_input = 1
                color_input = 0
                colors = [""]
                while (color_input == 0):
                    if (colors == [""]):
                        colors = [raw_input("What is your hero's color?\n")]
                    else:
                        colors.append(raw_input("What is your hero's color?\n"))
                    print("Would you like to add another color?\n")
                    user_colors = raw_input("(Y/N)\n").lower()
                    if (user_colors != 'y'):
                        if (user_colors == 'n'):
                            user_villian.newColors(colors)
                            color_input = 1
                        else:
                            print("That was an invalid response. So, your response has defaulted to 'no'.")
                            user_villian.newColors(colors)
                            color_input = 1
                user_created2 = 1
                create_new2 = 1
            elif (user_input2 == "n"):
                print("User doesn't want to create a new Villian either.")
                create_new2 = 1
            else:
                print("That was an invalid response. Please try again.")
                print("Would you like to create a new villian?\n")
                user_input2 = raw_input("(Y/N)\n").lower()
        create_new = 1
    else:
        print("That was an invalid response. Please try again.")
        print("Would you like to create a new hero?\n")
        user_input = raw_input("(Y/N)\n").lower()
if (user_created1 == 1):
    user_hero.default()
if (user_created2 == 1):
    user_villian.default()
    