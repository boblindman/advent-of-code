# aoc_template.py

import os 
import sys
from aocd import submit 
scriptdir = os.path.dirname(os.path.abspath(__file__))
inputFile = "Day03-input.txt"

# Set to true when ready to submit the answer
myPart = "a" # "a" or "b"
myYear = 2022
myDay = 0
imReady = False

if __name__ == "__main__":
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    for line in Lines:
        myData = line.strip()
        print("{}".format(myData))

    print(myAnswer)

    if imReady:
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))