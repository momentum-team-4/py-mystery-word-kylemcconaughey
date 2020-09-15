# TO PLAY, PLEASE ENSURE YOU'RE IN THIS DIRECTORY IN COMMAND LINE, AND ENTER 'python3 demon_words.py'

import math
import random
import os
with open('words.txt', 'rt') as infile:
    BLOB = infile.read().upper().split()
guessed = []
finalLength = 0
possWords = []
display = {}


def getWordLength():
    global finalLength
    global display
    wLength = input("How long a word would you like? --> ")
    while True:
        if wLength.isnumeric():
            print(f"You chose {wLength}")
            finalLength = int(wLength)
            for i in range(finalLength):
                display[i] = None
            print(f"display = {display}")
            return wLength
        else:
            wLength = input("Please enter a number: ")


def initialWords(num=getWordLength()):
    global possWords
    possWords = [x for x in BLOB if len(x) == int(num)]
    print(possWords)
    return possWords


def guessLetter():
    displayState()
    global guessed
    if not '_' in letterOrDash():
        playAgain()
    else:
        guess = input("Guess a letter --> ").upper()
        if guess in ['.', '-', ',', '/', '?'] or not guess.isalpha() or len(guess) > 1:
            print('Please guess A LETTER --> ')
            guessLetter()
        elif guess in guessed:
            print(
                f"You've already guessed these: {printGuessed()} -- Try a different one.")
            guessLetter()
        else:
            guessed.append(guess)
            pareWords(guess)


def pareWords(guess):
    global possWords
    newList = biggestFamily(guess)
    possWords = newList
    print(possWords)
    guessLetter()


def displayState():
    # os.system('clear')
    letterOrDash()
    if not '_' in letterOrDash():
        print("Congrats")
        playAgain()
    else:
        print(
            f"You have guessed these letters: {printGuessed()}. You've guessed {len(guessed)} times. Guess again!")


def biggestFamily(guess):
    global display
    bigFam = []
    global possWords
    for el in range(finalLength):
        if display[el] == None:
            bigFam.append([x for x in possWords if x[el] == guess])
    bigFam.append([x for x in possWords if guess not in x])
    newFam = max(bigFam)
    for el in range(finalLength):
        if newFam[0][el] == guess:
            display[el] = guess
    return newFam


def printGuessed():
    result = ''
    for i in range(len(guessed)):
        result += guessed[i] + ', '
    return result


def letterOrDash():
    soFar = ''
    for i in range(finalLength):
        if display[i] == None:
            soFar += '_ '
        else:
            soFar += display[i]
    return soFar


def playDemonGame():
    while True:
        if not '_' in letterOrDash():
            playAgain()
            return
        else:
            guessLetter()


def playAgain():
    global possWords
    global guessed
    global finalLength
    global display
    if not '_' in letterOrDash():
        print(
            f"Good job, you narrowed it down to {letterOrDash()} ----- Play again?")
    again = input("Y/N --> ").lower()
    if again == 'y':
        possWords = []
        guessed = []
        finalLength = 0
        display = {}
        playDemonGame()
    else:
        print("The devil always wins")
        exit()


if __name__ == "__main__":
    initialWords()
    playDemonGame()
