"""
Name: Zackery Vering
Project: Lab 3C: Fun House
Date: 7 Sept 2018
Instructions
Create a text-based game where the user is navigating through a "Fun" House. Prompt the user to make a decision 
and using if/elif/else statements, give them different outcomes based on their answers. Begin with an introduction 
to your fun house and prompt the user to choose between at least three different options. You can use nested 
if/elif/else statements to make the game more complex.

Requirments
Adhere to PEP8 (Comments, formatting, style, etc)
Utilize userinput
Utilize proper formatting
Utilize proper and clean if/elif/else statements
Follow instructions above
Additional
Take this a step further. Use some previous concepts. Here are some things you can do:
Create a file that holds all of your prompts
Store file prompts into a list, dict, etc
Use if/elif/else statements to validate user input
Use formatting to create UI elements and/or fancy prompts
Use operators and user input to perform calculations based on prompts
etc"""

print("{:_^30}").format('')
print("{:_^30}").format('')
print("{:_^30}").format('FUN HOUSE')
print("{:_^30}").format('')
print("{:_^30}").format('')
print("Welcome to the Fun House!\nWhere all your nightmares become real! Your goal is to navigate through\nthe Fun House and reach the other side.")
print("Please sign a waiver before entering.")
print("{:_^30}").format('')
print("{:_^30}").format('WAIVER')
print("This waiver protects Nightmare Inc from liability due to ruined clothing,\nbodily harm, maiming, and loss of life.")
print("{:_^30}").format('')
print("1: Sign the waiver.")
print("2: Don't sign the waiver.")
choice = 0
chance = 0
game_over = 0
dead = 0
alive = 1
undead = 0
waiver_choice = int(raw_input("Do you sign the waiver?\n"))
while choice == 0:
    if waiver_choice == 2:
        print("Oh, so you're a chicken. I think the kiddie park is over that way.\nGoodbye.")
        choice = 2
    elif waiver_choice == 1:
        print("Welcome to the Fun House. Watch your step. Try not to die.")
        choice = 1
    else:
        print("{:_^30}").format('')
        print("You're not good with instructions, are you? *sigh* Look, you either sign the waiver or you don't. So, which is it?")
        print("1: Sign the waiver.")
        print("2: Don't sign the waiver.")
        waiver_choice = int(raw_input("Do you sign the waiver?\n"))
