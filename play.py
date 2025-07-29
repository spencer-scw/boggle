from dict import BoggleDictionary
from board import Board
from frontend import show_frontend

import time
from copy import deepcopy

def new_game(lang='english', time_sec=150):
    show_frontend(lang, time_sec)

def help():
    print("This is a Boggle game built in Python on the command line. It might have LAN multiplayer one day.")
    print("When you start a new game, a timer will begin and a boggle grid is printed. Type words on the command line that can be formed by chaining together the letters in cardinal or diagonal directions (no repeats). At the end of the timer, the program will check if your words are valid and assign points based on the length and number of valid words found.")
    print("The computer will also show you all of the possible words that you missed.")


