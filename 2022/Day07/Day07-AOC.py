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
#inputFile = "Day{:02d}-test.txt".format(myDay)

def upDir(theDir):
    # Find the last /
    lastSlash = theDir.rfind("/")
    return theDir[:lastSlash]

def downDir(theDir, path):
    return "{}/{}".format(theDir,path).replace("//","/")

def getDirs(myDir,myDict):
    myList = []
    for key in myDict:
        curDir = "{}/{}".format(myDir,key).replace("//","/")
        if myDict[key] == "dir":
            myList += [curDir]
        if type(myDict[key]) is dict:
            myList += getDirs(curDir,myDict[key])
    return myList

def getDirSize(myDir,myDict):
    mySizeDict = {}
    for key in myDict:
        if type(myDict[key]) is dict:
            curDir = "{}/{}".format(myDir,key).replace("//","/")
            mySizeDict.update(getDirSize(curDir,myDict[key]))
        else:
            value = 0
            if myDict[key].isnumeric():
                value = int(myDict[key])
            if myDir in mySizeDict:
                newValue = mySizeDict[myDir] + value
                mySizeDict.update({myDir : newValue})
            else:
                mySizeDict[myDir] = value
    return mySizeDict

def addSubdirectories(mySizeDict):
    for key in mySizeDict:
        for key2 in mySizeDict:
            if key != key2:
                if key2[:len(key)] == key:
                    mySizeDict[key] = mySizeDict[key] + mySizeDict[key2]
    return mySizeDict


filesInDir = {"/" : "dir"}
currentDir = "/"
if __name__ == "__main__":
    print("Running {}, Day {} {} Part {}\n".format(scriptName,myDay,myYear,myPart))
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()
    i = 0
    while i < len(Lines):
        myData = Lines[i].strip()
        print("{}".format(myData))
        if myData[0:4] == "$ cd":
            newDir = myData[5:]
            if newDir == "/":
                currentDir = "/"
            elif newDir == "..":
                currentDir = upDir(currentDir)
            else:
                 currentDir = downDir(currentDir,newDir)
            i += 1
        elif myData[0:4] == "$ ls":
            i += 1
            myData = Lines[i].strip()
            while myData[0] != "$":
                mySize,myFile = myData.split(" ")      
                if filesInDir[currentDir] == "dir":
                    filesInDir[currentDir] = {}                  
                filesInDir[currentDir][myFile] = mySize
                i += 1
                if i < len(Lines):
                    myData = Lines[i].strip()
                else:
                    break
        else:
            i += 1
        if currentDir not in filesInDir and len(currentDir) > 0:
            filesInDir[currentDir] = "dir"
    print(filesInDir)

    # Get the list of directories

    listOfDirs = getDirs("",filesInDir)
    print(listOfDirs)
    sizeOfDirs = getDirSize("",filesInDir)
    print(sizeOfDirs)
    totalSizeOfDirs = addSubdirectories(sizeOfDirs)
    print(totalSizeOfDirs)

    for key in totalSizeOfDirs:
        if totalSizeOfDirs[key] < 100000:
            myAnswer += totalSizeOfDirs[key]

    print("My answer = {}".format(myAnswer))

    if imReady:
        print("\nSubmitting {}, Day {} {} Part {}".format(scriptName,myDay,myYear,myPart))
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))
    else:
        print("\n{} not submitted to AOC".format(scriptName))