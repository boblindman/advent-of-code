# aoc_template.py

import os 
import sys
from aocd import submit 
scriptdir = os.path.dirname(os.path.abspath(__file__))
inputFile = "Day03-input.txt"

# Set to true when ready to submit the answer
myPart = "a" # "a" or "b"
myYear = 2022
myDay = 3
imReady = False

def valueOfItem(item):
    value = 0
    if item.isupper():
        value = ord(item) - ord("A") + 27
    else:
        value = ord(item) - ord("a") + 1
    return value

if __name__ == "__main__":
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    for line in Lines:
        myData = line.strip()
        sack1 = myData[:len(myData)//2]
        sack2 = myData[len(myData)//2:]

        commonItems = ''.join(set(sack1).intersection(sack2))
        myAnswer += valueOfItem(commonItems)
        print("{} {} :: {} - {}".format(commonItems, valueOfItem(commonItems), sack1, sack2))

    print(myAnswer)

    if imReady:
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))