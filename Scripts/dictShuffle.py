"""Program that randomly picks words from a Dictionary."""
import sys
import random
import time
file = open("/usr/share/dict/web2", "r")
# User's choice of how many random words should be generated
numWords = int(sys.argv[1])

# Every word is separated by a newline
dictWords = file.readlines()

randWords = []
# Add a random word to randWords as many times as numWords


def getWords():
    start_time = time.time()
    while(len(randWords) < numWords):
        randWords.append(dictWords[random.randint(0, len(dictWords) - 1)])

    newStr = ""
    for word in randWords:
        newStr += (word.rstrip() + " ")
    end_time = time.time() - start_time
    print(newStr)
    print(float(end_time))


getWords()
