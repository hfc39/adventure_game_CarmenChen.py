import time
import random
items = []


def printpause(text):
    print(text)
    time.sleep(1)


def intro():
    printpause("You are Prince Charming of Kindom Far Far Away.\n")
    printpause("You travel to the Ogretown to rescue the beautiful princess"
               " who was taken by the ogres.\n")
    printpause("She was trapped in the Ogre Castle,"
               " and here you are at the gate of the Ogre Castle.\n")
    printpause("You enter the creepy castle.\n"
               "Right in front of you is a stairway that heads to 2nd floor"
               " and on your right hand cornor, you see a dark study room.\n")


def first_floor(items):
    first = input("Enter 1 to go on the stairway.\n"
                  "Enter 2 to go to the study room.\n"
                  "What would you like to do?\n"
                  "(Please enter 1 or 2.)\n")
    if first == '2':
        if 'key' in items:
            printpause("You've been here before."
                       " There is nothing usable here.")
            printpause("You are back to the entrance on the castle.\n")
            first_floor(items)
        else:
            printpause("You are in the study room"
                       " and you see something shining on the old bookshelf."
                       " It's a key.\n")
            printpause("You put the key in your pocket"
                       " and head back to the castle entrance.\n")
            printpause("You are back to the castle entrance.\n")
            items.append("key")
            first_floor(items)
    elif first == '1':
        second_floor(items)
    else:
        printpause("(Please enter 1 or 2.)\n")
    first_floor(items)


def second_floor(items):
    printpause("\nYou go through the stairway and now on the 2nd floor.\n")
    printpause("You see 3 doors in front of you."
               " You have to choose one to enter.\n")
    second = input("Enter 1 to choose the red door.\n"
                   "Enter 2 to choose the blue door.\n"
                   "Enter 3 to choose the yellow door.\n"
                   "What would you like to do?\n"
                   "(Please enter 1,2 or 3)\n")
    if second == '1':
        printpause("\nThere is an ogre behind the red door,"
                   " the orge attacked you.\n")
        printpause("You are dead from Ogre attack, bye bye")
        play_again()
    elif second == '2':
        if 'sword' in items:
            printpause("You've been here before and took what was here."
                       " You will be back to the entrance on 2nd floor.")
        else:
            printpause("\nYou open the blue door and see a big sword,"
                       " you grab the sword and go back to the 2F entrance.")
            items.append("sword")
        second_floor(items)
    elif second == '3':
        printpause("You see another stairway head to the 3rd floor,"
                   " and you bravely proceed.\n")
        third_floor(items)
    else:
        printpause("(Please enter 1,2 or 3)")
    second_floor(items)

def third_floor(items):
    beast = random.choice(["dragon", "python", "bear"])
    printpause(f"You are on the 3rd floor and see a {beast} guarding a door.")
    printpause(f"The {beast} finds you and is ready to attack you.")
    three = input(f"Would you like to (1) fight the {beast} or (2) run away?"
                  " Please enter 1 or 2.\n")
    if three == '2':
        printpause("You luckily escaped."
                   " You get back to the entrance of the castle.")
        first_floor(items)
    elif three == '1':
        if "sword" in items:
            printpause(f"You pull out the sword and kill the {beast}")
            printpause("You are now in front of the locked door"
                       " where you can hear the princess crying for help.")
            if 'key' in items:
                printpause("You use the key to open the door,"
                           " and successfully rescue the Princess.")
                printpause("You win the game!")
                play_again()
            else:
                printpause("Oh no! You don't have the key to open the door,"
                           " you rush back to first floor to find it"
                           " as the Princess awaits.")
                first_floor(items)
        else:
            time.sleep(2)
            printpause(f"Oops! You don't have a weapon to fight the {beast}.")
            printpause("You have to go back to the gate to find it"
                       "You go back to the entrance of the castle.")
            first_floor(items)


def play_game(items):
    intro()
    first_floor(items)


def play_again():
    again = input("Would you like to play the game again? Y/N\n").lower()
    while True:
        if again == 'y':
            play_game(items=[])
        elif again == 'n':
            exit()
        else:
            printpause("Please enter Y or N.")
            play_again()


play_game(items)
