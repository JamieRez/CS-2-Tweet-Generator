"""Program that randomly picks words from a Dictionary."""
import sys
import random
file = open("/usr/share/dict/web2", "r")
# User's choice of how many random words should be generated
numWords = int(sys.argv[1])

# Every word is separated by a newline
dictWords = file.readlines()

randWords = []
# Add a random word to randWords as many times as numWords
while(len(randWords) < numWords):
    randWords.append(dictWords[random.randint(0, len(dictWords))])

newStr = ""
for word in randWords:
    newStr += (word.rstrip() + " ")

print(newStr)
