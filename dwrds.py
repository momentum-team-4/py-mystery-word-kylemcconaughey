# TO PLAY, PLEASE ENSURE YOU'RE IN THIS DIRECTORY IN COMMAND LINE, AND ENTER 'python3 demon_words.py'

import math
import random
import os
with open('words.txt', 'rt') as infile:
    BLOB = infile.read().upper().split()
guessed = []
wrongGuesses = 0
finalLength = 0


def getWordLength():
    global finalLength
    wLength = input("How long a word would you like? --> ")
    while True:
        if wLength.isnumeric():
            print(f"You chose {wLength}")
            finalLength = wLength
            return wLength
        else:
            wLength = input("Please enter a number: ")


def initialWords(num=getWordLength()):
    possWords = [x for x in BLOB if len(x) == int(num)]
    print(possWords)
    return possWords


def guessLetter():
    global guessed
    if not '_' in letterOrDash():
        playAgain()
    guess = input("Guess a letter --> ").upper()
    if guess in ['.', '-', ',', '/', '?'] or not guess.isalpha() or len(guess) > 1:
        print('Please guess A LETTER --> ')
        guessLetter()
    elif guess in guessed:
        print(
            f"You've already guessed these: {printGuessed(guessed)} -- Try a different one.")
        guessLetter()
    else:
        guessed.append(guess)
        pareWords(guess)


def pareWords(guess):
    """
    -input: a single letter
    -make a number of families equal to the number of unguessed letters + 1
    -each family has the number of possible words with the input in a specific index
    -the last family has the list of words that don't have the input in them
    -possWords = largest family
    -output: the index of the largest family
    ----or False otherwise
    """
    pass


def printGuessed(ls):
    result = ''
    for i in range(len(ls)):
        result += ls[i] + ' '
    return result


def letterOrDash():
    pass


def playDemonGame():
    while True:
        if not '_' in letterOrDash():
            playAgain()
            return
        else:
            guessLetter()


def playAgain():
    if not '_' in letterOrDash():
        print(f"Good job, you narrowed it down to WORD-GOES-HERE ----- Play again?")
    again = input("Y/N --> ").lower()
    if again == 'y':
        possWords = []
        playDemonGame()
    else:
        print("The devil always wins")
        exit()


if __name__ == "__main__":
    initialWords()
