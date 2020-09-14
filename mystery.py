# TO PLAY, PLEASE ENSURE YOU'RE IN THIS DIRECTORY IN COMMAND LINE, AND ENTER 'python3 mystery.py'
import math
import random
import os
from drawing import drawn
with open('words.txt', 'rt') as infile:
    blob = infile.read().upper().split()
level1 = [x for x in blob if len(x) >= 3 and len(x) <= 5]
level2 = [x for x in blob if len(x) >= 6 and len(x) <= 8]
level3 = [x for x in blob if len(x) >= 8 and len(x) <= math.inf]
level4 = [x for x in blob if len(x) > 15 and len(x) < math.inf]
level0 = [x for x in blob if len(x) < 4]
guessed = []
wrongGuesses = 8


def selectDifficulty():
    global guessed
    global word
    guessed = []
    difficulty = input(
        "Choose difficulty... 1 (for easy), 2 (for medium), or 3 (for hard): ")

    while True:
        if difficulty in ['1', '2', '3', '0', '4']:
            word = random.choice(eval('level' + difficulty))
            break
        else:
            difficulty = input("Please choose between only 1, 2, and 3: ")
    # print(f"(Word: {word})")
    print(f"Your word has {len(word)} letters in it. Good luck!")
    return word


def guessLetter(word):
    print(f"(Word: {word})")
    global wrongGuesses
    if wrongGuesses == 0 or not '_' in letterOrDash(word):
        playAgain(word)
    guess = input("Guess a letter --> ").upper()
    if guess in ['.', '-', ',', '/', '?'] or not guess.isalpha() or len(guess) > 1:
        print('Please guess A LETTER --> ')
        guessLetter(word)
    elif guess in guessed:
        print(
            f"You've already guessed these: {printGuessed(guessed)} -- Try a different one.")
        guessLetter(word)
    else:
        guessed.append(guess)
        if guess not in word:
            guessedWrong()
            displayWord(word)
            print(
                f"Sorry, '{guess}' wasn't in the word. You've got {wrongGuesses} guesses left, make 'em count!")
            guessLetter(word)
        else:
            displayWord(word)
            print("Nice guess!")
            guessLetter(word)
    return guess


def printGuessed(ls):
    result = ''
    for i in range(len(ls)):
        result += ls[i] + ' '
    return result


def guessedWrong():
    global wrongGuesses
    wrongGuesses -= 1


def letterOrDash(word):
    soFar = ''
    for i in range(len(word)):
        if word[i] in guessed:
            soFar += word[i]
        else:
            soFar += '_ '
    return soFar


def displayWord(word):
    os.system('clear')
    print(
        f"So far, you've got {letterOrDash(word)} and have guessed these letters: {', '.join(x for x in guessed)}")
    global wrongGuesses
    drawn(wrongGuesses)


def playGame(wrongGuesses, word):
    while True:
        if wrongGuesses == 0 or not '_' in letterOrDash(word):
            wrongGuesses = 8
            playAgain(word)
            return
        else:
            guessLetter(word)


def playAgain(word):
    global wrongGuesses
    if wrongGuesses == 0:
        print(f"Sorry, the word was {word}, play again?")
    elif not '_' in letterOrDash(word):
        print(f"Congrats! You figured out it was '{word}' ---- Play again?")
    again = input("Y/N --> ").upper()
    if again == 'Y':
        wrongGuesses = 8
        nW = selectDifficulty()
        playGame(wrongGuesses, nW)
    else:
        print("See ya later sk8r")
        exit()


if __name__ == "__main__":
    playGame(wrongGuesses, selectDifficulty())
