# aoc_template.py

import os 
import sys
from aocd import submit 
scriptdir = os.path.dirname(os.path.abspath(__file__))
inputFile = "Day03-input.txt"

# Set to true when ready to submit the answer
myPart = "b" # "a" or "b"
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
    for i in range(0, len(Lines), 3):
        myData1 = Lines[i].strip()
        myData2 = Lines[i+1].strip()
        myData3 = Lines[i+2].strip()
        i += 2

        commonItems = ''.join(set(myData1).intersection(myData2).intersection(myData3))
        myAnswer += valueOfItem(commonItems)
        print("{} {}".format(commonItems, valueOfItem(commonItems)))

    print(myAnswer)

    if imReady:
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))