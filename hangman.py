import random

wrongGuessCount = 8

alreadyGuessed = []

letterDict = {}
letterList = []
word = ''


def hangman(file):
    randomWord()
    guessLetter()


# def open words.txt, read them into blob
# def select random word - must take difficulty input
def randomWord(difficulty=int(input('Enter the max length of word you would like: '))):
    with open(file, 'rt') as infile:
        blob = infile.read()

    allWords = blob.upper().split()
    global wordList
    wordList = [x for x in allWords if len(x) <= difficulty]
    global word
    word = random.choice(wordList)
    global letterList
    letterList = [x for x in word]
    global letterDict
    for i in range(len(word)):
        letterDict[i] = False
    # print(f'letterList: {letterList}')
    # print(f"letterDict: {letterDict}")
    return word


# input = input.upper(), if isalpha().len(1)

def guessLetter(guess=input(f"Guess a letter! --> ")):
    guess = guess.upper()
    if guess in alreadyGuessed:
        print(
            f"You've already guessed these letters: {printGuessedLetters(alreadyGuessed)} -- Try a different one!")
        guessLetter(guess=input(f"Guess a letter! --> "))

    else:
        alreadyGuessed.append(guess)
        if guess in letterList:
            # print("That's a letter!")
            ind = [i for i in range(len(letterList)) if letterList[i] == guess]
            for i in ind:
                letterDict[i] = True
            displayWord(word)
            if checkIfWonOrLost():
                print("======== Congratulations! You won! ========")
                return
            else:
                guessLetter(guess=input(f"Guess a letter! --> "))
        else:
            global wrongGuessCount
            wrongGuessCount -= 1
            print(f"Wrong guesses left: {wrongGuessCount}")
            if wrongGuessCount == 0:
                checkIfWonOrLost()
                return
            displayWord(word)
            guessLetter(guess=input(f"Guess a letter! --> "))


def printGuessedLetters(ls):
    result = ''
    for i in range(len(ls)):
        result += alreadyGuessed[i] + ' '
    return result

# if input in alreadyGuessed, let user know
# else alreadyGuessed.append(input)

# if guess is wrong, wrongGuessCount -= 1, display to user

# display function should loop through each letter in the list, and check the object. if true (guessed correctly) display the letter, if false (not yet guessed) display '_' in its place


def letterOrDash(word):
    print(f"Word: {word}")
    soFar = ''
    for i in range(len(word)):
        # print(i)
        if letterDict[i]:
            soFar += letterList[i] + ' '
        else:
            soFar += '_ '
    return soFar


def displayWord(word):
    print(f"So far: {letterOrDash(word)}")
    checkIfWonOrLost()

    # display should be run after each guess is computed

    # each time display is run, checkIfWonOrLost() should be run - if False not in wordObject keys, player has won. Otherwise check if wrongGuessCount = 0, in which case player has lost. Else, guess again.
    # ask if they want to play again - if so, reset wrongGuessCount, alreadyGuessed, wordObject, wordList, etc.


def checkIfWonOrLost():
    if all(letterDict.values()):
        return True
    else:
        if wrongGuessCount == 0:
            print("Oh no =( You lost.")


        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
        #
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Hangman!')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        hangman(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
