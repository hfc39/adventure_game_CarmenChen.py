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
