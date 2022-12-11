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
myDay = 9
imReady = True and False #comment out False to submit
inputFile = "Day{:02d}-input.txt".format(myDay)
#inputFile = "Day{:02d}-test.txt".format(myDay)

def follow(oh,h,t):
    answer = t
    if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
        answer = oh
    return answer   

if __name__ == "__main__":
    print("Running {}, Day {} {} Part {}\n".format(scriptName,myDay,myYear,myPart))
    myAnswer = 0
    file1 = open(os.path.join(scriptdir, inputFile), 'r')
    Lines = file1.readlines()

    myList = [[0,0]]
    row = 0
    col = 0
    head = [0,0]
    tail = [0,0]
    for line in Lines:
        myData = line.strip()
        direction,count = myData.split(" ")
        for i in range(0,int(count)):
            oldHead = head.copy()
            if direction == "U":
                head[0] = head[0] + 1
            if direction == "D":
                head[0] = head[0] - 1
            if direction == "R":
                head[1] = head[1] + 1
            if direction == "L":
                head[1] = head[1] - 1
            tail = follow(oldHead,head,tail)
            myList.append(tail)
    print(myList)
    mySet = set(tuple(i) for i in myList)
    myAnswer = len(mySet)
    print("My answer = {}".format(myAnswer))

    if imReady:
        print("\nSubmitting {}, Day {} {} Part {}".format(scriptName,myDay,myYear,myPart))
        myResponse = submit(myAnswer, part=myPart, day=myDay, year=myYear)
        print("{}".format(myResponse))
    else:
        print("\n{} not submitted to AOC".format(scriptName))