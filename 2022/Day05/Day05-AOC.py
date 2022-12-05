# aoc_template.py

import os 
import sys
from aocd import submit 
scriptdir = os.path.dirname(os.path.abspath(__file__))
scriptName = os.path.basename(__file__)

# Set to true when ready to submit the answer
myPart = "a" # "a" or "b"
myYear = 2022
myDay = 5
imReady = True and False #comment out False to submit
inputFile = "Day{:02d}-input.txt".format(myDay)
#inputFile = "test-input.txt".format(myDay)

if __name__ == "__main__":
    print("Running {}, Day {} {} Part {}\n".format(scriptName,myDay,myYear,myPart))
    myAnswer = ""

    # Grab the stacks from the original file
    stack = []
    lastDataLine = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    for line in Lines:
        lastDataLine += 1
        myData = line
        print(len(myData.strip()))
        if len(myData.strip())<1:
            break
        for i in range(1,len(myData)):
            if not ((i-1) % 4):
                stackNumber = int(((i-1)/4))
                if len(stack)<stackNumber+1:
                        stack.append([])
                if myData[i].isalpha():
                    stack[stackNumber].append(myData[i])
    print("{} , {}".format(stack,lastDataLine))

    # Run through the moves
    lineCount = 0
    for line in Lines:
        lineCount += 1
        if lineCount > lastDataLine:
            myData = line.strip()

            text1,numCratesText,text2,fromStackText,text3,toStackText = myData.split(" ")
            numCrates = int(numCratesText)
            fromStack = int(fromStackText) - 1
            toStack = int(toStackText) - 1
            #print(myData)
            print("MOVE {} FROM {} TO {}".format(numCrates,fromStack,toStack))
            for i in range(0,numCrates):
                if len(stack[fromStack]) > 0:
                    crate = stack[fromStack].pop(0)
                    stack[toStack].insert(0, crate)
            print("{}".format(stack))

    # Get the first/top entry from each stack
    for i in range(0,len(stack)):
        myAnswer += "{}".format(stack[i][0])

    print("My answer = {}".format(myAnswer))

    if imReady:
        print("\nSubmitting {}, Day {} {} Part {}".format(scriptName,myDay,myYear,myPart))
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))
    else:
        print("\n{} not submitted to AOC".format(scriptName))