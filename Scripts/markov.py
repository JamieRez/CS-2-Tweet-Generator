"""Get Sentence Generating Functionality."""
from histogram import histogramDict
import re
import random
corpusTextPath = "/Users/James/Downloads/bookOfText.txt"


def chainGram(bookFile):
    """Return a Dictionary of Chained Words."""
    book = open(bookFile)
    # open bookfile
    book = open(bookFile)
    # Which characters should be filtered out of of the words
    regex = re.compile('[,\.!?:/$()@]')
    # Filter out the read words, lowercase them, and put them into an array
    bookWords = regex.sub('', book.read().lower()).split()

    uniqueChain = []
    chaingram = []

    for i, word in enumerate(bookWords):
        # Words with letters only
        if not word.isdigit() and word.isalpha():
            prevWord = bookWords[i-1]
            chain = [prevWord, word]
            if chain not in uniqueChain:
                uniqueChain.append(chain)
                chaingram.append([chain, 1])
            else:
                chaingram[uniqueChain.index(chain)][1] += 1

    return chaingram


def getNewWord(chaingram, curWord, numOfWords, i):
    if i < numOfWords:



def makeRandomChain(chaingram, wordNum):
    """Generate a random pattern of words using the chaingram."""
    sentenceList = []
    curWord = random.choice(chaingram)[0][0]
    i = 1
    sentenceList = getNewWord(chaingram, curWord, wordNum, i)


# print(chainGram(corpusTextPath))
makeRandomChain(chainGram(corpusTextPath), 10)
