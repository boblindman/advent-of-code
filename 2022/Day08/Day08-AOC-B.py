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
            treeHeight = forrest[row][col]
            viewDistanceLeft = 0 
            viewDistanceRight = 0 
            viewDistanceUp = 0 
            viewDistanceDown = 0 
            for row2 in range(row-1,-1,-1):
                #print("UP {}{} {} Main {}{} {}".format(row2,col,forrest[row2][col],row,col,forrest[row][col]))
                viewDistanceUp += 1
                if forrest[row2][col] >= treeHeight:
                    break

            for row2 in range(row+1,rowMax):
                viewDistanceDown += 1
                if forrest[row2][col] >= treeHeight:
                    break

            for col2 in range(col-1,-1,-1):
                viewDistanceLeft += 1
                if forrest[row][col2] >= treeHeight:
                    break

            for col2 in range(col+1,colMax):
                #print("Right {}{} {} Main {}{} {}".format(row,col2,forrest[row][col2],row,col,forrest[row][col]))
                viewDistanceRight += 1
                if forrest[row][col2] >= treeHeight:
                    break
            scenicScore = viewDistanceLeft * viewDistanceRight * viewDistanceUp * viewDistanceDown
            #print("Tree [{}][{}] = Scenic score: {}, Left: {}, Right: {}, Up: {}, Down:{}".format(row,col,scenicScore,viewDistanceLeft,viewDistanceRight,viewDistanceUp,viewDistanceDown))
            if scenicScore > myAnswer:
                myAnswer = scenicScore

    print("My answer = {}".format(myAnswer))

    if imReady:
        print("\nSubmitting {}, Day {} {} Part {}".format(scriptName,myDay,myYear,myPart))
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))
    else:
        print("\n{} not submitted to AOC".format(scriptName))