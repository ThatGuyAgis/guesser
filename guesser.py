#!/usr/bin/env python
"""guesser.py, by Kacper Kubicki - 2016
This program will let the user guess a number between 1 and 100!
"""

import random
import os
import sys



playerScore = 0
language = 0 # 0 is english 1 is polish




>>>>>>> Stashed changes

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def check(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Invalid input! Please use: ")

def check_pl(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Blad! Uzyj:  ")

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except:
            cls()
            print("Not an option(has to be a number provided above)")
            continue
        else:
            return userInput
            break

def inputNumber_pl(message):
    while True:
        try:
            userInput = int(input(message))
        except:
            cls()
            print("Zly Wybor!(Musisz wybrac liczbe podana powyzej)")
            continue
        else:
            return userInput
            break



def main():
    cls()
    print "______Main Menu______"
    print "__1. Start Game__"
    print "__2. Settings__"
    print "__3. Quit__"
    userChoice = inputNumber("Your choice: ")
    if 1 <= int(userChoice) <= 3:
        if userChoice == 1:
            game()
        if userChoice == 2:
            langSelect()
        if userChoice == 3:
            sys.exit()
    else:
        main()



def main_pl():
    cls()
    print "______Menu Glowne______"
    print "__1. Zacznij rozgrywke__"
    print "__2. Ustawienia__"
    print "__3. Wyjdz__"
    userChoice = inputNumber("Twoj wybor: ")
    if 1 <= int(userChoice) <= 3:
        if userChoice == 1:
            game_pl()
        if userChoice == 2:
            langSelect_pl()
        if userChoice == 3:
            sys.exit()
    else:
        main_pl()

def langSelect_pl():
    cls()
    global language
    print "__Wybor Jezyka__"
    print "1. Angielski"
    print "2. Polski"
    print "3. Wyjdz bez zmiany"
    language = inputNumber("Twoj wybor: ")
    if 1 <= int(language) == 3:
        if language == 1:
            main()
        if language == 2:
            main_pl()
        if language == 3:
            main_pl()
    else:
        langSelect_pl()
def langSelect():
    cls()
    global language
    print "__LANGUAGE SELECTION__"
    print "1. English"
    print "2. Polish"
    print "3. Exit without change"
    language = inputNumber("Your choice(1/2/3): ")
    if 1 <= int(language) <= 3:
        if language == 1:
            main()
        if language == 2:
            main_pl()
        if language == 3:
            main()
    else:
        langSelect()


def game():
    cls()
    print "___Goal of the Game: Guess a number between 1 and 100___"
    print "___Score points and spend them as i add features___"
    found = False
    randomNumber = random.randint(1, 100)
    while not found:
        userGuess = inputNumber("Your Guess: ")

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
        userGuess = inputNumber("Zgadnij liczbe: ")

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
    #userAnswer = input("Your Answer(Yes/No): ").lower()
    if check("Your Answer:") == True:
        game()
    else:
        cls()
        print "         Thank you for playing!!"
        print "         Your final score: {}".format(playerScore)
        sys.exit()


def gameQuestion_pl():
    cls()
    global playerScore
    print "         Twoj wynik: {}".format(playerScore)
    print "Chcesz grac dalej?"
    #userAnswer = input("Twoj wybor(True/False): ")
    if check_pl("Twoj wybor") == True:
        game_pl()
    else:
        cls()
        print "         Dzieki za rozgrywke!"
        print "         Twoj ostateczny wynik to: {}".format(playerScore)
        sys.exit()


if __name__ == "__main__":
    main()
