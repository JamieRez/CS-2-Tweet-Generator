"""Histogram Program."""
import re
import random
bookFilePath = "/Users/James/Downloads/bookOfText.txt"


def histogram(bookFile):
    """Generate an array of each word and its frequency from a textfile."""
    # open bookfile
    book = open(bookFile)
    # Which characters should be filtered out of of the words
    regex = re.compile('[,\.!?:/$()@]')
    # Filter out the read words, lowercase them, and put them into an array
    bookWords = regex.sub('', book.read().lower()).split()

    uniqueWords = []
    histogramList = []

    for word in bookWords:
        # Words with letters only
        if not word.isdigit() and word.isalpha():
            # New words get added to uniqueWords as well as the histogramList.
            if word not in uniqueWords:
                uniqueWords.append(word)
                histogramList.append([word, 1])
            # Non New words get updated in the histogram frequency
            else:
                histogramList[uniqueWords.index(word)][1] += 1

    return histogramList


def unique_words(histogram):
    """Return the amount of words that only show up once in the histogram."""
    uniqueWords = []
    for histogramWord in histogram:
        if histogramWord[1] == 1:
            uniqueWords.append(histogramWord)
    return(len(uniqueWords))


def frequency(word, histogram):
    """Return the amount of times a word shows up in the histogram."""
    for histogramWord in histogram:
        if histogramWord[0] == word:
            return histogramWord[1]


def histogramDict(bookFile):
    book = open(bookFile)
    # open bookfile
    book = open(bookFile)
    # Which characters should be filtered out of of the words
    regex = re.compile('[,\.!?:/$()@]')
    # Filter out the read words, lowercase them, and put them into an array
    bookWords = regex.sub('', book.read().lower()).split()

    uniqueWords = []
    dictogram = {}

    for word in bookWords:
        # Words with letters only
        if not word.isdigit() and word.isalpha():
            # New words get added to uniqueWords as well as the histogramList.
            if word not in uniqueWords:
                uniqueWords.append(word)
                dictogram[word] = 1
            # Non New words get updated in the histogram frequency
            else:
                dictogram[word] += 1

    return dictogram


def getRandomWord(bookFile):
    # open bookfile
    book = open(bookFile)
    # Which characters should be filtered out of of the words
    regex = re.compile('[,\.!?:/$()@]')
    # Filter out the read words, lowercase them, and put them into an array
    bookWords = regex.sub('', book.read().lower()).split()

    return bookWords[random.randint(0, len(bookWords))]


#print(histogram(bookFilePath))
#print(unique_words(histogram(bookFilePath)))
#print(frequency("cigar", histogram(bookFilePath)))
#print(histogramDict(bookFilePath))
print(getRandomWord(bookFilePath))