if choice == 1:
    while game_over == 0:
        print("{:_^30}").format('')
        print("You have stepped through the entrance of the Fun House.\n")
        print("You now stand in the first room. It is dimly lit. A ghostly blue\nskull floats in front of you.\n")
        print('"Greetings!! I am Moriarte!" the skull says. "I will be your guide\nthrough the fun house!"')
        print('"The path through here is treacherous. I hope you can make it\nthrough here alive. Or at least not dead dead."\n')
        print('"As you might have noticed, the door you came through is gone."\n"The only way out is forward."')
        print("Looking behind you, you realize that the door is indeed gone.")
        print('"Now, which way would you like to go?" Moriarte asks.')
        print("{:_^30}").format('')
        print("1: Door to the left.")
        print("2: Door straight ahead.")
        print("3: Door to the right.")
        room1_choice = int(raw_input("Which door do you pick?\n"))
        choice = 0
        while choice == 0:
            if chance == 3:
                print("{:_^30}").format('')
                print('"I tried to tell you to make a choice. But you refused to listen."\nMoriarte says disappointedly.')
                print("You watch as Moriarte opens his mouth wide. You feel the life start\n to drain out of you.")
                print("You watch helplessly as Moriarte consumes your very essence.")
                print('"I told you to make a choice." he says before he fades away leaving your lifeless corpse on the floor.')
                dead = 1
                alive = 0
                choice = 99
                game_over = 1
            else:
                if room1_choice == 1:
                    print("{:_^30}").format('')
                    print('"Hmm. Not sure that one was the right choice. But you decided."')
                    print("{:_^30}").format('')
                    choice = 1
                elif room1_choice == 2:
                    print("{:_^30}").format('')
                    print('"Oh. This is going to be fun!"')
                    print("{:_^30}").format('')
                    choice = 2
                elif room1_choice == 3:
                    print("{:_^30}").format('')
                    print('"Alright! On we go!"')
                    print("{:_^30}").format('')
                    choice = 3
                else:
                    chance += 1
                    print("{:_^30}").format('')
                    print('"Look. You have to choose something. So, which is it?"')
                    print("{:_^30}").format('')
                    print("1: Door to the left.")
                    print("2: Door straight ahead.")
                    print("3: Door to the right.")
                    room1_choice = int(raw_input("Which door do you pick?\n"))
        if room1_choice == 1:
            print("The room you enter is dimly lit by candles scattered along the walls. A\nfigure stands in the middle of the room.")
            print('"You best be deciding quick. Which way do you want to go?" Moriarte asks.')
            print("{:_^30}").format('')
            print("1: Door to the left.")
            print("2: Door straight ahead.")
            print("3: Door to the right.")
            room2_choice = int(raw_input("Which door do you pick?\n"))
            choice = 0
            while choice == 0:
                if chance == 3:
                    print("{:_^30}").format('')
                    print("The figure moves towards you with inhuman speed.")
                    print("You are grappled and feel a bite on your neck.")
                    print('After a few moments, "Welcome to my collection" the figure says.')
                    print('"You are now a thrall to the vampire. You should have listened and made a\nchoice" Moriarte tells you.')
                    undead = 1
                    alive = 0
                    choice = 99
                    game_over = 1
                else:
                    if room2_choice == 1:
                        print("{:_^30}").format('')
                        print('"This might get interesting."')
                        print("{:_^30}").format('')
                        print("You enter the pitch black room. As soon as the door closes behind you,\ndim lights flash on.")
                        print("Cages with zombies line all the other walls. The door behind you is gone.")
                        print('"Well, this looks bad" Moriarte says.')
                        print("You here the locks on the cages begin to click.")
                        print('"Well, it was nice knowing you" Moriarte says as the zombies start to\nexit their cages.')
                        print("Within moments, you are torn to pieces.")
                        dead = 1
                        alive = 0
                        choice = 1
                        game_over = 1

                    elif room2_choice == 2:
                        print("{:_^30}").format('')
                        print('"This is going to be fun!"')
                        print("{:_^30}").format('')
                        choice = 2
                    elif room2_choice == 3:
                        print("{:_^30}").format('')
                        print('"Alright. If you say so."')
                        print("{:_^30}").format('')
                        print("The room you enter is well lit and completely void.")
                        print('"Well, I had fun. Feel free to go for another round through. Take care\nnow." Moriarte says before disappearing.')
                        print("A door opens on the wall in front of you.")
                        choice = 3
                        game_over = 1
                    else:
                        chance += 1
                        print("{:_^30}").format('')
                        print('"Look. You have to choose something. So, which is it?"')
                        print("{:_^30}").format('')
                        print("1: Door to the left.")
                        print("2: Door straight ahead.")
                        print("3: Door to the right.")
                        room2_choice = int(raw_input("Which door do you pick?\n"))
        elif room1_choice == 2:
            room3_choice = 0
        elif room1_choice == 3:
            print("{:_^30}").format('')
            print("The room is pitch black. As you step forward, you begin to fall. After a\ncouple seconds you are impaled by spikes.")
            print('Moriarte begins to laugh.')
            print('"I know you were told to watch your step" he says.')
            dead = 1
            alive = 0
            game_over = 1
    if game_over == 1:
        if dead == 1 and alive != 1:
            print("{:=^30}").format('')
            print("You have died. Thanks for playing.")
            print("{:=^30}").format('')
        elif undead == 1 and alive != 1:
            print("{:=^30}").format('')
            print("You have become an undead. Your home is now within the Fun House.")
            print("{:=^30}").format('')
        elif alive == 1:
            print("{:=^30}").format('')
            print("Huh. You somehow managed to make it through the Fun House alive.\n\nCONGRATULATIONS!!!")
            print("{:=^30}").format('')
        else:
            print("{:=^30}").format('')
            print("Well, this is awkward. The game has ended. But your status is unknown.")
            print("{:=^30}").format('')
    else:
        print("{:=^30}").format('')
        print("Not sure what happened, but the program broke. Lucky you.")
        print("{:=^30}").format('')