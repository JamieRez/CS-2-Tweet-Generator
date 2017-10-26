"""Program that shuffles a list of Strings."""
import sys
import random
currentInput = sys.argv


def rearrange(myList):
    """Print a shuffled version of a given list."""
    # Remove FileName from Argument List
    myList.pop(0)
    # Make a new list to contain our shuffled elements
    shuffledList = []
    # Use a while loop to loop through the amount of times as the original list length
    i = 0
    myListLength = len(myList)
    while i < myListLength:
        # Get a Random Index of the Original List
        randomListIndex = random.randint(0, len(myList) - 1)
        # Add that list index element to shuffledList
        shuffledList.append(myList[randomListIndex])
        # Remove that index element from original list
        del myList[randomListIndex]
        i += 1
    # Print a string with the list elements separated by a space
    print(" ".join(shuffledList))


rearrange(currentInput)
