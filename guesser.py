#!/usr/bin/env python
"""guesser.py, by Kacper Kubicki - 2016
This program will let the user guess a number between 1 and 100!
"""

import random
import os
import sys

playerScore = 0
language = 0 # 0 is english 1 is polish

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
        cls()
        global language
        print "__LANGUAGE SELECTION__"
        print "1. English"
        print "2. Polish"
        print "3. Exit without change"
        language = input("Your choice(1/2/3): ")
        if language == 1:
            main()
        if language == 2:
            main_pl()
        if language == 3:
            main()

    if userChoice == 3:
        sys.exit()

def main_pl():
    cls()
    print "______Menu Glowne______"
    print "__1. Zacznij rozgrywke__"
    print "__2. Ustawienia__"
    print "__3. Wyjdz__"
    userChoice = input("Twoj wybor: ")
    if userChoice == 1:
        game_pl()
    if  userChoice == 2:
        cls()
        global language
        print "__Wybor Jezyka__"
        print "1. Angielski"
        print "2. Polski"
        print "3. Wyjdz bez zmiany"
        language = input("Twoj wybor(1/2/3): ")
        if language == 1:
            main()
        if language == 2:
            main_pl()
        if language == 3:
            main_pl()

    if userChoice == 3:
        sys.exit()


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


def game_pl():
    cls()
    found = False
    randomNumber = random.randint(1, 100)
    while not found:
        userGuess = input("Zgadnij liczbe: ")

        if userGuess == randomNumber:
            print "Zgadles liczbe!"
            found = True
            global playerScore
            playerScore += 1
            gameQuestion_pl()
        elif userGuess > randomNumber:
            print "Zgaduj nizej!"
        else:
            print "Zgaduj wyzej!"




def gameQuestion():
    cls()
    global playerScore
    print "         Your Score is {}".format(playerScore)
    print "Do you want to carry on Playing?"
    userAnswer = input("Your Answer(True/False): ")
    if userAnswer == True:
        game()
    else:
        cls()
        print "         Thanks for playing!"
        print "         Your Final Score is {}".format(playerScore)
        sys.exit()


def gameQuestion_pl():
    cls()
    global playerScore
    print "         Twoj wynik: {}".format(playerScore)
    print "Chcesz grac dalej?"
    userAnswer = input("Twoj wybor(True/False): ")
    if userAnswer == True:
        game_pl()
    else:
        cls()
        print "         Dzieki za rozgrywke!"
        print "         Twoj ostateczny wynik to: {}".format(playerScore)
        sys.exit()


if __name__ == "__main__":
    main()
