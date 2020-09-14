# TO PLAY, PLEASE ENSURE YOU'RE IN THIS DIRECTORY IN COMMAND LINE, AND ENTER 'python3 demon_words.py'

import math
import random
import os
with open('words.txt', 'rt') as infile:
    blob = infile.read().upper().split()
level1 = [x for x in blob if len(x) >= 3 and len(x) <= 5]
level2 = [x for x in blob if len(x) >= 6 and len(x) <= 8]
level3 = [x for x in blob if len(x) >= 8 and len(x) <= math.inf]
level4 = [x for x in blob if len(x) > 15 and len(x) < math.inf]
level0 = [x for x in blob if len(x) < 4]
guessed = []
wrongGuesses = 8
