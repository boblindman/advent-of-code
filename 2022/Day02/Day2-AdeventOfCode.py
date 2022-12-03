import os.path
scriptdir = os.path.dirname(os.path.abspath(__file__))

# Grab the input file
inputFile = "Day2-AdventOfCode-Input.txt"
win = 6
draw = 3
lose = 0

rock = 1
paper = 2
scissors = 3

hand = {
  "A": rock,
  "B": paper,
  "C": scissors,
  "X": rock,
  "Y": paper,
  "Z": scissors
}

handType = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "rock",
  "Y": "paper",
  "Z": "scissors",
  6 : "win",
  3 : "draw",
  0 : "lose"
}

# Using readlines()
file1 = open(os.path.join(scriptdir, inputFile), 'r')
Lines = file1.readlines()

totalPoints = 0
for line in Lines:
    pointsForThisRound = 0;
    elfsHand,myHand = line.upper().strip().split(" ") 
    #print("{} {}, {} {}".format(elfsHand,hand[elfsHand],myHand,hand[myHand]))
    if handType[elfsHand] == "rock":
            if handType[myHand] == "rock":
                    pointsForThisRound = draw
            elif handType[myHand] == "paper":
                    pointsForThisRound = win
            elif handType[myHand] == "scissors":
                    pointsForThisRound = lose
    elif handType[elfsHand] == "paper":
            if handType[myHand] == "rock":
                    pointsForThisRound = lose
            elif handType[myHand] == "paper":
                    pointsForThisRound = draw
            elif handType[myHand] == "scissors":
                    pointsForThisRound = win
    elif handType[elfsHand] == "scissors":
            if handType[myHand] == "rock":
                    pointsForThisRound = win
            elif handType[myHand] == "paper":
                    pointsForThisRound = lose
            elif handType[myHand] == "scissors":
                    pointsForThisRound = draw

    print("Elf: {}, Me:{}, Status:{}, Points{}".format(handType[elfsHand],handType[myHand],handType[pointsForThisRound],pointsForThisRound))
    totalPoints += hand[myHand] + pointsForThisRound

print("Total point = {}".format(totalPoints))    
