import random

wrongGuessCount = 8

alreadyGuessed = []

letterDict = {}
letterList = []
word = ''


def hangman(file):
    displayWord(randomWord())


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
    print(f'letterList: {letterList}')
    print(f"letterDict: {letterDict}")
    return word


# input = input.upper(), if isalpha().len(1)

# if input in alreadyGuessed, let user know
# else alreadyGuessed.append(input)

# if guess is wrong, wrongGuessCount -= 1, display to user

# display function should loop through each letter in the list, and check the object. if true (guessed correctly) display the letter, if false (not yet guessed) display '_' in its place

def letterOrDash(word):
    print(f"47 lOD word: {word}")
    soFar = ''
    for i in range(len(word)):
        print(i)
        if letterDict[i]:
            soFar += letterList[i] + ' '
        else:
            soFar += '_ '
    return soFar


def displayWord(word):
    print(f"l57 So far you've got: {letterOrDash(word)}")

    # display should be run after each guess is computed

    # each time display is run, checkIfWonOrLost() should be run - if False not in wordObject keys, player has won. Otherwise check if wrongGuessCount = 0, in which case player has lost. Else, guess again.
    # ask if they want to play again - if so, reset wrongGuessCount, alreadyGuessed, wordObject, wordList, etc.


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
