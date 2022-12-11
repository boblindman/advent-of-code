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
myDay = 8
imReady = True and False #comment out False to submit
inputFile = "Day{:02d}-input.txt".format(myDay)
#inputFile = "Day{:02d}-test.txt".format(myDay)

if __name__ == "__main__":
    print("Running {}, Day {} {} Part {}\n".format(scriptName,myDay,myYear,myPart))
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    forrest = []
    for line in Lines:
        myData = line.strip()
        forrest.append(list(myData))
        print("{}".format(myData))
    print(forrest)

    rowMax = len(forrest[0])
    colMax = len(forrest)
    for row in range(0,rowMax):
        for col in range(0,colMax):
            #print("{} {} = {}".format(row,col,forrest[row][col]))
            isVisibe = False
            visible = False
            treeHeight = forrest[row][col]
            if row < 1 or row == rowMax-1 or col < 1 or col == colMax-1:
                visible = True
            isVisibe = isVisibe or visible
            visible = True
            for row2 in range(0,row):
                if forrest[row2][col] >= treeHeight:
                    visible = False
            isVisibe = isVisibe or visible
            visible = True
            for row2 in range(row+1,rowMax):
                if forrest[row2][col] >= treeHeight:
                    visible = False
            isVisibe = isVisibe or visible
            visible = True
            for col2 in range(0,col):
                if forrest[row][col2] >= treeHeight:
                    visible = False
            isVisibe = isVisibe or visible
            visible = True
            for col2 in range(col+1,colMax):
                if forrest[row][col2] >= treeHeight:
                    visible = False
            isVisibe = isVisibe or visible
            if isVisibe:
                myAnswer += 1
        

    print("My answer = {}".format(myAnswer))

    if imReady:
        print("\nSubmitting {}, Day {} {} Part {}".format(scriptName,myDay,myYear,myPart))
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))
    else:
        print("\n{} not submitted to AOC".format(scriptName))