#!/usr/bin/env python
"""guesser.py, by Kacper Kubicki - 2016
This program will let the user guess a number between 1 and 100!
"""

import random

def main():
    print "Guess a number between 1 and 100."



    randomNumber = random.randint(1, 100)
    userScore = 0


    found = False
    carryOnPlaying = False

    while not carryOnPlaying:
        while not found :
            userGuess = input("Your Guess: ")


            if userGuess == randomNumber:
                print "You got it!"
                found = True
                userScore += 1
            elif userGuess > randomNumber:
                print "Guess lower!"
            else:
                print "Guess higher!"

        print "Your score: %s" % userScore
        print " "
        print " "
        print " "
        print "Do you want to carry on Playing?"
        userAnswer = input("Your Answer: ")
        if userAnswer == True:
            carryOnPlaying = False
        else:
            carryOnPlaying = True


if __name__ == "__main__":
    main()
