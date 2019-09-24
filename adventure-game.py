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
