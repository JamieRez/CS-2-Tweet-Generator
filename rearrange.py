"""Program that shuffles a list of Strings."""
import sys
import random
currentInput = sys.argv


def rearrange(myList):
    """Print a shuffled version of a given list."""
    myList.pop(0)
    random.shuffle(myList)
    newStr = ""
    for word in myList:
        newStr += (word + " ")
    print(newStr)


rearrange(currentInput)
