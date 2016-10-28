#!/usr/bin/env python
"""guesser.py, by Kacper Kubicki - 2016
This program will let the user guess a number between 1 and 100!
"""

import random
import os

playerScore = 0

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    cls()
    print "______Main Menu______"
    print "__1. Start Game__"
    print "__2. Settings__"
    print "__3. Quit__"
    userChoice = input("Your choice: ")
    if userChoice == 1:
        game()
    if  userChoice == 2:
        print "There will be settings later!"
    if userChoice == 3:
        print "There will be a quit function"


def game():
    cls()
    found = False
    randomNumber = random.randint(1, 100)
    while not found:
        userGuess = input("Your Guess: ")

        if userGuess == randomNumber:
            print "You got it!"
            found = True
            global playerScore
            playerScore += 1
            gameQuestion()
        elif userGuess > randomNumber:
            print "Guess lower!"
        else:
            print "Guess higher!"





def gameQuestion():
    cls()
    global playerScore
    print "         Your Score is {}".format(playerScore)
    print "Do you want to carry on Playing?"
    userAnswer = input("Your Answer(y/n): ")
    if userAnswer == True:
        game()
    else:
        cls()
        print "         Thanks for playing!"
        print "         Your Final Score is {}".format(playerScore)


if __name__ == "__main__":
    main()
