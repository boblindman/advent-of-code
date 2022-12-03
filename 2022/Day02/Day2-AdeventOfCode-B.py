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
  "X": lose,
  "Y": draw,
  "Z": win
}

handType = {
  "A": "rock",
  "B": "paper",
  "C": "scissors",
  "X": "lose",
  "Y": "draw",
  "Z": "win"
}

# Using readlines()
file1 = open(inputFile, 'r')
Lines = file1.readlines()

totalPoints = 0
for line in Lines:
    pointsForThisRound = 0;
    elfsHand,myHand = line.upper().strip().split(" ") 
    #print("{} {}, {} {}".format(elfsHand,hand[elfsHand],myHand,hand[myHand]))
    if handType[elfsHand] == "rock":
            if handType[myHand] == "lose":
                    pointsForThisRound = lose + scissors
            elif handType[myHand] == "draw":
                    pointsForThisRound = draw + rock
            elif handType[myHand] == "win":
                    pointsForThisRound = win + paper
    elif handType[elfsHand] == "paper":
            if handType[myHand] == "lose":
                    pointsForThisRound = lose + rock
            elif handType[myHand] == "draw":
                    pointsForThisRound = draw + paper
            elif handType[myHand] == "win":
                    pointsForThisRound = win + scissors
    elif handType[elfsHand] == "scissors":
            if handType[myHand] == "lose":
                    pointsForThisRound = lose + paper
            elif handType[myHand] == "draw":
                    pointsForThisRound = draw + scissors
            elif handType[myHand] == "win":
                    pointsForThisRound = win + rock

    print("Elf: {}, Me:{}, Points: {}".format(handType[elfsHand],handType[myHand],pointsForThisRound))
    totalPoints += pointsForThisRound

print("Total point = {}".format(totalPoints))    
