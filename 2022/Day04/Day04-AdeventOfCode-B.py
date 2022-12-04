# aoc_template.py

import os 
import sys
from aocd import submit 
scriptdir = os.path.dirname(os.path.abspath(__file__))
inputFile = "Day04-input.txt"

# Set to true when ready to submit the answer
myPart = "b" # "a" or "b"
myYear = 2022
myDay = 4
imReady = 1<2

def fullyInRange(range1,range2):
    range1End = range1.start
    if len(range1) > 1:
        range1End = range1[-1]
    range1InRange2 = range1.start in range2 and range1End in range2
    print("{} {} {}".format(range1,range1.start,range1End))
    range2End = range2.start
    if len(range2) > 1:
        range2End = range2[-1]
    range2InRange1 = range2.start in range1 and range2End in range1
    print("{} {} {} {}".format(range2,range2.start,range2End, range2End in range1))
    return range1InRange2 or range2InRange1

def partialOverlap(range1,range2):
    myOverlap = set(range1).intersection(range2)
    #print("{}".format(myOverlap))
    return len(myOverlap) 

if __name__ == "__main__":
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    for line in Lines:
        myData = line.strip()
        elf1,elf2 = myData.split(",")
        elf1RangeStart,elf1RangeEnd = (elf1.split("-"))
        elf2RangeStart,elf2RangeEnd = (elf2.split("-"))
        elf1Range = range(int(elf1RangeStart),int(elf1RangeEnd)+1)
        elf2Range = range(int(elf2RangeStart),int(elf2RangeEnd)+1)
        if partialOverlap(elf1Range,elf2Range):
            myAnswer+= 1
        print("{}:{}  {}".format(elf1Range,elf2Range,myAnswer))

    print(myAnswer)

    if imReady:
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))