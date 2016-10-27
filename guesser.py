#!/usr/bin/env python
"""guesser.py, by Kacper Kubicki - 2016
This program will let the user guess a number between 1 and 100!
"""

import random

def main():
    print "Guess a number between 1 and 100."
    randomNumber = random.randint(1, 100)
    found = False


    while not found :
        userGuess = input("Your Guess: ")


        if userGuess == randomNumber:
            print "You got it!"
            found = True
        elif userGuess > randomNumber:
            print "Guess lower!"
        else:
            print "Guess higher!"
    print "Thanks for playing!"



if __name__ == "__main__":
    main()
