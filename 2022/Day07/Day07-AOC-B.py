# aoc_template.py

import os 
import sys
from aocd import submit 
scriptdir = os.path.dirname(os.path.abspath(__file__))
scriptName = os.path.basename(__file__)

# Set to true when ready to submit the answer
myPart = "a" # "a" or "b"
if scriptName[-5:-3] == "-B":
    myPart = "b"
myYear = 2022
myDay = 7
imReady = True and False #comment out False to submit
inputFile = "Day{:02d}-input.txt".format(myDay)

if __name__ == "__main__":
    print("Running {}, Day {} {} Part {}\n".format(scriptName,myDay,myYear,myPart))
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    for line in Lines:
        myData = line.strip()
        print("{}".format(myData))

    print("My answer = {}".format(myAnswer))

    if imReady:
        print("\nSubmitting {}, Day {} {} Part {}".format(scriptName,myDay,myYear,myPart))
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))
    else:
        print("\n{} not submitted to AOC".format(scriptName))