import random
import os
file = open('words.txt')
blob = file.read().upper().split()
level1 = [x for x in blob if len(x) >= 4 and len(x) <= 6]
level2 = [x for x in blob if len(x) >= 6 and len(x) <= 8]
level3 = [x for x in blob if len(x) >= 8 and len(x) <= 20]
guessed = []
wrongGuesses = 8


def selectDifficulty():
    global guessed
    guessed = []
    difficulty = input("Enter the difficulty you'd like - 1, 2, or 3: ")
    if difficulty == '1':
        word = random.choice(level1)
    elif difficulty == '2':
        word = random.choice(level2)
    elif difficulty == '3':
        word = random.choice(level3)
    # else:
    #     selectDifficulty()
    print(f"Your word has {len(word)} letters in it. Good luck!")
    return word


def printGuessed(ls):
    result = ''
    for i in range(len(ls)):
        result += ls[i] + ' '
    return result


def guessLetter(word):
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
                f"Sorry, '{guess}' wasn't in the word. You've got {wrongGuesses} left, make 'em count!")
            guessLetter(word)
        else:
            displayWord(word)
            print("Nice guess!")
            guessLetter(word)
    return guess


def guessedWrong():
    global wrongGuesses
    wrongGuesses -= 1


def letterOrDash(word):
    print(f"(Word: {word})")
    soFar = ''
    for i in range(len(word)):
        if word[i] in guessed:
            soFar += word[i]
        else:
            soFar += '_ '
    return soFar


def displayWord(word):
    os.system('clear')
    print(f"So far: {letterOrDash(word)}")


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
        print("Congrats! Play again?")
    again = input("Y/N --> ").upper()
    if again == 'Y':
        wrongGuesses = 8
        playGame(wrongGuesses, selectDifficulty())
    else:
        print("See ya later sk8r")
        exit()


if __name__ == "__main__":
    playGame(wrongGuesses, selectDifficulty())
