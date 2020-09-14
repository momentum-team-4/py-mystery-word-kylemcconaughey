import random
import os
file = open('words.txt')
wrongGuessCount = 8

alreadyGuessed = []

letterDict = {}
word = ''


def hangman(file):
    word = randomWord()
    print(word)
    guessLetter()


def playAgain():
    global wrongGuessCount
    global alreadyGuessed
    global letterDict
    global word
    wrongGuessCount = 0
    alreadyGuessed = []
    letterDict = {}
    word = ''
    hangman(file)


def randomWord(difficulty=int(input('Enter the difficulty you would like... 1, 2, or 3: '))):
    blob = file.read()

    if difficulty == 1:
        minLength = 4
        maxLength = 6
    elif difficulty == 2:
        minLength = 6
        maxLength = 8
    elif difficulty == 3:
        minLength = 8
        maxLength = 50
    allWords = blob.upper().split()
    global wordList
    wordList = [x for x in allWords if len(
        x) <= maxLength and len(x) >= minLength]
    global word
    word = random.choice(wordList)
    global letterDict
    for i in word:
        letterDict[i] = False

    return word


def guessLetter(guess=input("Guess a letter! --> ")):
    global wrongGuessCount
    if all(letterDict.values()) or wrongGuessCount == 0:
        checkIfWonOrLost()
        return
    else:
        if guess in ['.', '-', ',', '/', '?'] or not guess.isalpha():
            guessLetter(guess=input(f"Guess a LETTER! --> "))
        else:
            if len(guess) > 1:
                guessLetter(guess=input(f"Guess A (single) letter! --> "))
        guess = guess.upper()
        if guess in alreadyGuessed:
            print(
                f"You've already guessed these: {printGuessedLetters(alreadyGuessed)} -- Try a different one!")
            guessLetter(guess=input(f"Guess a letter! --> "))

        else:
            alreadyGuessed.append(guess)
            if guess in letterDict.keys():
                letterDict[guess] = True
                if all(letterDict.values()):
                    print("======== Congratulations! You won =) ========")
                    return
                else:
                    displayWord(word)
                    guessLetter(guess=input(
                        f"Good job! Guess another letter! --> "))
            else:
                wrongGuessCount -= 1
                displayWord(word)
                if wrongGuessCount > 0:
                    print(
                        f"Whoops, '{guess}' wasn't in the word. You've got {wrongGuessCount} guesses left. Make 'em count!")
                    guessLetter(guess=input(
                        f"Try and guess another letter! --> "))


def printGuessedLetters(ls):
    result = ''
    for i in range(len(ls)):
        result += alreadyGuessed[i] + ' '
    return result


def letterOrDash(word):
    print(f"(Word: {word})")
    soFar = ''
    for i in range(len(word)):
        # print(i)
        if letterDict[word[i]]:
            soFar += word[i] + ' '
        else:
            soFar += '_ '
    return soFar


def displayWord(word):
    os.system('clear')
    print(f"So far: {letterOrDash(word)}")
    checkIfWonOrLost()


def checkIfWonOrLost():
    if all(letterDict.values()):
        print("======== Congratulations! You won =) ========")
    else:
        if wrongGuessCount == 0:
            print(
                f"Oh no! You lost =( The word was: {word}. Better luck next time.")


if __name__ == "__main__":
    hangman(file)
